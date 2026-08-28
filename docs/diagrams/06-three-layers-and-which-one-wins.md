# Three layers, and which one wins

**Capability: Share**

Productside's own repo anatomy — not a GitHub feature. The mechanism is **precedence**.

```mermaid
flowchart TD
  CN["Constitution<br/>what we will not do<br/>CONSTITUTION.md"]
  CT["Contract<br/>how we work here<br/>CLAUDE.md"]
  CX["Context<br/>what we know and decided<br/>README and the files"]

  CN -->|"overrides"| CT
  CT -->|"overrides"| CX
  CX -.->|"a conflict escalates upward,<br/>never the other way"| CN
```

**Three files, three jobs, and the third one wins.** Say it here; call back to it in the Constitution capability.

---

[All diagrams](INDEX.md) · [Runbook reading order](../diagrams.md)
