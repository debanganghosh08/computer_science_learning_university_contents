# OPS404 · Performance and Capacity Engineering

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 8 | 4 (≈ 120 hours) | L3 → L4 | [OPS304](../../year_3/OPS304_site_reliability_engineering_slos_error_budgets/README.md); strongly recommended: [OPS302](../../year_3/OPS302_linux_systems_administration_in_depth/README.md), [FND116](../../../../01_year_1_foundations/semester_2/FND116_probability_and_statistics_i/README.md) | [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md), [CAR401](../../../../05_shared_years_3_to_5/CAR401_career_lab_ii_interviews_system_design_and_ai/README.md) |

Part of the [DevOps, SRE and Platform Engineering major](../../README.md). [OPS302](../../year_3/OPS302_linux_systems_administration_in_depth/README.md) taught you to find a bottleneck on one host, and [OPS304](../../year_3/OPS304_site_reliability_engineering_slos_error_budgets/README.md) introduced capacity planning for launches. This course gives you the mathematics and the methods to predict how a system will behave before the traffic arrives, to measure it without fooling yourself, and to buy exactly enough capacity. Test-tool depth for QA engineers is in [QAE303](../../../software_quality_test_engineering/year_3/QAE303_performance_and_load_testing/README.md), application-level caching and sharding in [BE402](../../../backend_engineering/year_4/BE402_scalability_and_performance_caching_sharding/README.md), and cloud cost management in [CLD403](../../../cloud_engineering/year_4/CLD403_finops_and_cloud_cost_engineering/README.md).

## Why this course matters now

Indian systems face some of the sharpest demand peaks in the world:

- **UPI:** NPCI formally defines peak hours (10 am–1 pm and 5–9:30 pm), when transactions per second are highest, and since August 2025 restricts system-initiated API calls during them.
- **Streaming:** live cricket on streaming platforms produces sudden concurrency spikes that Disney+ Hotstar has written about publicly.

Getting capacity wrong is expensive either way: too little and you have an outage, too much and you burn money for idle machines.

The methods are well established. Little's law, queueing models and the Universal Scalability Law predict where latency explodes. Google's "The Tail at Scale" (2013) explains why fan-out makes rare slowness common. Meta's Kraken (OSDI 2016) shifted live traffic to find limits in production. Google's Autopilot (EuroSys 2020) automated resource limits. Prequal (NSDI 2024) showed that balancing on load alone is the wrong goal.

The tools keep improving. k6 reached its 2.x line, Kubernetes made in-place pod resizing stable in 1.35, and KEDA and Karpenter make scaling event-driven and fast. AI assistants write load scripts and suggest optimisations quickly. They also produce benchmarks with coordinated omission, compare single noisy runs and "optimise" code that was never the bottleneck. Someone has to know the mathematics and the measurement traps.

## Learning outcomes

By the end you can:

1. **Define** performance goals as SLO-linked percentiles and budgets, and **explain** why averages and single runs mislead.
2. **Apply** Little's law, the utilization law and basic queueing models (M/M/1, M/M/c, Kingman's approximation) to predict latency, queue length and pool sizes.
3. **Fit** Amdahl's law and the Universal Scalability Law to load-test data, and **predict** the peak and retrograde regions of scaling.
4. **Run** load tests correctly: open vs closed models, arrival-rate executors, coordinated-omission-free tools, warm-up, steady state and statistical comparison.
5. **Find** bottlenecks with profiling (CPU, memory, locks, I/O, network, database), and **fix** the one that matters with before/after evidence.
6. **Build** capacity models from per-request resource costs, forecasts and headroom (N+k, zone loss), including lead times for scarce resources such as GPUs.
7. **Tune** autoscaling (HPA, KEDA, VPA and in-place resize, Karpenter or cluster autoscaler, scheduled and predictive scaling) and **explain** its stability limits.
8. **Choose** load-balancing algorithms and tail-latency techniques (power of two choices, hedged requests, Prequal-style probing) for a fan-out service.
9. **Trade off** cost, performance and reliability with cost per request, right-sizing, architecture choices (for example ARM instances) and AI inference metrics (TTFT, tokens per second).

## Chapters and lessons

### Chapter 1 · Performance goals and honest numbers (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Latency, throughput, utilization | Definitions, units, and how they interact | Measure all three for one service at 5 load levels |
| 1.2 Percentiles | Why averages lie, percentiles of percentiles are wrong, HDR histograms | Show two systems with equal averages and very different p99 |
| 1.3 Tail at scale | Fan-out maths: with 100 back-ends each slow 1% of the time, 63% of requests see a slow one (Dean and Barroso, 2013) | Compute fan-out tails for 10, 100 and 1,000 back-ends |
| 1.4 Budgets | Latency budgets per hop from an SLO; performance budgets in CI | Split a 300 ms checkout SLO across 5 services |

**Check your understanding:** (1) Why does fan-out make tail latency the common case? (2) Why can't you average p99s from different hosts? (3) What should a latency budget include besides service time?

### Chapter 2 · Queueing theory for engineers (weeks 2–3)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Little's law | L = λW for any stable system; using it to sanity-check every dashboard | Verify Little's law on a real queue from your metrics |
| 2.2 Utilization and response time | Utilization law; M/M/1 response time R = S / (1 − ρ); the knee of the curve | Plot predicted vs measured latency for a single-worker service |
| 2.3 Variability | Kingman's approximation: waiting time grows with arrival and service variability as well as utilization | Show that halving service-time variance cuts queueing delay |
| 2.4 Multiple servers and pooling | M/M/c, why one shared queue beats many small ones, Erlang C | Size a worker pool for a target wait time |
| 2.5 Pool sizing | Connection and thread pools from Little's law; why bigger pools can be slower | Size a database pool from measured latency and throughput |
| 2.6 Open vs closed systems | Users who wait vs arrivals that don't; why the distinction changes load-test results | Run the same test as open and closed; compare |

**Check your understanding:** (1) At 90% utilization, how much longer is the average M/M/1 response time than at 50%? (2) Why can adding threads increase latency? (3) Why does pooling queues help?

### Chapter 3 · Scalability models (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Amdahl's law | Serial fraction limits speed-up | Estimate the serial fraction of a batch job from timings |
| 3.2 Universal Scalability Law | Contention (σ) and coherency (κ) terms; peak and retrograde scaling (Neil Gunther) | Fit USL to throughput at 1–32 instances; predict the peak |
| 3.3 Where coherency costs come from | Locks, cache invalidation, consensus, cross-shard queries | Find the coherency cost in a provided service |
| 3.4 Designing a scaling experiment | Fixed per-instance load, enough data points, repeat runs, finding which tier saturates first | Plan and run a 6-point scaling test with 3 repeats per point |

**Check your understanding:** (1) What makes throughput fall when you add nodes? (2) How many data points do you need to fit USL credibly? (3) Which architectural change reduces κ?

### Chapter 4 · Measuring correctly (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Coordinated omission | Closed-loop tools that wait hide latency; wrk2 and constant-arrival-rate executors (Gil Tene) | Measure the same service with wrk and wrk2; explain the gap |
| 4.2 Experimental hygiene | Warm-up, steady state, noisy neighbours, CPU frequency scaling, repeat runs | Show run-to-run variance; find its sources |
| 4.3 Comparing results | Bootstrap confidence intervals, Mann-Whitney U, effect size | Decide whether a "5% improvement" is real |
| 4.4 Benchmarks in CI | Regression thresholds, baselines, noise budgets | Fail CI on a 10% p95 regression without false alarms |

**Check your understanding:** (1) Why does a closed-loop load generator under-report latency during stalls? (2) Why is one run never enough? (3) When is a regression real?

### Chapter 5 · Load testing practice (weeks 6–7)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Test types | Smoke, load, stress, soak, spike, breakpoint; what each answers | Write a test plan with one question per test |
| 5.2 k6 in depth | Scenarios, `constant-arrival-rate` and `ramping-arrival-rate` executors, thresholds, checks, k6 2.x | Build a spike test that reaches 10× baseline in 60 s |
| 5.3 Other tools | Gatling, Locust, Vegeta; distributed load generation and its own bottlenecks | Prove your load generator is not the bottleneck |
| 5.4 Realistic workloads | Modelling traffic mix from production logs, think times, data variety, cache-busting | Derive a workload model from access logs |
| 5.5 Testing in production | Shadow traffic, traffic shifting to find limits (Meta's Kraken, OSDI 2016), safety limits | Design a Kraken-style test for one service with abort rules |

**Check your understanding:** (1) What does a soak test find that a load test does not? (2) Why must test data vary? (3) What makes testing in production acceptable?

### Chapter 6 · Profiling and bottleneck analysis (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 CPU | Flame graphs, `pprof`, async-profiler, continuous profiling (Pyroscope, Parca) | Find and fix a hot path; show the flame graph change |
| 6.2 Memory and GC | Allocation profiling, JVM G1 and ZGC, Go GC tuning, pauses in the tail | Cut p99 by reducing allocations |
| 6.3 Locks and concurrency | Contention profiling, lock-free vs sharded designs | Remove a global lock; measure throughput |
| 6.4 Databases | `EXPLAIN ANALYZE`, N+1 queries, indexes, connection limits | Fix the slowest 3 queries in a demo app |
| 6.5 Network | Keep-alive, connection reuse, TLS handshakes, TCP tuning with evidence | Show the cost of no keep-alive at 1,000 requests/s |

**Check your understanding:** (1) Why fix only the bottleneck? (2) How do GC pauses show up in percentiles? (3) Why can an index make writes slower enough to matter?

### Chapter 7 · Capacity planning (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Demand forecasting | Trend, seasonality (daily, weekly, festival), events (sales, cricket finals, tax deadlines); forecast intervals | Forecast 3 months with intervals from synthetic history |
| 7.2 Capacity models | Resource cost per request × demand + headroom; per-zone N+k; failover load | Build a spreadsheet model for a 3-tier service |
| 7.3 Supply | Quotas, procurement and lead times; GPUs as a scarce resource | Plan GPU capacity with a 6-week lead time |
| 7.4 Launch and event reviews | Capacity reviews for launches; pre-scaling; load tests as sign-off | Run a capacity review for a mock sale day |

**Check your understanding:** (1) Why plan with forecast intervals, not single numbers? (2) How much headroom do you need to survive a zone loss at peak? (3) Why must load tests reach beyond the forecast?

### Chapter 8 · Autoscaling (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 HPA | `desiredReplicas = ceil(currentReplicas × currentMetric / target)`, stabilization windows, scaling policies, custom and external metrics | Tune HPA so a spike is absorbed without oscillation |
| 8.2 Event-driven scaling | KEDA (CNCF graduated) on queue depth and lag; scale to zero and cold starts | Scale consumers on Kafka or RabbitMQ lag |
| 8.3 Vertical scaling | VPA recommendations; in-place pod resize (stable in Kubernetes 1.35) | Right-size 5 workloads from VPA data |
| 8.4 Nodes | Cluster Autoscaler vs Karpenter, provisioning latency, spot interruption | Measure time from pending pod to running on a new node |
| 8.5 Predictive and scheduled | Pre-scaling for known events; why reactive scaling is too slow for a 60-second spike | Combine scheduled and reactive scaling for a match start |

**Check your understanding:** (1) Why can autoscaling oscillate? (2) What is the real time to new capacity, end to end? (3) Why doesn't autoscaling fix a database bottleneck?

### Chapter 9 · Load balancing and the tail (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Algorithms | Round robin, least requests, power of two choices, consistent hashing | Simulate p99 under each with heterogeneous servers |
| 9.2 Prequal | Google's probing-based balancing on requests in flight and latency (NSDI 2024) | Implement a simplified version; compare with least requests |
| 9.3 Hedged and tied requests | Sending a backup request after the p95; cost vs tail gain (Tail at Scale) | Add hedging; measure p99 and extra load |
| 9.4 Timeouts as performance tools | Deadline-aware work, cancellation | Cancel abandoned work and measure capacity gained |

**Check your understanding:** (1) Why can balancing on CPU make tails worse? (2) When is hedging too expensive? (3) What does cancellation buy you at peak?

### Chapter 10 · Cost and performance (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Cost per unit | Cost per request, per transaction, per active user; the unit that matters to the business | Compute cost per 1,000 requests for your P2 system |
| 10.2 Right-sizing and architecture | Instance families, ARM (Swiggy reported Graviton nodes 10% cheaper), spot for batch, caching ROI | Benchmark the same service on x86 and ARM |
| 10.3 Efficiency vs headroom vs reliability | The three-way trade-off; why 90% utilization targets are dangerous | Write a utilization policy per tier |
| 10.4 Energy | Power and carbon estimates per workload (Kepler, CNCF sandbox) | Estimate energy per 1,000 requests |

**Check your understanding:** (1) Why can a cheaper instance raise cost per request? (2) What utilization target is safe for a latency-critical service, and why? (3) Who should own cost per request?

### Chapter 11 · AI inference and AI-assisted performance work (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 LLM serving metrics | Time to first token, time per output token, tokens per second, batching, KV-cache memory | Load-test a local model server; plot TTFT vs concurrency |
| 11.2 Capacity in tokens | Planning GPU capacity from token demand, not request counts ([CLD404](../../../cloud_engineering/year_4/CLD404_ai_infrastructure_in_the_cloud_gpus_inference/README.md)) | Build a token-based capacity model |
| 11.3 AI suggestions under test | Assistant-suggested optimisations measured with the Chapter 4 methods | Test 5 AI suggestions; keep only the proven ones |
| 11.4 Cost per AI request | Smaller or quantised models, batching vs latency, prompt caching; cost per 1,000 requests at a fixed quality bar | Compare two model sizes on cost and latency at the same eval score |

**Check your understanding:** (1) Why is GPU utilization a poor capacity metric for LLM serving? (2) What changes when requests have very different output lengths? (3) How do you decide whether an AI-suggested optimisation is real?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Percentiles and fan-out | Fan-out tail report |
| 2 | 2 | Lab 2 · Little's law in the wild | Verified dashboard |
| 3 | 2 | Lab 3 · Queue model vs reality | P1 starts |
| 4 | 3 | Lab 4 · USL fit | **P1 due** |
| 5 | 4 | Lab 5 · Coordinated omission | wrk vs wrk2 report |
| 6 | 5 | Lab 6 · k6 scenarios | Test plan; P2 starts |
| 7 | 5 | Workload modelling | Mid-term (AI off) |
| 8 | 6 | Lab 7 · Profiling clinic | Before/after evidence |
| 9 | 7 | Lab 8 · Capacity model | Model spreadsheet |
| 10 | 8 | Lab 9 · Autoscaling tuning | **P2 due** |
| 11 | 9 | Load-balancer simulation | p99 comparison |
| 12 | 10 | Lab 10 · Cost per request, x86 vs ARM | Cost report; P3 design review |
| 13 | 11 | LLM serving test | TTFT curves |
| 14 | — | P3 event simulation | **P3 due** |
| 15 | Review | Exam and oral | Final |

## Working with AI in this course

- **Use AI for:** drafting k6, Gatling or Locust scripts; writing simulation code for queueing models; explaining profiler output; suggesting candidate optimisations to test. Named tools: Claude Code, GitHub Copilot, Cursor, ChatGPT.
- **Do without AI (drills):** every queueing and USL calculation in the mid-term and exam; choosing an open or closed model for a test; reading a flame graph and naming the bottleneck; the capacity review.
- **Verify AI output by:** checking that load scripts use arrival-rate executors when you mean arrival rates; checking for coordinated omission; repeating runs and computing confidence intervals; profiling before and after every suggested optimisation; checking capacity models against Little's law.
- **Where AI still fails here (show it):** ask for "a load test of 1,000 requests per second" and see whether it produces a closed-loop test with 1,000 virtual users, which is not the same thing. Ask it to optimise a slow endpoint without a profile and count how many suggestions target code that is not on the hot path. Log both in Lab 6 and Lab 7.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs 1–10 | 25% |
| Projects P1 / P2 / P3 | 5% / 15% / 25% |
| Mid-term (AI off) | 10% |
| Final exam (calculation and design, AI off) + oral | 20% |

**Mastery gate.** You pass when you can, without AI help: (1) predict the p95 latency of a single-queue service at a new load level within 25% from measured service time and arrival rate, and explain where the model breaks; (2) design, run and interpret a coordinated-omission-free load test that finds a service's breaking point, with confidence intervals; (3) produce a capacity plan for a stated peak event (forecast with intervals, per-zone headroom, autoscaling and pre-scaling, cost) that two examiners accept.

## Industry reality

Performance and capacity work sits inside SRE, platform and backend roles, and as a specialist title (performance engineer, capacity planner) in large companies. Interviews test it through system design ("how many servers for 50,000 requests per second?") and debugging ("p99 doubled after a deploy"). Public sources to study include Google's "The Tail at Scale", Meta's Kraken and Google's Autopilot and Prequal papers, Disney+ Hotstar's engineering posts on scaling for live sport, and Swiggy's account of moving Kubernetes workloads to Graviton.

**Interview questions from this course**

1. *Estimate how many instances we need for 50,000 requests/s at p99 < 200 ms.* Strong answer: measure per-request service time and resource cost; Little's law for concurrency; utilization target from queueing (not 100%); per-zone N+1 or N+2 headroom; validate with a load test; cost estimate.
2. *Our p99 doubled after a deploy but the average didn't change. What do you do?* Strong answer: compare histograms and traces before/after; check GC, lock contention, new dependency calls, cache hit rate, connection pool changes; profile; canary comparison; remember fan-out amplifies tails.
3. *How do you load-test correctly?* Strong answer: question-first plan; open model with arrival-rate executors for internet traffic; realistic workload mix and data; warm-up and steady state; coordinated-omission-free tools; prove the generator is not the bottleneck; repeat runs with confidence intervals; thresholds tied to SLOs.
4. *Design autoscaling for a cricket-match traffic spike.* Strong answer: reactive scaling is too slow for a sudden spike; scheduled pre-scaling from the match schedule; warm pools and node headroom; HPA tuned with stabilization; KEDA for queues; database and cache capacity planned separately; load tests at 10× baseline; graceful degradation if exceeded.
5. *What is Little's law and how have you used it?* Strong answer: L = λW, holds for stable systems regardless of distribution; examples: sizing connection pools, checking dashboard consistency, estimating concurrency from throughput and latency.

## Resources (free first)

- **Papers and texts:** Dean and Barroso, [The Tail at Scale](https://research.google/pubs/the-tail-at-scale/) (CACM 2013); Veeraraghavan et al., [Kraken](https://www.usenix.org/conference/osdi16/technical-sessions/presentation/veeraraghavan) (OSDI 2016); Rzadca et al., [Autopilot](https://research.google/pubs/autopilot-workload-autoscaling-at-google-scale/) (EuroSys 2020); Wydrowski et al., [Load is not what you should balance: Introducing Prequal](https://www.usenix.org/conference/nsdi24/presentation/wydrowski) (NSDI 2024); MIT OpenCourseWare, [6.262 Discrete Stochastic Processes](https://ocw.mit.edu/courses/6-262-discrete-stochastic-processes-spring-2011/) (queueing and Little's theorem); Gil Tene, [How NOT to Measure Latency](https://www.infoq.com/presentations/latency-response-time/); Google SRE workbook, [Managing Load](https://sre.google/workbook/managing-load/); Marc Brooker's [blog](https://brooker.co.za/blog/) on queueing and load in distributed systems.
- **Tools:** [k6](https://grafana.com/docs/k6/latest/), [Gatling](https://docs.gatling.io/), [Locust](https://docs.locust.io/), [wrk2](https://github.com/giltene/wrk2), [Vegeta](https://github.com/tsenart/vegeta), [HdrHistogram](https://hdrhistogram.github.io/HdrHistogram/), [FlameGraph](https://github.com/brendangregg/FlameGraph), [Pyroscope](https://grafana.com/docs/pyroscope/latest/), [KEDA](https://keda.sh/docs/), [Karpenter](https://karpenter.sh/docs/), [Kubernetes autoscaling](https://kubernetes.io/docs/concepts/workloads/autoscaling/) and [HPA algorithm](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/), [VPA](https://github.com/kubernetes/autoscaler/tree/master/vertical-pod-autoscaler), [OpenCost](https://github.com/opencost/opencost).
- **Case studies:** [Swiggy's Graviton migration](https://bytes.swiggy.com/how-swiggy-migrated-its-k8s-workload-to-graviton-d2643bbc7871); [Disney+ Hotstar: scaling infrastructure for millions](https://blog.hotstar.com/scaling-infrastructure-for-millions-from-challenges-to-triumphs-part-1-6099141a99ef).
- **Practice locally:** kind with KEDA and the metrics server; k6 and wrk2 against local services; a small local model server (Ollama or vLLM on CPU or a free cloud notebook GPU) for Chapter 11.
- **Paid, worth it:** Mor Harchol-Balter, *Performance Modeling and Design of Computer Systems* (Cambridge, 2013); Brendan Gregg, *Systems Performance*, 2nd ed. (2020); Neil Gunther, *Guerrilla Capacity Planning* (Springer, 2007).

## Sources

All checked 12 Oct 2026.
- MediaNama, [NPCI circular coverage](https://www.medianama.com/2025/05/223-npci-banks-balance-upi-transaction-guidelines/) (May 2025: peak hours 10 am–1 pm and 5–9:30 pm; limits effective 1 Aug 2025).
- Kubernetes, [in-place pod resize stable in v1.35](https://kubernetes.io/blog/2025/12/19/kubernetes-v1-35-in-place-pod-resize-ga/) (Dec 2025) and [HPA algorithm](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/).
- CNCF maturity (KEDA graduated 22 Aug 2023; Kepler sandbox) from the [CNCF landscape](https://github.com/cncf/landscape) data file; k6 v2.3.0 (Sep 2026) from GitHub releases.
- Swiggy Bytes, [Graviton migration](https://bytes.swiggy.com/how-swiggy-migrated-its-k8s-workload-to-graviton-d2643bbc7871) (10% cheaper than comparable x86, as cited in [CLD303](../../../cloud_engineering/year_3/CLD303_containers_and_kubernetes/README.md)).
- Papers as listed in Resources (Tail at Scale 2013; Kraken OSDI 2016; Autopilot EuroSys 2020; Prequal NSDI 2024).

_Last reviewed: 2026-10_
