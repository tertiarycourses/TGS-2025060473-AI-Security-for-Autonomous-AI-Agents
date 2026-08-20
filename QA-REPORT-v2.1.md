# Courseware QA Report — Version 2.1

**Course:** AI Security for Autonomous AI Agents
**Course code:** TGS-2025060473
**TSC:** ICT-INT-0052-1.1
**QA date:** 20 August 2026
**Outcome:** PASS

## A. Artifact and version integrity

- Trainer deck: 75 slides; editable PPTX and matching 75-page PDF; Version 2.1.
- Learner Guide: DOCX, Markdown mirror and 30-page PDF; Version 2.1.
- Lesson Plan: DOCX and 10-page PDF; Version 2.1; Day 1 = 480 minutes and Day 2 = 480 minutes.
- Assessments: Written Assessment and Case Study question papers plus trainer-only answer keys; DOCX and PDF; Version 2.1.
- Activities: five self-contained learner folders, 22 Markdown sources, 22 matching per-source PDFs and five consolidated learner PDFs.
- The current non-certification course rule was applied: no practice exam was added. The stale project checklist item that calls for a practice exam was intentionally not followed.

## B. Coverage added in v2.1

| Requested coverage | PPT | Learner Guide | Activity evidence |
|---|---|---|---|
| Realistic direct/indirect/context-file prompt injection | Slides 26–29 | Detailed safe simulations and acceptance criteria | Activity 2 practice and checklist |
| Malicious downloaded skills, plugins and MCP servers | Slides 45–46 | Supply-chain risk table and approval checklist | Activity 4 review and containment checklist |
| Guardrails, least privilege, sandbox, egress and monitoring | Framework/control slides and production checklist | Four-layer stack and six-stage implementation framework | Activities 1, 3, 4 and 5 checklists |
| Meaningful human-in-the-loop | Slides 54–55 | Code-triggered, narrow, informed approval design | Activity 5 deployment gate |
| Responsible AI and shared responsibility | Slides 58–59 | Principles-to-controls table and lifecycle roles | Activity 5 Responsible AI assurance section |
| PDPA for GenAI and agents | Slides 60–63 | Data-surface inventory, obligations and step-by-step checklist | Activities 2 and 5 checklists |

## C. WSQ and cross-artifact alignment

- Accredited learning outcomes and K1–K5/A1–A5 statements remain unchanged.
- Written Assessment: exactly one question for each K statement.
- Case Study: three questions mapped to LO1–LO3 and A1–A5.
- Activity durations match the Lesson Plan: 45, 60, 60, 60 and 25 minutes.
- Procedures remain in the Learner Guide and activity packs; the deck remains concept-led.
- Slide map regenerated after the final 75-slide build.

## D. Visual and technical QA

- Full-deck contact-sheet review completed, followed by enlarged inspection of cover, prompt-injection, skills/plugins, human approval, implementation, Responsible AI, shared-responsibility, PDPA and readiness slides.
- One skills/plugins layout collision and several footer-adjacent captions were corrected and re-rendered.
- Learner Guide, Lesson Plan, all five consolidated activity PDFs and both learner assessment question papers were rendered and visually inspected.
- PPTX, Learner Guide DOCX, Lesson Plan DOCX and all four assessment DOCX files pass Office XML validation.
- All 32 current learner-facing PDFs open successfully with valid page geometry.

## E. Publication safety

- `.env`, `assessment/`, `reference/`, `trainer-resources/` and all archive folders are excluded from the public GitHub release.
- Trainer activity debriefs were removed from `activities/` and retained only in ignored local trainer resources.
- The Drive/TMS learner assessment set is exactly the Written Assessment question paper and Case Study question paper. Answer keys remain trainer-only.
- Root `.env` contains the explicitly supplied Drive and GitHub destinations; values were checked without printing secrets in QA output.

## F. Exact primary artifact hashes (SHA-256)

| Artifact | SHA-256 |
|---|---|
| Trainer deck PPTX | `27d8954c6d506412abb180c01ffc35f959831ff208b172f42081620ed125008f` |
| Trainer deck PDF | `09ec5ed76bce1cf7c4744e00a30df3cefd0e198191d072672ec992f2923bd1e3` |
| Learner Guide DOCX | `b7e76df6d9bd5ef055e47a6452282356f1166738b01d35366345acfbdfd9a310` |
| Learner Guide PDF | `2d615a08d9e6c1479f995a51836bca823d2257933b637b5ad86eeb5de084cef1` |
| Lesson Plan DOCX | `62ae37ba71da8bdacffe098d674efa670bbfc860b7203cc73ceee02d5f6be10e` |
| Lesson Plan PDF | `a6a5d12fd125060deb6eef2f23493e16526fd07624e4f36b5b62e5ed6b990b29` |
| Activity 1 consolidated PDF | `0a2e1821ea53eb4a30f81df5d5c3532ef38ca5b4302b942e9cdf82ebca3759aa` |
| Activity 2 consolidated PDF | `bed7446c73f31347c3a894dfcd8ab66ea78e8eccca706ec150efc0e11d854ddd` |
| Activity 3 consolidated PDF | `712d9833fb8c0e020154dd1bdaf5dc5acfe53c37a3f9b2ac4aa03d4bbc1e1ab7` |
| Activity 4 consolidated PDF | `975b100f590bb07855907918432feb76dd5d1252b50a72ac46f486099501c4cb` |
| Activity 5 consolidated PDF | `104ce23e7f801096bb593bb00a996b01175619e9d0aceb6746a98a60c6da9aba` |

The hashes bind this PASS result to the exact primary files inspected before publication.
