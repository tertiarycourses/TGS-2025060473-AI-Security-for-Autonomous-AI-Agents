# AI Security for Autonomous AI Agents - Project Context

## Scope

- WSQ course `TGS-2025060473 - AI Security for Autonomous AI Agents`, 1 day, 8 hours. Approved Course Proposal: `../course_application/CP_IT_AI Ethnics_INT.xlsx` (LU, LO, K, A wording and minutes are fixed: LU1 120, LU2 120, LU3 180, WA 30, Case Study 30).
- v5.0 (7 Nov 2026) is a full overhaul. Single source: `.claude/skills/courseware-build/build/` (`course_data.py`, `data_labs.py`, `mock_data.py`, `lab_scripts/`). Build everything with `bash .claude/skills/courseware-build/build/build_courseware.sh`. Earlier builders and the eight activities are in `courseware/archive/` (git-ignored) and must not feed a build.
- Topics: (1) Human-AI Collaboration and Always-On AI Agents; (2) AI Agent Vulnerabilities; (3) AI Governance and Security. Six labs on the fictional Kopi Kaki Co.
- Deck theme: the Claude Code course design (`ccdeck.py`). Slide notes are the Learner Guide narrative.
- Labs follow the `wsq-lab-author` skill: one folder per lab with `data/`, `scripts/` and a PDF, no .md files, plus `prompts/index.html`. Lab folders are named for the topic (owner's choice), so Labs 2 to 4 have learners copy data/ and scripts/ into a plain Desktop folder before attaching it, and scoring is a separate step: a tipped-off model behaves (1 of 4 vs 4 of 4). Topic 1 and Lab 1 slides are copied from the Human-AI Workforce deck by copy_slides.py. Re-run attacks before class; results are in `research/V50-LAB-TEST-RESULTS.md`.
- Assessment: Written Assessment (5 SAQ, K1 to K5, questions must not change) and a Case Study (Q1 to Q3, lab screenshots pasted as answers). The instrument is "Case Study", as the CP names it. Never "PP".
- Facts: the verified ledger is `research/SOURCE-REGISTER-v50.md`, checked 7 Nov 2026. Do not cite buldrr for product facts. Write "Gemini Spark (now Task)" and "Grok Bot, SpaceXSI (formerly xAI)".

## Security framework

- Organisational guidance should combine: IMDA's Model AI Governance Framework for Agentic AI; NIST AI RMF; OWASP Top 10 for LLM Applications and Agentic Applications; MITRE ATLAS; and the PDPA/PDPC guidance.
- Controls must be layered: use-case risk tiering, scoped identity and permissions, trusted skill/plugin allowlists, sandboxing, egress controls, guardrails, deterministic human approvals, audit logs, monitoring, incident response, and safe decommissioning.
- Treat prompts, retrieved files, email, web pages, tool output, memory, context files, skills, plugins, MCP servers, and dependencies as potentially untrusted inputs.

## Build and QA

- Bump the package version and change-control entries before rebuilding.
- Build the slide deck before the Lesson Plan because slide mappings feed the LP.
- Regenerate the Learner Guide Markdown, DOCX, and PDF together.
- Run `.claude/commands/courseware-qa.md` against the exact rebuilt artifacts. Render every changed PPT/PDF/DOCX page and inspect it visually.
- Assessments are confidential and must remain ignored by Git, as must `build_assessment_v50.py` and `fgap/`. Answer keys never reach learner-facing LMS fields.

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
