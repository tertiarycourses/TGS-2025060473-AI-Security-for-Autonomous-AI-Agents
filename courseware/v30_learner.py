#!/usr/bin/env python3
"""Learner Guide source derived from the v3.0 slide and evidence model.

The deck remains concept-led.  This module expands every teaching slide into
learner-readable notes, then adds detailed activity procedures, acceptance
criteria and the full source register.
"""

from v30_content import SLIDES, SOURCES


SECTIONS = []


def add(kind, payload, level=0):
    SECTIONS.append((level, kind, payload))


def source_line(spec):
    ids = spec.get("sources", [])
    if not ids:
        return "Administrative or classroom-synthesis slide; no external factual claim is introduced."
    return "Sources: " + ", ".join(f"{sid} — {SOURCES[sid]['title']}" for sid in ids)


add("h1", "How to Use This Evidence-Grounded Guide")
add("p", "This guide follows the 207-slide trainer deck in sequence. It expands the concepts, "
         "evidence status and control logic while keeping click-by-click procedures in the five "
         "activity walkthroughs. Product capabilities are always configuration- and version-specific.")
add("table", (["Evidence label", "Meaning", "How to use it"], [
    ["HIST / DEF / PROD", "Historical, definitional or product documentation", "Cite the listed source and check the as-of date."],
    ["CASE-V", "Verified incident, vulnerability or adjudicated case", "State only what the primary or authoritative record supports."],
    ["CASE-R", "Reported security research or campaign", "Preserve the source's method, denominator and limitations."],
    ["SIM", "Realistic synthetic classroom scenario", "Treat every name, event and number as fictional."],
    ["SYN", "Instructional synthesis", "Use as a reasoning aid, not as a claimed empirical statistic."],
]))
add("callout", ("Evidence rule", "Never convert a demonstration into a breach, a simulation into a real incident, or a vendor statement into an independently verified outcome."))


for spec in SLIDES:
    if spec["kind"] in {"cover", "attendance", "trainer", "break", "lms", "thankyou"}:
        continue
    if spec["kind"] == "section":
        add("h1", spec["title"])
        if spec.get("note"):
            add("p", spec["note"])
        continue

    add("h2", f"Slide {spec['n']} — {spec['title']}")
    add("callout", (f"Evidence status: {spec['evidence']}", source_line(spec)))
    kind = spec["kind"]
    if kind == "table":
        add("table", (spec.get("headers", []), spec.get("rows", [])))
    elif kind == "compare":
        left = spec.get("left", [])
        right = spec.get("right", [])
        rows = []
        for idx in range(max(len(left), len(right))):
            rows.append([left[idx] if idx < len(left) else "", right[idx] if idx < len(right) else ""])
        add("table", ([spec.get("lhead", "First view"), spec.get("rhead", "Second view")], rows))
    elif kind == "cards":
        rows = []
        for card in spec.get("cards", []):
            if isinstance(card, dict):
                rows.append([card.get("title", ""), card.get("body", "")])
            else:
                rows.append(list(card[:2]))
        add("table", (["Concept", "Meaning or control implication"], rows))
    elif kind == "flow":
        add("numbered", spec.get("steps", []))
    else:
        items = spec.get("points", [])
        if items:
            add("bullets", items)
    if spec.get("note"):
        add("callout", ("Control implication", spec["note"]))


ACTIVITIES = [
    {
        "n": 1,
        "title": "Threat Modelling a Generative AI Concierge",
        "folder": "activity-1-threat-modelling-genai-concierge",
        "duration": "45 minutes",
        "evidence": "SIM — every organisation, person, event, count and value is fictional.",
        "steps": [
            "Read the scenario and list every channel, data store, retrieval source, model, tool and output consumer.",
            "Draw the data-flow diagram. Mark where data crosses from a public, partner or internal writer into model context.",
            "Mark personal data, secrets and business-sensitive data; record purpose, owner and retention for each.",
            "For each attacker-writable source, write one realistic abuse case without running it against a live system.",
            "Trace the authority path from content to model interpretation, tool selection, identity, action and effect.",
            "Rank each boundary by impact, likelihood, reversibility and detection difficulty.",
            "Choose the earliest deterministic control for the top three risks; state residual risk and operational cost.",
            "Recommend proceed, conditional proceed or halt, and attach the completed deployment checklist.",
        ],
        "evidence_items": ["One labelled data-flow diagram", "One ranked abuse-case table", "Three control decisions with owners", "A rollout decision and checklist"],
        "acceptance": "The diagram covers at least three channels, four retrieval sources and four tools; each of the top three risks has a source-to-sink chain, owner, control, test evidence, residual risk and operational cost; the group records one rollout decision.",
    },
    {
        "n": 2,
        "title": "Prompt Injection and the PDPA Breach Decision",
        "folder": "activity-2-prompt-injection-data-leakage",
        "duration": "60 minutes",
        "evidence": "SIM — use only the supplied masked data, local dummy tools and non-routable destinations.",
        "steps": [
            "Establish a clean baseline using a legitimate document and record expected output and permitted actions.",
            "Run the supplied direct-injection variant against the dummy harness; record whether intent or output changes.",
            "Run the indirect document/email variant and identify the exact carrier, trigger, interpreted instruction and proposed effect.",
            "Run the context-file and cross-modal variants only with the supplied synthetic files; never upload real customer data.",
            "Record attack success separately from refusal, false-positive and clean-task success rates.",
            "Replace prompt-only protection with structural controls: trusted recipient binding, tool schema validation, retrieval isolation and action approval.",
            "Re-run the same variant set and compare evidence, including useful-task degradation and operational friction.",
            "Apply the current PDPA significant-harm and significant-scale decision tests; document facts still needed and do not assume every leak is notifiable.",
            "Recommend a reduced-mode, conditional or halted posture and name the evidence needed to restore capability.",
        ],
        "evidence_items": ["Baseline and variant test log", "Source-to-sink chain", "ASR/false-positive/clean-task comparison", "PDPA decision record", "Prioritised remediation plan"],
        "acceptance": "The clean baseline and every supplied synthetic variant are logged against the same deterministic policy; attack success, false positives and clean-task success are reported separately; the PDPA record separates significant harm, significant scale, information gaps and the resulting decision.",
    },
    {
        "n": 3,
        "title": "Selecting a Security Framework for GenAI and Agents",
        "folder": "activity-3-security-framework-selection",
        "duration": "60 minutes",
        "evidence": "SIM — all deployment details and performance data are fictional classroom material.",
        "steps": [
            "Classify NIST AI RMF, OWASP LLM Top 10, OWASP Agentic Top 10, MITRE ATLAS, IMDA and PDPA by the question each answers.",
            "Separate the generative component from the acting component and record their data, tools, identity, state and autonomy.",
            "Map threats to OWASP categories and ATLAS techniques without claiming the taxonomies are controls.",
            "Map lifecycle actions to Govern, Map, Measure and Manage; name an owner and evidence artifact for each.",
            "Map higher-impact or irreversible actions to IMDA-aligned autonomy limits and meaningful human approval.",
            "Apply PDPA obligations where personal data is collected, used, disclosed, retained, transferred or breached.",
            "Interpret attack success, false positives, clean-task success and segment results together; show calculation assumptions.",
            "Define organisation-specific go-live thresholds, re-test triggers and a conditional go/no-go decision.",
        ],
        "evidence_items": ["Framework-purpose matrix", "Component-threat-control map", "Metric calculations", "Go-live gate with owners and re-test triggers"],
        "acceptance": "Each framework question is answered correctly; both operating layers are mapped; every go-live condition has a metric, organisation-defined threshold, owner, test method and re-test trigger rather than being presented as a universal fact.",
    },
    {
        "n": 4,
        "title": "Evidence-Based Rogue Agent Incident Review",
        "folder": "activity-4-rogue-agent-incident-review",
        "duration": "60 minutes",
        "evidence": "CASE-V and CASE-R — preserve the label, source date and stated limitations for every case.",
        "steps": [
            "Choose EchoLeak, the Amazon Q extension event, the Replit application-database incident or the reported ClawHavoc campaign.",
            "Record the source, publication date, evidence class and exact supported claim before analysis.",
            "Separate normal capability, vulnerability or control failure, and observed impact.",
            "Map the untrusted source, interpretation mechanism, identity or permission, privileged sink and effect.",
            "For skills, plugins and MCP servers, review provenance, publisher, version, update channel, requested capabilities and bundled code.",
            "Choose one preventive and one detective or recovery control at the earliest feasible chain point.",
            "Define the approval screen: exact action, target, data, scope, destination, reversibility and evidence shown to the reviewer.",
            "Present the reconstruction without converting research demonstrations into production breaches or reported counts into current prevalence.",
        ],
        "evidence_items": ["Evidence card for each case", "Source-to-sink chain", "Skill/plugin/MCP supply-chain review", "Preventive and recovery controls", "Residual-risk statement"],
        "acceptance": "Each of the four cases has a source, date, evidence label, source-to-sink chain, supported and unsupported claim, preventive control, detective or recovery control and residual risk; the Amazon Q code is stated as not executed, Replit as restored with no data loss, and campaign figures retain their dated-method limitations; one skill, plugin or MCP server receives an explicit gate decision.",
    },
    {
        "n": 5,
        "title": "Agent Governance and the Deployment Gate",
        "folder": "activity-5-agent-governance-deployment-gate",
        "duration": "25 minutes",
        "evidence": "SIM — the bank, customers, metrics, volumes and outcomes are fictional.",
        "steps": [
            "Read aggregate and segment results; identify what the aggregate hides and verify every calculation.",
            "Map personal-data purpose, notification, protection, retention, transfer and breach-response obligations.",
            "Classify each action as agent-alone, human approval required or prohibited, based on impact and reversibility.",
            "For every approval, specify the exact action, target, data, destination, evidence and rollback shown to the reviewer.",
            "Confirm guardrails, identity scopes, sandbox, egress, memory provenance, logging, monitoring, kill switch and recovery evidence.",
            "State go, conditional go or no-go; name accountable owner, unmet conditions, review date and release evidence.",
            "Describe the user notice, challenge route, human escalation and remedy for an affected person.",
        ],
        "evidence_items": ["Segment-risk interpretation", "Data and autonomy inventory", "Approval matrix", "Named accountable owner", "Testable deployment decision"],
        "acceptance": "All calculations are reproducible from the SIM data; all ten capabilities are classified; every irreversible or high-impact action is prohibited or behind deterministic approval; every condition has an owner, test, expiry or review date and re-test trigger; affected people have a human review and remedy route.",
    },
]


add("h1", "Detailed Activity Walkthroughs")
add("callout", ("Safe-lab boundary", "Use synthetic data, dummy credentials, local or sandboxed tools, and non-routable recipients. Do not probe production services, install unreviewed community packages, or paste real personal data into public AI systems."))
for activity in ACTIVITIES:
    add("h2", f"Activity {activity['n']} — {activity['title']}")
    add("table", (["Field", "Value"], [
        ["Duration", activity["duration"]],
        ["Folder", f"activities/{activity['folder']}/"],
        ["Evidence status", activity["evidence"]],
    ]))
    add("h3", "Step-by-step procedure")
    add("numbered", activity["steps"])
    add("h3", "Required evidence")
    add("bullets", activity["evidence_items"])
    add("callout", ("Acceptance criteria", activity["acceptance"]))


add("h1", "Operational Best-Practice Checklist")
add("table", (["Gate", "Minimum evidence before approval"], [
    ["Own", "Named business owner, technical owner, risk owner and incident owner"],
    ["Purpose", "Documented intended use, excluded uses, affected people and appeal route"],
    ["Data", "Sources, writers, personal-data purpose, minimisation, retention, deletion and transfers"],
    ["Content trust", "Untrusted-content map, provenance, ingestion review and prompt-injection test set"],
    ["Identity", "Dedicated agent identity, least privilege, short-lived credentials and revocation path"],
    ["Tools", "Allowlisted tools, constrained schemas, parameter validation and bounded action scope"],
    ["Runtime", "Sandbox, filesystem boundary, resource quotas and no privilege escalation"],
    ["Network", "Default-deny egress, named destinations, inspection and exception alerts"],
    ["Human approval", "Exact effect, target, data and reversibility shown before high-impact action"],
    ["Supply chain", "Publisher, version pin, signature or checksum, capability review and update re-approval"],
    ["Memory", "Provenance, review status, retention, correction, deletion and poisoning tests"],
    ["Measure", "Clean-task success, attack success, false positives, unsafe actions and segment results"],
    ["Operate", "Traceable logs, monitoring, kill switch, credential revoke, rollback and recovery test"],
    ["Change", "Re-test on model, prompt, corpus, tool, skill, identity, runtime or policy change"],
]))


add("h1", "Source Register")
add("p", "Access dates should be recorded by the trainer or course owner when the package is refreshed. Where a product page changes, the deployed version and configuration remain part of the evidence record.")
add("table", (["ID", "Source", "URL"], [[sid, item["title"], item["url"]] for sid, item in SOURCES.items()]))
