# Research Findings — Index

Digested from `research/web-searches/` (8 docs), `research/youtube-transcripts/`
(4 transcripts), and Dean's `productside-launchkit` repo (a working example, not
research). This is the "dip into" layer between raw source material and the
outline — read this before Phase 1, and come back to the detail files when a
module needs a specific quote, stat, or demo idea.

## Read this first: the format changed (2026-08-06)

**This webinar is now live and hands-on, not slides and talking points.** Kenny
Kranseler proposed running it as a live session where the GitHub setup happens on
screen, and Dean agreed. Two people on camera, building a real repo in the wild,
with the audience following along in their own. Mistakes stay in.

That reprioritizes everything in these files. Material that reads as
*demonstrable* now beats material that reads as *explainable*:

- **Anne Thomas's talk** (`youtube-transcript-gems.md`) jumps from "useful
  practitioner source" to near-ready demo script: issue templates, labels, emoji
  voting, a Zapier intake form, an org-level roadmap board, all walked through
  live by someone who ran it for real.
- **The PM Artifact Workflow** (`third-party-gems.md`) maps every git step to the
  plain-English sentence you type at an AI agent. That is the on-screen script
  for the whole "no git syntax required" promise.
- **The Content Guard** (`launchkit-gems.md`) is real running automation Dean
  owns. A live commit that gets *blocked* on screen is the most convincing
  possible governance demo, and it costs about fifteen seconds.
- **Diagrams, tables, and pull-quotes** drop in value. They were slide fuel, and
  there are fewer slides now.

Two constraints the outline has to respect: five plays demonstrated live will not
fit 45 to 60 minutes, and the registration copy now promises attendees can follow
along, so segments must be slow enough to be followable rather than just
watchable. Full detail and the two candidate pacing models are in the project
brief at `claude/webinar-instructions.md`.

Detail files:

- [`web-search-gems.md`](web-search-gems.md) — the eight AI-generated research docs
  (Claude, Gemini, GPT, Google), organized by the five confirmed plays.
- [`youtube-transcript-gems.md`](youtube-transcript-gems.md) — the four video
  transcripts. One (Anne Thomas's conference talk) is a real practitioner case
  study and is the strongest single source in the whole pile. The other three are
  generic Git/GitHub tutorials that happen to be tagged for PMs.
- [`launchkit-gems.md`](launchkit-gems.md) — from `~/Code/Productside/productside-launchkit`,
  Productside's own internal GitHub governance manual. Different kind of source:
  not research, a real system Dean already built and runs. Contains a working
  Content Guard (the actual answer to "no customer names as a check-in check"),
  a sharper licensing/vocabulary framework than anything in the web research, and
  — worth flagging prominently — **its own full draft webinar dated for the same
  deadline in its `HANDOFF.md`.** See that file's "Open threads" for the question
  of whether this is the same webinar as the one this session is outlining.
- [`third-party-gems.md`](third-party-gems.md) — the Aakash Gupta/Shubham Saboo
  Substack piece, the `pm-github-starter-kit` GitHub repo, and Department of
  Product's "GitHub Explained for Product Managers." Two of these three carry
  real redistribution restrictions (**read the top of the file before reusing
  anything from them**). The Gupta/Saboo piece is also the freshest, most
  AI-native material in any pile so far — GitHub as a single PM's personal AI
  operating system (CLAUDE.md, skills, evals), not just team collaboration.
- [`productside-copy-gems.md`](productside-copy-gems.md) — from Dean's own
  `docs/Productside on GitHub.internal training.docx`. Different from every
  other file here: **this is Dean's own writing**, so it's directly reusable
  copy, not just source material — including two long lists of ready-made
  benefit one-liners. Also resolves (probably) the "is it the same webinar"
  question raised in `launchkit-gems.md`, via a marketing-copy template that
  confirms the September 2 date, title, speaker, and moderator.

## Quick map: gem → play

**Context**
- "The commit history on those two files IS your strategy timeline. No more ask
  Dean, he remembers why we cut SSO." — claude.workbench
- "You can't revert a market." — claude.workbench, decision record template
- Anne Thomas: "product management does not equal project management... we're
  talking about the why as opposed to the how." — youtube/Anne Thomas

**Communications**
- Developer-vs-PM contrast table ("How do I change the system?" vs "What is
  changing, why, and for whom?") — gpt.overview
- Discussion vs Issue distinction ("Should we do something about this?" vs "We
  have decided to investigate or change this.") — gpt.workbench
- Emoji-reaction voting on issues as free, built-in internal feedback capture —
  youtube/Anne Thomas

**Confidence** (was Experimentation)
- "Commit velocity tells you where the money's actually going. Marketing slides
  tell you where they want you to look." — claude.workbench
- "Stars are not market share. Issue volume is not pain severity. Commit velocity
  is not customer value." — claude.workbench / gpt.workbench (both land this almost
  verbatim, independently)
- "Beware the squeaky wheel." — youtube/Anne Thomas (external feedback caveat,
  sharper and more human than the stats-based guardrail above)
- Google Form → Zapier → GitHub Issue, a no-code version of the same automation
  idea — youtube/Anne Thomas

**Constitution** (was Governance)
- Seven-layer governance table (expectations → intake → routing → validation →
  accountability → policy → moderation) — gpt.comms
- "A DMV operated through YAML." — gpt.comms, the actual coined source of the
  phrase already in the project brief
- CODEOWNERS broadened past code (pricing rules, AI system prompts, customer-
  facing language, etc.) — gpt.comms
- Real caveat not in any AI-research doc: **to comment or vote on a GitHub issue
  you must be added to the repo** — youtube/Anne Thomas. Her workaround: a public
  Trello roadmap mirrors the internal GitHub one.
- A real, running Content Guard (pre-commit hook + GitHub Action + org secret)
  that blocks client names, oversized files, SharePoint file types, and
  credential-shaped strings before they're ever committed — launchkit-gems,
  `docs/02-governance/02-08-repository-operations.md`. This is the working
  version of the "governance automation" idea the AI docs only sketch in YAML.
- The category trap: your repo's vocabulary and license type are a legal signal
  about what kind of company you are, and picking the wrong one (e.g. a
  software license for a services business, or vice versa) invites obligations
  your contracts never intended — launchkit-gems,
  `docs/02-governance/02-09-positioning-licensing-and-terms.md`. Directly
  answers Dean's own manufacturer-vs-service licensing example.

**Community**
- "GitHub for Product Managers is not just repository literacy. It is designing a
  participation system." — gpt.comms, near-verbatim match to the project's own
  community-play framing
- Full loop diagram (community conversation → structured submission → automated
  checks → triage → human decision → release → shared learning) — gpt.comms. Strong
  candidate for the whole show's closing visual, not just the community module.

**Cold open / straw-man material**
- Google AI Overview: GitHub as "alternative to Jira or Trello," vocabulary table
  that stops at repo/branch/commit/merge — Goog.Overview
- Dean's own `deanpeters/product-manager-prompts` repo shows up as a top Google
  result for "github for product managers" — Goog.Overview
- Independent third-party agreement with the brief's own guardrail: "This topic is
  not at all needed for a product manager... 99% of the time... but your
  developers will [need Git]." — youtube/Git and GitHub for Product Managers

**AI-native personal ops (new angle, third-party-gems)**
- "Your skills have versions. Your CLAUDE.md changes every week... a single
  word shift can completely break your OS's behavior." — the sharpest cold-open
  hook found in any source, and the most current (June 2026).
- Three Repos framework (Workspace/private, Shared Tools/public, Projects/
  per-initiative) and the PM Artifact Workflow mapping each git step to the
  plain-English sentence you'd actually say to Claude Code ("Pull the latest
  changes," "Open a pull request") — the most demo-ready material gathered.
- Third independent source (after the web research's Actions guards and the
  launchkit's real Content Guard) landing on the identical "scrub before you
  push, a private repo is not a privacy strategy" rule.

## Open threads for Dean

0. **Kenny's role: trainer or trainee.** His note said "use me as the trainer,"
   then described Dean getting him onto GitHub, which reads as trainee. Dean is
   settling it. Either way it's a two-person live build, so the outline isn't
   blocked. Two things do change with the answer: who narrates each on-screen
   step, and whether the abstract doc's "Moderator: Kenny Kranseler" field should
   read co-presenter instead.

1. **Live demo decision.** Anne Thomas's talk is essentially a ready-made demo
   script: issue templates, labels, emoji voting, a Zapier intake form, an
   org-level roadmap project. If Phase 0 confirms a live walkthrough, this is the
   fastest path to one instead of building a demo from scratch.
2. **The repo-access-gating caveat is a real gap.** None of the eight AI-research
   docs mention that GitHub doesn't natively support open public comment the way
   the "community" framing implies — you have to add people to the repo, or lean
   on org-level Discussions. Worth addressing honestly in the community module
   rather than overselling it.
3. **Sixth-pillar problem.** The Gemini docs' Investment Horizon / portfolio
   allocation material (Core Innovation ~50%, Tech Debt ~20%, etc.) doesn't map to
   any of the five confirmed plays. Fold a piece into governance, or cut it. See
   `web-search-gems.md` → Governance section for the full table.
4. **Label taxonomy as a teaching device.** Anne Thomas's five labels (revenue,
   technical debt, MVP, nice-to-have, support) are a much simpler entry point than
   the RICE/WSJF custom-field approach in the AI docs. Could work as "the two-
   minute version" before showing the heavier framework, or as the only framework
   this webinar needs — worth Dean's call.
5. **Webinar collision — now probably resolved.** `productside-launchkit`
   contains its own full draft webinar dated for the same deadline as that
   repo's `HANDOFF.md`. A marketing-copy template that just landed in this
   repo's own `docs/` confirms the September 2, 2026 webinar's date, title
   ("How to Set Up a GitHub for Your Product Team"), speaker (Dean), and
   moderator (Kenny Kranseler) — strong evidence this is the same event as the
   Five Plays outline, not a second one. Working theory: one webinar, and the
   Governance play absorbs the launchkit's category-trap/licensing/secrets
   content rather than that staying a separate show. Worth a two-minute
   confirmation from Dean rather than assuming. See `productside-copy-gems.md`
   and `launchkit-gems.md` for the full detail.
6. **Redistribution risk on two third-party sources.** The Aakash Gupta/Saboo
   piece is paid content and the `pm-github-starter-kit` repo explicitly says
   "should not be redistributed." Fine to mine for ideas and structure, not
   safe to copy templates or exact wording into anything Dean publishes. See
   `third-party-gems.md` for the full breakdown of what's usable vs. off-limits.
7. **A sixth Constitution rule exists in the training doc but not yet in the
   launchkit's `CONSTITUTION.md`**: standardize on one AI coding assistant
   (Claude, not GitHub Copilot) org-wide. Strong, current material for the
   Governance play regardless of whether the launchkit itself gets updated —
   see `productside-copy-gems.md`.
8. **Two separate builds, same source material.** The internal training doc
   also proposes a smaller, non-technical Lunch & Learn for Productside staff
   (suggested for July 2026, before the September webinar) — a different
   audience and different stakes than the external Five Plays webinar. Keep
   the two outlines distinct even where content overlaps.
