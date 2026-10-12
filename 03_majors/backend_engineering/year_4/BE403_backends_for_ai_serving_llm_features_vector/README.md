# BE403 · Backends for AI: Serving LLM Features, Vector Search and Cost Control

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 8 | 4 (≈ 120 hours) | L3 → L4 | [BE303](../../year_3/BE303_data_modeling_and_storage_for_backends_postgres/README.md) (also uses [BE301](../../year_3/BE301_api_design_rest_grpc_and_graphql/README.md), [BE304](../../year_3/BE304_asynchronous_systems_queues_streams_and_event/README.md)) | [BE501](../../year_5/BE501_frontier_seminar_durable_execution_serverless/README.md), [OV08A](../../../../04_overlaps/OV08_full_stack_ai_product_engineering/OV08A_shipping_ai_features_end_to_end/README.md), [OV08B](../../../../04_overlaps/OV08_full_stack_ai_product_engineering/OV08B_product_analytics_and_growth_for_ai_apps/README.md) |

Part of the [Backend Engineering major](../../README.md). This course treats a large language model as what it is to a backend: a slow, expensive, rate-limited, non-deterministic dependency that streams. Prompting and model internals belong to the AI Engineering major ([AIE301](../../../ai_engineering/year_3/AIE301_llm_fundamentals_for_engineers/README.md), [AIE303](../../../ai_engineering/year_3/AIE303_retrieval_augmented_generation_and_search/README.md)). Here you learn to serve LLM features reliably, cheaply and safely.

## Why this course matters now

Most product teams now ship at least one LLM feature, and the hard parts of those features are backend problems:
- **Streaming:** keeping streams alive through proxies.
- **Cost:** stopping generation (and the bill) when a user closes the tab, and staying inside provider rate limits measured in tokens per minute.
- **Retrieval:** filtering vector search by tenant without losing recall.
- **Agents:** running jobs that take twenty minutes and call tools with side effects.

Public engineering write-ups show the scale. Uber's GenAI Gateway (2024) gave about 30 teams one OpenAI-compatible API across vendors, with PII redaction and cost attribution, serving 16 million queries a month. Notion (February 2026) re-architected its vector search and cut search-engine spend by about 60%. Detecting changes at page level cut the data it had to re-embed by about 70%. The pricing levers are concrete. Batch APIs from OpenAI and Anthropic cost 50% less, and Anthropic's cached prompt reads cost 0.1× the base input price on most models. AI assistants write the integration code quickly. Engineers who can stream, cache, route, budget, evaluate and recover these systems under failure are the ones teams need.

## Learning outcomes

By the end you can:

1. **Decompose** an LLM feature into backend components (gateway, retrieval, orchestration, model calls, post-processing, evaluation) and **estimate** its latency (time to first token, tokens per second) and cost per request.
2. **Call** model APIs robustly: handle token-based rate limits, `429`s, long generations, structured outputs, tool calls and provider fallback.
3. **Stream** responses end to end with SSE or WebSockets through proxies and load balancers, with cancellation that stops upstream generation.
4. **Build** an LLM gateway with per-tenant quotas, budgets, routing, caching, logging and PII redaction.
5. **Implement** vector search in PostgreSQL with pgvector (HNSW and IVFFlat, filtered search with iterative scans, quantization, hybrid search), and **measure** recall against latency.
6. **Decide** when a dedicated vector store is worth it, and **design** ingestion pipelines with chunking, change detection and embedding-model migrations.
7. **Cut** cost with prompt caching, batch APIs, model routing, output limits and response caching, and **prove** quality held with evaluations.
8. **Run** long jobs and agents on queues and durable execution, with idempotent tool calls, human approval steps and step and budget limits.
9. **Instrument** AI features with traces, sampled online evaluations and CI evaluation gates.
10. **Defend** AI features against prompt injection, data leakage across tenants and unbounded consumption (OWASP Top 10 for LLM Applications 2025).

## Chapters and lessons

### Chapter 1 · What an LLM feature asks of a backend (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Anatomy of a request | Context assembly, retrieval, model call, tool calls, post-processing, guardrails, logging | Trace one request through a provided RAG app and time each stage |
| 1.2 Latency and cost profiles | Time to first token, output tokens per second, input vs output token prices, why long outputs dominate cost | Build a cost and latency calculator from provider pricing pages |
| 1.3 Non-determinism | Sampling, the same input giving different outputs, why tests need evaluations and not equality | Run one prompt 50 times and characterize the variation |
| 1.4 API, open weights or self-hosted | Trade-offs in cost, latency, data control, capacity and operations | Write a decision record for three features with different constraints |

**Check your understanding:** (1) Why is time to first token the latency number users notice? (2) Why can output tokens cost more than a large input? (3) When does self-hosting stop being cheaper than an API?

### Chapter 2 · Calling model APIs robustly (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Provider APIs | Messages/Responses-style APIs, roles, tool calling, structured outputs with strict JSON Schema | Call two providers through one internal interface |
| 2.2 Rate limits | Requests, input tokens and output tokens per minute; tiers; client-side token budgeting; `429` with retry hints | Build a client-side limiter that keeps a service under its token-per-minute quota |
| 2.3 Timeouts and retries | Long generations vs hung connections, idle timeouts, retrying only when no side effect occurred | Distinguish a slow stream from a dead one and handle each |
| 2.4 Fallback and degradation | Secondary providers or smaller models, cached answers, "AI unavailable" states | Fail over to a second provider when the first returns errors for 30 s |

**Check your understanding:** (1) Why is "requests per minute" the wrong unit for planning LLM capacity? (2) When is it unsafe to retry a model call? (3) What should users see when every provider is failing?

### Chapter 3 · Streaming end to end (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Server-sent events | The SSE format (WHATWG HTML standard), event IDs, reconnection, provider event types (deltas, tool-use blocks, stop reasons) | Relay a provider stream to a browser as SSE without buffering |
| 3.2 Proxies and load balancers | Response buffering (nginx `proxy_buffering`), idle timeouts, HTTP/2, keepalives, compression pitfalls | Find and fix three buffering and timeout problems in a provided proxy chain |
| 3.3 Cancellation | Client disconnect → cancel the upstream request → stop paying; partial-response accounting | Prove with usage numbers that a closed tab stops generation within 1 s |
| 3.4 WebSockets and resumable streams | Bidirectional streams, reconnect with resume tokens, MCP Streamable HTTP | Resume a stream after a network drop without losing tokens |
| 3.5 Streaming structured output | Partial JSON, tool-call deltas, validating as you go | Stream a structured answer and validate it incrementally |

**Check your understanding:** (1) Why does a default proxy configuration often make streaming look broken? (2) What does it cost you if cancellation does not reach the provider? (3) When would you choose WebSockets over SSE for an AI feature?

### Chapter 4 · The LLM gateway (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Why a gateway | One API for many providers, central keys, quotas, logging and policy (Uber's GenAI Gateway) | List what Uber's gateway centralizes and map it to your design |
| 4.2 Quotas and budgets | Per-tenant and per-user token budgets, hard and soft limits, budget alerts, priority classes | Enforce a monthly token budget per tenant with alerts at 80% |
| 4.3 Routing | Model routing by task, cost and latency; canaries for new models; fallback chains | Route classification to a small model and reasoning to a large one |
| 4.4 Logging and redaction | Prompt and response logging policy, PII redaction before vendor calls and before storage | Redact PII with placeholders and restore it in responses |
| 4.5 Build or adopt | LiteLLM, Envoy AI Gateway, Cloudflare AI Gateway | Stand up one open-source gateway and compare it with your own |

**Check your understanding:** (1) Why should provider keys never live in application services? (2) What breaks if you log every prompt verbatim? (3) How do you roll out a new model version safely?

### Chapter 5 · Vector search in PostgreSQL (weeks 5–6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Embeddings and distance | What embeddings capture, cosine vs inner product vs L2, normalization, dimensions vs cost | Embed a corpus with two models; compare retrieval on a labelled set |
| 5.2 HNSW and IVFFlat | Graph vs cluster indexes; `m`, `ef_construction`, `ef_search`, `lists`, `probes`; build time and memory | Plot recall@10 vs latency for both index types at four settings |
| 5.3 Filtered search | Why filters break approximate search; pgvector 0.8 iterative index scans; partial indexes and partitioning per tenant | Keep recall above 0.9 for a query filtered to a small tenant |
| 5.4 Shrinking vectors | `halfvec`, binary quantization with re-ranking, `sparsevec`; pgvectorscale's DiskANN index | Cut index memory by 4× or more and recover recall with re-ranking |
| 5.5 Hybrid search | Full-text (BM25-style) plus vectors, reciprocal rank fusion, re-rankers | Show hybrid beating vector-only on keyword-heavy queries |
| 5.6 Operating it | Index builds on live tables, `maintenance_work_mem`, vacuum and HNSW, monitoring recall over time | Rebuild an HNSW index without blocking writes |

**Check your understanding:** (1) Why can a filtered vector query return fewer than `k` results, and how do iterative scans help? (2) What do you lose with binary quantization, and how does re-ranking win it back? (3) Why measure recall against exact search instead of trusting the index settings?

### Chapter 6 · Dedicated vector stores and ingestion pipelines (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 When to leave Postgres | Scale, multitenancy, cost of memory-resident indexes, object-storage-based engines (turbopuffer), Qdrant, Milvus, Weaviate | Run the same workload on pgvector and one dedicated store; compare cost and recall |
| 6.2 Chunking and metadata | Chunk sizes and overlap, structure-aware chunking, metadata for filters and authorization | Compare three chunking strategies on a labelled set |
| 6.3 Change detection | Hash content and metadata separately; re-embed only changed text (Notion's page-level tracking) | Cut embedding calls by over 90% on a 1% change to the corpus |
| 6.4 Embedding-model migrations | Versioned indexes, dual-writing, backfill, cut-over (Notion re-indexed its corpus with a newer model) | Migrate to a new embedding model with zero downtime |

**Check your understanding:** (1) Why must permission metadata be stored alongside each chunk? (2) What does a new embedding model force you to do, and why can't you mix versions in one index? (3) When is a namespace per tenant better than a shared index with filters?

### Chapter 7 · Cost control (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Token accounting | Usage fields, cost attribution per tenant and feature, cost per successful task | Build a cost dashboard by tenant, feature and model |
| 7.2 Prompt caching | Stable prefixes first; Anthropic cache writes (1.25× for 5 minutes, 2× for 1 hour) and reads (0.1× on most models); OpenAI automatic caching; Gemini context caching | Restructure a prompt to raise the cache hit rate and measure the bill |
| 7.3 Batch APIs | 50% discounts for asynchronous work with a 24-hour window (OpenAI: up to 50,000 requests per batch); what belongs in batch | Move nightly summarization to a batch API |
| 7.4 Routing and smaller models | Routing easy requests to cheaper models (RouteLLM reports over 2× cost reduction in some settings); distillation and fine-tuned small models (AIE402) | Route 60% of traffic to a small model with no measurable quality drop |
| 7.5 Response caching | Exact-match caching, semantic caching and its correctness risks, output length limits | Show a semantic cache returning a wrong answer; restrict it to safe cases |

**Check your understanding:** (1) Why does putting user-specific text early in a prompt destroy cache hits? (2) What makes semantic caching dangerous for personalized answers? (3) Why measure "cost per successful task" instead of "cost per call"?

### Chapter 8 · Self-hosted inference for backend engineers (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 How serving engines batch | Continuous batching, the KV cache, PagedAttention in vLLM (2–4× throughput over earlier systems in the SOSP 2023 paper), prefix caching in SGLang | Serve a small open-weights model with vLLM and measure throughput vs batch size |
| 8.2 GPU memory arithmetic | Weights, KV cache per token, concurrency limits, quantization trade-offs | Compute the maximum concurrent 8k-token sessions for a given GPU |
| 8.3 Scaling and cold starts | Model load time, autoscaling on queue depth, warm pools, multi-model serving | Measure cold-start time and design a warm-pool policy |
| 8.4 Self-hosted models behind your gateway | OpenAI-compatible serving endpoints, request queues, admission control and load shedding for GPU-bound services | Put your vLLM server behind the Chapter 4 gateway with queue-depth-based shedding |

**Check your understanding:** (1) Why does the KV cache, not the model weights, limit concurrency? (2) What does continuous batching change for tail latency? (3) Which signals should drive autoscaling for an inference service?

### Chapter 9 · Long jobs and agents (weeks 10–11)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Jobs, not requests | `202 Accepted` with an operation resource, progress over SSE, queues for long tasks (BE304) | Turn a 10-minute report generation into a job API |
| 9.2 Durable execution for agents | Workflows, activities and replay; Temporal with the OpenAI Agents SDK (GA March 2026), AWS Lambda durable functions (runs up to one year), Restate, DBOS | Kill a worker mid-agent-run and resume without repeating completed steps |
| 9.3 Tools with side effects | Idempotency keys on tool calls, dry runs, approval steps, compensations | Make a "refund" tool safe under agent retries |
| 9.4 Limits and sandboxes | Step limits, wall-clock limits, per-run budgets, sandboxed code execution, scoped credentials | Stop a looping agent automatically and report why |
| 9.5 Human in the loop | Waiting for approval for hours or days, timeouts, escalation | Add a manager approval step that survives a deploy |

**Check your understanding:** (1) Why do durable execution engines require deterministic workflow code? (2) What happens to a non-idempotent tool when an agent step is retried? (3) Which agent actions should always wait for a human?

### Chapter 10 · Evaluation hooks and observability (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Tracing AI calls | Spans for retrieval, model and tool calls; OpenTelemetry GenAI semantic conventions (still evolving); Langfuse-style traces | Trace a RAG request with token counts and costs per span |
| 10.2 Offline evaluation in CI | Golden sets, LLM-as-judge with calibration, retrieval metrics, regression gates on prompt or model change (promptfoo, Ragas) | Block a deploy that drops answer quality by more than 3 points |
| 10.3 Online evaluation | Sampling production traffic for evaluation, user feedback capture, A/B tests for models and prompts | Sample 1% of traffic for automatic grading and plot quality over a week |
| 10.4 Closing the loop | Turning production failures into new evaluation cases, versioning evaluation sets, consent and retention rules for logged conversations | Add five production failures to the evaluation set and show the gate catching a regression on them |

**Check your understanding:** (1) Why is "it looked fine in the demo" not evidence? (2) What makes an LLM judge trustworthy enough to gate a deploy? (3) How do you evaluate without storing personal data you should not keep?

### Chapter 11 · Safety, security and abuse (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Prompt injection as untrusted input | Instructions hidden in documents and tool results; separating privileges; never letting model output authorize actions (OWASP LLM01:2025) | Build a defence-in-depth design where injected text cannot trigger a privileged tool, and test it on your own system |
| 11.2 Data boundaries | Authorization-aware retrieval, tenant isolation in vector stores (LLM08:2025), sensitive information disclosure (LLM02:2025) | Prove zero cross-tenant retrieval with 500 adversarial queries |
| 11.3 Unbounded consumption | Per-user rate and token limits, abuse detection, cost-based denial of service (LLM10:2025) | Cap a user's spend and detect a scripted abuse pattern |
| 11.4 Output handling and data law | Treating output as untrusted (LLM05:2025), excessive agency (LLM06:2025), DPDP Act duties for prompts and logs | Escape and validate model output before it reaches HTML, SQL or shell |

**Check your understanding:** (1) Why can't a system prompt alone stop prompt injection? (2) Where must authorization be enforced in a RAG system: before retrieval, after retrieval, or both? (3) What makes model output dangerous to pass into another system?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Cost and latency calculator | Feature cost model |
| 2 | 2 | Lab 1: robust client | Token limiter and provider fallback |
| 3 | 3 | Lab 2: streaming and cancellation | Usage proof of cancellation; P1 due |
| 4 | 4 | Lab 3: gateway | Quotas, routing, redaction |
| 5 | 5 | Lab 4: pgvector indexes (no AI) | Recall–latency plots |
| 6 | 5 | Filtered and hybrid search | Recall under filters; hybrid gain; P2 starts |
| 7 | 6 | Lab 5: ingestion pipeline | Change detection; model migration |
| 8 | 7 | Lab 6: cost cuts | Cache hit rate and bill before/after |
| 9 | 8 | Lab 7: vLLM | Throughput vs batch size; P2 due |
| 10 | 9 | Lab 8: durable agent | Crash-and-resume demonstration |
| 11 | 9 | Tools and approvals | Idempotent tools; approval step; P3 design review |
| 12 | 10 | Lab 9: evaluation gate | CI gate blocking a regression |
| 13 | 11 | Security tests | Injection and tenant-isolation suite |
| 14 | — | P3 integration | P3 demo and cost review |
| 15 | Review and exam | — | Written exam and live incident exam |

## Working with AI in this course

- **Use AI for:** everything a product team would: generating evaluation sets (then reviewing them), drafting prompts, writing gateway adapters for new providers, summarizing traces, and acting as the model under test. The course runs on real model APIs or a provided mock server that streams tokens at configurable speeds, so no paid key is required.
- **Do without AI (drills):** the cost and latency arithmetic; choosing index parameters from recall–latency data; designing where authorization happens in a RAG pipeline; the Lab 4 index study; the live incident exam (a streaming outage, a cost spike or a cross-tenant leak, diagnosed from logs and traces).
- **Verify AI output by:** measuring rather than trusting. Use recall against exact search, cost from usage fields, cancellation from provider usage logs, quality from an evaluation suite with a fixed seed set, and security from an adversarial test suite you wrote.
- **Where AI still fails here (show it yourself):** ask an assistant for "streaming chat through nginx" and check whether buffering is disabled and whether client disconnects cancel the upstream call. Ask for "RAG with permissions" and check whether it filters after retrieval only. Ask for "semantic caching to save cost" and test it with two users asking similar but personal questions. Ask for an agent that issues refunds and kill it mid-run. Record each failure.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs 1–9 | 25% |
| Projects P1 / P2 / P3 | 5% / 12% / 23% |
| Written exam (latency and cost arithmetic, vector search, streaming, durable agents, LLM security) | 20% |
| Live incident exam (no AI) | 15% |

**Mastery gate:** you pass when you can, without AI help, (a) estimate the monthly cost and peak token throughput of a stated AI feature and propose three changes that cut cost by half, with the arithmetic; (b) diagnose a planted streaming failure, a cost spike and a cross-tenant retrieval leak in a provided system within 90 minutes; and (c) show your P3 surviving worker crashes mid-agent-run with zero duplicated tool side effects, and passing its evaluation and security gates.

## Industry reality

- **Uber's GenAI Gateway** (July 2024) mirrors the OpenAI API in front of several vendors and Uber-hosted models. It redacts PII before vendor calls, centralizes cost attribution and audit, and served about 30 teams and 16 million queries a month at the time.
- **Notion** (February 2026) reported 10× scale at one-tenth the cost over two years of vector search. Moving to turbopuffer cut search-engine spend by about 60% and brought p50 latency from 70–100 ms to 50–70 ms. Page-level change detection cut data volume by about 70%, and moving embeddings to Ray is expected to cut that infrastructure's cost by over 90%.
- **pgvector** 0.8 (October 2024) added iterative index scans for filtered queries. The 0.8.x line was still receiving fixes in October 2026 (0.8.7).
- **Pricing levers:** OpenAI's Batch API offers a 50% discount with a 24-hour window. Anthropic's cache reads cost 0.1× the base input price on most models, with writes at 1.25× (5-minute cache) or 2× (1-hour cache).
- **Durable agents:** Temporal's integration with the OpenAI Agents SDK became generally available in March 2026. AWS Lambda durable functions (December 2025) run workflows for up to a year.

Interview questions from this course:

1. **"Design the backend for an assistant that answers questions over a company's documents for 10,000 employees."** A strong answer covers ingestion and change detection, chunking with permission metadata, authorization-aware retrieval, hybrid search, streaming, a gateway with quotas, evaluation, and cost per question.
2. **"How do you stream LLM responses through your API, and what breaks?"** Cover SSE vs WebSockets, proxy buffering, idle timeouts, HTTP/2, cancellation on disconnect, partial-response accounting and resumption.
3. **"Cut this feature's LLM bill by 50% without hurting quality."** Cover measuring cost per successful task, prompt caching via stable prefixes, batch APIs for non-interactive work, routing to smaller models, output limits and safe response caching, all proven with an evaluation suite.
4. **"pgvector or a dedicated vector database?"** Cover corpus size and memory, filtered search and recall, multitenancy, operations and backup, cost (including object-storage-based engines), and the value of one transactional store.
5. **"An agent task runs 20 minutes and can issue refunds. How do you make it reliable and safe?"** Cover durable execution with replay, idempotent tools, approval steps, step and budget limits, scoped credentials, audit logs and the resume path after a crash.

## Resources (free first)

- **Provider documentation:** Anthropic [streaming](https://platform.claude.com/docs/en/build-with-claude/streaming), [prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching), [batch processing](https://platform.claude.com/docs/en/build-with-claude/batch-processing) and [rate limits](https://platform.claude.com/docs/en/api/rate-limits); OpenAI [streaming](https://developers.openai.com/api/docs/guides/streaming-responses), [prompt caching](https://developers.openai.com/api/docs/guides/prompt-caching), [batch](https://developers.openai.com/api/docs/guides/batch) and [rate limits](https://developers.openai.com/api/docs/guides/rate-limits); Google [Gemini context caching](https://ai.google.dev/gemini-api/docs/caching).
- **Standards:** [Server-sent events (WHATWG)](https://html.spec.whatwg.org/multipage/server-sent-events.html); [MCP Streamable HTTP](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http); [OpenTelemetry GenAI semantic conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/).
- **Vector search:** [pgvector](https://github.com/pgvector/pgvector); [pgvectorscale](https://github.com/timescale/pgvectorscale); [Qdrant](https://qdrant.tech/documentation/); [Weaviate](https://weaviate.io/developers/weaviate); [turbopuffer](https://turbopuffer.com/docs); [MTEB leaderboard](https://huggingface.co/spaces/mteb/leaderboard) for choosing embedding models.
- **Serving and gateways:** [vLLM](https://docs.vllm.ai/) and the [PagedAttention paper](https://arxiv.org/abs/2309.06180); [SGLang](https://docs.sglang.ai/) and its [paper](https://arxiv.org/abs/2312.07104); [LiteLLM](https://docs.litellm.ai/); [Envoy AI Gateway](https://aigateway.envoyproxy.io/); [Cloudflare AI Gateway](https://developers.cloudflare.com/ai-gateway/); [RouteLLM](https://arxiv.org/abs/2406.18665).
- **Agents and durability:** [Temporal docs](https://docs.temporal.io/); [Restate docs](https://docs.restate.dev/); [DBOS docs](https://docs.dbos.dev/); [AWS Lambda durable functions](https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html); Anthropic, [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents).
- **Evaluation and security:** [promptfoo](https://www.promptfoo.dev/docs/intro/); [Ragas](https://docs.ragas.io/); [Langfuse](https://langfuse.com/docs); [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/).
- **Case studies:** Uber, [GenAI Gateway](https://www.uber.com/blog/genai-gateway/) (2024); Notion, [Two years of vector search](https://www.notion.com/blog/two-years-of-vector-search-at-notion) (2026).

## Sources

All checked 12 Oct 2026.

- Uber, *Navigating the LLM Landscape: Uber's Innovation with GenAI Gateway* (11 Jul 2024): https://www.uber.com/blog/genai-gateway/
- Notion, *Two years of vector search at Notion: 10x scale, 1/10th cost* (19 Feb 2026): https://www.notion.com/blog/two-years-of-vector-search-at-notion
- pgvector changelog (0.7.0 Apr 2024; 0.8.0 Oct 2024; 0.8.7 Oct 2026): https://github.com/pgvector/pgvector/blob/master/CHANGELOG.md
- Anthropic prompt caching pricing: https://platform.claude.com/docs/en/build-with-claude/prompt-caching ; Anthropic Message Batches (50% cost reduction): https://platform.claude.com/docs/en/build-with-claude/batch-processing ; OpenAI Batch API (50%, 24 h, 50,000 requests, 200 MB): https://developers.openai.com/api/docs/guides/batch
- Kwon et al., PagedAttention (SOSP 2023): https://arxiv.org/abs/2309.06180 ; Ong et al., RouteLLM (2024, rev. 2025): https://arxiv.org/abs/2406.18665
- Temporal and OpenAI Agents SDK integration (30 Jul 2025; GA update 23 Mar 2026): https://temporal.io/blog/announcing-openai-agents-sdk-integration
- AWS Lambda durable functions: https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html
- OWASP Top 10 for LLM Applications 2025: https://genai.owasp.org/llm-top-10/

_Last reviewed: 2026-10_
