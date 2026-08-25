<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 160" width="960" height="160">
  <rect width="960" height="160" rx="12" fill="#0B3D2E"/>
  <text x="48" y="58" font-family="system-ui, -apple-system, sans-serif" font-size="16" font-weight="600" letter-spacing="3" fill="#4ADE80" text-anchor="start">HOW WE GOT HERE</text>
  <text x="48" y="108" font-family="system-ui, -apple-system, sans-serif" font-size="44" font-weight="700" fill="#FFFFFF" text-anchor="start">Four steps, none of</text>
  <text x="48" y="140" font-family="system-ui, -apple-system, sans-serif" font-size="44" font-weight="700" fill="#FFFFFF" text-anchor="start">them planned</text>
</svg>

&nbsp;

Product teams are not adopting a developer tool. They are recognizing that collaborative knowledge work needs the same properties developers needed first: versioning, review, parallel changes, history, and machine accessibility.

```mermaid
flowchart LR
  G["2005 · Git<br/>tracks versions of files<br/>built for source code"]
  W["Then · Conventions<br/>gitflow and its cousins<br/>teams inventing process"]
  H["Then · GitHub<br/>issues, reviews, permissions<br/>coordinating people"]
  P["Now · Product teams<br/>the coordination layer does not care<br/>whether the files are source code"]

  G --> W --> H --> P
```

&nbsp;

## A branch is a safe place to be wrong

Work happens off to the side. The main line keeps working the entire time.

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

The main line never broke while the work was happening, and nothing became shared until somebody merged it deliberately.

&nbsp;

---

<sub>Beyond the Backlog · Productside · September 2, 2026</sub>

---

[&larr; The comparison](01_the-comparison.md) · [Next: The frame &rarr;](03_the-frame.md) · [Run](run.md)
