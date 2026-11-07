#!/usr/bin/env python3
"""Lab 6: does the incident report state what the traces and the PDPA demand?
Usage: python3 scripts/check_report.py outputs/ai-incident-report.docx (also reads .txt)"""
import re, sys, zipfile
p = sys.argv[1]
if p.lower().endswith(".docx"):
    xml = zipfile.ZipFile(p).read("word/document.xml").decode("utf-8")
    text = re.sub(r"<[^>]+>", " ", xml.replace("</w:p>", "\n"))
else:
    text = open(p, encoding="utf-8").read()
low = text.lower()
NEED = {"Root session id s-0807-0210": "s-0807-0210", "Exfiltration address": "audit-share.example",
        "Records affected 1,284": r"1,?284", "Leak time 02:17": r"02:17", "Injection source (fake supplier email)": "supplier",
        "Contain": "contain", "Assess": "assess", "Report": "report", "Evaluate": "evaluate", "PDPC": "pdpc",
        "3 calendar days": r"3 calendar days|three calendar days", "Five principles named": "traceability"}
miss = 0
for k, v in NEED.items():
    ok = re.search(v, low) is not None; miss += not ok
    print(f"{'PASS' if ok else 'MISSING':8s}{k}")
print("RESULT: READY for human review" if not miss else f"RESULT: {miss} gap(s). Check the traces and fix the report.")
