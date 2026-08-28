# The library consumption loop

**Capability: Reuse**

How a team turns published assets into adopted practice, and how improvements flow back.

```mermaid
flowchart LR
  PB["Published library<br/>skills, templates,<br/>frameworks"]
  CL["Clone it"]
  RN["Run a skill<br/>on your domain"]
  OP["Structured output<br/>cited, formatted"]
  WR["Written into<br/>your repo"]
  FG["Find a gap<br/>or an improvement"]
  PR["Contribute back<br/>via pull request"]

  PB --> CL --> RN --> OP --> WR
  WR -.->|"over time"| FG --> PR
  PR -.->|"merged: the library<br/>improves for everyone"| PB
```

**In plain English:** tribal knowledge becomes team infrastructure. The next person who runs that skill gets your improvements automatically.

---

[All diagrams](INDEX.md) · [Runbook reading order](../diagrams.md)
