# Slide Plan

Deck spec for **Beyond the Backlog: Five GitHub Plays for Product Teams**, built on the canonical Productside webinar template.

**Source kit:** `~/Code/productside-marketing-and-sales-design-system/ui_kits/deck-webinar/`
**Base layouts:** `ui_kits/deck/` · **Tokens:** `colors_and_type.css`
**Format:** 1920×1080, PowerPoint-export friendly.

---

## The governing constraint

**This is a live-build session, not a slide talk.** The audience spends most of the hour watching a screen share. The deck is not the teaching surface — it is the set of **bumpers between live segments**: enter a beat, state the idea, leave the deck, build it live, come back for the takeaway.

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
| `w-poll` | poll, 01–05 options |
| `w-promo` | report / tool promo with QR |
| `w-courses` | upcoming courses table |
| `w-end on-black` / `w-end on-green` | Q&A, thank you |

**Type rule:** Kraken Slab **only** on title and dividers. Clash Grotesk Medium for all other headings. PP Mori for body. Clash Display for ALL-CAPS eyebrows.

**Color rhythm:** black for title, big-stat moments, takeaways and Q&A. Green for dividers and thank-you only, never a full content slide. White for all teaching content.

---

## Open — fixed, do not redesign

The template's opening sequence is brand-mandated. Swap content, keep the skeleton.

| # | Layout | Content |
|---|---|---|
| 1 | `w-title on-black` | Hold. Title + date strip + "Thank you for waiting, we'll begin shortly." |
| 2 | `w-title on-black` | Title. **Beyond the Backlog** / Five GitHub Plays for Product Teams / September 2, 2026 |
| 3 | `w-spk` | Dean Peters and Kenny Kranseler. **Kenny is billed as co-presenter, not moderator** — his bio says he builds it live. |
| 4 | `w-about` | Why clients choose us + three pillars |
| 5 | `w-intro` | Please ask questions / how to watch later |
| 6 | `w-intro` | Connect with us on LinkedIn |
| 7 | `w-agenda` | The five plays, numbered. No durations — this session runs live and timings will move. |
| 8 | `w-poll` | **Poll 1** — see [`polls.md`](polls.md) |

---

## The two polls

Full question text, option wording, timings, and run instructions live in **[`polls.md`](polls.md)** — the source of truth. Do not restate the options here; they will drift.

Placement in the deck:

| Slide | Layout | Poll |
|---|---|---|
| 8, after the agenda | `w-poll` | **Poll 1** — which one hurts most right now |
| after the close hero | `w-poll` | **Poll 2** — starting today, what will you do differently |

Both share one taxonomy: the five plays. Poll 1 names five pains; Poll 2 offers the same five in their resolved state, in the same order, so the two result sets are directly comparable.

---

## Teaching middle

### Cold open · 0:00 — 2 slides

| Layout | Kicker | Content |
|---|---|---|
| `w-hero on-black` | — | *"Your best thinking dies in three places."* Nothing else on the slide. |
| white, diagram | `THE PROBLEM` | **Diagram 2 — Where thinking dies** |

### How git got here · 0:04 — 2 slides

| Layout | Kicker | Content |
|---|---|---|
| white, diagram | `HOW WE GOT HERE` | **Diagram 3 — Four steps, none of them planned** |
| white, diagram | `WHAT A BRANCH IS` | **Diagram 5 — A branch is a safe place to be wrong** |

Dean is on a terminal for this beat. These two are backdrop, not the content.

### The frame · 0:07 — 2 slides

| Layout | Kicker | Content |
|---|---|---|
| white, diagram | `THE NOTATION` | **Diagram 1 — The notation, once.** Show it here if showing more than two diagrams all session. |
| white, diagram | `TODAY'S BUILD` | **Diagram 6 — Two repos, two jobs.** The single most useful slide in the deck. |

### Play 1 · Context · 0:09 — 3 slides

| Layout | Kicker | Content |
|---|---|---|
| `w-step on-green` | `PLAY 01` | **Context** |
| white, diagram | `THE DIFFERENCE` | **Diagram 12 — Session starter, or durable context** |
| `w-hero on-black` | — | *"You can revert a belief. You cannot revert a market."* |

### Play 2 · Communications · 0:18 — 3 slides

| Layout | Kicker | Content |
|---|---|---|
| `w-step on-green` | `PLAY 02` | **Communications** |
| white, diagram | `THE FORK` | **Diagram 14 — Should we, or have we decided** |
| `w-hero on-black` | — | *"Arguing in a discussion costs nothing. Arguing in a roadmap costs a quarter."* |

### Play 3 · Confidence · 0:25 — 3 slides

| Layout | Kicker | Content |
|---|---|---|
| `w-step on-green` | `PLAY 03` | **Confidence** |
| white, diagram | `EVIDENCE` | **Diagram 17 — Assumption to decision, connected** |
| `w-hero on-black` | — | *"Stars are not market share. Issue volume is not pain severity."* |

### Play 4 · Constitution · 0:34 — 3 slides

| Layout | Kicker | Content |
|---|---|---|
| `w-step on-green` | `PLAY 04` | **Constitution** |
| white, diagram | `THE THREE LAYERS` | **Diagram 9 — Three layers, and which one wins** |
| `w-hero on-black` | — | *"Could we accidentally expose something sensitive? Yes, if we were sloppy. Which is why we are not being sloppy."* |

### Play 5 · Community · 0:40 — 3 slides

| Layout | Kicker | Content |
|---|---|---|
| `w-step on-green` | `PLAY 05` | **Community** |
| white, diagram | `THE LOOP` | **Diagram 25 — The participation system** |
| `w-hero on-black` | — | *"This is not repository literacy. It is designing a participation system."* |

### What GitHub is bad at · 0:50 — 1 slide

| Layout | Kicker | Content |
|---|---|---|
| `w-move` | `THE HONEST PART` | `.01` The UI curve · `.02` No Gantt charts · `.03` Not everything belongs here |

### Close · 0:50 — 2 slides before the fixed sequence

| Layout | Kicker | Content |
|---|---|---|
| `w-hero on-black` | — | *"Your strategy doc gets rewritten every Monday. Your repo doesn't have to."* |
| `w-poll` | `POLL QUESTION` | **Poll 2** — starting today, what will you do differently? |

---

## Close — fixed, do not redesign

`w-promo` (the public market intelligence library, with QR) → `w-promo` (join us in person) → upcoming webinar → `w-courses` → `w-end on-black` (Q&A) → `w-end on-green` (Thank You).

---

## Count

| Section | Slides |
|---|---|
| Fixed open | 7 + Poll 1 |
| Teaching middle | 20 |
| Close | 2 (hero + Poll 2) |
| Fixed close | 6 |
| **Total** | **35** |

Same order of magnitude as the canonical exemplar, and **13 of the 33 are brand chrome**. The teaching middle is 20 slides for a 50-minute session, most of which is a screen share.

---

## Open problems for whoever builds this

**1. The kit has no diagram layout.** Every layout class in the webinar template is built for text, stats, or quotes. Eleven slides here are diagram-led. Either add a `w-diagram` variant to `ui_kits/deck/layouts.css` (full-bleed white, one centered figure, kicker eyebrow, no body copy) or repurpose `w-hero` with the figure as the focal element. **This is a design-system decision, not a deck decision** — if `w-diagram` gets added, it belongs upstream in the kit.

**2. Mermaid does not render in a static deck.** The diagrams are mermaid in markdown, which GitHub renders but a slide will not. Three options, in order of preference:

- **Export SVG with `mmdc`** (mermaid-cli) from `docs/diagrams/*.md` into an `assets/` folder. Deterministic, scales cleanly, survives PowerPoint export, and can be scripted so a diagram edit regenerates the slide art.
- Embed `mermaid.js` in the deck HTML. Renders live but risks a blank slide if anything fails, and will not survive PowerPoint export.
- Screenshot. Fast, and wrong — raster art at 1920×1080 will look soft next to Kraken Slab.

**3. Slide copy follows the Copy Guidelines, which the run-of-show does not.** `assets/copy/productside-copy-guidelines.md` bans em dashes and a specific word list, and requires every claim to be anchored to a verified stat or marked `[Verify]`. The run-of-show is speaker notes and uses em dashes freely — **do not paste from it into slides without a pass.**

**4. One claim needs verification.** "Dedicated PM tools run $20–80 per user per month" comes from a 2020 conference talk. Either re-verify current pricing or mark it `[Verify]`. It appears in the Q&A prep, not on a slide, but it will be said out loud.

**5. Headshots.** Use the provided `assets/headshots/<Name>_Green@2x.png` files as-is. The green background and squircle corners are baked in. Never re-tint, never add `border-radius`.
