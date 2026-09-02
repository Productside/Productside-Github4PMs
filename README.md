# Beyond the Backlog

**A webinar companion for Product Managers who want to start using GitHub at work.**

GitHub can feel like it belongs to engineers. This repo is here to make it useful for Product Managers too: as a place to keep product context, decisions, evidence, experiments, reviews, and reusable practices where the team and its AI assistants can find them again.

You do not need to code to get value from this repo.

If GitHub makes you nervous, start in the browser and do not clone anything yet. Your job is to read the product context, ask better questions, and make small changes reviewable. The tools can handle the mechanics later.

## Start Here

Your first win is to understand one workflow well enough to try it safely.

1. Open the [Field Guide](docs/field-guide.md).
2. Do the browser-only exercise in **First Win: Read a Repo Like a Product Manager**.
3. Then try the second or third win when you are ready.

## Three Quick Wins

| Win | What you will do | Where to start |
|---|---|---|
| **First win** | Read a repo and know what matters | [Read a repo like a Product Manager](docs/field-guide.md#first-win-read-a-repo-like-a-product-manager) |
| **Second win** | Ask an AI assistant to orient you without touching anything | [Ask for orientation](docs/field-guide.md#second-win-ask-for-orientation) |
| **Third win** | Make one small product note reviewable | [Make one change safely](docs/field-guide.md#third-win-make-one-change-safely) |

## What GitHub Helps Product Teams Do

| Workflow | In plain English |
|---|---|
| **Share** | Give product context one durable home |
| **Collaborate** | Keep questions, commitments, and disagreement visible |
| **Review** | Check proposed changes before they become accepted context |
| **Trace** | See what changed, who changed it, and why |
| **Experiment** | Try alternatives without disturbing the version the team trusts |
| **Augment** | Let AI read the same durable context as the team |
| **Reuse** | Turn useful practices into assets another Product Manager or team can adopt |

Open [The seven capabilities as one story](docs/diagrams/32-the-seven-capabilities-as-one-story.md) if you want the whole model on one page.

## Use The Prompts

Copy one of these into Claude Code, Codex, GitHub Copilot, or whatever AI assistant can see your files.

```text
Explain this repo for a Product Manager. What is the purpose,
what files matter most, what decisions are visible, and what
should I avoid changing without review?
```

```text
Turn this unresolved product question into a GitHub issue with
context, options, and a clear decision needed.
```

```text
Show me what changed, summarize the product impact, and suggest
what a teammate should review before this becomes accepted.
```

## Clone This Repo When You Are Ready

You can read everything in the browser. Clone it only when you want a local copy to annotate, adapt, or inspect with an AI assistant. Cloning is a later win, not the price of admission.

```bash
mkdir -p ~/Projects
cd ~/Projects
git clone https://github.com/Productside/Productside-Github4PMs.git
cd Productside-Github4PMs
```

After cloning, ask:

```text
Orient me to this repo as a first-time Product Manager reader.
What should I read first, what should I try first, and what
should I ignore for now?
```

## What Lives Here

| Path | Purpose |
|---|---|
| [docs/field-guide.md](docs/field-guide.md) | The main practical guide |
| [docs/diagrams/INDEX.md](docs/diagrams/INDEX.md) | Reusable workflow diagrams |
| [docs/diagrams.md](docs/diagrams.md) | Editable source for the diagram set |
| [docs/blog-beyond-the-backlog.md](docs/blog-beyond-the-backlog.md) | Longer-form webinar framing |
| [CLAUDE.md](CLAUDE.md) | Guidance for AI assistants working in this repo |
| [CONSTITUTION.md](CONSTITUTION.md) | Safety, privacy, and reuse rules |

## Use This Safely At Work

Start private. Keep sensitive product, customer, learner, and company material out of public repositories. Make sharing a deliberate review step, not a casual settings change.

Before sharing anything from your organization, ask:

- Does this include customer, employee, learner, or client information?
- Does this include confidential product, sales, support, finance, or strategy context?
- Did we copy wording, templates, or assets from someone else?
- Would we be comfortable with this appearing in search results?
- Has a human reviewed it?

---

© 280 Group LLC dba Productside.
