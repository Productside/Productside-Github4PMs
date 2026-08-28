# The participation system

**Capability: Reuse**

The wider loop the contribution sits inside. Candidate closing visual for the whole show.

```mermaid
flowchart LR
  CV["Conversation<br/>someone has a problem"]
  SB["Structured submission<br/>a template, not a paragraph"]
  AC["Automated check<br/>the guard runs"]
  TR["Triage<br/>labelled and routed"]
  HD["Human decision<br/>yes, no, or not yet"]
  SH["Shipped"]
  RC["Visible record<br/>of what happened next"]

  CV --> SB --> AC --> TR --> HD --> SH --> RC
  RC -.->|"the next person<br/>starts informed"| CV
  HD -.->|"declined, with a reason<br/>anyone can read"| RC
```

**The line:** this is not repository literacy. It is designing a participation system.

**The caveat that goes with it:** to comment or contribute inside a private repo, a person has to be added to it. GitHub does not hand you open participation because you turned on Issues.

---

---

[All diagrams](INDEX.md) · [Runbook reading order](../diagrams.md)
