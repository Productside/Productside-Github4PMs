# Slide Plan

Deck spec for **Beyond the Backlog**, built on the canonical Productside webinar template.

**Note:** This plan reflects the pivot from five plays (Context, Communications, Confidence, Constitution, Community) to seven capabilities (Share, Collaborate, Review, Trace, Experiment, Augment, Reuse). The subtitle "Five GitHub Plays for Product Teams" needs updating. Candidate: **"How GitHub Compounds Your Product Team's Thinking"** or similar. Dean decides.

**Source kit:** `~/Code/productside-marketing-and-sales-design-system/ui_kits/deck-webinar/`
**Base layouts:** `ui_kits/deck/` · **Tokens:** `colors_and_type.css`
**Format:** 1920x1080, PowerPoint-export friendly.

---

## The governing constraint

**This is a live-build session, not a slide talk.** The audience spends most of the hour watching a screen share. The deck is not the teaching surface. It is the set of **bumpers between live segments**: enter a beat, state the idea, leave the deck, build it live, come back for the takeaway.

That drives every decision below:

- **Two or three slides per beat, maximum.** One of them is always the diagram.
- **No slide explains what the demo is about to show.** If the build shows it, the slide does not say it.
- **Every beat opens on a green divider** so the audience feels structure even while the screen share dominates.
- **Assume any slide may be on screen for eight seconds.** One idea, one focal point.

---

## Wiring

Link in this order, exactly as the template does:

```html
<link rel="stylesheet" href="../../colors_and_type.css">
<link rel="stylesheet" href="../deck/styles.css">
```

Layout classes available from the webinar template, in the sequence it uses them:

| Class | Role |
|---|---|
| `w-title on-black` | hold, title |
| `w-spk` | speakers |
| `w-about` | why clients choose us |
| `w-intro` | intro callouts (questions, LinkedIn) |
| `w-agenda` | agenda |
| `w-div on-green` | part divider |
| `w-step on-green` | step divider |
| `w-hero` / `w-hero on-black` | one big sentence, a moment |
| `w-bigstat on-black` | one dominant number |
| `w-data` | stat + verbatim quote + one line of context |
| `w-move` | `.01 / .02 / .03` three actions |
| `w-grid` | 4-up stat grid |
| `w-poll` | poll, 01-05 options |
| `w-promo` | report / tool promo with QR |
| `w-courses` | upcoming courses table |
| `w-end on-black` / `w-end on-green` | Q&A, thank you |

**Type rule:** Kraken Slab **only** on title and dividers. Clash Grotesk Medium for all other headings. PP Mori for body. Clash Display for ALL-CAPS eyebrows.

**Color rhythm:** black for title, big-stat moments, takeaways and Q&A. Green for dividers and thank-you only, never a full content slide. White for all teaching content.

---

## Open -- fixed, do not redesign

The template's opening sequence is brand-mandated. Swap content, keep the skeleton.

| # | Layout | Content |
|---|---|---|
| 1 | `w-title on-black` | Hold. Title + date strip + "Thank you for waiting, we'll begin shortly." |
| 2 | `w-title on-black` | Title. **Beyond the Backlog** / [updated subtitle] / September 2, 2026 |
| 3 | `w-spk` | Dean Peters and Kenny Kranseler. **Kenny is billed as co-presenter, not moderator.** |
| 4 | `w-about` | Why clients choose us + three pillars |
| 5 | `w-intro` | Please ask questions / how to watch later |
| 6 | `w-intro` | Connect with us on LinkedIn |
| 7 | `w-agenda` | The seven capabilities, listed. No durations. |
| 8 | `w-poll` | **Poll 1** -- see [`polls.md`](polls.md) |

---

## The two polls

Full question text, option wording, timings, and run instructions live in **[`polls.md`](polls.md)** -- the source of truth. Do not restate the options here; they will drift.

**Note:** The polls need rewriting to match the seven-capability structure. The current polls are built on the five-play taxonomy and are out of date. See `polls.md` for the update.

Placement in the deck:

| Slide | Layout | Poll |
|---|---|---|
| 8, after the agenda | `w-poll` | **Poll 1** -- which one hurts most right now |
| after the close hero | `w-poll` | **Poll 2** -- starting today, what will you do differently |

---

## Teaching middle

### Cold open -- 2 slides

| Layout | Kicker | Content |
|---|---|---|
| `w-hero on-black` | -- | *"Does your product team have a place where its thinking can compound?"* |
| white, diagram | `THE PROBLEM` | **Diagram -- Context rebuilt vs. context compounded** |

### The comparison -- 1 slide

| Layout | Kicker | Content |
|---|---|---|
| white, table | `THE REAL QUESTION` | **What is each environment optimized to support?** Table comparing SharePoint/Drive, Confluence, Jira, Claude Projects, GitHub. Not "these are bad." Different tools, different optimizations. |

### How git got here -- 2 slides

| Layout | Kicker | Content |
|---|---|---|
| white, diagram | `HOW WE GOT HERE` | **Diagram -- Four steps, none of them planned** |
| white, diagram | `WHAT A BRANCH IS` | **Diagram -- A branch is a safe place to be wrong** |

Dean is on a terminal for this beat. These two are backdrop, not the content.

### The frame -- 2 slides

| Layout | Kicker | Content |
|---|---|---|
| white, diagram | `THE NOTATION` | **Diagram -- The notation, once.** Show it here if showing more than two diagrams all session. |
| white, diagram | `TODAY'S BUILD` | **Diagram -- Two repos, two jobs.** The single most useful slide in the deck. |

### 01 Share -- 3 slides

| Layout | Kicker | Content |
|---|---|---|
| `w-step on-green` | `01 · SHARE` | **Share a complete product workspace** |
| white, diagram | `THE DIFFERENCE` | **Diagram -- Scattered artifacts vs. shared repository** |
| `w-hero on-black` | -- | Team context that compounds instead of being rebuilt. |

### 02 Collaborate -- 3 slides

| Layout | Kicker | Content |
|---|---|---|
| `w-step on-green` | `02 · COLLABORATE` | **Work together without trampling each other** |
| white, diagram | `THE FORK` | **Diagram -- Discussion vs. Issue: still a question, or already a commitment?** |
| `w-hero on-black` | -- | *"Arguing in a Discussion costs nothing. Arguing in a roadmap costs a quarter."* |

### 03 Review -- 3 slides

| Layout | Kicker | Content |
|---|---|---|
| `w-step on-green` | `03 · REVIEW` | **Make changes reviewable before they become truth** |
| white, diagram | `THE GATE` | **Diagram -- The pull request review flow** |
| `w-hero on-black` | -- | *"Review is a gate, not a ritual. The difference is whether you can push straight to main."* |

### 04 Trace -- 3 slides

| Layout | Kicker | Content |
|---|---|---|
| `w-step on-green` | `04 · TRACE` | **See what changed, who changed it, and why** |
| white, diagram | `EVIDENCE` | **Diagram -- Assumption to decision, connected** |
| `w-hero on-black` | -- | *"You can revert a belief. You cannot revert a market."* |

### 05 Experiment -- 3 slides

| Layout | Kicker | Content |
|---|---|---|
| `w-step on-green` | `05 · EXPERIMENT` | **Explore alternatives without breaking what works** |
| white, diagram | `PARALLEL` | **Diagram -- Linear revisions vs. parallel exploration** |
| `w-hero on-black` | -- | *"Stars are not market share. Issue volume is not pain severity. Test the bet before you commit the quarter."* |

### 06 Augment -- 3 slides

| Layout | Kicker | Content |
|---|---|---|
| `w-step on-green` | `06 · AUGMENT` | **Give AI the same context as the team** |
| white, diagram | `SHARED CONTEXT` | **Diagram -- Session-based AI vs. repo-based AI** |
| `w-hero on-black` | -- | The team and its AI systems work from the same persistent context. |

### 07 Reuse -- 3 slides

| Layout | Kicker | Content |
|---|---|---|
| `w-step on-green` | `07 · REUSE` | **Turn practices into reusable assets** |
| white, diagram | `INFRASTRUCTURE` | **Diagram -- Tribal knowledge becomes team infrastructure** |
| `w-hero on-black` | -- | *"Could we accidentally expose something sensitive? Yes, if we were sloppy. Which is why we are not being sloppy."* |

### What GitHub is not optimized for -- 1 slide

| Layout | Kicker | Content |
|---|---|---|
| `w-move` | `THE HONEST PART` | `.01` The UI curve . `.02` No Gantt charts . `.03` Not everything belongs here . `.04` AI makes the case more urgent, but does not create it |

### Close -- 2 slides before the fixed sequence

| Layout | Kicker | Content |
|---|---|---|
| `w-hero on-black` | -- | *"Does your product team have a place where its thinking can compound?"* |
| `w-poll` | `POLL QUESTION` | **Poll 2** -- starting today, what will you do differently? |

---

## Close -- fixed, do not redesign

`w-promo` (the public market intelligence library, with QR) -> `w-promo` (join us in person) -> upcoming webinar -> `w-courses` -> `w-end on-black` (Q&A) -> `w-end on-green` (Thank You).

---

## Count

| Section | Slides |
|---|---|
| Fixed open | 7 + Poll 1 |
| Teaching middle | 28 |
| Close | 2 (hero + Poll 2) |
| Fixed close | 6 |
| **Total** | **43** |

This is 8 more slides than the old five-play structure (35), driven by two additional capabilities (Review, Reuse) each getting 3 slides. The teaching middle is 28 slides, but 14 of those are green dividers and hero quotes that flash on screen for under 10 seconds each. The actual content slides number 14, which is comparable to the old 10.

---

## Open problems for whoever builds this

**1. Subtitle needs a decision.** The old subtitle "Five GitHub Plays for Product Teams" is out of date. Candidates: "How GitHub Compounds Your Product Team's Thinking" or "Seven Ways GitHub Changes How Product Teams Work." Dean decides.

**2. The kit has no diagram layout.** Every layout class in the webinar template is built for text, stats, or quotes. Fourteen slides here are diagram-led. Either add a `w-diagram` variant to `ui_kits/deck/layouts.css` (full-bleed white, one centered figure, kicker eyebrow, no body copy) or repurpose `w-hero` with the figure as the focal element. **This is a design-system decision, not a deck decision.**

**3. Mermaid does not render in a static deck.** The diagrams are mermaid in markdown, which GitHub renders but a slide will not. Three options, in order of preference:

- **Export SVG with `mmdc`** (mermaid-cli) from the slide pages. Deterministic, scales cleanly, survives PowerPoint export.
- Embed `mermaid.js` in the deck HTML. Renders live but risks a blank slide.
- Screenshot. Fast, and wrong at 1920x1080.

**4. Slide copy follows the Copy Guidelines, which the run-of-show does not.** `assets/copy/productside-copy-guidelines.md` bans em dashes and a specific word list. The run-of-show uses em dashes freely. **Do not paste from it into slides without a pass.**

**5. Polls need rewriting.** The current polls in `polls.md` are built on the five-play taxonomy. They need updating to match the seven-capability structure. The `w-poll` layout supports five options, so some capabilities will need to be grouped.

**6. Headshots.** Use the provided `assets/headshots/<Name>_Green@2x.png` files as-is.
