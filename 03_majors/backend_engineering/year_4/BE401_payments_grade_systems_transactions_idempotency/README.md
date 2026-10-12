# BE401 · Payments-Grade Systems: Transactions, Idempotency and Reconciliation

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 7 | 4 (≈ 120 hours) | L3 → L4 | [BE301](../../year_3/BE301_api_design_rest_grpc_and_graphql/README.md) (also uses [BE303](../../year_3/BE303_data_modeling_and_storage_for_backends_postgres/README.md), [BE304](../../year_3/BE304_asynchronous_systems_queues_streams_and_event/README.md), [BE305](../../year_3/BE305_authentication_authorization_and_backend/README.md)) | [BE501](../../year_5/BE501_frontier_seminar_durable_execution_serverless/README.md), [OV10A](../../../../04_overlaps/OV10_fintech_systems_engineering/OV10A_payment_systems_engineering_upi_cards/README.md), [OV10B](../../../../04_overlaps/OV10_fintech_systems_engineering/OV10B_fraud_detection_and_risk_systems/README.md) |

Part of the [Backend Engineering major](../../README.md). This is the course where "correct under failure" stops being a slogan. Every lab is graded on invariants such as "no money created or destroyed", not on whether the happy path works.

## Why this course matters now

India runs the world's most visible real-time payment system. In September 2026, UPI processed 24.07 billion transactions worth ₹29.37 lakh crore, an average of about 802 million a day. At that scale, small design mistakes become national news. On 12 April 2025, UPI was disrupted for hours. NPCI attributed it to some banks flooding the switch with "check transaction status" requests, including for old transactions. NPCI responded with hard rules: the first status check only 90 seconds after a transaction, at most three checks within two hours, and API response times cut from 30 s to 10–15 s from 16 June 2025. Elsewhere, Stripe's ledger processes about five billion events a day and verifies 99.99% of dollar volume within four days. The two worst-known failures in finance technology were both engineering-process failures:
- Knight Capital lost more than $460 million in 45 minutes in 2012 after a bad deployment.
- UK regulators fined TSB £48.65 million in 2022 over a 2018 IT migration that left customers unable to bank for months.

AI assistants write payment integrations fluently. They do not know what to do when a bank call times out with an unknown outcome, and that question is the whole job.

## Learning outcomes

By the end you can:

1. **Represent** money correctly (integer minor units, currency exponents, rounding rules, business dates and cut-offs) and **explain** every bug that floating-point money causes.
2. **Design** a double-entry ledger with immutable entries, holds, pending and posted states, and corrections by reversal, and **prove** its invariants with property-based tests.
3. **Model** payments, refunds, payouts and disputes as explicit state machines in which "unknown" is a first-class state.
4. **Implement** idempotency at every boundary (client API, internal steps, provider calls, callbacks), and **explain** why "exactly once" across organizations is an illusion built from at-least-once delivery plus idempotency.
5. **Handle** timeouts with status checks, backoff and reversal rules that respect real network rules (NPCI's status-check limits, RBI's turnaround-time and compensation rules).
6. **Explain** the UPI flow (payer app and PSP, NPCI switch, remitter and beneficiary banks) and card flows (issuer, acquirer, network; authorization, capture, clearing, settlement, chargebacks).
7. **Build** reconciliation that matches your ledger against provider and bank settlement data, classifies breaks and ages them.
8. **Apply** correctness engineering (invariants, deterministic simulation, chaos tests, shadow ledgers) and **run** payment operations with audit trails, maker-checker controls and PCI DSS scope reduction.
9. **Review** AI-generated payment code for blind retries, float money, missing idempotency and states that cannot be recovered.

## Chapters and lessons

### Chapter 1 · Money as data (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Amounts | Integer minor units (paise, cents), ISO 4217 exponents (0, 2, 3 decimals), why never `float`, `numeric` in Postgres | Find six float-money bugs in a provided codebase and write a failing test for each |
| 1.2 Rounding and allocation | Banker's rounding, splitting ₹100 three ways, fees and taxes (GST) on fractional amounts, allocation remainders | Implement a split that never loses or invents a paisa, and property-test it |
| 1.3 Time in finance | Business dates vs timestamps, IST cut-offs, settlement cycles, holidays, idempotent end-of-day jobs | Assign 1,000 transactions around midnight to the right business date |
| 1.4 Currencies and FX | Rates with timestamps and sources, conversion at capture vs settlement, unrealized gains as accounting entries | Book a USD charge settled in INR, including the FX difference |

**Check your understanding:** (1) Why does `0.1 + 0.2 != 0.3` matter for a ledger that sums millions of rows? (2) Where should a rounding remainder go when you split a fee among merchants? (3) Why is "today" an unsafe concept in a payments system?

### Chapter 2 · Double-entry ledgers (weeks 2–3)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Accounts and entries | Debit-normal and credit-normal accounts, journal entries that sum to zero, chart of accounts for a marketplace | Design a chart of accounts for a food-delivery marketplace (customers, merchants, riders, fees, taxes, bank) |
| 2.2 Immutability | Append-only entries, balances derived or cached with verification, corrections by reversal, never `UPDATE` history | Implement a reversal and show the audit trail of an incorrect charge |
| 2.3 Pending, holds and available balance | Authorization holds, pending vs posted, available vs ledger balance, hold expiry | Model a card authorization that is partially captured and then released |
| 2.4 Clearing accounts | Money in transit, suspense accounts, clearing accounts that should net to zero (Stripe's ledger approach) | Find a stuck payment from a non-zero clearing account |
| 2.5 Ledger storage | Postgres designs, contention on hot accounts, batching, TigerBeetle's dedicated design, PhonePe's TStore | Measure throughput on a single hot merchant account; apply two mitigations |

**Check your understanding:** (1) Why is "sum of all entries = 0" a stronger check than "balances look right"? (2) What does a non-zero clearing account at end of day tell you? (3) Why do hot accounts limit ledger throughput, and what are the trade-offs of sharding a single merchant's balance?

### Chapter 3 · Payment state machines (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 States and transitions | Created, authorized, captured, settled, refunded, failed, disputed; terminal and non-terminal states | Draw the state machine of a card payment and a UPI payment |
| 3.2 The unknown state | Timeouts produce "we don't know"; pending as a state with deadlines, not an error | Add `PENDING_UNKNOWN` with a resolution path to every transition |
| 3.3 Enforcing transitions | Database constraints, conditional updates, version checks, event logs of transitions | Make illegal transitions impossible at the database level |
| 3.4 Refunds, payouts and disputes | Partial refunds, refund-after-settlement, payout failures and returns, chargeback lifecycle and evidence | Model a partial refund racing a chargeback |

**Check your understanding:** (1) Why must a timed-out payment never be marked "failed" immediately? (2) Which transitions must be idempotent, and which must be strictly once? (3) How do refunds interact with settlement that has already happened?

### Chapter 4 · Idempotency end to end (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 At the API edge | Idempotency keys, fingerprints, stored responses (BE301); Stripe's and Razorpay's semantics | Reuse your BE301 idempotency layer on a payments API |
| 4.2 Inside the system | Deterministic step IDs, idempotent handlers, the pre-call / call / post-call split (Airbnb's Orpheus, 2019) | Split a payment into idempotent steps and crash between each |
| 4.3 Towards providers | Provider idempotency support, using your own reference IDs, what to do when the provider has none | Wrap a non-idempotent provider so retries are safe |
| 4.4 Callbacks and webhooks | Deduplicating provider callbacks, out-of-order notifications, trusting status checks over callbacks | Process shuffled, duplicated callbacks and still reach the right state |

**Check your understanding:** (1) What should the system do if a retry arrives with the same key while the first attempt is still talking to the bank? (2) Why should the provider reference ID be generated before the call? (3) When do you trust a webhook, and when do you confirm with a status check?

### Chapter 5 · Distributed transactions and the exactly-once illusion (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Why no global transaction | Organizations don't share a transaction manager; 2PC's blocking; Pat Helland's *Life beyond Distributed Transactions* (2007): entities, activities, idempotence | Explain a bank transfer's consistency model in Helland's terms |
| 5.2 Sagas for money | Debit, credit, compensate; pivot steps; which steps can never be undone | Write the saga for a wallet-to-bank payout with compensations |
| 5.3 Outbox for money events | Ledger write and event in one transaction (BE304); consumers that move money must be idempotent | Prove zero lost or duplicated payout instructions under crashes |
| 5.4 Exactly-once effects | At-least-once delivery + idempotent effect + reconciliation as the safety net | Show where each of the three would catch a different failure |

**Check your understanding:** (1) Why is reconciliation part of the correctness design and not just an accounting task? (2) Which step of a payout is the pivot, and why? (3) What is the difference between exactly-once delivery and exactly-once effect?

### Chapter 6 · Timeouts, retries and status checks (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Never retry a debit blindly | Retry only idempotent operations; resolve unknowns with status checks; backoff with jitter; retry budgets | Show a double debit caused by a naive retry, then fix it |
| 6.2 Status-check discipline | NPCI's 2025 rules: first check after 90 s, at most three within two hours; why uncontrolled checks can take down a switch (April 2025) | Implement a rule-compliant status checker and load-test it |
| 6.3 Response-time budgets | NPCI's cuts from 16 June 2025 (request/response pay 30 s → 15 s; status check and reversal 30 s → 10 s); timeout budgets across PSP, switch and banks | Build a timeout budget for a UPI-style call chain |
| 6.4 Reversals and turnaround times | RBI's 2019 TAT circular: failed UPI transfers auto-reversed by T+1, ₹100 per day compensation after that; merchant payments T+5 | Build an auto-reversal job that meets the TAT with simulated bank delays |

**Check your understanding:** (1) Why did aggressive status checking make an outage worse rather than better? (2) A debit succeeded but the credit's outcome is unknown: what does each party do, and when? (3) Why does a regulator's compensation rule change your engineering priorities?

### Chapter 7 · UPI architecture (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Participants | Payer app (third-party app provider), payer PSP bank, NPCI's UPI switch, remitter (issuer) bank, payee PSP, beneficiary bank; VPAs and their resolution | Draw who holds which data and who talks to whom |
| 7.2 The pay flow (simplified) | Request from payer PSP to the switch; debit at the remitter bank; credit at the beneficiary bank; responses and confirmations; where each timeout lives | Trace a P2P payment through a simulator and label each message |
| 7.3 Collect, mandates and limits | P2P collect requests stopped from 1 October 2025 (fraud); merchant collect; AutoPay mandates and their execution windows; per-app API usage caps from August 2025 | Design an AutoPay executor that respects off-peak windows |
| 7.4 Device binding and authentication | UPI PIN, device binding, RBI's 2025 directions requiring two factors with one dynamic (effective April 2026) | Compare UPI's authentication with card 3-D Secure |
| 7.5 Designing for the switch | Rate limits, technical-decline budgets, success-rate monitoring per bank, graceful degradation | Build a per-bank success-rate dashboard and an alert that would have fired in April 2025 |

**Check your understanding:** (1) Where can a UPI payment get stuck, and who resolves it? (2) Why did NPCI remove P2P collect but keep merchant collect? (3) What should a PSP do when one remitter bank's success rate drops to 50%?

### Chapter 8 · Card payments (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Four-party model | Cardholder, issuer, merchant, acquirer, network; payment aggregators and gateways | Map a checkout on an Indian e-commerce site to the four parties |
| 8.2 Authorization to settlement | Authorization, capture, clearing, settlement, interchange and fees; auth expiry; incremental and partial captures | Simulate auth → partial capture → settlement and post the ledger entries |
| 8.3 Authentication and tokens | EMV 3-D Secure, network tokens, RBI card-on-file tokenisation (from October 2022) | Design a saved-card flow that stores no card numbers |
| 8.4 Disputes | Chargeback reasons, evidence, timelines, representment, ledger entries for disputed funds | Model a chargeback and a successful representment |
| 8.5 PCI DSS scope | PCI DSS v4.0.1; future-dated requirements mandatory since 31 March 2025 (including payment-page script integrity); hosted fields and tokenization to shrink scope | Draw the cardholder-data environment for two designs and compare their scope |

**Check your understanding:** (1) Why do card authorizations expire, and what happens to the hold? (2) How does tokenization reduce your PCI DSS scope? (3) Why is a chargeback a ledger event long after the original payment?

### Chapter 9 · Reconciliation (weeks 10–11)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 What reconciliation is | Internal (ledger vs payment records), external (provider reports, bank statements), three-way matching | Classify ten real-world mismatch types |
| 9.2 Matching | Exact keys, fuzzy matching (amount, time, reference), one-to-many and many-to-one, fees netted in settlement | Match 1M ledger rows to a settlement file with 0.5% planted breaks |
| 9.3 Breaks and ageing | Break classification, ageing buckets, ownership, automatic resolution vs manual queues | Build a break dashboard with ageing and owners |
| 9.4 Data quality for money | Stripe's checks for clearing, timeliness and completeness; amount-weighted metrics | Add completeness and timeliness checks to your pipeline |
| 9.5 Settlement files | Formats, late and corrected files, idempotent ingestion, re-runs | Ingest the same file twice and a corrected file once; prove the ledger is unchanged by the duplicate |

**Check your understanding:** (1) Why weight reconciliation metrics by amount and not only by count? (2) Why must file ingestion be idempotent? (3) Which breaks should page someone at 2 a.m., and which can wait for the morning?

### Chapter 10 · Correctness engineering (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Invariants | Conservation of money, non-negative balances where required, state-machine legality, every external movement matched | Encode six invariants as checks that run after every test |
| 10.2 Property-based and model-based tests | Generators for transfers, refunds and failures; a reference model to compare against | Find a bug with a generator that hand-written tests missed |
| 10.3 Deterministic simulation | Seeded schedulers, simulated clocks, disks and networks; TigerBeetle's approach | Replay a failing seed and fix the bug it found |
| 10.4 Deploys and migrations | Knight Capital (2012) and TSB (2018) as engineering-process failures; shadow ledgers, dual running, kill switches | Write a migration plan for moving balances to a new ledger with dual running |

**Check your understanding:** (1) Why does deterministic simulation find bugs that chaos testing misses? (2) What process controls would have limited the Knight Capital loss? (3) How do you prove a new ledger matches the old one before cutting over?

### Chapter 11 · Audit, compliance and operations (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Audit trails | Who did what, when, from where; tamper evidence; retention | Make every manual action produce an audit record that cannot be edited |
| 11.2 Maker-checker and segregation of duties | Two-person approval for adjustments and refunds above limits; break-glass access | Add maker-checker to manual ledger adjustments |
| 11.3 Operating payments | Success rates by provider and bank, technical declines, amount-weighted alerts, provider failover, incident communication | Write a runbook for "a provider's success rate dropped to 60%" |
| 11.4 Regulation as requirements | RBI turnaround-time rules, RBI authentication directions, PCI DSS, India's DPDP Act (see BE305), audit requests | Turn three regulatory rules into automated checks |

**Check your understanding:** (1) Why should engineers not have direct write access to the production ledger? (2) What makes payment alerts different from ordinary error-rate alerts? (3) How do you fail over between payment providers without double charging?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1: money types | Float-money bug report with tests |
| 2 | 2 | Lab 2: ledger core (no AI) | Ledger passing invariant suite |
| 3 | 2 | Holds and hot accounts | Throughput measurements; P1 due |
| 4 | 3 | Lab 3: state machines | Database-enforced transitions |
| 5 | 4 | Lab 4: idempotent steps | Crash-between-steps report |
| 6 | 5 | Lab 5: payout saga | Saga with compensations; P2 starts |
| 7 | 6 | Lab 6: status checks and reversals | Rule-compliant checker; TAT job |
| 8 | 7 | UPI simulator | Message trace and bank dashboard |
| 9 | 8 | Lab 7: card lifecycle | Auth/capture/settle/chargeback entries; P2 due |
| 10 | 9 | Lab 8: matching | Match rate and break report |
| 11 | 9 | Settlement ingestion | Idempotent file ingestion; P3 design review |
| 12 | 10 | Lab 9: simulation | Seeded failing run and fix |
| 13 | 11 | Operations | Runbook, maker-checker, audit log |
| 14 | — | P3 integration | P3 demo and audit walkthrough |
| 15 | Review and exam | — | Written exam and live incident exam |

## Working with AI in this course

- **Use AI for:** generating synthetic settlement files with realistic breaks; drafting state-machine diagrams from your notes; writing property-based test generators; summarizing regulator circulars (then reading the source yourself); explaining provider API documentation.
- **Do without AI (drills):** the ledger core (Lab 2); posting journal entries for a scenario by hand (auth, partial capture, refund, chargeback, FX); deciding what to do with an unknown outcome; the live incident exam, where you resolve a set of stuck payments from logs and a ledger.
- **Verify AI output by:** running the invariant suite (money conserved, no illegal transitions, every external movement matched) after every generated change; crash-testing every step boundary; checking every regulatory number against the RBI or NPCI source (or the press coverage that quotes it, labelled as such); grepping generated code for `float`, `double` and `Number` used on amounts.
- **Where AI still fails here (show it yourself):** ask an assistant to "handle bank API timeouts in a payment service" and check whether it retries the debit. Ask it to "refund a payment" and check whether it edits the original ledger entry instead of posting a reversal. Ask it to explain UPI reversal timelines and compare its answer with the RBI circular. Ask it for a reconciliation job and run it twice on the same file. Record each failure and the test that caught it.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs 1–9 | 25% |
| Projects P1 / P2 / P3 | 5% / 12% / 23% |
| Written exam (journal entries, state machines, UPI and card flows, rules) | 20% |
| Live incident exam (no AI) | 15% |

**Mastery gate:** you pass when you can, without AI help, (a) post correct double-entry journal entries for a 10-step scenario (authorization, partial capture, fee, refund, chargeback, FX settlement) with zero errors; (b) resolve 20 stuck payments in a provided system from its logs, ledger and a provider status API within 60 minutes, without creating any double movement; and (c) show your P3 platform surviving its chaos suite with all money invariants intact and every planted reconciliation break detected.

## Industry reality

- **UPI scale (September 2026):** 24.07 billion transactions worth ₹29.37 lakh crore in the month, about 802 million a day on average (NPCI data as reported by DD News, 2 October 2026).
- **NPCI rules after the April 2025 outages:** status checks only after 90 seconds and at most three within two hours (April 2025); faster API response times from 16 June 2025; per-app caps on balance enquiries and fixed AutoPay windows from 1 August 2025; P2P collect requests stopped from 1 October 2025.
- **RBI:** the 2019 turnaround-time circular sets T+1 auto-reversal for failed UPI transfers, with ₹100 a day compensation beyond it. Authentication directions issued in 2025 require two factors, one dynamic, from 1 April 2026.
- **Stripe's ledger** is an immutable, double-entry log of about five billion events a day, with data-quality checks for clearing, timeliness and completeness (February 2024). **PhonePe's** TStore uses Kafka as a write-ahead log for payment records. **Airbnb** built Orpheus to make every payment step idempotent (2019).
- **Failures:** the SEC found that Knight Capital lost more than $460 million in 45 minutes on 1 August 2012 after a deployment error, while 97 warning emails went unread. The FCA and PRA fined TSB £48.65 million in December 2022 for operational-risk failings in its 2018 IT migration.

Interview questions from this course:

1. **"Design a wallet. How do you make sure balances never drift or go negative?"** A strong answer covers double-entry entries, immutable history, derived or verified balances, conditional debits or constraints, hot-account contention, idempotency keys, and reconciliation as the safety net.
2. **"The bank call timed out. What does your service do?"** Cover marking the payment pending-unknown, never retrying the debit blindly, status checks with backoff within network rules, deadlines for resolution, auto-reversal rules, and what the user sees.
3. **"Walk me through a UPI payment. What happens if the debit succeeds and the credit fails?"** Cover the participants and messages, where timeouts occur, the reversal responsibility, RBI's T+1 rule and compensation, and how each party's systems learn the outcome.
4. **"How would you reconcile your ledger with the provider's settlement file?"** Cover idempotent ingestion, matching keys and fuzzy matching, fees netted in settlement, break classification and ageing, amount-weighted metrics, and alerting.
5. **"How do you build payouts on a bank API that isn't idempotent?"** Cover your own reference IDs created before the call, a pre-call record, status queries before any retry, sagas with compensations, and daily reconciliation against bank statements.

## Resources (free first)

- **Ledgers:** Modern Treasury, [Accounting for Developers](https://www.moderntreasury.com/journal/accounting-for-developers-part-i); TigerBeetle docs on [financial accounting](https://docs.tigerbeetle.com/coding/financial-accounting/) and [safety](https://docs.tigerbeetle.com/concepts/safety/); Stripe, [Ledger](https://stripe.dev/blog/ledger-stripe-system-for-tracking-and-validating-money-movement) (2024).
- **Idempotency and distributed correctness:** Stripe, [Designing robust and predictable APIs with idempotency](https://stripe.com/blog/idempotency) (2017); Airbnb, [Avoiding Double Payments in a Distributed Payments System](https://medium.com/airbnb-engineering/avoiding-double-payments-in-a-distributed-payments-system-2981f6b070bb) (2019); Pat Helland, [Life beyond Distributed Transactions](https://www.cidrdb.org/cidr2007/papers/cidr07p15.pdf) (CIDR 2007); PhonePe, [Demystifying TStore](https://tech.phonepe.com/demystifying-tstore-the-backbone-of-billions-of-transactions-at-phonepe/) (2024).
- **India:** RBI, [TAT harmonisation circular](https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11693) (2019); NPCI's UPI pages and circulars at [npci.org.in](https://www.npci.org.in/); NPTEL and RBI Academy material on payment systems.
- **Cards and security:** [EMV 3-D Secure](https://www.emvco.com/emv-technologies/3-d-secure/); [PCI SSC document library](https://www.pcisecuritystandards.org/document_library/) (PCI DSS v4.0.1).
- **Failures to study:** SEC, [Knight Capital](https://www.sec.gov/newsroom/press-releases/2013-222) (2013); FCA, [TSB fined £48.65m](https://www.fca.org.uk/news/press-releases/tsb-fined-48m-operational-resilience-failings) (2022).
- **Paid, worth it:** Kleppmann and Riccomini, *Designing Data-Intensive Applications*, 2nd edition (2026), on transactions and derived data.

## Sources

All checked 12 Oct 2026. Where an NPCI circular could not be fetched directly, the reputable press report that quotes it is cited.

- UPI September 2026 statistics (DD News, 2 Oct 2026): https://ddindia.co.in/2026/10/upi-transactions-surge-23-to-24-07-billion-in-september-npci/
- April 2025 outage cause and status-check limits (IANS, 29 Apr 2025): https://ianslive.in/npci-directs-banks-to-limit-check-transaction-api-usage-to-avoid-upi-outage--20250429145943 ; Outlook Money (outage cause): https://www.outlookmoney.com/banking/upi-outage-attributed-to-surge-in-api-calls-from-banks-says-npci ; API caps from 1 Aug 2025 (Outlook Money, Jun 2025): https://www.outlookmoney.com/banking/npci-tightens-upi-api-rules-from-august-1-after-repeated-outages
- Response-time reductions effective 16 Jun 2025 (MediaNama, Jun 2025): https://www.medianama.com/2025/06/223-npci-upi-changes-transaction-speed-fraud-prevention/
- P2P collect discontinued from 1 Oct 2025 (Outlook Business, Aug 2025): https://www.outlookbusiness.com/news/npci-to-stop-upi-p2p-collect-requests-from-oct-1-to-combat-fraud
- RBI TAT circular (20 Sep 2019): https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11693 ; RBI authentication directions (Khaitan & Co summary, 2025): https://khaitanco.com/thought-leadership/RBI-Authentication-Mechanisms-for-Digital-Payments-Transactions-Directions ; card-on-file tokenisation from 1 Oct 2022 (Business Today, Aug 2022): https://www.businesstoday.in/latest/trends/story/rbis-debit-credit-card-rule-to-change-from-october-1-check-all-details-here-345354-2022-08-23
- PCI DSS v4.0.1 future-dated requirements (PCI SSC blog): https://blog.pcisecuritystandards.org/coffee-with-the-council-podcast-guidance-for-pci-dss-e-commerce-requirements-effective-after-31-march-2025
- Stripe Ledger (16 Feb 2024): https://stripe.dev/blog/ledger-stripe-system-for-tracking-and-validating-money-movement
- SEC press release 2013-222 (16 Oct 2013): https://www.sec.gov/newsroom/press-releases/2013-222 ; FCA press release on TSB (20 Dec 2022): https://www.fca.org.uk/news/press-releases/tsb-fined-48m-operational-resilience-failings

_Last reviewed: 2026-10_
