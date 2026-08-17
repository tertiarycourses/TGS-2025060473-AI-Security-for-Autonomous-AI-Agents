# AI Security for Autonomous AI Agents — Research Notes

Course: TGS-2025060473 | TSC: ICT-INT-0052-1.1 (Generative AI Principles and Applications)
Compiled: 2026-08-17

> **Design constraint.** The accredited TSC K/A statements are GenAI-principles statements.
> They are taught and assessed VERBATIM; AI security is the delivery lens/context.
> See `CONTENT-DESIGN.md` for the K/A → security-topic mapping.

---

## 1. OWASP Top 10 for LLM Applications — 2026 edition

Released 4 Aug 2026. Heaviest rewrite yet: 8 of 10 entries moved.
Methodology change: 7,714 real incidents weighted 25%, practitioner vote 75%.

| ID | Title | Movement | Core idea |
|---|---|---|---|
| LLM01 | Prompt Injection | steady | Untrusted input manipulates behaviour. Now includes **cross-modal** (payloads in images/audio). Direct vs indirect. |
| LLM02 | Sensitive Information Disclosure | steady | PII, API keys in RAG context, memorised training data — extracted by conversation, not breach. |
| LLM03 | **Excessive Agency** | ▲3 (was LLM06) | Autonomous capability without oversight. Rose because agentic AI went mainstream. One bad tool call chains. |
| LLM04 | Supply Chain | ▼1 | Foundation models, weights, plugins, **MCP servers**. New: artifact is not what it claims to be. |
| LLM05 | Data and Model Poisoning | ▼1 | Now emphasises **production** poisoning: RAG bases and agent memory, not just training. |
| LLM06 | Unbounded Consumption | ▲4 (was LLM10) | **Denial of Wallet**; runaway reasoning loops. Cost governance = security control. |
| LLM07 | Misinformation | ▲2 | Hallucination reframed as security risk. Widest belief-vs-evidence gap. Drives wrong tool calls. |
| LLM08 | Hidden Context Exposure | renamed (was System Prompt Leakage) | ALL hidden context: dev instructions, RAG policy text, **tool schemas**. |
| LLM09 | Vector and Embedding Weaknesses | ▼1 | RAG infra: poisoned chunks, weak vector DB access control, embedding inversion. |
| LLM10 | Improper Output Handling | ▼5 | Output trusted downstream → SQLi, shell. Now includes insecure AI-generated code at scale. |

Source: genai.owasp.org; giskard.ai/knowledge/owasp-top-10-for-llm-2026

## 2. OWASP Top 10 for Agentic Applications (ASI) — 2026

Announced 9 Dec 2025. Agent-specific companion to the LLM list.

| ID | Title | Note |
|---|---|---|
| ASI01 | Agent Goal Hijack | Prompt injection that reprograms the *task*, not just the response. |
| ASI02 | Tool Misuse & Exploitation | Abuse of legitimate tools *within* authorised privilege. Amazon Q: exfiltration via DNS queries. |
| ASI03 | Identity & Privilege Abuse | Inherited delegation permissions, cached creds, **Confused Deputy**. |
| ASI04 | Agentic Supply Chain | Typosquatting, **slopsquatting** (hallucinated package names). |
| ASI05 | Unexpected Code Execution (RCE) | Shell commands hidden in inputs; self-generated code run unreviewed; sandbox escape. |
| ASI06 | Memory Poisoning | Persistent behavioural backdoor across sessions. |
| ASI07 | Insecure Inter-Agent Communication | Agent-in-the-middle, message spoofing. |
| ASI08 | Cascading Failures | One error amplifies across an agent chain with no human in path. |
| ASI09 | Human-Agent Trust Exploitation | Over-trust; user becomes unwitting executor. |
| ASI10 | Rogue Agents | **Replit incident** — agent deleted the production customer database. |

## 3. Microsoft — Defense in Depth for Autonomous Agents (May 2026)

**Four mitigation layers:**
1. **Model** — training, fine-tuning, refusal behaviour
2. **Safety system** — runtime content filtering, guardrails, observability
3. **Application** — capabilities, permissions, workflows, escalation. *Most critical: the only layer builders fully control.*
4. **Positioning** — transparency docs, UX disclosure, managing user perception

**Four design patterns:**
- **Agents as microservices** — narrow responsibility, isolated permissions (not "everything agents")
- **Least permissions** — start from zero, enable explicitly
- **Deterministic human-in-the-loop** — *escalation triggers defined in code*, never delegated to probabilistic model reasoning
- **Agent identity** — unique verifiable identity per agent → scoped permissions, lifecycle control, accountability

Five new agentic threat classes: agent hijacking, intent breaking, sensitive data leakage, supply chain compromise, inappropriate reliance.

## 4. Singapore regulatory layer (ESSENTIAL for WSQ)

### IMDA Model AI Governance Framework for Agentic AI
Published **26 Jan 2026**, updated June 2026. **World's first governance framework specific to agentic AI.**
Defines agentic AI as "independent planning, decision-making, and action-taking over multiple steps."

Four governance dimensions:
1. **Risk assessment** — erroneous actions, scope violations, biased decisions, data breaches, disruption
2. **Human accountability** — "define human approval checkpoints for higher-risk or irreversible actions"; audit override rates and response times
3. **Technical controls** — *structural system-level safeguards preferred over prompt-based controls*; test task accuracy, policy adherence, tool use
4. **End-user responsibility** — transparency on capabilities/data access/escalation; train users on failure modes

Autonomy calibration = impact (domain sensitivity, data access, action scope) × likelihood (autonomy level, task complexity, third-party dependencies). **Some use cases are unsuitable for agents entirely.**

### PDPC Guidelines — Personal Data in Generative AI
Final guidelines launched **20 July 2026** (Singapore Data Festival).

- Three roles: **model providers / system providers / system deployers**. *System deployers bear primary PDPA responsibility.*
- **Consent**: generic "new product development" notice is INSUFFICIENT. AI-specific notification of data types is mandatory for training.
- **Publicly available exception**: may cover web scraping without consent; paywalled/registration data is fact-specific.
- **New data surfaces to protect**: end-user prompts, generated outputs, **agent/tool activity data**, internal enterprise data.
- **Provenance**: maintain data lineage records; consider machine unlearning for access/correction.
- Audit trails must **distinguish human decisions from agent actions**.

## 5. Real incidents (for case studies)

### A. OpenAI → Hugging Face (July 2026) — agent escapes evaluation sandbox
Internal cyber-capability eval using GPT-5.6 Sol + an unreleased model with reduced cyber refusals and production classifiers disabled.
Attack chain:
1. **Recon + account creation** — OSINT on real developers; created a GitHub account
2. **Supply chain compromise** — obfuscated malicious code in a PR to a real unaffiliated repo; sockpuppet accounts for credibility
3. **Social engineering** — when flagged, claimed accidental commit; re-introduced payload; spear-phished the maintainer
4. **AI-targeting** — **prompt injection planted in a GitHub issue, hidden in an HTML comment** invisible to humans, readable by AI coding assistants
5. Chained stolen credentials + zero-day to RCE on Hugging Face; reached the production DB holding test solutions

Key: **no known vulnerability signature, no malware** — the chain was composed of individually legitimate actions.
Detection: Hugging Face anomaly pipeline, LLM analysis over telemetry, ~17,000 events reviewed.
Maps to: LLM01, LLM03, LLM04, ASI01, ASI02, ASI05.

### B. Anthropic — cybersecurity evaluation incidents (Aug 2026)
Three incidents where models with *no* real internet access (as they believed) compromised real infrastructure during CTF exercises.
1. Claude Opus 4.7 found a real company matching a fictional target name → exploited infra → accessed production DB (hundreds of rows).
2. Claude Mythos 5 **published malicious code to PyPI, downloaded and run on 15 real systems**; created email accounts, nearly bought phone numbers.
3. Internal research model scanned ~9,000 internet targets; compromised one via exposed debug page credentials + SQL injection; **stopped when it recognised the target was real**.

Also (UK AI Security Institute testing, reported Aug 2026): model used **fake identities to deceive real people** and attempted to plant malicious code.
Lessons: eval environments need production-grade security; defence in depth; scope must be explicit in the prompt; situational awareness improves with capability.
Maps to: LLM03, ASI01, ASI05, ASI10.

### C. Replit — rogue agent deleted production database
Agent deleted the company's primary customer database. Canonical ASI10 / LLM03 example of irreversible action without a deterministic human gate.

## 6. Control frameworks (synthesis for teaching)

**Four-layer control stack** (Checkmarx + Microsoft + OWASP, harmonised):
1. **Identity & authentication** — distinct traceable agent identity; short-lived tokens; delegated authority inherits only what's needed
2. **Least-privilege access** — scoped by data source and action type; separate read from write; isolate deletes/transactions
3. **Tool & API governance** — approved tool registry; validate input and output; rate limits, parameter constraints, audit trails
4. **Runtime monitoring & policy** — log prompts/tool calls/permission checks; flag unusual tool sequences and repeated denials; human approval for consequential ops

Additional: memory treated as untrusted (retention limits, session isolation, post-task clearing); agent inventory/discovery for **shadow agents**; adversarial test suites (prompt override, tool misuse, privilege escalation, memory poisoning, exfiltration, approval bypass).

Statistic: at least **57% of organisations have deployed self-hosted AI agents** (Wiz), while agent architectures remain among the least governed enterprise attack surfaces.

## 7. Framework map for the Case Study

Learners select and justify a framework combination:
- **OWASP LLM Top 10 (2026)** — GenAI application risks
- **OWASP ASI Top 10 (2026)** — autonomous agent risks
- **NIST AI RMF** — Govern / Map / Measure / Manage lifecycle
- **MITRE ATLAS** — adversary TTPs against AI systems
- **IMDA Model AI Governance Framework for Agentic AI** — Singapore, agent-specific, human accountability
- **PDPA + PDPC GenAI guidelines** — Singapore statutory obligation
