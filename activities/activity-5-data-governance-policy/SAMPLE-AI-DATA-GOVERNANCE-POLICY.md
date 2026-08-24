# Sample AI Data Governance Policy — Sunset Bay Resort Singapore

**Evidence status: SIM — all data is fictional.** A generic sample for training only. It does not describe a real business. Aligned in spirit with the **IMDA Model AI Governance Framework** and the **Singapore Personal Data Protection Act (PDPA)**. No clause numbers are quoted.

**Owner of this policy:** General Manager, Sunset Bay Resort Singapore
**Version:** 1.0 · **Effective:** 25 August 2026 · **Next review:** 25 August 2027

---

## 1. Scope

This policy covers every AI system and AI agent used at the resort, and the data they touch.

- **AI systems / agents covered:** the WhatsApp guest-support agent, the marketing-analysis agent (spreadsheets), the slide-building agent, and any chatbot on our website.
- **Data assets covered:** guest booking records, guest contact details, marketing spreadsheets (spend and revenue), generated PowerPoint files and reports, and any training data or examples supplied to an agent.
- **Out of scope:** personal devices and private accounts of staff not used for resort work.

## 2. Roles

| Role | Who (example) | Responsibility |
|------|---------------|----------------|
| **Data Owner** | Front Office Manager | Owns guest data; decides what may be shared with an agent. |
| **Agent Owner** | Marketing Manager | Owns each AI agent; keeps its settings and skills current. |
| **Approver** | General Manager | Approves new agents, new skills, and any change to data rules. |
| **Reviewer** | Duty Supervisor | Checks agent output for accuracy before it reaches a guest or manager. |

A named human always holds each role. The AI holds none of them.

## 3. Principles

- **Accuracy** — Output is checked by a human before it is acted upon.
- **Purpose limitation** — Data is used only for the task it was collected for.
- **Protection** — Personal data is kept secure and shared only with approved agents.
- **Provenance** — We know where each piece of data and each agent skill came from.
- **Traceability** — Agent actions can be traced afterwards through logs.
- **Human accountability** — A named person, never the AI, is answerable for outcomes.

## 4. Rules

**What agents MAY read:** anonymised or aggregate marketing figures; a single guest's booking only when that guest is being served, and only the fields needed.

**What agents MAY write / change:** draft replies, draft reports and draft slides. Any change to a live booking, price, or guest record must be **approved by a human** first.

**What agents MAY generate:** summaries, drafts, slides and analysis — always marked as "AI draft — to be checked."

**Approvals for changes:** adding a new agent, turning on a new skill, or widening what data an agent can read requires **Approver** sign-off.

**Retention:** uploaded working files and agent chat logs are kept for 12 months, then deleted, unless needed for a specific record.

## 5. Audit & Logging

- Every agent keeps a log of what it was asked and what it did.
- Logs record the date, the staff member, the data used and any file produced.
- Logs are reviewed monthly by the Agent Owner and spot-checked by the Approver.

## 6. Accountability

- Accountability rests with the **named human owner** of each agent and each data asset — **never with the AI**.
- If an agent produces a wrong or harmful output, the Reviewer who released it and the Agent Owner are answerable, and the incident is recorded.

## 7. Review

- This policy is reviewed **every 12 months**, or sooner if a new agent, skill or data type is introduced, or after any incident.
- The General Manager owns the review and records the changes.

---

© 2026 Tertiary Infotech Pte Ltd · Training use only
