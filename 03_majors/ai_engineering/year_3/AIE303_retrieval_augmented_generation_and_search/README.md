# AIE303 · Retrieval-Augmented Generation and Search

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 5 | 4 (≈ 120 hours) | L1 → L3 | [CS214](../../../../02_year_2_core_computer_science/semester_4/CS214_machine_learning_foundations/README.md), [CS205](../../../../02_year_2_core_computer_science/semester_3/CS205_software_engineering_i_design_testing/README.md); taken alongside [AIE301](../AIE301_llm_fundamentals_for_engineers/README.md) | [AIE403](../../year_4/AIE403_llmops_observability_guardrails_cost_and_latency/README.md), [AIE304](../AIE304_tool_use_and_ai_agents_loops_harnesses_memory/README.md), [AIE305](../AIE305_evaluating_llm_systems/README.md), [BE403](../../../backend_engineering/year_4/BE403_backends_for_ai_serving_llm_features_vector/README.md) |

## Why this course matters now

Most LLM products that touch company data are retrieval systems underneath: support assistants, internal search, policy Q&A, text-to-SQL. Reported results show both the upside and the engineering involved. DoorDash's support assistant pairs retrieval with a two-tier guardrail and an LLM judge, and reports 90% fewer hallucinations (2024). LinkedIn combined RAG with a knowledge graph of past tickets, raising MRR by 77.6% and cutting median resolution time by 28.6% (2024). Anthropic's Contextual Retrieval cut top-20 retrieval failures by 49%, and by 67% with reranking (2024). Managed retrieval services and coding assistants can now stand up a demo in an afternoon. What separates a demo from a system people trust is human work: choosing chunk boundaries for messy documents, labelling relevance, enforcing who may see which document, keeping the index fresh, and proving with numbers that the system finds the answer and does not invent one.

## Learning outcomes

By the end you can:

1. **Implement** BM25 and a dense retriever, and **measure** both with recall@k, MRR and nDCG on labelled queries.
2. **Build** a document pipeline (parse, clean, chunk, enrich, embed) for PDFs, HTML and tables, including Indic-language text, and **justify** its chunking strategy with retrieval numbers.
3. **Combine** lexical and vector search with reciprocal rank fusion and a reranker, and **explain** the latency each stage adds.
4. **Operate** a vector index (pgvector, Qdrant or Elasticsearch): HNSW parameters, filtering, quantisation, updates, deletes, re-embedding migrations and per-document permissions.
5. **Generate** grounded answers with citations and an abstain path, and **detect** unfaithful answers automatically.
6. **Evaluate** a RAG system end to end, separating retrieval failures from generation failures, with a judge calibrated against human labels.
7. **Decide** when GraphRAG, text-to-SQL or agentic retrieval beats plain chunk retrieval, and **defend** the cost.
8. **Identify** RAG-specific security risks (permission leaks, poisoned documents, indirect injection, embedding inversion) and **apply** controls.

## Chapters and lessons

### Chapter 1 · Search before LLMs (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 The inverted index | Tokenising, stemming, postings lists, boolean retrieval; why search engines answered queries long before LLMs | Build an inverted index over 50,000 Wikipedia abstracts in Python |
| 1.2 TF-IDF and BM25 | Term frequency saturation (k1), length normalisation (b), IDF; BM25 as the default baseline | Implement BM25; compare with `bm25s` and Pyserini on the same queries |
| 1.3 Relevance and metrics | Qrels, precision@k, recall@k, MRR, nDCG; TREC-style evaluation with `trec_eval` | Label 50 queries yourself; compute all metrics for your BM25 |
| 1.4 Query logs | Head vs tail queries, zero-result rate, reformulation as a failure signal | Analyse a public query log sample; find the 20 most common failure patterns |

**Check your understanding:** Why is BM25 still hard to beat on exact identifiers such as order IDs, error codes and product SKUs? What does nDCG reward that recall@k ignores? Why must you label relevance yourself before trusting any metric?

### Chapter 2 · Dense retrieval and nearest-neighbour search (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Bi-encoders | Dense Passage Retrieval (Karpukhin et al., 2020); contrastive training with in-batch negatives (overview); sentence-transformers | Embed your corpus with two models; compare recall@10 with BM25 |
| 2.2 Exact vs approximate search | Brute-force cosine, HNSW graphs, IVF, product quantisation; the recall–latency–memory triangle (FAISS) | Build flat, HNSW and IVF-PQ indexes over 1M vectors; plot recall vs latency |
| 2.3 HNSW parameters | `M`, `ef_construction`, `ef_search`; build time vs query time; memory per vector | Tune `ef_search` to hit recall ≥ 0.95 at the lowest p95 latency |
| 2.4 Zero-shot generalisation | BEIR (Thakur et al., 2021): dense models trained on one domain can underperform BM25 on others | Run one dense model on three BEIR datasets; report where BM25 wins |

**Check your understanding:** Why can approximate search return a worse neighbour than brute force, and how do you measure how often? When would you accept 0.90 recall for a 10× latency gain? Why might a general-purpose embedding model fail on Indian legal or GST documents?

### Chapter 3 · Documents, parsing and chunking (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Parsing reality | PDFs with columns, tables and scans; HTML boilerplate; parsers such as Docling and MarkItDown; OCR for Devanagari, Tamil and other scripts | Parse 30 government PDFs (RBI circulars, railway notices); score extraction errors by hand |
| 3.2 Chunking strategies | Fixed-size with overlap, recursive by structure (headings, lists), semantic chunking, table-aware chunks | Chunk one corpus four ways; compare recall@5 on the same 100 queries |
| 3.3 Context for chunks | Metadata (title, section, date, source), parent–child ("small-to-big") retrieval, contextual chunk headers (Anthropic Contextual Retrieval), late chunking (Günther et al., 2024) | Add a generated 50-token context header per chunk; measure the recall change and the indexing cost |
| 3.4 Freshness and deletion | Incremental ingestion, content hashing, tombstones, re-indexing schedules, versioned documents | Build an ingestion job that handles edits and deletes; prove a deleted document never appears |

**Check your understanding:** A policy answer is right but cites last year's version. Which part of the pipeline failed? Why does "chunk size 512" have no meaning without a retrieval eval? What do you lose when you chunk a table row by row?

### Chapter 4 · Hybrid search and fusion (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Why hybrid | Lexical recall for names, codes and rare terms; semantic recall for paraphrase; their failure sets overlap little | Build a failure Venn diagram for BM25 vs dense on 200 queries |
| 4.2 Reciprocal rank fusion | score = Σ 1/(k + rank), k = 60 (Cormack et al., 2009); why rank-based fusion avoids score normalisation | Implement RRF; compare with weighted score fusion after min–max normalisation |
| 4.3 Hybrid in real engines | Elasticsearch/OpenSearch RRF, Qdrant hybrid queries, Vespa rank profiles, Postgres full-text + pgvector | Implement the same hybrid query in Postgres and in one dedicated engine |
| 4.4 Filters and routing | Metadata filters (date, language, product), pre- vs post-filtering with ANN, routing queries by type | Route ID-like queries to lexical only; measure the latency and recall effect |

**Check your understanding:** Why does RRF work without knowing what the raw scores mean? What happens to recall when a strict filter removes most HNSW neighbours? Which three query types would you never send to dense retrieval alone?

### Chapter 5 · Reranking (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Cross-encoders | Joint query–document scoring; why rerankers beat bi-encoders but cannot search a whole corpus | Rerank top-50 with a cross-encoder (e.g. bge-reranker); measure nDCG@10 gain |
| 5.2 Late interaction | ColBERT token-level matching (Khattab and Zaharia, 2020): a middle ground in cost and quality | Compare ColBERT with a bi-encoder + reranker on one BEIR dataset |
| 5.3 LLM rerankers | Pointwise, pairwise and listwise LLM ranking; cost per query; position bias in lists | Rerank with a small LLM; compare cost, latency and nDCG with a cross-encoder |
| 5.4 Latency budgets | Candidate counts (k = 20/50/100), batching, GPU vs CPU, caching rerank results | Find the smallest k that keeps 95% of the reranking gain |

**Check your understanding:** Why is reranking top-1,000 rarely worth it? When would an LLM reranker be justified despite its cost? What does a reranker do to a query whose answer is not in the candidate set?

### Chapter 6 · Query understanding (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Conversational queries | Rewriting "what about the second one?" into a standalone query from chat history | Build a condenser; measure recall on 50 multi-turn conversations |
| 6.2 Expansion and HyDE | Multi-query, synonyms, hypothetical document embeddings (Gao et al., 2022) | Compare raw, multi-query and HyDE retrieval on short, vague queries |
| 6.3 Decomposition | Splitting multi-part questions; extracting structured filters from text ("RBI circulars on UPI after 2024") | Implement filter extraction with structured outputs; validate with 40 queries |
| 6.4 Code-mixed queries | Hinglish, transliterated and mixed-script queries; multilingual embeddings vs translate-then-search | Build a 60-query Hinglish test; compare two strategies |

**Check your understanding:** Query rewriting fixed recall but broke three queries that used exact phrases. Why, and how do you guard against it? When does HyDE hurt? Why is translating every Hindi query to English before search not a free win?

### Chapter 7 · Vector databases in production (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Choosing a store | pgvector (HNSW since 0.5.0) vs Qdrant vs Elasticsearch/OpenSearch vs managed services; "use the database you already run" as a default | Write a decision record for a 5M-chunk corpus with a stated budget |
| 7.2 Memory and quantisation | float32 vs float16 vs int8 vs binary vectors; rescoring; Matryoshka truncation | Cut index memory 8× with quantisation + rescoring; report recall loss |
| 7.3 Permissions and tenancy | Document-level ACLs at query time, per-tenant indexes vs filtered shared indexes, the leak-by-retrieval failure | Prove with tests that user A never retrieves user B's documents, including through caches |
| 7.4 Operations | Backups, re-embedding migrations with dual indexes, index rebuild time, monitoring recall drift | Migrate to a new embedding model with zero downtime using dual writes |
| 7.5 RAG security | OWASP LLM08:2025 (vector and embedding weaknesses), poisoned documents, indirect injection in retrieved text, embedding inversion risk | Threat-model your P2 system; add provenance tags and an ingestion allow-list |

**Check your understanding:** Why is filtering after retrieval a permission bug waiting to happen? What would make you move from pgvector to a dedicated engine? How can a document planted in a shared drive influence answers for every employee?

### Chapter 8 · Grounded generation (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Assembling the prompt | Ordering retrieved chunks, deduplication, position effects (Liu et al., 2023), token budgets | Vary chunk order and count; measure answer accuracy |
| 8.2 Citations | Chunk IDs, quote spans, verifying each citation programmatically | Reject any answer whose quotes are not found verbatim in the cited chunk |
| 8.3 Abstention | "Not in the sources" paths, thresholds on retrieval scores, clarifying questions | Measure the accuracy–coverage trade-off as you tune the abstain threshold |
| 8.4 Self-correcting RAG | Self-RAG (Asai et al., 2023), Corrective RAG (Yan et al., 2024), retrieval evaluators and fallback web search | Add a retrieval-quality check that triggers a second search; measure gain and cost |

**Check your understanding:** The answer is correct but the citation points to the wrong chunk: is that acceptable in a legal product? Why is abstaining a feature, not a failure? When does a second retrieval round pay for its latency?

### Chapter 9 · Evaluating RAG (weeks 9–10)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Golden sets | Questions from real logs and from documents, answer keys, relevant-chunk labels, difficulty strata | Build a 200-question golden set with chunk-level labels |
| 9.2 Component metrics | Retrieval: recall@k, MRR, nDCG. Generation: faithfulness, answer relevance, context precision (Ragas, ARES) | Compute both layers; build a failure table by cause |
| 9.3 Judges you can trust | LLM-judge rubrics, agreement with human labels (Cohen's κ), drift of criteria (Shankar et al., 2024) | Calibrate a faithfulness judge on 60 human-labelled answers; report κ |
| 9.4 Error analysis | Taxonomy: not indexed, not retrieved, retrieved but ranked low, ignored by the model, contradicted, outdated | Classify 100 failures; pick the fix with the largest expected gain |
| 9.5 Online signals | Thumbs, escalations, reformulations, citation clicks; why they are biased | Design the dashboard for a support assistant; define each metric precisely |

**Check your understanding:** Faithfulness is 0.95 but users complain: what two explanations can faithfulness not catch? Why must the judge be validated on your own data? Which single failure category usually offers the cheapest fix?

### Chapter 10 · Structured and graph retrieval (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 GraphRAG | Entity and relation extraction, community summaries for "global" questions (Edge et al., 2024); LightRAG (Guo et al., 2024); indexing cost | Run Microsoft GraphRAG on a 200-document corpus; compare global-question answers with plain RAG |
| 10.2 Knowledge graphs in practice | LinkedIn's ticket graph for customer service (Xu et al., 2024); when explicit relations beat chunks | Model a ticket corpus as a graph; answer 20 multi-hop questions |
| 10.3 Text-to-SQL | Schema retrieval, few-shot SQL, validation and read-only execution; Uber QueryGPT (2024) and Swiggy Hermes (2024) | Build text-to-SQL over a sample e-commerce schema; measure execution accuracy |
| 10.4 Choosing the structure | Cost, freshness and maintenance of graphs vs chunks vs SQL | Write a one-page recommendation for a given company scenario |

**Check your understanding:** What question types justify GraphRAG's indexing cost? Why must generated SQL run with read-only credentials and row limits? When does a SQL query beat any amount of retrieval?

### Chapter 11 · Agentic retrieval (weeks 12–13)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Retrieval as a tool | The model decides when and what to search; search, fetch and grep tools; iterative refinement | Turn your pipeline into a `search` tool; compare agentic vs single-shot on multi-hop questions |
| 11.2 Just-in-time vs pre-indexed | Claude Code loads its CLAUDE.md files up front and uses glob and grep to fetch files just in time (Anthropic, Sept 2025); when an index still wins | Answer 30 questions over a code repo with grep-only tools vs a vector index |
| 11.3 Research agents | Parallel sub-searches and synthesis; Anthropic reported its multi-agent research system outperformed a single agent by 90.2% on an internal eval while using about 15× the tokens of chat (2025) | Build a two-level research agent; record tokens per answer |
| 11.4 Stopping and budgets | Search budgets, diminishing returns, duplicate detection, citation requirements | Add a budget and stopping rule; plot quality vs tokens |

**Check your understanding:** Why does agentic retrieval cost more and fail differently from a fixed pipeline? When is grep better than embeddings? What evidence would justify a 15× token cost to a product manager?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · BM25 and qrels | 50 labelled queries |
| 2 | 2 | Lab 2 · ANN index trade-offs | — |
| 3 | 3 | Lab 3 · Parsing and chunking bake-off | **P1 due** |
| 4 | 4 | Lab 4 · Hybrid with RRF | — |
| 5 | 5 | Lab 4 (cont.): Reranker budget | — |
| 6 | 6 | Lab 5 · Query rewriting and Hinglish queries | Mid-term (AI off): metrics and failure diagnosis |
| 7 | 7 | Lab 6 · Permissions and migrations | Threat model |
| 8 | 8 | Lab 7 · Citations and abstention | — |
| 9 | 9 | Lab 8 · Golden set and judge calibration | — |
| 10 | 9 | Lab 8 (cont.): error analysis | **P2 due** |
| 11 | 10 | Lab 9 · GraphRAG vs RAG; text-to-SQL | — |
| 12 | 11 | Lab 10 · Agentic retrieval | — |
| 13 | 11 | Lab 10 (cont.): budgets | Cost–quality report |
| 14 | Integration | P3 demo day | **P3 due** |
| 15 | Review | Oral defence of P3 | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** writing parsers and ingestion code (Claude Code, Cursor, GitHub Copilot); generating candidate questions from documents, which you then filter and label; drafting judge rubrics; summarising failure clusters; first drafts of SQL schemas descriptions for text-to-SQL.
- **Do without AI (drills):** label relevance for at least 100 query–chunk pairs by hand; compute recall@k, MRR and nDCG on paper for a small ranking; read 30 retrieved contexts and say why each answer failed; design a chunking strategy for an unseen document type and defend it orally.
- **Verify AI output by:** comparing every pipeline change against the golden set (retrieval and generation layers separately); checking judge agreement with human labels before using it; testing permissions with adversarial user pairs; re-running ingestion on edited and deleted documents.
- **Where AI still fails here (show it):** model-generated questions are easier than real user questions (often near-copies of a sentence in the chunk); compare the recall of your system on generated vs real queries. LLM judges rate fluent answers as faithful when they add plausible facts not in the context; find ten such cases in Lab 8. Models also answer confidently from training data when retrieval returns nothing; measure how often with retrieval switched off.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10, each with metrics) | 25% |
| Projects P1–P3 | 35% |
| Golden set + calibrated judge (graded on label quality and κ) | 10% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) + oral defence of P3 | 20% |

**Mastery gate.** You pass when you can: (1) given an unseen corpus of about 10,000 documents and 100 labelled questions, build a hybrid + rerank pipeline in one working day and beat a BM25 baseline's recall@10 by a margin you can show is not noise; (2) diagnose three planted faults (bad chunking, a permission leak, a stale index) in an unfamiliar RAG system within 90 minutes; (3) explain to a non-specialist, with numbers, why your system abstains when it does.

## Industry reality

Public engineering write-ups show the same pattern: retrieval quality and evaluation decide success. DoorDash describes an LLM guardrail (a semantic-similarity check, then an LLM evaluator for groundedness and compliance) and an LLM judge scoring retrieval correctness and response accuracy (Sept 2024). LinkedIn's knowledge-graph RAG ran in production for about six months before reporting its resolution-time gain (2024). Uber's QueryGPT and Swiggy's Hermes apply retrieval to database schemas for text-to-SQL (2024), and Zomato described an LLM orchestrator with a vector database behind its consumer assistant (2023). Hybrid search with RRF is built into Elasticsearch, OpenSearch, Qdrant and Vespa, and pgvector added HNSW in version 0.5.0 (2023). The newer shift is agentic retrieval: coding agents navigate repositories with search tools instead of a pre-built vector index (Anthropic, 2025).

**Interview questions from this course**

1. *Design RAG for 2 million internal documents with per-team permissions.* Strong answer: ingestion with change detection; structure-aware chunking with metadata; hybrid retrieval + reranker; ACL enforcement inside the query, not after it; citations and abstention; a golden set and online signals; cost and latency per query; re-embedding plan.
2. *Users say the assistant "can't find" a policy that exists. How do you debug?* Strong answer: reproduce; check whether it is indexed, chunked sensibly, retrieved in the top k, reranked, included in the prompt, or ignored; fix the earliest failing stage; add the case to the golden set.
3. *BM25, dense or hybrid?* Strong answer: depends on query types; BM25 for identifiers and rare terms, dense for paraphrase; hybrid with RRF as a strong default; prove with recall on your queries, not on a leaderboard.
4. *How do you know your RAG system is ready to launch?* Strong answer: separate retrieval and generation metrics on a stratified golden set; a judge validated against humans; permission tests; latency and cost budgets; a red-team pass for poisoned documents; thresholds agreed with the product owner before testing.
5. *When would you use GraphRAG or text-to-SQL instead?* Strong answer: global or multi-hop questions over entities for graphs; aggregations and exact numbers for SQL; cost of building and maintaining each; a measured comparison on representative questions.

## Resources (free first)

- **Information retrieval:** Manning, Raghavan and Schütze, *Introduction to Information Retrieval* (free online) — https://nlp.stanford.edu/IR-book/ ; TREC — https://trec.nist.gov/ ; trec_eval — https://github.com/usnistgov/trec_eval ; Pyserini — https://github.com/castorini/pyserini ; bm25s — https://github.com/xhluca/bm25s
- **Dense retrieval and ANN:** sentence-transformers — https://www.sbert.net/ ; FAISS — https://faiss.ai/ ; BEIR — https://github.com/beir-cellar/beir ; ColBERT — https://github.com/stanford-futuredata/ColBERT ; MTEB leaderboard — https://huggingface.co/spaces/mteb/leaderboard ; bge-reranker — https://huggingface.co/BAAI/bge-reranker-v2-m3
- **Engines:** pgvector — https://github.com/pgvector/pgvector ; Qdrant hybrid queries — https://qdrant.tech/documentation/search/hybrid-queries/ ; Elasticsearch RRF — https://www.elastic.co/docs/reference/elasticsearch/rest-apis/reciprocal-rank-fusion ; OpenSearch hybrid search — https://docs.opensearch.org/latest/vector-search/ai-search/hybrid-search/index/ ; Vespa hybrid tutorial — https://docs.vespa.ai/en/learn/tutorials/hybrid-search.html
- **Parsing:** Docling — https://github.com/docling-project/docling ; MarkItDown — https://github.com/microsoft/markitdown
- **RAG techniques and evaluation:** Anthropic, "Contextual Retrieval" — https://www.anthropic.com/engineering/contextual-retrieval ; Microsoft GraphRAG — https://microsoft.github.io/graphrag/ ; LightRAG — https://github.com/HKUDS/LightRAG ; Ragas — https://github.com/vibrantlabsai/ragas ; Chroma, "Context Rot" — https://www.trychroma.com/research/context-rot ; Eugene Yan, "Patterns for Building LLM-based Systems & Products" — https://eugeneyan.com/writing/llm-patterns/
- **Security:** OWASP LLM08:2025 Vector and Embedding Weaknesses — https://genai.owasp.org/llmrisk/llm082025-vector-and-embedding-weaknesses/
- **Indic language resources:** AI4Bharat — https://ai4bharat.iitm.ac.in/ ; IndicBERT — https://github.com/AI4Bharat/IndicBERT

## Sources

- DoorDash, "Path to high-quality LLM-based Dasher support automation" (17 Sept 2024) — https://careersatdoordash.com/blog/large-language-modules-based-dasher-support-automation/ (checked 2026-10)
- Xu et al., "Retrieval-Augmented Generation with Knowledge Graphs for Customer Service Question Answering" (LinkedIn, 2024) — https://arxiv.org/abs/2404.17723 (checked 2026-10)
- Anthropic, "Introducing Contextual Retrieval" (19 Sept 2024): failures −35% / −49% / −67% — https://www.anthropic.com/engineering/contextual-retrieval (checked 2026-10)
- Anthropic, "Effective context engineering for AI agents" (29 Sept 2025) — https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents ; "How we built our multi-agent research system" (13 Jun 2025) — https://www.anthropic.com/engineering/multi-agent-research-system (checked 2026-10)
- Uber, "QueryGPT – Natural Language to SQL Using Generative AI" (Sept 2024) — https://www.uber.com/blog/query-gpt/ ; Swiggy Bytes, "Hermes: A Text-to-SQL solution at Swiggy" (Jul 2024) — https://medium.com/swiggy-bytes/hermes-a-text-to-sql-solution-at-swiggy-81573fb4fb6e ; Zomato, "Introducing Zomato AI" (Sept 2023) — https://www.zomato.com/blog/introducing-zomato-ai-your-foodie-buddy/ (checked 2026-10)
- Cormack, Clarke and Büttcher, "Reciprocal Rank Fusion outperforms Condorcet and individual Rank Learning Methods" (SIGIR 2009) — https://cormack.uwaterloo.ca/cormacksigir09-rrf.pdf (checked 2026-10)
- pgvector CHANGELOG (HNSW in 0.5.0, Aug 2023) — https://github.com/pgvector/pgvector (checked 2026-10)
- Lewis et al. (2020) — https://arxiv.org/abs/2005.11401 ; Karpukhin et al. (2020) — https://arxiv.org/abs/2004.04906 ; Khattab and Zaharia (2020) — https://arxiv.org/abs/2004.12832 ; Thakur et al., BEIR (2021) — https://arxiv.org/abs/2104.08663 (checked 2026-10)
- Gao et al., HyDE (2022) — https://arxiv.org/abs/2212.10496 ; Asai et al., Self-RAG (2023) — https://arxiv.org/abs/2310.11511 ; Yan et al., CRAG (2024) — https://arxiv.org/abs/2401.15884 ; Günther et al., Late Chunking (2024) — https://arxiv.org/abs/2409.04701 ; Liu et al. (2023) — https://arxiv.org/abs/2307.03172 (checked 2026-10)
- Edge et al., GraphRAG (2024) — https://arxiv.org/abs/2404.16130 ; Guo et al., LightRAG (2024) — https://arxiv.org/abs/2410.05779 (checked 2026-10)
- Es et al., Ragas (2023) — https://arxiv.org/abs/2309.15217 ; Saad-Falcon et al., ARES (2023) — https://arxiv.org/abs/2311.09476 ; Shankar et al. (2024) — https://arxiv.org/abs/2404.12272 (checked 2026-10)

_Last reviewed: 2026-10_
