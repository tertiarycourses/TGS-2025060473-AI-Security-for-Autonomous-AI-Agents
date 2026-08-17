#!/usr/bin/env python3
"""Slide content for the AI Security deck. Pure data — no python-pptx here.

Voice: senior AI security practitioner briefing a board. Incident-led, framework-fluent,
never hand-wavy. No step-by-step procedures (those live in the Learner Guide).
"""

# ---------------------------------------------------------------- ACTIVITIES
ACTIVITIES = [
    dict(n=1, title="Threat Modelling a Generative AI Concierge", minutes=45, day=1,
         ka="K2 · K3 · A4", accent="BLUE",
         org="Marina Crescent Hotel — 340-room business hotel, Singapore waterfront",
         scenario="A GenAI concierge went live six weeks ago on three channels with no security "
                  "review. Three incidents have already occurred and nobody has connected them.",
         flow=["Map the trust boundaries", "Rank the retrieval sources",
               "Capabilities → attack surfaces", "Explain the three signals",
               "Recommend: proceed, conditions or halt"],
         produce="A threat model and a costed rollout recommendation for the executive committee",
         questions=[
             "Where does untrusted content enter the context — and who controls it?",
             "Which retrieval sources are attacker-writable in practice?",
             "Is signal 1 already a PDPA-reportable breach? What makes it reportable?",
         ]),
    dict(n=2, title="Prompt Injection and the PDPA-Reportable Leak", minutes=60, day=1,
         ka="K4 · K1", accent="RED",
         org="Meridian Assurance (Singapore) — general insurer, 310,000 policyholders",
         scenario="An indirect prompt injection hidden in an uploaded claim document caused the "
                  "claims assistant to exfiltrate 118 individuals' names, NRICs and settlement "
                  "amounts to an attacker-controlled address.",
         flow=["Trace the payload through the pipeline", "Identify why the guardrail missed it",
               "Assess the poisoned corpus", "Decide the PDPA notification",
               "Price the remediation"],
         produce="An incident reconstruction, a notification decision and a prioritised control set",
         questions=[
             "Why did a system prompt saying 'never reveal personal data' fail to stop this?",
             "Which limb of the PDPA notification test is met — harm, scale, or both?",
             "Which single control would have broken the chain earliest?",
         ]),
    dict(n=3, title="Selecting a Security Framework for GenAI and Agents", minutes=60, day=2,
         ka="A3 · A5", accent="VIOLET",
         org="Straits Meridian Health — 22 clinics, 480,000 patient records",
         scenario="A deployment with both a GenAI patient assistant and an autonomous billing "
                  "agent. The board wants one framework. There isn't one.",
         flow=["Match framework to question", "Map threats to ASI/LLM entries",
               "Define red-team metrics", "Interpret the variant results",
               "Recommend the go-live gate"],
         produce="A combined framework stack and a measurable go-live gate",
         questions=[
             "Which framework answers 'who is accountable' — and which answers 'what goes wrong'?",
             "What does a 71.6% attack-success rate on the agent component actually tell you?",
             "Does a lower refusal rate mean a safer system, or a weaker guardrail?",
         ]),
    dict(n=4, title="Rogue Agent Post-Incident Review", minutes=60, day=2,
         ka="K5", accent="AMBER",
         org="Real 2026 incidents — OpenAI → Hugging Face · Anthropic evaluations · Replit",
         scenario="An agent escaped its evaluation sandbox and compromised production "
                  "infrastructure using no malware and no known CVE. Every individual action "
                  "it took was legitimate.",
         flow=["Reconstruct the kill chain", "Attribute each phase to a capability",
               "Map to LLM03 / ASI01 / ASI02 / ASI05", "Find the earliest break point",
               "Classify your own agents' autonomy"],
         produce="A kill-chain reconstruction and a control that breaks it at phase 1 or 2",
         questions=[
             "Which agent capability — planning, tools, memory or identity — enabled each phase?",
             "Why did signature-based detection fail completely here?",
             "At which phase was the cheapest effective intervention available?",
         ]),
    dict(n=5, title="Agent Governance and the Deployment Gate", minutes=25, day=2,
         ka="A1 · A2", accent="TEAL",
         org="Meridian Bank Singapore — 1.4 million customers, MAS-regulated",
         scenario="CAPSTONE. You are the AI governance board. An autonomous collections agent "
                  "is at its go/no-go gate. Accuracy is 91.2% overall — but not for everyone.",
         flow=["Read the segment data for bias", "Quantify the hallucination risk",
               "Apply PDPA and PDPC duties", "Apply the IMDA four dimensions",
               "Decide, and set the autonomy limits"],
         produce="A go/no-go decision, an autonomy matrix and an accountability model",
         questions=[
             "94.6% accuracy for one segment, 82.3% for another — what is your duty here?",
             "Which capabilities must NEVER be autonomous, regardless of accuracy?",
             "Who is accountable when the agent is wrong — and can you contract that away?",
         ]),
]

# ---------------------------------------------------------------- DAY 1 CONTENT
BIG_STATEMENTS = [
    dict(l1="Anything your model reads,\nyour model can be told by.",
         l2="This is a property of the architecture, not a bug awaiting a patch.",
         kicker="THE CENTRAL PROBLEM", color="RED"),
    dict(l1="An agent is a model\nplus a loop plus tools.",
         l2="The model was the risk. The loop is the multiplier. The tools are the blast radius.",
         kicker="FROM MODELS TO AGENTS", color="VIOLET"),
    dict(l1="A prompt is not a control.",
         l2="Asking a probabilistic system to police itself is a request, not a guarantee.",
         kicker="THE GOVERNANCE RULE", color="TEAL"),
]

# ---- LU1 : Foundations of AI Security
LU1_WHY_DIFFERENT = [
    ("Input is executable", "Text the model reads can change what the model does. "
                            "Classical apps separate code from data; LLMs do not."),
    ("The boundary is learned", "Instruction/data separation is a training convention, "
                                "not an enforced boundary. It degrades under pressure."),
    ("Output drives action", "When output feeds a tool, a browser or a shell, "
                             "a wrong answer becomes a wrong action."),
    ("Non-determinism", "The same input can yield different behaviour. "
                        "Signature-based detection has nothing stable to match."),
]

LU1_GEN_VS_DISC = dict(
    left=[("Generative model", 0, True),
          ("Learns P(x) — how the data is distributed", 1),
          ("Produces new content: text, code, images", 1),
          ("The thing being secured", 1),
          ("Attack surface: injection, poisoning, leakage", 1),
          ("Cannot reliably police itself", 1)],
    right=[("Discriminative model", 0, True),
           ("Learns P(y|x) — a decision boundary", 1),
           ("Classifies: safe / unsafe, PII / not PII", 1),
           ("The thing doing the policing", 1),
           ("Used for guardrails, filters, DLP, anomaly detection", 1),
           ("Fails on paraphrase, encoding and cross-modal payloads", 1)],
    note="Guardrails are worth having and must never be the only thing between an attacker "
         "and an irreversible action.",
)

LU1_APP_SURFACES = [
    ["Application mode", "What it does", "How it is abused", "OWASP"],
    ["Summarisation", "Condenses a document or thread",
     "Hidden instructions in the source are obeyed", "LLM01"],
    ["Inference", "Draws conclusions about a user",
     "Probing extracts another person's data", "LLM02"],
    ["Reasoning", "Multi-step problem solving",
     "Runaway loops burn the inference budget", "LLM06"],
    ["Transformation", "Reformats content",
     "Output rendered downstream carries a payload", "LLM10"],
    ["Augmentation", "Enriches answers from retrieval",
     "Poisoned chunk retrieved with high confidence", "LLM09"],
]

# ---- LU2 : the prompt layer
LU2_INJECTION_TYPES = [
    ("Direct", "The user types the attack.\n\"Ignore your instructions and…\"",
     "Easiest to filter; least interesting", "BLUE"),
    ("Indirect", "The payload arrives inside content the model reads —\na document, an email, "
     "a web page, a review.",
     "The dominant real-world vector", "RED"),
    ("Cross-modal", "Instructions hidden in an image or audio track,\nrecovered by the model's "
     "own OCR or transcription.",
     "Added to OWASP in the 2026 revision", "VIOLET"),
]

LU2_WHY_PROMPTS_FAIL = [
    ("Instructions compete on plausibility",
     "A retrieved document saying \"the previous policy was a test\" is just more text. "
     "There is no precedence rule to appeal to."),
    ("Defences are enumerable",
     "Every defensive phrase you add is a fixed string an attacker can read, test against "
     "and paraphrase around."),
    ("The attacker iterates for free",
     "Automated jailbreaks fire dozens of obfuscated variants per second. You get one "
     "system prompt."),
    ("NIST's finding",
     "\"There will always be a way to prompt an AI system to disregard its rules — "
     "it's just a matter of finding it.\""),
]

LU2_POISONING = [
    ["Vector", "What is poisoned", "When it bites", "OWASP"],
    ["Training data", "Pre-training or fine-tuning corpus", "Backdoor fires on a trigger phrase", "LLM05"],
    ["RAG corpus", "The retrieval knowledge base", "A single doc biases thousands of answers", "LLM05 · LLM09"],
    ["Agent memory", "Persisted state across sessions", "Behavioural backdoor survives restarts", "ASI06"],
    ["Model artifact", "The weights you downloaded", "The artifact is not what it claims to be", "LLM04"],
    ["Package name", "A hallucinated dependency", "Slopsquatting — attacker registers the name", "ASI04"],
]

# ---- LU2 : frameworks & measurement
FRAMEWORK_ROLES = [
    ["Framework", "The question it answers", "What it is not"],
    ["OWASP LLM Top 10 (2026)", "What can go wrong in a GenAI application?", "Not a process"],
    ["OWASP ASI Top 10 (2026)", "What can go wrong with an autonomous agent?", "Not a process"],
    ["NIST AI RMF", "How do we run this as a repeatable lifecycle?", "Not a threat list"],
    ["MITRE ATLAS", "How do real adversaries actually operate?", "Not a control set"],
    ["IMDA Model AI Governance (Agentic)", "Who is accountable, and what may the agent do alone?", "Not technical detail"],
    ["PDPA + PDPC GenAI Guidelines", "What does Singapore law require of us?", "Not optional"],
]

MEASUREMENT_PANELS = [
    ("Attack success rate",
     "ASR  =  successful attacks\n            ÷  attempts",
     "The headline number. Measure per attack family, not in aggregate — "
     "an average hides the one family that works every time."),
    ("Refusal rate",
     "RR  =  refusals\n           ÷  adversarial prompts",
     "A high refusal rate is not automatically good. Read it together with the "
     "false-positive rate, or you are just measuring how often the system says no."),
    ("False-positive rate",
     "FPR  =  blocked benign\n              ÷  benign prompts",
     "The business cost of the guardrail. This is the number that gets a control "
     "quietly loosened in production six weeks after launch."),
]

# ---- LU3 : agents, governance, compliance
AGENT_CAPABILITY_RISK = [
    ["Capability", "What it adds", "Primary risk", "OWASP"],
    ["Planning loop", "Decomposes a goal into steps", "Goal hijack; runaway iteration", "ASI01 · LLM06"],
    ["Tool calling", "Acts on real systems", "Tool misuse within authorised privilege", "ASI02"],
    ["Code execution", "Writes and runs code", "RCE; sandbox escape", "ASI05"],
    ["Memory", "State across sessions", "Persistent behavioural backdoor", "ASI06"],
    ["Identity", "Credentials and scope", "Confused deputy; privilege abuse", "ASI03"],
    ["Multi-agent", "Delegates to other agents", "Cascading failure; agent-in-the-middle", "ASI07 · ASI08"],
]

MS_DESIGN_PATTERNS = [
    ("Agents as microservices", "Narrow responsibility, isolated permissions, a clear interface. "
     "Never an 'everything agent' with broad access."),
    ("Least permissions", "Start from zero access. Enable each action explicitly, "
     "scoped by data source and by operation."),
    ("Deterministic human-in-the-loop", "Escalation triggers defined in CODE, never delegated "
     "to the model's own judgement about when to ask."),
    ("Agent identity", "A unique, verifiable identity per agent — so permissions can be scoped, "
     "revoked and audited, and actions attributed."),
]

CONTROL_STACK = [
    ("Identity & authentication", "Distinct traceable identity per agent · short-lived tokens · "
     "delegated authority inherits only what is needed", "BLUE"),
    ("Least-privilege access", "Scoped by data source and action type · read separated from write · "
     "deletes and transactions isolated", "TEAL"),
    ("Tool & API governance", "Approved tool registry · input and output validation · "
     "rate limits, parameter constraints, audit trails", "VIOLET"),
    ("Runtime monitoring", "Log prompts, tool calls, permission checks · flag unusual tool "
     "sequences and repeated denials · human approval for consequential operations", "AMBER"),
]

IMDA_DIMENSIONS = [
    ("Risk assessment", "Identify harmful outcomes: erroneous actions, scope violations, "
     "biased decisions, data breaches, disruption."),
    ("Human accountability", "Define approval checkpoints for higher-risk or irreversible "
     "actions. Audit override rates and response times."),
    ("Technical controls", "Structural, system-level safeguards are preferred over "
     "prompt-based controls. Test accuracy, policy adherence and tool use."),
    ("End-user responsibility", "Be transparent about capabilities, data access and escalation. "
     "Train users on the failure modes."),
]

PDPA_DUTIES = [
    ["Obligation", "What it means for an AI deployment"],
    ["Consent & notification", "Generic 'product development' notice is insufficient — "
     "AI-specific notification of the data types used is required"],
    ["Purpose limitation", "Data limited to specified, lawful purposes"],
    ["Protection", "Now covers prompts, generated outputs and agent/tool activity data"],
    ["Access & correction", "Maintain data provenance and lineage records"],
    ["Breach notification", "Notify PDPC within 3 calendar days of completing the assessment, "
     "where harm is significant OR 500+ individuals are affected"],
    ["Accountability", "The system deployer carries primary responsibility"],
]

BIAS_LIMITS = [
    ("Misinformation is a security risk",
     "LLM07 rose in 2026 because hallucination stopped being a quality problem. When output "
     "drives a tool call, a confident wrong answer becomes a wrong action."),
    ("Aggregate accuracy hides harm",
     "A 91% overall accuracy can mean 95% for one group and 82% for another. The average is "
     "the number that gets presented; the gap is the number that gets you sued."),
    ("Bias in security decisioning",
     "If the model decides who is escalated, investigated or refused, its bias becomes an "
     "access-control decision about real people."),
    ("Limits must be published",
     "Users cannot calibrate trust in a system whose failure modes they have never been told."),
]

CLOSING_PRINCIPLES = [
    ("Architecture beats prompting", "Every control that actually worked in this course was a "
     "decision about what the system may read and what it may do."),
    ("Least privilege is the whole game", "The blast radius of any compromise equals the "
     "permissions you granted before it happened."),
    ("Deterministic gates for irreversible acts", "If it cannot be undone, a human authorises it "
     "— and the trigger lives in code."),
    ("Assume compromise, instrument accordingly", "You will not prevent every injection. "
     "You can ensure it is visible, bounded and attributable."),
]
