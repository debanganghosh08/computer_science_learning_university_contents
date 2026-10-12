# CS211 · Database Systems Internals

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 2 · 4 | 4 (≈ 120 hours) | L1 → L3 | [FND115](../../../01_year_1_foundations/semester_2/FND115_databases_i_data_modeling_and_sql/README.md), [CS201](../../semester_3/CS201_algorithms_and_complexity/README.md) | [BE303](../../../03_majors/backend_engineering/year_3/BE303_data_modeling_and_storage_for_backends_postgres/README.md), [BE402](../../../03_majors/backend_engineering/year_4/BE402_scalability_and_performance_caching_sharding/README.md), [DEN301](../../../03_majors/data_engineering/year_3/DEN301_data_modeling_and_warehousing/README.md), [DEN305](../../../03_majors/data_engineering/year_3/DEN305_lakehouse_architecture_parquet_iceberg_and_delta/README.md), [CLD305](../../../03_majors/cloud_engineering/year_3/CLD305_cloud_storage_and_managed_databases/README.md), [CSG303](../../../03_majors/computer_science_general/year_3/CSG303_distributed_systems_ii_consensus_replication/README.md) |

Part of [Year 2 · Core Computer Science](../../README.md). Runs alongside [CS212 Distributed Systems I](../CS212_distributed_systems_i/README.md), which picks up replication and consensus where Chapter 10 stops.

## Why this course matters now

Almost every product failure that reaches the news involves data that was lost, duplicated, inconsistent or slow. The engineers who fix those failures understand what sits under SQL: pages, buffer pools, B+trees, write-ahead logs and MVCC. Public write-ups show what this looks like in practice. Uber left PostgreSQL in 2016 over write amplification and replication traffic caused by its tuple-versioning design. Notion split PostgreSQL into 480 logical shards in 2021 after vacuum and transaction-ID wraparound pain. Zerodha runs about 20 TB on sharded PostgreSQL with hand-scheduled vacuuming. AI tools now write much of the SQL: the best system on the BIRD text-to-SQL benchmark reached about 83% execution accuracy in September 2026, against a human baseline of about 93%. So roughly one generated query in six is still wrong on a curated benchmark, and a person has to know why. CMU's 15-445 (Fall 2026) bans coding agents on its buffer-pool and index projects for the same reason: you cannot judge generated database code until you have built the core pieces yourself.

## Learning outcomes

By the end you can:

1. **Implement** a slotted-page heap file, a buffer pool with a replacement policy, and a concurrent B+tree, all passing differential and crash tests.
2. **Explain why** a B+tree of height 3–4 can index billions of rows, and **calculate** the I/O cost of a lookup, a range scan and an index build.
3. **Compare** B+trees and LSM trees by read, write and space amplification, and **choose** one for a stated workload.
4. **Implement** external merge sort, hash join and a Volcano-style iterator executor, and **measure** their I/O counts.
5. **Read** a PostgreSQL `EXPLAIN (ANALYZE, BUFFERS)` plan, find where estimates diverge from reality, and fix the cause.
6. **Reproduce** lost updates, write skew and phantom reads under named isolation levels, and **explain** how 2PL, OCC, timestamp ordering and MVCC prevent or allow each.
7. **Trace** ARIES recovery (analysis, redo, undo) on a given log by hand, and **implement** a WAL that survives `kill -9`.
8. **Design** a partitioning and replication scheme for a stated workload, **explain** what two-phase commit costs, and **verify** AI-generated SQL and storage code with plans, tests and invariants.

## Chapters and lessons

### Chapter 1 · Architecture and the storage hierarchy (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Anatomy of a DBMS | Process model, query parser, planner, executor, access methods, buffer manager, lock and log managers (Hellerstein, Stonebraker and Hamilton's *Architecture of a Database System*) | Map each component to a PostgreSQL backend process and a SQLite module |
| 1.2 The storage hierarchy | Latency from CPU cache to DRAM to NVMe SSD to network storage; why random I/O dominates; block devices and 4 KB sectors | Measure sequential vs random 4 KB reads on your own machine with a 50-line C or Rust program |
| 1.3 Why the DBMS manages its own memory | `mmap` vs a user-space buffer pool; page-fault stalls, write ordering and the case against `mmap` | Write a one-page argument for or against `mmap` for a KV store, with two failure cases |
| 1.4 SQLite as a whole system | Tokenizer, parser, code generator, bytecode VM, B-tree, pager, VFS (sqlite.org architecture page) | Run `EXPLAIN` on three SQLite queries and annotate the bytecode |

**Check your understanding:** (1) Why can't a DBMS simply trust the OS page cache to decide what to write back, and when? (2) A disk does 500 MB/s sequential and 50k random 4 KB reads/s: which is faster for reading 20% of a 10 GB table, a full scan or index lookups? Show the arithmetic. (3) Which SQLite layer would you change to store data in object storage instead of a local file?

### Chapter 2 · Pages, tuples and storage models (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Heap files and page directories | Pages, page IDs, free-space maps, heap vs sorted vs hashed files | Design the page directory for a 100 GB table and size it |
| 2.2 Slotted pages | Header, slot array, tuple offsets, compaction, record IDs; PostgreSQL's 8 kB page layout and line pointers | Implement a slotted page with insert, delete, update and compaction (Lab 1) |
| 2.3 Tuple layout | Null bitmaps, fixed vs variable-length fields, alignment padding, large values (PostgreSQL TOAST, SQLite overflow pages) | Measure bytes lost to padding in a table, then reorder columns and remeasure |
| 2.4 Row, column and hybrid storage | NSM vs DSM vs PAX; why analytics engines (DuckDB, Parquet) store columns | Run the same aggregate on a row store (SQLite) and a column store (DuckDB); explain the gap |
| 2.5 Compression | Dictionary, run-length, delta and bit-packing; late materialization | Compress a column of Indian PIN codes three ways and compare ratios |

**Check your understanding:** (1) Why do slotted pages use indirection through a slot array rather than storing tuple pointers directly in indexes? (2) When does a column store lose to a row store? (3) What breaks if you update a variable-length field in place and it grows?

### Chapter 3 · Buffer pool management (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Frames, page table, pin counts | Page table vs page directory, dirty bits, pin/unpin protocol, latches on the page table | Implement `FetchPage`, `UnpinPage`, `FlushPage` (Lab 2) |
| 3.2 Replacement policies | LRU, CLOCK, LRU-K, 2Q, ARC; sequential flooding | Replay a trace with a full scan mixed into point lookups and compare hit rates |
| 3.3 Buffer pool optimizations | Multiple pools, prefetching, scan sharing, buffer-pool bypass, `O_DIRECT` | Add prefetch for sequential scans and measure the change |
| 3.4 Asynchronous I/O | Why PostgreSQL 18 (Sept 2025) added an async I/O subsystem; `io_uring` in outline | Read the PostgreSQL 18 release notes and list which operations use AIO |

**Check your understanding:** (1) Why can a pinned page never be evicted, and what goes wrong if a caller forgets to unpin? (2) Why does LRU perform badly for a nightly report that scans a large table? (3) When is it safe to write a dirty page to disk? (Answer again after Chapter 9.)

### Chapter 4 · Hash tables and B+trees (weeks 4–5)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Disk-oriented hash tables | Linear probing, cuckoo hashing, extendible and linear hashing, directory doubling | Implement extendible hashing with a bucket split |
| 4.2 B+tree structure | Fanout, invariants, leaf chaining, height bound, clustered vs secondary indexes | Compute the height of a B+tree for 2 billion keys with 8 kB pages and 16-byte entries |
| 4.3 Insert, delete, split, merge | Splits, redistribution, merges, fill factor, bulk loading bottom-up | Implement insert, delete and range scan; fuzz against an in-memory sorted map (Lab 3) |
| 4.4 Index design in practice | Composite keys and column order, covering indexes, index-only scans, partial and expression indexes, prefix compression | Pick indexes for five queries on a 10-million-row orders table and justify the column order |
| 4.5 Index concurrency | Latches vs locks; latch crabbing, optimistic latch coupling, B-link trees | Make your B+tree thread-safe and run it under ThreadSanitizer with 16 threads |

**Check your understanding:** (1) Why is the key order in a composite index `(city, created_at)` not interchangeable? (2) Why must latch crabbing release ancestors only when a child is "safe"? (3) Bulk loading builds the tree bottom-up: why is it faster, and what fill factor would you choose for a table that will receive many inserts later?

### Chapter 5 · LSM trees and write-optimized storage (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 The log-structured merge tree | Memtable, WAL, immutable SSTables, flush (O'Neil et al., 1996) | Sketch the write path of RocksDB from `Put` to an L0 file |
| 5.2 Compaction | Leveled vs tiered (size-tiered) compaction; write stalls; RocksDB's leveled design | Simulate both strategies on a write-heavy trace and plot write amplification |
| 5.3 Read path and filters | Bloom filters, false-positive rate maths, block indexes, block cache | Derive the bits per key for a 1% false-positive rate and check it empirically |
| 5.4 Amplification trade-offs | Read, write and space amplification; why no structure wins all three | Fill a table: B+tree vs LSM for a ledger, a metrics store and a product catalogue |
| 5.5 Indexes beyond the classics | Skip lists, tries and adaptive radix trees, inverted indexes, vector indexes (HNSW and IVFFlat in pgvector) | Build an HNSW index with pgvector on 100k embeddings and measure recall vs latency |

**Check your understanding:** (1) Why do LSM engines need bloom filters more than B+tree engines do? (2) Discord moved message storage from Cassandra to ScyllaDB (both LSM-based) and cut nodes from 177 to 72: what in the storage engine could and could not explain that? (3) What happens to read latency during a large compaction, and how would you limit it?

### Chapter 6 · Query execution (weeks 7–8)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Processing models | Volcano iterator, materialization, vectorized (MonetDB/X100, DuckDB), push vs pull | Implement scan, filter, projection and limit as iterators (Lab 4) |
| 6.2 Sorting and aggregation | External merge sort, run generation, k-way merge, hash aggregation with spilling | Sort 4 GB with 256 MB of memory; count passes and I/Os |
| 6.3 Join algorithms | Nested-loop, block nested-loop, index nested-loop, sort-merge, grace hash join; cost formulas | Implement hash join and sort-merge join; compare against the cost model |
| 6.4 Parallel execution | Intra-operator (exchange operators) vs inter-operator parallelism; NUMA effects | Parallelize your hash join across 4 threads and measure speed-up |
| 6.5 Query compilation | Interpretation vs code generation (HyPer-style) vs vectorization trade-offs | Read DuckDB's execution docs and explain why it chose vectorization |

**Check your understanding:** (1) Why does grace hash join partition both inputs before building? (2) When is a nested-loop join the best choice? (3) A vectorized engine processes 2,048 values per call: what overhead does this remove compared with tuple-at-a-time?

### Chapter 7 · Query planning and optimization (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Rewrites | Predicate pushdown, projection pruning, subquery decorrelation, view inlining | Rewrite three correlated subqueries by hand and verify identical results |
| 7.2 Cardinality estimation | Histograms, most-common values, independence assumption, sampling; why estimates go wrong on correlated columns | Find a PostgreSQL query where estimated rows differ from actual by 100×; fix it with extended statistics |
| 7.3 Cost-based join ordering | System R dynamic programming, left-deep plans, interesting orders (Selinger et al., 1979); Cascades/top-down search | Enumerate join orders for a 4-table query by hand, then compare with PostgreSQL's choice |
| 7.4 Reading real plans | `EXPLAIN (ANALYZE, BUFFERS)`, loops, rows removed by filter, shared hit vs read | Lab 5: diagnose and fix ten slow queries |

**Check your understanding:** (1) Why does the independence assumption underestimate rows for `city = 'Bengaluru' AND state = 'Karnataka'`? (2) Why do optimizers often restrict themselves to left-deep trees? (3) A plan was fast yesterday and slow today with no code change: list four causes.

### Chapter 8 · Transactions and concurrency control (weeks 10–11)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 ACID and serializability | Schedules, conflict serializability, precedence graphs, view serializability | Test five schedules for conflict serializability |
| 8.2 Two-phase locking | Basic and strict 2PL, lock granularity and intention locks, deadlock detection vs prevention (wait-die, wound-wait) | Build a lock manager with deadlock detection (Lab 6) |
| 8.3 Timestamp ordering and OCC | Basic T/O, Thomas write rule, optimistic read/validate/write phases | Compare abort rates of 2PL and OCC under high and low contention |
| 8.4 MVCC | Version chains (append-only, time-travel, delta), snapshots, garbage collection; PostgreSQL `xmin`/`xmax`, InnoDB undo logs | Inspect tuple versions in PostgreSQL with the `pageinspect` extension |
| 8.5 Isolation levels in real systems | Anomalies (dirty read, lost update, write skew, phantom); snapshot isolation; PostgreSQL's serializable snapshot isolation | Reproduce write skew under `REPEATABLE READ`, then prevent it under `SERIALIZABLE` (Lab 7) |
| 8.6 Application-level correctness | `SELECT … FOR UPDATE`, optimistic version columns, idempotency keys for payments | Fix a double-spend bug in a wallet service three ways |

**Check your understanding:** (1) Why does snapshot isolation allow write skew but not lost updates (in PostgreSQL)? (2) Why does MVCC need vacuum or garbage collection, and what does transaction-ID wraparound force PostgreSQL to do? (3) Jepsen found Amazon RDS for PostgreSQL 17.4 multi-AZ clusters showing "long fork": what does that anomaly mean for a reader?

### Chapter 9 · Logging and recovery (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Failure model and buffer policies | Transaction, system and media failures; steal/no-steal, force/no-force | Explain why steal plus no-force needs both undo and redo |
| 9.2 Write-ahead logging | Log records, LSNs, pageLSN, flushedLSN, group commit, `fsync`; PostgreSQL WAL internals | Implement a WAL with group commit and measure commits/second vs batch size (Lab 8) |
| 9.3 Checkpoints | Consistent vs fuzzy checkpoints; dirty page table and transaction table | Add fuzzy checkpoints and measure recovery time vs checkpoint interval |
| 9.4 ARIES | Analysis, redo (repeating history), undo with compensation log records (Mohan et al., 1992) | Recover a 30-record log by hand, then in code |
| 9.5 Shadow paging and alternatives | SQLite rollback journal vs WAL mode; copy-on-write B-trees (LMDB) | Compare SQLite journal modes under a crash test |

**Check your understanding:** (1) Why does ARIES redo the work of transactions that later abort? (2) What exactly must be on disk before `COMMIT` returns, and what does PostgreSQL's `synchronous_commit = off` trade away? (3) Why do compensation log records make recovery safe if the system crashes during recovery?

### Chapter 10 · Distributed databases and choosing an engine (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Architectures | Shared-nothing, shared-disk, disaggregated storage (Aurora-style log-is-the-database) | Draw the write path of a shared-nothing and a disaggregated design |
| 10.2 Partitioning | Hash, range and directory partitioning; hot keys; resharding; Notion's 480 logical shards on 32 machines | Design a sharding key for a food-delivery orders table and list the cross-shard queries |
| 10.3 Replication | Primary-replica, synchronous vs asynchronous, logical vs physical (streaming) replication, read-your-writes | Set up PostgreSQL streaming replication in containers and measure lag under load |
| 10.4 Distributed transactions | Two-phase commit, blocking on coordinator failure, Spanner and Calvin in outline | Implement 2PC with a crashable coordinator (Lab 9) |
| 10.5 Choosing and operating an engine | OLTP vs OLAP vs HTAP engines; vacuum, bloat, connection pooling, point-in-time recovery | Write a one-page engine decision record for a stated workload |

**Check your understanding:** (1) Why can 2PC block forever, and what does CS212's consensus add? (2) Uber cited write amplification from secondary indexes as a reason to leave PostgreSQL in 2016: explain the mechanism from Chapters 2 and 8. (3) When is SQLite the right production database?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 0: storage microbenchmark | Latency table for your machine |
| 2 | 2 | Lab 1: slotted page | Page passing unit and fuzz tests |
| 3 | 3 | Lab 2: buffer pool | Buffer pool, hit-rate report (no coding agents) |
| 4 | 4 | Lab 3: B+tree (part 1) | Insert and search; P1 due |
| 5 | 4 | Lab 3: B+tree (part 2) | Delete, range scan, concurrency (no coding agents) |
| 6 | 5 | LSM simulation | Write-amplification plot; P2 starts |
| 7 | 6 | Lab 4: executor | Iterators, sort |
| 8 | 6 | Lab 4 cont. | Hash and sort-merge join, I/O counts |
| 9 | 7 | Lab 5: plan clinic | Ten diagnosed queries; P2 due |
| 10 | 8 | Lab 6: lock manager | Deadlock detection; P3 design review |
| 11 | 8 | Lab 7: anomalies | Reproduction scripts |
| 12 | 9 | Lab 8: WAL and recovery | Crash-test report |
| 13 | 10 | Lab 9: 2PC | Failure-injection log |
| 14 | 10 | P3 integration | P3 demo and write-up |
| 15 | Review and exam | — | Written exam, oral code walkthrough |

## Working with AI in this course

- **Use AI for:** explaining unfamiliar plan nodes and PostgreSQL internals pages; generating synthetic datasets and skewed workloads; writing test harnesses (fuzzers that compare your B+tree with a sorted map, crash-injection loops); reviewing your design docs; drafting SQL that you then verify.
- **Do without AI (drills):** the slotted page, buffer pool and B+tree labs (CMU 15-445 bans coding agents on its buffer-pool and index projects in Fall 2026); computing B+tree heights, join costs and sort passes on paper; tracing ARIES by hand; drawing version chains for a given schedule.
- **Verify AI output by:** differential testing against SQLite, DuckDB or an in-memory map; running every generated query through `EXPLAIN (ANALYZE, BUFFERS)` on realistic data volumes, not 10 rows; checking invariants after crash injection (sum of balances, no duplicate IDs); reproducing any claimed isolation behavior in two `psql` sessions before you believe it.
- **Where AI still fails here:** text-to-SQL is not solved: the top BIRD system was at about 83% execution accuracy in September 2026, below the human baseline. You can see the rest yourself. Ask an assistant whether a schedule is safe under `REPEATABLE READ` in PostgreSQL vs MySQL, then test it; ask it to write latch crabbing, then run ThreadSanitizer. Record every disagreement in your lab notes. Answers that sound right but miss engine-specific semantics are the main failure to learn to catch.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs 0–9 (autograded tests plus short write-ups) | 30% |
| Projects P1 / P2 / P3 | 5% / 12% / 18% |
| Written exam (cost calculations, schedules, recovery traces) | 25% |
| Oral code walkthrough of your buffer pool and B+tree | 10% |

**Mastery gate:** you pass when you can, without AI help, (a) explain every line of your buffer pool and B+tree and fix a bug the examiner plants in them within 30 minutes; (b) recover a 30-record ARIES log by hand with the correct final page states; and (c) given a PostgreSQL instance with four planted performance problems (missing index, stale statistics, a bad composite-index order, table bloat), find and fix at least three in two hours using `EXPLAIN (ANALYZE, BUFFERS)` and system views.

## Industry reality

PostgreSQL 18 (September 2025, with asynchronous I/O) is the current major release; 19 was in beta in October 2026. Beyond the Uber, Notion and Zerodha cases above:

- **Figma:** spent about nine months on horizontal sharding after its PostgreSQL stack grew almost 100× from 2020.
- **PhonePe:** TStore keeps payment records in HBase, with Kafka as its write-ahead log.
- **Discord:** moved message storage from Cassandra to ScyllaDB.

Interview questions from this course:

1. **"Why are databases built on B+trees and not binary search trees?"** A strong answer covers page-sized nodes and high fanout, height 3–4 for billions of keys, linked leaves for range scans, and the gap between random and sequential I/O.
2. **"When would you pick an LSM-based store over a B+tree?"** Cover write-heavy workloads, write/read/space amplification, compaction stalls and bloom filters, and give one named system for each.
3. **"What happens when a PostgreSQL transaction commits?"** Cover the WAL record and LSN, the flush and `fsync` (group commit), the fact that data pages are written later by checkpoints and the background writer, and how `synchronous_commit` and replication change this.
4. **"Explain write skew and how you would prevent it."** Give a concrete example (two on-call doctors both going off duty). Explain that snapshot isolation allows it, then give the fixes: `SERIALIZABLE` (SSI), materializing the conflict, or `SELECT … FOR UPDATE`.
5. **"A query became 100× slower after a bulk load. Debug it."** Cover `EXPLAIN ANALYZE` with estimated vs actual rows, stale statistics and `ANALYZE`, plan flips, bloat and vacuum, and verifying the fix under production-like data.

## Resources (free first)

- **Primary course:** [CMU 15-445/645 Fall 2026](https://15445.courses.cs.cmu.edu/fall2026/) (schedule, assignments, AI policy) and the [BusTub](https://github.com/cmu-db/bustub) educational DBMS (MIT licence). Advanced follow-up: [CMU 15-721 Fall 2025](https://www.cs.cmu.edu/~15721-f25/).
- **India:** NPTEL [Data Base Management System](https://nptel.ac.in/courses/106105175) (IIT Kharagpur).
- **Build-along texts:** [Let's Build a Simple Database](https://cstack.github.io/db_tutorial/) (SQLite clone in C); [Build Your Own Database From Scratch in Go](https://build-your-own.org/database/) (Part I free, Part II paid).
- **Documentation:** PostgreSQL [page layout](https://www.postgresql.org/docs/current/storage-page-layout.html), [MVCC](https://www.postgresql.org/docs/current/mvcc.html), [WAL](https://www.postgresql.org/docs/current/wal.html), [EXPLAIN](https://www.postgresql.org/docs/current/using-explain.html), [vacuuming](https://www.postgresql.org/docs/current/routine-vacuuming.html); SQLite [architecture](https://www.sqlite.org/arch.html), [file format](https://www.sqlite.org/fileformat.html), [testing](https://www.sqlite.org/testing.html); [RocksDB wiki](https://github.com/facebook/rocksdb/wiki) and [leveled compaction](https://github.com/facebook/rocksdb/wiki/Leveled-Compaction); [DuckDB docs](https://duckdb.org/docs/current/); [pgvector](https://github.com/pgvector/pgvector).
- **Papers:**
  - [Architecture of a Database System](https://dsf.berkeley.edu/papers/fntdb07-architecture.pdf) (2007)
  - [ARIES](https://research.ibm.com/publications/aries-a-transaction-recovery-method-supporting-fine-granularity-locking-and-partial-rollbacks-using-write-ahead-logging) (1992)
  - [The LSM-Tree](https://www.cs.umb.edu/~poneil/lsmtree.pdf) (1996)
  - [Access Path Selection in System R](https://courses.cs.washington.edu/courses/cse444/25wi/papers/selinger79.pdf) (1979)
  - [What Goes Around Comes Around… And Around…](https://db.cs.cmu.edu/papers/2024/whatgoesaround-sigmodrec2024.pdf) (Stonebraker and Pavlo, 2024)
- **Correctness in the wild:** [Jepsen analyses](https://jepsen.io/analyses).
- **Paid, worth it:** *Designing Data-Intensive Applications*, 2nd edition (Kleppmann and Riccomini, O'Reilly, March 2026); Alex Petrov, *Database Internals* (O'Reilly).

## Sources

All checked 12 Oct 2026 unless noted.
- CMU 15-445 Fall 2026 [assignments](https://15445.courses.cs.cmu.edu/fall2026/assignments.html), [schedule](https://15445.courses.cs.cmu.edu/fall2026/schedule.html), [syllabus and coding-agent policy](https://15445.courses.cs.cmu.edu/fall2026/syllabus.html).
- [PostgreSQL 18 release announcement](https://www.postgresql.org/about/news/postgresql-18-released-3142/) (25 Sep 2025); [PostgreSQL 19 Beta 4](https://www.postgresql.org/about/news/postgresql-19-beta-4-released-3386/) (24 Sep 2026); [versioning policy](https://www.postgresql.org/support/versioning/).
- [BIRD text-to-SQL leaderboard](https://bird-bench.github.io/): top test execution accuracy ≈ 82.95% (7 Sep 2026); human baseline 92.96%.
- [Uber: Why Uber Engineering Switched from Postgres to MySQL](https://www.uber.com/blog/postgres-to-mysql-migration/) (Jul 2016).
- [Notion: Herding elephants](https://www.notion.com/blog/sharding-postgres-at-notion) (Oct 2021).
- [Figma: How Figma's databases team lived to tell the scale](https://www.figma.com/blog/how-figmas-databases-team-lived-to-tell-the-scale/) (Mar 2024).
- [Zerodha: Working with PostgreSQL](https://zerodha.tech/blog/working-with-postgresql/) (Apr 2021).
- [PhonePe: Demystifying TStore](https://tech.phonepe.com/demystifying-tstore-the-backbone-of-billions-of-transactions-at-phonepe/) (Aug 2024).
- [Discord: How Discord stores trillions of messages](https://discord.com/blog/how-discord-stores-trillions-of-messages) (Mar 2023).
- [Jepsen: Amazon RDS for PostgreSQL 17.4](https://jepsen.io/analyses/amazon-rds-for-postgresql-17.4).
- [DDIA 2nd edition announcement](https://martin.kleppmann.com/2026/03/24/designing-data-intensive-applications-2e.html) (Mar 2026).

_Last reviewed: 2026-10_
