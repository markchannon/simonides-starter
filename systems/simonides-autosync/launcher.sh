#!/bin/bash
# Installed as ~/bin/simonides-sync.sh. Runs a fresh copy of the script that lives in the vault,
# so a change to the vault script reaches every computer through the sync itself.
SRC="$HOME/Simonides/systems/simonides-autosync/simonides-sync.sh"
TMP="$(mktemp "${TMPDIR:-/tmp}/simonides-sync.XXXXXX")" || exit 1
cp "$SRC" "$TMP" 2>/dev/null || { echo "$(date '+%Y-%m-%d %H:%M:%S') vault script missing at $SRC" >> "$HOME/Library/Logs/simonides-sync.log"; exit 1; }
/bin/bash "$TMP"; status=$?
rm -f "$TMP"
exit $status
