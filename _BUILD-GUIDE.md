---
title: "Simonides: The Complete Guide"
type: reference
scope: [all]
tags: [simonides, guide]
aliases: [build guide]
status: active
created: [today's date]
updated: [today's date]
related: []
---

_Your copy of the guide your Simonides was built from. Add a line to the right recipe whenever you add a part to your system. The latest public version: https://claude.ai/artifact/V17eykRieJ1eWN8TQVRn2T_


# Build your own Simonides

_From nothing to a working second brain that Claude actually uses, start to finish. Written for someone who does not write code and does not want to: you talk to Claude, and Claude does the technical parts. You start from the starter kit, a ready-made, empty Simonides on GitHub, and the recipes set it up one part at a time. Every step has the exact words to send, ready to copy. Follow the recipes in order and you finish with the full system: a private brain that learns about you every day, jobs that look after it while you sleep, and one page each morning that tells you what was done and what needs you. Everything here comes from the author's own system, which runs every day. Where it says "mine", that is the author's own setup; yours will grow its own way._

## Start here: what you end up with

**The dish.** One private folder of plain-text notes that holds everything about you and your work: who you are, who you know, what you are doing, what happened, how you do things. Claude reads it before it answers and writes to it when you say "remember this". It lives on GitHub so it works from any machine or from the cloud, tidies itself every morning, and gives you one page a day that says what ran overnight and what needs a decision from you.

**What it feels like once it is running.**
- You say "remember this" and paste anything. It is filed, tagged and linked for you. You never organise.
- You ask "what do I know about X" in any chat and get the answer from your own notes.
- You say "write this in my voice" and it sounds like you, because your real writing is in there.
- Jobs run in the cloud while you sleep: your app data pulled in, your notes tidied, your page rebuilt.
- You open one page each morning. Everything that needs you is on it, with a recommendation, and you can answer it right there.

**How long it takes.** Getting the kit and the core (recipes 1 to 5) is one afternoon. The rest (recipes 6 to 10: connectors and skills, scheduled jobs, the daily page, artifacts, keeping it true) is added one piece at a time over a few weeks, each piece in under an hour.

**How to use this guide.**
- Every box marked "Say to Claude" is the exact message to send. Press Copy, paste it into Claude, send it.
- Anything in [square brackets] is yours to fill in before you send, like [your-github-username].
- Get the starter kit first (below), then do the recipes in order. Each one starts with what it needs from the ones before.
- From recipe 4 on, start each recipe in a fresh chat inside your Simonides project (recipe 3 creates it). The brain holds what was done; a fresh chat catches up from the files.
- When a step says "in the Code tab", open the Code tab in the Claude desktop app, choose your own computer (Local, not the cloud) and pick your Simonides folder, so the work lands on your machine.
- Claude will sometimes ask a question or ask you to approve something (a sign-in, a permission, a file). That is normal. Answer it and carry on.
- A recipe is finished when its "Done when" check passes. Tick it off and move on.
- Until recipe 5 sets up the automatic sync, end each recipe chat by saying "commit and push my Simonides", so GitHub always has your latest notes.

**Get the starter kit.** This is the only way in. The kit is an empty Simonides with every part already in place: the folders, the rules, the skills, the daily tidy prompt, the daily page with sample data, the checker, the sync script and this guide. It holds nobody's personal data. You copy it once, then the recipes make each part yours.

1. Sign in to github.com (a free account is enough). Open [github.com/markchannon/simonides-starter](https://github.com/markchannon/simonides-starter), click "Use this template", then "Create a new repository". Name it simonides, choose Private, and click Create repository.
2. In the Claude desktop app, open Settings → Connectors → GitHub, sign in and allow access to your new simonides repository. Cloud chats and scheduled jobs reach your notes through this.
3. In the Code tab, choose your own computer (Local) and your home folder, and say:

> **Say to Claude:** Clone my private GitHub repository [your-github-username]/simonides to ~/Simonides. If this computer needs git or a GitHub sign-in first, set them up without an administrator password (the Mac's own pop-up installs the command line tools; the GitHub CLI can go in my home folder and sign me in through the browser) and give me the exact clicks; I do not use a terminal. Then read ~/Simonides/_BUILD-GUIDE.md and ~/Simonides/START-HERE.md and personalise the kit: ask me for my worlds (the areas of my life and work I want notes grouped by, for example personal, work, side-project), my time zone, and any client folders I want kept off every page. Fill in my GitHub username, worlds, time zone and today's date wherever the kit has a square-bracket blank for them, and leave the other blanks (the page link, the one-minute version, the Installed dates) for the recipes that fill them. Add the client folders to the PRIVATE list in systems/simonides-daily-dashboard/vault-tree.py, commit and push, and show me what changed.

4. Go to recipe 1. Its first step adds your Simonides folder to a chat; send the kickoff prompt below in that chat once the folder is added.

**The kickoff prompt.** Send this at the start of every chat you use for a recipe, once the chat can see your Simonides folder (recipe 1 shows how; from recipe 3 on, the project does it for you; in the Code tab, pick the folder). It turns Claude into a guide that walks you through the recipe one step at a time, instead of improvising. The guide is in your Simonides as _BUILD-GUIDE.md, so Claude reads it from there.

> **Say to Claude:** I am building my Simonides, a second brain for Claude, from the starter kit, by following _BUILD-GUIDE.md in my Simonides. Read it first. We are on recipe [number]. Walk me through it one step at a time: do the technical parts yourself, give me the exact clicks for anything only I can do, ask me only for my own details, and tell me when the recipe's "Done when" check passes. The kit already holds the files the recipes use: check them and make them mine, and never create a second copy of anything. Never skip a step, and never invent your own folder names or rules.

**The one rule that makes it work.** Claude pays the structure tax, not you. Strong structure from day one, invisible to you, done by Claude in seconds.

## Ingredients: what you need before you start

**Accounts and apps**
- A paid Claude plan and the Claude desktop app on your computer. This guide uses chats, projects (a saved setup so every chat in it is wired to the brain), skills, connectors, artifacts, the Code tab (where Claude does technical steps on your machine) and scheduled tasks (jobs that run in the cloud on a timer). If one of them is missing from your app, check what your plan includes in Settings.
- A free GitHub account. GitHub is where your copy of the kit lives as a private repository, the single true copy of your Simonides.
- A Mac or a PC that is on when you work. Nothing has to stay on all the time; the cloud does the overnight work. The steps show a Mac; on a PC, ask Claude for the Windows version of the same step.

**Optional**
- Obsidian, a free app that shows the folder as a graph of linked notes. Nice to look at, never required.
- Your own apps, if any have a Claude connector (a Claude connector is a way for Claude to read and act in an app). It might be a task app, a CRM or a website CMS.

**Habits**
- Say "remember this" the moment something matters. Capture is the whole game.
- Start a fresh chat when one gets long. The brain holds the state; a new chat catches up from the files.

**Words you will meet (plain versions)**
- Simonides, or the vault: your folder of notes. Same thing.
- Starter kit: the empty Simonides on GitHub that you copy to start your own.
- Template: a GitHub repository you can copy with one button ("Use this template").
- ~ (tilde): short for your home folder, so ~/Simonides is the Simonides folder in your home folder.
- README.md: a one-line note inside a folder saying what goes in it.
- Alias: another name a note can be found by (a nickname, an old name, a short form).
- Markdown: a plain text file with simple headings and links. Any app can read it in ten years.
- Frontmatter: a short label block at the top of each note (title, type, tags, dates).
- Wikilink: a link between two notes, written `[[like-this]]`.
- Repository (repo): a folder that GitHub keeps every version of. Your Simonides is one repository.
- Git: the tool that saves versions of a folder and sends them to GitHub. Claude runs it for you.
- CLI (command-line tool): a program you type commands into instead of clicking. Claude uses a few; you never have to.
- Launch agent: the Mac's way of running a small job in the background on a timer; the auto-sync uses one.
- CRM and CMS: the app that holds your contacts and deals (CRM), and the app that runs your website's pages (CMS).
- Commit and push: save a version of your changes, then send it to GitHub.
- Clone and pull: download a copy of a repository, and fetch the latest changes into it.
- Script: a small program that does one job; the kit has a few, and Claude runs them for you. You never edit them.
- Log: a file where a background job writes what it did, so you can check it.
- Project: a saved setup in Claude so every chat inside it starts wired to your brain.
- Code tab: the part of the Claude desktop app where Claude can run steps on your computer.
- Connector: a plug that lets Claude read and act in another app.
- Skill: a saved procedure Claude follows when you say a trigger phrase.
- Scheduled task: a saved instruction that runs on a timer in the cloud.
- Artifact: a page Claude builds and hosts at its own private link.
- Data block: the part of your daily page that holds the day's content, kept apart so the morning job can change the content without touching the design.
- Page database: a small store inside an artifact that keeps what you save on the page, such as your answers.

## Recipe 1: the folder

**Why.** Everything sits on one folder with a fixed shape. The kit gives you the shape; this recipe puts it in front of Claude and shows you your way round it.

**You need.** The starter kit on your computer (Start here), ten minutes.

**Steps**
1. In the Claude desktop app, click the + beside the message box, choose Add folder, and pick the Simonides folder in your home folder (on a Mac: Macintosh HD → Users → you → Simonides). Keep it out of iCloud, Dropbox and OneDrive; those fight with GitHub.
2. Ask Claude to show you round. Say:

> **Say to Claude:** Show me my Simonides folder as a tree. In one line each, tell me what every folder is for, using its README.md. Then tell me in plain words what CLAUDE.md, _CONVENTIONS.md and _TEMPLATE.md do, and which files I will never need to open myself.

3. Read this line back to yourself, it is the whole map: context is my world, people and organisations are who I know, projects are what I am doing, records are what happened, systems are how it runs, library is what I have read, daily is the diary.

**Done when.** You ask "what is in my Simonides folder?" in a new chat with the folder added, and Claude answers from the files.

## Recipe 2: the rules

**Why.** The rules file is what makes fifty future chats behave like one librarian. Claude reads it before filing anything. The kit's rules are a strong start; this recipe makes them yours.

**You need.** Recipe 1, twenty minutes.

**Steps**
1. Check your worlds. They are the "scope" label on every note, set when you personalised the kit. Mine are personal plus one for each business I run. Change them any time by saying so.
2. Go through the rules with Claude, one at a time. Say:

> **Say to Claude:** Walk me through _CONVENTIONS.md in my Simonides one rule at a time, in plain words, with a short example of each. After each rule, ask me whether to keep it, change it or drop it, and change the file as I answer. Keep my worlds as the scope list. At the end, read me the rules that are left in one short list.

3. Keep two rules exactly as they are, whatever else you change: never store passwords, keys or card numbers; and people notes, organisation notes and anything about clients never go onto a hosted page.

**Done when.** You ask "how would you file a new client called Sam?" and Claude answers with the folder, the file name and the frontmatter, without you explaining.

## Recipe 3: teach every chat where the brain is

**Why.** The folder is useless if a chat does not know it exists. Three small pieces, all already in the kit, make every chat, every project and every Code session find it on their own.

**You need.** Recipes 1 and 2, fifteen minutes.

**Steps**
1. Get the project text ready. In the chat with your folder added, say:

> **Say to Claude:** Show me the text in ~/Simonides/_PROJECT_INSTRUCTIONS.md that goes into a Claude project's Instructions, exactly as it is, ready for me to copy.

2. In the Claude app, open Projects in the sidebar and create a new project called Simonides. Open its Instructions and paste the text in. It tells every chat in the project where your brain is, on your computer or on GitHub when no computer is attached.
3. Connect the folder to the project too: open the project's Context panel, click +, and add the existing Simonides folder.
4. Install the capture skill, so "remember this" always does the same thing. Say:

> **Say to Claude:** Package ~/Simonides/skills/remember-this as a skill I can install, and give me the exact clicks to add it. When it is installed, put today's date in the Installed column of _SKILLS.md.

5. Follow the clicks Claude gives you (skills live under Settings → Capabilities). Skills are global: installed once, they work in every chat and project. From here on, work in a fresh chat inside the Simonides project.
6. Give the Code tab the same map. In the Code tab (your computer, Simonides folder), say:

> **Say to Claude:** Copy the block between the two --- lines in ~/Simonides/_CLAUDE-CODE.md into ~/.claude/CLAUDE.md, keeping anything already in that file and replacing only an older copy of this block. Show me the result.

**Done when.** You open a brand new chat in the Simonides project, ask "what is in my Simonides and what are its rules?" and it reads the folder without being told where it is.

## Recipe 4: the first captures

**Why.** The brain gets better the more it knows. These first notes are what every later post, deck and answer draws on. Do them in your own words, out loud if you like; voice dictation works well.

**You need.** Recipe 3, an hour, your real material.

**Steps**
1. Who you are. Say:

> **Say to Claude:** Remember this: here is my story. [Talk it through: your background, what you do now, where you are based, the businesses or roles you have, what you are known for.] File it as my biography in context and create context/[your-name]-personal.md as the overview page of me across everything.

2. Your worlds. For each business or area of your life, say:

> **Say to Claude:** Remember this: here is [business or area] in a paragraph. [What it is, who it serves, what it sells or does, how it is going.] Make it an overview page in context and link it from my personal overview.

3. Your voice. Collect ten pieces of your own writing (posts, emails you were proud of, a talk transcript). Then say:

> **Say to Claude:** Remember this as my voice and tone. Keep the raw examples word for word in context/voice-and-tone.md, then distil the patterns at the top: how I open, sentence length, words I use and never use, how I sound when I am persuading versus explaining. [Paste your ten pieces.]

4. Your people. The ten people you deal with most, one message each or all together:

> **Say to Claude:** Remember this: [name] is [who they are to me], [how we know each other], [anything I should not forget about them]. One note per person in people.

5. Your methods. The ways you work or teach, one at a time:

> **Say to Claude:** Remember this as one of my methods: [the name I use], [the steps], [when I use it and for whom]. File it in systems and add it to systems/frameworks.md.

6. Your stories. Anything you tell more than once:

> **Say to Claude:** Remember this story, word for word: [tell it]. File it in context/stories with tags for its themes and add it to a story bank index (create the index the first time).

7. Your ideas. The kit has one home for every post, talk or product idea, context/content-ideas.md. Say:

> **Say to Claude:** Add these to context/content-ideas.md, one line each with today's date: [your ideas].

8. Test retrieval after each batch. Say "what do I know about [thing]?" If it misses, say "add it to the index".

**Done when.** Twenty to forty notes, an index that lists them, and a daily note for today that records what you captured.

## Recipe 5: keep it in sync

**Why.** Your Simonides already lives on GitHub: that is where your copy of the kit came from. This recipe keeps your computer and GitHub identical without you thinking about it, so every version is kept, nothing is ever lost, and cloud jobs can read and write it with no computer on.

**You need.** Recipes 1 to 4, the Code tab, half an hour.

**Steps**
1. Install the auto-sync. The script is already in the kit. In the Code tab (your computer, Simonides folder), say:

> **Say to Claude:** Install the auto-sync on this computer by following ~/Simonides/systems/simonides-autosync/README.md. Every five minutes and at login it commits anything changed, pulls from GitHub and pushes. Test it and show me the last five lines of its log.

   On a PC, add this sentence to the end before you send it: "This is a Windows PC: use Task Scheduler instead of a launch agent, and keep the log in my user folder."

2. Check the rules every chat follows for the sync. They are in _GIT.md: GitHub is the single true copy, pull before you write, push when done, never overwrite on a conflict. If the sync ever finds a clash outside the daily notes, it stops and writes _SYNC-NEEDS-ATTENTION.md at the top of your Simonides; ask Claude to sort it out.
3. Second computer? In its Code tab (that computer, Local), say "clone my private repository [your-github-username]/simonides to ~/Simonides, then install the auto-sync by following ~/Simonides/systems/simonides-autosync/README.md". Same path on every machine.
4. Cloud chats already know what to do with no computer attached: the project text you pasted in recipe 3 tells them to clone your repository from GitHub.
5. Make the explainer yours. _EXPLAINER.md is the plain-words description of your system that you keep current from now on. Say:

> **Say to Claude:** Update _EXPLAINER.md for my Simonides: my worlds, my computers, how my notes stay in sync, and write the one-minute version at the end (it is a blank in the kit). Keep it plain enough to read to someone non-technical.

**Done when.** Add a line to a note, wait five minutes, see it on github.com. Then the reverse: edit a note on GitHub's website, wait five minutes, see it in your folder.

## Recipe 6: connectors and skills

**Why.** Connectors let Claude read and act in your tools. Skills let you say one phrase and get a repeatable job done. Together they turn the brain from a filing cabinet into something that works.

**You need.** Recipe 5, and one tool you would like Claude to reach.

**Steps**
1. Connect the apps you already use. In the Claude desktop app, Settings → Connectors: calendar, email, GitHub, Notion, whatever you live in. Each one is a sign-in, not a setup.
2. If you have your own app, ask its developer (or Claude in the Code tab) whether it has a Claude connector. With one, Claude can read and act in that app from any chat: for a task app, read your goals and create tasks.
3. The kit already holds the skill contract (_SKILL-TEMPLATE.md: every skill reads its content from your Simonides and never keeps copies) and the list of your skills (_SKILLS.md). Nothing to write.
4. Install the writer skill, which drafts in your voice from the notes you made in recipe 4. Say:

> **Say to Claude:** Package ~/Simonides/skills/writer as a skill I can install, and give me the exact clicks to add it. When it is installed, put today's date in the Installed column of _SKILLS.md.

5. Every new skill after this starts the same way: "Using _SKILL-TEMPLATE.md, build me a skill called [name] that [does what] when I say [trigger phrase]. Save its source in skills/[name]/, add it to _SKILLS.md and package it so I can install it." Install it and test the phrase.

**Done when.** One connector answers a live question ("what is on my calendar tomorrow?") and the writer skill drafts something in your voice from your Simonides without you pasting anything.

## Recipe 7: scheduled jobs in the cloud

**Why.** This is where the brain starts working for you. A scheduled task is a saved instruction that runs on a timer in the cloud: it opens your Simonides on GitHub, does its work, saves and sends it back. No computer has to be on.

**You need.** Recipe 5, a chat, about thirty minutes.

**Steps**
1. List your code projects, if you have any: websites, apps or tools you build in a coding tool (Claude Code, Lovable or anything else), each in its own GitHub repository. The daily tidy will read what changed in each one every morning and show it on your daily page under Code projects. No code projects? Skip to step 2. In a chat in your Simonides project, say:

> **Say to Claude:** Fill in the table in systems/code-projects.md in my Simonides: one row per code repository I have on GitHub (a website, an app, a tool), with its owner, its name, what it is in one line, what it was built with and its live address if it has one. Find what you can through my GitHub connector and ask me for the rest. Commit when done.

2. One thing first, because it is the step that breaks most often. A scheduled task gets its GitHub access from the chat it was created in, and editing the task later does not add access. So create every task from a fresh chat in your Simonides project that has the repositories attached, and start that chat like this (approve GitHub when Claude asks). If Claude says it cannot attach repositories or create scheduled tasks in that chat, ask it where in the app it can, and do this recipe there.

> **Say to Claude:** Attach my GitHub repository [your-github-username]/simonides to this chat with push access, and every repository listed in systems/code-projects.md with read access. I am about to create scheduled tasks that need them.

3. Create the daily tidy, the one job every Simonides needs. Its prompt is already in your kit, in systems/simonides-daily-dashboard/tidy-task-prompt.md. Each morning it keeps the index complete, files the inbox, fixes labels and links, merges duplicates, lists passed deadlines and the guesses waiting for you to confirm, checks your skills, tasks and artifacts against their lists, writes a short account in the day's note, reads what changed in your code projects, and takes every number from the checker. Once you publish your daily page (recipe 8) it also files the answers you saved there and rebuilds the page. In the same chat, say:

> **Say to Claude:** Create a scheduled task called "Simonides daily tidy" that runs every day at 08:45 my time ([your time zone]). Its prompt is the text in the Prompt section of systems/simonides-daily-dashboard/tidy-task-prompt.md in my repository, word for word. Show me the task when it is made.

4. Run it once now, so you see it work today rather than tomorrow. Say:

> **Say to Claude:** Run my Simonides daily tidy once now and show me its report.

5. Check your list of jobs. The kit's systems/workflows-and-automations.md already has a line for the daily tidy. Say:

> **Say to Claude:** Check the daily tidy line in systems/workflows-and-automations.md matches the task you just made (its name, when it runs, what it reads and what it writes) and correct it if not.

6. Add a sync for each app you connected, so the brain stays current without you. In a chat with the repository attached, say:

> **Say to Claude:** Create a scheduled task called "[app] daily sync" that runs every day at 08:25 my time, before the tidy. Each run: clone [your-github-username]/simonides; use the [app] connector to read what changed since the last run ([what matters, for example new meetings, open tasks, this week's goals]); write a current snapshot onto the overview page for that world; append the history to records/[app]/; append a short account to today's daily note under your own heading, with anything that needs me under a "Needs you" line, one plain question each; commit and push. Save the prompt into systems/ with a version number and add the task to systems/workflows-and-automations.md.

7. Add anything else that repeats, the same way: a weekly content refresh, a monthly bookkeeping run, a watch on a topic you care about, or a publishing run that posts finished articles to your website on a dated schedule (the schedule is a table in Simonides and each run marks its row published). The pattern never changes:

> **Say to Claude:** Create a scheduled task called "[name]" that runs [when]. Each run: clone [your-github-username]/simonides, [what it does, in plain words], write a short account into today's daily note under its own heading, commit and push. Never delete anything. Save the prompt into systems/ with a version number and add the task to systems/workflows-and-automations.md.

8. Three rules that save pain: never create a second task for a job that already has one (change the prompt file first, then update the task to match); never let a task delete a note; if a job ever reports that it cannot reach a repository (including a new code project you have just added to systems/code-projects.md), recreate it from a chat with every repository attached, using the saved prompt, then delete the old task.

**Done when.** The test run reported back, the tidy runs again tomorrow morning on its own, you see its commit on github.com, and the daily note has a section from it.

## Recipe 8: the daily page

**Why.** Without this you have to go looking. With it, one pinned page tells you what ran, what was done for you and what needs a decision, every morning, at the same link. You can answer right on the page.

**You need.** Recipe 7 running, fifteen minutes. The page is already in your kit, showing sample data.

**Steps**
1. Publish the page. In a chat in your Simonides project, say:

> **Say to Claude:** Publish systems/simonides-daily-dashboard/simonides-daily.html from my Simonides as an artifact, private to me, with the page's database switched on (it keeps the answers I save on the page). Then write the page's link into the "Page link" line of systems/simonides-daily-dashboard/tidy-task-prompt.md and into projects/artifacts-index.md, and commit.

2. Claude will ask you to approve switching on the page's database the first time; say yes. If a long chat refuses to publish it, open a fresh chat in the project and say "publish my Simonides Daily page with its database switched on". Only you (and anyone you give edit access) can write to it, and nobody can open the page unless you share it.
3. Pin the page in the Claude sidebar, so it is one click every morning. It has a side menu of seven sections: Needs you, From my apps, Done for you, What ran, Code projects, Inventory (a searchable tree of your notes, which open inside the page) and How it works. Press [ to open or close the menu, and the number keys 1 to 7 to jump between sections.
4. Nothing else to set up. The tidy's page steps switch on by themselves now that the link is filled in: from tomorrow morning it replaces the sample data with yours, fills the searchable tree of your notes, and files the answers you saved the day before. People notes, organisation notes and anything private never go on the page.
5. Answer on the page. Under every item in Needs you there is an answer box: Yes / No / Nearly for questions, Done / Not yet / Skip it for things you have to do, a one-line box otherwise. Save, and the next morning's tidy files your answer into the right note and moves the item to Done.
6. Optional: if your task app has a connector, answers can create tasks straight away. Say:

> **Say to Claude:** On my Simonides Daily page, when an answer I save clearly asks for a task ("add a task for Thursday"), create it in [task app] there and then through its connector, with only the date I named, and show "Done now: task created" on the card. Add a rule to the tidy prompt file that the tidy must never create the same task again, then update the task to match. Switch on the connector for the page when you publish.

**Done when.** You open the page tomorrow and it is dated today, rebuilt by the tidy, with your own items under Needs you, each linking to a real note, and an answer you saved yesterday shows under Done.

## Recipe 9: artifacts, the things you make

**Why.** Not everything you make is a note. A deck, a dashboard, an interactive tool, a one-page explainer: Claude builds these as artifacts, pages it hosts at their own private link. The brain has to know about every one of them, or they get lost the way files in a downloads folder get lost.

**You need.** Recipes 5 and 7. Any chat.

**Steps**
1. Check the index is complete. The kit has projects/artifacts-index.md. Say:

> **Say to Claude:** Check projects/artifacts-index.md against every artifact I have. Add any that are missing to the project they belong to, with the link and one line on what each is, and move anything under "found by the tidy" to its project.

2. Ask for an artifact the way you would ask for anything: "build me a deck for my talk on X as an artifact" or "make me a small tool that does Y". Claude builds the page and gives you a card with the link. The link never changes; later edits republish to the same link.
3. File it in the same session, every time. Your rules already say so (everything made in a chat is filed the same day, and websites or apps built in a coding tool live in their own repositories). If Claude forgets, say:

> **Say to Claude:** Remember this artifact in Simonides: save its source file into the project folder it belongs to, add it to that project's status note with its link and one line on what it is, and add a line to projects/artifacts-index.md.

4. The tidy catches the ones you forget: its artifacts step adds any missing artifact to the index under "found by the tidy", so nothing goes missing even on a busy day.

**Done when.** You ask "what artifacts have I got for [project]?" and get the list with links.

## Recipe 10: keep it true

**Why.** A brain that grows every day also drifts: a fact goes stale, a guess about you gets treated as true, a count is different every time Claude reads it. Four pieces keep it honest, and all four came with the kit: a checker, a confirm queue, a plain explainer and a monthly audit.

**You need.** Recipes 7 and 8 running, half an hour.

**Steps**
1. Meet the checker, so every number comes from a script and not from Claude counting by eye (counting by reading gives a different total each time; a script gives the same one). The tidy already runs it every morning. Say:

> **Say to Claude:** Run python3 systems/simonides-checks.py all in my Simonides and tell me in plain words what it found and what each check means.

2. Answer the confirm queue. Anything Claude has guessed about you is tagged #provisional, and the tidy gathers every one into systems/confirm-queue.md each morning; its count shows on your daily page. Open it now and then and answer yes, no or nearly, per item or per group. Claude changes the note the guess came from, never the queue.
3. Bring the explainer up to date with everything you have set up since recipe 5. Say:

> **Say to Claude:** Update _EXPLAINER.md so it covers everything my Simonides does now, in plain words: each scheduled job and what it does, what the Daily page shows and how answering on it works, my skills and connectors, the checker, the confirm queue and the monthly audit. Keep the one-minute version at the end current too.

4. The monthly audit is already in the tidy. It starts once you have a month of daily notes; from then on, on the 2nd of each month it reads every note against what is true today, fixes stale facts in place, never deletes, and puts the questions only you can answer under Needs you (kept in records/audit-open-items.md). Nothing to set up; answer its questions when they appear.

**Done when.** The tidy's report quotes the checker's numbers and the confirm queue's count (zero is fine on a new Simonides), and you can read the explainer to someone in a minute.

## Serve: the daily loop

**Morning**
- The cloud jobs have run: syncs first, the tidy last, the page rebuilt.
- Open the page. Answer what needs you on the page itself, or open a chat and say "open my Simonides Daily page and run through it".
- Anything that becomes work goes into your task app, not onto a list in the vault.

**During the day**
- "Remember this" whenever something matters. An email, a decision, a story, a contact, a piece of research.
- "What do I know about X" before any meeting or piece of writing.
- "Write it in my voice", "use my method", "for my [business]": tell Claude to use the brain and it will.
- Start a fresh chat when one gets long. The brain holds the state.

**Night**
- Nothing. The daily note records the day; the tidy checks it in the morning.

**Once a month**
- The full audit runs on its own. Answer its questions on the page, and confirm or correct a few items in the confirm queue.

## Keep it growing: the update rule

- Every new part of the system gets a line in your explainer the same day. If it cannot be explained to someone non-technical, it is not finished.
- Every asset you make in a chat (a deck, a page, a video, a tool) is filed in the vault in the same session, with its project. Claude has no library of files; the vault is the only place they can be found again.
- Content goes in the vault, process goes in skills. When a skill "learns" something, ask which it is.
- One job, one scheduled task. Change the task you have, never add a second one beside it. The vault holds the prompt; the task is a copy.
- A scheduled task keeps the GitHub access of the chat it was created in. If a job loses access, recreate it from a chat with the repository attached; editing it will not fix it.
- Numbers come from the checker, never from counting by eye.
- Prefer the fix that works from any machine. Nothing should depend on one computer being on.
- When the vault and anything else disagree, the vault wins and the other thing gets corrected.
- The two phrases that are the whole system: "use my brain" means read from it; "remember this" means write to it.
