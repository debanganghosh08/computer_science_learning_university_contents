# BE302 · Backend Frameworks and Service Internals

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 5 | 4 (≈ 120 hours) | L2 → L3 | [CS211](../../../../02_year_2_core_computer_science/semester_4/CS211_database_systems_internals/README.md), [CS212](../../../../02_year_2_core_computer_science/semester_4/CS212_distributed_systems_i/README.md) | [BE402](../../year_4/BE402_scalability_and_performance_caching_sharding/README.md), [BE404](../../year_4/BE404_microservices_service_mesh_and_platform_apis/README.md), [OV02A](../../../../04_overlaps/OV02_cloud_native_backend/OV02A_building_cloud_native_services/README.md) |

Part of the [Backend Engineering major](../../README.md). Runs in the same semester as [BE301 API Design](../BE301_api_design_rest_grpc_and_graphql/README.md) and [BE303 Data Modeling and Storage](../BE303_data_modeling_and_storage_for_backends_postgres/README.md). Builds on the processes, threads and sockets of [CS203](../../../../02_year_2_core_computer_science/semester_3/CS203_operating_systems/README.md) and [CS204](../../../../02_year_2_core_computer_science/semester_3/CS204_computer_networks/README.md).

## Why this course matters now

Every backend framework does the same job: accept a connection, parse a request, run middleware, call a handler, borrow a database connection from a pool, write a response, and emit telemetry. Frameworks change every few years; that lifecycle does not. Runtimes have changed a lot recently. Java 21 made virtual threads final (JEP 444), and Java 24 removed most pinning inside `synchronized` (JEP 491). Go 1.25 made `GOMAXPROCS` respect container CPU limits. Python 3.14 made the free-threaded build officially supported (PEP 779). Node.js moves to one major release a year from version 27. Coding agents such as Claude Code, GitHub Copilot, Cursor and Codex now scaffold a working CRUD service in minutes. Still, a person has to explain why p99 latency jumps from 80 ms to 4 s while CPU sits at 30%, why one slow JSON parse stalls every request in a Node process, and why a deploy drops 2% of requests. This course teaches the internals that answer those questions, using one framework in depth in each of four ecosystems.

## Learning outcomes

By the end you can:

1. **Trace** a request from `accept()` through TLS, HTTP parsing, routing, middleware, handler, pool checkout and serialization, and **attribute** measured latency to each stage.
2. **Explain** thread-per-request, event-loop, goroutine (M:N) and virtual-thread concurrency, and **predict** how each behaves under blocking I/O, CPU-heavy work and slow clients.
3. **Build** the same service in Go (`net/http`), Java (Spring Boot 4), TypeScript (Fastify on Node.js) and Python (FastAPI), and **compare** them on throughput, p99 latency, memory and startup time with reproducible load tests.
4. **Size** connection pools, timeouts and queue limits from Little's law and measured service times, and **demonstrate** backpressure (bounded queues, `503` with `Retry-After`) instead of collapse.
5. **Implement** configuration, liveness, readiness and startup probes, and a graceful shutdown that drops zero requests during a Kubernetes rolling update.
6. **Instrument** a service with structured logs, OpenTelemetry traces and RED metrics, and **use** them to find a planted fault.
7. **Test** services with real dependencies (Testcontainers), injected network faults (Toxiproxy) and property-based tests.
8. **Profile** CPU, allocation and lock contention in each runtime with flame graphs, and **fix** the hot spot.
9. **Review** AI-generated service code for blocking calls on async paths, missing timeouts, unbounded pools and lifecycle bugs.

## Chapters and lessons

### Chapter 1 · The request lifecycle (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 From socket to handler | Listen backlog, `accept()`, `SO_REUSEPORT`, keep-alive, the kernel's role vs the runtime's | `strace`/`ss` a running server; count syscalls per request |
| 1.2 HTTP/1.1, HTTP/2 and HTTP/3 on the server | Head-of-line blocking, multiplexed streams, flow control, why gRPC needs HTTP/2, where TLS terminates | Serve one endpoint over h1 and h2; compare connections and latency with `h2load` |
| 1.3 Routing and middleware | Trie and radix routers, the "onion" middleware model, ordering bugs (auth before rate limit or after?) | Draw the middleware chain of a real Spring Boot or Fastify app from its source |
| 1.4 Serialization and validation cost | JSON encode/decode, schema validation, reflection vs generated code | Profile a 1 MB JSON response in two stacks; find where time goes |
| 1.5 A framework in 300 lines | Parser, router, middleware, handler interface, error boundary | Lab 1: build an HTTP/1.1 server on raw sockets with keep-alive |

**Check your understanding:** (1) Why can a server with spare CPU still refuse connections? Name two queues a request waits in before your code runs. (2) Where should authentication sit in the middleware chain relative to rate limiting, and why does the answer change for unauthenticated endpoints? (3) Why does HTTP/2 reduce connection count but not remove head-of-line blocking over TCP?

### Chapter 2 · Concurrency models (weeks 2–3)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Little's law and thread-per-request | L = λ·W; why a 200-thread Tomcat pool caps throughput at 200 / latency; queueing when service time grows | Lab 0: measure concurrency vs latency on a toy server and fit Little's law |
| 2.2 The event loop | libuv phases, microtasks vs macrotasks, the worker pool, event-loop lag; Node's "Don't block the event loop" guide | Block the loop with a synchronous hash; measure the impact on unrelated requests |
| 2.3 Goroutines and the Go scheduler | G-M-P model, the netpoller, preemption, goroutine leaks, `GOMAXPROCS` in containers (Go 1.25) | Leak goroutines with an unclosed channel; find them with `pprof` goroutine profiles |
| 2.4 Java virtual threads | Mounting and unmounting, pinning (`synchronized` before Java 24, native frames), why you never pool virtual threads, `ThreadLocal` costs | Reproduce pinning on Java 21 and show it gone on Java 25 (JEP 491) |
| 2.5 Python: asyncio, the GIL and free-threading | Coroutines, the event loop, `run_in_executor`, sync vs async endpoints, the free-threaded build (supported since 3.14, not default) | Call a sync driver inside `async def` and measure the stall; fix it two ways |
| 2.6 Reactive vs blocking styles | Backpressure in Reactive Streams, when WebFlux or Vert.x still wins, why virtual threads removed most reasons to go reactive | Write the same fan-out (call 3 services, combine) in blocking, async and reactive style |

**Check your understanding:** (1) A service handles 400 requests/s at 50 ms each. How many requests are in flight, and what happens to that number when a dependency slows to 500 ms? (2) Why does a CPU-heavy task hurt a Node service more than a Go service with the same code? (3) Virtual threads make blocking cheap; what resource still runs out first, and what limits it?

### Chapter 3 · Go in depth: `net/http`, `context` and `database/sql` (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 `http.Handler` and `ServeMux` | Method and wildcard patterns (Go 1.22+), middleware as `func(http.Handler) http.Handler`, when to add chi | Build a versioned router with logging, recovery and request-ID middleware |
| 3.2 `context.Context` | Cancellation trees, deadlines, values (and their abuse), client disconnect propagation | Prove that a cancelled request cancels its in-flight Postgres query |
| 3.3 `database/sql` and pgx pools | `SetMaxOpenConns`, `SetMaxIdleConns`, `SetConnMaxLifetime`, `pgxpool` stats, prepared statements | Exhaust the pool on purpose; read `DBStats` to diagnose it |
| 3.4 Clients and timeouts | `http.Client` has no timeout unless you set one; `Transport` pooling, `MaxIdleConnsPerHost` | Find and fix a hang caused by a default client against a stalled server |
| 3.5 Logging and errors | `log/slog`, wrapped errors, `errgroup`, panics vs errors at the boundary | Convert an app to structured `slog` with a request-scoped logger |

**Check your understanding:** (1) Why should `context` values not carry business parameters? (2) What happens to idle connections above `MaxIdleConnsPerHost` under bursty load? (3) When is a goroutine-per-request design wrong?

### Chapter 4 · Java in depth: Spring Boot 4 (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 The container | Inversion of control, bean scopes, auto-configuration and conditions, Spring Boot 4.0 (Nov 2025) on Spring Framework 7 | Read the auto-configuration report and explain why each bean exists |
| 4.2 Request path | Servlet filters vs `HandlerInterceptor` vs `@ControllerAdvice`; Tomcat thread pool; problem-detail error responses | Add tenant resolution as a filter and as an interceptor; compare |
| 4.3 Proxies and transactions | `@Transactional` via proxies, the self-invocation trap, propagation and read-only hints | Write a test that fails because of self-invocation, then fix it |
| 4.4 Virtual threads in Spring | `spring.threads.virtual.enabled`, HikariCP as the real limit, JFR events for pinning | Load test platform vs virtual threads at 2,000 concurrent clients |
| 4.5 Startup and footprint | JIT warm-up, class data sharing, GraalVM native image trade-offs, Actuator endpoints | Measure startup and RSS for JVM vs native image builds |

**Check your understanding:** (1) Why does calling a `@Transactional` method from the same class skip the transaction? (2) With virtual threads on and a 10-connection Hikari pool, what does the 11th concurrent request do? (3) When is a native image a bad trade?

### Chapter 5 · TypeScript in depth: Node.js and Fastify (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Runtime and release model | Node 24 LTS vs Node 26 Current, the annual schedule from Node 27, built-in TypeScript type stripping, ESM | Pin an LTS version and document the upgrade window for your service |
| 5.2 Fastify's lifecycle | `onRequest` → `preParsing` → `preValidation` → `preHandler` → `preSerialization` → `onSend` → `onResponse`; encapsulated plugins; Express 5 and NestJS compared | Implement auth, rate limit and audit hooks at the correct stages |
| 5.3 Schemas as contracts | JSON Schema validation, compiled serializers, TypeBox/Zod type inference | Show the throughput change from a response schema |
| 5.4 Request context and async | `AsyncLocalStorage`, unhandled rejections, `AbortSignal` for cancellation | Carry a request ID through three async layers without passing it by hand |
| 5.5 CPU work off the loop | `worker_threads`, `piscina`, streaming parsers, request size limits | Move image resizing to a worker pool; measure event-loop lag before and after |

**Check your understanding:** (1) Why is a response schema a performance feature in Fastify and not just documentation? (2) What happens to a Node process on an unhandled promise rejection, and what should your service do? (3) When would you choose NestJS over Fastify alone?

### Chapter 6 · Python in depth: FastAPI (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 ASGI and Starlette | The ASGI interface, Uvicorn workers, lifespan events | Write a raw ASGI app, then the same in FastAPI |
| 6.2 Pydantic v2 | Validation and serialization, strict mode, the compiled core, response models | Benchmark validation of 10,000 objects with and without strict types |
| 6.3 Dependencies | `Depends`, scoped resources, yield dependencies for cleanup, testing overrides | Inject a DB session and a tenant; override both in tests |
| 6.4 Sync vs async endpoints | `def` endpoints run in a threadpool, `async def` on the loop; SQLAlchemy 2.0 async with asyncpg | Find a blocking call in an `async def` with event-loop debug mode |
| 6.5 Deployment shapes | Workers per core, Gunicorn vs Uvicorn processes, memory per worker, Python 3.14 free-threading and what it changes for web servers | Compare 4 workers × 1 thread with free-threaded builds under the same load |

**Check your understanding:** (1) Why can an `async def` endpoint be slower than a `def` endpoint? (2) What does a yield dependency guarantee if the client disconnects mid-request? (3) Why does each Uvicorn worker need its own pool, and what does that do to total DB connections?

### Chapter 7 · Pools, timeouts and backpressure (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Pool sizing | HikariCP's "small pool, saturated with threads" argument and its starting formula; pods × pool ≤ `max_connections` | Size pools for 20 pods against a 4-vCPU Postgres; defend the numbers |
| 7.2 Connection poolers | PgBouncer session vs transaction pooling, prepared statements in transaction mode (1.21+), RDS Proxy | Break a session-level feature under transaction pooling, then fix the code |
| 7.3 Timeouts everywhere | Connect, read, total and idle timeouts; deadline propagation; timeout budgets across hops | Write a timeout budget for a 3-hop request with a 1 s SLO |
| 7.4 Bulkheads and circuit breakers | Separate pools per dependency, Resilience4j, half-open probes | Make one slow dependency harmless to the rest of the service |
| 7.5 Backpressure and load shedding | Bounded queues, admission control, `503` + `Retry-After`, LIFO under overload | Lab 5: overload a service and keep goodput flat instead of collapsing |

**Check your understanding:** (1) Why does adding connections to a saturated database usually make latency worse? (2) A timeout of 30 s on a call inside a 2 s user request: what goes wrong? (3) Why shed load at the edge of the service rather than letting requests queue?

### Chapter 8 · Configuration, health and graceful shutdown (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Configuration | Twelve-Factor config, typed config objects, validation at boot, secrets kept out of config, feature flags (OpenFeature) | Make the service refuse to start on a bad config with a clear message |
| 8.2 Health probes | Liveness vs readiness vs startup; why liveness must not check the database | Write probes that survive a database blip without a restart storm |
| 8.3 Graceful shutdown | SIGTERM → fail readiness → drain → stop accepting → finish in-flight → close pools → exit; PID 1 and signal forwarding | Implement it in all four stacks |
| 8.4 Kubernetes termination | Endpoint removal races SIGTERM, `preStop` delay, `terminationGracePeriodSeconds` (default 30 s) | Lab 6: rolling restart under load with zero non-2xx responses |
| 8.5 Long-lived connections | Draining WebSockets, SSE and gRPC streams; `GOAWAY`; connection max age | Drain 1,000 open WebSockets without dropping messages |

**Check your understanding:** (1) Why can pods receive traffic after SIGTERM? (2) What breaks if liveness checks the database and the database is slow for 60 s? (3) Which state must be flushed before exit, and which can be lost safely?

### Chapter 9 · Observability and errors inside one service (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Structured logging | Fields not strings, levels, sampling, PII redaction; `slog`, Logback JSON, pino, structlog | Make every log line carry trace ID, tenant and route |
| 9.2 Traces | OpenTelemetry SDKs, auto-instrumentation vs manual spans, span attributes, context propagation | Trace one request across handler, pool wait and SQL |
| 9.3 Metrics | RED (rate, errors, duration), histograms vs averages, pool and runtime metrics | Build a RED dashboard with pool wait time and event-loop lag |
| 9.4 Error boundaries | Domain errors vs bugs, mapping to status codes and problem details, never leaking stack traces | Map 12 failure cases to responses; test each |

**Check your understanding:** (1) Why is average latency useless for alerting? (2) What should a log line never contain? (3) How do you show, from telemetry alone, that slowness is pool wait and not SQL time?

### Chapter 10 · Testing services (weeks 11–12)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 What to test where | Unit, component, integration, contract and end-to-end tests; the cost of mocks for databases | Rewrite mock-heavy tests as component tests and compare bugs caught |
| 10.2 Real dependencies | Testcontainers for Postgres, Redis and Kafka; fixtures; parallel test isolation | Lab 8: run the suite against real Postgres in under 60 s |
| 10.3 Faults on purpose | Toxiproxy latency, resets and bandwidth limits; testing retries and timeouts | Prove the circuit breaker opens and closes as designed |
| 10.4 Property-based tests | Hypothesis, jqwik, fast-check, Go's `testing/quick` and fuzzing | Find an input-validation bug with a generator |
| 10.5 Time and concurrency in tests | Fake clocks, Go 1.25's `testing/synctest`, race detectors | Make a flaky timeout test deterministic |

**Check your understanding:** (1) Why do database mocks hide the bugs that matter most? (2) How do you test that shutdown drains in-flight work? (3) What does a race detector miss?

### Chapter 11 · Profiling and runtime tuning (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Flame graphs | Sampling profilers: `pprof`, async-profiler and JFR, `node --cpu-prof`, py-spy | Lab 9: find a planted hot spot in each runtime |
| 11.2 Memory and GC | G1 and ZGC, Go `GOGC` and `GOMEMLIMIT`, V8 heap limits, Python reference counting | Fix an allocation-heavy handler; show GC time before and after |
| 11.3 Containers and CPU | CFS quota throttling, requests vs limits, JVM and Go container awareness | Show throttling in metrics and fix it by changing limits, not code |
| 11.4 Choosing a stack | Team skills, ecosystem, latency profile, hiring market, operational cost | Write an architecture decision record choosing a stack for P3 |

**Check your understanding:** (1) Why can a service be slow while CPU usage is low and no profile shows a hot spot? (2) What is `GOMEMLIMIT` for? (3) When should a team not adopt the "fastest" framework?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1: HTTP server on raw sockets (no AI) | Server passing the conformance tests |
| 2 | 2 | Lab 0: Little's law | Concurrency vs latency plot |
| 3 | 2 | Lab 3: blocking and pinning | Reproductions in Node, Java, Python |
| 4 | 3 | Lab 4: context cancellation | P1 due |
| 5 | 4 | Lab 2 (part 1): Spring Boot version | Same API in Java |
| 6 | 5 | Lab 2 (part 2): Fastify version | Same API in TypeScript |
| 7 | 6 | Lab 2 (part 3): FastAPI version | Four-stack benchmark report |
| 8 | 7 | Lab 5: pools and overload | Goodput-under-overload plot; P2 starts |
| 9 | 8 | Lab 6: zero-drop rolling restart | Load-test log with 0 errors |
| 10 | 9 | Lab 7: telemetry | RED dashboard and one diagnosed fault |
| 11 | 10 | Lab 8: Testcontainers and Toxiproxy | Green suite; P2 due |
| 12 | 10 | Property and time tests | Deterministic test suite; P3 design review |
| 13 | 11 | Lab 9: profiling | Three flame graphs, three fixes |
| 14 | 11 | P3 integration | P3 demo and write-up |
| 15 | Review and exam | — | Written exam and live debugging exam |

## Working with AI in this course

- **Use AI for:** scaffolding the same API across four stacks once you have written the first by hand; translating idioms ("what is the Fastify equivalent of a Spring filter?"); generating Testcontainers fixtures and k6 scripts; explaining profiler output and GC logs; reviewing your shutdown sequence against Kubernetes docs.
- **Do without AI (drills):** the raw-socket HTTP server (Lab 1); Little's law and pool-size calculations on paper; drawing each runtime's scheduler from memory; diagnosing the Lab 5 overload from dashboards alone; the live debugging exam.
- **Verify AI output by:** load-testing every generated change and comparing p99 and error rate with the baseline; running `go test -race`, Java's JFR pinning events and Python's asyncio debug mode; grepping generated code for missing timeouts, unbounded pools, `time.sleep` or synchronous drivers inside `async def`, and default HTTP clients; killing the process mid-request to test shutdown claims.
- **Where AI still fails here (show it yourself):** ask an assistant for a FastAPI endpoint that queries Postgres and check whether it puts a synchronous driver inside `async def`. Ask for a Go HTTP client and check whether it sets a timeout. Ask for a Spring service with two `@Transactional` methods calling each other. Ask for "graceful shutdown on Kubernetes" and check whether it handles the endpoint-removal race. Run each result under load or a fault, and record what broke in your lab notes. The pattern to learn: generated code is usually correct on the happy path and silent about lifecycle, limits and failure.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs 0–9 (tests plus short measured write-ups) | 30% |
| Projects P1 / P2 / P3 | 5% / 12% / 18% |
| Written exam (concurrency models, Little's law, pool sizing, shutdown sequences) | 20% |
| Live debugging exam (unfamiliar service, planted fault, no AI) | 15% |

**Mastery gate:** you pass when you can, without AI help, (a) take an unfamiliar service in any of the four stacks and find a planted fault (pool exhaustion, event-loop blocking, virtual-thread pinning, or a missing client timeout) from its metrics, traces and one profile within 45 minutes; (b) demonstrate a rolling restart of three replicas under 500 requests/s with zero non-2xx responses; and (c) explain every stage of your P3 service's request path and shutdown path line by line.

## Industry reality

Public engineering write-ups show runtime internals deciding real outcomes:

- **Discord** rewrote its Read States service from Go to Rust in 2020 because Go's garbage collector caused latency spikes roughly every two minutes on a large in-memory cache. The lesson is about runtime behaviour, not language rankings.
- **OpenAI** reported in January 2026 that an ORM-generated query joining 12 tables caused several high-severity incidents on the PostgreSQL primary behind ChatGPT. It also reported that connection pooling cut connection time from 50 ms to 5 ms.
- **Spring Boot 4.0** reached general availability on 20 November 2025 on Spring Framework 7; 4.1 followed in June 2026. **Java 25** is the current LTS release, and Java 27 shipped in September 2026.
- **Node.js 24** is the current LTS line. Node.js 26 is "Current". From Node.js 27, every major release becomes LTS after six months.
- In the Stack Overflow 2025 survey, Node.js (48.7%) and Express (19.9%) were among the most used web technologies, and FastAPI usage grew 5 points to 14.8%.

Interview questions from this course:

1. **"p99 latency jumps from 80 ms to 4 s under load, but CPU is at 30%. What do you check?"** A strong answer covers Little's law, pool wait time vs query time, thread or event-loop saturation, a downstream slowdown, GC pauses and CPU throttling. It names the metric that tells each one apart.
2. **"What happens in a Node.js service when one request runs a 200 ms synchronous JSON parse?"** Cover the blocked event loop and the latency added to every other request. Fixes: size limits, streaming parsers, worker threads. Say how to detect it (event-loop lag metrics).
3. **"Virtual threads or reactive (WebFlux) for a new Java service?"** Cover the blocking programming model, pinning and JEP 491, the database pool as the real limit, the debugging and stack-trace cost of reactive code, and the cases where reactive still fits (streaming backpressure).
4. **"How do you deploy with zero dropped requests on Kubernetes?"** Cover readiness failing first, the `preStop` delay for endpoint propagation, draining in-flight and long-lived connections, a grace period sized to the drain, and testing it under load.
5. **"How big should the database connection pool be with 20 pods?"** Cover total connections (pods × pool) against `max_connections`, HikariCP's small-pool argument, transaction-mode PgBouncer and its caveats, and how to verify the choice with a load test.

## Resources (free first)

- **Concurrency and runtimes:** [JEP 444 Virtual Threads](https://openjdk.org/jeps/444), [JEP 491 Synchronize Virtual Threads without Pinning](https://openjdk.org/jeps/491); Node.js [Don't Block the Event Loop](https://nodejs.org/en/learn/asynchronous-work/dont-block-the-event-loop); Go blog [Go Concurrency Patterns: Context](https://go.dev/blog/context); [PEP 779](https://peps.python.org/pep-0779/) (free-threaded Python).
- **Framework documentation:** Go [`net/http`](https://pkg.go.dev/net/http) and [`database/sql`](https://pkg.go.dev/database/sql); [Spring Boot reference](https://docs.spring.io/spring-boot/index.html); [Fastify docs](https://fastify.dev/docs/latest/); [FastAPI docs](https://fastapi.tiangolo.com/); [Pydantic docs](https://docs.pydantic.dev/latest/).
- **Pools and shutdown:** HikariCP [About Pool Sizing](https://github.com/brettwooldridge/HikariCP/wiki/About-Pool-Sizing); [PgBouncer features](https://www.pgbouncer.org/features.html); Kubernetes [Pod lifecycle and termination](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/); [The Twelve-Factor App](https://12factor.net/).
- **Testing and observability:** [Testcontainers](https://testcontainers.com/); [Toxiproxy](https://github.com/Shopify/toxiproxy); [OpenTelemetry docs](https://opentelemetry.io/docs/); [Grafana k6 docs](https://grafana.com/docs/k6/latest/).
- **Profiling:** Brendan Gregg's [flame graphs](https://www.brendangregg.com/flamegraphs.html); [async-profiler](https://github.com/async-profiler/async-profiler); [py-spy](https://github.com/benfred/py-spy); Go [diagnostics](https://go.dev/doc/diagnostics).
- **Paid, worth it:** Brendan Gregg, *Systems Performance*, 2nd edition (Addison-Wesley, 2020).

## Sources

All checked 12 Oct 2026.

- Go release history (Go 1.27 on 19 Aug 2026; 1.27.2 on 8 Oct 2026): https://go.dev/doc/devel/release ; Go 1.25 release notes (container-aware `GOMAXPROCS`, `testing/synctest`): https://go.dev/doc/go1.25
- Spring Boot 4.0.0 GA announcement (20 Nov 2025): https://spring.io/blog/2025/11/20/spring-boot-4-0-0-available-now/ ; current 4.1.x: https://spring.io/projects/spring-boot
- Node.js release lines and the schedule change from Node.js 27: https://nodejs.org/en/about/previous-releases
- Python release status (3.14.0 on 7 Oct 2025; 3.15.0 on 9 Oct 2026): https://www.python.org/downloads/ ; PEP 779 (accepted 16 Jun 2025): https://peps.python.org/pep-0779/
- JEP 491 (delivered in Java 24): https://openjdk.org/jeps/491 ; Java 27 GA coverage (InfoQ, Sep 2026): https://www.infoq.com/news/2026/09/java-news-roundup-sep14-2026/
- Fastify lifecycle (v5): https://fastify.dev/docs/latest/Reference/Lifecycle/ ; FastAPI 0.143.0 (8 Oct 2026): https://pypi.org/project/fastapi/
- HikariCP pool sizing: https://github.com/brettwooldridge/HikariCP/wiki/About-Pool-Sizing
- Discord, *Why Discord is switching from Go to Rust* (Feb 2020): https://discord.com/blog/why-discord-is-switching-from-go-to-rust
- OpenAI on scaling PostgreSQL (Jan 2026), original https://openai.com/index/scaling-postgresql/ , as reported by VentureBeat (23 Jan 2026): https://venturebeat.com/data/how-openai-is-scaling-the-postgresql-database-to-800-million-users
- Stack Overflow Developer Survey 2025, technology: https://survey.stackoverflow.co/2025/technology

_Last reviewed: 2026-10_
