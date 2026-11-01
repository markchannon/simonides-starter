#!/usr/bin/env python3
"""Builds the vault data for the Simonides Daily page. Run from the vault root.

    python3 systems/simonides-daily-dashboard/vault-tree.py           # JSON tree for DATA.tree
    python3 systems/simonides-daily-dashboard/vault-tree.py --notes   # JSON bundle of note texts for the page's reader

The tree lists every file with its title, type, tags, date and first line. Private notes are left out of the
tree and the notes bundle altogether, not even their names: people/, organisations/, any note with private in its
tags line, and the folders listed in PRIVATE below. Add your own client folders there.
The notes bundle is published next to the page as vault/notes.json.
"""
import os, re, json, sys, datetime

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
SKIP_DIRS = {".git", ".obsidian", "node_modules", "__pycache__"}
PRIVATE = ("people/", "organisations/")   # add client folders here, for example "projects/client-name/"


def frontmatter(text):
    fm = {}
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end > 0:
            for line in text[3:end].splitlines():
                m = re.match(r"^(\w[\w-]*):\s*(.*)$", line.strip())
                if m:
                    fm[m.group(1)] = re.sub(r"^\[|\]$", "", m.group(2).strip()).replace('"', "")
            return fm, text[end + 4:]
    return fm, text


def summary(body):
    for line in body.splitlines():
        s = line.strip()
        if not s or s.startswith(("#", "---", "<!--", "|", "_")):
            continue
        s = re.sub(r"\[\[([^\]|]+)(\|[^\]]+)?\]\]", r"\1", s)
        s = re.sub(r"[*_`>]", "", s)
        return re.sub(r"^\s*[-+]\s+", "", s)[:160]
    return ""


def private(path, text):
    """Private = a private folder, or private in the note's tags line, or a line that is only the tag #private.
    A note that merely mentions the tag in a sentence (like the rules) is not private."""
    return (path.startswith(PRIVATE)
            or re.search(r"^tags:.*\bprivate\b", text, re.M)
            or re.search(r"^\s*#private\s*$", text, re.M))


def walk(d, rel=""):
    items = []
    try:
        names = sorted(os.listdir(d), key=lambda n: (not os.path.isdir(os.path.join(d, n)), n.lower()))
    except OSError:
        return items
    for n in names:
        if n.startswith(".") or n in SKIP_DIRS:
            continue
        p = os.path.join(d, n)
        r = (rel + "/" + n).lstrip("/")
        if os.path.isdir(p):
            if r.startswith(tuple(x.rstrip("/") for x in PRIVATE)) and r.rstrip("/") + "/" in PRIVATE:
                continue                     # a private folder is not listed at all
            kids = walk(p, r)
            items.append({"name": n, "path": r, "dir": True, "children": kids, "count": sum(k.get("count", 1) for k in kids)})
            continue
        e = {"name": n, "path": r}
        if n.endswith(".md"):
            try:
                text = open(p, encoding="utf-8", errors="replace").read()
            except OSError:
                text = ""
            if private(r, text):
                continue                     # private: not listed, not named, never on the page
            fm, body = frontmatter(text)
            e["title"] = fm.get("title", "")
            for k in ("type", "tags", "updated"):
                if fm.get(k):
                    e[k] = fm[k]
            e["summary"] = summary(body)
        elif r.startswith(PRIVATE):
            continue
        items.append(e)
    return items


def notes_bundle(tree):
    out = {}
    def collect(items):
        for i in items:
            if i.get("dir"):
                collect(i["children"])
            elif i["path"].endswith(".md"):
                try:
                    out[i["path"]] = open(os.path.join(ROOT, i["path"]), encoding="utf-8", errors="replace").read()
                except OSError:
                    pass
    collect(tree)
    return out


if __name__ == "__main__":
    os.chdir(ROOT)
    ROOT = "."
    tree = walk(ROOT)
    today = datetime.date.today().isoformat()
    if len(sys.argv) > 1 and sys.argv[1] == "--notes":
        print(json.dumps({"generated": today, "notes": notes_bundle(tree)}, ensure_ascii=False))
    else:
        def count(items):
            return sum(count(i["children"]) if i.get("dir") else 1 for i in items)
        print(json.dumps({"generated": today, "files": count(tree), "tree": tree}, ensure_ascii=False))
