# BE304 · Labs and projects

Labs run locally with Docker Compose: a 3-broker Kafka cluster in KRaft mode, RabbitMQ 4.x, LocalStack or real SQS, PostgreSQL 18 and Debezium. A shared crash harness kills processes at random points and then checks invariants, so a lab is graded on what survives failure, not only on the happy path. Lab 4 and the live failure-analysis exam are done without AI assistants.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Queues vs logs | Show redelivery after a consumer crash (RabbitMQ, SQS) and replay from offset zero (Kafka) | Scripts, logs and a one-page comparison | 4 h |
| 2 · Broker practice | Topic exchange routing with tuned prefetch; SQS FIFO parallelism by message group; transactional enqueue with `SKIP LOCKED` | Throughput and fairness numbers; a per-group ordering check that passes | 6 h |
| 3 · Kafka durability and rebalances | Kill brokers under `acks=1` vs `acks=all` with `min.insync.replicas=2`; measure rebalance pauses with the classic and KIP-848 protocols | Loss counts per setting over 10 runs; pause-time plots | 8 h |
| 4 · Idempotent consumers (no AI) | Place acks and commits correctly; deduplicate by message ID; handle out-of-order versions | Crash-harness report: 200 crash points, zero lost and zero duplicated effects | 6 h |
| 5 · Outbox and CDC | Polling relay and Debezium relay for the same outbox; restart the database, the connector and Kafka | Zero-loss, zero-phantom proof over 1M events; replication-slot lag graph | 8 h |
| 6 · Saga | Orchestrated booking saga with compensations and a 24-hour timeout (simulated clock) | A test matrix covering failure at every step, with expected and observed end states | 6 h |
| 7 · Retry ladder and DLQ | Three delayed retry levels and a DLQ; a replay tool with idempotency | Replay of 50,000 dead-lettered messages after a bug fix, with zero duplicate effects | 5 h |
| 8 · Lag autoscaling | Autoscale consumers on lag with KEDA in kind; protect a rate-limited downstream | Recovery-time plot from a 1M-message backlog; downstream never exceeds its limit | 5 h |
| 9 · Schemas and tracing | Schema registry with backward compatibility in CI; trace context in headers across three async hops | CI run rejecting a breaking schema; one end-to-end trace from API call to final effect | 5 h |

## Projects

### P1 · Deadline-bound document delivery (L1, ~6 hours)

**Real-world inspiration:** Indian brokers must send contract notes to clients every trading day. Zerodha reported delivering over 1.5 million PDF contract notes by email in under 25 minutes after a backend revamp ([Zerodha, Feb 2024](https://zerodha.com/z-connect/updates/1-5-million-contract-notes-sent-in-less-than-25-minutes)). Zerodha has not published its design; the version here is your own, scaled to a laptop.

**What to build:** a job pipeline that takes 100,000 synthetic "contract note" records and does three things for each: renders a PDF, "signs" it (a hash stands in for a real signature), and sends it to a local SMTP sink. Use a queue (RabbitMQ, SQS or a Postgres-backed queue) and a pool of workers. Add progress tracking, retries with backoff for transient SMTP errors, and a DLQ for permanent failures.

**Acceptance criteria:**
- All 100,000 documents are delivered within 10 minutes on a 4-core laptop. A progress dashboard or log shows the throughput over time.
- With 2% of sends failing transiently and 0.1% failing permanently (injected), every transient failure eventually succeeds, and every permanent failure lands in the DLQ with its reason.
- Killing workers at random 20 times during a run causes zero duplicate emails. The SMTP sink counts sends per document ID.
- Workers shut down gracefully on SIGTERM and finish or release their current job.
- A README states the delivery guarantee you provide and where it would break.

**Stretch goals:** prioritize late-running batches automatically; resume from a crash of the coordinator; compare a Kafka share group against your queue for the same job.

**What it proves to an employer:** you can run a large batch against a hard deadline without losing or duplicating work. Every regulated industry has this job.

### P2 · Order events with outbox, CDC and idempotent consumers (L2, ~15 hours)

**Real-world inspiration:** the transactional outbox with change data capture ([Debezium outbox event router](https://debezium.io/documentation/reference/stable/transformations/outbox-event-router.html)) is the standard way to publish domain events reliably from a relational database. Uber's retry-topic ladder ([Uber, 2018](https://www.uber.com/blog/reliable-reprocessing/)) shows how to keep failures from blocking live traffic.

**What to build:**
- **Order service:** writes orders and outbox rows in one PostgreSQL transaction.
- **Relay:** Debezium to Kafka, keyed by order ID.
- **Consumers:** a search indexer (OpenSearch or a simple inverted index), a notification sender and a daily-sales projection in its own database.
- **Consumer correctness:** each consumer is idempotent, uses an inbox table or natural idempotency, and has a retry ladder with a DLQ.
- **Schemas:** event schemas are registered with backward compatibility enforced.

**Acceptance criteria:**
- **No loss, no phantoms:** over 1 million orders, with the crash harness killing the order service, Postgres, Debezium, Kafka brokers and consumers at random (at least 300 kill events), every committed order appears exactly once in every downstream store. No event appears for an order that was rolled back.
- **Ordering:** the status history of each order downstream matches the source order of transitions in 100% of orders, checked by a verifier.
- **Lag recovery:** after a 15-minute consumer outage under 2,000 orders/s, lag returns to under 5 seconds within 10 minutes.
- **Poison handling:** 100 malformed events go to the DLQ without blocking their partitions; a fix-and-replay clears them with no duplicate notifications.
- **Schema evolution:** a v2 event with a new optional field rolls out while v1 consumers keep working; a deliberately breaking change is rejected in CI.

**Stretch goals:** compare the polling relay against CDC on throughput and failure behaviour; add end-to-end latency SLOs with alerts; move one consumer to a Kafka share group.

**What it proves to an employer:** you can build event-driven integration that is actually reliable, and prove it under failure.

### P3 · Travel booking platform with sagas and event-sourced bookings (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** travel aggregators sell trips that combine train or flight seats, hotel rooms and a payment from different providers, any of which can fail or time out. None of them has published a design; this is an **illustrative scenario** built on the published saga pattern ([Garcia-Molina and Salem, 1987](https://www.cs.cornell.edu/andru/cs711/2002fa/reading/sagas.pdf)).

**What to build:**
- **Booking service:** booking is an event-sourced aggregate, with projections for "my trips" and an operations dashboard.
- **Orchestrated saga:** hold seat → hold room → capture payment → confirm both, with compensations, timeouts and a manual-review queue for stuck bookings.
- **Simulated providers:** they time out, fail, succeed late and occasionally send duplicate callbacks.
- **Plumbing:** outbox-based publishing, idempotent handlers everywhere, retry ladders with DLQs and a replay tool.
- **Operations:** lag-based autoscaling, backpressure towards a provider with a strict rate limit, and full tracing across all hops.

**Acceptance criteria:**
- **Saga correctness:** over 100,000 bookings, with random failures and crashes of every service (at least 500 kill events), every booking ends either fully confirmed or fully compensated within 5 minutes, or sits in the manual-review queue with a reason. There are zero double charges and zero charges without a confirmed booking (verified by reconciling against the simulated payment provider).
- **Event store:** concurrent commands on one booking are serialized by stream version, and a test with 50 concurrent commands shows no lost events.
- **Projections:** rebuilding all projections from 10 million events takes under 10 minutes, and the rebuilt state matches the live state exactly.
- **Backpressure:** the rate-limited provider never receives more than its limit, even during a 1-hour backlog drain.
- **Schema evolution:** a booking event changes shape (v1 → v2) with upcasting, and old streams still rebuild correctly.
- **Observability:** a trace shows one booking across every service and broker hop, with the time spent waiting in each queue.
- **Write-up:** a design document with the saga state machine, a compensation table, a failure-mode table and an event catalogue, plus a post-mortem of the worst bug you found with your own chaos tests.

**Stretch goals:** reimplement the orchestrator on a durable execution engine (Temporal, Restate or DBOS) and compare code size and failure handling (a preview of BE501); add crypto-shredding for personal data in events.

**What it proves to an employer:** you can design, build and operate a multi-service workflow whose correctness survives real failures. This is senior-level backend work.

## Feeds into

- [BE404 Microservices, Service Mesh and Platform APIs](../../year_4/BE404_microservices_service_mesh_and_platform_apis/README.md): event contracts and cross-service observability.
- [BE401 Payments-Grade Systems](../../year_4/BE401_payments_grade_systems_transactions_idempotency/README.md): outbox, sagas and reconciliation for money.
- [BE501 Frontier Seminar](../../year_5/BE501_frontier_seminar_durable_execution_serverless/README.md): durable execution as the next step after hand-built sagas.
- [OV02B Event-Driven Serverless Backends](../../../../04_overlaps/OV02_cloud_native_backend/OV02B_event_driven_serverless_backends/README.md) and [DEN303 Streaming Systems](../../../data_engineering/year_3/DEN303_streaming_systems_kafka_and_flink/README.md).
