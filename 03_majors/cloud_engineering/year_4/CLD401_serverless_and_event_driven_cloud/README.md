# CLD401 · Serverless and Event-Driven Cloud

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 7 | 4 (≈ 120 hours) | L3 → L4 | [CLD301](../../year_3/CLD301_cloud_architecture_on_aws_azure_and_google_cloud/README.md) | [CLD501](../../year_5/CLD501_frontier_seminar_sovereign_cloud_confidential/README.md), [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) |

Part of the [Cloud Engineering major](../../README.md). Messaging theory (queues, logs, ordering, exactly-once processing) is taught for application developers in [BE304](../../../backend_engineering/year_3/BE304_asynchronous_systems_queues_streams_and_event/README.md), and durable execution and edge runtimes as a research topic in [BE501](../../../backend_engineering/year_5/BE501_frontier_seminar_durable_execution_serverless/README.md). This course is the platform view: how serverless runtimes and managed event services behave, scale, fail and bill, and how to build production systems from them on AWS, Azure and Google Cloud.

## Why this course matters now

Serverless is where the cloud is still changing fastest. In twelve months AWS made Lambda's INIT phase billable for every configuration (1 August 2025), launched Lambda Managed Instances to run functions on your own EC2 capacity (November 2025), added Lambda durable functions that checkpoint and can suspend for up to a year (December 2025), and introduced Lambda MicroVMs for isolating user and AI-generated code for up to 8 hours (June 2026). Google merged Cloud Functions into Cloud Run (August 2024) and made Cloud Run worker pools generally available (April 2026). Microsoft is retiring the Linux Consumption plan for Azure Functions on 30 September 2028 in favour of Flex Consumption. Knative graduated in the CNCF in October 2025.

The model is attractive because you pay per use and operate almost nothing, but the failure modes are subtle: retries that double-charge customers, throttling that cascades into a database, cold starts on a payment path, a bill that explodes because a function calls itself. AI assistants generate handler code and templates well. They rarely reason about delivery semantics, concurrency limits or cost at scale, which are exactly what this course trains.

## Learning outcomes

By the end you can:

1. **Explain** how function platforms run code (microVMs, execution-environment lifecycle, concurrency models) and **compare** Lambda, Azure Functions, Cloud Run functions and serverless containers.
2. **Measure and reduce** cold-start latency with package design, SnapStart, provisioned concurrency, minimum instances and runtime choice.
3. **Design** for platform limits (timeouts, payload sizes, concurrency and scaling rates) and **protect** downstream systems from serverless scale.
4. **Build** event-driven systems with queues, topics, event buses, streams and schedulers, and **choose** between them.
5. **Implement** idempotent consumers, dead-letter handling, ordering and replay, and **prove** correctness under duplicate delivery.
6. **Orchestrate** long-running workflows with Step Functions, Durable Functions, Workflows or Lambda durable functions.
7. **Model** serverless cost per request and **find** the break-even point against containers and VMs.
8. **Trace and debug** asynchronous flows end to end with OpenTelemetry and structured logs.

## Chapters and lessons

### Chapter 1 · What serverless is underneath (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 The spectrum | Functions, serverless containers (Cloud Run, Azure Container Apps, Fargate), managed services; what "serverless" removes and what it keeps | Classify 10 services on operational burden and billing granularity |
| 1.2 Isolation | Firecracker microVMs (NSDI 2020), gVisor, why multi-tenant functions need VM-grade isolation; Lambda MicroVMs for untrusted code | Read the Firecracker paper's design goals and summarise the trade-offs |
| 1.3 Execution environment lifecycle | INIT, INVOKE, SHUTDOWN; environment reuse; what persists between invocations | Prove state reuse with a global counter and explain the danger |
| 1.4 Concurrency models | Lambda's one request per environment versus Cloud Run and Flex Consumption per-instance concurrency; Lambda Managed Instances on your own EC2 | Load-test the same handler on two platforms and compare instance counts |

**Check your understanding:** (1) Why does a global variable sometimes keep its value between requests? (2) Why do function platforms use microVMs instead of plain containers? (3) When does per-instance concurrency save money, and what does it risk?

### Chapter 2 · Functions in depth (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Lambda limits as design inputs | 128–10,240 MB memory (1,769 MB ≈ one vCPU), 15-minute timeout, 6 MB synchronous payload, 200 MB streamed responses, 1 MB asynchronous payload, 250 MB unzipped package or 10 GB image, `/tmp` up to 10 GB | Redesign a 40 MB report export that breaks the synchronous payload limit |
| 2.2 Packaging | Zip versus container images, layers, dependency trimming, Arm builds | Cut a Python package from 120 MB to under 20 MB |
| 2.3 Azure Functions and Cloud Run functions | Flex Consumption plan, triggers and bindings; Cloud Run functions as Cloud Run services | Port one handler to both platforms |
| 2.4 Configuration and secrets | Environment variables (4 KB limit on Lambda), parameter stores, secrets caching extensions | Load a secret once per environment and refresh it safely |

**Check your understanding:** (1) Why does more memory sometimes make a function cheaper? (2) What is the right pattern for returning a large file from a function? (3) Why should a secret not live in an environment variable?

### Chapter 3 · Cold starts and performance (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Measuring cold starts | Init duration in logs, p99 versus average, traffic shape; INIT billing since 1 August 2025 | Graph cold-start frequency and latency for a bursty workload |
| 3.2 Reducing them | Lazy loading, smaller packages, runtime choice, Arm, avoiding VPC overheads | Halve a function's init time and show the evidence |
| 3.3 Pre-warming options | Provisioned concurrency, SnapStart (Java, Python, .NET) and its uniqueness pitfalls, Cloud Run minimum instances and startup CPU boost, Azure always-ready instances | Compare p99 and monthly cost of three options for a payment API |
| 3.4 Tuning memory | Power tuning, cost versus latency curves | Find the cheapest memory size for three handlers |

**Check your understanding:** (1) Why can SnapStart break code that generates random IDs at init? (2) When is provisioned concurrency cheaper than tolerating cold starts? (3) Why measure p99, not average?

### Chapter 4 · Scale and its limits (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Concurrency quotas | Default 1,000 concurrent executions per region, scaling rate of 1,000 environments every 10 seconds per function, reserved and provisioned concurrency, throttling behaviour by invocation type | Throttle a function deliberately and record what each caller sees |
| 4.2 Protecting downstreams | Database connection storms, RDS Proxy, queue buffering, reserved concurrency as a valve, API Gateway's 10,000 requests per second default against Lambda's 1,000 concurrency | Protect a small Postgres from a 5,000-request spike |
| 4.3 Recursion and runaway cost | Recursive loop detection, event loops between services, budget guards | Trigger and stop an S3 → Lambda → S3 loop in a sandbox with a budget action |
| 4.4 Networking | Functions in VPCs, NAT costs, private endpoints, egress IPs | Give a function a fixed egress IP for a partner allow-list |

**Check your understanding:** (1) Why can serverless scale take down a database that never had a problem before? (2) What happens to an asynchronous invocation when the function is throttled? (3) Why does a function in a VPC need a NAT or endpoints?

### Chapter 5 · Event sources and routing (weeks 5–6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Invocation types | Synchronous, asynchronous (with retries and destinations), poll-based event source mappings | Map 10 AWS triggers to their invocation type and retry behaviour |
| 5.2 Queues | SQS standard and FIFO, visibility timeout, batch size and window, partial batch responses, DLQs, redrive; Azure Service Bus; Google Cloud Tasks | Process a batch where 3 of 10 messages fail, without reprocessing the 7 |
| 5.3 Topics and buses | SNS fan-out and filtering, EventBridge rules, schema registry, archives and replay, EventBridge Pipes and Scheduler; Google Pub/Sub and Eventarc; Azure Event Grid | Route order events to three consumers with content filtering |
| 5.4 Streams | Kinesis and DynamoDB Streams, shards and ordering, checkpointing, bisect-on-error; Pub/Sub ordering keys; Event Hubs | Process a stream with a poison record without blocking the shard |
| 5.5 Standard event formats | CloudEvents (CNCF graduated, January 2024), AsyncAPI for documenting event contracts | Publish an AsyncAPI document for your events |

**Check your understanding:** (1) Why does visibility timeout need to be longer than function timeout? (2) When would you choose a stream over a queue? (3) What does an event archive let you do after a bug?

### Chapter 6 · Delivery semantics and correctness (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 At-least-once everywhere | Where duplicates come from (retries, redelivery, replays), why exactly-once delivery is not offered | Count duplicates in a run with injected timeouts |
| 6.2 Idempotent consumers | Idempotency keys, conditional writes, Powertools idempotency utility, expiry of keys | Make a payment-capture consumer safe under 20% duplicate delivery |
| 6.3 Ordering | FIFO groups, partition keys, out-of-order handling with version numbers | Rebuild a correct balance from out-of-order events |
| 6.4 Failure handling | DLQs and on-failure destinations, poison messages, replay tooling, alerting on DLQ depth | Write a redrive runbook and test it |

**Check your understanding:** (1) Why can a retry after a timeout double-charge a customer? (2) What makes a DLQ useless in practice? (3) When is ordering per key enough?

### Chapter 7 · Workflows and durable execution (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Step Functions | Standard versus Express workflows, states, retries and catches, Map state, JSONata, service integrations, waiting for callbacks | Model a KYC onboarding flow with a human approval step |
| 7.2 Durable functions | Lambda durable functions (checkpointing, suspend without compute charges for up to a year), Azure Durable Functions, Google Workflows; Temporal as an open alternative | Implement the same flow as durable code and compare |
| 7.3 Sagas | Compensation, timeouts, partial failure in multi-service flows | Add compensation when the third step fails |
| 7.4 Choosing | Visual state machines versus code, cost per transition versus per duration, observability | Write a decision note for three workflows |

**Check your understanding:** (1) Why must durable code be deterministic on replay? (2) When does an Express workflow's at-least-once semantics matter? (3) What is the cost driver of each workflow service?

### Chapter 8 · Serverless containers (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Cloud Run | Services, jobs, worker pools (generally available April 2026), concurrency, minimum instances, GPUs | Deploy an API and a background worker pool |
| 8.2 Azure Container Apps and Fargate | Scale rules (KEDA-based on Container Apps), revisions, Fargate tasks with ECS | Run the same container on two platforms |
| 8.3 Knative | Serving and Eventing on Kubernetes (CNCF graduated, October 2025), scale to zero | Run a Knative service on kind and scale it to zero |
| 8.4 Functions or containers | Long requests, WebSockets, custom runtimes, portability, cost | Decide for five workloads with numbers |

**Check your understanding:** (1) Why do serverless containers suit long-lived connections better than functions? (2) What does scale-to-zero cost the first user? (3) What does Knative give you that Cloud Run does not, and the reverse?

### Chapter 9 · Cost engineering for serverless (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 The pricing model | Lambda: $0.20 per million requests and $0.0000166667 per GB-second for x86 in us-east-1, with a free tier of 1 million requests and 400,000 GB-seconds a month; Arm pricing; Cloud Run and Azure equivalents | Build a cost model for 50 million requests a month |
| 9.2 Hidden costs | API gateways, logs, NAT, workflow transitions, event bus events, data transfer | Find the largest non-compute line in a sample bill |
| 9.3 Break-even analysis | Steady versus spiky traffic; functions versus Lambda Managed Instances versus containers versus VMs | Plot cost against traffic for the four options |

**Check your understanding:** (1) Why is serverless often cheapest for spiky traffic and expensive for steady traffic? (2) Why can logging cost more than compute? (3) What changes the break-even point most?

### Chapter 10 · Observability and testing (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Tracing async flows | Correlation IDs across queues and buses, OpenTelemetry for Lambda, X-Ray, Cloud Trace, Application Insights | Trace one order across API, queue, function and workflow |
| 10.2 Logs and metrics | Structured logging, Powertools, embedded metric format, sampling and log cost | Cut log volume by 70% without losing debuggability |
| 10.3 Testing | Unit tests with event fixtures, local emulation (SAM, Functions Core Tools, LocalStack, which needs an auth token since March 2026), and tests in a real cloud account | Write an integration test suite that runs in an ephemeral stack |

**Check your understanding:** (1) Why do local emulators miss real failures? (2) What breaks tracing across an event bus? (3) How do you test retry behaviour?

### Chapter 11 · Security (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Per-function least privilege | One role per function, resource policies, event-source permissions | Remove every unused permission from a 10-function app |
| 11.2 Entry points | Function URLs, API authorisers, JWT validation, rate limiting | Lock a public function behind an authoriser |
| 11.3 Event injection and supply chain | Untrusted event data, deserialisation, dependency risks, code signing for Lambda | Find the injection in a sample handler that builds shell commands from an S3 key |

**Check your understanding:** (1) Why is an S3 object key untrusted input? (2) What does code signing prevent? (3) Why share no roles between functions?

### Chapter 12 · Serverless for AI systems (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Agent backends | Durable workflows for multi-step AI tasks, timeouts on model calls, idempotent tool calls | Build an agent workflow that survives a model timeout mid-task |
| 12.2 Running untrusted code | Lambda MicroVMs and similar sandboxes for AI-generated code; network and time limits | Run AI-generated code in an isolated sandbox with no network |
| 12.3 Event-driven inference | Queue-based batch inference, streaming responses, quotas on managed model APIs | Put a queue in front of a rate-limited model endpoint |
| 12.4 Reviewing generated serverless apps | Checking IAM, retries, idempotency, cost and limits in assistant-generated templates | Review a generated SAM or Terraform app and list defects |

**Check your understanding:** (1) Why must a tool call made by an agent be idempotent? (2) Why does AI-generated code need VM-level isolation? (3) How do you keep a model's rate limit from becoming your outage?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1: lifecycle and concurrency models | Comparison report |
| 2 | 2 | Lab 2: limits redesign | Large-export pattern |
| 3 | 3 | Lab 3: cold-start reduction | Before/after graphs; P1 starts |
| 4 | 4 | Lab 4: throttling and downstream protection | Protected database; P1 due |
| 5 | 5 | Lab 5: queues, partial batches, DLQs | Working consumer |
| 6 | 5 | Lab 6: buses and streams | Event routing; P2 starts |
| 7 | 6 | Lab 7: idempotency under duplicates | Zero double-charges |
| 8 | 7 | Lab 8: workflows and sagas | Two implementations |
| 9 | 8 | Lab 9: Cloud Run and Knative | Scale-to-zero demo; P2 due |
| 10 | 9 | Cost model and break-even | Plot and memo |
| 11 | 10 | Lab 10: tracing and tests | End-to-end trace; P3 starts |
| 12 | 11 | Security hardening | Permission diff |
| 13 | 12 | AI workflow and sandbox | Working agent backend |
| 14 | 12 | P3 completion | Demo and load test |
| 15 | Review and exam | — | Written exam and design oral |

## Working with AI in this course

- **Use AI for:** handler boilerplate, SAM/CDK/Terraform templates, event fixture generation, Step Functions definitions from a described flow, log-query writing, and summarising service quota pages. Named tools: Claude Code, GitHub Copilot, Kiro, Amazon Q Developer, Gemini Code Assist.
- **Do without AI (drills):** predicting retry and throttling behaviour per invocation type, idempotency design, the cost model in Chapter 9, and the design oral.
- **Verify AI output by:** injecting duplicates, timeouts and throttles in tests; checking every quoted limit against the quotas page; running IAM Access Analyzer on generated roles; load-testing at 10× expected traffic in a sandbox with a budget action armed.
- **Where AI still fails here (show it):** generated consumers are often not idempotent, use a visibility timeout shorter than the function timeout, grant `*` permissions, or omit DLQs. Ask an assistant for "an S3-triggered image resizer that writes thumbnails" and check whether it can loop on its own output. Record every defect for P3.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs | 25% |
| Projects P1 / P2 / P3 | 5% / 15% / 25% |
| Written exam (semantics, limits, cost, workflows) | 20% |
| Design oral | 10% |

**Mastery gate:** you pass when you can, without AI help, (a) design an event-driven flow for an unseen brief and state, for every hop, the delivery guarantee, retry behaviour, ordering, failure destination and idempotency mechanism; (b) show a system you built processing a run with 20% injected duplicates and 5% injected failures with zero incorrect side effects; and (c) produce a monthly cost model for a given traffic profile within 15% of a measured bill.

## Industry reality

Event-driven designs sit behind payments notifications, order pipelines, media processing and AI agent backends. Platform teams adopt serverless for spiky, event-shaped workloads and move steady high-volume services to containers when the cost curve crosses, so the break-even analysis in Chapter 9 is an everyday skill. Providers now also offer serverless primitives for AI agents, such as Bedrock AgentCore and Lambda MicroVMs, which makes isolation, timeouts and idempotent tool calls part of the job.

Interview questions from this course:

1. **"Design a system that sends a confirmation SMS and email for every UPI payment, exactly once from the user's view."** Cover at-least-once delivery, idempotency keys per payment and channel, fan-out, retries with back-off, DLQs, provider rate limits and monitoring.
2. **"Our Lambda-based API has bad p99 latency at 9 a.m. Why, and what do you do?"** Cover cold starts from scale-out, init work, package size, VPC, provisioned concurrency or SnapStart, and measuring before and after.
3. **"A spike of 10,000 requests per second hit our functions and the database fell over. Fix the design."** Cover concurrency limits, pooling proxies, queue buffering, reserved concurrency, load shedding and back-pressure.
4. **"When would you not use serverless?"** Cover steady high throughput, long-running or stateful connections, latency-critical paths, special hardware, cost break-even and portability.
5. **"How would you implement a 7-day onboarding workflow with human approvals?"** Cover Step Functions callbacks or durable functions, timeouts, compensation, idempotent steps, audit trails and cost per execution.

## Resources (free first)

- **Documentation:** [Lambda quotas](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html), [Lambda execution environment lifecycle](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtime-environment.html), [Lambda durable functions](https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html), [Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html), [EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html), [Cloud Run](https://docs.cloud.google.com/run/docs), [Eventarc](https://docs.cloud.google.com/eventarc/docs), [Azure Functions hosting options](https://learn.microsoft.com/en-us/azure/azure-functions/functions-scale), [Durable Functions](https://learn.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-overview).
- **Guides:** [Serverless Land](https://serverlessland.com/) (patterns and workshops), [Powertools for AWS Lambda](https://docs.aws.amazon.com/powertools/python/latest/), [CloudEvents](https://cloudevents.io/), [AsyncAPI](https://www.asyncapi.com/docs), [Knative](https://knative.dev/docs/).
- **Papers:** [Firecracker: Lightweight Virtualization for Serverless Applications](https://www.usenix.org/conference/nsdi20/presentation/agache) (NSDI 2020); [Cloud Programming Simplified: A Berkeley View on Serverless Computing](https://arxiv.org/abs/1902.03383) (2019).
- **Practising without a big bill:** Lambda's free tier (1 million requests and 400,000 GB-seconds a month) and Cloud Run's Free Tier (2 million requests a month) cover most labs. Arm a budget action that removes permissions or stops resources at a threshold before any load test, keep load tests to minutes, and watch log ingestion, which is often the first real cost.
- **Paid, worth it:** *Serverless Development on AWS* (Brisals and Hedger, O'Reilly, 2024).

## Sources

All checked 12 Oct 2026.
- [Lambda quotas](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html) and [Lambda pricing](https://aws.amazon.com/lambda/pricing/).
- [Lambda INIT phase billing](https://aws.amazon.com/blogs/compute/aws-lambda-standardizes-billing-for-init-phase/) (effective 1 Aug 2025).
- [Lambda Managed Instances](https://aws.amazon.com/about-aws/whats-new/2025/11/aws-lambda-managed-instances/) (Nov 2025); [Lambda durable functions](https://aws.amazon.com/about-aws/whats-new/2025/12/lambda-durable-multi-step-applications-ai-workflows/) (Dec 2025); [Lambda MicroVMs](https://aws.amazon.com/about-aws/whats-new/2026/06/aws-lambda-microvms) (Jun 2026).
- [Cloud Functions is now Cloud Run functions](https://cloud.google.com/blog/products/serverless/google-cloud-functions-is-now-cloud-run-functions) (21 Aug 2024); [Cloud Run release notes](https://docs.cloud.google.com/run/docs/release-notes) (worker pools GA, Apr 2026).
- [Migrate Consumption plan apps to Flex Consumption](https://learn.microsoft.com/en-us/azure/azure-functions/migration/migrate-plan-consumption-to-flex) (Linux Consumption retirement 30 Sep 2028).
- [CloudEvents graduation](https://www.cncf.io/announcements/2024/01/25/cloud-native-computing-foundation-announces-the-graduation-of-cloudevents/) (25 Jan 2024); [Knative graduation](https://www.cncf.io/announcements/2025/10/08/cloud-native-computing-foundation-announces-knatives-graduation/) (8 Oct 2025).
- [LocalStack 2026.03.0 release](https://blog.localstack.cloud/localstack-for-aws-release-2026-03-0/) (auth token required).

_Last reviewed: 2026-10_
