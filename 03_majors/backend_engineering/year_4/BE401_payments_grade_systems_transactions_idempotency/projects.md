# BE401 · Labs and projects

All labs use simulators, never real money or real bank credentials. The course provides a simulated bank, a simulated UPI-style switch and a simulated card network. They time out, reply late, duplicate callbacks and occasionally return wrong statuses, on a seed you control. Provider sandboxes (Razorpay or Stripe test mode) are optional for P3. Every lab ends with the same invariant suite: money conserved, no illegal state transitions, every external movement matched. Lab 2 and the live incident exam are done without AI assistants.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Money types | Integer minor units, ISO 4217 exponents, rounding and allocation; business-date assignment across IST midnight | Tests for six float-money bugs; a property test proving splits never lose a paisa | 4 h |
| 2 · Ledger core (no AI) | Accounts, balanced journal entries, holds, pending vs posted, reversals; invariants after every operation | Ledger library passing 1M random operations with the invariant suite | 8 h |
| 3 · State machines | Payment, refund and payout state machines enforced in the database with an `UNKNOWN` state and resolution deadlines | Diagram, constraints, and tests that illegal transitions are rejected | 5 h |
| 4 · Idempotent steps | Split a payment into pre-call, call and post-call steps; crash between every pair | Crash report: 300 crashes, zero duplicate debits, every payment resolved | 6 h |
| 5 · Payout saga | Wallet-to-bank payout saga with compensations and an outbox | Failure matrix for each step with the observed end state | 6 h |
| 6 · Status checks and reversals | A status checker obeying a configurable rule (first check after 90 s, at most 3 in 2 h) and an auto-reversal job meeting a simulated T+1 | Load test showing the rule is never violated; TAT compliance report over 100,000 failed transfers | 6 h |
| 7 · Card lifecycle | Authorization, partial capture, settlement with fees, refund and chargeback, all posted to the ledger | Journal entries per step and a balance sheet that ties out | 5 h |
| 8 · Reconciliation matching | Three-way matching (ledger, provider report, bank statement) over 1M rows with 0.5% planted breaks | Match rate, break classification and ageing report | 6 h |
| 9 · Deterministic simulation | A seeded simulation of clients, provider and clock; find and fix one bug by replaying its seed | The failing seed, the trace, the fix and the passing re-run | 6 h |

## Projects

### P1 · Double-entry ledger service (L1, ~6 hours)

**Real-world inspiration:** Stripe's ledger is an immutable double-entry log that verifies money movement ([Stripe, Feb 2024](https://stripe.dev/blog/ledger-stripe-system-for-tracking-and-validating-money-movement)). Modern Treasury's [Accounting for Developers](https://www.moderntreasury.com/journal/accounting-for-developers-part-i) and [TigerBeetle's docs](https://docs.tigerbeetle.com/coding/financial-accounting/) explain the model for engineers.

**What to build:** a ledger service on PostgreSQL with an HTTP API: create account, post a journal entry (two or more lines summing to zero), place, capture and release a hold, reverse an entry, get balance (ledger and available) and get history.

**Acceptance criteria:**
- **Conservation:** after 1,000,000 random operations from 8 concurrent clients, the sum of all entry lines is exactly zero, and every account's cached balance equals the sum of its entries. A checker runs after each test.
- **Rejection:** unbalanced entries, entries on closed accounts and holds exceeding the available balance are rejected by the database layer, not only by application code.
- **Immutability:** history is append-only; corrections are reversals. A test proves `UPDATE` and `DELETE` on entries are impossible for the application's database role.
- **Idempotency:** posting the same entry twice with one idempotency key creates one entry.
- **Throughput:** at least 2,000 entries/s on a laptop with p99 under 50 ms, measured with k6, including a hot-account test and your mitigation.

**Stretch goals:** multi-currency accounts with FX entries; balance-as-of-date queries; compare your throughput with TigerBeetle on the same workload.

**What it proves to an employer:** you understand the data model under every fintech product and can build it so it cannot quietly lose money.

### P2 · UPI-style switch and bank simulator with failure discipline (L2, ~15 hours)

**Real-world inspiration:** NPCI's 2025 rules after the April 2025 outage limit how often banks may check transaction status and tighten API response times ([IANS, Apr 2025](https://ianslive.in/npci-directs-banks-to-limit-check-transaction-api-usage-to-avoid-upi-outage--20250429145943); [MediaNama, Jun 2025](https://www.medianama.com/2025/06/223-npci-upi-changes-transaction-speed-fraud-prevention/)). RBI requires auto-reversal of failed UPI transfers by T+1 ([RBI, 2019](https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11693)). Your system is a teaching simulation, not NPCI's design.

**What to build:** five services:
- a payer app backend;
- a payer PSP;
- a central switch;
- a remitter bank and a beneficiary bank, each with its own ledger from P1.

Implement pay requests, debit, credit, responses, status checks, reversals, VPA resolution and per-bank success-rate monitoring. Fault injection on every hop: timeouts, slow responses, lost responses, duplicate responses and one bank degrading to 50% success.

**Acceptance criteria:**
- **Conservation:** over 1,000,000 transactions with 5% injected faults, total money across all bank ledgers is unchanged, checked after every run.
- **No stranded money:** every transaction debited but not credited is reversed or completed within simulated T+1. A report lists the time to resolution for each.
- **Status-check discipline:** the payer PSP never sends a status check before 90 s or more than three within two hours for any transaction (log audit). During the degraded-bank scenario, the switch's total request rate stays within its configured limit, unlike a provided naive client.
- **Latency:** with no faults, end-to-end p99 is under 2 s at 2,000 transactions/s on a laptop, and every hop respects its timeout budget.
- **Visibility:** a dashboard shows success and technical-decline rates per bank, and an alert fires within 2 minutes of the degraded-bank scenario starting.

**Stretch goals:** AutoPay mandates executed only in configured off-peak windows; UPI Lite-style small offline-first payments with later settlement; a deterministic simulation mode that replays any failing run.

**What it proves to an employer:** you can reason about money moving between independent organizations under real failure, which is what Indian fintech, banks and payment companies hire for.

### P3 · Merchant payments platform with reconciliation (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** payment gateways such as Razorpay and Stripe combine checkout, a payment state machine, idempotent APIs, signed webhooks, payouts, refunds, disputes and daily reconciliation. Airbnb's Orpheus shows step-level idempotency inside such a platform ([Airbnb, 2019](https://medium.com/airbnb-engineering/avoiding-double-payments-in-a-distributed-payments-system-2981f6b070bb)). The platform you build is an **illustrative scenario**; no real card data is used.

**What to build:**
- **Payments:** a merchant-facing API with payment intents, capture, refunds and payouts (idempotency from BE301, signed webhooks), and a payment state machine with an `UNKNOWN` state.
- **Money movement:** the ledger from P1; card payments through the simulated card network (or a provider's test mode) using tokens only, with no card numbers on your servers; UPI payments through the P2 switch.
- **Plumbing:** an outbox for all money events.
- **Settlement and reconciliation:** a settlement-file generator for the provider and the bank, with fees, late files and corrections, and a three-way reconciliation engine with break classification, ageing and owners.
- **Controls:** maker-checker for manual adjustments, a tamper-evident audit log, and a runbook.

**Acceptance criteria:**
- **Chaos:** over 200,000 payments with at least 500 kill events across every service and the database, there are zero double charges and zero payouts without matching ledger entries. Every payment reaches a terminal state or a manual queue with a reason within 10 minutes.
- **Reconciliation accuracy:** the engine detects 100% of 50 planted breaks (missing settlement, amount mismatch, duplicate in file, fee mismatch, late file, orphan refund), classifies at least 95% correctly, and has a false-positive rate under 1%.
- **Daily close:** ingesting and reconciling 1 million transactions completes in under 10 minutes. Re-ingesting the same files changes nothing.
- **Controls:** every manual adjustment needs two different approvers (tested). The audit log detects a modified record. The application's database role cannot alter ledger history.
- **PCI scope:** a data-flow diagram and a scan of logs and databases show that no full card number ever reaches your systems.
- **Write-up:** a design document with the state machines, chart of accounts, journal entries for each flow, a failure-mode table, a reconciliation break taxonomy, and a post-mortem of the worst bug your chaos suite found.

**Stretch goals:** provider failover between two simulated gateways without double charging; dispute workflow with evidence submission; a fraud-rule hook in the authorization path (a preview of OV10B).

**What it proves to an employer:** you can design, build and operate a payments platform whose correctness survives crashes, duplicates and messy external data. Few engineers can show this, and fintech, banks and marketplaces pay a premium for it.

## Feeds into

- [OV10A Payment Systems Engineering: UPI, Cards and Ledgers](../../../../04_overlaps/OV10_fintech_systems_engineering/OV10A_payment_systems_engineering_upi_cards/README.md) and [OV10B Fraud Detection and Risk Systems](../../../../04_overlaps/OV10_fintech_systems_engineering/OV10B_fraud_detection_and_risk_systems/README.md).
- [BE501 Frontier Seminar](../../year_5/BE501_frontier_seminar_durable_execution_serverless/README.md): payment workflows on durable execution engines.
- The [Backend Engineering flagship industry project](../../../../06_career_and_market_readiness/05_industry_projects/BE_backend_engineering.md) and a [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) capstone on payments correctness.
