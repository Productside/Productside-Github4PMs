# Three layers, and which one wins

**Capability: Share**

One useful repo anatomy pattern. The mechanism is **precedence**.

```mermaid
flowchart TD
  CN["Constitution<br/>what we will not do<br/>CONSTITUTION.md"]
  CT["Contract<br/>how we work here<br/>CLAUDE.md"]
  CX["Context<br/>what we know and decided<br/>README and the files"]

  CN -->|"overrides"| CT
  CT -->|"overrides"| CX
  CX -.->|"a conflict escalates upward,<br/>never the other way"| CN
```

**Three files, three jobs, and the third one wins.**

---

[All diagrams](INDEX.md) · [Diagram source](../diagrams.md)
