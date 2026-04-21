"""
Normalise tags across all papers/list_*.json part files.

Merges known redundant / misspelled / variant tags into a single canonical
form, then (optionally) re-saves each part file in place.

Usage:
    python clean_tags.py           # dry-run: shows what would change
    python clean_tags.py --apply   # apply changes and overwrite part files
"""

from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path
from collections import defaultdict

# ---------------------------------------------------------------------------
# Merge map  alias → canonical
# Each entry means: "replace any occurrence of the key tag with the value."
# Keys are matched case-insensitively after stripping whitespace.
# ---------------------------------------------------------------------------
MERGES: dict[str, str] = {
    # ── Plurals / singular ──────────────────────────────────────────────
    "llms":                     "llm",
    "tokens":                   "token",
    "transformers":             "transformer",
    "optimizers":               "optimizer",
    "hypernetwork":             "hypernetworks",

    # ── Hyphenation / spacing variants ──────────────────────────────────
    "flow-matching":            "flow matching",
    "multi-modal":              "multimodal",
    "meta learning":            "meta-learning",
    "meta tokens":              "meta-tokens",
    "fine-tuning":              "finetuning",

    # ── Typos ────────────────────────────────────────────────────────────
    "inpatining":               "inpainting",
    "guassian":                 "gaussian",

    # ── Abbreviation ↔ full form (keep the shorter/more-used one) ────────
    "reinforcement learning":   "rl",
    "reinforcement":            "rl",
    "stochastic gradient descent": "sgd",
    "fsl":                      "few-shot",
    "neural tangent kernel":    "ntk",
    "low rank adaptation":      "lora",
    "diffusion llm":            "dllm",

    # ── Near-synonyms ────────────────────────────────────────────────────
    "speculative sampling":     "speculative decoding",
    "self-correct":             "self-correction",
    "self-refinement":          "self-correction",
    "efficient inference":      "efficiency",
    "generative":               "generative models",
    "cache":                    "caching",
    "autoregression":           "autoregressive",
    "distillation":             "knowledge distillation",
    "self distillation":        "knowledge distillation",
}

# Build a lower-case lookup once
_MERGE_LOWER: dict[str, str] = {k.lower(): v for k, v in MERGES.items()}


def normalise_topic(topic: str) -> str:
    """Apply merge map to a comma-separated topic string."""
    if not topic:
        return topic
    out = []
    seen: set[str] = set()
    for raw in topic.split(","):
        t = raw.strip().lower()
        if not t:
            continue
        canonical = _MERGE_LOWER.get(t, t)
        if canonical not in seen:
            seen.add(canonical)
            out.append(canonical)
    return ", ".join(out)


def process_part(path: Path, apply: bool) -> dict[str, list[str]]:
    """Process one part file. Returns {paper_title: [old_topic, new_topic]} for changed papers."""
    with path.open("r") as f:
        papers = json.load(f)

    changes: dict[str, list[str]] = {}
    for paper in papers:
        old = paper.get("topic", "") or ""
        new = normalise_topic(old)
        if new != old:
            changes[paper.get("title", "?")] = [old, new]
            paper["topic"] = new

    if apply and changes:
        with path.open("w") as f:
            json.dump(papers, f, indent=2, ensure_ascii=False)
            f.write("\n")

    return changes


def tag_frequency(parts_dir: Path, manifest: dict) -> dict[str, int]:
    freq: dict[str, int] = defaultdict(int)
    for part_name in manifest["parts"]:
        with (parts_dir / part_name).open("r") as f:
            for paper in json.load(f):
                for t in (paper.get("topic") or "").split(","):
                    t = t.strip().lower()
                    if t:
                        freq[t] += 1
    return dict(freq)


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true",
                        help="Write changes to disk (default: dry-run only)")
    args = parser.parse_args(argv)

    manifest_path = Path("papers/list.json")
    with manifest_path.open("r") as f:
        manifest = json.load(f)

    if not (isinstance(manifest, dict) and "parts" in manifest):
        print("papers/list.json is not a manifest — run split_list.py first.")
        return 1

    parts_dir = manifest_path.parent
    total_changes = 0

    for part_name in manifest["parts"]:
        part_path = parts_dir / part_name
        changes = process_part(part_path, apply=args.apply)
        if changes:
            print(f"\n{part_name}: {len(changes)} paper(s) changed")
            for title, (old, new) in changes.items():
                print(f"  [{title[:60]}]")
                print(f"    before: {old}")
                print(f"    after:  {new}")
        total_changes += len(changes)

    if total_changes == 0:
        print("No changes needed — tags are already clean.")
        return 0

    if args.apply:
        print(f"\n✓ Applied {total_changes} change(s) across {len(manifest['parts'])} part file(s).")
        freq = tag_frequency(parts_dir, manifest)
        print(f"  Unique tags after cleanup: {len(freq)}")
    else:
        print(f"\nDry-run complete — {total_changes} change(s) pending.")
        print("Re-run with --apply to write changes.")

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
