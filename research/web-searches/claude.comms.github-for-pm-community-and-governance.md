# GitHub for Product Manager Communities and Governance

The Workbench doc is about how one Product Manager or one product team thinks: context, market intelligence, ideation, execution, the loop back to belief. Single team, single repo, self-governed.

This doc is what happens when that scales past one team. Once support, design, other product teams, and eng all want to file into the same system, "self-governed" isn't enough. You need rules about who can change what, and automations that enforce quality at the point of submission instead of in a review meeting three weeks later. That's a different problem with different stakeholders, so it gets its own document.

---

## 1. Org-Level Community: Beyond One Repo

GitHub Projects v2 pulls Issues and PRs from any repo across the org into a single board. "Community" stops meaning one team's repo and starts meaning product, design, support, and eng all filing into the same Opportunity board, filtered by custom fields (team, product line, lifecycle stage).

One shared feed, many views. Support sees their filter. Exec sees theirs. Same underlying data, no duplicate reporting, no "which spreadsheet is current."

This only works once the workbench repo pattern is already running in at least one team. Community layer sits on top of working practice, it doesn't substitute for it.

---

## 2. Governance: Who Can Change What

### CODEOWNERS for decision integrity

A `CODEOWNERS` file maps specific paths to required approvers.

```
/product-context/decisions/pricing-*.md    @finance-lead
/product-context/vision.md                 @vp-product
/product-context/decisions/                @product-leads
```

This stops quiet edits to strategy. Nobody rewrites `vision.md` without the right eyes on it, the same way nobody merges to `main` without review. If a decision record touches pricing, Finance signs off before it merges, not after it ships.

### Branch protection as context integrity

Protect the branch holding `/product-context`. Require an approving review and a passing automated check before merge. This is the closest GitHub equivalent to "you can't declare a new strategy in a hallway conversation and have it stick." If it's not reviewed and merged, it's not the strategy yet.

### Required fields, not just templates

Issue forms with `required: true` reject incomplete submissions at the form level, before a human wastes time on them.

```yaml
- type: textarea
  id: evidence
  attributes:
    label: What evidence supports this?
  validations:
    required: true
```

No more opportunity issues that just say "make it faster."

---

## 3. Automations That Enforce Guidelines Instead of Policing Them After the Fact

Each of these is a small GitHub Action, running quietly at submission or merge time:

- **Vocabulary check.** Runs on every PR touching `/product-context/*.md`. Checks changed text against a controlled lexicon and flags violations before merge. Same principle as controlled-vocabulary QA on a client deliverable, just running automatically instead of by hand.
- **Evidence-link enforcement.** A PR can't merge into `decisions/` unless its description links to at least one Issue labeled `evidence`. No decision record gets created on vibes alone.
- **Stale-idea sweep.** Anything labeled `exploring` with no activity in 60 days gets auto-flagged for a Park or Kill decision, instead of dying quietly and getting re-pitched by someone who forgot it existed.
- **Stakeholder ping.** Merging a change to a decision record notifies whoever is listed in that file's frontmatter (`stakeholders: [sales-lead, support-lead]`), so context changes don't sit undiscovered by the people they affect.
- **Needs-info auto-label.** An Action scans submitted text for missing required narrative sections, not just empty form fields, and auto-labels `needs-info`, assigns it back to the submitter, and comments with exactly what's missing.

Skeleton for the evidence-link check:

```yaml
name: Require Evidence Link
on:
  pull_request:
    paths:
      - 'product-context/decisions/**'
jobs:
  check-evidence:
    runs-on: ubuntu-latest
    steps:
      - name: Verify PR body links an evidence issue
        run: |
          if ! grep -qE "#[0-9]+" <<< "${{ github.event.pull_request.body }}"; then
            echo "No linked evidence issue found. Add a reference like #142."
            exit 1
          fi
```

---

## 4. Community Health Files, Repurposed

- `CONTRIBUTING.md` stops meaning "how to submit a pull request" and starts meaning "how to submit a product opportunity": what evidence is required, which Discussion category to use, what happens after submission, how long triage takes.
- `CODE_OF_CONDUCT.md` sets norms for how ideas get challenged: attack the evidence, not the person. Worth having the moment cross-functional strangers start filing into a shared board instead of just your own product team.

These exist so a new contributor from another team can self-serve the norms instead of learning them by getting publicly corrected.

---

## 5. What This Protects Against

- **Silent strategy drift.** Without CODEOWNERS, anyone can edit `vision.md` and nobody notices until it's load-bearing and wrong.
- **Backlog pollution.** Without required fields, "make it faster" becomes a ticket with a story point estimate before anyone asks what evidence supports it.
- **Zombie ideas.** Without the stale-idea sweep, killed-in-spirit ideas never get killed on paper, and someone re-pitches them next quarter as new.
- **Governance theater.** The failure mode of this whole doc is writing rules nobody enforces. If it's not automated or gated by CODEOWNERS, it's a wiki page people will ignore under deadline pressure. Automate the ones that matter, don't just document them.

---

## 6. Quick-Start Checklist

- [ ] Add a `CODEOWNERS` file requiring review on `/product-context/decisions/` and `vision.md`
- [ ] Protect the branch holding `/product-context`
- [ ] Add `required: true` to the evidence and outcome fields on your opportunity and market-signal issue forms
- [ ] Ship one governance Action to start: evidence-link enforcement on `decisions/` is the highest-leverage one
- [ ] Write a `CONTRIBUTING.md` framed around submitting an opportunity, not submitting code
- [ ] Set up the stale-idea sweep before you open the board to a second team, so the backlog doesn't rot in public
- [ ] Only open the Projects board to other teams once one team has run the workbench pattern cleanly for at least a month
