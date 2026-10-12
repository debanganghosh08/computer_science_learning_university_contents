# DEN501 · Labs and projects

This is a seminar, so the labs are short experiments tied to each week's papers. The projects form one research arc: review, reproduce, extend. Hardware: a laptop with 16 GB of RAM is enough for every lab at the stated scales. P2 and P3 may use a small cloud budget or a university cluster. Every lab result needs a fixed environment (container or lock file), a seed where randomness is involved, and at least 3 runs.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Three-pass review | Review the Dremel paper with Keshav's method | One-page review: claim, mechanism, evidence, weaknesses | 3 h |
| 2 · Arrow kernels | Filter and sum kernels on raw Arrow buffers, with and without selection vectors; compare with Arrow compute | Code and benchmark at 3 data sizes | 5 h |
| 3 · Compiled vs vectorised | Hand-compile a scan–filter–aggregate pipeline; implement a vectorised version; compare | Timings, profiler output and an explanation of the gap | 5 h |
| 4 · DataFusion extension | Add a table provider and an optimiser rule (for example, a predicate rewrite) | Code, tests and a before/after benchmark | 6 h |
| 5 · Join Order Benchmark | Run JOB on PostgreSQL and DuckDB; find the worst cardinality errors and their plans | Error distribution plot and 3 annotated plans | 5 h |
| 6 · Incremental views | Maintain a multi-join view with DBSP (Feldera) and with Flink SQL; apply inserts, updates and deletes | Correctness check against batch and update-cost comparison | 6 h |
| 7 · Real-time OLAP | Stream events into Apache Pinot; measure freshness and p99 latency under load | Freshness–latency curve | 4 h |
| 8 · Vector index under updates | Measure recall@10 for a graph index under 10% daily inserts and deletes, with and without consolidation | Recall-over-time plot | 5 h |
| 9 · Semantic operators | Run a semantic filter and join with LOTUS; optimise cost with cascades and caching | Accuracy, cost and latency table | 6 h |
| 10 · Data-agent evaluation | Build 50 tasks with checkable answers on your own platform; evaluate one data agent | Task set, scores and failure taxonomy | 5 h |
| 11 · Curation pipeline | Run a small `datatrove` pipeline on one Common Crawl segment; measure what each filter removes | Pipeline config and removal statistics | 4 h |

## Projects

### P1 · Critical review and mini-reproduction (L1, ~6 hours)

**Real-world inspiration:** engineering teams evaluate new engines and techniques from papers and vendor posts. A short, honest reproduction is the fastest way to know whether a claim holds for your hardware and data.

**What to build:** choose one paper from the reading list. Write a 2-page critical review: the problem, the mechanism, the evaluation and its threats to validity. Then reproduce one small, self-contained result from it. For example: one compression-ratio comparison from BtrBlocks, one figure's trend from the compiled-vs-vectorised study, or one recall–latency point from DiskANN at reduced scale.

**Acceptance criteria:**
- The review states the paper's central claim in one sentence and identifies at least 2 threats to validity, with reasons.
- The reproduction includes the exact environment, data and commands, and runs end to end from a clean checkout.
- Results are compared with the paper's numbers. Any difference beyond a stated tolerance is explained or reported as unexplained.

**Stretch goals:** run the same experiment on a second hardware platform (laptop vs cloud ARM instance) and explain the differences.

**What it proves to an employer:** you can evaluate technical claims with evidence instead of repeating them.

### P2 · Full reproduction of a systems result (L2, ~15 hours)

**Real-world inspiration:** reproducibility efforts in the database and systems communities (artefact evaluation at major conferences) exist because many results are hard to rerun. Reproducing a result is also the best way to understand a system deeply enough to extend it.

**What to build:** a full reproduction of one main result (a key table or figure) from a paper agreed with the instructor. Suggested options:

- the Join Order Benchmark cardinality-error analysis on current PostgreSQL and DuckDB;
- FreshDiskANN's recall under streaming updates at reduced scale;
- a DBSP incremental-maintenance experiment;
- a semantic-operator cost–accuracy result from LOTUS or Palimpzest, on Indian court judgments instead of the original data.

**Acceptance criteria:**
- **Artefact:** a container or lock-file environment that a peer reruns in under 1 hour (or with a documented subsampled mode), verified by an assigned peer.
- **Result:** the reproduced table or figure sits side by side with the original. Differences are quantified, and each is attributed to a specific cause (hardware, versions, data, unstated parameters) or marked unexplained.
- **Statistics:** at least 3 runs per point, with variance reported.
- **Report:** 4–6 pages in workshop format, including a section on what the authors did not report that you needed.

**Stretch goals:** contact the authors with specific questions and record the answers; contribute a fix or documentation to the original artefact.

**What it proves to an employer:** you can understand a complex system well enough to rebuild its key result and to say exactly where it differs.

### P3 · Extension paper with artefact (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** many data-infrastructure features and companies began as one research idea tested carefully. Open-source engines like DataFusion and DuckDB accept extensions from contributors who can show a measured benefit.

**What to build:** extend your P2 system, or another approved system, with one new idea. Test it against a fair baseline and write it up as a workshop paper. Example directions:

- a staleness-aware consolidation policy for a streaming vector index, evaluated on the DEN403 judgments corpus;
- a cost-based planner rule for semantic operators that orders cheap filters before model calls, with accuracy targets;
- a DataFusion or DuckDB optimiser rule for a pattern from your DEN301 or DEN302 workloads;
- incremental maintenance of a retrieval-quality metric as documents change;
- an evaluation harness for data agents on lakehouse tasks (multi-step pipelines, not single queries).

**Acceptance criteria:**
- **Hypothesis:** one falsifiable hypothesis stated before experiments, recorded in the repository history.
- **Baseline:** at least one strong baseline (the unmodified system or the best published alternative), tuned with the same effort as your method.
- **Evidence:** results on at least 2 datasets or workloads, with variance. A negative or mixed result is acceptable if analysed honestly.
- **Artefact:** code, data scripts and environment that an external reader can rerun in under 1 hour in a reduced mode. A peer verifies this.
- **Paper:** 6–8 pages in a standard two-column workshop format: problem, related work (every citation checked by hand), design, evaluation, limitations, and an AI-use statement describing what tools were used for and how outputs were verified.
- **Talk:** a 15-minute presentation with questions.
- **Upstream (preferred):** a pull request or issue to the relevant open-source project, linked in the paper.

**Stretch goals:** submit to a student research workshop or a database conference demo track; turn the artefact into the starting point for [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md).

**What it proves to an employer or a graduate programme:** you can create new knowledge in data systems, test it rigorously, and share it in a form others can rerun. This is the L5 mastery level.

## Feeds into

- [THS501 Thesis or Capstone I](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) and [THS502 Thesis or Capstone II](../../../../05_shared_years_3_to_5/THS502_thesis_or_capstone_ii/README.md): P3 is designed to become a thesis proposal.
- [RES502 Reading, Reproducing and Extending Papers](../../../../05_shared_years_3_to_5/RES502_reading_reproducing_and_extending_papers/README.md): P2 doubles as its reproduction exercise.
- [LCH502 Career Launch and Founder Studio](../../../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md): a strong artefact can become an open-source project or a product.
