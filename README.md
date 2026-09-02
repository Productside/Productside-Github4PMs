# Beyond the Backlog

**GitHub as durable memory for product teams — where your thinking compounds instead of evaporates.**

Teaching material from the [Productside](https://productside.com/) webinar "Beyond the Backlog" (September 2, 2026). Eight workflows show how a Product Manager and an AI assistant can share context, improve work on branches, commit with reasoning, review through pull requests, and reuse what the team already knows — without typing a single git command.

---

## Start Here

Pick the path that fits where you are right now.

**"I want to understand the argument."**
Read [Collaboration Pains](docs/slides/01_collaboration-pains.md). It names the five costs every product team pays — copying context, relitigating decisions, redoing discovery, remembering the rules, and losing unexplored ideas — and asks one question: *does your product team have a place where its thinking can compound?*

**"I want the vocabulary without the story."**
Open the [Field Guide](docs/field-guide.md). Twelve terms, nine workflows, a FAQ, and a "when to use what" matrix. Everything you need to talk about this with your team, in one page.

**"I want to see every workflow."**
Start at the [Slide Pages hub](docs/slides/run.md) and walk through all eight sections. Each page carries the teaching paragraphs, AI prompts, diagrams, and adoption limits that go deeper than the presentation deck.

**"I want the honest limits."**
Jump to [Appendix D: What GitHub Is Not Optimized For](docs/appendix.md#d-what-github-is-not-optimized-for). The UI curve, no Gantt charts, not everything belongs, the repo-access gate.

---

## The Collaborative Arc

The session tells one continuous story. Each section is the next thing that happens to Kenny — from naming the pain, through sharing and improving, to committing, reusing, and governing.

| Section | What happens | Workflows |
|---|---|---|
| [**Collaboration Pains**](docs/slides/01_collaboration-pains.md) | Name the five dysfunctions everyone shares | — |
| [**Collaborative Journey**](docs/slides/02_collaborative-journey.md) | The five-step learning path and first setup | WF1 |
| [**Collaborative Sharing**](docs/slides/03_collaborative-sharing.md) | Give AI and the team the same context; clone a shared library and run a skill | WF2–WF4 |
| [**Collaborative Improvements**](docs/slides/04_collaborative-improvements.md) | Branch safely; give SME feedback to the AI and watch it improve the work | WF5 |
| [**Collaborative Commits**](docs/slides/05_collaborative-commits.md) | Commit with reasoning, test the change, push a PR | WF6–WF7 |
| [**Collaborative Reuse**](docs/slides/06_collaborative-reuse.md) | Review, merge, turn practices into versioned assets | WF8 |
| [**Collaborative Governance**](docs/slides/07_collaborative-governance.md) | Legal, automation, and what GitHub is not optimized for | — |
| [**What Change Looks Like**](docs/slides/08_what-change-looks-like.md) | The KEEP / ADD / RESULT frame | — |

---

## Reference Material

| Document | What it gives you |
|---|---|
| [Field Guide](docs/field-guide.md) | Git and GitHub for Product Managers — vocabulary, nine workflows, FAQ, comparison matrix |
| [Appendix](docs/appendix.md) | Deeper reference: mental model, diagrams, adoption limits per workflow, governance, tool comparison |
| [Diagrams](docs/diagrams.md) | All diagrams in reading order — mermaid in markdown, version-controlled and diffable |
| [Polls](docs/polls.md) | The two audience polls and the taxonomy that connects them |

---

## The Three-Layer Pattern

This project demonstrates the governance pattern taught in the session. Every file you see here follows it:

| Layer | File | Job |
|---|---|---|
| **Context** | This README | What this project is and why it exists |
| **Contract** | [CLAUDE.md](CLAUDE.md) | How AI assistance works here: vocabulary rules, writing principles, what not to do |
| **Constitution** | [CONSTITUTION.md](CONSTITUTION.md) | Non-negotiable rules that override everything else |

The Constitution is the most important file. It is the one file nobody can override, including the AI. Open it. It is short.

---

## About the Session

**Beyond the Backlog** is a live, hands-on Productside webinar. Dean Peters narrates; Kenny Kranseler builds at the keyboard, hits the snags, and gets unstuck on camera. Kenny is on Windows, Dean is on a Mac — cross-platform by design, not by accident.

The AI harness (Claude Desktop + Claude Code) does the git. Kenny never types a git command. He says sentences. The only command line in the show is Dean's three-minute origin story.

This material is intended for reuse in Productside classes, workshops, and advisory engagements.

---

## Provenance and Reuse

All material in this project is original to Productside. Two research sources consulted during development carry redistribution restrictions (Aakash Gupta / Shubham Saboo piece, and `pm-github-starter-kit`); neither is included here, and derivative copying from them is not permitted.

© 280 Group LLC dba Productside. Licensed under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/).
