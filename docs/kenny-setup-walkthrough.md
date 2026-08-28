# Kenny's Setup Walkthrough

30-minute session. Dean on Mac, Kenny on Windows.
Goal: Kenny leaves with a working Claude Code → GitHub pipeline and one merged PR under his belt.

**What Kenny already has:** GitHub account (github.com/kennykranseler or similar).

**What Kenny needs installed before the call (or in the first 5 min):**

- Git for Windows — https://git-scm.com/downloads/win
- GitHub CLI — https://cli.github.com
- Claude Code — PowerShell: `irm https://claude.ai/install.ps1 | iex`

If these aren't installed yet, have Kenny do them while you talk through what's coming. All three are "next, next, finish" installers.

---

&nbsp;

## Phase 1 — Connect (10 min)

### 1.1 — Authenticate GitHub CLI

Kenny opens **PowerShell** (not CMD).

```powershell
gh auth login
```

It will ask:

| Prompt | Kenny picks |
|---|---|
| What account? | **GitHub.com** |
| Preferred protocol? | **HTTPS** |
| Authenticate how? | **Login with a web browser** |

A one-time code appears in the terminal. Kenny copies it, the browser opens, he pastes the code, and authenticates.

**Passkey note:** If Kenny's GitHub account doesn't have a passkey yet, GitHub will prompt him to set one up during this browser login. He should say yes — it replaces passwords with fingerprint/Windows Hello. If he already has one, it just works.

### 1.2 — Confirm the connection

```powershell
gh auth status
```

Should show: `Logged in to github.com account kennykranseler` (or whatever his handle is).

```powershell
git config --global user.name "Kenny Kranseler"
git config --global user.email "kenny's-github-email@example.com"
```

### 1.3 — Open Claude Code

```powershell
claude
```

First launch will ask Kenny to sign in to his Anthropic/Claude account (browser opens). Once signed in, he's in the Claude Code terminal.

**Confirm it can reach GitHub:**

```
Check whether Git and GitHub CLI are installed and whether
this computer is already authenticated with GitHub.
```

Claude should report all green. If `gh auth status` fails inside Claude Code, Kenny needs to close Claude Code, re-run `gh auth login` in PowerShell, then reopen `claude`.

**Phase 1 done when:** `gh auth status` works both in PowerShell and inside Claude Code.

---

&nbsp;

## Phase 2 — First Clone (5 min)

### 2.1 — Create a Projects folder

Still in Claude Code:

```
Create a folder called Projects in my home directory if it
doesn't exist, then clone the Productside Market Intelligence
Skills repository into it.
```

Or if Kenny prefers to pick the location:

```powershell
mkdir C:\Users\Kenny\Projects
cd C:\Users\Kenny\Projects
```

Then in Claude Code:

```
Clone the Productside Market Intelligence Skills repository
into this directory.
```

**What Kenny sees:** The repo downloads. 22 skills, 22 prompts, a CONSTITUTION.md, a CLAUDE.md.

### 2.2 — Look around

```
Read this repository and tell me what's here. What skills
are available? What rules does the CONSTITUTION say I
should follow?
```

Let Kenny read Claude's summary. This is the "AI gets the same context as the team" moment.

**Phase 2 done when:** Kenny has the repo locally and Claude can read it.

---

&nbsp;

## Phase 3 — First Branch + Edit (10 min)

### 3.1 — Create a branch

```
Make sure I'm on the main branch and it's up to date, then
create a new branch called kennys-first-edit.
```

Claude runs `git switch main`, `git pull`, `git switch -c kennys-first-edit`.

### 3.2 — Make a real edit

Pick something small and real. Options:

**Option A — Fix a typo or improve wording in a prompt:**

```
Open the battle card builder prompt and read it. Find one
thing you'd improve in the wording — a clearer instruction,
a better example — and make the change.
```

**Option B — Add a section to a skill:**

```
Open the battle card builder prompt. Add a section called
"Deal Context" after the competitor overview that asks the
user for their typical deal size and top three objections
they hear.
```

Let Kenny pick. The edit should be his, not yours.

### 3.3 — Review what changed

```
Show me exactly what I changed. Just the diff.
```

Kenny reads the diff. This is the first time he sees red/green line-level changes on his own work.

### 3.4 — Commit with a message

```
Help me write a commit message that explains what I changed
and why, then commit it.
```

Claude proposes a message, Kenny approves, the commit happens.

**Phase 3 done when:** Kenny has a commit on his branch with a meaningful message.

---

&nbsp;

## Phase 4 — First PR (5 min)

### 4.1 — Push and open the PR

```
Push my branch to GitHub and create a pull request.
Summarize what I changed and why in the PR description.
```

Claude runs `git push -u origin kennys-first-edit` then `gh pr create`.

A URL appears. Kenny clicks it. He sees his PR on github.com.

### 4.2 — Dean reviews (live)

Dean opens the PR on his machine. Shows Kenny:

- The diff tab (line-level changes)
- The conversation tab (where comments go)
- The "Files changed" view
- The content guard check (if it runs)

Dean leaves a comment, approves, merges.

### 4.3 — Kenny sees the merge

```
Check the status of my pull request.
```

Or Kenny just refreshes the browser. Merged. His name is on a commit in the Productside org.

**Phase 4 done when:** PR merged. Kenny has contributed to a public repository without typing a git command.

---

&nbsp;

## Troubleshooting

**"gh: command not found" inside Claude Code**
Close Claude Code, install GitHub CLI, reopen. Claude Code inherits the PATH from the shell it launched in.

**"Permission denied (publickey)"**
Kenny is trying SSH but only set up HTTPS. Fix:

```powershell
gh auth setup-git
```

This configures git to use `gh` as the credential helper for HTTPS.

**"fatal: not a git repository"**
Kenny isn't in the repo directory. In Claude Code:

```
Find the Productside Market Intelligence Skills folder on
this computer and go to it.
```

**Claude Code can't find Git Bash**
If Claude defaults to PowerShell and you want Bash, add to Claude Code settings:

```json
{
  "env": {
    "CLAUDE_CODE_GIT_BASH_PATH": "C:\\Program Files\\Git\\bin\\bash.exe"
  }
}
```

But PowerShell works fine for everything in this walkthrough. Don't bother unless something breaks.

**Passkey setup fails**
Fall back to a classic password + 2FA. GitHub will keep prompting for passkey setup on future logins; Kenny can do it later.

---

&nbsp;

## What Kenny walks away with

- [x] GitHub CLI authenticated via passkey/HTTPS
- [x] Claude Code connected to his GitHub identity
- [x] A local clone of the MI Skills repo
- [x] One branch created, one edit made, one commit with reasoning
- [x] One PR opened, reviewed, and merged
- [x] His name on a commit in a Productside repository

---

&nbsp;

<sub>Beyond the Backlog · Productside · Setup walkthrough for Kenny · August 29, 2026</sub>
