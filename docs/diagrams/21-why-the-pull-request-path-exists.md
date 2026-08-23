# Why the pull request path exists

**Play 4 · Constitution · 0:34**

Branch protection is what makes review real rather than ceremonial.

```mermaid
flowchart LR
  W["Someone wants<br/>to change main"]
  D1{"Direct push<br/>to main"}
  X["Blocked"]
  BR["Branch"]
  PR["Pull request"]
  RV["Review<br/>by another human"]
  M["Merged"]

  W --> D1 --> X
  X -.->|"the only<br/>way through"| BR
  W --> BR --> PR --> RV --> M
```

**Without this, the review in Play 5 is theatre** — the contributor could have pushed straight to main.

---

[All diagrams](INDEX.md) · [Runbook reading order](../diagrams.md)
