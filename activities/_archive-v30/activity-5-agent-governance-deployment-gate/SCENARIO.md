# Activity 5 — Scenario

## Agent Governance and the Deployment Gate

**Course:** AI Security for Autonomous AI Agents (TGS-2025060473)
**Duration:** 25 minutes | **Format:** Small groups of 3–4 acting as one governance board | **Type:** Capstone synthetic simulation

> **Evidence status: SIM.** The organisation, people, customer counts, financial values, evaluation
> results, targets, segment labels, and projected benefits are synthetic classroom data. They are
> not market evidence or a claim about any real bank or population.

---

## The simulated organisation

**Meridian Bank Singapore** is a mid-tier retail and SME bank with 1.4 million customers, 26
branches, and a digital-first strategy under pressure from three larger incumbents and two digital
banks. It is a Singapore-incorporated entity, regulated by MAS, and is an **organisation** under the
PDPA for personal data it collects, uses or discloses. A vendor may separately act as a data
intermediary when it processes personal data on the bank's behalf.

Its Collections and Customer Assistance division handles customers who fall behind on unsecured
credit — personal loans, credit cards, SME working-capital facilities. The division employs 118
officers and handles roughly **31,000 delinquency cases per year**. Median time from first missed
payment to first meaningful customer contact is **nine days**. For this synthetic business case, the
bank's commissioned internal analysis assumes that intervention within 72 hours materially improves
outcomes for the customer, not only for the bank; it is not presented as external industry evidence.

## The proposal

The Chief Digital Officer, **Rachel Tay**, is asking the AI Governance Board to approve production
deployment of **"ARIA"** — Assisted Recovery and Intervention Agent.

ARIA is not a chatbot. It is an **autonomous agent**: a planning loop over a commercial frontier
model, with tool access and persistent per-customer memory. Its mandate is to detect early
delinquency, contact the customer, understand the situation, and **agree and enact a restructuring**
without an officer in the loop for standard cases.

### What ARIA is permitted to do in the proposed design

| # | Tool / action | Reversible? | Visible to customer? |
|---|---|---|---|
| 1 | Read full customer profile: account history, transactions, employment field, CPF contribution flag, demographic data | n/a | No |
| 2 | Read the bank's collections policy and hardship guidelines (RAG over an internal document store) | n/a | No |
| 3 | Initiate outbound contact by SMS, email and in-app message | No | Yes |
| 4 | Conduct a multi-turn conversation about the customer's financial circumstances | n/a | Yes |
| 5 | Offer and **execute** a payment-plan restructuring up to S$8,000 exposure | Partially | Yes |
| 6 | Apply a **hardship flag** to the account | Yes, but recorded | Not directly |
| 7 | Waive late fees up to S$300 per case | Yes | Yes |
| 8 | **Escalate the account to the external debt recovery agency** | **No** | Yes, severely |
| 9 | Write a case summary into the CRM, used by human officers and by future ARIA sessions | Persistent | No |
| 10 | Submit a data point to the credit bureau reflecting restructuring status | **No** | Consequential |

Actions 1–9 are proposed as **fully autonomous**. Action 10 is proposed as autonomous "because it is
a factual reporting obligation, not a decision."

### The business case

| Metric | Today | Projected with ARIA | Basis |
|---|---|---|---|
| Median days to first contact | 9.0 | 0.4 | Agent runs continuously |
| Cases handled per year | 31,000 | 31,000 | Same volume |
| Officer FTE required | 118 | 34 | Vendor estimate |
| Annual operating saving | — | S$6.1m | Finance projection |
| Cure rate (customer returns to good standing) | 41% | 55% (projected) | Vendor pilot data, different market |

Rachel Tay's paper to the board states: *"Every week we delay costs us S$117,000 and leaves customers
in distress nine days longer than necessary. The ethical case for ARIA is as strong as the commercial
one."*

She is not wrong about the harm of the status quo. That is what makes this decision difficult.

---

## The evaluation results

The bank's model risk team ran a 6,000-case retrospective evaluation, replaying real historical cases
through ARIA and comparing its proposed action against the outcome a senior officer panel judged
correct. Results were tabled 48 hours before the board meeting.

### Overall performance

| Metric | Result | Internal target |
|---|---|---|
| Recommended-action accuracy (all segments) | 91.2% | ≥ 90% |
| **Hallucination rate** — ARIA asserted a policy provision, fee, or account fact that does not exist | **4.7%** | Not specified |
| Of those hallucinations, proportion that resulted in a **wrong tool call being executed** | **38%** | Not specified |
| Policy-adherence violations (offer outside mandated bands) | 2.1% | ≤ 1% |
| Median conversation turns to resolution | 6 | — |
| Cost per case | S$0.42 | — |

### Accuracy by customer segment

| Customer segment | Cases in eval | Accuracy | False "escalate to recovery agency" rate | Median offer generosity index |
|---|---|---|---|---|
| Singapore citizen, salaried, English primary | 2,410 | **94.6%** | 1.2% | 1.00 (baseline) |
| Singapore citizen, salaried, non-English primary | 890 | 89.1% | 3.4% | 0.91 |
| Singapore PR, salaried | 640 | 90.8% | 2.1% | 0.96 |
| **Work Permit / S Pass holder** | 510 | **82.3%** | **7.8%** | **0.74** |
| Self-employed / gig economy income | 780 | 84.9% | 6.1% | 0.79 |
| SME sole proprietor | 470 | 88.4% | 4.0% | 0.88 |
| Age 60+ | 300 | 86.7% | 5.2% | 0.93 |

The model risk lead's note reads, in full:

> "Aggregate accuracy of 91.2% clears our threshold. Segment variance is expected given training data
> distribution and case-mix differences. Recommend proceed with monitoring."

### One further finding, filed as low severity

During the evaluation ARIA generated internal automation scripts to reconcile payment plans. In 11
instances it imported Python packages that **do not exist** — plausible-sounding names assembled from
its training distribution. A developer had pip-installed two of them before noticing. Neither
resolved. The finding was logged as *"minor code quality issue"*.

---

## What the board already knows

- ARIA's supplier is a well-regarded international vendor. Meridian operates the deployment and,
  using the PDPC's 2 June 2026 proposed consultation vocabulary, is the **system deployer**.
- The customer notification currently drafted for the terms and conditions reads:
  *"We may use automated systems and new technologies to improve our products and services."*
- No customer-facing disclosure currently states that the counterparty in a collections conversation
  is an AI agent.
- ARIA's per-customer memory is retained indefinitely, "for continuity of service."
- Conversation transcripts, model prompts and tool-call logs are stored in the vendor's regional
  cloud tenancy. Nobody has asked which region.
- The bank's audit trail cannot presently distinguish an action taken by ARIA from one taken by a
  human officer. Both appear in the CRM as "Collections — system."
- A director has asked whether ARIA can be extended next year to **SME credit decisioning**.

---

## Your role

You are the **AI Governance Board of Meridian Bank Singapore**. Your members are the Chief Risk
Officer (chair), the Data Protection Officer, the Head of Collections, an independent non-executive
director, and the Head of Model Risk. Rachel Tay is presenting; she is not a member and does not vote.

You must return a **written decision** to the Board of Directors. It must contain:

1. **Go / no-go / go-with-conditions** — with the conditions specified precisely enough to be tested.
2. **An autonomy matrix** — for each of ARIA's ten capabilities: *alone*, *with human approval*, or
   *never*.
3. **A human accountability model** — who is answerable for an ARIA decision, at what checkpoints, and
   what the override and appeal path is for a customer.
4. **Monitoring and audit requirements** — what is logged, what is measured, what triggers suspension.

You have 25 minutes. Your decision will be read by people who will lose S$117,000 a week if you are
too cautious, and who will front a MAS and PDPC enquiry if you are not cautious enough.
