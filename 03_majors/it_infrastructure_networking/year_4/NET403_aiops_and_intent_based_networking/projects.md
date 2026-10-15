# NET403 · Labs and projects

The lab is your NET303 environment grown up: a 10–15 node Containerlab network generated from NetBox, a telemetry pipeline (gnmic, Prometheus or InfluxDB, Kafka optional), Batfish, and a fault-injection script that plants labelled faults on a schedule. Use local open-weight models or a hosted model under your institution's data rules; never send real employer configurations or logs to an external model without approval. Every experiment states the model, version, prompt and number of runs.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Claims vs evidence and baselines | Claims-vs-evidence table for two vendor AIOps platforms; baseline MTTD and MTTR for 10 planted lab faults diagnosed by hand | Table with sources; baseline metrics | 3 h |
| 2 · Telemetry pipeline with context | gNMI, syslog, flows and BMP into stores, enriched with NetBox site/role/link labels; data-quality checks | Pipeline code, data-quality report | 5 h |
| 3 · Anomaly detectors | EWMA, Holt-Winters, MAD and isolation-forest detectors on 4 weeks of generated traffic with 20 labelled incidents | Precision, recall, F1 and detection delay per detector at an alert budget of 5 per day | 5 h |
| 4 · Logs and routing events | Template mining on syslog; BMP-based detection of a flap, a leak and a mass withdrawal | Rare-template list, detection timestamps vs ground truth | 4 h |
| 5 · Topology-aware correlation | Graph from NetBox and LLDP; reduce alert storms to incidents; rank root causes | Noise-reduction ratio, top-1 and top-3 accuracy on 10 incidents | 5 h |
| 6 · Intents as assertions | Ten plain-language intents translated to Batfish assertions, run on every change and every 15 minutes | Assertion suite, CI runs showing a violation caught | 4 h |
| 7 · Verification under failures | Check reachability and isolation intents under every single-link failure; find a planted forwarding loop | Failure-scenario report, loop evidence | 4 h |
| 8 · Digital twins | Model twin and emulation twin rebuilt nightly from NetBox; answer 3 what-if questions; fidelity statement | Twin build logs, answers with evidence, fidelity statement | 5 h |
| 9 · Assistant with read-only tools | Retrieval over runbooks and configs; 4 read-only tools via a small MCP server; prompt-injection test with a planted interface description | Tool-call logs; injection test results | 5 h |
| 10 · Closed loop with guardrails | Traffic-shift loop with hysteresis, action catalogue, locks, size checks and a kill switch | Oscillation test, kill-switch timing, audit log | 5 h |

## Projects

### P1 · Network anomaly detection with an honest evaluation (L1, ~6 hours)

**Real-world inspiration.** NOCs serving many customers drown in threshold alerts that fire every Monday morning; vendors promise AI baselines. This project measures what simple, explainable methods achieve before anyone buys anything.

**What to build.** A detector service for interface utilisation, errors and latency across your lab (or a public dataset with labels), using seasonal baselines and robust statistics, with an optional isolation forest. Inject 20 labelled incidents of 5 types (link degradation, congestion, error bursts, latency step, silent black hole).

**Acceptance criteria**
- A report gives precision, recall and median detection delay per incident type, at a fixed alert budget of 5 alerts per day.
- The detector beats a static-threshold baseline on F1 by a stated margin, or the report explains why it does not.
- Every alert includes the evidence (expected range, observed value, duration) in plain text.
- Results are reproducible from one command with a fixed random seed.

**Stretch goals.** Add per-interface-class models; test robustness when 10% of data points are missing.

**What it proves to an employer.** You evaluate AI for operations with numbers rather than demos, which is rare and valued.

### P2 · Intent assurance service (L2, ~15 hours)

**Real-world inspiration.** RFC 9315 describes intent fulfilment and assurance; Batfish-style verification lets operators check properties such as "guest never reaches finance" before and after every change. Large operators and cloud providers use verification in-house; enterprises are starting to.

**What to build.** A service that holds 15 intents for the lab (reachability, isolation, redundancy, routing policy, security), translates each to verifiable checks (Batfish assertions plus live probes), runs them on every pipeline change and on a timer, reports violations with evidence, and links violations to the change or failure that caused them.

**Acceptance criteria**
- Across 20 scripted changes and failures (8 of which violate an intent), the service flags all 8 violations and raises no false alarms on the other 12.
- Each violation report names the intent, the failing flow or route, and the triggering change or event, within 2 minutes of the event.
- Intents are checked under all single-link failures at least daily, with results stored.
- The intent file is human-readable and reviewed like code.

**Stretch goals.** Add a natural-language front end that drafts new intents for human approval, and measure how often drafts need correction.

**What it proves to an employer.** You can make "the network does what the business needs" a continuously tested property, the core of intent-based networking.

### P3 · A guarded network operations agent with closed-loop remediation (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** Cisco's February 2026 AgenticOps announcement describes agents that reason from telemetry to root cause and act with "built-in oversight"; the AWS October 2025 and Cloudflare November 2025 outages show automation failing at scale. A managed network service provider (illustrative) wants an agent that cuts MTTR for its NOC without becoming the next outage.

**What to build.** An end-to-end system on your lab: telemetry pipeline with context (Lab 2), anomaly detection (P1), topology-aware correlation (Lab 5), intent assurance (P2), a diagnosis agent with read-only tools and a verifier step, and a closed loop that can execute only actions from your catalogue (for example, shut a flapping link, shift traffic, roll back the last change) under approval tiers, blast-radius caps, locks, hysteresis and a kill switch. Evaluate it on a benchmark of at least 25 planted faults against your Lab 1 human baseline.

**Acceptance criteria**
- Over 3 runs of the 25-fault benchmark, the report states top-1 diagnosis accuracy, median time to diagnosis and MTTR with and without the agent, with variance; MTTR improves on the human baseline for at least the fault classes the action catalogue covers.
- Zero actions outside the catalogue are executed; every executed action has evidence, approval record (where required) and a verified outcome in the audit log.
- In a planted "dangerous" scenario (for example, an action that would isolate a site), the blast-radius cap or approval tier stops it.
- A prompt-injection attempt placed in device data does not change the agent's tool use (logged and shown).
- The kill switch halts all automated actions within 5 seconds.
- A two-page adoption recommendation states which actions should stay manual, which can be approved, and which could become automatic, with the evidence for each.

**Stretch goals.** Compare two models (one local, one hosted) on accuracy, cost and latency; run the benchmark after a model upgrade and report regressions.

**What it proves to an employer.** You can build, measure and govern AI that operates a network, the work that is replacing ticket-driven operations and that few engineers can yet do well.

## Feeds into

- [NET501 Frontier Seminar](../../year_5/NET501_frontier_seminar_5g_satellite_internet/README.md): autonomous networks in 5G cores and programmable data planes.
- [RES502 Reading, Reproducing and Extending Papers](../../../../05_shared_years_3_to_5/RES502_reading_reproducing_and_extending_papers/README.md) and [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md): P3 can become a thesis on agent evaluation for networks.
- [OPS403 AIOps and Agentic Operations](../../../devops_sre_platform_engineering/year_4/OPS403_aiops_and_agentic_operations/README.md) as an elective for service-level AIOps.
- The major's [flagship industry project](../../../../06_career_and_market_readiness/05_industry_projects/NET_it_infrastructure_networking.md).
