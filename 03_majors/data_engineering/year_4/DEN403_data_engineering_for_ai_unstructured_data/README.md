# DEN403 · Data Engineering for AI: Unstructured Data, Embeddings and RAG Pipelines

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 8 | 4 (≈ 120 hours) | L3 → L4 | [DEN303](../../year_3/DEN303_streaming_systems_kafka_and_flink/README.md) | [DEN501](../../year_5/DEN501_frontier_seminar_real_time_ai_data_systems/README.md), [OV04](../../../../04_overlaps/OV04_mlops_ml_platform/README.md), [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) |

Part of the [Data Engineering major](../../README.md). Most data that AI systems need is not in tables. It sits in PDFs, scanned forms, web pages, tickets, chats and images. This course builds the pipelines that turn that material into clean, versioned, permission-aware datasets, chunk stores, embedding indexes and training sets, and keeps them fresh and measurable. Retrieval algorithms and prompt design are taught in [AIE303](../../../ai_engineering/year_3/AIE303_retrieval_augmented_generation_and_search/README.md), and model training pipelines in [MLE303](../../../machine_learning_engineering/year_3/MLE303_training_pipelines_feature_stores_and_experiment/README.md). This course owns the data underneath both.

## Why this course matters now

Model quality depends heavily on the data pipeline. The FineWeb project (2024) documented a 15-trillion-token dataset built from 96 Common Crawl snapshots, and showed through ablations that deduplication and filtering choices change model quality. An earlier study found that deduplicating training data makes language models better (Lee et al., 2021). A *Nature* paper (2024) showed that models trained recursively on generated data degrade, a phenomenon the authors call model collapse. On the retrieval side, a RAG assistant cannot answer correctly from a document that was parsed into garbage, chunked across a table, embedded with a different model version, or deleted at the source but still in the index. The tools are moving into the data stack: Spark 4.2 added a `NEAREST BY` top-K join, Flink CDC 3.7 (October 2026) calls embedding and chat models inside pipelines, and DuckDB reads Hugging Face datasets in place (September 2026). Indian public data adds real difficulty: the Indian Supreme Court judgments dataset on AWS Open Data covers 1950–2025 in English and regional languages, as PDFs with Parquet metadata. Assistants now parse documents with vision-language models, write chunkers and generate synthetic questions. Measuring whether any of it improved retrieval, and proving that a deleted record is gone from every index, remains engineering work.

## Learning outcomes

By the end you can:

1. **Build** ingestion for unstructured sources (object stores, web crawls, APIs) that records provenance, licences, permissions and change detection for every document.
2. **Parse** PDFs, scans and HTML with layout-aware tools and OCR (including Indic scripts), and **measure** parser quality on a labelled sample (character error rate, table-cell F1, cost per page).
3. **Clean** corpora at scale: normalisation, language identification, quality filtering, exact and near-duplicate removal (MinHash LSH), PII detection and redaction, and evaluation-set decontamination.
4. **Design** chunking strategies and **prove** which is best for a corpus with retrieval metrics, not intuition.
5. **Run** batch and streaming embedding pipelines with model versioning, re-embedding migrations, cost control and vector storage in Parquet, Lance or a vector database.
6. **Keep** retrieval indexes fresh and permission-correct under inserts, updates and deletes, and **propagate** erasure requests to every copy.
7. **Evaluate** retrieval data quality with golden sets and metrics (recall@k, MRR, nDCG), and **gate** pipeline changes on them in CI.
8. **Produce** versioned, documented training and fine-tuning datasets (datasheets, licences, splits, decontamination), and **use** labelling and synthetic data with measured risks.

## Chapters and lessons

### Chapter 1 · Data as the bottleneck for AI systems (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 The AI data lifecycle | Pretraining corpora, fine-tuning sets, RAG corpora, evaluation sets, feedback logs; who owns each | Map every dataset an AI support assistant needs, with owner and refresh rate |
| 1.2 Case study: FineWeb | Crawl snapshots → text extraction → filtering → deduplication → ablations; the open `datatrove` library | Read the FineWeb paper's pipeline section; redraw it as a DAG with data volumes |
| 1.3 Failure stories | Stale indexes, leaked permissions, duplicated documents, OCR noise, wrong embedding versions (illustrative scenarios) | For each failure, write the check that would have caught it |
| 1.4 The stack | Raw document store (bronze), parsed text, chunks, embeddings, indexes, datasets; open formats (Parquet, Lance, Iceberg) | Set up the course stack: MinIO, DuckDB, Ray, PostgreSQL with pgvector, LanceDB |

**Check your understanding:** (1) Why do RAG corpora need provenance and permissions more than warehouse tables do? (2) What did FineWeb's ablations measure that a pipeline unit test cannot? (3) Which layer of the stack should a deletion request reach first?

### Chapter 2 · Ingesting unstructured sources (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Sources and connectors | Object stores, document systems, ticketing and email APIs, web crawls; pagination, rate limits, incremental sync tokens | Ingest the Indian Supreme Court judgments bucket (unsigned S3 access) and its Parquet metadata |
| 2.2 Web data | `robots.txt`, crawl politeness, Common Crawl WARC/WAT/WET files, licence and terms checks | Extract 10,000 pages for one domain from a Common Crawl snapshot |
| 2.3 Change detection | ETags, content hashes, modified timestamps, tombstones for deleted sources | Detect changed and deleted documents between two syncs |
| 2.4 Metadata that must travel | Source URI, licence, access-control lists, language, timestamps, content hash, pipeline version | Design the document metadata schema and enforce it as a contract |

**Check your understanding:** (1) Why is a content hash a better change signal than a modified time? (2) What must you record to honour a licence later? (3) Why must ACLs be captured at ingestion rather than looked up at query time only?

### Chapter 3 · Parsing documents (weeks 3–4)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 PDF internals | Text layers vs scanned images, fonts and encodings, reading order, columns, headers and footers | Extract text from 50 judgments with `pypdf` and PyMuPDF; list every failure type |
| 3.2 Layout-aware parsing | Layout models, table structure recognition, section hierarchy; Docling and Unstructured | Parse the same 50 documents with Docling; compare structure and tables |
| 3.3 OCR | Tesseract with Indic language data, image preprocessing, confidence scores; vision-language models for parsing and their hallucination risk | OCR 30 scanned pages in Hindi and English; measure character error rate against hand transcriptions |
| 3.4 HTML | Boilerplate removal (Trafilatura), main-content extraction, links and tables | Extract main text from 1,000 news pages; measure boilerplate leakage on a labelled sample |
| 3.5 Measuring parsers | Labelled evaluation sets, character error rate, table-cell F1, cost and latency per page, routing by document type | Build a parser router that sends each document to the cheapest parser meeting a quality bar |

**Check your understanding:** (1) Why can a parser report success and still produce useless text? (2) When is a vision-language model worth its cost per page, and how do you catch it inventing table cells? (3) Why should parser choice be routed per document type?

### Chapter 4 · Cleaning, deduplication and filtering (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Normalisation and language | Unicode normalisation (NFC), Indic script handling, language identification, mixed-language text | Normalise and language-tag 100,000 chunks; count mixed-script cases |
| 4.2 Quality filters | Heuristic filters (length, symbol ratio, repetition), classifier filters; FineWeb's ablation approach | Apply 5 filters; measure what each removes on a labelled sample |
| 4.3 Deduplication | Exact hashing, MinHash with locality-sensitive hashing, thresholds, cluster representatives | Find near-duplicate judgments and news articles with `datasketch`; tune the threshold on labelled pairs |
| 4.4 PII | Detection with Microsoft Presidio and custom recognisers for Indian identifiers (PAN format; Aadhaar's Verhoeff check digit), redaction vs pseudonymisation | Build an Indian-identifier recogniser; measure precision and recall on a seeded set |
| 4.5 Decontamination | Removing evaluation questions and answers from training or retrieval corpora; n-gram overlap checks | Detect a planted leak of your golden set into the corpus |

**Check your understanding:** (1) Why does near-duplicate removal need a labelled sample to set its threshold? (2) Why is a regular expression alone a weak Aadhaar detector? (3) What goes wrong in evaluation if your golden questions are inside the corpus?

### Chapter 5 · Chunking (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Strategies | Fixed-size, recursive, structure-aware (sections, headings, tables), sentence windows, parent–child chunks | Implement 4 chunkers over the judgments corpus |
| 5.2 Metadata enrichment | Section path, document title, dates, court, citations, ACLs attached to every chunk | Add metadata; show a filtered retrieval that needs it |
| 5.3 Tables and lists | Keeping tables whole, table summaries, row-level chunks for structured content | Compare 3 ways of chunking tables on table-answerable questions |
| 5.4 Choosing by measurement | Retrieval metrics per chunker on a golden set; cost (chunks per document, tokens embedded) | Pick a chunker with evidence and record the decision |

**Check your understanding:** (1) Why does overlap help recall but cost money and create duplicates in results? (2) Which questions fail when a table is split across chunks? (3) Why must the chunker version be stored with each chunk?

### Chapter 6 · Embedding pipelines (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Choosing models | MTEB as a starting point, domain and language fit (Indic languages), dimensions, cost, licences; measuring on your own data | Shortlist 3 embedding models from MTEB; test on your golden set |
| 6.2 Batch embedding at scale | GPU batching, Ray Data and Spark with Arrow UDFs, API rate limits and retries, cost per million chunks | Embed 1M chunks with Ray Data; report throughput and cost |
| 6.3 Storage | Vectors in Parquet, Lance and Iceberg; quantisation (int8, binary) and its recall cost | Store vectors three ways; compare size, random-access latency and recall after quantisation |
| 6.4 Versioning and migration | Model and version on every vector, dual indexes, backfill re-embedding, cut-over | Migrate an index to a new model with zero downtime and an A/B recall check |

**Check your understanding:** (1) Why is mixing vectors from two model versions in one index a silent bug? (2) Where does the time go in a batch embedding job, and how do you find out? (3) When does binary quantisation lose too much recall?

### Chapter 7 · Vector stores and indexes (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Index structures | HNSW, IVF, product quantisation; build time, memory and recall trade-offs (building on [CS211](../../../../02_year_2_core_computer_science/semester_4/CS211_database_systems_internals/README.md) lesson 5.5) | Sweep HNSW parameters in pgvector; plot recall vs latency |
| 7.2 Where vectors live | pgvector in PostgreSQL, dedicated stores (Milvus, Qdrant), lake-native (LanceDB), warehouse vector features; operational trade-offs | Run the same 1M-vector workload on pgvector and LanceDB |
| 7.3 Filtering and hybrid search | Pre-filter vs post-filter, metadata indexes, BM25 plus vectors | Show a post-filter returning too few results; fix it |
| 7.4 Permissions in the index | Per-chunk ACLs, tenant isolation, filtering at query time vs separate indexes; testing for leaks | Write a test suite that proves no user can retrieve a chunk they cannot read at the source |

**Check your understanding:** (1) Why can approximate search hide a relevant chunk that exact search finds? (2) What does post-filtering do to recall under a strict filter? (3) Why is a permission leak in retrieval worse than one in a dashboard?

### Chapter 8 · Freshness, updates and deletion (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Incremental pipelines | Change-driven re-parsing and re-embedding, idempotent upserts by chunk ID, orphaned chunks | Update 1,000 source documents; verify only affected chunks are re-embedded |
| 8.2 Streaming ingestion | CDC from document stores and databases into Kafka, embedding in Flink (Flink CDC model functions) or consumers, back-pressure from rate-limited APIs (building on [DEN303](../../year_3/DEN303_streaming_systems_kafka_and_flink/README.md)) | Stream ticket updates into an index with a 60-second freshness target |
| 8.3 Deletes and erasure | Tombstones, index deletes vs rebuilds, copies in caches, backups, evaluation sets and fine-tuning data | Delete one person's documents and prove absence from every store |
| 8.4 Freshness SLOs | Source-to-index lag, monitoring, alerting; ACL change propagation lag | Build a freshness dashboard and an alert on ACL lag |

**Check your understanding:** (1) Why do deletes break many naive RAG pipelines? (2) Which is more dangerous, content lag or ACL lag, and why? (3) Where can a deleted document still hide after the index delete succeeds?

### Chapter 9 · Evaluating retrieval data quality (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Golden sets | Question-to-passage labels by domain experts, coverage of question types, size and refresh | Label 200 questions over the judgments corpus with a partner; measure agreement |
| 9.2 Metrics | Recall@k, MRR, nDCG; BEIR as a reference benchmark; RAGAS context precision and recall | Compute all metrics for 3 pipeline variants |
| 9.3 Synthetic questions | Generating questions with an LLM, filtering and human review, biases of synthetic sets | Generate 500 questions; compare metric rankings with the human set |
| 9.4 Regression gates | Running retrieval evaluation in CI when parsers, chunkers or models change; thresholds | Block a chunker change that lowers recall@10 by more than 2 points |

**Check your understanding:** (1) Why can synthetic questions make a pipeline look better than it is? (2) What does a recall@10 drop of 3 points mean for users? (3) Why should the golden set be versioned like code?

### Chapter 10 · Datasets for training and fine-tuning (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Documentation | Datasheets for Datasets (Gebru et al.), Hugging Face dataset cards, licence and consent provenance | Write a datasheet for your corpus |
| 10.2 Formats and splits | JSONL chat formats, train/validation/test splits by source and time to avoid leakage | Build an instruction dataset from judgments (question, answer, citation) with leak-free splits |
| 10.3 Versioning | Iceberg snapshots and tags, lakeFS branches, DVC, Hugging Face dataset revisions; reproducible data builds | Reproduce dataset v1 exactly after building v2 |
| 10.4 Reading datasets in place | DuckDB over Hugging Face datasets (`hf://`), Parquet on object storage | Profile a public Hugging Face dataset without downloading it |

**Check your understanding:** (1) Why split by source or time instead of randomly? (2) What must a datasheet say about consent and licences? (3) How do you prove that a model was trained on exactly dataset v1?

### Chapter 11 · Labelling and synthetic data (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Labelling workflows | Label Studio projects, guidelines, inter-annotator agreement (Cohen's kappa), adjudication | Run a 3-annotator labelling round; compute kappa and fix the guideline |
| 11.2 LLMs as labellers | Pre-labelling with an LLM, human audit sampling, measuring LLM–human agreement | Pre-label 2,000 items; audit 200; decide whether to trust it |
| 11.3 Synthetic data | Generation for rare cases and privacy, filtering, mixing ratios; model collapse risk (*Nature*, 2024) | Add synthetic examples for a rare class; measure the effect and the drift |
| 11.4 Privacy of generated data | Memorisation and re-identification risk; links to privacy-enhancing technologies ([OV07A](../../../../04_overlaps/OV07_privacy_engineering/OV07A_privacy_by_design_and_privacy_enhancing/README.md)) | Test whether synthetic records copy real ones by nearest-neighbour distance |

**Check your understanding:** (1) What does low inter-annotator agreement tell you about the task? (2) When is LLM pre-labelling a false economy? (3) Why must synthetic data be labelled as synthetic in every downstream table?

### Chapter 12 · Designing and operating an AI data platform (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Reference architecture | Raw documents → parsed → chunks → embeddings → indexes and datasets; feedback logs back into evaluation | Draw your P3 architecture with data volumes and SLOs |
| 12.2 Cost model | Cost per 1M pages parsed, per 1M chunks embedded, per index rebuild; GPU vs API trade-offs | Build a cost model and find the top two drivers |
| 12.3 Observability | Parse failure rates, OCR confidence, embedding lag, index size, retrieval metrics over time (from [DEN401](../DEN401_data_quality_observability_and_data_contracts/README.md)) | Add 8 monitors to P3 |
| 12.4 Governance | PII, licences, ACLs, erasure and retention under India's DPDP Act and GDPR (deepened in [DEN404](../DEN404_data_governance_lineage_and_privacy_engineering/README.md)) | Write the governance section of your P3 design |
| 12.5 Capstone review | Present and defend P3 | Oral defence |

**Check your understanding:** (1) Which costs scale with corpus size, and which with update rate? (2) What single metric would you show leadership for "is our RAG data healthy"? (3) Which governance failure would be hardest to detect, and how would you detect it?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Stack and FineWeb DAG | Running stack; pipeline diagram |
| 2 | 2 | Lab 2 · Ingesting judgments | Bronze documents with metadata contract |
| 3 | 3 | Lab 3 · Parser shoot-out | Failure taxonomy |
| 4 | 3 | Lab 4 · OCR and routing | CER table, router; **P1 due** |
| 5 | 4 | Lab 5 · Dedup, PII, decontamination | Threshold and recogniser reports |
| 6 | 5 | Lab 6 · Chunker comparison | Metric table |
| 7 | 6 | Lab 7 · Embedding at scale | Throughput and cost; mid-term (AI off) |
| 8 | 7 | Lab 8 · Indexes and permissions | Recall–latency plot; leak tests |
| 9 | 8 | Lab 9 · Freshness and erasure | Erasure proof; **P2 due** |
| 10 | 9 | Lab 10 · Golden sets and CI gates | Blocked regression |
| 11 | 10 | Lab 11 · Versioned instruction dataset | Datasheet; reproducible build |
| 12 | 11 | Lab 12 · Labelling and synthetic data | Kappa and audit reports |
| 13 | 12 | P3 integration | Monitors and cost model |
| 14 | 12 | Capstone review | **P3 due** |
| 15 | Review | Oral defence of P3 | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** document parsing (vision-language models as one parser option among several), generating candidate questions for golden sets, pre-labelling, writing connector and pipeline boilerplate, summarising parser failure logs. Tools: Claude Code, GitHub Copilot, Cursor; hosted and open-weight embedding and chat models; Docling and Unstructured, which can call models internally.
- **Do without AI (drills):** labelling the first 100 golden-set items yourself; computing recall@k, MRR and nDCG by hand for a small example; tracing a document from source to index by hand to verify its ACL; writing the erasure proof. Evaluation that you cannot do by hand, you cannot audit.
- **Verify AI output by:** (1) a labelled sample for every AI-assisted step (parsing, labelling, question generation), with agreement or error rates computed; (2) retrieval metrics on a human golden set before and after any AI-proposed change; (3) leak tests for permissions and decontamination; (4) cost and latency per page or chunk, measured.
- **Where AI still fails here (show it yourself):** in Lab 4, parse 30 tables with a vision-language model and with a layout parser. Count invented or shifted cells against the source. In Lab 10, compare metric rankings from synthetic and human questions, and record where they disagree. In Lab 12, audit LLM pre-labels and report the agreement. Every course deliverable that uses AI includes its measured error rate.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs 1–12 | 25% |
| Projects P1 / P2 / P3 | 5% / 12% / 18% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) | 20% |
| Oral defence of P3 | 10% |

**Mastery gate.** You pass when you can, without AI: (1) given a new corpus and a 100-question golden set, choose a parser, chunker and embedding model with measured evidence, and beat a provided baseline's recall@10; (2) prove, for a named person, that their documents are absent from every store (raw, parsed, chunks, vectors, caches, datasets) after an erasure request; (3) find a planted defect (a wrong embedding model on 5% of vectors, an ACL leak, or a golden-set leak into the corpus) within 45 minutes using your monitors and tests.

## Industry reality

Open pipelines like FineWeb's show what large-scale text curation looks like in public. Commercial RAG systems depend on the same unglamorous steps: connectors, parsing, chunking, embedding, indexing, permission filtering and freshness. Vendors are moving these steps into existing data tools: model calls in Flink CDC pipelines, nearest-neighbour joins in Spark, vector features in warehouses, and direct dataset access from DuckDB. The market map for this role lists "AI data engineer" as a newer title focused on document ingestion, chunking, embeddings and retrieval indexes ([DEN market page](../../../../06_career_and_market_readiness/01_market_map/roles/DEN_data_engineering.md)).

**Interview questions from this course**

1. *"Design the ingestion pipeline for a RAG assistant over 2 million company documents."* A strong answer covers connectors with change detection, ACL capture, parser routing by document type, chunking with metadata, embedding with versioning, index choice, freshness and deletion handling, evaluation with a golden set, and cost.
2. *"Retrieval quality dropped after last week's release. How do you find out why?"* Check what changed (parser, chunker, model, index parameters, corpus), compare golden-set metrics per version, inspect failing questions, look for mixed embedding versions or stale chunks, and roll back by version.
3. *"How do you remove a user's data from an AI system?"* Cover raw stores, parsed and chunk tables, vector indexes, caches, backups, evaluation and fine-tuning datasets, lakehouse snapshots, and how to prove absence. Note what cannot be undone for models already trained.
4. *"How would you deduplicate a 500 GB text corpus?"* Cover exact hashing, MinHash LSH for near duplicates, shingle size and threshold tuning on labelled pairs, distributed execution, and the effect on downstream quality.
5. *"How do you know your chunking strategy is good?"* Answer with a golden set, recall@k, MRR and nDCG per strategy, cost per strategy, failure analysis on tables and long sections, and a CI gate for future changes.

## Resources (free first)

- **Papers:** [The FineWeb Datasets](https://arxiv.org/abs/2406.17557) (2024); [Deduplicating Training Data Makes Language Models Better](https://arxiv.org/abs/2107.06499) (2021); [AI models collapse when trained on recursively generated data](https://www.nature.com/articles/s41586-024-07566-y) (*Nature*, 2024); [Datasheets for Datasets](https://arxiv.org/abs/1803.09010); [BEIR](https://arxiv.org/abs/2104.08663); [MTEB](https://arxiv.org/abs/2210.07316); [Docling Technical Report](https://arxiv.org/abs/2408.09869).
- **Tools:** [datatrove](https://github.com/huggingface/datatrove); [Docling](https://github.com/docling-project/docling); [Unstructured](https://github.com/Unstructured-IO/unstructured); [Tesseract](https://github.com/tesseract-ocr/tesseract) and [language data](https://github.com/tesseract-ocr/tessdata); [pypdf](https://pypdf.readthedocs.io/); [PyMuPDF](https://github.com/pymupdf/PyMuPDF); [Trafilatura](https://github.com/adbar/trafilatura); [datasketch](https://github.com/ekzhu/datasketch); [Microsoft Presidio](https://microsoft.github.io/presidio/); [pgvector](https://github.com/pgvector/pgvector); [LanceDB](https://lancedb.github.io/lancedb/) and the [Lance format](https://github.com/lance-format/lance); [Qdrant](https://qdrant.tech/documentation/); [Ray Data](https://docs.ray.io/en/latest/data/data.html); [Flink CDC](https://nightlies.apache.org/flink/flink-cdc-docs-stable/); [RAGAS](https://docs.ragas.io/); [Label Studio](https://labelstud.io/); [DVC](https://dvc.org/); [lakeFS docs](https://docs.lakefs.io/); [Hugging Face datasets](https://huggingface.co/docs/datasets/) and [dataset cards](https://huggingface.co/docs/hub/datasets-cards); [MTEB leaderboard](https://huggingface.co/spaces/mteb/leaderboard).
- **Datasets:** [Indian Supreme Court Judgments](https://registry.opendata.aws/indian-supreme-court-judgments/) and [Indian High Court Judgments](https://registry.opendata.aws/indian-high-court-judgments/) (AWS Open Data, CC-BY-4.0); [Common Crawl](https://commoncrawl.org/get-started); [FineWeb on Hugging Face](https://huggingface.co/datasets/HuggingFaceFW/fineweb).
- **Courses:** [Data Engineering Zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp) for pipeline foundations (free); retrieval depth in [AIE303](../../../ai_engineering/year_3/AIE303_retrieval_augmented_generation_and_search/README.md).

## Sources

All checked October 2026.

- Penedo et al., "The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale" (arXiv 2406.17557, v2 31 Oct 2024): 15T tokens, 96 Common Crawl snapshots, FineWeb-Edu 1.3T tokens. https://arxiv.org/abs/2406.17557
- Lee et al., "Deduplicating Training Data Makes Language Models Better" (arXiv 2107.06499). https://arxiv.org/abs/2107.06499
- Shumailov et al., "AI models collapse when trained on recursively generated data", *Nature* (2024). https://www.nature.com/articles/s41586-024-07566-y
- AWS Open Data Registry, Indian Supreme Court Judgments (1950–2025, English and regional languages, JSON and Parquet metadata, bi-monthly updates, CC-BY-4.0, Dattam Labs) and Indian High Court Judgments (25 High Courts, PDFs with Parquet metadata, quarterly). https://registry.opendata.aws/indian-supreme-court-judgments/ ; https://registry.opendata.aws/indian-high-court-judgments/
- Apache Spark 4.2.0 release notes (`NEAREST BY` top-K ranking join). https://spark.apache.org/releases/spark-release-4-2-0.html
- Apache Flink posts (Flink CDC 3.7.0, 10 Oct 2026: pluggable model API, OpenAI-compatible client, text and multimodal functions). https://flink.apache.org/posts/
- DuckDB, "DuckDB and Hugging Face: Querying Datasets Directly" (25 Sep 2026). https://duckdb.org/2026/09/25/hugging-face.html

_Last reviewed: 2026-10_
