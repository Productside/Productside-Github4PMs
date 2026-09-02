# The contribution loop

**Capability: Reuse**

The reusable contribution path.

```mermaid
flowchart LR
  C["Clone<br/>already done"]
  BR["Branch"]
  A["Add the artifact"]
  PU["Commit and push"]
  PR["Open the<br/>pull request"]
  G{"Content guard<br/>runs as a check"}
  RV["A teammate reviews"]
  M["Merge to main"]

  C --> BR --> A --> PU --> PR --> G
  G -->|"green"| RV
  G -->|"red"| A
  RV --> M
```

**The red path is not a failure state.** A guard that catches something early is worth more than a false green check.

---

[All diagrams](INDEX.md) · [Diagram source](../diagrams.md)
