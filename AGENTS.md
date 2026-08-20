# AI Security for Autonomous AI Agents - Project Context

## Scope

- WSQ course: `TGS-2025060473 - AI Security for Autonomous AI Agents`.
- Treat `courseweare/course_data.py`, `courseweare/v30_content.py`, and `courseweare/v30_learner.py` as the active v3.0 instructional source of truth. `deck_content.py` and `lg_content.py` are legacy v2.x sources and must not feed a v3.x build.
- Preserve the existing `courseweare/` spelling. Do not rename it during a scoped release.
- This is a technical AI-security course, but the verified learner-facing hands-on directory is `activities/`. Preserve that public destination unless the project owner explicitly changes it.

## Content and design

- Keep the PowerPoint concept-led and highly visual. Put detailed procedures, evidence requirements, acceptance criteria, and checklists in the Learner Guide and activity packs.
- Cover prompt injection, indirect and cross-modal injection, personal-data exposure under Singapore's PDPA, excessive agency, tool misuse, memory poisoning, and malicious or untrusted agent skills/plugins.
- Use realistic, clearly fictional Singapore business scenarios. Distinguish verified incidents from reported or hypothetical cases.
- Every factual slide must carry an evidence label and one or more source IDs resolved in `research/CLAIM-LEDGER-v30.md`; every synthetic scenario must display `SIM` and state that its names, events and numbers are fictional.
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
