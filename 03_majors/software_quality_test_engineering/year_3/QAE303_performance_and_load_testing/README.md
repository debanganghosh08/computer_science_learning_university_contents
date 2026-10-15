# QAE303 · Performance and Load Testing

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 5 | 4 (≈ 120 hours) | L2 → L3 | [CS205](../../../../02_year_2_core_computer_science/semester_3/CS205_software_engineering_i_design_testing/README.md); uses [CS203](../../../../02_year_2_core_computer_science/semester_3/CS203_operating_systems/README.md), [CS204](../../../../02_year_2_core_computer_science/semester_3/CS204_computer_networks/README.md), [FND116](../../../../01_year_1_foundations/semester_2/FND116_probability_and_statistics_i/README.md) | [QAE403](../../year_4/QAE403_security_and_accessibility_testing/README.md) (catalog prerequisite); feeds [QAE304](../QAE304_testing_in_ci_cd_and_test_infrastructure/README.md), [OPS404](../../../devops_sre_platform_engineering/year_4/OPS404_performance_and_capacity_engineering/README.md) |

Part of the [Software Quality and Test Engineering major](../../README.md). Developers meet benchmarking in [SWE305](../../../software_engineering/year_3/SWE305_concurrency_and_performance_engineering/README.md); this course is the tester's side: modelling real traffic, running load against whole systems, reading the results correctly and finding the bottleneck before users do.

## Why this course matters now

Peak events define reputations in India: Tatkal ticket openings (IRCTC's public record is 28,434 tickets booked in one minute, on 12 November 2022), festive e-commerce sales, IPO days at brokers and exam-result days. A system that is fine at normal traffic can fail in seconds under a burst. Tools are mature and free: Grafana k6 reached version 2.0 on 11 May 2026 (2.3 by October), alongside JMeter 5.6, Gatling 3.16 and Locust 2.46. AI assistants now write a load script from a HAR file in seconds, but the hard parts are still human: choosing an open or closed workload model, avoiding coordinated omission, reading p99 rather than averages, noticing that the load generator itself is the bottleneck, and turning a flame graph into a fix. Google's "The Tail at Scale" showed why tail latency dominates user experience in fan-out systems; this course makes you the person who measures it honestly.

## Learning outcomes

By the end you can:

1. **Explain** latency, throughput, utilisation and queueing with Little's law and the utilisation law, and **predict** where a system will saturate.
2. **Measure** latency correctly with histograms and percentiles, open workload models and coordinated-omission-safe tools, and **report** results with run-to-run variance.
3. **Build** a workload model from logs or analytics (arrival rates, transaction mix, data distributions, peak factors) and **defend** its assumptions.
4. **Write** load tests in k6 (scenarios, executors, thresholds) and **read** equivalent JMeter, Gatling and Locust scripts.
5. **Design and run** smoke, average-load, stress, spike, soak and breakpoint tests, each with acceptance criteria tied to SLOs.
6. **Find** bottlenecks with the USE and RED methods, profilers and flame graphs, traces and database plans, and **verify** a fix with before/after evidence.
7. **Plan** capacity for a peak event, including headroom, autoscaling lag, overload protection and cost per request.
8. **Gate** performance in CI with budgets and baselines that detect a planted regression without false alarms.

## Chapters and lessons

### Chapter 1 · Why systems get slow (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Latency and throughput | Service time vs waiting time; throughput ceilings; the hockey-stick curve | Plot latency against load for a single-threaded toy server |
| 1.2 Queueing basics | Little's law (L = λW), utilisation law, why latency explodes above ~70–80% utilisation | Predict queue length at 3 arrival rates; verify by measurement |
| 1.3 Tails | Percentiles; "The Tail at Scale" (Dean and Barroso, 2013): fan-out multiplies the chance of hitting a slow server | Simulate fan-out of 1, 10 and 100 calls; compare p99 of the whole request |
| 1.4 SLIs and SLOs | Latency and availability SLIs, SLO targets, error budgets as acceptance criteria | Write SLOs for browse, search and checkout of an illustrative store |

**Check your understanding:** Why does the average hide the problem users complain about? Why does a service at 95% CPU have much worse latency than at 70%, even if throughput is similar? Why does p99 of a 100-way fan-out depend on p99.99 of each backend?

### Chapter 2 · Measurement done right (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Histograms | HdrHistogram, bucket error, merging histograms across generators; never average percentiles | Merge results from 3 load generators correctly and incorrectly; compare |
| 2.2 Coordinated omission | Closed-loop tools that wait for slow responses under-report latency (Gil Tene; wrk2) | Measure a server with a stall using a closed and an open model |
| 2.3 Open vs closed models | Arrival-rate executors vs virtual users with think time; which real systems are open | Model the same test both ways in k6; explain the difference in p99 |
| 2.4 Experimental hygiene | Warm-up, JIT and cache effects, generator saturation (CPU, ports, bandwidth), clock sources, repeated runs and confidence intervals | Prove your generator is not the bottleneck; report 5 runs with spread |

**Check your understanding:** Why does a closed-model tool report a fast p99 during a 2-second server stall? When is a closed model the right choice? How do you show a reader that a 5% difference between two runs is real?

### Chapter 3 · Workload modelling (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 From logs to a model | Arrival rates by minute, transaction mix, session paths, user think times | Derive a model from a provided week of anonymised access logs |
| 3.2 Data distributions | Hot keys and Zipf distributions, cache-hit ratios, realistic payload sizes, unique vs repeated users | Show how a uniform key choice hides a cache bottleneck |
| 3.3 Peaks and bursts | Peak factors, flash bursts at a fixed time (ticket openings, sale starts), retries from impatient users | Model a 10-second opening burst anchored on IRCTC's public per-minute record (illustrative) |
| 3.4 Assumptions as risks | Documenting every assumption; sensitivity analysis | Rerun with ±30% on the two most uncertain assumptions |

**Check your understanding:** Why does testing with a single user account give misleading cache results? What happens to load when the app is slow and users press refresh? Which assumption in your model would change the answer most?

### Chapter 4 · k6 in depth (weeks 4–5)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Scripts and checks | k6 JavaScript API, checks vs thresholds, tags and groups, `SharedArray` data | Script a 4-step user journey with parametrised users |
| 4.2 Scenarios and executors | `constant-arrival-rate`, `ramping-arrival-rate`, `ramping-vus`; multiple scenarios in one run | Mix browse (open) and admin (closed) traffic in one test |
| 4.3 Thresholds as acceptance | `p(95)<300`, error-rate thresholds, abort-on-fail; exit codes for CI | Fail a run on an SLO breach; read the exit code in CI |
| 4.4 Outputs and dashboards | Built-in web dashboard (core binary since k6 2.0), Prometheus remote write, Grafana | Stream a run to Grafana; build a latency heat map |
| 4.5 Browser and extensions | k6 browser module and Web Vitals (INP, LCP, CLS); `xk6-disruptor` for fault injection; changes in 2.0 (removed commands, module path) | Combine protocol load with 2 browser users; inject latency into a dependency |

**Check your understanding:** Why should SLO thresholds, not checks, fail a CI run? Why add a few browser users to a protocol-level test? What did k6 2.0 remove that old tutorials still use?

### Chapter 5 · JMeter, Gatling and Locust (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 JMeter | Thread groups, samplers, timers, listeners in non-GUI mode, the arrivals thread group | Port your k6 journey to JMeter; run headless |
| 5.2 Gatling | Scenario DSL in the Java SDK (also used from Kotlin and Scala) or the JavaScript/TypeScript SDK, injection profiles (open and closed), HTML reports | Port to Gatling with an open injection profile |
| 5.3 Locust | Python user classes, weights, distributed workers | Port to Locust; run 1 master and 3 workers |
| 5.4 Choosing | Language fit, protocol support, resource cost per virtual user, reporting, team skills | Compare memory per 1,000 users and results across all four tools |

**Check your understanding:** Why might two tools report different p99 for the same server and load? When would you choose Locust over k6? What makes a tool's report trustworthy?

### Chapter 6 · Test types and acceptance criteria (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Smoke and average load | The question each answers; baselines | Baseline your target at expected load |
| 6.2 Stress and breakpoint | Finding the knee and the breaking point; what breaks first | Ramp until SLO breach; name the first saturated resource |
| 6.3 Spike | Sudden 10× bursts; autoscaling lag; cold caches and connection storms | Spike test with and without warm caches |
| 6.4 Soak | Memory leaks, connection-pool exhaustion, log and disk growth over hours | 4-hour soak; plot memory and file handles |

**Check your understanding:** Why does a spike test fail where a stress test at the same peak passes? What does a soak test find that no short test can? How do you write pass/fail criteria for a breakpoint test?

### Chapter 7 · Finding bottlenecks (weeks 8–9)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Methods | USE (utilisation, saturation, errors per resource) and RED (rate, errors, duration per service) | USE checklist for one host, RED dashboard for 3 services |
| 7.2 CPU profiling | Sampling profilers (`perf`, async-profiler, py-spy, Go pprof), flame graphs, continuous profiling (Pyroscope) | Find the hottest function under load; fix it; re-measure |
| 7.3 Waiting, not computing | Off-CPU time, lock contention, GC pauses, thread-pool and connection-pool limits | Find a pool-exhaustion bottleneck from traces and metrics |
| 7.4 Databases | `EXPLAIN ANALYZE`, missing indexes, N+1 queries, lock waits, connection limits | Fix an N+1 under load; show the before/after p95 |
| 7.5 Distributed traces | OpenTelemetry spans, finding the slow hop, correlating load-test IDs with traces | Tag load requests; follow the slowest 1% in traces |

**Check your understanding:** Why can CPU be at 30% while latency is terrible? Why tag load-test traffic? What evidence proves that your fix, and not noise, improved p95?

### Chapter 8 · Capacity, overload and resilience (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Scalability models | Amdahl's law; Gunther's Universal Scalability Law (contention and coherence) | Fit USL to throughput at 1, 2, 4 and 8 replicas |
| 8.2 Capacity planning | Peak forecast, headroom, autoscaling lag, warm pools, cost per 1,000 requests | Capacity plan for a sale day with a 3× safety margin |
| 8.3 Overload behaviour | Load shedding, backpressure, rate limits, queues with deadlines, retry storms (Google SRE book) | Show a retry storm; fix it with budgets and jittered backoff |
| 8.4 Graceful degradation | Waiting rooms, feature kill switches, serving stale data | Add a token-bucket admission gate; measure goodput under 5× load |

**Check your understanding:** Why can adding replicas reduce throughput? Why is "autoscaling will handle it" not a capacity plan? What is goodput, and why is it the right measure under overload?

### Chapter 9 · Frontend and mobile performance (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Core Web Vitals | LCP, INP (replaced FID in March 2024), CLS; lab vs field (CrUX) | Measure 3 pages with Lighthouse and compare with field data |
| 9.2 Constrained devices | CPU and network throttling, low-end Android realities (detailed in QAE305) | Run Lighthouse with 4× CPU slowdown and slow 4G |
| 9.3 Backend-frontend links | How API latency shows up in INP and LCP; caching and CDNs | Inject 500 ms API latency; measure Web Vitals change |

**Check your understanding:** Why can a page pass Lighthouse on your laptop and fail for real users? Which backend change improves LCP most? Why is INP harder to test in a lab?

### Chapter 10 · Performance in CI/CD (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 What belongs in CI | Micro-benchmarks, short load smoke tests, budgets; full load tests on schedule | Design a per-commit, nightly and pre-release performance plan |
| 10.2 Noise | Shared runners, CPU frequency scaling, neighbours; dedicated runners; repeated runs | Measure the noise floor of your CI runner over 20 runs |
| 10.3 Baselines and regression detection | Relative thresholds against a stored baseline, statistical tests, change-point detection over history | Detect a planted 15% regression without false alarms on 10 clean runs |
| 10.4 Reporting | Trend dashboards, annotated releases, performance review in pull requests | Comment p95 deltas on every pull request automatically |

**Check your understanding:** Why do absolute thresholds on shared runners cause false alarms? What is the smallest regression your setup can detect, and how do you know? Which tests belong nightly rather than per commit?

### Chapter 11 · Peak-event readiness and AI (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Readiness programmes | Load test calendar, game days, freeze windows, runbooks, kill switches (illustrative sale-day plan) | Write the readiness plan for P3 |
| 11.2 Testing in production | Shadow traffic, synthetic transactions, safe load tests on production with abort criteria | Design abort criteria for a production load test |
| 11.3 AI in performance work | LLMs that write k6 scripts from HAR files and summarise results; failure modes | Generate a script with AI; audit it for model, think time, data and API errors |
| 11.4 Reporting to leaders | One-page result: capacity, risks, recommendation, confidence | Present P3 results in 5 minutes |

**Check your understanding:** Why are production load tests sometimes safer than staging tests? What does an AI-written load script usually get wrong? What confidence statement would you put on a capacity number?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Queueing by measurement | — |
| 2 | 2 | Lab 2 · Coordinated omission | — |
| 3 | 3 | Lab 3 · Workload model from logs | Model document |
| 4 | 4 | Lab 4 · k6 scenarios and thresholds | **P1 due** |
| 5 | 4 | Lab 5 · Dashboards, browser and fault injection | — |
| 6 | 5 | Lab 6 · Four tools, one journey | — |
| 7 | 6 | Lab 7 · Stress, spike and soak | Mid-term (AI off) |
| 8 | 7 | Lab 8 · Profiling and flame graphs | — |
| 9 | 7 | Lab 9 · Database and traces | **P2 due** |
| 10 | 8 | Lab 10 · Overload and admission control | — |
| 11 | 9 | Web Vitals under throttling | — |
| 12 | 10 | CI performance gate | Gate demo |
| 13 | 11 | P3 | Readiness plan |
| 14 | 11 | P3 | **P3 due** |
| 15 | Review | P3 presentation | Final exam (AI off): read and diagnose results |

## Working with AI in this course

- **Use AI for:** converting HAR recordings or Postman collections into k6 or Gatling scripts; writing data generators; drafting Grafana panels and PromQL; summarising long result files; explaining profiler output. Tools: Claude, ChatGPT, Gemini, Claude Code, Codex, Copilot.
- **Do without AI (drills):** Little's law and utilisation predictions; the workload model; choosing open vs closed; reading histograms and flame graphs; the mid-term and final, which give you raw results to diagnose.
- **Verify AI output by:** checking the executor and model type in every script; removing `sleep`-driven pacing in open-model tests; confirming every API call exists in the k6 or tool version you run (2.0 removed several commands and modules); checking generator CPU; comparing AI result summaries against the raw histograms.
- **Where AI still fails here (show it):** in Lab 2 and Lab 11.3 you log real examples: closed-loop scripts presented as "1,000 requests per second", averaged percentiles, invented k6 options, think times copied from tutorials, and conclusions about the server drawn from a saturated generator.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 20% |
| P1, P2, P3 | 10%, 20%, 25% |
| Mid-term (AI off) | 5% |
| Final exam (AI off) + P3 presentation | 20% |

**Mastery gate.** You pass when you can: (1) given an unfamiliar service and a week of access logs, deliver within one day a documented workload model and an open-model k6 test with SLO thresholds whose p95 varies less than 10% across 5 runs; (2) with AI off, look at a provided set of results (histograms, USE metrics, a flame graph, traces) and name the bottleneck and the evidence for it within 45 minutes; (3) show a CI gate that catches a planted 15% p95 regression and stays green on 10 clean runs.

## Industry reality

Performance engineers work in product companies with peak-driven traffic, in banks and brokers, and in services firms that run performance-testing engagements (see the [market page](../../../../06_career_and_market_readiness/01_market_map/roles/QAE_software_quality_test_engineering.md)). Public material to study: Google's "The Tail at Scale" and the SRE book chapters on overload and cascading failures; the k6, Gatling, JMeter and Locust documentation; IRCTC's published booking record as a scale anchor (internal designs are not public).

**Interview questions from this course**

1. *Our average latency is 120 ms but users complain. What do you look at?* Strong answer: percentiles and histograms, not averages; tail by endpoint and user segment; fan-out; coordinated omission in the measurement; saturation signals; field data vs lab data.
2. *Design a load test for a flash sale that opens at 12:00.* Strong answer: open model with a burst arrival profile; realistic mix and hot items; retries and refreshes; warm vs cold caches; SLOs for browse and checkout; abort criteria; generator capacity; what happens at overload (waiting room, shedding).
3. *Explain coordinated omission.* Strong answer: a closed-loop client waits for slow responses and stops sending, so the stall is under-sampled; fix with open models or correction (wrk2, HdrHistogram expected-interval correction); give a numeric example.
4. *Throughput stopped increasing at 4 replicas. Why?* Strong answer: a shared bottleneck (database, lock, connection pool, downstream limit); contention and coherence (USL); how to prove it with USE metrics and traces.
5. *How would you stop performance regressions reaching production?* Strong answer: budgets and baselines in CI with noise control, nightly full tests, change-point detection on trends, production SLO monitoring and canaries, ownership of regressions.

## Resources (free first)

- **Concepts:** Dean and Barroso, "The Tail at Scale" (CACM 2013) — https://research.google/pubs/the-tail-at-scale/ ; Google SRE book, "Handling Overload" — https://sre.google/sre-book/handling-overload/ and "Addressing Cascading Failures" — https://sre.google/sre-book/addressing-cascading-failures/ ; Neil Gunther, Universal Scalability Law — https://www.perfdynamics.com/Manifesto/USLscalability.html ; Tom Wilkie, the RED method — https://grafana.com/blog/2018/08/02/the-red-method-how-to-instrument-your-services/
- **Measurement:** HdrHistogram — https://hdrhistogram.github.io/HdrHistogram/ ; wrk2 (README explains coordinated omission) — https://github.com/giltene/wrk2 ; k6 open vs closed models — https://grafana.com/docs/k6/latest/using-k6/scenarios/concepts/open-vs-closed/
- **Tools:** k6 docs — https://grafana.com/docs/k6/latest/ (test types https://grafana.com/docs/k6/latest/testing-guides/test-types/ , browser https://grafana.com/docs/k6/latest/using-k6-browser/ ) ; xk6-disruptor — https://github.com/grafana/xk6-disruptor ; JMeter — https://jmeter.apache.org/usermanual/index.html ; Gatling — https://docs.gatling.io/ ; Locust — https://docs.locust.io/en/stable/
- **Profiling:** FlameGraph — https://github.com/brendangregg/FlameGraph ; async-profiler — https://github.com/async-profiler/async-profiler ; py-spy — https://github.com/benfred/py-spy ; Grafana Pyroscope — https://grafana.com/oss/pyroscope/ ; PostgreSQL `EXPLAIN` — https://www.postgresql.org/docs/current/using-explain.html ; OpenTelemetry — https://opentelemetry.io/docs/
- **Frontend:** web.dev Web Vitals — https://web.dev/articles/vitals ; Chrome UX Report — https://developer.chrome.com/docs/crux
- **Practice targets:** Grafana QuickPizza — https://github.com/grafana/quickpizza ; Online Boutique — https://github.com/GoogleCloudPlatform/microservices-demo
- **Paid, optional:** Brendan Gregg, *Systems Performance* (2nd ed.).

## Sources

All checked 12 Oct 2026.

- IRCTC, Internet Ticketing page (28,434 tickets per minute on 12 Nov 2022) — https://www.irctc.com/internet-ticketing.php
- Grafana k6 v2.0.0 release notes (11 May 2026) — https://github.com/grafana/k6/releases/tag/v2.0.0 ; latest release v2.3.0 (GitHub releases, 12 Oct 2026) — https://github.com/grafana/k6/releases
- Latest releases on 12 Oct 2026: JMeter 5.6.3 — https://github.com/apache/jmeter/releases ; Gatling 3.16.0 — https://github.com/gatling/gatling/releases ; Locust 2.46.7 (PyPI) — https://pypi.org/project/locust/
- Dean and Barroso, "The Tail at Scale", CACM 56(2), 2013 — https://research.google/pubs/the-tail-at-scale/
- web.dev, "Interaction to Next Paint becomes a Core Web Vital on March 12" — https://web.dev/blog/inp-cwv-march-12

_Last reviewed: 2026-10_
