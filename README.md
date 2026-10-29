# Copilot in Practice

Half-day workshop materials for getting real work done with Microsoft Copilot in Outlook, Word, Excel, Edge and Chat. Built for the Curtin Executive Education team, written for non-technical users, and published openly so other teams can reuse the structure.

**Live site:** https://michael-borck.github.io/copilot-in-practice/

## The course

Five short blocks. Two teaching, two hands-on, one commit at the end.

| Block | Time | Question | What happens |
|---|---|---|---|
| Open | 9:00 | What can it see? | The gap between Chat and Outlook, the one idea, a context pre-flight |
| Judge | 9:15 | Where does it help and fail? | Opportunity, risk, a sycophancy demo, the rules on what may go in |
| See | 10:00 | How do I carry context? | App, licence and tenant; the carry pattern; Edge; five prompt habits |
| Build | 11:00 | Can I use it on real work? | Brief to proposal outline, red-team critique, budget table |
| Yours | 11:45 | Will it work every week? | Map a workflow, build a reusable prompt, name the checkpoints |

Morning tea 10:30. Close 12:30.

## The one idea

You are the orchestrator. The prompts use RTCF: role, task, context, format, with four upgrades for when the output misses. Copilot keeps Curtin's data inside the tenant, but it does not pass work between Outlook, Word, Excel and Chat for you. Copilot in Outlook sees the open email. Copilot Chat in the browser does not, unless you paste or upload. So the skill is to get context in front of the right Copilot, carry the output to the next step yourself, and check it before it leaves the building.

## Layout

```
site/                Companion site pages (Markdown, rendered with pandoc)
deck/                deck.html (with speaker notes), deck.css, deck.js
handouts/            Print handout for the checklist PDF
assets/              Site stylesheet, favicon, fonts, QR code
build/               build.py and pandoc templates
docs/                Generated site, served by GitHub Pages. Do not edit; rebuild.
materials/           Prompt library, context and settings guide, take-home checklist
survey/              Pre-session survey
source-documents/    Sanitised samples (committed) and originals (local only)
```

## Build

Needs `pandoc`, `weasyprint`, and Python with `playwright` and Google Chrome.

```sh
python3 build/build.py            # site, deck, checklist PDF, slides PDF
python3 build/build.py --no-pdf   # quick rebuild of pages and deck
```

The build publishes a copy of the deck with all speaker notes removed. The repository is public, so `deck/deck.html` is readable on GitHub, but the site copy is the clean one.

Preview locally with `python3 -m http.server -d docs`.

## Presenting

Open `deck/deck.html` from the repo, not the site. It has the speaker notes.

Keys: arrows, Space or a clicker to advance; `1` to `5` to jump to a session; `N` for the presenter window (allow pop-ups); `M` to show notes on the main screen; `T` to start the exercise timer; `R` to reset it; `B` to blank the screen; `F` for full screen.

The deck relies on `../assets/fonts` and `../assets/qr.svg`, so present from the repo or the built `docs/deck/`, not from a lone file.

## Editing

- **Site:** edit `site/*.md`, then rebuild. Pandoc fenced divs (`.cards`, `.card`, `.note`) and the `.flow` HTML block give the layout.
- **Deck:** edit `deck/deck.html`. Each slide is a `<section>` with `data-ch` (session 0 to 4). Speaker notes go in `<aside class="notes">`. Use `data-s="1"` for progressive reveals and `data-min` for the exercise timer.
- **Checklist PDF:** edit `handouts/checklist.html`.
- **Styles:** `assets/site.css` for the site, `deck/deck.css` for the slides.

## Sanitised source documents

The exercises use two briefs derived from real Curtin work: a professional development proposal and an international tender response. Client names, staff names, partner organisations, day rates, margins and contract totals are removed. The originals are kept outside version control. See `source-documents/README.md`.

## Licence

Content (c) Michael Borck. Code MIT. Fonts (Domine, Funnel Sans, Nanum Gothic Coding) are under the SIL Open Font License.
