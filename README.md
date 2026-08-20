# AI Security for Autonomous AI Agents

**WSQ course code:** TGS-2025060473

**TSC:** Generative AI Principles and Applications (ICT-INT-0052-1.1)

**Duration:** 2 days · 16 hours

**Courseware version:** 3.0 · 20 August 2026

Evidence-grounded courseware for understanding and controlling the security risks of generative AI, agentic operating patterns and deployed AI agents.

![Version 3.0 trainer-deck cover](screenshot.png)

## Course progression

The 207-slide trainer deck follows a simple-to-complex sequence:

1. AI history and the transition from prediction to generation and action.
2. Generative AI, agentic behaviour and deployed AI agents as overlapping operating layers.
3. Product and harness boundaries across OpenClaw, Hermes, Prime Agent, QM, DeepSeek Harness, Claude Code, Codex and ChatGPT Chat/Work.
4. Threat modelling from untrusted content through identity, tools, runtime, memory, network and impact.
5. Prompt injection, jailbreaks, data leakage, PDPA, token exposure, malicious skills/plugins/MCP, code execution and persistent compromise.
6. Controls, governance, incident response, rollback and deployment assurance.

## Frameworks and evidence

| Framework | Course use |
|---|---|
| NIST AI RMF | Govern, map, measure and manage AI risk across the lifecycle |
| OWASP Top 10 for LLM Applications | Generative-AI application risk taxonomy |
| OWASP Top 10 for Agentic Applications | Agentic goals, tools, identity, memory and coordination risks |
| MITRE ATLAS | Adversary tactics and techniques involving AI-enabled systems |
| IMDA Model AI Governance Framework for Agentic AI v1.5 | Bounds, human accountability, technical controls and end-user responsibility |
| Singapore PDPA and PDPC publications | Purpose, protection, retention, transfers, accountability and breach notification |

PDPC's June 2026 generative-AI material is identified as proposed public-consultation guidance, not represented as final law or final guidance.

Documented cases retain evidence labels and limitations. They include EchoLeak as a verified vulnerability rather than a claimed breach; the Amazon Q extension supply-chain event where malicious code was distributed but did not execute because of a syntax error; Replit's first-party account that the affected application database was restored with no data lost; and the dated ClawHavoc security-research snapshot without generalising its reported figures to the current marketplace.

## Organisational control model

The implementation sequence is designed to leave observable evidence:

1. Inventory and risk-tier the use case.
2. Bound data, tools and autonomy.
3. Give each agent a scoped, short-lived identity.
4. Apply guardrails and deterministic schema/policy validation.
5. Sandbox code and files.
6. Deny network egress by default and allow named destinations.
7. Require meaningful human approval for consequential actions.
8. Log the decision, approval and resulting action.
9. Monitor sequences and boundary crossings, not only isolated events.
10. Red-team before go-live and retain rollback, incident and decommissioning evidence.

## Current learner-facing artifacts

| Artifact | Current file |
|---|---|
| Trainer deck | `courseweare/WSQ - Master Trainer Slides - TGS-2025060473 - AI Security for Autonomous AI Agents-v30.pptx` and matching PDF |
| Learner Guide | `courseweare/Learner Guide - TGS-2025060473 - AI Security for Autonomous AI Agents.docx` and PDF |
| Learner Guide Markdown | `courseweare/LEARNER-GUIDE.md` |
| Lesson Plan | `courseweare/Lesson Plan - TGS-2025060473 - AI Security for Autonomous AI Agents.docx` and PDF |
| Activities | Five self-contained folders under `activities/`, each with Markdown and printable PDFs |

The Learner Guide is 109 pages. The Lesson Plan is 9 pages. Detailed procedures are kept in the Learner Guide and activity packs; the trainer slides remain concept-led.

## Activities

| # | Activity | Day | Duration | Evidence |
|---|---|---:|---:|---|
| 1 | Threat Modelling a Generative AI Concierge | 1 | 45 min | K2, K3, A4 |
| 2 | Prompt Injection and the PDPA Breach Decision | 2 | 60 min | K4, K1 |
| 3 | Selecting a Security Framework for GenAI and Agents | 2 | 60 min | A3, A5 |
| 4 | Evidence-Based Rogue Agent Incident Review | 2 | 60 min | K5 |
| 5 | Agent Governance and the Deployment Gate | 2 | 25 min | A1, A2 |

Every activity includes a learner workflow, required evidence, acceptance criteria and an operational checklist. Prompt-injection practice uses synthetic, local and reversible table-top tests. Learners must not upload answer keys, real credentials, production secrets or personal data.

## Assessment boundary

The confidential `assessment/` folder is excluded from GitHub. Learner question papers are distributed through the approved Drive/LMS workflow; answer keys remain trainer-only and are never linked from LMS-TMS.

## Release safety

- `.env`, credentials and local source packs are excluded.
- Archived versions and temporary QA renders are excluded.
- Case statements distinguish verified vulnerabilities, first-party incidents, research reports and fictional simulations.
- The public release contains courseware artifacts only; assessments, answer keys and internal QA/build materials remain excluded.

---

This material belongs to Tertiary Infotech Pte Ltd (UEN 20120096W). All Rights Reserved.
