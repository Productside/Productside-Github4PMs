# Pull latest and see what moved

**Capability: Catchup**

The workflow a PM runs every morning: what changed since I was last here, and why.

```mermaid
flowchart LR
  PM["PM opens<br/>the repo"]
  PL["Pull latest<br/>from main"]
  DF["See the diff<br/>what changed overnight"]
  CM["Read commit messages<br/>who changed it and why"]
  IS["Check issues<br/>new questions or decisions"]
  PR["Check pull requests<br/>pending reviews"]
  OR["Oriented<br/>without a standup"]

  PM --> PL --> DF --> CM --> OR
  PM --> IS --> OR
  PM --> PR --> OR
```

**In plain English:** the standup you do not have to schedule. The repo is the standup.

---

---

[All diagrams](INDEX.md) · [Runbook reading order](../diagrams.md)
