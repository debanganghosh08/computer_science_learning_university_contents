# BE303 · Labs and projects

Labs use PostgreSQL 18 in Docker, Redis or Valkey, and DynamoDB Local or a single-node ScyllaDB/Cassandra container. A shared data generator produces skewed, realistic data: Indian names, PIN codes and cities, power-law tenant sizes and bursty timestamps. Fixtures with 10 rows hide every interesting bug, so most labs run on 10–200 million rows. Lab 3 and the live exam are done without AI assistants.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Domain model | Model a food-delivery domain with keys, types and constraints so that 12 listed invalid states cannot be stored | Schema, ER diagram and a test per invalid state showing the database rejects it | 5 h |
| 2 · Index design | Index five queries on a 20M-row orders table, including one that benefits from PostgreSQL 18 skip scan | Before/after `EXPLAIN (ANALYZE, BUFFERS)` and index sizes, with column-order reasoning | 5 h |
| 3 · Plan clinic (no AI) | Diagnose ten slow queries from `pg_stat_statements` on a replayed workload | Root cause, fix and speed-up for each, plus one plan you could not improve and why | 6 h |
| 4 · Anomalies | Reproduce a lost update, write skew, a deadlock and a lock-queue pile-up behind `ALTER TABLE` | Two-session scripts, observed outcomes and the fix for each | 5 h |
| 5 · `SKIP LOCKED` queue | A 16-worker job queue in a Postgres table with retries and visibility timeouts | A proof run of 1M jobs: none lost, none run twice (checked by a unique constraint on results) | 5 h |
| 6 · Restore drill | WAL archiving and point-in-time recovery after an accidental `DELETE` | Timed runbook and the recovered row count | 4 h |
| 7 · Live migration | Expand/contract migration of a 50M-row table while k6 drives 1,000 requests/s | Error log (target: zero), p99 plot during the backfill, and the lock waits you observed | 8 h |
| 8 · Redis | Cache-aside with invalidation, a token-bucket rate limiter in Lua, and a fenced lock | Concurrency tests for each, plus a demonstration of the unfenced lock's failure | 6 h |
| 9 · Access-pattern design | Single-table DynamoDB design (or Cassandra model) for orders and riders from a list of 10 access patterns | Key design, GSIs, a hot-partition load test and the fix | 6 h |

## Projects

### P1 · Order schema and query pack (L1, ~6 hours)

**Real-world inspiration:** food-delivery and quick-commerce apps in India (Swiggy, Zomato, Zepto, Blinkit) answer the same questions all day: a customer's recent orders, a restaurant's open orders, a rider's active deliveries, daily sales per store. Their exact schemas are not public; the domain and its queries are. The data volumes here are an **illustrative scenario**.

**What to build:** a PostgreSQL schema for customers, restaurants, menu items (with price history), orders, order items and delivery assignments. Add a data generator for 10 million orders over 90 days, with realistic skew (a few very large restaurants, lunch and dinner peaks). Write a query pack of 10 named queries an API would run.

**Acceptance criteria:**
- Every one of the 10 queries runs under 10 ms at p95 on the full data set (measured with `pgbench` custom scripts or k6), with the plan saved for each.
- Eight specified invalid states are impossible to store, and a test proves each: an item from another restaurant in the order, a negative price, a delivered order without a rider, overlapping price-history periods, and four more.
- Money is stored as integer paise or `numeric`, never as a float, and all timestamps are `timestamptz`. A reviewer's checklist confirms both.
- A README justifies each index with the query it serves and shows the total index size against the table size.

**Stretch goals:** keyset pagination for order history; a materialized view for daily sales with a refresh strategy; compare UUIDv7 and `bigint` keys at this scale.

**What it proves to an employer:** you model data so that bugs cannot be stored, and you index from queries rather than by guessing.

### P2 · Zero-downtime migration under live traffic (L2, ~15 hours)

**Real-world inspiration:** Stripe's four-step dual-write pattern for online migrations ([Stripe, 2017](https://stripe.com/blog/online-migrations)). OpenAI allows only lightweight schema changes with a 5-second timeout on its main PostgreSQL primary, and throttles backfills ([VentureBeat, Jan 2026](https://venturebeat.com/data/how-openai-is-scaling-the-postgresql-database-to-800-million-users)).

**What to build:** a running service (from BE302 or a provided one) stores a free-text `address` column on a 50M-row `customers` table. Migrate it to structured columns (`line1`, `city`, `pin_code`, `state`) and a separate `addresses` table, while a k6 load test keeps running at 1,000 requests/s, half of them writes. Do it as a series of deploys:
- expand;
- dual-write;
- batched, throttled backfill with progress tracking;
- switch reads behind a flag;
- a verification job comparing old and new data;
- contract.

Each step needs a tested rollback.

**Acceptance criteria:**
- Zero failed requests across the whole migration (k6 output attached).
- p99 latency never exceeds the baseline by more than 20% during the backfill. The throttle adapts to replica lag or p99, and a plot shows it.
- No DDL statement waits more than 2 s for a lock: `lock_timeout` is set and retries are logged.
- The verification job reports zero mismatches before the contract step, and a deliberately injected mismatch is caught.
- Rolling back from any step before "contract" restores the previous behaviour with no data loss, demonstrated for two steps.
- A runbook another student can follow without asking you questions.

**Stretch goals:** repeat the migration with pgroll and compare; add a `NOT NULL` constraint on 50M rows using `NOT VALID` plus `VALIDATE`; replicate the new table to a search index through CDC.

**What it proves to an employer:** you can change the shape of production data without an outage. This is one of the most trusted skills a backend engineer can show.

### P3 · Block-based workspace storage layer (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** Notion stores pages as trees of blocks in PostgreSQL, sharded by workspace ID into 480 logical shards (see CS211 sources). Its 2026 write-up on vector search shows the same workspace-keyed partitioning reused for AI features ([Notion, Feb 2026](https://www.notion.com/blog/two-years-of-vector-search-at-notion)). Your version runs on one node with partitions standing in for shards.

**What to build:** the storage layer and a thin API for a multi-tenant workspace app:
- **Schema:** workspaces, pages and nested blocks; block properties in JSONB, with typed columns where queries need them.
- **Tenancy:** hash partitioning by workspace, and row-level security as a second tenant guard.
- **Access:** sharing and permission tables; full-text and trigram search across a workspace.
- **History:** an append-only edit history.
- **Cache:** a Redis or Valkey cache for page trees, with correct invalidation.
- **Reads:** a read replica with read-your-writes routing.
- **Operations:** a migration pipeline, backups with point-in-time recovery, and a load generator.

**Acceptance criteria:**
- **Scale:** 50 million blocks across 20,000 workspaces with power-law sizes; the largest workspace holds at least 2 million blocks.
- **Read latency:** loading a page tree of up to 500 blocks at depth ≤ 3 takes under 30 ms at p95, both cold and warm.
- **Write rate:** 2,000 block writes/s sustained for 30 minutes with p99 under 50 ms and no autovacuum falling behind (dead-tuple ratio plotted).
- **Cache correctness:** cache hit rate above 90% on the read workload. A consistency checker that reads after every write in the same session finds zero stale reads on the read-your-writes path over 1 million operations.
- **Tenant isolation:** an adversarial test suite, including queries with a missing or forged tenant filter, shows zero cross-workspace reads with RLS enabled.
- **Recovery:** restore to a chosen timestamp in under 15 minutes on the full data set, timed and documented.
- **Migration:** one schema change applied under load with zero errors.
- **Write-up:** a design document with an engine decision record and a failure-mode table. The record must explain why you did or did not add a second store such as a search engine or document database.

**Stretch goals:** move the largest workspace to its own partition or node without downtime; add `pgvector` similarity search over block text (a preview of BE403); run the same workload on a distributed SQL database and compare.

**What it proves to an employer:** you can own the data layer of a real multi-tenant product: modeling, performance, isolation, caching, migrations and recovery, with numbers to back every claim.

## Feeds into

- [BE403 Backends for AI](../../year_4/BE403_backends_for_ai_serving_llm_features_vector/README.md): P3's storage layer gains vector search and embedding pipelines.
- [BE401 Payments-Grade Systems](../../year_4/BE401_payments_grade_systems_transactions_idempotency/README.md): the isolation and locking work of Chapter 4 becomes ledger correctness.
- [BE402 Scalability and Performance](../../year_4/BE402_scalability_and_performance_caching_sharding/README.md): caching, replicas and sharding at larger scale.
- [BE304 Asynchronous Systems](../BE304_asynchronous_systems_queues_streams_and_event/README.md): change data capture and the transactional outbox.
- [DEN301 Data Modeling and Warehousing](../../../data_engineering/year_3/DEN301_data_modeling_and_warehousing/README.md): an elective for analytical modeling.
