# SWE401 · Labs and projects

Design work is graded on documents plus evidence. Every design states its assumptions in a table, and every number either comes from a cited source or is marked as an assumption. Systems such as UPI, IRCTC and WhatsApp are used only with their public facts; any internal detail you need is an **illustrative assumption** and must be labelled. Load tests run on your own infrastructure (local Docker, kind, or a small cloud account with a budget alarm).

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Requirements and SLOs | Turn 3 one-line product requests into requirements, SLOs, non-goals and an access-pattern table | Three one-page requirement sheets, peer-reviewed | 3 h |
| 2 · Estimation drills (AI off, then compare) | 10 timed estimates (QPS, storage, bandwidth, fleet, cost); then compare with two AI assistants' answers | Your estimates with assumptions, the AI answers graded against a rubric, and the errors you found | 4 h |
| 3 · Same data, three databases | Model a chat-history workload in Postgres, ScyllaDB/Cassandra and MongoDB; run the same read/write mix | Schema per store, p99 and throughput at 3 load levels, and a recommendation tied to access patterns | 6 h |
| 4 · Hot keys and rebalancing | Simulate a hot partition (a viral link or a popular train); apply key splitting and request coalescing; add nodes with and without virtual nodes | Load distribution plots, p99 before/after, data moved during rebalancing | 5 h |
| 5 · Cache races and herds | Reproduce a stale-set race and a thundering herd; fix with leases/versioning and request coalescing | Reproduction scripts, fixes, and DB load during a cold start before/after | 4 h |
| 6 · Idempotent consumers and delayed jobs | Partitioned order-events topic; idempotent consumer; seat-hold expiry with a delay mechanism | Duplicate-injection test with zero double effects; expiry accuracy under 1 million holds | 5 h |
| 7 · Search and geospatial | Index 1 million product titles; nearby-partner search with H3 vs naive scan | Query latency tables and index sizes | 4 h |
| 8 · Idempotency and reconciliation | Idempotent payment API with stored responses; a reconciliation job against a simulated bank settlement file with planted mismatches | All 1,000 duplicate requests return the same result; every planted mismatch reported with its category | 5 h |
| 9 · Surge admission | Waiting room + token bucket + inventory holds for a 10-second burst at 10× normal load | Goodput, fairness (order of admission vs arrival), p99 for admitted users, rejection latency | 6 h |
| 10 · Failure and cells | Availability calculation for your P2 design; then split it into cells and run a cell-failure drill | Availability math, blast-radius comparison, drill results | 4 h |

## Projects

### P1 · Shortener design doc with a working prototype (L1, ~6 hours)

**Real-world inspiration:** link shorteners used in SMS campaigns, OTP-adjacent messages and social media, where redirects must be fast and abuse must be controlled.

**What to build:** a design document (4–6 pages) for a shortener at 100 million new links a month and 50,000 redirects per second at peak (stated assumptions), plus a single-node prototype of the redirect path.

**Acceptance criteria:**
- The doc has requirements, SLOs, an estimates table (QPS, storage for 5 years, bandwidth, cache size), an ID-generation choice with two rejected alternatives, data model, caching and an abuse section.
- Prototype serves redirects at p99 < 10 ms at 5,000 requests/s on a laptop with a Zipf key distribution (k6 output).
- One reviewer from another team signs off after at most one revision; all comments and responses are included.

**Stretch goals:** custom aliases with collision handling; a privacy-preserving analytics pipeline.

**What it proves to an employer:** you can produce a complete, quantified design and back the hot path with a measurement.

### P2 · Messaging backend at a scale you can test (L2, ~15 hours)

**Real-world inspiration:** WhatsApp, Discord and Slack. Their public engineering material describes connection gateways, per-channel storage partitions and request coalescing. Scale numbers here are **illustrative**.

**What to build:** a design doc for 1:1 and group messaging at 500 million daily users (assumptions stated), and a scaled-down implementation: connection gateway (WebSocket), message service, per-conversation ordering, delivery and read receipts, offline queue with push stub, group fan-out with a size limit, message storage partitioned by conversation and time bucket.

**Acceptance criteria:**
- Per-conversation ordering holds under concurrent senders (property test over 10,000 generated message interleavings).
- 50,000 concurrent WebSocket connections on one gateway node (or the documented maximum for your machine) with memory per connection reported.
- Killing a message-service instance mid-send loses no acknowledged message and duplicates none visible to clients (client-side dedup by message ID allowed and documented).
- Group fan-out to a 1,000-member group completes with p99 < 1 s at a stated rate.
- The design doc's estimates are compared with the measured per-node numbers, and the fleet size is recomputed from them.

**Stretch goals:** presence with eventual consistency and a bound on staleness; a media path with presigned uploads to object storage.

**What it proves to an employer:** you can design and build the core of a real-time system and reconcile paper estimates with measurements.

### P3 · Surge-proof booking or payments platform: full design review (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** Tatkal ticket openings (IRCTC's record: 28,434 tickets in one minute) and UPI-scale payments (24.07 billion transactions in September 2026). Internal designs of these systems are not public; your design is an **illustrative** system inspired by their public scale.

**What to build:** choose track A (surge booking) or track B (payment service provider backend handling 5% of UPI-like volume). Deliver:
1. A full design document (10–15 pages): requirements, SLOs, estimates, architecture, data model and partitioning, consistency per operation, failure modes (at least 8), multi-AZ/region and data-residency choices, cost model, rollout plan.
2. A prototype of the two riskiest paths (track A: admission + inventory holds; track B: idempotent debit with timeout, status check and reversal + reconciliation).
3. A design review: a 45-minute panel with two reviewers using your pre-read, plus your written responses and ADRs for every changed decision.

**Acceptance criteria:**
- Track A: at 10× the record rate for 60 seconds on a scaled-down fleet, zero oversold seats across 10 runs, admitted users' p99 < 500 ms, rejected users answered in < 100 ms, and admission order within a documented fairness bound.
- Track B: across 100,000 simulated transactions with injected bank timeouts, duplicates and late callbacks, zero money created or lost (ledger balances to zero), every timed-out debit resolved by status check or reversal, and reconciliation flags 100% of planted mismatches.
- Failure drills for at least 3 of the documented failure modes, with observed behaviour vs designed behaviour.
- Cost per 1,000 bookings or payments computed from measured per-node throughput.
- An "AI adversary" appendix: risks raised by two AI reviewers, which were real, which were wrong, and how you checked.

**Stretch goals:** cell-based deployment with a cell-failure drill; a chaos run with network partitions between services.

**What it proves to an employer:** you can design a system where correctness, surges and money all matter, defend it in review, and prove its riskiest parts work. This is the core of senior system-design interviews and real senior work.

## Feeds into

- [SWE501 Frontier Seminar](../../year_5/SWE501_frontier_seminar_agentic_software_engineering/README.md): design reasoning is one of the open problems for AI agents.
- [CAR401 Career Lab II](../../../../05_shared_years_3_to_5/CAR401_career_lab_ii_interviews_system_design_and_ai/README.md): mock high-level design interviews use these case studies.
- [THS501 Thesis or Capstone I](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) and the [SWE flagship industry project](../../../../06_career_and_market_readiness/05_industry_projects/SWE_software_engineering.md): P3's design doc is a strong capstone starting point.
- [OV10 FinTech Systems Engineering](../../../../04_overlaps/OV10_fintech_systems_engineering/README.md): track B goes much deeper there.
