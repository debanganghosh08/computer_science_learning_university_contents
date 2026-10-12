# AIE301 · LLM Fundamentals for Engineers

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 5 | 4 (≈ 120 hours) | L1 → L3 | [CS214](../../../../02_year_2_core_computer_science/semester_4/CS214_machine_learning_foundations/README.md), [CS205](../../../../02_year_2_core_computer_science/semester_3/CS205_software_engineering_i_design_testing/README.md) | [AIE401](../../year_4/AIE401_multi_agent_systems_mcp_and_orchestration/README.md); taken alongside [AIE302](../AIE302_prompt_and_context_engineering/README.md) and [AIE303](../AIE303_retrieval_augmented_generation_and_search/README.md); prepares for [AIE304](../AIE304_tool_use_and_ai_agents_loops_harnesses_memory/README.md), [AIE305](../AIE305_evaluating_llm_systems/README.md) |

## Why this course matters now

AI engineering means building products on top of foundation models that someone else trained, usually through an API and sometimes on your own GPUs. Every design decision is a trade-off between quality, latency and money, and the ranges are wide. In October 2026 Anthropic listed its smallest current model from $0.10 per million input tokens and its largest at $10, a 100× spread. Batch requests cost 50% less, and cached prompt prefixes are billed at 2.5–10% of the input price, depending on the model. Open-weight models such as OpenAI's gpt-oss-120b (Apache 2.0, runs on a single 80 GB GPU) make self-hosting realistic for teams with data-residency needs. Coding assistants (Claude Code, Cursor, GitHub Copilot, OpenAI Codex) write API client code quickly, but they often reproduce API shapes from their training data. That data can include interfaces that no longer exist: OpenAI's Assistants API was shut down on 26 August 2026, and Claude models from 4.7 onward reject the old `budget_tokens` thinking parameter. This course gives you the mental model underneath the APIs: tokens, attention, the KV cache, sampling and serving. With it you can estimate cost before you build, explain latency when it spikes, and choose a model with evidence.

## Learning outcomes

By the end you can:

1. **Explain** byte-pair encoding and **measure** how token counts differ by language, script, code and number format, and what that does to cost and context.
2. **Explain** next-token generation (embeddings, attention, logits, prefill vs decode, KV cache) well enough to **predict** how prompt length and output length affect latency and memory.
3. **Control** decoding (temperature, top-p, top-k, min-p, stop sequences, max tokens, logprobs) and **explain** why "temperature 0" is still not reproducible on most serving stacks.
4. **Use** embeddings for similarity, clustering and classification, and **choose** an embedding model with MTEB plus your own retrieval test.
5. **Build** clients from scratch for two providers, covering messages, streaming, tool calling, structured outputs, batch and prompt caching, with retries, timeouts and error handling.
6. **Model** cost and latency (TTFT, inter-token latency, throughput, rate limits) for a feature, then **validate** the model against measurements within ±15%.
7. **Decide** when a reasoning model and a higher effort setting are worth their extra tokens.
8. **Serve** an open-weight model locally (Ollama or llama.cpp) and on a GPU server (vLLM), and **size** memory for weights plus KV cache.
9. **Select** a model for a task with a written rubric (quality on your own eval, cost, latency, licence, data handling) rather than from a leaderboard.

## Chapters and lessons

### Chapter 1 · Text to tokens (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Why subwords | Character vs word vs subword vocabularies; byte-pair encoding (Sennrich et al., 2015); byte-level BPE; SentencePiece (Kudo and Richardson, 2018) | Implement BPE training on 1 MB of text in under 100 lines (follow Karpathy's minbpe) |
| 1.2 Real tokenizers | tiktoken encodings, Hugging Face `tokenizers`, special tokens, chat templates; provider token-counting endpoints | Count one prompt with three tokenizers and one provider counting endpoint; explain differences |
| 1.3 Language and script cost | Up to 15× token-length differences for the same content across languages (Petrov et al., 2023); speakers of some languages "overcharged" (Ahia et al., 2023) | Tokenize the same paragraph in English, Hindi (Devanagari), romanised Hindi, Tamil and Bengali; build a cost table |
| 1.4 Tokens and failure modes | Digit splitting and arithmetic, whitespace in code, rare strings; tokenizer changes between generations (Anthropic: 1M tokens hold ~750k words on older models, ~555k on the tokenizer introduced with Claude Opus 4.7) | Find five inputs whose token count surprises you; explain each |

**Check your understanding:** Why does a model struggle to count letters in a word it can spell correctly? A provider switches tokenizer and your bill rises 30% for the same traffic: what changed and what do you re-measure? Why is a Hindi-first product's context window effectively smaller?

### Chapter 2 · How a transformer produces the next token (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Embeddings to logits | Token embeddings, positional information (RoPE), stacked attention + MLP blocks, the output softmax over the vocabulary (Vaswani et al., 2017) | Step through a 2-layer model in the Transformer Explainer and an LLM visualiser; label each tensor shape |
| 2.2 Attention and the KV cache | Queries, keys, values; causal masking; caching keys/values so decoding is one token at a time; memory grows with sequence length × layers × heads | Compute KV-cache size for a 70B-class model at 8k and 128k context |
| 2.3 Prefill vs decode | Prefill is parallel and compute-bound; decode is sequential and memory-bandwidth-bound; why long prompts raise time-to-first-token and long outputs raise total time | Measure TTFT and tokens/s while varying input 1k→64k and output 100→2,000 |
| 2.4 From pretraining to assistant | Next-token pretraining, scaling laws (Kaplan et al., 2020; Hoffmann et al., 2022), instruction tuning and RLHF (Ouyang et al., 2022), Constitutional AI (Bai et al., 2022) | Compare a base model and its instruct version on 10 prompts; describe the differences |
| 2.5 Why models make things up | Fluency is not truth; knowledge cutoffs; no built-in lookup; calibration | Ask 30 questions with dated answers after the cutoff; classify refusals vs confident errors |

**Check your understanding:** Why does doubling the prompt length hurt TTFT more than doubling the output length does? Why does a long conversation eventually cost more memory on the server than the model weights for that request? What does RLHF change about a model, and what does it not change?

### Chapter 3 · Sampling and decoding (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 From logits to a choice | Greedy, temperature scaling, top-k, nucleus/top-p (Holtzman et al., 2019), min-p (Nguyen et al., 2024) | Implement all five samplers on a small open model's logits; compare outputs |
| 3.2 Logprobs and confidence | Token logprobs, sequence likelihood, using logprobs for classification confidence and abstention | Build a classifier that abstains below a logprob threshold; plot accuracy vs coverage |
| 3.3 Stops and lengths | Stop sequences, `max_tokens`, stop reasons (end_turn, max_tokens, tool_use, refusal), truncated JSON | Trigger every stop reason deliberately and handle each in code |
| 3.4 Non-determinism | Batch-dependent floating-point reductions make "temperature 0" outputs vary on shared servers (Thinking Machines, Sept 2025); seeds; reasoning models that fix sampling parameters | Send one prompt 50 times at temperature 0; count distinct outputs |

**Check your understanding:** When is high temperature the right choice in a product? Why might top-p 0.9 behave very differently on a confident and an uncertain model? How would you write a test for a function whose LLM call is not deterministic?

### Chapter 4 · Embeddings (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Vectors for meaning | Sentence embeddings, cosine vs dot product, normalisation, anisotropy | Embed 1,000 support tickets; find nearest neighbours; inspect five failures |
| 4.2 Choosing a model | MTEB (Muennighoff et al., 2022) and its leaderboard, multilingual models, dimensions and Matryoshka truncation (Kusupati et al., 2022), API vs local (sentence-transformers) | Compare three models on your own 100-query test rather than the leaderboard |
| 4.3 Beyond search | Clustering, deduplication, zero-shot classification, anomaly detection | Cluster 5,000 app reviews; name clusters; measure purity on a labelled sample |
| 4.4 Operating embeddings | Re-embedding on model change, versioning vectors, cost of storage at 3,072 vs 256 dims | Estimate storage and recall when truncating dims 3,072 → 256 |

**Check your understanding:** Why can a model rank first on MTEB and still lose on your data? What breaks if you mix vectors from two embedding model versions in one index? When is a keyword search better than an embedding search?

### Chapter 5 · The model landscape (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Closed frontier families | Anthropic, OpenAI and Google model tiers (large/medium/small), context windows, modalities, pinned snapshots, deprecation schedules | Build a one-page table of current tiers and prices from official pages, dated |
| 5.2 Open-weight families | Llama, Qwen3, DeepSeek-V3/R1, gpt-oss, Gemma, Mistral; mixture-of-experts (total vs active parameters); Indian efforts such as Sarvam's models and AI4Bharat's IndicTrans2 | Run two open models on the same 30 Indic-language prompts; compare |
| 5.3 Licences and model cards | Apache 2.0 vs custom community licences, acceptable-use policies, what a model card must state | Read three model cards; list the restrictions that would affect a commercial product |
| 5.4 Leaderboards and their limits | LMArena, Artificial Analysis, "The Leaderboard Illusion" (Singh et al., 2025): private testing and selective reporting can skew arena rankings | Write a half-page critique of one leaderboard claim |

**Check your understanding:** What does "120B parameters, 5.1B active" mean for memory and for speed? Why might a startup choose a smaller open model even when a closed model scores higher? What would make you distrust a leaderboard result?

### Chapter 6 · The API surface I: messages, streaming and errors (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Request anatomy | Messages and roles, system prompts, Anthropic Messages API, OpenAI Responses API (Chat Completions still supported; Assistants shut down Aug 2026), Gemini API | Call all three with raw HTTP (no SDK) and log the full request/response |
| 6.2 Streaming | Server-Sent Events, event types (deltas, tool-input deltas, stop events), partial JSON, back-pressure | Write a streaming parser from the raw byte stream; render tokens in a terminal UI |
| 6.3 Failure handling | 400/401/403/404/413/429/500/529 classes; retry with exponential backoff and jitter; honouring `retry-after`; timeouts; idempotent retries | Inject failures with a fake server; prove your client never double-charges a side effect |
| 6.4 Rate limits | Requests/min and tokens/min, input vs output token limits, usage tiers, token buckets on the client | Build a client-side token bucket; load-test it at 2× the published limit |

**Check your understanding:** Why stream at all if total time is the same? What should happen to a half-received stream when the connection drops? Why does the retry policy for a chat answer differ from one for a tool call that sends money?

### Chapter 7 · The API surface II: tools, structure, batch and caching (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Tool calling | JSON Schema tool definitions, `tool_use` → `tool_result` round-trip, parallel tool calls, strict tool schemas | Implement a two-tool weather + currency assistant with raw API calls |
| 7.2 Structured outputs | OpenAI Structured Outputs (Aug 2024); Anthropic structured outputs (GA Feb 2026); refusals and truncation as residual failure cases | Extract fields from 100 receipts; report schema-valid rate and field accuracy |
| 7.3 Prompt caching | Cache breakpoints, minimum cacheable lengths, write vs read pricing (Anthropic: 1.25× write for 5 min, 2× for 1 h, reads 0.1× or less); OpenAI's automatic caching; Gemini implicit/explicit caching | Measure cost and TTFT with and without caching on a 20k-token system prompt |
| 7.4 Batch APIs | 50% discount, results within 24 hours (Anthropic, OpenAI, Gemini); when offline is acceptable (evals, backfills, nightly enrichment) | Re-run a 5,000-item classification job via batch; compare cost and wall-clock time |
| 7.5 Multimodal inputs | Images, PDFs, audio; token cost of images; OCR vs native vision | Extract a table from 20 scanned Indian railway or utility documents; compare with OCR |

**Check your understanding:** Where in a prompt should a cache breakpoint go, and what invalidates it? Which two jobs in your organisation should move to a batch API tomorrow, and why? Why can a strict schema still produce an unusable answer?

### Chapter 8 · Cost and latency mathematics (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 The cost model | cost = input × price_in + output × price_out, adjusted for cache reads/writes, batch and reasoning tokens (billed as output) | Spreadsheet model for a feature at 50k daily users; sensitivity analysis on each term |
| 8.2 Latency anatomy | Network, queueing, TTFT, inter-token latency, output length; p50 vs p95 vs p99 | Trace 500 calls; decompose p95 latency into its parts |
| 8.3 Throughput and concurrency | Little's law (concurrency = arrival rate × latency), provider limits, why long outputs consume concurrency | Compute the concurrency needed for 30 req/s at 6 s average latency; test it |
| 8.4 Levers | Smaller model, shorter output, caching, batch, streaming for perceived latency, routing easy queries to cheap models (FrugalGPT, 2023; RouteLLM, 2024) | Cut the cost of your Chapter 7 assistant by 50% with no measured quality loss |

**Check your understanding:** Why does output usually dominate cost even when inputs are 6× longer? Your p50 latency is fine but p99 is 25 s: what are four likely causes? When does a cheaper model end up costing more?

### Chapter 9 · Reasoning models (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Test-time compute | Spending more inference compute can beat a larger model (Snell et al., 2024); s1 budget forcing (2025) | Plot accuracy against reasoning tokens on 50 maths and logic items |
| 9.2 How they are trained | Reinforcement learning on verifiable rewards; DeepSeek-R1 (2025) and distillation into small models; o1 system card (2024) | Summarise the R1 training recipe in one diagram |
| 9.3 Controls | OpenAI `reasoning.effort` (values from `none` to `max`, model-dependent); Anthropic adaptive thinking steered by `effort`; Gemini `thinking_level`; interleaved thinking with tools | Find the cheapest effort level that meets a 90% target on your task |
| 9.4 When not to reason | Classification, extraction and short lookups; latency budgets; overthinking | Compare a small non-reasoning model with a reasoning model on 200 extraction items |

**Check your understanding:** Why are reasoning tokens billed even when you never see them? Your agent became slower and more expensive after an upgrade but not more accurate: what do you check? When is effort `low` on a big model better than effort `high` on a small one?

### Chapter 10 · Open-weight models and local inference (weeks 10–11)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Running locally | Ollama (OpenAI-compatible endpoint at `localhost:11434/v1`), llama.cpp and the GGUF format, quantisation levels (8-bit, 4-bit K-quants) | Run a 7–20B model on a laptop; measure tokens/s at two quantisation levels |
| 10.2 Memory sizing | Weights = parameters × bytes per parameter; KV cache = 2 × layers × KV heads × head dim × tokens × bytes; MoE memory vs compute | Size a deployment of gpt-oss-20b and a 70B dense model for 32 concurrent 8k-token users |
| 10.3 Serving at scale | vLLM and PagedAttention (Kwon et al., 2023), continuous batching, prefix caching; SGLang RadixAttention (Zheng et al., 2023) | Serve a model with vLLM; load-test at 1/8/32 concurrency; plot throughput vs p95 |
| 10.4 Faster decoding | Speculative decoding (Leviathan et al., 2022), FlashAttention (Dao et al., 2022), quantisation trade-offs (deeper in [MLE404](../../../machine_learning_engineering/year_4/MLE404_efficient_inference_quantization_distillation/README.md)) | Enable speculative decoding; measure speed-up and check that outputs match |
| 10.5 Self-host or API? | Data residency and India's DPDP Act, privacy, fixed vs variable cost, utilisation, operations burden | Write a one-page decision memo with a break-even calculation |

**Check your understanding:** Why does continuous batching raise throughput but can raise individual latency? At what utilisation does a rented GPU beat an API for your workload? Why can a 4-bit model pass your smoke test and fail your eval?

### Chapter 11 · Choosing and shipping a model (weeks 12–13)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Selection rubric | Task-specific eval first, then cost, latency, context, licence, data retention, region, support lifecycle | Score four models on a 150-case task eval; choose with a written rationale |
| 11.2 Provider abstraction | Thin adapters vs gateways (LiteLLM), fallbacks, feature drift across providers | Add a fallback provider; fail the primary in a test; verify identical outputs schema |
| 11.3 Data handling | Retention and training policies, zero-data-retention options, regional endpoints, PII redaction before sending | Map a feature's data flow; mark what leaves your network and where it is stored |
| 11.4 Lifecycle | Deprecations and retirement dates, pinned IDs, upgrade evals, contract and cost reviews | Write an upgrade runbook for a model retirement notice |

**Check your understanding:** Why should the eval come before the shortlist? What does a fallback provider not protect you from? What is your plan the day a model you depend on gets a retirement date?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · BPE from scratch and the language cost table | — |
| 2 | 2 | Lab 2 · Prefill/decode latency curves | — |
| 3 | 3 | Lab 3 · Samplers and logprob abstention | **P1 due** |
| 4 | 4 | Lab 4 · Embedding model shoot-out | — |
| 5 | 5 | Lab 5 · Model landscape table and licence audit | Dated model table |
| 6 | 6 | Lab 6 · Raw HTTP streaming client with retries | Mid-term (AI off): cost and latency estimation |
| 7 | 7 | Lab 7 · Tools, structured outputs, caching, batch | — |
| 8 | 8 | Lab 8 · Cost model validated against traces | — |
| 9 | 9 | Lab 8 (cont.): Reasoning effort curves | **P2 due** |
| 10 | 10 | Lab 9 · Local inference and memory sizing | — |
| 11 | 10 | Lab 9 (cont.): vLLM load test | Self-host memo |
| 12 | 11 | Lab 10 · Model selection with a rubric | — |
| 13 | 11 | Lab 10 (cont.): fallback and upgrade runbook | — |
| 14 | Integration | P3 demo day | **P3 due** |
| 15 | Review | Oral defence of P3 | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** scaffolding API clients and load-test scripts (Claude Code, Cursor, GitHub Copilot, OpenAI Codex); explaining an unfamiliar error; drafting the cost spreadsheet structure; generating synthetic test prompts in several languages.
- **Do without AI (drills):** derive KV-cache and weight memory by hand; compute a feature's monthly cost on paper from prices and traffic; implement BPE and the samplers yourself; write one raw-HTTP streaming client without an SDK or assistant. The mid-term and final are AI-off.
- **Verify AI output by:** checking every generated API call against the provider's current reference page (date it); running against the live API with logging of the full request; comparing token counts from the provider's counting endpoint with your estimate; validating any cost claim with a real 100-call trace.
- **Where AI still fails here (show it):** assistants trained on older docs suggest retired interfaces (Assistants API threads, `budget_tokens`, prefilled assistant turns on models that reject them); keep a log of each one you catch, with the date and the current replacement. Models also state prices and context limits from memory; compare three such claims with the official pricing page.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10, each with measured numbers) | 25% |
| Projects P1–P3 | 35% |
| Written memos (model table, self-host decision, upgrade runbook) | 10% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) + oral defence of P3 | 20% |

**Mastery gate.** You pass when you can: (1) build, from an empty file and with no SDK, a streaming client for one provider that handles tool calls, structured output, 429/529 retries and stop reasons, in under 3 hours; (2) predict the monthly cost and p95 latency of a described feature, then come within ±15% of measured values on a 500-call trace; (3) serve an open-weight model with vLLM or llama.cpp and explain its throughput–latency curve and memory use from first principles.

## Industry reality

AI engineering as a job title grew out of exactly this layer: building on models through APIs rather than training them (swyx, "The Rise of the AI Engineer", Latent Space, June 2023; Chip Huyen, *AI Engineering*, 2025). Teams choose among model tiers by cost and latency: Anthropic's own guidance in 2026 positions its smallest model for "classification, extraction, and routing" and its largest for "demanding reasoning and long-horizon agentic work" (models overview, checked 2026-10). Batch and caching discounts are now standard across Anthropic, OpenAI and Google, and open-weight releases such as gpt-oss (Aug 2025, Apache 2.0) and Qwen3 (2025) made on-premises deployment practical for regulated sectors. In India, the DPDP Rules were notified in November 2025 with most obligations phased in over 18 months, so where prompts and logs are stored is now part of the engineering design.

**Interview questions from this course**

1. *Estimate the monthly LLM bill for 50,000 daily users who each send 6 requests of 3,000 input and 500 output tokens.* Strong answer: does the arithmetic aloud (9M requests/month, 27B input and 4.5B output tokens), applies a stated price, then shows how caching a stable 2,500-token prefix, batching offline work and routing easy queries change it; notes that output often dominates.
2. *Why isn't temperature 0 deterministic in production?* Strong answer: batch-dependent floating-point reduction order on shared GPUs, MoE routing, provider-side changes; mentions seeds and snapshot IDs; designs tests on properties and distributions, not exact strings.
3. *Explain the KV cache and what it means for long conversations.* Strong answer: per-token keys/values per layer; memory grows linearly with context; prefill vs decode costs; prefix caching; why long chats increase TTFT and server memory.
4. *A fintech in Mumbai asks whether to self-host or use an API. How do you decide?* Strong answer: data classification and DPDP obligations, regional endpoints and retention options, quality gap on their eval, utilisation-based break-even, operations skills, an exit plan; no answer without numbers.
5. *Your launch hits 429 errors within an hour. What do you do now and next week?* Strong answer: backoff with jitter and `retry-after`, queueing, client-side token buckets, shedding non-critical traffic, moving offline work to batch; next week: tier increase, caching, smaller models for easy routes, multi-provider fallback, load tests before launch.

## Resources (free first)

- **Understanding the model:** Andrej Karpathy, "Let's build the GPT Tokenizer" — https://www.youtube.com/watch?v=zduSFxRajkE and "Deep Dive into LLMs like ChatGPT" — https://www.youtube.com/watch?v=7xTGNNLPyMI ; minbpe — https://github.com/karpathy/minbpe ; nanoGPT — https://github.com/karpathy/nanoGPT ; nanochat — https://github.com/karpathy/nanochat ; The Illustrated Transformer — https://jalammar.github.io/illustrated-transformer/ ; Transformer Explainer — https://poloclub.github.io/transformer-explainer/ ; LLM visualisation — https://bbycroft.net/llm
- **Courses:** Stanford CS336 Language Modeling from Scratch — https://cs336.stanford.edu/ ; Stanford CS224N — https://web.stanford.edu/class/cs224n/ ; Hugging Face LLM Course — https://huggingface.co/learn/llm-course
- **Provider docs:** Anthropic models overview — https://platform.claude.com/docs/en/about-claude/models/overview ; pricing — https://platform.claude.com/docs/en/about-claude/pricing ; prompt caching — https://platform.claude.com/docs/en/build-with-claude/prompt-caching ; batch — https://platform.claude.com/docs/en/build-with-claude/batch-processing ; token counting — https://platform.claude.com/docs/en/build-with-claude/token-counting ; OpenAI Responses migration — https://developers.openai.com/api/docs/guides/migrate-to-responses ; reasoning — https://developers.openai.com/api/docs/guides/reasoning ; batch — https://developers.openai.com/api/docs/guides/batch ; Gemini caching — https://ai.google.dev/gemini-api/docs/caching ; Gemini thinking — https://ai.google.dev/gemini-api/docs/thinking
- **Local and open models:** Ollama OpenAI compatibility — https://docs.ollama.com/api/openai-compatibility ; llama.cpp — https://github.com/ggml-org/llama.cpp ; GGUF spec — https://github.com/ggml-org/ggml/blob/master/docs/gguf.md ; vLLM — https://docs.vllm.ai/en/latest/ ; SGLang — https://github.com/sgl-project/sglang ; gpt-oss — https://github.com/openai/gpt-oss ; Qwen3 — https://github.com/QwenLM/Qwen3 ; Gemma — https://deepmind.google/models/gemma/ ; Sarvam on Hugging Face — https://huggingface.co/sarvamai ; IndicTrans2 — https://github.com/ai4bharat/IndicTrans2
- **Comparison and tooling:** Tiktokenizer — https://tiktokenizer.vercel.app/ ; tiktoken — https://github.com/openai/tiktoken ; MTEB leaderboard — https://huggingface.co/spaces/mteb/leaderboard ; Artificial Analysis — https://artificialanalysis.ai/ ; LiteLLM — https://github.com/BerriAI/litellm
- **Paid, optional:** Chip Huyen, *AI Engineering* (O'Reilly, 2025); free companion material at https://github.com/chiphuyen/aie-book

## Sources

- Anthropic models overview (lineup, prices, 1M context, words-per-token note, pinned IDs, `budget_tokens` not accepted after 4.6) — https://platform.claude.com/docs/en/about-claude/models/overview (checked 2026-10)
- Anthropic prompt caching (1.25× / 2× writes, 0.1× reads; model-specific minimums) — https://platform.claude.com/docs/en/build-with-claude/prompt-caching ; batch processing (50%, 24 h) — https://platform.claude.com/docs/en/build-with-claude/batch-processing ; structured outputs (beta Nov 2025, GA Feb 2026) — https://platform.claude.com/docs/en/build-with-claude/structured-outputs (checked 2026-10)
- OpenAI Assistants API migration ("officially sunset on August 26, 2026") — https://developers.openai.com/api/docs/assistants/migration ; batch (50%, 24 h) — https://developers.openai.com/api/docs/guides/batch ; prompt caching — https://developers.openai.com/api/docs/guides/prompt-caching ; reasoning effort values — https://developers.openai.com/api/docs/guides/reasoning (checked 2026-10)
- OpenAI, gpt-oss model card (Aug 2025) — https://arxiv.org/abs/2508.10925 and https://github.com/openai/gpt-oss (checked 2026-10)
- Gemini batch (50%) — https://ai.google.dev/gemini-api/docs/batch-api ; thinking levels — https://ai.google.dev/gemini-api/docs/thinking (checked 2026-10)
- Sennrich et al. (2015) — https://arxiv.org/abs/1508.07909 ; Kudo and Richardson (2018) — https://arxiv.org/abs/1808.06226 ; Petrov et al. (2023) — https://arxiv.org/abs/2305.15425 ; Ahia et al. (2023) — https://arxiv.org/abs/2305.13707 (checked 2026-10)
- Vaswani et al. (2017) — https://arxiv.org/abs/1706.03762 ; Kaplan et al. (2020) — https://arxiv.org/abs/2001.08361 ; Hoffmann et al. (2022) — https://arxiv.org/abs/2203.15556 ; Ouyang et al. (2022) — https://arxiv.org/abs/2203.02155 ; Bai et al. (2022) — https://arxiv.org/abs/2212.08073 (checked 2026-10)
- Holtzman et al. (2019) — https://arxiv.org/abs/1904.09751 ; Nguyen et al., min-p (2024) — https://arxiv.org/abs/2407.01082 ; Thinking Machines, "Defeating Nondeterminism in LLM Inference" (Sept 2025) — https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/ (checked 2026-10)
- Muennighoff et al., MTEB (2022) — https://arxiv.org/abs/2210.07316 ; Kusupati et al., Matryoshka (2022) — https://arxiv.org/abs/2205.13147 ; Singh et al., "The Leaderboard Illusion" (2025) — https://arxiv.org/abs/2504.20879 (checked 2026-10)
- Chen et al., FrugalGPT (2023) — https://arxiv.org/abs/2305.05176 ; Ong et al., RouteLLM (2024) — https://arxiv.org/abs/2406.18665 ; Snell et al. (2024) — https://arxiv.org/abs/2408.03314 ; Muennighoff et al., s1 (2025) — https://arxiv.org/abs/2501.19393 ; DeepSeek-R1 (2025) — https://arxiv.org/abs/2501.12948 ; OpenAI o1 System Card (2024) — https://arxiv.org/abs/2412.16720 (checked 2026-10)
- Kwon et al., PagedAttention (2023) — https://arxiv.org/abs/2309.06180 ; Zheng et al., SGLang (2023) — https://arxiv.org/abs/2312.07104 ; Leviathan et al. (2022) — https://arxiv.org/abs/2211.17192 ; Dao et al. (2022) — https://arxiv.org/abs/2205.14135 (checked 2026-10)
- swyx, "The Rise of the AI Engineer" (June 2023) — https://www.latent.space/p/ai-engineer (checked 2026-10)
- India DPDP Rules 2025 (notified Nov 2025; phased obligations) — https://www.pib.gov.in/PressReleasePage.aspx?PRID=2190014 (checked 2026-10)

_Last reviewed: 2026-10_
