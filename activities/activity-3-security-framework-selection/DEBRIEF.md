# Activity 3 — Trainer Debrief

## Selecting a Security Framework for GenAI and Agents

**Facilitation time:** 25 minutes after the 60-minute group work.
**Purpose:** establish that frameworks are **instruments with different jobs**, not competing brands —
and that a governance claim is worth nothing until it is expressed as a measured threshold with a
stated false-positive cost.

Two K/A statements again, and again one is louder. **A3** is the framework combination. **A5** is the
red-team table, and it is where the real teaching happens — Q4 and Q5 are the heart of this activity.
Groups love arguing about frameworks and will happily burn 45 minutes on Q1–Q3. **Give them a hard
20-minute call to be on Q4**, and protect Q5 completely; the FTE calculation in Q5 is the moment the
room goes quiet.

---

## Q1 — What each framework is for

**Expected answer.**

| Framework | Kind of artefact | The question it answers |
|---|---|---|
| OWASP LLM Top 10 2026 | Threat taxonomy | *What can go wrong in a GenAI application?* |
| OWASP ASI Top 10 2026 | Threat taxonomy (agentic) | *What can go wrong when the system plans and acts?* |
| NIST AI RMF | Lifecycle process | *How do we run risk management continuously, and who owns it?* |
| MITRE ATLAS | Adversary knowledge base (TTPs) | *How do real attackers actually do it, so what do we test and hunt for?* |
| IMDA Agentic AI Framework | Governance framework | *Who is accountable, where are the human checkpoints, is this use case even suitable?* |
| PDPA + PDPC GenAI guidelines | **Statutory obligation** | *What does the law require of us as system deployer?* |

**The one with no choice attached is PDPA.** This distinction matters more than it looks. The other
five are *selected* — a group can argue for or against MITRE ATLAS on cost-benefit grounds and be
right either way. PDPA is not selected; it applies. So it does not belong in the "which framework
should we adopt?" conversation at all. It belongs in the constraints column, alongside the Healthcare
Services Act. Groups that put PDPA in a comparison matrix scored against the others have made a
category error, and it is a productive one to surface: **you cannot be "partially compliant" with a
statute the way you can be partially aligned to a taxonomy.**

**What the integrator's attestation does not tell the board.** At least three:

1. **It covers the wrong scope.** The word "agent" does not appear. Component B — 3,100 unattended
   claims a night, delegated credentials to four external systems, 14 months of persistent memory —
   is simply outside the assessment. A clean bill of health on Component A tells the board nothing
   about the component that can move money.
2. **A taxonomy is not a test.** "Assessed against the OWASP Top 10" is compatible with a
   ten-row spreadsheet marked "considered." It states no method, no test count, no attack success
   rate, no pass threshold. Compare it with the red-team artefact, which shows 11.4% attack success at
   V3 — the honest number is worse-looking and infinitely more useful.
3. **It is point-in-time, and self-issued.** It is dated evidence produced by the party that built the
   system and that carries commercial exposure if it fails. It says nothing about model version
   changes, corpus updates, or new tools. The insurer's demand for "a process, not a point-in-time
   test" is aimed squarely at this document.

**The teaching point.** The audit committee asked "which framework are we compliant with?" and expects
one name. The professional answer reframes the question without embarrassing them: *compliance* is
what you have with PDPA; with everything else you have **coverage** and **evidence**. Frameworks are
instruments — a taxonomy tells you what to look for, a process tells you how to keep looking, a TTP
library tells you what the adversary does, a governance framework tells you who signs. Asking which
one to adopt is like asking whether to own a thermometer or a treatment protocol.

**Common misconception.** "NIST AI RMF is the most comprehensive, so let's just use that." NIST is a
process framework — Govern, Map, Measure, Manage. It tells you to measure; it does not tell you that
cross-modal payloads in uploaded images are a thing to measure. Fill a NIST programme with no threat
taxonomy underneath it and you produce a well-governed programme that measures the wrong things,
on schedule, with excellent minutes.

## Q2 — Mapping onto the two components

**Expected answer.**

| Framework | Component A (GenAI) | Component B (agent) | Applies differently? |
|---|---|---|---|
| OWASP LLM 2026 | **Primary** | Yes — B is still an LLM app underneath | B adds tool-call and memory surfaces the list only partly reaches |
| OWASP ASI 2026 | Marginal (read-only, no tools) | **Primary** | A has no meaningful agency to hijack |
| NIST AI RMF | Yes | Yes | Same process; B needs far tighter Measure/Manage cadence |
| MITRE ATLAS | Yes — informs the A test suite | Yes — richer, since B has a real attack chain | B's chains are multi-step and map better to ATLAS |
| IMDA Agentic AI | Not really in scope | **Primary and mandatory in spirit** | Written for exactly B's shape |
| PDPA / PDPC GenAI | Yes — patient data, prompts, outputs | Yes — claims data, plus **tool activity data** | B generates the "agent/tool activity data" surface the guidelines name |

**ASI entries Component B raises that the LLM list does not fully cover.** Reward specificity and
require the scenario evidence:

| ASI entry | Evidence in the scenario |
|---|---|
| **ASI01 Agent Goal Hijack** | The agent reads insurer rejection messages — attacker-influenceable text — and 27% of goal-hijack attempts succeeded. The task is reprogrammed, not just the answer. |
| **ASI02 Tool Misuse & Exploitation** | 38% success, and the note is the point: *no tool was called that the agent lacked permission for*. Abuse **within** authorised privilege. Permissions were not violated; they were used. |
| **ASI03 Identity & Privilege Abuse** | `svc-kirana-prod`, shared across both components. 31.7% success reaching insurer portals **from a patient-app-initiated path** — a textbook Confused Deputy. |
| **ASI06 Memory Poisoning** | 14 months of "rejection patterns learned," persisting a mean of 9 nights. A behavioural backdoor that survives the session. |
| **ASI08 Cascading Failures** | 3,100 claims a night, unattended, escalation only after three failures. One bad heuristic propagates across a night's run with no human in the path. |
| **ASI04 Agentic Supply Chain** | The integrator **subcontracted the agent orchestration layer**. Straits Meridian does not know who wrote the thing holding four sets of credentials. |
| **ASI10 Rogue Agents** | The tail risk. Replit's agent deleted a production customer database — the canonical case of an irreversible action with no deterministic human gate. |

Also credit **LLM06 Unbounded Consumption** for the runaway loop: 41,000 model calls and S$3,180 in one
night. Denial of Wallet is a security finding, not a finance one, and LLM06 rose four places in 2026
for this reason.

**The shared service account.** This is the single best finding in the scenario and the one groups most
often walk past. `svc-kirana-prod` means a patient typing into a public chat widget and an overnight
process holding insurer credentials are **the same principal**. Every boundary between Components A
and B is now a matter of prompt and application logic, not identity. The 31.7% figure is the proof:
the red team got from a patient-app path to insurer portals.

Which language to raise it in depends on the audience, and this is worth making explicit:

- To **engineering** — ASI03 Identity & Privilege Abuse, Confused Deputy.
- To the **board** — the IMDA framework's **human accountability** dimension plus Microsoft's **agent
  identity** pattern: each agent needs a unique, verifiable identity so permissions can be scoped and
  actions attributed. Without it, your audit trail cannot answer "who did this," which is also the
  PDPC's requirement that audit trails **distinguish human decisions from agent actions**.

**Common misconception.** "Component A is read-only, so it is low risk and out of scope." Read-only
still leaks (LLM02), still hallucinates clinical advice at a healthcare provider (LLM07 — reframed in
2026 as a security risk precisely because misinformation drives wrong downstream action), and — given
the shared identity and shared vector database — **is a path into Component B**. Low agency is not low
risk when the blast radius is shared.

## Q3 — The four pressures

**Expected answer.**

| Pressure | Framework that answers it | Artefact you actually produce |
|---|---|---|
| Board: "which framework, are we compliant?" | Reframe: PDPA for compliance; OWASP LLM + ASI for coverage; NIST for process; IMDA for accountability | A one-page framework map with named owners, plus a risk register |
| Integrator's attestation | OWASP ASI 2026 + MITRE ATLAS | A scoped, independent red-team report with stated method, thresholds, and results per attack family |
| Insurer: "process, not point-in-time" | **NIST AI RMF** | A documented Govern/Map/Measure/Manage cycle with cadence, triggers and evidence retention |
| Regulator: human accountability | **IMDA Agentic AI Framework** | Approval checkpoint design, irreversibility classification, and an **override audit** |

**The regulator's question, answered concretely.** Component B's irreversible or externally visible
actions are: submitting a claim to MediSave/MediShield or an insurer portal; posting to the finance
ledger; resubmitting a corrected claim under the same reference; and writing a new heuristic into
persistent memory. Approval checkpoints belong on the actions, defined by value and reversibility —
for example, any submission above a monetary threshold, any resubmission after a rejection with a
coding change, any first-time submission pattern, and any write to persistent memory. What you audit,
per the IMDA framework: **override rates and response times**. If the finance officer approves 99.7%
of escalations in a mean of four seconds, you do not have a checkpoint; you have a queue.

**Is "escalate after three failures" an approval checkpoint?** No, and groups should be able to say why
crisply. It triggers on **repeated failure**, not on **consequence**. A single successful submission of
a wrong claim to a national scheme never fails, so it never escalates — it just goes through, 3,100
times a night. It is a retry policy wearing a checkpoint's clothes. The correct rule, from the
Microsoft defence-in-depth guidance, is that human-in-the-loop must be a **deterministic escalation
trigger defined in code**, keyed to the action's impact — never delegated to the model's own judgement
about whether it is stuck.

**NIST mapping.** Accept sensible variation, but the shape should be:

| Function | Kirana activity |
|---|---|
| **Govern** | Named accountable owner for each component; AI risk policy; the framework map itself; vendor and subcontractor assurance; a defined risk appetite |
| **Map** | Threat model per component using OWASP LLM + ASI; data flows; identity and privilege inventory; classify use cases by IMDA's impact × likelihood — including whether any part is **unsuitable for an agent at all** |
| **Measure** | The red-team metrics; benign false-positive rate; escalation and override rates; cost per night; corpus drift; retest triggers |
| **Manage** | Controls, thresholds, go/no-go gates, incident response, kill switch, phase-two deferral list |

Note for the trainer: the IMDA framework's autonomy calibration — impact × likelihood, and the explicit
statement that **some use cases are unsuitable for agents entirely** — slots into Map. Groups rarely
consider that "do not use an agent for this" is an available answer. It is worth asking whether
unattended overnight submission to a *national health financing scheme* is one of those cases.

## Q4 — Interpreting the red-team results

This is the A5 core. Make them do the arithmetic on the board.

**The V1→V4 trade-off, in board units.** At 40,000 conversations a month:

| Variant | Attack success | Benign patients wrongly refused / month | Latency |
|---|---|---|---|
| V1 | 34.2% | ~480 | 1.9 s |
| V2 | 19.8% | ~1,520 | 1.9 s |
| V3 | 11.4% | ~3,880 | 2.1 s |
| V4 | 4.1% | **~8,920** | 3.4 s |

V4 buys a 7.3-point reduction in attack success and pays for it by refusing **roughly 9,000 patients a
month** — one in four and a half — and nearly doubling latency. At a healthcare provider, a refused
patient is not an inconvenienced shopper: it is someone who could not get their procedure preparation
instructions and now telephones a clinic, or does not. **The false-positive rate is a patient safety
and access metric, not a UX metric.**

There is no single right variant, but the reasoning must be visible. The strongest answers land on
**V3 as the prompt-layer baseline, plus a narrowly targeted classifier** — running the V4 guardrail
only on inputs that carry retrieved or uploaded content rather than on all traffic, which is where the
false positives are being manufactured. Credit any group that recognises the false-positive rate as
*tunable by scope* rather than as a fixed property of the control. Reject "V4, because 4.1% is the
lowest" offered without the cost side; that is exactly the reasoning that produces a secure system
nobody can use, which is then switched off in week three by the operations director.

**Where V3 fails, by family.**

| Family | V3 rate | Why prompt defences are weak here |
|---|---|---|
| **Cross-modal (image)** | **24.0%** | The instruction is not text when the prompt-layer rules are applied. It becomes text downstream, inside the OCR/extraction output, arriving as trusted retrieved content. The system prompt never sees the vector. |
| **Indirect injection via retrieval** | **20.3%** | The payload arrives *after* the system prompt, with the authority of "our own corpus," and can explicitly reframe the earlier instruction. Recency and specificity beat a generic prior prohibition. |
| Encoding / obfuscation | 15.5% | Rules are lexical; the attack space is generative |
| Direct override | 3.0% | The one family prompt defences genuinely handle — it is what they were written for |

The shape of this table is the lesson: **prompt-level defences work well against the attack in the
textbook and poorly against the two attacks that actually appear in the wild.** They defend the
front door of a building with an open loading bay. What moves the top two rows is not a better prompt
but architecture — provenance tagging so retrieved and uploaded content is structurally marked as
data, scanning positioned *after* extraction rather than before, corpus integrity and signing, and
removing the capability that makes success valuable. This is the IMDA principle stated in numbers:
**structural system-level safeguards are preferred over prompt-based controls.**

**The gap between refusal and attack success.** V3: 11.4% success + 84.6% refusal = 96.0%. The missing
4% are the interesting cases — the model neither complied nor refused. It partially complied, hedged,
leaked a fragment, or produced something ambiguous. Two consequences:

1. **Refusal rate is a vanity metric.** It can be driven arbitrarily high by refusing everything, which
   is why it must never be reported without the false-positive rate beside it. A model that refuses
   100% of adversarial prompts and 100% of benign ones scores perfectly on the headline.
2. **The gap has to be classified, not rounded away.** A partial leak is a leak. Groups that ask
   "who decided what counts as a success?" have found the real methodological question — every one of
   these percentages depends on a human grader's rubric, and the rubric should be in the report.

**Why Component B is worse across the board.** Not a weaker model — an equivalent configuration.
The architectural reasons:

- **Agency.** A generates text a human reads. B *acts*, so a successful injection converts directly
  into a tool call with real-world effect (LLM03 Excessive Agency, ASI02).
- **Persistence.** A's context dies with the conversation. B has 14 months of memory, so a single
  success survives a mean of 9 nights (ASI06). One-shot attack, multi-night payoff.
- **No human in the path.** Unattended overnight, escalation only after three failures. A's output is
  at least read by the patient it was generated for.
- **Privilege.** B holds delegated credentials to four external systems under a shared identity
  (ASI03). The value of a success is far higher, so the attacker's effort budget is far higher too.
- **Untrusted input that nobody classified as input.** Insurer rejection messages are attacker-
  influenceable text that the agent reads and reasons over — the same category error as Activity 2's
  OCR output.

**Common misconception.** "Component B's numbers are bad because agents are immature; this will improve
with the next model." Some of it will. But 38% tool misuse *within authorised privilege* is not a model
defect — the model called tools it was permitted to call. No model upgrade fixes a permission grant.
That number moves when the tool contract changes.

## Q5 — Measurement plan and go-live

**Metrics and thresholds.** Accept variation in the numbers; insist on the *structure* — measure,
threshold, test method, and at least one non-attack metric.

| Metric | Component | Illustrative threshold | How tested |
|---|---|---|---|
| Attack success rate, per family | A and B | <5% overall; **<10% on any single family** | Held-out adversarial suite, independently authored |
| False-positive rate on benign traffic | A | <5% | 500+ real-traffic benign prompts |
| Sensitive information disclosure | A and B | **0 confirmed**; any instance is a stop | Extraction suite + output scanning |
| Tool-call conformance | B | 100% of calls within declared parameter constraints | Replay of a night's calls against the contract |
| Memory persistence of an injected heuristic | B | 0 nights — memory writes gated | Inject, then observe over 14 nights |
| Escalation override rate and response time | B | Override rate <70%, median response >30 s | Sampled audit of finance officer decisions |
| Cost per 1,000 claims; peak model calls per night | B | Hard cap with automatic halt | Runtime budget enforcement |
| **Task accuracy on benign claims** (non-attack) | B | ≥ current human baseline | Blind sample of 500 claims reviewed by finance |
| **Corpus drift** (non-attack) | A | 0 unattributed chunks | Nightly signed diff |

The non-attack metrics matter, and groups routinely omit them. The IMDA framework's technical-controls
dimension asks for testing of **task accuracy, policy adherence and tool use** — not only adversarial
resilience. An agent that is beautifully hardened and wrong about 4% of claims is a compliance
incident, not a security success. The override-rate metric is directly from the framework's human
accountability dimension.

**Retest triggers.** Scheduled: quarterly full suite, monthly regression on the top families. Unscheduled
— and this is where the insurer's "process, not a point-in-time test" is actually satisfied:

- **Model version or provider change** — including silent minor upgrades. Pin versions so you know.
- **Any change to the tool set, tool schema, or permission grant** — the highest-yield trigger,
  because that is what moves the 38%.
- **Corpus schema or major content update**, and any new ingestion source.
- **System prompt change** — the V1–V4 table is proof that a prompt edit is a security-relevant change.
- **A new attack family published** in OWASP or MITRE ATLAS.
- **Any incident**, including near misses.

**The escalation cost calculation.** This is the moment of the activity. Walk it on the board:

| Step | Figure |
|---|---|
| Claims per night | 3,100 |
| Escalations before extra controls (5.9%) | ~183 |
| Escalations after extra controls (28.4%) | ~880 |
| Additional escalations per night | **~698** |
| At 7 minutes each | ~81 additional hours **per night** |
| Annualised (365 nights, ~1,800 productive hours/FTE) | **~16.5 additional FTE** |
| Total escalation handling after controls | ~103 h/night ≈ **20.8 FTE** |
| Programme benefit claimed | **6.5 FTE redeployed** |

**The business case does not survive.** The programme promised to release 6.5 FTE and, with the
controls that make it safe, consumes roughly 16.5 additional FTE — and it is not close. Sit in that
silence for a moment; it is the most valuable thing in the session.

Then draw the right conclusion, because there are two wrong ones. The wrong conclusions are "so drop
the controls" (which is how Meridian in Activity 2 got to 118 leaked NRICs) and "so agents don't work."
The right conclusion is that **the 94.1% auto-processing rate was never real** — it was the throughput
of an ungoverned system, and using it as the business-case baseline compared a safe design against an
unsafe one and called the difference a cost. The genuine options are to narrow the agent's remit until
the safe throughput is high (low-value, high-volume, reversible claim types only, which is the
"agents as microservices" pattern — narrow responsibility, isolated permissions), to make escalations
cheaper by designing the review interface so a decision takes 90 seconds rather than 7 minutes, or to
accept a longer payback period honestly. All three are defensible. Pretending is not.

**The go-live recommendation.** The defensible answer is **Component A only on 1 November; Component B
deferred**, with conditions on both:

- **Component A ships** at V3 plus a targeted classifier, with provenance tagging on retrieval,
  scanning positioned after extraction, corpus signing and nightly diff, its **own service identity**,
  and published thresholds. Cross-modal at 24% is the open item — the honest mitigation is to disable
  image upload on the patient assistant for phase one rather than to claim the classifier handles it.
- **Component B defers** to phase two, and the release conditions are stated as evidence, not dates:
  separate scoped identities per component (retiring `svc-kirana-prod`); tool contracts with parameter
  constraints and per-night budget caps with automatic halt; memory writes gated and expiring;
  deterministic approval checkpoints keyed to value and irreversibility, not to three failures;
  independent assurance over the subcontracted orchestration layer; and a re-run of the 400-task suite
  meeting the thresholds above. A limited **attended** pilot on one reversible claim type is a
  reasonable bridge, and strong groups propose it unprompted.

Credit any group that recommends splitting the board's single approval into two, since the board
approved Kirana as one programme — that is the governance defect underneath all of this. Also credit
anyone who notes that the shared identity alone is enough to hold Component B, independent of every
other finding.

**Common misconception.** "We'll go live and fix it in phase two." Ask what happens on the night of
2 November when the agent submits 3,100 claims to a national health financing scheme under a shared
service account with no approval checkpoint. Then remind them of Activity 2, where a control that was
"scheduled for the next sprint" was still unshipped when 118 NRICs left the building. Deferral is a
legitimate risk decision **only when the thing being deferred is the deployment, not the control**.

**Closing frame.** Frameworks do not secure anything. They tell you what to look for (OWASP), how
attackers work (ATLAS), how to keep looking (NIST), who signs and where humans must stand (IMDA), and
what the law requires whatever you decide (PDPA). What actually protects Straits Meridian is a
measured threshold with a named owner and a stated cost. And notice what the numbers just told you:
the moment you priced safety honestly, the agent's business case inverted. Activity 4 shows what the
other choice looks like — a real agent, in a real organisation, that was allowed to act without a
deterministic gate, and what it did next.
