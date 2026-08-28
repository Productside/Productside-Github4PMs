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

**Kenny never types a git command at any rung.** He says sentences.

---

---

[All diagrams](INDEX.md) · [Runbook reading order](../diagrams.md)
