def lesson(tid, title, level, priority, minutes, summary, **parts):
    blocks = []

    def add(heading, text=None, bullets=None, code=None, out=None, ordered=None):
        if text is None and not bullets and not code and not ordered:
            return
        block = {"h": heading}
        if text:
            block["p"] = text if isinstance(text, list) else [text]
        if bullets:
            block["ul"] = bullets
        if ordered:
            block["ol"] = ordered
        if code:
            block["code"] = code
        if out:
            block["out"] = out
        blocks.append(block)

    add("Prerequisites", parts.get("prereq"))
    add("What it is", parts.get("what"))
    add("Why it exists", parts.get("why"))
    add("How it works", parts.get("how"))
    add("Syntax or shape", parts.get("syntax"), code=parts.get("syntax_code"), out=parts.get("syntax_out"))
    add("Beginner example", parts.get("example"), code=parts.get("code"), out=parts.get("out"))
    add("Backend or product example", parts.get("realistic"))
    add("Common mistakes", bullets=parts.get("mistakes"))
    add("Best practice and security", parts.get("safe"), bullets=parts.get("safe_list"))
    add("Performance", parts.get("perf"))
    add("When to use it", parts.get("when"))
    add("Compared with a neighbour", parts.get("compare"))
    add("Exercise", parts.get("exercise"))
    add("Implementation task", parts.get("task"))
    add("Interview prompts", bullets=parts.get("interview"))
    add("References", bullets=parts.get("refs"))
    add("Checklist", bullets=parts.get("checklist"))
    add("Next", parts.get("nxt"))
    return {
        "id": tid,
        "title": title,
        "level": level,
        "priority": priority,
        "minutes": minutes,
        "summary": summary,
        "blocks": blocks,
    }


def mod(mid, title, topics):
    return {"id": mid, "title": title, "topics": topics}


def phase(title, modules):
    return {"title": title, "modules": modules}
