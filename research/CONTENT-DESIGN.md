# Content Design — AI Security for Autonomous AI Agents

Course code: **TGS-2025060473** | TSC: **ICT-INT-0052-1.1** | Version 2.1
Design decision: **Option A** — accredited K/A taught VERBATIM, AI security is the delivery lens.

---

## 1. The alignment rule

Every K and A statement below is reproduced **exactly** as accredited. The *security lens* column is
how it is taught and contextualised — it never replaces the statement.

Assessment rule (per client instruction 2026-08-17):
- **Written Assessment (WA/SAQ)** — exactly **one question per K statement** → 5 questions (Q1–Q5)
- **Case Study** — **one question per LO**, each mapping to that LO's A statements → 3 questions (Q1–Q3)
- Zero multiple choice. Every question prints its K/A code.

## 2. LU / LO / K / A master map

### LU1 — Generative AI Fundamentals → **Foundations of AI Security**
**LO1 (corrected per client):** Demonstrate generative AI concepts and applications relevant to
customer service and hospitality management.

> Note: the CP repeats a PDPA-consent LO on two LU1 rows. Confirmed as a CP copy-paste defect;
> the correct LO1 above is used everywhere. PDPA is still taught (under LU3/A2) — it is not lost.

| Code | Accredited statement (verbatim) | Security lens | Assessed |
|---|---|---|---|
| K2 | Underlying principles, core concepts and theories governing generative AI | How transformer/attention mechanics create the **instruction-data confusion** that makes prompt injection unfixable at the model layer | WA Q1 |
| K3 | Difference between generative and discriminative models | Why **discriminative guardrail classifiers** are used to police generative models; why filters fail on cross-modal payloads | WA Q2 |
| A4 | Demonstrate the use of generation AI in diverse applications (e.g., summarisation, inference, reasoning, transformation of content, augmentation of content) | Each application mode as an **attack surface**: summarisation→indirect injection; transformation→improper output handling (LLM10); augmentation→RAG poisoning (LLM09) | CS Q1 |

### LU2 — Prompt Engineering → **Attacking and Defending the Prompt Layer**
**LO2:** Apply prompt engineering techniques and analyse output variations to improve generative AI
performance in service settings.

| Code | Accredited statement (verbatim) | Security lens | Assessed |
|---|---|---|---|
| K1 | Importance of data quality, preprocessing, model pipeline and model training (e.g., impact of data bias from training data) | **Data and model poisoning (LLM05)** — production poisoning of RAG bases and agent memory (ASI06); supply chain artifact integrity (LLM04) | WA Q3 |
| K4 | Impact of prompt engineering on the model outputs of generative AI | **Prompt injection (LLM01)** direct/indirect/cross-modal; system prompt and **hidden context exposure (LLM08)**; defensive prompt patterns and why they are insufficient alone | WA Q4 |
| A3 | Apply understanding of generative AI principles to use cases | **Selecting and justifying a security framework** (OWASP LLM/ASI, NIST AI RMF, MITRE ATLAS, IMDA agentic framework, PDPA) for a real deployment | CS Q2 |
| A5 | Analyse generative AI models' performance metrics and evaluate the influence of prompt variations | **Adversarial/red-team testing**: attack success rate, refusal rate, false-positive cost; measuring guardrail effectiveness across prompt variants | CS Q2 |

### LU3 — Ethical Considerations → **Agent Autonomy, Governance and Singapore Compliance**
**LO3:** Identify ethical risks and analyse bias in AI-generated content used in customer engagement.

| Code | Accredited statement (verbatim) | Security lens | Assessed |
|---|---|---|---|
| K5 | Generative AI model workings, including training data, algorithms, and outputs | From model to **agent**: planning loops, tool calling, memory. **Excessive agency (LLM03)**, uncontrolled execution (ASI05), rogue agents (ASI10) | WA Q5 |
| A2 | Identify the ethical implications and societal impact of AI-generated content | **Responsible AI controls and shared responsibility**, **PDPA obligations**, PDPC GenAI guidelines (deployer accountability), IMDA agentic framework, societal harm from autonomous action | CS Q3 |
| A1 | Analyse limitations and potential biases in AI-generated content | **Misinformation as a security risk (LLM07)** — hallucination driving wrong tool calls; slopsquatting (ASI04); bias in security decisioning | CS Q3 |

**Coverage check:** K1,K2,K3,K4,K5 all in WA (5 Qs). A1,A2,A3,A4,A5 all in CS (3 Qs across LO1/LO2/LO3). No gaps.

## 3. Course structure — 2 days × 8h

### Day 1 — Generative AI Security
| Block | Topic | K/A |
|---|---|---|
| LU1 T1 | Threat landscape; why GenAI breaks classical security assumptions | K2 |
| LU1 T2 | Generative vs discriminative; the guardrail classifier pattern | K3 |
| LU1 T3 | Application modes as attack surfaces | A4 |
| **Activity 1** | **Threat Modelling a GenAI Concierge** (hospitality) | K2,K3,A4 |
| LU2 T1 | Data quality, poisoning, supply chain integrity | K1 |
| LU2 T2 | Prompt injection deep dive — direct, indirect, cross-modal | K4 |
| **Activity 2** | **Prompt Injection & Data Leakage Clinic** (PDPA breach) | K4,K1 |

### Day 2 — Autonomous Agent Security
| Block | Topic | K/A |
|---|---|---|
| LU2 T3 | Security frameworks: OWASP LLM/ASI, NIST AI RMF, MITRE ATLAS, IMDA, PDPA | A3 |
| LU2 T4 | Measuring guardrails — adversarial testing and metrics | A5 |
| **Activity 3** | **Framework Selection Workshop** | A3,A5 |
| LU3 T1 | Agent anatomy; excessive agency; uncontrolled/destructive execution | K5 |
| **Activity 4** | **Rogue Agent Post-Incident Review** (OpenAI→HF / Replit) | K5 |
| LU3 T2 | Responsible AI assurance, shared responsibility, PDPA, PDPC GenAI guidelines, IMDA agentic governance | A2 |
| LU3 T3 | Misinformation, bias and limitations as security risks | A1 |
| **Activity 5** | **Agent Governance & Deployment Gate** (capstone) | A1,A2 |
| | Assessment: WA + Case Study | all |

## 4. Activities (each in its own folder under `activities/`)

Every activity ships: `README.md` (scenario + LO/K/A + facilitation), `SCENARIO.md`,
`DISCUSSION-QUESTIONS.md`, `DEBRIEF.md`, and a PDF of the scenario+questions+debrief.
All are **real-world case studies**. Step-by-step detail lives in the **LG**, not the PPT.

| # | Folder | Case study | K/A |
|---|---|---|---|
| 1 | `activity-1-threat-modelling-genai-concierge` | Hospitality GenAI concierge (Singapore hotel) | K2,K3,A4 |
| 2 | `activity-2-prompt-injection-data-leakage` | Indirect injection → PDPA-reportable leak | K4,K1 |
| 3 | `activity-3-security-framework-selection` | Choosing OWASP/NIST/IMDA/PDPA for a deployment | A3,A5 |
| 4 | `activity-4-rogue-agent-incident-review` | OpenAI→Hugging Face agent escape; Replit DB deletion | K5 |
| 5 | `activity-5-agent-governance-deployment-gate` | Capstone: go/no-go gate for an autonomous agent | A1,A2 |

## 5. Deck rules

- Pitch level: **AI security guru** — authoritative, incident-led, framework-fluent.
- **Highly visual**: tile grids, flow diagrams, threat-chain diagrams, cards. No bullet walls.
- **No step-by-step in the PPT** (client instruction) — steps live in the LG.
- **No practice exam** (client instruction; also correct — non-certification course).
- Case studies appear in the deck as scenario + discussion prompts.
- Two trainer profile cards; Download Course Material visual; Assessment Flow diagram;
  TRAQOM front and end; Briefing before Assessment; one version label on cover.
