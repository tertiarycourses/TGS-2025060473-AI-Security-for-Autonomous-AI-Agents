#!/usr/bin/env python3
"""Single source of truth for the AI Security for Autonomous AI Agents courseware.

Course code TGS-2025060473 · TSC ICT-INT-0052-1.1.

DESIGN NOTE (important for anyone editing this file):
The accredited TSC K/A statements are Generative-AI-principles statements. They are taught
and assessed VERBATIM — AI security is the delivery LENS, not a replacement for them.
Never reword a K or A statement. See research/CONTENT-DESIGN.md.
"""

VERSION = "4.14"
VERSION_DATE = "26 August 2026"

TITLE = "AI Security for Autonomous AI Agents"
SHORT_TITLE = "AI Security for Autonomous AI Agents"
COURSE_CODE = "TGS-2025060473"
TSC_TITLE = "Generative AI Principles and Applications"
TSC_CODE = "ICT-INT-0052-1.1"
PROFICIENCY = "Level 1"
TRAINER = "Dr Alfred Ang"
DURATION = "1 Day · 8 Hours"

# ---------------------------------------------------------------- accredited K & A
# VERBATIM from the Course Proposal. Do not edit the text.
TSC_KNOWLEDGE = [
    ("K1", "Importance of data quality, preprocessing, model pipeline and model training "
           "(e.g., impact of data bias from training data)"),
    ("K2", "Underlying principles, core concepts and theories governing generative AI"),
    ("K3", "Difference between generative and discriminative models"),
    ("K4", "Impact of prompt engineering on the model outputs of generative AI"),
    ("K5", "Generative AI model workings, including training data, algorithms, and outputs"),
]

TSC_ABILITIES = [
    ("A1", "Analyse limitations and potential biases in AI-generated content"),
    ("A2", "Identify the ethical implications and societal impact of AI-generated content"),
    ("A3", "Apply understanding of generative AI principles to use cases"),
    ("A4", "Demonstrate the use of generation AI in diverse applications (e.g., summarisation, "
           "inference, reasoning, transformation of content, augmentation of content)"),
    ("A5", "Analyse generative AI models' performance metrics and evaluate the influence of "
           "prompt variations"),
]

# ---------------------------------------------------------------- LO / LU
LEARNING_OUTCOMES = [
    ("LO1", "Demonstrate generative AI concepts and applications relevant to customer service "
            "and hospitality management."),
    ("LO2", "Apply prompt engineering techniques and analyse output variations to improve "
            "generative AI performance in service settings."),
    ("LO3", "Identify ethical risks and analyse bias in AI-generated content used in customer "
            "engagement."),
]

# The three delivered topics, mapped one-to-one onto the learning outcomes.
LEARNING_UNITS = [
    ("Topic 1", "Generative AI, Agentic AI and AI Agents",
     "How GenAI works, context and harness engineering, the agentic loop, "
     "OpenClaw and Hermes agents, and multi-agent systems (LO1)"),
    ("Topic 2", "Prompt Engineering and Post-Training for Autonomous AI Agents",
     "Prompt-engineering principles, running prompts through the Hermes agent on MiniMax, "
     "and installing tools and skills to lift output quality (LO2)"),
    ("Topic 3", "Security Risk of Autonomous AI Agents",
     "AI data governance, job impact and redesign, and the security risks of "
     "autonomous agents and how to roll them out safely (LO3)"),
]

ASSESSMENT = {
    "wa": "Written Assessment (SAQ) — 5 short-answer questions, one per K statement (K1–K5)",
    "cs": "Case Study — 3 reflective tasks (two questions each) in which learners document "
          "their own observations from the in-class activities, mapped to LO1–LO3 and the "
          "A statements",
    "format": "Open Book",
    "grading": "Competent / Not Yet Competent",
}
