# Diagrams

The visual bench for the webinar, **organized by capability**. Not all of these go on screen — that's a live call. The point is to have more than you need and choose.

Every diagram here is mermaid in markdown, which GitHub renders natively — so each one is text, version-controlled, and diffable in a pull request. **Say that out loud the first time one appears.** A diagram you can diff is the thesis of this session; a downloaded PNG quietly contradicts it.

**This file is the source of truth.** Individual per-diagram files live in [`diagrams/`](diagrams/INDEX.md) and are generated — edit here, then run `python3 scripts/split-diagrams.py`.

House style, matching `Productside-Market-Intelligence-Skills` and `Productside-Precedents-Thinking`: `flowchart` with quoted labels, `<br/>` for line breaks, dotted edges for feedback, no color. **Labels must never contain `](`** — the link validator reads raw text including fenced blocks and would misread it as a broken relative link.

---
---

# How to read these

## 1. The notation, once

Every diagram in this set uses the same four marks. Learn them here and they never change — which is the point. If you show more than two diagrams live, show this one first.

```mermaid
flowchart LR
  T["A thing<br/>rectangle"]
  D{"A decision<br/>diamond"}
  Y["One outcome"]
  N["The other outcome"]

  T --> D
  D -->|"a labelled choice"| Y
  D -->|"the other choice"| N
  Y -.->|"dotted means feedback,<br/>or a path back"| T
```

- **Rectangle** — a thing that exists: a file, a repo, a person, a state.
- **Diamond** — a decision or a check. Something evaluates and routes.
- **Solid arrow** — the forward path. What normally happens next.
- **Dotted arrow** — a return: feedback, a loop, a fallback, or a rejection with a reason.
- **Box around a group** — a boundary that matters. Usually a machine or an organization.

**The one thing worth saying out loud:** dotted lines are where the value is. A process with no dotted lines is a conveyor belt, and nobody learns anything on a conveyor belt.

---
---

# The problem and the reframe

## 2. Where thinking dies

Three destinations, all terminal, and the reason every AI session starts from zero.

```mermaid
flowchart LR
  T["What you<br/>actually figured out"]
  N["A doc<br/>nobody reopens"]
  S["A thread<br/>nobody can find"]
  D["A deck rebuilt<br/>from scratch<br/>every quarter"]
  X["Gone"]
  AI["Every AI tool<br/>you touch"]
  Z["Starts from zero<br/>you re-explain<br/>the product again"]

  T --> N --> X
  T --> S --> X
  T --> D --> X
  AI --> Z
  X -.->|"nothing it can read"| AI
```

**The line:** nothing you know lives anywhere your tools can find it.

## 3. What GitHub actually is

Four familiar categories stacked, rather than one abstract metaphor. Dean's own framing.

```mermaid
flowchart TD
  G["GitHub"]
  V["Digital vault<br/>versioned, recoverable,<br/>nothing silently lost"]
  P["Publishing platform<br/>when you decide<br/>something should be seen"]
  C["Collaboration space<br/>issues, reviews,<br/>disagreement on the record"]
  M["Institutional memory<br/>why we decided,<br/>and when"]

  G --> V
  G --> P
  G --> C
  G --> M
```

**The straw man to kill first:** search results will tell you it's an alternative to Jira. That's the wrong answer to the wrong question.

## 4. Four steps, none of them planned

```mermaid
flowchart LR
  G["2005 · Git<br/>tracks versions of files<br/>built for source code"]
  W["Then · Conventions<br/>gitflow and its cousins<br/>teams inventing process"]
  H["Then · GitHub<br/>issues, reviews, permissions<br/>coordinating people"]
  P["Now · Product teams<br/>the coordination layer does not care<br/>whether the files are source code"]

  G --> W --> H --> P
```

**The handoff line:** every one of those steps was somebody discovering the tool did more than it was built to do. We're just the next ones to notice.

---
---

# Capability: Share

## 5. What goes in the repo

Anatomy of Kenny's domain research Project. Stubs are fine and honest.

```mermaid
flowchart TD
  R["domain-research"]
  RM["README.md<br/>what this domain is,<br/>why the team cares"]
  WK["what-we-know.md<br/>current understanding"]
  OQ["open-questions.md<br/>what we have not settled"]
  GL["glossary.md<br/>words this domain<br/>uses differently"]
  SR["sources.md<br/>where it came from"]
  DC["decisions<br/>one file per<br/>decision, dated"]

  R --> RM
  R --> WK
  R --> OQ
  R --> GL
  R --> SR
  R --> DC
```

## 6. Three layers, and which one wins

Productside's own repo anatomy — not a GitHub feature. The mechanism is **precedence**.

```mermaid
flowchart TD
  CN["Constitution<br/>what we will not do<br/>CONSTITUTION.md"]
  CT["Contract<br/>how we work here<br/>CLAUDE.md"]
  CX["Context<br/>what we know and decided<br/>README and the files"]

  CN -->|"overrides"| CT
  CT -->|"overrides"| CX
  CX -.->|"a conflict escalates upward,<br/>never the other way"| CN
```

**Three files, three jobs, and the third one wins.** Say it here; call back to it in the Constitution capability.

## 7. Two repos, two jobs

The architecture of the whole session. Kenny's work never leaves private.

```mermaid
flowchart LR
  subgraph K["Kenny's machine · Windows"]
    KR["Domain research<br/>PRIVATE, stays private<br/>what the team believes"]
    ML["Market intelligence<br/>cloned copy<br/>22 skills, 22 prompts"]
  end
  subgraph P["Productside org"]
    MI["Market Intelligence<br/>PUBLIC<br/>published before the show"]
  end
  D["Dean's machine · Mac"]

  MI -->|"clone, once"| ML
  ML -->|"run a sweep,<br/>write the evidence"| KR
  D -->|"collaborator:<br/>issues and commits"| KR
  ML -->|"branch and<br/>pull request"| MI
  MI -.->|"review and merge"| D
```

## 8. The tool ladder

Three rungs. The browser is the floor, and every failure recovery drops back to it.

```mermaid
flowchart TD
  B["Rung 1 · The browser<br/>create, edit, commit, review<br/>always works"]
  CD["Rung 2 · Claude Desktop<br/>reads and writes files<br/>in one local folder<br/>no git, no auth"]
  CC["Rung 3 · Claude Code<br/>clone, commit, push,<br/>branch, pull request"]

  B --> CD --> CC
  CC -.->|"if anything stalls"| B
  CD -.->|"if anything stalls"| B
```

**Kenny never types a git command at any rung.** He says sentences.

---
---

# Capability: Collaborate

## 9. Two machines, one understanding

Windows and macOS, different paths, same repo. The objection this kills: *"I'd need the same setup as my engineers."*

```mermaid
flowchart LR
  K["Kenny · Windows<br/>C:\\Users\\...\\Documents"]
  R["The repo<br/>does not care"]
  D["Dean · Mac<br/>~/Documents"]

  K -->|"commit and push"| R
  D -->|"commit and push"| R
  R -.->|"pull"| K
  R -.->|"pull"| D
```

## 10. Should we, or have we decided

The fork most teams have no home for.

```mermaid
flowchart TD
  I["An idea<br/>arrives"]
  Q{"Which is it"}
  DS["Discussion<br/>should we do<br/>something about this"]
  IS["Issue<br/>we have decided<br/>to investigate or change"]
  K["Dies here,<br/>cheaply, on the record"]
  C["Closed, with<br/>what happened next"]

  I --> Q
  Q -->|"still a question"| DS
  Q -->|"already a commitment"| IS
  DS --> K
  DS -.->|"survives the argument"| IS
  IS --> C
```

**The line:** arguing in a Discussion costs nothing. Arguing in a roadmap costs a quarter.

## 11. An issue closes with an outcome, not silence

```mermaid
flowchart LR
  O["Opened<br/>with context"]
  L["Labelled<br/>and routed"]
  A["Argued<br/>in the open"]
  R{"Resolved"}
  Y["Closed:<br/>here is what<br/>we did"]
  N["Closed:<br/>here is why<br/>we will not"]

  O --> L --> A --> R
  R -->|"yes"| Y
  R -->|"no"| N
```

**The part teams skip:** the second box. A declined request with a written reason is a better answer than silence.

---
---

# Capability: Review

## 12. A branch is a safe place to be wrong

The whole idea, at the only granularity a product audience needs. Work happens off to the side. The main line keeps working the entire time.

```mermaid
gitGraph
  commit id: "main is good"
  commit id: "still good"
  branch proposal
  commit id: "try something"
  commit id: "revise it"
  checkout main
  commit id: "unaffected"
  merge proposal
  commit id: "now everyone has it"
```

**The two things to point at:** the main line never broke while the work was happening, and nothing became shared until somebody merged it deliberately.

**What not to do here:** do not name the branching models. Gitflow, trunk-based, and the rest are conventions engineering teams argue about, and none of that helps this audience. If someone asks, the answer is "there are named patterns for this, your engineers have opinions, you do not need them today."

## 13. The same shape, in product terms

Why a product manager should care about a mechanic built for source code.

```mermaid
flowchart LR
  M["main<br/>what the team<br/>currently agrees"]
  B["branch<br/>a proposed change<br/>nobody has agreed to yet"]
  R["pull request<br/>the conversation about<br/>whether to agree"]
  M2["main<br/>what the team<br/>now agrees"]

  M -->|"someone proposes"| B --> R
  R -->|"approved"| M2
  R -.->|"declined, with a reason<br/>anyone can read later"| B
```

**The line:** a branch is a proposal, a pull request is the argument, and a merge is the moment it becomes what the team believes. That is a product process that happens to be implemented in git.

## 14. Why the pull request path exists

Branch protection is what makes review real rather than ceremonial.

```mermaid
flowchart LR
  W["Someone wants<br/>to change main"]
  D1{"Direct push<br/>to main"}
  X["Blocked"]
  BR["Branch"]
  PR["Pull request"]
  RV["Review<br/>by another human"]
  M["Merged"]

  W --> D1 --> X
  X -.->|"the only<br/>way through"| BR
  W --> BR --> PR --> RV --> M
```

**Without this, the review is theatre** — the contributor could have pushed straight to main.

---
---

# Capability: Trace

## 15. The commit history is the strategy timeline

The payoff shot, drawn. Every dot is a dated, attributed, recoverable change.

```mermaid
gitGraph
  commit id: "what we know v1"
  commit id: "added glossary"
  branch discovery
  commit id: "plant manager interviews"
  commit id: "throughput assumption challenged"
  checkout main
  merge discovery
  commit id: "primary metric changed"
  commit id: "open question closed"
```

**The line:** no more "ask Dean, he remembers why we changed that."

## 16. A decision record is superseded, never deleted

```mermaid
flowchart LR
  D1["0001<br/>we optimize<br/>for throughput"]
  N["New evidence<br/>arrives"]
  D2["0002<br/>we optimize for<br/>changeover time"]
  H["0001 stays,<br/>marked superseded<br/>by 0002"]

  D1 --> N --> D2
  D1 --> H
  D2 -.->|"links back to<br/>what it replaced"| H
```

**Why it matters:** you can revert a belief. You cannot revert a market. The record tells you which one you are looking at.

## 17. What changed, who changed it, and why

The workflow-level view: a PM asks a question, the history answers it without a meeting.

```mermaid
flowchart LR
  Q["Someone asks:<br/>why does the brief<br/>say this now"]
  H["Open file history"]
  D["The diff<br/>what changed,<br/>line by line"]
  A["The author<br/>who changed it"]
  M["The message<br/>why they changed it"]
  AN["Answered<br/>without a meeting"]

  Q --> H --> D
  H --> A
  H --> M
  D --> AN
  A --> AN
  M --> AN
```

**In plain English:** the trace is only as good as the commit message. "Updated file" tells you nothing. "Added deal-context section after Q1 loss review" tells you everything.

---
---

# Capability: Experiment

## 18. Try a different approach without touching what the team trusts

The PM-facing version: you do not need permission to be wrong, you need a safe place for it.

```mermaid
flowchart TD
  M["main<br/>the positioning<br/>the team trusts today"]
  B["branch<br/>a different positioning<br/>approach"]
  W["Work on it<br/>without touching main"]
  R{"Was it<br/>better"}
  MR["Merge it<br/>main improves"]
  DL["Delete the branch<br/>main never changed"]

  M -->|"create a branch"| B --> W --> R
  R -->|"yes"| MR
  R -->|"no"| DL
  MR -.->|"the team now<br/>trusts the new version"| M
```

**In plain English:** a branch is a safe place to be wrong. If the experiment fails, delete it. Main never changed.

---
---

# Capability: Augment

## 19. Session starter, or durable context

The abstract's hardest promise, and the reason this matters to an AI-shaped team.

```mermaid
flowchart LR
  subgraph B["What most people do"]
    H1["You re-explain<br/>the product"]
    A1["The tool answers"]
    E1["Session ends<br/>context evaporates"]
    H1 --> A1 --> E1
    E1 -.->|"tomorrow, again<br/>from scratch"| H1
  end
  subgraph G["What a repo does"]
    F["Files in the repo<br/>strategy, decisions,<br/>research"]
    A2["The tool reads them"]
    N2["New findings<br/>written back"]
    F --> A2 --> N2
    N2 -.->|"the record compounds"| F
  end
```

## 20. What the AI reads when it opens the repo

The file-level view: the AI assistant does not start from zero because the context is already there.

```mermaid
flowchart TD
  AI["AI assistant<br/>opens the repo"]
  CO["CONSTITUTION.md<br/>what it must not do"]
  CL["CLAUDE.md<br/>how to work here"]
  RE["README.md<br/>what this is about"]
  RS["research/<br/>evidence and sources"]
  DC["decisions/<br/>what the team settled"]
  SK["skills/<br/>what it can run"]

  AI --> CO
  AI --> CL
  AI --> RE
  AI --> RS
  AI --> DC
  AI --> SK
```

**The line:** the team and its AI work from the same persistent memory. Re-explaining your product every morning is over.

---
---

# Capability: Reuse

## 21. Install, clone, or fork

Three ways to consume the same library, for three different intents.

```mermaid
flowchart TD
  W{"What do you<br/>want to do"}
  I["Install<br/>two lines,<br/>nothing to manage"]
  C["Clone<br/>a copy you can<br/>read and change"]
  F["Fork<br/>your own copy<br/>on GitHub"]
  U["Just run the skills"]
  CH["Change it and<br/>contribute back"]
  OW["Take it your<br/>own direction"]

  W --> U --> I
  W --> CH --> C
  W --> OW --> F
```

**Kenny clones**, because a pull request needs a branch and a branch needs a clone.

## 22. The library consumption loop

How a team turns published assets into adopted practice, and how improvements flow back.

```mermaid
flowchart LR
  PB["Published library<br/>skills, templates,<br/>frameworks"]
  CL["Clone it"]
  RN["Run a skill<br/>on your domain"]
  OP["Structured output<br/>cited, formatted"]
  WR["Written into<br/>your repo"]
  FG["Find a gap<br/>or an improvement"]
  PR["Contribute back<br/>via pull request"]

  PB --> CL --> RN --> OP --> WR
  WR -.->|"over time"| FG --> PR
  PR -.->|"merged: the library<br/>improves for everyone"| PB
```

**In plain English:** tribal knowledge becomes team infrastructure. The next person who runs that skill gets your improvements automatically.

## 23. The contribution loop

The segment Kenny rehearses most.

```mermaid
flowchart LR
  C["Clone<br/>already done"]
  BR["Branch"]
  A["Add the artifact"]
  PU["Commit and push"]
  PR["Open the<br/>pull request"]
  G{"Content guard<br/>runs as a check"}
  RV["Dean reviews<br/>on his Mac"]
  M["Merge to main"]

  C --> BR --> A --> PU --> PR --> G
  G -->|"green"| RV
  G -->|"red"| A
  RV --> M
```

**The red path is not a failure state.** A guard that catches something on camera is worth more than a green tick.

## 24. The participation system

The wider loop the contribution sits inside. Candidate closing visual for the whole show.

```mermaid
flowchart LR
  CV["Conversation<br/>someone has a problem"]
  SB["Structured submission<br/>a template, not a paragraph"]
  AC["Automated check<br/>the guard runs"]
  TR["Triage<br/>labelled and routed"]
  HD["Human decision<br/>yes, no, or not yet"]
  SH["Shipped"]
  RC["Visible record<br/>of what happened next"]

  CV --> SB --> AC --> TR --> HD --> SH --> RC
  RC -.->|"the next person<br/>starts informed"| CV
  HD -.->|"declined, with a reason<br/>anyone can read"| RC
```

**The line:** this is not repository literacy. It is designing a participation system.

**The caveat that goes with it:** to comment or contribute inside a private repo, a person has to be added to it. GitHub does not hand you open participation because you turned on Issues.

---
---

# Capability: Catchup

## 25. Pull latest and see what moved

The workflow a PM runs every morning: what changed since I was last here, and why.

```mermaid
flowchart LR
  PM["PM opens<br/>the repo"]
  PL["Pull latest<br/>from main"]
  DF["See the diff<br/>what changed overnight"]
  CM["Read commit messages<br/>who changed it and why"]
  IS["Check issues<br/>new questions or decisions"]
  PR["Check pull requests<br/>pending reviews"]
  OR["Oriented<br/>without a standup"]

  PM --> PL --> DF --> CM --> OR
  PM --> IS --> OR
  PM --> PR --> OR
```

**In plain English:** the standup you do not have to schedule. The repo is the standup.

---
---

# Guardrails and governance

## 26. The guard runs before anything lands

```mermaid
flowchart LR
  C["A change<br/>is proposed"]
  G{"Content guard"}
  B1["Client or customer name"]
  B2["Credential-shaped string"]
  B3["Oversized or<br/>wrong file type"]
  R["Rejected,<br/>with the reason"]
  P["Allowed through<br/>to review"]

  C --> G
  G --> B1 --> R
  G --> B2 --> R
  G --> B3 --> R
  G -->|"clean"| P
```

**Dean's shape, verbatim:** the obvious concern is, could we accidentally expose something sensitive? Yes, if we were sloppy. Which is why we are not being sloppy.

## 27. Nothing is born public

```mermaid
flowchart LR
  N["New Project"]
  PV["Private<br/>by default"]
  RV{"Publication<br/>review"}
  SC["Scrub, license,<br/>attribution, guard"]
  PB["Public,<br/>deliberately"]

  N --> PV --> RV
  RV -->|"not yet"| PV
  RV -->|"ready"| SC --> PB
```

**The line:** start private. Make it public only when you mean to. Turning something public should feel like a small launch, not a casual settings change.

## 28. Which materials may go public

Productside's own classification. The category decides the answer far more often than the platform does.

```mermaid
flowchart TD
  Q["Something you<br/>want to publish"]
  C1{"Did a client<br/>bring it"}
  C2{"Was it created during<br/>a client engagement"}
  C3{"Are the rights<br/>solely ours"}
  NO1["No · client IP,<br/>never ours to license"]
  NO2["No · vests in the client<br/>as work made for hire"]
  NO3["No · not ours<br/>to grant alone"]
  YES["Yes, after<br/>publication review"]

  Q --> C1
  C1 -->|"yes"| NO1
  C1 -->|"no"| C2
  C2 -->|"yes"| NO2
  C2 -->|"no"| C3
  C3 -->|"no"| NO3
  C3 -->|"yes"| YES
```

**And the rule that governs the gray middle:** material published for public training may be published; bespoke customer material may not. Where something serves both, publish with public in mind and never identify a customer.

## 29. The evidence chain — reuse, do not rebuild

**This diagram already exists** in `Productside-Market-Intelligence-Skills/README.md` — `Instantiate → Collect → Fuse → Act → Monitor`, with a dotted "what changed" edge feeding the next run.

Pull it up from the Project on screen. That the library documents its own method is the point, and showing it live beats reproducing it here.

## 30. Assumption to decision, connected

```mermaid
flowchart LR
  AS["Assumption<br/>we believe X"]
  EX["Experiment<br/>here is how<br/>we would know"]
  EV["Evidence<br/>cited, dated"]
  DE{"Were we<br/>right"}
  KE["Decision recorded<br/>and acted on"]
  WR["Wrong, recorded<br/>as such"]

  AS --> EX --> EV --> DE
  DE -->|"yes"| KE
  DE -->|"no"| WR
  WR -.->|"sharpens the<br/>next assumption"| AS
```

**The one most teams cannot do:** the bottom path. A finding that says *we were wrong* is only valuable if it is findable later.

## 31. Confidence stacks across independent sources

Why six sources can be two disciplines — the trap the library exists to catch.

```mermaid
flowchart LR
  S1["Source A"]
  S2["Source B"]
  S3["Source C"]
  O["One origin<br/>a single press release"]
  I1["Discipline 1"]
  I2["Discipline 2"]
  H["Higher confidence"]
  L["Not higher confidence,<br/>just louder"]

  S1 --> O
  S2 --> O
  S3 --> O
  O --> L
  I1 --> H
  I2 --> H
```

**The line:** stars are not market share, issue volume is not pain severity, commit velocity is not customer value. And beware the squeaky wheel.

---
---

# The spine and the runbook

## 32. The seven capabilities as one story

Not seven demos. One team's thinking, compounding across seven capabilities.

```mermaid
flowchart TD
  S["Share<br/>a home for what<br/>the team knows"]
  CO["Collaborate<br/>work together without<br/>trampling each other"]
  RV["Review<br/>changes are reviewable<br/>before they become truth"]
  TR["Trace<br/>what changed,<br/>who, and why"]
  EX["Experiment<br/>explore without breaking<br/>what works"]
  AU["Augment<br/>AI reads the same<br/>context as the team"]
  RE["Reuse<br/>practices become assets<br/>another team can adopt"]

  S --> CO --> RV --> TR --> EX --> AU --> RE
  RE -.->|"the library improves,<br/>the next team starts ahead"| S
```

## 33. When something breaks on camera

The thirty-second rule. Dean's real job during the build.

```mermaid
flowchart TD
  B["Something<br/>stalls"]
  T{"Thirty<br/>seconds"}
  N["Dean narrates<br/>the hunt out loud"]
  F["Drop to the fallback<br/>browser, or the<br/>rehearsed saved output"]
  S["Say what happened,<br/>and keep going"]

  B --> T
  T -->|"under"| N
  T -->|"over"| F --> S
  N -.->|"still stuck"| F
```

**Never re-run a failed step live.** One attempt, then fallback. Owning it out loud is stronger than hiding it.

## 34. The hour

```mermaid
gantt
  title Run of show
  dateFormat HH:mm
  axisFormat %H:%M
  section Open
  Hold and title         :00:00, 2m
  Cold open              :00:02, 3m
  Housekeeping           :00:05, 3m
  Poll one               :00:08, 2m
  How git got here       :00:10, 2m
  Rules of the show      :00:12, 1m
  section The build
  Context                :00:13, 7m
  Communications         :00:20, 6m
  Confidence             :00:26, 8m
  Constitution           :00:34, 5m
  Community              :00:39, 9m
  section Close
  What GitHub is bad at  :00:48, 2m
  Close                  :00:50, 2m
  Poll two               :00:52, 2m
  Q and A                :00:54, 6m
```

## 35. Kenny's ten days

```mermaid
gantt
  title Prep to September 2
  dateFormat YYYY-MM-DD
  section Kenny solo
  Account and browser      :2026-08-24, 1d
  Windows toolchain        :2026-08-25, 1d
  Rebuild alone            :2026-08-27, 1d
  section Together
  Dry run one, no clock    :2026-08-26, 1d
  Dry run two, recorded    :2026-08-28, 1d
  Tech check               :2026-09-01, 1d
  section Dean solo
  Publish and configure    :2026-08-31, 1d
  section Buffer
  Deliberately empty       :2026-08-29, 2d
  section Show
  Live                     :2026-09-02, 1d
```
