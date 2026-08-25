# Productside-Github4PMs

Working project for the Productside webinar **"Beyond the Backlog: How GitHub Compounds Your Product Team's Thinking"** — Wednesday, September 2, 2026, 1PM ET / 10AM PT.

**Status: private.** Nothing here is published. See [CONSTITUTION.md](CONSTITUTION.md) before that changes.

## What this project is

A live, hands-on webinar in which Dean Peters and Kenny Kranseler build a GitHub setup from scratch, on screen, in the wild. No slides about GitHub. No net. Attendees can follow along in their own browser and leave with a working repo instead of notes about one.

The session is organized around seven capabilities that answer one question: *Does your product team have a place where its thinking can compound?*

| Capability | The promise |
|---|---|
| **Share** | A complete product workspace where research, strategy, decisions, and evidence live together |
| **Collaborate** | Work together without trampling each other: discussions for questions, issues for commitments |
| **Review** | Make changes reviewable before they become truth |
| **Trace** | See what changed, who changed it, and why |
| **Experiment** | Explore alternatives without breaking what works |
| **Augment** | Give AI the same persistent context as the team |
| **Reuse** | Turn practices into reusable assets another PM or team can adopt and improve |

Beyond September 2, this material is intended for reuse in Productside classes, workshops, and advisory engagements.

## What lives here

```
docs/
  run-of-show.md         The live-build script: timings, who does what, failure recovery
  polls.md               The two audience polls — SOURCE OF TRUTH for question and option text
  seed-questions.md      Seven Q&A seeds for Kenny to ask if the room is quiet
  slide-plan.md          Deck spec, built on the canonical Productside webinar template
  kenny-prep.md          Kenny's 10-day track: what he sets up, what he rehearses, by when
  mi-repo-publication.md Audit + checklist for making the market intelligence Project public
  diagrams.md            All 29 diagrams in runbook reading order — SOURCE OF TRUTH
  diagrams/              The same diagrams, one file each, plus INDEX.md (generated)
  slides/
    00_the-problem.md .. 10_the-honest-part.md   Branded play pages for the teaching middle
    run.md             Teleprompter page linking all 11 play pages sequentially
    assets/            Exported diagram PNGs (mermaid + Figma) — not tracked by git
    *.pptx             The deck — not tracked by git
  *.docx                 Dean's source documents (abstract template, internal training proposal)
scripts/
  split-diagrams.py      Regenerates docs/diagrams/ from docs/diagrams.md
research/
  findings/              Digested, cross-referenced source material — START HERE
  web-searches/          8 AI-generated research docs (Claude, GPT, Gemini, Google)
  youtube-transcripts/   4 transcripts; the Anne Thomas talk is the strongest single source
HANDOFF.md               Current state, critical path to Sept 2, deck spec, publication plan
CLAUDE.md                How AI assistance works in this project
CONSTITUTION.md          Non-negotiable rules that override everything else
```

`research/findings/README.md` is the index between the raw sources and the outline. Read it before touching the content.

## Decisions already made

- **Title is final:** "Beyond the Backlog." The subtitle "How GitHub Compounds Your Product Team's Thinking" is a placeholder; Dean decides. The old title ("Five GitHub Plays for Product Teams") and the original title ("How to Set Up a GitHub for Your Product Team") both appear in older research notes; ignore them.
- **Format is live and hands-on**, not slides. Mistakes stay in.
- **Kenny is a co-presenter at the keyboard**, not just a moderator — he builds, hits the snags, and gets unstuck on camera. Dean narrates and rescues. The abstract document's "Moderator" field understates this.
- **One webinar, not two.** The Five Plays session and the draft in `productside-launchkit` are the same September 2 event. The Constitution play absorbs the launchkit's category-trap, licensing, and secrets material.
- **The internal Lunch & Learn is a separate build** — different audience (Productside staff), different stakes. Shared source material, distinct outline.
- **Session length is written for 60 minutes**, with 45-minute cut marks in the run-of-show. Confirm the actual slot with marketing.
- **Two repos, two jobs.** Kenny's domain-research repo is **private and stays private** — the session never violates its own "start private" rule. The Productside market intelligence repo is public, and Kenny is a collaborator on it.
- **Kenny clones the market intelligence repo once**, in Play 3, and works from it standalone. A pull request needs a branch and a branch needs a clone, so the clone happens early and openly.
- **Kenny is on Windows, Dean is on a Mac.** Narrated, not hidden — it's what a real team looks like, and it kills the "I'd need my engineers' setup" objection.
- **Tool handoff:** Claude Desktop reads and writes the local folder; Claude Code does the git. Kenny never types a git command.
- **Dean opens with a three-minute git origin story** on his own terminal — history, not a tutorial.
- **The seven capabilities are one continuous story**, not seven demos: the team needs a shared workspace, they need to collaborate and review, trace decisions, experiment safely, let AI work from the same context, and turn what works into reusable assets.

## Start here

[`HANDOFF.md`](HANDOFF.md) — current state, the dated critical path to September 2, the deck spec, and the plan for publishing this Project afterward.

## Next ten days

Kenny is the student and the audience's proxy. His prep track is in [`docs/kenny-prep.md`](docs/kenny-prep.md) — two joint dry runs (Wed Aug 26, Fri Aug 28), a tech check Sep 1, and a deliberately empty weekend buffer.

- **The contribution piece is a new framework skill** — McKinsey Growth Pyramid or BCG growth-share matrix, neither of which exists in the library. Leaning Growth Pyramid because Kenny has presented on it and can speak to it fluently if the demo stalls. Must be prefabbed and green against the validator before Aug 27.

## Still open

- The takeaway artifact: is there a template repo attendees clone afterward, or is the on-screen build the whole deliverable?
- Marketing copy is unwritten — LinkedIn Live, four social posts, four emails, and the YouTube description are all still `[insert copy here]` in the abstract document.
- The Copilot standardization rule appears in Dean's internal training document but not in the launchkit's `CONSTITUTION.md`. Reconcile, or use it in the webinar only.
- `productside-launchkit` 02-09's "Training Deliverables → No" row reads stricter than the actual rule and invites a wrong reading. Consider rewording to "materials whose rights are not solely Productside's." 

## Provenance and reuse

Two research sources carry redistribution restrictions and must not be copied into anything published. See the top of `research/findings/third-party-gems.md` before reusing any template or wording from third-party material.

---

© 280 Group LLC dba Productside.
