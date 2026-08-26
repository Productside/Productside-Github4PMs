<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 160" width="960" height="160">
  <rect width="960" height="160" rx="12" fill="#0B3D2E"/>
  <text x="48" y="58" font-family="system-ui, -apple-system, sans-serif" font-size="16" font-weight="600" letter-spacing="3" fill="#4ADE80" text-anchor="start">01 · SHARE</text>
  <text x="48" y="108" font-family="system-ui, -apple-system, sans-serif" font-size="48" font-weight="700" fill="#FFFFFF" text-anchor="start">Share a complete</text>
  <text x="48" y="148" font-family="system-ui, -apple-system, sans-serif" font-size="48" font-weight="700" fill="#FFFFFF" text-anchor="start">product workspace</text>
  <circle cx="900" cy="80" r="36" fill="none" stroke="#4ADE80" stroke-width="2"/>
  <text x="900" y="88" font-family="system-ui, -apple-system, sans-serif" font-size="28" font-weight="700" fill="#4ADE80" text-anchor="middle">01</text>
</svg>

&nbsp;

## The difference

Your VP asks on Tuesday why the team dropped a feature last quarter. You spend the afternoon searching six tools to reconstruct your own rationale. That scavenger hunt is the cost of scattered context.

```mermaid
flowchart LR
  subgraph S["Scattered"]
    R["Research<br/>in Drive"]
    C["Chat<br/>in Slack"]
    AI["AI session<br/>in Claude"]
    D["Decision<br/>in an email"]
    P["PRD<br/>in Confluence"]
  end
  subgraph G["Shared"]
    RE["Research"]
    ST["Strategy"]
    DE["Decisions"]
    PR["Prompts"]
    TE["Templates"]
    subgraph REPO["One repository"]
      RE --- ST --- DE --- PR --- TE
    end
  end

  S -->|"each disconnected<br/>from the others"| X["Context<br/>rebuilt weekly"]
  G -->|"everything connected<br/>and findable"| Y["Context<br/>compounds over time"]
```

&nbsp;

<img src="assets/diag_01_share.svg" alt="Scattered artifacts vs. shared repository" width="800"/>

&nbsp;

Research, strategy, decisions, requirements, prompts, templates, and supporting evidence live together. Not in a folder. In a workspace where every piece knows its relationship to every other piece.

In plain English: the whole team stops re-explaining the product to each other and to their tools.

&nbsp;

---

<sub>Beyond the Backlog · Productside · September 2, 2026</sub>

---

[&larr; The frame](03_the-frame.md) · [Next: Collaborate &rarr;](05_collaborate.md) · [Run](run.md)
