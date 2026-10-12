# SWE305 · Labs and projects

You need a Linux machine (native or a VM with `perf` access) and access to one ARM machine for Lab 5 (a cloud ARM instance, a Raspberry Pi 4/5 or Apple silicon). Every result is reported with the machine, kernel, runtime version, number of runs and a confidence interval. Labs 1 and 5 are AI-off. Elsewhere agents are allowed, but no performance or correctness claim is accepted without the measurement or the checker output.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Percentiles, fan-out and USL (AI off for the analysis) | Measure a service's latency histogram; simulate fan-out to 1/10/100 backends; fit the Universal Scalability Law to 1–32 thread throughput | Histogram, fan-out p99 table, USL fit with coefficients and a paragraph on what limits scaling | 4 h |
| 2 · Caches and false sharing | Row vs column traversal; padded vs unpadded per-thread counters; AoS vs SoA | `perf stat` counters (cache misses, cycles) and timings for each pair | 4 h |
| 3 · Broken benchmarks | Fix 6 planted microbenchmark flaws in Java (JMH), Go and Rust (Criterion); run one service under closed and open load models | Fixed benchmarks with explanations; closed vs open p99 comparison showing coordinated omission | 5 h |
| 4 · Flame graphs and off-CPU | Profile a provided service that is slow for 3 different reasons (CPU hot loop, lock wait, synchronous disk I/O) | CPU and off-CPU flame graphs, the cause of each slowdown, and before/after numbers for each fix | 5 h |
| 5 · Litmus tests on x86 and ARM (AI off) | Run store-buffering and message-passing litmus tests with relaxed, acquire/release and seq-cst orderings | Observed outcome counts per platform and ordering, with an explanation of every surprising result | 4 h |
| 6 · Contention and lock-free alternatives | Find the hottest lock in a provided Java or Go service and fix it with striping, sharded counters or read-mostly structures; then build a Treiber stack and an SPSC ring buffer in Rust (crossbeam-epoch) or Java and reproduce ABA without reclamation | Lock profile and 1–32 thread throughput before/after; loom or jcstress results; lock-free vs mutex throughput | 10 h |
| 7 · TSan, jcstress, loom, TLA+ | Find 4 planted concurrency bugs, each with the right tool; write a TLA+ spec of a bounded buffer | Tool outputs, fixes, and the TLC run with the invariant that caught the planted design bug | 6 h |
| 8 · Server architectures | Echo/key-value server with epoll, io_uring, thread-per-request (virtual threads) and a reactor runtime | p50/p99 and memory at 1k, 10k and 50k connections | 6 h |
| 9 · Parallel speedup | Parallel merge sort and a parallel log aggregation with work stealing; find the sequential cut-off | Speedup and efficiency plots; the serial fraction you measured and removed | 4 h |
| 10 · Overload, retries and bursts | 3-service chain: show a retry storm, then add deadlines, retry budgets, jittered backoff, load shedding and hedging | Goodput vs offered load (up to 3×), p99 before/after, extra load caused by hedging | 6 h |

## Projects

### P1 · A trustworthy benchmark report (L1, ~6 hours)

**Real-world inspiration:** library and runtime maintainers routinely reject performance pull requests that come without a sound benchmark; many public "X is faster than Y" posts do not survive a careful rerun.

**What to build:** pick a public performance claim (a blog post or project README comparing two JSON libraries, two HTTP routers or two collections). Reproduce it with a sound methodology, then extend it with one realistic workload the original did not test.

**Acceptance criteria:**
- Harness uses JMH, `testing.B` + benchstat or Criterion correctly (warm-up, blackholes, multiple forks/runs).
- Results reported as medians with 95% confidence intervals over at least 10 runs; environment fully described.
- The report states clearly whether the original claim holds, partly holds or fails, and why.
- A reviewer can rerun everything with one command and get results within the stated intervals.

**Stretch goals:** submit the reproduction to the original author or project; add allocation measurements.

**What it proves to an employer:** you do not believe numbers you have not measured properly, and you can measure properly.

### P2 · Concurrent in-memory cache with proven correctness (L2, ~15 hours)

**Real-world inspiration:** in-process caches such as Caffeine (Java) and Ristretto (Go) sit in front of databases in high-traffic services, where lock contention and eviction policy decide tail latency.

**What to build:** a thread-safe cache library in Java, Go or Rust with sharded storage, a W-TinyLFU or segmented-LRU eviction policy, TTL, a size bound, and statistics. Provide a model-based test against a simple single-threaded reference.

**Acceptance criteria:**
- Linearisability-style check: 1,000 randomised concurrent histories (or loom/jcstress exhaustive tests on small cases) show no result impossible under some sequential order.
- Race detector / TSan clean under a 30-minute stress run.
- Throughput scales to at least 60% efficiency at 16 threads on a read-heavy (90/10) Zipf workload (USL fit included).
- Hit rate within 3 percentage points of Caffeine or Ristretto on two published traces or a Zipf workload of your choosing (method stated).
- p99 `get` latency under 1 µs at 16 threads on a stated machine, measured with HdrHistogram.

**Stretch goals:** lock-free read path; per-entry loading with request coalescing ("single flight") and a test that 1,000 concurrent misses trigger one load.

**What it proves to an employer:** you can build a concurrent data structure that is fast and that you can prove correct, a senior-level skill.

### P3 · Performance investigation of a real system (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** booking surges such as Tatkal ticket openings (IRCTC's public record is 28,434 tickets booked in one minute on 12 November 2022) and flash sales put sudden load on systems that are fine at normal traffic. The system and numbers below are an **illustrative scenario**.

**What to build:** take a provided open-source-style booking service (API, Postgres, a cache, a payment stub) or a real open-source application you can load-test legally on your own infrastructure. Define an SLO (for example p99 < 300 ms at 2,000 requests/s with a 10-second burst to 10,000 requests/s). Investigate, fix and document.

**Acceptance criteria:**
- Baseline: open-model load test (k6 constant-arrival-rate) with HdrHistogram output, CPU and off-CPU flame graphs, lock profile and USE-method checklist.
- At least 3 distinct bottlenecks found (for example: a contended lock, an N+1 query, a missing bound on a queue, GC pressure, a retry storm), each with evidence, a fix and a measured result.
- Burst behaviour: during the 10× burst, goodput stays within 20% of capacity, rejected requests get fast `429`/`503` responses with `Retry-After`, and no request waits past its deadline.
- One concurrency fix verified with a race detector or model checker, not only with tests.
- A CI benchmark gate that catches a reintroduced 10% regression in the hottest path and ignores noise (shown with 10 runs).
- A 6–10 page investigation report: hypothesis, measurement, change, result, and what you would do next.

**Stretch goals:** compare a thread-per-request (virtual threads) and an event-loop version of the hottest endpoint; continuous profiling with Parca or Pyroscope across deploys.

**What it proves to an employer:** you can make a real system fast under real load and prove it, which is what performance, backend and SRE teams look for.

## Feeds into

- [SWE401 Large-Scale System Design](../../year_4/SWE401_large_scale_system_design/README.md): capacity estimates, queueing and overload control at system scale.
- [SWE403 Reliability, Observability and Incident Engineering](../../year_4/SWE403_reliability_observability_and_incident/README.md): profiles and latency budgets become SLOs and incident evidence.
- [OPS404 Performance and Capacity Engineering](../../../devops_sre_platform_engineering/year_4/OPS404_performance_and_capacity_engineering/README.md) and [BE402 Scalability and Performance](../../../backend_engineering/year_4/BE402_scalability_and_performance_caching_sharding/README.md): electives that go further on capacity and data-tier scaling.
- [SWE flagship industry project](../../../../06_career_and_market_readiness/05_industry_projects/SWE_software_engineering.md): P3's method is its performance section.
