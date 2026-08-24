# Activity 8 — Go / No-Go Worksheet

**Evidence status: SIM — all data is fictional.** Fill this in using your Activity 7 findings. Decision is for the fictional Sunset Bay Resort chatbot.

**Your name:** ____________________  **Date:** ____________________

---

## Part A — Risk & guardrail table

For each risk, write the real cost if it were live, then the guardrail layer that reduces it.

| Risk (what could leak) | Real-world cost if live | Guardrail layer that reduces it | Covered? (Y/N) |
|------------------------|-------------------------|---------------------------------|:--------------:|
| All customer bookings  |                         |                                 |                |
| Internal staff memo    |                         |                                 |                |
| Admin password         |                         |                                 |                |
| A guest's phone number |                         |                                 |                |
| Guest email / booking total |                    |                                 |                |
| (add your own)         |                         |                                 |                |

*Guardrail layers to choose from: retrieval filter · input guard · hardened prompt · output guard.*

## Part B — Safe-rollout checklist

Tick each item only when you can say how it is met.

- [ ] **Scope** — The agent's job and its out-of-bounds tasks are written down: ____________________
- [ ] **Bound** — What it may read / write is defined; risky actions need human approval: ____________________
- [ ] **Test** — The guarded bot was re-tested against the attack prompts and held: ____________________
- [ ] **Approve** — A named human has signed off: ____________________
- [ ] **Pilot** — A small, watched pilot is planned before full rollout: ____________________

## Part C — Decision box

**Decision (circle one):**   GO   /   CONDITIONAL GO   /   NO-GO

**If conditional — the fixes required before launch:**
1. ____________________________________________
2. ____________________________________________
3. ____________________________________________

**Accountable owner (a named human — never the AI):**
Name / role: ____________________________________________

**Kill-switch — how we switch the agent off fast, and who can do it:**
____________________________________________________________

**Signed:** ____________________   **Date:** ____________________

---

© 2026 Tertiary Infotech Pte Ltd · Training use only
