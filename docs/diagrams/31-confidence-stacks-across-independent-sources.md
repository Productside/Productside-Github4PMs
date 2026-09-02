# Confidence stacks across independent sources

**Guardrails and governance**

Why six sources can be two disciplines — the trap the library exists to catch.

```mermaid
flowchart LR
  S1["Source A"]
  S2["Source B"]
  S3["Source C"]
  O["One origin<br/>a single press release"]
  I1["Discipline 1"]
  I2["Discipline 2"]
  H["Higher confidence"]
  L["Not higher confidence,<br/>just louder"]

  S1 --> O
  S2 --> O
  S3 --> O
  O --> L
  I1 --> H
  I2 --> H
```

**The line:** stars are not market share, issue volume is not pain severity, commit velocity is not customer value. And beware the squeaky wheel.

---

---

[All diagrams](INDEX.md) · [Diagram source](../diagrams.md)
