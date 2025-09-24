#!/usr/bin/env python3
"""Optional richer miner using javalang."""

from __future__ import annotations

import csv
import pathlib
import sys

try:
    import javalang
except ImportError:  # pragma: no cover - optional dependency
    javalang = None


def classify(snippet: str) -> str:
    s = snippet.lower()
    if any(key in s for key in ["setvisible", " visible", "show(", "hide("]):
        return "visibility"
    if any(key in s for key in ["next", "previous", "navigate", "route", "switch", "case "]):
        return "branching"
    if any(key in s for key in ["required", "validate", "validation", "error", "adderror", "pattern.compile", "matches("]):
        return "validation"
    if any(key in s for key in ["equals", "compareto", "isafter", "isbefore", "age", "difference"]):
        return "computed"
    if any(key in s for key in ["options", "choices", "list", "lookup", "filter"]):
        return "options"
    return "unknown"


def iter_java_files(root: pathlib.Path):
    for path in root.rglob("*.java"):
        yield path


def mine(root: pathlib.Path, writer: csv.writer) -> None:
    if javalang is None:
        raise SystemExit("Install javalang to use mine.py (pip install javalang)")

    for path in iter_java_files(root):
        source = path.read_text(encoding="utf-8", errors="ignore")
        try:
            tree = javalang.parse.parse(source)
        except Exception:
            continue

        lines = source.splitlines()
        for _, node in tree.filter(javalang.tree.MethodInvocation):
            line_no = node.position.line if node.position else 0
            snippet = lines[line_no - 1].strip() if line_no > 0 and line_no <= len(lines) else ""
            writer.writerow([
                classify(snippet),
                "method",
                "",
                "",
                snippet,
                str(path),
                line_no,
            ])


def main() -> None:
    root = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path(".")
    writer = csv.writer(sys.stdout)
    writer.writerow(["kind", "scope", "target", "inputs", "condition_snippet", "file", "line"])
    mine(root, writer)


if __name__ == "__main__":
    main()
