# OPS404 · Labs and projects

Use local services on kind (with metrics-server, KEDA and the OPS303 telemetry stack) and load generators running on a separate machine or container with pinned CPUs, so the generator never competes with the system under test. For the ARM vs x86 comparison, use a free-tier or credit-funded cloud VM of each type for a few hours, with a budget alarm, and destroy it afterwards. Labs 2, 4 and 5 are done without AI assistance.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Percentiles and fan-out | Build a fan-out service (1 → 10, 100 back-ends) with a 1% slow path; measure end-to-end tails; compare with 1 − 0.99ⁿ | Plots, measured vs predicted table | 3 h |
| 2 · Little's law in the wild | Verify L = λW on a real queue (worker pool or broker) from your metrics; find a dashboard that violates it and explain why | Calculations, explanation | 3 h |
| 3 · Queue model vs reality | Single-worker service with controlled service-time distributions; predict latency with M/M/1 and Kingman; measure | Prediction vs measurement plot, error analysis | 5 h |
| 4 · USL fit | Measure throughput at 1, 2, 4, 8, 16, 32 instances; fit σ and κ; predict the peak | Data, fit, prediction vs a validation run | 4 h |
| 5 · Coordinated omission | Test the same service with wrk and wrk2 (or k6 arrival-rate) while injecting 1-second stalls | Latency distributions and an explanation of the gap | 3 h |
| 6 · k6 scenarios | Smoke, load, stress, soak, spike and breakpoint tests with thresholds; prove the generator is not the bottleneck | Scripts, results, generator CPU evidence, AI script audit | 5 h |
| 7 · Profiling clinic | Profile a slow demo service (CPU, allocations, locks, queries); fix the top bottleneck only | Flame graphs before/after, p99 before/after with confidence intervals | 5 h |
| 8 · Capacity model | Spreadsheet or notebook model: per-request cost × forecast demand + per-zone headroom; sensitivity analysis | Model, assumptions, sensitivity chart | 4 h |
| 9 · Autoscaling tuning | Tune HPA (stabilization, policies), KEDA on queue lag and a scheduled pre-scale; measure time to capacity end to end | Configs, timelines from pending pod to serving | 5 h |
| 10 · Cost per request, x86 vs ARM | Run the same service on comparable x86 and ARM VMs at the same p99 target; compute cost per 1,000 requests | Benchmark data, cost table, destroy proof | 4 h |

## Projects

### P1 · Queueing model vs reality (L1, ~6 hours)

**Real-world inspiration:** Little's law and the utilization knee are behind every connection-pool and worker-pool setting in production; Google's SRE workbook chapter on [managing load](https://sre.google/workbook/managing-load/) shows why services fall over well before 100% utilization.

**What to build:** a small service with a configurable worker pool and service-time distribution, a load generator using an open arrival model, and a notebook that predicts latency from queueing models and compares with measurements.

**Acceptance criteria:**
- **Prediction:** below 70% utilization, predicted mean and p95 latency are within 20% of measured values for at least two service-time distributions.
- **Knee:** the report identifies the utilization at which latency doubles from its low-load value, predicted and measured.
- **Pool sizing:** a pool size computed from Little's law achieves the target throughput; a pool twice that size is shown not to help (or to hurt), with an explanation.
- **Honesty:** the report states where the model fails (high utilization, heavy tails) and why.

**Stretch goals:** an M/M/c model for a multi-worker pool and a demonstration that one shared queue beats per-worker queues.

**What it proves to an employer:** you can reason about capacity with mathematics rather than guesswork, which is rare and visible in system-design interviews.

### P2 · Load-test, profile and double a service's capacity (L2, ~15 hours)

**Real-world inspiration:** Gil Tene's work on [measuring latency correctly](https://www.infoq.com/presentations/latency-response-time/) and Google's [The Tail at Scale](https://research.google/pubs/the-tail-at-scale/).

**What to build:** take a three-tier demo application (API, cache, database). Write a workload model from its access logs, run a breakpoint test, find and fix at least two real bottlenecks with profiles, and add a performance regression test to CI.

**Acceptance criteria:**
- **Capacity:** the request rate sustainable at p99 under 300 ms and error rate under 0.1% at least doubles, shown with before/after breakpoint tests.
- **Measurement quality:** all tests use an open arrival model without coordinated omission; each comparison uses at least 5 runs and reports 95% confidence intervals.
- **Evidence:** each fix has a profile showing the bottleneck before and its absence after; one rejected "optimisation" (including at least one AI-suggested one) is documented with data.
- **Regression guard:** a CI job fails on a planted 10% p95 regression and passes on the unchanged code in 10 of 10 runs (no false alarms).
- **Generator health:** the load generator's CPU stayed below 70% throughout.

**Stretch goals:** hedged requests for one fan-out call, with the p99 gain and extra load reported; a USL fit predicting the next bottleneck.

**What it proves to an employer:** you can make a system faster with evidence and stop regressions, which backend and SRE teams need constantly.

### P3 · Capacity plan and rehearsal for a peak event (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** NPCI's definition of UPI peak hours and its limits on system-initiated calls during them ([MediaNama, May 2025](https://www.medianama.com/2025/05/223-npci-banks-balance-upi-transaction-guidelines/)); Disney+ Hotstar's posts on [scaling for live sport](https://blog.hotstar.com/scaling-infrastructure-for-millions-from-challenges-to-triumphs-part-1-6099141a99ef); Meta's [Kraken](https://www.usenix.org/conference/osdi16/technical-sessions/presentation/veeraraghavan) live-traffic tests. The event and the traffic numbers are an *illustrative scenario*. Do not use or guess any company's private figures.

**What to build:** for a service of your choice (your P2 system, or the OPS304 payment simulator), prepare for a "match final" or "festival sale" peak of 10× normal traffic arriving within 60 seconds:
- a demand forecast with intervals from 12 months of synthetic history (including daily, weekly and festival seasonality);
- a capacity model per tier, including database and cache;
- autoscaling with scheduled pre-scaling plus reactive HPA and KEDA, with node provisioning;
- a degradation plan that sheds non-critical features first;
- a full rehearsal with a spike test;
- a cost estimate and a post-event report.

**Acceptance criteria:**
- **Survives the spike:** at 10× baseline reached within 60 seconds, p99 stays within the SLO and the error rate stays under 0.1%, with pre-scaling allowed; graphs show every tier.
- **Time to capacity:** without pre-scaling, the measured time from spike to sufficient capacity is reported. The plan explains why pre-scaling is (or is not) required.
- **Beyond forecast:** at 15× the system degrades gracefully: non-critical features are shed, critical journeys stay above 99% success, and there is no metastable tail after load drops.
- **Cost:** cost per 1 million requests at peak and at baseline is computed, plus one optimisation with measured savings and no SLO breach.
- **Review:** a capacity review document (forecast, model, assumptions, risks, go/no-go criteria) is approved by two classmates acting as engineering managers, and a post-event report compares forecast with what happened.

**Stretch goals:** a token-based capacity model for an LLM feature in the same product; a Prequal-style load balancer compared with least-requests under heterogeneous back-ends.

**What it proves to an employer:** you can stand in a launch review and say with evidence how much capacity is needed, what it will cost and what happens if you are wrong. That is a senior SRE and capacity-engineer skill.

## Feeds into

- [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md): performance modelling and autoscaling are strong capstone topics.
- [CAR401](../../../../05_shared_years_3_to_5/CAR401_career_lab_ii_interviews_system_design_and_ai/README.md): back-of-the-envelope capacity estimates in system-design interviews.
- [CLD403 FinOps and Cloud Cost Engineering](../../../cloud_engineering/year_4/CLD403_finops_and_cloud_cost_engineering/README.md): cost per request feeds FinOps practice.
- [OPS501 Frontier Seminar](../../year_5/OPS501_frontier_seminar_autonomous_infrastructure/README.md): autoscaling as a control loop and learned resource management.
