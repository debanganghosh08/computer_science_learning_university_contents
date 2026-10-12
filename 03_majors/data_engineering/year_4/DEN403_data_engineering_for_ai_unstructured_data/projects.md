# DEN403 · Labs and projects

The main corpora are the [Indian Supreme Court Judgments](https://registry.opendata.aws/indian-supreme-court-judgments/) and [Indian High Court Judgments](https://registry.opendata.aws/indian-high-court-judgments/) datasets on AWS Open Data (CC-BY-4.0, readable without an AWS account), plus Common Crawl extracts. Together they give real PDFs, scans, Indic scripts, citations and near-duplicates. The labs run on a laptop with MinIO, DuckDB, PostgreSQL with pgvector, LanceDB and Ray. A small GPU or a capped embedding-API budget helps for Labs 7 and 9. Labs 4, 6 and 10 include an AI-off component: the hand labels and metric calculations.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Stack and FineWeb DAG | Run the course stack; redraw FineWeb's pipeline as a DAG with volumes | Running stack, DAG diagram | 3 h |
| 2 · Ingesting judgments | Ingest one year of Supreme Court judgments with a metadata contract (source, licence, language, hash) | Bronze table, contract, change-detection test | 4 h |
| 3 · Parser shoot-out | Parse 50 judgments with `pypdf`, PyMuPDF and Docling | Failure taxonomy and quality table | 5 h |
| 4 · OCR and routing | Hand-transcribe 30 pages (Hindi and English); measure CER for Tesseract and one model-based parser; build a router | CER table, cost per page, router code | 6 h |
| 5 · Dedup, PII, decontamination | MinHash near-dedup with a tuned threshold; an Indian-identifier recogniser; detect a planted golden-set leak | Precision/recall reports and leak evidence | 5 h |
| 6 · Chunker comparison | 4 chunkers evaluated on a 100-question golden set you label yourself | Metric table and decision record | 6 h |
| 7 · Embedding at scale | Embed 1M chunks with Ray Data; store in Parquet, Lance and pgvector | Throughput, cost, storage and recall-after-quantisation table | 5 h |
| 8 · Indexes and permissions | HNSW parameter sweep; per-chunk ACLs; a leak-test suite | Recall–latency plot and passing leak tests | 5 h |
| 9 · Freshness and erasure | Streaming updates with a 60-second target; erase one person from every store | Freshness dashboard and erasure proof | 5 h |
| 10 · Golden sets and CI gates | Compute recall@k, MRR and nDCG by hand for 5 queries, then in code; gate a chunker change in CI | Hand calculations, CI run that blocks a regression | 4 h |
| 11 · Versioned instruction dataset | Build a citation-grounded question–answer dataset with leak-free splits and a datasheet | Dataset v1 and v2, reproducibility proof, datasheet | 5 h |
| 12 · Labelling and synthetic data | 3-annotator round with kappa; LLM pre-labelling with audit; synthetic rare-class data with a copying check | Agreement and audit reports | 5 h |

## Projects

### P1 · Clean judgments corpus (L1, ~6 hours)

**Real-world inspiration:** legal research tools in India are built on court judgments published through eCourts. The AWS Open Data copies are maintained as PDFs with JSON and Parquet metadata. Turning them into clean, searchable text is the first step for any legal AI product.

**What to build:** a pipeline that takes 500 Supreme Court judgments, at least 50 of them in Hindi or another regional language, and produces a Parquet table of parsed text with metadata. It must:

- route each document to a parser;
- normalise Unicode;
- tag language;
- flag near-duplicates;
- scan for personal identifiers.

**Acceptance criteria:**
- Every output row carries source URI, licence, language, content hash, parser name and version.
- On 30 hand-checked pages, the character error rate is under 5% for English text-layer documents, and the measured rate for regional-language scans is reported honestly, whatever it is.
- Near-duplicate pairs above your chosen threshold are listed. Precision is measured on 50 labelled pairs.
- Re-running the pipeline on unchanged input produces identical output (same content hashes).

**Stretch goals:** extract case citations into a separate table and build a citation graph; compare two OCR engines on the regional-language subset.

**What it proves to an employer:** you can turn messy, multilingual documents into a trustworthy corpus with provenance, which every AI data team needs first.

### P2 · Measured RAG ingestion pipeline (L2, ~15 hours)

**Real-world inspiration:** teams building retrieval assistants often tune prompts while the real problem sits in parsing, chunking or embedding. A pipeline with a golden set and metrics turns guesses into decisions.

**What to build:** an ingestion pipeline for about 20,000 judgments from one High Court: parse, clean, chunk (3 strategies), embed (2 models), and index in pgvector or LanceDB. Build a golden set of 150 questions with relevant passages. At least 100 questions are labelled by you; the rest may be synthetic but must be reviewed. Add a CI job that runs retrieval evaluation on every pipeline change, and an incremental update that processes a new quarterly release.

**Acceptance criteria:**
- **Measurement:** recall@10, MRR and nDCG@10 are reported for all 6 chunker × model combinations, with confidence intervals from bootstrap resampling.
- **Improvement:** the chosen combination beats a provided naive baseline (fixed 512-token chunks, a default model) by at least 10 points of recall@10, or the report explains with evidence why no combination can.
- **Regression gate:** a deliberately worse chunker change is blocked by CI.
- **Incremental update:** a simulated quarterly update re-embeds only new or changed documents, verified by counting, and the index never mixes embedding model versions (checked by a test).
- **Cost:** cost per 1,000 documents (parsing, embedding, storage) is reported.

**Stretch goals:** hybrid BM25 plus vector retrieval; a re-ranker and its cost–quality trade-off; table-aware chunking for judgments that contain tables.

**What it proves to an employer:** you build AI data pipelines that are measured, gated and incremental, not demos.

### P3 · AI data platform with freshness, permissions and erasure (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** enterprise assistants must answer from fresh data, never show a user a document they cannot open, and forget people on request. India's DPDP Rules 2025 and the EU's GDPR both require erasure of personal data in many cases (see [DEN404](../DEN404_data_governance_lineage_and_privacy_engineering/README.md)). The organisation below is illustrative.

**What to build:** a platform for a fictional legal-services firm that serves both retrieval and fine-tuning data. It has three sources:

- public judgments (batch, quarterly);
- an internal document store of about 5,000 synthetic case notes with per-document ACLs for 4 user groups;
- a stream of client tickets (Kafka) that must be searchable within 2 minutes.

The platform must:

- run parsing, cleaning, PII redaction, chunking and embedding with versioning;
- keep an ACL-aware index;
- build a versioned instruction dataset (with a datasheet) derived from public data only;
- run an erasure workflow that covers every store;
- monitor its own health (parse failures, OCR confidence, embedding lag, ACL lag, retrieval metrics);
- come with a cost model.

**Acceptance criteria:**
- **Freshness:** p95 source-to-searchable latency is under 2 minutes for tickets and under 24 hours for internal documents, measured over a 48-hour run.
- **Permissions:** a leak-test suite of at least 200 cases (users × documents) passes with zero leaks. A revoked permission takes effect in the index within 5 minutes.
- **Erasure:** for 3 named synthetic clients, an erasure run removes their data from raw, parsed, chunk, vector, cache and dataset stores, and from lakehouse snapshots within the retention policy. An automated proof scans every store for their identifiers and finds none. The run produces an auditable report.
- **Quality:** recall@10 on a 150-question golden set stays within 2 points of the P2 result while all of this runs. Monitors detect each of 3 planted defects (wrong model on 5% of vectors, an ACL leak, a parser regression) within 30 minutes.
- **Dataset:** the instruction dataset is reproducible by version, has leak-free splits by case, contains no internal or redacted personal data (verified by scan), and has a complete datasheet.
- **Cost and write-up:** a cost model per 1M pages and per 1M chunks, a design document with governance and failure modes, a runbook, and a 5-minute recorded demo that includes an erasure and a permission revocation.

**Stretch goals:** a streaming re-embedding path in Flink using model functions; a comparison of pgvector, LanceDB and one dedicated vector store on the same workload; a human-reviewed synthetic question set with a measured bias analysis.

**What it proves to an employer:** you can run the data layer of an enterprise AI system: fresh, permission-correct, measurable, cost-modelled and able to forget. Few candidates can show this, and it is what the "AI data engineer" role asks for.

## Feeds into

- [DEN501 Frontier Seminar](../../year_5/DEN501_frontier_seminar_real_time_ai_data_systems/README.md): real-time AI data systems at scale.
- [OV04 MLOps and ML Platform Engineering](../../../../04_overlaps/OV04_mlops_ml_platform/README.md): datasets and evaluation in model pipelines.
- [DEN404 Data Governance, Lineage and Privacy Engineering](../DEN404_data_governance_lineage_and_privacy_engineering/README.md): erasure and access control become audited governance.
- [THS501 Thesis or Capstone I](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md): retrieval data quality and multilingual parsing are strong research topics.
