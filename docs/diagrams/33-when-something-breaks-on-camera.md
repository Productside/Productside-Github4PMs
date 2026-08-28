# When something breaks on camera

**The spine and the runbook**

The thirty-second rule. Dean's real job during the build.

```mermaid
flowchart TD
  B["Something<br/>stalls"]
  T{"Thirty<br/>seconds"}
  N["Dean narrates<br/>the hunt out loud"]
  F["Drop to the fallback<br/>browser, or the<br/>rehearsed saved output"]
  S["Say what happened,<br/>and keep going"]

  B --> T
  T -->|"under"| N
  T -->|"over"| F --> S
  N -.->|"still stuck"| F
```

**Never re-run a failed step live.** One attempt, then fallback. Owning it out loud is stronger than hiding it.

---

[All diagrams](INDEX.md) · [Runbook reading order](../diagrams.md)
