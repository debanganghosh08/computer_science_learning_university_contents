# OPS402 · Labs and projects

The lab environment is a kind cluster running [Online Boutique](https://github.com/GoogleCloudPlatform/microservices-demo) or the [OpenTelemetry Demo](https://opentelemetry.io/docs/demo/), with Istio (or another mesh), Chaos Mesh, LitmusChaos, toxiproxy, k6 and the observability stack from [OPS303](../../year_3/OPS303_observability_metrics_logs_traces/README.md). Simulations are written in Python or Go. Every experiment has a written hypothesis and abort condition before it runs, even locally. Labs 2, 4 and 7 are done without AI assistance.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Gray failure | Build a service whose health check passes while 30% of user requests fail; detect it from user-facing SLIs | Code, detection query, write-up | 3 h |
| 2 · Retry storm simulator | Discrete-event simulation of a 3-layer call chain; compare naive retries, backoff, jitter and retry budgets | Simulator, plots of load amplification and recovery time | 5 h |
| 3 · Breakers and bulkheads | Add circuit breakers and separate pools so one slow dependency cannot take down the frontend | Config, before/after latency under fault | 4 h |
| 4 · Shedding and metastability | Priority load shedding and an adaptive concurrency limit; then push a simulator into a metastable state and recover it | Shedding evidence, recovery runbook | 5 h |
| 5 · Fallback policy | Classify every dependency as hard or soft; implement degraded modes; survive a cache flush | Dependency table, stampede test | 4 h |
| 6 · Chaos Mesh and Litmus | Three experiments (latency, partition, pod kill) with probes and automatic abort on SLO burn | Experiment documents, results, abort proof | 6 h |
| 7 · DR drill | Restore a database from backup and fail a service over to a second cluster; measure RTO and RPO | Timings against targets, gaps found | 4 h |
| 8 · Faults in CI | Five toxiproxy fault tests (latency, reset, timeout, slow close, bandwidth) in an integration pipeline | Pipeline, a test that caught a real bug | 4 h |
| 9 · LLM resilience | Inject 429s and long latencies into an LLM call path; add a breaker, a fallback model and an agent step/spend budget | Config, test results, cost cap proof | 4 h |
| 10 · Nightly chaos | Schedule three experiments nightly, gated on remaining error budget; publish a resilience scorecard | Workflow, 5 nights of results | 4 h |

## Projects

### P1 · Retry-storm laboratory (L1, ~6 hours)

**Real-world inspiration:** AWS's analysis of [exponential backoff and jitter](https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/); Google Cloud's June 2025 herd effect and its commitment to randomised exponential backoff ([incident](https://status.cloud.google.com/incidents/ow5i3PPK96RduMcb1SsW)); the UPI status-check storms behind NPCI's 2025 API limits ([MediaNama](https://www.medianama.com/2025/05/223-npci-banks-balance-upi-transaction-guidelines/)).

**What to build:** a reproducible simulator (with a small CLI) of clients, a mid-tier service and a backend with limited capacity, supporting: no retries, fixed retries, exponential backoff, full jitter, retry budgets, a minimum delay before status checks, and client-side adaptive throttling.

**Acceptance criteria:**
- **Reproduces the problem:** naive retries across 3 layers amplify backend load by at least 5× during a 60-second backend slowdown.
- **Shows the fix:** with jittered backoff plus a 10% retry budget, amplification stays at or below 1.2×, and backlog drains within 2× the fault duration.
- **Status-check rule:** adding a 90-second minimum delay before status checks (as in the NPCI circular) is shown to cut peak load, with a plot.
- **Reproducible:** fixed random seeds; one command regenerates every plot; results are explained in a 2-page note.

**Stretch goals:** model a cache in front of the backend and show a cold-cache metastable failure.

**What it proves to an employer:** you understand retries as a system property, which is the source of many real outages.

### P2 · Harden a microservice application (L2, ~15 hours)

**Real-world inspiration:** AWS Builders' Library guidance on [timeouts and retries](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/), [load shedding](https://aws.amazon.com/builders-library/using-load-shedding-to-avoid-overload/) and [fallbacks](https://aws.amazon.com/builders-library/avoiding-fallback-in-distributed-systems/).

**What to build:** take Online Boutique (or the OpenTelemetry Demo) and make it resilient: deadlines and timeouts from measured latencies, retry budgets, breakers with outlier detection, bulkheads, priority shedding that protects checkout, degraded modes for recommendations and ads, and six chaos experiments that prove it.

**Acceptance criteria:**
- **Soft-dependency latency:** with +2 s latency injected into a non-critical service, checkout success stays at or above 99% and checkout p99 stays under 1.5 s.
- **Hard-dependency failure:** with the payment dependency failing at 50%, the system fails fast (p99 error response under 300 ms) and recovers within 60 seconds of the fault ending, with no metastable tail.
- **Overload:** at 3× normal load, checkout is protected by shedding lower-priority traffic, and shed requests get a clear 503 with `Retry-After`.
- **Safety:** each of the 6 experiments has a document, a blast-radius limit and an abort condition; at least one abort fires automatically during testing.
- **Evidence:** before/after dashboards for every experiment.

**Stretch goals:** shuffle-sharded tenants with a noisy-tenant experiment; deadline propagation verified in traces.

**What it proves to an employer:** you can make an existing system measurably more resilient, which is the day-to-day work of senior SREs.

### P3 · Continuous resilience programme and capstone game day (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** the AWS October 2025 event, in which EC2 recovery lagged DynamoDB's because of a lease backlog ([summary](https://aws.amazon.com/message/101925/)); the OSDI 2022 study of [metastable failures in the wild](https://www.usenix.org/conference/osdi22/presentation/huang-lexiang); Netflix's [Principles of Chaos Engineering](https://principlesofchaos.org/).

**What to build:** a resilience programme for your P2 system (or your [OPS304](../../year_3/OPS304_site_reliability_engineering_slos_error_budgets/README.md) P3 payment system):
- nightly automated experiments gated on error budget;
- a resilience scorecard covering failure modes per service;
- a DR runbook with timed restore and failover;
- a facilitated 3-hour game day with four scenarios: zone or cluster loss, DNS failure, dependency brownout and bad config push;
- one deliberately induced metastable state that responders must recover from;
- a public-quality learning review.

**Acceptance criteria:**
- **Steady state:** the SLO is held in at least 3 of 4 scenarios, or each breach has a documented fix that is implemented and re-tested before hand-in.
- **Detection:** every scenario is detected by an alert within 5 minutes.
- **Metastable recovery:** responders who did not design it recover from the induced metastable state within 10 minutes using documented levers.
- **DR:** measured RTO and RPO meet the targets you set in advance (for example RTO 15 minutes, RPO 1 minute), or the gap is explained with a plan.
- **Automation:** nightly experiments ran for at least 7 nights, with results on the scorecard and at least one regression caught.
- **Learning review:** published, blameless, with contributing factors and actions; two actions implemented.

**Stretch goals:** a deterministic simulation test for one service's retry and timeout logic; an AI assistant proposing next week's experiments, with your critique of each.

**What it proves to an employer:** you can run resilience as an ongoing engineering programme, not a one-off demo, and you can lead people through failure.

## Feeds into

- [OPS501 Frontier Seminar](../../year_5/OPS501_frontier_seminar_autonomous_infrastructure/README.md): metastability, gray failure and deterministic simulation are seminar topics.
- [OPS403 AIOps and Agentic Operations](../OPS403_aiops_and_agentic_operations/README.md): your experiments become labelled data for evaluating AI incident tools.
- [SAR404 Resilience, Business Continuity and Security Strategy](../../../security_architecture/year_4/SAR404_resilience_business_continuity_and_security/README.md): continuity planning at organisation level.
- [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md): many resilience questions make good capstones.
