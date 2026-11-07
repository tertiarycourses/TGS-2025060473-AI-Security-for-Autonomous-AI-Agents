#!/usr/bin/env python3
"""Lab 6: read the agent's traces yourself, so you can check what the AI tells you.
Usage: python3 scripts/trace_query.py data/agent-traces.jsonl            (overview, odd events)
       python3 scripts/trace_query.py data/agent-traces.jsonl s-0807-0210 (one session)"""
import collections, json, sys
ev = [json.loads(l) for l in open(sys.argv[1], encoding="utf-8") if l.strip()]
if len(sys.argv) > 2:
    for e in ev:
        if e["session"] == sys.argv[2]:
            print(e["ts"], f"{e['event']:12s}", e.get("tool") or "-", e.get("target") or "-", e.get("bytes") or "", e.get("status") or "", e.get("note") or "")
    sys.exit()
print(f"{len(ev)} events, {ev[0]['ts']} to {ev[-1]['ts']}")
print("By event type:", dict(collections.Counter(e["event"] for e in ev)))
print("Models used:", dict(collections.Counter(e["model"] for e in ev)))
print("\nSessions that touched personal data or an external address:")
seen = {}
for e in ev:
    t = str(e.get("target") or "")
    if "loyalty-members" in t or (e.get("tool") == "http_post"):
        seen.setdefault(e["session"], []).append(e)
for s, items in seen.items():
    print(" ", s, "|", "; ".join(f"{i['ts'][11:16]} {i['tool']} {i['target']}" for i in items))
