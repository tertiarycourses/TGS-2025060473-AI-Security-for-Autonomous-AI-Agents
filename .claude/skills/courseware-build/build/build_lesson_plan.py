#!/usr/bin/env python3
"""Lesson Plan from course_data.SCHEDULE and the deck's slide_map.json. CP minutes per LU and per method are asserted."""
import json, os, sys
from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.table import WD_TABLE_ALIGNMENT
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import course_data as C
from data_labs import LABS
import prodoc
from version_history import PRIOR
def _repo():
    d = HERE
    for _ in range(8):
        d = os.path.dirname(d)
        if os.path.isdir(os.path.join(d, "courseware")) and os.path.isdir(os.path.join(d, "labs")): return d
REPO = _repo(); ASSETS = os.path.join(os.path.dirname(HERE), "assets")
MAP = json.load(open(os.path.join(HERE, "slide_map.json")))
def rng(a, b):
    if a is None: return "-"
    return str(MAP[a]) if MAP[b] - 1 == MAP[a] else f"{MAP[a]}–{MAP[b] - 1}"
def H24(t):
    h, mi = t.split(":"); h = int(h)
    return f"{h + 12 if h < 9 else h}:{mi}"
HEAD = "21201C"; FILL = {"topic": "FFFFFF", "admin": "F3F1EB", "lab": "F6E7DF", "break": "EFECE4", "lunch": "EFECE4", "assess": "DCEBE9"}
doc = Document(); normal = doc.styles["Normal"]; normal.font.name = "Arial"; normal.font.size = Pt(11)
prodoc.style_headings(doc)
prodoc.add_cover_page(doc, "LESSON PLAN", C.TITLE, C.VERSION, org_logo=os.path.join(ASSETS, "tertiary-infotech-logo.png"), course_code=C.COURSE_CODE)
prodoc.add_version_control(doc, PRIOR + [C.VERSION_ROW]); prodoc.add_toc(doc)
H = lambda t, l=1: doc.add_heading(t, level=l)
def cell(c, t, bold=False, size=9.5, color=None, fill=None):
    c.text = ""; r = c.paragraphs[0].add_run(str(t)); r.bold = bold; r.font.size = Pt(size); r.font.name = "Arial"
    if color: r.font.color.rgb = color
    if fill: prodoc._shade_cell(c, fill)
def table(head, rows, widths, fills=None):
    t = doc.add_table(rows=0, cols=len(head)); t.style = "Table Grid"; t.alignment = WD_TABLE_ALIGNMENT.CENTER
    h = t.add_row().cells
    for i, x in enumerate(head): cell(h[i], x, True, 9.5, RGBColor(255, 255, 255), HEAD)
    for n, r in enumerate(rows):
        c = t.add_row().cells
        for i, x in enumerate(r): cell(c[i], x, fill=(fills[n] if fills else None))
    prodoc.set_widths(t, widths); return t

H("Course Information")
table(["Item", "Detail"], [["Course Title", C.TITLE], ["WSQ Course Reference", C.COURSE_CODE], ["TSC", f"{C.TSC_TITLE} ({C.TSC_CODE}), {C.LEVEL}"], ["Training Provider", f"{C.ORG} ({C.UEN})"],
    ["Duration", "1 day, 8 hours: 7 hours of instruction including tea, plus 1 hour of assessment"], ["Daily Timing", "9:00 am to 6:00 pm, with a 1-hour lunch that is not counted"], ["Mode", "Classroom Facilitated Training. Learners bring a laptop"],
    ["Course scenario", C.SCENARIO + ". All lab data is fictional"], ["Slide deck", f"{C.DECK_NAME}.pptx ({MAP['end'] - 1} slides)"], ["Trainer", C.TRAINER]], [1.9, 4.9])
H("Learning Outcomes")
for lo, t in C.LEARNING_OUTCOMES: doc.add_paragraph(style="List Bullet").add_run(f"{lo}: {t}")
H("Knowledge and Ability Statements")
table(["Code", "Statement"], [[a, b] for a, b in C.KNOWLEDGE + C.ABILITIES], [0.7, 6.1])
H("Learning Units (approved Course Proposal)")
rows = []
for u in C.LUS:
    m = sum(r[2] for r in C.SCHEDULE if r[5] == u["lu"]); assert m == u["minutes"]
    rows.append([f"{u['lu']}: {u['title']}", f"{u['lo']}: " + dict(C.LEARNING_OUTCOMES)[u["lo"]], "\n".join(u["cp_topics"]), ", ".join(u["codes"]), u["delivered"], f"{u['minutes']} min"])
rows.append(["Assessment", "All", f"{C.ASSESS['wa']} ({C.ASSESS['wa_min']} min) and {C.ASSESS['cs']} ({C.ASSESS['cs_min']} min)", "K1–K5, A1–A5", "5:00 pm to 6:00 pm", "60 min"])
table(["LU", "Learning Outcome", "Course Proposal topics", "K & A", "Delivered through", "Allocated"], rows, [0.95, 1.4, 2.05, 0.6, 0.95, 0.85])
H("Reconciliation to the Course Proposal")
rows = []
for u in C.LUS:
    for meth, want in u["methods"].items():
        got = sum(r[2] for r in C.SCHEDULE if r[5] == u["lu"] and (r[6] == meth or (r[6] == "-" and meth == "Interactive presentation")))
        assert got == want, (u["lu"], meth, got, want)
        rows.append([u["lu"], meth, f"{want} min", f"{got} min", "Yes"])
for n, m in (("Written Exam", C.ASSESS["wa_min"]), ("Case Study", C.ASSESS["cs_min"])): rows.append(["Assessment", n, f"{m} min", f"{m} min", "Yes"])
table(["LU", "Method", "CP minutes", "Scheduled", "Match"], rows, [1.0, 3.0, 1.0, 1.0, 0.8])
p = doc.add_paragraph(); r = p.add_run("Tea breaks sit inside the presentation time of the LU they fall in. Lunch (60 minutes) is not counted. Total: 420 minutes of instruction plus 60 minutes of assessment."); r.italic = True; r.font.size = Pt(9.5)
H("Course Schedule")
rows = []; fills = []
for s, e, m, k, tx, lu, meth, a, b in C.SCHEDULE:
    rows.append([f"{H24(s)}–{H24(e)}", f"{m} min", tx, "Assess" if lu == "ASSESS" else (lu or "-"), meth, rng(a, b)]); fills.append(FILL[k])
table(["Time", "Duration", "Topic / Activity", "LU", "Method", "Slides"], rows, [1.0, 0.75, 2.7, 0.55, 1.1, 0.7], fills)
H("Lab Reference")
next_key = {1: ("lab1", "t2"), 2: ("lab2", "t2jb"), 3: ("lab3", "t2leak"), 4: ("lab4", "t3"), 5: ("lab5", "t3inc"), 6: ("lab6", "wrap")}
table(["Lab", "Title", "Allocated", "LO, Ability", "Evidence for", "Slides"], [[L["label"], L["title"], f"{L['minutes']} min", f"{L['lo']}, {L['codes']}", L["shot"], rng(*next_key[L["num"]])] for L in LABS], [0.55, 2.7, 0.8, 0.95, 1.1, 0.7])
doc.add_paragraph(); doc.add_paragraph("Lab materials: one folder per lab under labs/, holding LAB-0N-Instructions.pdf, data/ and scripts/. Prompts can be copied from prompts/index.html, also published at " + C.PROMPTS_URL + ".").runs[0].font.size = Pt(10)
H("Resources")
for t in ["Learner laptop (Mac on Apple Silicon, or Windows) with Hermes Desktop", "Free Nous Portal account; a ChatGPT plan for the stronger model where available; Meta Muse account", "Training Google account seeded with the Lab 1 mock meetings and emails, prepared by the trainer", "Slide deck, Learner Guide, lab PDFs and the copy-prompt page"]:
    doc.add_paragraph(style="List Bullet").add_run(t)
prodoc.add_page_numbers(doc); prodoc.enable_update_fields(doc)
doc.core_properties.title = C.TITLE + " Lesson Plan"; doc.core_properties.author = C.ORG
OUT = os.path.join(REPO, "courseware", C.LP_NAME + ".docx"); doc.save(OUT); print("saved", OUT)
