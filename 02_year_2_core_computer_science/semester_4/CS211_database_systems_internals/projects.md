# CS211 · Labs and projects

Labs can be done in C++ on top of CMU's public [BusTub](https://github.com/cmu-db/bustub) codebase, or in Go or Rust against the same interfaces (page, buffer pool, index, executor). Every lab ships with tests you must pass, plus a short write-up of what you measured. Labs 1–3 are done without coding agents. From Lab 4 on, AI assistants are allowed, but you must be able to explain every line in the oral walkthrough.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 0 · Storage microbenchmark | Measure sequential vs random 4 KB reads and `fsync` latency on your own SSD | A latency table, a 10-line program, and one paragraph on what it means for page size | 3 h |
| 1 · Slotted page | Implement insert, delete, update and compaction on an 8 KB slotted page with record IDs | Code passing unit tests and a 100k-operation fuzz test against an in-memory map | 5 h |
| 2 · Buffer pool manager | Page table, pin/unpin, dirty flush, and LRU-K or CLOCK replacement; thread-safe | Code, a hit-rate comparison on a trace with a sequential-flooding scan, and a ThreadSanitizer-clean run | 8 h |
| 3 · B+tree index | Insert, delete with merge and redistribution, range scan iterator, latch crabbing | Code passing concurrent tests (16 threads), and a fuzz test against a sorted map with 1M operations | 12 h |
| 4 · Query executor | Volcano iterators: sequential scan, index scan, filter, projection, external sort, hash join, sort-merge join, hash aggregation | Code plus a table of measured vs predicted page I/Os for each join on three input sizes | 10 h |
| 5 · PostgreSQL plan clinic | Diagnose ten slow queries on a 20-million-row synthetic e-commerce dataset | For each query: the plan before and after, the root cause, the fix, and the speed-up | 6 h |
| 6 · Lock manager | Shared/exclusive and intention locks, strict 2PL, deadlock detection with a waits-for graph | Code passing deadlock and starvation tests | 6 h |
| 7 · Isolation anomalies | Reproduce dirty read (where possible), lost update, write skew and phantom in PostgreSQL at each isolation level | Two-session scripts, observed outcomes, and an explanation tied to MVCC and SSI | 4 h |
| 8 · WAL and recovery | WAL with LSNs and group commit, fuzzy checkpoints, ARIES-style redo and undo with CLRs | Code passing a 200-iteration `kill -9` crash test, and a plot of commits per second vs group-commit size | 10 h |
| 9 · Two-phase commit | Coordinator and three participants, with failure injection at every protocol step | A log of each failure case showing which ones block and why | 5 h |

## Projects

### P1 · SQLite file inspector (L1, ~6 hours)

**Real-world inspiration:** SQLite's on-disk format is fully documented and stable ([file format](https://www.sqlite.org/fileformat.html)). Backup tools, data-recovery tools and mobile-app debuggers read database files directly without the SQLite library. Reading the format teaches B-tree pages faster than any diagram.

**What to build:** a command-line tool, written from the spec without the SQLite library, that opens a `.db` file. It should print the header (page size, page count, text encoding), list tables from `sqlite_schema`, and dump every row of a named table by walking interior and leaf table b-tree pages.

**Acceptance criteria:**
- On three provided files (one page; 10,000 rows spanning interior pages; a table with an index), your row dump is identical to `sqlite3 -csv` output, with an empty `diff`.
- Varint and record-header decoding is covered by at least 20 unit tests, including 9-byte varints.
- The tool reads a 10 MB file in under 2 seconds.
- It refuses corrupt input (wrong magic string, out-of-range page number) with a clear error instead of crashing.

**Stretch goals:** overflow pages for large text; lookups through an index b-tree; listing freelist pages; reading uncheckpointed frames from a `-wal` file.

**What it proves to an employer:** you can turn a binary format specification into working code, and you understand how a real B-tree is laid out on disk.

### P2 · Crash-safe LSM key-value store (L2, ~15 hours)

**Real-world inspiration:** RocksDB's [leveled compaction](https://github.com/facebook/rocksdb/wiki/Leveled-Compaction) design. PhonePe's TStore ledger uses Kafka as its write-ahead log in front of HBase ([PhonePe Tech, 2024](https://tech.phonepe.com/demystifying-tstore-the-backbone-of-billions-of-transactions-at-phonepe/)). Write-optimized storage sits under most high-ingest systems.

**What to build:** an embedded KV store with `put`, `get`, `delete` and `scan`. It needs:
- a WAL with checksums and a configurable `fsync` policy;
- a sorted memtable;
- immutable SSTables with a block index and a bloom filter;
- tombstones;
- leveled compaction from L0 to at least L2;
- recovery on start-up.

**Acceptance criteria:**
- 1,000,000 random operations, checked differentially against an in-memory map, give zero mismatches.
- In sync mode, 200 `kill -9` crash cycles at random moments lose no acknowledged write. Checksums detect torn records, which are discarded rather than returned.
- Measured bloom-filter false-positive rate at 10 bits per key is within 1.5× of the theoretical value.
- A report gives write amplification for a 10-million-key write-heavy workload, plus p50 and p99 `get` latency both outside and during compaction, with plots.
- A README explains the on-disk format and one design decision you would change.

**Stretch goals:** snapshot reads using sequence numbers; block compression; a switch between tiered and leveled compaction, with a comparison; a deterministic fault-injection file system for tests.

**What it proves to an employer:** you can build storage with real durability guarantees, test it adversarially, and talk about amplification trade-offs with numbers.

### P3 · Transactional ledger engine (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** payment ledgers behind UPI apps and payout platforms. Razorpay makes idempotency keys mandatory on payouts so that retries cannot pay twice ([Razorpay docs](https://razorpay.com/docs/api/x/payout-idempotency/)). TigerBeetle tests its financial database by deterministic simulation under injected faults ([TigerBeetle safety](https://docs.tigerbeetle.com/concepts/safety/)).

**What to build:** a single-node engine for accounts and transfers, built from your own components:
- the buffer pool and B+tree from the labs;
- the WAL with ARIES-style recovery and fuzzy checkpoints;
- concurrency control, either MVCC with serializable validation for transfers or strict 2PL (justify the choice);
- idempotency keys;
- a typed API or a small SQL subset;
- a benchmark driver.

**Acceptance criteria:**
- **Conservation:** the sum of all balances is unchanged after 10 million random transfers from 16 concurrent clients. A checker verifies this after every run.
- **Idempotency:** in a property test that replays 100,000 requests with duplicate keys, money moves at most once and the duplicate returns the original result.
- **Crash safety:** across 500 crash-and-recover cycles at random points (including during checkpoints and during recovery), no committed transfer is lost and no transfer is partly applied.
- **Recovery speed:** recovery takes under 5 seconds for a 1 GB log with checkpointing enabled.
- **Isolation:** a provided anomaly suite (lost update, write skew on overdraft limits) passes at your declared isolation level, and you document every anomaly it still allows.
- **Scaling:** throughput and p99 latency are reported at 1, 4 and 16 threads. Throughput at 4 threads is at least 2.5× the single-thread figure on a machine with 4 or more cores.
- **Write-up:** a design document, a failure-mode table, and a 5-minute screen recording of a crash and recovery.

**Stretch goals:** ship the WAL to a follower that replays it (a preview of CS212); a deterministic simulation harness with a seeded scheduler and fault-injecting disk; double-entry postings with balance history queries.

**What it proves to an employer:** that you can be trusted with money-moving code. You reason about invariants, idempotency, isolation and durability, and you prove them with adversarial tests rather than asserting them.

## Feeds into

- [BE303 Data Modeling and Storage for Backends](../../../03_majors/backend_engineering/year_3/BE303_data_modeling_and_storage_for_backends_postgres/README.md) and [BE402 Scalability and Performance](../../../03_majors/backend_engineering/year_4/BE402_scalability_and_performance_caching_sharding/README.md): indexing, plans, sharding.
- [BE401 Payments-Grade Systems](../../../03_majors/backend_engineering/year_4/BE401_payments_grade_systems_transactions_idempotency/README.md) and the [OV10A Payment Systems Engineering](../../../04_overlaps/OV10_fintech_systems_engineering/OV10A_payment_systems_engineering_upi_cards/README.md) overlap: P3 is the starting point.
- [DEN305 Lakehouse Architecture](../../../03_majors/data_engineering/year_3/DEN305_lakehouse_architecture_parquet_iceberg_and_delta/README.md): columnar storage and compression from Chapter 2.
- [CLD305 Cloud Storage and Managed Databases](../../../03_majors/cloud_engineering/year_3/CLD305_cloud_storage_and_managed_databases/README.md): replication and disaggregated storage.
- [CS212 Distributed Systems I](../CS212_distributed_systems_i/README.md) and [CSG303 Distributed Systems II](../../../03_majors/computer_science_general/year_3/CSG303_distributed_systems_ii_consensus_replication/README.md): replicating the WAL with consensus.
