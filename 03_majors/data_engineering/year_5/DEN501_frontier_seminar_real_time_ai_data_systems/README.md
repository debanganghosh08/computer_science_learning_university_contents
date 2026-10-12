# DEN501 · Frontier Seminar: Real-Time AI Data Systems and Query Engine Internals

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 5 · 9 | 4 (≈ 120 hours) | L4 → L5 | [DEN401](../../year_4/DEN401_data_quality_observability_and_data_contracts/README.md), [DEN403](../../year_4/DEN403_data_engineering_for_ai_unstructured_data/README.md) | [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md), [THS502](../../../../05_shared_years_3_to_5/THS502_thesis_or_capstone_ii/README.md), [RES502](../../../../05_shared_years_3_to_5/RES502_reading_reproducing_and_extending_papers/README.md) |

Part of the [Data Engineering major](../../README.md). This is a research seminar. You have used Spark, Flink, DuckDB, warehouses and RAG pipelines. Here you read the papers behind them, reproduce key results, and extend one. There are two threads. The first is **query engine internals**: columnar formats, vectorised and compiled execution, composable engines, optimisers and incremental computation. The second is **real-time AI data systems**: fresh features and embeddings, streaming vector indexes, semantic operators that call language models inside query plans, and data agents. It runs alongside [RES501](../../../../05_shared_years_3_to_5/RES501_research_methods_and_scientific_writing/README.md) and [RES502](../../../../05_shared_years_3_to_5/RES502_reading_reproducing_and_extending_papers/README.md), and most students take their thesis topic from it.

## Why this course matters now

Data systems are being rebuilt from shared parts. Meta's Composable Data Management System Manifesto (VLDB 2023) argued for reusable components (Arrow for memory, Substrait for plans, Velox for execution), and Apache DataFusion (SIGMOD 2024) became a toolkit many new engines start from. At the same time, AI is being pushed into the data layer. Research systems such as LOTUS (semantic operators) and Palimpzest add language-model calls to declarative query plans. Products have followed: Flink CDC 3.7 runs model functions in pipelines, Spark 4.2 adds a `NEAREST BY` top-K join, BigQuery offers a Data Engineering Agent, and DuckDB's CLI has an agent mode (October 2026). Benchmarks show how far automation still has to go. Text-to-SQL on BIRD reached about 83% against a human 93% (September 2026), and ELT-Bench (April 2025) found that the best agent tested built only 3.9% of required data models correctly. Nobody yet knows how to make language-model operators cheap, correct and reproducible inside query plans, or how to keep vector indexes fresh under heavy updates. Those are open research questions, and this seminar trains you to work on them.

## Learning outcomes

By the end you can:

1. **Read** a systems paper critically: identify its claims, evaluation design, baselines and threats to validity, and **write** a one-page review.
2. **Reproduce** a published systems result (a benchmark figure or table) within a stated tolerance, and **explain** any gap.
3. **Explain** vectorised and compiled execution, morsel-driven parallelism and columnar memory layouts, and **implement** a small vectorised operator pipeline on Arrow arrays.
4. **Extend** a composable engine (DataFusion or DuckDB) with a new operator, function or optimiser rule, and **benchmark** it.
5. **Analyse** optimiser failures with the Join Order Benchmark, and **evaluate** a learned or adaptive technique against a classical baseline.
6. **Compare** incremental-computation models (differential dataflow, DBSP, stream processors) on correctness and cost for a real-time workload.
7. **Design and measure** a real-time AI data system (fresh features, streaming embeddings, a freshness-aware vector index, or semantic operators) under accuracy, latency and cost constraints.
8. **Write** a workshop-style paper with a reproducible artefact, and **present** it to peers.

## Chapters and lessons

### Chapter 1 · Reading and reproducing systems research (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 How to read a paper | Keshav's three-pass method; finding the claim, the mechanism and the evidence | Three-pass read of the Dremel paper; one-page review |
| 1.2 Evaluating evaluations | Baselines, workloads, hardware, warm vs cold runs, statistical treatment; benchmark pitfalls | Critique the evaluation section of a recent engine paper |
| 1.3 Reproduction | Artefacts, environment capture, tolerances, reporting failures honestly; links to [RES502](../../../../05_shared_years_3_to_5/RES502_reading_reproducing_and_extending_papers/README.md) | Pick the paper you will reproduce; write a reproduction plan |
| 1.4 The canon | The reading list below: what each paper changed and what came after | Build a citation map of 15 papers |

**Check your understanding:** (1) What is the difference between a paper's claim and its evidence? (2) Name three ways a benchmark can favour the authors' system without fraud. (3) When is a failed reproduction a contribution?

### Chapter 2 · Columnar memory and formats (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 From C-Store and X100 to Arrow | Column stores, vectorised processing, cache-conscious layouts | Read MonetDB/X100; relate each idea to Arrow |
| 2.2 Arrow in depth | Buffers, validity bitmaps, offsets, dictionary and run-end encodings, the C data interface; Arrow Flight and ADBC (dbt v2 ships ADBC-based adapters) | Implement filter and sum kernels on raw Arrow buffers; compare with Arrow's compute kernels |
| 2.3 Lightweight compression | Encodings that allow execution on compressed data; BtrBlocks (SIGMOD 2023) and cascaded encodings | Reproduce one BtrBlocks compression-ratio comparison on NYC TLC columns |
| 2.4 Newer file formats | Random access for ML workloads; Lance, Vortex and Nimble compared with Parquet; Iceberg v4 direction | Benchmark random-row access on Parquet vs Lance for an embedding table |

**Check your understanding:** (1) Why does a validity bitmap beat sentinel values for NULLs? (2) Which workloads justify a new file format over Parquet? (3) What does "execute on compressed data" require from an encoding?

### Chapter 3 · Vectorised vs compiled execution (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Compilation | Producer/consumer code generation (Neumann, VLDB 2011); pipelines and pipeline breakers | Hand-compile a 3-operator plan into one loop; compare with an iterator version |
| 3.2 Vectorisation | Batch-at-a-time primitives, selection vectors, SIMD | Implement a vectorised hash aggregation with selection vectors |
| 3.3 The comparison | "Everything you always wanted to know about compiled and vectorized queries" (Kersten et al., VLDB 2018) | Reproduce one figure's trend at small scale |
| 3.4 Parallelism | Morsel-driven parallelism (Leis et al., SIGMOD 2014), work stealing, NUMA awareness | Measure DuckDB scaling from 1 to 16 threads on TPC-H; explain the curve |

**Check your understanding:** (1) Where does each approach win, and why? (2) Why do most new engines choose vectorisation? (3) What limits parallel scaling in your measurement?

### Chapter 4 · Composable engines (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 The manifesto | Shared language front ends, plan representation (Substrait), execution libraries, memory format | Map DuckDB, DataFusion, Velox and Spark to the manifesto's layers |
| 4.2 DataFusion | Architecture, extension points (user-defined functions, table providers, optimiser rules), users | Add a custom table provider and an optimiser rule to DataFusion |
| 4.3 Velox, Photon and accelerators | Velox (VLDB 2022), Photon (SIGMOD 2022), Gluten and Comet bringing native execution under Spark | Run a TPC-H subset on Spark with and without Comet or Gluten; analyse the differences |
| 4.4 Embedded engines | DuckDB's design (SIGMOD 2019 demo) and extension model; in-process analytics in applications | Write a DuckDB extension function and benchmark it |

**Check your understanding:** (1) What does a composable stack make easier, and what does it make harder (semantics, debugging)? (2) Why does a native engine under Spark not speed up every query? (3) When is an embedded engine the right architecture for a product?

### Chapter 5 · Optimisers: why they fail and what helps (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Cardinality estimation | "How Good Are Query Optimizers, Really?" (Leis et al., VLDB 2015) and the Join Order Benchmark | Run JOB on PostgreSQL and DuckDB; find the worst estimation errors |
| 5.2 Learned and steered optimisers | Bao (SIGMOD 2021): learning to choose hints; risks of regressions | Reproduce Bao's idea in a simplified form on 20 JOB queries |
| 5.3 Adaptive execution | Runtime re-optimisation (Spark AQE), robust join algorithms | Compare static and adaptive plans on skewed data |
| 5.4 Language models and query plans | Rewriting queries with LLMs, verifying equivalence, failure modes | Have a model rewrite 20 slow queries; verify results and measure speed-ups and regressions |

**Check your understanding:** (1) Why do errors in cardinality estimates compound across joins? (2) What evidence would convince you to deploy a learned optimiser? (3) How do you verify that a rewritten query is equivalent?

### Chapter 6 · Incremental and streaming computation (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Foundations | MillWheel (2013), the Dataflow model (2015), asynchronous barrier snapshots (2015) | Write a two-page synthesis of what each paper contributed |
| 6.2 Differential dataflow | Incremental computation over collections with timestamps (McSherry et al., CIDR 2013) | Run a differential-dataflow example; measure update cost vs recomputation |
| 6.3 DBSP | Incremental view maintenance for rich query languages (Budiu et al., VLDB 2023); Feldera as an implementation | Maintain a multi-join view incrementally; compare with Flink SQL on the same stream |
| 6.4 Disaggregated state | Flink 2.0's ForSt backend; trade-offs of remote state for rescaling and cost | Measure checkpoint and rescale time with local vs remote state |

**Check your understanding:** (1) What do incremental view maintenance systems guarantee that a Flink job does not, by default? (2) Why is retraction (deleting a past contribution) central to correctness? (3) When is recomputation cheaper than incremental maintenance?

### Chapter 7 · Real-time analytics stores (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Google's designs | Procella (VLDB 2019) unifying serving and analytics at YouTube; Napa (VLDB 2021) and its freshness, cost and query-latency trade-off | Summarise Napa's tunable trade-off as a design space diagram |
| 7.2 Open-source real-time OLAP | Apache Pinot and Apache Druid: ingestion from streams, segment design, indexes; Uber's use of Pinot (SIGMOD 2021 paper) | Load a stream into Pinot; measure freshness and p99 query latency |
| 7.3 Lakehouse vs real-time stores | When a streaming lakehouse is enough; when a serving store is needed | Decide for 3 use cases with measurements |

**Check your understanding:** (1) What does Napa let a customer trade, and why is that useful? (2) Why are real-time OLAP stores often separate from the lake? (3) Which workloads break a "query the lakehouse directly" design?

### Chapter 8 · Fresh features and embeddings (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Online and offline consistency | Point-in-time correctness, training–serving skew, streaming feature computation | Measure skew between a streaming and a batch feature over a week of replayed data |
| 8.2 Vector search systems | DiskANN (NeurIPS 2019) for billion-scale search on one node; graph indexes vs quantisation | Reproduce a recall-vs-latency curve at small scale |
| 8.3 Streaming vector indexes | FreshDiskANN (2021): inserts and deletes without full rebuilds; filtered search | Measure recall degradation under a 10% daily update rate with and without consolidation |
| 8.4 Freshness as a metric | Source-to-index lag, staleness-weighted retrieval quality | Define and compute a staleness-aware retrieval metric for your DEN403 pipeline |

**Check your understanding:** (1) Why do deletes hurt graph-based vector indexes? (2) How would you measure the business cost of stale embeddings? (3) What makes training–serving skew hard to detect?

### Chapter 9 · Language models inside data systems (weeks 9–10)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Semantic operators | LOTUS's semantic filter, join and top-k operators; Palimpzest's declarative optimisation of AI workloads | Run a semantic join over judgments and statutes with LOTUS; measure accuracy, cost and time |
| 9.2 Optimising model calls | Model cascades, caching, batching, approximate filters before model calls, cost-based planning with accuracy targets | Cut a semantic query's cost by 5× while keeping accuracy within 2 points |
| 9.3 Model functions in production engines | Flink CDC model functions, LLM functions in warehouses, Spark's `NEAREST BY` join; reproducibility and versioning | Run the same enrichment in a warehouse LLM function and Flink; compare cost, latency and determinism |
| 9.4 Text-to-SQL and data agents | BIRD and Spider 2.0; ELT-Bench; agents on BigQuery and DuckDB; evaluating agents on your own schema | Build a 50-task evaluation for a data agent on your P3 platform from DEN401 or DEN404 |
| 9.5 Event-driven agents | Agents that react to streams (Flink Agents); safety, permissions, audit logs | Design an event-driven agent with an approval gate; threat-model it |

**Check your understanding:** (1) Why is a language-model filter non-deterministic, and how do you make its results reproducible? (2) What does a cost-based optimiser need to know to plan model calls? (3) Why are public text-to-SQL scores weak evidence for your company's schema?

### Chapter 10 · Data for training at scale (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Web-scale curation | FineWeb and `datatrove`: extraction, filtering, deduplication ablations | Run a small datatrove pipeline over one Common Crawl segment |
| 10.2 Deduplication at scale | Exact and MinHash deduplication, suffix-array methods (Lee et al., 2021) | Compare two dedup methods on the same corpus slice |
| 10.3 Synthetic data and collapse | Recursive training and model collapse (*Nature*, 2024); mixing and filtering | Write a critical review of one synthetic-data paper |

**Check your understanding:** (1) Why did FineWeb rely on training ablations rather than heuristics alone? (2) What is the systems bottleneck in deduplicating trillions of tokens? (3) What would convince you that a synthetic-data method avoids collapse?

### Chapter 11 · Research project (weeks 12–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Reproduction report | Presenting a reproduction: setup, results, gaps, lessons | Submit the reproduction (P2) |
| 11.2 Extension | Turning a gap into a hypothesis and an experiment | Run the extension experiments for P3 |
| 11.3 Writing | Workshop-paper structure, figures that make one point, threats to validity | Draft, peer review, revise |
| 11.4 Presenting | 15-minute talk with questions | Seminar presentation |

**Check your understanding:** (1) What is your paper's one claim, and which figure supports it? (2) What would a sceptical reviewer attack first? (3) Is your artefact runnable by a stranger in one hour?

## Weekly rhythm

| Week | Chapter | Seminar and lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Reading method; Dremel review | Review 1; reproduction plan |
| 2 | 2 | Arrow kernels; BtrBlocks | Kernel benchmark |
| 3 | 3 | Compiled vs vectorised | Hand-compiled plan; **P1 due** |
| 4 | 4 | DataFusion extension | Extension with benchmark |
| 5 | 5 | Join Order Benchmark | Estimation-error report |
| 6 | 6 | Differential dataflow and DBSP | Incremental-view comparison |
| 7 | 7 | Real-time OLAP | Pinot freshness study; mid-term oral (AI off) |
| 8 | 8 | Streaming vector indexes | Recall-under-updates study |
| 9 | 9 | Semantic operators | Cost–accuracy study |
| 10 | 9 | Data agents | Agent evaluation set; **P2 due** |
| 11 | 10 | Training-data curation | datatrove run and review |
| 12 | 11 | Project work | Extension results |
| 13 | 11 | Peer review | Paper draft |
| 14 | 11 | Presentations | **P3 due** |
| 15 | Review | Oral examination on the reading list | Final oral (AI off) |

## Working with AI in this course

- **Use AI for:** explaining unfamiliar notation and background in papers; finding related work (then verifying each citation exists and says what is claimed); scaffolding benchmark harnesses and plotting code; drafting extension code for DataFusion or DuckDB; checking your writing for clarity. Tools: Claude Code, GitHub Copilot, Cursor; DuckDB's CLI agent mode and the DuckDB skills for Claude Code; research search tools.
- **Do without AI (drills):** the three-pass reading and the written reviews; the oral mid-term and final on the reading list; deriving why a technique works from first principles. Research judgement comes from your own reading.
- **Verify AI output by:** (1) opening every cited paper and checking the claim on its page; (2) re-running every benchmark the assistant scaffolded, with your own statistical treatment; (3) differential testing of any engine extension against an existing implementation; (4) reading every line of any code included in your artefact.
- **Where AI still fails here (show it yourself):** keep a log of citations suggested by an assistant during the course and record how many were wrong, misattributed or non-existent. When an assistant summarises a paper's results, compare its numbers with the paper's tables. These errors are why every reference in your paper must be checked by hand.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Weekly reviews and labs | 20% |
| P1 (review and mini-reproduction) | 10% |
| P2 (full reproduction) | 20% |
| P3 (extension paper and artefact) | 30% |
| Oral mid-term and final on the reading list (AI off) | 20% |

**Mastery gate.** You pass when you can: (1) reproduce a published systems result within a stated tolerance, or document precisely why it cannot be reproduced; (2) present an extension with a clear hypothesis, a fair baseline and a runnable artefact that a peer can rerun in under an hour; (3) answer, without notes or AI, questions on any five papers from the reading list: what problem, what mechanism, what evidence, what came next.

## Industry reality

The ideas in this seminar are in production systems: vectorised execution in DuckDB, Photon and Velox; Arrow as the memory format across engines and clients; incremental view maintenance in streaming databases; graph-based vector indexes; and language-model functions in warehouses and stream processors. Engine companies, cloud data platforms and AI labs hire engineers who can read these papers and build on them. The same skills also suit a founder, since many recent data-infrastructure companies began as one paper's idea turned into a product.

**Interview questions from this course**

1. *"Why are modern analytical engines vectorised?"* A strong answer covers interpretation overhead per tuple, cache and SIMD efficiency, the comparison with compiled execution (Kersten et al.), and engineering trade-offs (debuggability, portability).
2. *"Our query optimiser picks terrible join orders on some queries. What do you do?"* Cover cardinality estimation errors and how they compound, statistics and sampling, hints, adaptive execution, learned steering such as Bao, and how to evaluate any change without regressions.
3. *"How would you keep a vector index fresh with 10% of documents changing daily?"* Cover streaming insert and delete support, consolidation, recall monitoring under updates, freshness metrics, and when to rebuild.
4. *"How would you add language-model filtering to SQL queries without making them slow and expensive?"* Cover cheap pre-filters, model cascades, caching and batching, accuracy targets, cost-based planning, and reproducibility through pinned model versions.
5. *"Tell me about a paper you reproduced."* Cover what was claimed, your setup, what matched, what did not and why, and what you would do next.

## Resources (free first)

**Reading list** (core papers; most are free):

- *Foundations:* [MapReduce](https://static.googleusercontent.com/media/research.google.com/en//archive/mapreduce-osdi04.pdf) (2004); [GFS](https://static.googleusercontent.com/media/research.google.com/en//archive/gfs-sosp2003.pdf) (2003); [C-Store](https://web.stanford.edu/class/cs345d-01/rl/cstore.pdf) (2005); [MonetDB/X100](https://www.cidrdb.org/cidr2005/papers/P19.pdf) (2005); [Dremel](https://research.google/pubs/dremel-interactive-analysis-of-web-scale-datasets-2/) (2010) and [Dremel: a decade](https://www.vldb.org/pvldb/vol13/p3461-melnik.pdf) (2020); [Kafka](https://notes.stephenholiday.com/Kafka.pdf) (2011); [Spark RDDs](https://www.usenix.org/conference/nsdi12/technical-sessions/presentation/zaharia) (2012); [Spark SQL](https://people.csail.mit.edu/matei/papers/2015/sigmod_spark_sql.pdf) (2015).
- *Execution and optimisation:* [Efficiently Compiling Efficient Query Plans](https://www.vldb.org/pvldb/vol4/p539-neumann.pdf) (2011); [Morsel-Driven Parallelism](https://db.in.tum.de/~leis/papers/morsels.pdf) (2014); [How Good Are Query Optimizers, Really?](https://www.vldb.org/pvldb/vol9/p204-leis.pdf) (2015); [Compiled vs vectorized](https://www.vldb.org/pvldb/vol11/p2209-kersten.pdf) (2018); [Bao](https://arxiv.org/abs/2004.03814) (2021); [DuckDB](https://duckdb.org/pdf/SIGMOD2019-demo-duckdb.pdf) (2019); [Velox](https://www.vldb.org/pvldb/vol15/p3372-pedreira.pdf) (2022); [Photon](https://people.eecs.berkeley.edu/~matei/papers/2022/sigmod_photon.pdf) (2022); [Composable Data Management System Manifesto](https://www.vldb.org/pvldb/vol16/p2679-pedreira.pdf) (2023); [Apache DataFusion](https://andrew.nerdnetworks.org/pdf/SIGMOD-2024-lamb.pdf) (2024).
- *Storage and lakehouses:* [Delta Lake](https://www.vldb.org/pvldb/vol13/p3411-armbrust.pdf) (2020); [Lakehouse](https://www.cidrdb.org/cidr2021/papers/cidr2021_paper17.pdf) (2021); [Analyzing and Comparing Lakehouse Storage Systems](https://www.cidrdb.org/cidr2023/papers/p92-jain.pdf) (2023); [Snowflake](https://dl.acm.org/doi/10.1145/2882903.2903741) (2016); [Iceberg spec](https://iceberg.apache.org/spec/); BtrBlocks ([code](https://github.com/maxi-k/btrblocks), SIGMOD 2023).
- *Streaming and incremental:* [MillWheel](https://research.google/pubs/millwheel-fault-tolerant-stream-processing-at-internet-scale/) (2013); [Differential Dataflow](https://www.cidrdb.org/cidr2013/Papers/CIDR13_Paper111.pdf) (2013); [Dataflow Model](https://www.vldb.org/pvldb/vol8/p1792-Akidau.pdf) (2015); [Asynchronous barrier snapshots](https://arxiv.org/abs/1506.08603) (2015); [DBSP](https://www.vldb.org/pvldb/vol16/p1601-budiu.pdf) (2023).
- *Real-time analytics:* [Procella](https://www.vldb.org/pvldb/vol12/p2022-chattopadhyay.pdf) (2019); [Napa](https://www.vldb.org/pvldb/vol14/p2986-sankaranarayanan.pdf) (2021); [Real-time Data Infrastructure at Uber](https://arxiv.org/abs/2104.00087) (2021).
- *AI data systems:* [DiskANN](https://papers.nips.cc/paper/2019/hash/09853c7fb1d3f8ee67a61b6bf4a7f8e6-Abstract.html) (2019); [FreshDiskANN](https://arxiv.org/abs/2105.09613) (2021); [Semantic Operators / LOTUS](https://arxiv.org/abs/2407.11418); [Palimpzest](https://arxiv.org/abs/2405.14696); [ELT-Bench](https://arxiv.org/abs/2504.04808) (2025); [FineWeb](https://arxiv.org/abs/2406.17557) (2024); [Deduplicating Training Data](https://arxiv.org/abs/2107.06499) (2021); [Model collapse](https://www.nature.com/articles/s41586-024-07566-y) (2024).
- **Method:** S. Keshav, ["How to Read a Paper"](https://web.stanford.edu/class/ee384m/Handouts/HowtoReadPaper.pdf).
- **Courses:** [CMU 15-721 Advanced Database Systems](https://15721.courses.cs.cmu.edu/spring2024/) (Spring 2024 materials) and [Fall 2025](https://www.cs.cmu.edu/~15721-f25/).
- **Code to read and extend:** [Apache DataFusion](https://datafusion.apache.org/); [DuckDB](https://duckdb.org/docs/stable/); [Apache Arrow](https://arrow.apache.org/docs/format/Columnar.html) and [ADBC](https://arrow.apache.org/adbc/); [Substrait](https://substrait.io/); [Feldera](https://github.com/feldera/feldera); [Vortex](https://github.com/vortex-data/vortex); [Nimble](https://github.com/facebookincubator/nimble); [Lance](https://github.com/lance-format/lance); [Apache Pinot](https://pinot.apache.org/); [Apache Druid](https://druid.apache.org/).

## Sources

All checked October 2026.

- Pedreira et al., "The Composable Data Management System Manifesto" (PVLDB 16, 2023). https://www.vldb.org/pvldb/vol16/p2679-pedreira.pdf
- Lamb et al., "Apache Arrow DataFusion: A Fast, Embeddable, Modular Analytic Query Engine" (SIGMOD 2024). https://andrew.nerdnetworks.org/pdf/SIGMOD-2024-lamb.pdf
- "Semantic Operators: A Declarative Model for Rich, AI-based Data Processing" (LOTUS; arXiv 2407.11418) and "A Declarative System for Optimizing AI Workloads" (Palimpzest; arXiv 2405.14696). https://arxiv.org/abs/2407.11418 ; https://arxiv.org/abs/2405.14696
- BIRD leaderboard (≈ 82.95% top, 7 Sep 2026; human 92.96%). https://bird-bench.github.io/
- Jin, Zhu and Kang, ELT-Bench (arXiv 2504.04808, Apr 2025): best agent 3.9% of data models correct. https://arxiv.org/abs/2504.04808
- Apache Flink posts (Flink CDC 3.7.0, 10 Oct 2026; Flink Agents). https://flink.apache.org/posts/
- Apache Spark 4.2.0 release notes. https://spark.apache.org/releases/spark-release-4-2-0.html
- DuckDB news ("Agent Mode in the DuckDB CLI", 9 Oct 2026; "DuckDB Skills for Claude Code", 16 Sep 2026). https://duckdb.org/news/
- dbt, "Upgrading to v2" (ADBC-based adapters). https://docs.getdbt.com/docs/dbt-versions/dbt-upgrade/upgrading-to-v2

_Last reviewed: 2026-10_
