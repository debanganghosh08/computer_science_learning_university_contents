# BE403 · Labs and projects

Labs work with real model APIs if you have keys, and otherwise with a provided mock LLM server. The mock streams tokens at a configurable speed, reports usage, emits `429`s and errors on a schedule, and honours cancellation, so every acceptance criterion can be met without spending money. Open-weights models can be served locally with vLLM where hardware allows. Lab 4 and the live incident exam are done without AI assistants.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Robust client | One internal interface over two providers (or the mock in two modes): token-per-minute limiter, retry rules that respect side effects, fallback after 30 s of errors | Tests for `429` handling, fallback, and never retrying after a tool side effect | 5 h |
| 2 · Streaming and cancellation | Relay a model stream as SSE through nginx and a load balancer; fix buffering and idle-timeout problems; cancel upstream on disconnect | Captured timings showing tokens arrive unbuffered; usage logs proving generation stops within 1 s of disconnect | 5 h |
| 3 · Gateway | Per-tenant budgets and quotas, model routing rules, PII redaction with placeholder restoration, request logs with cost | Gateway with tests; a budget-exhaustion demo; a redaction test set with 50 cases | 6 h |
| 4 · pgvector index study (no AI) | HNSW and IVFFlat on 1M vectors at four settings each; filtered queries with and without iterative scans; `halfvec` and binary quantization with re-ranking | Recall@10 vs latency plots against exact search, memory per configuration, and a recommendation | 7 h |
| 5 · Ingestion pipeline | Structure-aware chunking with permission metadata; content and metadata hashing; re-embed only changes; migrate to a new embedding model with dual indexes | Embedding-call counts for a 1% corpus change; zero-downtime migration log | 6 h |
| 6 · Cost cuts | Restructure prompts for cache hits; move a nightly job to a batch API; route easy traffic to a small model | Bill (or computed cost) before and after, with evaluation scores showing no quality loss | 5 h |
| 7 · Self-hosted serving | Serve a small open-weights model with vLLM (or use a provided remote GPU endpoint); sweep concurrency | Throughput and time-to-first-token vs concurrency; KV-cache memory arithmetic checked against measurements | 4 h |
| 8 · Durable agent | A multi-step agent on Temporal, Restate or DBOS with an idempotent side-effecting tool; kill workers at random | Crash-test report: 100 kills, zero repeated side effects, every run completed or parked with a reason | 6 h |
| 9 · Evaluation gate | 100-case evaluation set (retrieval and answer quality), an LLM judge calibrated against 30 human labels, a CI gate | A pipeline run that blocks a planted prompt regression and passes the fix | 5 h |

## Projects

### P1 · Streaming chat endpoint with accounting (L1, ~6 hours)

**Real-world inspiration:** every chat feature streams tokens to users, usually through SSE ([WHATWG](https://html.spec.whatwg.org/multipage/server-sent-events.html)), and pays per token. Provider rate limits are set in tokens per minute ([Anthropic](https://platform.claude.com/docs/en/api/rate-limits), [OpenAI](https://developers.openai.com/api/docs/guides/rate-limits)).

**What to build:** a `POST /conversations/{id}/messages` endpoint. It streams a model response as SSE through nginx, stores the conversation in Postgres, records token usage and cost per message, enforces a per-user token rate limit, and cancels upstream generation when the client disconnects.

**Acceptance criteria:**
- **Low overhead:** your backend adds under 50 ms at p95 to time to first token compared with calling the model directly (measured over 500 requests).
- **Concurrency:** 500 concurrent streams on a laptop against the mock server, with no stream stalls longer than 2 s (event-gap histogram).
- **Cancellation:** closing the client stops upstream generation within 1 s in 99% of 200 trials. Recorded usage matches the tokens actually generated.
- **Limits:** a user over the token limit gets `429` with `Retry-After` before any model call is made.
- **Persistence:** a stream interrupted by a server restart is marked as incomplete, never stored as a complete answer.

**Stretch goals:** resumable streams with event IDs; structured-output streaming with incremental validation; a WebSocket variant and a comparison.

**What it proves to an employer:** you can ship the basic AI feature correctly, including the parts that silently cost money when done wrong.

### P2 · Hybrid search service on PostgreSQL (L2, ~15 hours)

**Real-world inspiration:** Notion's vector search write-up shows the cost of re-embedding and the value of change detection ([Notion, Feb 2026](https://www.notion.com/blog/two-years-of-vector-search-at-notion)). pgvector's iterative index scans address filtered queries ([pgvector](https://github.com/pgvector/pgvector)).

**What to build:** a multi-tenant search service over a public corpus of at least 1 million chunks (for example Wikipedia or arXiv abstracts), split into synthetic tenants of very different sizes. It needs:
- an ingestion pipeline with change detection and permission metadata;
- pgvector HNSW plus PostgreSQL full-text search combined by reciprocal rank fusion, with an optional re-ranker;
- tenant filters and a query API;
- a labelled evaluation set of at least 200 queries.

**Acceptance criteria:**
- **Recall and latency:** recall@10 of at least 0.95 against exact search at p95 under 50 ms for unfiltered queries at 200 queries/s.
- **Filtered recall:** for the smallest tenant (under 0.5% of the corpus), recall@10 stays at or above 0.9 with iterative scans or your partitioning design. You show the recall without them for comparison.
- **Hybrid gain:** hybrid search beats vector-only on nDCG@10 on the labelled set, and you report the margin with a confidence interval.
- **Incremental updates:** after a 1% change to the corpus, the pipeline makes at least 90% fewer embedding calls than a full rebuild, and search reflects changes within 60 s.
- **Model migration:** switching to a new embedding model uses a versioned index and a backfill with zero failed queries and no mixed-version results.
- **Isolation:** 500 adversarial queries return zero results from another tenant.

**Stretch goals:** binary quantization with re-ranking to cut memory by at least 4×; the same workload on a dedicated vector store with a cost comparison; query-time personalization without breaking caching.

**What it proves to an employer:** you can build retrieval that is accurate, fast, multi-tenant and cheap to keep fresh, which sits under most AI features.

### P3 · AI support assistant backend for a marketplace (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** Uber's GenAI Gateway centralizes keys, routing, PII redaction and cost attribution ([Uber, 2024](https://www.uber.com/blog/genai-gateway/)). Temporal's integration with the OpenAI Agents SDK makes agent runs durable ([Temporal, 2025–26](https://temporal.io/blog/announcing-openai-agents-sdk-integration)). The OWASP Top 10 for LLM Applications 2025 lists the risks ([OWASP](https://genai.owasp.org/llm-top-10/)). The marketplace is an **illustrative scenario**.

**What to build:** the backend for a customer-support assistant on a food or commerce marketplace:
- **Gateway:** routing, fallback, prompt caching, budgets per tenant and redaction.
- **Retrieval:** authorization-aware retrieval over help articles and the customer's own orders.
- **Streaming:** a streaming conversation API.
- **Agent:** MCP tools (look up order, explain delay, issue goodwill credit up to a limit, request a refund that needs human approval), with the agent running on a durable execution engine.
- **Quality and cost:** an evaluation suite in CI, online sampling, and a cost dashboard.

**Acceptance criteria:**
- **Cost:** cost per resolved conversation falls by at least 40% from a documented baseline through caching, routing and output limits. The evaluation score drops by no more than 2 points on a 150-case suite.
- **Resilience:** during a simulated 10-minute outage of the primary provider, under 1% of conversations fail, and users see a clear degraded state rather than errors.
- **Durability:** over 200 random worker kills during agent runs, there are zero duplicated credits or refund requests, and every run completes, waits for approval or parks with a reason.
- **Security:** 500 adversarial inputs (other customers' order IDs, instructions hidden in help articles and order notes) cause zero cross-customer data disclosures and zero tool calls beyond the caller's permissions.
- **Approvals:** refunds always wait for approval. An approval given after a deploy or a restart still completes the run correctly.
- **Latency:** time to first token at p95 is under 1.5 s with a real provider, or your added overhead is under 100 ms with the mock.
- **Write-up:** an architecture document, a cost model with the arithmetic, the evaluation methodology and a threat model mapped to the OWASP LLM Top 10.

**Stretch goals:** self-hosted small model for classification with vLLM, routed by the gateway; per-tenant fine-grained budgets with alerts; an A/B test of two prompts with a pre-registered success metric.

**What it proves to an employer:** you can take an AI feature from demo to production: reliable, measured, affordable and safe. This is one of the most in-demand backend profiles in 2026.

## Feeds into

- [BE501 Frontier Seminar](../../year_5/BE501_frontier_seminar_durable_execution_serverless/README.md): durable execution and agent infrastructure in depth.
- [OV08A Shipping AI Features End to End](../../../../04_overlaps/OV08_full_stack_ai_product_engineering/OV08A_shipping_ai_features_end_to_end/README.md) and [OV08B Product Analytics and Growth for AI Apps](../../../../04_overlaps/OV08_full_stack_ai_product_engineering/OV08B_product_analytics_and_growth_for_ai_apps/README.md).
- [AIE403 LLMOps: Observability, Guardrails, Cost and Latency](../../../ai_engineering/year_4/AIE403_llmops_observability_guardrails_cost_and_latency/README.md) and [OV12 Agent Infrastructure](../../../../04_overlaps/OV12_agent_infrastructure_platform/README.md).
