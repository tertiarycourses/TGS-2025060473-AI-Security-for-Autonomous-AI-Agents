#!/usr/bin/env python3
"""WSQ Lesson Plan — AI Security for Autonomous AI Agents (TGS-2025060473).

2 days × 8 instructional hours. 9:30am–6:30pm with a 1-hour lunch; tea breaks
counted within the day. Asserts 480 min/day before saving.
"""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SKILL = os.path.join(HERE, "..", ".claude", "skills", "tertiary-lesson-plan")
sys.path.insert(0, os.path.abspath(SKILL))
sys.path.insert(0, HERE)

import prodoc
# This course is delivered by Tertiary Infotech Pte Ltd (UEN 20120096W) — not the
# Academy entity hardcoded in the shared helper. Override before use.
prodoc.ORG = "Tertiary Infotech Pte Ltd"
prodoc.UEN = "UEN: 20120096W"
prodoc.COPYRIGHT = ("This material belongs to Tertiary Infotech Pte Ltd (UEN: 20120096W). "
                    "All Rights Reserved.")

from prodoc import (add_cover_page, add_version_control, add_toc, add_page_numbers,
                    enable_update_fields, style_headings, _shade_cell)
from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
import course_data as C

BRAND = RGBColor(0x1F, 0x6F, 0xEB); DARK = RGBColor(0x11, 0x18, 0x27)
GREY = RGBColor(0x55, 0x5B, 0x66)
ASSETS = os.path.join(HERE, "assets")

VERSIONS = [
    ("1.0", "16 June 2025", "Initial release — Core Principles and Ethical Challenges in "
                            "Generative AI.", "Dr Alfred Ang"),
    ("2.0", C.VERSION_DATE, "Course revised and retitled to AI Security for Autonomous AI "
                            "Agents. Content rebuilt around AI security for generative AI and "
                            "autonomous agents (OWASP LLM Top 10 2026, OWASP ASI Top 10 2026, "
                            "NIST AI RMF, MITRE ATLAS, IMDA Model AI Governance for Agentic AI, "
                            "PDPA/PDPC). Five real-world case-study activities added. "
                            "Assessment restructured: Written Assessment (one question per K) "
                            "and Case Study (one question per LO). Accredited TSC K/A statements "
                            "unchanged.", "Dr Alfred Ang"),
]

# (time, topic, minutes, kind)  kind: topic | activity | break | admin | assess
DAY1 = [
    ("9:30 – 9:45", "Welcome, digital attendance (AM), introductions and ground rules", 15, "admin"),
    ("9:45 – 10:00", "Course overview, learning outcomes and assessment briefing", 15, "admin"),
    ("10:00 – 10:45", "LU1 T1: The AI security threat landscape — why generative AI breaks "
                      "classical security assumptions (K2)", 45, "topic"),
    ("10:45 – 11:00", "Tea break", 15, "break"),
    ("11:00 – 11:45", "LU1 T1 (cont.): The context window has no trust boundary; prompt "
                      "injection as an architectural property (K2)", 45, "topic"),
    ("11:45 – 12:30", "LU1 T2: Generative vs discriminative models — the guardrail classifier "
                      "pattern and its limits (K3)", 45, "topic"),
    ("12:30 – 1:30", "Lunch break", 60, "lunch"),
    ("1:30 – 2:15", "LU1 T3: Application modes as attack surfaces — summarisation, inference, "
                    "reasoning, transformation, augmentation (A4)", 45, "topic"),
    ("2:15 – 3:00", "Activity 1: Threat Modelling a Generative AI Concierge (K2, K3, A4)", 45, "activity"),
    ("3:00 – 3:45", "LU2 T1: Data quality, preprocessing and the model pipeline — poisoning "
                    "across training, RAG, memory and artifacts (K1)", 45, "topic"),
    ("3:45 – 4:00", "Tea break", 15, "break"),
    ("4:00 – 4:45", "LU2 T2: Prompt injection in depth — direct, indirect and cross-modal; "
                    "why prompt-based defences fail (K4)", 45, "topic"),
    ("4:45 – 5:45", "Activity 2: Prompt Injection and the PDPA-Reportable Leak (K4, K1)", 60, "activity"),
    ("5:45 – 6:15", "Activity 2 debrief — notification decision and prioritised controls", 30, "activity"),
    ("6:15 – 6:30", "Day 1 recap, Q&A and PM digital attendance", 15, "admin"),
]

DAY2 = [
    ("9:30 – 9:40", "Day 1 recap and AM digital attendance", 10, "admin"),
    ("9:40 – 10:25", "LU2 T3: Security frameworks for generative AI and agents — OWASP LLM "
                     "Top 10 2026, OWASP ASI Top 10 2026, NIST AI RMF, MITRE ATLAS, IMDA and "
                     "the PDPA (A3)", 45, "topic"),
    ("10:25 – 11:00", "LU2 T4: Measuring whether a guardrail works — attack success rate, "
                      "refusal rate, false-positive rate across prompt variants (A5)", 35, "topic"),
    ("11:00 – 11:15", "Tea break", 15, "break"),
    ("11:15 – 12:15", "Activity 3: Selecting a Security Framework for GenAI and Agents (A3, A5)", 60, "activity"),
    ("12:15 – 12:45", "LU3 T1: Agent anatomy — model, loop, tools, memory, identity. Excessive "
                      "agency, uncontrolled and destructive execution (K5)", 30, "topic"),
    ("12:45 – 1:45", "Lunch break", 60, "lunch"),
    ("1:45 – 2:00", "LU3 T1 (cont.): Defence in depth and the four-layer control stack (K5)", 15, "topic"),
    ("2:00 – 3:00", "Activity 4: Rogue Agent Post-Incident Review — the real 2026 incidents (K5)", 60, "activity"),
    ("3:00 – 3:30", "LU3 T2: Ethical implications and societal impact — PDPA, PDPC GenAI "
                    "guidelines and the IMDA Model AI Governance Framework for Agentic AI (A2)", 30, "topic"),
    ("3:30 – 3:45", "Tea break", 15, "break"),
    ("3:45 – 4:05", "LU3 T3: Limitations and bias — misinformation as a security risk, "
                    "aggregate accuracy and disparate impact (A1)", 20, "topic"),
    ("4:05 – 4:30", "Activity 5: Agent Governance and the Deployment Gate — capstone (A1, A2)", 25, "activity"),
    ("4:30 – 4:40", "Course synthesis, Q&A and briefing for assessment", 10, "admin"),
    ("4:40 – 5:40", "Assessment 1: Written Assessment (SAQ) — 5 questions · 40 marks · 60 min", 60, "assess"),
    ("5:40 – 6:20", "Assessment 2: Case Study — 3 questions · 70 marks · 40 min", 40, "assess"),
    ("6:20 – 6:30", "Assessment digital attendance · TRAQOM survey · course close", 10, "assess"),
]

SHADE = {"topic": "E8F0FE", "activity": "E6F7F1", "break": "FDF3E3", "lunch": "FDF3E3",
         "admin": "F2F4F7", "assess": "FDECEC"}


def h1(doc, t):
    p = doc.add_heading(t, level=1); return p


def h2(doc, t):
    return doc.add_heading(t, level=2)


def para(doc, t, size=11, bold=False, color=DARK, after=6):
    p = doc.add_paragraph(); r = p.add_run(t)
    r.font.size = Pt(size); r.font.bold = bold; r.font.color.rgb = color
    r.font.name = "Arial"
    p.paragraph_format.space_after = Pt(after)
    return p


def table(doc, headers, rows, widths=None, shades=None):
    t = doc.add_table(rows=1, cols=len(headers)); t.style = "Table Grid"
    for j, htxt in enumerate(headers):
        c = t.rows[0].cells[j]; c.text = ""
        r = c.paragraphs[0].add_run(htxt)
        r.font.bold = True; r.font.size = Pt(10); r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        r.font.name = "Arial"
        _shade_cell(c, "1F6FEB")
    for i, row in enumerate(rows):
        cells = t.add_row().cells
        for j, val in enumerate(row):
            cells[j].text = ""
            r = cells[j].paragraphs[0].add_run(str(val))
            r.font.size = Pt(9.5); r.font.name = "Arial"
            r.font.bold = (j == 0 and shades is None)
        if shades:
            for c in cells:
                _shade_cell(c, shades[i])
    if widths:
        for j, w in enumerate(widths):
            for row in t.rows:
                row.cells[j].width = Inches(w)
    return t


def day_table(doc, day):
    rows = [(tm, tp, f"{mn} min") for tm, tp, mn, _ in day]
    shades = [SHADE[k] for _, _, _, k in day]
    table(doc, ["Time", "Topic / Activity", "Duration"], rows,
          widths=[1.15, 5.15, 0.85], shades=shades)
    total = sum(mn for _, _, mn, k in day if k not in ("lunch",))
    return total


def build():
    doc = Document()
    style_headings(doc)
    st = doc.styles["Normal"]; st.font.name = "Arial"; st.font.size = Pt(11)

    add_cover_page(doc, "LESSON PLAN", C.TITLE, C.VERSION,
                   conducted_by="Tertiary Infotech Pte Ltd",
                   org_logo=os.path.join(ASSETS, "tertiary-infotech-logo.png"),
                   course_logo=None, course_code=C.COURSE_CODE)

    h1(doc, "Document Version Control Record")
    add_version_control(doc, VERSIONS)

    h1(doc, "Table of Contents")
    add_toc(doc)

    # ---- overview  (add_toc already ends the page; a second break renders blank)
    h1(doc, "1. Course Overview")
    para(doc, f"{C.TITLE} is a {C.DURATION} WSQ course that equips learners to identify, "
              "analyse and mitigate the security risks introduced by generative AI systems and "
              "by autonomous AI agents. The course is delivered through real-world case studies "
              "drawn from 2026 incidents and is grounded in the current security and governance "
              "frameworks, including the OWASP Top 10 for LLM Applications (2026), the OWASP Top "
              "10 for Agentic Applications (2026), the NIST AI Risk Management Framework, MITRE "
              "ATLAS, the IMDA Model AI Governance Framework for Agentic AI, and Singapore's "
              "PDPA together with the PDPC guidelines on personal data in generative AI.")
    para(doc, "The course covers AI security for BOTH generative AI (prompt injection, data "
              "leakage, poisoning, PDPA exposure) and autonomous agents (uncontrolled and "
              "destructive execution, tool misuse, agent vulnerabilities and cyber-attack "
              "chains).")

    h2(doc, "Skills Framework Alignment")
    table(doc, ["Element", "Detail"],
          [["TSC Title", C.TSC_TITLE],
           ["TSC Code", C.TSC_CODE],
           ["Proficiency Level", C.PROFICIENCY],
           ["Course Code", C.COURSE_CODE],
           ["Duration", C.DURATION],
           ["Delivery", "Instructor-led classroom with facilitated case-study activities"]],
          widths=[1.9, 5.25])
    para(doc, "")
    para(doc, "Note: the accredited knowledge and ability statements below are reproduced "
              "verbatim. They are taught and assessed as accredited; AI security is the "
              "delivery context through which each statement is evidenced.", size=9.5,
         color=GREY)

    h2(doc, "Learning Outcomes")
    table(doc, ["LO", "Learning Outcome"],
          [[c, d] for c, d in C.LEARNING_OUTCOMES], widths=[0.7, 6.45])

    h2(doc, "Knowledge Statements (assessed by the Written Assessment)")
    table(doc, ["Code", "Knowledge statement"],
          [[c, d] for c, d in C.TSC_KNOWLEDGE], widths=[0.7, 6.45])

    h2(doc, "Ability Statements (assessed by the Case Study)")
    table(doc, ["Code", "Ability statement"],
          [[c, d] for c, d in C.TSC_ABILITIES], widths=[0.7, 6.45])

    doc.add_page_break()

    # ---- schedule
    h1(doc, "2. Daily Schedule")
    para(doc, "Each training day runs 9:30am – 6:30pm and delivers 8 instructional hours. "
              "A 1-hour lunch break is excluded from instructional time; short tea breaks are "
              "counted within the day.", size=10, color=GREY)

    h2(doc, "Day 1 — Generative AI Security")
    para(doc, "Slides 1–30 of the trainer deck.", size=9.5, color=GREY)
    t1 = day_table(doc, DAY1)
    para(doc, "")
    para(doc, f"Day 1 instructional total: {t1} minutes ({t1/60:.0f} hours), excluding the "
              "1-hour lunch break.", size=10, bold=True)

    h2(doc, "Day 2 — Autonomous Agent Security")
    para(doc, "Slides 31–64 of the trainer deck.", size=9.5, color=GREY)
    t2 = day_table(doc, DAY2)
    para(doc, "")
    para(doc, f"Day 2 instructional total: {t2} minutes ({t2/60:.0f} hours), excluding the "
              "1-hour lunch break.", size=10, bold=True)

    doc.add_page_break()

    # ---- activities
    h1(doc, "3. Activities")
    para(doc, "Every activity is a real-world case study. Each has its own folder under "
              "activities/ containing the scenario, the discussion questions, the trainer "
              "debrief and a printable PDF. Full step-by-step facilitation detail is in the "
              "Learner Guide.")
    table(doc, ["#", "Activity", "Day", "Duration", "K/A assessed"],
          [["1", "Threat Modelling a Generative AI Concierge", "1", "45 min", "K2, K3, A4"],
           ["2", "Prompt Injection and the PDPA-Reportable Leak", "1", "60 min", "K4, K1"],
           ["3", "Selecting a Security Framework for GenAI and Agents", "2", "60 min", "A3, A5"],
           ["4", "Rogue Agent Post-Incident Review", "2", "60 min", "K5"],
           ["5", "Agent Governance and the Deployment Gate (capstone)", "2", "25 min", "A1, A2"]],
          widths=[0.4, 3.6, 0.5, 0.9, 1.75])

    h1(doc, "4. Tools and Resources")
    table(doc, ["Resource", "Purpose"],
          [["Trainer slide deck (PPTX/PDF)", "Facilitation, diagrams and case-study prompts"],
           ["Learner Guide", "Detailed step-by-step notes and activity walkthroughs"],
           ["Activity packs (activities/)", "Scenario, discussion questions and debrief per activity"],
           ["LMS/TMS portal", "lms-tms.tertiaryinfotech.com — course material and submission"],
           ["Whiteboard / flip chart", "Group threat modelling and kill-chain reconstruction"],
           ["OWASP LLM & ASI Top 10 (2026)", "Reference taxonomies used throughout"],
           ["IMDA / PDPC publications", "Singapore governance and data-protection reference"]],
          widths=[2.5, 4.65])

    h1(doc, "5. Assessment")
    para(doc, "Assessment is conducted at the end of Day 2. The briefing for assessment is "
              "delivered before the assessment begins.")
    table(doc, ["Instrument", "Covers", "Detail"],
          [["Written Assessment (SAQ)", "K1 – K5", C.ASSESSMENT["wa"]],
           ["Case Study", "A1 – A5 via LO1 – LO3", C.ASSESSMENT["cs"]],
           ["Format", "—", C.ASSESSMENT["format"]],
           ["Grading", "—", C.ASSESSMENT["grading"]],
           ["Re-assessment", "—", "Available for learners assessed Not Yet Competent"]],
          widths=[1.75, 1.35, 4.05])
    para(doc, "")
    para(doc, "Funding eligibility requires a minimum 75% attendance recorded through SSG "
              "digital attendance, an assessment outcome of Competent, and completion of the "
              "TRAQOM survey.", size=10)

    add_page_numbers(doc)
    enable_update_fields(doc)

    assert t1 == 480, f"Day 1 is {t1} min, expected 480"
    assert t2 == 480, f"Day 2 is {t2} min, expected 480"

    out = os.path.join(HERE, f"Lesson Plan - {C.COURSE_CODE} - {C.TITLE}.docx")
    doc.save(out)
    print(f"Saved: {out}")
    print(f"Day 1 = {t1} min · Day 2 = {t2} min")


if __name__ == "__main__":
    build()
