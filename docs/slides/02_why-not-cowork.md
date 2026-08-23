<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 160" width="960" height="160">
  <rect width="960" height="160" rx="12" fill="#1a1a1a"/>
  <text x="48" y="58" font-family="system-ui, -apple-system, sans-serif" font-size="16" font-weight="600" letter-spacing="3" fill="#4ADE80" text-anchor="start">THE OTHER OBVIOUS QUESTION</text>
  <text x="48" y="108" font-family="system-ui, -apple-system, sans-serif" font-size="44" font-weight="700" fill="#FFFFFF" text-anchor="start">Why not just a Claude</text>
  <text x="48" y="140" font-family="system-ui, -apple-system, sans-serif" font-size="44" font-weight="700" fill="#FFFFFF" text-anchor="start">project directory?</text>
</svg>

&nbsp;

Claude's Cowork projects give you a folder, a conversation history, and a way to share. That is genuinely useful, and it is where most people start. The question is where it stops.

| | **Claude Cowork project** | **GitHub repo** |
|---|---|---|
| **File hierarchy** | Yes. You organize folders and files. | Yes. Same idea, same flexibility. |
| **History** | Conversation history. You can scroll back and see what you asked and what Claude produced. | Commit history. Every change is a named, dated, attributed record of what changed and why. |
| **Who changed what** | Unclear. The conversation shows prompts and responses, but edits blur together. | Every commit names the author. Every line in every file can be traced to the person and moment that wrote it. |
| **Branching and experimentation** | No. You edit the files in place. If an experiment fails, you undo manually or lose the prior state. | Branch, try it, throw it away or merge it. The main copy never saw the experiment unless you chose to keep it. |
| **Review before changes land** | No gate. Anyone with access can change any file. | Pull requests. Someone reviews before it reaches the main copy. |
| **Works with tools beyond Claude** | Limited. The files live inside Claude's environment. Other AI tools, scripts, and automation cannot reach them easily. | One clone, every tool. Claude Code, Cursor, VS Code, scripts, CI, any AI assistant that can read a folder. |
| **Sharing and access control** | Share a link. Everyone with the link gets the same access. | Granular. Read-only, write, admin. Teams, individuals, public, private. |
| **Survives switching tools** | If you stop using Claude, the project stays in Claude. | The repo is yours. Host it anywhere. Download it. Move it. It does not depend on any one vendor. |

&nbsp;

A Cowork project is a workspace. A repo is a **system of record**.

Start in Cowork if that is where you are comfortable. But when the work matters enough that you need to know who changed what, when, and why, and you need other people and other tools to build on it, that is when you move to a repo.

Kenny started exactly this way. He could have kept his domain research in a Claude project. He chose a GitHub repo because he wants the commit history, the option to branch, and the freedom to share it later on his terms.

&nbsp;

---

<sub>Beyond the Backlog: Five GitHub Plays for Product Teams · Productside · September 2, 2026</sub>

---

[&larr; Why not SharePoint?](01_why-not-sharepoint.md) · [Next: How we got here &rarr;](03_how-we-got-here.md) · [Run](run.md)
