<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 160" width="960" height="160">
  <rect width="960" height="160" rx="12" fill="#1a1a1a"/>
  <text x="48" y="42" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="600" letter-spacing="3" fill="#4ADE80" text-anchor="start">WORKFLOW 2 · CONTEXT</text>
  <text x="48" y="100" font-family="system-ui, -apple-system, sans-serif" font-size="44" font-weight="800" fill="#FFFFFF" text-anchor="start">Clone a shared library</text>
  <text x="48" y="148" font-family="system-ui, -apple-system, sans-serif" font-size="44" font-weight="800" fill="#FFFFFF" text-anchor="start">&amp; install its skills.</text>
</svg>

&nbsp;

## Workflow 2 · Clone a shared library & install its skills

&nbsp;

**The Situation:**
Productside publishes a market intelligence skills library on GitHub. You want to bring it onto your machine, install the skills into your AI harness, and start using them.

**The PM Gain:**
One command gives you a versioned local copy of 22 skills and 22 prompts. You can read every skill, run them, and eventually improve them. Shared context compounds. Email attachments evaporate.

&nbsp;

> **The AI Prompt**
>
> ```
> Clone the Productside Market Intelligence Skills repository
> into my Projects directory and install the skills. Show me
> what's available.
> ```
>
> ---
>
> **The Invisible Machinery**
>
> `git clone https://github.com/Productside/Productside-Market-Intelligence-Skills.git` · `/plugin install mintel`

&nbsp;

**What lands on your machine:**
- `prompts/` — 22 standalone prompts including Battle Card Builder, SWOT, Five Forces, TAM/SAM/SOM
- `reference/` — frameworks, evidence standards, the do-not-invent list
- `CONSTITUTION.md` — the guardrails: no pretexting, no NDA-protected material, no scraping against terms
- The guardrails shipped with the tool. That's what good instructional material looks like.

&nbsp;

---

<sub>Beyond the Backlog · Productside · September 2, 2026</sub>

---

[← Previous](06_wf-setup.md) · [Next: Workflow 3 →](08_wf-collaborate.md) · [Run](run.md)
