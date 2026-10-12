# CLD401 · Labs and projects

Labs use one provider unless stated; P3 needs two platforms. Before any load test, arm a budget action that stops or de-permissions resources at your ceiling. Deploy with IaC (SAM, CDK or Terraform/OpenTofu) so every stack can be destroyed in one command. Lab 7's design and the cost model in Lab 10 are done without AI.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Lifecycle and concurrency | Show environment reuse and init behaviour on Lambda; compare instance counts under the same load on Cloud Run (per-instance concurrency) | Logs proving reuse, instance-count graphs, a short explanation | 3 h |
| 2 · Designing around limits | Rebuild a report export that exceeds the 6 MB synchronous payload limit using presigned URLs or response streaming | Working design, sequence diagram and limit references | 3 h |
| 3 · Cold starts | Measure init duration and p99 for a bursty workload; reduce it with packaging, Arm, lazy init, then SnapStart or provisioned concurrency | Before/after p50/p99, init duration and monthly cost of each option | 5 h |
| 4 · Throttling and downstream protection | Spike to 5,000 requests per second against a function that writes to a small Postgres; then add a queue buffer, reserved concurrency and a pooling proxy | Error and latency graphs before and after; DB connection counts | 5 h |
| 5 · Queues done right | SQS (or Service Bus) consumer with batch processing, partial batch responses, DLQ, redrive and alarm on DLQ depth | Test showing only failed messages retry; redrive runbook | 4 h |
| 6 · Buses and streams | Route order events with EventBridge (or Event Grid/Eventarc) content filters to three consumers; process a Kinesis or Pub/Sub stream with a poison record | Routing rules, archive-and-replay demo, poison handling evidence | 4 h |
| 7 · Idempotency under fire (design without AI) | Payment-capture consumer under 20% duplicate delivery and 5% injected timeouts | Ledger showing zero double captures across 10,000 events, and the design note | 5 h |
| 8 · Workflows and sagas | KYC onboarding with a human approval: once in Step Functions, once with durable functions (Lambda or Azure) | Both implementations, a failure-and-compensation run, cost per 1,000 executions | 6 h |
| 9 · Serverless containers | Same API on Cloud Run and Azure Container Apps (or Fargate), and a Knative service on kind scaled to zero | Cold-start and latency comparison, scale-to-zero evidence | 4 h |
| 10 · Tracing and cost (cost model without AI) | End-to-end OpenTelemetry trace across API, queue, function and workflow; then a monthly cost model at 50 million requests | Exported trace (JSON) and the cost model with its assumptions | 5 h |

## Projects

### P1 · A safe, cheap image pipeline (L1, ~6 hours)

**Real-world inspiration:** S3-triggered processing is the classic serverless pattern, and AWS added recursive loop detection to Lambda because functions writing back to their trigger bucket caused runaway bills ([Lambda docs](https://docs.aws.amazon.com/lambda/latest/dg/invocation-recursion.html)).

**What to build:** an upload API with presigned URLs, a function that validates and resizes images into a *different* bucket, a DLQ for failures, structured logs and a budget action.

**Acceptance criteria:**
- 1,000 uploads processed with zero duplicates in the output bucket and every failure in the DLQ with a reason.
- A deliberately misconfigured version that writes to its own trigger bucket is stopped by loop detection or your guard within one minute; show the evidence.
- Per-function IAM role with no wildcard actions.
- **Cost ceiling:** US$1 (stays within free tiers).

**Stretch goals:** malware scanning step; Arm build with measured cost difference.

**What it proves to an employer:** you build event-driven code that cannot quietly burn money.

### P2 · An order pipeline that is correct under duplicates and spikes (L2, ~15 hours)

**Real-world inspiration:** food-delivery and e-commerce platforms in India see sharp spikes at meal times and during sales; their order flows must survive retries and partial failures. The [AWS Builders' Library on timeouts, retries and backoff](https://builder.aws.com/content/3EumjoZascWd1oZiEgL8ORlv3qE/timeouts-retries-and-backoff-with-jitter) explains why naive retries amplify outages. The business is an *illustrative scenario*.

**What to build:** an order API (synchronous) that writes an order and publishes an `OrderPlaced` event; consumers for payment capture, restaurant notification and rider assignment via an event bus; a workflow for order cancellation with compensation; idempotency on every consumer; DLQs, alarms and an end-to-end trace.

**Acceptance criteria:**
- A load test from 50 to 2,000 orders per second over 2 minutes completes with p99 API latency under 400 ms and no lost orders.
- With 20% duplicate delivery injected on every consumer, there are zero double payments, notifications or rider assignments (checked by reconciliation queries).
- Killing the payment consumer for 5 minutes causes no data loss; backlog drains within 10 minutes after recovery.
- A cancellation after payment triggers compensation (refund event) and the workflow history shows each step.
- Every order can be traced across all hops with one ID.
- **Cost ceiling:** US$15.

**Stretch goals:** event schema registry with a breaking-change check in CI; replay of archived events into a new consumer.

**What it proves to an employer:** you can build asynchronous systems that are correct, observable and resilient, which is rarer than building ones that merely work.

### P3 · A serverless AI agent backend with sandboxed code execution and a cost case (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:**
- AWS's Lambda durable functions (December 2025) target multi-step applications and AI workflows ([AWS](https://aws.amazon.com/about-aws/whats-new/2025/12/lambda-durable-multi-step-applications-ai-workflows/)).
- Lambda MicroVMs (June 2026) target isolated execution of user and AI-generated code ([AWS](https://aws.amazon.com/about-aws/whats-new/2026/06/aws-lambda-microvms)).
- The product is an *illustrative scenario*: a data-analysis assistant for small Indian businesses that writes and runs Python on uploaded spreadsheets.

**What to build:**
- a chat API with streaming responses;
- a durable workflow per user task: plan, call a managed model, generate code, run it in an isolated sandbox with no network and a time limit, check the result, retry or ask the user;
- idempotent tool calls and a queue in front of the model endpoint to respect its quota;
- per-tenant usage metering;
- the same core flow on a second platform (for example Cloud Run with Workflows, or Azure Functions with Durable Functions);
- a cost and latency comparison, and a break-even memo against a container-based design.

**Acceptance criteria:**
- **Durability:** killing the workflow's compute mid-task (or forcing a model timeout) resumes from the last checkpoint without repeating completed tool calls; show the history.
- **Isolation:** generated code that tries to open a network connection, read environment variables or run longer than the limit is blocked, and the attempt is logged.
- **Quotas:** at twice the model endpoint's rate limit, requests queue and complete with no 429 errors reaching users.
- **Metering:** per-tenant tokens, compute seconds and cost are recorded and reconcile within 5% of the bill for a test run.
- **Comparison:** p50/p99 task latency, cost per 1,000 tasks and operational differences on both platforms, with a break-even chart against containers.
- **AI review:** a table of defects found in an assistant-generated version of the workflow (retries, idempotency, IAM, limits).
- **Cost ceiling:** US$40 including model usage; use a small model and cap tokens per task.

**Stretch goals:** Lambda Managed Instances for steady parts of the load with a cost comparison; OpenTelemetry GenAI semantic conventions in traces.

**What it proves to an employer:** you can build the backend that AI products need, with isolation, durability, quotas and cost under control.

## Feeds into

- [CLD403 FinOps](../CLD403_finops_and_cloud_cost_engineering/README.md): unit economics and cost per request.
- [CLD404 AI Infrastructure](../CLD404_ai_infrastructure_in_the_cloud_gpus_inference/README.md): model endpoints, quotas and inference serving.
- [CLD501 Frontier Seminar](../../year_5/CLD501_frontier_seminar_sovereign_cloud_confidential/README.md): isolation and confidential computing.
- [BE501 Durable Execution, Serverless and Edge Backends](../../../backend_engineering/year_5/BE501_frontier_seminar_durable_execution_serverless/README.md) and [OV12 Agent Infrastructure](../../../../04_overlaps/OV12_agent_infrastructure_platform/README.md).
