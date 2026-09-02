# Which materials may go public

**Guardrails and governance**

Productside's own classification. The category decides the answer far more often than the platform does.

```mermaid
flowchart TD
  Q["Something you<br/>want to publish"]
  C1{"Did a client<br/>bring it"}
  C2{"Was it created during<br/>a client engagement"}
  C3{"Are the rights<br/>solely ours"}
  NO1["No · client IP,<br/>never ours to license"]
  NO2["No · vests in the client<br/>as work made for hire"]
  NO3["No · not ours<br/>to grant alone"]
  YES["Yes, after<br/>publication review"]

  Q --> C1
  C1 -->|"yes"| NO1
  C1 -->|"no"| C2
  C2 -->|"yes"| NO2
  C2 -->|"no"| C3
  C3 -->|"no"| NO3
  C3 -->|"yes"| YES
```

**And the rule that governs the gray middle:** material published for public training may be published; bespoke customer material may not. Where something serves both, publish with public in mind and never identify a customer.

---

[All diagrams](INDEX.md) · [Diagram source](../diagrams.md)
