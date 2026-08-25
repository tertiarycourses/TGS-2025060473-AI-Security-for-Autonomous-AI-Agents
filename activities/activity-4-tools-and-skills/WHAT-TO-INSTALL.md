# What to Install — Two Real Skills

**Evidence status: SIM — the data stays fictional.** The two skills below are **real, publicly available skills**; you only use them on the fictional Sunset Bay Resort data. No coding required.

## Where do skills come from?

Hermes follows the open **Agent Skills** standard, so it can install skills from public skill libraries:

- **Skills Hub:** agentskills.io — browse community-contributed skills
- **Anthropic's public skills repo:** github.com/anthropics/skills — includes the two document skills used in this activity (`xlsx` and `pptx`)
- **Hermes docs:** hermes-agent.nousresearch.com/docs — see the *Skills* section

## How to install (no coding needed)

Pick whichever route your trainer has set up:

1. **Ask the agent in chat (easiest).** Type:
   > "Install the **xlsx** and **pptx** skills from the **anthropics/skills** GitHub repo, then list your active skills so I can confirm."
2. **Dashboard.** Open the Hermes dashboard → **Skills** page → **Learn a skill** → paste the skill's folder URL from github.com/anthropics/skills (search the repo for `xlsx` or `pptx` if the folders have moved).
3. **Trainer pre-install (command line).** The trainer can run `hermes skills search xlsx` / `hermes skills install …` before class so the skills are already active.

## Skill 1 — `xlsx` (spreadsheet skill)

**What it is:** Anthropic's spreadsheet skill — teaches the agent to read and build Excel files properly instead of guessing from pasted text.

**What it improves:**
- Reads columns by name (Spend, Revenue, Conversions) instead of guessing.
- Does the maths step by step (totals, ROI, month-on-month change) and shows its working.
- Returns clean tables you can copy into a report.
- Flags when a number looks odd (for example, revenue that fell while spend rose).

**Good test after installing:** Re-run the **"top channels by ROI"** or **"executive summary"** prompt from Activity 2 and check whether the numbers are clearer and the working is shown.

**What to still check yourself:** The skill can calculate quickly but cannot know if the underlying data is correct. You confirm the figures make sense.

## Skill 2 — `pptx` (slides skill)

**What it is:** Anthropic's PowerPoint skill — teaches the agent to build a real, downloadable `.pptx` file with clean, consistent layout.

**What it improves:**
- Produces an actual PowerPoint file, not just an outline in chat.
- Keeps bullets short and evenly spaced across slides.
- Applies fonts and colours consistently across the whole deck.
- Builds a proper summary slide from the key points.

**Good test after installing:** Re-run the **10-slide prompt** in `PROMPTS.md` (the same one you ran before installing) and compare the two decks side by side.

**What to still check yourself:** Nicer formatting does not make the content true. You confirm every point matches the script and nothing was invented.

## The one rule for any new skill

> Before switching on a skill, ask: **what can it read, what can it change, and who approved it?**

---

© 2026 Tertiary Infotech Pte Ltd · Training use only
