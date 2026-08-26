<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 160" width="960" height="160">
  <rect width="960" height="160" rx="12" fill="#1a1a1a"/>
  <text x="48" y="100" font-family="system-ui, -apple-system, sans-serif" font-size="44" font-weight="700" fill="#FFFFFF" text-anchor="start">Does your product team have a</text>
  <text x="48" y="140" font-family="system-ui, -apple-system, sans-serif" font-size="44" font-weight="700" fill="#FFFFFF" text-anchor="start">place where its thinking compounds?</text>
  <text x="912" y="140" font-family="system-ui, -apple-system, sans-serif" font-size="14" fill="#94D2BD" text-anchor="end">Productside</text>
</svg>

&nbsp;

```mermaid
flowchart LR
  subgraph R["What most teams do"]
    direction LR
    W["The team<br/>figures something out"]
    D["A doc, a thread,<br/>a chat, a deck"]
    L["Lost or buried<br/>within weeks"]
    RE["Someone else<br/>asks the same question"]
    W --> D --> L --> RE
    RE -.->|"rebuilt from scratch,<br/>every time"| W
  end
  subgraph C["What compounding looks like"]
    direction LR
    T["The team<br/>figures something out"]
    S["Written into<br/>the shared workspace"]
    B["Available to the team<br/>and to every tool<br/>connected to it"]
    T --> S --> B
    B -.->|"the next question<br/>starts informed"| T
  end
```

&nbsp;

<img src="assets/diag_00_compound.svg" alt="Context rebuilt vs. context compounded" width="800"/>

&nbsp;

Most product teams do not struggle because they lack effort. They struggle because clarity is missing. The question is whether your team's knowledge gets rebuilt every week or whether it compounds over time.

&nbsp;

---

<sub>Beyond the Backlog · Productside · September 2, 2026</sub>

---

[Next: The comparison &rarr;](01_the-comparison.md) · [Run](run.md)
