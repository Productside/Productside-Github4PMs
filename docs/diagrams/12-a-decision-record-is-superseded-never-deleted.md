# A decision record is superseded, never deleted

**Play 1 · Context · 0:09**

```mermaid
flowchart LR
  D1["0001<br/>we optimize<br/>for throughput"]
  N["New evidence<br/>arrives"]
  D2["0002<br/>we optimize for<br/>changeover time"]
  H["0001 stays,<br/>marked superseded<br/>by 0002"]

  D1 --> N --> D2
  D1 --> H
  D2 -.->|"links back to<br/>what it replaced"| H
```

**Why it matters:** you can revert a belief. You cannot revert a market. The record tells you which one you are looking at.

---

[All diagrams](INDEX.md) · [Runbook reading order](../diagrams.md)
