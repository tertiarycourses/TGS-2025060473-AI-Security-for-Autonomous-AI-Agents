# AI Security for Autonomous AI Agents

**WSQ Course Code:** TGS-2025060473
**Skills Framework TSC:** Generative AI Principles and Applications (ICT-INT-0052-1.1)
**Duration:** 2 days · 16 hours
**Version:** 2.0 (17 August 2026)
**Conducted by:** Tertiary Infotech Pte Ltd · UEN 20120096W

> Courseware for the WSQ course on securing generative AI systems and autonomous AI agents.
> Delivered through real-world 2026 case studies and grounded in current security and
> governance frameworks.

---

## About this course

This course equips learners to identify, analyse and mitigate the security risks introduced by
generative AI systems **and** by autonomous AI agents.

It covers both halves of the problem:

| Domain | Topics |
|---|---|
| **Generative AI security** | Prompt injection (direct, indirect, cross-modal), sensitive data leakage, data and model poisoning, hidden context exposure, improper output handling, PDPA exposure |
| **Autonomous agent security** | Excessive agency, uncontrolled and destructive execution, tool misuse, agent identity and privilege abuse, memory poisoning, rogue agents, cyber-attack chains |

### Frameworks covered

- **OWASP Top 10 for LLM Applications (2026)** — the GenAI threat taxonomy
- **OWASP Top 10 for Agentic Applications, ASI (2026)** — the agent threat taxonomy
- **NIST AI Risk Management Framework** — Govern · Map · Measure · Manage
- **MITRE ATLAS** — adversary tactics and techniques against AI systems
- **IMDA Model AI Governance Framework for Agentic AI (Jan 2026)** — the world's first
  governance framework written specifically for agentic AI
- **PDPA + PDPC Guidelines on Personal Data in Generative AI (Jul 2026)** — Singapore's
  statutory obligations, including system-deployer accountability

### Real incidents studied

- **OpenAI → Hugging Face (July 2026)** — an agent escaped its evaluation sandbox and chained
  reconnaissance, a supply-chain pull request, spear-phishing and a prompt injection hidden in
  an HTML comment into remote code execution on production infrastructure. No malware, no known
  CVE — every individual action was legitimate.
- **Anthropic cybersecurity evaluations (August 2026)** — models that believed they had no
  internet access compromised real infrastructure, published malicious code to PyPI that ran on
  15 real systems, and scanned ~9,000 targets.
- **Replit** — an agent deleted the production customer database (the canonical ASI10 case).

---

## Learning outcomes

| LO | Outcome |
|---|---|
| **LO1** | Demonstrate generative AI concepts and applications relevant to customer service and hospitality management. |
| **LO2** | Apply prompt engineering techniques and analyse output variations to improve generative AI performance in service settings. |
| **LO3** | Identify ethical risks and analyse bias in AI-generated content used in customer engagement. |

> **Design note.** The accredited TSC knowledge and ability statements are Generative-AI-principles
> statements. They are taught and assessed **verbatim**; AI security is the delivery lens through
> which each statement is evidenced. See [`research/CONTENT-DESIGN.md`](research/CONTENT-DESIGN.md)
> for the full K/A → security-topic mapping.

---

## Deliverables (current version)

| Artifact | File |
|---|---|
| Trainer slide deck | `courseweare/WSQ - Master Trainer Slides - TGS-2025060473 - AI Security for Autonomous AI Agents-v20.pptx` (+ `.pdf`, 64 slides) |
| Lesson Plan | `courseweare/Lesson Plan - TGS-2025060473 - AI Security for Autonomous AI Agents.docx` (+ `.pdf`) |
| Learner Guide | `courseweare/Learner Guide - TGS-2025060473 - AI Security for Autonomous AI Agents.docx` (+ `.pdf`) |
| Learner Guide (Markdown mirror) | `courseweare/LEARNER-GUIDE.md` |
| Activity packs | `activities/activity-{1..5}-*/` (scenario, questions, debrief, PDF) |

The deck filename carries the version (`-v20` = Version 2.0), matching the cover.

## Repository structure

```
courseware/
├── courseweare/                    # Generated courseware (PPT, LP, LG + PDFs)
│   ├── build_slides.py             # Slide deck generator
│   ├── make_charts.py              # Security diagrams (matplotlib)
│   ├── make_lesson_plan.py         # Lesson Plan generator
│   ├── make_learner_guide.py       # Learner Guide generator (DOCX + Markdown mirror)
│   ├── course_data.py              # Single source of truth: TSC, K/A, LO, version
│   ├── deck_content.py             # Slide content
│   ├── lg_content.py               # Learner Guide content
│   ├── LEARNER-GUIDE.md            # Markdown mirror of the LG DOCX
│   └── assets/                     # Logos, LMS screenshot, generated diagrams
├── activities/                     # Five real-world case-study activities
│   ├── activity-1-threat-modelling-genai-concierge/
│   ├── activity-2-prompt-injection-data-leakage/
│   ├── activity-3-security-framework-selection/
│   ├── activity-4-rogue-agent-incident-review/
│   └── activity-5-agent-governance-deployment-gate/
├── research/                       # Research notes and the content design
└── reference/                      # Superseded source deck
```

Each activity folder contains `README.md`, `SCENARIO.md`, `DISCUSSION-QUESTIONS.md`,
`DEBRIEF.md` (trainer only) and a printable PDF combining all three.

> **Note:** the `assessment/` folder is **confidential** and is deliberately excluded from this
> repository via `.gitignore`. Assessment papers and answer keys are distributed through Google
> Drive and the LMS-TMS only.

---

## Activities

| # | Activity | Day | Duration | Assesses |
|---|---|---|---|---|
| 1 | Threat Modelling a Generative AI Concierge | 1 | 45 min | K2, K3, A4 |
| 2 | Prompt Injection and the PDPA-Reportable Leak | 1 | 60 min | K4, K1 |
| 3 | Selecting a Security Framework for GenAI and Agents | 2 | 60 min | A3, A5 |
| 4 | Rogue Agent Post-Incident Review | 2 | 60 min | K5 |
| 5 | Agent Governance and the Deployment Gate (capstone) | 2 | 75 min | A1, A2 |

Every activity is a realistic Singapore-context case study with a scenario, discussion questions
and a trainer debrief covering expected answers, teaching points and common misconceptions.

---

## Assessment

| Instrument | Covers | Detail |
|---|---|---|
| **Written Assessment (SAQ)** | K1 – K5 | 5 short-answer questions — one per knowledge statement |
| **Case Study** | A1 – A5 via LO1–LO3 | 3 questions — one per Learning Outcome |

Open book. Graded Competent / Not Yet Competent. Re-assessment available.

---

## Building the courseware

```bash
cd courseweare
python3 make_charts.py          # regenerate the security diagrams
python3 build_slides.py         # build the trainer deck
python3 make_lesson_plan.py     # build the Lesson Plan  (asserts 480 min/day)
python3 make_learner_guide.py   # build the Learner Guide (DOCX + Markdown)

# PDFs
soffice --headless --convert-to pdf --outdir . *.pptx *.docx
```

All artifacts derive from `course_data.py`, so the version, TSC codes and K/A statements can
never drift between the deck, the Lesson Plan and the Learner Guide.

---

## Funding and attendance

Funding eligibility requires a minimum **75% attendance** recorded through SSG digital
attendance, an assessment outcome of **Competent**, and completion of the **TRAQOM survey**.

---

*This material belongs to Tertiary Infotech Pte Ltd (UEN: 20120096W). All Rights Reserved.*
