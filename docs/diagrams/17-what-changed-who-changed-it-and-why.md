# What changed, who changed it, and why

**Capability: Trace**

The workflow-level view: a Product Manager asks a question, the history answers it without a meeting.

```mermaid
flowchart LR
  Q["Someone asks:<br/>why does the brief<br/>say this now"]
  H["Open file history"]
  D["The diff<br/>what changed,<br/>line by line"]
  A["The author<br/>who changed it"]
  M["The message<br/>why they changed it"]
  AN["Answered<br/>without a meeting"]

  Q --> H --> D
  H --> A
  H --> M
  D --> AN
  A --> AN
  M --> AN
```

**In plain English:** the trace is only as good as the commit message. "Updated file" tells you nothing. "Added deal-context section after Q1 loss review" tells you everything.

---

---

[All diagrams](INDEX.md) · [Diagram source](../diagrams.md)
