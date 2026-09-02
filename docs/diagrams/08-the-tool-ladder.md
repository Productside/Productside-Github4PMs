# The tool ladder

**Capability: Share**

Three rungs. The browser is the floor, and every failure recovery drops back to it.

```mermaid
flowchart TD
  B["Rung 1 · The browser<br/>create, edit, commit, review<br/>always works"]
  CD["Rung 2 · Claude Desktop<br/>reads and writes files<br/>in one local folder<br/>no git, no auth"]
  CC["Rung 3 · Claude Code<br/>clone, commit, push,<br/>branch, pull request"]

  B --> CD --> CC
  CC -.->|"if anything stalls"| B
  CD -.->|"if anything stalls"| B
```

**The adoption idea:** the person using the workflow can ask for outcomes in plain English while the tool handles the mechanics.

---

---

[All diagrams](INDEX.md) · [Diagram source](../diagrams.md)
