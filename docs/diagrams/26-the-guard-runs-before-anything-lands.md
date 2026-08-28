# The guard runs before anything lands

**Guardrails and governance**

```mermaid
flowchart LR
  C["A change<br/>is proposed"]
  G{"Content guard"}
  B1["Client or customer name"]
  B2["Credential-shaped string"]
  B3["Oversized or<br/>wrong file type"]
  R["Rejected,<br/>with the reason"]
  P["Allowed through<br/>to review"]

  C --> G
  G --> B1 --> R
  G --> B2 --> R
  G --> B3 --> R
  G -->|"clean"| P
```

**Dean's shape, verbatim:** the obvious concern is, could we accidentally expose something sensitive? Yes, if we were sloppy. Which is why we are not being sloppy.

---

[All diagrams](INDEX.md) · [Runbook reading order](../diagrams.md)
