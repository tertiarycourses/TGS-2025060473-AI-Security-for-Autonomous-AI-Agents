# Activity 3 — Selecting a Security Framework for GenAI and Agents

**Course:** AI Security for Autonomous AI Agents
**Course Code:** TGS-2025060473 | **TSC:** ICT-INT-0052-1.1
**Block:** Day 2 — Autonomous Agent Security

---

## At a glance

| | |
|---|---|
| **Duration** | 60 minutes |
| **Format** | Small groups of 3–4, plenary debrief |
| **Type** | Realistic synthetic simulation (SIM) |
| **Learning Outcome** | LO2 |
| **K/A statements assessed** | A3, A5 |

## Purpose

Learners select and combine security frameworks (OWASP LLM & ASI Top 10, NIST AI RMF, MITRE ATLAS, IMDA Agentic Framework, PDPA) for a deployment with both a GenAI and an autonomous agent component, then interpret red-team metrics across prompt variants.

## Files in this folder

| File | Audience | Use |
|---|---|---|
| `SCENARIO.md` | Learner | The case study narrative, artefacts and data |
| `DISCUSSION-QUESTIONS.md` | Learner | The five questions to work through in groups |
| `SECURITY-CHECKLIST.md` | Learner | Framework coverage and go-live evidence checklist |
| `Activity-3-*.pdf` | Learner | Printable full learner pack including the checklist |

## How to run it

1. **Set up (5 min).** Form groups of 3–4. Issue `SCENARIO.md` and `DISCUSSION-QUESTIONS.md`.
   Trainer debrief notes are supplied separately and are not stored in the learner-facing Activities folder.
2. **Group work (45 minutes).** Groups work the five questions in order. Circulate; the questions are
   designed to be argued, not looked up.
3. **Presentation (5 minutes).** Each group presents its answer to one nominated question.
4. **Debrief (5 minutes).** Use the separate trainer notes to draw out the teaching points and correct recurring misconceptions.

## Learner workflow

1. Classify NIST AI RMF, OWASP LLM Top 10, OWASP Agentic Top 10, MITRE ATLAS, IMDA and PDPA by the question each answers.
2. Separate the generative and acting operating layers; record their data, tools, identities, state and delegated authority.
3. Map threats to OWASP categories and ATLAS techniques without treating either taxonomy as a control set.
4. Map lifecycle actions to Govern, Map, Measure and Manage, naming an owner and evidence artifact for each.
5. Map higher-impact and irreversible actions to autonomy limits and meaningful human approval.
6. Apply current PDPA obligations wherever personal data is collected, used, disclosed, retained, transferred or breached.
7. Reproduce the supplied metric calculations and interpret attack success, false positives, clean-task success and segment results together.
8. Define organisation-specific go-live thresholds, re-test triggers and a conditional go/no-go decision.

## Required evidence

- One framework-purpose matrix that answers all six framework questions correctly.
- One component-threat-control map covering both operating layers.
- Reproducible metric calculations with assumptions shown.
- One go-live gate in which each condition has a metric, threshold, owner, test method and re-test trigger.

## Acceptance criteria

The submission passes when each framework is used for its designed purpose, both operating layers are
covered, and thresholds are explicitly organisation-defined instead of being presented as universal
facts.

> The slide deck remains concept-led. These learner procedures are also reproduced in the Learner Guide.

## Alignment

Every question in `DISCUSSION-QUESTIONS.md` is tagged with the K or A statement it evidences.
This activity contributes to **LO2** and is assessed through the Case Study.

---

*This material belongs to Tertiary Infotech Pte Ltd (UEN: 20120096W). All Rights Reserved.*
