# BE404 · Labs and projects

Labs run on a local multi-node Kubernetes cluster (kind or k3d) with Envoy, Istio (sidecar and ambient modes) or Linkerd, the Kubernetes Gateway API, an OpenTelemetry Collector with Jaeger or Tempo, a Pact broker and Backstage. A provided "monolith" (a food-delivery application with orders, menus, payments, delivery and notifications in one codebase) is the raw material for most labs. Lab 8 and the live architecture review are done without AI assistants.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Event storming and context map | Find bounded contexts in the provided monolith's domain | Event-storming board, context map with integration patterns, and ownership per team | 5 h |
| 2 · Strangler extraction | Extract the notifications capability behind a routing layer; move its data with expand/contract | Rollout log from 1% to 100% with error rates, plus a rollback rehearsal | 8 h |
| 3 · Composition vs CQRS | Build "order details" from four services by API composition and by a CQRS view | Latency, freshness and failure behaviour of each, with a recommendation | 5 h |
| 4 · Hand-configured Envoy | Listeners, routes and clusters for two services; outlier detection; a 5% canary with automatic rollback | Envoy config, canary script, and a rollback triggered by an injected error rate | 5 h |
| 5 · Sidecar vs ambient mesh | The same workload with no mesh, Istio sidecars and Istio ambient (or Linkerd); mTLS and service-to-service allowlists | p50/p99 latency and memory per pod for each mode; tests that unapproved calls are denied | 8 h |
| 6 · Gateway API | Replace an Ingress with Gateway API resources split between a platform team and two app teams | Manifests, RBAC, and a demonstration that an app team cannot change another team's routes | 4 h |
| 7 · Contract testing | Pact contracts between three services; provider verification in CI; `can-i-deploy` gate | A pipeline run blocking an incompatible provider change | 5 h |
| 8 · Tracing investigation (no AI) | Find a planted cross-service latency regression using traces, exemplars and tail sampling | Root cause, evidence screenshots, and the fix, within a 60-minute time box | 4 h |
| 9 · Resilience across hops | Show retry amplification across three layers; fix with single-layer retries and budgets; degrade gracefully when a non-critical service is down | Before/after load-test results and a dependency-failure demo | 6 h |

## Projects

### P1 · Modular monolith with enforced boundaries (L1, ~6 hours)

**Real-world inspiration:** Shopify keeps a very large Rails monolith and enforces module boundaries with Packwerk ([Shopify Engineering](https://shopify.engineering/shopify-monolith)). Segment returned to a single service after running more than 140 ([Segment, 2018](https://www.twilio.com/en-us/blog/developers/best-practices/goodbye-microservices)).

**What to build:** refactor the provided monolith into modules that follow your Lab 1 context map. Use Packwerk, Spring Modulith, ArchUnit, import-linter or Go internal packages. Each module gets a public interface, private internals and its own tables. Cross-module calls go only through public interfaces or in-process domain events.

**Acceptance criteria:**
- A boundary checker runs in CI and fails on a planted violation (a direct import of another module's internals, and a query on another module's tables).
- Zero existing violations remain, or each remaining one is listed in a dated "debt" file with an owner.
- All existing tests still pass, and an end-to-end order flow works unchanged.
- Every module has a one-page README with its responsibility, public API, events it publishes and data it owns.
- A decision record explains which module would be extracted first and the evidence that would justify it.

**Stretch goals:** generate a dependency graph from the code and compare it with your context map; publish module events through an in-process bus that could later become Kafka.

**What it proves to an employer:** you can get most of the benefits of microservices without paying their costs, and you know when that stops being enough.

### P2 · Extract two services with a mesh and contracts (L2, ~15 hours)

**Real-world inspiration:** the strangler fig pattern and incremental data migration, plus mesh-level identity and allowlists as Monzo applies across its 1,500+ services ([Monzo, 2019](https://monzo.com/blog/we-built-network-isolation-for-1-500-services)).

**What to build:** extract the delivery and notifications contexts from the P1 modular monolith into two services:
- **Data:** each gets its own database, moved with expand/contract and CDC.
- **Communication:** delivery is called synchronously over gRPC with deadlines, and notifications is fed by outbox events (BE304).
- **Mesh:** run everything in a mesh with mTLS and default-deny allowlists, and route traffic with the Gateway API.
- **Contracts:** Pact covers the HTTP and gRPC interfaces, and a schema registry covers the events.
- **Observability:** add tracing across all hops.

**Acceptance criteria:**
- **Zero-downtime extraction:** a k6 run at 500 requests/s across the whole extraction shows zero failed requests and p99 within 25% of the monolith baseline.
- **Data ownership:** after cut-over, no service reads another's tables. A database permission audit proves the monolith's role cannot access the extracted schemas.
- **Independent deploy:** each service deploys alone through a pipeline gated by contract tests. A planted incompatible change is blocked before deploy.
- **Security:** the network allowlist blocks every call not in the approved list (tested for all service pairs), and mTLS is enforced (a plaintext call fails).
- **Traces:** one trace shows an order from the gateway through the monolith, delivery (gRPC) and notifications (via Kafka), with queue wait time visible.
- **Write-up:** mesh overhead (latency, CPU, memory) measured, and a recommendation on whether this system needs the mesh.

**Stretch goals:** repeat with ambient mode and compare; add a canary for the delivery service driven by SLO burn rate; shadow-traffic diffing before cut-over.

**What it proves to an employer:** you can carve services out of a live system safely and give them the identity, contracts and observability that make independence real.

### P3 · Internal developer platform with a golden path (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** platform teams publish golden paths through software catalogs and templates. Backstage is the CNCF incubating project most used for this ([CNCF](https://www.cncf.io/projects/backstage/)). Uber's domain gateways ([Uber, 2020](https://www.uber.com/blog/microservice-architecture/)) show how platform-level conventions tame thousands of services. The organization in this project is an **illustrative scenario**.

**What to build:** a small internal developer platform on your cluster:
- **Catalog:** Backstage with every P2 service, owners, APIs and dependencies.
- **Template:** a "new service" golden path that creates a repository from your BE302 chassis, wired with CI, contract tests, OpenTelemetry, mesh enrolment, Gateway API routes and SLO dashboards.
- **Platform APIs:** declarative custom resources for `Database` and `Topic`, with controllers that provision Postgres schemas and Kafka topics with safe defaults, quotas and owners.
- **Scorecards:** checks for tracing, SLOs, contract tests, and no critical vulnerabilities.
- **Deprecation:** migration tooling for one deprecated platform feature.
- **Agent access:** an MCP tool interface that lets an AI agent request a new service or database, with human approval for anything touching production.

**Acceptance criteria:**
- **Time to first deploy:** a new developer, observed, creates a service from the template and deploys it to staging with tracing, contracts and dashboards working in under 30 minutes.
- **Declarative APIs:** applying a `Database` resource twice changes nothing (idempotent). Deleting it follows a documented retention policy. Manual drift is reconciled within 60 seconds.
- **Guardrails:** requests over quota or without an owner are rejected with actionable messages. The scorecard flags a planted service missing SLOs.
- **Agent safety:** in a 20-task agent suite, the agent completes at least 90% of staging tasks and makes zero production changes without an approval record. Every action is in the audit log.
- **Migration:** ten generated services move off a deprecated platform API using your codemod, with zero failed deploys.
- **Platform reliability:** the platform's own controllers have SLOs, and a controller crash during reconciliation leaves no half-provisioned resources (tested with 50 kills).
- **Write-up:** a platform product document (users, golden paths, metrics), architecture, and a review of what you would not build.

**Stretch goals:** policy as code for platform requests (OPA or Kyverno); cost showback per team; a second golden path for event-driven services.

**What it proves to an employer:** you can build the platform other engineers build on. That is senior and staff-level leverage, and it is hard to automate away.

## Feeds into

- [BE501 Frontier Seminar](../../year_5/BE501_frontier_seminar_durable_execution_serverless/README.md): durable execution, serverless and edge as platform primitives.
- [OV02 Cloud-Native Backend](../../../../04_overlaps/OV02_cloud_native_backend/README.md) and [OPS401 Platform Engineering and Internal Developer Platforms](../../../devops_sre_platform_engineering/year_4/OPS401_platform_engineering_and_internal_developer/README.md).
- The [Backend Engineering flagship industry project](../../../../06_career_and_market_readiness/05_industry_projects/BE_backend_engineering.md).
