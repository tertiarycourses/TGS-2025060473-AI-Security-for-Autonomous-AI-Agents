#!/usr/bin/env python3
"""Lab 3: a guardrail no prompt can talk its way past. Code, not a request to the model.
Only codes on the allowlist get through; anything above 10% is refused and logged.
Usage: python3 scripts/voucher_gate.py STAFF-FREE-100"""
import datetime as dt, sys
ALLOW = {"KAKI10": 10}
code = (sys.argv[1] if len(sys.argv) > 1 else "").strip().upper()
pct = ALLOW.get(code)
stamp = dt.datetime.now().isoformat(timespec="seconds")
if pct is None:
    print(f"{stamp}  DENIED  {code or '(blank)'}  not on the allowlist. Needs a human manager.")
    sys.exit(1)
print(f"{stamp}  ALLOWED  {code}  {pct}% goodwill voucher.")
