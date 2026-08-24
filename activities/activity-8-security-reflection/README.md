# Activity 8 — Reflect on Agent Security and Decide Go / No-Go

**Purpose:** Use what you learned in Activity 7 to weigh the risks of a real chatbot rollout and make a clear go / conditional / no-go decision with an accountable owner.

## What you need

- Your notes and findings from **Activity 7** (what leaked, which guardrail stopped it)
- The worksheet in this folder: `WORKSHEET.md`

**Evidence status: SIM — all data is fictional.** You are deciding on a made-up rollout for the fictional Sunset Bay Resort.

## Steps

1. **List what a real leak could cost.** Using Activity 7, write down the real-world harm if this were live data — lost guest trust, a PDPA breach, financial loss, reputational damage.
2. **Map each guardrail to a risk.** For each risk (leaked bookings, leaked memo, leaked password, leaked personal data), name the guardrail layer that reduces it (retrieval filter / input guard / hardened prompt / output guard).
3. **Apply the safe-rollout framework** — five steps, in order:
   - **Scope** — what will the agent do, and what is out of bounds?
   - **Bound** — what data may it read/write, and what needs human approval?
   - **Test** — re-run the attack prompts; does the guarded bot hold?
   - **Approve** — a named human signs off.
   - **Pilot** — start small, watch closely, then expand.
4. **Make the decision:** **Go**, **Conditional go** (with named fixes), or **No-go**.
5. **Name the accountable owner** (a human, never the AI) and a **kill-switch** — how to switch the agent off fast if something goes wrong.
6. Complete `WORKSHEET.md` as your record.

## What you produce

- A completed risk-and-guardrail table
- A completed rollout checklist (scope → bound → test → approve → pilot)
- A signed go / conditional / no-go decision with a named owner and a kill-switch

## Reflect (Data Privacy / Job Impact / Ethical Concerns / Cyber Security)

- **Data Privacy:** Which single leak from Activity 7 would be the most damaging, and why?
- **Job Impact:** Who owns the agent day-to-day once it goes live, and what does that job involve?
- **Ethical Concerns:** If you chose "Go", could you defend it to an affected guest?
- **Cyber Security:** What would make you pull the kill-switch immediately?

---

© 2026 Tertiary Infotech Pte Ltd · Training use only
