"""Single source for TGS-2025060473 v5.0. LO, LU, topic, K and A wording is VERBATIM from the approved
Course Proposal (course_application/CP_IT_AI Ethnics_INT.xlsx). Never reword it."""

VERSION = "5.0"
VERSION_DATE = "7 November 2026"
TITLE = "AI Security for Autonomous AI Agents"
SHORT_TITLE = "AI Security for Autonomous AI Agents"
COURSE_CODE = "TGS-2025060473"
TSC_TITLE = "Generative AI Principles and Applications"
TSC_CODE = "ICT-INT-0052-1.1"
LEVEL = "Level 1"
ORG = "Tertiary Infotech Academy Pte Ltd"
UEN = "UEN: 201200696W"
TRAINER = "Dr Alfred Ang"
REPO_URL = "https://github.com/tertiarycourses/TGS-2025060473-AI-Security-for-Autonomous-AI-Agents"
PAGES_URL = "https://tertiarycourses.github.io/TGS-2025060473-AI-Security-for-Autonomous-AI-Agents/"
PROMPTS_URL = PAGES_URL + "prompts/index.html"
REG_URL = "https://www.tertiarycourses.com.sg/wsq-ai-security-for-autonomous-ai-agents.html"
LMS_URL = "https://lms-tms.tertiaryinfotech.com/"
DECK_NAME = f"WSQ - Master Trainer Slides - {COURSE_CODE} - {TITLE}-v50"
LG_NAME = f"Learner Guide - {COURSE_CODE} - {TITLE}"
LP_NAME = f"Lesson Plan - {COURSE_CODE} - {TITLE}"
SCENARIO = "Kopi Kaki Co., a fictional Singapore kopi startup"

KNOWLEDGE = [
    ("K1", "Importance of data quality, preprocessing, model pipeline and model training (e.g., impact of data bias from training data)"),
    ("K2", "Underlying principles, core concepts and theories governing generative AI"),
    ("K3", "Difference between generative and discriminative models"),
    ("K4", "Impact of prompt engineering on the model outputs of generative AI"),
    ("K5", "Generative AI model workings, including training data, algorithms, and outputs"),
]
ABILITIES = [
    ("A1", "Analyse limitations and potential biases in AI-generated content"),
    ("A2", "Identify the ethical implications and societal impact of AI-generated content"),
    ("A3", "Apply understanding of generative AI principles to use cases"),
    ("A4", "Demonstrate the use of generation AI in diverse applications (e.g., summarisation, inference, reasoning, transformation of content, augmentation of content)"),
    ("A5", "Analyse generative AI models' performance metrics and evaluate the influence of prompt variations"),
]
LEARNING_OUTCOMES = [
    ("LO1", "Demonstrate generative AI concepts and applications relevant to customer service and hospitality management."),
    ("LO2", "Apply prompt engineering techniques and analyse output variations to improve generative AI performance in service settings."),
    ("LO3", "Identify ethical risks and analyse bias in AI-generated content used in customer engagement."),
]
# CP: LU, LO, CP topics verbatim, K/A, methods in minutes, assessment minutes.
LUS = [
    dict(lu="LU1", title="Generative AI Fundamentals", lo="LO1", codes=["K2", "K3", "A4"], minutes=120,
         methods={"Interactive presentation": 60, "Peer teaching / Peer practice": 30, "Case studies": 30},
         cp_topics=["T1: Underlying principles, core concepts and theories governing generative AI",
                    "T2: Difference between generative and discriminative models",
                    "T3: Demonstrate the use of generation AI in diverse applications (e.g., summarisation, inference, reasoning, transformation of content, augmentation of content)"],
         delivered="Topic 1: Human-AI Collaboration and Always-On AI Agents"),
    dict(lu="LU2", title="Prompt Engineering", lo="LO2", codes=["K1", "K4", "A3", "A5"], minutes=120,
         methods={"Interactive presentation": 60, "Peer teaching / Peer practice": 30, "Case studies": 30},
         cp_topics=["T1: Importance of data quality, preprocessing, model pipeline and model training (e.g., impact of data bias from training data)",
                    "T2: Impact of prompt engineering on the model outputs of generative AI",
                    "T3: Apply understanding of generative AI principles to use cases",
                    "T4: Analyse generative AI models' performance metrics and evaluate the influence of prompt variations"],
         delivered="Topic 2: AI Agent Vulnerabilities"),
    dict(lu="LU3", title="Ethical Considerations", lo="LO3", codes=["K5", "A1", "A2"], minutes=180,
         methods={"Interactive presentation": 100, "Peer teaching / Peer practice": 40, "Case studies": 40},
         cp_topics=["T1: Generative AI model workings, including training data, algorithms, and outputs",
                    "T2: Identify the ethical implications and societal impact of AI-generated content",
                    "T3: Analyse limitations and potential biases in AI-generated content"],
         delivered="Topic 3: AI Governance and Security"),
]
TOPICS = [
    dict(num=1, title="Human-AI Collaboration and Always-On AI Agents", lu="LU1",
         items=["AI history, 1960 to 2026", "Agentic AI versus AI agents", "OpenClaw, Hermes, always-on agents", "Use cases and five collaboration scenarios", "Five always-on agents compared", "Lab 1: your always-on CEO assistant"]),
    dict(num=2, title="AI Agent Vulnerabilities", lu="LU2",
         items=["Prompt engineering and data quality", "Prompt injection, Lab 2", "Jailbreak, Lab 3", "Data leak and the PDPA, Lab 4"]),
    dict(num=3, title="AI Governance and Security", lu="LU3",
         items=["How models work, limits, bias, ethics", "The five principles of AI security", "Lab 5: AI Governance Policy", "Incident response, Lab 6: AI Incident Report"]),
]
ASSESS = dict(wa="Written Assessment (SAQ)", wa_min=30, cs="Case Study", cs_min=30, total=60)

# (start, end, minutes, kind, text, LU, method, slide-map start key, slide-map end key)
SCHEDULE = [
    ("9:00", "9:10", 10, "admin", "Welcome, digital attendance, trainer, ground rules, Learning Outcomes, LMS and assessment briefing", "LU1", "Interactive presentation", "admin", "t1"),
    ("9:10", "9:50", 40, "topic", "Topic 1: From rules to learning to action; four engineering lenses 2023 to 2026; agentic AI versus AI agents; how an agent works like a person; the agentic loop; how generative AI writes; generative versus discriminative models; AI does the work, humans decide", "LU1", "Interactive presentation", "t1", "t1cases"),
    ("9:50", "10:20", 30, "topic", "Topic 1: Five Human-AI collaboration scenarios; use cases; AI for science; OpenClaw to Hermes to hosted always-on agents; the Big Five always-on agents compared", "LU1", "Case studies", "t1cases", "lab1"),
    ("10:20", "10:30", 10, "break", "Tea break", "LU1", "-", None, None),
    ("10:30", "11:00", 30, "lab", "Lab 1: Your always-on CEO assistant. Screenshot for Case Study Q1", "LU1", "Peer teaching / Peer practice", "lab1", "t2"),
    ("11:00", "11:30", 30, "topic", "Topic 2: Prompt engineering and data quality; definition and examples of prompt injection; why a model cannot tell a genuine prompt from a malicious one; consequences", "LU2", "Interactive presentation", "t2", "lab2"),
    ("11:30", "12:00", 30, "lab", "Lab 2: Install Hermes Desktop on a free model, simulate prompt injection, fix it. Screenshots for Case Study Q2", "LU2", "Case studies", "lab2", "t2jb"),
    ("12:00", "12:15", 15, "topic", "Topic 2: Definition and examples of jailbreak; techniques; what stronger models and guardrails change", "LU2", "Interactive presentation", "t2jb", "lab3"),
    ("12:15", "12:30", 15, "lab", "Lab 3: Simulate a jailbreak, fix it. Screenshots for Case Study Q2", "LU2", "Peer teaching / Peer practice", "lab3", "t2leak"),
    ("12:30", "1:30", 60, "lunch", "Lunch", None, "-", None, None),
    ("1:30", "1:45", 15, "topic", "Topic 2: Definition and examples of data leak; personal data and the PDPA", "LU2", "Interactive presentation", "t2leak", "lab4"),
    ("1:45", "2:00", 15, "lab", "Lab 4: Simulate a data leak, fix it. Screenshots for Case Study Q2", "LU2", "Peer teaching / Peer practice", "lab4", "t3"),
    ("2:00", "3:10", 70, "topic", "Topic 3: How a model works; limits, bias and ethics; the five principles of AI security explained, with examples", "LU3", "Interactive presentation", "t3", "t3tea"),
    ("3:10", "3:20", 10, "break", "Tea break", "LU3", "-", None, None),
    ("3:20", "3:30", 10, "topic", "Topic 3: The frameworks behind the five principles: IMDA, NIST, OWASP, ISO, PDPA", "LU3", "Interactive presentation", "t3tea", "lab5"),
    ("3:30", "4:10", 40, "lab", "Lab 5: Create an AI Governance Policy from an interview prompt. Screenshot for Case Study Q3", "LU3", "Peer teaching / Peer practice", "lab5", "t3inc"),
    ("4:10", "4:20", 10, "topic", "Topic 3: Incident response under the PDPA: Contain, Assess, Report, Evaluate", "LU3", "Interactive presentation", "t3inc", "lab6"),
    ("4:20", "5:00", 40, "lab", "Lab 6: Create an AI Incident Report from mock agent traces. Screenshot for Case Study Q3", "LU3", "Case studies", "lab6", "wrap"),
    ("5:00", "5:30", 30, "assess", "Written Assessment (SAQ): 5 questions, K1 to K5", "ASSESS", "Written Exam", "wrap", "end"),
    ("5:30", "6:00", 30, "assess", "Case Study: Q1 to Q3, paste your lab screenshots as your answers, A1 to A5", "ASSESS", "Case Study", "wrap", "end"),
]
for _lu in LUS:
    _m = sum(r[2] for r in SCHEDULE if r[5] == _lu["lu"])
    assert _m == _lu["minutes"], (_lu["lu"], _m)
assert sum(r[2] for r in SCHEDULE if r[5] == "ASSESS") == 60

VERSION_ROW = ("5.0", VERSION_DATE, "Full overhaul. Deck redesigned in the Agentic AI Applications with Claude Code theme. Topic 1 and Lab 1 reuse the Human-AI Workforce with Autonomous AI Agents course slides, with this course's code, plus K2, K3 and A4 slides. Topic 2: prompt injection, jailbreak and data leak. Topic 3: the five principles of AI security, governance and incident response. Six labs replace the eight activities, each in its own folder with mock data, scripts and a PDF of prompt instructions, plus a copy-prompt web page. Case Study rewritten as Q1 to Q3 with lab screenshots as answers. Written Assessment questions unchanged; duration aligned to the approved Course Proposal (30 + 30 minutes).", TRAINER)
