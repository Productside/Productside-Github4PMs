# Two machines, one understanding

**Capability: Collaborate**

Windows and macOS, different paths, same repo. The objection this kills: *"I'd need the same setup as my engineers."*

```mermaid
flowchart LR
  K["Kenny · Windows<br/>C:\\Users\\...\\Documents"]
  R["The repo<br/>does not care"]
  D["Dean · Mac<br/>~/Documents"]

  K -->|"commit and push"| R
  D -->|"commit and push"| R
  R -.->|"pull"| K
  R -.->|"pull"| D
```

---

[All diagrams](INDEX.md) · [Runbook reading order](../diagrams.md)
