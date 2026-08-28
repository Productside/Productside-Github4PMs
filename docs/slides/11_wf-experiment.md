<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 160" width="960" height="160">
  <rect width="960" height="160" rx="12" fill="#1a1a1a"/>
  <text x="48" y="42" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="600" letter-spacing="3" fill="#4ADE80" text-anchor="start">WORKFLOW 6 · CONFIDENCE</text>
  <text x="48" y="100" font-family="system-ui, -apple-system, sans-serif" font-size="44" font-weight="800" fill="#FFFFFF" text-anchor="start">Branch to improve</text>
  <text x="48" y="148" font-family="system-ui, -apple-system, sans-serif" font-size="44" font-weight="800" fill="#FFFFFF" text-anchor="start">what you know best.</text>
</svg>

&nbsp;

## Workflow 6 · Branch to improve what you know best

&nbsp;

**The Situation:**
Kenny ran the Battle Card skill and spotted gaps. He's an SME on battle cards. He wants to improve the skill based on what he knows works in real deals, but the rest of the team is still using the current version.

**The PM Gain:**
Kenny can rewrite the skill on a branch without touching what the team trusts today. His improvements live in parallel until the team is ready to review them. No "FINAL_v7" naming. No editing traffic jam.

&nbsp;

> **The AI Prompt**
>
> ```
> Go to my clone of the Market Intelligence Skills repo. Make sure
> main is current, then create a branch called improve-battle-card.
> Do not change main.
> ```
>
> ---
>
> **The Invisible Machinery**
>
> `git switch main` · `git pull` · `git switch -c improve-battle-card`

&nbsp;

**In plain English:** a branch is a safe place to be wrong. Kenny's improvements live on `improve-battle-card`. The team's published version stays on `main`. Both exist at the same time.

&nbsp;

---

<sub>Beyond the Backlog · Productside · September 2, 2026</sub>

---

[← Previous](10_wf-trace.md) · [Next: Workflow 7 →](12_wf-augment.md) · [Run](run.md)
