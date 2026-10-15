# OV02A · Building Cloud-Native Services

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 7 | 4 (≈ 120 hours) | L3 → L4 | [BE301](../../../03_majors/backend_engineering/year_3/BE301_api_design_rest_grpc_and_graphql/README.md), [BE304](../../../03_majors/backend_engineering/year_3/BE304_asynchronous_systems_queues_streams_and_event/README.md), [CLD303](../../../03_majors/cloud_engineering/year_3/CLD303_containers_and_kubernetes/README.md) | [OV02B](../OV02B_event_driven_serverless_backends/README.md), [BE501](../../../03_majors/backend_engineering/year_5/BE501_frontier_seminar_durable_execution_serverless/README.md), [THS501](../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) |

Part of the [OV02 Cloud-Native Backend overlap](../README.md). BE301 taught API contracts, BE304 messaging semantics and CLD303 the Kubernetes platform. This course builds one realistic service on all three and operates it as if it were yours in production.

## Why this course matters now

82% of container users now run Kubernetes in production ([CNCF, Jan 2026](https://www.cncf.io/reports/the-cncf-annual-cloud-native-survey/)), so "backend engineer" increasingly means "engineer whose service runs on a shared, constantly changing platform". Pods are killed during node upgrades, autoscalers add and remove replicas every minute, and every call crosses a network that sometimes fails. The architecture debate has also matured: Segment publicly consolidated more than 140 services back into a single service in 2018 ([Twilio Segment](https://www.twilio.com/en-us/blog/developers/best-practices/goodbye-microservices)), while Slack made each availability zone a drainable cell so that a failure in one zone stays in that zone ([Slack Engineering, Aug 2023](https://slack.engineering/slacks-migration-to-a-cellular-architecture/)). The lesson is that boundaries and failure isolation matter more than service count. AI coding agents (Claude Code, GitHub Copilot, Cursor) now produce a working service, Dockerfile and Helm chart in minutes; they rarely get graceful shutdown, retry budgets, connection-pool arithmetic or cost right. Those are the skills this course trains.

## Learning outcomes

By the end you can:

1. **Build** a service that honours the platform contract: correct probes, graceful shutdown with zero dropped requests, container-aware runtime settings, and logs, metrics and traces by default.
2. **Configure** a service with layered configuration, feature flags, external secrets and workload identity, with no static credentials.
3. **Operate** a relational database behind an autoscaled service without connection exhaustion, and **ship** schema changes with zero downtime.
4. **Apply** timeouts, deadlines, retries with budgets, circuit breakers, bulkheads and load shedding, and **prove** their effect with fault injection.
5. **Choose and justify** service-to-service communication (HTTP, gRPC, mesh, Dapr) for a given latency and reliability target.
6. **Scale** a service on the right signal and **measure** latency during scale-out, node consolidation and upgrades.
7. **Deliver** changes by GitOps and canary with automated analysis, and **roll back** without manual action.
8. **Design** tenant isolation, cells and a multi-region strategy, and **state** the cost per request of each choice.

## Chapters and lessons

### Chapter 1 · What "cloud-native" asks of a service (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 The definitions that matter | The Twelve-Factor App (open-sourced for community revision in November 2024): config in the environment, disposability, backing services as attached resources, logs as event streams | Audit an existing service against the twelve factors; list three violations |
| 1.2 The platform contract | What Kubernetes promises a service and what it expects: signals, probes, resource accounting, ephemeral filesystems, identity | Write the "platform contract" one-pager for the course service |
| 1.3 How many services? | Monolith, modular monolith, services; Segment's 2018 return to a monolith; domain-oriented boundaries over service count (deep dive in BE404) | Argue for and against splitting the course service; record the decision as an ADR |
| 1.4 The course service | An illustrative order service in Go, Java or Python: REST and gRPC APIs, PostgreSQL, Kafka outbox (from BE304) | Scaffold it with tests and a local Kubernetes environment |

**Check your understanding:** Which twelve-factor rule do AI-generated services break most often, and why? What does "disposable" require of a service that holds in-flight work? When is a modular monolith the most cloud-native choice?

### Chapter 2 · Running well on Kubernetes (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Probes with meaning | Startup, readiness and liveness semantics; why liveness must not check dependencies; readiness during warm-up and overload | Show a cascading restart caused by a dependency-checking liveness probe, then fix it |
| 2.2 Graceful shutdown | SIGTERM handling, readiness flip, `preStop` delay for endpoint propagation, draining in-flight requests and consumer offsets, `terminationGracePeriodSeconds` | Achieve zero failed requests during 50 rolling restarts under load |
| 2.3 Runtimes in containers | `GOMAXPROCS` and CPU limits, container-aware JVM memory, Python worker counts; CPU throttling in CFS quotas; OOMKilled diagnosis | Measure p99 latency with and without CPU limits for one runtime |
| 2.4 Requests and limits from evidence | Sizing from load tests, not guesses; QoS classes; in-place pod resize (stable since v1.35) | Derive requests from a load test; document the method |

**Check your understanding:** Why can a liveness probe turn a slow database into a total outage? What happens to a request that arrives after SIGTERM but before the endpoint is removed? Why can a CPU limit raise tail latency even at low average CPU?

### Chapter 3 · Configuration, secrets and identity (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Configuration layering | Defaults, environment config, per-tenant config; validation at startup; config changes as deploys | Fail startup on invalid configuration with a clear message |
| 3.2 Feature flags | OpenFeature API, kill switches, flag lifecycle and debt | Ship a feature dark and enable it per tenant |
| 3.3 Secrets | External Secrets Operator or CSI driver, rotation without restarts, never in images or Git | Rotate the database password with no failed requests |
| 3.4 Workload identity | EKS Pod Identity or IRSA, GKE Workload Identity Federation, Azure Workload Identity; SPIFFE identities for service-to-service authentication | Remove every static cloud key from the service |

**Check your understanding:** Why should invalid configuration crash a pod at startup rather than at first use? What makes a feature flag a liability? What does workload identity remove from your incident response plan?

### Chapter 4 · Data behind autoscaled services (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Managed database or operator | Managed PostgreSQL versus CloudNativePG on Kubernetes; failover behaviour seen by the application | Measure application errors during a managed failover |
| 4.2 Connection arithmetic | Pods × pool size ≤ `max_connections`; PgBouncer and RDS Proxy; pool sizing from latency and concurrency | Reproduce connection exhaustion at scale-out, then fix it |
| 4.3 Zero-downtime schema change | Expand-contract, backfills in batches, migrations as Kubernetes Jobs, lock timeouts | Rename a column under load with zero errors |
| 4.4 Caches | Cache-aside with Valkey, stampede protection, invalidation on events, cache as a dependency that can fail | Survive a cache flush at peak load without database overload |

**Check your understanding:** Your service scales from 10 to 60 pods; what happens to the database, and what should have prevented it? Why must every migration be backward compatible with the previous release? When does a cache make an outage worse?

### Chapter 5 · Resilience patterns (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Timeouts and deadlines | Deadline propagation (gRPC deadlines, header-based budgets), timeouts shorter downstream than upstream | Find and fix a timeout inversion in a three-service chain |
| 5.2 Retries that do not kill you | Exponential backoff with jitter, retry budgets, idempotency requirements (from BE301); the AWS Builders' Library guidance | Show a retry storm, then cap it with a budget |
| 5.3 Breakers, bulkheads, shedding | Circuit breakers, per-dependency concurrency limits, adaptive load shedding, priority traffic | Keep one endpoint healthy while its sibling's dependency fails |
| 5.4 Where the logic lives | Library (resilience4j, Polly, Go middleware) versus proxy (Envoy outlier detection) versus gateway; avoiding double retries | Map every retry layer in the course system; remove duplicates |

**Check your understanding:** Why do retries at every layer multiply load? What makes a request safe to retry? How does a circuit breaker change what users see during an outage?

### Chapter 6 · Service-to-service communication (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 gRPC on Kubernetes | HTTP/2 long-lived connections and L4 load-balancing imbalance; headless services, client-side balancing, xDS | Measure per-pod load imbalance with and without a fix |
| 6.2 Gateway API for services | HTTPRoute and GRPCRoute for north-south and east-west traffic, timeouts and retries in routes | Route 10% of traffic by header to a new version |
| 6.3 Mesh or no mesh | mTLS, retries and telemetry from Istio ambient or Linkerd; cost and failure modes (deep dive in BE404) | Write a one-page decision for your system |
| 6.4 Building blocks with Dapr | Dapr (CNCF graduated November 2024): pub/sub, state, workflow, service invocation; portability against lock-in | Replace direct Kafka calls with Dapr pub/sub; compare code and latency |

**Check your understanding:** Why does a Kubernetes Service not balance gRPC requests evenly? What does a mesh give you that a library cannot? When is Dapr's abstraction a cost rather than a benefit?

### Chapter 7 · Observability built in (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 OpenTelemetry in the service | SDK and auto-instrumentation (OpenTelemetry Operator), resource attributes, context propagation over HTTP, gRPC and Kafka headers | Trace one order across HTTP, Kafka and a consumer |
| 7.2 Metrics that answer questions | RED metrics, histograms and exemplars, cardinality budgets | Build the service dashboard with exemplar links to traces |
| 7.3 Logs | Structured logs with trace IDs, sampling, PII redaction | Find a failed order from a user complaint in under two minutes |
| 7.4 SLOs for a service | Availability and latency SLIs from the user's view, error budgets, multi-window burn-rate alerts (from OPS303 and OPS304) | Define two SLOs and alerts; trigger one in a drill |

**Check your understanding:** Which label would blow up your metrics bill, and how would you notice? Why measure SLIs at the edge rather than in the pod? What is a burn-rate alert protecting you from?

### Chapter 8 · Scaling and performance (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Scaling signals | HPA on CPU versus requests per second versus queue lag (KEDA); stabilisation windows | Compare three scaling signals under the same spike |
| 8.2 Node dynamics | Karpenter or Cluster Autoscaler consolidation, PodDisruptionBudgets, topology spread across zones | Keep p99 stable through a node consolidation event |
| 8.3 Load testing | k6 scenarios, open versus closed workload models, realistic payloads | Find the service's knee point and its limiting resource |
| 8.4 Cold capacity | Image pull time, JIT warm-up, startup CPU; pre-scaling for known peaks (sales, cricket matches) | Cut time-to-ready of a new pod by half |

**Check your understanding:** Why can CPU-based autoscaling react too late for a payments spike? What does a PodDisruptionBudget protect, and what can it block? Why does a closed-model load test hide queueing?

### Chapter 9 · Delivery for services (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 GitOps for one service | Image built once, promoted by digest; Argo CD sync; environment repos (from OPS301 and OPS305) | Promote a release from staging to production by pull request |
| 9.2 Canary with analysis | Argo Rollouts with Prometheus analysis; what to measure; bake time | Auto-rollback a planted latency regression |
| 9.3 Contract tests | Consumer-driven contracts with Pact; breaking-change checks with oasdiff and buf | Block a breaking API change in CI |
| 9.4 Inner loop | Tilt or Skaffold for local Kubernetes development; ephemeral preview environments | Measure edit-to-running time before and after |

**Check your understanding:** Why rebuild nothing between staging and production? Which metric would have caught your last bug in a canary? What does a contract test catch that an integration test misses?

### Chapter 10 · Tenants, cells and regions (weeks 10–11)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Tenant isolation in a service | Tenant context propagation, per-tenant rate limits and quotas, noisy-neighbour detection | Stop one tenant from degrading others under a load test |
| 10.2 Cell-based architecture | Cells as blast-radius boundaries, cell routers, shuffle sharding; AWS's cell-based architecture guidance; Slack's cellular migration | Split the service into two cells behind a router |
| 10.3 Multi-region options | Active-passive and active-active; data choices (Aurora Global Database, Spanner, DynamoDB global tables) and their consistency | Write the multi-region design with RPO and RTO |
| 10.4 Evacuation drills | Draining a zone or cell, failover runbooks, testing failback | Evacuate one zone in the lab with no SLO breach |

**Check your understanding:** What does a cell protect that multi-AZ does not? Why is active-active hard for an order service but easy for a catalogue? What would you test first in a regional failover?

### Chapter 11 · Security and cost of a service (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Secure defaults | Non-root images, restricted Pod Security, NetworkPolicy, signed images (detail in OV01B and OV03A) | Make the service pass the restricted profile |
| 11.2 Dependency hygiene | Renovate or Dependabot with tests, SBOMs, update SLAs | Merge a week of dependency updates safely |
| 11.3 Cost per request | Requests versus usage, idle replicas, cross-zone traffic charges, NAT and load-balancer costs; OpenCost by namespace | Compute cost per 1,000 orders and cut it by 20% |
| 11.4 Right-sizing safely | VPA recommendations, bin-packing, Spot for stateless pods with disruption handling | Move half the replicas to Spot with no SLO breach |

**Check your understanding:** Which cloud network charge surprises service teams most? Why can lower requests raise cost? What does a Spot interruption look like to a well-built service?

### Chapter 12 · AI and the service lifecycle (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Reviewing AI-built services | A review checklist: shutdown, probes, timeouts, retries, idempotency, pool sizes, limits, identity, telemetry | Review an AI-generated service and fix every defect found |
| 12.2 Calling models from a service | Timeouts, streaming, fallbacks and per-tenant budgets for model APIs (detail in BE403) | Add an AI feature with a cost cap and a fallback |
| 12.3 Agents as API clients | Agents calling your API through MCP or function calling; scoped credentials, rate limits, dry runs (from BE301 Chapter 11) | Expose two safe, idempotent tools from the service |
| 12.4 Production readiness review | Ownership, SLOs, runbooks, dashboards, load and failure test evidence | Pass a production readiness review run by a classmate |

**Check your understanding:** Which defect would an AI reviewer most likely miss in a Kubernetes manifest, and why? Why must an agent-facing endpoint be idempotent? What evidence should a readiness review demand instead of claims?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Course service skeleton | ADR on service boundaries |
| 2 | 2 | Lab 2 · Zero-drop restarts | — |
| 3 | 3 | Lab 3 · No static keys | — |
| 4 | 4 | Lab 4 · Connection storms and migrations | **P1 due** |
| 5 | 5 | Lab 5 · Fault injection | — |
| 6 | 6 | Lab 6 · gRPC balancing and routing | Mid-term (AI off): failure-mode design review |
| 7 | 7 | Lab 7 · Traces and SLOs | — |
| 8 | 8 | Lab 8 · Scaling under spikes | Load-test report |
| 9 | 9 | Lab 9 · Canary with auto-rollback | **P2 due** |
| 10 | 10 | Lab 10 · Cells | — |
| 11 | 10 | Zone evacuation drill | Multi-region design |
| 12 | 11 | Cost and Spot | Cost report |
| 13 | 12 | AI review exercise | — |
| 14 | 12 | Production readiness review | **P3 due** |
| 15 | Review | Live failure drill and oral defence of P3 | Final exam |

## Working with AI in this course

- **Use AI for:** scaffolding services, Dockerfiles, Helm charts and Kubernetes manifests; writing k6 scripts and fault-injection scenarios; explaining traces and flame graphs; drafting ADRs for you to edit.
- **Do without AI (drills):** graceful-shutdown sequences and timeout budgets worked out by hand; connection-pool arithmetic; reading a trace to find a bottleneck; the mid-term design review and the final failure drill.
- **Verify AI output by:** running the zero-drop restart test, the fault-injection suite and a load test on every AI-generated change; checking manifests against restricted Pod Security and your policies; confirming every retry is on an idempotent operation.
- **Where AI still fails here:** log each AI-generated service defect you find with the test that caught it. Expect missing SIGTERM handling, liveness probes that call the database, retries on non-idempotent POSTs, and pool sizes copied from examples.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1–P3 | 35% |
| Mid-term design review (AI off) | 10% |
| Final: live failure drill + oral defence of P3 | 30% |

**Mastery gate.** You pass when you can, with AI tools off: (1) given a service and a failure description (retry storm, connection exhaustion, dropped requests during deploys), find the cause within 30 minutes using its telemetry; (2) design timeouts, retries and pool sizes for a three-service chain and justify every number; (3) take your P3 service through a rolling upgrade, a zone evacuation and a canary rollback with no SLO breach.

## Industry reality

Public engineering writing shows these problems are everyday ones: Slack's cellular migration was driven by zone-level failures in a multi-AZ system; Segment's monolith reversal was driven by operational load, not by technology fashion; Disney+ Hotstar's scaling posts describe pre-scaling for cricket peaks ([Hotstar](https://blog.hotstar.com/scaling-infrastructure-for-millions-from-challenges-to-triumphs-part-1-6099141a99ef)). Interviewers probe the same ground in system-design and "debug this production issue" rounds.

**Interview questions from this course**

1. *During every deploy we see a burst of 502s. Why, and how do you fix it?* Strong answer: requests routed to pods after SIGTERM or before readiness; fixes are readiness flip plus `preStop` delay, draining in-flight work, correct `terminationGracePeriodSeconds`, and a test that proves zero drops.
2. *Our service autoscaled during a sale and the database fell over. What happened?* Strong answer: connection pools multiplied by replicas; fixes with a pooler, pool sizing from concurrency, caps on replicas or a queue, load shedding, and monitoring of connections as a saturation signal.
3. *Design timeouts and retries for gateway → orders → payments.* Strong answer: end-to-end deadline, decreasing timeouts downstream, retries only on idempotent operations with idempotency keys, jittered backoff, a retry budget, a circuit breaker on payments, and what the user sees on failure.
4. *When would you not use a service mesh?* Strong answer: small number of services, team without capacity to run it, latency-sensitive paths, or needs met by libraries and Gateway API; names the operational failure modes of sidecars and the ambient alternative.
5. *How would you make the order service survive a zone loss without a full multi-region build?* Strong answer: multi-AZ replicas with topology spread and PDBs, a multi-AZ database with tested failover, static stability (no control-plane calls needed), zone-evacuation drills, and cells to limit blast radius.

## Resources (free first)

- **Methodology:** The Twelve-Factor App — https://12factor.net/ ; AWS Builders' Library, "Timeouts, retries, and backoff with jitter" — https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/ ; AWS, "Reducing the Scope of Impact with Cell-Based Architecture" — https://docs.aws.amazon.com/wellarchitected/latest/reducing-scope-of-impact-with-cell-based-architecture/reducing-scope-of-impact-with-cell-based-architecture.html ; Google SRE books (free online) — https://sre.google/books/
- **Documentation:** Kubernetes pod lifecycle and termination — https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/ ; Gateway API — https://gateway-api.sigs.k8s.io/ ; OpenTelemetry — https://opentelemetry.io/docs/ ; Dapr — https://docs.dapr.io/ ; Argo Rollouts — https://argoproj.github.io/argo-rollouts/ ; KEDA — https://keda.sh/docs/ ; OpenFeature — https://openfeature.dev/ ; Pact — https://docs.pact.io/ ; k6 — https://grafana.com/docs/k6/latest/
- **Case studies:** Slack's cellular architecture — https://slack.engineering/slacks-migration-to-a-cellular-architecture/ ; Segment's "Goodbye Microservices" — https://www.twilio.com/en-us/blog/developers/best-practices/goodbye-microservices
- **Paid, optional:** Sam Newman, *Building Microservices*, 2nd ed. (O'Reilly, 2021); Martin Kleppmann, *Designing Data-Intensive Applications* (2nd ed. in progress). The free sources above cover the course.

## Sources

All checked 12 Oct 2026.

- CNCF Annual Cloud Native Survey (20 Jan 2026) — https://www.cncf.io/reports/the-cncf-annual-cloud-native-survey/
- Twilio Segment, "Goodbye Microservices: From 100s of problem children to 1 superstar" (2018) — https://www.twilio.com/en-us/blog/developers/best-practices/goodbye-microservices
- Slack Engineering, "Slack's Migration to a Cellular Architecture" (2023) — https://slack.engineering/slacks-migration-to-a-cellular-architecture/
- The Twelve-Factor App, "Twelve-Factor App Methodology is now Open Source" (12 Nov 2024) — https://12factor.net/blog/open-source-announcement
- CNCF, Dapr graduation (12 Nov 2024) — https://www.cncf.io/announcements/2024/11/12/cloud-native-computing-foundation-announces-dapr-graduation/
- Kubernetes blog, in-place pod resize GA in v1.35 (19 Dec 2025) — https://kubernetes.io/blog/2025/12/19/kubernetes-v1-35-in-place-pod-resize-ga/
- Disney+ Hotstar, "Scaling Infrastructure for Millions", part 1 — https://blog.hotstar.com/scaling-infrastructure-for-millions-from-challenges-to-triumphs-part-1-6099141a99ef

_Last reviewed: 2026-10_
