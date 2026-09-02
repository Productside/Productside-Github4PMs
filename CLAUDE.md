# CLAUDE.md

Working contract for AI assistance in this public-facing webinar companion repo.

## Project purpose

This repo supports Productside's **Beyond the Backlog** webinar by giving Product Managers a practical reference for using GitHub at work.

The durable teaching point is not "learn Git." The point is that product teams can use a repository as shared, versioned, AI-readable memory for research, decisions, experiments, reviews, and reusable practices.

## Audience

Write for Product Managers, product leaders, consultants, analysts, designers, founders, students, and AI-curious builders. Many of them cannot code, are weak at it, or are actively nervous around developer tools. They are still smart, busy people doing real product work.

Prefer:

- Plain English.
- Concrete examples.
- Short setup paths.
- Clear safety boundaries.
- Product-team language.
- Explanations of why a workflow matters before explaining mechanics.
- Browser-first wins before local setup.
- AI-assisted prompts that let the reader stay in the Product Manager seat.

Avoid:

- Treating GitHub as only an engineering tool.
- Teaching command-line Git for its own sake.
- Making clone, install, or terminal steps the first win.
- Publishing private company, customer, learner, participant, or client material.
- Describing Productside's materials as software, an app, or a maintained product.

## Seven workflows

Keep public content aligned to these seven workflows:

| Workflow | Job |
|---|---|
| **Share** | Give product context one durable home |
| **Collaborate** | Make questions, decisions, and disagreement visible |
| **Review** | Check proposed changes before they become trusted context |
| **Trace** | Preserve what changed, who changed it, and why |
| **Experiment** | Explore alternatives without breaking the trusted version |
| **Augment** | Let AI read the same context as the team |
| **Reuse** | Turn useful practices into assets others can adopt |

## Content boundaries

Keep public files focused on reusable teaching material, examples, diagrams, and safety guidance. Do not add private operational material, restricted third-party material, sensitive company context, personal data, credentials, or large binary artifacts.

## Repo anatomy

- `README.md`: public front door and scope.
- `docs/field-guide.md`: practical attendee reference.
- `docs/diagrams.md`: source of truth for the diagram set.
- `docs/diagrams/`: generated one-file-per-diagram pages and assets.
- `docs/blog-beyond-the-backlog.md`: long-form framing.
- `scripts/split-diagrams.py`: regenerates the diagram pages from `docs/diagrams.md`.

## Working rule

When editing, keep changes small and reviewable. If a file contains material that is not clearly public-safe, reduce or remove it before polishing it.
