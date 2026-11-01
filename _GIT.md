# How Simonides syncs

- **GitHub is the single true copy**: the private repository [your-github-username]/simonides.
- **~/Simonides on each computer is a local copy**, kept level with GitHub by the auto-sync (systems/simonides-autosync/), every five minutes and at login.
- **A chat on my computer** just edits the files; the sync does the rest. Do not push by hand unless I ask. Until the auto-sync is installed (recipe 5 of the guide), a chat commits and pushes when it finishes instead.
- **A cloud session or scheduled task** clones the repository, works, commits and pushes.
- **Four rules**: pull before you write; commit with a short message; push when done; never overwrite on a conflict.
- **On a conflict** the sync keeps both sides inside daily/ and carries on; anywhere else it stops and writes _SYNC-NEEDS-ATTENTION.md at the top of the vault. If that file exists, tell me before touching anything, and say "fix the Simonides sync conflict" to resolve it.
- Never force-push and never rewrite history.
