#!/usr/bin/env python3
"""Lab 4: an output guardrail. Scans an agent reply for personal data before anyone sends it.
Usage: python3 scripts/leak_scan.py outputs/agency-sample-weak.txt"""
import re, sys
text = open(sys.argv[1], encoding="utf-8").read()
CHECKS = {"NRIC": r"\b[STFGM]\d{7}[A-Z]\b", "Mobile": r"(?<![\d*])[89]\d{7}\b",
          "Email": r"\b[\w.]{2,}@example\.com\b", "Birth date": r"\b(19[4-9]\d|200\d)-\d{2}-\d{2}\b"}
total = 0
print(f"File: {sys.argv[1]}")
for name, rx in CHECKS.items():
    n = len(re.findall(rx, text)); total += n
    print(f"{name:11s} {n}")
print("RESULT:", f"LEAK - {total} personal data items found. Do not send." if total else "CLEAN - no personal data found.")
