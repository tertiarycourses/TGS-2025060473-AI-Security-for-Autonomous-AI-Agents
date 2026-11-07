# AI Security for Autonomous AI Agents

Attack a real AI agent three ways, stop it each time, then write the governance policy and the incident report your company needs. A one-day WSQ course with no coding.

| Course detail | Information |
|---|---|
| Course code | `TGS-2025060473` |
| Programme | WSQ |
| TSC | Generative AI Principles and Applications (ICT-INT-0052-1.1), Level 1 |
| Duration | 1 day, 8 hours: 9:00 am to 6:00 pm, including a 1-hour assessment (lunch not counted) |
| Registration | [View course details and register](https://www.tertiarycourses.com.sg/wsq-ai-security-for-autonomous-ai-agents.html) |
| Funding | Up to 70% WSQ funding; SkillsFuture Credit claimable. Eligibility and terms apply: see the course page. |
| Courseware | Version 5.0, 7 November 2026 |

**[Copy every lab prompt in one click](https://tertiarycourses.github.io/TGS-2025060473-AI-Security-for-Autonomous-AI-Agents/prompts/index.html)** · [Download the course ZIP](https://github.com/tertiarycourses/TGS-2025060473-AI-Security-for-Autonomous-AI-Agents/archive/refs/heads/master.zip)

## About the course

Always-on AI agents now read inboxes overnight, answer customers and hold company data. In the morning you see what they do, with a brief history of AI from 1966 to 2026, the path from OpenClaw to Hermes to hosted agents, and five agents compared. Then you break one. On a Hermes agent running on a free model, you plant a prompt injection in a customer review, jailbreak it with a comedy skit and watch an ordinary request leak fictional member data. You fix each one and measure the difference.

In the afternoon you govern them, with the five principles of AI security: Data Control, Permission Control, Human in the Loop, Traceability and Right-Sized Models. An interview prompt helps you write an AI Governance Policy, and mock traces of a leak three months ago become an AI Incident Report under Singapore's PDPA. All lab data belongs to Kopi Kaki Co., a fictional Singapore kopi startup.

## Learning outcomes

- **LO1:** Demonstrate generative AI concepts and applications relevant to customer service and hospitality management.
- **LO2:** Apply prompt engineering techniques and analyse output variations to improve generative AI performance in service settings.
- **LO3:** Identify ethical risks and analyse bias in AI-generated content used in customer engagement.

## Topics covered

1. **Human-AI Collaboration and Always-On AI Agents.** AI history, 1960 to 2026. How generative AI writes. Generative versus discriminative models. Agentic AI versus AI agents. OpenClaw, Hermes and always-on agents. Use cases. Five Human-AI collaboration scenarios. Gemini Spark (now Task), Meta Muse, OpenAI dots, Grok Bot and Manus Cue compared.
2. **AI Agent Vulnerabilities.** Prompt engineering and data quality. Prompt injection: what it is, real examples, why a model cannot tell a genuine prompt from a malicious one in the context window, and what it costs. Jailbreak. Data leak, personal data and the PDPA.
3. **AI Governance and Security.** How a model works; limits, bias and ethics. The five principles of AI security, each with examples. The frameworks behind them: IMDA, NIST, OWASP, ISO and the PDPA. Incident response with C.A.R.E.

## Labs

Each lab is one folder holding mock data, scripts and a PDF of instructions and prompts. Your agent runs the scripts, and you read the result.

| Lab | Topic | Time | What you do | Evidence for |
|---|---|---|---|---|
| [Lab 1](labs/lab1-ai-agents/LAB-01-Instructions.pdf) | 1 | 30 min | Your always-on CEO assistant: Meta Muse or OpenAI dots reads your calendar and catches a clash | Case Study Q1 |
| [Lab 2](labs/lab2-prompt-injection/LAB-02-Instructions.pdf) | 2 | 30 min | Prompt injection: install Hermes Desktop on a free model, plant a note in a review, fix it with a stronger model or a guardrail | Case Study Q2 |
| [Lab 3](labs/lab3-jailbreak/LAB-03-Instructions.pdf) | 2 | 15 min | Jailbreak: a comedy skit gets 100% off from your agent. A written guardrail, a stronger model and a gate in code each try to stop it | Case Study Q2 |
| [Lab 4](labs/lab4-data-leak/LAB-04-Instructions.pdf) | 2 | 15 min | Data leak: an ordinary request exposes fictional NRICs. Fix it by masking, a privacy rule and an output scan | Case Study Q2 |
| [Lab 5](labs/lab5-ai-governance-policy/LAB-05-Instructions.pdf) | 3 | 40 min | AI Governance Policy: your agent interviews you, then writes it around the five principles | Case Study Q3 |
| [Lab 6](labs/lab6-ai-incident-report/LAB-06-Instructions.pdf) | 3 | 40 min | AI Incident Report: from mock traces of a leak three months ago, checked by you against the evidence | Case Study Q3 |

In Labs 2, 3 and 4 you copy the lab's data and scripts into a plain working folder on your Desktop before attaching it. In testing, a folder named after the attack tipped off the model.

## Assessment

Written Assessment (SAQ), 30 minutes, 5 short-answer questions, K1 to K5. Case Study, 30 minutes, Q1 to Q3, A1 to A5: you paste your own lab screenshots as your answers and add a short analysis. Open book. Competent or Not Yet Competent.

## Courseware in this repository

| Item | Files |
|---|---|
| Slide deck (131 slides) | [PowerPoint](courseware/WSQ%20-%20Master%20Trainer%20Slides%20-%20TGS-2025060473%20-%20AI%20Security%20for%20Autonomous%20AI%20Agents-v50.pptx) · [PDF](courseware/WSQ%20-%20Master%20Trainer%20Slides%20-%20TGS-2025060473%20-%20AI%20Security%20for%20Autonomous%20AI%20Agents-v50.pdf) |
| Learner Guide | [Word](courseware/Learner%20Guide%20-%20TGS-2025060473%20-%20AI%20Security%20for%20Autonomous%20AI%20Agents.docx) · [PDF](courseware/Learner%20Guide%20-%20TGS-2025060473%20-%20AI%20Security%20for%20Autonomous%20AI%20Agents.pdf) · [Markdown](courseware/LEARNER-GUIDE.md) |
| Lesson Plan | [Word](courseware/Lesson%20Plan%20-%20TGS-2025060473%20-%20AI%20Security%20for%20Autonomous%20AI%20Agents.docx) · [PDF](courseware/Lesson%20Plan%20-%20TGS-2025060473%20-%20AI%20Security%20for%20Autonomous%20AI%20Agents.pdf) |
| Facilitator Guide | [Word](courseware/FG_TGS-2025060473_AI%20Security%20for%20Autonomous%20AI%20Agents_v5.docx) · [PDF](courseware/FG_TGS-2025060473_AI%20Security%20for%20Autonomous%20AI%20Agents_v5.pdf) |
| Labs and prompts | [`labs/`](labs/) · [`prompts/index.html`](prompts/index.html) |

**Not in this repository:** assessment papers, answer keys and the Assessment Plan. They are confidential and held on Google Drive and the LMS. Credentials and source references are also excluded.

Attacks in the labs are for your own lab agent and the fictional shop only. Never run them on systems you do not own.

---

Provided by [Tertiary Infotech Academy Pte Ltd](https://www.tertiarycourses.com.sg/) (UEN 201200696W).
