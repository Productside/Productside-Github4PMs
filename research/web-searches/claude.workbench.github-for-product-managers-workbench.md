# GitHub as a Product Manager Workbench

GitHub for engineers is organized around code: the thing you can diff and test. GitHub for Product Managers has to organize around a different unit: decisions. What we believed, what changed, why, and what we did about it.

This doc is the repo scaffold, the workflows, and the templates that make that real, not a metaphor.

---

## 1. Repo Architecture

One repo per product or initiative. This is the skeleton.

```
/product-context
    vision.md
    outcomes.md
    personas.md
    glossary.md
    metrics.md
    market-assumptions.md
    decisions/
        0001-why-we-cut-sso-from-v1.md
        0002-why-we-repriced-tier-2.md
    experiments/
        exp-014-onboarding-checklist.md
.github/
    copilot-instructions.md
    prompts/
        market-scan.prompt.md
        rfc-review.prompt.md
    ISSUE_TEMPLATE/
        opportunity.yml
        market-signal.yml
```

`vision.md` and `outcomes.md` are living documents. Every time the team's understanding changes, that's a commit with a reason attached. The commit history on those two files IS your strategy timeline. No more "ask Dean, he remembers why we cut SSO."

---

## 2. The Five Systems

### System 1: Context

**GitHub primitive:** Repository + Wiki + commit history
**Replaces:** Confluence pages nobody updates, tribal knowledge, "wait, why did we decide that?"

- `vision.md` / `outcomes.md` at root: current state of belief, always current, always versioned.
- Wiki tab: slower-moving reference (personas, glossary, market assumptions) that doesn't need commit-level granularity.
- `decisions/` folder: one file per real decision. Template below.

**Decision Record template:**
```markdown
# Decision 0002: Why we repriced Tier 2

Date: 2026-03-14
Status: Active

## What we believed before
[the old assumption]

## What changed
[the evidence, the signal, the customer conversation]

## What we decided
[the actual decision, stated plainly]

## What would make us revisit this
[the trigger condition for re-litigating, not reverting]
```

Note: "revert" is an engineering concept that doesn't survive translation. You can't revert a market. The decision record's job is to name the condition under which you'd re-open the question with fresh evidence, not restore old state.

---

### System 2: Market Intelligence

**GitHub primitive:** Watched repos, Issues search, Discussions, release diffs
**Replaces:** Manually checking competitor blogs and hoping their marketing page tells the truth

Three concrete workflows, run on a cadence:

**Competitive change detection**
1. Watch competitor/adjacent public repos.
2. Diff each release against the last.
3. Read the issues and PRs tied to that release.
4. Log what's getting sustained investment vs. one-off patches.

Commit velocity tells you where the money's actually going. Marketing slides tell you where they want you to look. These are not the same list.

**Problem mining**
Search public issues/discussions in adjacent ecosystems for:
- "I'm trying to..."
- "The workaround is..."
- "Why doesn't this support..."

This is hypothesis generation from unfiltered user language, before you've spent a dollar on formal discovery.

**Ecosystem mapping**
Forks, dependents, contributor graphs. Shows what's becoming infrastructure and where integration friction is creating an opening for you.

**The caveat that keeps this honest:**
Stars are not market share. Issue volume is not pain severity. Commit velocity is not customer value. This is signal for triangulation, not proof. File every signal as an Issue (see template below) and let it earn its way to a decision.

**Market signal issue template (`market-signal.yml`):**
```yaml
name: Market Signal
body:
  - type: textarea
    attributes:
      label: What did you observe?
  - type: dropdown
    attributes:
      label: Source type
      options: [competitor release, public issue thread, customer signal, analyst report, other]
  - type: dropdown
    attributes:
      label: Confidence
      options: [low, medium, high]
  - type: textarea
    attributes:
      label: What decision might this inform?
```

---

### System 3: Ideation

**GitHub primitive:** Discussions -> Issue forms -> Projects board
**Replaces:** Idea docs in Drive that die silently with no record of why

Ideas don't go straight to backlog. They go through a funnel:

```
Observed signal
    -> Opportunity note (Discussion thread)
    -> Divergent options, pushback, reactions
    -> Assumptions and evidence gaps named
    -> Smallest useful test proposed
    -> Decision: Explore / Park / Kill
    -> If explored: becomes an Issue with evidence attached
```

Discussions are for divergence. Issues are for things that have earned commitment. Collapsing that distinction is how you get a backlog full of half-formed ideas wearing ticket costumes.

**Opportunity issue template (`opportunity.yml`):**
```yaml
name: Opportunity
body:
  - type: textarea
    attributes:
      label: What problem or unmet need did you observe?
  - type: textarea
    attributes:
      label: Who experiences it?
  - type: textarea
    attributes:
      label: What evidence supports it?
  - type: textarea
    attributes:
      label: What outcome would this move?
  - type: textarea
    attributes:
      label: What's the smallest useful test?
  - type: textarea
    attributes:
      label: What would make us NOT pursue this?
```

That last field matters most. It's the one nobody asks and the one that kills zombie ideas before they eat a quarter.

Killed ideas stay visible, labeled `killed`, not deleted. Same as an abandoned branch. Nobody re-pitches a zombie six months later without someone linking the receipt.

---

### System 4: Execution

**GitHub primitive:** Projects v2 with custom fields
**Replaces:** A roadmap slide that's actually just a prioritized guess

- Custom fields for RICE (Reach, Impact, Confidence, Effort) or WSJF, so prioritization is visible math, not a HiPPO's gut feeling.
- One underlying dataset, three views: Kanban for sprint execution, Table for backlog grooming, Roadmap view for the exec update. Same data, three audiences, zero reformatting.
- Every Issue in this system links back to the Opportunity or Decision Record that justified it. If it doesn't link back, it's scope creep with a ticket number.

---

### System 5: The Loop Back

**This is the one everyone skips, and it's the one that makes this a system instead of a stack of tools.**

```
context -> market signal -> opportunity -> options -> evidence
-> decision -> issue -> PR -> release -> outcome -> back to context
```

Shipping is not the end state. It's an update to what the team believes. When a release goes out, the loop isn't closed until:
- The outcome gets logged against the original hypothesis.
- `vision.md` or the relevant decision record gets updated if belief changed.
- The experiment file in `/experiments` gets its result filled in.

If the repo doesn't write back to context, you've built a delivery tracker with better branding. Not a product operating system.

---

## 3. The AI Layer

`.github/copilot-instructions.md` gives any agent operating on this repo persistent knowledge of your outcomes, glossary, and decision history before it answers a single question. Repo-level prompt files (`market-scan.prompt.md`, `rfc-review.prompt.md`) turn recurring PM workflows into reusable, versioned assets instead of a prompt you retype into a chat window every Tuesday.

This is the same three-file scaffold logic (README / CLAUDE.md / CONSTITUTION.md) already running for engineering context, pointed at product reasoning instead of build systems. Same instinct, different object.

---

## 4. What This Isn't

- Not a replacement for customer research. It's triangulation input.
- Not a guarantee ideas get better. It's a guarantee bad ideas leave a trace when they die.
- Not "Jira with extra steps." If your team starts treating Issues as the front door for every half-formed thought, you've rebuilt the ticket-monkey backlog with a GitHub logo on it. The Discussion-to-Issue funnel is the whole point. Don't skip it.

---

## 5. Quick-Start Checklist

- [ ] Create `/product-context` with `vision.md` and `outcomes.md`
- [ ] Write Decision Record 0001 for your last big call, even retroactively
- [ ] Set up `opportunity.yml` and `market-signal.yml` issue forms
- [ ] Create three Discussion categories: Customer Problems, Market Observations, Product Ideas
- [ ] Build one Projects v2 board with a RICE or WSJF custom field
- [ ] Write `.github/copilot-instructions.md` pointing at `/product-context`
- [ ] Pick one shipped feature and write the "loop back" entry for it, so you have a working example before asking the team to do it live

Ready to open this up past one team? See the companion doc: **GitHub for Product Manager Communities and Governance.**
