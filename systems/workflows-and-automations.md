---
title: Workflows and automations
type: system
scope: [all]
tags: [automation, scheduled-task]
aliases: []
status: active
created: [today's date]
updated: [today's date]
related: []
---

# Workflows and automations

## Recurring automations
One line per scheduled task: name, when it runs, what it reads, what it writes. The daily tidy compares this list with the real schedule.

- Simonides daily tidy: every day at 08:45 [your time zone]. Reads the whole vault; writes fixes, today's daily note, CLAUDE.md's daily log and (from recipe 8) the Daily page. Prompt: systems/simonides-daily-dashboard/tidy-task-prompt.md.
