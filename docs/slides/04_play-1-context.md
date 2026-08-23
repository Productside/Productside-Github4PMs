<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 160" width="960" height="160">
  <rect width="960" height="160" rx="12" fill="#0B3D2E"/>
  <text x="48" y="58" font-family="system-ui, -apple-system, sans-serif" font-size="16" font-weight="600" letter-spacing="3" fill="#4ADE80" text-anchor="start">PLAY 01</text>
  <text x="48" y="108" font-family="system-ui, -apple-system, sans-serif" font-size="48" font-weight="700" fill="#FFFFFF" text-anchor="start">Context</text>
  <text x="48" y="138" font-family="system-ui, -apple-system, sans-serif" font-size="16" fill="#94D2BD" text-anchor="start">Beyond the Backlog · Productside</text>
  <circle cx="900" cy="80" r="36" fill="none" stroke="#4ADE80" stroke-width="2"/>
  <text x="900" y="88" font-family="system-ui, -apple-system, sans-serif" font-size="28" font-weight="700" fill="#4ADE80" text-anchor="middle">01</text>
</svg>

&nbsp;

## The difference

Every tool you hand your AI assistant starts a conversation from zero.
A repo starts every conversation from everything you already know.

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

&nbsp;

> **"You can revert a belief. You cannot revert a market."**

&nbsp;

---

<sub>Beyond the Backlog: Five GitHub Plays for Product Teams · Productside · September 2, 2026</sub>

---

[&larr; The frame](03_the-frame.md) · [Next: Play 2 &rarr;](05_play-2-communications.md) · [Run](run.md)
