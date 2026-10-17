"""Helpers for curriculum topic dicts."""


def topic(
    topic_id: str,
    title: str,
    *,
    level: str,
    priority: str,
    minutes: int,
    summary: str,
    prereq: list[str] | None = None,
    blocks: list[dict] | None = None,
) -> dict:
    body = list(blocks or [])
    if prereq:
        body = [{"h": "Prerequisites", "ul": prereq}] + body
    return {
        "id": topic_id,
        "title": title,
        "level": level,
        "priority": priority,
        "minutes": minutes,
        "summary": summary,
        "blocks": body,
    }
