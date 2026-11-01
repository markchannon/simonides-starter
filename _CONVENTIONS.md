---
title: Simonides conventions
type: reference
scope: [all]
tags: [simonides, rules]
aliases: [rules, operating manual]
status: active
created: [today's date]
updated: [today's date]
related: ["[[CLAUDE]]", "[[_TEMPLATE]]"]
---

# Simonides conventions

The rules every chat, skill and scheduled job follows. Read before writing anything. These are starter rules from the Simonides starter kit: change anything that is not how you think, so it sounds like your rules.

**My worlds** (the scope label on every note): [your worlds, for example personal, work, side-project], plus `all`.

## 1. Notes
1. **Notes are entities, not facts.** One note per person, company, project or idea, which grows over time. Never make a note for a single fact; add the fact to the note it belongs to.
2. **One home per note.** Each note lives in one folder; connections across folders are made with tags and wikilinks (links between notes, written with double square brackets), never by copying.
3. **One fact lives in one note.** Everything else links to it. Duplicated text drifts.
4. **Frontmatter on every note**, from _TEMPLATE.md. Types are a closed list: person, organisation, business, project, process, reference, record, story, daily, system.
5. **Folders.** context is my world · people and organisations are who I know · projects are what I am doing · records are what happened · systems are how it runs · library is what I have read · daily is the diary. Quick test: is it about my world? context. Who I know? people or organisations. What I am doing? projects. What happened? records. How it runs? systems. Someone else's knowledge? library.

## 2. Capturing ("remember this")
6. Search CLAUDE.md and the aliases for an existing note first. If one exists, play it back and ask whether to add detail, correct it or leave it.
7. Otherwise file a new note from the template in the right folder, fill the frontmatter, turn relative dates into real dates, link it to related notes and to the overview page for that world, add one line to CLAUDE.md, and log the capture in today's daily note.
8. Mid-flow or unclear: drop it in _inbox now and file it properly after.

## 3. Retrieving ("what do I know about X", "use my brain")
9. Read CLAUDE.md, open the note it points to, follow its links. Never read the whole vault. Say which notes you used. If nothing matches, say so and offer to save it.

## 4. Truth
10. **Facts versus interpretations.** Hard facts are filed confidently. Anything inferred about me (a belief, a preference, how I think) is tagged #provisional until I confirm it. The confirm queue ([[confirm-queue]]) lists them.
11. **Keep my exact words** for stories, phrases I coin and anything where how I say it matters.
12. **Decisions** go in records/decisions-log.md with a status (active, parked, rejected) and the reason. When a new idea touches an old decision, play the old one back first.

## 5. Daily notes
13. daily/YYYY-MM-DD.md is shared and append-only. Read today's note first, add your own section under a heading with your name and the time (`## Capture, 14:10`), never rewrite what is there.

## 6. Skills, artifacts and code
14. **Skills point at notes** in the vault for their content and never keep copies. See [[_SKILL-TEMPLATE]].
15. **Everything made in a chat is filed in the same session**: its source in the right project folder, and a line in projects/artifacts-index.md if it is an artifact. Files made in a chat (other than published artifacts) are not kept anywhere searchable later. System pages, like the Daily page, live in systems/.
16. **Code lives apart.** Websites and apps built in a coding tool live in their own GitHub repositories; everything made by chatting, including an HTML page, lives in Simonides. Always say which repository you mean.

## 7. Privacy and security
17. **Never store** passwords, keys, tokens or card numbers. For an account, the web address and username only.
18. **Private notes**: people notes, organisation notes, the client folders listed in the tree script and any note with private in its tags line never go onto a hosted page or into anything shared; the Daily page's tree script leaves them out, not even their names. The Daily page itself is private to me, but keep client detail in those private notes rather than in daily notes or records.

## 8. Keeping it tidy
19. **Decay rule.** When a project finishes, its line moves from CLAUDE.md to context/archive-index.md; the note stays where it is.
20. **CLAUDE.md stays an index**: short lines, no content, the daily log holds the last seven days only.
21. **Numbers come from the checker** (`python3 systems/simonides-checks.py all`), never from counting by eye.
22. **One job, one scheduled task.** Change the task you have; never add a second one beside it. The vault holds the prompt; the task is a copy.
23. **The explainer stays current.** Whenever something new is added to the system, add a plain line to [[_EXPLAINER]] in the same session.
