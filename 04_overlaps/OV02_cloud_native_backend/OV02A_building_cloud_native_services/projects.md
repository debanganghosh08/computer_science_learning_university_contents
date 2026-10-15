# OV02A · Labs and projects

All labs use the course order service (Go, Java or Python) with PostgreSQL and Kafka, run on kind or k3d locally and on one small managed cluster for the scaling and zone labs. Every lab ships code, a test or experiment that proves the claim, and measured numbers. Tear down cloud resources after each session.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Course service skeleton | Scaffold the service with REST and gRPC endpoints, a Kafka outbox and a local cluster setup; audit it against the twelve factors | Repo, twelve-factor audit, ADR on service boundaries | 4 h |
| 2 · Zero-drop restarts | Implement probes, SIGTERM handling, readiness flip and `preStop`; run 50 rolling restarts under k6 load | Failed-request count before and after (target 0), latency chart | 5 h |
| 3 · No static keys | Move configuration to validated layers, secrets to External Secrets, and cloud access to workload identity | Diff showing removed keys; proof the pod reaches its bucket and nothing else | 4 h |
| 4 · Connection storms and migrations | Reproduce pool exhaustion at scale-out; add PgBouncer; rename a column with expand-contract under load | Before/after error rates, pool-sizing calculation, migration log with zero errors | 6 h |
| 5 · Fault injection | Add deadlines, retry budgets, a circuit breaker and load shedding; inject latency and errors with Toxiproxy or a mesh fault filter | Experiment table: fault × user-visible error rate × p99, with and without each pattern | 6 h |
| 6 · gRPC balancing and routing | Show per-pod imbalance for gRPC behind a ClusterIP Service; fix with client-side balancing or a proxy; header-based routing with Gateway API | Load distribution charts, route configuration | 4 h |
| 7 · Traces and SLOs | OpenTelemetry across HTTP, gRPC and Kafka; RED dashboard with exemplars; two SLOs with burn-rate alerts; a drill that fires one | Trace screenshot of one order end to end, SLO definitions, alert evidence | 5 h |
| 8 · Scaling under spikes | Compare HPA on CPU, RPS and Kafka lag (KEDA) under the same spike; keep p99 stable through node consolidation | Scaling timelines, p99 during each event, chosen signal with reasons | 5 h |
| 9 · Canary with auto-rollback | Argo CD plus Argo Rollouts with Prometheus analysis; ship a planted regression | Rollout history showing automatic rollback, analysis template | 4 h |
| 10 · Cells | Split the service into two cells behind a router with tenant-to-cell mapping; drain one cell | Routing design, drain run with SLO graph | 5 h |

## Projects

### P1 · The well-behaved service (L1, ~6 hours)

**Real-world inspiration.** Platform teams publish a "service contract" (probes, shutdown, telemetry, resource sizing) because a handful of misbehaving services cause most deploy-time incidents on shared clusters.

**What to build.** A service template (repository template or cookiecutter) that produces a new service which honours the platform contract out of the box.

**Acceptance criteria**
- A generated service passes 50 rolling restarts under 200 requests per second with 0 failed requests.
- Liveness does not depend on downstream services; a test kills the database and shows no restart loop.
- Logs are structured JSON with trace IDs; a default dashboard and one SLO are created by the template.
- Requests and limits are derived from a documented load-test method included in the template.
- The template README lists every platform expectation and how the template meets it.

**Stretch goals.** Generate the service from a Backstage scaffolder template; add a startup self-check of configuration.

**What it proves to an employer.** You understand the contract between a service and its platform, and you can encode it for other engineers.

### P2 · Resilience under failure (L2, ~15 hours)

**Real-world inspiration.** The AWS Builders' Library documents how retries without budgets and jitter turn small failures into outages; Slack's cellular work shows the value of containing failure to one zone. The fault scenarios here are illustrative.

**What to build.** A three-service chain (gateway → orders → payments simulator) with deadlines, idempotency keys, retry budgets, circuit breakers, bulkheads and load shedding, plus an automated fault-injection suite that runs in CI against an ephemeral cluster.

**Acceptance criteria**
- The suite runs at least 8 fault scenarios (latency, errors, dropped connections, database failover, broker outage, pod kills, CPU starvation, dependency returning slow 200s).
- For each scenario the report shows user-visible error rate and p99 with and without the protections; protections reduce user-visible errors by at least 80% in at least 6 scenarios.
- No duplicate payments across 10,000 requests with retries enabled (verified by a ledger check).
- Total retry traffic never exceeds 10% of base traffic during any scenario (retry budget evidence).
- Each scenario has a one-paragraph explanation of the mechanism, not just the numbers.

**Stretch goals.** Compare library-based resilience with mesh-based retries and outlier detection on the same suite.

**What it proves to an employer.** You can design for failure and prove it with experiments, which is what senior backend interviews probe.

### P3 · Production-grade order service (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** Indian food-delivery and quick-commerce platforms face extreme peaks (festivals, cricket matches, sales), and Disney+ Hotstar has described pre-scaling its Kubernetes infrastructure ahead of live events. The system below is illustrative.

**What to build.** The order service as a production candidate: GitOps delivery with canary analysis, autoscaling on the right signal, two cells, SLOs and alerts, zero static credentials, signed images, a cost model and a production readiness review pack.

**Acceptance criteria**
- At 300 orders per second for 15 minutes, p99 order creation < 400 ms and error rate < 0.1% on a stated cluster.
- A spike from 50 to 500 orders per second within 60 seconds keeps error rate < 1% (pre-scaling allowed if documented as a runbook).
- A zone or cell evacuation completes with no SLO breach; a node upgrade of the whole pool completes with 0 failed requests.
- A faulty release is rolled back automatically within 10 minutes of rollout start.
- Cost per 1,000 orders is reported at three traffic levels; one optimisation cuts it by ≥ 15% without breaching SLOs.
- The readiness pack (ownership, SLOs, runbooks for five failure modes, dashboards, load and failure evidence) passes a review by a classmate using a published checklist.

**Stretch goals.** Active-passive second region with a measured failover RTO; an AI feature behind a per-tenant budget and fallback.

**What it proves to an employer.** You can own a service in production on Kubernetes, the most common senior backend job shape.

## Feeds into

- [OV02B Event-Driven Serverless Backends](../OV02B_event_driven_serverless_backends/README.md): the order service becomes the synchronous core of the event-driven system.
- The [OV02 capstone](../README.md): P3 is its Kubernetes half.
- [BE501 Frontier Seminar: Durable Execution, Serverless and Edge Backends](../../../03_majors/backend_engineering/year_5/BE501_frontier_seminar_durable_execution_serverless/README.md): cells and resilience experiments become research questions.
- [OV01B Kubernetes and Container Security](../../OV01_cloud_security/OV01B_kubernetes_and_container_security/README.md) and [OV03 DevSecOps](../../OV03_devsecops/README.md): the service is a realistic target for hardening and supply-chain controls.
