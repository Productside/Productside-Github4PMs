# The same shape, in product terms

**Capability: Review**

Why a product manager should care about a mechanic built for source code.

```mermaid
flowchart LR
  M["main<br/>what the team<br/>currently agrees"]
  B["branch<br/>a proposed change<br/>nobody has agreed to yet"]
  R["pull request<br/>the conversation about<br/>whether to agree"]
  M2["main<br/>what the team<br/>now agrees"]

  M -->|"someone proposes"| B --> R
  R -->|"approved"| M2
  R -.->|"declined, with a reason<br/>anyone can read later"| B
```

**The line:** a branch is a proposal, a pull request is the argument, and a merge is the moment it becomes what the team believes. That is a product process that happens to be implemented in git.

---

[All diagrams](INDEX.md) · [Diagram source](../diagrams.md)
