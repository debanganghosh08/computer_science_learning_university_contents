# BE404 · Microservices, Service Mesh and Platform APIs

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 8 | 4 (≈ 120 hours) | L3 → L4 | [BE304](../../year_3/BE304_asynchronous_systems_queues_streams_and_event/README.md) (also uses [BE301](../../year_3/BE301_api_design_rest_grpc_and_graphql/README.md), [BE302](../../year_3/BE302_backend_frameworks_and_service_internals/README.md), [BE305](../../year_3/BE305_authentication_authorization_and_backend/README.md)) | [BE501](../../year_5/BE501_frontier_seminar_durable_execution_serverless/README.md), [OV02](../../../../04_overlaps/OV02_cloud_native_backend/README.md), [OPS401](../../../devops_sre_platform_engineering/year_4/OPS401_platform_engineering_and_internal_developer/README.md) |

Part of the [Backend Engineering major](../../README.md). Assumes Kubernetes basics from [CS215](../../../../02_year_2_core_computer_science/semester_4/CS215_cloud_and_devops_foundations/README.md); [CLD303 Containers and Kubernetes](../../../cloud_engineering/year_3/CLD303_containers_and_kubernetes/README.md) is a strongly recommended elective before this course.

## Why this course matters now

The industry has spent a decade learning when not to use microservices, and the evidence is public:
- **Segment** merged more than 140 services back into one in 2018.
- **Amazon Prime Video** moved an audio and video monitoring service from serverless microservices into a single process on ECS, and reported a 90% cut in costs (2023).
- **Istio** merged its own control-plane microservices into one binary, `istiod`, in 2020, explaining that the usual benefits did not apply.
- **Uber** organized about 2,200 critical microservices into roughly 70 domains with layers and gateways (2020).
- **Monzo** runs more than 1,500 services and limits each to an approved list of callers.

The tools kept moving. Istio's sidecar-less ambient mode became generally available in November 2024. Linkerd stopped publishing open-source stable releases in February 2024; edge releases are open source and stable builds come from vendors. Kubernetes Gateway API now covers both ingress and mesh traffic. Google archived Service Weaver, its "modular monolith deployed as microservices" framework, in March 2026. AI agents can generate a new service, a Helm chart and mesh configuration in minutes. The expensive decisions still fall to a backend engineer: where the boundaries go, who owns which data, how services fail together, and what the platform should make easy.

## Learning outcomes

By the end you can:

1. **Decide** between a monolith, a modular monolith and microservices for a stated organization and product, and **defend** the decision with costs and named case studies.
2. **Find** service boundaries with domain-driven design (bounded contexts, aggregates, context maps, event storming), and **map** them to team ownership.
3. **Extract** services from a monolith safely with the strangler fig pattern, branch by abstraction and data migration by expand/contract.
4. **Design** inter-service communication (synchronous, asynchronous, API composition, CQRS views) that avoids a distributed monolith.
5. **Operate** service discovery and a service mesh (Envoy, Istio sidecar and ambient modes, Linkerd), and **measure** what the mesh costs in latency and resources.
6. **Configure** API gateways and the Kubernetes Gateway API for north–south and east–west traffic, keeping business logic out of the gateway.
7. **Implement** consumer-driven contract testing (Pact) and compatibility checks that let services deploy independently.
8. **Trace** requests across services with OpenTelemetry and W3C Trace Context, and **set** SLOs per user journey.
9. **Apply** resilience patterns across hops (timeout budgets, single-layer retries, circuit breakers, bulkheads, network isolation).
10. **Design** platform APIs and golden paths (Backstage catalog and templates, declarative self-service) that product teams and AI agents can use safely.

## Chapters and lessons

### Chapter 1 · Monoliths, modular monoliths and microservices (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 What microservices buy | Independent deployment, team autonomy, per-component scaling, fault isolation; Fowler and Lewis (2014) | List which benefits a 6-engineer startup actually needs |
| 1.2 What they cost | Network calls, partial failure, data consistency, operational load, debugging across hops, platform cost | Estimate the added latency and infrastructure of splitting one endpoint into four services |
| 1.3 Reversals | Segment (2018), Prime Video monitoring (2023), Istio's `istiod` (2020): why each one consolidated | Write a one-page analysis of one reversal: what changed and what they gave up |
| 1.4 The modular monolith | Enforced module boundaries (Shopify's Packwerk, Spring Modulith), Service Weaver's idea and its archiving | Add enforced module boundaries to a sample monolith and break the build on a violation |
| 1.5 Conway's law and teams | Team Topologies: stream-aligned and platform teams, cognitive load | Draw team and service boundaries for a 40-engineer food-delivery company |

**Check your understanding:** (1) Which microservice benefit cannot be had in a modular monolith, and when is it worth the cost? (2) Why did the Prime Video team's costs fall when they removed service boundaries? (3) What does Conway's law predict if one team owns ten services?

### Chapter 2 · Domain-driven design for boundaries (weeks 2–3)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Ubiquitous language and bounded contexts | One model per context; "order" means different things to checkout, kitchen and delivery | Run an event-storming session for a food-delivery flow |
| 2.2 Aggregates and invariants | Consistency boundaries, one aggregate per transaction, references by ID | Design the order and payment aggregates and their invariants |
| 2.3 Context mapping | Customer–supplier, conformist, anti-corruption layer, shared kernel, published language | Draw a context map with integration patterns for six contexts |
| 2.4 Domain events | Events that cross boundaries, internal vs published events, event ownership (BE304) | Define the published events for each context |
| 2.5 Domains at scale | Uber's domain-oriented architecture: domains, layers, gateways and extensions | Group 30 services into domains and layers with gateway interfaces |

**Check your understanding:** (1) Why is a shared "Customer" table across contexts a long-term trap? (2) How do aggregate boundaries limit what a service can promise transactionally? (3) When is an anti-corruption layer worth building?

### Chapter 3 · Splitting a monolith (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Strangler fig | Routing slices of traffic to a new service, incremental cut-over, rollback | Extract one capability behind a routing layer with a 1% → 100% rollout |
| 3.2 Branch by abstraction | Introducing seams inside the monolith before extraction | Introduce an interface and swap implementations behind a flag |
| 3.3 Extracting data | Database per service, the shared-database anti-pattern, expand/contract across ownership (BE303), CDC during migration | Move a table to a new service's database with zero downtime |
| 3.4 Verifying behaviour | Shadow traffic, dual running, diffing responses | Run old and new implementations side by side and diff 100,000 responses |

**Check your understanding:** (1) Why extract data ownership before, during or after code, and what goes wrong with each order? (2) What does shadow traffic prove, and what can it not prove? (3) When should you stop extracting?

### Chapter 4 · Communication between services (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Sync vs async | Temporal coupling, availability arithmetic (BE304), when a synchronous call is right | Replace two synchronous calls on a checkout path with events; show the availability gain |
| 4.2 Composition | API composition, backend-for-frontend, CQRS read models for cross-service queries | Build an "order details" view from four services two ways; compare latency and freshness |
| 4.3 Distributed monolith smells | Lock-step deploys, chatty interfaces, shared libraries with business logic, cascading synchronous chains | Audit a provided system and list its distributed-monolith smells |
| 4.4 Data consistency across services | Sagas and outbox (BE304), eventual consistency visible to users, reconciliation | Design user-facing states for an order that is "paid but not yet confirmed" |

**Check your understanding:** (1) Why does a chain of five synchronous calls make every service only as available as the weakest? (2) When is a CQRS view better than API composition? (3) Which smell tells you two services should be merged?

### Chapter 5 · Service discovery and traffic basics (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Discovery | DNS, Kubernetes Services and EndpointSlices, client-side vs server-side discovery, xDS | Watch EndpointSlices change during a rolling deploy |
| 5.2 Envoy | Listeners, routes, clusters, filters; outlier detection, retries and timeouts in the proxy | Configure Envoy by hand for two services with retries and outlier ejection |
| 5.3 Traffic management | Canary and blue–green routing, header-based routing, mirroring | Run a 5% canary with automatic rollback on error rate |
| 5.4 Readiness, warm-up and draining | How readiness, outlier detection, slow start and draining interact with discovery during deploys | Show requests failing against a cold instance, then fix it with readiness gates and slow start |

**Check your understanding:** (1) Why does client-side load balancing matter for gRPC? (2) What should a proxy retry, and what must it never retry? (3) What makes a canary statistically meaningful?

### Chapter 6 · Service mesh (weeks 7–8)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 What a mesh does | mTLS identity, traffic policy, telemetry, resilience; control plane vs data plane | List which of your BE302 chassis features a mesh would replace |
| 6.2 Sidecar meshes | Istio with Envoy sidecars, Linkerd's Rust micro-proxy; injection, startup ordering, resource overhead | Measure added p50/p99 latency and memory per pod with sidecars |
| 6.3 Sidecar-less meshes | Istio ambient mode (GA in 1.24): ztunnel for L4, waypoint proxies for L7; Cilium's eBPF approach | Move the same workload to ambient mode and repeat the measurements |
| 6.4 Mesh policy | mTLS everywhere, authorization policies between services, Gateway API for mesh traffic (GAMMA) | Allow only approved service-to-service calls, as Monzo did, and test denial |
| 6.5 Running a mesh | Upgrades and canary control planes, certificate rotation, debugging with proxy admin endpoints | Upgrade the mesh control plane with a canary revision and no traffic loss |

**Check your understanding:** (1) What does a mesh's mTLS prove about a caller, and what does it not prove about the user? (2) Why did ambient mode separate L4 and L7 processing? (3) When is a mesh not worth its operational cost?

### Chapter 7 · API gateways and the edge (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Gateway responsibilities | Authentication, rate limits, routing, request shaping, TLS; north–south vs east–west | Put authentication and rate limiting at a gateway; keep authorization in services |
| 7.2 Kubernetes Gateway API | `Gateway`, `HTTPRoute`, `GRPCRoute`, role separation between platform and app teams (v1.6 in October 2026) | Replace an Ingress with Gateway API routes owned by two teams |
| 7.3 Backends for frontends | Per-client aggregation layers, GraphQL BFFs (BE301), ownership by client teams | Build a mobile BFF that halves round trips |
| 7.4 Gateway anti-patterns | Business logic in the gateway, a single gateway team as bottleneck, gateway as the only security layer | Refactor a gateway plugin that contains pricing rules |

**Check your understanding:** (1) Why must object-level authorization stay in the service even with a gateway? (2) What problem does Gateway API's role separation solve? (3) When does a BFF become a distributed monolith?

### Chapter 8 · Contract testing and independent deploys (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Why end-to-end tests don't scale | Combinatorial environments, flakiness, slow feedback | Measure the flake rate of a provided end-to-end suite |
| 8.2 Consumer-driven contracts | Pact consumer tests, provider verification, a broker, `can-i-deploy` | Add Pact contracts between three services and block an incompatible deploy |
| 8.3 Schema compatibility | OpenAPI and protobuf breaking-change checks (BE301), event schemas in a registry (BE304) | Gate all three contract types in one CI pipeline |
| 8.4 Testing in production | Canaries, feature flags, synthetic checks, dark launches | Ship a change behind a flag to 1% of traffic with automated rollback |

**Check your understanding:** (1) What does a contract test prove that a unit test cannot? (2) Who should own a contract, the consumer or the provider? (3) Why is "deploy everything together" a sign of failure?

### Chapter 9 · Observability across services (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Distributed tracing | W3C Trace Context, OpenTelemetry SDKs and Collector, span links for async hops | Trace one checkout across six services and two queues |
| 9.2 Sampling | Head vs tail sampling, keeping errors and slow traces, cost | Configure tail sampling that keeps all errors and 1% of normal traffic |
| 9.3 SLOs per journey | User-journey SLOs vs per-service SLOs, error budgets, alerting on burn rate (see OPS304) | Define SLOs for "place order" and alert on burn rate |
| 9.4 Debugging across services | Service maps, exemplars linking metrics to traces, comparing traces before and after a regression | Find a planted cross-service latency regression in 30 minutes |

**Check your understanding:** (1) Why can a per-service SLO be met while the user journey is failing? (2) What do you lose with head-based sampling? (3) How do you trace through a Kafka hop?

### Chapter 10 · Resilience across hops (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Timeout budgets | Deadline propagation, per-hop budgets, gRPC deadlines (BE301) | Propagate a 1 s budget across four hops and observe cancellation |
| 10.2 Retries at one layer | Retry amplification across layers (3 × 3 × 3 = 27 attempts), retry budgets, mesh vs client retries | Show amplification in a 3-layer system; fix it |
| 10.3 Circuit breakers and bulkheads | Per-dependency isolation, fallback behaviour, load shedding (BE402) | Keep checkout working while recommendations are down |
| 10.4 Network isolation | Default-deny between services; Monzo's allowlists (each service calls about six others on average) | Write and enforce allowlists for your P3 services |

**Check your understanding:** (1) Why should only one layer retry? (2) What should a service return when a non-critical dependency is down? (3) What does default-deny networking catch that mTLS alone does not?

### Chapter 11 · Platform APIs and internal developer platforms (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Platform as a product | Golden paths, self-service, paved roads vs mandates, measuring adoption and developer experience | Interview three "users" and write a platform roadmap |
| 11.2 Catalogs and templates | Backstage (CNCF incubating) software catalog, ownership metadata, software templates, scorecards | Register your services in Backstage with owners, APIs and dependencies |
| 11.3 Declarative platform APIs | Kubernetes custom resources and controllers, reconcile loops, Crossplane-style composition; designing for idempotency and drift | Write a `Database` custom resource whose controller provisions Postgres with defaults |
| 11.4 Evolving and retiring platform features | Versioned platform APIs, deprecation, migration tooling | Migrate ten services off an old platform API with a codemod |
| 11.5 Agents as platform users | Exposing platform actions as safe tools (MCP), guardrails, approvals, audit | Let an AI agent create a new service from a template, with approval required for production |

**Check your understanding:** (1) Why do declarative APIs suit platforms better than imperative ones? (2) How do you know if a golden path is actually used? (3) Which platform actions should an agent never perform without a human?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Reversal analysis; module boundaries | Analysis note; failing build on violation |
| 2 | 2 | Lab 1: event storming | Context map |
| 3 | 2 | Aggregates and events | Aggregate design; P1 due |
| 4 | 3 | Lab 2: strangler extraction | 1% → 100% rollout log |
| 5 | 4 | Lab 3: composition vs CQRS | Latency and freshness comparison |
| 6 | 5 | Lab 4: hand-configured Envoy | Canary with automatic rollback; P2 starts |
| 7 | 6 | Lab 5: sidecar mesh | Overhead measurements |
| 8 | 6 | Lab 5 (cont.): ambient mesh and policy | Comparison and allowlist tests |
| 9 | 7 | Lab 6: Gateway API | Two-team route ownership; P2 due |
| 10 | 8 | Lab 7: Pact | Blocked incompatible deploy |
| 11 | 9 | Lab 8: tracing and SLOs (no AI) | Regression found from traces; P3 design review |
| 12 | 10 | Lab 9: resilience | Amplification fixed; graceful degradation |
| 13 | 11 | Platform API | Custom resource and controller |
| 14 | — | P3 integration | P3 demo and architecture review |
| 15 | Review and exam | — | Written exam and live architecture review |

## Working with AI in this course

- **Use AI for:** generating Kubernetes manifests, Helm charts, Envoy and mesh configuration (then reviewing every field); drafting context maps from event-storming notes; writing Pact tests; explaining trace data; scaffolding controllers and Backstage templates.
- **Do without AI (drills):** drawing service boundaries and context maps for a new domain; deciding monolith vs services for a case; the Lab 8 trace investigation; the live architecture review, where you defend boundaries and failure behaviour.
- **Verify AI output by:** applying generated configuration to a test cluster and checking it with the mesh's own validation tools (`istioctl analyze`, `linkerd check`); load-testing to measure mesh overhead instead of trusting claims; running contract tests before any deploy; reading every generated retry and timeout setting against your timeout budget.
- **Where AI still fails here (show it yourself):** ask an assistant to "split this monolith into microservices" and count the synchronous calls on the critical path in its design. Ask for mesh retry policies and check whether they multiply with client retries. Ask for an authorization setup "using the mesh" and check whether it confuses service identity with user permissions. Ask it to design boundaries for a domain and check whether it splits by technical layer instead of business capability. Record each finding.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs 1–9 | 25% |
| Projects P1 / P2 / P3 | 5% / 12% / 23% |
| Written exam (boundaries, communication, mesh, contracts, resilience) | 20% |
| Live architecture review (no AI) | 15% |

**Mastery gate:** you pass when you can, without AI help, (a) produce a context map and service-boundary proposal for an unfamiliar domain in 90 minutes, including a reasoned decision on which parts stay in a modular monolith; (b) find a planted cross-service latency regression and a retry-amplification bug from traces and configuration within 45 minutes; and (c) show your P3 deploying one service independently while contract tests, SLO alerts and network policies stay green.

## Industry reality

- **Consolidations:** Segment merged over 140 destination services into one (2018). Prime Video's monitoring service cut costs by 90% by moving from Step Functions and Lambda into one process on ECS (InfoQ, May 2023). Istio merged Pilot, Galley, Citadel and the sidecar injector into `istiod` (March 2020) because the components were always released together and owned by one team.
- **Large-scale microservices:** Uber's domain-oriented architecture grouped about 2,200 critical microservices into roughly 70 domains (2020). Monzo restricted its 1,500+ services so that each can call only an approved list, about six others on average (2019).
- **Meshes and gateways in 2026:** Istio 1.31 is current, and its ambient mode has been GA since 1.24 (November 2024). Linkerd 2.20 shipped in June 2026, with stable artifacts from vendors since February 2024. Envoy is a CNCF graduated project. Kubernetes Gateway API reached v1.6, with mesh support through the GAMMA initiative.
- **Modular monoliths:** Shopify enforces module boundaries in its Rails monolith with Packwerk. Google's Service Weaver entered maintenance mode in December 2024, and its repository was archived in March 2026.
- **Platforms:** Backstage has been a CNCF incubating project since March 2022.

Interview questions from this course:

1. **"Should this 15-person startup move to microservices?"** A strong answer covers team size and Conway's law, deploy independence vs operational cost, a modular monolith with enforced boundaries as the default, the signals that justify extraction, and named reversals.
2. **"How would you find service boundaries for a food-delivery platform?"** Cover bounded contexts, aggregates and invariants, event storming, data ownership, context-map integration patterns, and avoiding splits by technical layer.
3. **"Do we need a service mesh?"** Cover what it gives (mTLS identity, traffic policy, telemetry), the cost (latency, resources, upgrades), sidecar vs ambient, alternatives (libraries, gateway only), and the scale at which it pays off.
4. **"Two teams keep breaking each other's deploys. Fix it."** Cover consumer-driven contracts, schema compatibility gates, versioning, `can-i-deploy`, feature flags and canaries, and removing lock-step deploys.
5. **"A checkout request is slow only sometimes. Find out why across 12 services."** Cover traces with tail sampling, exemplars, comparing slow and fast traces, retry amplification, timeout budgets, queue waits and noisy neighbours.

## Resources (free first)

- **Foundations:** Martin Fowler and James Lewis, [Microservices](https://martinfowler.com/articles/microservices.html) (2014); Eric Evans, [DDD Reference](https://www.domainlanguage.com/ddd/reference/) (free); [microservices.io](https://microservices.io/patterns/apigateway.html) pattern language; [Team Topologies](https://teamtopologies.com/).
- **Case studies:** Segment, [Goodbye Microservices](https://www.twilio.com/en-us/blog/developers/best-practices/goodbye-microservices) (2018); InfoQ, [Prime Video switched from serverless to EC2 and ECS](https://www.infoq.com/news/2023/05/prime-ec2-ecs-saves-costs/) (2023); Istio, [Introducing istiod](https://istio.io/latest/blog/2020/istiod/) (2020); Uber, [Domain-Oriented Microservice Architecture](https://www.uber.com/blog/microservice-architecture/) (2020); Shopify, [Deconstructing the Monolith](https://shopify.engineering/deconstructing-monolith-designing-software-maximizes-developer-productivity) and [Under Deconstruction](https://shopify.engineering/shopify-monolith); Monzo, [network isolation for 1,500 services](https://monzo.com/blog/we-built-network-isolation-for-1-500-services) (2019).
- **Mesh and gateways:** [Envoy docs](https://www.envoyproxy.io/docs/envoy/latest/); Istio, [ambient mode GA](https://istio.io/latest/blog/2024/ambient-reaches-ga/); [Linkerd overview](https://linkerd.io/2/overview/) and [releases](https://linkerd.io/releases/); [Cilium service mesh](https://cilium.io/use-cases/service-mesh/); [Gateway API](https://gateway-api.sigs.k8s.io/docs/introduction/) and [GAMMA](https://gateway-api.sigs.k8s.io/docs/mesh/gamma/).
- **Contracts and observability:** [Pact docs](https://docs.pact.io/); [OpenTelemetry docs](https://opentelemetry.io/docs/); [W3C Trace Context](https://www.w3.org/TR/trace-context/).
- **Modularity and platforms:** [Packwerk](https://github.com/Shopify/packwerk); [Spring Modulith](https://spring.io/projects/spring-modulith); [Service Weaver](https://github.com/ServiceWeaver/weaver) (archived, still worth reading); [Backstage](https://backstage.io/docs/overview/what-is-backstage).
- **Paid, worth it:** Sam Newman, *Building Microservices*, 2nd edition (O'Reilly, 2021) and *Monolith to Microservices* (2019); Vaughn Vernon, *Implementing Domain-Driven Design*.

## Sources

All checked 12 Oct 2026.

- Segment/Twilio, *Goodbye Microservices* (10 Jul 2018): https://www.twilio.com/en-us/blog/developers/best-practices/goodbye-microservices
- InfoQ, *Prime Video Switched from Serverless to EC2 and ECS to Save Costs* (3 May 2023): https://www.infoq.com/news/2023/05/prime-ec2-ecs-saves-costs/
- Istio, *Introducing istiod* (19 Mar 2020): https://istio.io/latest/blog/2020/istiod/ ; ambient mode GA in 1.24 (Nov 2024): https://istio.io/latest/blog/2024/ambient-reaches-ga/ ; releases (1.31.x current): https://istio.io/latest/news/releases/
- Uber, *Introducing Domain-Oriented Microservice Architecture* (23 Jul 2020): https://www.uber.com/blog/microservice-architecture/
- Monzo, network isolation (6 Nov 2019): https://monzo.com/blog/we-built-network-isolation-for-1-500-services
- Linkerd releases (2.20, 23 Jun 2026; stable releases from vendors since Feb 2024): https://linkerd.io/releases/
- Kubernetes Gateway API releases (v1.6.3, Oct 2026): https://github.com/kubernetes-sigs/gateway-api/releases
- Service Weaver repository (maintenance mode from 5 Dec 2024; archived 4 Mar 2026): https://github.com/ServiceWeaver/weaver
- CNCF project pages: Backstage (incubating since 15 Mar 2022) https://www.cncf.io/projects/backstage/ ; Envoy https://www.cncf.io/projects/envoy/

_Last reviewed: 2026-10_
