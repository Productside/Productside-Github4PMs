# Kenny's Setup Walkthrough

30-minute session. Dean on Mac, Kenny on Windows.
Kenny stays in **Claude Desktop** the entire time. Claude Code runs as an MCP server inside it — Kenny never sees a terminal after the one-time setup.

**What Kenny already has:** GitHub account, Claude Desktop installed.

---

&nbsp;

## Slack-Ready Commands

Copy-paste these to Kenny one at a time. Each block is one message. Tell him to open PowerShell (search "PowerShell" in the Windows Start menu) and paste each one.

---

**Message 1 — Install Git**

> Paste this into PowerShell and hit Enter. It'll install Git. Say yes if it asks for permission.
>
> `winget install Git.Git`

---

**Message 2 — Install GitHub CLI**

> Same thing. This installs the GitHub command-line tool.
>
> `winget install GitHub.cli`

---

**Message 3 — Close and reopen PowerShell**

> Close PowerShell and open a fresh one so it picks up the new installs.

---

**Message 4 — Install Claude Code**

> Paste this. It installs the engine that connects Claude Desktop to GitHub.
>
> `irm https://claude.ai/install.ps1 | iex`

---

**Message 5 — Log into GitHub**

> Paste this. It'll ask you three questions — pick GitHub.com, HTTPS, and Login with a web browser. Then it gives you a code to paste in the browser.
>
> `gh auth login`
>
> If GitHub asks about setting up a passkey (fingerprint / Windows Hello), say yes.

---

**Message 6 — Set your name**

> Paste these two lines (one at a time). Use the email on your GitHub account.
>
> `git config --global user.name "Kenny Kranseler"`
>
> `git config --global user.email "kenny@example.com"`

---

**Message 7 — Confirm it all works**

> Paste this. You should see your GitHub username and version numbers. Screenshot it for me.
>
> `gh auth status && git --version && claude --version`

---

**Message 8 — Wire Claude Desktop to Claude Code**

> In Claude Desktop, go to **Settings → Developer → Edit Config**. Replace everything in that file with this, then save:
>
> ```
> {
>   "mcpServers": {
>     "claude-code": {
>       "command": "claude",
>       "args": ["mcp"]
>     }
>   }
> }
> ```
>
> Then **quit Claude Desktop completely** (not just close the window — right-click the icon in the system tray and quit) and reopen it.

---

**Message 9 — Test it**

> In a new Claude Desktop conversation, type this:
>
> `Check whether Git and GitHub CLI are installed and whether this computer is already authenticated with GitHub. Tell me who I'm logged in as.`
>
> It should show your GitHub username. Screenshot it for me.

---

**That's it. Close PowerShell. You're done with it.** Everything from here happens in Claude Desktop.

---

&nbsp;

## Phase 0 recap — what the messages above install

| What | Why | How Kenny got it |
|---|---|---|
| Git for Windows | The version control engine | Message 1 |
| GitHub CLI (gh) | Authenticates with GitHub | Message 2 |
| Claude Code CLI | The MCP server Claude Desktop calls | Message 4 |
| gh auth | Passkey/browser login to GitHub | Message 5 |
| MCP config | Tells Claude Desktop to use Claude Code | Message 8 |

Kenny doesn't need to understand any of this. He just needs the screenshot from Message 9 showing his GitHub username.

---

&nbsp;

## Phase 2 — First Clone (5 min)

### 2.1 — Pull down the repo

```
Create a folder called Projects in my home directory if it
doesn't already exist. Then clone the Productside Market
Intelligence Skills repository from GitHub into it.
```

Kenny sees Claude report the clone. 22 skills, 22 prompts, a CONSTITUTION.md.

### 2.2 — Let the AI read the room

```
Read that repository you just cloned and tell me what's
here. What skills are available? What rules does the
CONSTITUTION say I should follow?
```

This is the moment: the AI just got the same context as the team, from the repo, with no copy-paste.

**Phase 2 done when:** Kenny has the repo locally and Claude can summarize it.

---

&nbsp;

## Phase 3 — First Branch + Edit (10 min)

### 3.1 — Create a safe space to work

```
Go to the Market Intelligence Skills repo you just cloned.
Make sure I'm on the main branch and it's current, then
create a new branch called kennys-first-edit.
```

### 3.2 — Make a real change

Let Kenny pick. The edit should be his idea, not yours.

**Option A — Improve wording:**

```
Open the battle card builder prompt and read it to me. Then
find one thing you'd improve in the wording — maybe a
clearer instruction or a better example — and make the
change.
```

**Option B — Add a section:**

```
Open the battle card builder prompt. Add a section called
"Deal Context" after the competitor overview. It should ask
the user for their typical deal size, sales cycle length,
and the top three objections they hear from buyers.
```

### 3.3 — See what changed

```
Show me exactly what I changed. I want to see the
before-and-after diff.
```

This is Kenny's first line-level diff on his own work.

### 3.4 — Save it with the reasoning

```
Help me write a commit message that explains what I changed
and why. Then commit it.
```

Claude proposes a message. Kenny says "yes" or adjusts it. Committed.

**Phase 3 done when:** Kenny has a commit on a branch with a meaningful message.

---

&nbsp;

## Phase 4 — First Pull Request (5 min)

### 4.1 — Propose it to the team

```
Push my branch to GitHub and create a pull request to the
main repository. Summarize what I changed and why in the PR
description.
```

A PR URL appears in the chat. Kenny clicks it. He's looking at his pull request on github.com — the diff, the description, the review interface.

### 4.2 — Dean reviews and merges

Dean opens the same PR. Shows Kenny:

- The **diff** — line-by-line changes
- The **conversation** — where reviewers comment
- The **content guard** check — automated guardrails ran
- The **merge button** — Dean approves and merges

### 4.3 — Kenny confirms

Back in Claude Desktop:

```
What happened with my pull request? Was it merged?
```

Claude checks and confirms. Kenny's name is on a merged commit in the Productside org. Zero terminal commands typed.

**Phase 4 done when:** PR merged. Kenny is a contributor.

---

&nbsp;

## Troubleshooting

**Claude Desktop says "No tools available" or can't run commands**
The MCP config didn't load. Check:
1. The JSON is valid (no trailing commas, no typos in `"claude"`)
2. Claude Desktop was fully restarted (quit, not just closed)
3. `claude --version` works in PowerShell (the CLI is in PATH)

If `claude` isn't in PATH after install, Kenny may need to close and reopen PowerShell, or add it manually. The installer usually tells you.

**"gh: command not found" when Claude tries to use it**
Same PATH issue. Close Claude Desktop, open PowerShell, run `gh --version` to confirm it's installed, then reopen Claude Desktop. The MCP server inherits the PATH from when Claude Desktop launched.

**"Permission denied" or auth errors**
Kenny's `gh auth login` didn't stick, or the credential helper isn't set. In Claude Desktop:

```
Run gh auth setup-git to configure Git to use the GitHub
CLI for authentication, then try again.
```

**"fatal: not a git repository"**
Claude is looking at the wrong folder. In Claude Desktop:

```
Find the Productside Market Intelligence Skills folder on
my computer and work from there.
```

**Passkey setup fails at GitHub**
Fall back to password + 2FA. Kenny can set up the passkey later; it's not blocking.

**Nuclear restart**
If everything is sideways, have Kenny open PowerShell one more time:

```powershell
gh auth login
claude --version
```

Confirm both work, restart Claude Desktop.

---

&nbsp;

## What Kenny walks away with

- [x] Claude Desktop wired to Claude Code (permanent — survives restarts)
- [x] GitHub CLI authenticated via passkey/HTTPS
- [x] A local clone of the MI Skills repo
- [x] One branch, one edit, one commit with reasoning
- [x] One PR opened, reviewed, and merged
- [x] His name on a commit in a Productside repository
- [x] A workflow he can repeat tomorrow without opening a terminal

---

&nbsp;

<sub>Beyond the Backlog · Productside · Setup walkthrough for Kenny · August 29, 2026</sub>
