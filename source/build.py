#!/usr/bin/env python3
"""Regenerate career_upgrade_master_documentation.html from source modules."""

import json
from pathlib import Path

from continuity import CONTINUITY
from interviews import INTERVIEWS
from plan import LATER, PLAN
from projects import PROJECTS
from refs import REFS
from topics import PHASES

ROOT = Path(__file__).resolve().parent
OUT = ROOT.parent / "career_upgrade_master_documentation.html"
INDEX = ROOT.parent / "index.html"


def main() -> None:
    data = {
        "phases": PHASES,
        "plan": PLAN,
        "later": LATER,
        "projects": PROJECTS,
        "interviews": INTERVIEWS,
        "refs": REFS,
        "continuityHtml": CONTINUITY,
    }
    raw = json.dumps(data, ensure_ascii=False).replace("<", "\\u003c")
    template = (ROOT / "template.html").read_text(encoding="utf-8")
    if "__DATA_JSON__" not in template:
        raise SystemExit("template placeholder missing")
    html = template.replace("__DATA_JSON__", raw)
    ids = []
    for phase in PHASES:
        for module in phase["modules"]:
            for topic in module["topics"]:
                ids.append(topic["id"])
    dupes = {i for i in ids if ids.count(i) > 1}
    if dupes:
        raise SystemExit(f"duplicate topic ids: {dupes}")
    OUT.write_text(html, encoding="utf-8")
    INDEX.write_text(html, encoding="utf-8")
    print(f"wrote {OUT} and {INDEX} topics={len(ids)} bytes={OUT.stat().st_size}")


if __name__ == "__main__":
    main()
