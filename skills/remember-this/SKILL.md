---
name: remember-this
description: Simonides capture and retrieval. Use when I say "remember this", "save this", "note this", "file this", paste something to keep, ask "what do I know about X" or "pull everything on X", or say "use my brain".
---

# Remember this → Simonides

One personal second brain: frictionless capture, fast retrieval, quality that holds up as it grows.

## The one vault
- On my computer: ~/Simonides. In a cloud session with no computer attached: clone my private GitHub repository [your-github-username]/simonides (see _GIT.md) to /home/claude/simonides, treat that as the vault, and commit and push when done.
- Always read and write that vault, whichever project or chat triggered the skill. Never create a second vault.
- If the folder is empty or missing CLAUDE.md or _CONVENTIONS.md, stop and tell me. An empty folder means a failed clone or sync, not a fresh vault; never rebuild it.
- On my computer the vault syncs itself every five minutes. After writing, just stop. Until the auto-sync is installed (recipe 5), commit and push after writing instead. If _SYNC-NEEDS-ATTENTION.md exists at the top of the vault, tell me before touching anything.
- CLAUDE.md (the index) and _CONVENTIONS.md (the rules) are authoritative. Read _CONVENTIONS.md first and follow it. Never keep copies of my rules in this skill.

## Whose knowledge is it? (ask before choosing a folder)
- Someone else's (a study, article, book, podcast, another person's idea) → library/, one note per topic, with the source, the date and my take.
- My own methods and "hows" → systems/ (listed in systems/frameworks.md).
- My beliefs, voice, stories, ideas → context/.
- What happened (meetings, talks, decisions) → records/.
- A live piece of work → its folder in projects/.
- People → people/; companies → organisations/.
- One capture can split in two (what I read → library, what I built on it → systems), each linking to the other.

## Capturing
1. Search CLAUDE.md and the aliases for an existing or related note first. If one exists, tell me before filing: "I already have this ([[note]], updated <date>): add detail, correct it, or leave it?"
2. Mid-flow or unclear → drop it into _inbox now, file it properly after.
3. Update the existing note, or copy _TEMPLATE.md into the right folder (kebab-case file name); fill the frontmatter; turn relative dates into real dates; anything with a date goes under Action items.
4. Link it with [[wikilinks]] to related notes and to the overview page for that world in context/.
5. Add one line under the right heading in CLAUDE.md. Log the capture in today's daily note (read it first, append under `## Capture, HH:MM`).
6. Decisions also go in records/decisions-log.md with a status; if it touches an earlier decision, play that back first.
7. Anything inferred about me, rather than said by me, is tagged #provisional.
8. Confirm in one or two lines what was saved and where. In a cloud session, commit and push and give the commit.

## Retrieving
- Pinpoint → CLAUDE.md → the note → answer.
- Everything about X → the overview page in context/, or notes filtered by scope and tags.
- Recent ("what have I told you this week") → the last few daily notes.
- Decisions → records/decisions-log.md.
- Say which notes you used. No match → say so plainly and offer to save it.
