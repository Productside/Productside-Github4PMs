# Appendix — Beyond the Backlog

Deeper reference material for anyone who wants to go further after the webinar. Each section stands alone.

**Productside** · Beyond the Backlog · September 2, 2026

---

## A. Vocabulary and Mental Model

You only need enough vocabulary to ask for the outcome. The AI harness handles the mechanics.

| Term | Think of it as... |
|---|---|
| **Repository** | A versioned workspace containing the team's product context |
| **Clone** | Bring a shared repository onto my computer |
| **Pull** | Bring the latest shared changes down to me |
| **Push** | Share my local changes back to GitHub |
| **Branch** | Give me a safe parallel workspace for an alternative |
| **Commit** | Preserve a meaningful checkpoint and the reason for it |
| **Diff** | Show me exactly what changed |
| **Merge** | Make an accepted change part of the trusted version |
| **Pull request** | Ask the team to review a proposed change before accepting it |
| **Fork** | Give me my own copy of someone else's repository to evolve safely |
| **Issue** | An open question, unresolved product work, or a commitment to track |
| **Discussion** | A question that is still a question, not yet a commitment |
| **Main** | The team's trusted baseline. Not eternal truth, but the known starting point |

**The mental model:** Git is the machinery. GitHub is the shared workspace built around it. The AI harness is the operator and mechanic. You just need to know what outcome to ask for.

**Git is not GitHub.** Git tracks changes, branches, commits, merges, and history, starting on your computer. GitHub adds sharing, review, discussion, permissions, automation, and collaboration around Git repositories.

---

## B. Diagrams Reference

All diagrams in this project are mermaid in markdown, which GitHub renders natively. Each one is text, version-controlled, and diffable in a pull request. A diagram you can diff is the thesis of this session; a downloaded PNG quietly contradicts it.

The complete set lives in [`diagrams.md`](diagrams.md) (source of truth) with individual files generated in [`diagrams/`](diagrams/INDEX.md).

### Diagrams by section

| Section | Diagram | What it shows |
|---|---|---|
| The Problem | Where Thinking Dies | Three destinations where product thinking goes terminal |
| The Problem | Context Rebuilt vs. Compounded | The cost of starting from zero every session |
| Collaborative Journey | Four Steps, None of Them Planned | How version control became a collaboration platform |
| Collaborative Sharing | Scattered Artifacts vs. Shared Repository | The difference between a file share and a versioned workspace |
| Collaborative Sharing | Session-Based AI vs. Repo-Based AI | Why AI that reads the repo beats AI that reads your prompt |
| Collaborative Improvements | The Branch as a Safe Place to Be Wrong | Parallel exploration without breaking what works |
| Collaborative Commits | The Pull Request Path | Propose, review, discuss, merge |
| Collaborative Reuse | Tribal Knowledge Becomes Team Infrastructure | How practices move from people to reusable assets |
| Collaborative Governance | The Three Layers | Context (README), Contract (CLAUDE.md), Constitution (non-negotiable rules) |

### Notation

Every diagram in this set uses the same four marks:

- **Rectangle** — a thing that exists: a file, a repo, a person, a state
- **Diamond** — a decision or a check. Something evaluates and routes
- **Solid arrow** — the forward path. What normally happens next
- **Dotted arrow** — a return: feedback, a loop, a fallback, or a rejection with a reason

Dotted lines are where the value is. A process with no dotted lines is a conveyor belt, and nobody learns anything on a conveyor belt.

---

## C. Adoption and Limits

Each workflow in the webinar carries its own limits. They are collected here for reference.

### WF1-WF2: Setup and cloning

**Use this when:** the team is ready to put product context somewhere it can be versioned and shared.

**Skip it when:** the team has no product artifacts worth versioning yet. Start with the artifacts, not the infrastructure.

**What it does not do:** make anyone write things down who was not already writing things down.

### WF3: Give AI the same context as the team

**Use this when:** more than one person (or more than one AI session) is working from the same product context.

**Skip it when:** the work is genuinely solo and you trust your memory.

**What it does not do:** decide anything for you. It gets much better at drafting and at arguing with you. It still does not know which customer matters most.

### WF4: Run a shared skill

**Use this when:** the team has validated a repeatable practice and wants to run it consistently.

**Skip it when:** the skill has not been tested against real cases yet. A bad method applied consistently is worse than inconsistency.

**What it does not do:** guarantee accuracy. Every claim in a skill's output carries a source and a confidence label for a reason. Read the section that says what it will not claim, first.

### WF5: Branch to improve

**Use this when:** you are an SME on the work and you see something that should be better.

**Skip it when:** the improvement is trivial enough to commit directly. Not everything needs a branch. Fixing a typo and changing product strategy are not the same kind of change.

**What it does not do:** protect you from a bad idea. It protects the team from a bad idea shipping without review. The idea itself is still on you.

### WF6-WF7: Commit and push a PR

**Use this when:** the change deserves a record and a conversation before it becomes accepted truth.

**Skip it when:** the change is non-controversial and the team trusts you to commit directly. Process is a tool, not a virtue.

**What it does not do:** create a commit message for you. The AI writes one, but the reasoning is yours. "Updated file" is not reasoning. "Sharpened objection handling after losing the Acme deal" is.

### WF8: Review and merge

**Use this when:** the team needs to see exactly what changed, discuss it, and decide whether to accept it.

**Skip it when:** you are the only person who will ever read this context.

**What it does not do:** substitute for domain expertise. The reviewer does not have to be another PM. An engineer, a designer, or a support lead reading your reasoning will catch different things and usually better ones. But the reviewer needs enough context to challenge the change, not just approve it.

---

## D. What GitHub Is Not Optimized For

This is the honest part. GitHub's real caveats make the pitch more credible, not less.

### The UI curve

GitHub's interface was designed for developers. The learning curve is real for non-technical users, and pretending otherwise costs credibility. The AI harness absorbs most of the command-line complexity, but navigating the web UI still takes practice. The settings hunt is the number one dead-air risk in any live demo.

### No Gantt charts, no roadmap views

GitHub Projects can track work, but they are not a replacement for purpose-built project management. If your team needs Gantt charts, resource leveling, or portfolio-level views, those tools still have a job. GitHub is not trying to be Jira.

### Not everything belongs here

Whiteboards, slides, spreadsheets, analytics dashboards, and real-time collaborative documents still have jobs to do. The question is not "should we move everything to GitHub?" It is "which product context benefits from being shared, versioned, reviewable, traceable, safely experimentable, reusable, and accessible to AI?" That subset is the interesting candidate.

### The repo-access gate

Anyone who wants to comment on an issue, review a PR, or participate in a discussion needs a GitHub account and access to the repository. This is a genuine hole in the community story. Executives and external stakeholders are not going to create accounts. What changes is what you bring to them: you stop arriving with recollection and start arriving with what you knew, when, and what you traded away. But GitHub does not give you open participation, and anyone who tells you a stakeholder portal falls out of this is selling something.

### AI makes the case more urgent, but does not create it

The argument for structured, versioned, reviewable product context existed before AI. AI makes it more urgent because AI dramatically increases how much product work gets generated and changed, which makes coordination more important. But if the underlying practice is bad, AI just makes it bad faster.

---

## E. Governance Deep Dive

### The three-layer pattern

Every Productside repository follows three layers:

| Layer | File | Job |
|---|---|---|
| **Context** | `README.md` | What this project is and why it exists |
| **Contract** | `CLAUDE.md` | How AI assistance works here: vocabulary rules, writing principles, voice sources, what not to do |
| **Constitution** | `CONSTITUTION.md` | Non-negotiable rules that override everything else: no client names, no credentials, human review before publishing, private stays private |

The Constitution is the most important file in the repository. It is the one file nobody can override, including the AI. Its rules are short, absolute, and written for the worst case: the day someone asks the AI to do something it should not.

### Content guards

GitHub Actions can automate repeatable checks. The content guard workflow in Productside repositories blocks:

- Client names (from a blocked-terms list stored as an org secret, never committed)
- SharePoint file types (.pptx, .xlsx, .docx) that could accidentally carry metadata
- Oversized files that do not belong in a versioned repository
- Credentials and secrets patterns

The guard runs on every pull request. It is not a replacement for human review. It is the check that catches the things humans forget to look for under deadline.

### Branch protection

Branch protection on `main` means nobody pushes directly. Every change goes through a pull request, and at least one person reviews it before it merges. That is the gate between "someone proposed this" and "the team accepts this."

### Licensing for teaching materials

Productside's published materials use **CC BY-NC-ND 4.0** (Creative Commons Attribution-NonCommercial-NoDerivatives). This means: you can share the materials and give credit, but you cannot sell them, modify them, or create derivative works for commercial use. Copyright is held by 280 Group LLC dba Productside.

---

## F. Where to Go Next

### Repositories worth studying

**For product teams getting started:**
- Look at how open-source projects use Issues not as bug reports, but as proposals with discussion threads
- Study how `CONTRIBUTING.md` files set expectations without a meeting
- Notice how pull request templates turn "here's my change" into "here's what I changed, why, and how to test it"

### Prompts worth stealing

**Before a meeting:**
> Bring me current on this repository. Summarize the consequential changes since my last work and flag anything that changes our assumptions, decisions, strategy, or requirements.

**After customer research:**
> Show me what product context should change based on these findings. Propose the changes on a branch so I can review them before anything becomes part of main.

**After an AI working session:**
> Compare what we just produced with the team's trusted version. Show me the meaningful differences and ask before committing or merging anything.

**When two people are exploring alternatives:**
> Create separate branches from the latest main so we can explore both approaches without overwriting each other. Later, help us compare the differences.

**Three months later:**
> Help me trace when and why we changed this decision. Use the repository history and summarize the relevant commits and review trail.

**Setting guardrails:**
> Create a CONSTITUTION.md in this repository with these rules: no customer names, no material from client engagements, no credentials, private stays private, human review before anything leaves. Commit it to main.

---

## G. Tool Comparison

### Where each tool fits

| Capability | SharePoint / Confluence | Slack / Teams | Claude / ChatGPT Projects | GitHub (with AI Harness) |
|---|---|---|---|---|
| **Store finalized docs** | Strong | No | No | Possible but not its job |
| **Real-time chat** | No | Strong | No | No |
| **Persistent AI context** | No | No | Strong (solo) | Strong (team) |
| **Line-level diff** | No | No | No | Yes |
| **Branching / concurrent exploration** | No | No | No | Yes |
| **Commit with reasoning** | No | No | No | Yes |
| **Pull request review** | No | No | No | Yes |
| **Automated guardrails** | Limited | No | No | Yes (GitHub Actions) |
| **Fork and reuse** | Copy/paste | No | No | Yes (with relationship to source) |
| **Decision traceability** | Weak (page history) | No (scroll up) | No (session-bound) | Strong (commit + PR trail) |

**The point is not "migrate everything."** The point is: stop losing things. SharePoint stores the finished strategy. GitHub is where the strategy is still being argued.

### "But we already have..."

**SharePoint / Google Drive** — Strong at storing, organizing, and governing finalized documents. Cannot show you a line-level diff of what changed between two versions of a strategy document, who changed it, and why. No branching. No concurrent editing without "FINAL_v7" naming.

**Confluence** — Strong at publishing and navigating shared knowledge. Cannot let three people explore competing interpretations of new evidence on separate branches and compare the exact differences. Page history is snapshots, not a reviewable trail of reasoning.

**Claude Projects / ChatGPT Projects** — Strong at giving one person persistent AI context. Cannot share that context across a team. Your AI session is yours. A colleague's is theirs. Nobody sees what the other changed, and neither AI reads what the other produced.

**Slack / Teams** — Strong at fast, informal conversation. Cannot preserve decisions. The answer to "when did we decide to change the positioning?" is never "scroll up."

**GitHub is not replacing any of these.** It is the layer underneath for product context that is actively evolving, contested, and needs to be traceable.

---

*Productside · [productside.com](https://productside.com/) · Beyond the Backlog · September 2, 2026*
