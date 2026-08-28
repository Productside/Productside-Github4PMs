<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 160" width="960" height="160">
  <rect width="960" height="160" rx="12" fill="#1a1a1a"/>
  <text x="48" y="42" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="600" letter-spacing="3" fill="#4ADE80" text-anchor="start">WORKFLOW 5 · CONFIDENCE</text>
  <text x="48" y="100" font-family="system-ui, -apple-system, sans-serif" font-size="44" font-weight="800" fill="#FFFFFF" text-anchor="start">Commit the change</text>
  <text x="48" y="148" font-family="system-ui, -apple-system, sans-serif" font-size="44" font-weight="800" fill="#FFFFFF" text-anchor="start">with the reasoning.</text>
</svg>

&nbsp;

## Workflow 5 · Commit the change with the reasoning

&nbsp;

**The Situation:**
Kenny improved the battle card skill based on what he's seen work in real deals. He wants future-you to know this was a deliberate improvement based on field experience, not a mysterious edit.

**The PM Gain:**
The history preserves more than "a file changed." It preserves a useful, traceable point in the evolution of the team's practice. Six months from now, someone can see exactly what changed and why.

&nbsp;

> **The AI Prompt**
>
> ```
> Show me exactly what I changed in the battle card skill. Help
> me write a concise commit message that captures why, then
> commit it. Do not push until I approve.
> ```
>
> ---
>
> **The Invisible Machinery**
>
> `git diff` · `git add prompts/battle-card-builder-prompt.md` · `git commit -m 'Add deal-context section and sharpen objection handling based on field experience'`

&nbsp;

**In plain English:** you can revert a belief. You cannot revert a market. The record tells you which one you're looking at.

&nbsp;

---

<sub>Beyond the Backlog · Productside · September 2, 2026</sub>

---

[← Previous](09_wf-review.md) · [Next: Workflow 6 →](11_wf-experiment.md) · [Run](run.md)
