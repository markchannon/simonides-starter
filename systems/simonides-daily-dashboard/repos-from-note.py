#!/usr/bin/env python3
"""Reads the table in systems/code-projects.md and prints it as JSON for the Daily page (DATA.repos).

    python3 systems/simonides-daily-dashboard/repos-from-note.py [pushes.json]

pushes.json (optional) maps "owner/repository" to its last push date, for example
{"your-github-username/my-website": "2026-01-14T17:02:11Z"}; the daily tidy writes it from GitHub.
"""
import os, re, sys, json

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
note = open(os.path.join(ROOT, "systems", "code-projects.md"), encoding="utf-8").read()
pushes = json.load(open(sys.argv[1], encoding="utf-8")) if len(sys.argv) > 1 else {}

repos, in_table = [], False
for line in note.splitlines():
    if line.startswith("## "):
        in_table = line.strip() == "## My repositories"
        continue
    if not in_table or not line.startswith("|") or re.match(r"^\|\s*-", line):
        continue
    cells = [c.strip().strip("`") for c in line.strip().strip("|").split("|")]
    if len(cells) < 2 or cells[0].lower() == "owner" or not cells[0] or not cells[1]:
        continue
    cells += [""] * (5 - len(cells))
    owner, name, what, built, live = cells[:5]
    if live and not live.startswith("http"):
        live = ""
    repos.append({"org": owner, "name": name, "what": what, "built": built, "live": live,
                  "lastPush": pushes.get(f"{owner}/{name}", "")})
print(json.dumps(repos, ensure_ascii=False, indent=1))
