#!/usr/bin/env python3
import json
import os
import subprocess
from datetime import date
from pathlib import Path

PAPERS_MANIFEST = Path("papers/list.json")
MAX_ENTRIES_PER_PART = 100


def _read_json(path: Path):
    with path.open("r") as f:
        return json.load(f)


def _write_json(path: Path, data) -> None:
    with path.open("w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")


def _load_all_entries(manifest_path: Path) -> list:
    data = _read_json(manifest_path)
    if isinstance(data, dict) and isinstance(data.get("parts"), list):
        entries = []
        for part_name in data["parts"]:
            chunk = _read_json(manifest_path.parent / part_name)
            entries.extend(chunk)
        return entries
    if isinstance(data, list):
        return data
    raise ValueError(f"{manifest_path} is not a valid list or manifest")


def _is_newest_first(manifest_path: Path, parts: list) -> bool:
    """Return True if the manifest lists newest entries first (list_0000001 = newest).

    Detected by comparing the year of the first entry in the first part versus
    the last part.  If the first part's year is greater, the order is newest-first.
    """
    if len(parts) < 2:
        return False
    try:
        first_chunk = _read_json(manifest_path.parent / parts[0])
        last_chunk = _read_json(manifest_path.parent / parts[-1])
        first_year = int(first_chunk[0].get("year", 0)) if first_chunk else 0
        last_year = int(last_chunk[0].get("year", 0)) if last_chunk else 0
        return first_year > last_year
    except (ValueError, TypeError, IndexError, FileNotFoundError):
        return False


def check_and_split_papers() -> None:
    """Re-split papers/list.json if any part exceeds MAX_ENTRIES_PER_PART entries.

    After re-splitting:
      - list_0000001.json holds the oldest entries
      - The highest-indexed file holds the newest entries (add new papers here)
    """
    if not PAPERS_MANIFEST.exists():
        return

    data = _read_json(PAPERS_MANIFEST)
    if not isinstance(data, dict) or not isinstance(data.get("parts"), list):
        return
    parts = data["parts"]

    needs_split = any(
        len(_read_json(PAPERS_MANIFEST.parent / p)) > MAX_ENTRIES_PER_PART
        for p in parts
    )
    if not needs_split:
        return

    print(f"Re-splitting papers: a part exceeds {MAX_ENTRIES_PER_PART} entries...")

    all_entries = _load_all_entries(PAPERS_MANIFEST)

    # If currently newest-first, reverse so oldest entries go into list_0000001
    # and newest entries end up in the highest-indexed file.
    if _is_newest_first(PAPERS_MANIFEST, parts):
        all_entries = list(reversed(all_entries))

    # Remove old part files.
    stem = PAPERS_MANIFEST.stem
    for sibling in PAPERS_MANIFEST.parent.glob(f"{stem}_*.json"):
        if sibling.stem[len(stem) + 1:].isdigit():
            sibling.unlink()

    # Split into fixed-size chunks.
    chunks = [
        all_entries[i : i + MAX_ENTRIES_PER_PART]
        for i in range(0, len(all_entries), MAX_ENTRIES_PER_PART)
    ]

    part_names = []
    for i, chunk in enumerate(chunks, start=1):
        part_name = f"{stem}_{i:07d}.json"
        _write_json(PAPERS_MANIFEST.parent / part_name, chunk)
        part_names.append(part_name)
        print(f"  wrote {part_name} ({len(chunk)} entries)")

    _write_json(PAPERS_MANIFEST, {"parts": part_names})
    print(f"  manifest: {len(part_names)} parts — newest entries in {part_names[-1]}")


def update_html():
    current_date = date.today().strftime("%Y-%m-%d")

    with open('index.html', 'r') as file:
        content = file.readlines()

    for i, line in enumerate(content):
        if "Last updated:" in line:
            content[i] = f"    <small style=\"position:fixed;bottom:10px;left:12px;font-size:11px;opacity:0.4;pointer-events:none;\">Last updated: {current_date}</small>\n"

    with open('index.html', 'w') as file:
        file.writelines(content)

    return current_date


def git_operations(date):
    commands = [
        ['git', 'add', '.'],
        ['git', 'commit', '-m', f"Updated on {date}"],
        ['git', 'push']
    ]

    for cmd in commands:
        subprocess.run(cmd, check=True)


if __name__ == "__main__":
    check_and_split_papers()
    current_date = update_html()
    git_operations(current_date)
    print(f"Changes have been committed and pushed. Date updated to {current_date} in index.html")
