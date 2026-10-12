# AIE303 · Labs and projects

Every lab and project ships an ingestion script that rebuilds the index from raw documents, a labelled evaluation set (queries with relevant chunk IDs), metric scripts, and a write-up separating retrieval results from generation results. No number without its eval set.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · BM25 and qrels | Build an inverted index and BM25 over 50,000 Wikipedia abstracts; label 50 queries yourself | Code, qrels file, recall@10, MRR and nDCG@10 vs `bm25s` and Pyserini | 4 h |
| 2 · ANN index trade-offs | Flat, HNSW and IVF-PQ indexes over 1M vectors (FAISS); tune `ef_search` for recall ≥ 0.95 | Recall–latency–memory plots; chosen parameters with justification | 4 h |
| 3 · Parsing and chunking bake-off | Parse 30 public PDFs (RBI circulars, railway notices); compare four chunking strategies and contextual chunk headers | Extraction error log, recall@5 per strategy, indexing cost of headers | 6 h |
| 4 · Hybrid search, RRF and reranking | Combine BM25 and dense retrieval with RRF and weighted fusion; rerank top-k with a cross-encoder and an LLM; find the smallest k that keeps 95% of the gain | Failure Venn diagram, fusion comparison, nDCG and latency per k | 6 h |
| 5 · Query rewriting and Hinglish queries | Conversational condensation, multi-query, HyDE, filter extraction; a 60-query Hinglish test | Recall per technique, regressions found, chosen strategy | 4 h |
| 6 · Permissions and migrations | Document-level ACLs enforced inside the query; tests with adversarial user pairs; zero-downtime migration to a new embedding model | Permission test suite (including caches), migration runbook and logs | 5 h |
| 7 · Citations and abstention | Verify every citation verbatim; tune an abstain threshold; add a corrective second retrieval | Accuracy–coverage curve, citation precision, cost of the second round | 4 h |
| 8 · Golden set, judge calibration and error analysis | Build a 200-question golden set with chunk labels; calibrate a faithfulness judge on 60 human labels; classify 100 failures | Golden set, κ and TPR/TNR of the judge, failure table with the chosen fix | 7 h |
| 9 · GraphRAG vs RAG; text-to-SQL | Run Microsoft GraphRAG on 200 documents and compare on global questions; build text-to-SQL over a sample schema with execution-based scoring | Comparison table with indexing cost; SQL execution accuracy | 6 h |
| 10 · Agentic retrieval with budgets | Turn the pipeline into a search tool for an agent; compare with single-shot retrieval on multi-hop questions; add a token budget and stopping rule | Quality vs tokens plot, recommendation | 5 h |

## Projects

### P1 · A search engine you can measure (L1, ~6 hours)

**Real-world inspiration.** Before any RAG system works, retrieval must work. Search teams measure it with labelled queries and metrics from TREC-style evaluation, and BM25 remains the baseline that dense retrieval must beat (BEIR, 2021).

**What to build.** A search service over a public Indian corpus of at least 5,000 documents (for example PIB press releases or RBI notifications) with BM25 and one dense retriever. Provide a small web or CLI interface, and an evaluation script.

**Acceptance criteria**
- 60 queries labelled by you (at least 15 containing identifiers such as circular numbers or scheme names, at least 10 in Hinglish).
- Reports recall@10, MRR and nDCG@10 for BM25, dense, and simple RRF fusion, each with a bootstrap CI.
- Shows at least five queries where BM25 wins and five where dense wins, with an explanation.
- Index rebuild from raw data is one command and takes under 15 minutes on a laptop.

**Stretch goals.** Add a cross-encoder reranker and report the gain per query type.

**What it proves to an employer.** You know retrieval is an empirical discipline and can show it with labelled data.

### P2 · Permission-aware hybrid RAG over regulatory documents (L2, ~15 hours)

**Real-world inspiration.** DoorDash's support assistant pairs retrieval with a two-tier guardrail and an LLM judge and reports 90% fewer hallucinations (2024). Anthropic's Contextual Retrieval reduced top-20 retrieval failures by 49%, and by 67% with reranking (2024). Banks and fintechs in India answer staff questions from RBI and SEBI circulars, and different teams may see different internal documents. The access-control scenario is illustrative.

**What to build.** A RAG assistant over at least 300 public regulatory PDFs (RBI circulars and master directions), plus 50 synthetic "internal" notes assigned to three departments. Pipeline: structure-aware parsing and chunking with metadata and contextual headers; hybrid retrieval with RRF; cross-encoder reranking; grounded answers with verified citations and an abstain path; ACLs enforced at query time; incremental ingestion with deletes.

**Acceptance criteria**
- 150-question golden set with chunk-level labels (including 30 questions whose answers are in department-restricted notes).
- Recall@10 ≥ 0.85, and higher than BM25 alone with a CI that excludes zero.
- Zero cross-department leaks in 1,000 automated adversarial queries, including after cache warm-up.
- A faithfulness judge calibrated on 60 human labels (κ ≥ 0.6 reported); faithfulness ≥ 0.9 on the golden set.
- Abstains on ≥ 85% of 25 unanswerable questions; p95 latency under 3 s on stated hardware.
- Deleting a document removes it from answers within one ingestion cycle, verified by a test.

**Stretch goals.** Contextual BM25; late chunking; Hindi questions over English documents.

**What it proves to an employer.** You can build RAG that a compliance team would sign off on: measured, permission-safe and able to say "I don't know".

### P3 · A routed knowledge assistant: documents, tables and graphs (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** Real questions mix document lookups, numbers in databases and relationships across records. Uber's QueryGPT and Swiggy's Hermes turn questions into SQL (2024). LinkedIn's knowledge-graph RAG over support tickets improved MRR by 77.6% and cut median resolution time by 28.6% (2024). Microsoft's GraphRAG targets "global" questions over whole corpora (2024). Coding agents search repositories with tools on demand (Anthropic, 2025). The scenario below is illustrative.

**What to build.** An assistant for an imagined e-commerce operations team, built on public data: a relational dataset (for example the Olist e-commerce dataset), a corpus of policy and process documents you write or collect, and a ticket history you generate and label. A router sends each question to document RAG (your P2 pipeline), text-to-SQL (read-only, row-limited, validated), graph retrieval over tickets (GraphRAG or your own entity graph), or an agentic multi-step search. Include an evaluation dashboard and cost per answer.

**Acceptance criteria**
- A 250-question test set covering the four routes plus mixed questions, with answer keys; router accuracy ≥ 90%.
- Text-to-SQL execution accuracy ≥ 80% on 80 questions; generated SQL runs only with read-only credentials and a row limit, and 20 unsafe requests (writes, schema changes) are all refused.
- Graph route beats document RAG on at least 20 multi-hop or global questions, with numbers.
- Retrieval and generation metrics reported separately per route, with a failure taxonomy of 100 errors and the fix applied for the top category.
- Cost per answer and p95 latency per route on a dashboard; the agentic route has a hard token budget.

**Stretch goals.** Learn routing from logs; nightly incremental re-indexing with drift alerts; an MCP server exposing the retrieval tools.

**What it proves to an employer.** You can choose the right retrieval structure for each question type and prove the choice with evaluation, which is the core skill behind enterprise AI assistants.

## Feeds into

- [AIE304 Tool Use and AI Agents](../AIE304_tool_use_and_ai_agents_loops_harnesses_memory/README.md): retrieval becomes a tool inside an agent harness.
- [AIE305 Evaluating LLM Systems](../AIE305_evaluating_llm_systems/README.md): the golden set and judge calibration are extended with statistics and CI gating.
- [AIE403 LLMOps](../../year_4/AIE403_llmops_observability_guardrails_cost_and_latency/README.md): P2 and P3 are instrumented, guarded and cost-engineered.
- [BE403 Backends for AI](../../../backend_engineering/year_4/BE403_backends_for_ai_serving_llm_features_vector/README.md) and [OV08](../../../../04_overlaps/OV08_full_stack_ai_product_engineering/): vector search and serving at scale.

## Sources

- Thakur et al., BEIR (2021) — https://arxiv.org/abs/2104.08663 (checked 2026-10)
- DoorDash (Sept 2024) — https://careersatdoordash.com/blog/large-language-modules-based-dasher-support-automation/ ; Anthropic, Contextual Retrieval (Sept 2024) — https://www.anthropic.com/engineering/contextual-retrieval (checked 2026-10)
- Uber QueryGPT (2024) — https://www.uber.com/blog/query-gpt/ ; Swiggy Hermes (2024) — https://medium.com/swiggy-bytes/hermes-a-text-to-sql-solution-at-swiggy-81573fb4fb6e ; Xu et al., LinkedIn KG-RAG (2024) — https://arxiv.org/abs/2404.17723 ; Edge et al., GraphRAG (2024) — https://arxiv.org/abs/2404.16130 (checked 2026-10)
- RBI notifications — https://www.rbi.org.in/Scripts/NotificationUser.aspx ; PIB — https://www.pib.gov.in/ ; Olist dataset — https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce ; FAISS — https://faiss.ai/ (checked 2026-10)
