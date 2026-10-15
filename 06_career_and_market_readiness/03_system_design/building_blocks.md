# Building blocks

Every design is assembled from a small set of components. For each one this page gives what it is, when to use it, what it costs you, and numbers you can quote. The theory behind them is in [CS212](../../02_year_2_core_computer_science/semester_4/CS212_distributed_systems_i/README.md) and [BE402](../../03_majors/backend_engineering/year_4/BE402_scalability_and_performance_caching_sharding/README.md); this page is the interview-ready summary.

**How to use the numbers.** Measured or documented numbers carry a source and a date. Numbers marked **rough** are order-of-magnitude ballparks for back-of-the-envelope work: they vary by 3–10× with hardware, payload and configuration, so say "roughly" in an interview and measure before you size a real fleet.

## Contents

0. [Latency numbers](#0-latency-numbers-every-engineer-should-know) · 1. [Load balancers](#1-load-balancers) · 2. [Caches](#2-caches) · 3. [CDNs](#3-cdns) · 4. [Databases](#4-databases-sql-nosql-newsql) · 5. [Replication](#5-replication) · 6. [Sharding](#6-sharding) · 7. [Consistent hashing](#7-consistent-hashing) · 8. [Queues and streams](#8-queues-and-streams) · 9. [Search indexes](#9-search-indexes) · 10. [Object storage](#10-object-storage) · 11. [Rate limiters](#11-rate-limiters) · 12. [Idempotency](#12-idempotency) · 13. [Consensus](#13-consensus-and-coordination) · 14. [Unique IDs](#14-unique-ids-and-time) · 15. [Observability](#15-observability) · 16. [Vector databases](#16-vector-databases) · 17. [LLM serving](#17-llm-serving)

---

## 0. Latency numbers every engineer should know

### The original table (Jeff Dean, 2009)

From the slide "Numbers Everyone Should Know" in Jeff Dean's keynote *Designs, Lessons and Advice from Building Large Distributed Systems* (LADIS, October 2009). Peter Norvig published an earlier version in "Teach Yourself Programming in Ten Years".

| Operation | Time |
|---|---|
| L1 cache reference | 0.5 ns |
| Branch mispredict | 5 ns |
| L2 cache reference | 7 ns |
| Mutex lock/unlock | 25 ns |
| Main memory reference | 100 ns |
| Compress 1 KB with Zippy (Snappy) | 3,000 ns = 3 µs |
| Send 2 KB over 1 Gbps network | 20,000 ns = 20 µs |
| Read 1 MB sequentially from memory | 250,000 ns = 250 µs |
| Round trip within same datacenter | 500,000 ns = 500 µs |
| Disk seek | 10,000,000 ns = 10 ms |
| Read 1 MB sequentially from disk | 20,000,000 ns = 20 ms |
| Send packet California → Netherlands → California | 150,000,000 ns = 150 ms |

### The same ideas, measured in 2026

The open *napkin-math* project re-measured its numbers on a GCP `c4-standard-48-lssd` instance (Intel Xeon 6985P-C) in March 2026 and rounds them for memorisation. Selected rows:

| Operation | Latency | Throughput |
|---|---|---|
| Sequential memory read/write, 64 B, one thread | 0.5 ns | 20 GiB/s |
| Non-cryptographic hash, 64 B | 10 ns | 5 GiB/s |
| Cryptographic hash, 64 B | 100 ns | 1 GiB/s |
| System call | 300 ns | — |
| Context switch | 10 µs | — |
| Sequential SSD read, 8 KiB | 1 µs | 8 GiB/s |
| Random SSD read, 8 KiB | 100 µs | 70 MiB/s |
| Sequential SSD write with fsync, 8 KiB | 300 µs | 30 MiB/s |
| Random HDD read, 8 KiB | 10 ms | 0.7 MiB/s |
| Network round trip within a zone or region | 250 µs | 2–25 GiB/s |
| A simple query to MySQL, Memcached or Redis (including the network) | 500 µs | — |
| Network NA East ↔ NA West | 60 ms | 25 MiB/s per connection |
| Network EU West ↔ NA East | 80 ms | 25 MiB/s |
| Network NA West ↔ Singapore | 180 ms | 25 MiB/s |
| Blob storage GET, 128 KiB, one connection | 80 ms | 100 MiB/s |
| Blob storage PUT, 128 KiB, one connection | 200 ms | 100 MiB/s |

**What to take from both tables:**

1. **Memory is about 1,000× faster than a network round trip, and a network round trip in a region is about 200× faster than crossing an ocean.** A design that makes 10 sequential cross-region calls per request cannot meet a 200 ms p99.
2. **Random SSD reads (≈100 µs) replaced disk seeks (≈10 ms).** That 100× change is why "one database server" goes much further today than in 2009.
3. **fsync is expensive (≈300 µs).** Durable writes are batched (group commit) for this reason.
4. **Distance is physics.** Light in fibre travels about 200,000 km/s, so every 100 km of fibre adds about 1 ms of round trip. Use measured region-to-region latencies (for example cloudping.co) for your provider; for Indian users, keep latency-critical paths in Indian regions.
5. **Colin Scott's interactive table** extrapolates Dean's numbers year by year from hardware trends. It is useful for intuition, but its values are modelled, not measured; prefer measured figures when you quote numbers.

### Throughput ballparks

| Component | Number | Type |
|---|---|---|
| One Redis core (Uber's CacheFront) | 6 million reads/s served by about 3,000 Redis cores ≈ 2,000 reads/s per core in that deployment (it replaced ≈ 60,000 storage-engine cores) | Derived from Uber, Feb 2024 |
| A single in-memory key-value instance, simple GET/SET | ~100,000 ops/s | **Rough** |
| Kafka, 3 brokers (2014 hardware: 6 cores, 1 GbE, SATA disks) | 2,024,032 records/s of 100 bytes from 3 producers with 3× async replication; median end-to-end latency 2 ms | Measured, LinkedIn 2014 |
| DynamoDB, one partition | 3,000 read units/s and 1,000 write units/s (1 write unit = one 1 KB write/s) | Documented limit |
| S3, one key prefix | at least 3,500 writes/s and 5,500 reads/s; 100–200 ms first-byte latency for small objects | Documented |
| Persistent TCP connections on one server | over 2 million on one FreeBSD/Erlang box (24 logical CPUs, ~96 GiB RAM) | WhatsApp, Jan 2012 |
| A stateless JSON API on one vCPU | hundreds to a few thousand requests/s | **Rough** |
| A well-indexed relational primary, simple single-row writes | thousands to tens of thousands per second; reads scale out with replicas | **Rough** |
| A single relational primary at very large scale | OpenAI reported (Jan 2026) serving ChatGPT's main relational workload from one PostgreSQL primary and nearly 50 replicas | Reported |
| Sharded MySQL fleet | Slack peaked at 2.3 million queries/s on Vitess (2020) | Reported |

---

## 1. Load balancers

**What.** A component that spreads requests across healthy backends and hides their failure. **L4** balancers route TCP/UDP connections by address and port (fast, protocol-agnostic). **L7** balancers understand HTTP or gRPC and route by path, header or cookie, terminate TLS, retry, and rate-limit. A global layer (DNS-based or anycast) picks the region.

**Algorithms.** Round robin (fine for uniform requests); least outstanding requests (better when request costs vary); **power of two choices** (pick two random backends, send to the less loaded: near-optimal with almost no coordination); **consistent hashing** when the same key should reach the same backend (cache affinity). Google's Maglev (NSDI 2016) is a software L4 balancer on commodity Linux that uses its own consistent hashing so connections survive backend changes.

**When.** From the second server onwards. Every stateless tier sits behind one.

**Trade-offs and gotchas.**
- Health checks that only test "process up" route traffic to a server whose database connection is broken; check a dependency-light readiness endpoint, and eject outliers by error rate.
- Retries at the balancer multiply load during an outage. Use a retry budget (for example, retries ≤ 10% of requests).
- Long-lived connections (WebSocket, gRPC streams) do not rebalance when you add servers; you need connection draining and periodic reconnection.
- The balancer is itself a single point of failure unless it is redundant (active-active pairs, anycast, or a managed service).

**Interview line.** "Stateless API servers behind an L7 balancer with least-request routing; sticky routing only for the WebSocket gateway, where I hash user ID to a gateway node."

## 2. Caches

**What.** A faster copy of data that is expensive to compute or fetch. Layers: client, CDN, reverse proxy, in-process, distributed (Redis, Memcached).

**Patterns.**

| Pattern | How | Risk |
|---|---|---|
| Cache-aside | App reads cache; on miss reads DB and fills cache | Stale data after writes; thundering herd on a hot miss |
| Read-through | Cache library loads from DB on miss | Same as cache-aside, hidden in a library |
| Write-through | Write cache and DB together | Write latency; cache fills with data nobody reads |
| Write-behind | Write cache, flush to DB later | Data loss if the cache dies before the flush |

**Invalidation is the hard part.** Options: TTLs with random jitter (so keys do not expire together); delete-on-write; versioned keys; change-data-capture (CDC) that tails the database log and invalidates. Uber's CacheFront tails the MySQL binlog to invalidate Redis entries within seconds, reports 99.99% consistency, a 99%+ hit rate for its largest use case, and P99.9 latency down over 67% (Feb 2024). Facebook's *Scaling Memcache* (NSDI 2013) introduced **leases** to stop stale sets and thundering herds.

**Hot keys.** One celebrity profile or one viral link can overload a single cache shard. Mitigations: replicate the hot key to several shards with a random suffix; keep a small in-process cache in front; coalesce concurrent misses into one backend request.

**When not to cache.** Account balances, seat inventory and anything where a stale read causes a wrong action. Cache the *display* ("about 12 seats left"), never the *decision*.

**Numbers.** A cache hit costs ~0.5 ms over the network (napkin-math); an in-process hit costs ~100 ns. Memory is the cost driver: size the cache from the hot set ([estimation.md, example 4](estimation.md#example-4--cache-size-for-a-url-shortener)).

## 3. CDNs

**What.** A network of edge servers near users that caches static and some dynamic content, terminates TLS close to the user, and absorbs traffic spikes and attacks.

**Use for.** Images, video segments, JavaScript bundles, public API responses that are identical for many users (a scorecard, a product page without personal data).

**Design points.**
- **Cache key.** Include only what changes the response. Adding a session cookie to the key turns a 95% hit rate into ~0%.
- **TTL and purge.** Short TTLs for live data (1–5 s for a live score), long TTLs plus versioned file names for assets.
- **Origin shield.** A middle tier so that thousands of edge misses become one origin request.
- **Signed URLs** for paid or private content.

**Real systems.** Netflix's Open Connect places its own appliances inside ISP networks (provided free to qualifying ISPs) and fills them with content ahead of demand, with nightly fills over peering links. Hotstar reported more than 10 Tbps of peak bandwidth when it served 25.3 million concurrent viewers in 2019 (AWS re:Invent talk, as reported). See [case study 10](case_studies/10_live_video_streaming.md).

**Trade-offs.** Cost per GB, purge latency, and limited ability to personalise. Personalised parts of a page come from the origin or from edge compute.

## 4. Databases: SQL, NoSQL, NewSQL

**Choose from access patterns, not fashion.** Write the access-pattern table first (query → key → frequency → consistency), then pick.

| Family | Examples | Choose when | Costs |
|---|---|---|---|
| Relational (SQL) | PostgreSQL, MySQL | Transactions across rows, joins, constraints, ad-hoc queries; most products for years | One primary limits write throughput; sharding is manual (or via Vitess, Citus) |
| Key-value | DynamoDB, Redis, RocksDB-based stores | Lookups by key at any scale with predictable latency | No joins; secondary indexes cost extra writes |
| Wide-column | Cassandra, ScyllaDB, Bigtable, HBase | Very high write rates, time-ordered data per key (messages, events) | Tables designed per query; tombstones and compaction to manage |
| Document | MongoDB, Firestore | Flexible nested records read as a whole | Cross-document transactions are limited or costly |
| Search | Elasticsearch, OpenSearch | Full-text and faceted search | Not a source of truth; eventually consistent |
| Time-series | Prometheus, InfluxDB, TimescaleDB | Metrics and sensor data, downsampling | Narrow query model |
| NewSQL (distributed SQL) | Spanner, CockroachDB, TiDB, YugabyteDB | SQL and transactions beyond one machine or across regions | Each write needs a consensus round; cross-region writes pay at least one inter-region round trip |
| Graph | Neo4j; Meta's TAO (a graph-shaped cache over MySQL) | Multi-hop relationship queries | Hard to shard; many teams model graphs in key-value stores instead |

**Evidence that "boring" goes far.** OpenAI reported in January 2026 that ChatGPT's main relational workload runs on one PostgreSQL primary with nearly 50 read replicas, protected by caching, workload isolation and strict query discipline. Slack moved to Vitess (sharded MySQL) when per-workspace sharding created hot spots (2020). Discord moved trillions of messages from 177 Cassandra nodes to 72 ScyllaDB nodes and cut p99 read latency from 40–125 ms to about 15 ms (2023).

**Interview line.** "The order and payment tables need multi-row transactions, so Postgres. The location stream is append-only, write-heavy and keyed by driver, so a wide-column store or just an in-memory geo-index with a log."

## 5. Replication

**Why.** Survive machine loss (durability, availability) and serve more reads.

| Model | How | Use | Watch out for |
|---|---|---|---|
| Single leader, followers | Writes to leader, log shipped to followers | Most databases | Replication lag: users may not read their own writes from a follower |
| Synchronous vs asynchronous | Sync waits for follower ack; async does not | Sync for zero data loss within a region | Sync adds a round trip per commit; async can lose the last writes on failover |
| Multi-leader | Several leaders accept writes, exchange changes | Multi-region writes, offline clients | Write conflicts: need last-writer-wins, CRDTs or app-level merge |
| Leaderless quorum | Write to W of N replicas, read from R; if R + W > N, a read overlaps the latest write | Dynamo-style stores (Cassandra, Riak) | Sloppy quorums and hinted handoff weaken the guarantee; read repair and anti-entropy needed |

**Read-your-writes in practice.** After a user writes, route their reads to the leader for a few seconds, or carry the write's log position and wait until the follower has caught up.

**Numbers.** In-region synchronous replication adds ~0.25–0.5 ms (one round trip). Cross-region synchronous replication adds tens to hundreds of milliseconds, which is why most systems replicate across regions asynchronously and accept a small recovery point objective (RPO).

## 6. Sharding

**What.** Splitting data across machines by a **shard key** so that each machine holds a fraction.

| Scheme | How | Good | Bad |
|---|---|---|---|
| Hash | shard = hash(key) mod N (or a ring) | Even spread | Range scans hit every shard; changing N moves data unless consistent hashing |
| Range | Keys sorted into ranges, ranges split when big | Range queries, time-ordered data | Hot ranges (all new writes go to "now") |
| Directory / lookup | A table maps key → shard | Flexible moves, tenant isolation | The directory is a critical dependency; cache it |
| Geographic / tenant | By region or customer | Data residency, isolation | Uneven sizes; large tenants outgrow a shard (Slack's problem) |

**Choosing the key.** It must (1) appear in almost every query, (2) spread load evenly, (3) keep things that are transacted together on one shard. Orders by `order_id` spread well, but "all orders of a restaurant" becomes a scatter-gather; a **global secondary index** keyed by restaurant fixes reads at the cost of extra writes.

**Hot keys.** Split a hot key into `key#0 … key#k` and merge on read; cache aggressively; or give the hot tenant its own shard. DynamoDB documents that one partition delivers at most 3,000 reads and 1,000 writes per second (per unit size), so a single hot partition key caps you regardless of table size.

**Resharding.** Move data online with dual writes or log-based copy, verify, then flip reads. Plan it before you need it; it is a project, not a command.

## 7. Consistent hashing

**Problem.** With `hash(key) mod N`, adding one server remaps almost every key, which empties every cache at once.

**Idea (Karger et al., 1997).** Place servers and keys on a ring of hash values; a key belongs to the next server clockwise. Adding or removing a server moves only about 1/N of the keys.

**Virtual nodes.** Each physical server takes 100–200 positions on the ring, which evens out load and lets bigger machines take more positions. Dynamo (2007) and Cassandra use this.

**Alternatives.** **Rendezvous (highest-random-weight) hashing:** score every server per key and pick the highest; simple, no ring. **Jump consistent hash** (Lamping and Veach, 2014): tiny, fast, no memory, but servers can only be added or removed at the end. **Maglev hashing:** a lookup table built for fast, even, minimally disruptive assignment in load balancers.

**Interview line.** "Cache nodes on a consistent-hash ring with virtual nodes, so adding a node moves about 1/N of the keys instead of nearly all of them." [lld/02_lru_cache.md](lld/02_lru_cache.md) covers the per-node cache; [case study 12](case_studies/12_distributed_kv_store.md) uses the ring.

## 8. Queues and streams

**What.** A buffer between producers and consumers so they can run at different speeds and fail independently.

| | Message queue | Log / stream |
|---|---|---|
| Examples | RabbitMQ, Amazon SQS | Apache Kafka, Amazon Kinesis, Apache Pulsar |
| Consumption | Each message to one consumer, deleted after ack | Consumers track an offset; messages retained for days; many independent readers |
| Ordering | Usually none (or FIFO with limits) | Per partition only |
| Use | Background jobs, work distribution | Event sourcing, CDC, analytics, fan-out to many systems, replay |

**Rules.**
- **Ordering exists only within a partition.** Partition by the entity whose events must stay in order (order ID, chat ID).
- **Delivery is at-least-once in practice.** Make every consumer idempotent (store processed message IDs, or make the effect naturally idempotent). "Exactly-once" in Kafka covers its own read-process-write transactions, not your call to a bank.
- **Parallelism ≤ partitions.** A consumer group cannot use more consumers than partitions.
- **Dead-letter queues** for messages that keep failing, with alerts.
- **Transactional outbox.** To update a database and publish an event atomically, write the event to an outbox table in the same transaction and let a relay publish it.

**Numbers.** LinkedIn measured 2,024,032 records/s (100 bytes each) on three 2014-era brokers with 3× replication, median end-to-end latency 2 ms. Kafka 4.0 (March 2025) runs without ZooKeeper, using its own Raft-based KRaft controller. Mechanics are taught in [BE304](../../03_majors/backend_engineering/year_3/BE304_asynchronous_systems_queues_streams_and_event/README.md).

## 9. Search indexes

**What.** An **inverted index** maps each term to the list of documents containing it (a posting list), so a query intersects lists instead of scanning documents. Ranking typically starts with BM25 and adds signals (popularity, freshness, personalisation, learned ranking).

**Design points.**
- **Not the source of truth.** Feed it from the database by CDC or events; rebuild it when the mapping changes.
- **Near-real-time.** Elasticsearch makes new documents searchable after a periodic refresh, by default every second. Say "searchable within about a second", not "immediately".
- **Sharding.** Usually by document: each shard holds a full index of its documents, and a query fans out to all shards and merges the top-k. Tail latency of the slowest shard sets the query latency.
- **Hybrid search.** Combine lexical (BM25) and vector similarity, then rerank. Used in RAG ([case study 14](case_studies/14_rag_enterprise_assistant.md)).

## 10. Object storage

**What.** Flat namespace of immutable objects (S3, Google Cloud Storage, Azure Blob, MinIO) addressed by key. Cheap, durable, effectively unlimited.

**Numbers (AWS documentation).** S3 Standard is designed for 99.999999999% (11 nines) durability. Each key prefix supports at least 3,500 writes/s and 5,500 reads/s, scaling gradually (with 503 "Slow Down" responses while it scales); small-object latency is about 100–200 ms.

**Patterns.**
- Store the bytes in object storage and the **metadata** (owner, size, checksum, status) in a database.
- **Pre-signed URLs** let clients upload and download directly, so your servers never proxy large files.
- **Multipart upload** for large files; resumable from the last part.
- **Lifecycle tiers** move cold objects to cheaper classes automatically.
- Put a **CDN** in front for reads; object storage latency is too high to serve hot media directly.

## 11. Rate limiters

**What.** Caps how fast a client (user, API key, IP, tenant) can call you, to protect capacity and enforce fairness.

| Algorithm | State per key | Behaviour |
|---|---|---|
| Token bucket | tokens, last refill time | Allows bursts up to bucket size, then a steady rate; the common default |
| Leaky bucket | queue or level | Smooths output to a constant rate |
| Fixed window counter | count per window | Cheap; allows 2× the limit across a window boundary |
| Sliding log | timestamps of recent requests | Exact; memory grows with the limit |
| Sliding window counter | current and previous window counts | Weighted estimate; near-exact at fixed-window cost |

**Real systems.** Stripe (2017) runs four limiters: a per-user request-rate limiter (token bucket in Redis), a concurrent-requests limiter, a fleet-usage load shedder that reserves capacity for critical requests, and a worker-utilisation load shedder. Cloudflare (2017) uses the sliding window counter with memcache-based counters in each data centre; on 400 million requests it measured 0.003% wrongly allowed or limited and a 6% average difference from the true rate.

**Design points.** Return HTTP 429 (RFC 6585) with a retry hint; fail open if the limiter store is down (Stripe's advice), except for security-critical limits such as login attempts; dark-launch new limits to see what they would block. Full design in [case study 02](case_studies/02_rate_limiter.md); class design in [lld/03_rate_limiter_class.md](lld/03_rate_limiter_class.md).

## 12. Idempotency

**What.** An operation is idempotent if doing it twice has the same effect as doing it once. Networks time out, clients retry, and queues redeliver, so every operation that changes money, inventory or messages must be idempotent.

**How.**
1. The client generates an **idempotency key** (a UUID) per logical operation and sends it on every retry.
2. The server stores `(key → request hash, status, response)` atomically with the effect, inside the same transaction where possible.
3. A repeated key returns the stored response; a repeated key with a different request body is rejected.
4. Keys expire after a window longer than any retry (Stripe documents that keys can be pruned after they are at least 24 hours old).

**Natural idempotency.** "Set status to SHIPPED" is idempotent; "add ₹100" is not, but "apply transaction T123" is if T123 is unique in the ledger.

**References.** Stripe's idempotency design (2017); the IETF draft *The Idempotency-Key HTTP Header Field*; Razorpay's payout idempotency documentation. Used in [case study 08](case_studies/08_upi_style_payment_switch.md) and [case study 09](case_studies/09_tatkal_flash_booking.md).

## 13. Consensus and coordination

**What.** A protocol (Raft, Paxos, Zab) that lets a group of nodes agree on a sequence of values despite failures, as long as a majority is up. Systems built on it: etcd and ZooKeeper (coordination), Kafka's KRaft controller, Spanner and CockroachDB (per-range replication).

**Use it for** small, critical, strongly consistent state: leader election, cluster membership, configuration, locks with fencing tokens, shard maps. **Do not** use a coordination service as a general database: etcd's default request limit is 1.5 MiB and its suggested maximum storage is 8 GiB.

**Numbers and rules.**
- 3 nodes tolerate 1 failure; 5 tolerate 2. Even sizes add cost without adding tolerance.
- Every committed write needs a majority acknowledgement: one round trip in a region (~0.25–0.5 ms plus fsync), tens of milliseconds or more across regions.
- **Locks need fencing.** A lock holder that pauses (garbage collection) may wake up after its lease expired; pass a monotonically increasing fencing token to the storage layer and reject stale tokens.

The Raft paper (Ongaro and Ousterhout, 2014) and [CSG303](../../03_majors/computer_science_general/year_3/CSG303_distributed_systems_ii_consensus_replication/README.md) cover the algorithm.

## 14. Unique IDs and time

| Scheme | Size | Sortable by time | Coordination | Notes |
|---|---|---|---|---|
| Database auto-increment | 64-bit | Yes | Central | Simple; leaks business volume; a bottleneck when sharded |
| UUID v4 | 128-bit | No | None | Random; poor index locality in B-trees |
| UUID v7 (RFC 9562, 2024) | 128-bit | Yes (ms timestamp prefix) | None | Good default for new systems |
| Snowflake-style | 64-bit | Roughly | Worker IDs assigned once | Twitter (2010): 41-bit ms timestamp (~69 years), 10-bit machine ID (1,024 machines), 12-bit sequence (4,096 IDs per ms per machine) |
| Hash of content | varies | No | None | Deduplication; collisions must be handled |

**Clocks.** Wall clocks on different machines disagree by milliseconds or more, so never order events across machines by timestamp alone. Use a single sequencer per ordered stream (per chat, per order), logical or hybrid logical clocks, or a system with bounded clock uncertainty (Spanner's TrueTime).

## 15. Observability

**What to measure.** Google's SRE book names four golden signals: **latency, traffic, errors, saturation**. The RED method (rate, errors, duration) suits request-driven services; the USE method (utilisation, saturation, errors) suits resources such as CPUs, disks and queues.

**Three tools.**
- **Metrics** for dashboards and alerts (Prometheus-style time series, histograms for latency; never average latencies across hosts).
- **Logs** for detail, structured as JSON with a request ID.
- **Traces** for where time goes across services (OpenTelemetry is the vendor-neutral standard).

**SLOs make it a design input.** An availability SLO of 99.9% allows 43.2 minutes of failure per 30 days; 99.99% allows 4.3 minutes. Alert on error-budget burn rate, not on every spike. For AI systems, add token usage, cost per request, time to first token, and evaluation scores ([AIE403](../../03_majors/ai_engineering/year_4/AIE403_llmops_observability_guardrails_cost_and_latency/README.md)).

**Interview line.** "Each service emits RED metrics and traces with the request ID; the pager fires on SLO burn rate; payments additionally have a reconciliation mismatch metric, because a correct-looking dashboard can hide lost money."

## 16. Vector databases

**What.** Stores embeddings (vectors of, say, 384–3,072 numbers) and finds the nearest ones to a query vector. Used for semantic search, RAG, recommendations and deduplication.

**Index types.**

| Index | Idea | Trade-off |
|---|---|---|
| Flat (brute force) | Compare with every vector | Exact; fine up to ~1 million vectors on a GPU or with batching (**rough**) |
| HNSW (Malkov and Yashunin, 2016) | Multi-layer proximity graph, greedy search | High recall and low latency; memory-hungry; slow to build; deletes are awkward |
| IVF | Cluster vectors; search only the nearest clusters | Less memory; recall depends on how many clusters you probe |
| Product quantisation (PQ) | Compress each vector into short codes | 10–50× less memory; lower recall unless you rerank with full vectors |

**Memory arithmetic.** 10 million vectors × 768 dimensions × 4 bytes = 30.7 GB of raw float32, before graph links (HNSW adds roughly 2 × M neighbour IDs per vector at the base layer; with M = 16 that is 32 × 4 bytes = 128 bytes each, about 1.3 GB). PQ with 96 one-byte codes stores the same vectors in 0.96 GB.

**Design points.**
- **Recall@k is the quality metric**, measured against exact search on a sample. Tune index parameters to hit a recall target at your p99 latency.
- **Filtering** (tenant, permissions, date) must happen inside the search or with enough over-fetching; filtering the top-10 after search can return nothing.
- **Options.** A dedicated engine (Milvus, Qdrant, Weaviate, Pinecone), a library (FAISS), or an extension in the database you already run (pgvector for PostgreSQL). Below tens of millions of vectors, the extension in your existing database is often the simplest correct answer.
- **Embedding model changes** mean re-embedding everything; version your vectors.

## 17. LLM serving

**Two phases.** **Prefill** processes the whole prompt in parallel (compute-bound) and produces the first token. **Decode** generates one token at a time, each step reading all model weights and the KV cache from GPU memory (memory-bandwidth-bound).

**Metrics.** Time to first token (**TTFT**, dominated by queueing + prefill), time per output token (**TPOT**, decode speed), throughput (tokens/s per GPU), and cost per million tokens.

**The KV cache.** For each token in context the model stores a key and a value vector per layer:

`KV bytes per token = 2 × layers × KV heads × head dimension × bytes per value`

| Model (config from the Llama 3 paper, 2024) | Layers | KV heads × head dim | KV per token at 16-bit | 8,192-token context |
|---|---|---|---|---|
| Llama 3 8B | 32 | 8 × 128 | 2 × 32 × 8 × 128 × 2 B = 128 KiB | 1 GiB |
| Llama 3 70B | 80 | 8 × 128 | 2 × 80 × 8 × 128 × 2 B = 320 KiB | 2.5 GiB |

So on GPUs the binding constraint is usually memory: the weights of a 70B model at 16 bits are about 140 GB, more than one 80 GB H100, and every concurrent long conversation needs gigabytes of KV cache on top.

**Bandwidth bound on decode (ideal arithmetic).** An H100 SXM has 80 GB of HBM3 at 3.35 TB/s (NVIDIA). Reading 140 GB of weights takes ≥ 42 ms on one GPU's bandwidth; split across 4 GPUs with tensor parallelism, ≥ ~10 ms per step, so at most ~95 tokens/s for one sequence. **Batching** shares each weight read across many sequences, which is why throughput per GPU rises almost linearly with batch size until compute or KV memory runs out.

**Techniques, with the published evidence.**

| Technique | What it does | Evidence |
|---|---|---|
| Continuous (iteration-level) batching | New requests join and finished ones leave at every decode step | Orca (OSDI 2022): up to 36.9× throughput over FasterTransformer on GPT-3 175B at the same latency |
| Paged KV cache | Allocates KV memory in blocks like virtual-memory pages; near-zero fragmentation; shares blocks between sequences | vLLM / PagedAttention (SOSP 2023): 2–4× throughput over FasterTransformer and Orca at the same latency |
| Prefix caching | Reuses KV cache for a shared prompt prefix (system prompt, documents) | SGLang's RadixAttention (2024); provider "prompt caching" features |
| Prefill/decode disaggregation | Runs the two phases on different GPUs so they stop interfering | DistServe (OSDI 2024): up to 7.4× more requests or 12.6× tighter SLOs |
| Speculative decoding | A small draft model proposes tokens; the large model verifies several at once | Leviathan et al. (ICML 2023): 2–3× faster on T5-XXL with identical outputs |
| Quantisation | 8-bit or 4-bit weights (and KV) | Halves or quarters memory and bandwidth; must be evaluated for quality loss ([MLE404](../../03_majors/machine_learning_engineering/year_4/MLE404_efficient_inference_quantization_distillation/README.md)) |

**Routing.** Send requests that share a prefix to the replica that already holds it (prefix-aware routing); route by model, context length and priority; autoscale on queue depth and KV-cache utilisation, not CPU. Full design: [case study 16](case_studies/16_llm_inference_serving.md).

---

## Sources

All checked 12 Oct 2026.

- Jeff Dean, *Designs, Lessons and Advice from Building Large Distributed Systems*, LADIS keynote (Oct 2009), slide "Numbers Everyone Should Know" — https://www.cs.cornell.edu/projects/ladis2009/talks/dean-keynote-ladis2009.pdf
- Peter Norvig, "Teach Yourself Programming in Ten Years" — https://norvig.com/21-days.html
- Simon Eskildsen, *napkin-math* (numbers re-measured March 2026) — https://github.com/sirupsen/napkin-math
- Colin Scott, "Latency Numbers Every Programmer Should Know" (interactive, extrapolated) — https://colin-scott.github.io/personal_website/research/interactive_latency.html
- Uber, "How Uber Serves Over 40 Million Reads Per Second from Online Storage Using an Integrated Cache" (15 Feb 2024) — https://www.uber.com/blog/how-uber-serves-over-40-million-reads-per-second-using-an-integrated-cache/
- Jay Kreps, "Benchmarking Apache Kafka: 2 Million Writes Per Second (On Three Cheap Machines)" (27 Apr 2014) — https://engineering.linkedin.com/kafka/benchmarking-apache-kafka-2-million-writes-second-three-cheap-machines
- Apache Kafka 4.0 release announcement (18 Mar 2025) — https://kafka.apache.org/blog/2025/03/18/apache-kafka-4.0.0-release-announcement/
- AWS, DynamoDB partition key best practices — https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-partition-key-design.html ; S3 performance — https://docs.aws.amazon.com/AmazonS3/latest/userguide/optimizing-performance.html ; S3 storage classes (durability) — https://aws.amazon.com/s3/storage-classes/
- WhatsApp, "1 million is so 2011" (6 Jan 2012) — https://blog.whatsapp.com/1-million-is-so-2011
- OpenAI on PostgreSQL (Jan 2026), as reported by VentureBeat (23 Jan 2026) — https://venturebeat.com/data/how-openai-is-scaling-the-postgresql-database-to-800-million-users ; Slack, "Scaling Datastores at Slack with Vitess" (2020) — https://slack.engineering/scaling-datastores-at-slack-with-vitess/ ; Discord, "How Discord Stores Trillions of Messages" (2023) — https://discord.com/blog/how-discord-stores-trillions-of-messages
- Eisenbud et al., "Maglev: A Fast and Reliable Software Network Load Balancer" (NSDI 2016) — https://research.google/pubs/maglev-a-fast-and-reliable-software-network-load-balancer/
- Nishtala et al., "Scaling Memcache at Facebook" (NSDI 2013) — https://www.usenix.org/conference/nsdi13/technical-sessions/presentation/nishtala
- Netflix Open Connect — https://openconnect.netflix.com/en/
- Hotstar at AWS re:Invent 2019 (CMY302), report by Classmethod — https://dev.classmethod.jp/articles/reinvent-2019-cmy302/
- Karger et al., "Consistent Hashing and Random Trees" (STOC 1997) — https://dl.acm.org/doi/10.1145/258533.258660 ; DeCandia et al., "Dynamo" (SOSP 2007) — https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf ; Lamping and Veach, "A Fast, Minimal Memory, Consistent Hash Algorithm" (2014) — https://arxiv.org/abs/1406.2294
- Elasticsearch, near real-time search — https://www.elastic.co/guide/en/elasticsearch/reference/current/near-real-time.html
- Stripe, "Scaling your API with rate limiters" (30 Mar 2017) — https://stripe.com/blog/rate-limiters ; Cloudflare, "How we built rate limiting capable of scaling to millions of domains" (Jun 2017) — https://blog.cloudflare.com/counting-things-a-lot-of-different-things/ ; RFC 6585 — https://www.rfc-editor.org/rfc/rfc6585
- Stripe, "Designing robust and predictable APIs with idempotency" (2017) — https://stripe.com/blog/idempotency ; Stripe API idempotent requests — https://docs.stripe.com/api/idempotent_requests ; IETF draft Idempotency-Key header — https://datatracker.ietf.org/doc/draft-ietf-httpapi-idempotency-key-header/ ; Razorpay payout idempotency — https://razorpay.com/docs/api/x/payout-idempotency/
- Ongaro and Ousterhout, "In Search of an Understandable Consensus Algorithm" (USENIX ATC 2014) — https://raft.github.io/raft.pdf ; etcd system limits — https://etcd.io/docs/v3.5/dev-guide/limit/
- RFC 9562 (UUIDs) — https://www.rfc-editor.org/rfc/rfc9562 ; Twitter Snowflake README (2010) — https://github.com/twitter-archive/snowflake/tree/snowflake-2010
- Google SRE book, "Monitoring Distributed Systems" — https://sre.google/sre-book/monitoring-distributed-systems/ ; OpenTelemetry — https://opentelemetry.io/docs/
- Malkov and Yashunin, HNSW — https://arxiv.org/abs/1603.09320 ; pgvector — https://github.com/pgvector/pgvector ; FAISS — https://github.com/facebookresearch/faiss
- Llama 3 model configurations: "The Llama 3 Herd of Models" (2024) — https://arxiv.org/abs/2407.21783 ; NVIDIA H100 specifications — https://www.nvidia.com/en-us/data-center/h100/
- Yu et al., "Orca" (OSDI 2022) — https://www.usenix.org/conference/osdi22/presentation/yu ; Kwon et al., "Efficient Memory Management for Large Language Model Serving with PagedAttention" (SOSP 2023) — https://arxiv.org/abs/2309.06180 ; Zheng et al., "SGLang" (2024) — https://arxiv.org/abs/2312.07104 ; Zhong et al., "DistServe" (OSDI 2024) — https://arxiv.org/abs/2401.09670 ; Leviathan et al., "Fast Inference from Transformers via Speculative Decoding" (ICML 2023) — https://arxiv.org/abs/2211.17192

_Last reviewed: 2026-10_
