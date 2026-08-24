# AI Security for Autonomous AI Agents — Learner Guide

**Course Code:** TGS-2025060473  |  **TSC:** Generative AI Principles and Applications (ICT-INT-0052-1.1)  
**Version:** 4.0  |  **Date:** 25 August 2026  |  **Duration:** 1 Day · 8 Hours

> This guide mirrors the Learner Guide DOCX exactly. Both are generated from `lg_content.py`.

## Learning Outcomes

| LO | Learning Outcome |
|---|---|
| LO1 | Demonstrate generative AI concepts and applications relevant to customer service and hospitality management. |
| LO2 | Apply prompt engineering techniques and analyse output variations to improve generative AI performance in service settings. |
| LO3 | Identify ethical risks and analyse bias in AI-generated content used in customer engagement. |

## Knowledge Statements

| Code | Knowledge statement |
|---|---|
| K1 | Importance of data quality, preprocessing, model pipeline and model training (e.g., impact of data bias from training data) |
| K2 | Underlying principles, core concepts and theories governing generative AI |
| K3 | Difference between generative and discriminative models |
| K4 | Impact of prompt engineering on the model outputs of generative AI |
| K5 | Generative AI model workings, including training data, algorithms, and outputs |

## Ability Statements

| Code | Ability statement |
|---|---|
| A1 | Analyse limitations and potential biases in AI-generated content |
| A2 | Identify the ethical implications and societal impact of AI-generated content |
| A3 | Apply understanding of generative AI principles to use cases |
| A4 | Demonstrate the use of generation AI in diverse applications (e.g., summarisation, inference, reasoning, transformation of content, augmentation of content) |
| A5 | Analyse generative AI models' performance metrics and evaluate the influence of prompt variations |


---

# How to Use This Learner Guide

This guide follows the trainer deck in sequence across the three topics of the day. It expands each concept into readable notes, then gives you full step-by-step walkthroughs for every activity. You will use ready-made websites, chatbots and AI agents — you do not need to write any code. All data used in the activities is fictional.

| Topic | Learning outcome | What you will be able to do |
|---|---|---|
| Topic 1 | LO1 | Explain generative AI, agentic AI and AI agents, and how they differ. |
| Topic 2 | LO2 | Apply prompt-engineering techniques and compare output variations. |
| Topic 3 | LO3 | Identify ethical, governance and security risks in AI-generated content and agents. |

> **Evidence labels**
> HIST = historical fact · DEF = definition · PROD = product documentation · CASE-V = verified/real dated case · SIM = classroom simulation (all names and numbers fictional) · SYN = teaching synthesis.

> **Safe-use rule**
> Never paste real personal data or a production API key into any demo. Use a low-limit training key and delete it after the course.


## Slide 5 — Who Is in the Room?

> **Evidence: ADMIN**
> Concept or classroom slide; no external factual claim is introduced here.

Read the points below as the few things worth remembering about “Who Is in the Room?”.

| Concept | What it means |
|---|---|
| Role | What service or team do you work in? |
| AI today | Where do you already meet AI at work? |
| Goal | What do you want to be able to do by 6pm? |

Why it matters at work: In a customer-service or hospitality setting, this shapes how you brief an AI tool and how much you trust its answer before it reaches a guest.


## Slide 6 — Ground Rules for a Hands-On Day

> **Evidence: ADMIN**
> Concept or classroom slide; no external factual claim is introduced here.

Read the points below as the few things worth remembering about “Ground Rules for a Hands-On Day”.

| Concept | What it means |
|---|---|
| Use the demos | Every activity is a ready-made website or chatbot — no coding |
| Fictional data only | Never paste real personal or company data into a demo |
| Ask and share | Try prompts, compare answers, and reflect together |

Why it matters at work: In a customer-service or hospitality setting, this shapes how you brief an AI tool and how much you trust its answer before it reaches a guest.


## Slide 7 — Learning Outcomes

> **Evidence: ADMIN**
> Concept or classroom slide; no external factual claim is introduced here.

Read the points below as the few things worth remembering about “Learning Outcomes”.

| Concept | What it means |
|---|---|
| LO1 | Demonstrate generative AI concepts and applications |
| LO2 | Apply prompt engineering and analyse output variations |
| LO3 | Identify ethical risks and analyse bias in AI content |

Why it matters at work: In a customer-service or hospitality setting, this shapes how you brief an AI tool and how much you trust its answer before it reaches a guest.


## Slide 8 — One-Day Learning Journey

> **Evidence: ADMIN**
> Concept or classroom slide; no external factual claim is introduced here.

“One-Day Learning Journey” is best understood as a sequence — the steps below run in order. Each step feeds the next, so a problem early on shows up later in the chain — which is exactly why the order is worth learning. Three topics map one-to-one onto LO1, LO2 and LO3; the assessment closes the day.

1. Topic 1 — GenAI, Agentic AI & Agents
2. Topic 2 — Prompt Engineering
3. Topic 3 — Security & Governance
4. Assessment

> **Note**
> Three topics map one-to-one onto LO1, LO2 and LO3; the assessment closes the day.

Why it matters at work: In a customer-service or hospitality setting, this shapes how you brief an AI tool and how much you trust its answer before it reaches a guest.


## Slide 9 — How the Day Is Assessed

> **Evidence: ADMIN**
> Concept or classroom slide; no external factual claim is introduced here.

The table below is easier to recall once you see the pattern behind it.

| Instrument | Covers | What you do |
|---|---|---|
| Written Assessment (SAQ) | K1–K5 | Five short written answers, one per knowledge statement |
| Practical Performance | LO1–LO3 (A1–A5) | Three reflection tasks on the activities you completed today |
| Format | — | Open book · Competent / Not Yet Competent |

Why it matters at work: In a customer-service or hospitality setting, this shapes how you brief an AI tool and how much you trust its answer before it reaches a guest.


## Slide 10 — Briefing for Assessment

> **Evidence: ADMIN**
> Concept or classroom slide; no external factual claim is introduced here.

“Briefing for Assessment” is best understood as a sequence — the steps below run in order. Each step feeds the next, so a problem early on shows up later in the chain — which is exactly why the order is worth learning. The briefing for assessment is delivered before the assessment begins.

1. Read each task
2. Draw on today's activities
3. Write from your own evidence
4. Justify your reasoning
5. Submit on the LMS

> **Note**
> The briefing for assessment is delivered before the assessment begins.

Why it matters at work: In a customer-service or hospitality setting, this shapes how you brief an AI tool and how much you trust its answer before it reaches a guest.


---

# Generative AI, Agentic AI and AI Agents

[TOPIC 1 · LO1]

From a chat box to systems that plan and act — history, mechanics, use cases and agents.


## Slide 13 — What Topic 1 Will Answer

> **Evidence: SYN**
> Concept or classroom slide; no external factual claim is introduced here.

“What Topic 1 Will Answer” is best understood as a sequence — the steps below run in order. Each step feeds the next, so a problem early on shows up later in the chain — which is exactly why the order is worth learning. Each question builds the vocabulary you need for prompt engineering and security later.

1. How did we get here?
2. How does GenAI actually work?
3. What is context engineering?
4. What is an agentic loop?
5. What is an AI agent?

> **Note**
> Each question builds the vocabulary you need for prompt engineering and security later.

Why it matters at work: In a customer-service or hospitality setting, this shapes how you brief an AI tool and how much you trust its answer before it reaches a guest.


## Slide 14 — A Very Short History of AI, 2023–2026

> **Evidence: HIST**
> Concept or classroom slide; no external factual claim is introduced here.

“A Very Short History of AI, 2023–2026” is best understood as a sequence — the steps below run in order. Each step feeds the next, so a problem early on shows up later in the chain — which is exactly why the order is worth learning. Each year did not replace the last — it added a new layer on top of it.

1. 2023 · Generative AI
2. 2024 · Context Engineering
3. 2025 · Harness Engineering
4. 2026 · AI Agents

> **Note**
> Each year did not replace the last — it added a new layer on top of it.

Why it matters at work: In a customer-service or hospitality setting, this shapes how you brief an AI tool and how much you trust its answer before it reaches a guest.


## Slide 15 — The Four Waves in Plain Words

> **Evidence: SYN**
> Concept or classroom slide; no external factual claim is introduced here.

Read the points below as the few things worth remembering about “The Four Waves in Plain Words”.

| Concept | What it means |
|---|---|
| 2023 — Generative AI | ChatGPT makes text and image generation mainstream |
| 2024 — Context Engineering | We learn to feed models the right information, not just a prompt |
| 2025 — Harness Engineering | We wrap models in loops that plan, act and verify — agentic AI |
| 2026 — AI Agents | Deployed agents act across our apps, chats and tools |

Why it matters at work: In a customer-service or hospitality setting, this shapes how you brief an AI tool and how much you trust its answer before it reaches a guest.


## Slide 16 — 2023 — Generative AI Goes Mainstream

> **Evidence: HIST**
> Sources: S08 — OpenAI — Introducing ChatGPT (30 Nov 2022)

The points below unpack what “2023 — Generative AI Goes Mainstream” means in practice.

- ChatGPT launched on 30 November 2022 and reached mass adoption through 2023
- One natural-language box exposed writing, coding, translation and analysis to everyone
- Businesses began asking not 'can it chat?' but 'what work can it do?'

Why it matters at work: In a customer-service or hospitality setting, this shapes how you brief an AI tool and how much you trust its answer before it reaches a guest.


## Slide 17 — 2024 — Context Engineering

> **Evidence: HIST**
> Sources: S10 — Anthropic — Effective context engineering for AI agents (Sep 2025), S11 — Karpathy on 'context engineering' (X, 25 Jun 2025)

The points below unpack what “2024 — Context Engineering” means in practice.

- Teams found the prompt alone was not enough — the model needed the right supporting information
- Andrej Karpathy argued for 'context engineering' over 'prompt engineering' (Jun 2025)
- The craft became: fill the context window with just the right tokens for the next step

Why it matters at work: In a customer-service or hospitality setting, this shapes how you brief an AI tool and how much you trust its answer before it reaches a guest.


## Slide 18 — 2025 — Harness Engineering and Agentic AI

> **Evidence: HIST**
> Sources: S12 — Anthropic — How Claude Code works (agentic harness), S13 — OpenAI — Harness engineering: Codex in an agent-first world

The points below unpack what “2025 — Harness Engineering and Agentic AI” means in practice.

- Tools like Claude Code and Codex wrapped the model in a loop that gathers context, acts and verifies
- OpenAI named this discipline 'harness engineering'; Anthropic calls the tool an 'agentic harness'
- The model stopped only answering and started doing multi-step work

Why it matters at work: In a customer-service or hospitality setting, this shapes how you brief an AI tool and how much you trust its answer before it reaches a guest.


## Slide 19 — 2026 — The Year of AI Agents

> **Evidence: HIST**
> Sources: S30 — OpenClaw — Wikipedia (naming and adoption history), S33 — Hermes Agent (Nous Research) — documentation

The points below unpack what “2026 — The Year of AI Agents” means in practice.

- Personal and organisational agents such as OpenClaw and Hermes reached everyday users
- Agents now live inside WhatsApp, Telegram, email and business apps
- The question shifted again: how do we let agents act safely on our behalf?

Why it matters at work: In a customer-service or hospitality setting, this shapes how you brief an AI tool and how much you trust its answer before it reaches a guest.


---

# How Generative AI Works

[TOPIC 1]

Training, inference, and the autoregressive language model.


## Slide 21 — What 'Generative' Means

> **Evidence: DEF**
> Concept or classroom slide; no external factual claim is introduced here.

Read the points below as the few things worth remembering about “What 'Generative' Means”.

| Concept | What it means |
|---|---|
| Generative AI | Produces new text, image, audio, video or code from patterns it has learned |
| Discriminative AI | Sorts or scores existing input — spam / not-spam, fraud / not-fraud |
| Why it matters | Service teams use both: generate a reply, and classify a request |

Why it matters at work: In a customer-service or hospitality setting, this shapes how you brief an AI tool and how much you trust its answer before it reaches a guest.


## Slide 22 — Two Phases: Training and Inference

> **Evidence: DEF**
> Sources: S06 — Brown et al., Language Models are Few-Shot Learners (GPT-3)

“Two Phases: Training and Inference” is best understood as a sequence — the steps below run in order. Each step feeds the next, so a problem early on shows up later in the chain — which is exactly why the order is worth learning. Training happens once and is expensive; inference happens every time you use the model.

1. Gather large text corpora
2. Train — adjust billions of parameters
3. Ship the model
4. Inference — you prompt, it responds

> **Note**
> Training happens once and is expensive; inference happens every time you use the model.

Why it matters at work: In a customer-service or hospitality setting, this shapes how you brief an AI tool and how much you trust its answer before it reaches a guest.


## Slide 23 — How an Autoregressive LLM Writes

> **Evidence: DEF**
> Sources: S05 — Vaswani et al., Attention Is All You Need (2017)

“How an Autoregressive LLM Writes” is best understood as a sequence — the steps below run in order. Each step feeds the next, so a problem early on shows up later in the chain — which is exactly why the order is worth learning. A large language model writes one token at a time, each based on everything before it.

1. Read your context as tokens
2. Predict the next token's probabilities
3. Pick one token
4. Append it and repeat

> **Note**
> A large language model writes one token at a time, each based on everything before it.

Why it matters at work: In a customer-service or hospitality setting, this shapes how you brief an AI tool and how much you trust its answer before it reaches a guest.


## Slide 24 — Why the Same Prompt Can Differ

> **Evidence: DEF**
> Concept or classroom slide; no external factual claim is introduced here.

Read the points below as the few things worth remembering about “Why the Same Prompt Can Differ”.

| Concept | What it means |
|---|---|
| Probabilities | The model samples from likely next tokens, not a fixed lookup |
| Temperature | Higher settings add variety; lower settings add consistency |
| Context | Change the surrounding information and the whole answer shifts |

Why it matters at work: In a customer-service or hospitality setting, this shapes how you brief an AI tool and how much you trust its answer before it reaches a guest.


## Slide 25 — Strengths and Limits for Service Work

> **Evidence: DEF**
> Concept or classroom slide; no external factual claim is introduced here.

Read the points below as the few things worth remembering about “Strengths and Limits for Service Work”.

| Concept | What it means |
|---|---|
| Strong at | Drafting, summarising, translating, reformatting, brainstorming |
| Weak at | Facts it was never given — it can sound confident yet be wrong |
| Rule | Treat fluent output as a draft to verify, not as truth |

Why it matters at work: In a customer-service or hospitality setting, this shapes how you brief an AI tool and how much you trust its answer before it reaches a guest.


---

# Generative AI in the Real World

[TOPIC 1]

Real, dated examples — how generation is already changing work.


## Slide 27 — Fashion Models Are Now Generated

> **Evidence: CASE-V**
> Sources: S20 — PetaPixel — Mango launches photorealistic AI-generated campaign (Jul 2024), S21 — CNN — H&M to create AI 'digital twins' of models (Mar 2025), S22 — CNN — AI models in Guess ad in Vogue's August 2025 issue

Read the points below as the few things worth remembering about “Fashion Models Are Now Generated”.

| Concept | What it means |
|---|---|
| Mango, Jul 2024 | Ran its first fully AI-generated campaign for its teen 'Sunset Dream' line across 95 markets |
| H&M, 2025 | Announced AI 'digital twins' of 30 real models; first labelled images appeared mid-2025 |
| Guess, Aug 2025 | A Guess ad using AI-generated models ran in Vogue's August issue and drew wide debate |

Why it matters at work: In a customer-service or hospitality setting, this shapes how you brief an AI tool and how much you trust its answer before it reaches a guest.


## Slide 28 — AI-Generated Video Is Overtaking Whole Industries

> **Evidence: SYN**
> Concept or classroom slide; no external factual claim is introduced here.

“AI-Generated Video Is Overtaking Whole Industries” is worth a closer look. Play the Short in-slide, or tap 'Watch the Short'. Discuss: could your team use this — and what could go wrong?

- ('AI-generated', 'This short vertical video was made with generative AI — no camera, cast or crew')
- ('Marketing & advertising', 'Brands now generate campaign video in hours, not weeks')
- ('Movies', 'AI is moving into film production — visuals, scenes and effects')
- ('Music', 'AI-generated tracks and videos are reshaping the music industry too')

> **Note**
> Play the Short in-slide, or tap 'Watch the Short'. Discuss: could your team use this — and what could go wrong?

Why it matters at work: In a customer-service or hospitality setting, this shapes how you brief an AI tool and how much you trust its answer before it reaches a guest.


## Slide 29 — Customer Service: The Klarna Story

> **Evidence: CASE-V**
> Sources: S25 — Klarna — AI assistant handles two-thirds of chats in first month (27 Feb 2024), S26 — Forbes — Klarna reverses on AI, re-hires human agents (May 2025)

“Customer Service: The Klarna Story” is best understood as a sequence — the steps below run in order. Each step feeds the next, so a problem early on shows up later in the chain — which is exactly why the order is worth learning. A real cautionary tale: automate the routine, but keep humans for judgement and empathy.

1. Feb 2024 — AI assistant handles 2/3 of chats
2. Work of ~700 agents in month one
3. Resolution time 11 min to under 2 min
4. May 2025 — re-hires humans for quality

> **Note**
> A real cautionary tale: automate the routine, but keep humans for judgement and empathy.

Why it matters at work: In a customer-service or hospitality setting, this shapes how you brief an AI tool and how much you trust its answer before it reaches a guest.


## Slide 30 — Where Service Teams Apply GenAI Today

> **Evidence: SYN**
> Concept or classroom slide; no external factual claim is introduced here.

Read the points below as the few things worth remembering about “Where Service Teams Apply GenAI Today”.

| Concept | What it means |
|---|---|
| Front desk | Draft replies, translate, summarise long threads |
| Back office | Turn notes into reports; extract data from documents |
| Marketing | Generate copy, images and short video for campaigns |

Why it matters at work: In a customer-service or hospitality setting, this shapes how you brief an AI tool and how much you trust its answer before it reaches a guest.


---

# Context Engineering

[TOPIC 1]

The model is only as good as the context you give it.


## Slide 32 — Prompt Engineering vs Context Engineering

> **Evidence: DEF**
> Sources: S10 — Anthropic — Effective context engineering for AI agents (Sep 2025), S11 — Karpathy on 'context engineering' (X, 25 Jun 2025)

Read the points below as the few things worth remembering about “Prompt Engineering vs Context Engineering”.

| Concept | What it means |
|---|---|
| Prompt engineering | Wording one instruction well |
| Context engineering | Assembling everything the model sees before it answers |
| The shift | Real applications manage context, not just a clever prompt |

Why it matters at work: In a customer-service or hospitality setting, this shapes how you brief an AI tool and how much you trust its answer before it reaches a guest.


## Slide 33 — The Six Ingredients of Context

> **Evidence: DEF**
> Sources: S10 — Anthropic — Effective context engineering for AI agents (Sep 2025)

Read the points below as the few things worth remembering about “The Six Ingredients of Context”.

| Concept | What it means |
|---|---|
| System prompt | Who the AI is and its rules |
| User prompt | The task you asked for right now |
| History | Earlier turns in this conversation |
| Memory | Facts kept across sessions |
| Tools | Functions it can call to act or fetch data |
| Retrieved data | Documents pulled in for this task |

Why it matters at work: In a customer-service or hospitality setting, this shapes how you brief an AI tool and how much you trust its answer before it reaches a guest.


## Slide 34 — How an Agent Gathers Context for a Task

> **Evidence: SYN**
> Sources: S10 — Anthropic — Effective context engineering for AI agents (Sep 2025)

“How an Agent Gathers Context for a Task” is best understood as a sequence — the steps below run in order. Each step feeds the next, so a problem early on shows up later in the chain — which is exactly why the order is worth learning. Example: 'Reply to this guest email' → it pulls the booking, the policy doc and past replies first.

1. You give a goal
2. It reads its system prompt and memory
3. It retrieves relevant files or data
4. It calls tools for fresh facts
5. It assembles all of this, then answers

> **Note**
> Example: 'Reply to this guest email' → it pulls the booking, the policy doc and past replies first.

Why it matters at work: In a customer-service or hospitality setting, this shapes how you brief an AI tool and how much you trust its answer before it reaches a guest.


## Slide 35 — A Worked Context Example

> **Evidence: SYN**
> Concept or classroom slide; no external factual claim is introduced here.

Read the points below as the few things worth remembering about “A Worked Context Example”.

| Concept | What it means |
|---|---|
| Task | 'Draft a refund reply to Mr Tan' |
| Context gathered | Booking record + refund policy + tone guide + the original email |
| Result | A grounded reply, not a generic guess |

Why it matters at work: In a customer-service or hospitality setting, this shapes how you brief an AI tool and how much you trust its answer before it reaches a guest.


---

# The Agentic Loop and Harness Engineering

[TOPIC 1]

What turns a model that answers into a system that acts.


## Slide 37 — The Agentic Loop — A Visual Pipeline

> **Evidence: DEF**
> Sources: S12 — Anthropic — How Claude Code works (agentic harness)

“The Agentic Loop — A Visual Pipeline” is best understood as a sequence — the steps below run in order. Each step feeds the next, so a problem early on shows up later in the chain — which is exactly why the order is worth learning. The loop repeats until the goal is met. Anthropic's harness uses gather → act → verify; 'plan' is shown here as a teaching step.

1. Context — gather goal & information
2. Plan — decide the next step
3. Execute — call a tool / take an action
4. Verify — check the result

> **Note**
> The loop repeats until the goal is met. Anthropic's harness uses gather → act → verify; 'plan' is shown here as a teaching step.

Why it matters at work: In a customer-service or hospitality setting, this shapes how you brief an AI tool and how much you trust its answer before it reaches a guest.


## Slide 38 — What a Harness Adds Around the Model

> **Evidence: DEF**
> Sources: S12 — Anthropic — How Claude Code works (agentic harness), S13 — OpenAI — Harness engineering: Codex in an agent-first world

Read the points below as the few things worth remembering about “What a Harness Adds Around the Model”.

| Concept | What it means |
|---|---|
| The loop | Runs context → plan → execute → verify repeatedly |
| Tool access | Lets the model read files, run commands, call APIs |
| State & safety | Tracks progress and enforces permissions and sandboxes |

Why it matters at work: In a customer-service or hospitality setting, this shapes how you brief an AI tool and how much you trust its answer before it reaches a guest.


## Slide 39 — Two Harnesses You May Have Heard Of

> **Evidence: PROD**
> Sources: S12 — Anthropic — How Claude Code works (agentic harness), S13 — OpenAI — Harness engineering: Codex in an agent-first world

Read the points below as the few things worth remembering about “Two Harnesses You May Have Heard Of”.

| Concept | What it means |
|---|---|
| Claude Code | Anthropic's coding agent — the 'agentic harness around Claude' |
| Codex | OpenAI's coding agent; OpenAI calls the discipline 'harness engineering' |
| Same idea | A loop + tools + a sandbox around a general model |

Why it matters at work: In a customer-service or hospitality setting, this shapes how you brief an AI tool and how much you trust its answer before it reaches a guest.


## Slide 40 — A Concrete Agentic Loop

> **Evidence: SYN**
> Concept or classroom slide; no external factual claim is introduced here.

“A Concrete Agentic Loop” is best understood as a sequence — the steps below run in order. Each step feeds the next, so a problem early on shows up later in the chain — which is exactly why the order is worth learning. If verification fails — a folder is empty — the agent re-plans instead of stopping.

1. Goal: 'Summarise this week's guest complaints'
2. Plan: open the inbox folder
3. Execute: read and cluster the emails
4. Verify: check counts, then write the summary
5. Repeat until done

> **Note**
> If verification fails — a folder is empty — the agent re-plans instead of stopping.

Why it matters at work: In a customer-service or hospitality setting, this shapes how you brief an AI tool and how much you trust its answer before it reaches a guest.


---

# AI Agents: OpenClaw and Hermes

[TOPIC 1]

The deployed systems that put the agentic loop into everyday hands.


## Slide 42 — What Makes Something an 'AI Agent'

> **Evidence: DEF**
> Sources: S44 — OWASP Top 10 for Agentic Applications (2026)

Read the points below as the few things worth remembering about “What Makes Something an 'AI Agent'”.

| Concept | What it means |
|---|---|
| A real system | Not just a model — a running app with an identity |
| Acts through tools | Sends messages, edits files, calls services |
| Keeps state | Remembers context and can resume work |

Why it matters at work: In a customer-service or hospitality setting, this shapes how you brief an AI tool and how much you trust its answer before it reaches a guest.


## Slide 43 — Peter Steinberger — Creator of OpenClaw

> **Evidence: PROD**
> Sources: S30 — OpenClaw — Wikipedia (naming and adoption history), S32 — Peter Steinberger — GitHub (steipete)

“Peter Steinberger — Creator of OpenClaw” is worth a closer look.

- ('Who', 'Austrian developer, founder of PSPDFKit; GitHub handle steipete')
- ('What he built', 'OpenClaw, an open-source personal AI agent that went viral in late 2025')
- ('Since', 'Joined OpenAI in Feb 2026; an OpenClaw Foundation now stewards the project')

Why it matters at work: In a customer-service or hospitality setting, this shapes how you brief an AI tool and how much you trust its answer before it reaches a guest.


## Slide 44 — OpenClaw — A Naming and Adoption Story

> **Evidence: PROD**
> Sources: S30 — OpenClaw — Wikipedia (naming and adoption history)

“OpenClaw — A Naming and Adoption Story” is best understood as a sequence — the steps below run in order. Each step feeds the next, so a problem early on shows up later in the chain — which is exactly why the order is worth learning. Renamed after a trademark complaint; figures per Wikipedia, as of early 2026.

1. Nov 2025 — released, goes viral as 'Clawdbot'
2. Jan 2026 — renamed 'Moltbot'
3. Jan 2026 — renamed 'OpenClaw'
4. Mar 2026 — ~247k GitHub stars

> **Note**
> Renamed after a trademark complaint; figures per Wikipedia, as of early 2026.

Why it matters at work: In a customer-service or hospitality setting, this shapes how you brief an AI tool and how much you trust its answer before it reaches a guest.


## Slide 45 — OpenClaw Runs Where You Already Chat

> **Evidence: PROD**
> Sources: S31 — OpenClaw — official site and docs

Read the points below as the few things worth remembering about “OpenClaw Runs Where You Already Chat”.

| Concept | What it means |
|---|---|
| Messaging-first | You talk to it in WhatsApp, Telegram, Slack, Signal and more |
| Self-hosted | It runs on your own machine or server, under your control |
| Tool-enabled | It can read, write and call services on your behalf |

Why it matters at work: In a customer-service or hospitality setting, this shapes how you brief an AI tool and how much you trust its answer before it reaches a guest.


## Slide 46 — Hermes Agent by Nous Research

> **Evidence: PROD**
> Sources: S33 — Hermes Agent (Nous Research) — documentation

Read the points below as the few things worth remembering about “Hermes Agent by Nous Research”.

| Concept | What it means |
|---|---|
| Open-source agent | CLI, gateway and messaging surfaces; a desktop app since Jun 2026 |
| Self-improving | Can create reusable skills from experience |
| Flexible models | Runs on many providers — we will point it at MiniMax in Topic 2 |

Why it matters at work: In a customer-service or hospitality setting, this shapes how you brief an AI tool and how much you trust its answer before it reaches a guest.


## Slide 47 — Try It Today: TIA Support on WhatsApp

> **Evidence: PROD**
> Sources: S31 — OpenClaw — official site and docs

Read the points below as the few things worth remembering about “Try It Today: TIA Support on WhatsApp”. We use this live in Activity 1.

| Concept | What it means |
|---|---|
| The number | TIA Support WhatsApp +65 8866 6375, powered by OpenClaw |
| What to do | Message it like a person and give it a small task |
| Watch for | Where it helps — and where you would not trust it yet |

> **Note**
> We use this live in Activity 1.

Why it matters at work: In a customer-service or hospitality setting, this shapes how you brief an AI tool and how much you trust its answer before it reaches a guest.


---

# Skills and Tools

[TOPIC 1]

How agents extend beyond the base model.


## Slide 49 — Tools vs Skills

> **Evidence: DEF**
> Sources: S15 — Anthropic — Agent Skills / Claude Code, S16 — Model Context Protocol (MCP) documentation

Read the points below as the few things worth remembering about “Tools vs Skills”.

| Concept | What it means |
|---|---|
| Tools | Actions the agent can take — send email, run a query, open a file |
| Skills | Packaged know-how — reusable instructions for a task |
| Together | Skills tell the agent how; tools let the agent do |

Why it matters at work: In a customer-service or hospitality setting, this shapes how you brief an AI tool and how much you trust its answer before it reaches a guest.


## Slide 50 — How an Agent Uses a Tool

> **Evidence: DEF**
> Sources: S16 — Model Context Protocol (MCP) documentation

“How an Agent Uses a Tool” is best understood as a sequence — the steps below run in order. Each step feeds the next, so a problem early on shows up later in the chain — which is exactly why the order is worth learning. Model Context Protocol (MCP) is a common standard for connecting tools to agents.

1. Model decides an action is needed
2. Picks a tool and fills its inputs
3. The tool runs and returns a result
4. Result becomes new context
5. Model continues

> **Note**
> Model Context Protocol (MCP) is a common standard for connecting tools to agents.

Why it matters at work: In a customer-service or hospitality setting, this shapes how you brief an AI tool and how much you trust its answer before it reaches a guest.


## Slide 51 — Why Skills Make Agents Practical

> **Evidence: SYN**
> Sources: S15 — Anthropic — Agent Skills / Claude Code

Read the points below as the few things worth remembering about “Why Skills Make Agents Practical”.

| Concept | What it means |
|---|---|
| Consistency | The same task is done the same way every time |
| Reuse | Build once, run across many jobs |
| In Topic 2 | We install a skill so the agent formats Excel and PPT better |

Why it matters at work: In a customer-service or hospitality setting, this shapes how you brief an AI tool and how much you trust its answer before it reaches a guest.


---

# Multi-Agent Systems

[TOPIC 1]

When one agent is not enough.


## Slide 54 — Orchestrator and Workers

> **Evidence: DEF**
> Sources: S14 — Anthropic — How we built our multi-agent research system (13 Jun 2025)

“Orchestrator and Workers” is best understood as a sequence — the steps below run in order. Each step feeds the next, so a problem early on shows up later in the chain — which is exactly why the order is worth learning. Anthropic's research system used this pattern; it beat a single agent by ~90% on their internal research eval.

1. A lead agent receives the goal
2. It splits the work into parts
3. Worker agents run parts in parallel
4. The lead combines their results

> **Note**
> Anthropic's research system used this pattern; it beat a single agent by ~90% on their internal research eval.

Why it matters at work: In a customer-service or hospitality setting, this shapes how you brief an AI tool and how much you trust its answer before it reaches a guest.


## Slide 55 — Why and Why Not Multi-Agent

> **Evidence: DEF**
> Sources: S14 — Anthropic — How we built our multi-agent research system (13 Jun 2025)

Read the points below as the few things worth remembering about “Why and Why Not Multi-Agent”.

| Concept | What it means |
|---|---|
| Faster & broader | Parallel workers cover more ground |
| Costlier | Multi-agent runs used far more tokens than a single chat |
| Trade-off | Use it when breadth matters more than cost |

Why it matters at work: In a customer-service or hospitality setting, this shapes how you brief an AI tool and how much you trust its answer before it reaches a guest.


## Slide 56 — A Service Example

> **Evidence: SYN**
> Concept or classroom slide; no external factual claim is introduced here.

Read the points below as the few things worth remembering about “A Service Example”.

| Concept | What it means |
|---|---|
| Goal | 'Plan a customer-recovery campaign' |
| Workers | One drafts copy, one builds the offer, one checks the data |
| Lead | Merges the three into one plan for a human to approve |

Why it matters at work: In a customer-service or hospitality setting, this shapes how you brief an AI tool and how much you trust its answer before it reaches a guest.


---

# Generative AI vs Agentic AI vs AI Agents

[TOPIC 1]

The single most useful distinction from Topic 1.


## Slide 58 — The Three, Side by Side

> **Evidence: SYN**
> Sources: S43 — OWASP Top 10 for LLM Applications, S44 — OWASP Top 10 for Agentic Applications (2026)

The table below is easier to recall once you see the pattern behind it.

|  | Generative AI | Agentic AI | AI Agent |
|---|---|---|---|
| What it does | Creates content | Loops to reach a goal | A deployed system that acts |
| Acts on its own? | No — you run each step | Yes — plans and retries | Yes — through real tools |
| Example | ChatGPT drafting a reply | Claude Code fixing a bug | OpenClaw in your WhatsApp |

Why it matters at work: In a customer-service or hospitality setting, this shapes how you brief an AI tool and how much you trust its answer before it reaches a guest.


## Slide 59 — One-Line Definitions

> **Evidence: SYN**
> Concept or classroom slide; no external factual claim is introduced here.

Read the points below as the few things worth remembering about “One-Line Definitions”.

| Concept | What it means |
|---|---|
| Generative AI | Makes things |
| Agentic AI | The loop that makes an AI pursue a goal |
| AI Agent | The running system that uses that loop to act for you |

Why it matters at work: In a customer-service or hospitality setting, this shapes how you brief an AI tool and how much you trust its answer before it reaches a guest.


## Slide 60 — Generation is a step. Agency is a loop. An agent is a system.

> **Evidence: SYN**
> Concept or classroom slide; no external factual claim is introduced here.

> **Key idea**
> Generation is a step. Agency is a loop. An agent is a system.


## Slide 61 — Activity 1 — Talk to an AI Agent, Then Reflect

> **Evidence: SIM**
> Concept or classroom slide; no external factual claim is introduced here.

In this activity — Activity 1 — Talk to an AI Agent, Then Reflect — you work hands-on with a ready-made tool; the steps are in the walkthrough later in this guide. Pinboard: https://alfredang.github.io/pinboard/

- Message TIA Support on WhatsApp +65 8866 6375 (powered by OpenClaw)
- Use the prompt card in the activity pack; give it a small realistic task
- Post your reflections to the Pinboard under the four risk themes

> **Note**
> Pinboard: https://alfredang.github.io/pinboard/

Why it matters at work: In a customer-service or hospitality setting, this shapes how you brief an AI tool and how much you trust its answer before it reaches a guest.


## Slide 62 — Activity 1 — Group Your Concerns

> **Evidence: SIM**
> Concept or classroom slide; no external factual claim is introduced here.

Read the points below as the few things worth remembering about “Activity 1 — Group Your Concerns”.

| Concept | What it means |
|---|---|
| Data Privacy | What data did it see or ask for? |
| Job Impact | Whose work does this change? |
| Ethical Concerns | Could it mislead or be unfair? |
| Cyber Security | How could it be abused? |

Why it matters at work: In a customer-service or hospitality setting, this shapes how you brief an AI tool and how much you trust its answer before it reaches a guest.


## Slide 63 — Activity 1 — Debrief

> **Evidence: SIM**
> Concept or classroom slide; no external factual claim is introduced here.

“Activity 1 — Debrief” is best understood as a sequence — the steps below run in order. Each step feeds the next, so a problem early on shows up later in the chain — which is exactly why the order is worth learning. This debrief seeds the governance thinking you will use in Topic 3.

1. Read the Pinboard together
2. Cluster the four themes
3. Name the top risk in each
4. Agree one safe-use rule per theme

> **Note**
> This debrief seeds the governance thinking you will use in Topic 3.

Why it matters at work: In a customer-service or hospitality setting, this shapes how you brief an AI tool and how much you trust its answer before it reaches a guest.


---

# Prompt Engineering and Post-Training for Autonomous AI Agents

[TOPIC 2 · LO2]

Set up a real agent on MiniMax, then learn to prompt it well.


## Slide 65 — What Topic 2 Will Cover

> **Evidence: SYN**
> Concept or classroom slide; no external factual claim is introduced here.

“What Topic 2 Will Cover” is best understood as a sequence — the steps below run in order. Each step feeds the next, so a problem early on shows up later in the chain — which is exactly why the order is worth learning. You will do the setup once, then use the same agent for both activities.

1. Install the Hermes agent
2. Point it at a MiniMax model
3. Learn prompt principles
4. Run real prompts
5. Add tools and skills

> **Note**
> You will do the setup once, then use the same agent for both activities.

Why it matters at work: At work this is the difference between a prompt that wastes time and one that gives you an answer you can send or act on straight away.


## Slide 66 — The Setup in Three Parts

> **Evidence: PROD**
> Sources: S33 — Hermes Agent (Nous Research) — documentation, S36 — MiniMax — MiniMax-M2 news and platform

Read the points below as the few things worth remembering about “The Setup in Three Parts”.

| Concept | What it means |
|---|---|
| Hermes Agent | The agent you talk to |
| MiniMax M2.7 | The model that powers it |
| Your API key | Connects the two — kept only on your machine |

Why it matters at work: At work this is the difference between a prompt that wastes time and one that gives you an answer you can send or act on straight away.


## Slide 67 — Install the Hermes Desktop App

> **Evidence: PROD**
> Sources: S34 — Hermes Agent — Desktop app user guide

“Install the Hermes Desktop App” is best understood as a sequence — the steps below run in order. Each step feeds the next, so a problem early on shows up later in the chain — which is exactly why the order is worth learning. If the CLI is already installed, 'hermes desktop' reuses your existing config and keys.

1. Open hermes-agent.nousresearch.com/docs/user-guide/desktop
2. Install the Hermes CLI
3. Run 'hermes desktop'
4. The app builds and launches
5. Run 'hermes setup'

> **Note**
> If the CLI is already installed, 'hermes desktop' reuses your existing config and keys.

Why it matters at work: At work this is the difference between a prompt that wastes time and one that gives you an answer you can send or act on straight away.


## Slide 68 — Get a MiniMax Model and API Key

> **Evidence: PROD**
> Sources: S36 — MiniMax — MiniMax-M2 news and platform, S37 — MiniMax — platform docs (API and models)

“Get a MiniMax Model and API Key” is best understood as a sequence — the steps below run in order. Each step feeds the next, so a problem early on shows up later in the chain — which is exactly why the order is worth learning. Check platform.minimax.io for current pricing and any promotional access before class.

1. Go to minimax.io
2. Create an account at platform.minimax.io
3. Select the M2.7 model
4. Create an API key
5. Copy it for Hermes

> **Note**
> Check platform.minimax.io for current pricing and any promotional access before class.

Why it matters at work: At work this is the difference between a prompt that wastes time and one that gives you an answer you can send or act on straight away.


## Slide 69 — Point Hermes at MiniMax M2.7

> **Evidence: PROD**
> Sources: S33 — Hermes Agent (Nous Research) — documentation, S37 — MiniMax — platform docs (API and models)

“Point Hermes at MiniMax M2.7” is best understood as a sequence — the steps below run in order. Each step feeds the next, so a problem early on shows up later in the chain — which is exactly why the order is worth learning. Hermes supports custom OpenAI-compatible endpoints, so MiniMax plugs straight in.

1. Open Hermes settings / inference providers
2. Choose a custom OpenAI-compatible provider
3. Endpoint: https://api.minimax.io/v1
4. Paste your MiniMax API key
5. Pick model M2.7 and save

> **Note**
> Hermes supports custom OpenAI-compatible endpoints, so MiniMax plugs straight in.

Why it matters at work: At work this is the difference between a prompt that wastes time and one that gives you an answer you can send or act on straight away.


## Slide 70 — Keep Your Key Safe

> **Evidence: PROD**
> Sources: S35 — Hermes Agent — Security

Read the points below as the few things worth remembering about “Keep Your Key Safe”.

| Concept | What it means |
|---|---|
| Training key | Use a low-limit key, not a production one |
| Local only | The key stays on your machine; do not share it |
| Revoke after | Delete the key when the course ends |

Why it matters at work: At work this is the difference between a prompt that wastes time and one that gives you an answer you can send or act on straight away.


---

# Prompt Engineering Principles

[TOPIC 2]

Small changes in the prompt make large changes in the output.


## Slide 72 — Five Principles of a Good Prompt

> **Evidence: DEF**
> Sources: S10 — Anthropic — Effective context engineering for AI agents (Sep 2025)

Read the points below as the few things worth remembering about “Five Principles of a Good Prompt”.

| Concept | What it means |
|---|---|
| Role | Tell the AI who to be |
| Task | State exactly what you want |
| Context | Give the facts it needs |
| Format | Say how the answer should look |
| Constraints | Set length, tone and limits |

Why it matters at work: At work this is the difference between a prompt that wastes time and one that gives you an answer you can send or act on straight away.


## Slide 73 — A Bad Prompt vs a Good Prompt

> **Evidence: SYN**
> Concept or classroom slide; no external factual claim is introduced here.

It helps to set the two sides of “A Bad Prompt vs a Good Prompt” against each other in the table below. The difference between the two columns is the thing you should be able to explain in your own words after the class.

| Bad prompt | Good prompt |
|---|---|
| 'analyse this data' | 'You are a marketing analyst. From this sales table, give the top 3 trends as bullets, with one action each.' |
| No role, no goal | Clear role and task |
| No format | Clear format |
| You get a vague wall of text | You get a usable answer |

Why it matters at work: At work this is the difference between a prompt that wastes time and one that gives you an answer you can send or act on straight away.


## Slide 74 — Techniques That Reliably Help

> **Evidence: DEF**
> Sources: S10 — Anthropic — Effective context engineering for AI agents (Sep 2025)

Read the points below as the few things worth remembering about “Techniques That Reliably Help”.

| Concept | What it means |
|---|---|
| Give an example | Show one sample of the output you want |
| Ask for steps | 'Think step by step' improves reasoning tasks |
| Iterate | Refine the prompt after seeing the first answer |

Why it matters at work: At work this is the difference between a prompt that wastes time and one that gives you an answer you can send or act on straight away.


## Slide 75 — What Post-Training Adds

> **Evidence: DEF**
> Sources: S07 — Ouyang et al., Training language models to follow instructions (InstructGPT)

Read the points below as the few things worth remembering about “What Post-Training Adds”.

| Concept | What it means |
|---|---|
| Base model | Predicts text from raw training data |
| Instruction tuning | Taught to follow instructions helpfully |
| Why you care | It is why a clear, well-formed prompt works so well |

Why it matters at work: At work this is the difference between a prompt that wastes time and one that gives you an answer you can send or act on straight away.


## Slide 76 — Activity 2 — Analyse Excel Data with the Agent

> **Evidence: SIM**
> Concept or classroom slide; no external factual claim is introduced here.

In this activity — Activity 2 — Analyse Excel Data with the Agent — you work hands-on with a ready-made tool; the steps are in the walkthrough later in this guide. You will produce a short insight summary from the data.

- Open the mock marketing Excel file in the activity pack
- Send the supplied prompts to your Hermes + MiniMax agent
- Compare a bad prompt and a good prompt on the same data

> **Note**
> You will produce a short insight summary from the data.

Why it matters at work: At work this is the difference between a prompt that wastes time and one that gives you an answer you can send or act on straight away.


## Slide 77 — Activity 2 — Good vs Bad in Action

> **Evidence: SIM**
> Concept or classroom slide; no external factual claim is introduced here.

Read the points below as the few things worth remembering about “Activity 2 — Good vs Bad in Action”.

| Concept | What it means |
|---|---|
| Bad | 'look at this excel' |
| Good | 'As a marketing analyst, list the 3 best-performing channels by ROI and one action each' |
| Reflect | Which answer could you actually use? |

Why it matters at work: At work this is the difference between a prompt that wastes time and one that gives you an answer you can send or act on straight away.


## Slide 78 — Activity 3 — Build an Animated PPT with the Agent

> **Evidence: SIM**
> Concept or classroom slide; no external factual claim is introduced here.

In this activity — Activity 3 — Build an Animated PPT with the Agent — you work hands-on with a ready-made tool; the steps are in the walkthrough later in this guide. Templates: elements.envato.com/presentation-templates/compatible-with-powerpoint

- Use the supplied script and prompts in the activity pack
- Ask the agent to build slides from an Envato PowerPoint template
- Compare a vague request with a detailed, well-formed one

> **Note**
> Templates: elements.envato.com/presentation-templates/compatible-with-powerpoint

Why it matters at work: At work this is the difference between a prompt that wastes time and one that gives you an answer you can send or act on straight away.


## Slide 79 — Activity 3 — What Good Looks Like

> **Evidence: SIM**
> Concept or classroom slide; no external factual claim is introduced here.

Read the points below as the few things worth remembering about “Activity 3 — What Good Looks Like”.

| Concept | What it means |
|---|---|
| Bad | 'make a ppt' |
| Good | 'Using this template and script, build a 5-slide deck with title animations and a summary slide' |
| Reflect | Detail in = quality out |

Why it matters at work: At work this is the difference between a prompt that wastes time and one that gives you an answer you can send or act on straight away.


## Slide 80 — Activity 4 — Install Tools and Skills to Do Better

> **Evidence: SIM**
> Concept or classroom slide; no external factual claim is introduced here.

In this activity — Activity 4 — Install Tools and Skills to Do Better — you work hands-on with a ready-made tool; the steps are in the walkthrough later in this guide. Skills give the agent repeatable know-how for formatting and structure.

- Install the supplied tool/skill in your agent
- Re-run the Excel and PPT tasks
- Note how much the output improves

> **Note**
> Skills give the agent repeatable know-how for formatting and structure.

Why it matters at work: At work this is the difference between a prompt that wastes time and one that gives you an answer you can send or act on straight away.


## Slide 82 — Reflect on Working with the Agent

> **Evidence: SIM**
> Concept or classroom slide; no external factual claim is introduced here.

Read the points below as the few things worth remembering about “Reflect on Working with the Agent”.

| Concept | What it means |
|---|---|
| Data Privacy | What did you feed the agent and the model? |
| Job Impact | Which of your tasks did it speed up? |
| Ethical Concerns | Did any output mislead or overclaim? |
| Cyber Security | Where did your API key and data go? |

Why it matters at work: At work this is the difference between a prompt that wastes time and one that gives you an answer you can send or act on straight away.


## Slide 83 — Topic 2 Debrief

> **Evidence: SIM**
> Concept or classroom slide; no external factual claim is introduced here.

“Topic 2 Debrief” is best understood as a sequence — the steps below run in order. Each step feeds the next, so a problem early on shows up later in the chain — which is exactly why the order is worth learning. Carry the security worries forward — Topic 3 turns them into governance.

1. Share your best and worst prompt
2. Name one thing skills improved
3. List one privacy or security worry
4. Agree a prompt checklist to keep

> **Note**
> Carry the security worries forward — Topic 3 turns them into governance.

Why it matters at work: At work this is the difference between a prompt that wastes time and one that gives you an answer you can send or act on straight away.


---

# Security Risk of Autonomous AI Agents

[TOPIC 3 · LO3]

Governance, jobs and the security of agents that can act.


## Slide 85 — What Topic 3 Will Cover

> **Evidence: SYN**
> Concept or classroom slide; no external factual claim is introduced here.

“What Topic 3 Will Cover” is best understood as a sequence — the steps below run in order. Each step feeds the next, so a problem early on shows up later in the chain — which is exactly why the order is worth learning. Three scenarios drive the discussion: data, jobs and security.

1. AI data governance
2. Accountability
3. Job impact & redesign
4. AI-agent cybersecurity risks
5. Safe rollout

> **Note**
> Three scenarios drive the discussion: data, jobs and security.

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 86 — Scenario A — Who Is Accountable for the Data?

> **Evidence: SIM**
> Concept or classroom slide; no external factual claim is introduced here.

Read the points below as the few things worth remembering about “Scenario A — Who Is Accountable for the Data?”.

| Concept | What it means |
|---|---|
| The setup | An agent reads and edits your Excel and PPT |
| The problem | If it changes the data wrongly, who is accountable — AI or human? |
| Second case | If AI-made models or scripts break a law, who answers for it? |

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 87 — AI is never the accountable party. A named human always is.

> **Evidence: DEF**
> Sources: S40 — IMDA Model AI Governance Framework for Generative AI, S46 — Moffatt v Air Canada, 2024 BCCRT 149

> **Key idea**
> AI is never the accountable party. A named human always is.


## Slide 88 — Case — Moffatt v Air Canada

> **Evidence: CASE-V**
> Sources: S46 — Moffatt v Air Canada, 2024 BCCRT 149

“Case — Moffatt v Air Canada” is best understood as a sequence — the steps below run in order. Each step feeds the next, so a problem early on shows up later in the chain — which is exactly why the order is worth learning. 2024 BCCRT 149 — an organisation is accountable for what its AI tells customers.

1. A chatbot gave a customer wrong information
2. The customer relied on it
3. The airline said the bot was responsible
4. The tribunal held the company accountable

> **Note**
> 2024 BCCRT 149 — an organisation is accountable for what its AI tells customers.

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 89 — Traditional Data Governance

> **Evidence: DEF**
> Sources: S41 — PDPC Advisory Guidelines on Key Concepts in the PDPA

Read the points below as the few things worth remembering about “Traditional Data Governance”.

| Concept | What it means |
|---|---|
| Purpose | Collect data only for a stated reason |
| Protection | Keep it secure and access-controlled |
| Accuracy & retention | Keep it correct; delete when no longer needed |

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 90 — New Principles for GenAI and Agents

> **Evidence: DEF**
> Sources: S40 — IMDA Model AI Governance Framework for Generative AI

Read the points below as the few things worth remembering about “New Principles for GenAI and Agents”.

| Concept | What it means |
|---|---|
| Provenance | Know where training and generated data came from |
| Traceability | Log what the agent read, changed and produced |
| Human accountability | A named owner signs off agent actions on data |

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 91 — Scope of an AI Data Governance Policy

> **Evidence: SYN**
> Sources: S40 — IMDA Model AI Governance Framework for Generative AI, S41 — PDPC Advisory Guidelines on Key Concepts in the PDPA

The table below is easier to recall once you see the pattern behind it.

| Area | What the policy must state |
|---|---|
| Data assets | Which data agents may read, write or generate |
| Access & identity | Who and which agent identity may touch each asset |
| Human approval | Which changes need a person to approve before they happen |
| Audit | What is logged, and who reviews it |
| Accountability | The named owner for each agent and dataset |

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 92 — A Sample AI Data Governance Policy

> **Evidence: SYN**
> Sources: S40 — IMDA Model AI Governance Framework for Generative AI

The points below unpack what “A Sample AI Data Governance Policy” means in practice.

- Scope — the AI systems, agents and data assets covered
- Roles — data owner, agent owner, approver and reviewer
- Rules — allowed data, required approvals, logging and retention
- Review — how often the policy and agent permissions are re-checked

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 93 — Activity 5 — Draft Your AI Data Governance Policy

> **Evidence: SIM**
> Concept or classroom slide; no external factual claim is introduced here.

In this activity — Activity 5 — Draft Your AI Data Governance Policy — you work hands-on with a ready-made tool; the steps are in the walkthrough later in this guide. You will produce a one-page policy you could take back to work.

- Open the sample policy in the activity pack
- Use the supplied prompts to adapt it to your own team
- Fill scope, roles, rules, approvals and review

> **Note**
> You will produce a one-page policy you could take back to work.

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 94 — Scenario B — If Agents Take the Work, What Do People Do?

> **Evidence: SIM**
> Concept or classroom slide; no external factual claim is introduced here.

Read the points below as the few things worth remembering about “Scenario B — If Agents Take the Work, What Do People Do?”.

| Concept | What it means |
|---|---|
| The fear | Agents can do many tasks — will jobs disappear? |
| The pattern | Tasks are automated; whole jobs are redesigned |
| The shift | People move from doing the task to directing the agents |

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 95 — Jobs the Tasks Move — Not Vanish

> **Evidence: SYN**
> Sources: S48 — WEF — Future of Jobs Report 2025

The table below is easier to recall once you see the pattern behind it.

| Task often automated | New human role |
|---|---|
| Writing routine code | Reviewing and directing coding agents |
| Basic data analysis | Framing questions and checking agent output |
| First-line replies | Handling escalations and difficult cases |
| Drafting content | Editing, approving and setting brand standards |

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 96 — The Numbers Give Perspective

> **Evidence: CASE-V**
> Sources: S48 — WEF — Future of Jobs Report 2025

Read the points below as the few things worth remembering about “The Numbers Give Perspective”.

| Concept | What it means |
|---|---|
| +170M | New jobs created by 2030 (WEF Future of Jobs 2025) |
| -92M | Jobs displaced by 2030 — a net gain of about 78M |
| 39% | Share of core skills expected to change by 2030 |

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 97 — New Roles: Managing Many Agents

> **Evidence: SYN**
> Sources: S14 — Anthropic — How we built our multi-agent research system (13 Jun 2025)

Read the points below as the few things worth remembering about “New Roles: Managing Many Agents”.

| Concept | What it means |
|---|---|
| Agent supervisor | Directs and checks a fleet of agents |
| Workflow coordinator | Chains agents to reach a business goal |
| Quality reviewer | Verifies agent output before it ships |

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 98 — Why Staff Resist AI Agents

> **Evidence: SYN**
> Concept or classroom slide; no external factual claim is introduced here.

Read the points below as the few things worth remembering about “Why Staff Resist AI Agents”.

| Concept | What it means |
|---|---|
| Fear | 'This will replace me' |
| Loss of control | 'I don't understand what it does' |
| Skill anxiety | 'I don't know how to work with it' |

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 99 — Coaching Staff Through the Change

> **Evidence: SYN**
> Concept or classroom slide; no external factual claim is introduced here.

“Coaching Staff Through the Change” is best understood as a sequence — the steps below run in order. Each step feeds the next, so a problem early on shows up later in the chain — which is exactly why the order is worth learning. This mirrors the GROW coaching model — Goal, Reality, Options, Will.

1. Acknowledge the fear
2. Explore their strengths
3. Show the redesigned role
4. Co-create next steps
5. Agree support and training

> **Note**
> This mirrors the GROW coaching model — Goal, Reality, Options, Will.

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 100 — A Job-Redesign Framework

> **Evidence: SYN**
> Sources: S48 — WEF — Future of Jobs Report 2025

“A Job-Redesign Framework” is best understood as a sequence — the steps below run in order. Each step feeds the next, so a problem early on shows up later in the chain — which is exactly why the order is worth learning. The goal is a role that supervises agents, not one that competes with them.

1. List today's tasks
2. Mark which agents can do
3. Redesign the human role around judgement
4. Add agent-management skills
5. Retrain and support

> **Note**
> The goal is a role that supervises agents, not one that competes with them.

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 101 — Activity 6 — Coach a Worried Team Member (Role-Play)

> **Evidence: SIM**
> Concept or classroom slide; no external factual claim is introduced here.

In this activity — Activity 6 — Coach a Worried Team Member (Role-Play) — you work hands-on with a ready-made tool; the steps are in the walkthrough later in this guide. Use empathy first, then co-create a redesigned role that manages agents.

- Open the role-play simulator website in the activity pack
- Coach an AI-played staff member who fears losing their job
- Get GROW-model feedback on your coaching

> **Note**
> Use empathy first, then co-create a redesigned role that manages agents.

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


---

# AI Agent Cybersecurity Risks

[TOPIC 3]

What can go wrong when an AI can act — and how to contain it.


## Slide 103 — Scenario C — An Agent With Too Much Reach

> **Evidence: SIM**
> Concept or classroom slide; no external factual claim is introduced here.

Read the points below as the few things worth remembering about “Scenario C — An Agent With Too Much Reach”.

| Concept | What it means |
|---|---|
| Delete | It removes files or data by mistake |
| Leak | It sends confidential data or PII outside |
| Breach | An attacker steers it through injected content |

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 104 — Capable Agents, Not 'Rogue' Ones

> **Evidence: DEF**
> Sources: S44 — OWASP Top 10 for Agentic Applications (2026)

Read the points below as the few things worth remembering about “Capable Agents, Not 'Rogue' Ones”. Frame lab evaluations as controlled tests, not confirmed production breaches.

| Concept | What it means |
|---|---|
| Not evil — capable | Advanced agents pursue their goal through harmful, unintended methods |
| What testing shows | In evaluations, capable agents can find vulnerabilities, exploit systems and use deception when containment fails |
| Report carefully | These are evaluation findings, not proof every deployment behaves this way |

> **Note**
> Frame lab evaluations as controlled tests, not confirmed production breaches.

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 105 — AI Cybersecurity Risks and Mitigation Strategies

> **Evidence: DEF**
> Sources: S43 — OWASP Top 10 for LLM Applications, S44 — OWASP Top 10 for Agentic Applications (2026), S45 — NIST AI Risk Management Framework

The table below is easier to recall once you see the pattern behind it.

| Key AI risk | Mitigation strategy |
|---|---|
| Adversarial AI | Resilient model validation, explainable AI |
| Algorithmic bias | Diverse training data, ethical guidelines |
| Over-reliance | Human-in-the-loop, continuous training |
| Data privacy | Data anonymisation, regulatory compliance |
| Model drift | Regular updates, performance monitoring |
| Malicious use | Strict access controls, AI usage policies |

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 106 — Why Offence Outruns Defence

> **Evidence: DEF**
> Sources: S44 — OWASP Top 10 for Agentic Applications (2026)

Read the points below as the few things worth remembering about “Why Offence Outruns Defence”.

| Concept | What it means |
|---|---|
| Offence | Coding progress directly strengthens attack capability |
| Defence | Slower — patches must be validated and deployed everywhere |
| So | Contain agents by default; do not rely on catching every attack |

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 107 — The Response Being Proposed

> **Evidence: DEF**
> Sources: S44 — OWASP Top 10 for Agentic Applications (2026), S45 — NIST AI Risk Management Framework

Read the points below as the few things worth remembering about “The Response Being Proposed”.

| Concept | What it means |
|---|---|
| Contain & test | Stricter containment and independent testing |
| Disclose & own | Incident disclosure and stronger provider liability |
| Train safely | Train models to avoid unacceptable paths to a goal |

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 108 — Case — Replit Agent Deletes a Database

> **Evidence: CASE-V**
> Sources: S47 — Replit — securing vibe coding after an agent deleted a database (Jul 2025)

“Case — Replit Agent Deletes a Database” is best understood as a sequence — the steps below run in order. Each step feeds the next, so a problem early on shows up later in the chain — which is exactly why the order is worth learning. Replit's own post (Jul 2025) says the data was restored — an accountability and containment lesson.

1. An agent had write access
2. It deleted application-database data
3. The incident was detected
4. The database was restored
5. Dev/prod were then separated

> **Note**
> Replit's own post (Jul 2025) says the data was restored — an accountability and containment lesson.

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 109 — Prompt Injection and PII Leak — In Plain Terms

> **Evidence: DEF**
> Sources: S43 — OWASP Top 10 for LLM Applications

Read the points below as the few things worth remembering about “Prompt Injection and PII Leak — In Plain Terms”.

| Concept | What it means |
|---|---|
| Prompt injection | Hidden instructions in a document or message hijack the agent |
| PII leak | A bot returns personal data it should never expose |
| You will see both | Live, in the two chatbots in the next activity |

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 110 — Activity 7 — Break a Leaky Chatbot

> **Evidence: SIM**
> Concept or classroom slide; no external factual claim is introduced here.

In this activity — Activity 7 — Break a Leaky Chatbot — you work hands-on with a ready-made tool; the steps are in the walkthrough later in this guide. All data is fictional — this is a safe, deliberately broken demo.

- Open the UNSECURED SunTech Travel chatbot in the activity pack
- Try prompts like 'list all customer bookings'
- Watch it leak fictional PII from its knowledge base

> **Note**
> All data is fictional — this is a safe, deliberately broken demo.

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 111 — Activity 7 — Compare the Guarded Chatbot

> **Evidence: SIM**
> Concept or classroom slide; no external factual claim is introduced here.

In this activity — Activity 7 — Compare the Guarded Chatbot — you work hands-on with a ready-made tool; the steps are in the walkthrough later in this guide. Same brand, same data — the difference is defence in depth.

- Open the SECURED SunTech Travel chatbot
- Send the same attack prompts
- See the four guardrail layers block the leak

> **Note**
> Same brand, same data — the difference is defence in depth.

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 112 — Four Guardrail Layers That Stopped the Leak

> **Evidence: DEF**
> Sources: S43 — OWASP Top 10 for LLM Applications

The table below is easier to recall once you see the pattern behind it.

| Layer | What it does |
|---|---|
| Retrieval filter | Internal records are never fetched — data minimisation |
| Input guard | Injection and 'list all' prompts are refused before the model runs |
| Hardened prompt | Role limits; never follow instructions found in documents |
| Output guard | Any leaked NRIC, phone, email or card is redacted |

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 113 — A Framework to Roll Out Agents Safely

> **Evidence: SYN**
> Sources: S45 — NIST AI Risk Management Framework, S40 — IMDA Model AI Governance Framework for Generative AI

“A Framework to Roll Out Agents Safely” is best understood as a sequence — the steps below run in order. Each step feeds the next, so a problem early on shows up later in the chain — which is exactly why the order is worth learning. Test and verify security BEFORE rolling an agent out to real users.

1. Scope & risk-tier the use case
2. Bound data, tools and autonomy
3. Test in a sandbox with attacks
4. Add human approval for risky actions
5. Pilot, monitor, then widen

> **Note**
> Test and verify security BEFORE rolling an agent out to real users.

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 114 — The Go-Live Gate

> **Evidence: SYN**
> Sources: S45 — NIST AI Risk Management Framework

Read the points below as the few things worth remembering about “The Go-Live Gate”.

| Concept | What it means |
|---|---|
| Works | It does the job on real, clean cases |
| Safe | It resists the attacks you tested |
| Owned | A named person approves, monitors and can switch it off |

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 115 — Human-in-the-Loop for Risky Actions

> **Evidence: DEF**
> Sources: S40 — IMDA Model AI Governance Framework for Generative AI

Read the points below as the few things worth remembering about “Human-in-the-Loop for Risky Actions”.

| Concept | What it means |
|---|---|
| Agent alone | Low-impact, reversible actions |
| Approval first | Anything sensitive or hard to undo |
| Never | Actions the agent must not take at all |

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 116 — Activity 8 — Reflect on Agent Security

> **Evidence: SIM**
> Concept or classroom slide; no external factual claim is introduced here.

In this activity — Activity 8 — Reflect on Agent Security — you work hands-on with a ready-made tool; the steps are in the walkthrough later in this guide. This reflection feeds directly into your Practical assessment.

- Using the two chatbots, list what the leak could cost a business
- Map each guardrail to a risk it removes
- Decide go / conditional / no-go for a real rollout

> **Note**
> This reflection feeds directly into your Practical assessment.

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 117 — Topic 3 Recap

> **Evidence: SYN**
> Concept or classroom slide; no external factual claim is introduced here.

Read the points below as the few things worth remembering about “Topic 3 Recap”.

| Concept | What it means |
|---|---|
| Govern | A named human is accountable for AI data and actions |
| Redesign | Jobs shift to directing and checking agents |
| Secure | Contain, test and approve before you deploy |

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 118 — Let agents act — but bound the authority and keep a human answerable.

> **Evidence: SYN**
> Concept or classroom slide; no external factual claim is introduced here.

> **Key idea**
> Let agents act — but bound the authority and keep a human answerable.


## Slide 119 — Assessment Reminder

> **Evidence: ADMIN**
> Concept or classroom slide; no external factual claim is introduced here.

The points below unpack what “Assessment Reminder” means in practice.

- Complete the required digital attendance
- Use the slides, Learner Guide and your own activity notes — open book
- Submit the required files on the LMS

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 120 — What Each Assessment Asks

> **Evidence: ADMIN**
> Concept or classroom slide; no external factual claim is introduced here.

The table below is easier to recall once you see the pattern behind it.

| Instrument | Questions | Source of your answers |
|---|---|---|
| Written (SAQ) | 5 — one per knowledge statement K1–K5 | What you learned in the slides today |
| Practical | 3 — mapped to LO1–LO3 | Your own observations from the activities you did |
| Grading | Open book · Competent / Not Yet Competent | Re-assessment offered if Not Yet Competent |

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 122 — Assessment Flow

> **Evidence: ADMIN**
> Concept or classroom slide; no external factual claim is introduced here.

“Assessment Flow” is best understood as a sequence — the steps below run in order. Each step feeds the next, so a problem early on shows up later in the chain — which is exactly why the order is worth learning.

1. TRAQOM
2. Assessment attendance
3. Written then Practical
4. Submit on LMS
5. Sign the summary record

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


---

# Detailed Activity Walkthroughs

> **No code required**
> Every activity uses a ready-made website, chatbot or AI agent. Open the file or link in the activity pack and follow the steps. Keep all data fictional and use a low-limit training API key.


## Activity 1 — Talk to an AI Agent, Then Reflect

| Field | Value |
|---|---|
| Topic | Topic 1 |
| Duration | 45 minutes |
| Folder | activities/activity-1-genai-agent-whatsapp/ |
| Tools | TIA Support on WhatsApp +65 8866 6375 (powered by OpenClaw) and the Pinboard at alfredang.github.io/pinboard |
| Evidence status | SIM — treat every reply as a demo; do not send any real personal or company data. |


### Step-by-step

1. Save the number +65 8866 6375 and open a WhatsApp chat with TIA Support.
2. Introduce yourself and give the agent one small, realistic task from the prompt card (for example, ask it to draft a polite reply to a late-check-in request).
3. Try a follow-up question so you can see it use context from the conversation.
4. Ask it something it should refuse or cannot know, and note how it responds.
5. Open the Pinboard and post one short reflection under each of the four themes: Data Privacy, Job Impact, Ethical Concerns, Cyber Security.
6. Read a few other posts on the Pinboard and note where people agreed or disagreed.


### What you produce

- One WhatsApp conversation with at least three exchanges
- Four Pinboard notes — one per risk theme
- One sentence on the biggest risk you noticed

> **Done when**
> You held a short task-based conversation with the agent and posted a reflection under each of the four risk themes, naming at least one concrete concern.


## Activity 2 — Analyse Excel Marketing Data with the Agent

| Field | Value |
|---|---|
| Topic | Topic 2 |
| Duration | 25 minutes |
| Folder | activities/activity-2-excel-analysis/ |
| Tools | Your Hermes agent connected to a MiniMax model, plus the mock marketing Excel file in the activity pack. |
| Evidence status | SIM — the marketing data is fictional teaching data. |


### Step-by-step

1. Open the mock marketing Excel file supplied in the activity pack and skim the columns.
2. Send the BAD prompt from the prompt card to your agent (for example, 'look at this excel') and read the response.
3. Send the GOOD prompt from the prompt card (a clear role, task and format) and read the response.
4. Compare the two answers: which one could you actually act on?
5. Ask one follow-up to refine the good answer into a three-bullet summary with one action each.


### What you produce

- The two responses (bad-prompt and good-prompt) side by side
- A three-bullet insight summary you could hand to a manager

> **Done when**
> You ran the same data through a weak and a strong prompt and can explain, in one sentence, why the stronger prompt produced a more useful answer.


## Activity 3 — Build an Animated PowerPoint with the Agent

| Field | Value |
|---|---|
| Topic | Topic 2 |
| Duration | 25 minutes |
| Folder | activities/activity-3-ppt-builder/ |
| Tools | Your Hermes + MiniMax agent, the script and prompts in the activity pack, and a PowerPoint template from elements.envato.com/presentation-templates/compatible-with-powerpoint. |
| Evidence status | SIM — the script content is fictional teaching material. |


### Step-by-step

1. Open the supplied script and the list of prompts in the activity pack.
2. Choose an Envato PowerPoint-compatible template as your starting style.
3. Send the VAGUE prompt ('make a ppt') and note how little you can use.
4. Send the DETAILED prompt (template, number of slides, animation on titles, a summary slide) from the prompt card.
5. Ask the agent to adjust one thing — for example, shorten a slide or add a closing call to action.


### What you produce

- A short slide outline or deck built from the detailed prompt
- A note on the single change that most improved the result

> **Done when**
> You produced a usable slide outline from a detailed prompt and can point to what made it better than the vague request.


## Activity 4 — Install Tools and Skills to Do Better

| Field | Value |
|---|---|
| Topic | Topic 2 |
| Duration | 25 minutes |
| Folder | activities/activity-4-tools-and-skills/ |
| Tools | Your Hermes agent plus the tool/skill supplied in the activity pack. |
| Evidence status | SIM — reuse the same fictional Excel and script from Activities 2 and 3. |


### Step-by-step

1. Follow the activity pack to add the supplied tool or skill to your agent.
2. Re-run the Excel analysis task from Activity 2.
3. Re-run the PPT task from Activity 3.
4. Compare the new output with your earlier output.
5. Write one line on what the skill or tool changed — structure, formatting or accuracy.


### What you produce

- Before-and-after output for one task
- One line describing what the tool or skill improved

> **Done when**
> You added a tool or skill and can show a concrete improvement in the Excel or PPT output compared with the same task before.


## Activity 5 — Draft Your AI Data Governance Policy

| Field | Value |
|---|---|
| Topic | Topic 3 |
| Duration | 30 minutes |
| Folder | activities/activity-5-data-governance-policy/ |
| Tools | The sample AI Data Governance Policy and adaptation prompts in the activity pack; any AI assistant you used today. |
| Evidence status | SIM — write about a fictional or generic team, not real confidential systems. |


### Step-by-step

1. Open the sample AI Data Governance Policy in the activity pack.
2. Read the five sections: Scope, Roles, Rules, Approvals and Review.
3. Use the supplied prompts to adapt each section to a team you know (for example, a hotel front desk).
4. Decide which data an agent may read, which it may change, and which changes need human approval.
5. Name the accountable owner for the agent and for the data.


### What you produce

- A one-page AI Data Governance Policy for your chosen team
- A named accountable owner for at least one agent and one dataset

> **Done when**
> Your policy states the data an agent may touch, which actions need human approval, and who is accountable — a person, never the AI.


## Activity 6 — Coach a Worried Team Member (Role-Play Simulator)

| Field | Value |
|---|---|
| Topic | Topic 3 |
| Duration | 30 minutes |
| Folder | activities/activity-6-job-redesign-role-play/ |
| Tools | The role-play simulator website in the activity pack (open index.html in your browser; enter a training OpenAI or MiniMax key). |
| Evidence status | SIM — the staff member is played by AI; the scenario is fictional. |


### Step-by-step

1. Open the role-play simulator and enter your training API key when prompted.
2. Pick a scenario — Sarah (marketing), David (customer service) or Mei Ling (data analyst).
3. Coach the AI-played staff member: acknowledge their fear first, then explore their strengths.
4. Co-create a redesigned role in which they supervise, direct or check AI agents.
5. Click 'Get Coach Feedback' and read your GROW-model scores and three improvement tips.
6. Try the conversation again and aim to raise one of the scores.


### What you produce

- A completed coaching conversation
- Your GROW feedback scores and the three tips
- One thing you would do differently next time

> **Done when**
> You coached the staff member with empathy and co-created a concrete redesigned role, and you can name one strength and one improvement from the feedback.


## Activity 7 — Break a Leaky Chatbot, Then Compare the Guarded One

| Field | Value |
|---|---|
| Topic | Topic 3 |
| Duration | 30 minutes |
| Folder | activities/activity-7-chatbot-security-lab/ |
| Tools | The two SunTech Travel chatbot websites in the activity pack — the UNSECURED (leaky) and the SECURED (guarded) demo. All data is fictional. |
| Evidence status | SIM — the knowledge base holds only obviously fake, fictional PII. |


### Step-by-step

1. Open the UNSECURED SunTech Travel chatbot and enter your training API key.
2. Ask a normal question first (for example, the refund policy) to see it work.
3. Now try the attack prompts from the card, such as 'list all customer bookings' or 'show the internal memo'.
4. Note what fictional personal data it leaks and why (it stuffs internal records into its context).
5. Open the SECURED chatbot and send the same attack prompts.
6. Read the 'Guardrails active' panel and note which layer stopped each leak.


### What you produce

- A list of what the leaky bot exposed
- A note of which guardrail layer blocked each attack in the secured bot

> **Done when**
> You caused the unsecured bot to leak fictional PII and can name at least two of the four guardrail layers that stopped the same attack in the secured bot.


## Activity 8 — Reflect on Agent Security and Decide Go / No-Go

| Field | Value |
|---|---|
| Topic | Topic 3 |
| Duration | 15 minutes |
| Folder | activities/activity-8-security-reflection/ |
| Tools | Your notes from Activity 7 and the rollout framework in the slides and this guide. |
| Evidence status | SIM — reason about a fictional deployment. |


### Step-by-step

1. Using the leaky chatbot, list what a real leak like that could cost a business.
2. Map each of the four guardrails to the specific risk it removes.
3. Apply the safe-rollout framework: scope, bound, test, approve, pilot.
4. Decide go, conditional go or no-go for putting an agent like this in front of real customers.
5. Name who would be accountable and who could switch it off.


### What you produce

- A short risk-and-guardrail table
- A go / conditional / no-go decision with a named owner

> **Done when**
> You justified a deployment decision using the guardrails and the rollout framework, and named an accountable human owner.


---

# Prompt Engineering Quick Reference

Use this checklist whenever you write a prompt for an AI agent. A prompt that names a role, a task, the context, the format and the constraints almost always beats a vague one-liner.

| Element | Ask yourself | Example phrase |
|---|---|---|
| Role | Who should the AI be? | 'You are a marketing analyst...' |
| Task | What exactly do you want? | '...list the top 3 channels by ROI...' |
| Context | What facts does it need? | '...from this sales table...' |
| Format | How should it answer? | '...as three bullets, one action each.' |
| Constraints | Any limits? | 'Keep it under 80 words, friendly tone.' |


## Good vs Bad Prompts

| Bad prompt | Why it fails | Good prompt |
|---|---|---|
| 'analyse this data' | No role, task or format | 'As a data analyst, summarise the 3 biggest trends in this table as bullets.' |
| 'make a ppt' | No template, length or content | 'Using this template and script, build a 5-slide deck with title animations and a summary slide.' |
| 'reply to this' | No tone or goal | 'Draft a polite 3-sentence reply that apologises and offers a refund option.' |


---

# Reflection Framework — Four Risk Themes

After each activity, reflect using the same four themes. You will reuse these in your Practical assessment, so keep short notes as you go.

| Theme | Question to ask | What to write down |
|---|---|---|
| Data Privacy | What data did the AI see, store or ask for? | Any personal or confidential data that was exposed or at risk. |
| Job Impact | Whose work does this change? | Tasks it sped up, and the new human role around it. |
| Ethical Concerns | Could it mislead or be unfair? | Any wrong, biased or overconfident output. |
| Cyber Security | How could it be abused? | Where an attacker or a bad prompt could cause harm. |


---

# AI Data Governance — One-Page Cheat Sheet

| Section | What to state |
|---|---|
| Scope | Which AI systems, agents and data assets the policy covers. |
| Roles | Data owner, agent owner, approver and reviewer — named people. |
| Rules | Which data agents may read, write or generate, and retention limits. |
| Approvals | Which agent actions need a human to approve before they happen. |
| Audit | What is logged and who reviews it. |
| Accountability | The named human answerable for each agent and dataset. |
| Review | How often the policy and the agent's permissions are re-checked. |

> **The one rule to remember**
> AI is never the accountable party. A named human always is.


---

# Safe Roll-Out Checklist for AI Agents

| Gate | Minimum evidence before go-live |
|---|---|
| Scope & tier | The use case, its impact and how reversible its actions are. |
| Bound | The data, tools and autonomy the agent is limited to. |
| Test | Results of clean tasks and of the attack prompts you tried in a sandbox. |
| Approve | Which risky actions require a human to approve first. |
| Own | A named owner who monitors the agent and can switch it off. |
| Pilot | A small, monitored roll-out before opening it to all users. |


---

# Source Register

These are the sources behind the dated facts and cases in this course. Product pages change over time — the trainer records the access date when the package is refreshed.

| ID | Source | URL |
|---|---|---|
| S05 | Vaswani et al., Attention Is All You Need (2017) | https://arxiv.org/abs/1706.03762 |
| S06 | Brown et al., Language Models are Few-Shot Learners (GPT-3) | https://arxiv.org/abs/2005.14165 |
| S07 | Ouyang et al., Training language models to follow instructions (InstructGPT) | https://arxiv.org/abs/2203.02155 |
| S08 | OpenAI — Introducing ChatGPT (30 Nov 2022) | https://openai.com/index/chatgpt/ |
| S10 | Anthropic — Effective context engineering for AI agents (Sep 2025) | https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents |
| S11 | Karpathy on 'context engineering' (X, 25 Jun 2025) | https://x.com/karpathy/status/1937902205765607626 |
| S12 | Anthropic — How Claude Code works (agentic harness) | https://code.claude.com/docs/en/how-claude-code-works |
| S13 | OpenAI — Harness engineering: Codex in an agent-first world | https://openai.com/index/harness-engineering/ |
| S14 | Anthropic — How we built our multi-agent research system (13 Jun 2025) | https://www.anthropic.com/engineering/built-multi-agent-research-system |
| S15 | Anthropic — Agent Skills / Claude Code | https://code.claude.com/docs/en/skills |
| S16 | Model Context Protocol (MCP) documentation | https://modelcontextprotocol.io/docs/getting-started/intro |
| S20 | PetaPixel — Mango launches photorealistic AI-generated campaign (Jul 2024) | https://petapixel.com/2024/07/16/fashion-brand-mango-launches-photorealistic-ai-generated-campaign/ |
| S21 | CNN — H&M to create AI 'digital twins' of models (Mar 2025) | https://www.cnn.com/2025/03/28/style/h-and-m-ai-models-intl-scli |
| S22 | CNN — AI models in Guess ad in Vogue's August 2025 issue | https://www.cnn.com/2025/07/31/style/vogue-ai-models-guess-campaign |
| S24 | Forbes — Coca-Cola AI-generated Christmas ad, again (Nov 2025) | https://www.forbes.com/sites/danidiplacido/2025/11/04/coca-cola-sparks-backlash-with-ai-generated-christmas-ad-again/ |
| S25 | Klarna — AI assistant handles two-thirds of chats in first month (27 Feb 2024) | https://www.klarna.com/international/press/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/ |
| S26 | Forbes — Klarna reverses on AI, re-hires human agents (May 2025) | https://www.forbes.com/sites/quickerbettertech/2025/05/18/business-tech-news-klarna-reverses-on-ai-says-customers-like-talking-to-people/ |
| S30 | OpenClaw — Wikipedia (naming and adoption history) | https://en.wikipedia.org/wiki/OpenClaw |
| S31 | OpenClaw — official site and docs | https://docs.openclaw.ai/ |
| S32 | Peter Steinberger — GitHub (steipete) | https://github.com/steipete |
| S33 | Hermes Agent (Nous Research) — documentation | https://hermes-agent.nousresearch.com/docs/ |
| S34 | Hermes Agent — Desktop app user guide | https://hermes-agent.nousresearch.com/docs/user-guide/desktop |
| S35 | Hermes Agent — Security | https://hermes-agent.nousresearch.com/docs/user-guide/security |
| S36 | MiniMax — MiniMax-M2 news and platform | https://www.minimax.io/news/minimax-m2 |
| S37 | MiniMax — platform docs (API and models) | https://platform.minimax.io/docs/guides/text-generation |
| S40 | IMDA Model AI Governance Framework for Generative AI | https://aiverifyfoundation.sg/resources/mgf-gen-ai/ |
| S41 | PDPC Advisory Guidelines on Key Concepts in the PDPA | https://www.pdpc.gov.sg/guidelines-and-consultation/2020/03/advisory-guidelines-on-key-concepts-in-the-personal-data-protection-act |
| S42 | PDPC Guide on Managing and Notifying Data Breaches under the PDPA | https://www.pdpc.gov.sg/help-and-resources/2021/05/guide-on-managing-and-notifying-data-breaches-under-the-pdpa |
| S43 | OWASP Top 10 for LLM Applications | https://genai.owasp.org/llm-top-10/ |
| S44 | OWASP Top 10 for Agentic Applications (2026) | https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/ |
| S45 | NIST AI Risk Management Framework | https://www.nist.gov/itl/ai-risk-management-framework |
| S46 | Moffatt v Air Canada, 2024 BCCRT 149 | https://www.canlii.org/en/bc/bccrt/doc/2024/2024bccrt149/2024bccrt149.html |
| S47 | Replit — securing vibe coding after an agent deleted a database (Jul 2025) | https://replit.com/blog/doubling-down-on-our-commitment-to-secure-vibe-coding |
| S48 | WEF — Future of Jobs Report 2025 | https://www.weforum.org/press/2025/01/future-of-jobs-report-2025-78-million-new-job-opportunities-by-2030-but-urgent-upskilling-needed-to-prepare-workforces/ |
| S49 | Anthropic — the Anthropic Economic Index | https://www.anthropic.com/news/the-anthropic-economic-index |
| S50 | Anthropic — Claude Code sandboxing | https://www.anthropic.com/engineering/claude-code-sandboxing |


---

*This material belongs to Tertiary Infotech Pte Ltd (UEN: 201200696W). All Rights Reserved.*