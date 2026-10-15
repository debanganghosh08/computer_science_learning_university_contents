# BE · Backend Engineering: interview question bank

| Role and market | Levels | Practise with | Score with |
|---|---|---|---|
| [BE role page](../../01_market_map/roles/BE_backend_engineering.md) | NG → Mid → Sr | [Mock kit](../how_to_run_a_mock_with_any_llm.md) · [Day 2 simulation](../simulation_days.md#2-day-2-backend-engineer-sde-2-mid-level) | [Rubrics](../rubrics.md) |

Backend loops test whether you can keep data correct when everything around it fails: retries, concurrency, partial outages, slow queries and migrations. AI assistants write handlers and queries quickly; interviews therefore lean on the parts they get subtly wrong.

## 1. The typical loop

| Round | Duration | What it tests | AI policy you may meet | Mock brief |
|---|---|---|---|---|
| Online assessment | 60–90 min | DSA, sometimes SQL | AI-off, proctored | Day 1 OA prompt |
| Coding | 45–60 min | DSA with a scale twist (streams, top-k, rate limits) | AI-off | Kit 4.1 |
| Low-level design / machine coding | 60–120 min | Rate limiter, cache, booking, idempotent endpoints; runnable code in India | AI-off | Kit 4.10 backend variant |
| System design | 60 min | Data model, consistency, idempotency, failure handling, capacity | AI-off | Kit 4.3 |
| Database deep dive | 45 min | Indexes, plans, isolation, migrations | AI-off | Day 2 deep-dive brief |
| AI-assisted coding or AI code review | 25–60 min | Catching AI errors in realistic backend code | AI-on (Canva expects it for backend roles, [Jun 2025](https://www.canva.dev/blog/engineering/yes-you-can-use-ai-in-our-interviews/)) | Kit 4.2 |
| Behavioural / HM | 45 min | Incidents, trade-offs, ownership | AI-off | Kit 4.11, 4.12 |

**Level differences.** NG: coding plus an API or LLD round. Mid (SDE-2): system design and the database round decide the level. Sr: design under ambiguity, migrations, multi-team trade-offs.

## 2. How to use this bank

Answer aloud with a timer, then open the guide. Run any question as a mock by adding `QUESTION: <text>` to the matching brief. Tags show the lowest level at which a question is common.

## 3. Questions

### Coding

**Q1 · NG · Merge event streams.** Merge k sorted streams of events (by timestamp) into one sorted output, reading lazily.

<details><summary>Answer guide</summary>

- **Testing:** heaps, iterators, memory awareness.
- **Strong answer:** min-heap of (timestamp, stream index, event) seeded with the head of each stream; pop, emit, push that stream's next. O(N log k) time, O(k) memory. Break ties deterministically (stream index). Handle empty and exhausted streams.
- **Common mistakes:** concatenating and sorting everything (O(N log N) and full memory).
- **Follow-ups:** streams can deliver late events up to 5 seconds out of order (watermarks, a small reorder buffer); one stream stalls.
</details>

**Q2 · Mid · Consistent hashing.** Implement a ring that maps keys to nodes with virtual nodes; support add and remove node.

<details><summary>Answer guide</summary>

- **Testing:** data-distribution reasoning.
- **Strong answer:** hash each node to V points on a ring stored in a sorted array or tree; a key maps to the first point clockwise (binary search, wrap around). Adding a node moves about 1/N of keys; virtual nodes smooth load and allow weights. Use a stable hash (not a language's randomised hash).
- **Common mistakes:** `hash(key) % N`, which remaps almost every key when N changes.
- **Follow-ups:** replication to the next R distinct physical nodes; measure balance (standard deviation of keys per node).
</details>

**Q3 · Mid · Token bucket.** Implement a thread-safe token-bucket limiter: capacity C, refill R tokens per second, `try_acquire(n)`.

<details><summary>Answer guide</summary>

- **Testing:** time-based logic, concurrency.
- **Strong answer:** store tokens (float) and last refill time; on each call compute elapsed × R, cap at C, then subtract if enough. Lazy refill avoids a background thread. Use a monotonic clock. Guard with a lock or an atomic compare-and-set loop. Test with an injected fake clock.
- **Common mistakes:** wall-clock time (jumps with NTP); a timer thread per bucket; integer truncation losing tokens.
- **Follow-ups:** per-user buckets for 10 million users (memory, expiry); distributed limit across servers (central store with atomic script, or local buckets with a share of the global rate).
</details>

**Q4 · Mid · Heavy hitters in the last five minutes.** Return the top 10 API keys by request count over a sliding 5-minute window, queried every second.

<details><summary>Answer guide</summary>

- **Testing:** windowed aggregation trade-offs.
- **Strong answer:** ring buffer of 300 one-second buckets, each a hash map of counts, plus a running total map updated on bucket expiry; top-k by heap over the total map on query, or maintain approximate structures (Count-Min Sketch plus heap) when keys are many. State accuracy vs memory trade-off.
- **Common mistakes:** storing every request timestamp; recomputing from scratch every second over all buckets.
- **Follow-ups:** distributed across 20 servers (local aggregation, periodic merge); exactness required for billing.
</details>

### Low-level design

**Q5 · Mid · Idempotent payment endpoint.** Design `POST /payments` so client retries never double-charge.

<details><summary>Answer guide</summary>

- **Testing:** correctness under retries.
- **Strong answer:** client sends an `Idempotency-Key`; server stores (key, request hash, status, response) with a unique constraint; first request inserts "in progress" then calls the gateway; concurrent duplicates wait or get 409; completed duplicates get the stored response; same key with different body is rejected. Keys expire after a retention window. The call to the gateway also uses an idempotency key. Reconcile against gateway reports daily.
- **Common mistakes:** check-then-insert without a unique constraint (race); storing only success responses.
- **Follow-ups:** the server crashes after charging but before saving the response; how does reconciliation fix it?
</details>

**Q6 · Mid · Seat booking with holds.** Users pick seats on a train or in a cinema (illustrative scenario); seats are held for 10 minutes during payment.

<details><summary>Answer guide</summary>

- **Testing:** concurrency, expiry, state machines.
- **Strong answer:** seat states available → held(user, expires_at) → booked; atomic conditional update to hold (`WHERE state='available' OR expires_at < now()`); payment success books, failure or expiry releases; a sweeper is not required for correctness if expiry is checked on read. Unique constraint on (show, seat) in bookings. Handle payment completing after hold expiry (refund or honour if still free).
- **Common mistakes:** in-memory locks on one server; relying on a cron job to free seats.
- **Follow-ups:** a popular show with 100,000 users at opening (queue, virtual waiting room); group bookings that must be adjacent.
</details>

**Q7 · NG · Design a REST API for orders.** Create, list with filters, cancel.

<details><summary>Answer guide</summary>

- **Testing:** API design basics.
- **Strong answer:** resources and verbs (`POST /orders`, `GET /orders?status=&cursor=`, `POST /orders/{id}/cancel` as an action), correct status codes (201, 400, 404, 409 for invalid state), cursor pagination, validation errors with field details, idempotency for creates, versioning strategy, authentication and per-user authorisation (users see only their orders).
- **Common mistakes:** `GET /cancelOrder`; offset pagination for large data; leaking other users' orders by ID.
- **Follow-ups:** partial cancellation of items; backwards-compatible field changes.
</details>

### Database deep dive

**Q8 · NG · Composite indexes.** Why does an index on `(user_id, created_at)` help `WHERE user_id = ? AND created_at > ?` but not `WHERE created_at > ?` alone?

<details><summary>Answer guide</summary>

- **Testing:** B+tree mental model.
- **Strong answer:** a B+tree on (a, b) is sorted by a, then b within each a. Equality on a narrows to a contiguous range, then b is a range scan inside it. Without a condition on a, matching rows are scattered across all a values (a skip scan may help in some engines, but generally not). Also covers `ORDER BY created_at` per user. Mention covering indexes and the write cost of each index.
- **Common mistakes:** "the database uses any index with the column".
- **Follow-ups:** read an `EXPLAIN` output and identify a sequential scan; when is a sequential scan correct?
</details>

**Q9 · Mid · Isolation anomalies.** Explain lost update and write skew with concrete tables, and how to prevent each in PostgreSQL.

<details><summary>Answer guide</summary>

- **Testing:** transaction semantics.
- **Strong answer:** lost update: two transactions read a balance of 100 and each write 100 − 10; prevent with atomic `UPDATE ... SET balance = balance - 10`, `SELECT ... FOR UPDATE`, or optimistic version checks. Write skew: two on-call doctors each see the other on call and both go off call; each updates a different row, so row locks do not conflict. Prevent with `SERIALIZABLE` isolation (with retries on serialization failures), or by locking the set (`FOR UPDATE` on both rows) or materialising the constraint. Note PostgreSQL's REPEATABLE READ prevents lost updates by aborting but not write skew.
- **Common mistakes:** believing REPEATABLE READ prevents all anomalies.
- **Follow-ups:** cost of SERIALIZABLE under contention; how to write the retry loop.
</details>

**Q10 · Mid · Deep pagination is slow.** `ORDER BY created_at DESC LIMIT 20 OFFSET 200000` takes seconds. Why, and what instead?

<details><summary>Answer guide</summary>

- **Testing:** query execution understanding.
- **Strong answer:** OFFSET still reads and discards 200,000 rows. Use keyset (cursor) pagination: `WHERE (created_at, id) < (?, ?) ORDER BY created_at DESC, id DESC LIMIT 20` with an index on `(created_at, id)` (plus filter columns first); return an opaque cursor. Trade-off: no jumping to page N; stable under inserts.
- **Common mistakes:** cursor on `created_at` alone (ties skip or repeat rows).
- **Follow-ups:** filter by user and status as well; which index?
</details>

**Q11 · Mid · Zero-downtime migration.** Rename `users.phone` to `phone_e164` and make it NOT NULL on a live 200-million-row table.

<details><summary>Answer guide</summary>

- **Testing:** expand–contract migrations.
- **Strong answer:** expand: add the new nullable column; deploy code that writes both; backfill in batches with throttling; verify counts; add the NOT NULL constraint safely (in PostgreSQL, add a `CHECK (col IS NOT NULL) NOT VALID`, then `VALIDATE CONSTRAINT`, which avoids a long exclusive lock); switch reads; contract: stop writing the old column, drop it later. Each step is reversible until the drop.
- **Common mistakes:** a single `ALTER TABLE ... RENAME` that breaks running code; one giant backfill transaction.
- **Follow-ups:** how do you handle rows written during backfill? How do you roll back after the read switch?
</details>

**Q12 · Sr · PostgreSQL or a wide-column store?** A messaging feature: 2 billion messages a month, read by conversation, newest first.

<details><summary>Answer guide</summary>

- **Testing:** choosing storage from access patterns.
- **Strong answer:** list access patterns first (by conversation ID and time; by user inbox; search). A wide-column or key-value store partitioned by conversation with time-sorted clustering fits the main pattern and scales writes linearly; PostgreSQL with partitioning and careful indexing can go far and keeps transactions and ad-hoc queries. Consider hot partitions (huge group chats: bucket by time), retention, secondary indexes, operational skill of the team, and cost. Recommend with numbers and a migration path.
- **Common mistakes:** choosing by fashion; ignoring hot partitions.
- **Follow-ups:** search across messages; deletes for compliance.
</details>

### Distributed systems

**Q13 · Mid · The dual-write problem.** An order service writes to its database and publishes `OrderCreated` to a broker. What goes wrong and how do you fix it?

<details><summary>Answer guide</summary>

- **Testing:** reliable messaging.
- **Strong answer:** if the process dies between the two writes, the database and the broker disagree. Transactional outbox: insert the event into an `outbox` table in the same transaction as the order; a relay (polling or change data capture) publishes and marks it sent; consumers must be idempotent because the relay can publish twice. Ordering per aggregate via partition key.
- **Common mistakes:** "publish first, then write"; two-phase commit across database and broker as the default.
- **Follow-ups:** outbox table growth; how consumers deduplicate.
</details>

**Q14 · Mid · "Our pipeline is exactly-once." What does that actually mean?**

<details><summary>Answer guide</summary>

- **Testing:** delivery semantics precision.
- **Strong answer:** networks give at-least-once or at-most-once delivery; "exactly-once" is achieved as exactly-once *effects* by combining at-least-once delivery with idempotent or transactional processing. Kafka's idempotent producer and transactions give exactly-once within Kafka (read-process-write to Kafka topics); side effects outside Kafka (emails, payments, other databases) still need idempotency keys or deduplication tables.
- **Common mistakes:** believing a broker setting makes external side effects exactly-once.
- **Follow-ups:** design the dedup table and its retention.
</details>

**Q15 · Sr · Saga for order, payment and inventory.**

<details><summary>Answer guide</summary>

- **Testing:** distributed transactions without 2PC.
- **Strong answer:** steps with compensations (reserve inventory ↔ release; charge ↔ refund; confirm order). Orchestration (a coordinator with explicit state, easier to reason about and monitor) vs choreography (events, looser coupling, harder to trace). Persist saga state; time-outs; idempotent steps and compensations; semantic locks (order "pending"); handle compensation failures (retry, then manual queue).
- **Common mistakes:** assuming compensations always succeed; no saga state store.
- **Follow-ups:** a refund fails for a day; what does the customer see?
</details>

**Q16 · Mid · Cache stampede.** A hot key expires and 5,000 requests hit the database at once.

<details><summary>Answer guide</summary>

- **Testing:** caching failure modes.
- **Strong answer:** request coalescing (single flight: one loader, others wait); early probabilistic refresh before expiry; TTL jitter to avoid synchronised expiry; serve stale while revalidating; protect the database with a concurrency limit. Discuss invalidation strategy (cache-aside with delete on write, versioned keys).
- **Common mistakes:** longer TTL as the only fix.
- **Follow-ups:** cache and database disagree after a failed delete; how do you bound staleness?
</details>

**Q17 · Sr · Distributed lock for a scheduled job.** Only one instance should run the nightly billing job.

<details><summary>Answer guide</summary>

- **Testing:** correctness of locks under pauses.
- **Strong answer:** a lease (lock with TTL) from a coordination service or database; a paused process (GC, network) may lose the lease and still act, so use fencing tokens: a monotonically increasing number checked by the resource being written. Make the job idempotent per billing period so a double run is harmless. Prefer a database row lock or a consensus-backed store (etcd, ZooKeeper) over ad-hoc approaches when correctness matters.
- **Common mistakes:** a lock without expiry (deadlock forever) or with expiry but no fencing.
- **Follow-ups:** the job takes longer than the lease; lease renewal design.
</details>

### System design

**Q18 · Mid · Payments with a third-party gateway.** Checkout, gateway redirect or SDK, webhooks, refunds.

<details><summary>Answer guide</summary>

- **Testing:** money-path design.
- **Strong answer:** payment intent created server-side with idempotency; state machine (created → pending → succeeded/failed → refunded); webhooks verified by signature, processed idempotently, out of order tolerated; status polling as a fallback; a double-entry ledger for internal accounting; daily reconciliation against gateway settlement files; never trust client-side success. PCI scope minimised by using the gateway's hosted fields.
- **Common mistakes:** updating order status from the client redirect; no reconciliation.
- **Follow-ups:** the webhook arrives before your database commit; partial refunds.
</details>

**Q19 · Mid · One-to-one chat with delivered and read receipts.**

<details><summary>Answer guide</summary>

- **Testing:** real-time systems.
- **Strong answer:** persistent connections (WebSocket) to gateway servers; a session registry mapping user → gateway; messages stored durably with per-conversation sequence numbers before acknowledgement; delivery to online users via the gateway, push notification otherwise; receipts as small messages updating per-user read pointers; client-generated message IDs for deduplication; ordering per conversation.
- **Common mistakes:** global ordering; storing receipts per message per user for huge groups.
- **Follow-ups:** multi-device sync; group chats of 1,000 members.
</details>

**Q20 · Sr · Multi-tenant SaaS API with noisy neighbours.**

<details><summary>Answer guide</summary>

- **Testing:** isolation trade-offs.
- **Strong answer:** isolation models (shared tables with tenant ID and row-level security; schema per tenant; database per tenant for large customers); per-tenant rate limits and quotas; workload isolation (separate queues or pools for heavy tenants, cell-based architecture); tenant-aware observability; data residency; migration of a tenant between cells. Cost vs isolation per tier.
- **Common mistakes:** forgetting tenant ID in one query (data leak); one shared queue.
- **Follow-ups:** how do you test that no query ever misses the tenant filter?
</details>

### Debugging and production

**Q21 · Mid · p99 latency spikes every hour, on the hour.**

<details><summary>Answer guide</summary>

- **Testing:** hypothesis-driven debugging.
- **Strong answer:** periodicity suggests scheduled causes: cron or batch jobs sharing the database, cache entries with identical TTLs expiring together, log rotation, certificate or token refresh, garbage collection after hourly loads, a dependency's scheduled task. Correlate with database load, GC logs, cache hit rate; check traces of slow requests for where time goes. Fix the specific cause (jitter, move batch to a replica, throttle).
- **Common mistakes:** scaling up instances without finding the cause.
- **Follow-ups:** the spike persists after jitter; what next?
</details>

**Q22 · Mid · Consumer lag is growing on a queue.**

<details><summary>Answer guide</summary>

- **Testing:** stream processing operations.
- **Strong answer:** check produce rate vs consume rate; per-partition lag (one hot partition vs all); processing time per message (a slow downstream, retries with long backoff, poison messages); consumer group rebalances; number of consumers vs partitions (consumers beyond partition count sit idle). Mitigate: scale consumers up to partition count, batch writes, move poison messages to a dead-letter topic, fix the slow dependency.
- **Common mistakes:** adding consumers beyond the partition count.
- **Follow-ups:** you must catch up 6 hours of backlog without overloading the database.
</details>

**Q23 · Mid · "Timeout acquiring connection from pool."** Diagnose and size the pool.

<details><summary>Answer guide</summary>

- **Testing:** resource sizing, Little's law.
- **Strong answer:** causes: slow queries holding connections, leaks (connections not returned on error paths), long transactions, pool too small for concurrency, or database max connections reached across many instances. Little's law: connections needed ≈ request rate × average time holding a connection. Bigger is not always better: databases degrade with too many active connections; use a pooler (for example PgBouncer) and fix slow queries.
- **Common mistakes:** setting the pool to 500 per instance.
- **Follow-ups:** autoscaling adds instances and exhausts database connections; fix.
</details>

### AI-era review

**Q24 · Mid · The assistant generated this migration for a 500-million-row PostgreSQL table. Would you ship it?**

```sql
ALTER TABLE orders ADD COLUMN status TEXT NOT NULL DEFAULT 'new';
CREATE INDEX idx_orders_status ON orders(status);
```

<details><summary>Answer guide</summary>

- **Testing:** verifying AI output against engine behaviour.
- **Strong answer:** the first statement is fast on PostgreSQL 11 and later (a constant default is stored in metadata, no table rewrite), but confirm the server version. The second takes a lock that blocks writes for the whole build; use `CREATE INDEX CONCURRENTLY`, which cannot run inside a transaction block, so the migration tool must allow that. Question the index itself: a low-cardinality column is a poor index; if queries look for `status = 'new'`, a partial index `WHERE status = 'new'` is smaller and better. Add a lock timeout to fail fast.
- **Common mistakes:** approving because the SQL is valid; or rejecting the first line without knowing version behaviour.
- **Follow-ups:** `CREATE INDEX CONCURRENTLY` failed halfway; what state is the index in and what do you do?
</details>

**Q25 · Mid · Review this AI-generated handler.**

```python
@app.get("/orders")
def list_orders(user_id: str, status: str):
    rows = db.execute(f"SELECT * FROM orders WHERE user_id = '{user_id}' AND status = '{status}'")
    return [{**r, "items": db.execute(f"SELECT * FROM items WHERE order_id = {r['id']}")} for r in rows]
```

<details><summary>Answer guide</summary>

- **Testing:** security and performance review.
- **Strong answer:** (1) SQL built by string formatting: use parameterised queries. (2) `user_id` comes from the request, not the authenticated session, so any user can read others' orders (broken object-level authorisation); derive it from the session. (3) N+1 queries for items: fetch with one query using `WHERE order_id = ANY(...)` or a join. (4) No pagination; `SELECT *` leaks columns and breaks with schema changes. (5) Validate `status` against an allowed set. Suggest tests for each fix.
- **Common mistakes:** fixing injection but missing the authorisation flaw.
- **Follow-ups:** how would you catch these automatically (static analysis rules, authorisation tests in CI)?
</details>

**Q26 · Sr · Product wants an endpoint that uses an LLM to categorise support tickets. Make it production-grade.**

<details><summary>Answer guide</summary>

- **Testing:** integrating a non-deterministic dependency.
- **Strong answer:** asynchronous processing via a queue (not on the request path); strict timeouts, retries with backoff, circuit breaker and a fallback category; structured output validated against a schema with a fixed category list; a labelled evaluation set with accuracy per category and a regression run on every prompt or model change; cost budget per ticket and caching of duplicates; PII minimisation before sending; logging of inputs and outputs with retention rules; human review for low-confidence cases; monitoring of category distribution drift.
- **Common mistakes:** synchronous call in the user request; no evaluation set; trusting free-text output.
- **Follow-ups:** the model provider changes behaviour silently; how do you notice within a day?
</details>

### Behavioural

**Q27 · Mid · Tell me about an incident you handled end to end.**

<details><summary>Answer guide</summary>

- **Testing:** ownership under pressure.
- **Strong answer:** detection and impact; first mitigation and why; communication cadence; root cause found with evidence; action items and their completion; what monitoring now catches it earlier. Blameless framing; your specific role.
- **Common mistakes:** a story where you only watched; no follow-up actions.
- **Follow-ups:** what would you have done if rollback was not possible?
</details>

## Sources

- Canva Engineering, *Yes, You Can Use AI in Our Interviews* (11 Jun 2025): https://www.canva.dev/blog/engineering/yes-you-can-use-ai-in-our-interviews/
- PostgreSQL documentation (checked October 2026): `ALTER TABLE` (fast defaults since version 11), `CREATE INDEX CONCURRENTLY`, transaction isolation: https://www.postgresql.org/docs/current/
- Loop structure: [BE role page](../../01_market_map/roles/BE_backend_engineering.md); company policies: [section README](../README.md#6-company-policies-allowed-required-or-banned).

_Last reviewed: 2026-10_
