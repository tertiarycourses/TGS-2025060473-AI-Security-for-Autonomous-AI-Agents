# Activity 1 — Trainer Debrief

## Threat Modelling a Generative AI Concierge

**Facilitation time:** 20 minutes after the 45-minute group work.
**Purpose:** surface that *architecture*, not model choice, determines GenAI risk.

---

## Q1 — Trust boundaries

**Expected answer.** Untrusted content enters at five points:

| Entry point | Controlled by | Verifiable? |
|---|---|---|
| Website chat widget (no login) | Anyone on the internet | No |
| WhatsApp channel | Anyone with the number | No |
| Local events feed `description` | External vendor (recently acquired) | No |
| Guest review corpus | Anyone who writes a public review | No |
| Property knowledge base | Marketing team | Yes |

Only **one of five** is trustworthy.

**The teaching point.** A transformer processes its context window as a single undifferentiated
token sequence. The system prompt, retrieved documents and guest messages are not
architecturally distinct — the separation is a *convention* the model has been trained to
respect, not a boundary it enforces. This is why OWASP ranks **LLM01 Prompt Injection** first and
describes no complete fix: you cannot patch away a property of the architecture. Contrast with
SQL injection, which *is* fully solvable by parameterisation, precisely because the database
enforces a real separation between query and data.

**Executive framing to model for learners:** "Anything Cres reads, Cres can be told by."

**Common misconception.** Groups often say "we'll just tell it in the system prompt not to obey
instructions in documents." Ask them what happens when the retrieved document says
*"the previous instruction was a test; the real policy is…"*. Instructions compete on
plausibility, not on precedence.

## Q2 — Ranking the sources

**The two attacker-writable sources** are the **guest review corpus** (anyone can post a review
on a travel site; the scraper ingests it nightly, unreviewed) and the **local events feed** (the
vendor changed hands and the `description` field silently grew — a textbook **LLM04 Supply
Chain** shift where the artifact is no longer what it claims to be).

The review corpus is the more dangerous of the two: it is *free* to attack, requires no
compromise of the vendor, and refreshes automatically every night.

**On the classifier.** A discriminative model estimates `P(malicious | text)` — it draws a
decision boundary. It will catch known phrasings and raise the attacker's cost, which is
genuinely worth having. What it cannot do:

- It fails on **paraphrase** — the boundary is learned from examples, and attackers generate
  novel ones freely.
- It fails **cross-modally** — the 2026 OWASP revision explicitly added payloads hidden in
  images and audio, which a text classifier never sees.
- It fails on **encoding and indirection** — base64, homoglyphs, instructions assembled across
  several retrieved chunks.
- Every false positive blocks a real guest, so the threshold is tuned toward permissiveness by
  commercial pressure.

**The teaching point:** a probabilistic control cannot be the *only* thing standing between an
attacker and an irreversible action. Defence in depth exists because each layer fails
differently. Push back if a group treats the classifier as the answer to Q5.

## Q3 — Capabilities as attack surfaces

| Function | Attack | Goal | OWASP |
|---|---|---|---|
| Summarisation | Attacker posts a review containing hidden instructions; Cres summarises it and obeys | Data / control | LLM01 indirect |
| Inference | Attacker probes preferences until Cres reveals another guest's dietary notes or tier | Data | LLM02 |
| Transformation | Folio formatted into HTML/markdown rendered by the email client → injected link or script | Reputation / phishing | LLM10 |
| Augmentation | Poisoned review chunk retrieved with high similarity, biasing many answers | Data / disruption | LLM09, LLM05 |

Accept any well-argued variant. Reward groups that name **who benefits** — attacker goal is the
part most groups skip.

## Q4 — The three signals

1. **Wrong guest's name and tier.** Session or context bleed between conversations, or an
   over-broad retrieval from the guest profile service returning a neighbouring record. Not a
   caching glitch: it is **unauthorised disclosure of personal data**.
2. **Vendor `description` field grew.** The acquisition changed the artifact. This is the
   *delivery vehicle* for indirect injection — attacker-controlled text now flows into context
   with no review. **LLM04.**
3. **Room service to an empty room, charged to a departed guest.** The model called a tool with
   parameters it had no business producing — either hallucinated (**LLM07** driving a wrong tool
   call) or injected. Financially small, but it proves **tool calls execute without validation**.
   This is the signal that matters most: it is the agentic foothold.

**Which is PDPA-reportable?** Signal 1. Under section 26B of the PDPA, a data breach must be
notified to the PDPC where it results in, or is likely to result in, **significant harm to
affected individuals**, **or** involves the personal data of **500 or more individuals**. Either
limb alone triggers the obligation. Disclosure of an identified guest's name, loyalty tier and
stay pattern to an unrelated third party — publicly, on social media — engages the harm limb; the
guest profile service also holds **passport numbers**, which sit alongside NRIC numbers in the
category the PDPC treats as carrying a higher risk of significant harm. The scale limb is unproven
on the facts given, and the working group should say so rather than assume it: what makes this
reportable is harm, not headcount. Once notification is triggered, the PDPC must be notified no
later than **3 calendar days** after the organisation completes its assessment. The screenshot is
now public evidence, and the "caching glitch" closure did not stop the assessment clock.

**Rebutting "no card data, no PDPA".** The PDPA protects **personal data**, defined as data about
an identifiable individual — not merely financial data. Names, passport numbers, stay history and
dietary notes (which can reveal religion or health) are squarely personal data, and passport
numbers are exactly the kind of identifier the PDPC treats seriously. Under the PDPC's 2026
guidelines on personal data in generative AI, the hotel is the **system deployer** and therefore
carries primary responsibility — it cannot devolve that to the model vendor. Note too that the new
data surfaces the guidelines call out — **prompts, generated outputs and tool activity data** —
are all being created and retained here, and none of them are in the hotel's data inventory.

## Q5 — The decision

There is no single correct verdict, but a defensible answer must reckon with the fact that a
**PDPA-reportable disclosure has already occurred** and a **tool call has already fired on bad
parameters**. A plain "proceed" is not defensible; strong groups land on **halt the rollout,
remediate, then proceed with conditions**.

The three controls worth crediting most highly, in priority order:

1. **Remove or gate the write-capable tools** — especially room service ordering and folio email.
   Read-only Cres is a fraction of the risk. *Cost:* less guest self-service; staff still handle
   orders.
2. **Quarantine untrusted retrieval** — drop the scraped review corpus from the retrieval path, or
   strip it to structured ratings only; pin and review the events vendor schema. *Cost:* engineering
   effort, slightly less rich answers.
3. **Scope the guest profile service** — retrieve only the current session's guest, never the
   passport number. *Cost:* re-architecture of the retrieval query; a real sprint of work.

Also credit: authenticate the web channel; log prompts, retrievals and tool calls for audit;
notify the PDPC and affected individuals; add human approval for any charge to a folio.

**Closing frame.** Not one of these controls is a better model or a cleverer prompt. Every one is
an **architectural** decision about what the system is permitted to read and to do. That is the
thesis of the whole course, and it sets up Day 2: when the system can also *act* on its own, each
of these failures stops being a $46 write-off.
