# OPS303 · Labs and projects

The shared lab environment is the [OpenTelemetry Demo](https://opentelemetry.io/docs/demo/) (a polyglot "astronomy shop" of about a dozen services) on kind or Docker Compose. Its [feature flags](https://opentelemetry.io/docs/demo/feature-flags/) inject realistic faults such as failing payments, a leaking cache and CPU spikes, so you can practise finding problems you did not plant yourself. You need a laptop with 16 GB of RAM, or you can trim the demo to fewer services. Labs 3, 4 and 10 are done without AI assistance.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Demo up | Run the OpenTelemetry Demo; map every signal it emits and where it is stored | Signal map (service × signal × backend) | 3 h |
| 2 · Prometheus from scratch | Install Prometheus with Kubernetes service discovery, node exporter and remote write to a second instance; kill it mid-scrape | Config, WAL replay evidence, scrape-target health | 4 h |
| 3 · PromQL katas | 20 graded queries: rates with resets, joins with `group_left`, histogram quantiles, `absent()` | Queries with hand-computed expected values | 5 h |
| 4 · Cardinality budget | Add an unbounded label on purpose, measure series growth, then enforce a 5,000-series budget per service | `tsdb analyze` output before/after, relabel rules | 4 h |
| 5 · Logs: Loki vs ClickHouse | Ship the same 10 GB of structured logs through Vector into Loki and ClickHouse | Storage size, ingest rate and 5 query timings for each, with a recommendation | 6 h |
| 6 · Tail sampling | Collector gateway with load-balancing exporter and tail sampling: 100% of errors and slow traces, 5% of the rest | Collector config, proof that no error trace was dropped across 10,000 requests | 5 h |
| 7 · Collector gateway | Multi-tenant routing, memory limiter, PII redaction processor; overload test | Config, overload graph, redaction test cases | 4 h |
| 8 · eBPF and profiling | Instrument one service with OBI and the SDK; compare spans; find a CPU regression with Pyroscope or Parca | Comparison table and profile diff | 5 h |
| 9 · Dashboards as code | Generate overview, service and instance dashboards for every service from one template | Template, generated JSON, screenshots of the drill-down | 4 h |
| 10 · Alert tests | 10 alerts with `promtool` unit tests, Alertmanager routing for 3 teams, inhibition | Rules, tests (all passing), routing tree | 4 h |

## Projects

### P1 · Instrument and explain a three-service app (L1, ~6 hours)

**Real-world inspiration:** Google's four golden signals and the RED method are the default first dashboard in most SRE teams ([SRE book](https://sre.google/sre-book/monitoring-distributed-systems/)). The OpenTelemetry Demo shows how a vendor-neutral setup looks.

**What to build:** three services in at least two languages (for example Go and Python), instrumented with OpenTelemetry for metrics, traces and logs, sent through one Collector to Prometheus, Tempo or Jaeger, and Loki.

**Acceptance criteria:**
- **Correlation:** for any request, you can go from a latency spike on a dashboard to an exemplar trace to its logs in three clicks; every log line carries the trace ID.
- **Coverage:** a RED dashboard exists for every service, with latency as a heatmap and percentiles computed from aggregated buckets.
- **Alerts:** three alerts (error ratio, latency, absence of data) each pass `promtool` unit tests, including a "service completely down" case.
- **Performance:** every dashboard panel loads in under 2 seconds on one week of data.

**Stretch goals:** context propagation through a message queue; zero-code instrumentation for a third language.

**What it proves to an employer:** you can make a service observable correctly, which every backend, DevOps and SRE team expects from day one.

### P2 · Telemetry pipeline on a budget (L2, ~15 hours)

**Real-world inspiration:** Zerodha moved logging from ELK to ClickHouse and Vector when index storage grew to 3–4× the raw size and ingestion slowed at peak ([Logging at Zerodha](https://zerodha.tech/blog/logging-at-zerodha/)); it runs Prometheus with VictoriaMetrics across data centres and cloud ([monitoring post](https://zerodha.tech/blog/infra-monitoring-at-zerodha/)).

**What to build:** for the OpenTelemetry Demo, a Collector agent-and-gateway pipeline with tail sampling, cardinality guards, PII redaction and per-team routing; long-term metrics in Thanos or VictoriaMetrics on object storage (MinIO); logs in Loki or ClickHouse with two retention classes; and a cost model per service.

**Acceptance criteria:**
- **Volume:** total telemetry bytes per 1,000 requests fall by at least 60% against the naive baseline, measured at the gateway.
- **Fidelity:** 100% of error traces and of traces slower than the p99 threshold are retained (checked across 20,000 requests with planted errors).
- **Guards:** a service that suddenly emits 50,000 new series is capped at its budget within one scrape interval, and an alert names it.
- **Detection:** for 5 injected faults (demo feature flags), the relevant alert fires within 5 minutes each.
- **Privacy:** a scan of stored logs finds zero planted email addresses or phone numbers.
- **Cost:** a one-page report gives cost per service per month for your setup, with the three biggest levers.

**Stretch goals:** a 180-day "compliance" log tier on cheap object storage, sized and priced; dashboards generated as code from the service catalog.

**What it proves to an employer:** you can run observability as an engineered, budgeted system, which is what observability-engineer and senior SRE roles are hired for.

### P3 · "Find the fault" on-call platform (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** the hiring loop's incident scenario ("alerts fire, the dashboard is red: what do you do?") from this repository's [market map](../../../../06_career_and_market_readiness/01_market_map/roles/OPS_devops_sre_platform_engineering.md), and the OpenTelemetry Demo's built-in failure scenarios.

**What to build:** a complete observability platform for the OpenTelemetry Demo, reproducible from Git:
- metrics, logs, traces and continuous profiles, with eBPF network flows where useful;
- an SLO-ready dashboard hierarchy generated as code;
- symptom-based alerts with runbooks;
- Alertmanager routing to a chat channel;
- a 24-hour soak with a load generator and randomly scheduled faults from the demo's flags.

**Acceptance criteria:**
- **Rebuild:** `git clone` plus one command brings the whole platform up on a clean machine in under 20 minutes.
- **On-call trial:** in a blind test, a classmate on call identifies the faulty service and cause for at least 6 of 8 injected faults within 10 minutes each, using only your dashboards, alerts and runbooks.
- **Alert precision:** over the 24-hour soak, at least 80% of pages correspond to a real injected fault, and no fault goes unpaged.
- **Explainability:** for each fault, an incident timeline reconstructed purely from telemetry, with the exact query used at each step.
- **Cost:** telemetry cost per million requests is reported, with a comparison against one SaaS vendor's public price list.
- **AI audit:** an AI assistant is given the same 8 faults; you report its accuracy and every wrong conclusion it drew.

**Stretch goals:** an MCP server exposing read-only queries to an assistant, with the queries it ran logged; LLM-call tracing with token and cost attributes for a small AI feature added to the demo.

**What it proves to an employer:** you can build the system an on-call team depends on and prove it works under blind test, not just show screenshots.

## Feeds into

- [OPS304 Site Reliability Engineering](../OPS304_site_reliability_engineering_slos_error_budgets/README.md): SLIs and burn-rate alerts are built on P2 and P3.
- [OPS403 AIOps and Agentic Operations](../../year_4/OPS403_aiops_and_agentic_operations/README.md): P3's telemetry is the data set for anomaly detection and investigation agents.
- [OPS404 Performance and Capacity Engineering](../../year_4/OPS404_performance_and_capacity_engineering/README.md): profiles and latency histograms drive performance work.
- [OV12A Running Agents in Production](../../../../04_overlaps/OV12_agent_infrastructure_platform/OV12A_running_agents_in_production_sandboxes_durable/README.md): agent observability.
