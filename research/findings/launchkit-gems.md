# Launchkit Gems — from `productside-launchkit`

Source repo: `~/Code/Productside/productside-launchkit`, Productside's private
internal manual for how it runs its own GitHub organization. This is a different
kind of source than the web research or the YouTube transcripts: it is not
someone's theory about GitHub governance, it is a **working system Dean already
built and is running**, with real file names, real automation, and real scar
tissue in `HANDOFF.md`'s "traps that have already bitten" section.

Two things worth flagging before the gems themselves.

**This repo already contains a full draft webinar.**
`drafts/webinar-2026-09-02-github-for-product-teams.md`, dated for the exact
webinar deadline named in `HANDOFF.md` ("the one deadline"). It is titled
"Setting Up a GitHub Presence for a Company That Doesn't Build Software" and
covers nine modules: the category trap, the three-layer repo anatomy, nothing-
born-public, licensing, where legal docs live, secrets, automation guardrails,
published commitments, and mistakes to skip. **This may be the same webinar as
the "Five Plays Beyond the Backlog" one this session has been outlining, a
companion session, or an earlier draft that got superseded** — worth confirming
with Dean directly rather than assuming. Either way, most of its content is
usable raw material, not just inspiration, and is called out below module by
module.

**This repo is itself the best possible case study for the "governance" play.**
Everything the AI research docs describe hypothetically (CODEOWNERS, branch
protection, automated guardrails, blocked-term checks) exists here as real,
running code with real filenames. If the webinar wants one concrete "here's a
company that actually did this" example instead of a hypothetical, this is it —
though it would need Productside-specific details scrubbed (see the
"needs generalizing" notes throughout).

---

## The category trap — Productside's sharpest, most generalizable idea

From `docs/02-governance/02-09-positioning-licensing-and-terms.md` and Module 1
of the draft webinar:

> "If Productside's published materials are described as 'code' or 'software,'
> a client's legal team can reasonably conclude that Productside is a software
> vendor. When that happens, a services agreement starts attracting software
> obligations: security questionnaires that run dozens of pages, vulnerability
> disclosure commitments, uptime and support expectations, and warranty terms
> that make no sense for a workshop handout."

This is Dean's own manufacturer/service example, already worked out in
Productside's specific case (training/advisory firm vs. software vendor). The
underlying rule generalizes cleanly to any audience, not just training
companies:

**Your GitHub repo's vocabulary and license type are a legal signal about what
kind of company you are, and that signal can attach obligations your contracts
never intended.** A manufacturer publishing firmware or an SDK on GitHub *is* a
software supplier for that repo and needs a real software license with the
warranty/liability terms that go with it. A services firm, consultancy, or
agency publishing prompts, templates, or worksheets is not, and a software
license (MIT, Apache) puts that categorization in writing, in a file at the top
of a public repo, undermining the exact argument they'd want to make later. The
generalizable lesson isn't "pick Creative Commons" — it's "figure out which
category of company you actually are for *this specific repo*, then choose the
license and vocabulary that matches it, instead of copying whatever's popular
on GitHub."

The vocabulary substitution table (02-09 / Module 1), directly reusable as a
slide or exercise:

| Term to avoid | Use instead |
|---|---|
| code, codebase | materials, resources, digital takeaways, files |
| software | *(omit, or say "the platform" when you mean GitHub itself)* |
| scripts | prompts, skills, templates |
| your developer | whoever set up the tool, your technical contact |
| app, application | tool |
| deliverable, product | takeaway, example, material |

Three exceptions worth keeping even in a generic version, because they preempt
the obvious pushback: `CODE_OF_CONDUCT.md`/`CODEOWNERS` are GitHub-mandated
filenames, not category claims; naming a vendor's product ("Claude Code," "AWS
Lambda") isn't a claim about what *you* sell; and prohibitions that name code
("never put a secret in code") describe what you forbid, not what you build.

**The exercise from the draft webinar is genuinely usable as-is**: search your
own public files for code/software/script/app/developer/deliverable, and for
each hit ask "does this describe what we sell, or what we forbid?" Fix the
first kind, keep the second. Good candidate for an interactive moment in the
live session.

**For the generic launchkit:** strip the training/workshop framing and the
"workbook" analogy (Productside-specific), keep the vocabulary table and the
generalized manufacturer/service framing above, and consider adding a second
worked example alongside Productside's (a hardware company, an agency) so the
pattern reads as universal rather than borrowed from one company's fix.

---

## The three-layer repo anatomy — Context, Contract, Constitution

From `docs/01-foundations/01-04-repo-anatomy.md` and Module 2 of the draft
webinar. This is a cleaner, more opinionated version of the "Context /
Communications / Governance" structure than anything in the AI research docs,
because it comes with an explicit precedence rule:

> "The Constitution outranks the Contract, which outranks the Context."

| Layer | File | Answers |
|---|---|---|
| Context | `README.md` + docs | What is this and why does it exist? |
| Contract | `CLAUDE.md` / `AGENTS.md` | How should an AI assistant work here? |
| Constitution | `CONSTITUTION.md` | What can never be overridden, by anyone? |

The reasoning for why this needs three files instead of one is sharp and
quotable: *"a rule that lives only in a README is a suggestion."* Good
constitutional rules, per the doc, are "short, absolute, and explain nothing" —
explanation belongs in the Contract or docs, the Constitution is just the floor.
This is a genuinely good teaching device: show a bad constitutional rule
("secrets should generally be avoided when possible") next to a good one
("never expose secrets, no exceptions") and let the room feel the difference.

**Real templates exist and are copy-paste ready**: `templates/CLAUDE.sample.md`
and `templates/CONSTITUTION.sample.md`, both already genericized with
`[repo-name]` placeholders. These could ship directly as webinar takeaways
rather than being rebuilt from scratch.

**For the generic launchkit:** this module needs almost no stripping. It's
already close to company-agnostic. The main edit is generalizing "Productside"
references inside the sample templates.

---

## Nothing is born public — the graduation model

From `docs/01-foundations/01-05-choosing-where-work-lives.md` and Module 3 of
the draft webinar. The AWS origin-story analogy is a strong, reusable hook:

> "Amazon did not build AWS as a product for the outside world; it built
> infrastructure for itself, and the pieces that proved themselves graduated
> into products."

The graduation sequence — built internally, proven by reuse, copied out (never
flipped), cleaned of names/data, approved, published — is a concrete answer to
a question the AI research docs raise but never resolve: how does something
actually earn its way from private to public? The explicit reason to copy
rather than flip visibility is worth keeping word for word: *"its entire
history comes along with it, and history contains things the current files do
not show."*

Side benefit worth surfacing as its own line: *"everything public is provably
something you actually use. 'We use this ourselves' becomes a selection
criterion instead of a claim."* That's a genuinely good marketing point dressed
up as a governance rule.

**What never graduates**, regardless of company type, generalizes well: work
product created *for* a specific client (Foreground IP, vests in the client),
material the client brought (Client IP, never yours to begin with), and
anything under a paid-participant license stricter than what you'd grant the
public. Any services business has some version of this trap.

**For the generic launchkit:** the "Training Deliverables" category and the
SharePoint-vs-Project file-type table are Productside-specific (they assume a
training business with named paying participants). The generalized version
needs a more universal three-way split: what you built for yourself, what you
built for a specific client, and what's safe to show a stranger.

---

## The licensing decision, generalized

From `docs/02-governance/02-09-positioning-licensing-and-terms.md`,
`HANDOFF.md`'s "decisions already made," and Module 4 of the draft webinar.

The most useful reframe for a general audience is the myth this section opens
with: *"ask a room of PMs 'what does a repository with no license mean?' and
most say 'free to use.' It means the opposite."* No license means all rights
reserved. That's a strong, surprising opener for a licensing segment regardless
of audience.

The CC-vs-MIT/Apache distinction is the direct payoff of the category trap
above: MIT and Apache are *software* licenses, Creative Commons licenses are
*content* licenses, and the choice itself is a public, written statement about
what kind of company you are. Reading a CC license name as three separable
permissions (BY = must credit you, NC = a competitor can't resell training
built on it, ND = no modified versions circulate under your name) is a clean,
teachable structure.

Two details HANDOFF.md and the doc both flag as easy to get wrong, worth
keeping as a "gotcha" beat in any version: the license only governs strangers
on the internet, not the people already under a signed contract with you (so
"doesn't NoDerivatives stop our own clients from adapting this?" has a clean
answer: no, they're not operating under the repo license at all) — and a
content license grants **zero** trademark rights, so someone can legally share
your worksheet with attribution and still have no right to put your logo on
anything.

**Precedence chain**, worth keeping as a single memorable line: *"signed
agreements > live website > repository license > repository docs."*

**For the generic launchkit:** CC BY-NC-ND is Productside's specific answer for
a training business monetizing via lead-gen and paid workshops. A manufacturer
or a software company will land somewhere else entirely (a real software
license, a proprietary license, or an open-source license depending on
business model). The generalized version should present the decision *logic*
(what category are you, what do you actually want to permit) rather than
Productside's specific answer, and maybe show two or three different companies
landing on different licenses through the same logic — this is the natural home
for Dean's manufacturer example if he wants to make it concrete.

---

## The Content Guard — a real, running answer to "no customer names"

This is the most directly reusable material in the whole repo, and it's the
exact real-world version of Dean's second example (a "no customer names" rule
enforced as an actual GitHub check-in gate). From
`docs/02-governance/02-08-repository-operations.md`,
`templates/content-guard.sample.yml`, and `templates/pre-commit.sample`.

It runs in two places, and the doc is explicit about why both matter:

> "The local hook is the one that matters most. Once material is committed and
> pushed, deleting it does not remove it from the history. Catching it before
> the commit exists is the only clean stop."

Four checks, real and running, not hypothetical:

| Check | Catches |
|---|---|
| Blocked terms | Client and customer names |
| SharePoint file types | `.docx`, `.pptx`, `.xlsx`, `.pdf`, `.msg`, `.eml` |
| Oversized files | Anything over 5MB, which slows every future clone forever |
| Credential patterns | Recognizable shapes of API keys and private keys (`sk-`, `ghp_`, `AKIA`, PEM headers, etc.) |

**The blocklist paradox is the single best "gotcha" in this entire repo**, and
it's a real trap Dean already avoided:

> "A list of your clients' names is itself a client list. Commit it to a public
> repository to power your blocklist and you have leaked precisely what the
> blocklist existed to protect."

The fix: the blocked-terms list never lives in the repo. It lives in a GitHub
organization secret (`BLOCKED_TERMS`) for the CI check, and a local file outside
every repo (`~/.config/productside/blocked-terms.txt`) for the pre-commit hook.
A sample file exists with placeholder names for exactly this reason.

**And the honesty clause is worth keeping in any version**, because it's the
difference between a governance module that builds trust and one that oversells
itself: *"A guard that is oversold is worse than no guard, because people stop
checking."* It explicitly will not catch a client referred to by description
("the big aerospace account"), a logo inside a screenshot, a name nobody added
to the list, anything already in history, or someone running
`git commit --no-verify`.

This directly upgrades the "governance automation" section of the web-research
gems (`web-search-gems.md`) from hypothetical YAML skeletons to an actual
working implementation Dean can screenshot or even live-demo.

**For the generic launchkit:** the workflow and pre-commit script are already
close to drop-in generic (they take the client-name list from an external
secret, not a hardcoded value). Mainly needs the Productside-specific comments
trimmed and maybe a lighter "here's the five-minute version" excerpt for a
webinar audience that won't want to read a full bash script live.

---

## Naming conventions as brand governance

From `docs/02-governance/02-04-naming-conventions.md`. Simple, visual, and
works well as a quick teaching moment: `Productside-Title-Case` signals
public-or-public-capable, `productside-lowercase` signals private-only, and the
rule of thumb is stated as a single memorable sentence:

> "Name it for the stranger who finds it six months from now."

Good complementary detail: repo-type prefixes (`client-[name]-[project]`,
`workshop-[topic]-[date]`, `internal-[app-name]`, `lab-[experiment-name]`) give
a scannable taxonomy for organizing an org's repos by purpose, not just by
visibility. Generalizes to literally any company with more than a handful of
repos.

---

## The checklists — ready-made takeaways

`docs/03-operations/03-01-admin-checklist.md`,
`03-02-publication-checklist.md`, and `03-03-project-checklist.md` are three
short, concrete, checkbox-formatted documents: org setup, going-public review,
and project-wrap review. These are exactly the kind of thing an audience wants
to leave a webinar holding. Each one's already close to generic — the
publication checklist in particular ("no secrets," "no customer data," "the
README is accurate," "another reviewer has checked it") barely mentions
Productside by name.

The golden rule on the publication checklist is a strong closing line for a
governance module regardless of audience: *"You can go from private to public.
You cannot unpublish what the world has already seen."*

---

## Mistakes to skip — the most human material in the repo

From `HANDOFF.md`'s "Traps that have already bitten" and Module 9 of the draft
webinar. This is real, dated, and specific — not a hypothetical failure mode,
an actual thing that happened at Productside:

- **Two clones of the same repo** — a session worked for hours in a stale
  clone while the real repo moved four commits ahead, producing duplicated
  work and a false report that a chapter didn't exist.
- **A stale instruction file gets followed** — an old `CLAUDE.md` told AI
  sessions to build a website crawler Productside never intended to build.
  Fixing the visible README without fixing the instruction file meant the
  crawler kept coming back.
- **Claiming a control exists before it does** — Dean described an automated
  client-name blocker to the COO in the present tense before it was actually
  built, while she was assessing legal exposure. The rule that came out of it
  is genuinely great, quotable advice for any audience: *"say 'designed, not
  yet built, here is the date.' That sentence costs nothing and protects
  everything."*
- **A blocklist of client names is itself a client list** — same trap as
  above, independently rediscovered and worth the repetition.

These read as confessions, not lessons, and that's exactly what makes them
land. Good closing-module material for the webinar — audiences remember "here's
what actually went wrong at a real company" far better than a generic listicle
of best practices.

---

## Open threads for Dean

1. **Is this the same webinar?** The draft at
   `drafts/webinar-2026-09-02-github-for-product-teams.md` shares a date with
   `HANDOFF.md`'s "the one deadline" and covers overlapping ground (CODEOWNERS,
   branch protection, guardrail automation) with the "Five Plays Beyond the
   Backlog" outline this session has been building. Worth settling directly:
   one webinar, two webinars, or does this become the seed of the future
   `Productside-GitHub-Launchkit` public repo instead, on its own timeline?
2. **Audience mismatch.** The launchkit's draft webinar is written for
   "product managers, marketers, and consultants at companies that sell
   services" — narrower than the "Five Plays" webinar's general Product
   Manager audience. If these merge, the category-trap/licensing material
   would need to become one module inside the five-play structure rather than
   its own nine-module show.
3. **The Content Guard is a genuine gift to the governance module** regardless
   of how the above gets resolved — it's the one piece of real, running
   automation in either research pile, and it directly answers Dean's own
   "no customer names as a check-in check" example.
4. **Generalizing checklist:** before anything here goes into
   `Productside-GitHub-Launchkit`, strip: 280 Group LLC / Productside entity
   references, the SharePoint-vs-Project file split (assumes Productside's own
   tool stack), the "student/learner/participant" language (assumes a training
   business), and the specific CC BY-NC-ND choice (keep the decision logic,
   not the answer).
