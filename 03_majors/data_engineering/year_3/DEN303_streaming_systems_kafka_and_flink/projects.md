# DEN303 · Labs and projects

Everything runs locally with Docker Compose: Kafka 4.x in KRaft mode (3 brokers), Flink 2.x, PostgreSQL, Debezium and MinIO for object storage. A laptop with 16 GB of RAM is enough for every lab. Labs 1, 2 and 6 are done without AI assistants. Every correctness claim is checked against a batch recomputation over the archived topic.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · A log from scratch | File-backed append-only log with offsets, segment rollover and a crash-safe reader | Code and a crash test (100 kills) with no lost or repeated reads | 4 h |
| 2 · Losing acknowledged writes | Kill brokers under different `acks`, `min.insync.replicas` and unclean-election settings | Table of acknowledged-but-lost records per setting, with explanations | 4 h |
| 3 · KRaft and compaction | Fail the active controller; compact a customer-updates topic | Failover timings; before/after offsets showing the latest value per key | 3 h |
| 4 · Producer and consumer semantics | Measure 6 producer configurations; build a consumer that commits offsets inside a PostgreSQL transaction | Throughput/latency table; zero-duplicate proof under crashes | 5 h |
| 5 · Schema evolution | Evolve an Avro or Protobuf order event through 3 versions with old consumers running | Registry compatibility log, consumer outputs per version | 3 h |
| 6 · Watermarks and windows | Event-time windows on Wikimedia edits; reproduce and fix a stalled watermark | Window outputs at 3 lateness settings, late-event counts | 5 h |
| 7 · Crash testing exactly-once | Flink job from Kafka to a transactional Kafka sink and an upsert database sink | Report of 50 random crashes: duplicates and losses per sink | 5 h |
| 8 · Savepoints and upgrades | Change logic and parallelism from a savepoint; break it once by omitting operator UIDs | Working upgrade and the failure analysis | 3 h |
| 9 · Streaming joins | Interval join and temporal join with a versioned dimension | Correctness check against batch as-of joins | 4 h |
| 10 · Debezium CDC | Capture inserts, updates, deletes and a schema change from PostgreSQL; stop the connector and watch slot growth | Rebuilt table diffed with source; slot-growth alert | 4 h |
| 11 · Velocity features | Sliding-window count and sum features with state TTL | p99 latency at 3 rates and state-size measurements | 5 h |
| Game day | Three injected incidents: rebalance storm, idle-partition watermark stall, replication-slot growth | Incident report with timeline, detection signal and fix | 3 h |

## Projects

### P1 · Live edits monitor (L1, ~6 hours)

**Real-world inspiration:** Wikimedia publishes every edit to its wikis as a public server-sent event stream ([EventStreams](https://wikitech.wikimedia.org/wiki/Event_Platform/EventStreams_HTTP_Service)). The service is backed internally by Kafka. Each event's ID carries the Kafka topic, partition and offset, so clients can resume after a disconnect. The server closes connections after 15 minutes and injects canary events that clients must discard, the same problems a production consumer has to handle.

**What to build:** a producer that reads the `recentchange` stream into a Kafka topic keyed by wiki, and a consumer (Python or Flink SQL) that computes edits per wiki per minute by event time. Bot and human edits are counted separately. Results go to a small table or dashboard.

**Acceptance criteria:**
- The producer survives a network drop and the 15-minute server timeout, and resumes from the last event ID without gaps. Prove it by comparing event IDs before and after a forced disconnect. Canary events never reach the topic.
- For a chosen 30-minute window, streaming counts per wiki per minute equal a batch recomputation in DuckDB over the archived topic.
- Late events (event time more than 60 s behind the watermark) are counted in a separate output instead of being dropped silently.
- A README states the delivery semantics end to end and where duplicates could occur.

**Stretch goals:** session windows per editor; a spike detector for edit wars.

**What it proves to an employer:** you can move real events into Kafka and compute correct event-time aggregates, and you can say exactly what your pipeline guarantees.

### P2 · CDC replication into the lakehouse (L2, ~15 hours)

**Real-world inspiration:** most companies replicate operational databases into their analytics platform with log-based change data capture rather than nightly dumps. Debezium is the common open-source tool, and Flink CDC 3.7 (October 2026) builds full pipelines on the same idea.

**What to build:** a PostgreSQL e-commerce database (orders, order items, customers) with a load generator that inserts, updates and deletes rows. Changes flow through Debezium into Kafka, and Flink upserts them into Iceberg tables on MinIO. Include:

- a mid-run schema change (new nullable column);
- a deliberate connector outage;
- a replication-slot monitor;
- a reconciliation job that compares source and target.

**Acceptance criteria:**
- **Row-level correctness:** after 1,000,000 changes and 20 random crashes across Kafka, Debezium and Flink, the Iceberg tables equal the source tables exactly (full diff on primary key and all columns).
- **Latency:** end-to-end p95 latency from source commit to query visibility is under 10 seconds at 500 changes per second, measured with commit timestamps.
- **Schema change:** the new column appears in the target without a manual restart, and historical rows read it as NULL.
- **Outage handling:** during a 30-minute connector stop, an alert fires before the replication slot exceeds a set size. After restart, the pipeline catches up with no loss.
- **Deletes:** source deletes produce deletes in the target, verified by count and by key.

**Stretch goals:** the outbox pattern for one service; time-travel queries comparing the table at two snapshots; compaction of small files written by the stream.

**What it proves to an employer:** you can run near-real-time replication that stays exactly right through crashes, schema changes and outages. Many data platforms depend on this.

### P3 · Real-time payment risk signals (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** payment platforms score transactions within a fraction of a second using velocity features over cards, devices and accounts. Uber describes fraud detection as one of its core real-time use cases (SIGMOD 2021). The payment stream here is synthetic and illustrative. It is modelled on public descriptions of UPI-style flows (payer and payee virtual addresses, merchant category, device, amount), and the generator includes configurable fraud patterns.

**What to build:**

- **Generator:** produces 20,000 events per second with realistic skew (a few very large merchants), out-of-order arrival (up to 2 minutes late) and duplicate retries.
- **Flink job:** computes 8 velocity features (for example, payments per device in the last 10 minutes, distinct payees per payer in 1 hour, amount z-score against the payer's 7-day history) and applies 5 rules. It emits a risk decision with the features that triggered it.
- **Sinks:** decisions go to a transactional Kafka topic; features go to an online store (Redis or PostgreSQL) with an event-time stamp.
- **Batch path:** recomputes the same features from the archived topic for backfills and audits.
- **Operations:** monitoring dashboards, a runbook and a capacity plan.

**Acceptance criteria:**
- **Correctness:** for 1 hour of replayed data, every streaming feature value equals the batch recomputation at the same event time. Allowed differences are listed and explained (for example, events beyond allowed lateness).
- **Exactly-once:** after 50 random crashes of TaskManagers and brokers, no decision is duplicated or lost (checked by event ID).
- **Latency:** p99 from event arrival to decision is under 1 second at 20,000 events per second on stated hardware.
- **State:** state size stays bounded over a 6-hour soak test thanks to TTL, plotted over time.
- **Upgrade:** a new feature is added through a savepoint upgrade with no state loss and no downtime longer than 60 seconds.
- **Operations:** the dashboard shows lag in seconds, watermark lag, checkpoint duration, backpressure and decision rate, each with an alert threshold. A game-day report covers three injected incidents.
- **Write-up:** a design document (keys, windows, state, guarantees, failure modes), a capacity plan for 10× traffic, and a 5-minute recorded demo including a crash and recovery.

**Stretch goals:** shadow-score decisions with a simple model and compare with the rules; a share-group consumer for manual review queues; a cost estimate for running the system on a managed Kafka and Flink service.

**What it proves to an employer:** you can build a stateful, low-latency, exactly-once streaming system, prove that it is correct against batch, and operate it through failures and upgrades. This is the profile hired for payments, fraud and logistics platforms.

## Feeds into

- [DEN403 Data Engineering for AI](../../year_4/DEN403_data_engineering_for_ai_unstructured_data/README.md): streaming freshness for embedding and retrieval indexes.
- [OV10A Payment Systems Engineering](../../../../04_overlaps/OV10_fintech_systems_engineering/OV10A_payment_systems_engineering_upi_cards/README.md) and [OV10B Fraud Detection and Risk Systems](../../../../04_overlaps/OV10_fintech_systems_engineering/OV10B_fraud_detection_and_risk_systems/README.md): P3 is the base system.
- [DEN305 Lakehouse Architecture](../DEN305_lakehouse_architecture_parquet_iceberg_and_delta/README.md): P2's streaming upserts drive the compaction and merge-on-read work.
- [DEN501 Frontier Seminar](../../year_5/DEN501_frontier_seminar_real_time_ai_data_systems/README.md): real-time AI data systems.
