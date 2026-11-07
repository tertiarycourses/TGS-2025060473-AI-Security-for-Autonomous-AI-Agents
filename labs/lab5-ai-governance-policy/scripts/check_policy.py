#!/usr/bin/env python3
"""Lab 5: does your AI Governance Policy cover all five principles and name real people?
Usage: python3 scripts/check_policy.py outputs/ai-governance-policy.docx (also reads .txt)"""
import re, sys, zipfile
p = sys.argv[1]
if p.lower().endswith(".docx"):
    xml = zipfile.ZipFile(p).read("word/document.xml").decode("utf-8")
    text = re.sub(r"<[^>]+>", " ", xml.replace("</w:p>", "\n"))
else:
    text = open(p, encoding="utf-8").read()
low = text.lower()
NEED = {"Data Control": "data control", "Permission Control": "permission control", "Human in the Loop": "human in the loop",
        "Traceability": "traceability", "Right-Sized Models": "right-sized model", "Named owner": "owner",
        "PDPA reference": "pdpa", "Incident reporting": "incident", "Review date": "review"}
miss = 0
for k, v in NEED.items():
    ok = v in low; miss += not ok
    print(f"{'PASS' if ok else 'MISSING':8s}{k}")
print(f"{len(text.split())} words.", "RESULT: READY for human review" if not miss else f"RESULT: {miss} gap(s). Ask the agent to fix them.")
