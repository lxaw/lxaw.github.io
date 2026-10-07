"""
Validate the history map's events (history/events/*.json and
history/events/deep/*.json) and print how many each country or deep-time
scope has.

Checks every event for the required fields, sane coordinates and years, a
year in "date" that matches "year-from"/"year-to", a unique id, a source URL,
and (for events that link to an article) that the file and #anchor exist.
Deep-time events are dated in millions of years ago ("ma") instead and belong
to a scope rather than a country.

Usage:
    python check_events.py
"""

from __future__ import annotations
import json
import re
import sys
from pathlib import Path

EVENTS_DIR = Path("history/events")
MANIFEST = EVENTS_DIR / "list.json"
REQUIRED = ["id", "title", "date", "year-from", "place", "lat", "lon",
            "country", "importance", "description", "source"]
DEEP_REQUIRED = ["id", "title", "date", "ma", "scope", "importance",
                 "description", "source"]
SCOPES = ["Universe", "Milky Way", "Solar System", "Earth", "Life"]


def check_deep_event(event: dict, seen_ids: set[str]) -> list[str]:
    """Return a list of problems with one deep-time event."""
    problems = [f"missing '{key}'" for key in DEEP_REQUIRED if event.get(key) in (None, "")]
    if problems:
        return problems

    if event["id"] in seen_ids:
        problems.append("duplicate id")
    seen_ids.add(event["id"])

    if event["scope"] not in SCOPES:
        problems.append(f"scope must be one of {SCOPES}")
    if event["importance"] not in (1, 2, 3):
        problems.append("importance must be 1, 2 or 3")

    ma = event["ma"]
    ma_to = event.get("ma-to", ma)
    if not all(isinstance(v, (int, float)) for v in (ma, ma_to)) or not 0 < ma <= 13800:
        problems.append(f"ma must be a number of millions of years ago, up to 13800: {ma}")
    elif not 0 <= ma_to <= ma:
        problems.append("ma-to must be the later (smaller) number")
    if "years ago" not in event["date"]:
        problems.append('date should read like "541 million years ago"')

    has = [key for key in ("lat", "lon") if key in event]
    if len(has) == 1:
        problems.append("lat and lon must be given together")
    elif has and (not -90 <= event["lat"] <= 90 or not -180 <= event["lon"] <= 180):
        problems.append(f"coordinates out of range: {event['lat']}, {event['lon']}")

    if not event["source"].startswith("http"):
        problems.append("source must be a URL")
    return problems


def check_event(event: dict, seen_ids: set[str]) -> list[str]:
    """Return a list of problems with one event (empty if it is fine)."""
    if "ma" in event or "scope" in event:
        return check_deep_event(event, seen_ids)
    problems = [f"missing '{key}'" for key in REQUIRED if event.get(key) in (None, "")]
    if problems:
        return problems

    if event["id"] in seen_ids:
        problems.append("duplicate id")
    seen_ids.add(event["id"])

    if not -90 <= event["lat"] <= 90 or not -180 <= event["lon"] <= 180:
        problems.append(f"coordinates out of range: {event['lat']}, {event['lon']}")
    if event["importance"] not in (1, 2, 3):
        problems.append("importance must be 1, 2 or 3")

    year_from = event["year-from"]
    year_to = event.get("year-to", year_from)
    if year_from > year_to:
        problems.append("year-from is after year-to")

    # Any four-digit year written in "date" should be one of the event's years.
    for year in re.findall(r"\b\d{4}\b", event["date"]):
        if int(year) not in (abs(year_from), abs(year_to)):
            problems.append(f"date says {year} but years are {year_from}..{year_to}")

    if not event["source"].startswith("http"):
        problems.append("source must be a URL")

    link = event.get("link")
    if link and not link.startswith("http"):
        target, _, anchor = link.partition("#")
        if not Path(target).is_file():
            problems.append(f"link target not found: {target}")
        elif anchor and f'id="{anchor}"' not in Path(target).read_text(encoding="utf-8"):
            problems.append(f"anchor #{anchor} not found in {target}")

    return problems


def main() -> int:
    with MANIFEST.open("r") as f:
        parts = json.load(f)["parts"]

    seen_ids: set[str] = set()
    total = 0
    total_problems = 0

    on_disk = {p.relative_to(EVENTS_DIR).as_posix() for p in EVENTS_DIR.glob("**/*.json")}
    unlisted = on_disk - set(parts) - {MANIFEST.name}
    for name in sorted(unlisted):
        print(f"{name}: not listed in {MANIFEST}")
        total_problems += 1

    print(f"{'country / scope':<24}{'events':>7}{'with article':>14}{'years':>24}")
    for part_name in parts:
        with (EVENTS_DIR / part_name).open("r", encoding="utf-8") as f:
            events = json.load(f)

        problems = []
        for event in events:
            for problem in check_event(event, seen_ids):
                problems.append(f"  [{event.get('id') or event.get('title', '?')}] {problem}")

        deep = part_name.startswith("deep/")
        countries = sorted({e.get("scope" if deep else "country", "?") for e in events})
        if len(countries) != 1 and not deep:
            problems.append(f"  more than one country in file: {countries}")

        if deep:
            ages = [e["ma"] for e in events if isinstance(e.get("ma"), (int, float))]
            span = f"{max(ages):g} to {min(ages):g} Ma" if ages else "-"
        else:
            years = [e["year-from"] for e in events if "year-from" in e]
            span = f"{min(years)} to {max(years)}" if years else "-"
        with_article = sum(1 for e in events if e.get("link"))
        print(f"{', '.join(countries):<24}{len(events):>7}{with_article:>14}{span:>24}")
        for line in problems:
            print(line)

        total += len(events)
        total_problems += len(problems)

    print(f"\n{total} events in {len(parts)} files.")
    if total_problems:
        print(f"{total_problems} problem(s) found.")
        return 1
    print("No problems found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
