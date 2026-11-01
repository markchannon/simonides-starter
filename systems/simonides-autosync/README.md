---
title: Simonides auto-sync
type: process
scope: [all]
tags: [simonides, github, sync, automation]
aliases: [autosync, sync conflict]
status: active
created: [today's date]
updated: [today's date]
related: ["[[_GIT]]"]
---

# Simonides auto-sync (one per computer)

**What it does.** Every five minutes and at login: commit anything changed in ~/Simonides, pull from GitHub, push. You never open GitHub. Cloud jobs push to GitHub; the next tick pulls their work down.

**On a conflict.** A clash inside daily/ keeps both sides and carries on (the log says `merged both sides of daily/...`). A clash anywhere else stops the sync and writes _SYNC-NEEDS-ATTENTION.md at the top of the vault. Say "fix the Simonides sync conflict" to resolve it.

**Where things are**
- The real script, inside the vault so it syncs like any file: systems/simonides-autosync/simonides-sync.sh
- The launcher that runs a fresh copy of it: ~/bin/simonides-sync.sh (from launcher.sh here)
- The launch agent: ~/Library/LaunchAgents/com.simonides.sync.plist (from the file here)
- The log: ~/Library/Logs/simonides-sync.log

## Install (once per Mac, from the Code tab, your computer)
Say: "Install the Simonides auto-sync by following ~/Simonides/systems/simonides-autosync/README.md. Do every step yourself, confirm each one, and show me the last five lines of the log at the end."

Claude then:
1. Sets a git name and email for this computer if none is set.
2. Makes sure git can reach GitHub without asking: checks the GitHub command-line tool is signed in (if it is missing, installs it into your home folder, so no administrator password is needed, and walks you through one browser approval), then sets it up for git.
3. Checks ~/Simonides points at your private repository and tracks main.
4. Copies launcher.sh to ~/bin/simonides-sync.sh and makes it runnable.
5. Copies com.simonides.sync.plist to ~/Library/LaunchAgents/, replacing HOME_PLACEHOLDER with your home folder, and loads it.
6. Runs the sync once and shows the log; expect a line ending `ok <commit>`.
7. Checks the job is scheduled.

**On a PC:** ask for "the Windows version of the Simonides auto-sync, using Task Scheduler instead of a launch agent, running the same script with Git for Windows, and logging to my user folder".

## Uninstall
Say: "Uninstall the Simonides auto-sync on this computer."
