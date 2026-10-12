# BE402 · Labs and projects

Labs run on a local Kubernetes cluster (kind or k3d) or on a small cloud budget, using PostgreSQL with replicas, Redis or Valkey, Varnish or nginx as a CDN stand-in, Envoy as a load balancer, and k6 or Locust with open-model (arrival-rate) executors. Every result must include the workload model, the raw histogram data and the hardware, so someone else can reproduce it. Lab 3 and the live exam are done without AI assistants.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Coordinated omission | Load-test a service with a planted 2-second stall using a closed-loop tool and an open-model tool | Both histograms and a paragraph explaining the p99 difference | 3 h |
| 2 · Workload model and spike | Build a request mix and data skew from a provided access log; run spike, soak and breakpoint tests | Workload model, three test reports, and the capacity number you would sign off | 6 h |
| 3 · Bottleneck hunt (no AI) | Raise a provided service's throughput at fixed p99 by finding and fixing three bottlenecks in sequence | Before/after evidence (profiles, wait events, pool metrics) for each step | 6 h |
| 4 · Eviction policies | Replay a skewed trace through LRU, LFU and W-TinyLFU at three cache sizes | Hit-ratio table and a recommendation with reasoning | 4 h |
| 5 · Stampedes and hot keys | Expire a hot key at 20k requests/s with no protection, a lock, request coalescing and XFetch; then survive one key taking 50% of traffic | Origin-load plots for each technique | 6 h |
| 6 · Read-your-writes routing | LSN-aware routing between primary and replicas with a staleness checker | Zero stale reads on the user's own data over 1M operations; replica offload percentage | 5 h |
| 7 · Hashing schemes | Implement modulo, ring with virtual nodes, jump and rendezvous hashing; add and remove nodes | Keys moved and load imbalance for each scheme | 4 h |
| 8 · Load-balancing simulation | Compare round robin, least request and power of two choices with heterogeneous and slow instances in Envoy | p99 per algorithm; outlier ejection removing a slow instance | 5 h |
| 9 · Overload | Priority load shedding, concurrency limits and retry budgets under 3× overload | Goodput vs offered-load plot showing flat goodput and protected priority traffic | 6 h |

## Projects

### P1 · Capacity report for a real service (L1, ~6 hours)

**Real-world inspiration:** before peak events, teams sign off a capacity number with evidence. Shopify ran five scale tests before BFCM 2025, the last at 200 million requests per minute ([Shopify Engineering](https://shopify.engineering/bfcm-readiness-2025)).

**What to build:** a capacity report for your BE302 P3 service (or a provided one): a workload model from logs, an open-model load sweep to the breaking point, a USE analysis of every resource at the knee, the bottleneck, and the capacity number with headroom.

**Acceptance criteria:**
- The load sweep uses arrival-rate executors with at least 8 steps and runs three times. Run-to-run variation in p99 at each step is reported, and is under 15% below the knee.
- The knee is identified with a named saturated resource, supported by metrics (CPU, pool wait, locks or I/O).
- The capacity number is stated as "X requests/s at p99 under Y ms with Z% headroom", and a validation run at that rate passes for 30 minutes.
- The report includes a coordinated-omission check: the same test with a closed-loop tool, and an explanation of the difference.
- Another student reproduces your knee within 20% using only your report.

**Stretch goals:** fit the Universal Scalability Law to the sweep and predict throughput at double the CPU; add a soak test that finds a slow leak.

**What it proves to an employer:** you can say how much load a system can take and prove it, which is the first question before any launch.

### P2 · Multi-tier cache for a menu and pricing API (L2, ~15 hours)

**Real-world inspiration:** read-heavy catalogue APIs (restaurant menus, product listings) change prices and availability often but are read far more often. *Scaling Memcache at Facebook* ([NSDI 2013](https://www.usenix.org/conference/nsdi13/technical-sessions/presentation/nishtala)) and OpenAI's cache locking against thundering herds ([VentureBeat, Jan 2026](https://venturebeat.com/data/how-openai-is-scaling-the-postgresql-database-to-800-million-users)) show the techniques. The traffic numbers are an **illustrative scenario**.

**What to build:** a menu and pricing API backed by PostgreSQL with three cache tiers:
- a CDN stand-in (Varnish or nginx) for anonymous reads, with `stale-while-revalidate` and `stale-if-error`;
- Redis or Valkey for shared data;
- an in-process cache for the hottest items.

Invalidation is driven by change data capture or outbox events after commit. Add stampede protection, hot-key handling and a staleness checker that writes prices and immediately reads them back through every tier.

**Acceptance criteria:**
- **Throughput:** 20,000 reads/s sustained on the test cluster with p99 under 30 ms, and the database receives under 2% of read traffic.
- **Freshness:** after a price change, 99.9% of reads at every tier return the new price within 2 seconds. The staleness checker reports the full distribution, and the maximum stays under 10 seconds.
- **Stampede:** when the hottest key expires under full load, origin queries for that key stay at or under 1 per cache node per refresh (plot attached).
- **Outage:** with Redis stopped for 2 minutes, the API keeps serving (stale-if-error at the edge, degraded in-process cache), p99 stays under 200 ms, and it recovers automatically.
- **Hot key:** one item receiving 40% of traffic does not raise p99 by more than 20%.
- **Write-up:** the invalidation design, with a timeline diagram of the race you prevented.

**Stretch goals:** purge by tag at the CDN tier; compare TTL-only, delete-after-commit and CDC-driven invalidation on freshness and origin load; add per-tenant cache quotas.

**What it proves to an employer:** you can make reads cheap without serving wrong data, and you can show both with numbers.

### P3 · Live-event platform built for a 10× spike (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** cricket streaming in India has reached 65.2 million concurrent viewers on one platform ([ICC, Mar 2026](https://www.icc-cricket.com/media-releases/icc-men-s-t20-world-cup-2026-sets-new-global-streaming-record-on-jiohotstar-during-india-england-semi-final)). Around the video sit services such as live scores, reactions, polls and personalised feeds, and these get hammered at the same moments. Your platform is an **illustrative scenario** of those surrounding services, scaled to what you can run.

**What to build:**
- **Live score:** a live-score service with edge-cacheable snapshots and push updates over SSE or WebSockets.
- **Reactions:** an ingestion path (100k events/s target on the test cluster, or the highest you can reach, documented) with sharded counters and approximate aggregation.
- **Personalised feed:** read replicas with read-your-writes routing.
- **Caching:** a cache cluster with consistent hashing and a node-loss drill.
- **Overload protection:** priority classes (score and payments-like actions above reactions), concurrency limits and load shedding.
- **Scaling:** scheduled pre-scaling plus reactive autoscaling.
- **Planning:** a capacity and cost model, and a game-day runbook.

**Acceptance criteria:**
- **Spike:** traffic rising 5× in 30 seconds keeps goodput at or above 90% of measured capacity. Priority-path p99 stays under 200 ms. Shed requests get `503` with `Retry-After`, and clients back off (verified in client logs).
- **Fan-out:** a score update reaches 95% of 50,000 connected test clients within 2 seconds.
- **Cache node loss:** losing one of four cache nodes raises the origin hit rate by less than the share of keys that node owned (consistent hashing evidence), and causes zero errors.
- **Shard move:** moving one shard of reaction counters to a new node under load causes zero lost increments (verified by an exact recount) and zero errors.
- **Model accuracy:** your capacity model predicts the measured knee within 20%, and your cost model reports the cost per million requests. A documented change cuts it by at least 25%.
- **Game day:** a scripted game day with five injected failures (spike, cache-node loss, replica lag, slow dependency, a bad deploy rolled back) is run, recorded and written up as a post-mortem with action items.

**Stretch goals:** a multi-region design with regional failover and a measured RTO; hedged requests for the feed's fan-out; edge compute for personalised but cacheable responses (a preview of BE501).

**What it proves to an employer:** you can design for a known spike, prove the design under failure and explain its cost. This is the work behind every big sale, launch or match day.

## Feeds into

- [BE404 Microservices, Service Mesh and Platform APIs](../BE404_microservices_service_mesh_and_platform_apis/README.md): load balancing and resilience across many services.
- [BE501 Frontier Seminar](../../year_5/BE501_frontier_seminar_durable_execution_serverless/README.md): edge and serverless approaches to the same problems.
- [OPS404 Performance and Capacity Engineering](../../../devops_sre_platform_engineering/year_4/OPS404_performance_and_capacity_engineering/README.md) and [CLD403 FinOps and Cloud Cost Engineering](../../../cloud_engineering/year_4/CLD403_finops_and_cloud_cost_engineering/README.md) as electives.
- The [Backend Engineering flagship industry project](../../../../06_career_and_market_readiness/05_industry_projects/BE_backend_engineering.md).
