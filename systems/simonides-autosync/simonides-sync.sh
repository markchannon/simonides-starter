#!/bin/bash
# Simonides auto-sync: commit, pull, push ~/Simonides. Safe to run every few minutes.
# Installed by systems/simonides-autosync/README.md. Logs to ~/Library/Logs/simonides-sync.log.

VAULT="$HOME/Simonides"
LOG="$HOME/Library/Logs/simonides-sync.log"
FLAG="$VAULT/_SYNC-NEEDS-ATTENTION.md"
export PATH="/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin"
ts() { date '+%Y-%m-%d %H:%M:%S'; }
host() { scutil --get ComputerName 2>/dev/null || hostname; }

cd "$VAULT" 2>/dev/null || { echo "$(ts) vault not found at $VAULT" >> "$LOG"; exit 1; }

# A previous run hit a conflict and left it for a human. Do nothing until it is cleared.
if [ -f "$FLAG" ] || [ -d .git/rebase-merge ] || [ -d .git/rebase-apply ] || [ -f .git/MERGE_HEAD ]; then
  echo "$(ts) attention flag or unfinished rebase present, skipping" >> "$LOG"
  exit 0
fi

# 1. Commit local changes, if any.
git add -A
if ! git diff --cached --quiet; then
  git commit -qm "Auto-sync from $(host) $(ts)" >> "$LOG" 2>&1
fi

# 2. Pull with rebase. Offline: silently try again next time.
# A clash inside daily/ is a diary written from two places at once: keep both sides and carry on.
# A clash anywhere else is a real disagreement: stop and flag.
flag_and_stop() {
  git rebase --abort >> "$LOG" 2>&1
  {
    echo "# Simonides sync needs attention"
    echo
    echo "A pull from GitHub hit a merge conflict at $(ts) on $(host)."
    echo "Files: $1"
    echo "Auto-sync has paused on this computer. Nothing is lost: local commits are intact and GitHub is intact."
    echo
    echo "Ask Claude: \"fix the Simonides sync conflict\". It will pull, resolve the file, and delete this flag."
    echo "Auto-sync resumes as soon as this file is gone."
  } > "$FLAG"
  echo "$(ts) CONFLICT in $1: flagged, auto-sync paused" >> "$LOG"
  exit 1
}

keep_both() {
  # Strip the conflict markers, keeping the GitHub side then the local side, in that order.
  awk 'BEGIN{c=0} /^<<<<<<< /{c=1; next} /^=======$/{ if(c){next} } /^>>>>>>> /{ if(c){c=0; next} } {print}' "$1" > "$1.tmp" && mv "$1.tmp" "$1"
}

if ! git pull --rebase -q origin main >> "$LOG" 2>&1; then
  tries=0
  while [ -d .git/rebase-merge ] || [ -d .git/rebase-apply ]; do
    tries=$((tries+1)); [ "$tries" -gt 20 ] && flag_and_stop "rebase did not finish"
    conflicted=$(git diff --name-only --diff-filter=U)
    [ -z "$conflicted" ] && conflicted=$(git ls-files -u | awk '{print $4}' | sort -u)
    others=$(echo "$conflicted" | grep -v '^daily/' | grep -v '^$' || true)
    [ -n "$others" ] && flag_and_stop "$(echo $others)"
    for f in $conflicted; do
      keep_both "$f" && git add "$f"
      echo "$(ts) merged both sides of $f" >> "$LOG"
    done
    GIT_EDITOR=true git rebase --continue >> "$LOG" 2>&1 || true
  done
  if ! git merge-base --is-ancestor origin/main HEAD 2>/dev/null; then
    echo "$(ts) pull failed (offline?), will retry" >> "$LOG"
    exit 0
  fi
fi

# 3. Push.
if git push -q origin main >> "$LOG" 2>&1; then
  echo "$(ts) ok $(git rev-parse --short HEAD)" >> "$LOG"
else
  echo "$(ts) push failed, will retry" >> "$LOG"
fi
