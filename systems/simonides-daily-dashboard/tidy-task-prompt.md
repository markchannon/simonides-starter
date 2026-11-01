---
title: Daily tidy, the scheduled task prompt
type: system
scope: [all]
tags: [simonides, scheduled-task]
aliases: [tidy prompt]
status: active
created: [today's date]
updated: [today's date]
related: ["[[workflows-and-automations]]"]
---

# Daily tidy, the scheduled task prompt

The exact text the scheduled task "Simonides daily tidy" runs (recipe 7 of the guide creates the task from it). This file is the record; the task is a copy. When the task changes, change this file first, give it a new version, then update the task to match. Never create a second task for the same job.

**Page link:** [the Simonides Daily page link, once published in recipe 8]

Two parts switch themselves on: answers and the daily page run once the page link above is a real link (they skip while it is still in square brackets), and the monthly audit starts once Simonides has a month of daily notes.

## Prompt (version 1)

```text
Run the daily tidy for my Simonides. This runs in the cloud; do not look for anything on my computer.

ACCESS. Clone my private GitHub repository [your-github-username]/simonides to /home/claude/simonides (if it is already there, pull instead). If the clone is refused, stop, change nothing, and report: "Simonides clone refused: recreate this task from a chat with the repository attached." Treat that folder as the vault wherever a note says ~/Simonides. Set git user.name "Simonides daily tidy".

PAGE. Read the "Page link" line in systems/simonides-daily-dashboard/tidy-task-prompt.md. If it is a real link, my Daily page is published and the ANSWERS and DAILY PAGE steps below run. If it is still in square brackets, skip them without comment.

DAILY NOTE. daily/<today>.md is shared with other jobs and with my captures. Never rewrite it. Read it first and append your account under your own heading "## Simonides daily tidy, <time>".

ANSWERS (only when the page is published; do this first). Read the "answers" collection in the page's database. For each record, act on my answer exactly as if I had said it in a chat: the title is the question, the link is the note that holds the detail. File it in the right note with today's date; if the question is an unticked line in records/audit-open-items.md, tick that line with today's date. List it under Done with my answer quoted, and delete the record. An answer you cannot act on safely (it asks for a deletion, a change outside Simonides, or you cannot tell what it means) stays in the database and becomes a new plain question for me. If the page has no database yet, skip this.

THE WORK. Read _CONVENTIONS.md and follow it. Then:
1. Index: every note except daily notes is listed in CLAUDE.md with one line; add missing lines, remove lines for notes that no longer exist. Keep CLAUDE.md an index only, short lines, no content.
2. Inbox: file everything in _inbox into the right folder as a proper note, then empty it.
3. Frontmatter: every note has it, with a type from the list in _CONVENTIONS.md; fix what is missing. README.md files, CLAUDE.md, START-HERE.md, LICENSE.md, daily notes, everything in skills/ and the files at the top starting with _ are not notes; leave them out of this check and the index check.
4. Links: fix wikilinks that point nowhere; link notes that nothing links to into their overview page.
5. Duplicates and stale facts: merge duplicate notes (check aliases first), fix facts you can see are out of date, and list anything you are not sure about as a question for me.
6. Deadlines: list action items whose date has passed.
7. Unconfirmed notes: run python3 systems/simonides-checks.py review to rebuild systems/confirm-queue.md from everything tagged #provisional, and report the count and the oldest three.
8. Skills: compare the skills I installed myself (not the ones built into Claude) with _SKILLS.md and add a row for any that are missing.
9. Scheduled tasks: compare my tasks with the list in systems/workflows-and-automations.md and add any that are missing.
10. Artifacts: compare my artifacts with projects/artifacts-index.md and add any that are missing, under "found by the tidy".
11. Recent daily notes: skim the last few days for anything that should have become or updated a note, and do it.
12. Numbers: after your changes, run python3 systems/simonides-checks.py all and quote its numbers. Never count by eye.

CODE PROJECTS. systems/code-projects.md lists my code repositories (websites, apps, tools), each living in its own GitHub repository apart from Simonides. Skip this step while its table is empty. For each repository in it: read its commits from the last 24 hours (gh api "repos/<owner>/<repository>/commits?since=<24 hours ago>") and its last push date (gh api repos/<owner>/<repository> -q .pushed_at). For each one that changed, add one line to that note's "Code activity log" (date, repository, what changed in plain words, from the commit messages) and list it under Done. A repository that answers 403 or 404 was not attached to the chat this task was created in: ask me one plain question, "Your daily tidy cannot see <repository>. Shall we recreate it from a chat with that repository attached (recipe 7 of the guide)?" Never change anything in a code repository; read only. If a commit shows that a row's "what it is" or live address is out of date, correct the row and say so under Done.

MONTHLY AUDIT. Only once the oldest note in daily/ is at least 28 days old. Then, on the 2nd of each month (or the first run after it, if records/audit-open-items.md has no "## Audit of" heading for this month yet): write down what is true today from CLAUDE.md, my scheduled tasks, my artifacts and the last month of daily notes. Split the vault into four slices by folder and give each slice to a separate reviewer working in parallel. Each reviewer fixes stale facts in place with the smallest change, never deletes, and lists the questions only I can answer. Append those questions to records/audit-open-items.md under "## Audit of <date>", one unticked line each with a recommendation (create the file the first time). Never re-add a question that is still open.

DAILY PAGE (only when the page is published; do this last). Edit only the data block between /* ===== DATA ===== */ and /* ===== END DATA ===== */ in systems/simonides-daily-dashboard/simonides-daily.html, never the design. Use exactly these fields. sample: false. date ("YYYY-MM-DD"), dateLabel (for example "Thursday 15 January") and rebuilt ("HH:MM", my time) for now; rebuiltBy: "Simonides daily tidy". repoUrl: my Simonides repository's GitHub address. vaultNotes: the note count from the checker. dailyNote: the path of today's daily note. decisions: a list of this run's questions for me, each item {kind, title, q, rec, link, age}: kind is one of "Yes / No", "One line", "Your call", "You do it", "Have a look"; title is the question as one plain sentence; q is one or two sentences of context; rec is your recommendation, starting with what you would do; link is the path of the one note that holds the detail (add links, a list of paths, when it is about several notes); age is "today" or "N days". When the confirm queue is not empty, add one item with its count, linking to systems/confirm-queue.md. audit: every unticked line in records/audit-open-items.md as the same item shape, using the line's own question as the title word for word; auditDate: the date of the latest "## Audit of" heading, or "" when there is none. apps: the "Needs you" lines my app syncs wrote in today's daily note, same item shape. done: a list of {title, detail, link} for what this run and the syncs did, plus yesterday's answered items for one day. jobs: one {name, when, status, at, line} per scheduled task, where status is "ran", "due", "failed" or "idle", at is when it last ran, and line is one plain sentence of what it did. code: one {repo, count, line, lastPush} per code repository that changed in the last 24 hours ("owner/name", the number of commits, the commit messages in plain words, the push time). repos: the JSON printed by python3 systems/simonides-daily-dashboard/repos-from-note.py, given a JSON file of {"owner/name": last push date} as its argument. inventory: four cells {label, value, note}: Notes (from the checker), Skills (rows in _SKILLS.md), Scheduled tasks (my tasks), Code projects ("N of M readable"); note is "match" or what is missing. tree: the JSON object printed by python3 systems/simonides-daily-dashboard/vault-tree.py. explainer: the text of _EXPLAINER.md without its frontmatter. Then run python3 systems/simonides-daily-dashboard/vault-tree.py --notes > /home/claude/notes.json and republish the page to its link with that file published beside it as vault/notes.json. If the publish is refused because you have not read the page in this run, read it and publish again. People notes, organisation notes and anything private never go on the page; the script already leaves them out.

RULES. Never delete a note; flag it instead. The only things you may remove: an inbox item once it is filed, a duplicate note once merged into the other (keep its name as an alias), and answer records you have filed. Never store secrets. Plain words, no jargon. When you can safely do something yourself, do it and list it as done; only ask me when it needs my knowledge or my decision, and then ask one plain question.

FINISH. Add one short line about this run to CLAUDE.md under a "Daily log" heading and keep only the last seven lines there; older days live in the daily notes. Commit with the message "Simonides daily tidy <date>: <one line>", pull with rebase, push, and quote the commit. Report in bullets: what you fixed, what needs me (one question each), what has not changed.
```
