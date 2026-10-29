#!/usr/bin/env python3
"""Build the companion site into docs/ (published by GitHub Pages).

    python3 build/build.py            # everything (needs weasyprint and playwright)
    python3 build/build.py --no-pdf   # site and deck only (fast)

Sources:

    site/*.md            -> docs/*.html        (pandoc + build/templates/site.html)
    deck/                -> docs/deck/         (speaker notes and private slides removed)
    source-documents/samples/* -> docs/downloads/
    handouts/checklist.html -> docs/downloads/checklist.pdf   (weasyprint)
    docs/deck/index.html -> docs/downloads/slides.pdf         (playwright + Chrome)
"""
import pathlib
import re
import shutil
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
DL = DOCS / "downloads"
PDF = "--no-pdf" not in sys.argv


def run(*cmd, **kw):
    print("  $", " ".join(str(c) for c in cmd))
    subprocess.run([str(c) for c in cmd], check=True, **kw)


def public_deck(html: str) -> str:
    """Strip speaker notes and instructor-only slides (data-private) from the deck."""
    html = re.sub(r"\s*<aside class=\"notes\">.*?</aside>", "", html, flags=re.S)
    html = re.sub(r"\s*<!--[^>]*?instructor only[^>]*?-->", "", html)
    html = re.sub(r"\s*<section[^>]*data-private=\"true\"[^>]*>.*?</section>", "", html, flags=re.S)
    return html


def main():
    print("clean docs/")
    if DOCS.exists():
        shutil.rmtree(DOCS)
    DOCS.mkdir(parents=True)
    DL.mkdir()
    (DOCS / ".nojekyll").touch()

    print("assets")
    for f in (ROOT / "assets").rglob("*"):
        if f.is_file() and not f.name.startswith("._"):
            dest = DOCS / "assets" / f.relative_to(ROOT / "assets")
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(f, dest)

    shutil.copy2(ROOT / "build/templates/404.html", DOCS / "404.html")

    print("site pages")
    for md in sorted(m for m in (ROOT / "site").glob("*.md") if not m.name.startswith("._")):
        run("pandoc", md, "-f", "markdown", "-t", "html5",
            "--template", ROOT / "build/templates/site.html",
            "-o", DOCS / (md.stem + ".html"))

    print("deck (public copy)")
    (DOCS / "deck").mkdir()
    src = (ROOT / "deck/deck.html").read_text()
    pub = public_deck(src)
    (DOCS / "deck/index.html").write_text(pub)
    for f in ("deck.css", "deck.js"):
        shutil.copy2(ROOT / "deck" / f, DOCS / "deck" / f)
    n_all = src.count('<section class="slide')
    n_pub = pub.count('<section class="slide')
    print(f"  {n_all} slides in source, {n_pub} public; notes removed")

    print("downloads")
    for f in (ROOT / "source-documents/samples").iterdir():
        if f.suffix in (".docx", ".md") and not f.name.startswith("._"):
            shutil.copy2(f, DL / f.name)

    if not PDF:
        print("done (no PDFs)")
        return

    print("handouts (pdf)")
    run("weasyprint", "-q", ROOT / "handouts/checklist.html", DL / "checklist.pdf")

    print("slides (pdf)")
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch(channel="chrome")
        pg = b.new_page(viewport={"width": 1280, "height": 720})
        pg.goto((DOCS / "deck/index.html").as_uri() + "?print")
        pg.wait_for_load_state("networkidle")
        pg.evaluate("document.fonts.ready")
        pg.pdf(path=str(DL / "slides.pdf"), width="1280px", height="720px", print_background=True)
        b.close()
    print("done")


if __name__ == "__main__":
    main()
