# Publishing the Market Intelligence Project

Audit of `Productside/Productside-Market-Intelligence-Skills` against `productside-launchkit` → `docs/02-governance/02-09-positioning-licensing-and-terms.md`. Run 2026-08-23.

**Why this matters to the webinar:** Play 5 ends with Kenny opening a pull request against this Project and Dean merging it live. That requires it to be public, with branch protection and a working content guard, before September 2. Target date: **Monday, August 31**.

---

## Status: clear to publish. What remains is configuration.

### What passed

- `sources/` is gitignored with an explicit "never committed" comment. **Zero source files tracked** — the provenance shelf held.
- No credentials, no local paths. The only scanner hits were `release_tools.py`'s own detector regexes.
- No TODOs or placeholders. `example.invalid` is correctly used as the reserved domain for synthetic examples.
- All 22 skills validate: frontmatter, portable projection, stage doctrine, templates, examples.
- `ROADMAP.md` opens *"Directional only. Nothing here is a commitment to build, maintain, or deliver."* — satisfies the positioning rule.
- `NOTICE.md` and `CONSTITUTION.md` rule 5 do the positioning work more thoroughly than the checklist requires, including the synthetic-examples declaration and the "validation utilities are not the deliverable" carve-out that keeps `scripts/` from being a vocabulary problem.
- `TRADEMARKS.md` present, linking the live Privacy Policy and Terms & Conditions.

### Do not "clean" these

The `deanpeters/product-manager-prompts` references throughout are **deliberate attribution**, documented in `NOTICE.md` as "by the same author and carried here with the same license." Removing them breaks the provenance chain.

---

## The IP question, correctly framed

An earlier version of this audit treated "has any of this been used in a paid course?" as a publication blocker. **That was wrong.** The Training Deliverables row in 02-09 describes a restriction on *the participant* — single-user, individual-use-only, no sharing. It does not limit Productside's right to publish material Productside owns.

The operative rule, per Dean:

> Material published for public training may be published. **Bespoke customer training materials may not.** Where something serves both, publish with public in mind and never identify a customer.

Applied here: no customer is named anywhere in this Project, and every example is synthetic and labeled. **It clears the bar.**

Attribution to `deanpeters/product-manager-prompts` is already handled in `NOTICE.md` — same author, same license, disclosed. Nothing to decide there.

*(The 02-09 table's wording invites the stricter misreading. Worth rewording that row to "materials whose rights are not solely Productside's.")*

---

## Four edits against the 02-09 checklist

- [ ] **`LICENSE` has no `Copyright (c) 280 Group LLC dba Productside` line** and no plain-language "as is" preamble. 02-09 requires both; the copyright currently lives only in `NOTICE.md`.
- [ ] **README lacks the canonical positioning statement.** It's in `NOTICE.md` instead, but README is where a stranger looks.
- [ ] **README lacks the plain-language "as is" disclaimer**, same reason.
- [ ] **The license is CC BY-NC-SA, not the documented CC BY-NC-ND default.** SA is the right call here and the webinar depends on it — ND forbids derivatives, which would make Kenny's contribution a license violation on camera. But the deviation is undocumented. Either record the exception in 02-09 or note it in this Project's README.

---

## Configuration blockers

- [ ] **Grant the `BLOCKED_TERMS` org secret to this repository.** The content guard fails closed on public repos without it — flip to public first and every workflow run goes red. Needs org admin; could not be verified from a local session.
- [ ] **Branch protection on `main`:** require a pull request, require one approval. Without it, Dean's review in Play 5 is ceremonial — Kenny could have pushed straight to main.
- [ ] **Add Kenny as a collaborator**; confirm the invite is accepted.
- [ ] **Confirm one workflow run is green** after the flip, before show day.

## Free while it is still private

- [x] **Rename — decided: no.** The `-Skills` suffix does positioning work. `Productside-Market-Intelligence` would read as a service Productside provides; `-Skills` reads as instructional material about the discipline, consistent with the ROADMAP's "not a data service" boundary. The name is also baked into the documented install command, so it should not change after publication.
- [ ] **`CODEOWNERS` points at `@Productside/maintainers` and `@Productside/owners`, and neither team exists** — both return 404, so GitHub silently ignores the file. Either create the teams or repoint it. Note that per 02-09 the *filename* is fine: it is an explicitly listed exception, a GitHub platform convention, not a description of Productside's business.
- [ ] **Commit authorship** on both commits is `Dean Peters <deanpeters@gmail.com>`. Once public it is permanent and visible on every commit. Two commits, so trivial to rewrite now.

---

## Sequence

1. Make the four checklist edits.
2. Grant `BLOCKED_TERMS`; flip public; confirm a green run.
3. Turn on branch protection; add Kenny; confirm the invite.
4. Rehearse the full PR flow in dry run #1, Wednesday August 26.
