# Git & GitHub for Product Managers: Field Guide

*A field guide for people who care about product context, not becoming command-line experts.*

**Productside** · Beyond the Backlog · September 2, 2026

---

## Why bother with this?

Product context changes constantly. Research challenges assumptions. Strategy moves. Decisions get revisited. AI generates alternatives. Several people may be changing related work at the same time.

The hard problem is not creating another document. It is keeping the product team oriented while the context changes:

- What changed? Why? When? Who changed it?
- What did we decide? What alternatives did we reject?
- What does the team trust now?
- Can I explore something new without stepping on everyone else's work?

Git and GitHub give product teams useful machinery for shared context, granular history, concurrent work, review, safe experimentation, automation, and reuse. And if you use Claude Code, Codex, or a similar AI harness, you can ask the harness to operate that machinery for you.

---

## Git is not GitHub

**Git** is the version-control machinery. It tracks changes, branches, commits, merges, and history, usually starting on your computer.

**GitHub** is the shared online workspace around Git repositories. It adds sharing, review, discussion, permissions, automation, and collaboration.

**The mental model:** Git is the machinery. GitHub is the shared workspace built around it. The AI harness is the operator and mechanic. You just need to know what outcome to ask for.

---

## You only need enough Git vocabulary to ask for the outcome

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

You can also make the harness slow down and explain itself:

~~~
Explain what you're about to do before you do it.
~~~

~~~
What are my options here, and what are the tradeoffs?
~~~

~~~
Tell me what branch I'm on and whether I have unfinished work.
~~~

~~~
Show me what changed and summarize the consequential differences.
~~~

~~~
Do the Git work for me, but don't merge anything without asking me.
~~~

---

## 0. Give this work one predictable home

Repositories multiply quickly. Keep them out of the archaeological dig that often becomes Documents. Put them under a Projects directory.

**macOS / Linux**

```bash
mkdir -p ~/Projects
cd ~/Projects
```

**Windows Command Prompt**

```cmd
cd %USERPROFILE%
mkdir Projects
cd Projects
```

From here on, examples assume repositories live under `~/Projects` on macOS/Linux or `%USERPROFILE%\Projects` on Windows.

---

## Workflow 1. Make sure the machinery is available

**The situation:** You're about to use a repository for the first time and would rather discover missing tools now than five minutes before a workshop.

~~~
Check whether Git and GitHub CLI are installed and whether this
computer is already authenticated with GitHub. Explain anything
I need to fix.
~~~

**The invisible machinery:**

```
git --version
gh --version
gh auth status
```

If one of these commands is not found, ask the harness to explain the installation options for your computer before proceeding.

---

## Workflow 2. Connect this computer to GitHub

**The situation:** You want your local product workspace and GitHub to stay connected so you can bring down team changes without fighting authentication every time.

~~~
Connect this computer to my GitHub account. Explain the
authentication choices, let me complete any browser sign-in
myself, and confirm Git can use the connection.
~~~

**The invisible machinery:**

```
gh auth login
gh auth setup-git
gh auth status
```

**What you gained:** Your harness can now pull shared context from GitHub and push your work back. GitHub CLI guides you through browser authentication, where your normal GitHub sign-in methods apply.

---

## Workflow 3. Clone a shared library & install its skills

**The situation:** Productside publishes a market intelligence skills library on GitHub with 22 skills and 22 prompts. You want to bring it onto your machine, install the skills into your AI harness, and start using them.

~~~
Clone the Productside Market Intelligence Skills repository into
my Projects directory and install the skills. Show me what's
available.
~~~

**The invisible machinery (macOS / Linux):**

```bash
cd ~/Projects
git clone https://github.com/Productside/Productside-Market-Intelligence-Skills.git
cd Productside-Market-Intelligence-Skills
```

**The invisible machinery (Windows):**

```cmd
cd %USERPROFILE%\Projects
git clone https://github.com/Productside/Productside-Market-Intelligence-Skills.git
cd Productside-Market-Intelligence-Skills
```

**To install the skills as a plugin:**

```
/plugin marketplace add Productside/Productside-Market-Intelligence-Skills
/plugin install mintel
```

**What you gained:** A versioned local copy of the entire library. You can read every skill, run them, and eventually improve them. The guardrails (evidence labeling, the do-not-invent list, the CONSTITUTION) ship with the tool.

---

## Workflow 4. Run a skill the team already built

**The situation:** You need a battle card for a competitor who showed up in two lost deals. The Battle Card Builder skill exists in the library you just cloned. Run it.

~~~
Use the battle card builder skill. My product is [your product].
The competitor is [competitor name]. We've lost two deals to them
in the mid-market segment. Build the card from public evidence.
~~~

**What happens:** The skill asks at most 3 setup questions, sweeps public sources, and produces a field-action card with a source URL and Fact / Inference / Assumption label on every claim. The section titled "the claims you must not make" is the one to read first.

**What you gained:** Instead of starting from scratch, you ran a skill the team already built and validated. The output is cited and traceable, not a hallucinated summary.

---

## Workflow 5. Fork a useful body of work and make it your own

**The situation:** You find the MI Skills library useful and want to adapt it for your own product or organization without changing Productside's original work.

~~~
Fork this repository into my GitHub account, clone my fork into
Projects, and explain the relationship between my copy and
the original.
~~~

**The invisible machinery:**

```
cd ~/Projects          # or %USERPROFILE%\Projects on Windows
gh repo fork Productside/Productside-Market-Intelligence-Skills --clone
cd Productside-Market-Intelligence-Skills
git remote -v
```

**What you gained:** You can reuse good product practice instead of rebuilding it, while safely evolving your own version. Your fork's relationship to the source stays visible.

---

## Workflow 6. Branch to improve what you know best

**The situation:** You ran the Battle Card Builder and spotted gaps. You're an SME on battle cards. You want to improve the skill based on what you know works in real deals, but the rest of the team is still using the current version.

~~~
Go to my clone of the Market Intelligence Skills repo. Make sure
main is current, then create a branch called improve-battle-card.
Do not change main.
~~~

**The invisible machinery:**

```
cd ~/Projects/Productside-Market-Intelligence-Skills
git status
git switch main
git pull
git switch -c improve-battle-card
```

**What you gained:** Your improvements live on `improve-battle-card`. The team's published version stays on `main`. Both exist at the same time. A branch is a safe place to be wrong.

---

## Workflow 7. Commit the change with the reasoning

**The situation:** You improved the battle card skill based on what you've seen work in real deals. You want future-you to know this was a deliberate improvement based on field experience, not a mysterious edit.

~~~
Show me exactly what I changed in the battle card skill. Help me
write a concise commit message that captures why, then commit it.
Do not push until I approve.
~~~

**The invisible machinery:**

```
git diff
git add prompts/battle-card-builder-prompt.md
git commit -m "Add deal-context section and sharpen objection handling based on field experience"
```

**What you gained:** The history preserves more than "a file changed." It preserves a useful, traceable point in the evolution of the team's practice.

---

## Workflow 8. Open a PR for the maintainer to review

**The situation:** Your battle card improvements are committed on your branch. You do not want to silently overwrite the published skill. You want the maintainer to see exactly what changed, discuss it, and approve before it becomes part of the library.

~~~
Push my improve-battle-card branch to GitHub and create a pull
request to the Productside Market Intelligence Skills repo.
Summarize what I improved and why. Do not merge it.
~~~

**The invisible machinery:**

```
git push -u origin improve-battle-card
gh pr create --fill
```

**What you gained:** The team can challenge the proposed change before it becomes accepted, trusted context. The content guard runs automatically on the PR: no client names, no credentials, no oversized files.

---

## Workflow 9. Walk into the meeting knowing what changed

**The situation:** It is Monday morning. Several people have worked in the MI Skills repo since you last looked. You do not want to reread every skill to discover what moved.

~~~
Bring me up to speed on the Productside Market Intelligence Skills
repo. Tell me what branch I'm on, what changed recently, and what
PRs were merged. Summarize the consequential changes, not just
filenames.
~~~

**The invisible machinery:**

```
cd ~/Projects/Productside-Market-Intelligence-Skills
git fetch
git log --oneline --decorate -10
gh pr list --state merged --limit 5
```

**What you gained:** Enter the conversation knowing exactly what changed: who improved which skill, what was merged, what PRs are open. No reconstructing history from chat.

---

## Prompts worth stealing

**Before a meeting:**

~~~
Bring me current on this repository. Summarize the consequential
changes since my last work and flag anything that changes our
assumptions, decisions, strategy, or requirements.
~~~

**After customer research:**

~~~
Show me what product context should change based on these findings.
Propose the changes on a branch so I can review them before anything
becomes part of main.
~~~

**After an AI working session:**

~~~
Compare what we just produced with the team's trusted version.
Show me the meaningful differences and ask before committing or
merging anything.
~~~

**When two people are exploring alternatives:**

~~~
Create separate branches from the latest main so we can explore
both approaches without overwriting each other. Later, help us
compare the differences.
~~~

**Three months later:**

~~~
Help me trace when and why we changed this decision. Use the
repository history and summarize the relevant commits and review
trail.
~~~

**Setting guardrails on sensitive material:**

~~~
Create a CONSTITUTION.md in this repository with these rules:
no customer names, no material from client engagements, no
credentials, private stays private, human review before anything
leaves. Commit it to main.
~~~

---

## When to use what

|  | **Static Storage** | **Actively Evolving Context** |
|---|---|---|
| **Team Alignment** | **SharePoint / Confluence** — Excellent for storing and publishing finalized knowledge and governance | **GitHub (with AI Harness)** — The only ground for actively evolving, contested, and traceable team context where humans and AI work concurrently |
| **Solo Work** | **Local Documents** — Disconnected. Prone to versioning chaos. Good for scratchpads | **Standalone ChatGPT / Claude** — Excellent for persistent AI context, but isolates the PM from the team's shared changes |

The point is not "migrate everything." The point is: stop losing things.

---

## FAQ for Product Managers

**Why not just use SharePoint?**
SharePoint is strong at storing, sharing, organizing, and governing documents. GitHub becomes interesting when the job is not merely "find the strategy document" but "show me exactly how the strategy changed, why, what alternatives were explored, and let several people work concurrently without trampling the trusted version."

**Why not just use Confluence?**
Confluence is strong at publishing and navigating shared knowledge. GitHub is useful when that knowledge is actively evolving and contested. Three people can explore different interpretations of new evidence separately, compare the exact differences, discuss them, and deliberately decide what becomes trusted context.

**Why not just use a Claude Project or ChatGPT Project?**
Those environments can be excellent for giving an AI persistent context. The harder problem is team context: you use one AI, a colleague uses another, somebody works manually, and all of you are changing related product thinking. A repository gives humans and AI systems shared ground where changes can be compared, reviewed, traced, and reconciled.

**Does everyone have to use the command line?**
No. The command line is here so you can see the machinery once. GitHub has graphical interfaces, and AI harnesses can perform Git operations for you. The useful skill is understanding the operation well enough to ask for the outcome and recognize what the harness proposes to do.

**Why should I care about branches?**
Because Product Managers ask "what if?" constantly. A branch lets you explore a different positioning, problem framing, requirement set, prompt, or product bet without rewriting what the rest of the team currently trusts.

**Why should I care about commits?**
Because "someone edited this in March" is weak product history. A useful commit creates a checkpoint around a meaningful change and records why it happened, making the evolution of product thinking easier to reconstruct later.

**Why would we use pull requests for product work?**
Some changes deserve conversation before they become accepted truth. If new evidence changes the problem framing or strategy, a pull request lets the team see exactly what is proposed, discuss it, revise it, and decide whether to accept it.

**Does this create a bunch of process?**
It can if you make everything ceremonial. Do not. Fixing a typo and changing product strategy are not the same kind of change. Use branches, review, and other controls when the uncertainty, collaboration, importance, or consequences justify them.

**What happens when several people work at once?**
They can work concurrently instead of taking turns in the same artifact or creating defensive copies. Git keeps parallel work separate until the team is ready to reconcile it. If changes collide, the conflict becomes explicit instead of somebody's work quietly disappearing.

**How does this help us remember why we made a decision?**
The reasoning can travel with the change through commits, reviews, issues, and discussions. That gives the team a trail closer to: what we knew, what changed, what we considered, what we decided, why.

**Where do GitHub Issues fit?**
Think "open question or unresolved product work," not "engineering ticket." An Issue can hold a customer problem we do not understand, conflicting evidence, an assumption to test, a decision to make, or a strategic question that should not disappear into meeting notes or chat.

**Where do GitHub Projects fit?**
Projects can give the team a view across investigations, experiments, decisions, and unresolved questions. The goal is not to rebuild Jira. It is to make evolving product work visible enough that the team knows what is being explored, what is unresolved, and what has been decided.

**Where do GitHub Actions fit?**
Think "what do we keep forgetting to check?" Actions can automate repeatable checks: required sections, citations, broken links, accidental secrets, prompt evaluations, or team conventions. The gain is not automation for its own sake; it is spending less human attention on repetitive vigilance.

**Where do AI agents fit?**
AI can dramatically increase how much product work gets generated and changed. That makes coordination more important. An agent can investigate or propose changes on a branch; the team can inspect, compare, challenge, reject, or accept them. AI gets freedom to work without automatically getting authority to change what the team trusts.

**Can multiple agents and humans work concurrently?**
Yes. Separate branches give humans and agents parallel working environments based on the same trusted context. Their proposals can later be compared and reconciled instead of everyone editing the same shared artifact at once.

**What's so important about main?**
Think of main as the team's trusted baseline, not eternal truth. Research, strategy, requirements, and decisions can all change. Main simply gives the team a known point from which to work while proposed changes are explored elsewhere.

**Should our entire product organization move everything into GitHub?**
Probably not. Whiteboards, slides, spreadsheets, analytics systems, and collaborative documents still have jobs to do. Ask which product context benefits from being shared, versioned, reviewable, traceable, safely experimentable, reusable, and accessible to AI. That is the interesting candidate.

---

## The point

Product teams are going to work faster, with more people and more AI systems producing and changing context. That makes an old problem more painful: What changed? Why? When? Who decided? What did we know then? What is trusted now? How do we explore alternatives without trampling each other?

**You are not learning Git so you can become a programmer.**

You are learning just enough of the model to tell your AI harness what outcome you want, ask it to explain your options, and let it handle the mechanics while you provide the product judgment.

---

**The library used in this guide is live:** [Productside Market Intelligence Skills](https://github.com/Productside/Productside-Market-Intelligence-Skills)

*Productside · [productside.com](https://productside.com/) · Beyond the Backlog · September 2, 2026*
