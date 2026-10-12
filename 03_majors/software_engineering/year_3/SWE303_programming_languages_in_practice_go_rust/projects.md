# SWE303 · Labs and projects

Toolchains: Go 1.27, Rust stable (2024 edition) with Tokio, and JDK 25 (LTS). Everything runs on a laptop with Docker. Every performance claim must come with a benchmark or load-test output and the machine description. The race-and-leak hunt in Lab 3 and the borrow-checker kata in Lab 4 are AI-off. Elsewhere coding agents are allowed; you must run the verification tools listed in each lab on anything an agent writes.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Three runtimes, one workload | Same HTTP endpoint (parse JSON, compute, respond) in Go, Rust (axum) and Java 25 | Startup time, idle RSS, throughput and p99 at 3 load levels (k6), 3 runs each | 5 h |
| 2 · Idiomatic Go | Streaming log processor on `io.Reader` with typed errors, table-driven tests and a fuzz target | Code, coverage, and fuzzing output for 10 minutes | 4 h |
| 3 · Races, leaks and containers (the race-and-leak hunt is AI off) | Find and fix 3 data races and 3 goroutine leaks planted in a 1,200-line service; then reproduce CPU throttling and an OOM kill in a 2-CPU, 512 MB container and fix them with runtime settings | Fix commits; `-race` output and `goroutineleak` profiles before/after; before/after graphs (latency, RSS, GC cycles) and the settings you chose | 8 h |
| 4 · Borrow-checker kata (AI off) | 15 graded Rust exercises on ownership, borrowing and lifetimes, no `.clone()` allowed unless justified | Passing tests and a one-line explanation per fix | 5 h |
| 5 · No `unwrap()` | Harden a Rust config loader and request handler: every fallible path returns a typed error | Clippy clean with `unwrap_used` denied; a test per error path; a malformed-config test that does not panic | 4 h |
| 6 · Async Rust and cancellation | Tokio chat server with `select!`; find a message loss caused by cancellation; add back-pressure | 10,000-connection test results; the cancellation bug's reproduction and fix | 6 h |
| 7 · JMM and JMH | Reproduce unsafe publication with jcstress; fix 3 broken JMH benchmarks | jcstress report, corrected benchmarks and an explanation of each original flaw | 4 h |
| 8 · GC shoot-out | One allocation-heavy Spring Boot service under G1, generational ZGC and generational Shenandoah, with and without compact object headers | Table: p50/p99, CPU, heap; GC log excerpts supporting each conclusion | 5 h |
| 9 · Virtual threads under load | Fan-out service on platform threads vs virtual threads; reproduce pinning on JDK 21 and its absence on JDK 25; starve a 20-connection DB pool | Latency/throughput plots, thread dumps showing pinning, the fix for starvation | 5 h |
| 10 · Interop | Rust library exposed via C ABI, called from Go (cgo) and Java (FFM), and as a Python extension (PyO3) | Per-call overhead for each binding, and the batched version's overhead | 5 h |

## Projects

### P1 · Concurrent link checker in Go (L1, ~6 hours)

**Real-world inspiration:** documentation sites and government portals with thousands of pages and links that rot; crawler workers are a classic Go use case.

**What to build:** a CLI that crawls a site from a start URL (same host only), checks every link with bounded concurrency, respects `robots.txt` and a per-host rate limit, and writes a JSON report. Use `context` for a global timeout and `errgroup` for worker coordination.

**Acceptance criteria:**
- Crawls a provided local test site of 5,000 pages with 200 broken links and reports exactly those 200 (fixture comparison).
- Never exceeds the configured concurrency or the per-host rate (verified by the test server's request log).
- Ctrl-C or the global timeout stops all goroutines within 1 second; the `goroutineleak` profile is empty at exit.
- `go test -race ./...` passes with at least 15 tests, including one that uses `testing/synctest` for timeout logic.
- Single static binary under 20 MB.

**Stretch goals:** add retries with jittered backoff; export Prometheus metrics; compare with a Python `asyncio` version.

**What it proves to an employer:** you write concurrent Go that stops cleanly, does not leak, and respects the systems it touches.

### P2 · Rate-limited API gateway in Rust (L2, ~15 hours)

**Real-world inspiration:** edge proxies such as Cloudflare's Pingora (written in Rust) and API gateways in front of payment and booking APIs. Traffic numbers are an **illustrative scenario**.

**What to build:** an async reverse proxy on Tokio and hyper/axum that routes by path to upstream services, enforces per-API-key token-bucket limits, sets per-request deadlines, applies a circuit breaker per upstream, and hot-reloads its config without dropping connections. All errors are typed; no `unwrap()` outside tests.

**Acceptance criteria:**
- At 20,000 requests/s on a laptop (k6 or `oha`), added p99 latency over direct upstream calls under 2 ms.
- Rate limits accurate within 2% over a 60-second test for 1,000 keys.
- A malformed config file is rejected with a clear error and the old config stays active (test included); this is the lesson of Cloudflare's November 2025 outage.
- When an upstream hangs, requests fail at their deadline and the circuit opens within the configured window; no task leak (tokio-console or task-count metric evidence).
- Clippy clean with `unwrap_used` and `expect_used` denied in non-test code; Miri passes on any `unsafe` (or there is none).

**Stretch goals:** HTTP/2 upstreams; a WebAssembly plugin hook for request filters; compare with an equivalent Go gateway.

**What it proves to an employer:** you can build safe, fast network infrastructure in Rust and you design for bad input and slow dependencies.

### P3 · One service, three runtimes: a measured language decision (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** companies periodically decide which language a new high-traffic component should use; Discord's Go-to-Rust write-up (2020) and Google's Android Rust data (2025) are public examples of evidence-driven decisions. The component below is an **illustrative scenario**.

**What to build:** a "PIN-code serviceability and delivery-estimate" service (load the India Post PIN directory from the [Open Government Data Platform](https://www.data.gov.in/), answer lookups and compute delivery estimates with a small rules engine), implemented in Go, Rust and Java 25 with virtual threads. Same API (gRPC and HTTP), same tests (shared contract suite), same container limits (2 CPUs, 1 GB). Then write the decision record.

**Acceptance criteria:**
- All three pass one shared contract-test suite of at least 40 cases.
- Benchmark matrix: cold start, idle memory, throughput and p50/p99/p99.9 at 3 load levels, each repeated 5 times, with confidence intervals; raw data in the repo.
- One profile (flame graph) per implementation at peak load, with the top hot spot explained and one optimisation applied and measured.
- Failure drills: upstream timeout, malformed data file, memory pressure; behaviour documented for each runtime.
- Developer-cost data: lines of code, build time, time spent per implementation (your log), and the number of agent suggestions you rejected per language, with reasons.
- A two-page language decision record that a reviewer could disagree with on specific points.

**Stretch goals:** GraalVM native image for the Java version; a Rust core shared with the Go version via C ABI, measured.

**What it proves to an employer:** you choose technology with evidence, you can work in all three ecosystems, and you understand their runtimes deeply enough to debug them.

## Feeds into

- [SWE305 Concurrency and Performance Engineering](../SWE305_concurrency_and_performance_engineering/README.md): memory models and profiling go deeper.
- [SWE403 Reliability, Observability and Incident Engineering](../../year_4/SWE403_reliability_observability_and_incident/README.md): runtime metrics and failure drills from P2 and P3 become SLO-driven operations.
- [SWE402 Legacy Modernization and Refactoring with AI](../../year_4/SWE402_legacy_modernization_and_refactoring_with_ai/README.md): language migrations (for example C or Java to Rust or Go) with agents.
- [OV02 Cloud-Native Backend](../../../../04_overlaps/OV02_cloud_native_backend/README.md): Go and JVM services on Kubernetes.
