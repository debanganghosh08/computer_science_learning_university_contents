# OPS402 · Chaos Engineering and Resilience

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 7 | 4 (≈ 120 hours) | L3 → L4 | [OPS302](../../year_3/OPS302_linux_systems_administration_in_depth/README.md); strongly recommended: [OPS304](../../year_3/OPS304_site_reliability_engineering_slos_error_budgets/README.md), [CS212](../../../../02_year_2_core_computer_science/semester_4/CS212_distributed_systems_i/README.md) | [OPS501](../../year_5/OPS501_frontier_seminar_autonomous_infrastructure/README.md), [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) |

Part of the [DevOps, SRE and Platform Engineering major](../../README.md). [CS212](../../../../02_year_2_core_computer_science/semester_4/CS212_distributed_systems_i/README.md) taught why distributed systems fail. [OPS304](../../year_3/OPS304_site_reliability_engineering_slos_error_budgets/README.md) taught how to respond when they do. This course teaches you to design services that degrade gracefully instead of collapsing, and to prove it by injecting failure on purpose, safely, before reality does. Multi-region architecture is designed in [CLD301](../../../cloud_engineering/year_3/CLD301_cloud_architecture_on_aws_azure_and_google_cloud/README.md); business continuity strategy is in [SAR404](../../../security_architecture/year_4/SAR404_resilience_business_continuity_and_security/README.md). Here you build, test and break.

## Why this course matters now

The outages that hurt most are rarely a single crash. They are retries, queues and dependencies amplifying a small fault:

- **Google Cloud (June 2025):** restarting tasks created "a herd effect" on a database. The fixes included auditing that "our systems employ randomized exponential backoff".
- **AWS us-east-1 (October 2025):** EC2 kept failing for hours after DynamoDB recovered, because a backlog of host leases had to be re-established.
- **UPI (March–May 2025):** NPCI linked India's outages to banks firing "check transaction status" requests at very high speed, and responded with mandatory limits.

Research names the pattern. "Metastable failures" (HotOS 2021, OSDI 2022) are states in which a system stays down after the trigger is gone. A USENIX study of 198 user-reported failures found that most catastrophic ones could have been prevented by simple testing of error-handling code.

The tools are mature. Chaos Mesh and LitmusChaos are CNCF incubating projects, and AWS Fault Injection Service and Azure Chaos Studio are managed services. AI assistants generate retry code and chaos experiments quickly. The retry code often lacks jitter, budgets or idempotency, and the experiments often lack a steady-state hypothesis or abort condition. The judgment of what to break, how far, and when to stop stays human.

## Learning outcomes

By the end you can:

1. **Classify** failures (crash, omission, timing, gray failure, correlated failure) and **predict** how each propagates through a dependency graph.
2. **Implement** timeouts with deadline propagation, retries with exponential backoff, jitter and retry budgets, and idempotency keys, and **measure** retry amplification.
3. **Apply** circuit breakers, outlier detection, bulkheads, shuffle sharding and cell-based isolation, and **justify** each with a failure mode.
4. **Protect** services from overload with admission control, priority-based load shedding, adaptive concurrency limits and client-side throttling, and **recover** from a metastable state.
5. **Design** chaos experiments with a steady-state hypothesis, blast-radius limits, abort conditions and approvals.
6. **Run** fault injection with Chaos Mesh, LitmusChaos, service-mesh fault injection and toxiproxy, locally and in CI.
7. **Plan and facilitate** game days and disaster-recovery drills, and **turn** results into fixes.
8. **Test** resilience earlier with error-path tests, Jepsen-style checks and deterministic simulation.
9. **Engineer** resilience for AI-dependent systems (LLM provider failures, rate limits, runaway agent loops).

## Chapters and lessons

### Chapter 1 · How systems fail (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Faults, errors, failures | Fault tolerance vs resilience; crash, omission, timing, Byzantine-lite faults | Classify 15 incidents from OPS304's case list |
| 1.2 Gray failure | Partial, differential observability: the health check passes while users fail (Huang et al., HotOS 2017) | Build a service whose health check lies; detect it from user SLIs |
| 1.3 Correlated failure | Shared dependencies, shared config, shared deploys, zones and regions | Draw the hidden shared dependencies of a "redundant" system |
| 1.4 Static stability | Keep working without the control plane; pre-provisioned capacity (AWS Builders' Library) | Show a data plane that survives control-plane loss |

**Check your understanding:** (1) Why do redundant systems fail together? (2) What makes a gray failure hard to see? (3) What does static stability cost?

### Chapter 2 · Timeouts and retries (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Timeouts | Picking timeouts from latency percentiles, deadline propagation (gRPC deadlines), timeout budgets across hops | Set timeouts for a 4-hop call chain from measured p99s |
| 2.2 Retries | When to retry (idempotent, transient), exponential backoff, full jitter vs equal jitter (AWS, 2015) | Simulate synchronised retries with and without jitter |
| 2.3 Retry budgets | Token buckets and retry ratios (Envoy, Finagle-style), retrying at one layer only | Cap retries at 10% of requests; measure the effect |
| 2.4 Amplification | 3 layers × 3 attempts = 27× load; status-check storms (UPI 2025); herd effects (Google 2025) | Reproduce a 27× amplification and remove it |
| 2.5 Idempotency | Idempotency keys, safe retries for payments (link [BE401](../../../backend_engineering/year_4/BE401_payments_grade_systems_transactions_idempotency/README.md)) | Make a payment endpoint safe to retry |

**Check your understanding:** (1) Why can a retry make an outage longer? (2) Why retry at one layer only? (3) What does NPCI's 90-second minimum before a status check do to the load curve?

### Chapter 3 · Isolation (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Circuit breakers | Closed, open, half-open; error-rate and latency triggers; Resilience4j; Envoy outlier detection | Add a breaker; show it shedding calls to a failing dependency |
| 3.2 Bulkheads | Separate pools for separate dependencies and tenants | Stop one slow dependency from exhausting all threads |
| 3.3 Shuffle sharding | Each customer on a random subset of workers; blast radius maths (AWS Builders' Library) | Compute and simulate the blast radius of one bad tenant |
| 3.4 Cells | Cell-based architecture, cell routers, cell-by-cell deployment | Split a service into 3 cells; fail one |

**Check your understanding:** (1) What does a breaker protect: the caller or the callee? (2) Why does shuffle sharding beat simple sharding for noisy tenants? (3) What is the cost of cells?

### Chapter 4 · Overload and metastability (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Queues and overload | Why latency explodes near saturation (preview of [OPS404](../OPS404_performance_and_capacity_engineering/README.md)); unbounded queues as hidden outages | Show latency vs load on a single queue |
| 4.2 Load shedding | Admission control, priority (critical vs sheddable), LIFO and CoDel queueing, deadline-aware dropping | Keep checkout alive while shedding recommendations |
| 4.3 Adaptive limits | Adaptive concurrency (Netflix concurrency-limits, Envoy), client-side throttling (SRE book, Handling Overload) | Replace a fixed limit with an adaptive one |
| 4.4 Metastable failures | Trigger vs sustaining effect (retries, cache misses, lease backlogs); recovery levers | Push a simulator into a metastable state and get it out |
| 4.5 Backlog recovery | Avoiding insurmountable queue backlogs; dropping vs draining; the AWS October 2025 lease backlog | Design recovery for a queue with 6 hours of backlog |

**Check your understanding:** (1) Why doesn't a metastable system recover when the trigger stops? (2) What is the difference between load shedding and rate limiting? (3) Which recovery lever would you pull first in the AWS 2025 case?

### Chapter 5 · Dependencies and fallbacks (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Dependency criticality | Hard vs soft dependencies; degrading features rather than failing | Classify every dependency of a demo app |
| 5.2 Fallbacks done carefully | Why rarely used fallbacks fail (AWS, Avoiding fallback in distributed systems); fail-open vs fail-closed choices | Write the fallback policy for an auth service and a recommender |
| 5.3 Caches as dependencies | Cold-cache stampedes, request coalescing, stale-while-revalidate | Survive a cache flush without overloading the database |
| 5.4 DNS and control planes | DNS TTLs, resolver caching, control-plane dependencies of the data plane | Trace your app's dependency on DNS and test its failure |

**Check your understanding:** (1) Why can a fallback be more dangerous than failing? (2) When should an authorisation check fail closed? (3) What happens to your service if DNS is slow rather than down?

### Chapter 6 · The chaos engineering method (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Principles | Steady-state hypothesis, real-world events, production (eventually), automation, minimal blast radius (Principles of Chaos Engineering) | Write a hypothesis for 5 experiments |
| 6.2 Experiment design | Variables, abort conditions, rollback, observability prerequisites, approvals | Write a full experiment document reviewed by a classmate |
| 6.3 History | Netflix Chaos Monkey (2011) and later fault-injection platforms; Google's DiRT exercises | Summarise what each added beyond the previous one |
| 6.4 Ethics and safety | Customer impact budgets, communication, regulated systems, error budget as permission | Write the safety section for a fintech experiment |

**Check your understanding:** (1) Why start from a steady state rather than "let's see what breaks"? (2) When is an experiment not allowed to run? (3) How does an error budget give permission for experiments?

### Chapter 7 · Fault-injection tooling (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Chaos Mesh | PodChaos, NetworkChaos (latency, loss, partition), IOChaos, StressChaos, TimeChaos, Workflows | Inject 300 ms latency to one dependency with abort on SLO burn |
| 7.2 LitmusChaos | ChaosEngine, experiments from ChaosHub, probes as steady-state checks | Run a node-drain experiment with HTTP probes |
| 7.3 Mesh and app-level injection | Istio fault injection, toxiproxy for databases and caches, Krkn | Inject faults into a Redis connection in CI |
| 7.4 Cloud services | AWS Fault Injection Service, Azure Chaos Studio, Gremlin: scope, guardrails, cost | Read one service's safety controls; compare with Chaos Mesh |

**Check your understanding:** (1) Why do experiments need probes, not just faults? (2) What can a network partition test reveal that a pod kill cannot? (3) What guardrails would you require before running a cloud fault-injection template?

### Chapter 8 · Game days and DR drills (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Planning | Objectives, scenarios, roles, safety officer, communication plan, dry run | Plan a 2-hour game day |
| 8.2 Disaster recovery | RTO and RPO tested, not assumed; backup restore; region evacuation; data-location limits (RBI payment data stays in India) | Restore a database and fail over a service; time both |
| 8.3 Facilitation | Running the day, observing, the learning review afterwards | Facilitate a classmate's game day |
| 8.4 Turning findings into fixes | Prioritising, owners, retest | Close one finding and rerun the experiment |

**Check your understanding:** (1) Why rehearse with the real on-call team, not experts? (2) What limits your DR options when data must stay in one country? (3) How do you know a game-day fix worked?

### Chapter 9 · Testing resilience earlier (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Error-path testing | The USENIX OSDI 2014 study: most catastrophic failures came from mishandled non-fatal errors | Write tests that force every error branch of one module |
| 9.2 Faults in CI | toxiproxy and test containers to inject latency and resets in integration tests | Add 5 fault tests to a pipeline |
| 9.3 Consistency testing | Jepsen-style checks for databases and queues (from CS212) | Run a partition test against a replicated store and check linearizability |
| 9.4 Deterministic simulation | FoundationDB's simulation testing, property-based tests for retry logic | Property-test a retry library for budget and idempotency invariants |

**Check your understanding:** (1) Why are error paths the least tested code? (2) What does deterministic simulation give you that chaos in production cannot? (3) What invariant should every retry library hold?

### Chapter 10 · Resilience for AI systems (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 LLM provider failures | Rate limits, timeouts, partial outages, latency spikes, model deprecations | Inject 429s and 30 s latencies into an LLM call path |
| 10.2 Fallbacks and breakers for models | Secondary models, cached answers, graceful "AI unavailable" modes, quality drop as a failure | Build a breaker that switches to a smaller model and alerts |
| 10.3 Agent loops | Runaway retries, cost explosions, tool-call storms; budgets and step limits | Cap an agent's steps, tokens and spend; test it |
| 10.4 AI-generated experiments | Using assistants to propose chaos experiments; checking for hypotheses and abort conditions | Grade 10 AI-proposed experiments against the Chapter 6 checklist |

**Check your understanding:** (1) Why is a degraded model answer harder to detect than an error? (2) What should an agent do when its tool keeps failing? (3) What did the AI-proposed experiments most often lack?

### Chapter 11 · Continuous resilience (weeks 11–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Automating experiments | Scheduled experiments in pipelines, gated by error budget | Run 3 experiments nightly with automatic abort |
| 11.2 Resilience scorecards | Coverage of failure modes per service; tracking fixes | Build a scorecard for 5 services |
| 11.3 Capstone game day | Four scenarios, live, with observers | P3 game day and learning review |
| 11.4 Resilience reviews of new designs | Failure mode and effects analysis (FMEA) in design documents, pre-mortems | Run a pre-mortem on a classmate's design and list its top 5 failure modes |

**Check your understanding:** (1) Why gate automated experiments on the error budget? (2) What does "coverage" mean for resilience? (3) Which finding from your game day would you fix first, and why?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Gray failure | Lying health check demo |
| 2 | 2 | Lab 2 · Retry storm simulator | Amplification plots; P1 starts |
| 3 | 3 | Lab 3 · Breakers and bulkheads | **P1 due** |
| 4 | 4 | Lab 4 · Shedding and metastability | Recovery demo |
| 5 | 5 | Lab 5 · Fallback policy | Dependency table; P2 starts |
| 6 | 6 | Experiment design review | Experiment docs |
| 7 | 7 | Lab 6 · Chaos Mesh and Litmus | Mid-term (AI off) |
| 8 | 8 | Lab 7 · DR drill | Timed restore and failover |
| 9 | 9 | Lab 8 · Faults in CI | **P2 due** |
| 10 | 10 | Lab 9 · LLM resilience | Breaker + budgets |
| 11 | 11 | Lab 10 · Nightly chaos | Scorecard; P3 design review |
| 12 | 11 | P3 build | — |
| 13 | 11 | P3 game day | Game day log |
| 14 | 11 | Learning review | **P3 due** |
| 15 | Review | Design exam and oral | Final |

## Working with AI in this course

- **Use AI for:** generating Chaos Mesh and Litmus manifests, toxiproxy setups, simulation code and load scripts; proposing experiment ideas from an architecture diagram; summarising game-day notes. Named tools: Claude Code, GitHub Copilot, Cursor.
- **Do without AI (drills):** retry-amplification arithmetic, blast-radius calculations for shuffle sharding, writing steady-state hypotheses and abort conditions, the mid-term and design exam, and acting as safety officer in game days.
- **Verify AI output by:** reading every retry policy for jitter, a budget, a maximum and idempotency; running experiments first in a local cluster with abort conditions tested (inject a fault that should abort and check that it does); checking that an experiment's blast radius matches its document.
- **Where AI still fails here (show it):** ask an assistant for "a robust HTTP client with retries" and check for jitter, budgets and idempotency handling; ask it to design a chaos experiment and check for a steady-state hypothesis and abort conditions. In Lab 9, record how often generated code retries non-idempotent requests.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs 1–10 | 25% |
| Projects P1 / P2 / P3 | 5% / 15% / 25% |
| Mid-term (AI off) | 10% |
| Design exam (3 hours, AI off) + oral | 20% |

**Mastery gate.** You pass when you can: (1) given an architecture and its dependency latencies, design timeouts, retry budgets, breakers and shedding priorities in 90 minutes without AI, with the amplification factor computed; (2) design, run and safely abort a chaos experiment on an unfamiliar service, with a written hypothesis and result; (3) bring a simulated system out of a metastable state you did not create within 15 minutes, explaining the sustaining effect.

## Industry reality

Netflix popularised chaos engineering and published the [Principles of Chaos Engineering](https://principlesofchaos.org/). AWS teaches the same resilience patterns in its free Builders' Library (timeouts, retries, jitter, load shedding, shuffle sharding, static stability). Cloud providers sell fault injection as managed services ([AWS FIS](https://aws.amazon.com/fis/), [Azure Chaos Studio](https://learn.microsoft.com/en-us/azure/chaos-studio/)). In India, NPCI's 2025 API rules for UPI members are a public example of resilience requirements imposed on clients by a network operator.

**Interview questions from this course**

1. *How do you implement retries correctly?* Strong answer: retry only idempotent or idempotency-keyed operations and only transient errors; exponential backoff with full jitter; a maximum and a retry budget; one layer only; deadlines propagated; metrics on retries; explains amplification maths.
2. *A downstream dependency gets slow. What happens to your service, and how do you protect it?* Strong answer: thread or connection pool exhaustion, queueing, cascading latency; timeouts from percentiles, bulkheads, breakers with outlier detection, shedding of non-critical work, fallbacks chosen carefully.
3. *What is a metastable failure? Give an example.* Strong answer: a trigger pushes the system into a bad state that a sustaining effect (retries, cache misses, backlog) keeps it in after the trigger ends; examples from the OSDI 2022 study, Google 2025 herd effect, AWS 2025 lease backlog; recovery by cutting load or the sustaining loop.
4. *Design a chaos experiment for our checkout service.* Strong answer: steady-state SLI and hypothesis, a specific fault (dependency latency), scope and blast radius, abort conditions tied to SLO burn, approvals and communication, observability ready, run in staging then a small production slice, learning review.
5. *How would you test disaster recovery for a payments database in India?* Strong answer: RTO/RPO from the business, restore drills timed end to end, replica promotion drills, data-localisation constraints on region choice, data integrity checks after restore, runbook rehearsed by on-call, results tracked.

## Resources (free first)

- **Principles and patterns:** [Principles of Chaos Engineering](https://principlesofchaos.org/); AWS Builders' Library: [Timeouts, retries and backoff with jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/), [Using load shedding to avoid overload](https://aws.amazon.com/builders-library/using-load-shedding-to-avoid-overload/), [Workload isolation using shuffle-sharding](https://aws.amazon.com/builders-library/workload-isolation-using-shuffle-sharding/), [Avoiding fallback in distributed systems](https://aws.amazon.com/builders-library/avoiding-fallback-in-distributed-systems/), [Static stability](https://aws.amazon.com/builders-library/static-stability-using-availability-zones/), [Avoiding insurmountable queue backlogs](https://aws.amazon.com/builders-library/avoiding-insurmountable-queue-backlogs/); AWS Architecture Blog, [Exponential backoff and jitter](https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/); Google SRE book, [Handling Overload](https://sre.google/sre-book/handling-overload/) and [Addressing Cascading Failures](https://sre.google/sre-book/addressing-cascading-failures/).
- **Papers:** Bronson et al., [Metastable Failures in Distributed Systems](https://sigops.org/s/conferences/hotos/2021/papers/hotos21-s11-bronson.pdf) (HotOS 2021); Huang et al., [Metastable Failures in the Wild](https://www.usenix.org/conference/osdi22/presentation/huang-lexiang) (OSDI 2022); Yuan et al., [Simple Testing Can Prevent Most Critical Failures](https://www.usenix.org/conference/osdi14/technical-sessions/presentation/yuan) (OSDI 2014); Huang et al., "Gray Failure: The Achilles' Heel of Cloud-Scale Systems" (HotOS 2017); [FoundationDB paper](https://www.foundationdb.org/files/fdb-paper.pdf) (SIGMOD 2021, simulation testing).
- **Tools:** [Chaos Mesh](https://chaos-mesh.org/docs/), [LitmusChaos](https://docs.litmuschaos.io/), [Krkn](https://github.com/krkn-chaos/krkn), [Chaos Toolkit](https://github.com/chaostoolkit/chaostoolkit), [toxiproxy](https://github.com/Shopify/toxiproxy), [Resilience4j](https://resilience4j.readme.io/), [Envoy outlier detection](https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/upstream/outlier), [Netflix concurrency-limits](https://github.com/Netflix/concurrency-limits), [Chaos Monkey](https://netflix.github.io/chaosmonkey/), [Jepsen](https://jepsen.io/).
- **Practice locally:** [Online Boutique](https://github.com/GoogleCloudPlatform/microservices-demo) or the [OpenTelemetry Demo](https://opentelemetry.io/docs/demo/) on kind with Chaos Mesh and Istio.
- **Paid, optional:** Michael Nygard, *Release It!*, 2nd ed. (2018); Casey Rosenthal and Nora Jones, *Chaos Engineering* (O'Reilly, 2020).

## Sources

All checked 12 Oct 2026.
- Google Cloud, [incident report](https://status.cloud.google.com/incidents/ow5i3PPK96RduMcb1SsW) (12 Jun 2025: herd effect; randomized exponential backoff audit).
- AWS, [DynamoDB service disruption summary](https://aws.amazon.com/message/101925/) (19–20 Oct 2025: DWFM lease re-establishment after DynamoDB recovery).
- MediaNama, [NPCI circular coverage](https://www.medianama.com/2025/05/223-npci-banks-balance-upi-transaction-guidelines/) (May 2025).
- USENIX, [Simple Testing Can Prevent Most Critical Failures](https://www.usenix.org/conference/osdi14/technical-sessions/presentation/yuan) (198 failures studied; most catastrophic failures preventable by testing error handling).
- USENIX, [Metastable Failures in the Wild](https://www.usenix.org/conference/osdi22/presentation/huang-lexiang) (OSDI 2022).
- CNCF maturity (Chaos Mesh and LitmusChaos incubating since 2022; Krkn sandbox) from the [CNCF landscape](https://github.com/cncf/landscape) data file; Chaos Mesh 2.8.4 and LitmusChaos 3.32 from GitHub releases.
- Google SRE book, [Handling Overload](https://sre.google/sre-book/handling-overload/) (client-side adaptive throttling).

_Last reviewed: 2026-10_
