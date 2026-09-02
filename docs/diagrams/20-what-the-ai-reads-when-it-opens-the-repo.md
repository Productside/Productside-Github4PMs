# What the AI reads when it opens the repo

**Capability: Augment**

The file-level view: the AI assistant does not start from zero because the context is already there.

```mermaid
flowchart TD
  AI["AI assistant<br/>opens the repo"]
  CO["CONSTITUTION.md<br/>what it must not do"]
  CL["CLAUDE.md<br/>how to work here"]
  RE["README.md<br/>what this is about"]
  RS["evidence/<br/>sources and observations"]
  DC["decisions/<br/>what the team settled"]
  SK["skills/<br/>what it can run"]

  AI --> CO
  AI --> CL
  AI --> RE
  AI --> RS
  AI --> DC
  AI --> SK
```

**The line:** the team and its AI work from the same persistent memory. Re-explaining your product every morning is over.

---

---

[All diagrams](INDEX.md) · [Diagram source](../diagrams.md)
