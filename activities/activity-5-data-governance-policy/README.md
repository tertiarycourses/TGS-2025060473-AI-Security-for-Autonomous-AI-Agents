# Activity 5 — Draft Your AI Data Governance Policy

**Purpose:** Use the **AI Data Policy Generator website** to draft an AI data governance policy for your own (fictional) company, then check and refine it against the 7-part framework taught in class.

## What you need

- The generator website in this folder: `ai-data-policy-generator.html` (open it in any browser)
- A **training OpenAI API key** from your trainer (low limit; revoked after class)
- The reference sample in this folder: `SAMPLE-AI-DATA-GOVERNANCE-POLICY.md`
- The refinement prompt sheet: `PROMPTS.md` (for polishing sections with the Hermes agent)

**Evidence status: SIM — all data is fictional.** The sample policy is written for the fictional **Sunset Bay Resort Singapore**. Invent your own fictional company — never enter a real company's confidential details.

## The 7-part framework (taught in class)

Every policy the generator drafts follows the framework from the slides, aligned in spirit with the **IMDA Model AI Governance Framework** and the **PDPA**:

1. **Scope** · 2. **Roles** · 3. **Principles** · 4. **Rules** · 5. **Audit & Logging** · 6. **Accountability** · 7. **Review**

## Steps

1. Skim `SAMPLE-AI-DATA-GOVERNANCE-POLICY.md` once so you know what a finished policy looks like.
2. Open `ai-data-policy-generator.html` in your browser (double-click the file).
3. Enter the **training API key** your trainer gives you. Never paste a production key.
4. Fill in your **fictional** company: name, what the business does, the AI agents it uses (for example, a WhatsApp guest-support agent and a marketing spreadsheet agent) and the data those agents touch.
5. Click **Generate** and read the drafted policy section by section against the sample.
6. Check the two golden rules: every role is held by a **named human job title** (never the AI), and any change to live data needs **human approval first**.
7. Refine: regenerate with better inputs, or paste a weak section into the Hermes agent with the matching prompt from `PROMPTS.md`.
8. Click **Download .md** (or Print / Save as PDF) and keep the policy as your activity output.

## What you produce

- A one-to-two page AI data governance policy for your fictional company, covering all 7 parts
- At least one **named human owner** (job title) for each key responsibility
- One clear rule stating what the agent may **read**, **write** and **generate**

## Reflect (Data Privacy / Job Impact / Ethical Concerns / Cyber Security)

- **Data Privacy:** Which customer data should an agent never be allowed to read? (PDPA in spirit: collect and use only what is needed.) And what about the API key you just typed into a website — where did it go, and who could see it?
- **Job Impact:** Who now owns "checking the agent's output" as part of their role?
- **Ethical Concerns:** Your policy says the human is accountable, never the AI. Why does that matter?
- **Cyber Security:** How would you know, weeks later, what the agent read or changed? (Audit & logging.)

---

© 2026 Tertiary Infotech Pte Ltd · Training use only
