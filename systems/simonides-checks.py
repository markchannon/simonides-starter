#!/usr/bin/env python3
"""Simonides checker: every count the daily tidy reports comes from here, never from counting by eye.

Run from the vault root:
    python3 systems/simonides-checks.py all       # report every check
    python3 systems/simonides-checks.py review    # rebuild systems/confirm-queue.md from #provisional items

Each rule is code, with the date it was added, so the same vault always gives the same numbers.
Add a rule when the tidy learns something; never delete one, retire it with a dated comment.
"""
import os, re, sys, datetime

VAULT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SKIP_DIRS = {".git", ".obsidian", "node_modules", "__pycache__"}
TYPES = {"person", "organisation", "business", "project", "process", "reference", "record", "story", "daily", "system"}


def all_files():
    out = []
    for root, dirs, files in os.walk(VAULT):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.startswith(".")]
        for f in files:
            out.append(os.path.relpath(os.path.join(root, f), VAULT).replace(os.sep, "/"))
    return sorted(out)


def is_note(path):
    """R1 (starter): a note is a .md file that is not a README, not CLAUDE.md, START-HERE.md or LICENSE.md, not a root file starting with _,
    not inside skills/ (skill files are procedures, not notes)."""
    if not path.endswith(".md"):
        return False
    name = os.path.basename(path)
    if name == "README.md" or path in ("CLAUDE.md", "START-HERE.md", "LICENSE.md") or ("/" not in path and name.startswith("_")):
        return False
    if path.startswith("skills/"):
        return False
    return True


def read(path):
    try:
        with open(os.path.join(VAULT, path), encoding="utf-8", errors="replace") as fh:
            return fh.read()
    except OSError:
        return ""


def frontmatter(text):
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end < 0:
        return None
    fm = {}
    for line in text[3:end].splitlines():
        m = re.match(r"^(\w[\w-]*):\s*(.*)$", line.strip())
        if m:
            fm[m.group(1)] = m.group(2).strip()
    return fm


def strip_code(text):
    """R2 (starter): links inside `code` or ``` blocks are examples, not links."""
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    return re.sub(r"`[^`]*`", "", text)


def checks():
    files = all_files()
    notes = [p for p in files if is_note(p)]
    stems = {os.path.splitext(os.path.basename(p))[0].lower() for p in files}
    index = read("CLAUDE.md")
    index_links = {m.lower() for m in re.findall(r"\[\[([^\]|#]+)", strip_code(index))}
    index_paths = set(re.findall(r"\(([^)\s]+\.md)\)", index))

    res = {}
    # R3 (starter): every note except daily notes is listed in CLAUDE.md (by [[stem]] or by path)
    res["missing from index"] = [p for p in notes if not p.startswith("daily/")
                                 and os.path.splitext(os.path.basename(p))[0].lower() not in index_links
                                 and p not in index_paths]
    # R4 (starter): index lines that point at notes that do not exist
    res["index points nowhere"] = sorted([l for l in index_links if l not in stems])
    # R5 (starter): wikilinks that point nowhere, anywhere in the vault
    broken = []
    for p in files:
        if not p.endswith(".md") or p.startswith("skills/"):
            continue
        for i, line in enumerate(strip_code(read(p)).splitlines(), 1):
            for m in re.finditer(r"\[\[([^\]|#]+)", line):
                t = m.group(1).strip()
                if t.lower() not in stems:
                    broken.append(f"{p} line {i} -> [[{t}]]")
    res["broken wikilinks"] = broken
    # R6 (starter): notes without frontmatter, and types outside the closed list.
    # R9 (starter): daily notes are append-only diary pages, so they are not checked for frontmatter.
    nofm, badtype = [], []
    for p in notes:
        if p.startswith("daily/"):
            continue
        fm = frontmatter(read(p))
        if fm is None:
            nofm.append(p)
        elif fm.get("type") and fm["type"] not in TYPES:
            badtype.append(f"{p}: {fm['type']}")
    res["no frontmatter"] = nofm
    res["type not in the list"] = badtype
    return res


def provisional():
    """R7 (starter): every line tagged #provisional, with the note's updated date, newest first."""
    items = []
    for p in all_files():
        if not is_note(p):
            continue
        text = read(p)
        fm = frontmatter(text) or {}
        when = fm.get("updated", "") or fm.get("created", "")
        for i, line in enumerate(text.splitlines(), 1):
            bare = re.sub(r"`[^`]*`", "", line)
            if "#provisional" not in bare or line.strip().startswith(("tags:", "#")):
                continue
            # R8 (starter): a line that only describes the tag ("tagged #provisional", "every #provisional item") is not an item
            if re.search(r"(tagged|every|each|all|any)\s+#provisional", bare, re.I):
                continue
            items.append((when, p, i, line.strip()[:200]))
    items.sort(key=lambda x: (x[0], x[1]), reverse=True)
    return items


def report():
    res = checks()
    total = 0
    for name, rows in res.items():
        print(f"=== {name.upper()}: {len(rows)} ===")
        for r in rows[:50]:
            print("   " + r)
        total += len(rows)
    prov = provisional()
    print(f"=== UNCONFIRMED (#provisional): {len(prov)} ===")
    for when, p, i, line in sorted(prov)[:3]:
        print(f"   oldest: {p} line {i} ({when or 'no date'}): {line[:120]}")
    notes = sum(1 for p in all_files() if is_note(p))
    print(f"\nSUMMARY: {notes} notes | problems {total} | unconfirmed {len(prov)}")


def review():
    prov = provisional()
    # R10 (starter): keep the queue's first created date; only updated changes on a rebuild
    created = (frontmatter(read("systems/confirm-queue.md")) or {}).get("created", "")
    if not re.match(r"\d{4}-\d{2}-\d{2}$", created):
        created = str(datetime.date.today())
    out = ["---", "title: Confirm queue", "type: system", "scope: [all]", "tags: [provisional, confirm]",
           "aliases: []", "status: active", f"created: {created}", f"updated: {datetime.date.today()}",
           "related: []", "---", "", "# Confirm queue", "",
           "Generated by `python3 systems/simonides-checks.py review`. Every #provisional item, grouped by note, newest first.",
           "Answer yes, no or nearly, per item or per note; the source note changes, not this file.", ""]
    if not prov:
        out.append("_Nothing to confirm._")
    current = None
    for when, p, i, line in prov:
        if p != current:
            out += ["", f"## {p} ({when or 'no date'})"]
            current = p
        out.append(f"- line {i}: {line}")
    with open(os.path.join(VAULT, "systems", "confirm-queue.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(out) + "\n")
    print(f"confirm queue rebuilt: {len(prov)} items")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "all"
    if cmd == "review":
        review()
    else:
        report()
