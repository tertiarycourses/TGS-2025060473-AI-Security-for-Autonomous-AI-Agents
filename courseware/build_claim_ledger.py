#!/usr/bin/env python3
"""Generate the v3.0 slide-level claim and source ledger."""

from pathlib import Path
from v30_content import SLIDES, SOURCES

OUT = Path(__file__).resolve().parent.parent / "research" / "CLAIM-LEDGER-v30.md"


def esc(value):
    return str(value).replace("|", "\\|").replace("\n", " ")


lines = [
    "# Claim Ledger — v3.0",
    "",
    "Generated from `courseware/v30_content.py`. Evidence labels distinguish sourced facts, "
    "product documentation, reported research, verified cases, simulations and course synthesis.",
    "",
    "| Slide | Title | Evidence | Source IDs | Claim / caveat |",
    "|---:|---|---|---|---|",
]

for slide in SLIDES:
    payload = slide.get("note")
    if not payload:
        items = (slide.get("points") or slide.get("steps") or slide.get("cards") or
                 slide.get("rows") or slide.get("left") or [])
        payload = "; ".join(" — ".join(map(str, x)) if isinstance(x, (list, tuple)) else str(x)
                            for x in items[:3])
    lines.append(f"| {slide['n']} | {esc(slide['title'])} | {esc(slide['evidence'])} | "
                 f"{esc(', '.join(slide.get('sources', [])) or '—')} | {esc(payload or '—')} |")

lines += ["", "## Source Register", "", "| ID | Source | URL |", "|---|---|---|"]
for sid, item in SOURCES.items():
    lines.append(f"| {sid} | {esc(item['title'])} | {item['url']} |")

OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
print(OUT)
