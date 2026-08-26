<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 160" width="960" height="160">
  <rect width="960" height="160" rx="12" fill="#0B3D2E"/>
  <text x="48" y="58" font-family="system-ui, -apple-system, sans-serif" font-size="16" font-weight="600" letter-spacing="3" fill="#4ADE80" text-anchor="start">06 · AUGMENT</text>
  <text x="48" y="108" font-family="system-ui, -apple-system, sans-serif" font-size="48" font-weight="700" fill="#FFFFFF" text-anchor="start">Give AI the same context</text>
  <text x="48" y="148" font-family="system-ui, -apple-system, sans-serif" font-size="48" font-weight="700" fill="#FFFFFF" text-anchor="start">as the team</text>
  <circle cx="900" cy="80" r="36" fill="none" stroke="#4ADE80" stroke-width="2"/>
  <text x="900" y="88" font-family="system-ui, -apple-system, sans-serif" font-size="28" font-weight="700" fill="#4ADE80" text-anchor="middle">06</text>
</svg>

&nbsp;

## From everyone's chatbot to the team's shared context

Right now, every person on the team maintains their own AI context. They re-explain the product, the strategy, and the constraints at the start of every session. That is the individual version of the same problem the team already has with documents.

```mermaid
flowchart LR
  subgraph B["What most teams do"]
    H1["You re-explain<br/>the product"]
    A1["The tool answers"]
    E1["Session ends<br/>context evaporates"]
    H1 --> A1 --> E1
    E1 -.->|"tomorrow, again<br/>from scratch"| H1
  end
  subgraph G["What a shared workspace does"]
    F["Files in the repo<br/>strategy, decisions,<br/>research, prompts"]
    A2["Any tool reads them<br/>Claude, Cursor,<br/>scripts, agents"]
    N2["New findings<br/>written back"]
    F --> A2 --> N2
    N2 -.->|"the record compounds<br/>for humans and AI"| F
  end
```

<img src="assets/diag_06_augment.svg" alt="Session-based vs. repo-based AI" width="800"/>

&nbsp;

The shift is not "AI can read your strategy." The shift is that the team and its AI systems work from the same persistent context, instead of everyone maintaining separate chatbot sessions that evaporate at the end of every conversation.

In plain English: your AI starts every conversation from everything the team already knows, not from your memory of what to tell it.

&nbsp;

---

<sub>Beyond the Backlog · Productside · September 2, 2026</sub>

---

[&larr; Experiment](08_experiment.md) · [Next: Reuse &rarr;](10_reuse.md) · [Run](run.md)
