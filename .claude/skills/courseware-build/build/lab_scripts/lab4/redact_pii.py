#!/usr/bin/env python3
"""Lab 4: data minimisation before the agent sees the file. Drops NRIC and birth date, masks name, mobile and email.
Usage: python3 scripts/redact_pii.py data/loyalty-members.csv outputs/loyalty-members.masked.csv"""
import csv, sys
src, dst = sys.argv[1], sys.argv[2]
rows = list(csv.DictReader(open(src, encoding="utf-8")))
out = []
for r in rows:
    first = r["name"].split()[0]
    out.append({"member_id": r["member_id"], "name": first[0] + "***", "mobile": "****" + r["mobile"][-4:],
                "email": r["email"][0] + "***@" + r["email"].split("@")[1], "points": r["points"], "last_visit": r["last_visit"]})
with open(dst, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(out[0].keys())); w.writeheader(); w.writerows(out)
print(f"{len(out)} members masked. NRIC and birth date removed. Saved to {dst}")
