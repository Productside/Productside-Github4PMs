# Run of Show — Beyond the Backlog: Five GitHub Plays for Product Teams

**Wednesday, September 2, 2026 · 1:00–2:00 PM ET / 10:00–11:00 AM PT**

**Dean Peters** — narrates, frames each play, contributes, reviews and merges. **On a Mac.**
**Kenny Kranseler** — drives. Builds live, asks the question the audience is thinking, gets stuck on camera and gets unstuck. **On Windows.**

Live and hands-on. Mistakes stay in.

> **Slot length unconfirmed.** Written for 60 minutes. Sections marked **[45-min cut]** go if it's 45.

---

## The spine: one story, not five demos

This is the change that makes the show work. The five plays are **five moments in a single continuous story**, not five separate segments. Kenny has a real problem — he needs to build shared understanding of a domain — and each play is the next thing that happens to him.

1. Kenny needs a home for what he's learning about a domain → **Context**
2. Dean joins him in it, and they build the understanding together → **Communications**
3. Kenny needs market evidence, so he borrows Productside's intelligence skills → **Confidence**
4. Some of what he's collecting must never leak → **Constitution**
5. He finds a gap in the shared library and contributes back → **Community**

Nothing Kenny builds ever goes public. That is deliberate and worth saying out loud: **the session never violates its own "start private" rule.**

---

## Two repos, two jobs

| | **Kenny's domain research** | **Productside Market Intelligence** |
|---|---|---|
| Visibility | **Private.** Stays private. | **Public** (flipped before the show) |
| Owner | Kenny | Productside org |
| Purpose | What his team believes about one domain | A shared library of 22 skills + 22 prompts |
| Kenny's access | Owner | **Collaborator** — can push a branch, cannot merge |
| Dean's access | Collaborator, contributes live | Reviews and merges |
| Local path | `C:\Users\...\Documents\<domain>-research` | Cloned to his machine in Play 3, used standalone |

**Domain: TBD.** Something like "PM for Manufacturing." Must be a domain, never a customer.

---

## Kenny clones the library, once

Kenny **clones the market intelligence repo to his own machine** and works from it standalone. One acquisition step, at the start of Play 3, and it never changes.

That matters mechanically: **a pull request needs a branch, and a branch needs a clone.** If Kenny only ever installed the skills, Play 5 would have no branch to push and no way to contribute. The clone is what makes the ending possible, so it happens early and openly rather than appearing as a surprise step at 0:40.

It also matches how a product manager would really live with a borrowed library: a folder on your machine you can read, run, and eventually improve.

---

> Diagrams for the architecture, the tool ladder, the contribution loop, and the story arc are in [`diagrams.md`](diagrams.md).

## Two machines, on purpose

Kenny is on Windows, Dean is on a Mac. **Do not hide this — narrate it.** Kenny's path is `C:\Users\...\Documents\`, Dean's is `~/Documents/`, and the repo does not care. That is exactly what a real product team looks like, and it quietly kills the "I'd need the same setup as my engineers" objection.

---

## The tool handoff

**Claude Desktop** works from the local folder — reads what's there, writes research into it. No git, no auth, nothing to break.

**Claude Code** does the git: install the plugin, run the sweep, commit, push, branch, open the PR.

**Kenny never types a git command at either stage.** He says sentences. The only command line in the show is Dean's, at 0:10, doing history.

---

## Timing at a glance

> **Retimed 2026-08-24 to fit the two polls and the fixed open.** The previous version started the clock at the cold open and never accounted for the hold slide, speakers, housekeeping, or the agenda — about five minutes of real time. The two polls cost four more. **The plays absorbed the difference: 35 minutes, down from 41.** If that is too tight, the honest fixes are a 75-minute slot or cutting a play. Not shaving Play 5.

| Time | Segment | Driver |
|---|---|---|
| 0:00–0:02 | Hold and title, people arriving | — |
| 0:02–0:05 | Cold open | Dean |
| 0:05–0:08 | Speakers, housekeeping, agenda | Both |
| 0:08–0:10 | **Poll 1** · which one hurts most right now | Kenny reads results |
| 0:10–0:12 | How git got here | Dean's terminal |
| 0:12–0:13 | Rules of the show; Kenny takes the screen | Dean |
| 0:13–0:20 | **Play 1 — Context** · private repo, cloned, Claude Desktop | Kenny |
| 0:20–0:26 | **Play 2 — Communications** · Dean joins the repo | Both |
| 0:26–0:34 | **Play 3 — Confidence** · clone the library, run a sweep | Kenny, in Claude Code |
| 0:34–0:39 | **Play 4 — Constitution** · guardrails on what he just collected | Kenny + Dean |
| 0:39–0:48 | **Play 5 — Community** · branch, PR, guard, merge | Kenny opens, Dean merges |
| 0:48–0:50 | What GitHub is bad at | Dean |
| 0:50–0:52 | Close | Dean |
| 0:52–0:54 | **Poll 2** · starting today, what will you do differently | Kenny reads results |
| 0:54–1:00 | Q&A | Kenny moderates |

Plays 1 and 3 are the designated time donors. Play 5 is not — it is the ending.

**The two polls share one taxonomy: the five plays.** Poll 1 names five problems before the agenda names five answers. Poll 2 asks the same five back as commitments. Read Poll 1's winner out loud and say which play covers it; if one option runs away, spend an extra minute there and take it from a play that landed lower. **Question and option text: [`polls.md`](polls.md).**

---

## 0:02–0:05 · Cold open

**On screen:** nothing. Two faces.

**The loss, not the tool.** Your best thinking dies in three places: a Notion doc nobody reopens, a Slack thread nobody can find, and a deck rebuilt from scratch every quarter. Meanwhile every AI tool you touch starts from zero, because nothing you know lives anywhere it can find it.

**The straw man, named.** Search "GitHub for product managers" and you get a vocabulary lesson — repo, branch, commit, merge — and a suggestion that it's an alternative to Jira. Wrong answer to the wrong question.

**The turn.** GitHub isn't Jira with a different logo. Think of it as part digital vault, part publishing platform, part collaboration space, and part institutional memory.

**The promise, flatly.** In the next fifty minutes Kenny goes from nothing to a private research repo his team shares, evidence collected into it by AI, and a merged contribution to a public Productside library. Built live. If it breaks, you'll watch it break.

---

## 0:10–0:12 · How git got here

**Dean's terminal. Dean's hands. Nobody is expected to repeat any of this** — say that before the first command, or half the audience starts panicking about keeping up.

The only command line in the show. It exists to earn one argument: **GitHub outgrew what it was built for, and product managers are the ones who benefit.**

1. **Git tracked versions of files.** 2005, built for source code. Dean commits, edits, commits again, shows the diff. *"Two versions of a file and a note about why. That is the entire original idea."*
2. **Then teams needed rules for working together** — gitflow and its cousins. Branches, releases, who merges what. **None of it was in the original design.** Teams invented process because the tool left room.
3. **Then GitHub put it on the web** and added what isn't version control at all: issues, discussions, reviews, permissions. The center of gravity moved from *tracking files* to *coordinating people.*
4. **And nobody told product managers.** The coordination layer doesn't care whether the files underneath are source code. It works the same on research notes, a decision record, or a competitive brief.

**The handoff line:** every one of those steps was somebody discovering the tool did more than it was built to do. We're just the next ones to notice.

**Close the terminal, visibly.** *"That's the last command line you'll see today."*

**[45-min cut]** Two beats, sixty seconds, no terminal, spoken over an empty GitHub page.

---

## 0:12–0:13 · Rules of the show

**Kenny shares screen. Empty GitHub account. Windows machine, and say so.**

1. **Nobody is being asked to become a developer.** Kenny says sentences; an AI assistant does the git part.
2. **Kenny is on Windows, Dean is on a Mac.** Different paths, same repo. That's a real team.
3. **Everything Kenny builds today stays private.** The one public thing is Productside's, and it was published deliberately, in advance, with a review.

**Kenny's job here:** ask the question the audience has. *"I'm not shipping code. What would I even put in a repo?"* Dean's answer is the thesis: you're shipping decisions and understanding, and those have a worse retention rate than code.

---

## 0:13–0:20 · Play 1 — Context

**Kenny's problem:** he's been asked to get smart on a domain — call it PM for Manufacturing — and everything he learns is currently scattered across tabs, notes, and one increasingly cursed document.

**What he builds:**
1. **New repo. Private.** Named for the domain. Not "docs," not "notes."
2. A `README.md` saying what this domain is and why the team cares. Thirty seconds, not a masterpiece.
3. Stub files: `what-we-know.md`, `open-questions.md`, `glossary.md`, `sources.md`. **Empty headings are fine and honest.**
4. **Clone it to his machine** — `C:\Users\...\Documents\<domain>-research`. Claude Code does this; Kenny says where he wants it.
5. **Point Claude Desktop at that folder.** It reads what's there.
6. Kenny asks Claude Desktop to help him write up what he's learned so far. Text lands *in the files*, not in a chat window that disappears.
7. **The payoff shot:** back to the browser, commit the changes, open a file's history. Two versions, timestamped, side by side.

**Dean's line over the history view:** that history *is* your understanding of this domain over time. Not what Kenny thinks today — what the team thought in August and why it changed.

**And the harder one:** you can revert a belief. You can't revert a market. The record tells you which one you're looking at.

**The AI point, precisely:** Kenny did not paste context into a chat window. The context lives in files, and it will still be there next quarter when someone else asks.

**Failure recovery:** if Claude Desktop can't see the folder, Kenny edits in the browser instead and Dean says the true thing — *"the browser always works, and that's the floor under everything else today."* Do not burn ninety seconds on a permissions dialog.

**[45-min cut]** Two stub files, not four.


### Adoption and limits  ·  *say these out loud*

**Use this when** your team keeps relitigating settled decisions, when the person who knows why is a single point of failure, or when you are re-explaining your product to an AI tool every morning.

**Skip it when** you are two people who talk daily about one thing. The overhead will exceed the memory you are buying.

**What it does not do:** it will not make anyone write things down. A repo is a place for the record, not a reason to keep one. If your team does not currently write decisions anywhere, this changes where nothing gets written.

---

## 0:20–0:26 · Play 2 — Communications

**Kenny's problem:** he's one person with one view of the domain, and he knows he's wrong about some of it.

**What happens:**
1. Kenny **adds Dean as a collaborator** on his private repo. On screen, ten seconds.
2. **Dean opens an Issue** — not a correction, a question. *"You've got throughput listed as the primary metric. Is that what the plant managers actually optimize, or what the software vendors say they optimize?"*
3. Kenny responds in the issue. The disagreement is now **written down, attached to the thing it's about, and dated.**
4. **Dean commits an edit** to `open-questions.md` from his Mac. Kenny pulls it. Two machines, two operating systems, one shared understanding.
5. Labels — five, and only five. Enough to sort, not enough to become a taxonomy project.

**Dean's line:** this is the cheapest disagreement you will ever have. Arguing in an issue costs nothing. Arguing in a roadmap costs a quarter.

**The shared-context point, which is the whole play:** most teams have "shared understanding" that lives in one person's head and gets re-explained on demand. This is the same understanding, in a place two people just edited from different operating systems.

**Failure recovery:** if the collaborator invite is slow to land, Dean narrates from his own screen while it arrives. Have the invite pre-accepted as a fallback.


### Adoption and limits  ·  *say these out loud*

**Use this when** disagreements are happening in threads that scroll away, when the same argument keeps restarting, or when nobody can find why a request was declined.

**Skip it when** the conversation genuinely belongs in a meeting. This is for the argument you want to still be readable in six months, not for everything.

**What it does not do:** it will not make people comment. Adoption is a people problem and GitHub does not solve it. Expect to seed the first several yourself, and expect some colleagues to reply by email anyway.

---

## 0:26–0:34 · Play 3 — Confidence

**Kenny's problem:** he has opinions about the domain and very little evidence.

**The switch, named out loud:** Claude Desktop was reading and writing files in one folder. Now Kenny needs something that can *fetch a library, go get evidence, and put it somewhere.* **He switches to Claude Code.**

**What he does:**
1. **Clones the market intelligence repo** to his machine. Claude Code does it; Kenny says where he wants it. Dean names what just happened in one sentence: *"That's a copy of a library Productside published. It's his now — he can read every skill in it, run them, and change them."*
2. **Runs a sweep** against a pre-chosen public company, using a skill from that clone. *(Target rehearsed in advance — see pre-flight.)*
3. The output is **cited, and labeled by confidence.** Dean points at what it refuses to claim: *"the claims you must not make."* That section is the reason to trust the rest.
4. **The result gets written into Kenny's repo**, committed, pushed. It's now part of the domain's record, not a chat transcript.

**Dean's line:** a research folder tells you what you learned. A repo tells you what you learned, when, from where, and what you did about it. The second one survives a reorg.

**The guardrail, plainly:** stars are not market share, issue volume is not pain severity, and commit velocity is not customer value. When the evidence is external, beware the squeaky wheel.

**Failure recovery — this is the highest-variance segment in the show.** A live sweep needs web access and takes real time.
- If it's slow, Dean talks over it. Have something to say for ninety seconds.
- If it fails or returns junk, **Kenny opens the rehearsed saved output** and Dean says so out loud: *"we ran this yesterday too — here's what it produced, and here's why we keep the receipts."* Owning the fallback is stronger than hiding it.
- **Never re-run a failed sweep live.** One attempt, then fallback.

**[45-min cut]** Show the clone, then go straight to the saved output. The clone is the teachable part; the wait is not.


### Adoption and limits  ·  *say these out loud*

**Use this when** your research keeps getting redone because nobody can find the last round, or when you need evidence a skeptical executive will accept — cited, dated, and traceable.

**Skip it when** you need an answer in the next ten minutes. This is a compounding asset, not a fast one.

**What it does not do:** it does not make the evidence true. A confident, well-cited, wrong answer is still wrong. The library labels what it cannot claim precisely because the tooling cannot supply judgment.

---

## 0:34–0:39 · Play 4 — Constitution

**Kenny's problem:** he has just pulled a pile of competitive material into a repo, and some of what he collects must never leak.

**What gets built:**
1. Kenny creates **`CONSTITUTION.md`** in his own repo. Plain English, short: no customer names, no material from a client engagement, no credentials, private stays private, human review before anything leaves.
2. Dean names the three layers that make it stick: **Context** is what we know, **Contract** is how we work, **Constitution** is what we will not do. Three files, three jobs, and the third one wins.
3. **The ethics beat, which this domain hands you for free:** the market intelligence skills already refuse pretexting, NDA-protected material, and scraping against terms. Dean shows where the library says so. *"The guardrail shipped with the tool. That's what good instructional material looks like."*
4. **Branch protection on the Productside repo** — set up in advance, shown here. This is what makes Play 5's review real rather than ceremonial.

**Dean's rhetorical shape, use it verbatim:** the obvious concern is, could we accidentally expose something sensitive? Yes, if we were sloppy. Which is why we are not being sloppy.

**Do not stage a fake secret-blocking demo here.** The real one happens in Play 5, on a real pull request, as a real check. Save it.


### Adoption and limits  ·  *say these out loud*

**Use this when** you have material that must never leak, contributors who do not know your rules, or a rule that currently lives in one person's memory and gets enforced by nagging.

**Skip it when** you are the only contributor and the stakes are low. A constitution with an audience of one is journaling.

**What it does not do:** automation catches patterns, not judgment. A guard can spot a credential-shaped string; it cannot tell you that a paragraph is strategically unwise or that a claim will not survive legal review. It moves the floor, not the ceiling.

---

## 0:39–0:48 · Play 5 — Community

**Kenny's problem:** using the library, he found a gap.

**The contribution: a new framework skill.** Either the **McKinsey Growth Pyramid** or the **BCG growth-share matrix** — Dean and Kenny to settle which. Neither exists in the library today; `reference/frameworks.md` covers SWOT, Five Forces, Ansoff, TAM/SAM/SOM, PESTEL, Positioning, and the battle card, and stops there.

**Why the gap is credible:** the library has growth *direction* (Ansoff), competitive *structure* (Five Forces), and *sizing* (TAM/SAM/SOM), but nothing that allocates across a portfolio. Kenny found that by using it. He should say so in his own words.

**Leaning Growth Pyramid** — Kenny has presented on it before, so he can talk about it fluently if anything stalls. That matters more live than the taxonomy fit.

> **Prefab requirements — non-negotiable, due before Aug 26:**
> - Four files: `SKILL.md`, `template.md`, `examples/worked-example.md`, `examples/weak-example.md`
> - A `SKILL_REGISTRY` line in `scripts/validate-skills.py`
> - **Green against `./scripts/test-library.sh` before dry run #1.** The CI validator checks thirteen required sections, section order, evidence labels, the do-not-invent list, the Final Step block, stage doctrine, and five Key Concepts each carrying a violation signal. A wall of validator errors at 0:45 is not a teachable moment.
> - Name it for the method, not the firm — `mi-analyze-growth-share`, matching `mi-analyze-five-forces`. Add attribution to `NOTICE.md`.
> - Have a sentence ready for the moment the `.py` registry edit appears on screen. `NOTICE.md` already carves those utilities out as "not the deliverable."
> - Confirm the source material is **Supplier IP, not a Training Deliverable**, per `productside-launchkit` 02-09.

**This is the ending. Do not rush it, do not cut it.**

**What happens:**
1. **He already has the clone** from Play 3 — that's why this works. Dean calls back to it: *"Remember, he copied the whole library. Which means he can improve it."*
2. Kenny **creates a branch.** Claude Code does it; Kenny says what he wants it called.
3. He **adds the prefabbed artifact** Dean supplied in advance — drag it into the cloned folder. *(No live authoring. This is a mechanics demo, not a writing demo.)*
4. Claude Code **commits and pushes the branch**, then **opens the pull request.**
5. **The content guard runs on the PR, live, as a real check.** Green tick, or a red X you talk through. **This is the governance demo — real automation on a real contribution, no staging.**
6. **Dean reviews on his Mac.** Leaves a comment. Kenny sees it. Dean approves.
7. **Dean merges.**

**The closing image:** a merged pull request on a public Productside repository with Kenny's name on it. Attendees can open the merge commit while the call is still running.

**Dean's line:** Kenny has not typed a git command today. He described what he wanted in the words he'd use in a hallway, and a public library changed. That's what "no coding required" means now — not that we hid the hard part, but that the hard part stopped being yours.

**The honest caveat, head-on:** to comment or contribute inside a private repo, a person has to be added to it. GitHub does not hand you open public participation because you turned on Issues. Kenny is a collaborator because Dean added him. Say it plainly — the credibility is worth more than the tidier story.

**Failure recovery:**
- PR won't open → Kenny pushes the branch and Dean opens the PR from his side. Same outcome.
- Guard goes red unexpectedly → **that is a good outcome.** Read the error aloud, explain what it caught, fix or revert. A guard that catches something on camera is worth more than a green tick.
- Merge conflict → do not resolve live. Dean says "I'll take this one" and moves on.


### Adoption and limits  ·  *say these out loud*

**Use this when** the same requests keep arriving through five channels, or when people ask for things and never learn what happened next.

**Skip it when** your contributors are customers who will never make a GitHub account. Meet them where they are and mirror it here.

**What it does not do:** GitHub does not give you open public participation. To comment or contribute inside a private repo, a person has to be added to it. Kenny is a collaborator because Dean added him. Say this plainly — the credibility is worth more than the tidier story.

---

## 0:48–0:50 · What GitHub is bad at

> **Each play already carried its own limit.** Do not repeat them here — that turns honesty into a disclaimer. This segment covers only what belongs to no single play.

- **The UI overwhelms non-technical people.** Real, and the most common reason adoption dies in week two. The fix is onboarding, not avoidance.
- **No Gantt charts.** Milestones are not timelines. If you run client-deadline work, you will still need something else.
- **Not everything belongs here.** Living operational churn stays where your team already works. This is the layer underneath that.

**The frame:** we are not asking you to migrate. We're asking you to stop losing things.

**[45-min cut]** Two bullets — the UI curve and "not everything belongs here." The rest were already said in the plays.

---

## 0:50–0:52 · Close

**The callback:** Kenny's account was empty forty-five minutes ago. Now: a private repo two people share, evidence collected into it with citations, guardrails written down, and a merged contribution to a public library.

**The thesis line:** your strategy doc gets rewritten every Monday. Your repo doesn't have to.

**The Productside beat, in Dean's words:** we teach clients not to operate as "One Team" in name while everyone works in separate silos, folders, sessions, and projects. We should not work that way either.

**CTA:** *(confirm with marketing)* the recording, the public market intelligence library, and the courses hub.

---

## 0:52–0:54 · Poll 2

> **Starting today, what will you do differently?** — five options, one per play. Exact wording in [`polls.md`](polls.md).

Kenny reads the results. **Compare them against Poll 1 out loud.** That comparison is the most useful thing this session produces besides registrations, and saying it in the room is what makes the audience feel the arc close.

---

## 0:54–1:00 · Q&A

Kenny moderates. Pre-loaded:

- **"Isn't this just a wiki?"** A wiki has no history you can diff, no review before change, and no automation that can say no.
- **"What about Confluence / Notion / Jira?"** Keep them. This is the durable layer underneath, and it's the one your AI can read.
- **"Do I need to be technical?"** Kenny wasn't, an hour ago, and he's on Windows without a terminal open.
- **"Will my engineers hate this?"** They already live there. You're moving toward them.
- **"What does it cost?"** Free for everything you just watched. Dedicated PM tools run $20–80 per user per month.
- **"Can I use your market intelligence library?"** Yes — it's public, CC BY-NC-SA, attribution required, non-commercial. Clone it like Kenny did, or install it as a plugin if you only ever want to run the skills; the QUICKSTART covers both.

---

## Pre-flight checklist

**Done days before:**
- [ ] Market intelligence repo **flipped public**, with `BLOCKED_TERMS` granted and one workflow run confirmed green
- [ ] **Branch protection on `main`**: require a pull request, require one approval
- [ ] **Kenny added as collaborator** on the MI repo; invite accepted
- [ ] **Dean added as collaborator** on Kenny's private repo; invite accepted
- [ ] **`.gitattributes` with `* text=auto`** in both repos — see the CRLF note in `kenny-prep.md`. Skip this and Kenny's PR diff shows every line changed.
- [ ] Sweep target company chosen and rehearsed; **saved output staged as fallback**
- [ ] Prefabbed artifact for Play 5 written and handed to Kenny
- [ ] Domain chosen and Kenny's repo named

**Show day:**
- [ ] Demo accounts only — **no client work, no internal systems, no inbox** on either screen
- [ ] Claude Desktop connected to Kenny's folder; Claude Code authenticated
- [ ] Kenny's repo reset to empty
- [ ] Browser zoom readable on a phone; notifications off on both machines
- [ ] Dean's terminal ready: clean directory, large font, history cleared
- [ ] Someone watching chat
- [ ] Recording started
