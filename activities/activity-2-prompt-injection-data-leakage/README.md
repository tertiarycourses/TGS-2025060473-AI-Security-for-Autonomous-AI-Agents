# Activity 2 — Prompt Injection and the PDPA Breach Decision

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
| **K/A statements assessed** | K4, K1 |

## Purpose

Learners dissect a realistic synthetic indirect prompt-injection scenario at a Singapore insurer in which personal data is disclosed, trace the payload through the pipeline, decide the PDPA notification question, and price the remediation.

## Files in this folder

| File | Audience | Use |
|---|---|---|
| `SCENARIO.md` | Learner | The case study narrative, artefacts and data |
| `DISCUSSION-QUESTIONS.md` | Learner | The five questions to work through in groups |
| `PROMPT-INJECTION-PRACTICE.md` | Learner | Safe, synthetic direct, indirect and context-file exercises |
| `SECURITY-CHECKLIST.md` | Learner | Prompt-injection controls, test evidence and PDPA response checks |
| `Activity-2-*.pdf` | Learner | Printable full learner pack including practice and checklist |

## How to run it

1. **Set up (5 min).** Form groups of 3–4. Issue `SCENARIO.md` and `DISCUSSION-QUESTIONS.md`.
   Trainer debrief notes are supplied separately and are not stored in the learner-facing Activities folder.
2. **Group work (45 minutes).** Groups work the five questions in order. Circulate; the questions are
   designed to be argued, not looked up.
3. **Presentation (5 minutes).** Each group presents its answer to one nominated question.
4. **Debrief (5 minutes).** Use the separate trainer notes to draw out the teaching points and correct recurring misconceptions.

## Learner workflow

1. Establish a clean baseline using the supplied fictional claim and record the expected output and permitted action.
2. Apply the direct-injection variant in `PROMPT-INJECTION-PRACTICE.md` to the table-top dummy policy; record the response and proposed tool arguments.
3. Repeat for the indirect document/email, context-file and cross-modal variants using synthetic files only.
4. For each variant, trace the carrier, trigger, interpreted instruction, proposed tool call and blocked or permitted effect.
5. Report attack success, refusal, false-positive and clean-task success separately.
6. Replace prompt-only protection with trusted recipient binding, record-scope binding, schema validation, retrieval isolation and deterministic approval.
7. Re-test the same baseline and variants; record both security improvement and useful-task degradation.
8. Apply the current PDPA significant-harm and significant-scale tests, recording facts still missing rather than assuming every disclosure is notifiable.
9. Recommend reduced mode, conditional release or halt, with the evidence required to restore capability.

## Required evidence

- One completed baseline and variant log using only synthetic data and non-routable destinations.
- One source-to-sink chain for each tested injection class.
- Separate attack-success, false-positive and clean-task-success results before and after controls.
- One PDPA decision record addressing significant harm, significant scale and information gaps.
- One prioritised remediation and release recommendation.

## Acceptance criteria

The submission passes when every supplied variant is tested against the same deterministic policy,
hostile content cannot change the record scope, recipient or action, the clean task still works, and
the PDPA conclusion is tied to documented facts and gaps rather than a blanket assumption.

> The slide deck remains concept-led. These learner procedures are also reproduced in the Learner Guide.

## Alignment

Every question in `DISCUSSION-QUESTIONS.md` is tagged with the K or A statement it evidences.
This activity contributes to **LO2** and is assessed through the Written Assessment (SAQ).

---

*This material belongs to Tertiary Infotech Pte Ltd (UEN: 20120096W). All Rights Reserved.*
