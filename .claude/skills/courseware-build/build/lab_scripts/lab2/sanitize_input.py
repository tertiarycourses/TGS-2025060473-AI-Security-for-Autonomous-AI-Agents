#!/usr/bin/env python3
"""Lab 2: an input guardrail that runs BEFORE the model. It does not ask the model to behave:
it flags instruction-like text in customer comments and removes it from the copy the agent reads.
Usage: python3 scripts/sanitize_input.py data/customer-feedback.csv outputs/customer-feedback.clean.csv"""
import csv, re, sys
src, dst = sys.argv[1], sys.argv[2]
PATTERNS = [r"https?://", r"\bignore\b.*\binstruction", r"\bsystem (notice|message|prompt)\b",
            r"\bnote from\b", r"\bmust (close|end|include)\b", r"\bverbatim\b", r"\[.*\]"]
rx = re.compile("|".join(PATTERNS), re.I | re.S)
rows = list(csv.DictReader(open(src, encoding="utf-8")))
flagged = 0
for r in rows:
    if rx.search(r["comment"]):
        flagged += 1
        print(f"FLAGGED  id={r['id']}  {r['customer']}: {r['comment'][:90]}...")
        r["comment"] = "[removed by input guardrail: instruction-like text. A person must review this row.]"
with open(dst, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
print(f"{len(rows)} rows read, {flagged} flagged. Clean copy saved to {dst}")
