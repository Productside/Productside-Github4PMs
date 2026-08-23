# Kenny's Prep Track — 10 Days

**Today: Sunday, August 23, 2026. Show: Wednesday, September 2, 1PM ET.**

Kenny has a GitHub account he's never really used, and he's on **Windows**. Dean is on a **Mac**. By September 2 Kenny needs to be fluent in about nine moves and confident enough to get stuck on camera without freezing.

---

## The principle that governs this track

**Rehearse for fluency, not for polish.**

Kenny's genuine confusion is the show's content, not a defect in it. He is the audience's proxy.

**Rehearse until boring:**
- Where things live in the GitHub UI — the settings hunt is the #1 dead-air risk
- Creating a private repo, adding a file, editing, committing
- Viewing a file's history and opening a diff
- Adding a collaborator
- Saying a sentence to Claude Code that results in a clone, a commit, a branch, or a PR
- The fallback when any of it stalls

**Do not rehearse away:**
- "Why would I put that there?" — the question the audience has
- "That's not what I expected"
- Genuine surprise when something works
- Asking Dean to slow down

If Kenny arrives sounding like a co-host who already knows the answers, the show loses its best asset.

---

## The one trap that must die before show day

**Line endings.** Windows writes CRLF, macOS writes LF. If this isn't handled, **Kenny's pull request will show every line of the file as changed**, Dean's review will be unreadable, and there is no graceful way to explain it live.

Fix it during setup, in both repos:

```
* text=auto
```

in a `.gitattributes` file at the root. On Kenny's machine also set:

```
git config --global core.autocrlf true
```

**Verify it during dry run #1** by having Kenny push a change and Dean look at the diff on his Mac. If the diff shows only the lines that actually changed, it's handled. This is on the pre-flight checklist for a reason.

---

> The contribution loop Kenny rehearses most is diagrammed in [`diagrams.md`](diagrams.md).

## What Kenny must be able to do without thinking

1. Create a new private repo with a README
2. Add a file through the browser; edit one in place and commit with a message
3. **View a file's history and open a diff** — the payoff shot in Play 1
4. Add a collaborator to his repo
5. Open an Issue and reply to one
6. Ask Claude Code to clone a repo to a specific Windows path
7. Point Claude Desktop at a local folder and ask it about the contents
8. Ask Claude Code to commit and push
9. Ask Claude Code to create a branch and open a pull request

Not on the list, ever: typing a git command himself.

---

## The schedule

### Mon Aug 24 — Kenny solo, 45 min · *Account and browser*

- Sign in; **confirm 2FA is on.** Discovering this on show day is a disaster.
- Profile photo and display name — he'll be on screen.
- Create a private repo `kenny-practice`. Add three files. Edit one twice. **Open its history and read the diff.**
- Add Dean as a collaborator, then remove him.
- Delete the repo, to prove it's low-stakes.

### Tue Aug 25 — Kenny solo + Dean on call, 60 min · *The Windows toolchain*

**The highest-risk hour in the track.** Everything else assumes this worked.

- **Git for Windows** installed — Claude Code needs it.
- **Claude Code** installed and authenticated to GitHub.
- **Claude Desktop** installed, with access to a local folder.
- Set `git config --global core.autocrlf true`.
- Prove it end to end: ask Claude Code to clone any small public repo into `C:\Users\<kenny>\Documents\`, then ask Claude Desktop a question about a file in it.

**If this runs past 60 minutes, stop and get Dean on a screen share.** Setup friction here is exactly what must not surface live.

### Wed Aug 26 — **Dry run #1 with Dean, 90 min** · *No clock*

Full build, stopping whenever either wants to.

- Dean runs the 0:04 origin story once so Kenny has seen it.
- Kenny builds his private domain-research repo, clones it, points Claude Desktop at it.
- Dean joins as collaborator and contributes from his Mac. **Check the diff for the CRLF problem.**
- Kenny clones the market intelligence repo and runs one sweep.
- Kenny branches, adds the prefabbed artifact, opens a PR. Dean reviews and merges.
- **Write down every question Kenny asks.** Those are the live script — the ones he asks unprompted are the ones the audience has.

*Deliverables: Kenny's real questions, and a list of everything that broke.*

### Thu Aug 27 — Kenny solo, 45 min · *Rebuild alone*

Same sequence, from nothing, without Dean. Whatever he has to look up is the thing to drill.

### Fri Aug 28 — **Dry run #2 with Dean, 60 min** · *On the clock, recorded*

Timer running, screen shared as it will be, recorded.

- No stopping. If something breaks, **practice the recovery** rather than fixing it properly.
- Note where they ran long. Plays 1 and 3 are the donors; Play 5 is not.
- Watch it back separately. Uncomfortable, and the highest-value hour in the track.

### Sat–Sun Aug 29–30 — Buffer

Deliberately empty. Ten-day plans that use all ten days fail.

### Mon Aug 31 — Dean solo, 60 min · *Lock the risky parts*

- **Flip the market intelligence repo public**; confirm `BLOCKED_TERMS` is granted and one workflow run is green.
- **Branch protection on `main`**: require a pull request, require one approval.
- Confirm both collaborator invites are accepted, in both directions.
- Choose the sweep target company; run it; **save the output as the fallback.**
- Write the prefabbed artifact and hand it to Kenny.
- Confirm slot length and the CTA.

### Tue Sep 1 — Tech check together, 30 min

- Screen share on the actual platform, at the actual resolution.
- Browser zoom readable on a phone. Notifications off on both machines, verified.
- Recording tested.
- Demo accounts only, nothing else on screen — see `CONSTITUTION.md`, live-session addendum.

### Wed Sep 2 — Show day

- **60 minutes before:** delete and recreate Kenny's domain-research repo so it genuinely starts empty. The closing reveal depends on it.
- 20 minutes before: both online, Claude Desktop connected, Claude Code authenticated, staged text and fallback output open.

---

## Dean's job

Kenny is the student; Dean is the reason the student is safe to fail on camera.

- **Every failure recovery lands on the browser**, which always works. Dean's real job during the build is watching for the thirty-second mark and calling the drop before the audience feels the stall.
- **Narrate the stumbles as content, not apology.** "This is the part nobody shows you" turns a fumble into the most credible ninety seconds of the hour.
- **Never take the keyboard.** The moment Dean drives, it becomes an expert demoing a tool instead of a product manager learning one.

---

## If the track slips

Cut in this order:

1. Dry run #1 goes to 60 minutes instead of 90
2. Thu Aug 27 solo rebuild becomes optional
3. The live sweep in Play 3 becomes the saved output only
4. Drop to the 45-minute cuts and give the time to Q&A

**Do not cut:** the Tuesday toolchain session, dry run #2, the tech check, or the CRLF verification.
