# Nothing is born public

**Guardrails and governance**

```mermaid
flowchart LR
  N["New Project"]
  PV["Private<br/>by default"]
  RV{"Review"}
  SC["Review, license,<br/>attribution, guard"]
  PB["Public,<br/>deliberately"]

  N --> PV --> RV
  RV -->|"not yet"| PV
  RV -->|"ready"| SC --> PB
```

**The line:** start private. Share deliberately. Public work deserves review, not vibes.

---

[All diagrams](INDEX.md) · [Diagram source](../diagrams.md)
