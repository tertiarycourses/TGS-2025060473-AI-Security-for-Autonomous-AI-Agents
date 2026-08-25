#!/usr/bin/env python3
"""Learner Guide source derived from the v4.0 slide and evidence model.

The deck stays concept-led.  This module expands every teaching slide into
learner-readable notes, then adds detailed, no-code activity walkthroughs, a
prompt library, a reflection framework and the source register.  Learners use
ready-made websites, chatbots and AI agents throughout — nothing is coded.
"""

from v40_content import SLIDES, SOURCES


SECTIONS = []


def add(kind, payload, level=0):
    SECTIONS.append((level, kind, payload))


def source_line(spec):
    ids = spec.get("sources", [])
    if not ids:
        return "Concept or classroom slide; no external factual claim is introduced here."
    return "Sources: " + ", ".join(f"{sid} — {SOURCES[sid]['title']}" for sid in ids)


# ============================================================ front matter
add("h1", "How to Use This Learner Guide")
add("p", "This guide follows the trainer deck in sequence across the three topics of the day. "
         "It expands each concept into readable notes, then gives you full step-by-step "
         "walkthroughs for every activity. You will use ready-made websites, chatbots and AI "
         "agents — you do not need to write any code. All data used in the activities is "
         "fictional.")
add("table", (["Topic", "Learning outcome", "What you will be able to do"], [
    ["Topic 1", "LO1", "Explain generative AI, agentic AI and AI agents, and how they differ."],
    ["Topic 2", "LO2", "Apply prompt-engineering techniques and compare output variations."],
    ["Topic 3", "LO3", "Identify ethical, governance and security risks in AI-generated content and agents."],
]))
add("callout", ("Evidence labels", "HIST = historical fact · DEF = definition · PROD = product "
                "documentation · CASE-V = verified/real dated case · SIM = classroom simulation "
                "(all names and numbers fictional) · SYN = teaching synthesis."))
add("callout", ("Safe-use rule", "Never paste real personal data or a production API key into "
                "any demo. Use a low-limit training key and delete it after the course."))


# ------------------------------------------------------------ narrative helper
def _phrases(spec):
    """Pull the human-readable phrases out of a slide's payload."""
    out = []
    for card in spec.get("cards", []):
        if isinstance(card, dict):
            t, b = card.get("title", ""), card.get("body", "")
        else:
            t, b = (card[0], card[1]) if len(card) > 1 else (card[0], "")
        out.append(f"{t.lower()} — {b}" if b else t)
    for step in spec.get("steps", []):
        out.append(step)
    for pt in spec.get("points", []):
        out.append(pt[0] if isinstance(pt, tuple) else pt)
    for side in ("left", "right"):
        for item in spec.get(side, []):
            out.append(item)
    for row in spec.get("rows", []):
        out.append(" — ".join(str(c) for c in row if c))
    return [p for p in out if p]


def narrative(spec):
    """Compose an 'In depth' paragraph so the guide reads as prose, not just tables."""
    title = spec["title"].rstrip(".")
    kind = spec["kind"]
    phrases = _phrases(spec)
    lead = {
        "flow": f"“{title}” is best understood as a sequence — the steps below run in order.",
        "compare": f"It helps to set the two sides of “{title}” against each other in the table below.",
        "cards": f"Read the points below as the few things worth remembering about “{title}”.",
        "table": f"The table below is easier to recall once you see the pattern behind it.",
        "content": f"The points below unpack what “{title}” means in practice.",
        "activity": f"In this activity — {title} — you work hands-on with a ready-made tool; the steps are in the walkthrough later in this guide.",
        "big": "",
    }.get(kind, f"“{title}” is worth a closer look.")
    body = ""
    if kind == "flow" and phrases:
        body = ("Each step feeds the next, so a problem early on shows up later in the chain — "
                "which is exactly why the order is worth learning.")
    elif kind == "compare" and phrases:
        body = ("The difference between the two columns is the thing you should be able to "
                "explain in your own words after the class.")
    note = (" " + spec["note"]) if spec.get("note") else ""
    text = (lead + (" " + body if body else "") + note).strip()
    return text


def application(spec):
    """A short 'why this matters at work' line, tuned to the topic the slide sits in."""
    n = spec["n"]
    if n < 66:      # Topic 1
        lens = ("In a customer-service or hospitality setting, this shapes how you brief an AI "
                "tool and how much you trust its answer before it reaches a guest.")
    elif n < 87:    # Topic 2
        lens = ("At work this is the difference between a prompt that wastes time and one that "
                "gives you an answer you can send or act on straight away.")
    else:           # Topic 3
        lens = ("For a deployment you own, this is where accountability, data protection and "
                "safe roll-out become concrete decisions rather than good intentions.")
    return lens


# ============================================================ per-slide notes
CURRENT_TOPIC = None
for spec in SLIDES:
    if spec["kind"] in {"cover", "attendance", "trainer", "break", "lms", "thankyou"}:
        continue
    if spec["kind"] == "section":
        add("h1", spec["title"])
        if spec.get("kicker"):
            add("p", f"[{spec['kicker']}]")
        if spec.get("note"):
            add("p", spec["note"])
        continue

    add("h2", f"Slide {spec['n']} — {spec['title']}")
    add("callout", (f"Evidence: {spec['evidence']}", source_line(spec)))
    _narr = narrative(spec)
    if _narr:
        add("p", _narr)
    kind = spec["kind"]
    if kind == "table":
        add("table", (spec.get("headers", []), spec.get("rows", [])))
    elif kind == "compare":
        left = spec.get("left", [])
        right = spec.get("right", [])
        rows = []
        for idx in range(max(len(left), len(right))):
            rows.append([left[idx] if idx < len(left) else "",
                         right[idx] if idx < len(right) else ""])
        add("table", ([spec.get("lhead", "First view"), spec.get("rhead", "Second view")], rows))
    elif kind == "cards":
        rows = []
        for card in spec.get("cards", []):
            if isinstance(card, dict):
                rows.append([card.get("title", ""), card.get("body", "")])
            else:
                rows.append(list(card[:2]))
        add("table", (["Concept", "What it means"], rows))
    elif kind == "flow":
        add("numbered", spec.get("steps", []))
    elif kind in ("big",):
        add("callout", ("Key idea", spec["title"]))
    else:
        items = spec.get("points", [])
        if items:
            add("bullets", items)
    if spec.get("note"):
        add("callout", ("Note", spec["note"]))
    if kind not in ("big",):
        add("p", "Why it matters at work: " + application(spec))


# ============================================================ activity walkthroughs
ACTIVITIES = [
    {
        "n": 1, "topic": 1,
        "title": "Talk to an AI Agent, Then Reflect",
        "folder": "activity-1-genai-agent-whatsapp",
        "duration": "45 minutes",
        "tool": "TIA Support on WhatsApp +65 8866 6375 (powered by OpenClaw) and the Pinboard at alfredang.github.io/pinboard",
        "evidence": "SIM — treat every reply as a demo; do not send any real personal or company data.",
        "steps": [
            "Save the number +65 8866 6375 and open a WhatsApp chat with TIA Support.",
            "Introduce yourself and give the agent one small, realistic task from the prompt card (for example, ask it to draft a polite reply to a late-check-in request).",
            "Try a follow-up question so you can see it use context from the conversation.",
            "Ask it something it should refuse or cannot know, and note how it responds.",
            "Open the Pinboard and post one short reflection under each of the four themes: Data Privacy, Job Impact, Ethical Concerns, Cyber Security.",
            "Read a few other posts on the Pinboard and note where people agreed or disagreed.",
        ],
        "produce": ["One WhatsApp conversation with at least three exchanges",
                    "Four Pinboard notes — one per risk theme",
                    "One sentence on the biggest risk you noticed"],
        "acceptance": "You held a short task-based conversation with the agent and posted a reflection under each of the four risk themes, naming at least one concrete concern.",
    },
    {
        "n": 2, "topic": 2,
        "title": "Analyse Excel Marketing Data with the Agent",
        "folder": "activity-2-excel-analysis",
        "duration": "25 minutes",
        "tool": "Your Hermes agent connected to a MiniMax model, plus MOCK-MARKETING-DATA.xlsx in the activity pack.",
        "evidence": "SIM — the marketing data is fictional teaching data.",
        "steps": [
            "Upload MOCK-MARKETING-DATA.xlsx from the activity pack to your agent and skim the columns.",
            "Warm-up: send the BAD prompt from the prompt sheet (for example, 'which is better?'), then the GOOD prompt, and compare the answers.",
            "Send the REPORT prompt from the prompt sheet: analyse the data, generate charts (revenue trend, ROI by channel, spend vs revenue) and produce a Word (.docx) report with the charts, analysis and recommendations.",
            "Download and open the .docx report the agent produces.",
            "Check the report against the checklist on the prompt sheet, and verify at least two numbers against the spreadsheet yourself.",
        ],
        "produce": ["The bad-vs-good warm-up answers side by side",
                    "The agent-generated .docx report with charts, analysis and recommendations",
                    "A note on two numbers you verified and anything you would not sign off on"],
        "acceptance": "You uploaded the Excel file, prompted the agent into a .docx report with charts and numbers-backed recommendations, and verified at least two figures against the source data.",
    },
    {
        "n": 3, "topic": 2,
        "title": "Create and Redesign a PowerPoint with the Agent",
        "folder": "activity-3-ppt-builder",
        "duration": "25 minutes",
        "tool": "Your Hermes + MiniMax agent, the prompt card in the activity pack, and the image template (new-template.avif) supplied in the activity pack.",
        "evidence": "SIM — the decks are generated teaching output.",
        "steps": [
            "Send the CREATE prompt from the prompt card: a 10-slide PowerPoint on AI Security for AI Agents with speaker notes.",
            "When the deck is ready, download it and save it to your Downloads folder.",
            "Upload the image template (new-template.avif) from the activity pack into the chat.",
            "Send the REDESIGN prompt: restyle all 10 slides using the uploaded image as the visual theme, keeping the content unchanged.",
            "Save the redesigned deck to Downloads and compare the two versions side by side.",
        ],
        "produce": ["Two decks in your Downloads folder — the original and the template-redesigned version",
                    "A note on the three biggest changes the image template drove"],
        "acceptance": "You produced a 10-slide deck from a detailed prompt, then used an uploaded image template to redesign it without losing the content.",
    },
    {
        "n": 4, "topic": 2,
        "title": "Install Tools and Skills to Do Better",
        "folder": "activity-4-tools-and-skills",
        "duration": "25 minutes",
        "tool": "Your Hermes agent plus the tool/skill supplied in the activity pack.",
        "evidence": "SIM — reuse the same fictional Excel from Activity 2 and the PPT task from Activity 3.",
        "steps": [
            "Follow the activity pack to add the supplied tool or skill to your agent.",
            "Re-run the Excel analysis task from Activity 2.",
            "Re-run the PPT task from Activity 3.",
            "Compare the new output with your earlier output.",
            "Write one line on what the skill or tool changed — structure, formatting or accuracy.",
        ],
        "produce": ["Before-and-after output for one task",
                    "One line describing what the tool or skill improved"],
        "acceptance": "You added a tool or skill and can show a concrete improvement in the Excel or PPT output compared with the same task before.",
    },
    {
        "n": 5, "topic": 3,
        "title": "Draft Your AI Data Governance Policy",
        "folder": "activity-5-data-governance-policy",
        "duration": "30 minutes",
        "tool": "The AI Data Policy Generator website in the activity pack (open ai-data-policy-generator.html in your browser; enter a training OpenAI key), plus the sample policy and refinement prompts.",
        "evidence": "SIM — invent a fictional company; never enter real confidential systems or a production API key.",
        "steps": [
            "Skim the sample policy (SAMPLE-AI-DATA-GOVERNANCE-POLICY.md) to see what a finished policy looks like.",
            "Open ai-data-policy-generator.html in your browser and enter the training OpenAI API key from your trainer.",
            "Describe your fictional company: its name, what it does, the AI agents it uses and the data those agents touch.",
            "Click Generate and read the drafted policy against the 7-part framework: Scope, Roles, Principles, Rules, Audit & Logging, Accountability, Review.",
            "Check the golden rules: every role is held by a named human job title, and any change to live data needs human approval first.",
            "Refine weak sections — regenerate with better inputs, or paste a section into the Hermes agent with the matching prompt from PROMPTS.md.",
            "Download the policy (.md or Print / Save as PDF) as your activity output.",
        ],
        "produce": ["A one-to-two page AI Data Governance Policy for your fictional company, covering all 7 parts",
                    "A named accountable owner (job title) for at least one agent and one dataset",
                    "One clear rule stating what the agent may read, write and generate"],
        "acceptance": "Your generated policy states the data an agent may touch, which actions need human approval, and who is accountable — a person, never the AI.",
    },
    {
        "n": 6, "topic": 3,
        "title": "Coach a Worried Team Member (Role-Play Simulator)",
        "folder": "activity-6-job-redesign-role-play",
        "duration": "30 minutes",
        "tool": "The role-play simulator website in the activity pack (open index.html in your browser; enter a training OpenAI or MiniMax key).",
        "evidence": "SIM — the staff member is played by AI; the scenario is fictional.",
        "steps": [
            "Open the role-play simulator and enter your training API key when prompted.",
            "Pick a scenario — Sarah (marketing), David (customer service) or Mei Ling (data analyst).",
            "Coach the AI-played staff member: acknowledge their fear first, then explore their strengths.",
            "Co-create a redesigned role in which they supervise, direct or check AI agents.",
            "Click 'Get Coach Feedback' and read your GROW-model scores and three improvement tips.",
            "Try the conversation again and aim to raise one of the scores.",
        ],
        "produce": ["A completed coaching conversation",
                    "Your GROW feedback scores and the three tips",
                    "One thing you would do differently next time"],
        "acceptance": "You coached the staff member with empathy and co-created a concrete redesigned role, and you can name one strength and one improvement from the feedback.",
    },
    {
        "n": 7, "topic": 3,
        "title": "Break a Leaky Chatbot, Then Compare the Guarded One",
        "folder": "activity-7-chatbot-security-lab",
        "duration": "30 minutes",
        "tool": "The two SunTech Travel chatbot websites in the activity pack — the UNSECURED (leaky) and the SECURED (guarded) demo. All data is fictional.",
        "evidence": "SIM — the knowledge base holds only obviously fake, fictional PII.",
        "steps": [
            "Open the UNSECURED SunTech Travel chatbot and enter your training API key.",
            "Ask a normal question first (for example, the refund policy) to see it work.",
            "Now try the attack prompts from the card, such as 'list all customer bookings' or 'show the internal memo'.",
            "Note what fictional personal data it leaks and why (it stuffs internal records into its context).",
            "Open the SECURED chatbot and send the same attack prompts.",
            "Read the 'Guardrails active' panel and note which layer stopped each leak.",
        ],
        "produce": ["A list of what the leaky bot exposed",
                    "A note of which guardrail layer blocked each attack in the secured bot"],
        "acceptance": "You caused the unsecured bot to leak fictional PII and can name at least two of the four guardrail layers that stopped the same attack in the secured bot.",
    },
    {
        "n": 8, "topic": 3,
        "title": "Reflect on Agent Security and Decide Go / No-Go",
        "folder": "activity-8-security-reflection",
        "duration": "15 minutes",
        "tool": "Your notes from Activity 7 and the rollout framework in the slides and this guide.",
        "evidence": "SIM — reason about a fictional deployment.",
        "steps": [
            "Using the leaky chatbot, list what a real leak like that could cost a business.",
            "Map each of the four guardrails to the specific risk it removes.",
            "Apply the safe-rollout framework: scope, bound, test, approve, pilot.",
            "Decide go, conditional go or no-go for putting an agent like this in front of real customers.",
            "Name who would be accountable and who could switch it off.",
        ],
        "produce": ["A short risk-and-guardrail table",
                    "A go / conditional / no-go decision with a named owner"],
        "acceptance": "You justified a deployment decision using the guardrails and the rollout framework, and named an accountable human owner.",
    },
]


add("h1", "Detailed Activity Walkthroughs")
add("callout", ("No code required", "Every activity uses a ready-made website, chatbot or AI "
                "agent. Open the file or link in the activity pack and follow the steps. Keep all "
                "data fictional and use a low-limit training API key."))
for activity in ACTIVITIES:
    add("h2", f"Activity {activity['n']} — {activity['title']}")
    add("table", (["Field", "Value"], [
        ["Topic", f"Topic {activity['topic']}"],
        ["Duration", activity["duration"]],
        ["Folder", f"activities/{activity['folder']}/"],
        ["Tools", activity["tool"]],
        ["Evidence status", activity["evidence"]],
    ]))
    add("h3", "Step-by-step")
    add("numbered", activity["steps"])
    add("h3", "What you produce")
    add("bullets", activity["produce"])
    add("callout", ("Done when", activity["acceptance"]))


# ============================================================ prompt library
add("h1", "Prompt Engineering Quick Reference")
add("p", "Use this checklist whenever you write a prompt for an AI agent. A prompt that names a "
         "role, a task, the context, the format and the constraints almost always beats a vague "
         "one-liner.")
add("table", (["Element", "Ask yourself", "Example phrase"], [
    ["Role", "Who should the AI be?", "'You are a marketing analyst...'"],
    ["Task", "What exactly do you want?", "'...list the top 3 channels by ROI...'"],
    ["Context", "What facts does it need?", "'...from this sales table...'"],
    ["Format", "How should it answer?", "'...as three bullets, one action each.'"],
    ["Constraints", "Any limits?", "'Keep it under 80 words, friendly tone.'"],
]))
add("h2", "Good vs Bad Prompts")
add("table", (["Bad prompt", "Why it fails", "Good prompt"], [
    ["'analyse this data'", "No role, task or format", "'As a data analyst, summarise the 3 biggest trends in this table as bullets.'"],
    ["'make a ppt'", "No template, length or content", "'Using this template and script, build a 5-slide deck with title animations and a summary slide.'"],
    ["'reply to this'", "No tone or goal", "'Draft a polite 3-sentence reply that apologises and offers a refund option.'"],
]))


# ============================================================ reflection framework
add("h1", "Reflection Framework — Four Risk Themes")
add("p", "After each activity, reflect using the same four themes. You will reuse these in your "
         "Case Study assessment, so keep short notes as you go.")
add("table", (["Theme", "Question to ask", "What to write down"], [
    ["Data Privacy", "What data did the AI see, store or ask for?", "Any personal or confidential data that was exposed or at risk."],
    ["Job Impact", "Whose work does this change?", "Tasks it sped up, and the new human role around it."],
    ["Ethical Concerns", "Could it mislead or be unfair?", "Any wrong, biased or overconfident output."],
    ["Cyber Security", "How could it be abused?", "Where an attacker or a bad prompt could cause harm."],
]))


# ============================================================ governance cheat-sheet
add("h1", "AI Data Governance — One-Page Cheat Sheet")
add("p", "The 7-part policy framework used by the Activity 5 generator website, aligned in "
         "spirit with the IMDA Model AI Governance Framework and the PDPA.")
add("table", (["Section", "What to state"], [
    ["1. Scope", "Which AI systems, agents and data assets the policy covers."],
    ["2. Roles", "Data owner, agent owner, approver and reviewer — named people."],
    ["3. Principles", "Accuracy, purpose limitation, protection, provenance, traceability, "
                      "human accountability."],
    ["4. Rules", "Which data agents may read, write or generate; which actions need human "
                 "approval first; and retention limits."],
    ["5. Audit & Logging", "What is logged and who reviews it, how often."],
    ["6. Accountability", "The named human answerable for each agent and dataset."],
    ["7. Review", "How often the policy and the agent's permissions are re-checked, and the "
                  "triggers for an early review."],
]))
add("callout", ("The one rule to remember", "AI is never the accountable party. A named human "
                "always is."))
add("p", "A worked example from the sample policy in the activity pack (Sunset Bay Resort — "
         "every detail fictional) shows what each of the four load-bearing sections looks like "
         "when it is filled in:")
add("table", (["Section", "Example from the sample policy"], [
    ["Scope", "The WhatsApp guest-support agent, the marketing-analysis agent and the website "
              "chatbot — plus the guest bookings, contact details and marketing spreadsheets "
              "they touch. Staff personal devices are out of scope."],
    ["Roles", "Data Owner — Front Office Manager (owns guest data). Agent Owner — Marketing "
              "Manager (keeps each agent's settings current). Approver — General Manager "
              "(signs off new agents and data rules). Reviewer — Duty Supervisor (checks "
              "output before it reaches a guest)."],
    ["Rules", "Agents may read one guest's booking only while serving that guest; may draft "
              "replies, reports and slides; any change to a live booking or price needs human "
              "approval first; chat logs are kept 12 months, then deleted."],
    ["Review", "The policy is reviewed every 12 months — earlier when a new agent, skill or "
               "data type is added, or after any incident. The General Manager owns the "
               "review."],
]))


# ============================================================ rollout checklist
add("h1", "Safe Roll-Out Checklist for AI Agents")
add("table", (["Gate", "Minimum evidence before go-live"], [
    ["Scope & tier", "The use case, its impact and how reversible its actions are."],
    ["Bound", "The data, tools and autonomy the agent is limited to."],
    ["Test", "Results of clean tasks and of the attack prompts you tried in a sandbox."],
    ["Approve", "Which risky actions require a human to approve first."],
    ["Own", "A named owner who monitors the agent and can switch it off."],
    ["Pilot", "A small, monitored roll-out before opening it to all users."],
]))


# ============================================================ source register
add("h1", "Source Register")
add("p", "These are the sources behind the dated facts and cases in this course. Product pages "
         "change over time — the trainer records the access date when the package is refreshed.")
add("table", (["ID", "Source", "URL"], [[sid, item["title"], item["url"]]
                                        for sid, item in SOURCES.items()]))
