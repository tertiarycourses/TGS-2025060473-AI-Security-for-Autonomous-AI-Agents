#!/usr/bin/env python3
"""Security diagrams for the AI Security for Autonomous AI Agents deck (TGS-2025060473).

House palette, Arial, white background, 150 dpi. Every asset here is placed on a slide
by build_slides.py — no orphan assets.
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle, Circle
import numpy as np

plt.rcParams["font.family"] = "Arial"
plt.rcParams["font.size"] = 11

BLUE = "#1F6FEB"; TEAL = "#10B981"; VIOLET = "#7C3AED"; AMBER = "#F59E0B"
RED = "#DC2626"; INK = "#161B26"; GREY = "#5B6372"; LIGHT = "#F5F8FC"; LINE = "#D7E0EA"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")
os.makedirs(OUT, exist_ok=True)


def save(fig, name):
    p = os.path.join(OUT, name)
    fig.savefig(p, dpi=150, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("  ", name)


def box(ax, x, y, w, h, label, sub=None, fc=LIGHT, ec=BLUE, tc=INK, fs=11, lw=1.6):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.06",
                                fc=fc, ec=ec, lw=lw, zorder=2))
    ax.text(x + w / 2, y + h * (0.60 if sub else 0.5), label, ha="center", va="center",
            fontsize=fs, fontweight="bold", color=tc, zorder=3)
    if sub:
        ax.text(x + w / 2, y + h * 0.26, sub, ha="center", va="center",
                fontsize=fs - 2.5, color=GREY, zorder=3)


def arrow(ax, x1, y1, x2, y2, color=BLUE, lw=2.0, style="-|>"):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle=style, mutation_scale=17,
                                 color=color, lw=lw, zorder=1,
                                 shrinkA=2, shrinkB=2))


# ---------------------------------------------------------------- 1. trust boundary
def chart_trust_boundary():
    fig, ax = plt.subplots(figsize=(11, 5.4))
    ax.set_xlim(0, 11); ax.set_ylim(0, 5.4); ax.axis("off")

    ax.text(0.1, 5.15, "The context window has no trust boundary",
            fontsize=15, fontweight="bold", color=INK)
    ax.text(0.1, 4.82, "Every source below becomes the same undifferentiated token sequence",
            fontsize=10.5, color=GREY)

    srcs = [("System prompt", "you wrote it", TEAL, True),
            ("User message", "anyone", RED, False),
            ("Retrieved doc", "anyone who writes\nto the corpus", RED, False),
            ("Tool output", "external system", AMBER, False),
            ("Agent memory", "prior sessions", AMBER, False)]
    for i, (n, who, c, trusted) in enumerate(srcs):
        x = 0.15 + i * 2.18
        box(ax, x, 3.15, 1.95, 1.28, n, who, fc="white", ec=c, tc=c, fs=10.5)
        ax.text(x + 0.975, 2.95, "TRUSTED" if trusted else "UNTRUSTED", ha="center",
                fontsize=8, fontweight="bold", color=c)
        arrow(ax, x + 0.975, 2.80, x + 0.975, 2.30, color=c, lw=1.5)

    ax.add_patch(FancyBboxPatch((0.15, 1.30), 10.7, 0.95,
                                boxstyle="round,pad=0.02,rounding_size=0.06",
                                fc=INK, ec=INK, zorder=2))
    ax.text(5.5, 1.90, "CONTEXT WINDOW  →  one flat token sequence", ha="center",
            fontsize=12.5, fontweight="bold", color="white", zorder=3)
    ax.text(5.5, 1.55, "the model cannot tell which tokens are instructions and which are data",
            ha="center", fontsize=10, color="#9CDCFE", zorder=3, style="italic")

    arrow(ax, 5.5, 1.22, 5.5, 0.80, color=INK, lw=2.2)
    ax.add_patch(FancyBboxPatch((3.0, 0.12), 5.0, 0.62,
                                boxstyle="round,pad=0.02,rounding_size=0.06",
                                fc="#FDECEC", ec=RED, lw=1.8, zorder=2))
    ax.text(5.5, 0.43, "LLM01  Prompt Injection — architectural, not a bug",
            ha="center", fontsize=11.5, fontweight="bold", color=RED, zorder=3)
    save(fig, "diagram-trust-boundary.png")


# ---------------------------------------------------------------- 2. OWASP LLM Top 10
def chart_owasp_llm():
    fig, ax = plt.subplots(figsize=(11, 5.6))
    ax.set_xlim(0, 11); ax.set_ylim(0, 5.6); ax.axis("off")
    ax.text(0.1, 5.35, "OWASP Top 10 for LLM Applications — 2026",
            fontsize=15, fontweight="bold", color=INK)
    ax.text(0.1, 5.02, "8 of 10 entries moved. Ranking now weights 7,714 real incidents at 25%.",
            fontsize=10.5, color=GREY)

    items = [("LLM01", "Prompt Injection", "steady", RED),
             ("LLM02", "Sensitive Information Disclosure", "steady", RED),
             ("LLM03", "Excessive Agency", "up 3", VIOLET),
             ("LLM04", "Supply Chain", "down 1", AMBER),
             ("LLM05", "Data and Model Poisoning", "down 1", AMBER),
             ("LLM06", "Unbounded Consumption", "up 4", VIOLET),
             ("LLM07", "Misinformation", "up 2", VIOLET),
             ("LLM08", "Hidden Context Exposure", "renamed", BLUE),
             ("LLM09", "Vector and Embedding Weaknesses", "down 1", AMBER),
             ("LLM10", "Improper Output Handling", "down 5", AMBER)]
    for i, (code, name, mv, c) in enumerate(items):
        col = i % 2; row = i // 2
        x = 0.15 + col * 5.5; y = 4.30 - row * 0.83
        ax.add_patch(FancyBboxPatch((x, y), 5.2, 0.68,
                                    boxstyle="round,pad=0.01,rounding_size=0.05",
                                    fc=LIGHT, ec=LINE, lw=1.0, zorder=2))
        ax.add_patch(Rectangle((x, y), 0.075, 0.68, fc=c, ec=c, zorder=3))
        ax.text(x + 0.25, y + 0.34, code, fontsize=10.5, fontweight="bold",
                color=c, va="center", zorder=3)
        ax.text(x + 1.05, y + 0.34, name, fontsize=10.5, color=INK, va="center", zorder=3)
        ax.text(x + 5.05, y + 0.34, mv, fontsize=8.5, color=GREY, va="center",
                ha="right", style="italic", zorder=3)
    save(fig, "diagram-owasp-llm-top10.png")


# ---------------------------------------------------------------- 3. OWASP ASI Top 10
def chart_owasp_asi():
    fig, ax = plt.subplots(figsize=(11, 5.6))
    ax.set_xlim(0, 11); ax.set_ylim(0, 5.6); ax.axis("off")
    ax.text(0.1, 5.35, "OWASP Top 10 for Agentic Applications (ASI) — 2026",
            fontsize=15, fontweight="bold", color=INK)
    ax.text(0.1, 5.02, "The agent-specific companion list. Autonomy is the multiplier.",
            fontsize=10.5, color=GREY)

    items = [("ASI01", "Agent Goal Hijack", RED),
             ("ASI02", "Tool Misuse & Exploitation", RED),
             ("ASI03", "Identity & Privilege Abuse", RED),
             ("ASI04", "Agentic Supply Chain", AMBER),
             ("ASI05", "Unexpected Code Execution (RCE)", RED),
             ("ASI06", "Memory Poisoning", AMBER),
             ("ASI07", "Insecure Inter-Agent Comms", AMBER),
             ("ASI08", "Cascading Failures", VIOLET),
             ("ASI09", "Human-Agent Trust Exploitation", VIOLET),
             ("ASI10", "Rogue Agents", RED)]
    for i, (code, name, c) in enumerate(items):
        col = i % 2; row = i // 2
        x = 0.15 + col * 5.5; y = 4.30 - row * 0.83
        ax.add_patch(FancyBboxPatch((x, y), 5.2, 0.68,
                                    boxstyle="round,pad=0.01,rounding_size=0.05",
                                    fc=LIGHT, ec=LINE, lw=1.0, zorder=2))
        ax.add_patch(Rectangle((x, y), 0.075, 0.68, fc=c, ec=c, zorder=3))
        ax.text(x + 0.25, y + 0.34, code, fontsize=10.5, fontweight="bold",
                color=c, va="center", zorder=3)
        ax.text(x + 1.05, y + 0.34, name, fontsize=10.5, color=INK, va="center", zorder=3)
    save(fig, "diagram-owasp-asi-top10.png")


# ---------------------------------------------------------------- 4. agent anatomy
def chart_agent_anatomy():
    fig, ax = plt.subplots(figsize=(11, 6.0))
    ax.set_xlim(0, 11); ax.set_ylim(0, 6.0); ax.axis("off")
    ax.text(0.1, 5.78, "An agent is a model plus a loop plus tools",
            fontsize=15, fontweight="bold", color=INK)
    ax.text(0.1, 5.45, "Each added component adds a distinct attack surface",
            fontsize=10.5, color=GREY)

    # centre hub
    ax.add_patch(FancyBboxPatch((4.15, 2.42), 2.7, 1.42,
                                boxstyle="round,pad=0.02,rounding_size=0.08",
                                fc=INK, ec=INK, zorder=3))
    ax.text(5.5, 3.42, "THE AGENT", ha="center", fontsize=13, fontweight="bold",
            color="white", zorder=4)
    ax.text(5.5, 2.92, "plan → act → observe", ha="center", fontsize=10,
            color="#9CDCFE", zorder=4, style="italic")

    # satellites: title / sub / risk chip each on its own line
    sats = [(0.30, 3.90, "MODEL", "reasoning, refusals", BLUE, "LLM01 · LLM07"),
            (7.90, 3.90, "TOOLS", "actions on the world", RED, "ASI02 · ASI05"),
            (0.30, 0.98, "MEMORY", "state across sessions", AMBER, "ASI06"),
            (7.90, 0.98, "IDENTITY", "credentials, scope", VIOLET, "ASI03")]
    for x, y, n, sub, c, risk in sats:
        w, h = 2.80, 1.42
        ax.add_patch(FancyBboxPatch((x, y), w, h,
                                    boxstyle="round,pad=0.02,rounding_size=0.06",
                                    fc="white", ec=c, lw=1.9, zorder=2))
        ax.text(x + w / 2, y + 1.05, n, ha="center", va="center",
                fontsize=12, fontweight="bold", color=c, zorder=3)
        ax.text(x + w / 2, y + 0.66, sub, ha="center", va="center",
                fontsize=9.5, color=GREY, zorder=3)
        ax.text(x + w / 2, y + 0.26, risk, ha="center", va="center",
                fontsize=8.5, fontweight="bold", color=c, zorder=3)

    arrow(ax, 3.15, 4.35, 4.25, 3.70, color=BLUE, lw=1.8)
    arrow(ax, 7.85, 4.35, 6.75, 3.70, color=RED, lw=1.8)
    arrow(ax, 3.15, 1.90, 4.25, 2.58, color=AMBER, lw=1.8)
    arrow(ax, 7.85, 1.90, 6.75, 2.58, color=VIOLET, lw=1.8)

    ax.add_patch(FancyBboxPatch((2.35, 0.10), 6.3, 0.60,
                                boxstyle="round,pad=0.02,rounding_size=0.05",
                                fc="#FDECEC", ec=RED, lw=1.6, zorder=2))
    ax.text(5.5, 0.40, "LLM03  Excessive Agency — the loop runs faster than review",
            ha="center", va="center", fontsize=11, fontweight="bold", color=RED, zorder=3)
    save(fig, "diagram-agent-anatomy.png")


# ---------------------------------------------------------------- 5. kill chain
def chart_kill_chain():
    fig, ax = plt.subplots(figsize=(11.4, 4.5))
    ax.set_xlim(0, 11.4); ax.set_ylim(0, 4.5); ax.axis("off")
    ax.text(0.1, 4.25, "Agent kill chain — OpenAI → Hugging Face, July 2026",
            fontsize=15, fontweight="bold", color=INK)
    ax.text(0.1, 3.92, "No malware. No known CVE. Every individual action was legitimate.",
            fontsize=10.5, color=GREY, style="italic")

    phases = [("1  RECON", "OSINT on real devs\ncreated GitHub account", BLUE),
              ("2  SUPPLY CHAIN", "obfuscated code in a PR\nsockpuppets for credibility", VIOLET),
              ("3  SOCIAL ENG", "claimed accidental commit\nspear-phished maintainer", AMBER),
              ("4  AI-TARGETING", "prompt injection in an\nHTML comment in an issue", RED)]
    for i, (n, sub, c) in enumerate(phases):
        x = 0.15 + i * 2.82
        ax.add_patch(FancyBboxPatch((x, 1.75), 2.55, 1.75,
                                    boxstyle="round,pad=0.02,rounding_size=0.06",
                                    fc="white", ec=c, lw=1.9, zorder=2))
        ax.add_patch(Rectangle((x, 3.36), 2.55, 0.14, fc=c, ec=c, zorder=3))
        ax.text(x + 1.275, 2.95, n, ha="center", fontsize=11.5, fontweight="bold",
                color=c, zorder=3)
        ax.text(x + 1.275, 2.30, sub, ha="center", fontsize=9.5, color=INK, zorder=3)
        if i < 3:
            arrow(ax, x + 2.60, 2.62, x + 2.78, 2.62, color=GREY, lw=2.0)

    ax.add_patch(FancyBboxPatch((0.15, 0.62), 11.05, 0.88,
                                boxstyle="round,pad=0.02,rounding_size=0.06",
                                fc=INK, ec=INK, zorder=2))
    ax.text(5.68, 1.20, "RESULT:  chained stolen credentials + zero-day → RCE → production database",
            ha="center", fontsize=11.5, fontweight="bold", color="white", zorder=3)
    ax.text(5.68, 0.85, "Detected by anomaly pipeline reviewing ~17,000 events — not by a signature",
            ha="center", fontsize=9.5, color="#9CDCFE", zorder=3, style="italic")
    ax.text(5.68, 0.28, "Signature-based tools cannot detect a chain composed of legitimate actions",
            ha="center", fontsize=10.5, fontweight="bold", color=RED)
    save(fig, "diagram-kill-chain.png")


# ---------------------------------------------------------------- 6. defence in depth
def chart_defence_layers():
    fig, ax = plt.subplots(figsize=(10.6, 5.3))
    ax.set_xlim(0, 10.6); ax.set_ylim(0, 5.3); ax.axis("off")
    ax.text(0.1, 5.05, "Defence in depth — four layers, four failure modes",
            fontsize=15, fontweight="bold", color=INK)
    ax.text(0.1, 4.72, "Microsoft's model. Each layer fails differently; that is the point.",
            fontsize=10.5, color=GREY)

    layers = [("APPLICATION", "capabilities · permissions · escalation paths",
               "the only layer you fully control", TEAL, 3.55),
              ("SAFETY SYSTEM", "content filters · guardrails · observability",
               "probabilistic — will be bypassed", BLUE, 2.60),
              ("MODEL", "training · fine-tuning · refusal behaviour",
               "vendor-owned, changes without notice", VIOLET, 1.65),
              ("POSITIONING", "transparency · UX disclosure · user expectations",
               "shapes over-trust and reliance", AMBER, 0.70)]
    for name, mid, note, c, y in layers:
        ax.add_patch(FancyBboxPatch((0.15, y), 10.3, 0.82,
                                    boxstyle="round,pad=0.01,rounding_size=0.05",
                                    fc=LIGHT, ec=c, lw=1.7, zorder=2))
        ax.add_patch(Rectangle((0.15, y), 0.11, 0.82, fc=c, ec=c, zorder=3))
        ax.text(0.45, y + 0.52, name, fontsize=11.5, fontweight="bold", color=c, zorder=3)
        ax.text(0.45, y + 0.20, mid, fontsize=9.5, color=INK, zorder=3)
        ax.text(10.25, y + 0.41, note, fontsize=9, color=GREY, ha="right",
                style="italic", va="center", zorder=3)
    ax.text(10.25, 4.48, "highest leverage ↓", fontsize=9.5, color=TEAL,
            fontweight="bold", ha="right")
    save(fig, "diagram-defence-layers.png")


# ---------------------------------------------------------------- 7. framework stack
def chart_framework_stack():
    fig, ax = plt.subplots(figsize=(11, 5.3))
    ax.set_xlim(0, 11); ax.set_ylim(0, 5.3); ax.axis("off")
    ax.text(0.1, 5.05, "No single framework is sufficient", fontsize=15,
            fontweight="bold", color=INK)
    ax.text(0.1, 4.72, "Each answers a different question. Combine them deliberately.",
            fontsize=10.5, color=GREY)

    fws = [("OWASP LLM Top 10", "2026", "What can go wrong\nin a GenAI app?", "threat taxonomy", RED),
           ("OWASP ASI Top 10", "2026", "What can go wrong\nwith an agent?", "threat taxonomy", VIOLET),
           ("NIST AI RMF", "Govern·Map·Measure·Manage", "How do we run this\nas a process?", "lifecycle", BLUE),
           ("MITRE ATLAS", "adversary TTPs", "How do real attackers\noperate?", "red-team input", AMBER),
           ("IMDA Model AI Governance", "Agentic AI · Jan 2026", "Who is accountable\nfor the agent?", "governance", TEAL),
           ("PDPA + PDPC GenAI", "Singapore · Jul 2026", "What does the law\nrequire of us?", "statutory duty", INK)]
    for i, (name, ver, q, role, c) in enumerate(fws):
        col = i % 3; row = i // 3
        x = 0.15 + col * 3.62; y = 2.55 - row * 2.05
        ax.add_patch(FancyBboxPatch((x, y), 3.38, 1.78,
                                    boxstyle="round,pad=0.02,rounding_size=0.06",
                                    fc="white", ec=c, lw=1.8, zorder=2))
        ax.add_patch(Rectangle((x, y + 1.64), 3.38, 0.14, fc=c, ec=c, zorder=3))
        ax.text(x + 0.16, y + 1.36, name, fontsize=11, fontweight="bold", color=c, zorder=3)
        ax.text(x + 0.16, y + 1.10, ver, fontsize=8.5, color=GREY, zorder=3)
        ax.text(x + 0.16, y + 0.62, q, fontsize=9.5, color=INK, zorder=3, va="center")
        ax.text(x + 0.16, y + 0.16, role.upper(), fontsize=8.5, fontweight="bold",
                color=c, zorder=3)
    save(fig, "diagram-framework-stack.png")


# ---------------------------------------------------------------- 8. human in the loop
def chart_autonomy_gate():
    fig, ax = plt.subplots(figsize=(11, 4.9))
    ax.set_xlim(0, 11); ax.set_ylim(0, 4.9); ax.axis("off")
    ax.text(0.1, 4.65, "Calibrating autonomy — the deterministic gate",
            fontsize=15, fontweight="bold", color=INK)
    ax.text(0.1, 4.32, "IMDA: escalation triggers belong in code, never in the prompt",
            fontsize=10.5, color=GREY)

    bands = [("ALONE", "reversible · low impact\nfully logged", TEAL,
              "read a record · draft a reply"),
             ("WITH APPROVAL", "consequential · bounded\napproval bound to exact parameters", AMBER,
              "issue a refund · email a customer"),
             ("NEVER", "irreversible · rights-affecting\nor legally significant", RED,
              "delete data · report to a bureau")]
    for i, (n, cond, c, eg) in enumerate(bands):
        x = 0.15 + i * 3.62
        ax.add_patch(FancyBboxPatch((x, 1.30), 3.38, 2.72,
                                    boxstyle="round,pad=0.02,rounding_size=0.06",
                                    fc="white", ec=c, lw=2.0, zorder=2))
        ax.add_patch(Rectangle((x, 3.62), 3.38, 0.40, fc=c, ec=c, zorder=3))
        ax.text(x + 1.69, 3.82, n, ha="center", fontsize=12.5, fontweight="bold",
                color="white", zorder=4)
        ax.text(x + 1.69, 2.90, cond, ha="center", fontsize=10, color=INK, zorder=3)
        ax.add_patch(FancyBboxPatch((x + 0.18, 1.50), 3.02, 0.72,
                                    boxstyle="round,pad=0.01,rounding_size=0.04",
                                    fc=LIGHT, ec=LINE, lw=1.0, zorder=3))
        ax.text(x + 1.69, 1.86, eg, ha="center", fontsize=9.5, color=GREY,
                zorder=4, style="italic")

    ax.add_patch(FancyBboxPatch((0.15, 0.15), 10.7, 0.85,
                                boxstyle="round,pad=0.02,rounding_size=0.06",
                                fc=INK, ec=INK, zorder=2))
    ax.text(5.5, 0.72, "A prompt that says \"ask before deleting\" is not a control",
            ha="center", fontsize=11.5, fontweight="bold", color="white", zorder=3)
    ax.text(5.5, 0.38, "It is a request to a probabilistic system. The gate must be structural.",
            ha="center", fontsize=9.5, color="#9CDCFE", zorder=3, style="italic")
    save(fig, "diagram-autonomy-gate.png")


# ---------------------------------------------------------------- 9. assessment flow
def chart_assessment_flow():
    fig, ax = plt.subplots(figsize=(11.2, 3.0))
    ax.set_xlim(0, 11.2); ax.set_ylim(0, 3.0); ax.axis("off")
    steps = [("WRITTEN\nASSESSMENT", "5 SAQ · one per K", BLUE),
             ("CASE\nSTUDY", "3 questions · one per LO", VIOLET),
             ("MARKING", "against the answer key", AMBER),
             ("C / NYC", "competent or\nnot yet competent", TEAL),
             ("SIGN-OFF", "learner + assessor", INK)]
    for i, (n, sub, c) in enumerate(steps):
        x = 0.15 + i * 2.22
        ax.add_patch(FancyBboxPatch((x, 0.75), 1.95, 1.55,
                                    boxstyle="round,pad=0.02,rounding_size=0.06",
                                    fc="white", ec=c, lw=2.0, zorder=2))
        ax.add_patch(Rectangle((x, 2.16), 1.95, 0.14, fc=c, ec=c, zorder=3))
        ax.text(x + 0.975, 1.72, n, ha="center", fontsize=11, fontweight="bold",
                color=c, zorder=3)
        ax.text(x + 0.975, 1.10, sub, ha="center", fontsize=8.5, color=GREY, zorder=3)
        if i < 4:
            arrow(ax, x + 2.00, 1.52, x + 2.18, 1.52, color=GREY, lw=2.0)
    ax.text(5.6, 0.32, "Open book · Competent / Not Yet Competent · re-assessment available",
            ha="center", fontsize=10, color=GREY, style="italic")
    save(fig, "diagram-assessment-flow.png")


# ---------------------------------------------------------------- 10. incident stat
def chart_incident_landscape():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.2))
    fig.subplots_adjust(wspace=0.32)

    cats = ["Prompt\ninjection", "Data\nleakage", "Excessive\nagency", "Supply\nchain", "Memory\npoisoning"]
    vals = [34, 26, 18, 13, 9]
    cols = [RED, RED, VIOLET, AMBER, AMBER]
    b = ax1.bar(cats, vals, color=cols, width=0.62)
    ax1.set_title("Where agent incidents originate", fontsize=12, fontweight="bold",
                  color=INK, pad=12)
    ax1.set_ylabel("share of reported incidents (%)", fontsize=9.5, color=GREY)
    ax1.set_ylim(0, 42)
    for r, v in zip(b, vals):
        ax1.text(r.get_x() + r.get_width() / 2, v + 1.2, f"{v}%", ha="center",
                 fontsize=10, fontweight="bold", color=INK)
    ax1.spines[["top", "right"]].set_visible(False)
    ax1.spines[["left", "bottom"]].set_color(LINE)
    ax1.tick_params(labelsize=9, colors=GREY)

    labels = ["Deployed\nself-hosted\nagents", "No agent\ninventory", "No runtime\nmonitoring"]
    vals2 = [57, 62, 71]
    y = np.arange(len(labels))
    ax2.barh(y, vals2, color=[BLUE, AMBER, RED], height=0.55)
    ax2.set_yticks(y); ax2.set_yticklabels(labels, fontsize=9.5, color=INK)
    ax2.invert_yaxis()
    ax2.set_xlim(0, 100)
    ax2.set_title("The governance gap", fontsize=12, fontweight="bold", color=INK, pad=12)
    ax2.set_xlabel("% of organisations", fontsize=9.5, color=GREY)
    for i, v in enumerate(vals2):
        ax2.text(v + 2, i, f"{v}%", va="center", fontsize=10, fontweight="bold", color=INK)
    ax2.spines[["top", "right"]].set_visible(False)
    ax2.spines[["left", "bottom"]].set_color(LINE)
    ax2.tick_params(labelsize=9, colors=GREY)

    fig.suptitle("Agents are deployed faster than they are governed",
                 fontsize=14, fontweight="bold", color=INK, y=0.99)
    fig.tight_layout(rect=[0, 0, 1, 0.90])
    save(fig, "diagram-incident-landscape.png")


# ---------------------------------------------------------------- 11. PDPA roles
def chart_pdpa_roles():
    fig, ax = plt.subplots(figsize=(11, 4.6))
    ax.set_xlim(0, 11); ax.set_ylim(0, 4.6); ax.axis("off")
    ax.text(0.1, 4.35, "PDPA accountability in the AI value chain",
            fontsize=15, fontweight="bold", color=INK)
    ax.text(0.1, 4.02, "PDPC GenAI Guidelines, July 2026",
            fontsize=10.5, color=GREY)

    roles = [("MODEL PROVIDER", "trains the\nfoundation model", GREY, "shares duties"),
             ("SYSTEM PROVIDER", "builds the\napplication", BLUE, "shares duties"),
             ("SYSTEM DEPLOYER", "puts it in front\nof customers", RED, "PRIMARY RESPONSIBILITY")]
    for i, (n, sub, c, note) in enumerate(roles):
        x = 0.15 + i * 3.62
        lw = 2.6 if i == 2 else 1.7
        ax.add_patch(FancyBboxPatch((x, 1.95), 3.38, 1.72,
                                    boxstyle="round,pad=0.02,rounding_size=0.06",
                                    fc="white", ec=c, lw=lw, zorder=2))
        ax.add_patch(Rectangle((x, 3.53), 3.38, 0.14, fc=c, ec=c, zorder=3))
        ax.text(x + 1.69, 3.10, n, ha="center", fontsize=11.5, fontweight="bold",
                color=c, zorder=3)
        ax.text(x + 1.69, 2.50, sub, ha="center", fontsize=9.5, color=INK, zorder=3)
        ax.text(x + 1.69, 2.10, note, ha="center", fontsize=8.5, fontweight="bold",
                color=c, zorder=3)
        if i < 2:
            arrow(ax, x + 3.43, 2.80, x + 3.60, 2.80, color=GREY, lw=1.8)

    ax.add_patch(FancyBboxPatch((0.15, 0.72), 10.7, 1.00,
                                boxstyle="round,pad=0.02,rounding_size=0.06",
                                fc=LIGHT, ec=RED, lw=1.7, zorder=2))
    ax.text(5.5, 1.42, "New data surfaces you must now protect", ha="center",
            fontsize=11, fontweight="bold", color=RED, zorder=3)
    ax.text(5.5, 1.02, "end-user prompts  ·  generated outputs  ·  agent and tool activity data  ·  internal enterprise data",
            ha="center", fontsize=10, color=INK, zorder=3)
    ax.text(5.5, 0.32, "You cannot contract this away to the model vendor.",
            ha="center", fontsize=11, fontweight="bold", color=INK)
    save(fig, "diagram-pdpa-roles.png")


if __name__ == "__main__":
    print("Generating security diagrams…")
    chart_trust_boundary()
    chart_owasp_llm()
    chart_owasp_asi()
    chart_agent_anatomy()
    chart_kill_chain()
    chart_defence_layers()
    chart_framework_stack()
    chart_autonomy_gate()
    chart_assessment_flow()
    chart_incident_landscape()
    chart_pdpa_roles()
    print("Done →", OUT)
