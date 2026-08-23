# Web Research Gems — the eight AI-generated source docs

Source folder: `research/web-searches/`. Files: `claude.comms...md`,
`claude.workbench...md`, `gem.comms...md`, `gem.workbench...md`, `Goog.Ovierview.md`,
`gpt.comms...md`, `gpt.overview...md`, `gpt.workbench...md`.

Organized by the five confirmed plays, plus a cold-open section and a leftover-
material section for the stuff that doesn't fit cleanly.

---

## Context setting

**Repo architecture that actually got proposed** (claude.workbench):

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
    experiments/
        exp-014-onboarding-checklist.md
.github/
    copilot-instructions.md
    prompts/
        market-scan.prompt.md
        rfc-review.prompt.md
```

This is screenshot-able as-is for a "here's what the folder actually looks like"
slide.

**Decision Record template** (claude.workbench) — the punchline is the last field:

```
# Decision 0002: Why we repriced Tier 2
Date / Status
## What we believed before
## What changed
## What we decided
## What would make us revisit this
```

Quote: *"'Revert' is an engineering concept that doesn't survive translation. You
can't revert a market."* This is the single sharpest line in the whole set —
strong candidate for the module's closing beat.

**The line that should open this module**: *"The commit history on those two
files IS your strategy timeline. No more 'ask Dean, he remembers why we cut
SSO.'"* (claude.workbench). Note it literally uses "Dean" as the stand-in name in
the sample doc — worth a wink if you use it live.

**GPT's version leans on real citations** (gpt.workbench) — repo-level Copilot
custom instructions, reusable prompt files, custom agents, repository indexing are
all real, currently-shipping GitHub Copilot features with doc links. Use this doc
if a module needs "here's the actual feature, here's the actual GitHub doc"
grounding instead of a hypothetical.

**Gemini's six-pillar ASCII diagram** (the doc filed as `gem.comms` despite the
content being structural, not comms-specific):

```
1. CONTEXT & STRATEGY HUB
        |
2. MARKET DISCOVERY RADAR   |   3. ASYNC IDEATION STUDIO
        |
4. PRODUCT GOVERNANCE & STAGE-GATES
        |
5. PORTFOLIO & INVESTMENTS  |   6. EXECUTION & OPERATIONS
```

Could be redrawn as a visual for the run-of-show overview slide even though the
webinar collapses this into five plays, not six.

---

## Communications

**The single best slide-ready asset across all eight docs** — developer-vs-PM
contrast table (gpt.overview):

| GitHub for developers | GitHub for Product Managers |
|---|---|
| How do I change the system? | What is changing, why, and for whom? |
| Branches, commits, tests, builds | Issues, decisions, dependencies, releases |
| Code correctness | Product intent and outcome alignment |
| Implementation detail | Traceability from problem to shipped behavior |
| Merge the change | Understand, challenge, explain, and learn from the change |
| Optimize engineering flow | Reduce context loss across the product team |

**Discussion vs Issue, the cleanest phrasing found** (gpt.workbench):
*"Discussion: 'Should we do something about this?' Issue: 'We have decided to
investigate or change this.' Pull request: 'Here is the proposed
implementation.' Release: 'Here is what became available.'"*

**PRD "code reviews"** (gem.comms / gpt.overview, both docs independently land
this): drafting a PRD as a Markdown file on a branch, opening it as a pull
request, and letting engineers/designers/security leave line-by-line inline
comments directly on the spec text. This is the single most concrete "here's how
a PM actually uses a pull request" idea in the whole set — good live-demo
candidate.

**The developer-vs-PM review lens list** (gpt.overview) — what a PM should
actually be looking for when reviewing a pull request, as opposed to code
elegance: user-visible language, business rules, edge cases, accessibility,
analytics/observability, permissions/privacy, rollout behavior, documentation,
reversibility.

---

## Experimentation

**The line to build the whole module around** (claude.workbench): *"Commit
velocity tells you where the money's actually going. Marketing slides tell you
where they want you to look."*

**Immediately followed by the guardrail** — three sources land nearly identical
phrasing independently (claude.workbench, gpt.workbench): *"Stars are not market
share. Issue volume is not pain severity. Commit velocity is not customer
value."* Use both lines back to back — the swagger line, then the humility line.

**Problem-mining search language** (claude.workbench / gpt.workbench) — search
public issues/discussions for the phrases people actually use:
- "I'm trying to..."
- "The workaround is..."
- "Why doesn't this support...?"
- "This breaks when..."
- "Is there a way to...?"

**The opportunity issue template**, full field list (claude.workbench):

```yaml
- What problem or unmet need did you observe?
- Who experiences it?
- What evidence supports it?
- What outcome would this move?
- What's the smallest useful test?
- What would make us NOT pursue this?
```

The last field is called out explicitly in the source doc as the one that
matters most — *"it's the one nobody asks and the one that kills zombie ideas
before they eat a quarter."*

**The full loop-back diagram** (claude.workbench), System 5:

```
context → market signal → opportunity → options → evidence
→ decision → issue → PR → release → outcome → back to context
```

Quote: *"If the repo doesn't write back to context, you've built a delivery
tracker with better branding. Not a product operating system."* Strong closing
line for this module, or for the whole show.

**Killed ideas stay visible, labeled `killed`, not deleted** — "same as an
abandoned branch. Nobody re-pitches a zombie six months later without someone
linking the receipt." Good concrete artifact to show on screen.

---

## Governance

**The best structural asset in the whole set** — the seven-layer governance
table (gpt.comms):

| Layer | GitHub mechanism | Product purpose |
|---|---|---|
| Set expectations | README, CONTRIBUTING, Code of Conduct, SUPPORT, SECURITY | Explain participation rules |
| Structure intake | Discussion forms, issue forms, PR templates | Request the right context |
| Classify and route | Labels, Projects, workflows, Actions | Put submissions in the right flow |
| Validate | GitHub Actions and status checks | Test required standards |
| Request accountability | CODEOWNERS and required reviews | Bring the right decision-makers in |
| Enforce policy | Branch protection and rulesets | Prevent noncompliant changes |
| Moderate behavior | Discussion permissions and moderation tools | Protect community health |

This is a cleaner structure than anything in the current project brief and is
sourced to real GitHub docs (the original has footnote links to
docs.github.com for every row).

**The source of the guardrail phrase already in the brief** (gpt.comms): *"Not
every guideline should become a hard gate. Otherwise, the community becomes a
DMV operated through YAML."* This is the actual coinage, not a paraphrase — cite
it directly if the module wants a sourced quote instead of an unattributed
guardrail.

**CODEOWNERS broadened past code** (gpt.comms), the full list: product
principles, pricing rules, analytics schemas, AI system prompts, safety
policies, customer-facing language, API contracts, accessibility standards,
legal/compliance documentation. Good proof-of-translation material — "code
owner" sounds narrow, isn't.

**Concrete governance automations** (claude.comms), five of them, each with a
one-line description and one has a working YAML skeleton:

- Vocabulary check on every PR touching product-context files
- Evidence-link enforcement — a PR can't merge into `decisions/` without a
  linked evidence issue
- Stale-idea sweep — anything labeled `exploring` with 60 days of no activity
  gets auto-flagged for Park or Kill
- Stakeholder ping — merging a decision-record change notifies whoever's listed
  in that file's frontmatter
- Needs-info auto-label — an Action scans for missing narrative sections, not
  just empty form fields

Evidence-link Action skeleton, real and runnable:

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

**Four failure modes this whole play protects against** (claude.comms) — good
candidate for a single "why bother" slide:

- Silent strategy drift — nobody notices `vision.md` got quietly rewritten
- Backlog pollution — "make it faster" becomes a ticket before anyone asks for
  evidence
- Zombie ideas — killed-in-spirit ideas never get killed on paper, get re-pitched
- Governance theater — the failure mode of the whole doc: rules nobody enforces
  are just a wiki page people ignore under deadline pressure

---

## Community

**The line that is nearly your project's own thesis, verbatim** (gpt.comms):
*"'GitHub for Product Managers' is not just repository literacy. It is designing
a participation system."*

**The five-primitive breakdown** (gpt.comms): *"Discussions create the community
conversation. Projects make participation and progress visible. Issues turn
promising conversations into structured investigation or work. Pull requests
submit changes for review. Rules and automation shape what happens next."*

**The best single diagram in the whole set** (gpt.comms) — the full community
operating loop:

```
Community conversation
→ Structured opportunity submission
→ Automated completeness and policy checks
→ Transparent triage in GitHub Projects
→ Community feedback and evidence gathering
→ Named owner and human decision
→ Experiment, Issue, pull request, or rejection
→ Required reviews and governance checks
→ Release and outcome measurement
→ Decision and learning shared with the community
```

Strong candidate for the closing synthesis slide of the entire webinar, not just
the community module — it's the only diagram that actually stitches all five
plays into one picture.

**The punchy contrast line** (gpt.comms): *"A board without conversation is just
public administration."* Good pairing with the Google-overview straw man in the
cold open.

**A healthy community needs more than intake automation** (gpt.comms) — the
full list: clear behavioral standards, named moderators, transparent decision
criteria, visible disposition of submissions, respectful rejection explanations,
paths for appeal or reconsideration, recognition for meaningful contributions,
protection against domination by the loudest participants.

---

## Cold open / straw-man material (Google AI Overview)

The Google doc is deliberately the outside-in take — don't pull pillar content
from it, use it only as the "here's what people think this is" opener.

Direct quote of the flattened take: *"GitHub Projects & Issues: Act as a
built-in alternative to Jira or Trello... Pull Requests: track which features
are ready for user acceptance testing (UAT) or blocked by code reviews."*

The vocabulary section it offers stops at: Repository, Branch, Commit, Merge.
That shallowness is the point — use it to show exactly the flattened
"repo-literacy" version the webinar is arguing against.

One genuinely fun detail: Dean's own `deanpeters/product-manager-prompts` repo
(108 GenAI prompts for PM workflows) appears as one of Google's top-cited
resources when it answers "github for product managers." Usable beat: *"Even
Google's AI already points people at my own repo when they ask this question,
and it still gets the whole picture wrong."*

Also notes GitHub Copilot "Plan Mode" as a real, current (2026) feature PMs are
adopting to clarify requirements and test MVP scope before development — worth
checking whether this belongs in the context-setting or experimentation module
as a live, current-year feature namedrop.

---

## Leftover material — doesn't map cleanly to the five plays

**Investment Horizon Framework** (both Gemini docs carry this, filed under
"Portfolio & Investments" / a sixth pillar):

| Investment Category | Tag | Focus | Target Allocation |
|---|---|---|---|
| Core Innovation | `type: strategic-bet` | New revenue, market expansion | ~50% |
| Product Health & Delight | `type: ux-polish` | Retention, accessibility | ~20% |
| Technical Debt & Scale | `type: architecture` | Performance, security, infra | ~20% |
| Operational Maintenance | `type: bug-fix` | Customer friction, escalations | ~10% |

Real and well-sourced, but it's capital-allocation content that doesn't belong to
context, comms, experimentation, governance, or community cleanly. Candidate for
folding a line into governance ("decision integrity over resourcing, not just
over content") or cutting entirely. Flagged in the README as an open question for
Dean.
