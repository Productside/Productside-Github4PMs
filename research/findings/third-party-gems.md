# Third-Party Gems — Aakash Gupta/Shubham Saboo, the PM GitHub Starter Kit, and Department of Product

Three sources, all published by other people, none of them Productside's own
research. Two carry real usage restrictions worth flagging up front, in the
same spirit as Productside's own third-party-materials rule
(`productside-launchkit` → `docs/02-governance/02-06-third-party-materials-and-attribution.md`:
*"if you did not make it, confirm you have the right to share it"*). Applying
that standard here:

- The Aakash Gupta / Shubham Saboo Substack piece is marked **PAID** and the
  version Dean supplied is the paywalled preview (it cuts off mid-article with
  a "keep reading with a 7-day free trial" wall). Fine to mine for ideas and
  structure. **Do not reproduce its infographics, exact wording, or full
  content in any public Productside material** — treat it as inspiration and
  attribution-worthy source, not copy-paste stock.
- The linked GitHub repo, `pm-github-starter-kit`, states directly in its own
  README: **"This resource is restricted to Product Growth paid subscribers
  only and should not be redistributed."** Its actual template files weren't
  retrievable (GitHub blocks automated scraping and the raw README itself
  carries the restriction notice), so what's below is limited to the concepts
  the README exposes publicly, not the templates themselves. **Treat the
  templates as off-limits; build Productside's own equivalents from scratch if
  the webinar wants to hand out something similar.**
- The Department of Product article is a free public blog post — no
  restriction, safe to reference and quote normally.

---

## From the Aakash Gupta / Shubham Saboo piece ("GitHub for PMs: Version Control for Everything You Build With AI")

This is a meaningfully different angle from every other source gathered so
far. The web research and YouTube transcripts frame GitHub as infrastructure
for *team* product management (roadmaps, decisions, customer evidence). This
piece frames GitHub as infrastructure for **a single PM's personal AI
operating system** — CLAUDE.md files, reusable skills, eval criteria,
autoresearch configs. It's the most current-dated source in the whole pile
(June 2026) and the one most directly aligned with this webinar's actual
title ("Five Plays Beyond the Backlog" for *AI* Product Management).

**The cold-open hook, sharper than anything gathered elsewhere**: *"Your skills
have versions. Your CLAUDE.md changes every week. Your eval criteria evolve...
When you don't track your AI infrastructure, a single word shift can
completely break your OS's behavior."* This names a pain the audience is
almost certainly already living through if they use Claude Code or similar
tools day to day — arguably a better hook than the Google-Overview straw man,
because it's a real problem rather than a flattened misconception.

**The "Without Git / With GitHub" comparison**, more concrete and punchier than
the developer-vs-PM tables from the AI research docs:

| Without Git | With GitHub |
|---|---|
| Laptop dies | Clone in 2 min |
| Broke something | Revert in 1 cmd |
| Files overwrite | Branches & merge |
| Work stays private | Public portfolio |
| No backup plan | Always recoverable |

**Three repos, one PM** — the piece's central framework:

| Repo | Visibility | Contains |
|---|---|---|
| Workspace | Private | CLAUDE.md with personal context, skills folder, autoresearch configs, project drafts |
| Shared Tools | Public/team | Skills stripped of personal context, prompt templates, starter configs others can fork |
| Projects | Per-initiative, private | PLANNING.md, eval scoring criteria, the code itself — one repo per initiative, archived when done |

The line that matters most for a governance module: *"The core difference from
your private workspace is simple: shared tools have all personal and
company-specific context completely stripped out."* That's the same discipline
Productside's own launchkit enforces on client names, just applied to a
different asset class (personal AI context instead of customer data) —
independent confirmation that "strip it before you share it" is the load-
bearing rule regardless of what's being shared.

**Security note, stated twice in the piece, nearly word-for-word matching
Productside's own Content Guard philosophy** (three unrelated sources now
landing on the same practice — web research's GitHub Actions guards, the
launchkit's real pre-commit hook, and this):

> "Do not blindly push your PM workspace to GitHub. A private repo is not a
> privacy strategy. Before your first push, you must completely remove API
> keys, .env files, actual customer names, transcripts, internal strategy docs
> you are not allowed to upload, HR or performance feedback, raw Slack
> exports, and screenshots with sensitive information. Use .gitignore first.
> Then run a secret scan. Then push."

**The PM Artifact Workflow — the single most demo-ready asset across every
source gathered so far**, because it pairs each git mechanic with the actual
natural-language sentence a PM types into Claude Code instead of git syntax:

| Step | What it does | What you actually say |
|---|---|---|
| Pull | Get teammates' overnight changes | "Pull the latest changes" |
| Branch | Your own copy, isolated | "Create a branch called improve/prd-reviewer-v7" |
| Edit | Make the actual change | *(you just make the changes)* |
| Commit | Snapshot with a message | "Commit with message: add behavior contract check to PRD reviewer" |
| Push | Upload to GitHub | "Push my changes" |
| PR | Ask for review before it's official | "Open a pull request" |
| Merge | Reviewer approves, you click merge | *(reviewer approves, you click merge)* |

This is the concrete, current-year answer to the audience guardrail already in
the brief ("nobody needs to memorize git syntax") — not by avoiding git
entirely, but by showing the AI agent as the translation layer. Strong
candidate for the actual live-demo script if Phase 0 confirms one; better than
building a demo from scratch, and more current than Anne Thomas's 2020 GitHub-
native UI demo.

**Four version-control workflows the piece calls out as things "that only work
in Git"** — real commands, genuinely AI-PM-specific, good advanced/bonus
material:

| Workflow | Command | What it solves |
|---|---|---|
| Skill Versioning & Rollback | `git checkout [hash] -- skills/prd-reviewer.md` | A tweaked skill got worse; restore the previous version in one command |
| CLAUDE.md Pruning | `git diff HEAD~20 CLAUDE.md` | Instructions drifted over 20 sessions; see exactly what changed |
| Autoresearch Experiment Log | `git log --oneline skills/prd-reviewer/` | The Karpathy-loop runs 100 iterations overnight; no spreadsheet needed to track them |
| Eval Criteria Versioning | `git log evals/chatbot-criteria.md` | A score dropped from 0.82 to 0.71; find which criteria change or model swap caused it |

**GitHub profile setup as career/portfolio material** — a genuinely new angle
none of the other sources touch: use your real name, a profile README as your
homepage, pin 2-3 repos so visitors know what you build, install Cursor or
Claude Code so the tool can push directly. Ties naturally to the "What to
Build" section's week-by-week ramp (Week 1-2: fork the starter kit, push a
CLAUDE.md; Month 1: build a first PM automation tool; Month 2: strip a skill
and publish it to a shared repo; Month 3: launch a per-initiative repo with
PLANNING.md and eval criteria).

**Real, name-droppable proof points** that the "community" play is already
happening in this exact niche: Garry Tan's `gstack` (23 specialist skills),
Pawel Huryn's `pm-skills` (100+ skills across 8 plugins, 2.5k stars), Carl
Vellotti's `claude-code-pm-course`. Worth checking current star counts before
using live, since these move fast and the piece is dated June 2026.

---

## From `pm-github-starter-kit` (concept only — see restriction note above)

What's usable is the *idea* that a PM's GitHub presence functions as a hiring
signal, not the actual kit contents.

The stat quoted in its own overview, worth treating as a claim to attribute
rather than a verified fact: *"24% of PM candidates have a GitHub. The latest
PMs I placed at OpenAI, Anthropic, and Meta AI all had one."* Strong hook for
a "why bother" opener if the webinar wants to make a career-capital argument,
not just a productivity one.

Principles worth restating in Productside's own words rather than reusing
directly: one substantial, real project beats several shallow ones; documented
design decisions and outcomes matter more than code; recent consistent
activity reads better than accumulated stars; and the anti-patterns are
genuinely useful as a "don't do this" list — unmaintained repos, shallow
copy-paste projects, artificially inflated contribution metrics, letting AI do
all the work without understanding the product decisions, and abandoning a
project without further iteration.

---

## From Department of Product's "GitHub Explained for Product Managers"

The most traditional, 101-level piece of the three — free, well-structured,
and a useful contrast point precisely because it's exactly the kind of content
this webinar is arguing against being: solid repo-literacy, zero PM-specific
framing beyond a closing paragraph.

**Best raw teaching material for absolute beginners**, if the show ever wants
a simpler on-ramp before the Five Plays framing: the codebase as "a tree
trunk" with features as temporary branches, and merge conflicts as "trying to
untangle earphones stuck in your bag for 3 months — horrible work, but
necessary." Both are more vivid than any analogy pulled from the web-research
docs.

**The clearest, simplest end-to-end worked example across every source
gathered in this whole project**: an engineer clones the repo, changes a
button's CSS from red to blue, commits with a descriptive message, pushes,
opens a PR, gets reviewed, merges, and the change deploys through CI. Eight
steps, one trivial change, nothing hypothetical. If the webinar wants the
literal first thing an audience watches happen on screen, before any PM-
specific material lands on top of it, this is the simplest version anyone has
built.

**Three practical takeaways for PMs**, useful mainly as a baseline to contrast
against the Five Plays' more ambitious framing: understand your team's
branching strategy so you can empathize when conflicts slow things down; audit
your release process and flag it if it eats "2+ days and 4 engineers"; push
for dedicated DevOps investment to automate developer workflows. These are
solid but generic — worth noting explicitly that this is close to the ceiling
of what most public "GitHub for PMs" content offers, which is exactly the gap
the Five Plays webinar is positioned to fill.

---

## Open threads for Dean

1. **Redistribution risk.** Two of these three sources carry explicit "don't
   redistribute" language. Before anything from the Aakash Gupta piece or the
   starter kit shows up in a slide, a takeaway PDF, or (especially) the future
   public `Productside-GitHub-Launchkit`, it needs to be rebuilt in
   Productside's own words and examples — the concepts are fair game, the
   actual templates and copy are not. This is Productside's own 02-06 rule
   applied to material Dean is now on the receiving end of, not just the
   giving end.
2. **The AI-native angle is the freshest material in any research pile so
   far.** The Three Repos framework, the PM Artifact Workflow's natural-
   language mapping, and the four git-only workflows for skills/CLAUDE.md/
   evals are all more current and more specific to this webinar's actual
   premise than the general "GitHub for product teams" framing in the other
   sources. Worth deciding whether one full module gets built around
   "GitHub as your personal AI operating system" using this as the anchor, or
   whether it stays a seasoning folded into the Context and Experimentation
   plays.
3. **Redundant validation, not new information:** the secrets/scrub-before-
   push warning here is the third independent source (after the web research's
   GitHub Actions guards and the launchkit's real Content Guard) to land on
   the identical rule. Worth a single slide that shows all three side by side
   as proof this isn't Productside's idiosyncratic caution — it's universal
   practice wherever people put AI context or work product into GitHub.
4. **The Department of Product piece is useful mainly as a contrast, not a
   source of new content** — it's solid 101 material but doesn't go beyond
   repo literacy, reinforcing rather than challenging the brief's central
   thesis.
