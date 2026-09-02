# Two repos, two jobs

**Capability: Share**

A common workplace pattern: private product context stays private, while reusable team assets can be published after review.

```mermaid
flowchart LR
  subgraph L["Local workspace"]
    KR["Domain research<br/>PRIVATE, stays private<br/>what the team believes"]
    ML["Shared skills library<br/>cloned copy<br/>skills, prompts,<br/>templates"]
  end
  subgraph O["Team or company org"]
    MI["Reusable library<br/>PUBLIC or internal<br/>published after review"]
  end
  R["Reviewer"]

  MI -->|"clone, once"| ML
  ML -->|"run a sweep,<br/>write the evidence"| KR
  R -->|"questions and<br/>review"| KR
  ML -->|"branch and<br/>pull request"| MI
  MI -.->|"review and merge"| R
```

---

[All diagrams](INDEX.md) · [Diagram source](../diagrams.md)
