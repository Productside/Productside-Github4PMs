# Productside-Github4PMs

Working project for the Productside webinar **"Beyond the Backlog"** — Tuesday, September 2, 2026, 1PM ET / 10AM PT.

**Status: private.** Nothing here is published. See [CONSTITUTION.md](CONSTITUTION.md) before that changes.

## What this project is

A live, hands-on webinar in which Dean Peters and Kenny Kranseler build a GitHub setup from scratch, on screen, in the wild. No slides about GitHub. No net. Attendees can follow along in their own browser and leave with a working repo instead of notes about one.

The session tells one continuous collaboration story, answering one question: *Does your product team have a place where its thinking can compound?*

| Section | What happens |
|---|---|
| **Collaboration Pains** | Name the five dysfunctions everyone shares |
| **Collaborative Journey** | The five-step learning path: Share, Collaborate, Experiment, Review, Reuse |
| **Collaborative Sharing** | Give AI and the team the same context; clone a shared library and run a skill |
| **Collaborative Improvements** | Branch safely; give SME feedback to the AI and watch it improve the work |
| **Collaborative Commits** | Commit with reasoning, test the change, push a PR |
| **Collaborative Reuse** | Review, merge, turn practices into versioned assets |
| **Collaborative Governance** | Legal, automation, and the "What Change Looks Like" recap |

Eight numbered workflows (WF1-WF8) are distributed across these sections. The deck is 34 slides. Full prompt text in [`docs/live-demo-prompts.md`](docs/live-demo-prompts.md).

Beyond September 2, this material is intended for reuse in Productside classes, workshops, and advisory engagements.

## What lives here

```
docs/
  slides/                Expanded teaching pages for each section of the deck
    01_collaboration-pains.md      The three dysfunctions and five collaborative pains
    02_collaborative-journey.md    The five-step learning path and WF1
    03_collaborative-sharing.md    Clone, AI context, run a skill — WF2-WF4
    04_collaborative-improvements.md  Branch safely, SME feedback — WF5
    05_collaborative-commits.md    Commit with reasoning, push a PR — WF6-WF7
    06_collaborative-reuse.md      Review, merge, team reuse — WF8
    07_collaborative-governance.md Legal, automation, honest limits
    08_what-change-looks-like.md   The KEEP/ADD/RESULT frame and closing
    run.md                         Navigation hub for all eight pages
  polls.md               The two audience polls — SOURCE OF TRUTH for question and option text
  field-guide.md         Git & GitHub for Product Managers — durable reference companion
  appendix.md            Deeper reference: vocabulary, diagrams, adoption limits, governance
  diagrams.md            All diagrams in runbook reading order — SOURCE OF TRUTH
  diagrams/              The same diagrams, one file each, plus INDEX.md (generated)
scripts/
  split-diagrams.py      Regenerates docs/diagrams/ from docs/diagrams.md
CLAUDE.md                How AI assistance works in this project
CONSTITUTION.md          Non-negotiable rules that override everything else
```

## Key decisions

- **Title:** "Beyond the Backlog."
- **Format:** live and hands-on, not slides. Mistakes stay in.
- **Two presenters:** Dean narrates; Kenny builds at the keyboard, hits snags, and gets unstuck on camera.
- **Two repos, two jobs.** Kenny's domain-research repo is private. The Productside market intelligence repo is public and Kenny collaborates on it.
- **Cross-platform by design.** Kenny is on Windows, Dean is on a Mac. Narrated, not hidden.
- **Tool handoff:** Claude Desktop reads and writes the local folder; Claude Code does the git. Kenny never types a git command.
- **The "Collaborative ___" arc is one continuous story**, not a series of demos. Each section is the next thing that happens to Kenny. Eight workflows (WF1-WF8) across seven sections.
- **34-slide deck.** Final.

## Start here

[`docs/slides/run.md`](docs/slides/run.md) — navigation hub for the eight teaching pages. [`docs/field-guide.md`](docs/field-guide.md) — the durable reference companion.

## Provenance and reuse

All material in this project is original to Productside. Two research sources consulted during development carry redistribution restrictions (Aakash Gupta / Shubham Saboo piece, and `pm-github-starter-kit`); neither is included here, and derivative copying from them is not permitted.

---

© 280 Group LLC dba Productside.
