#!/usr/bin/env python3
"""Summarize mined Java rules into a Markdown digest."""

from __future__ import annotations

import argparse
import csv
import io
import itertools
from collections import Counter, defaultdict
from pathlib import Path
from textwrap import dedent
import codecs


DEFAULT_INPUT = Path(__file__).parent / "sample-output" / "rules.csv"
DEFAULT_OUTPUT = Path(__file__).parent.parent.parent / "docs" / "rules-digest.md"


KEYWORDS = {
    "visibility": ["setvisible", " visible", "show(", "hide("],
    "branching": ["next", "previous", "navigate", "route", "switch", "case "],
    "validation": ["required", "validate", "validation", "error", "adderror", "pattern.compile", "matches("],
    "computed": ["equals", "compareto", "isafter", "isbefore", "age", "difference"],
    "options": ["options", "choices", "list", "lookup", "filter"],
}


def classify(snippet: str, current: str) -> str:
    if current and current != "unknown":
        return current
    s = snippet.lower()
    for kind, tokens in KEYWORDS.items():
        if any(token in s for token in tokens):
            return kind
    return "unknown"


def load_csv(path: Path) -> list[dict[str, str]]:
    raw = path.read_bytes()
    if raw.startswith(codecs.BOM_UTF16_LE):
        text = raw.decode("utf-16-le")
    elif raw.startswith(codecs.BOM_UTF16_BE):
        text = raw.decode("utf-16-be")
    elif raw.startswith(codecs.BOM_UTF8):
        text = raw.decode("utf-8")
    else:
        text = raw.decode("utf-8", errors="ignore")
    reader = csv.DictReader(io.StringIO(text))
    return list(reader)


def normalize_row(row: dict[str, str]) -> dict[str, str]:
    snippet = (row.get("condition_snippet") or row.get("snippet") or "").strip()
    kind = (row.get("kind") or "unknown").strip().lower()
    kind = classify(snippet, kind)
    target = (row.get("target") or "").strip()
    if not target:
        # try to infer from pagename reference inside snippet
        for token in itertools.chain(row.get("inputs", "" ).split(), snippet.split()):
            if "page" in token.lower():
                target = token.strip(',;')
                break
    return {
        "kind": kind,
        "scope": (row.get("scope") or "").strip(),
        "target": target,
        "inputs": (row.get("inputs") or "").strip(),
        "snippet": snippet,
        "file": (row.get("file") or "").strip(),
        "line": (row.get("line") or "").strip(),
    }


def summarize(rows, limit: int):
    kind_counts = Counter()
    target_counts = defaultdict(Counter)
    samples = defaultdict(list)

    for row in rows:
        kind = row["kind"] or "unknown"
        kind_counts[kind] += 1
        key = row["target"] or row["file"]
        if key:
            target_counts[kind][key] += 1
        if len(samples[kind]) < limit:
            samples[kind].append(row)

    return kind_counts, target_counts, samples


def render_markdown(kind_counts, target_counts, samples, limit: int) -> str:
    lines: list[str] = []
    total = sum(kind_counts.values()) or 1

    lines.append("# Rule Miner Digest\n")
    lines.append(
        dedent(
            f"""
            Generated from `tools/rule-miner/sample-output/rules.csv`.
            Total matches: **{total}** across **{len(kind_counts)}** rule kinds.
            """
        ).strip()
    )
    lines.append("")

    lines.append("## Distribution by kind\n")
    lines.append("| Kind | Count | Share |\n|------|-------|-------|")
    for kind, count in kind_counts.most_common():
        share = (count / total) * 100
        lines.append(f"| {kind} | {count} | {share:.1f}% |")
    lines.append("")

    for kind, counts in target_counts.items():
        lines.append(f"## Top targets – {kind}\n")
        lines.append("| Target / Page | Hits |\n|---------------|------|")
        for target, count in counts.most_common(limit):
            display = target or "(unknown)"
            lines.append(f"| {display} | {count} |")
        lines.append("")

        lines.append(f"### Sample snippets ({kind})\n")
        for row in samples[kind]:
            location = f"{row['file']}:{row['line']}" if row["file"] else "(unknown)"
            snippet = row["snippet"].replace("|", "\\|")
            lines.append(f"- `{location}` — {snippet}")
        lines.append("")

    lines.append(
        dedent(
            """
            ---
            _Regenerate with_: `python tools/rule-miner/summarize.py`
            """
        ).strip()
    )

    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", default=str(DEFAULT_INPUT))
    parser.add_argument("--output", "-o", default=str(DEFAULT_OUTPUT))
    parser.add_argument("--limit", "-n", type=int, default=20, help="Top entries per section")
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)

    raw_rows = load_csv(input_path)
    rows = [normalize_row(row) for row in raw_rows]
    kind_counts, target_counts, samples = summarize(rows, args.limit)
    markdown = render_markdown(kind_counts, target_counts, samples, args.limit)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(markdown, encoding="utf-8")
    print(f"Wrote digest to {output_path.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
