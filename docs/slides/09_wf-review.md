<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 160" width="960" height="160">
  <rect width="960" height="160" rx="12" fill="#1a1a1a"/>
  <text x="48" y="42" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="600" letter-spacing="3" fill="#4ADE80" text-anchor="start">WORKFLOW 4 · REVIEW</text>
  <text x="48" y="100" font-family="system-ui, -apple-system, sans-serif" font-size="44" font-weight="800" fill="#FFFFFF" text-anchor="start">Open a PR for</text>
  <text x="48" y="148" font-family="system-ui, -apple-system, sans-serif" font-size="44" font-weight="800" fill="#FFFFFF" text-anchor="start">Dean to approve.</text>
</svg>

&nbsp;

## Workflow 4 · Open a PR for Dean to approve

&nbsp;

**The Situation:**
Kenny's battle card improvements are committed on his branch. He does not want to silently overwrite the published skill. He wants Dean to see exactly what changed, discuss it, and approve before it becomes part of the library.

**The PM Gain:**
The team can challenge the proposed change before it becomes accepted, trusted context. Review is a gate, not a ritual. Dean sees a line-by-line diff, not a "hey, I updated the battle card" message in Slack.

&nbsp;

> **The AI Prompt**
>
> ```
> Push my improve-battle-card branch to GitHub and create a pull
> request to the Productside Market Intelligence Skills repo.
> Summarize what I improved and why. Do not merge it.
> ```
>
> ---
>
> **The Invisible Machinery**
>
> `git push -u origin improve-battle-card` · `gh pr create --fill`

&nbsp;

**What Dean sees as reviewer:**
- A line-by-line diff of exactly what Kenny changed in the skill
- Kenny's summary of why he made the changes
- A place to comment, approve, or request revisions
- The content guard runs automatically: no client names, no credentials, no oversized files

&nbsp;

---

<sub>Beyond the Backlog · Productside · September 2, 2026</sub>

---

[← Previous](08_wf-collaborate.md) · [Next: Workflow 5 →](10_wf-trace.md) · [Run](run.md)
