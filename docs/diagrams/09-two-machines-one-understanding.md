# Two machines, one understanding

**Capability: Collaborate**

Different machines, different paths, same repo. The objection this helps with: *"I'd need the same setup as my engineers."*

```mermaid
flowchart LR
  K["Product Manager<br/>Windows<br/>C:\\Users\\...\\Documents"]
  R["The repo<br/>does not care"]
  D["Teammate<br/>Mac<br/>~/Projects"]

  K -->|"commit and push"| R
  D -->|"commit and push"| R
  R -.->|"pull"| K
  R -.->|"pull"| D
```

---

[All diagrams](INDEX.md) · [Diagram source](../diagrams.md)
