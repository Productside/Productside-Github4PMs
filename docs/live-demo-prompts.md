# Live Demo Prompts

Dean's cheat sheet for walking Kenny through the webinar demo.
Two windows visible: **Claude Code** (where Kenny types prompts) and **Terminal** (where output scrolls).

Repo used throughout: `Productside/Productside-Market-Intelligence-Skills`

---

&nbsp;

## 0 — PRE-CHECK (before going live)

Confirm Kenny's machine is ready. Do this off-camera.

**Terminal:**

```bash
git --version
gh --version
gh auth status
```

All three should return clean output. If `gh auth status` fails, run:

```bash
gh auth login
```

and complete the browser sign-in.

---

&nbsp;

## 1 — CLONE THE SKILLS LIBRARY

*Slide 15 · Share · WF2*

Dean says: "Kenny, pull down the Productside skills library."

**Claude Code prompt:**

```
Clone the Productside Market Intelligence Skills repository
into my Projects directory and install the skills so I can
use them.
```

**What the audience sees:** Claude runs `git clone`, the repo appears locally, skills get installed.

**If you need to do it manually (Terminal):**

```bash
cd ~/Projects
git clone https://github.com/Productside/Productside-Market-Intelligence-Skills.git
cd Productside-Market-Intelligence-Skills
```

---

&nbsp;

## 2 — RUN THE BATTLE CARD BUILDER

*Slide 18 · Collaborate · WF3*

Dean says: "Now use one of those skills on a real competitor."

**Claude Code prompt:**

```
Use the battle card builder skill. My product is Productside
Blueprint. The competitor is Pragmatic Institute. Focus on
corporate training engagements.
```

**What the audience sees:** Claude reads the prompt file, asks 2-3 setup questions, researches, writes a structured battle card to `output/`.

**Pause here** and let the audience read the output for a moment.

---

&nbsp;

## 3 — BRANCH TO IMPROVE THE SKILL

*Slide 22 · Review · WF6*

Dean says: "Kenny spotted something he'd improve. Let's do it safely."

**Claude Code prompt:**

```
Go to my clone of the Market Intelligence Skills repo. Make
sure main is current, then create a branch called
improve-battle-card so I can update the battle card builder
skill.
```

**What the audience sees:** Claude runs `git switch main`, `git pull`, `git switch -c improve-battle-card`. The branch name appears in the terminal prompt.

Dean says: "That branch is a safe place to be wrong. Main never changed."

---

&nbsp;

## 4 — MAKE THE IMPROVEMENT

*Still on the branch from Step 3*

Dean says: "Kenny, tell the AI what to fix."

**Claude Code prompt:**

```
Open the battle card builder prompt. Add a section called
"Deal Context" that asks the user for their typical deal size,
sales cycle length, and top three objections. Put it after
the competitor overview section.
```

**What the audience sees:** Claude edits the prompt file. The diff scrolls by.

---

&nbsp;

## 5 — COMMIT WITH THE REASONING

*Slide 21 · Review · WF5*

Dean says: "Save that with enough context that a future reader understands why."

**Claude Code prompt:**

```
Show me exactly what I changed in the battle card skill.
Help me write a concise commit message that captures the
what and the why.
```

**What the audience sees:** Claude runs `git diff`, shows the changes, proposes a commit message, commits.

Dean says: "That commit message is product reasoning, not a timestamp."

---

&nbsp;

## 6 — OPEN A PULL REQUEST

*Slide 19 · Collaborate · WF4*

Dean says: "Don't just push it. Propose it. Let me see the diff."

**Claude Code prompt:**

```
Push my improve-battle-card branch to GitHub and create a
pull request to the Productside Market Intelligence Skills
repository. Summarize what I changed and why.
```

**What the audience sees:** Claude runs `git push`, then `gh pr create`. A PR URL appears.

Dean says: "Now I can see exactly what Kenny proposes, line by line, before it becomes part of what the team trusts."

---

&nbsp;

## 7 — AI READS THE REPO CONTEXT

*Slide 24 · Experiment · WF7*

Dean says: "Watch what happens when the AI starts from the repo instead of from scratch."

**Claude Code prompt:**

```
Read this repository and tell me what skills are available,
what frameworks they use, and what rules I should follow.
```

**What the audience sees:** Claude reads `CONSTITUTION.md`, `CLAUDE.md`, the `prompts/` directory, the `reference/` directory. It summarizes the repo's structure, the guardrails, and the available skills.

Dean says: "The AI just got the same context as the team. Nobody pasted anything."

---

&nbsp;

## 8 — DEAN REVIEWS AND MERGES

*Slide 26 · Reuse · WF8*

Dean does this one. Switch to Dean's screen or do it from the browser at github.com.

**Browser:** Open the PR URL from Step 6. Review the diff. Leave a comment. Approve.

**Or Terminal (Dean's machine):**

```bash
gh pr review --approve
gh pr merge
```

Dean says: "The content guard passed. The changes are sound. Merged. Kenny's name is on a commit in a public repository. Not one git command typed."

---

&nbsp;

## 9 — MONDAY MORNING CATCHUP

*Not in the flow deck — use as a verbal callback during "What Change Looks Like" (slide 27)*

Dean says: "Monday morning, Kenny opens Claude Code and says..."

**Claude Code prompt:**

```
Bring me up to speed on the Productside Market Intelligence
Skills repo. Tell me what branch I'm on, what changed
recently, and what PRs were merged. Summarize the
consequential changes, not just filenames.
```

**What the audience sees:** Claude runs `git fetch`, `git log`, `gh pr list`. It tells Kenny what happened over the weekend in plain English.

Dean says: "That only works because we committed with meaningful messages, branched for experiments, and reviewed through pull requests."

---

&nbsp;

## RECOVERY PROMPTS

If something breaks live, these get you back on track.

**Claude Code isn't responding:**

```bash
claude --resume
```

**Wrong branch:**

```bash
git switch main
git pull
```

**Auth expired mid-demo:**

```bash
gh auth login --web
```

**Need to start fresh (nuclear option):**

```bash
cd ~/Projects
rm -rf Productside-Market-Intelligence-Skills
```

Then go back to Step 1.

---

&nbsp;

<sub>Beyond the Backlog · Productside · September 2, 2026</sub>
