# Skill template

Start every new skill from this. Copy the block into the new skill's SKILL.md and fill in the parts in [brackets].

---

```
---
name: [skill-name]
description: [one sentence: what it does and the phrases that trigger it]
---

# [Skill name]

## Uses Simonides
This skill uses my Simonides (~/Simonides on my computer, or the repository clone in a cloud session, see _GIT.md).
- READS: CLAUDE.md, then only the notes it needs: [list them, for example context/voice-and-tone.md].
- WRITES: [where its output goes], by the rules in _CONVENTIONS.md, appending rather than overwriting.
- Never keep copies of my voice, audience or methods in this skill; read them from the vault every time.
- Never call another skill; if you need another skill's output, read it from the vault.

## Steps
1. [step]
2. [step]

## Done
Confirm in one or two lines what was made and where it was saved.
```

---

After building: install the skill, add a row to _SKILLS.md, and test the trigger phrase.
