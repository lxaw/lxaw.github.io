"""Check that each event's Wikipedia source exists and that the event's year
(and day and month, when given) appear in the article, citations removed.

Fetches wikitext 20 titles per request and caches it in the system's
temporary directory (or the file named in WIKI_CACHE). This only shows that the figures are somewhere on the
page, so it is weaker than reading the source.

Usage:
    python check_sources.py history/events/poland.json ...
"""
import json
import os
import re
import sys
import tempfile
import time
import urllib.parse
import urllib.request
from pathlib import Path

API = "https://en.wikipedia.org/w/api.php"
CACHE = Path(os.environ.get("WIKI_CACHE") or Path(tempfile.gettempdir()) / "history_map_wiki_cache.json")
MONTHS = {"Jan": "January", "Feb": "February", "Mar": "March", "Apr": "April", "May": "May", "Jun": "June",
          "Jul": "July", "Aug": "August", "Sep": "September", "Oct": "October", "Nov": "November", "Dec": "December"}
cache = json.loads(CACHE.read_text()) if CACHE.exists() else {}


def title_of(url):
    return urllib.parse.unquote(url.split("/wiki/")[1]).replace("_", " ")


def fetch(titles):
    query = urllib.parse.urlencode({"action": "query", "prop": "revisions", "rvprop": "content", "rvslots": "main",
                                    "redirects": 1, "format": "json", "formatversion": 2, "titles": "|".join(titles)})
    req = urllib.request.Request(f"{API}?{query}", headers={"User-Agent": "history-map-source-check/1.0"})
    for attempt in range(5):
        try:
            data = json.load(urllib.request.urlopen(req, timeout=60))["query"]
            break
        except Exception as err:
            print(f"  retry after {err}", flush=True)
            time.sleep(20 * (attempt + 1))
    else:
        sys.exit("could not reach Wikipedia")
    back = {}
    for step in data.get("normalized", []) + data.get("redirects", []):
        back[step["to"]] = back.get(step["from"], step["from"])
    for page in data["pages"]:
        text = None if page.get("missing") else page["revisions"][0]["slots"]["main"]["content"]
        if text is not None:
            text = re.sub(r"<ref[^>/]*/>|<ref[^>]*>.*?</ref>", " ", text, flags=re.S)
            text = re.sub(r"\[\[(?:[^\]|]*\|)?([^\]]*)\]\]", r"\1", text).replace("&nbsp;", " ")
        original = page["title"]
        while original in back:
            original = back.pop(original)
        cache[original] = text
    CACHE.write_text(json.dumps(cache))
    time.sleep(2)


events = [ev for path in sys.argv[1:] for ev in json.load(open(path, encoding="utf-8"))]
wanted = sorted({title_of(ev["source"]) for ev in events if "wikipedia.org/wiki/" in ev["source"]} - set(cache))
for i in range(0, len(wanted), 20):
    fetch(wanted[i:i + 20])
for title in wanted:
    if title not in cache:  # lost in a batch (an odd redirect); ask for it alone
        fetch([title])

bad = 0
for ev in events:
    if "wikipedia.org/wiki/" not in ev["source"]:
        print(f"SKIP  {ev['id']}: not Wikipedia")
        continue
    title = title_of(ev["source"])
    text = cache.get(title, "")
    problems = []
    if title not in cache:
        problems.append("not fetched")
    elif text is None:
        problems.append("page missing")
    else:
        if not re.search(rf"\b{abs(ev['year-from'])}\b", text):
            problems.append(f"year {abs(ev['year-from'])} not in text")
        m = re.match(r"(?:(\d{1,2}) )?([A-Z][a-z]{2}) ", ev["date"])
        if m and m.group(2) in MONTHS:
            day, month, year = m.group(1), MONTHS[m.group(2)], abs(ev["year-from"])
            num = list(MONTHS.values()).index(month) + 1
            if day:
                pattern = rf"\b{day}(?:st|nd|rd|th)? {month}\b|\b{month} {day}\b|\|{year}\|0?{num}\|0?{day}\b"
            else:
                pattern = rf"\b{month}\b|\|{year}\|0?{num}\b"
            if not re.search(pattern, text):
                problems.append(f"'{(day + ' ') if day else ''}{month}' not in text")
    if problems:
        bad += 1
        print(f"FAIL  {ev['id']}: {'; '.join(problems)}  <{ev['source']}>")
print(f"{len(events)} events checked, {bad} need a look.")
