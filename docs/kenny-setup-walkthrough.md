# Kenny's Setup Walkthrough

30-minute session. Dean on Mac, Kenny on Windows.
Kenny stays in **Claude Desktop** the entire time. Claude Code runs as an MCP server inside it — Kenny never sees a terminal after the one-time setup.

**What Kenny already has:** GitHub account, Claude Desktop installed.

---

&nbsp;

## Slack-Ready Commands

Copy-paste these to Kenny one at a time via Slack. Each block is one message.

---

**Message 1 — Open PowerShell**

> On your Windows machine, click the Start menu and search for **PowerShell**. Open it. You'll see a dark window with a blinking cursor. That's where the next six messages go.

---

**Message 2 — Install Git (in PowerShell)**

> In that **PowerShell window**, paste this and hit Enter. It'll install Git. Say yes if Windows asks for permission.
>
> `winget install Git.Git`

---

**Message 3 — Install GitHub CLI (in PowerShell)**

> Still in **PowerShell**. Paste this and hit Enter. It installs the GitHub command-line tool.
>
> `winget install GitHub.cli`

---

**Message 4 — Close and reopen PowerShell**

> Close that PowerShell window (just X it out) and open a fresh one the same way — Start menu, search "PowerShell." The new window picks up the stuff you just installed. The old one won't.

---

**Message 5 — Install Claude Code (in PowerShell)**

> In the **new PowerShell window**, paste this and hit Enter. It installs the engine that connects Claude Desktop to GitHub.
>
> `irm https://claude.ai/install.ps1 | iex`

---

**Message 6 — Log into GitHub (in PowerShell)**

> Still in **PowerShell**. Paste this and hit Enter:
>
> `gh auth login`
>
> It asks three questions. Pick these answers:
> 1. **GitHub.com** (not Enterprise)
> 2. **HTTPS**
> 3. **Login with a web browser**
>
> It gives you a one-time code. Your browser opens. Paste the code there.
>
> If GitHub asks about setting up a passkey (fingerprint / Windows Hello), say yes.

---

**Message 7 — Set your name (in PowerShell)**

> Still in **PowerShell**. Paste these two lines one at a time, hitting Enter after each. Use the email on your GitHub account.
>
> `git config --global user.name "Kenny Kranseler"`
>
> `git config --global user.email "kenny@example.com"`

---

**Message 8 — Confirm it all works (in PowerShell)**

> Still in **PowerShell**. Paste this and hit Enter. You should see your GitHub username and three version numbers. Screenshot it and send it to me.
>
> `gh auth status && git --version && claude --version`

---

**Message 9 — Wire Claude Desktop to Claude Code (in Claude Desktop, not PowerShell)**

> Now switch to **Claude Desktop** (the app, not the PowerShell window).
>
> Go to **Settings → Developer → Edit Config**. It opens a text file. Replace everything in that file with this, then save:
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
> Then **quit Claude Desktop completely** — not just close the window. Right-click the Claude icon in the system tray (bottom-right of your screen, near the clock) and click Quit. Then reopen it from the Start menu.

---

**Message 10 — Test it (in Claude Desktop)**

> Open **Claude Desktop** and start a new conversation. Type this into the **Claude Desktop chat box** (not PowerShell):
>
> `Check whether Git and GitHub CLI are installed and whether this computer is already authenticated with GitHub. Tell me who I'm logged in as.`
>
> It should show your GitHub username. Screenshot it and send it to me.

---

**That's it. Close PowerShell. You're done with it forever.** Everything from here happens in Claude Desktop.

---

&nbsp;

## Phase 0 recap — what the messages above install

| What | Why | How Kenny got it |
|---|---|---|
| Git for Windows | The version control engine | Message 2 |
| GitHub CLI (gh) | Authenticates with GitHub | Message 3 |
| Claude Code CLI | The MCP server Claude Desktop calls | Message 5 |
| gh auth | Passkey/browser login to GitHub | Message 6 |
| MCP config | Tells Claude Desktop to use Claude Code | Message 9 |

Kenny doesn't need to understand any of this. He just needs the screenshot from Message 10 showing his GitHub username.

---

&nbsp;

## Phase 2 — First Clone (5 min)

Everything from here happens in **Claude Desktop** — the app with the chat window, not PowerShell.

### 2.1 — Pull down the repo

Kenny types this into the **Claude Desktop chat box**:

```
Create a folder called Projects in my home directory if it
doesn't already exist. Then clone the Productside Market
Intelligence Skills repository from GitHub into it.
```

Kenny sees Claude report the clone. 22 skills, 22 prompts, a CONSTITUTION.md.

### 2.2 — Let the AI read the room

Still in the **Claude Desktop chat box**:

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

All of these go into the **Claude Desktop chat box**.

### 3.1 — Create a safe space to work

In the **Claude Desktop chat box**:

```
Go to the Market Intelligence Skills repo you just cloned.
Make sure I'm on the main branch and it's current, then
create a new branch called kennys-first-edit.
```

### 3.2 — Make a real change

Let Kenny pick. The edit should be his idea, not yours.

**Option A — Improve wording** (in the **Claude Desktop chat box**):

```
Open the battle card builder prompt and read it to me. Then
find one thing you'd improve in the wording — maybe a
clearer instruction or a better example — and make the
change.
```

**Option B — Add a section** (in the **Claude Desktop chat box**):

```
Open the battle card builder prompt. Add a section called
"Deal Context" after the competitor overview. It should ask
the user for their typical deal size, sales cycle length,
and the top three objections they hear from buyers.
```

### 3.3 — See what changed

In the **Claude Desktop chat box**:

```
Show me exactly what I changed. I want to see the
before-and-after diff.
```

This is Kenny's first line-level diff on his own work.

### 3.4 — Save it with the reasoning

In the **Claude Desktop chat box**:

```
Help me write a commit message that explains what I changed
and why. Then commit it.
```

Claude proposes a message. Kenny says "yes" or adjusts it. Committed.

**Phase 3 done when:** Kenny has a commit on a branch with a meaningful message.

---

&nbsp;

## Phase 4 — First Pull Request (5 min)

Still in the **Claude Desktop chat box** unless noted otherwise.

### 4.1 — Propose it to the team

In the **Claude Desktop chat box**:

```
Push my branch to GitHub and create a pull request to the
main repository. Summarize what I changed and why in the PR
description.
```

A PR URL appears in the chat. Kenny clicks it. He's looking at his pull request on **github.com in the browser** — the diff, the description, the review interface.

### 4.2 — Dean reviews and merges

Dean does this in a **web browser at github.com**. Shows Kenny:

- The **diff** — line-by-line changes
- The **conversation** — where reviewers comment
- The **content guard** check — automated guardrails ran
- The **merge button** — Dean approves and merges

### 4.3 — Kenny confirms

Back in the **Claude Desktop chat box**:

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
