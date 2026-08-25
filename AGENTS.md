# AI Security for Autonomous AI Agents - Project Context

## Scope

- WSQ course: `TGS-2025060473 - AI Security for Autonomous AI Agents`. As of v4.0 (25 Aug 2026) this is a **1-day (8-hour) course** — see the official page https://www.tertiarycourses.com.sg/wsq-ai-security-for-autonomous-ai-agents.html. It was previously a 2-day security course; do not reintroduce the 2-day structure.
- Treat `courseware/course_data.py`, `courseware/v40_content.py`, and `courseware/v40_learner.py` as the active v4.0 instructional source of truth. The v3.0 modules (`v30_content.py`, `v30_learner.py`) and v2.x modules (`deck_content.py`, `lg_content.py`) are legacy and must not feed a v4.x build. `build_slides.py` selects the content module by `C.VERSION`.
- The course now has three topics mapped to LO1/LO2/LO3: (1) Generative AI, Agentic AI and AI Agents; (2) Prompt Engineering and Post-Training (Hermes agent on MiniMax); (3) Security Risk of Autonomous AI Agents.
- Learners do NOT code. Every activity uses a ready-made website, chatbot or AI agent under `activities/` (activity-1..8). Activities 6 and 7 are self-contained `index.html` websites powered by a learner-supplied OpenAI or MiniMax key.
- The build output folder is `courseware/` (the old `courseweare/` typo was renamed in Aug 2026; do not reintroduce it).

## Content and design

- Keep the PowerPoint concept-led and highly visual. Put detailed procedures and checklists in the Learner Guide and activity packs. The Learner Guide targets ~120-150 pages (one slide-note block per page).
- Topic 1 covers GenAI mechanics (autoregressive LLM, training/inference), real use cases, context engineering, the agentic loop/harness engineering, OpenClaw/Hermes/Peter Steinberger, skills/tools and multi-agent systems. Topic 3 covers AI data governance, job impact/redesign and AI-agent cybersecurity risks (adversarial AI, algorithmic bias, over-reliance, data privacy, model drift, malicious use) plus safe rollout.
- Evidence policy is "lighter touch": real dated facts and named cases carry an evidence label + source ID (resolved in `v40_content.SOURCES`); concept/definition slides may stand alone. Every synthetic scenario is labelled `SIM` with fictional names and numbers.
- OpenAI product claims may use only current official pages under `learn.chatgpt.com`, `developers.openai.com`, or `platform.openai.com` for this package.
- Generated images must contain no embedded text, logos, trademarks, or watermarks. Keep titles and labels editable in PowerPoint.
- Do not add a practice-exam slide unless this course is explicitly mapped to an external certification exam and a matching exam exists.

## Security framework

- Organisational guidance should combine: IMDA's Model AI Governance Framework for Agentic AI; NIST AI RMF; OWASP Top 10 for LLM Applications and Agentic Applications; MITRE ATLAS; and the PDPA/PDPC guidance.
- Controls must be layered: use-case risk tiering, scoped identity and permissions, trusted skill/plugin allowlists, sandboxing, egress controls, guardrails, deterministic human approvals, audit logs, monitoring, incident response, and safe decommissioning.
- Treat prompts, retrieved files, email, web pages, tool output, memory, context files, skills, plugins, MCP servers, and dependencies as potentially untrusted inputs.

## Build and QA

- Bump the package version and change-control entries before rebuilding.
- Build the slide deck before the Lesson Plan because slide mappings feed the LP.
- Regenerate the Learner Guide Markdown, DOCX, and PDF together.
- Every learner-facing Markdown file under `activities/` must have an aligned current PDF counterpart within the same activity folder.
- Run `.claude/commands/courseware-qa.md` against the exact rebuilt artifacts. Render every changed PPT/PDF/DOCX page and inspect it visually.
- Assessments are confidential and must remain ignored by Git. Answer keys are trainer-only and never attached to learner-facing LMS fields.
- The assessment (v4.4) is a Written Assessment (5 SAQ, one per K1–K5) plus a **reflection-based Case Study** (3 tasks, one per LO1–LO3, two questions each) in which learners document their own observations from the day's activities. The instrument is titled "Case Study" both in the DOCX filenames and inside the papers. Built by `build_assessment_set.py`.

## Environment and publication

- `.env` is gitignored and contains `COURSEWARE_LINK`, `GDRIVE_FOLDER_ID`, and `GITHUB_REPO_URL`. Never stage or print credential values.
- Release order: courseware QA, secure GitHub push, Google Drive dry-run, Google Drive upload/readback, LMS-TMS no-write preview, secure before snapshot, production update, complete readback verification.
- The Google Drive folder ID must match the LMS Courseware Link. Abort on mismatch unless the project owner explicitly confirms the override after seeing both IDs.
- Google Drive publication is upload-only: superseded files move to `archive/`; nothing is deleted.
- LMS-TMS receives current PPT/PDF/LG/LP/activity links plus learner-facing question papers only. Preserve unrelated LMS fields.

## Change safety

- Inspect `git status` and target diffs before editing or publishing.
- Stage specific public files only. Do not use `git add .` or `git add -A`.
- Stop rather than overwrite overlapping user changes.
