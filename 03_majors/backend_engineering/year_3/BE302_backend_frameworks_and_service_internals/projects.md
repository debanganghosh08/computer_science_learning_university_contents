# BE302 · Labs and projects

All labs run on a laptop with Docker and a local Kubernetes cluster (kind or k3d). Every lab ships with a k6 or Locust script and a results template, so you report numbers rather than impressions. Lab 1 and the live debugging drills are done without coding agents. From Lab 2 on, AI assistants are allowed, but you must be able to explain every line and every number in the oral review.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 0 · Little's law | Measure in-flight requests, throughput and latency on a toy server at 6 load levels, then fit L = λ·W | A plot, the fitted line, and one paragraph on where the law broke down and why | 3 h |
| 1 · HTTP on raw sockets | HTTP/1.1 server with keep-alive, chunked responses, a router, a middleware chain and an error boundary, in any language, without a framework | Code passing the provided conformance tests (pipelined requests, malformed headers, 1 MB bodies) | 8 h |
| 2 · One API, four stacks | The same 5-endpoint "orders" API in Go `net/http`, Spring Boot 4, Fastify and FastAPI against one Postgres | Benchmark table (throughput, p50/p99, RSS, startup time) at 100, 1,000 and 3,000 virtual users, run three times each | 12 h |
| 3 · Blocking and pinning | Reproduce event-loop blocking (Node), virtual-thread pinning (Java 21 vs Java 25) and a sync driver inside `async def` (Python), then fix each | Before/after latency plots and the profiler or JFR evidence for each | 6 h |
| 4 · Cancellation | Show that a client disconnect cancels the in-flight SQL query in Go (`context`) and in one other stack | Postgres `pg_stat_activity` evidence and a test that fails without cancellation | 4 h |
| 5 · Pools and overload | Exhaust a connection pool, then add bounded queues, `503` + `Retry-After` and a per-dependency bulkhead | A goodput-vs-offered-load plot showing flat goodput past saturation instead of collapse | 6 h |
| 6 · Zero-drop rolling restart | Graceful shutdown in all four stacks; rolling restart of 3 replicas on kind under 500 requests/s | k6 output with zero non-2xx responses across five restarts, plus the shutdown sequence diagram | 6 h |
| 7 · Telemetry | Structured logs, OpenTelemetry traces and RED metrics with pool wait time and runtime metrics | A dashboard screenshot and a write-up of one planted fault found from telemetry alone | 5 h |
| 8 · Real-dependency tests | Testcontainers for Postgres and Redis, Toxiproxy for latency and connection resets, one property-based test | A suite that runs in under 60 s and catches the three bugs planted by the instructor | 6 h |
| 9 · Profiling | Flame graphs with `pprof`, async-profiler, `node --cpu-prof` and py-spy on a provided slow service | Three flame graphs, the hot spot in each, the fix, and the measured improvement | 5 h |

## Projects

### P1 · PIN code serviceability API (L1, ~6 hours)

**Real-world inspiration:** checkout flows in Indian e-commerce and food delivery check whether a PIN code is serviceable before taking payment. India Post's PIN code directory is published as open data on the [Open Government Data Platform](https://www.data.gov.in/), so the data set is real even though the service is a teaching version.

**What to build:** a read-only service in the stack you know least. It loads the PIN code directory at startup and serves:
- `GET /pincodes/{pin}` (office names, district, state);
- `GET /pincodes?district=` with cursor pagination;
- `GET /healthz` and `GET /readyz`.

Required pieces: typed configuration validated at boot, structured logs with request IDs, problem-details error responses, request timeouts, graceful shutdown, and a Dockerfile.

**Acceptance criteria:**
- p99 latency under 20 ms at 1,000 requests/s on a 4-vCPU laptop for `GET /pincodes/{pin}` (k6 script and output included).
- `readyz` fails until the data set has loaded and passed a row-count check; `healthz` never touches external dependencies.
- Under `kill -TERM` during a load test, in-flight requests finish and the process exits within 10 s with zero failed responses.
- Invalid input (`/pincodes/12AB`, a 7-digit PIN) returns `400` with a problem-details body; unknown PINs return `404`.
- At least 15 tests, including one that starts the real binary and calls it over HTTP.

**Stretch goals:** hot-reload the data set without downtime; add an `ETag` and conditional `GET`; build a native image (GraalVM) or a distroless image and compare startup and memory.

**What it proves to an employer:** you ship small services with the production basics done right, in a language you just learned.

### P2 · Seat-hold service in two stacks (L2, ~15 hours)

**Real-world inspiration:** high-contention booking such as Indian Railways Tatkal tickets or cinema seat selection, where many clients race for a few seats at the same second. The workload and numbers here are an **illustrative scenario**, not a description of IRCTC's or any company's system.

**What to build:** the same seat-hold API in two of the four stacks, sharing one Postgres schema:
- `POST /shows/{id}/holds` holds up to 4 seats for 5 minutes;
- `POST /holds/{id}/confirm`;
- `DELETE /holds/{id}`;
- a background expiry job.

Use row-level locking (`SELECT … FOR UPDATE SKIP LOCKED`) or a conditional `UPDATE`, explicit pool sizing, per-request deadlines and a bounded admission queue.

**Acceptance criteria:**
- **Correctness under contention:** 2,000 concurrent clients competing for 100 seats produce zero double-holds and zero lost seats, checked by an invariant query after every run (10 runs).
- **Performance:** p99 under 150 ms at 1,500 requests/s with the pool size you documented, on both stacks.
- **Overload:** at 3× capacity, the service returns `503` with `Retry-After` for excess load, goodput stays within 15% of its peak, and no request waits longer than its deadline.
- **Expiry:** holds expire within 5 s of their deadline even while a pod restarts.
- **Comparison report:** throughput, p99, memory, lines of code and one debugging story per stack. You explain why the slower stack was slower, with profile evidence.

**Stretch goals:** a third stack; replace the polling expiry with Postgres `LISTEN/NOTIFY`; a chaos run with Toxiproxy adding 200 ms to the database.

**What it proves to an employer:** you can make concurrent code correct first and fast second, and you can compare runtimes with evidence instead of opinion.

### P3 · Service chassis and reference service (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** platform teams give product teams a "golden path" template so every new service starts with health checks, telemetry, shutdown and testing already done. [Backstage software templates](https://backstage.io/docs/features/software-templates/) are the CNCF project most commonly used to publish such templates.

**What to build:** a reusable chassis in one stack of your choice, published as a template repository. On top of it, build a reference "order status" service that calls Postgres, Redis and one slow external HTTP dependency (simulated). The chassis must include:
- typed config and secrets loading;
- liveness, readiness and startup probes;
- graceful shutdown that drains HTTP and one long-lived stream type (SSE or WebSocket);
- structured logging, OpenTelemetry traces and RED metrics;
- timeouts, a circuit breaker and a bulkhead per dependency;
- Testcontainers and Toxiproxy test harnesses, and a k6 suite;
- a Helm chart or Kustomize overlay;
- an architecture decision record and a runbook.

**Acceptance criteria:**
- **Performance:** p99 under 100 ms at 2,000 requests/s on 3 replicas with 1 vCPU each, with the profile and dashboard that show where the time goes.
- **Deploys:** five rolling deploys under load with zero non-2xx responses and no dropped stream messages.
- **Dependency failure:** when the external dependency's latency rises to 2 s, the breaker opens within 10 s, the service degrades as documented (cached or partial response) and p99 for other endpoints stays under 150 ms. After the fault is removed, it recovers within 30 s.
- **Soak:** a 60-minute soak at 60% capacity with resident memory growth under 10% and no goroutine, thread or connection leaks (runtime metrics attached).
- **Test suite:** under 3 minutes, covering every failure path in the runbook.
- **Reuse:** a second, minimal service generated from the template passes the same checks with under 50 lines of service-specific code.
- **Write-up:** a 4-page design note covering the concurrency model, pool sizes and timeout budget with the arithmetic, and two incidents you induced and debugged.

**Stretch goals:** port the chassis to a second stack and compare; add canary analysis on the RED metrics; add continuous profiling (Pyroscope or Parca).

**What it proves to an employer:** you think like a platform or senior backend engineer: you make the right thing the default for other teams, and you can show with numbers that it works under failure.

## Feeds into

- [BE402 Scalability and Performance](../../year_4/BE402_scalability_and_performance_caching_sharding/README.md): the P3 chassis is the system you scale, cache and load-test.
- [BE404 Microservices, Service Mesh and Platform APIs](../../year_4/BE404_microservices_service_mesh_and_platform_apis/README.md): the chassis becomes a platform API with contract tests.
- [OV02A Building Cloud-Native Services](../../../../04_overlaps/OV02_cloud_native_backend/OV02A_building_cloud_native_services/README.md): deploying the chassis on managed Kubernetes.
- [SWE305 Concurrency and Performance Engineering](../../../software_engineering/year_3/SWE305_concurrency_and_performance_engineering/README.md): a deeper elective on the runtime topics of Chapters 2 and 11.
