# AI Security for Autonomous AI Agents — Learner Guide

**Course Code:** TGS-2025060473  |  **TSC:** Generative AI Principles and Applications (ICT-INT-0052-1.1)  
**Version:** 4.15  |  **Date:** 26 August 2026  |  **Duration:** 1 Day · 8 Hours

> This guide mirrors the Learner Guide DOCX exactly. Both are generated from `v40_learner.py`.

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
| LO1 | Demonstrate generative AI concepts and applications relevant to customer service and hospitality management |
| LO2 | Apply prompt engineering techniques and analyse output variations to improve generative AI performance in service settings |
| LO3 | Identify ethical risks and analyse bias in AI-generated content used in customer engagement |

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


## Slide 9 — Briefing for Assessment

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


## Slide 10 — How the Day Is Assessed

> **Evidence: ADMIN**
> Concept or classroom slide; no external factual claim is introduced here.

The table below is easier to recall once you see the pattern behind it.

| Instrument | Covers | What you do |
|---|---|---|
| Written Assessment (SAQ) | K1–K5 | Five short written answers, one per knowledge statement |
| Case Study | LO1–LO3 (A1–A5) | Three reflection tasks (two questions each) on the activities you completed today |
| Format | — | Open book · Competent / Not Yet Competent |

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

“2024 — Context Engineering” is worth a closer look.

- ('Beyond the prompt', 'The model also needs the right supporting information')
- ('The context window', 'Instructions, history, memory, tools and retrieved data meet here')
- ('The craft', "Select just the right tokens for the model's next step")

Why it matters at work: In a customer-service or hospitality setting, this shapes how you brief an AI tool and how much you trust its answer before it reaches a guest.


## Slide 18 — 2025 — Harness Engineering and Agentic AI

> **Evidence: HIST**
> Sources: S12 — Anthropic — How Claude Code works (agentic harness), S13 — OpenAI — Harness engineering: Codex in an agent-first world

“2025 — Harness Engineering and Agentic AI” is worth a closer look.

- ('Loop', 'Gather context, plan, act and verify until the goal is met')
- ('Tools', 'The harness gives the model controlled ways to affect real systems')
- ('Safety', 'Permissions, sandboxes and verification constrain each action')

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


## Slide 26 — Probabilistic Output — Why Traditional Security Struggles

> **Evidence: DEF**
> Sources: S43 — OWASP Top 10 for LLM Applications

It helps to set the two sides of “Probabilistic Output — Why Traditional Security Struggles” against each other in the table below. The difference between the two columns is the thing you should be able to explain in your own words after the class. You cannot write a rule for every possible answer — so security must also watch what the model says and does, not just what goes in.

| Traditional software | A large language model |
|---|---|
| Deterministic — the same input always produces the same output | Probabilistic — the same prompt can produce a different answer every run |
| Behaviour can be fully tested before release | The space of possible outputs can never be fully tested |
| Firewalls and filters match known, fixed patterns | There is no fixed signature — a harmful answer can look new every time |
| An unexpected output is a bug you can reproduce and patch | An unexpected output is normal behaviour, not a fault |

> **Note**
> You cannot write a rule for every possible answer — so security must also watch what the model says and does, not just what goes in.

Why it matters at work: In a customer-service or hospitality setting, this shapes how you brief an AI tool and how much you trust its answer before it reaches a guest.


---

# Generative AI in the Real World

[TOPIC 1]

Real, dated examples — how generation is already changing work.


## Slide 28 — Fashion Models Are Now Generated

> **Evidence: CASE-V**
> Sources: S20 — PetaPixel — Mango launches photorealistic AI-generated campaign (Jul 2024), S21 — Process Excellence Network — H&M debuts AI 'digital twins' of models (Mar 2025), S22 — ABC News — AI-generated models in Guess ad in Vogue (Aug 2025)

“Fashion Models Are Now Generated” is worth a closer look.

Why it matters at work: In a customer-service or hospitality setting, this shapes how you brief an AI tool and how much you trust its answer before it reaches a guest.


## Slide 29 — AI-Generated Video Is Overtaking Whole Industries

> **Evidence: SYN**
> Concept or classroom slide; no external factual claim is introduced here.

“AI-Generated Video Is Overtaking Whole Industries” is worth a closer look. The clip is embedded — click it and press Play in slideshow.

- ('Music', 'This AI-generated singer — no camera, cast or crew — shows how AI is reshaping the music industry')
- ('Three industries', 'The next three demos show marketing, film and how fast this is moving')
- ('Made for feeds', 'Vertical clips like this are built for TikTok, Reels and YouTube Shorts')
- ('For your team', 'Ask: where could you use this, and where would you not?')

> **Note**
> The clip is embedded — click it and press Play in slideshow.

Why it matters at work: In a customer-service or hospitality setting, this shapes how you brief an AI tool and how much you trust its answer before it reaches a guest.


## Slide 30 — AI in Marketing and Advertising

> **Evidence: SYN**
> Concept or classroom slide; no external factual claim is introduced here.

“AI in Marketing and Advertising” is worth a closer look. Embedded clip — click and press Play. Discuss: would you trust an all-AI ad for your brand?

- ('Campaign in hours', 'Brands now generate ad and campaign video in hours, not weeks')
- ('No production crew', 'No shoot, studio, cast or location — just a prompt and a model')
- ('Coca-Cola', "Aired an AI-generated 'Holidays Are Coming' ad in 2024 and again in 2025")
- ('Watch for', 'Brand risk, authenticity and disclosure when the whole ad is synthetic')

> **Note**
> Embedded clip — click and press Play. Discuss: would you trust an all-AI ad for your brand?

Why it matters at work: In a customer-service or hospitality setting, this shapes how you brief an AI tool and how much you trust its answer before it reaches a guest.


## Slide 31 — AI in Film and Movies

> **Evidence: SYN**
> Concept or classroom slide; no external factual claim is introduced here.

“AI in Film and Movies” is worth a closer look. Embedded clip — click and press Play. Discuss: what does this mean for creative jobs?

- ('Into film production', 'AI now generates visuals, scenes and effects for film')
- ('Faster and cheaper', 'Shots that needed a crew and budget can be generated')
- ('Still maturing', 'Consistency, control and rights are the open questions')
- ('The takeaway', 'Whole creative industries are being reshaped — fast')

> **Note**
> Embedded clip — click and press Play. Discuss: what does this mean for creative jobs?

Why it matters at work: In a customer-service or hospitality setting, this shapes how you brief an AI tool and how much you trust its answer before it reaches a guest.


## Slide 32 — Customer Service: The Klarna Story

> **Evidence: CASE-V**
> Sources: S25 — Klarna — AI assistant handles two-thirds of chats in first month (27 Feb 2024), S26 — Entrepreneur — Klarna CEO reverses course, hiring more humans not AI (May 2025)

“Customer Service: The Klarna Story” is best understood as a sequence — the steps below run in order. Each step feeds the next, so a problem early on shows up later in the chain — which is exactly why the order is worth learning. A real cautionary tale: automate the routine, but keep humans for judgement and empathy.

1. Feb 2024 — AI assistant handles 2/3 of chats
2. Work of ~700 agents in month one
3. Resolution time 11 min to under 2 min
4. May 2025 — re-hires humans for quality

> **Note**
> A real cautionary tale: automate the routine, but keep humans for judgement and empathy.

Why it matters at work: In a customer-service or hospitality setting, this shapes how you brief an AI tool and how much you trust its answer before it reaches a guest.


## Slide 33 — Where Service Teams Apply GenAI Today

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


## Slide 35 — Prompt Engineering vs Context Engineering

> **Evidence: DEF**
> Sources: S10 — Anthropic — Effective context engineering for AI agents (Sep 2025), S11 — Karpathy on 'context engineering' (X, 25 Jun 2025)

Read the points below as the few things worth remembering about “Prompt Engineering vs Context Engineering”.

| Concept | What it means |
|---|---|
| Prompt engineering | Wording one instruction well |
| Context engineering | Assembling everything the model sees before it answers |
| The shift | Real applications manage context, not just a clever prompt |

Why it matters at work: In a customer-service or hospitality setting, this shapes how you brief an AI tool and how much you trust its answer before it reaches a guest.


## Slide 36 — The Six Ingredients of Context

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


## Slide 37 — How an Agent Gathers Context for a Task

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


## Slide 38 — A Worked Context Example

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


## Slide 40 — The Agentic Loop — A Visual Pipeline

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


## Slide 41 — What a Harness Adds Around the Model

> **Evidence: DEF**
> Sources: S12 — Anthropic — How Claude Code works (agentic harness), S13 — OpenAI — Harness engineering: Codex in an agent-first world

Read the points below as the few things worth remembering about “What a Harness Adds Around the Model”.

| Concept | What it means |
|---|---|
| The loop | Runs context → plan → execute → verify repeatedly |
| Tool access | Lets the model read files, run commands, call APIs |
| State & safety | Tracks progress and enforces permissions and sandboxes |

Why it matters at work: In a customer-service or hospitality setting, this shapes how you brief an AI tool and how much you trust its answer before it reaches a guest.


## Slide 42 — Two Harnesses You May Have Heard Of

> **Evidence: PROD**
> Sources: S12 — Anthropic — How Claude Code works (agentic harness), S13 — OpenAI — Harness engineering: Codex in an agent-first world

Read the points below as the few things worth remembering about “Two Harnesses You May Have Heard Of”.

| Concept | What it means |
|---|---|
| Claude Code | Anthropic's coding agent — the 'agentic harness around Claude' |
| Codex | OpenAI's coding agent; OpenAI calls the discipline 'harness engineering' |
| Same idea | A loop + tools + a sandbox around a general model |

Why it matters at work: In a customer-service or hospitality setting, this shapes how you brief an AI tool and how much you trust its answer before it reaches a guest.


## Slide 43 — The Coding Harnesses — Claude Code, Codex, DeepSeek

> **Evidence: PROD**
> Sources: S53 — Anthropic — Claude Code (repository), S54 — OpenAI — Codex (repository), S55 — DeepSeek Harness (dsh) — developer preview repository

The table below is easier to recall once you see the pattern behind it. All three wrap a model in the same gather-context → act → verify loop; they differ in tools, sandbox and host authority.

| Harness | What it is | Where to find it |
|---|---|---|
| Claude Code | Anthropic's terminal coding agent — reads your codebase, edits files, runs tests and git by natural language | github.com/anthropics/claude-code |
| Codex | OpenAI's coding agent; its execution engine (the 'harness') was open-sourced in Aug 2026 | github.com/openai/codex |
| DeepSeek Harness (dsh) | DeepSeek's plugin-based, model-agnostic harness — a v0.1 developer preview | github.com/deepseek-ai/deepseek-harness |

> **Note**
> All three wrap a model in the same gather-context → act → verify loop; they differ in tools, sandbox and host authority.

Why it matters at work: In a customer-service or hospitality setting, this shapes how you brief an AI tool and how much you trust its answer before it reaches a guest.


## Slide 44 — DeepSeek Harness — 'Everything Is a Plugin'

> **Evidence: PROD**
> Sources: S55 — DeepSeek Harness (dsh) — developer preview repository, S65 — MindStudio — DeepSeek Harness: agentic coding where everything is a plugin

Read the points below as the few things worth remembering about “DeepSeek Harness — 'Everything Is a Plugin'”. A v0.1 developer preview. Its openness is powerful; in Topic 3 we treat each plugin as untrusted until reviewed.

| Concept | What it means |
|---|---|
| One idea | Every capability — tools, models, UI, even core behaviour — is a swappable plugin |
| Model-agnostic | Plug in any model; the harness is not tied to DeepSeek's own |
| Why it matters | Flexible and extensible — but every plugin is also new code and a new trust boundary to review |

> **Note**
> A v0.1 developer preview. Its openness is powerful; in Topic 3 we treat each plugin as untrusted until reviewed.

Why it matters at work: In a customer-service or hospitality setting, this shapes how you brief an AI tool and how much you trust its answer before it reaches a guest.


## Slide 45 — A Concrete Agentic Loop

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


## Slide 46 — When the Loop Goes Wrong — Misreading the Goal

> **Evidence: SYN**
> Concept or classroom slide; no external factual claim is introduced here.

“When the Loop Goes Wrong — Misreading the Goal” is best understood as a sequence — the steps below run in order. Each step feeds the next, so a problem early on shows up later in the chain — which is exactly why the order is worth learning. The same re-planning that makes the loop powerful becomes dangerous when the goal is open-ended and nothing limits the actions — Topic 3 adds the guardrails and human approvals that stop this.

1. Goal: 'Do whatever it takes to remove this stubborn malware'
2. Plan: delete the infected files
3. Verify: malware still there — so the agent re-plans
4. Escalate: 'to be sure' — wipe every file on the machine
5. Result: malware gone, and so is all your work

> **Note**
> The same re-planning that makes the loop powerful becomes dangerous when the goal is open-ended and nothing limits the actions — Topic 3 adds the guardrails and human approvals that stop this.

Why it matters at work: In a customer-service or hospitality setting, this shapes how you brief an AI tool and how much you trust its answer before it reaches a guest.


---

# AI Agents: OpenClaw, Hermes and the Latest

[TOPIC 1]

The deployed systems that put the agentic loop into everyday hands.


## Slide 48 — What Makes Something an 'AI Agent'

> **Evidence: DEF**
> Sources: S44 — OWASP Top 10 for Agentic Applications (2026)

Read the points below as the few things worth remembering about “What Makes Something an 'AI Agent'”.

| Concept | What it means |
|---|---|
| A real system | Not just a model — a running app with an identity |
| Acts through tools | Sends messages, edits files, calls services |
| Keeps state | Remembers context and can resume work |

Why it matters at work: In a customer-service or hospitality setting, this shapes how you brief an AI tool and how much you trust its answer before it reaches a guest.


## Slide 49 — Peter Steinberger in 2026 — Creator of OpenClaw

> **Evidence: PROD**
> Sources: S30 — OpenClaw — Wikipedia (naming and adoption history), S32 — Peter Steinberger — GitHub (steipete), S52 — Peter Steinberger — official 2026 speaker photograph

“Peter Steinberger in 2026 — Creator of OpenClaw” is worth a closer look.

- ('Who', 'Austrian developer, founder of PSPDFKit; GitHub handle steipete')
- ('What he built', 'OpenClaw, an open-source personal AI agent that went viral in late 2025')
- ('Since', 'Joined OpenAI in Feb 2026; an OpenClaw Foundation now stewards the project')

Why it matters at work: In a customer-service or hospitality setting, this shapes how you brief an AI tool and how much you trust its answer before it reaches a guest.


## Slide 50 — OpenClaw — A Naming and Adoption Story

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


## Slide 51 — OpenClaw Runs Where You Already Chat

> **Evidence: PROD**
> Sources: S31 — OpenClaw — official site and docs

Read the points below as the few things worth remembering about “OpenClaw Runs Where You Already Chat”.

| Concept | What it means |
|---|---|
| Messaging-first | You talk to it in WhatsApp, Telegram, Slack, Signal and more |
| Self-hosted | It runs on your own machine or server, under your control |
| Tool-enabled | It can read, write and call services on your behalf |

Why it matters at work: In a customer-service or hospitality setting, this shapes how you brief an AI tool and how much you trust its answer before it reaches a guest.


## Slide 52 — Hermes Agent by Nous Research

> **Evidence: PROD**
> Sources: S33 — Hermes Agent (Nous Research) — documentation

“Hermes Agent by Nous Research” is worth a closer look.

- ('Open-source agent', 'CLI, gateway, messaging surfaces and a desktop app')
- ('Self-improving', 'Can create reusable skills from experience')
- ('Flexible models', 'Runs on many providers — we will point it at MiniMax')

Why it matters at work: In a customer-service or hospitality setting, this shapes how you brief an AI tool and how much you trust its answer before it reaches a guest.


## Slide 53 — The Latest AI Agents (2025–2026)

> **Evidence: PROD**
> Sources: S56 — OpenClaw — repository, S57 — Hermes Agent (Nous Research) — repository, S58 — Prime Agent (Prime Intellect) — repository, S59 — OpenWorker — open standard for employing AI in organisations, S60 — QM (Quartermaster, Y Combinator) — multiplayer agent harness

The table below is easier to recall once you see the pattern behind it. All open-source and self-hosted. Capability is not a safety rating — verify each one's permissions, sandbox and data access before use.

| Agent | What it is | Where to find it |
|---|---|---|
| OpenClaw | Peter Steinberger's open-source personal agent; runs on your own devices, reached via your messaging apps | github.com/openclaw/openclaw |
| Hermes Agent | Nous Research's self-improving personal agent; learns skills, model-agnostic (we use MiniMax) | github.com/NousResearch/hermes-agent |
| Prime Agent | Prime Intellect's self-improving agent for coding and long-running autonomous tasks | github.com/PrimeIntellect-ai/prime-agent |
| OpenWorker | An open standard to hire, govern and trust AI 'workers' inside an organisation | github.com/openworker-io/openworker |
| QM (Quartermaster) | Y Combinator's multiplayer agent harness for teams in Slack / web, with scoped memory and sandboxes | github.com/yc-software/qm |

> **Note**
> All open-source and self-hosted. Capability is not a safety rating — verify each one's permissions, sandbox and data access before use.

Why it matters at work: In a customer-service or hospitality setting, this shapes how you brief an AI tool and how much you trust its answer before it reaches a guest.


## Slide 54 — Applications of AI Agents in Threat Detection

> **Evidence: SYN**
> Concept or classroom slide; no external factual claim is introduced here.

Read the points below as the few things worth remembering about “Applications of AI Agents in Threat Detection”. AI is on both sides of the fight — the same capabilities also power attackers, which is why Topic 3 defends the agents themselves.

| Concept | What it means |
|---|---|
| Real-time threat detection | Agents watch traffic, endpoints and events continuously and flag cyber threats as they emerge — not hours later |
| Automated vulnerability detection | Scan code, systems and configurations for weaknesses, then analyse severity and exploitability |
| Malware analysis & classification | Dissect and classify malicious samples far faster than manual reverse-engineering |

> **Note**
> AI is on both sides of the fight — the same capabilities also power attackers, which is why Topic 3 defends the agents themselves.

Why it matters at work: In a customer-service or hospitality setting, this shapes how you brief an AI tool and how much you trust its answer before it reaches a guest.


## Slide 55 — AI Agents in Network and Social-Engineering Security

> **Evidence: SYN**
> Concept or classroom slide; no external factual claim is introduced here.

Read the points below as the few things worth remembering about “AI Agents in Network and Social-Engineering Security”.

| Concept | What it means |
|---|---|
| Network intrusion detection | Learn what normal network behaviour looks like and catch intrusions that signature rules miss |
| Attack classification | Label detected attacks by type and severity so responders know what to tackle first |
| Phishing & deceptive language | Detect and defend against phishing attacks and manipulative, deceptive language in messages |
| Log analysis & anomaly detection | Sift millions of system-log lines to surface the anomalies worth investigating |

Why it matters at work: In a customer-service or hospitality setting, this shapes how you brief an AI tool and how much you trust its answer before it reaches a guest.


## Slide 56 — Applications of AI Agents in Incident Response

> **Evidence: SYN**
> Concept or classroom slide; no external factual claim is introduced here.

Read the points below as the few things worth remembering about “Applications of AI Agents in Incident Response”.

| Concept | What it means |
|---|---|
| Repair & patch generation | Automate vulnerability repair and generate candidate patches for human review |
| Workflows & playbooks | Streamline incident-response workflows and execute playbooks consistently under pressure |
| Post-attack analysis | Reconstruct the attack, identify the root cause and recommend fixes to stop a repeat |

Why it matters at work: In a customer-service or hospitality setting, this shapes how you brief an AI tool and how much you trust its answer before it reaches a guest.


## Slide 57 — Applications of AI in Security Operations Centres (SOCs)

> **Evidence: SYN**
> Concept or classroom slide; no external factual claim is introduced here.

Read the points below as the few things worth remembering about “Applications of AI in Security Operations Centres (SOCs)”. The SOC of 2026 pairs human analysts with AI agents — the analyst sets direction and approves actions; the agent does the heavy lifting.

| Concept | What it means |
|---|---|
| Proactive defence & threat hunting | Hunt for hidden threats across the estate instead of waiting for alerts |
| Risk management & predictive analytics | Score risks and predict likely attack paths before they are exploited |
| Adaptive decision-making | Learn continuously from every incident and adapt defences over time |

> **Note**
> The SOC of 2026 pairs human analysts with AI agents — the analyst sets direction and approves actions; the agent does the heavy lifting.

Why it matters at work: In a customer-service or hospitality setting, this shapes how you brief an AI tool and how much you trust its answer before it reaches a guest.


## Slide 58 — Try It Today: TIA Support on WhatsApp

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


## Slide 59 — An Agent on WhatsApp Is Exposed to the Internet

> **Evidence: DEF**
> Sources: S43 — OWASP Top 10 for LLM Applications, S44 — OWASP Top 10 for Agentic Applications (2026)

Read the points below as the few things worth remembering about “An Agent on WhatsApp Is Exposed to the Internet”. The convenience of a public channel is also its attack surface — Topic 3 shows the defences.

| Concept | What it means |
|---|---|
| Open to anyone | A WhatsApp or Telegram agent accepts messages from the whole internet — including bad actors |
| Prompt injection | A crafted message overrides the agent's instructions and hijacks its tools |
| Data poisoning | Malicious content the agent reads or saves corrupts what it does later |
| What is at stake | Confidential data extracted, or the server behind the agent harmed |

> **Note**
> The convenience of a public channel is also its attack surface — Topic 3 shows the defences.

Why it matters at work: In a customer-service or hospitality setting, this shapes how you brief an AI tool and how much you trust its answer before it reaches a guest.


---

# Skills and Tools

[TOPIC 1]

How agents extend beyond the base model.


## Slide 61 — Tools vs Skills

> **Evidence: DEF**
> Sources: S15 — Anthropic — Agent Skills / Claude Code, S16 — Model Context Protocol (MCP) documentation

Read the points below as the few things worth remembering about “Tools vs Skills”.

| Concept | What it means |
|---|---|
| Tools | Actions the agent can take — send email, run a query, open a file |
| Skills | Packaged know-how — reusable instructions for a task |
| Together | Skills tell the agent how; tools let the agent do |

Why it matters at work: In a customer-service or hospitality setting, this shapes how you brief an AI tool and how much you trust its answer before it reaches a guest.


## Slide 62 — How an Agent Uses a Tool

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


## Slide 63 — Why Skills Make Agents Practical

> **Evidence: SYN**
> Sources: S15 — Anthropic — Agent Skills / Claude Code

Read the points below as the few things worth remembering about “Why Skills Make Agents Practical”.

| Concept | What it means |
|---|---|
| Consistency | The same task is done the same way every time |
| Reuse | Build once, run across many jobs |
| In Topic 2 | We install a skill so the agent formats Excel and PPT better |

Why it matters at work: In a customer-service or hospitality setting, this shapes how you brief an AI tool and how much you trust its answer before it reaches a guest.


## Slide 64 — Case — A Malicious Skill on ClawHub

> **Evidence: CASE-V**
> Sources: S17 — Snyk — How a Malicious Google Skill on ClawHub Tricks Users Into Installing Malware (10 Feb 2026)

“Case — A Malicious Skill on ClawHub” is best understood as a sequence — the steps below run in order. Each step feeds the next, so a problem early on shows up later in the chain — which is exactly why the order is worth learning. Snyk, 10 Feb 2026 — the malware was in the skill's instructions, not its code. Install skills only from sources you trust; clones of the flagged skill reappeared within hours.

1. A fake 'Google' skill is published on ClawHub, OpenClaw's skill marketplace
2. Its SKILL.md instructions tell the user to install a fake 'openclaw-core' utility
3. The install command hides base64-encoded code that runs the attacker's scripts
4. Users trust their own agent — and infect their own machines

> **Note**
> Snyk, 10 Feb 2026 — the malware was in the skill's instructions, not its code. Install skills only from sources you trust; clones of the flagged skill reappeared within hours.

Why it matters at work: In a customer-service or hospitality setting, this shapes how you brief an AI tool and how much you trust its answer before it reaches a guest.


---

# Multi-Agent Systems

[TOPIC 1]

When one agent is not enough.


## Slide 67 — How a Multi-Agent System Works

> **Evidence: DEF**
> Sources: S14 — Anthropic — How we built our multi-agent research system (13 Jun 2025)

“How a Multi-Agent System Works” is worth a closer look. A lead agent takes your goal, delegates to specialist workers that run in parallel, then combines their results. Anthropic's research system used this pattern and beat a single agent by ~90% on its internal eval.

> **Note**
> A lead agent takes your goal, delegates to specialist workers that run in parallel, then combines their results. Anthropic's research system used this pattern and beat a single agent by ~90% on its internal eval.

Why it matters at work: At work this is the difference between a prompt that wastes time and one that gives you an answer you can send or act on straight away.


## Slide 68 — Why and Why Not Multi-Agent

> **Evidence: DEF**
> Sources: S14 — Anthropic — How we built our multi-agent research system (13 Jun 2025)

Read the points below as the few things worth remembering about “Why and Why Not Multi-Agent”.

| Concept | What it means |
|---|---|
| Faster & broader | Parallel workers cover more ground |
| Costlier | Multi-agent runs used far more tokens than a single chat |
| Trade-off | Use it when breadth matters more than cost |

Why it matters at work: At work this is the difference between a prompt that wastes time and one that gives you an answer you can send or act on straight away.


## Slide 69 — A Service Example — Customer Recovery

> **Evidence: SYN**
> Concept or classroom slide; no external factual claim is introduced here.

“A Service Example — Customer Recovery” is worth a closer look.

- ('Goal', 'Recover customer trust')
- ('Parallel workers', 'Draft message · Build offer · Check customer data')
- ('Lead + human', 'Merge one plan · Review · Approve')

Why it matters at work: At work this is the difference between a prompt that wastes time and one that gives you an answer you can send or act on straight away.


## Slide 70 — Agent-to-Agent Messaging — A Security Blind Spot

> **Evidence: DEF**
> Sources: S44 — OWASP Top 10 for Agentic Applications (2026)

Read the points below as the few things worth remembering about “Agent-to-Agent Messaging — A Security Blind Spot”. More agents means more paths to monitor. Log every agent-to-agent hand-off and validate what an agent receives — never trust a message just because another agent sent it. OWASP's 2026 agentic Top 10 flags exactly this cascading multi-agent failure mode.

| Concept | What it means |
|---|---|
| One agent's output is the next agent's input | A hallucinated or maliciously injected result is passed downstream — and the receiving agent treats it as trusted fact |
| Errors and attacks cascade | One bad message can propagate through every agent behind it, ending in a wrong or harmful action far from where it started |
| Topology multiplies message paths | Every extra agent adds agent-to-agent links — no single log shows the whole data flow end to end, so visibility drops |
| Tracing and attribution get harder | When something goes wrong, finding which agent introduced the bad data needs per-agent logs of every hand-off |

> **Note**
> More agents means more paths to monitor. Log every agent-to-agent hand-off and validate what an agent receives — never trust a message just because another agent sent it. OWASP's 2026 agentic Top 10 flags exactly this cascading multi-agent failure mode.

Why it matters at work: At work this is the difference between a prompt that wastes time and one that gives you an answer you can send or act on straight away.


---

# Generative AI vs Agentic AI vs AI Agents

[TOPIC 1]

The single most useful distinction from Topic 1.


## Slide 72 — The Three, Side by Side

> **Evidence: SYN**
> Sources: S43 — OWASP Top 10 for LLM Applications, S44 — OWASP Top 10 for Agentic Applications (2026)

The table below is easier to recall once you see the pattern behind it.

|  | Generative AI | Agentic AI | AI Agent |
|---|---|---|---|
| What it does | Creates content | Loops to reach a goal | A deployed system that acts |
| Acts on its own? | No — you run each step | Yes — plans and retries | Yes — through real tools |
| Example | ChatGPT drafting a reply | Claude Code fixing a bug | OpenClaw in your WhatsApp |

Why it matters at work: At work this is the difference between a prompt that wastes time and one that gives you an answer you can send or act on straight away.


## Slide 73 — One-Line Definitions

> **Evidence: SYN**
> Concept or classroom slide; no external factual claim is introduced here.

Read the points below as the few things worth remembering about “One-Line Definitions”.

| Concept | What it means |
|---|---|
| Generative AI | Makes things |
| Agentic AI | The loop that makes an AI pursue a goal |
| AI Agent | The running system that uses that loop to act for you |

Why it matters at work: At work this is the difference between a prompt that wastes time and one that gives you an answer you can send or act on straight away.


## Slide 74 — Generation is a step. Agency is a loop. An agent is a system.

> **Evidence: SYN**
> Concept or classroom slide; no external factual claim is introduced here.

> **Key idea**
> Generation is a step. Agency is a loop. An agent is a system.


## Slide 75 — Activity 1 — Talk to an AI Agent, Then Reflect

> **Evidence: SIM**
> Concept or classroom slide; no external factual claim is introduced here.

In this activity — Activity 1 — Talk to an AI Agent, Then Reflect — you work hands-on with a ready-made tool; the steps are in the walkthrough later in this guide. Pinboard: https://alfredang.github.io/pinboard/

- Message TIA Support on WhatsApp +65 8866 6375 (powered by OpenClaw)
- Use the prompt card in the activity pack; give it a small realistic task
- Post your reflections to the Pinboard under the four risk themes

> **Note**
> Pinboard: https://alfredang.github.io/pinboard/

Why it matters at work: At work this is the difference between a prompt that wastes time and one that gives you an answer you can send or act on straight away.


## Slide 76 — Activity 1 — Group Your Concerns

> **Evidence: SIM**
> Concept or classroom slide; no external factual claim is introduced here.

Read the points below as the few things worth remembering about “Activity 1 — Group Your Concerns”.

| Concept | What it means |
|---|---|
| Data Privacy | What data did it see or ask for? |
| Job Impact | Whose work does this change? |
| Ethical Concerns | Could it mislead or be unfair? |
| Cyber Security | How could it be abused? |

Why it matters at work: At work this is the difference between a prompt that wastes time and one that gives you an answer you can send or act on straight away.


## Slide 77 — Activity 1 — Debrief

> **Evidence: SIM**
> Concept or classroom slide; no external factual claim is introduced here.

“Activity 1 — Debrief” is best understood as a sequence — the steps below run in order. Each step feeds the next, so a problem early on shows up later in the chain — which is exactly why the order is worth learning. This debrief seeds the governance thinking you will use in Topic 3.

1. Read the Pinboard together
2. Cluster the four themes
3. Name the top risk in each
4. Agree one safe-use rule per theme

> **Note**
> This debrief seeds the governance thinking you will use in Topic 3.

Why it matters at work: At work this is the difference between a prompt that wastes time and one that gives you an answer you can send or act on straight away.


---

# Prompt Engineering and Post-Training for Autonomous AI Agents

[TOPIC 2 · LO2]

Set up a real agent on MiniMax, then learn to prompt it well.


## Slide 79 — What Topic 2 Will Cover

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


## Slide 80 — The Setup in Three Parts

> **Evidence: PROD**
> Sources: S33 — Hermes Agent (Nous Research) — documentation, S36 — MiniMax — MiniMax-M2 news and platform

Read the points below as the few things worth remembering about “The Setup in Three Parts”.

| Concept | What it means |
|---|---|
| Hermes Agent | The agent you talk to |
| MiniMax M2.7 | The model that powers it |
| Your API key | Connects the two — kept only on your machine |

Why it matters at work: At work this is the difference between a prompt that wastes time and one that gives you an answer you can send or act on straight away.


## Slide 81 — Install the Hermes Desktop App

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


## Slide 82 — Get a MiniMax Model and API Key

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


## Slide 83 — Point Hermes at MiniMax M2.7

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


## Slide 84 — Keep Your Key Safe

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


## Slide 86 — Five Principles of a Good Prompt

> **Evidence: DEF**
> Sources: S10 — Anthropic — Effective context engineering for AI agents (Sep 2025)

“Five Principles of a Good Prompt” is worth a closer look.

- ('Role', 'Who the AI should be')
- ('Task', 'Exactly what result you want')
- ('Context', 'The facts it needs')
- ('Format', 'How the answer should look')
- ('Constraints', 'Length, tone and limits')

Why it matters at work: At work this is the difference between a prompt that wastes time and one that gives you an answer you can send or act on straight away.


## Slide 87 — A Bad Prompt vs a Good Prompt

> **Evidence: SYN**
> Concept or classroom slide; no external factual claim is introduced here.

It helps to set the two sides of “A Bad Prompt vs a Good Prompt” against each other in the table below. The difference between the two columns is the thing you should be able to explain in your own words after the class.

| Bad prompt | Good prompt |
|---|---|
| 'analyse this data' | 'You are a marketing analyst. From this sales table, give the top 3 trends as bullets, with one action each.' |
| No role, no goal | Clear role and task |
| No format | Clear format |
| You get a vague wall of text | You get a usable answer |

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 88 — Techniques That Reliably Help

> **Evidence: DEF**
> Sources: S10 — Anthropic — Effective context engineering for AI agents (Sep 2025)

Read the points below as the few things worth remembering about “Techniques That Reliably Help”.

| Concept | What it means |
|---|---|
| Give an example | Show one sample of the output you want |
| Ask for steps | 'Think step by step' improves reasoning tasks |
| Iterate | Refine the prompt after seeing the first answer |

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 89 — 'Post-Training' for Agents — Memory and Skills, Not Fine-Tuning

> **Evidence: DEF**
> Sources: S10 — Anthropic — Effective context engineering for AI agents (Sep 2025), S15 — Anthropic — Agent Skills / Claude Code

Read the points below as the few things worth remembering about “'Post-Training' for Agents — Memory and Skills, Not Fine-Tuning”. This is how the Hermes agent 'self-improves': it writes learnings to memory and skills, then reuses them.

| Concept | What it means |
|---|---|
| Not fine-tuning | You are not retraining the model's weights — that is expensive and out of reach for most teams |
| It's context engineering | The agent stores what it learns in memory files and reusable skills |
| Improves over time | Next time, it loads those memories and skills — so it gets better without retraining |
| Stays consistent | The same saved skill makes the agent do a task the same way every time |

> **Note**
> This is how the Hermes agent 'self-improves': it writes learnings to memory and skills, then reuses them.

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 90 — Reflect — Does Prompt Engineering Still Matter With Agents?

> **Evidence: SYN**
> Concept or classroom slide; no external factual claim is introduced here.

Read the points below as the few things worth remembering about “Reflect — Does Prompt Engineering Still Matter With Agents?”. Discuss: think back to your bad-vs-good prompts — how many extra agent steps did the vague one cause?

| Concept | What it means |
|---|---|
| The question | An agentic loop can plan, retry and self-correct — so is a good prompt still worth the effort? |
| Still yes | A clear prompt points the loop at the right goal from the start, instead of it guessing and looping |
| Saves time & tokens | A vague prompt makes the agent take extra steps — more turns, more tokens, more cost and delay |
| The takeaway | Prompt engineering matters MORE with agents: a clear brief up front saves a whole loop of rework |

> **Note**
> Discuss: think back to your bad-vs-good prompts — how many extra agent steps did the vague one cause?

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 91 — Activity 2 — Analyse Excel Data with the Agent

> **Evidence: SIM**
> Concept or classroom slide; no external factual claim is introduced here.

In this activity — Activity 2 — Analyse Excel Data with the Agent — you work hands-on with a ready-made tool; the steps are in the walkthrough later in this guide. You will produce a Word report with charts, analysis and numbers-backed recommendations.

- Upload MOCK-MARKETING-DATA.xlsx to your Hermes + MiniMax agent
- Warm up with a bad prompt vs a good prompt on the same data
- Then prompt the agent to analyse the data, generate charts and produce a .docx report with recommendations

> **Note**
> You will produce a Word report with charts, analysis and numbers-backed recommendations.

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 92 — Activity 2 — From Spreadsheet to Report

> **Evidence: SIM**
> Concept or classroom slide; no external factual claim is introduced here.

Read the points below as the few things worth remembering about “Activity 2 — From Spreadsheet to Report”.

| Concept | What it means |
|---|---|
| Bad | 'which is better?' |
| Good | 'Rank channels by ROI = Revenue / Spend as a table' |
| Report | 'Analyse the file, chart revenue, ROI and spend, and generate a .docx report with recommendations' |
| Verify | Check two numbers in the report against the spreadsheet |

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 93 — Activity 3 — Create and Redesign a PPT with the Agent

> **Evidence: SIM**
> Concept or classroom slide; no external factual claim is introduced here.

In this activity — Activity 3 — Create and Redesign a PPT with the Agent — you work hands-on with a ready-made tool; the steps are in the walkthrough later in this guide. The image template and two worked-example decks are in the activity pack.

- Ask the agent for a 10-slide deck on AI Security for AI Agents
- Save the finished deck to your Downloads folder
- Upload the image template and ask the agent to redesign the deck

> **Note**
> The image template and two worked-example decks are in the activity pack.

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 94 — Activity 3 — What Good Looks Like

> **Evidence: SIM**
> Concept or classroom slide; no external factual claim is introduced here.

Read the points below as the few things worth remembering about “Activity 3 — What Good Looks Like”.

| Concept | What it means |
|---|---|
| Create | 'Build a 10-slide deck on AI Security for AI Agents with speaker notes' |
| Redesign | 'Restyle every slide using this uploaded image as the visual theme' |
| Reflect | Content first, then design — the agent iterates on its own output |

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 95 — Activity 4 — Install Tools and Skills to Do Better

> **Evidence: SIM**
> Concept or classroom slide; no external factual claim is introduced here.

In this activity — Activity 4 — Install Tools and Skills to Do Better — you work hands-on with a ready-made tool; the steps are in the walkthrough later in this guide. Skills give the agent repeatable know-how for formatting and structure.

- Install the supplied tool/skill in your agent
- Re-run the Excel and PPT tasks
- Note how much the output improves

> **Note**
> Skills give the agent repeatable know-how for formatting and structure.

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 97 — Reflect on Working with the Agent

> **Evidence: SIM**
> Concept or classroom slide; no external factual claim is introduced here.

Read the points below as the few things worth remembering about “Reflect on Working with the Agent”.

| Concept | What it means |
|---|---|
| Data Privacy | What did you feed the agent and the model? |
| Job Impact | Which of your tasks did it speed up? |
| Ethical Concerns | Did any output mislead or overclaim? |
| Cyber Security | Where did your API key and data go? |

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 98 — Topic 2 Debrief

> **Evidence: SIM**
> Concept or classroom slide; no external factual claim is introduced here.

“Topic 2 Debrief” is best understood as a sequence — the steps below run in order. Each step feeds the next, so a problem early on shows up later in the chain — which is exactly why the order is worth learning. Carry the security worries forward — Topic 3 turns them into governance.

1. Share your best and worst prompt
2. Name one thing skills improved
3. List one privacy or security worry
4. Agree a prompt checklist to keep

> **Note**
> Carry the security worries forward — Topic 3 turns them into governance.

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


---

# Security Risk of Autonomous AI Agents

[TOPIC 3 · LO3]

Governance, jobs and the security of agents that can act.


## Slide 100 — What Topic 3 Will Cover

> **Evidence: SYN**
> Concept or classroom slide; no external factual claim is introduced here.

“What Topic 3 Will Cover” is best understood as a sequence — the steps below run in order. Each step feeds the next, so a problem early on shows up later in the chain — which is exactly why the order is worth learning. Real Singapore cases drive the discussion — building to the key AI challenges every business must manage.

1. Data governance & accountability
2. Brand damage
3. Job impact & redesign
4. Cybersecurity & safe rollout
5. The key challenges to business

> **Note**
> Real Singapore cases drive the discussion — building to the key AI challenges every business must manage.

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 101 — Discussion Point 1 — Who Is Accountable for the Data?

> **Evidence: SIM**
> Concept or classroom slide; no external factual claim is introduced here.

Read the points below as the few things worth remembering about “Discussion Point 1 — Who Is Accountable for the Data?”.

| Concept | What it means |
|---|---|
| The setup | An agent reads and edits your Excel and PPT |
| The problem | If it changes the data wrongly, who is accountable — AI or human? |
| Second case | If AI-made models or scripts break a law, who answers for it? |

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 102 — AI is never the accountable party. A named human always is.

> **Evidence: DEF**
> Sources: S40 — IMDA Model AI Governance Framework for Generative AI, S46 — Moffatt v Air Canada, 2024 BCCRT 149

> **Key idea**
> AI is never the accountable party. A named human always is.


## Slide 103 — Case — Moffatt v Air Canada

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


## Slide 104 — Traditional Data Governance

> **Evidence: DEF**
> Sources: S41 — PDPC Advisory Guidelines on Key Concepts in the PDPA

Read the points below as the few things worth remembering about “Traditional Data Governance”.

| Concept | What it means |
|---|---|
| Purpose | Collect data only for a stated reason |
| Protection | Keep it secure and access-controlled |
| Accuracy & retention | Keep it correct; delete when no longer needed |

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 105 — New Principles for GenAI and Agents

> **Evidence: DEF**
> Sources: S40 — IMDA Model AI Governance Framework for Generative AI

Read the points below as the few things worth remembering about “New Principles for GenAI and Agents”.

| Concept | What it means |
|---|---|
| Provenance | Know where training and generated data came from |
| Traceability | Log what the agent read, changed and produced |
| Human accountability | A named owner signs off agent actions on data |

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 106 — Scope of an AI Data Governance Policy

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


## Slide 107 — The 7-Part AI Data Governance Policy Framework

> **Evidence: SYN**
> Sources: S40 — IMDA Model AI Governance Framework for Generative AI, S41 — PDPC Advisory Guidelines on Key Concepts in the PDPA

The table below is easier to recall once you see the pattern behind it. The structure of the sample policy in the activity pack — aligned in spirit with the IMDA Model AI Governance Framework and the PDPA.

| Section | What it covers |
|---|---|
| 1 · Scope | The AI systems, agents and data assets the policy covers |
| 2 · Roles | Data Owner, Agent Owner, Approver, Reviewer — every role a named human |
| 3 · Principles | Accuracy, purpose limitation, protection, provenance, traceability, human accountability |
| 4 · Rules | What agents may read, write and generate; approvals; retention |
| 5 · Audit & Logging | What each agent did, who reviews the logs and how often |
| 6 · Accountability | A named human is answerable — never the AI |
| 7 · Review | Review cadence, the review owner, and early-review triggers |

> **Note**
> The structure of the sample policy in the activity pack — aligned in spirit with the IMDA Model AI Governance Framework and the PDPA.

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 108 — The Sample Policy in Action — Sunset Bay Resort

> **Evidence: SIM**
> Concept or classroom slide; no external factual claim is introduced here.

The table below is easier to recall once you see the pattern behind it. From the sample AI Data Governance Policy in the activity pack — every detail is fictional.

| Section | Example from the sample policy (a fictional resort) |
|---|---|
| Scope | The WhatsApp guest-support agent, the marketing-analysis agent and the website chatbot — plus the guest bookings, contact details and marketing spreadsheets they touch |
| Roles | Data Owner — Front Office Manager · Agent Owner — Marketing Manager · Approver — General Manager · Reviewer — Duty Supervisor |
| Rules | Agents may read one guest's booking only while serving that guest; may draft replies, reports and slides; any change to a live booking or price needs human approval first; chat logs kept 12 months, then deleted |
| Review | The policy is reviewed every 12 months — earlier when a new agent, skill or data type is added, or after any incident |

> **Note**
> From the sample AI Data Governance Policy in the activity pack — every detail is fictional.

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 109 — Activity 5 — Draft Your AI Data Governance Policy

> **Evidence: SIM**
> Concept or classroom slide; no external factual claim is introduced here.

In this activity — Activity 5 — Draft Your AI Data Governance Policy — you work hands-on with a ready-made tool; the steps are in the walkthrough later in this guide. The generator website (ai-data-policy-generator.html) drafts the policy from your company details using the 7-part framework. Refine weak sections with the Hermes prompts in PROMPTS.md. Keep every detail fictional.

- Does every role belong to a named human — never the AI?
- Which changes to live data need human approval first?
- Where did your API key go when you typed it into the website?

> **Note**
> The generator website (ai-data-policy-generator.html) drafts the policy from your company details using the 7-part framework. Refine weak sections with the Hermes prompts in PROMPTS.md. Keep every detail fictional.

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 110 — Discussion Point 2 — Brand Damage from Generative AI

> **Evidence: SIM**
> Concept or classroom slide; no external factual claim is introduced here.

Read the points below as the few things worth remembering about “Discussion Point 2 — Brand Damage from Generative AI”.

| Concept | What it means |
|---|---|
| The temptation | AI can make an ad or a campaign in 24–48 hours, from about S$1,000 |
| The risk | A cheap or misleading AI ad can read as low-effort and hurt the brand |
| Who feels it most | Big and luxury brands — the backlash is sharpest for them |

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 111 — Case — Gen-AI Ads Flood Singapore, and Could Backfire

> **Evidence: CASE-V**
> Sources: S64 — CNA — Gen-AI ads flooding the Singapore market could backfire on brands (24 Aug 2026)

The table below is easier to recall once you see the pattern behind it. CNA, 24 Aug 2026. An industry-wide risk, not one named failure — the harm is to trust, authenticity and brand equity.

| What is happening | The warning |
|---|---|
| AI ad demand in Singapore is up 4–5x; half of advertisers already use gen-AI for video | 'Using AI will not necessarily damage a brand. Using it poorly can.' (SMU Prof Sabine Benoit) |
| Virtual influencers and AI livestream avatars are replacing human hosts | Virtual influencers can 'give people the creeps' and breed mistrust (NUS Assoc Prof Ang Swee Hoon) |
| Luxury and global brands are adopting AI ads to cut cost | Seen as 'lacking effort' and 'less authentic'; 'not all publicity is good publicity' |
| Regulators are watching | ASAS: 'Disclosure of the use of AI alone does not whitewash this issue' |

> **Note**
> CNA, 24 Aug 2026. An industry-wide risk, not one named failure — the harm is to trust, authenticity and brand equity.

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 112 — Why AI Content Can Damage a Brand

> **Evidence: SYN**
> Sources: S64 — CNA — Gen-AI ads flooding the Singapore market could backfire on brands (24 Aug 2026)

Read the points below as the few things worth remembering about “Why AI Content Can Damage a Brand”.

| Concept | What it means |
|---|---|
| Signals low effort | 'The company hasn't put much effort into the product' |
| Feels inauthentic | Synthetic faces and voices erode trust and connection |
| Ethical shadow | Models trained on creators' work 'without their consent' — a visible symbol of unfairness |
| Backlash is costly | Negative buzz can force an ad down — the campaign fails its objective |

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 113 — Discuss & Debrief — Protecting the Brand

> **Evidence: SIM**
> Concept or classroom slide; no external factual claim is introduced here.

“Discuss & Debrief — Protecting the Brand” is best understood as a sequence — the steps below run in order. Each step feeds the next, so a problem early on shows up later in the chain — which is exactly why the order is worth learning. Debrief: authenticity, disclosure, human sign-off and knowing which content should never be fully synthetic.

1. When is AI content fine — and when is it a risk?
2. Should you disclose that an ad is AI-made?
3. What review would catch a brand-damaging ad first?
4. Write one brand-safe-AI rule for your team

> **Note**
> Debrief: authenticity, disclosure, human sign-off and knowing which content should never be fully synthetic.

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 114 — Discussion Point 3 — If Agents Take the Work, What Do People Do?

> **Evidence: SIM**
> Concept or classroom slide; no external factual claim is introduced here.

Read the points below as the few things worth remembering about “Discussion Point 3 — If Agents Take the Work, What Do People Do?”.

| Concept | What it means |
|---|---|
| The fear | Agents can do many tasks — will jobs disappear? |
| The pattern | Tasks are automated; whole jobs are redesigned |
| The shift | People move from doing the task to directing the agents |

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 115 — Jobs Move — Not Vanish

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


## Slide 116 — Why Now — 12,000+ Agents in Singapore Healthcare

> **Evidence: CASE-V**
> Source: Singapore Ministry of Health, HIMSS26 APAC speech, 24 Aug 2026

Singapore public healthcare professionals have created more than **12,000 AI agents** on the AgentSea platform since it launched in late May 2026 — built with **no code required**, and with **human review** retained.

> **Note**
> MOH: when AI can act, assurance must shift from outputs to actions. The doctor remains responsible for the clinical decision.

The lesson for every organisation is the same — ownership cannot be automated.

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 117 — The Stakes — The Numbers Give Perspective

> **Evidence: CASE-V**
> Sources: S48 — WEF — Future of Jobs Report 2025; WEF workforce strategies

The advantage comes from redesigning work — not merely deploying AI.

| Global job change by 2030 | Figure |
|---|---|
| Created | +170M |
| Displaced | −92M |
| Net | +78M |

22% of today's formal jobs are projected to be disrupted.

| The employer response | Share |
|---|---|
| Expect AI to transform their business | 86% |
| Plan to upskill workers for AI | 77% |
| Also expect workforce reductions from automation | 41% |

> **Note**
> The opportunity: make agent management part of the job.

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 118 — Our Operating Model — A Human at Every Consequential Gate

> **Evidence: SYN**
> Source: Tertiary Infotech Academy practitioner experience (websites and software projects)

At Tertiary, agents support website and software workflows — and we help clients apply the same pattern.

1. **Frame** — the human sets the goal, context and constraints
2. **Orchestrate** — agents research, build, test and monitor
3. **Challenge** — the human reviews evidence, risks and exceptions
4. **Decide** — a named owner approves release and remains accountable

> **Note**
> Agents increase throughput. Humans protect judgement and accountability.

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 119 — The Problem — Adoption Debt When Roles Lag Behind

> **Evidence: SYN**
> Source: Tertiary practitioner observations and the Sarah coaching scenario

AI deployment creates **adoption debt** when roles lag behind the technology. If identity, decision rights and accountability remain unresolved, resistance compounds.

**What we hear:** "The agent is wrong." · "This will not work here." · "I do not have time to learn it."

| What is often underneath | The unasked question |
|---|---|
| JOB | Will I still be needed? |
| IDENTITY | What happens to my expertise? |
| CONTROL | Can I stop a bad action? |
| BLAME | Am I liable for its mistakes? |

> **Note**
> Resistance is not a people problem. It is a role-design signal.

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 120 — The Solution — An Explicit Human Owner Role

> **Evidence: SYN**
> Work redesign pattern: human direction, challenge, approval, escalation and continuous improvement

The solution is an explicit **Human Owner** role: move routine production to the agent and make human decision rights visible.

**BEFORE — the DOER:** drafts every output · runs every check · handles every routine case · measures effort by volume

| AFTER — the HUMAN OWNER | Responsibility |
|---|---|
| DIRECT | Set intent and boundaries |
| CHALLENGE | Test evidence and assumptions |
| DECIDE | Approve consequential actions |
| ESCALATE | Own exceptions and recovery |
| IMPROVE | Refine prompts, tools and rules |

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 121 — Coaching Staff Through the Change

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


## Slide 122 — A Job-Redesign Framework

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


## Slide 123 — The Intervention — Use GROW to Turn Resistance into Redesign

> **Evidence: DEF**
> Concept or classroom slide; no external factual claim is introduced here.

Read the points below as the few things worth remembering about “The GROW Coaching Model”. Coach by asking, not telling — it builds ownership. You will use GROW in the role-play, and your feedback is scored against it.

| Concept | What it means |
|---|---|
| G — Goal | Agree what they want. 'What would a good outcome look like for you?' |
| R — Reality | Explore where they are now, with empathy. 'What's happening, and what worries you?' |
| O — Options | Generate ways forward together. 'What could you do? What choices do you have?' |
| W — Will | Commit to concrete next steps. 'What will you do, and by when?' |

> **Note**
> Coach by asking, not telling — it builds ownership. You will use GROW in the role-play, and your feedback is scored against it.

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 124 — The Product — The Job-Redesign Coaching Simulator

> **Evidence: SIM**
> Live training simulator — six fictional scenarios; demo mode makes no external API calls

The **AI Agent Job Redesign Coach** simulator makes the hard conversation safe to practise, building coaching confidence across six realistic forms of resistance.

| Person | Role | Resistance |
|---|---|---|
| Sarah | Marketing | Fear / identity |
| David | Customer Service | Anger / trust |
| Mei Ling | Data Analyst | Anxiety / withdrawal |
| Arjun | Software Developer | Scepticism / pride |
| Aisha | Web Operations | Control / accountability |
| Farah | HR Executive | Ethics / purpose |

The flow is: **pick a person → coach the transition → get GROW feedback.**

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 125 — The Worked Example — Sarah's Redesigned Role

> **Evidence: SIM**
> Source: A6 coaching scenario supplied for this presentation; fictional staff and company data

A coaching conversation can reframe fear as ownership. Sarah moves from threatened doer to AI-augmented marketing lead.

**REALITY —** "The agent writes the campaign copy and builds the decks. That is basically my whole job." Fear of redundancy · loss of identity · no consultation · anxiety about blame.

| REDESIGNED ROLE — AI-Augmented Marketing Lead | |
|---|---|
| DIRECTION | Goals, creative angle and brand voice |
| CHALLENGE | Audit assumptions, facts and market fit |
| APPROVAL | Final gate for external content |
| INSIGHT | Feed live client and market context back |
| LEARNING | Refine the human-agent workflow |

> **Note**
> AI lights the way. The human decides the path.

The full transcript is in the Activity 6 pack as `A6-Coaching-Sarah.docx`.

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 126 — Activity 6 — Coach a Worried Team Member (Role-Play)

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


## Slide 128 — The Singapore Reality — Fast on AI, Slower on Security

> **Evidence: CASE-V**
> Sources: S61 — CPA Australia — Singapore businesses lead in AI and data adoption but face cybersecurity challenges (Dec 2025)

“The Singapore Reality — Fast on AI, Slower on Security” is worth a closer look. CPA Australia Business Technology Survey, 1,117 respondents, Jul–Sep 2025. Adoption races ahead of security — and AI-enabled threats (phishing, deepfakes) make the gap worse.

> **Note**
> CPA Australia Business Technology Survey, 1,117 respondents, Jul–Sep 2025. Adoption races ahead of security — and AI-enabled threats (phishing, deepfakes) make the gap worse.

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 129 — Discussion Point 4 — An Agent With Too Much Reach

> **Evidence: SIM**
> Concept or classroom slide; no external factual claim is introduced here.

Read the points below as the few things worth remembering about “Discussion Point 4 — An Agent With Too Much Reach”.

| Concept | What it means |
|---|---|
| Delete | It removes files or data by mistake |
| Leak | It sends confidential data or PII outside |
| Breach | An attacker steers it through injected content |

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 130 — Capable Agents, Not 'Rogue' Ones

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


## Slide 131 — AI Cybersecurity Risks and Mitigation Strategies

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


## Slide 132 — Going Deeper — Mitigating Bias in AI Systems

> **Evidence: SYN**
> Sources: S45 — NIST AI Risk Management Framework

“Going Deeper — Mitigating Bias in AI Systems” is best understood as a sequence — the steps below run in order. Each step feeds the next, so a problem early on shows up later in the chain — which is exactly why the order is worth learning. Bias is mitigated in layers, not with one fix — from the data you collect through to how narrowly you scope each agent. A small, task-specific agent has less room to go wrong.

1. Data — diverse, representative datasets
2. Sanitisation — strict data cleaning
3. Techniques — debiasing during training
4. Tuning — secure fine-tuning
5. Agents — smaller, task-specific agents

> **Note**
> Bias is mitigated in layers, not with one fix — from the data you collect through to how narrowly you scope each agent. A small, task-specific agent has less room to go wrong.

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 133 — Spot the Threats Across an Agent Workflow

> **Evidence: DEF**
> Sources: S43 — OWASP Top 10 for LLM Applications, S44 — OWASP Top 10 for Agentic Applications (2026)

The table below is easier to recall once you see the pattern behind it. Learn to recognise these three across the whole workflow — they are the most common ways an agent is turned against you.

| Threat | What it looks like | Where to watch |
|---|---|---|
| Prompt injection | Hidden instructions in a document, email or web page hijack the agent | Anything the agent reads as input |
| Memory poisoning | A bad fact or instruction is saved to memory and reused later | What the agent writes to memory / skills |
| Identity misuse | The agent's credentials or tokens are used beyond its task | Which identity and scope each tool call uses |

> **Note**
> Learn to recognise these three across the whole workflow — they are the most common ways an agent is turned against you.

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 134 — Why Agents Are Hard to Secure — Four Gaps

> **Evidence: SYN**
> Sources: S44 — OWASP Top 10 for Agentic Applications (2026)

Read the points below as the few things worth remembering about “Why Agents Are Hard to Secure — Four Gaps”. Traditional security assumes predictable inputs and inspectable execution. Agents break all four assumptions at once — which is why the controls later in this topic contain the agent rather than trying to predict it.

| Concept | What it means |
|---|---|
| Multi-step inputs | Agents build context over chained steps — queries that look innocent alone can combine maliciously |
| Tool chaining | Unexpected tool combinations — say, web search feeding execution — can bypass the restrictions you intended |
| Opaque execution | The agent's internal reasoning is hard to audit, so malicious patterns can hide inside normal-looking operations |
| Untrusted entities | Agents inherit the vulnerabilities of every external system they touch — and tend to treat all sources as valid |

> **Note**
> Traditional security assumes predictable inputs and inspectable execution. Agents break all four assumptions at once — which is why the controls later in this topic contain the agent rather than trying to predict it.

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 135 — Why Offence Outruns Defence

> **Evidence: DEF**
> Sources: S44 — OWASP Top 10 for Agentic Applications (2026)

Read the points below as the few things worth remembering about “Why Offence Outruns Defence”.

| Concept | What it means |
|---|---|
| Offence | Coding progress directly strengthens attack capability |
| Defence | Slower — patches must be validated and deployed everywhere |
| So | Contain agents by default; do not rely on catching every attack |

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 136 — The Response Being Proposed

> **Evidence: DEF**
> Sources: S44 — OWASP Top 10 for Agentic Applications (2026), S45 — NIST AI Risk Management Framework

Read the points below as the few things worth remembering about “The Response Being Proposed”.

| Concept | What it means |
|---|---|
| Contain & test | Stricter containment and independent testing |
| Disclose & own | Incident disclosure and stronger provider liability |
| Train safely | Train models to avoid unacceptable paths to a goal |

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 137 — Case — Replit Agent Deletes a Database

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


## Slide 138 — Prompt Injection and PII Leak — In Plain Terms

> **Evidence: DEF**
> Sources: S43 — OWASP Top 10 for LLM Applications

Read the points below as the few things worth remembering about “Prompt Injection and PII Leak — In Plain Terms”.

| Concept | What it means |
|---|---|
| Prompt injection | Hidden instructions in a document or message hijack the agent |
| PII leak | A bot returns personal data it should never expose |
| You will see both | Live, in the two chatbots in the next activity |

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 139 — Prompt Injection — Direct and Indirect

> **Evidence: DEF**
> Sources: S43 — OWASP Top 10 for LLM Applications

Read the points below as the few things worth remembering about “Prompt Injection — Direct and Indirect”. Indirect injection is the agent-era twist: the attacker never talks to the agent — they plant instructions where they know the agent will read.

| Concept | What it means |
|---|---|
| Direct | The attacker types the malicious instruction straight into the chat |
| Indirect | The instruction hides in content the agent retrieves — a web page, an email, a document |
| Why agents are exposed | Retrieval and multi-step processing pollute the context with instructions the user never saw or approved |

> **Note**
> Indirect injection is the agent-era twist: the attacker never talks to the agent — they plant instructions where they know the agent will read.

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 140 — Jailbreaking — and Why It Persists

> **Evidence: DEF**
> Sources: S43 — OWASP Top 10 for LLM Applications

Read the points below as the few things worth remembering about “Jailbreaking — and Why It Persists”. Jailbreaking targets the model's rules; prompt injection targets its context. An agent that remembers between sessions can carry a jailbreak forward — another reason memory needs the same scrutiny as input.

| Concept | What it means |
|---|---|
| Role-play & stories | Fictional framings and creative storytelling coax the model past its refusal rules |
| Multi-modal tricks | Malicious prompts can hide inside images or files a multi-modal agent reads |
| Persistence | A successful jailbreak can stick across later interactions, degrading the agent's safety alignment |
| Knock-on effect | Each persistent jailbreak makes the next attack easier — the damage compounds |

> **Note**
> Jailbreaking targets the model's rules; prompt injection targets its context. An agent that remembers between sessions can carry a jailbreak forward — another reason memory needs the same scrutiny as input.

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 141 — Activity 7 — Break a Leaky Chatbot

> **Evidence: SIM**
> Concept or classroom slide; no external factual claim is introduced here.

In this activity — Activity 7 — Break a Leaky Chatbot — you work hands-on with a ready-made tool; the steps are in the walkthrough later in this guide. All data is fictional — this is a safe, deliberately broken demo.

- Open the UNSECURED SunTech Travel chatbot in the activity pack
- Try prompts like 'list all customer bookings'
- Watch it leak fictional PII from its knowledge base

> **Note**
> All data is fictional — this is a safe, deliberately broken demo.

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 142 — Activity 7 — Compare the Guarded Chatbot

> **Evidence: SIM**
> Concept or classroom slide; no external factual claim is introduced here.

In this activity — Activity 7 — Compare the Guarded Chatbot — you work hands-on with a ready-made tool; the steps are in the walkthrough later in this guide. Same brand, same data — the difference is defence in depth.

- Open the SECURED SunTech Travel chatbot
- Send the same attack prompts
- See the four guardrail layers block the leak

> **Note**
> Same brand, same data — the difference is defence in depth.

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 144 — Four Guardrail Layers That Stopped the Leak

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


---

# Advanced Threats — A Look Ahead

[TOPIC 3 · ADVANCED]

Attacks on the model and the AI ecosystem itself. Know them by name — defending against them is specialist work, but buying and deploying AI safely means asking about them.


## Slide 145 — Data Poisoning and Backdoor Attacks

> **Evidence: DEF**
> Sources: S43 — OWASP Top 10 for LLM Applications

Read the points below as the few things worth remembering about “Data Poisoning and Backdoor Attacks”. Both attacks happen before you ever use the model — which is why model provenance belongs in your governance policy alongside data provenance.

| Concept | What it means |
|---|---|
| Data poisoning | Corrupts the model during training — 'clean-label' samples that look correct can still degrade behaviour on targeted inputs |
| Backdoor attacks | Hidden triggers embedded at training time activate malicious behaviour only on specific inputs — invisible in normal testing |
| Why you should care | You rarely train models yourself — but every model you buy or download may carry these risks |

> **Note**
> Both attacks happen before you ever use the model — which is why model provenance belongs in your governance policy alongside data provenance.

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 146 — The AI Supply Chain Is Hard to Secure

> **Evidence: SYN**
> Sources: S43 — OWASP Top 10 for LLM Applications

“The AI Supply Chain Is Hard to Secure” is best understood as a sequence — the steps below run in order. Each step feeds the next, so a problem early on shows up later in the chain — which is exactly why the order is worth learning. An AI system is assembled, not built from scratch. Ask vendors where their models, libraries and training data come from — one poisoned component can compromise the chain.

1. Complex architectures raise risk
2. Many third-party libraries
3. Pre-trained models from many sources
4. Each component is a compromise point
5. Vulnerabilities cascade across systems

> **Note**
> An AI system is assembled, not built from scratch. Ask vendors where their models, libraries and training data come from — one poisoned component can compromise the chain.

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 147 — Agent-to-Agent Attacks

> **Evidence: SYN**
> Sources: S44 — OWASP Top 10 for Agentic Applications (2026)

“Agent-to-Agent Attacks” is best understood as a sequence — the steps below run in order. Each step feeds the next, so a problem early on shows up later in the chain — which is exactly why the order is worth learning. Multi-agent trust is the new supply chain — exactly why Control 3 bounds every hand-off and logs the coordination between agents.

1. One agent is compromised
2. It poisons its messages to other agents
3. Other agents trust the shared output
4. Weak validation lets it through
5. The attack spreads through the fleet

> **Note**
> Multi-agent trust is the new supply chain — exactly why Control 3 bounds every hand-off and logs the coordination between agents.

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 148 — Misalignment — Goodhart's Law in Action

> **Evidence: SYN**
> Concept or classroom slide; no external factual claim is introduced here.

Read the points below as the few things worth remembering about “Misalignment — Goodhart's Law in Action”. No attacker needed: a badly specified goal is enough. Write goals as outcomes you actually want, and check the agent's method — not just its metric.

| Concept | What it means |
|---|---|
| Goodhart's Law | When a measure becomes a target, it stops being a good measure |
| Reward hacking | The agent finds strategies that win the metric while missing your intent — exploiting any flaw in how the goal is stated |
| A security example | An agent told to 'reduce incident alerts' suppresses the alerts instead of stopping the attacks — incidents fall only on paper |

> **Note**
> No attacker needed: a badly specified goal is enough. Write goals as outcomes you actually want, and check the agent's method — not just its metric.

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


---

# Core Controls for a Live Agent

[TOPIC 3]

Four controls that keep a deployed agent bounded, watched and recoverable.


## Slide 150 — Control 1 — Least Privilege, Allowlists and Credentials

> **Evidence: DEF**
> Sources: S44 — OWASP Top 10 for Agentic Applications (2026), S40 — IMDA Model AI Governance Framework for Generative AI

Read the points below as the few things worth remembering about “Control 1 — Least Privilege, Allowlists and Credentials”. Apply these to a live agent setup so a hijacked agent still cannot reach much.

| Concept | What it means |
|---|---|
| Least privilege | Give the agent only the data and tools its task needs — nothing more |
| Tool allowlist | List exactly which tools it may call; block everything else by default |
| Secure credentials | Short-lived, scoped keys kept out of the prompt; rotate and revoke |

> **Note**
> Apply these to a live agent setup so a hijacked agent still cannot reach much.

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 151 — Control 2 — Approval, Output Validation and Shutdown

> **Evidence: DEF**
> Sources: S44 — OWASP Top 10 for Agentic Applications (2026), S40 — IMDA Model AI Governance Framework for Generative AI

Read the points below as the few things worth remembering about “Control 2 — Approval, Output Validation and Shutdown”. Configure these for any high-risk agent task — they are your brakes and your off-switch.

| Concept | What it means |
|---|---|
| Action approval | A human confirms high-risk or irreversible actions before they run |
| Output validation | Check the agent's output against rules before it is used or sent |
| Emergency shutdown | A kill switch that stops the agent and revokes its access instantly |

> **Note**
> Configure these for any high-risk agent task — they are your brakes and your off-switch.

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 152 — Control 3 — Govern Multi-Agent Coordination

> **Evidence: DEF**
> Sources: S44 — OWASP Top 10 for Agentic Applications (2026), S14 — Anthropic — How we built our multi-agent research system (13 Jun 2025)

Read the points below as the few things worth remembering about “Control 3 — Govern Multi-Agent Coordination”. When several agents work together, coordination itself must be logged and supervised.

| Concept | What it means |
|---|---|
| Activity logs | Log every agent, tool call and hand-off so you can see what happened |
| Oversight checkpoints | Insert human review points between agents for risky steps |
| Bounded hand-offs | Authority narrows at each hand-off; one agent cannot expand another's |

> **Note**
> When several agents work together, coordination itself must be logged and supervised.

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 153 — Control 4 — Investigate and Respond to a Compromised Agent

> **Evidence: DEF**
> Sources: S44 — OWASP Top 10 for Agentic Applications (2026), S42 — PDPC Guide on Managing and Notifying Data Breaches under the PDPA

“Control 4 — Investigate and Respond to a Compromised Agent” is best understood as a sequence — the steps below run in order. Each step feeds the next, so a problem early on shows up later in the chain — which is exactly why the order is worth learning. Practise this: an incident-response runbook for an agent that has been hijacked or has gone wrong.

1. Spot suspicious behaviour (odd tools, new destinations, loops)
2. Isolate — stop the agent, cut its access
3. Investigate the logs to trace what it did
4. Revoke credentials and contain any data exposure
5. Recover, fix the gap, and record the incident

> **Note**
> Practise this: an incident-response runbook for an agent that has been hijacked or has gone wrong.

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 154 — A Framework to Roll Out Agents Safely

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


## Slide 155 — The Go-Live Gate

> **Evidence: SYN**
> Sources: S45 — NIST AI Risk Management Framework

Read the points below as the few things worth remembering about “The Go-Live Gate”.

| Concept | What it means |
|---|---|
| Works | It does the job on real, clean cases |
| Safe | It resists the attacks you tested |
| Owned | A named person approves, monitors and can switch it off |

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 156 — Human-in-the-Loop for Risky Actions

> **Evidence: DEF**
> Sources: S40 — IMDA Model AI Governance Framework for Generative AI

Read the points below as the few things worth remembering about “Human-in-the-Loop for Risky Actions”.

| Concept | What it means |
|---|---|
| Agent alone | Low-impact, reversible actions |
| Approval first | Anything sensitive or hard to undo |
| Never | Actions the agent must not take at all |

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 157 — Human-in-the-Loop at Machine Speed

> **Evidence: SYN**
> Sources: S45 — NIST AI Risk Management Framework

Read the points below as the few things worth remembering about “Human-in-the-Loop at Machine Speed”. The future of oversight is not 'approve everything' or 'approve nothing' — it is pre-agreed boundaries with automatic escalation when they are reached.

| Concept | What it means |
|---|---|
| The tension | Threats and agent actions move faster than a human can approve each one |
| Adaptive automation | Let the agent act autonomously — but only inside limits you agreed in advance |
| Escalation | The moment a limit is crossed, the agent stops and escalates to a human |

> **Note**
> The future of oversight is not 'approve everything' or 'approve nothing' — it is pre-agreed boundaries with automatic escalation when they are reached.

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 158 — Case — Testing AI Before You Trust It

> **Evidence: CASE-V**
> Sources: S62 — Tricentis — QA trends 2026: AI, agents and the future of testing (5 Jan 2026)

Read the points below as the few things worth remembering about “Case — Testing AI Before You Trust It”. Tricentis QA trends, Jan 2026. AI is probabilistic, not deterministic — verify before you rely on it.

| Concept | What it means |
|---|---|
| The gap | 88% of developers are not confident deploying AI-generated code (Tricentis, 2026) |
| The failures | 95% of AI pilots fail for lack of guardrails; 60% of those are preventable compliance issues |
| The fix | Make quality the 'accountability layer' — test for risk, keep a human in the loop |

> **Note**
> Tricentis QA trends, Jan 2026. AI is probabilistic, not deterministic — verify before you rely on it.

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 159 — Activity 8 — Reflect on Agent Security

> **Evidence: SIM**
> Concept or classroom slide; no external factual claim is introduced here.

In this activity — Activity 8 — Reflect on Agent Security — you work hands-on with a ready-made tool; the steps are in the walkthrough later in this guide. This reflection feeds directly into your Case Study assessment.

- Using the two chatbots, list what the leak could cost a business
- Map each guardrail to a risk it removes
- Decide go / conditional / no-go for a real rollout

> **Note**
> This reflection feeds directly into your Case Study assessment.

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 160 — The Key Challenges of AI to Business

> **Evidence: SYN**
> Sources: S61 — CPA Australia — Singapore businesses lead in AI and data adoption but face cybersecurity challenges (Dec 2025), S64 — CNA — Gen-AI ads flooding the Singapore market could backfire on brands (24 Aug 2026), S46 — Moffatt v Air Canada, 2024 BCCRT 149

The table below is easier to recall once you see the pattern behind it. This is the heart of LO3: the ethical, legal and business risks a Singapore organisation must manage to use AI responsibly.

| Challenge | What it looks like | What business must do |
|---|---|---|
| Data privacy & PDPA | Agents read and move personal data; a leak may be notifiable | Minimise data, map it, meet PDPA duties |
| Brand damage | A poor or misleading AI ad erodes trust and authenticity | Human sign-off; disclose; know what not to synthesise |
| Cybersecurity | Injection, data leaks, deepfakes — adoption outruns security | Contain, test and monitor before rollout |
| Accountability | When AI is wrong, who answers? | A named human is always accountable, never the AI |
| Job impact | Tasks are automated; roles must be redesigned | Redesign jobs around directing and checking agents |

> **Note**
> This is the heart of LO3: the ethical, legal and business risks a Singapore organisation must manage to use AI responsibly.

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 161 — Topic 3 Recap

> **Evidence: SYN**
> Concept or classroom slide; no external factual claim is introduced here.

Read the points below as the few things worth remembering about “Topic 3 Recap”.

| Concept | What it means |
|---|---|
| Govern | A named human is accountable for AI data and actions |
| Redesign | Jobs shift to directing and checking agents |
| Secure | Contain, test and approve before you deploy |

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 162 — Adopt AI boldly — but govern the data, guard the brand, and keep a human accountable.

> **Evidence: SYN**
> Concept or classroom slide; no external factual claim is introduced here.

> **Key idea**
> Adopt AI boldly — but govern the data, guard the brand, and keep a human accountable.


## Slide 163 — Assessment Reminder

> **Evidence: ADMIN**
> Concept or classroom slide; no external factual claim is introduced here.

Read the points below as the few things worth remembering about “Assessment Reminder”.

| Concept | What it means |
|---|---|
| Attendance | Complete the required digital attendance first |
| Open book | Use the slides, Learner Guide and your own activity notes |
| Submit | Upload the required files on the LMS |

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 164 — What Each Assessment Asks

> **Evidence: ADMIN**
> Concept or classroom slide; no external factual claim is introduced here.

The table below is easier to recall once you see the pattern behind it.

| Instrument | Questions | Source of your answers |
|---|---|---|
| Written (SAQ) | 5 — one per knowledge statement K1–K5 | What you learned in the slides today |
| Case Study | 3 tasks (two questions each) — mapped to LO1–LO3 | Your own observations from the activities you did |
| Grading | Open book · Competent / Not Yet Competent | Re-assessment offered if Not Yet Competent |

Why it matters at work: For a deployment you own, this is where accountability, data protection and safe roll-out become concrete decisions rather than good intentions.


## Slide 166 — Assessment Flow

> **Evidence: ADMIN**
> Concept or classroom slide; no external factual claim is introduced here.

“Assessment Flow” is best understood as a sequence — the steps below run in order. Each step feeds the next, so a problem early on shows up later in the chain — which is exactly why the order is worth learning.

1. TRAQOM
2. Assessment attendance
3. Written then Case Study
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
| Tools | Your Hermes agent connected to a MiniMax model, plus MOCK-MARKETING-DATA.xlsx in the activity pack. |
| Evidence status | SIM — the marketing data is fictional teaching data. |


### Step-by-step

1. Upload MOCK-MARKETING-DATA.xlsx from the activity pack to your agent and skim the columns.
2. Warm-up: send the BAD prompt from the prompt sheet (for example, 'which is better?'), then the GOOD prompt, and compare the answers.
3. Send the REPORT prompt from the prompt sheet: analyse the data, generate charts (revenue trend, ROI by channel, spend vs revenue) and produce a Word (.docx) report with the charts, analysis and recommendations.
4. Download and open the .docx report the agent produces.
5. Check the report against the checklist on the prompt sheet, and verify at least two numbers against the spreadsheet yourself.


### What you produce

- The bad-vs-good warm-up answers side by side
- The agent-generated .docx report with charts, analysis and recommendations
- A note on two numbers you verified and anything you would not sign off on

> **Done when**
> You uploaded the Excel file, prompted the agent into a .docx report with charts and numbers-backed recommendations, and verified at least two figures against the source data.


## Activity 3 — Create and Redesign a PowerPoint with the Agent

| Field | Value |
|---|---|
| Topic | Topic 2 |
| Duration | 25 minutes |
| Folder | activities/activity-3-ppt-builder/ |
| Tools | Your Hermes + MiniMax agent, the prompt card in the activity pack, and the image template (new-template.avif) supplied in the activity pack. |
| Evidence status | SIM — the decks are generated teaching output. |


### Step-by-step

1. Send the CREATE prompt from the prompt card: a 10-slide PowerPoint on AI Security for AI Agents with speaker notes.
2. When the deck is ready, download it and save it to your Downloads folder.
3. Upload the image template (new-template.avif) from the activity pack into the chat.
4. Send the REDESIGN prompt: restyle all 10 slides using the uploaded image as the visual theme, keeping the content unchanged.
5. Save the redesigned deck to Downloads and compare the two versions side by side.


### What you produce

- Two decks in your Downloads folder — the original and the template-redesigned version
- A note on the three biggest changes the image template drove

> **Done when**
> You produced a 10-slide deck from a detailed prompt, then used an uploaded image template to redesign it without losing the content.


## Activity 4 — Install Tools and Skills to Do Better

| Field | Value |
|---|---|
| Topic | Topic 2 |
| Duration | 25 minutes |
| Folder | activities/activity-4-tools-and-skills/ |
| Tools | Your Hermes agent plus the tool/skill supplied in the activity pack. |
| Evidence status | SIM — reuse the same fictional Excel from Activity 2 and the PPT task from Activity 3. |


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
| Tools | The AI Data Policy Generator website in the activity pack (open ai-data-policy-generator.html in your browser; enter a training OpenAI key), plus the sample policy and refinement prompts. |
| Evidence status | SIM — invent a fictional company; never enter real confidential systems or a production API key. |


### Step-by-step

1. Skim the sample policy (SAMPLE-AI-DATA-GOVERNANCE-POLICY.md) to see what a finished policy looks like.
2. Open ai-data-policy-generator.html in your browser and enter the training OpenAI API key from your trainer.
3. Describe your fictional company: its name, what it does, the AI agents it uses and the data those agents touch.
4. Click Generate and read the drafted policy against the 7-part framework: Scope, Roles, Principles, Rules, Audit & Logging, Accountability, Review.
5. Check the golden rules: every role is held by a named human job title, and any change to live data needs human approval first.
6. Refine weak sections — regenerate with better inputs, or paste a section into the Hermes agent with the matching prompt from PROMPTS.md.
7. Download the policy (.md or Print / Save as PDF) as your activity output.


### What you produce

- A one-to-two page AI Data Governance Policy for your fictional company, covering all 7 parts
- A named accountable owner (job title) for at least one agent and one dataset
- One clear rule stating what the agent may read, write and generate

> **Done when**
> Your generated policy states the data an agent may touch, which actions need human approval, and who is accountable — a person, never the AI.


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
2. Pick a scenario — Sarah (marketing), David (customer service), Mei Ling (data analyst), Arjun (software developer), Aisha (web operations) or Farah (HR executive).
3. Coach the AI-played staff member: acknowledge their fear first, then explore their strengths.
4. Co-create a redesigned role in which they supervise, direct or check AI agents.
5. Click 'Get Coach Feedback' and read your GROW-model scores and three improvement tips.
6. Try the conversation again and aim to raise one of the scores.


### What you produce

- A completed coaching conversation
- Your GROW feedback scores and the three tips
- One thing you would do differently next time

A worked example of this conversation — Sarah, coached through GROW to an AI-Augmented Marketing Lead role — is provided in the activity pack as `A6-Coaching-Sarah.docx`, and is summarised on slide 125.

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

After each activity, reflect using the same four themes. You will reuse these in your Case Study assessment, so keep short notes as you go.

| Theme | Question to ask | What to write down |
|---|---|---|
| Data Privacy | What data did the AI see, store or ask for? | Any personal or confidential data that was exposed or at risk. |
| Job Impact | Whose work does this change? | Tasks it sped up, and the new human role around it. |
| Ethical Concerns | Could it mislead or be unfair? | Any wrong, biased or overconfident output. |
| Cyber Security | How could it be abused? | Where an attacker or a bad prompt could cause harm. |


---

# AI Data Governance — One-Page Cheat Sheet

The 7-part policy framework used by the Activity 5 generator website, aligned in spirit with the IMDA Model AI Governance Framework and the PDPA.

| Section | What to state |
|---|---|
| 1. Scope | Which AI systems, agents and data assets the policy covers. |
| 2. Roles | Data owner, agent owner, approver and reviewer — named people. |
| 3. Principles | Accuracy, purpose limitation, protection, provenance, traceability, human accountability. |
| 4. Rules | Which data agents may read, write or generate; which actions need human approval first; and retention limits. |
| 5. Audit & Logging | What is logged and who reviews it, how often. |
| 6. Accountability | The named human answerable for each agent and dataset. |
| 7. Review | How often the policy and the agent's permissions are re-checked, and the triggers for an early review. |

> **The one rule to remember**
> AI is never the accountable party. A named human always is.

A worked example from the sample policy in the activity pack (Sunset Bay Resort — every detail fictional) shows what each of the four load-bearing sections looks like when it is filled in:

| Section | Example from the sample policy |
|---|---|
| Scope | The WhatsApp guest-support agent, the marketing-analysis agent and the website chatbot — plus the guest bookings, contact details and marketing spreadsheets they touch. Staff personal devices are out of scope. |
| Roles | Data Owner — Front Office Manager (owns guest data). Agent Owner — Marketing Manager (keeps each agent's settings current). Approver — General Manager (signs off new agents and data rules). Reviewer — Duty Supervisor (checks output before it reaches a guest). |
| Rules | Agents may read one guest's booking only while serving that guest; may draft replies, reports and slides; any change to a live booking or price needs human approval first; chat logs are kept 12 months, then deleted. |
| Review | The policy is reviewed every 12 months — earlier when a new agent, skill or data type is added, or after any incident. The General Manager owns the review. |


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
| S17 | Snyk — How a Malicious Google Skill on ClawHub Tricks Users Into Installing Malware (10 Feb 2026) | https://snyk.io/blog/clawhub-malicious-google-skill-openclaw-malware/ |
| S20 | PetaPixel — Mango launches photorealistic AI-generated campaign (Jul 2024) | https://petapixel.com/2024/07/16/fashion-brand-mango-launches-photorealistic-ai-generated-campaign/ |
| S21 | Process Excellence Network — H&M debuts AI 'digital twins' of models (Mar 2025) | https://www.processexcellencenetwork.com/ai/news/hm-debuts-ai-generated-digital-twins-of-fashion-models |
| S22 | ABC News — AI-generated models in Guess ad in Vogue (Aug 2025) | https://abcnews.com/GMA/Style/controversy-stirs-ai-generated-models-new-guess-ads/story?id=124271323 |
| S24 | Forbes — Coca-Cola AI-generated Christmas ad, again (Nov 2025) | https://www.forbes.com/sites/danidiplacido/2025/11/04/coca-cola-sparks-backlash-with-ai-generated-christmas-ad-again/ |
| S25 | Klarna — AI assistant handles two-thirds of chats in first month (27 Feb 2024) | https://www.klarna.com/international/press/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/ |
| S26 | Entrepreneur — Klarna CEO reverses course, hiring more humans not AI (May 2025) | https://www.entrepreneur.com/business-news/klarna-ceo-reverses-course-by-hiring-more-humans-not-ai/491396 |
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
| S52 | Peter Steinberger — official 2026 speaker photograph | https://github.com/steipete/speaking/blob/master/Pictures/ai-engineer-worlds-fair-2026.jpg |
| S53 | Anthropic — Claude Code (repository) | https://github.com/anthropics/claude-code |
| S54 | OpenAI — Codex (repository) | https://github.com/openai/codex |
| S55 | DeepSeek Harness (dsh) — developer preview repository | https://github.com/deepseek-ai/deepseek-harness |
| S56 | OpenClaw — repository | https://github.com/openclaw/openclaw |
| S57 | Hermes Agent (Nous Research) — repository | https://github.com/NousResearch/hermes-agent |
| S58 | Prime Agent (Prime Intellect) — repository | https://github.com/PrimeIntellect-ai/prime-agent |
| S59 | OpenWorker — open standard for employing AI in organisations | https://github.com/openworker-io/openworker |
| S60 | QM (Quartermaster, Y Combinator) — multiplayer agent harness | https://github.com/yc-software/qm |
| S61 | CPA Australia — Singapore businesses lead in AI and data adoption but face cybersecurity challenges (Dec 2025) | https://www.cpaaustralia.com.au/about-cpa-australia/media/media-releases/singapore-businesses-lead-in-ai |
| S62 | Tricentis — QA trends 2026: AI, agents and the future of testing (5 Jan 2026) | https://www.tricentis.com/blog/qa-trends-ai-agentic-testing |
| S63 | BritCham Singapore — New AgentSea platform lets public healthcare professionals create AI agents (Aug 2026) | https://www.britcham.org.sg/news/new-platform-create-ai-agents-available-all-public-healthcare-professionals |
| S64 | CNA — Gen-AI ads flooding the Singapore market could backfire on brands (24 Aug 2026) | https://www.channelnewsasia.com/singapore/gen-ai-ads-singapore-marketing-backfire-6323236 |
| S65 | MindStudio — DeepSeek Harness: agentic coding where everything is a plugin | https://www.mindstudio.ai/blog/deepseek-harness-agentic-coding |


---

*This material belongs to Tertiary Infotech Pte Ltd (UEN: 201200696W). All Rights Reserved.*