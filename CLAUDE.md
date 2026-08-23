# CLAUDE.md

Working contract for AI assistance in `Productside-Github4PMs`. Constitutional rules in [CONSTITUTION.md](CONSTITUTION.md) override anything here.

## What this project is

Production project for the September 2, 2026 Productside webinar "Beyond the Backlog: Five GitHub Plays for Product Teams," plus the durable teaching material that outlives it. See [README.md](README.md) for the plays, the decisions already made, and what is still open.

## Who the audience is

Two audiences, and they need different registers:

**The webinar audience** — Product Managers and product leaders at other companies. No git experience. No coding. Many have watched engineers use GitHub and concluded it is not for them. They are tired of losing decisions, rebuilding context, and re-explaining their product to an AI tool every morning. Write for someone competent and busy who has never typed `git commit` and does not intend to start.

**Internal readers** — Dean, Kenny, and Productside marketing, reading the run-of-show and working notes. Direct, specific, no throat-clearing.

## Vocabulary: the one rule that trips everyone

Productside is a **services firm, not a software company**. Describing published materials as "code" or "software" invites counterparties to treat Productside as a software vendor, which attaches software warranty terms to a training agreement.

**The nuance specific to this project:** this webinar teaches GitHub. Words like *repo*, *issue*, *pull request*, *commit*, and *branch* are the subject matter and must be used plainly — that is the teaching. The rule bites on how we describe **Productside's own published materials**: those are digital takeaways and examples that demonstrate Productside's teaching and advisory services. Never "our software," "our app," "our codebase."

Never add a roadmap item, feature promise, or capability claim to public-facing copy that would read as a commitment to build or maintain software.

## Writing principles

- **Plain English over jargon.** If a sentence needs a git glossary to parse, rewrite it.
- **Concrete over abstract.** "The commit history on those two files IS your strategy timeline" beats "version control provides an audit trail."
- **Name the fear, concede it, then show the guardrail.** Dean's own rhetorical shape, and the best one in the source material: *"The obvious concern is: could we accidentally expose something sensitive? Yes, if we were sloppy. Which is why we are not being sloppy."* Reuse this structure, don't just quote it.
- **"In plain English" as a recurring beat.** Dean uses it in his internal training document. It gives the show a rhythm the audience starts to anticipate.
- **Every concept carries its own limit and its own adoption test.** Each play in the run-of-show ends with an `Adoption and limits` block: *use this when*, *skip it when*, *what it does not do*. A limitation admitted next to the thing it limits reads as expertise; the same limitation batched into a disclaimer at the end reads as covering yourself. Keep this pattern when adding any new material.
- **Honest about limits.** GitHub's real caveats make the pitch more credible, not less. The repo-access gate on commenting is a genuine hole in the community story — address it, never oversell past it.
- **Professional and practical, never hype-y.** House tone across all Productside material.
- **No em dashes in marketing copy** unless Dean's own source copy uses them.

## Voice sources, ranked

1. **Dean's own writing** — `docs/Productside on GitHub.internal training.docx`, digested in `research/findings/productside-copy-gems.md`. Directly reusable. Includes two long lists of ready-made benefit one-liners; pull from that bank rather than inventing equivalents.
2. **The abstract and registration copy** already written for this webinar. The voice is set. Match it.
3. **Anne Thomas's practitioner talk** — real, demonstrable, honest about caveats.
4. Everything else in `research/` is raw material, not voice.

## The escalation ladder

The live build climbs three rungs, and content written for this project should know which rung it belongs to:

1. **Browser only** — github.com, clicking. The safety floor. Every failure recovery drops back to it.
2. **Claude Desktop** — reads and writes files in Kenny's local folder. No git, no auth, nothing to break.
3. **Claude Code** — clones, commits, pushes, branches, opens the pull request.

Kenny never types a git command at any rung; he says sentences. The only command line in the show is Dean's three-minute origin story. Full detail in `docs/run-of-show.md`.

## Structure conventions

- Lowercase-hyphen filenames in `docs/` (`run-of-show.md`). Source `.docx` files keep their original names.
- Research is read-only history. Do not rewrite `research/findings/*` to reflect new decisions — record decisions in `README.md` instead, and note where a finding is now superseded.
- Dates absolute, never relative. "September 2, 2026," not "next month."

## When adding new content

Check `research/findings/README.md` first — it maps every gem to its play and flags what is already covered. Most "new" content is already sitting in there under a different name.

## What not to do

- **Do not teach git mechanics.** Branching, merging, and rebasing are what every other "GitHub for PMs" video does, and the research pile documents that trap in detail. The audience needs GitHub as durable memory, not a command-line tutorial.
  - **One deliberate exception:** Dean's three-minute origin story at 0:04 of the live show — git as version control, then gitflow-style conventions layered on top, then GitHub adding the coordination layer that doesn't care whether the files are source code. That is history in service of the thesis, delivered by Dean, with nobody repeating after him. It is not a tutorial and it does not license adding more command-line content anywhere else.
- **Do not copy from the two restricted third-party sources.** The Aakash Gupta / Shubham Saboo piece is paywalled, and `pm-github-starter-kit` states it must not be redistributed. Mine for ideas; build Productside's own equivalents from scratch.
- **Do not commit client names, learner names, or anything from a real engagement.** See CONSTITUTION.md.
- **Do not write copy that promises software.** See the vocabulary rule above.
- **Do not resolve Dean's open threads by assumption.** `research/findings/README.md` carries nine of them and README.md records which are now closed. If something is still open, ask.
- **Do not use the old title.**

## Repo anatomy

Three layers, per Productside's pattern:

- **Context** — `README.md` — what this project is and why it exists
- **Contract** — this file — how AI works here
- **Constitution** — `CONSTITUTION.md` — non-negotiable rules that override everything

See `productside-launchkit: docs/01-foundations/01-04-repo-anatomy.md`.
