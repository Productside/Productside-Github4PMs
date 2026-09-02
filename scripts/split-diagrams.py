#!/usr/bin/env python3
"""Split docs/diagrams.md into one file per diagram in docs/diagrams/.

docs/diagrams.md is the source of truth and the reading order for the diagram set.
This regenerates the individual files from it, so the two can never drift.

    python3 scripts/split-diagrams.py
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "docs" / "diagrams.md"
OUT = ROOT / "docs" / "diagrams"


def slug(text: str) -> str:
    text = text.lower().replace("&", "and")
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return re.sub(r"-{2,}", "-", text).strip("-")


def parse(text: str):
    """Yield (number, title, beat, body) for each '## N. Title' section."""
    beat = None
    number = title = None
    body: list[str] = []
    for line in text.splitlines():
        heading = re.match(r"^## (\d+)\.\s+(.*)$", line)
        if heading:
            if number:
                yield number, title, beat, "\n".join(body).strip()
            number, title = heading.group(1), heading.group(2).strip()
            body = []
            continue
        if line.startswith("# ") and not line.startswith("# Diagrams"):
            if number:
                yield number, title, beat, "\n".join(body).strip()
                number = title = None
                body = []
            beat = line[2:].strip()
            continue
        if number:
            body.append(line)
    if number:
        yield number, title, beat, "\n".join(body).strip()


def main() -> int:
    if not SOURCE.exists():
        print(f"missing {SOURCE}", file=sys.stderr)
        return 1

    OUT.mkdir(parents=True, exist_ok=True)
    for stale in OUT.glob("*.md"):
        stale.unlink()

    rows = []
    for number, title, beat, body in parse(SOURCE.read_text(encoding="utf-8")):
        name = f"{int(number):02d}-{slug(title)}.md"
        clean = re.sub(r"\n-{3,}\n", "\n", body).strip()
        has_diagram = "```mermaid" in clean
        page = (
            f"# {title}\n\n"
            f"**{beat}**\n\n"
            f"{clean}\n\n"
            f"---\n\n"
            f"[All diagrams](INDEX.md) · [Diagram source](../diagrams.md)\n"
        )
        (OUT / name).write_text(page, encoding="utf-8")
        rows.append((int(number), title, beat, name, has_diagram))

    lines = [
        "# Diagrams — Index",
        "",
        "One file per diagram. **Generated — do not edit these by hand.**",
        "Edit [`../diagrams.md`](../diagrams.md) and run `python3 scripts/split-diagrams.py`.",
        "",
        "| # | Diagram | Beat |",
        "|---|---|---|",
    ]
    for n, title, beat, name, has in sorted(rows):
        label = title if has else f"{title} *(note, no diagram)*"
        lines.append(f"| {n} | [{label}]({name}) | {beat} |")
    lines.append("")
    (OUT / "INDEX.md").write_text("\n".join(lines), encoding="utf-8")

    diagrams = sum(1 for r in rows if r[4])
    print(f"wrote {len(rows)} files ({diagrams} with diagrams) to docs/diagrams/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
