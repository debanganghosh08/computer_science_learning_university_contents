# BE402 · Scalability and Performance: Caching, Sharding and Load

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 7 | 4 (≈ 120 hours) | L3 → L4 | [BE302](../../year_3/BE302_backend_frameworks_and_service_internals/README.md) (also uses [BE303](../../year_3/BE303_data_modeling_and_storage_for_backends_postgres/README.md)) | [BE404](../BE404_microservices_service_mesh_and_platform_apis/README.md), [BE501](../../year_5/BE501_frontier_seminar_durable_execution_serverless/README.md), [OPS404](../../../devops_sre_platform_engineering/year_4/OPS404_performance_and_capacity_engineering/README.md) |

Part of the [Backend Engineering major](../../README.md). [BE302](../../year_3/BE302_backend_frameworks_and_service_internals/README.md) made one service correct and observable. This course makes a system fast and keeps it standing when traffic multiplies.

## Why this course matters now

Traffic in India now spikes to sizes few systems have handled anywhere:
- **JioHotstar:** 65.2 million peak concurrent viewers during the India–England T20 World Cup semi-final on 5 March 2026, which the ICC called a world record for a live event.
- **Shopify:** Black Friday–Cyber Monday 2025 peaked at 489 million requests per minute at the edge and over 117 million per minute on app servers. Shopify rehearsed with load tests of up to 200 million requests per minute.
- **OpenAI:** reported in January 2026 that it serves ChatGPT's main relational workload from one PostgreSQL primary and nearly 50 replicas. It relies on caching with locks against thundering herds, workload isolation and strict query discipline rather than sharding.

The lesson from all three is that scale comes from measurement and a few well-understood techniques, applied with judgement. AI tools now write load-test scripts, suggest indexes and read flame graphs. Deciding what to cache, how to invalidate it, where to cut a shard and how much headroom to buy still needs an engineer who can reason with numbers.

## Learning outcomes

By the end you can:

1. **Measure** latency distributions correctly (percentiles, histograms, coordinated omission) and **analyse** systems with Little's law and the USE and RED methods.
2. **Design** and **run** open-model load tests (spike, soak, stress, breakpoint) that reflect production traffic, and **report** a defensible capacity number.
3. **Find** bottlenecks with profiles, database statistics and queueing evidence, and **show** where the bottleneck moves after each fix.
4. **Design** multi-tier caches (client, CDN, reverse proxy, in-process, distributed) with explicit invalidation, stampede protection and hot-key handling.
5. **Scale** reads with replicas while keeping read-your-writes and monotonic reads where users need them.
6. **Shard** data with hash, range or directory schemes; **explain** consistent, jump and rendezvous hashing; and **reshard** without downtime.
7. **Configure** load balancing (L4/L7, least-request, power of two choices, Maglev-style hashing) with health checks, outlier ejection and draining.
8. **Protect** systems from overload with timeouts, retry budgets, load shedding, admission control and hedged requests, and **reason** about tail latency at scale.
9. **Plan** capacity and cost from load models, and **perform** back-of-envelope estimates in interviews and design reviews.

## Chapters and lessons

### Chapter 1 · Measuring performance (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Latency is a distribution | Percentiles, why averages lie, HDR histograms, merging percentiles is wrong | Compute p50/p99/p99.9 from raw samples and from pre-aggregated data; compare |
| 1.2 Throughput, goodput and utilization | Saturation, the knee of the curve, Little's law in capacity terms | Find the knee of a provided service from a load sweep |
| 1.3 USE and RED | Utilization, saturation and errors for resources; rate, errors and duration for services (Brendan Gregg) | Run a USE checklist on a Linux host under load |
| 1.4 Coordinated omission | Closed-loop tools hide stalls; wrk2's constant-throughput model; open vs closed workloads | Show a 10× p99 difference between a closed and an open test of the same stall |
| 1.5 SLOs as the target | Latency and availability objectives, error budgets, what "fast enough" means | Write SLOs for three endpoints from user expectations |

**Check your understanding:** (1) Why can't you average the p99s of ten servers to get the fleet p99? (2) How does a closed-loop load generator hide a 2-second pause? (3) Utilization is 60% but latency is terrible: name two resources the USE method would make you check.

### Chapter 2 · Load testing that tells the truth (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Tools | k6 (1.0 in May 2025; arrival-rate executors), Locust, Gatling; distributed load generation | Write the same arrival-rate test in k6 and Locust |
| 2.2 Workload models | Request mix from production logs, think time, data skew, cache-warm vs cold, realistic payloads | Build a workload model from a provided access log |
| 2.3 Test types | Smoke, load, stress, spike, soak and breakpoint tests; what each one answers | Run a 30-second 10× spike and a 2-hour soak; explain what each found |
| 2.4 Rehearsing big events | Shopify's BFCM scale tests and game days; testing in production with synthetic traffic | Write a scale-test plan for a sale day with pass/fail criteria |

**Check your understanding:** (1) Why does a load test with one user ID give misleadingly good results? (2) What does a soak test find that a 10-minute test never will? (3) Who must be told before you run a load test against shared infrastructure, and why?

### Chapter 3 · Finding bottlenecks (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 CPU and off-CPU profiles | On-CPU flame graphs, off-CPU analysis for waiting, lock contention profiles | Find a lock-contention bottleneck that no CPU profile shows |
| 3.2 The database side | `pg_stat_statements`, wait events, connection saturation, plan regressions under load | Identify whether a slowdown is CPU, I/O, lock or pool wait in Postgres |
| 3.3 Queues everywhere | Accept queues, thread pools, connection pools, broker queues; where requests wait | Trace one slow request and list every queue it sat in |
| 3.4 The bottleneck moves | Amdahl's law, fixing one constraint exposes the next | Fix three bottlenecks in sequence and plot throughput after each |

**Check your understanding:** (1) Why can a service at 30% CPU be at maximum throughput? (2) How do you tell pool wait from query time without changing code? (3) Why should you predict the next bottleneck before fixing the current one?

### Chapter 4 · Caching fundamentals (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Where caches live | Browser, CDN, reverse proxy, in-process, distributed (Redis/Valkey, Memcached), database buffer pool | Draw every cache between a mobile app and Postgres for one request |
| 4.2 Hit-ratio arithmetic | Effective latency = hit × cache latency + miss × origin latency; why 90% vs 99% matters | Compute origin load at 90%, 99% and 99.9% hit ratios for 100k requests/s |
| 4.3 Patterns | Cache-aside, read-through, write-through, write-behind, refresh-ahead; negative caching | Implement cache-aside and refresh-ahead; compare staleness and origin load |
| 4.4 Eviction and sizing | LRU, LFU, W-TinyLFU (Caffeine), working-set size, memory overhead per key | Replay a skewed trace through three eviction policies and compare hit ratios |
| 4.5 What not to cache | Per-user data with low reuse, rapidly changing values, authorization decisions without care | Remove a cache that was making things worse, with evidence |

**Check your understanding:** (1) Why can going from 99% to 99.9% hit ratio cut origin load by 10×? (2) When is an in-process cache better than Redis, and what does it cost in consistency? (3) Why is caching an authorization decision dangerous?

### Chapter 5 · Invalidation, stampedes and hot keys (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Invalidation strategies | TTL, explicit delete after commit, versioned keys, CDC-driven invalidation | Prove that delete-before-commit can leave stale data; fix it |
| 5.2 Leases and races | The stale-set race; leases in *Scaling Memcache at Facebook* (NSDI 2013) | Reproduce the stale-set race and fix it with a lease or version check |
| 5.3 Stampede protection | Locking on miss (OpenAI's cache locking), request coalescing (Discord), probabilistic early expiration (XFetch, VLDB 2015) | Expire a hot key under 20k requests/s with and without protection; plot origin load |
| 5.4 Hot keys | Detecting them, local caching, key splitting and replication, rate limiting per key | Survive one key receiving 50% of all traffic |

**Check your understanding:** (1) Why does deleting a cache key before the database commit cause stale reads? (2) Which stampede technique works without coordination between servers? (3) How does a single viral item break a well-sharded cache?

### Chapter 6 · CDNs and the edge (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 HTTP caching at scale | `Cache-Control`, `s-maxage`, `stale-while-revalidate`, `stale-if-error`, `Vary`, cache keys | Make an API response safely cacheable at a CDN for anonymous users |
| 6.2 Purging and versioning | Purge by URL and tag, immutable versioned assets, purge storms | Design purge for a price change across 10,000 product pages |
| 6.3 Tiered caching and origin shields | Collapsing requests at the edge, origin protection, live-event patterns | Measure origin requests with and without request collapsing in a local Varnish or nginx setup |
| 6.4 Edge compute | Running logic at the edge, personalization vs cacheability (deeper in BE501) | Move a geo-redirect to the edge and measure the latency change |

**Check your understanding:** (1) Why can `Vary: Cookie` destroy a CDN hit ratio? (2) How does `stale-if-error` turn an origin outage into a non-event for readers? (3) Why is a live cricket scoreboard cacheable even though it changes every few seconds?

### Chapter 7 · Scaling reads with replicas (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Replica topologies | Primary–replica, cascading replicas, replica lag sources | Measure lag under write load and under a long replica query |
| 7.2 Consistency for users | Read-your-writes, monotonic reads, session stickiness, LSN-aware routing | Implement LSN-based routing so a user always sees their own write |
| 7.3 Workload isolation | Separate replicas for analytics, batch and user traffic; OpenAI's priority isolation | Isolate a heavy report from user traffic and show p99 is unaffected |
| 7.4 Limits of read scaling | Write bottlenecks, replication cost, when to move write-heavy domains elsewhere | Decide which tables in a sample system should leave the primary |

**Check your understanding:** (1) What does a user see if their read goes to a replica 500 ms behind? (2) Why do long queries on a replica cause lag or cancellations? (3) When do replicas stop helping?

### Chapter 8 · Sharding and partitioning (weeks 8–9)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Choosing a shard key | Tenant, user, region; access patterns; skew; cross-shard queries | Pick shard keys for a chat app, a marketplace and a ledger; defend each |
| 8.2 Placement schemes | Hash, range and directory sharding; logical vs physical shards (Notion's 480 logical shards) | Implement a directory with logical shards mapped to physical nodes |
| 8.3 Consistent hashing family | Karger et al. (1997), virtual nodes, jump consistent hash (2014), rendezvous hashing, Maglev hashing | Measure keys moved when adding a node under each scheme |
| 8.4 Resharding without downtime | Double writes, backfill, verification, cut-over, Figma's and Notion's public accounts | Move a hot tenant to a new shard under load with zero errors |
| 8.5 Cross-shard work | Scatter-gather queries, global secondary indexes, cross-shard transactions and sagas | Build a global "recent orders" view without cross-shard joins |
| 8.6 When not to shard | Vertical scaling, read replicas, moving domains out, OpenAI's choice | Write a "do not shard yet" decision record with the numbers that would change it |

**Check your understanding:** (1) Why do logical shards make resharding easier? (2) How many keys move when you add a node with jump hashing compared with modulo hashing? (3) What breaks first when one tenant becomes 30% of all traffic?

### Chapter 9 · Load balancing (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 L4 and L7 | Connection vs request balancing, TLS termination, HTTP/2 and gRPC effects | Show uneven gRPC load behind L4 and fix it with L7 |
| 9.2 Algorithms | Round robin, least connections, least request, power of two random choices, weighted, consistent hashing for affinity | Simulate the algorithms with heterogeneous servers; compare tail latency |
| 9.3 Health and ejection | Active and passive health checks, outlier ejection, slow start, draining | Make a load balancer stop sending traffic to a slow (not dead) instance |
| 9.4 Global traffic | DNS-based and anycast routing, regional failover, Maglev (NSDI 2016) | Design failover between two regions with a stated RTO |

**Check your understanding:** (1) Why does "power of two choices" beat random selection so much? (2) How does a slow but healthy instance hurt p99, and how do you detect it? (3) What goes wrong with DNS-based failover and long TTLs?

### Chapter 10 · Overload and tail latency (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 The tail at scale | Fan-out amplifies tail latency; hedged and tied requests (Dean and Barroso, 2013) | Add hedged requests to a fan-out service; measure p99 and extra load |
| 10.2 Retries that don't kill you | Backoff with jitter, retry budgets, retrying only idempotent calls (Amazon Builders' Library) | Show a retry storm and stop it with a token-bucket retry budget |
| 10.3 Load shedding and admission control | Shedding by priority, concurrency limits, adaptive limits, `503` with `Retry-After` (Builders' Library) | Keep goodput flat at 3× overload with priority shedding |
| 10.4 Cascading failures | Positive feedback loops, crash loops, the SRE book's guidance, brownouts and graceful degradation | Inject a slow dependency and stop the cascade |

**Check your understanding:** (1) Why does a service that calls 100 backends see a much worse p99 than any single backend? (2) When do hedged requests make things worse? (3) Why is shedding load early kinder to users than queueing it?

### Chapter 11 · Capacity planning and cost (weeks 12–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Back-of-envelope estimation | Requests/s from users, bytes and storage, peak-to-average ratios, latency numbers every engineer should know | Estimate capacity for a live-scores service at 10 million concurrent users |
| 11.2 Queueing intuition | Utilization vs wait time, why 80% utilization hurts latency, the Universal Scalability Law | Fit the USL to your load-test data and predict the next knee |
| 11.3 Autoscaling | Reactive (HPA on CPU, RPS, queue lag) vs scheduled and predictive scaling, warm-up time | Pre-scale for a scheduled event and compare with reactive scaling |
| 11.4 Cost per request | Compute, storage, egress and cache costs; cost as a design constraint | Report the cost per million requests of your P3 design and cut it by 30% |

**Check your understanding:** (1) Why can't you run servers at 95% CPU and still meet a tight p99? (2) Why does reactive autoscaling fail for a match that starts at 7:30 pm? (3) Which costs grow with traffic, and which grow with data?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1: coordinated omission | Closed vs open test comparison |
| 2 | 2 | Lab 2: workload model and spike test | Load-test plan and results |
| 3 | 3 | Lab 3: bottleneck hunt (no AI) | Three fixes in sequence; P1 due |
| 4 | 4 | Lab 4: eviction and hit ratios | Policy comparison report |
| 5 | 5 | Lab 5: stampede and hot keys | Origin-load plots with and without protection |
| 6 | 6 | CDN rules | Cacheable API and purge design; P2 starts |
| 7 | 7 | Lab 6: read-your-writes routing | Routing implementation and tests |
| 8 | 8 | Lab 7: hashing schemes | Keys-moved measurements |
| 9 | 8 | Resharding | Live tenant move with zero errors |
| 10 | 9 | Lab 8: load-balancing simulation | Tail-latency comparison; P2 due |
| 11 | 10 | Lab 9: overload | Goodput under 3× overload; P3 design review |
| 12 | 11 | Capacity model | USL fit and prediction |
| 13 | 11 | Cost model | Cost per million requests |
| 14 | — | P3 integration | P3 demo and game day |
| 15 | Review and exam | — | Written exam and live estimation-and-design exam |

## Working with AI in this course

- **Use AI for:** writing k6 and Locust scripts from your workload model; summarizing flame graphs and database wait-event data; generating synthetic traces with realistic skew; drafting capacity spreadsheets that you then check; explaining load-balancer and CDN configuration options.
- **Do without AI (drills):** back-of-envelope estimates; hit-ratio and queueing arithmetic; choosing shard keys; the Lab 3 bottleneck hunt; the live estimation-and-design exam.
- **Verify AI output by:** re-running every performance claim as an open-model load test with the same workload; checking that generated load scripts use arrival-rate (open) executors and realistic data; validating cache invalidation with a staleness checker under concurrent writes; comparing capacity predictions with measured knees.
- **Where AI still fails here (show it yourself):** ask an assistant to "add caching to this endpoint" and check whether it invalidates before or after the database commit, and whether it protects against stampedes. Ask for a load test and check whether it is closed-loop with one user. Ask it to "shard this table" and check whether it considers hot tenants and cross-shard queries. Ask for an estimate of capacity for 10 million concurrent users and check the arithmetic. Record each failure with your measurement.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs 1–9 | 25% |
| Projects P1 / P2 / P3 | 5% / 12% / 23% |
| Written exam (measurement, caching, sharding, overload, estimation) | 20% |
| Live estimation-and-design exam (no AI) | 15% |

**Mastery gate:** you pass when you can, without AI help, (a) produce a capacity estimate for a stated product (users, requests/s, storage, cache size, shard count) within 30 minutes that an examiner judges within 2× of a reference model, with every assumption stated; (b) take a provided slow system and raise its sustainable throughput at the same p99 by at least 3× within 3 hours, showing the bottleneck after each step; and (c) run a game day on your P3 that survives a 5× spike, a cache-node loss and a shard move without breaching its SLO.

## Industry reality

- **Live events:** the ICC reported 65.2 million peak concurrent viewers on JioHotstar for the 5 March 2026 India–England semi-final, and called it a world record for live-event concurrency.
- **Shopify (BFCM 2025):** peaks of 489 million requests per minute at the edge, over 117 million per minute on app servers and 31.8 million API requests per minute. Shopify ran five scale tests before the event, the last at 200 million requests per minute.
- **OpenAI (January 2026):** one PostgreSQL primary with nearly 50 read replicas. It uses cache locking against thundering herds and isolates high- and low-priority workloads. A connection pooling change cut connection time from 50 ms to 5 ms.
- **Discord** added request coalescing in a Rust data-services layer in front of its message database (2023). **Facebook's** memcache paper (2013) remains the standard reference for leases, regional pools and invalidation at scale.
- **Google's** *The Tail at Scale* (2013) and Maglev load balancer (2016), and Amazon's Builders' Library on timeouts, retries and load shedding, are the public references most system-design interviewers expect you to know.

Interview questions from this course:

1. **"Design caching for a product catalogue whose prices change every minute."** A strong answer covers what to cache at each tier, TTL vs explicit invalidation, invalidation after commit or via CDC, stampede protection, hot keys, and how you measure staleness.
2. **"p50 is 50 ms but p99 is 2 s. Find and fix it."** Cover measuring correctly (open-model tests, histograms), locating the slow component with traces, GC pauses, pool waits, noisy neighbours, slow instances and load-balancer settings, fan-out effects and hedging.
3. **"How would you shard the orders table, and how would you reshard later?"** Cover shard-key choice and skew, logical shards with a directory, consistent hashing, double-write and backfill migration, verification, and cross-shard queries.
4. **"Prepare a system for a 10× traffic event such as a sale or a cricket final."** Cover estimation, load-test rehearsal, pre-scaling, CDN and caching for read-heavy paths, load shedding by priority, feature flags to switch off non-critical features, and a game-day runbook.
5. **"Explain consistent hashing and why caches use it."** Cover modulo hashing's mass remapping, the ring with virtual nodes, jump and rendezvous hashing, the keys moved when nodes are added or removed, and hot-spot handling.

## Resources (free first)

- **Papers:** Dean and Barroso, [The Tail at Scale](https://research.google/pubs/the-tail-at-scale/) (2013); Nishtala et al., [Scaling Memcache at Facebook](https://www.usenix.org/conference/nsdi13/technical-sessions/presentation/nishtala) (NSDI 2013); Eisenbud et al., [Maglev](https://research.google/pubs/maglev-a-fast-and-reliable-software-network-load-balancer/) (NSDI 2016); Lamping and Veach, [A Fast, Minimal Memory, Consistent Hash Algorithm](https://arxiv.org/abs/1406.2294) (2014); Vattani et al., [Optimal Probabilistic Cache Stampede Prevention](https://www.vldb.org/pvldb/vol8/p886-vattani.pdf) (VLDB 2015).
- **Guides:** Google SRE book chapters on [load balancing in the datacenter](https://sre.google/sre-book/load-balancing-datacenter/), [handling overload](https://sre.google/sre-book/handling-overload/) and [addressing cascading failures](https://sre.google/sre-book/addressing-cascading-failures/); Amazon Builders' Library on [timeouts, retries and backoff with jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/), [load shedding](https://aws.amazon.com/builders-library/using-load-shedding-to-avoid-overload/) and [caching](https://aws.amazon.com/builders-library/caching-challenges-and-strategies/); Brendan Gregg's [USE method](https://www.brendangregg.com/usemethod.html).
- **Tools:** [Grafana k6 docs](https://grafana.com/docs/k6/latest/); [Locust](https://locust.io/); [wrk2](https://github.com/giltene/wrk2) (read its README on coordinated omission).
- **Case studies:** Shopify, [BFCM readiness 2025](https://shopify.engineering/bfcm-readiness-2025); Discord, [How Discord stores trillions of messages](https://discord.com/blog/how-discord-stores-trillions-of-messages).
- **Paid, worth it:** Brendan Gregg, *Systems Performance*, 2nd edition (2020); Kleppmann and Riccomini, *Designing Data-Intensive Applications*, 2nd edition (2026), on partitioning and replication.

## Sources

All checked 12 Oct 2026.

- ICC media release on JioHotstar concurrency record (7 Mar 2026): https://www.icc-cricket.com/media-releases/icc-men-s-t20-world-cup-2026-sets-new-global-streaming-record-on-jiohotstar-during-india-england-semi-final
- Shopify BFCM 2025 results (press release, Dec 2025): https://www.shopify.com/investors/press-releases/shopify-merchants-achieve-record-breaking-146-billion-black ; Shopify Engineering, BFCM readiness 2025: https://shopify.engineering/bfcm-readiness-2025
- OpenAI on scaling PostgreSQL (Jan 2026), original https://openai.com/index/scaling-postgresql/ , as reported by VentureBeat (23 Jan 2026): https://venturebeat.com/data/how-openai-is-scaling-the-postgresql-database-to-800-million-users
- Grafana k6 1.0 release (May 2025): https://grafana.com/blog/2025/05/07/grafana-k6-1.0-release/
- Discord (Mar 2023): https://discord.com/blog/how-discord-stores-trillions-of-messages
- Papers and guides as linked under Resources.

_Last reviewed: 2026-10_
