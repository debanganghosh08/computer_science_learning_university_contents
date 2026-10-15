# QAE303 · Labs and projects

Load tests run **only against systems you own and host**: your laptop, a local Kubernetes cluster (kind or k3d), or a cloud account you pay for, with spending alerts set. Never point load at a public website or a demo you do not control; that is indistinguishable from a denial-of-service attack. Every result reports the workload model (open or closed), the generator's own CPU and network use, the number of runs and the spread between them. Percentiles come from histograms, never from averaging per-run percentiles.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Queueing by measurement | Predict queue length and latency at 3 arrival rates for a toy single-threaded server using Little's law; measure them | Predictions, measurements, an explanation of every gap | 3 h |
| 2 · Coordinated omission | Measure a server with a planted 2-second stall using a closed-loop tool and an open model (k6 `constant-arrival-rate` or wrk2) | Both histograms, the p99 difference, a one-paragraph explanation | 3 h |
| 3 · Workload model from logs | Turn a week of anonymised access logs into arrival rates, transaction mix, think times and key distributions | Model document with every assumption and a sensitivity table | 4 h |
| 4 · k6 scenarios and thresholds | Mixed open and closed scenarios, parametrised users, SLO thresholds that fail CI | Script, CI run with a failing and a passing threshold, exit codes | 4 h |
| 5 · Dashboards, browser and fault injection | Stream a run to Prometheus and Grafana; add 2 k6 browser users; inject 300 ms latency into one dependency with `xk6-disruptor` | Dashboard JSON, Web Vitals before and after injection, a short reading of the results | 5 h |
| 6 · Four tools, one journey | Port one 4-step journey to JMeter, Gatling and Locust | Scripts, memory per 1,000 users, p95/p99 per tool at the same arrival rate, reasons for differences | 6 h |
| 7 · Stress, spike and soak | Ramp to the breaking point; 10× spike with cold and warm caches; 4-hour soak | Knee and breaking point with the first saturated resource; spike comparison; memory and file-handle plots | 6 h |
| 8 · Profiling and flame graphs | Profile a service under load (`perf`, async-profiler, py-spy or pprof); fix the hottest path | Flame graphs before and after; p95 and CPU per request before and after across 5 runs | 4 h |
| 9 · Database and traces | Find an N+1 query and a connection-pool limit using OpenTelemetry traces and `EXPLAIN ANALYZE` | Trace screenshots, query plans, the fix, before/after p95 | 4 h |
| 10 · Overload and admission control | Trigger a retry storm; add retry budgets, jittered backoff and a token-bucket admission gate | Goodput vs offered load chart with and without protection | 4 h |

## Projects

### P1 · Honest baseline for a small service (L1, ~6 hours)

**Real-world inspiration:** the first performance baseline a team needs before anyone can say a change made things slower.

**What to build:** run [Grafana QuickPizza](https://github.com/grafana/quickpizza) locally. Write a smoke test and an average-load test in k6 with an open workload model, realistic think times and parametrised users, with thresholds for the SLOs you write.

**Acceptance criteria:**
- SLOs written before testing (for example p95 and p99 per endpoint, error rate) with a reason for each number.
- Load generator CPU below 70% throughout every run (evidence attached).
- 5 repeated runs: p95 per endpoint varies by less than 10% between runs, or the report explains the noise source and how it was reduced.
- Report shows latency histograms or heat maps, not only summary numbers, and states the workload model and every assumption.
- The test runs in CI and fails when a threshold is breached (demonstrated with an artificially tightened threshold).

**Stretch goals:** reproduce the same baseline in Locust and explain any difference in reported percentiles.

**What it proves to an employer:** you measure performance correctly and can tell noise from signal.

### P2 · Festive-sale load model for a microservices shop (L2, ~15 hours)

**Real-world inspiration:** Indian festive-season sales, where traffic at sale start can be many times a normal day. The traffic shape and numbers below are an **illustrative scenario**; no company's internal figures are used.

**What to build:** deploy [Online Boutique](https://github.com/GoogleCloudPlatform/microservices-demo) on a local kind or k3d cluster with Prometheus, Grafana and OpenTelemetry tracing. Build a workload model from the provided synthetic access logs (browse, search, product view, add to cart, checkout; hot products following a Zipf distribution). Run average load, a 10× spike at "sale start", a stress test to the breaking point and a 2-hour soak.

**Acceptance criteria:**
- Workload model document with arrival rates, transaction mix, data distribution, peak factor and a sensitivity analysis on the two most uncertain assumptions.
- SLOs as k6 thresholds: for example browse p95 < 300 ms, checkout p99 < 1 s, error rate < 0.5% at the target arrival rate (adjust to your hardware, but fix them before testing).
- The first saturated resource at the breaking point is named with USE or RED evidence and a trace of a slow request.
- One bottleneck fixed (configuration, resources, caching or code) with before/after results across 3 runs each and a statistical comparison.
- Spike results compare cold and warm caches and report time to recover to SLO after the spike.
- A one-page readiness note: capacity at SLO, headroom, risks, recommendation.

**Stretch goals:** add an autoscaler and measure its reaction lag during the spike; inject dependency latency with `xk6-disruptor` and show how the shop degrades.

**What it proves to an employer:** you can turn messy traffic data into a defensible test, find what breaks first, and explain it to a release manager.

### P3 · Surge readiness and capacity plan for a booking service (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** Tatkal openings, where demand arrives at a fixed second. IRCTC's public record is 28,434 tickets booked in one minute (12 November 2022); internal designs of IRCTC are not public, so the service and all numbers here are an **illustrative scenario** that uses the public record only as a scale anchor.

**What to build:** a booking service (your own or the instructor's starter) with seat inventory per train, class and date, holds with expiry, a stubbed payment step with realistic latency, and PostgreSQL. Then:
1. A workload model for a 10-second opening burst including retries and refreshes from impatient users.
2. Spike, stress, soak and breakpoint tests in k6 (open models), with SLOs per step.
3. Diagnosis of the first two bottlenecks with profiles, traces and database plans, and fixes.
4. Overload protection: an admission gate (token bucket or waiting room), retry budgets and graceful degradation (for example a read-only seat-availability page from cache).
5. A CI performance gate that compares each pull request against a stored baseline.
6. A capacity plan and an executive report.

**Acceptance criteria:**
- **Correctness under load:** zero oversold seats and zero double bookings across all runs, verified by a database invariant check after each run (performance results without this check do not count).
- **Goodput:** with protection on, successful bookings per second at 5× the design peak stay at or above 90% of goodput at 1× peak; without protection, the report shows the collapse.
- **Latency:** p99 for "seat availability" under 500 ms and p95 for "book" under 2 s at design peak (or targets you justify in advance for your hardware).
- **Regression gate:** catches a planted 15% p95 regression in the booking path and stays green on 10 unchanged runs.
- **Capacity plan:** replicas and database size for 2× design peak, headroom, autoscaling lag, cost per 1,000 bookings at your cloud provider's list prices (cite the price page and date).
- **Report:** a one-page summary a non-engineer can act on, plus a technical appendix with raw histograms and the generator's resource use.

**Stretch goals:** run a production-style "safe load test" design with abort criteria and synthetic accounts; fit the Universal Scalability Law to your replica tests and predict the next breaking point, then check it.

**What it proves to an employer:** you can prepare a system for its biggest day with evidence, protect correctness under load, and give leaders a capacity number with a stated confidence.

## Feeds into

- [QAE304 Testing in CI/CD and Test Infrastructure](../QAE304_testing_in_ci_cd_and_test_infrastructure/README.md): P3's regression gate joins the pipeline's quality gates.
- [QAE403 Security and Accessibility Testing](../../year_4/QAE403_security_and_accessibility_testing/README.md) (catalog follow-on): running scanners and audits as pipeline stages with budgets.
- [QAE404 Quality Engineering Leadership](../../year_4/QAE404_quality_engineering_leadership_and_metrics/README.md): readiness reports and SLO-based release decisions.
- [OPS404 Performance and Capacity Engineering](../../../devops_sre_platform_engineering/year_4/OPS404_performance_and_capacity_engineering/README.md): deeper capacity work, as an elective.
- [QAE flagship industry project](../../../../06_career_and_market_readiness/05_industry_projects/QAE_software_quality_test_engineering.md): P2's workload model is its load-testing layer.
