# Git and GitHub for Product Managers: Field Guide

*For people who care about product context, not becoming command-line experts.*

Productside · Beyond the Backlog

---

## The Point

Product work changes constantly. Research arrives. Assumptions break. Decisions move. AI produces alternatives. Several people may be changing related work at the same time.

The hard problem is not writing one more document. The hard problem is keeping the team oriented while the work changes:

- What changed?
- Why did it change?
- Who changed it?
- What did we decide?
- What is still open?
- What does the team trust now?

GitHub helps because it gives product work a shared place with history, review, discussion, and safe experimentation.

You do not need to become a programmer. You need enough of the model to ask for the outcome you want and recognize whether the answer is safe.

---

## First Win: Read A Repo Like A Product Manager

Do this in the browser. No install. No command line.

Open any GitHub repository your team uses, then look for four things:

| Look for | What it tells you |
|---|---|
| `README.md` | What this workspace is for and where to start |
| Folders | What kinds of work live here |
| Recent commits | What changed recently |
| Issues or pull requests | What is open, proposed, or under review |

Ask yourself:

- Can I tell what this repo is for in under two minutes?
- Can I find the trusted starting point?
- Can I tell what changed recently?
- Can I tell what is still unresolved?

That is the first win. You are not operating GitHub yet. You are learning how to read it as product context.

---

## Second Win: Ask For Orientation

If you have an AI assistant that can see the repo, ask it to orient you before it changes anything.

```text
Explain this repo for a Product Manager. What is the purpose,
what files matter most, what decisions are visible, and what
should I avoid changing without review?
```

Then ask for the safety check:

```text
Before suggesting changes, tell me what you can see, what you
cannot see, and what assumptions you are making.
```

What good looks like:

- The assistant points to specific files.
- It separates facts from guesses.
- It tells you what not to change casually.
- It offers a small next step instead of a giant makeover.

If the answer sounds confident but vague, ask it to slow down:

```text
Show me the files you used and quote only the short lines that
support your summary.
```

---

## Third Win: Make One Change Safely

Start with one small piece of product thinking:

- An open question.
- A decision note.
- A customer insight summary.
- A competitive observation.
- An assumption list.
- A meeting follow-up that should not disappear into chat.

Ask your assistant:

```text
Create a short Markdown note for this product question. Keep it
simple: context, what we know, what is open, and the decision
needed. Do not publish or merge anything.
```

Then ask:

```text
Show me the exact change. Explain what changed in plain English
and suggest a commit message that captures why this note matters.
```

What good looks like:

- You can see the exact difference.
- The change is small enough to review.
- The reason for the change is written down.
- Nothing becomes trusted team context without review.

---

## The Words You Actually Need

| Term | Think of it as |
|---|---|
| **Repository** | A shared, versioned workspace |
| **README** | The front door |
| **Commit** | A meaningful checkpoint with a reason |
| **Diff** | The exact before-and-after |
| **Branch** | A safe place to try something |
| **Pull request** | A proposed change asking for review |
| **Issue** | A visible question, decision, or piece of work |
| **Main** | The version the team currently trusts |

You do not need to memorize the machinery. You need to know which word maps to the product behavior you want.

---

## Seven Product Workflows

| Workflow | Use it when | First prompt |
|---|---|---|
| **Share** | Product context is scattered | `What should live in this repo so a new teammate can understand the product faster?` |
| **Collaborate** | A question keeps resurfacing | `Turn this into a GitHub issue with context, options, and a clear decision needed.` |
| **Review** | A change affects shared understanding | `Show me what changed and what a reviewer should pay attention to.` |
| **Trace** | Nobody remembers why something changed | `Use the file history to explain what changed, when, and why.` |
| **Experiment** | You want to try an alternative | `Create a safe branch for this idea and keep the trusted version unchanged.` |
| **Augment** | AI needs durable context | `Read the repo context first, then explain the rules and files that should guide this work.` |
| **Reuse** | A useful practice should spread | `Turn this repeated workflow into a reusable template or checklist.` |

---

## What To Ask Before A Change

Before your assistant changes files, ask:

```text
Tell me the smallest safe change you recommend, which files it
would touch, and what could go wrong.
```

Before accepting a change, ask:

```text
Show me the exact diff and summarize the product impact in plain
English.
```

Before sharing work more broadly, ask:

```text
Check this for sensitive information, copied third-party material,
unsupported claims, and anything that needs human review.
```

These prompts keep you in the Product Manager seat. The assistant can handle the mechanics. You keep judgment.

---

## When To Use GitHub

GitHub is useful when the product context is:

- Changing over time.
- Shared by more than one person.
- Important enough to review.
- Easy to lose in chat or slides.
- Useful for an AI assistant to read later.
- Something another team might reuse.

GitHub is probably not the right home when the work is:

- A one-off scratchpad.
- A polished presentation.
- A spreadsheet-heavy analysis.
- A confidential document that belongs in an approved internal system.
- A whiteboard conversation that has not settled into anything durable yet.

The point is not to move everything. The point is to stop losing the product thinking that should compound.

---

## Frequently Asked Questions

**Do I have to use the command line?**
No. You can learn the model in the browser and ask an AI assistant to handle the mechanics when local Git work is needed.

**Am I supposed to become a developer?**
No. The goal is to understand enough to collaborate, review, trace, and protect product context.

**What if I break something?**
Start small. Ask the assistant what it will change before it changes anything. Use branches for experiments. Review the diff before accepting changes.

**Why not just use docs or slides?**
Use them where they fit. GitHub helps when the context keeps changing and the team needs history, review, parallel work, and durable AI-readable context.

**What belongs in a Product Manager repo?**
Research summaries, decision notes, assumptions, strategy drafts, reusable templates, product narratives, prompts, guardrails, and anything the team needs to find again with its reasoning intact.

**What should stay out?**
Sensitive company information, customer or learner data, credentials, copied third-party material, and anything your organization would not want shared outside the right audience.

---

## A Good First Repo Shape

```text
README.md
decisions/
  0001-example-decision.md
questions/
  pricing-open-questions.md
research/
  synthesis.md
templates/
  decision-note.md
CONSTITUTION.md
```

This is not a rule. It is a starting shape. The best repo is the one your team can understand and keep using.

---

## The Product Manager Job

The assistant can create branches, write files, summarize diffs, and prepare commits.

Your job is to decide:

- Is this the right problem?
- Is the evidence good enough?
- Is this safe to share?
- Who should review it?
- What should become trusted team context?

That is why GitHub matters for Product Managers. It gives your product judgment a durable place to live.

---

Productside · [productside.com](https://productside.com/)
