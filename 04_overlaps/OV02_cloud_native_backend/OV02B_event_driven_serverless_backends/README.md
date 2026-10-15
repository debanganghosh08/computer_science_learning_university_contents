# OV02B · Event-Driven Serverless Backends

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 8 | 4 (≈ 120 hours) | L3 → L4 | [BE301](../../../03_majors/backend_engineering/year_3/BE301_api_design_rest_grpc_and_graphql/README.md), [BE304](../../../03_majors/backend_engineering/year_3/BE304_asynchronous_systems_queues_streams_and_event/README.md), [CLD303](../../../03_majors/cloud_engineering/year_3/CLD303_containers_and_kubernetes/README.md); recommended [OV02A](../OV02A_building_cloud_native_services/README.md) | [BE501](../../../03_majors/backend_engineering/year_5/BE501_frontier_seminar_durable_execution_serverless/README.md), [THS501](../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md), [LCH502](../../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md) |

Part of the [OV02 Cloud-Native Backend overlap](../README.md). BE304 taught the semantics (outbox, sagas, idempotent consumers); [CLD401](../../../03_majors/cloud_engineering/year_4/CLD401_serverless_and_event_driven_cloud/README.md) teaches serverless platform internals for cloud majors. This course is the backend engineer's view: designing and shipping an event-driven product on managed brokers, functions and durable workflows, and knowing when to run the same design on Kubernetes instead.

## Why this course matters now

Event-driven, managed-service backends are the default for many new products and for the asynchronous half of most large systems: notifications, settlements, document processing, analytics feeds and AI jobs. The platforms changed quickly: AWS added durable functions to Lambda in December 2025 (multi-step code that checkpoints and can wait without compute charges) ([AWS](https://aws.amazon.com/about-aws/whats-new/2025/12/lambda-durable-multi-step-applications-ai-workflows/)); CloudEvents graduated in the CNCF in January 2024 and Knative in October 2025 ([CNCF](https://www.cncf.io/announcements/2024/01/25/cloud-native-computing-foundation-announces-the-graduation-of-cloudevents/), [CNCF](https://www.cncf.io/announcements/2025/10/08/cloud-native-computing-foundation-announces-knatives-graduation/)); Temporal and Restate made durable execution a mainstream design choice. AI assistants can generate a SAM, CDK or Terraform stack with functions and queues in minutes. What they do not provide is the design: which events to publish, how to get exactly-once effects from at-least-once delivery, how to replay safely, how to version a workflow that is mid-flight for a week, and what a business event costs.

## Learning outcomes

By the end you can:

1. **Discover and design** domain events with event storming, and **specify** them as CloudEvents with AsyncAPI contracts and compatibility rules.
2. **Choose** between functions, serverless containers, Kubernetes with KEDA or Knative, and durable-execution engines for each part of a backend, with measured latency and cost.
3. **Implement** idempotent handlers, partial-batch failure handling and conditional writes so that duplicates and retries never produce duplicate effects.
4. **Build** a transactional outbox on a serverless data store (DynamoDB Streams or Postgres with change data capture) and **prove** no event is lost or invented.
5. **Orchestrate** long-running business processes with Step Functions, durable functions, Temporal or Restate, including compensation, timeouts, human steps and versioning.
6. **Trace** a business flow across synchronous calls, buses, queues and workflows, and **operate** it with lag, age and DLQ alerts and safe replay.
7. **Secure** event-driven systems: least privilege per function, event injection, webhook verification and tenant isolation.
8. **Model** cost per business event and **find** the traffic level where a different platform becomes cheaper.

## Chapters and lessons

### Chapter 1 · Designing with events (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Event storming | Big-picture and design-level event storming (Alberto Brandolini); domain events, commands, policies, read models | Run a two-hour event storm for the course order platform |
| 1.2 Kinds of events | Domain versus integration events; notification versus event-carried state transfer; thin and fat events (from BE301) | Classify 20 events from the storm and choose payload styles |
| 1.3 Contracts | CloudEvents attributes, AsyncAPI 3.0 documents, schema registries and compatibility modes (from BE304) | Write AsyncAPI for five events; add a compatibility check in CI |
| 1.4 Ownership | One owner per event type, an event catalogue (EventCatalog or a Backstage plugin), deprecation | Publish the catalogue with owners and consumers |

**Check your understanding:** Why should most integration events carry enough state for consumers to act without calling back? Who decides whether a field can be removed from an event? What does a command disguised as an event do to coupling?

### Chapter 2 · The toolbox and how to choose (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Compute options | Functions (Lambda, Cloud Run functions, Azure Functions Flex Consumption), serverless containers (Cloud Run, Azure Container Apps, Fargate), Kubernetes with KEDA or Knative | Fill a decision matrix for six workloads in the course platform |
| 2.2 Brokers and buses | SQS and SNS, EventBridge, Google Pub/Sub and Eventarc, Azure Service Bus and Event Grid, Kafka (managed); queue versus bus versus log | Map each event in the catalogue to a transport with reasons |
| 2.3 Limits as design inputs | Payload sizes, timeouts, concurrency quotas, ordering guarantees (full detail in CLD401) | Find the two limits most likely to break your design |
| 2.4 Portability | What is portable (CloudEvents, AsyncAPI, OpenTelemetry, Knative, KEDA, Dapr) and what is not; exit cost as a design input | Estimate the effort to move one flow from EventBridge to Kafka |

**Check your understanding:** When is a Kubernetes consumer with KEDA a better choice than a function? Why does a bus with content filtering change how teams depend on each other? Which limit would you design around first for document processing?

### Chapter 3 · Writing handlers that survive retries (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Handler structure | Initialisation outside the handler, dependency injection, typed event parsing with schema validation | Refactor a generated handler into testable layers |
| 3.2 Idempotency | Idempotency keys from event IDs, conditional writes, Powertools idempotency utility, key expiry and in-flight states | Process the same event 100 times; prove one effect |
| 3.3 Batches | Partial batch responses, poison-message isolation, batch windows and their latency cost | Fail one record in a batch of ten without reprocessing the other nine |
| 3.4 Timeouts in chains | Function timeout below queue visibility timeout, downstream deadlines, what happens to work cut off mid-way | Reproduce double processing from a timeout mismatch; fix it |

**Check your understanding:** Where does the idempotency key come from when the producer did not set one? Why must the visibility timeout exceed the function timeout? What makes a poison message different from a transient failure?

### Chapter 4 · Data and the outbox in serverless backends (weeks 4–5)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 DynamoDB for event-driven apps | Access-pattern design, conditional expressions for state transitions and optimistic locking, TTL (from CLD305) | Model order state transitions as conditional updates |
| 4.2 Change feeds as outbox | DynamoDB Streams or Firestore triggers as the outbox; ordering per key; Postgres with Debezium for relational stores (from BE304) | Publish order events from the stream; prove no lost events across crashes |
| 4.3 Relational databases from functions | Connection storms, RDS Proxy, HTTP data APIs and serverless drivers; Aurora DSQL in outline | Load-test 500 concurrent functions against Postgres with and without a proxy |
| 4.4 Read models | Projections from events into query-optimised stores, rebuild from history, projection lag | Build an order-status projection and rebuild it from scratch |
| 4.5 Consistency the user sees | Read-your-writes, optimistic UI, status endpoints and polling versus push | Design the "where is my order" experience under 5-second projection lag |

**Check your understanding:** Why is the change stream a safer outbox than publishing from the handler? What breaks if two writers update the same item without conditions? How do you tell users the truth during projection lag?

### Chapter 5 · Routing and choreography (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Content-based routing | EventBridge rules and input transformation, Pub/Sub filters, fan-out with SNS | Route payment events to three consumers with different filters |
| 5.2 Archives and replay | Event archives, replay windows, idempotent consumers as a precondition | Replay one hour of events into a new consumer safely |
| 5.3 Avoiding event spaghetti | Choreography's hidden coupling, cycle detection, tracing a flow nobody owns | Draw the event flow graph and find a cycle |
| 5.4 Cross-account and cross-team buses | Bus-to-bus routing, resource policies, schema governance across teams | Deliver events from a "payments" account to an "analytics" account with least privilege |

**Check your understanding:** Why must every consumer be idempotent before you replay? When does choreography become harder to change than orchestration? Who should own the routing rules on a shared bus?

### Chapter 6 · Orchestration and durable execution (weeks 7–8)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 State machines | Step Functions Standard versus Express, retries and catches, Map state, callbacks with task tokens | Build the refund workflow with a human approval step |
| 6.2 Durable execution | Lambda durable functions, Azure Durable Functions, Temporal and Restate: deterministic replay, activities, timers, signals | Implement the same order saga in Step Functions and Temporal or Restate |
| 6.3 Sagas with compensation | Pivot steps, retriable steps, compensations that fail, idempotent activities (from BE304) | Inject failures at each step; prove the system ends consistent |
| 6.4 Versioning live workflows | Patching and versioning in Temporal, new state machine versions, draining old executions | Change a workflow while 100 executions are waiting on timers |

**Check your understanding:** Why must workflow code be deterministic? What happens to in-flight executions when you deploy a new version? When is a state machine diagram clearer than code, and when is it worse?

### Chapter 7 · Ordering and exactly-once effects (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Ordering scopes | FIFO message groups, partition keys, ordering keys; total order is rarely needed | Choose ordering keys for five event types and justify each |
| 7.2 Out-of-order handling | Version numbers, last-writer-wins traps, buffering and reordering windows | Apply events out of order and still reach the correct state |
| 7.3 Deduplication windows | SQS FIFO deduplication interval, consumer-side dedup tables, cost of long windows | Show a duplicate that slips past a 5-minute window and how the consumer catches it |
| 7.4 End-to-end exactly-once effects | Outbox + idempotent consumer + inbox as the pattern; what "exactly once" from a vendor actually means | Write a proof sketch for the course order flow |

**Check your understanding:** Why does "exactly-once delivery" in marketing usually mean "deduplicated within a window"? When is per-entity ordering enough? What state must a consumer keep to be correct under reordering?

### Chapter 8 · Edge and real-time (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Edge functions | Cloudflare Workers and similar runtimes; what belongs at the edge (auth checks, routing, caching) and what does not | Move request validation to the edge; measure latency from two regions |
| 8.2 Actors with storage | Cloudflare Durable Objects: one single-threaded object per key with strongly consistent storage | Build a per-restaurant order queue as a Durable Object |
| 8.3 Push to clients | WebSockets through API gateways or Durable Objects, server-sent events, fan-out to many clients | Push order status updates to a browser |
| 8.4 Streaming AI output | Streaming model responses through functions and edge runtimes; cancellation and partial results | Stream a model response with cancellation and a cost cap |

**Check your understanding:** Why does a single-threaded object per key simplify consistency? What is the cost of putting business logic at the edge? How do you stop paying for a stream the user abandoned?

### Chapter 9 · Testing and observability (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Testing pyramid for events | Unit tests with event fixtures, schema contract tests, integration tests in an ephemeral cloud stack per pull request; local emulation and its limits (LocalStack requires an auth token since March 2026) | Run the full flow in a per-PR stack and tear it down |
| 9.2 Tracing async flows | OpenTelemetry context in message attributes, span links for batches, trace across a workflow | One trace from HTTP request through bus, queue, function and workflow |
| 9.3 Operational signals | Queue age, consumer lag, DLQ depth and age, workflow failures, throttles | Build the dashboard and three alerts with runbooks |
| 9.4 Safe replay and redrive | DLQ triage, classification, bulk redrive with rate limits | Redrive 1,000 messages without overloading the database |

**Check your understanding:** What can an emulator never tell you about a managed service? Why is the age of the oldest message a better alert than queue depth? What must be true before you press "redrive all"?

### Chapter 10 · Security and multi-tenancy (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Least privilege per function | One role per function, resource policies on buses and queues, event-source permissions | Generate least-privilege roles and verify with an access analyser |
| 10.2 Untrusted events | Event injection, schema validation at the boundary, deserialisation risks, webhook HMAC verification (from BE301) | Reject malformed and unsigned events with tests |
| 10.3 Tenant isolation | Tenant ID in every event, per-tenant keys and quotas, attribute-based access with session tags to restrict data by tenant | Prove tenant A's function cannot read tenant B's items |
| 10.4 Denial of wallet | Concurrency limits, budgets and alarms, recursion detection, abuse of public triggers | Contain a simulated flood on a public endpoint within a set budget |

**Check your understanding:** Why is a function's role the real perimeter in a serverless backend? How can an attacker turn your autoscaling into a bill? What does tenant isolation require from event design?

### Chapter 11 · Cost, limits and regional failure (week 13)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Cost per business event | Requests, duration, transitions, bus events, logs, data transfer; pricing pages as inputs | Compute cost per 1,000 orders for the serverless half |
| 11.2 Break-even | Spiky versus steady traffic; functions versus serverless containers versus Kubernetes consumers | Plot cost against traffic for three platforms; find crossovers |
| 11.3 Throttling cascades | Concurrency quotas, downstream protection, backpressure via queues | Reproduce a throttling cascade and fix it with reserved concurrency and buffering |
| 11.4 Regional failure | Multi-region event buses (EventBridge global endpoints), replicated tables, idempotency across regions | Fail over the bus and prove no double processing |

**Check your understanding:** Why is logging often the largest hidden serverless cost? At what traffic level did your design stop being cheapest, and what would you change? What new duplicate risk does multi-region failover create?

### Chapter 12 · AI workloads on event-driven backends (week 14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Async AI jobs | Queue-based document and inference pipelines, batch APIs (about 50% cheaper at several providers), retries and partial failure | Move a synchronous AI call to an async job with status updates |
| 12.2 Agents on durable execution | Multi-step agent tasks as workflows: checkpoints, timeouts on model calls, idempotent tool calls, human approval | Run a three-tool agent task as a durable workflow that survives a crash |
| 12.3 Reviewing generated stacks | Checking AI-generated SAM, CDK or Terraform for IAM wildcards, missing DLQs, timeout mismatches and unbounded concurrency | Review two generated stacks and file every defect |

**Check your understanding:** Why is an agent's tool call a side effect that needs an idempotency key? What does a durable workflow give an agent that a long-running function does not? Which defect in a generated stack is most expensive in production?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Event storm and contracts | Event catalogue |
| 2 | 2 | Lab 2 · Platform decision matrix | — |
| 3 | 3 | Lab 3 · Idempotent handlers | — |
| 4 | 4 | Lab 4 · Stream outbox | **P1 due** |
| 5 | 4 | Lab 4 (cont.) · Projections | — |
| 6 | 5 | Lab 5 · Routing and replay | Mid-term (AI off): design and failure analysis |
| 7 | 6 | Lab 6 · Sagas two ways | — |
| 8 | 6 | Lab 6 (cont.) · Workflow versioning | — |
| 9 | 7 | Lab 7 · Out-of-order events | **P2 due** |
| 10 | 8 | Lab 8 · Durable Objects and push | — |
| 11 | 9 | Lab 9 · Tracing and redrive | Operations dashboard |
| 12 | 10 | Lab 10 · Tenant isolation | — |
| 13 | 11 | Cost and failover experiments | Cost model |
| 14 | 12 | AI jobs and agents | **P3 due** |
| 15 | Review | Live incident drill on the event platform and oral defence of P3 | Final exam |

## Working with AI in this course

- **Use AI for:** generating infrastructure-as-code stacks, handler boilerplate, event fixtures and AsyncAPI drafts; explaining provider limits and pricing pages; suggesting failure scenarios to test.
- **Do without AI (drills):** event storming and event design; reasoning about duplicates, ordering and timeouts on paper; the saga failure table; the mid-term and final drill.
- **Verify AI output by:** running the duplicate, reorder, crash and replay test suites on every change; checking generated IAM with an access analyser; comparing generated timeouts and visibility timeouts against your own table; pricing every generated architecture with the provider calculator before adopting it.
- **Where AI still fails here:** record every AI-generated handler or stack that passed review but failed a duplicate or replay test. Expect missing idempotency, function timeouts longer than visibility timeouts, and DLQs that nobody alerts on.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1–P3 | 35% |
| Mid-term design and failure analysis (AI off) | 10% |
| Final: live incident drill + oral defence of P3 | 30% |

**Mastery gate.** You pass when you can, with AI tools off: (1) given a business process, produce the events, contracts, ordering keys and idempotency design in 60 minutes; (2) given a production symptom (duplicates, stuck workflow, growing DLQ, throttling), find the cause from dashboards and traces within 30 minutes; (3) show your P3 system processing 10,000 events with injected crashes and redeliveries with zero duplicate effects.

## Industry reality

Event-driven designs are common where work is naturally asynchronous: Zerodha reported emailing 1.5 million contract notes in under 25 minutes after a backend revamp ([Zerodha, Feb 2024](https://zerodha.com/z-connect/updates/1-5-million-contract-notes-sent-in-less-than-25-minutes)), and Indian payment providers expose webhooks that merchants must verify and deduplicate (BE301). Workflow engines such as Temporal and Step Functions are now routine interview topics for backend roles because they encode sagas, timeouts and retries that teams once hand-built.

**Interview questions from this course**

1. *A customer was charged twice. The flow is API → queue → function → payment provider. Find the cause.* Strong answer: at-least-once delivery plus a missing or wrong idempotency key, or a function timeout above the visibility timeout; checks logs by message ID; fixes with provider idempotency keys, conditional writes, and correct timeouts; adds a ledger reconciliation.
2. *Orchestration or choreography for order → payment → inventory → delivery?* Strong answer: orchestration for the core saga (visibility, compensation, timeouts) with events published for other consumers; names failure handling and who owns the flow.
3. *How do you change a workflow definition when thousands of executions are in flight?* Strong answer: versioning or patching APIs, deterministic replay constraints, running old and new versions side by side, draining, and tests that replay recorded histories.
4. *When does serverless stop being the cheapest option?* Strong answer: steady high utilisation, long-running work, heavy logging; computes cost per event versus per-node cost; mentions serverless containers and Kubernetes consumers as middle grounds and the operational cost of each.
5. *How would you replay a day of events into a new service safely?* Strong answer: idempotent consumer first, separate consumer identity, rate-limited replay from an archive, side effects disabled or deduplicated, monitoring of downstream load, and verification by comparing projections.

## Resources (free first)

- **Design:** EventStorming — https://www.eventstorming.com/ ; CloudEvents — https://cloudevents.io/ ; AsyncAPI — https://www.asyncapi.com/docs ; EventCatalog — https://www.eventcatalog.dev/
- **Platforms:** AWS Lambda developer guide — https://docs.aws.amazon.com/lambda/latest/dg/welcome.html ; Amazon EventBridge — https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html ; AWS Step Functions — https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html ; Powertools for AWS Lambda (Python) idempotency — https://docs.powertools.aws.dev/lambda/python/latest/utilities/idempotency/ ; Google Cloud Run — https://cloud.google.com/run/docs ; Azure Durable Functions — https://learn.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-overview ; Knative — https://knative.dev/docs/ ; KEDA — https://keda.sh/docs/
- **Durable execution and edge:** Temporal documentation — https://docs.temporal.io/ ; Restate documentation — https://docs.restate.dev/ ; Cloudflare Durable Objects — https://developers.cloudflare.com/durable-objects/
- **Paid, optional:** none needed; free tiers of AWS, Google Cloud and Cloudflare cover the labs if you tear down resources.

## Sources

All checked 12 Oct 2026.

- AWS, Lambda durable functions announcement (Dec 2025) — https://aws.amazon.com/about-aws/whats-new/2025/12/lambda-durable-multi-step-applications-ai-workflows/
- CNCF, CloudEvents graduation (25 Jan 2024) — https://www.cncf.io/announcements/2024/01/25/cloud-native-computing-foundation-announces-the-graduation-of-cloudevents/ ; Knative graduation (8 Oct 2025) — https://www.cncf.io/announcements/2025/10/08/cloud-native-computing-foundation-announces-knatives-graduation/
- LocalStack 2026.03.0 release (auth token required) — https://blog.localstack.cloud/localstack-for-aws-release-2026-03-0/
- Batch API discounts: OpenAI (50%) — https://developers.openai.com/api/docs/guides/batch ; Gemini (50%) — https://ai.google.dev/gemini-api/docs/batch-api
- Zerodha, "1.5 million contract notes sent in less than 25 minutes" (5 Feb 2024) — https://zerodha.com/z-connect/updates/1-5-million-contract-notes-sent-in-less-than-25-minutes

_Last reviewed: 2026-10_
