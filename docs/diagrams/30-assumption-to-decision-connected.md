# Assumption to decision, connected

**Guardrails and governance**

```mermaid
flowchart LR
  AS["Assumption<br/>we believe X"]
  EX["Experiment<br/>here is how<br/>we would know"]
  EV["Evidence<br/>cited, dated"]
  DE{"Were we<br/>right"}
  KE["Decision recorded<br/>and acted on"]
  WR["Wrong, recorded<br/>as such"]

  AS --> EX --> EV --> DE
  DE -->|"yes"| KE
  DE -->|"no"| WR
  WR -.->|"sharpens the<br/>next assumption"| AS
```

**The one most teams cannot do:** the bottom path. A finding that says *we were wrong* is only valuable if it is findable later.

---

[All diagrams](INDEX.md) · [Runbook reading order](../diagrams.md)
