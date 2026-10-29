# Source documents

Two folders, on purpose.

## `private/`

The original client and tender documents, exactly as supplied. Client names, staff names, day rates, margins and contract totals are all still in them.

**This folder is gitignored.** The files live on this machine but never enter the repository or its history.

Why: a GitHub repo, even a private one, is still a copy on someone else's infrastructure, with access managed per account and a history that is hard to erase. The documents contain commercially sensitive material and terms that may be confidential to the client or the tender. The team's view that sanitising was unnecessary was about the room, where everyone is already across the work. Putting the originals in a repo is a different act with a different audience and a longer tail.

If there is a genuine reason to keep the originals under version control later, use a separate store with encryption (for example git-crypt) and check with Curtin records or legal first. Do not simply commit them here.

## `samples/`

Sanitised briefs derived from the originals. These are what the exercises use and what is committed.

Removed: client identity, staff names, partner organisations, day rates, margins, totals and anything covered by a confidentiality clause. Kept: the structure, the outcomes, the evaluation criteria and the kind of judgement the work demands.

Both a Markdown source and a Word version sit here. Participants drop the Word version into Copilot during Session 3.

## Adding a document

1. Put the original in `private/`.
2. Make a sanitised copy in `samples/`.
3. Check it for names, rates, totals and client-identifying detail before you commit.
4. Commit only the sample.
