<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 160" width="960" height="160">
  <rect width="960" height="160" rx="12" fill="#1a1a1a"/>
  <text x="48" y="42" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="600" letter-spacing="3" fill="#4ADE80" text-anchor="start">WORKFLOW 9 · COMMUNICATIONS</text>
  <text x="48" y="100" font-family="system-ui, -apple-system, sans-serif" font-size="44" font-weight="800" fill="#FFFFFF" text-anchor="start">Walk into the meeting</text>
  <text x="48" y="148" font-family="system-ui, -apple-system, sans-serif" font-size="44" font-weight="800" fill="#FFFFFF" text-anchor="start">knowing what changed.</text>
</svg>

&nbsp;

## Workflow 9 · Walk into the meeting knowing what changed

&nbsp;

**The Situation:**
It is Monday morning. Several people have worked in the MI Skills repo since you last looked. You do not want to reread every skill to discover what moved.

**The PM Gain:**
Enter the conversation knowing exactly what changed: Kenny improved the battle card, Dean merged it, the content guard passed. You know this because the commit messages, the PR discussion, and the review trail are all there. No reconstructing history from chat.

&nbsp;

> **The AI Prompt**
>
> ```
> Bring me up to speed on the Productside Market Intelligence
> Skills repo. Tell me what branch I'm on, what changed recently,
> and what PRs were merged. Summarize the consequential changes,
> not just filenames.
> ```
>
> ---
>
> **The Invisible Machinery**
>
> `git fetch` · `git log --oneline --decorate -10` · `gh pr list --state merged --limit 5`

&nbsp;

This is the payoff of all the other workflows. Because the team committed with meaningful messages, branched for experiments, and reviewed through pull requests, the AI can reconstruct the story, not just the file list.

&nbsp;

---

<sub>Beyond the Backlog · Productside · September 2, 2026</sub>

---

[← Previous](13_wf-reuse.md) · [Next: Prompts Worth Stealing →](15_prompts-worth-stealing.md) · [Run](run.md)
