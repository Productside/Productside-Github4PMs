# Try a different approach without touching what the team trusts

**Capability: Experiment**

The PM-facing version: you do not need permission to be wrong, you need a safe place for it.

```mermaid
flowchart TD
  M["main<br/>the positioning<br/>the team trusts today"]
  B["branch<br/>a different positioning<br/>approach"]
  W["Work on it<br/>without touching main"]
  R{"Was it<br/>better"}
  MR["Merge it<br/>main improves"]
  DL["Delete the branch<br/>main never changed"]

  M -->|"create a branch"| B --> W --> R
  R -->|"yes"| MR
  R -->|"no"| DL
  MR -.->|"the team now<br/>trusts the new version"| M
```

**In plain English:** a branch is a safe place to be wrong. If the experiment fails, delete it. Main never changed.

---

---

[All diagrams](INDEX.md) · [Runbook reading order](../diagrams.md)
