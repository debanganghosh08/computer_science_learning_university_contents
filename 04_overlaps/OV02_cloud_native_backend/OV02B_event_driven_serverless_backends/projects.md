# OV02B · Labs and projects

Labs run on one cloud provider's free tier (AWS is used in examples; Google Cloud and Azure equivalents are accepted) plus one Kubernetes cluster with KEDA for comparison, and Cloudflare's free tier for the edge lab. Every stack is defined as code and torn down after each session. Each lab ships code, tests and measured numbers.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Event storm and contracts | Run an event storm for the order platform; write AsyncAPI documents and CloudEvents schemas for five events; add a compatibility check to CI | Storm photo or board export, AsyncAPI files, CI run blocking a breaking change | 4 h |
| 2 · Platform decision matrix | For six workloads (order intake, notifications, PDF invoices, settlement, analytics feed, AI summaries), choose a compute and transport option and prototype two of them | Matrix with reasons, latency and cost of the two prototypes | 4 h |
| 3 · Idempotent handlers | Implement an SQS-triggered handler with Powertools idempotency and partial batch responses; send each event 100 times | Effect count (must be 1 per event), batch-failure test, timeout table | 5 h |
| 4 · Stream outbox and projections | Write orders with conditional updates in DynamoDB; publish events from Streams; build a status projection and rebuild it from history | Crash-injection run showing zero lost or invented events, rebuild time | 7 h |
| 5 · Routing and replay | Route payment events through EventBridge rules to three consumers; archive and replay one hour into a new consumer | Rule definitions, replay report with downstream load graph | 4 h |
| 6 · Sagas two ways | Implement the order saga in Step Functions and in Temporal or Restate; inject failures at every step; change the workflow while executions wait | Failure table (step × outcome), version-change evidence, comparison note | 8 h |
| 7 · Out-of-order events | Apply versioned events in random order and with duplicates; reach the correct final state | Property-based test results over 10,000 random sequences | 4 h |
| 8 · Durable Objects and push | Per-restaurant order queue as a Durable Object; push status to a browser over WebSockets | Demo, latency from two regions, consistency argument | 4 h |
| 9 · Tracing and redrive | One trace across API, bus, queue, function and workflow; dashboard with oldest-message age and DLQ alerts; rate-limited redrive of 1,000 messages | Trace screenshot, alert runbooks, redrive log | 5 h |
| 10 · Tenant isolation | Per-tenant data access with session tags or equivalent; per-tenant concurrency limits; flood test on a public endpoint | Access-denied tests, budget alarm evidence | 4 h |

## Projects

### P1 · Notifications service (L1, ~6 hours)

**Real-world inspiration.** Brokers and fintechs send millions of statements and alerts against deadlines; Zerodha has described sending 1.5 million contract notes in under 25 minutes (Feb 2024). The service here is a smaller, illustrative version.

**What to build.** An event-driven notification service: consumes `OrderPlaced`, `OrderDelivered` and `RefundIssued` events, renders templates, sends through a mock email/SMS provider with rate limits, and records delivery status.

**Acceptance criteria**
- Each event produces exactly one notification even when delivered 5 times (test with 1,000 events).
- 100,000 notifications complete within 15 minutes against a mock provider limited to 200 requests per second, with no provider throttling errors.
- Poison events land in a DLQ with an alert; a redrive script replays them after a fix.
- Infrastructure is code; `deploy` and `destroy` each run in one command.

**Stretch goals.** Per-user channel preferences and quiet hours; a cost report per 100,000 notifications.

**What it proves to an employer.** You can build the asynchronous workhorse every product needs, correctly and within a deadline.

### P2 · Refunds with a durable workflow (L2, ~15 hours)

**Real-world inspiration.** Refunds and settlements wait for external parties for hours or days and must never pay twice; workflow engines exist because hand-built timers and retries fail in exactly these flows.

**What to build.** A refund workflow: request validation, fraud-check activity, human approval above a threshold, payment-provider refund call with an idempotency key, ledger update, customer notification, and compensation when steps fail. Implement in one durable-execution engine and document how it would look in the other.

**Acceptance criteria**
- Crash injection at every step (100 runs per step) ends with zero double refunds and every workflow in a terminal state.
- Human approval can wait 7 simulated days via timers; time-skipping tests prove behaviour without waiting.
- A workflow code change is deployed while 50 executions are waiting; all complete correctly (versioning evidence).
- Every activity is idempotent; the report lists each activity's idempotency mechanism.
- One trace shows a refund from API call through workflow completion.

**Stretch goals.** Replay recorded workflow histories in CI to catch non-deterministic changes before deploy.

**What it proves to an employer.** You can implement long-running business processes that are correct under failure, a skill payments and marketplace teams test directly.

### P3 · Event-driven order platform (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** Food-delivery and quick-commerce backends combine a synchronous ordering core with a large asynchronous estate of events, workflows and notifications. The design below is illustrative and is the serverless half of the [OV02 capstone](../README.md).

**What to build.** The asynchronous side of the order platform: event catalogue and contracts, stream-based outbox, routing on a bus, order and refund workflows, status projections, push updates to clients, an AI summary job for support tickets, tenant isolation for two restaurant groups, full tracing, and a cost model.

**Acceptance criteria**
- 10,000 orders processed with injected function crashes, redeliveries and a 2-minute downstream outage: zero duplicate effects, zero lost events, all orders terminal within 10 minutes of recovery.
- Order status visible to clients within 3 seconds p95 of the state change.
- Replaying one day of archived events into a new analytics consumer produces totals matching the source of truth exactly.
- Cost per 1,000 orders reported at 1, 10 and 100 orders per second, with a chart against a KEDA-on-Kubernetes alternative and the crossover point explained.
- Least-privilege review: no wildcard actions in any function role; an access-analyser report is attached.
- Three architecture decision records, including one about a limit you designed around.

**Stretch goals.** Multi-region event bus failover with a measured recovery time; edge validation with Durable Objects for per-restaurant ordering.

**What it proves to an employer.** You can design, build and operate an event-driven backend end to end and defend its correctness and cost with evidence.

## Feeds into

- The [OV02 capstone](../README.md): P3 is the event-driven half.
- [BE501 Frontier Seminar: Durable Execution, Serverless and Edge Backends](../../../03_majors/backend_engineering/year_5/BE501_frontier_seminar_durable_execution_serverless/README.md): workflow versioning and exactly-once effects lead into its research chapters.
- [OV04B LLMOps at Scale](../../OV04_mlops_ml_platform/OV04B_llmops_at_scale/README.md) and [OV12 Agent Infrastructure](../../OV12_agent_infrastructure_platform/README.md): durable workflows for agents and async AI jobs.
- [LCH502 Career Launch and Founder Studio](../../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md): a serverless event-driven stack is a low-fixed-cost base for a solo product.
