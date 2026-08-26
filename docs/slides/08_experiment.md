<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 160" width="960" height="160">
  <rect width="960" height="160" rx="12" fill="#0B3D2E"/>
  <text x="48" y="58" font-family="system-ui, -apple-system, sans-serif" font-size="16" font-weight="600" letter-spacing="3" fill="#4ADE80" text-anchor="start">05 · EXPERIMENT</text>
  <text x="48" y="108" font-family="system-ui, -apple-system, sans-serif" font-size="48" font-weight="700" fill="#FFFFFF" text-anchor="start">Explore alternatives without</text>
  <text x="48" y="148" font-family="system-ui, -apple-system, sans-serif" font-size="48" font-weight="700" fill="#FFFFFF" text-anchor="start">breaking what works</text>
  <circle cx="900" cy="80" r="36" fill="none" stroke="#4ADE80" stroke-width="2"/>
  <text x="900" y="88" font-family="system-ui, -apple-system, sans-serif" font-size="28" font-weight="700" fill="#4ADE80" text-anchor="middle">05</text>
</svg>

&nbsp;

## Parallel exploration vs. linear revision

Experimentation is a daily habit for product managers. It should not be a version control risk. When your team has three competing strategic directions, you should not need three duplicate files and crossed fingers.

```mermaid
flowchart TD
  subgraph L["Linear tools"]
    O["Original"]
    V1["Copy 1<br/>strategy A"]
    V2["Copy 2<br/>strategy B"]
    V3["Copy 3<br/>strategy C"]
    CONF["Which one is current?<br/>Nobody knows"]
    O --> V1
    O --> V2
    O --> V3
    V1 --> CONF
    V2 --> CONF
    V3 --> CONF
  end
  subgraph B["Branches"]
    M["Main<br/>trusted version"]
    BA["Branch<br/>strategy A"]
    BB["Branch<br/>strategy B"]
    BC["Branch<br/>strategy C"]
    MERGE["Compare line by line<br/>merge the survivors"]
    M --> BA
    M --> BB
    M --> BC
    BA --> MERGE
    BB --> MERGE
    BC --> MERGE
    MERGE --> M
  end
```

<img src="assets/diag_05_experiment.svg" alt="Parallel branch exploration" width="800"/>

&nbsp;

Try competing strategies, hypotheses, problem framings, requirements, prompts, or product bets. The trusted version stays untouched until someone deliberately merges the parts that survived.

In plain English: curiosity and experimentation should be daily habits, not massive risks that threaten to overwrite the master strategy document.

> **"Stars are not market share. Issue volume is not pain severity. Test the bet before you commit the quarter."**

&nbsp;

---

<sub>Beyond the Backlog · Productside · September 2, 2026</sub>

---

[&larr; Trace](07_trace.md) · [Next: Augment &rarr;](09_augment.md) · [Run](run.md)
