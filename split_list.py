"""
Split a large JSON list file into chunks of ~500 lines each.

Usage:
    python split_list.py <path-to-list.json> [--max-lines N]

Behavior:
  - The input file must contain either:
      (a) a plain JSON array of objects (original, unsplit list), or
      (b) a manifest of the form {"parts": ["list_0000001.json", ...]}
          whose referenced parts live in the same directory.
  - All entries are read (manifests are expanded), then the line count of
    the combined data (serialized with indent=2) is measured.
  - If the combined file would exceed --max-lines (default 500), it is
    split into files of at most that many lines, named
    "<stem>_0000001.json", "<stem>_0000002.json", ... next to the input.
    The input path is then rewritten as a manifest pointing at those parts.
  - If the file is already under the threshold, the script leaves things
    alone (but normalizes the manifest if it already was one).

This is compatible with the website's `loadList(...)` helper, which reads
the path, detects a manifest, and fetches+concatenates the parts.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

DEFAULT_MAX_LINES = 500


def load_all_entries(path: Path) -> list:
    """Read either an array file or a manifest file, return all entries."""
    with path.open("r") as f:
        data = json.load(f)

    if isinstance(data, dict) and isinstance(data.get("parts"), list):
        entries: list = []
        for part_name in data["parts"]:
            part_path = path.parent / part_name
            with part_path.open("r") as f:
                chunk = json.load(f)
            if not isinstance(chunk, list):
                raise ValueError(f"Manifest part {part_path} is not a JSON array")
            entries.extend(chunk)
        return entries

    if isinstance(data, list):
        return data

    raise ValueError(
        f"{path} must be a JSON array or a manifest object with a 'parts' list"
    )


def line_count(obj) -> int:
    """Line count of obj when serialized with indent=2."""
    return json.dumps(obj, indent=2, ensure_ascii=False).count("\n") + 1


def chunk_entries(entries: list, max_lines: int) -> list[list]:
    """Greedy split so each chunk's serialized form is <= max_lines lines.

    Each chunk is a JSON array; the wrapping '[' and ']' contribute 2 lines,
    and each entry contributes its own line count plus 1 (for the trailing
    comma or closing bracket newline). A single oversized entry is placed
    alone in its own chunk even if it exceeds max_lines.
    """
    chunks: list[list] = []
    current: list = []
    # Lines already spoken for by '[' and ']'.
    current_lines = 2

    for entry in entries:
        # Lines contributed by this entry: its own pretty-printed lines
        # (which already start indented within an array).
        entry_lines = line_count(entry)

        if current and current_lines + entry_lines > max_lines:
            chunks.append(current)
            current = []
            current_lines = 2

        current.append(entry)
        current_lines += entry_lines

    if current:
        chunks.append(current)

    return chunks


def write_json(path: Path, data) -> None:
    with path.open("w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")


def cleanup_old_parts(path: Path) -> None:
    """Remove existing <stem>_NNNNNNN.json siblings so stale parts don't linger."""
    stem = path.stem
    for sibling in path.parent.glob(f"{stem}_*.json"):
        # Only touch files that match the numeric-suffix pattern we produce.
        suffix = sibling.stem[len(stem) + 1 :]  # after "<stem>_"
        if suffix.isdigit():
            sibling.unlink()


def split_list(path: Path, max_lines: int) -> None:
    entries = load_all_entries(path)
    combined_lines = line_count(entries)

    print(f"{path}: {len(entries)} entries, {combined_lines} lines combined")

    if combined_lines <= max_lines:
        # Already small enough. If it's a manifest, we leave the parts alone.
        # If it's a plain array, we don't touch it.
        print(f"  <= {max_lines} lines; no split needed.")
        return

    chunks = chunk_entries(entries, max_lines)
    print(f"  splitting into {len(chunks)} parts (max {max_lines} lines each)")

    cleanup_old_parts(path)

    stem = path.stem
    ext = path.suffix
    part_names: list[str] = []
    for i, chunk in enumerate(chunks, start=1):
        part_name = f"{stem}_{i:07d}{ext}"
        part_path = path.parent / part_name
        write_json(part_path, chunk)
        part_names.append(part_name)
        print(f"  wrote {part_path} ({len(chunk)} entries, {line_count(chunk)} lines)")

    write_json(path, {"parts": part_names})
    print(f"  wrote manifest {path} -> {len(part_names)} parts")


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", help="Path to the list.json file to check/split")
    parser.add_argument(
        "--max-lines",
        type=int,
        default=DEFAULT_MAX_LINES,
        help=f"Maximum lines per chunk file (default: {DEFAULT_MAX_LINES})",
    )
    args = parser.parse_args(argv)

    path = Path(args.path)
    if not path.is_file():
        print(f"error: {path} does not exist or is not a file", file=sys.stderr)
        return 1

    split_list(path, args.max_lines)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
