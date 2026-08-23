# The contribution loop

**Play 5 · Community · 0:40**

The segment Kenny rehearses most.

```mermaid
flowchart LR
  C["Clone<br/>already done<br/>in Play 3"]
  BR["Branch"]
  A["Add the artifact"]
  PU["Commit and push"]
  PR["Open the<br/>pull request"]
  G{"Content guard<br/>runs as a check"}
  RV["Dean reviews<br/>on his Mac"]
  M["Merge to main"]

  C --> BR --> A --> PU --> PR --> G
  G -->|"green"| RV
  G -->|"red"| A
  RV --> M
```

**The red path is not a failure state.** A guard that catches something on camera is worth more than a green tick.

---

[All diagrams](INDEX.md) · [Runbook reading order](../diagrams.md)
