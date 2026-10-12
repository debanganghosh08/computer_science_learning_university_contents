# AIE301 · Labs and projects

Every lab and project ships three things: code in a repository with a README, a log of real API or inference calls (JSONL with request IDs, token counts and timings), and a short write-up with measured numbers and the date the prices and limits were checked. Prices change, so every cost figure must cite the pricing page and the date you read it.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · BPE from scratch and the language cost table | Train a byte-level BPE tokenizer (minbpe-style) on 1 MB of mixed English/Hindi text; compare it with two production tokenizers and one provider counting endpoint | Tokenizer code, a table of tokens per 1,000 words for 8 languages/scripts, one paragraph on the cost implications | 4 h |
| 2 · Prefill and decode curves | Measure TTFT and tokens/s while varying input (1k → 64k tokens) and output (100 → 2,000 tokens) on one API model and one local model | Two plots, a fitted linear model for TTFT vs input length, and an explanation tied to the KV cache | 3 h |
| 3 · Samplers and logprob abstention | Implement greedy, temperature, top-k, top-p and min-p on an open model's logits; build a classifier that abstains below a logprob threshold | Sampler code with tests; accuracy-vs-coverage curve; 50-run determinism experiment at temperature 0 | 4 h |
| 4 · Embedding model shoot-out | Compare three embedding models (one local via sentence-transformers) on your own 100-query retrieval test; test Matryoshka truncation | Recall@10 table by model and dimension; storage cost estimate; one-page recommendation | 4 h |
| 5 · Model landscape and licence audit | Build a dated table of current closed and open model tiers (price, context, modalities, licence, retirement date) from official pages only | The table with a source link per cell; a list of three licence clauses that would affect a commercial product | 3 h |
| 6 · Raw HTTP streaming client | Write a client for one provider with no SDK: SSE parsing, stop reasons, retries with jitter and `retry-after`, timeouts, client-side token bucket | Code, a fake-server test suite that injects 429/500/529 and dropped streams, and a load-test report at 2× the rate limit | 6 h |
| 7 · Tools, structured outputs, caching and batch | Two-tool assistant via raw API; receipt extraction with structured outputs; a 20k-token cached prefix; a 5,000-item batch job | Schema-valid rate and field accuracy on 100 receipts; cost and TTFT with vs without caching; batch vs synchronous cost and wall-clock | 6 h |
| 8 · Cost model validated against traces | Build a spreadsheet cost and latency model for a described feature, then validate it on a 500-call trace; extend with reasoning effort curves (Chapter 9) | Model, trace, error analysis (target ±15%), and an accuracy-vs-reasoning-tokens plot with the cheapest acceptable effort level | 5 h |
| 9 · Local inference and memory sizing | Run a 7–20B model with Ollama or llama.cpp at two quantisation levels, then serve with vLLM and load-test at 1/8/32 concurrency | Hand-computed memory budget vs measured; throughput–p95 plot; a one-page self-host decision memo with break-even | 7 h |
| 10 · Model selection with a rubric | Score four models on a 150-case task eval; add a fallback provider and an upgrade runbook | Rubric, results with confidence intervals, a written choice, and a runbook for a retirement notice | 5 h |

## Projects

### P1 · Token cost explorer for Indian languages (L1, ~6 hours)

**Real-world inspiration.** The same content can need up to 15× more tokens in some languages than in others (Petrov et al., 2023), and speakers of some languages pay more for poorer results (Ahia et al., 2023). Products built for India, from government services using Bhashini to consumer apps answering in Hindi, Tamil or Hinglish, inherit this cost directly.

**What to build.** A command-line tool and a short report. Given a text file, the tool counts tokens with at least three tokenizers (for example tiktoken `o200k_base`, a Llama-family tokenizer and a Gemma or Qwen tokenizer) and with one provider's token-counting endpoint, then prints tokens per 1,000 words, the share of the context window used, and the cost per million words at the provider's current input and output prices.

**Acceptance criteria**
- Covers at least 8 languages or scripts, including English, Hindi in Devanagari, romanised Hindi (Hinglish), and at least three other Indic languages, using parallel text (e.g. from IndicTrans2 outputs checked by a speaker, or public parallel corpora).
- Counts from the provider endpoint are reported alongside local estimates, and the difference is explained.
- The report shows a cost table and a chart, with prices cited and dated.
- Unit tests cover empty input, emoji, mixed scripts and numbers.

**Stretch goals.** Measure how much transliteration or translation-to-English before the call saves, and what it costs in quality on 30 questions.

**What it proves to an employer.** You understand that tokens are the unit of cost and capacity, and you can quantify a product decision that most teams only discover on the invoice.

### P2 · A provider-agnostic LLM client from raw HTTP (L2, ~15 hours)

**Real-world inspiration.** Gateways and SDKs such as LiteLLM wrap many providers behind one interface, and every serious team ends up owning retries, rate limiting, streaming and cost accounting. Interfaces also change: OpenAI's Assistants API was shut down on 26 August 2026, and newer Claude models reject parameters that older ones accepted.

**What to build.** A small library (Python or TypeScript) with one interface over two providers (for example Anthropic and OpenAI, or one API plus a local Ollama endpoint). It supports chat messages, streaming, tool calling with a round-trip helper, structured outputs, prompt caching hints, batch submission and polling, retries with exponential backoff and jitter, a client-side token bucket, and per-call cost accounting from a dated price table.

**Acceptance criteria**
- One interface, two providers; a conformance test suite passes on both, including tool calls and structured outputs.
- A fake server test suite injects 429, 500, 529, timeouts and dropped streams; the client never retries a call marked non-idempotent, and never loses a completed stream chunk.
- Per-call cost computed by the library matches the provider's reported usage-based cost within 1% over 200 calls.
- Streaming adds less than 5 ms of client overhead per chunk (measured).
- The README documents every provider difference you had to paper over, with links to the docs.

**Stretch goals.** OpenTelemetry GenAI spans for every call; a fallback policy that switches provider on repeated 5xx errors with an eval-based guard.

**What it proves to an employer.** You can work below the SDK, handle failure properly and keep costs visible. These are the basics of any production LLM integration.

### P3 · Cost-aware model router with a local fallback (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** Routing and cascades send easy queries to cheap models and hard ones to strong models (FrugalGPT, 2023; RouteLLM, 2024). Provider guidance in 2026 explicitly positions small models for classification and routing and large ones for hard reasoning. Regulated Indian firms also weigh self-hosting for data residency under the DPDP Rules. The scenario below is illustrative.

**What to build.** A service that classifies and drafts replies for customer-support messages (use the public Bitext customer-support dataset, plus 200 messages you translate into Hindi and Hinglish and check by hand). A router predicts difficulty and chooses between (a) a small open model served locally with vLLM or llama.cpp, (b) a mid-tier API model, and (c) a reasoning model at a chosen effort level. Include a validated cost and latency model, a dashboard and a fallback to the local model when the API fails.

**Acceptance criteria**
- A 300-case labelled test set (with at least 30% Hindi/Hinglish) and a documented labelling guide.
- Compared with always using the strongest model, the router cuts cost by at least 40% with no more than 1 point of accuracy loss, shown with a paired bootstrap confidence interval.
- p95 end-to-end latency under 4 s for classification at 5 requests/s on stated hardware.
- With the API disabled, the service keeps answering via the local model, and the measured quality drop is reported.
- The cost model predicts the monthly bill for a stated traffic profile within ±15% of the replayed-traffic measurement.
- A one-page decision memo covers data residency, retention settings and the self-host break-even point.

**Stretch goals.** Learn the router from preference data (RouteLLM-style); add prompt caching and measure hit rate; add speculative decoding to the local model.

**What it proves to an employer.** You can make model choice an engineering decision with numbers, covering quality, cost, latency, resilience and compliance together. This is the core of an AI engineer's job.

## Feeds into

- [AIE302 Prompt and Context Engineering](../AIE302_prompt_and_context_engineering/README.md) and [AIE303 RAG and Search](../AIE303_retrieval_augmented_generation_and_search/README.md): your client library and token tooling are reused in every lab.
- [AIE304 Tool Use and AI Agents](../AIE304_tool_use_and_ai_agents_loops_harnesses_memory/README.md): the raw tool-calling loop from Lab 7 becomes the agent loop.
- [AIE403 LLMOps](../../year_4/AIE403_llmops_observability_guardrails_cost_and_latency/README.md): P3's router and cost model become the starting point for the gateway and cost-engineering projects.
- [AIE402 Fine-Tuning and Small Models](../../year_4/AIE402_fine_tuning_and_small_models_for_products/README.md): the local serving stack from Lab 9 serves your fine-tuned models.

## Sources

- Petrov et al. (2023) — https://arxiv.org/abs/2305.15425 ; Ahia et al. (2023) — https://arxiv.org/abs/2305.13707 ; Chen et al., FrugalGPT (2023) — https://arxiv.org/abs/2305.05176 ; Ong et al., RouteLLM (2024) — https://arxiv.org/abs/2406.18665 (checked 2026-10)
- OpenAI Assistants API migration (sunset 26 Aug 2026) — https://developers.openai.com/api/docs/assistants/migration ; Anthropic models overview — https://platform.claude.com/docs/en/about-claude/models/overview (checked 2026-10)
- Bitext customer-support dataset — https://huggingface.co/datasets/bitext/Bitext-customer-support-llm-chatbot-training-dataset ; LiteLLM — https://github.com/BerriAI/litellm ; IndicTrans2 — https://github.com/ai4bharat/IndicTrans2 (checked 2026-10)
