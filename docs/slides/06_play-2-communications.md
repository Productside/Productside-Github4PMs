<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 160" width="960" height="160">
  <rect width="960" height="160" rx="12" fill="#0B3D2E"/>
  <text x="48" y="58" font-family="system-ui, -apple-system, sans-serif" font-size="16" font-weight="600" letter-spacing="3" fill="#4ADE80" text-anchor="start">PLAY 02</text>
  <text x="48" y="108" font-family="system-ui, -apple-system, sans-serif" font-size="48" font-weight="700" fill="#FFFFFF" text-anchor="start">Communications</text>
  <text x="48" y="138" font-family="system-ui, -apple-system, sans-serif" font-size="16" fill="#94D2BD" text-anchor="start">Beyond the Backlog · Productside</text>
  <circle cx="900" cy="80" r="36" fill="none" stroke="#4ADE80" stroke-width="2"/>
  <text x="900" y="88" font-family="system-ui, -apple-system, sans-serif" font-size="28" font-weight="700" fill="#4ADE80" text-anchor="middle">02</text>
</svg>

&nbsp;

## The fork

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

&nbsp;

> **"Arguing in a Discussion costs nothing. Arguing in a roadmap costs a quarter."**

&nbsp;

---

<sub>Beyond the Backlog: Five GitHub Plays for Product Teams · Productside · September 2, 2026</sub>

---

[&larr; Play 1](05_play-1-context.md) · [Next: Play 3 &rarr;](07_play-3-confidence.md) · [Run](run.md)
