#!/usr/bin/env python3
"""Lab 1: check the agent's work. Finds real clashes in the mock Kopi Kaki calendar.
Usage: python3 scripts/clash_check.py data/seed-calendar.csv
Compare this list with what your always-on assistant told you."""
import csv, sys
from datetime import datetime as D
rows = list(csv.DictReader(open(sys.argv[1] if len(sys.argv) > 1 else "data/seed-calendar.csv", encoding="utf-8")))
for r in rows:
    r["s"] = D.fromisoformat(r["start"]); r["e"] = D.fromisoformat(r["end"])
rows.sort(key=lambda r: r["s"])
n = 0
for i, a in enumerate(rows):
    for b in rows[i + 1:]:
        if b["s"] < a["e"]:
            n += 1
            print(f"CLASH  {a['start']}  {a['title']}  <->  {b['title']}")
print(f"{len(rows)} meetings checked, {n} clash(es) found (Asia/Singapore time).")
