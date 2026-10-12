# OPS303 · Observability: Metrics, Logs, Traces and OpenTelemetry

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 5 | 4 (≈ 120 hours) | L2 → L3 (P3 reaches L4) | [CS215](../../../../02_year_2_core_computer_science/semester_4/CS215_cloud_and_devops_foundations/README.md), [CS203](../../../../02_year_2_core_computer_science/semester_3/CS203_operating_systems/README.md) | [OPS304](../OPS304_site_reliability_engineering_slos_error_budgets/README.md), [OPS403](../../year_4/OPS403_aiops_and_agentic_operations/README.md), [OPS404](../../year_4/OPS404_performance_and_capacity_engineering/README.md) |

Part of the [DevOps, SRE and Platform Engineering major](../../README.md). [CS215](../../../../02_year_2_core_computer_science/semester_4/CS215_cloud_and_devops_foundations/README.md) had you instrument one service, build a RED dashboard and write one burn-rate alert. This course teaches you to design the telemetry system for a whole company: what to collect, how to store and query it, what it costs, and how to turn it into alerts that wake the right person for the right reason. SLO design itself is taught in [OPS304](../OPS304_site_reliability_engineering_slos_error_budgets/README.md); security monitoring in [SEC302](../../../cybersecurity_defense/year_3/SEC302_security_operations_soc_siem_and_monitoring/README.md).

## Why this course matters now

Observability has standardised quickly:

- **OpenTelemetry** graduated in the CNCF in May 2026 and is the vendor-neutral way to produce metrics, logs and traces.
- **Prometheus 3.0** (November 2024) added native histograms, UTF-8 metric names and OTLP ingestion; 3.15 shipped in September 2026.
- **Jaeger v2** is rebuilt on the OpenTelemetry Collector.
- **eBPF instrumentation:** Grafana donated its Beyla eBPF auto-instrumentation to OpenTelemetry as OBI.

The hard problems are no longer "can we see it" but cost, cardinality and signal quality. Zerodha described leaving ELK for ClickHouse and Vector partly because indexing every field inflated storage "by a minimum of 3-4x the original size". Assistants such as Grafana Assistant and Datadog's Bits AI investigation agent now write PromQL and summarise traces. They are only as good as the telemetry underneath, and they make classic mistakes, such as averaging percentiles or taking `rate()` of a gauge, with full confidence. Only 20% of developers who use AI use it to operate or troubleshoot production (Stack Overflow 2026). People who can design telemetry, and check what an AI concludes from it, are scarce.

## Learning outcomes

By the end you can:

1. **Choose** signals (metrics, logs, traces, profiles, events) for a question, and **explain** the cost and fidelity trade-off of each.
2. **Write** correct PromQL, including rates over counters with resets, vector matching and `histogram_quantile` over aggregated buckets, and **test** recording and alerting rules with `promtool`.
3. **Control** cardinality with a per-service active-series budget, relabelling and aggregation, and **size** a long-term store (Thanos, Mimir or VictoriaMetrics).
4. **Build** a log pipeline (Fluent Bit, Vector or the OTel Collector) into Loki or ClickHouse, with structure, sampling, redaction and retention.
5. **Instrument** polyglot services with OpenTelemetry SDKs and zero-code agents, propagate W3C Trace Context, and **configure** head and tail sampling.
6. **Operate** an OpenTelemetry Collector fleet (agent and gateway) and **use** eBPF tools (OBI, Hubble, continuous profilers) where SDKs cannot reach.
7. **Design** dashboards that answer named questions and **define** alerts that are actionable, with routing, grouping and inhibition.
8. **Estimate and cut** telemetry cost per service, and **govern** personal data in telemetry under India's DPDP Act.
9. **Audit** AI-generated queries and AI conclusions drawn from telemetry.

## Chapters and lessons

### Chapter 1 · What observability is for (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Monitoring vs observability | Known failure modes vs unknown ones; asking new questions without shipping new code | Classify 10 past incidents by whether existing dashboards could have explained them |
| 1.2 The signals | Metrics (cheap, aggregated), logs (rich, costly), traces (causal), profiles (code-level), events (changes) | For 5 questions, pick the cheapest signal that answers each |
| 1.3 Method frameworks | Four golden signals (SRE book), RED for services, USE for resources | Map each framework onto one service and one host |
| 1.4 The telemetry pipeline | Produce → collect → process → store → query → act; where cost and loss happen | Draw the pipeline of your CS215 project; mark loss points |

**Check your understanding:** (1) Why can't you debug a new failure mode with metrics alone? (2) Which signal is best for "which deploy started this?" (3) Where in the pipeline is the cheapest place to drop data?

### Chapter 2 · Metrics and Prometheus internals (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Data model | Series = metric name + label set; counters, gauges, classic and native histograms, summaries (and why summaries cannot be aggregated) | Instrument one endpoint with each type; compare queries |
| 2.2 Collection | Pull, service discovery (Kubernetes, EC2 tags, file), exporters, Pushgateway's narrow use, OTLP push into Prometheus 3 | Scrape a fleet discovered from labels; add a node exporter |
| 2.3 Storage | TSDB head block, WAL, 2-hour blocks, compaction, retention, remote write | Kill Prometheus mid-scrape and inspect WAL replay |
| 2.4 High availability | Paired Prometheus instances, deduplication, why "HA" here is not consensus | Run two replicas behind Thanos Query and deduplicate |

**Check your understanding:** (1) Why can't you average p99s from two summaries? (2) What happens to counters when a pod restarts, and how does PromQL cope? (3) When is push the right model?

### Chapter 3 · PromQL in depth (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Rates | `rate` vs `irate` vs `increase`, range length vs scrape interval, extrapolation | Show how a 1m window with a 30s scrape misleads |
| 3.2 Aggregation and matching | `sum by`, `without`, `on`/`ignoring`, `group_left` for joining labels from info metrics | Compute error ratio per team by joining a service-owner metric |
| 3.3 Histograms | `histogram_quantile` over `sum by (le)`, native histogram functions, bucket layout errors | Fix a dashboard that computes quantiles per pod, then averages them |
| 3.4 Rules | Recording rules for expensive queries, naming conventions, `promtool test rules` | Write rules with unit tests that cover counter resets |
| 3.5 Pitfalls | Staleness, missing series and `absent()`, division by zero, subquery cost | Solve 20 graded PromQL katas |

**Check your understanding:** (1) Why must you `sum by (le)` before `histogram_quantile`? (2) Your alert never fires when the service is completely down. Why? (3) When does `irate` lie?

### Chapter 4 · Cardinality and scale (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Cardinality | Series count = product of label values; unbounded labels (user ID, URL path, request ID) | Find the top-10 cardinality offenders with `promtool tsdb analyze` |
| 4.2 Budgets and guards | Per-service series budgets, `metric_relabel_configs` drops, `sample_limit` | Enforce a 5,000-series budget per service |
| 4.3 Long-term storage | Thanos, Grafana Mimir, VictoriaMetrics, Cortex: object storage, downsampling, query fan-out | Run Thanos with object storage on MinIO; query 30 days |
| 4.4 Real architecture | Zerodha's hybrid multi-data-centre and cloud monitoring with Prometheus, Grafana and VictoriaMetrics | Draw their architecture from the blog and critique one choice |

**Check your understanding:** (1) Why does adding one label sometimes multiply cost by 1,000? (2) What do you lose with downsampling? (3) Where should a cardinality guard live: the app, the collector or the database?

### Chapter 5 · Logs (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Structured logging | JSON and logfmt, stable field names, levels as a contract, trace and request IDs in every line | Convert a service's free-text logs to structured logs |
| 5.2 Shipping | Fluent Bit, Vector, OTel Collector logs pipeline; buffering, backpressure, at-least-once delivery | Kill the log store for 10 minutes; prove no lines were lost |
| 5.3 Stores | Loki (indexes labels, not content; LogQL), Elasticsearch/OpenSearch (inverted index), ClickHouse (columnar) | Load the same 10 GB into Loki and ClickHouse; compare size and query time |
| 5.4 Case: Zerodha | Why ELK struggled after traffic grew (Logstash slowdowns, 3–4× index inflation) and the move to ClickHouse and Vector | Reproduce their trade-off at small scale |
| 5.5 Retention and privacy | Tiered retention, sampling of debug logs, PII redaction at the collector; CERT-In 180-day log rule; DPDP Act duties for personal data | Write a retention and redaction policy and implement it |

**Check your understanding:** (1) Why do high-cardinality Loki labels hurt? (2) Which logs may you sample, and which never? (3) Where should redaction happen, and why not at query time?

### Chapter 6 · Distributed tracing (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Spans and context | Trace and span IDs, parent-child, links, W3C Trace Context and Baggage | Propagate context across HTTP, gRPC and a message queue |
| 6.2 Sampling | Head (probabilistic), tail (in the Collector: keep errors and slow traces), consistent sampling | Keep 100% of error traces with 5% of the rest |
| 6.3 Backends | Jaeger v2, Grafana Tempo (TraceQL), span metrics, service graphs | Find the slowest dependency with a TraceQL query |
| 6.4 Exemplars and correlation | Linking a latency histogram bucket to an example trace; logs carrying trace IDs | Click from a p99 spike to a trace to its logs |

**Check your understanding:** (1) Why can head sampling miss the traces you need most? (2) What breaks context propagation through a queue? (3) What does tail sampling cost you in memory and complexity?

### Chapter 7 · OpenTelemetry end to end (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 API, SDK and semantic conventions | Why the API is separate from the SDK; resource attributes; stable vs experimental conventions | Instrument Go and Python services to the HTTP conventions |
| 7.2 Zero-code instrumentation | Java agent, Python and Node auto-instrumentation, the OTel Operator injecting agents on Kubernetes | Instrument a Java service without changing its code |
| 7.3 The Collector | Receivers, processors (batch, memory limiter, attributes, filter, tail sampling), exporters; agent vs gateway | Build a gateway that routes by tenant |
| 7.4 Running Collectors | Scaling, load balancing exporter for tail sampling, self-monitoring, upgrades | Overload a Collector and watch the memory limiter protect it |

**Check your understanding:** (1) Why does tail sampling need a load-balancing layer keyed on trace ID? (2) What is the risk of experimental semantic conventions in dashboards? (3) When is zero-code instrumentation not enough?

### Chapter 8 · eBPF-based observability (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 eBPF primer | Verifier, maps, kprobes, uprobes, tracepoints; required privileges and kernel versions | Write a bpftrace one-liner that histograms syscall latency |
| 8.2 Zero-code traces from the kernel | OpenTelemetry eBPF Instrumentation (OBI): HTTP and gRPC spans without SDKs, and its limits | Compare OBI spans to SDK spans for the same service |
| 8.3 Network flows | Cilium Hubble flows, DNS and drop visibility | Find which pod is calling a forbidden service |
| 8.4 Continuous profiling | Parca and Grafana Pyroscope, profiles as the fourth signal | Find a CPU regression between two versions in a profile diff |

**Check your understanding:** (1) What can eBPF see that an SDK cannot, and the reverse? (2) Why does running eBPF agents need a security review? (3) When is a profile more useful than a trace?

### Chapter 9 · Dashboards that answer questions (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Question-first design | One dashboard per audience; overview → service → instance drill-down | Redesign a 40-panel dashboard into 3 linked ones |
| 9.2 Visual honesty | Heatmaps for latency, log scales, consistent units, no averages of percentiles | Fix 5 misleading panels |
| 9.3 Dashboards as code | Grafana 13 provisioning and JSON models, Grafonnet, Perses (CNCF sandbox) | Generate dashboards for 10 services from one template |
| 9.4 Change overlays | Deploy and feature-flag annotations, incident markers | Annotate deploys automatically from CI |

**Check your understanding:** (1) Why do averaged latency panels hide outages? (2) What makes a dashboard rot, and how does "as code" help? (3) Which panel would you look at first in an incident, and why?

### Chapter 10 · Alert design (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 What deserves a page | Symptom-based, urgent, actionable, novel; tickets vs pages | Classify 30 existing alerts into page, ticket or delete |
| 10.2 Alertmanager | Routing trees, grouping, inhibition, silences, receivers, time-based muting | Build routing for 3 teams with business-hours tickets |
| 10.3 Testing alerts | `promtool test rules`, synthetic failure injection, "would this have fired?" replays | Unit-test 10 alerts including flapping cases |
| 10.4 Measuring alert quality | Pages per shift, percentage actionable, time to acknowledge, alerts with no runbook | Produce an alert-quality report for a week of data |

**Check your understanding:** (1) Why is "CPU above 80%" usually a bad page? (2) What does inhibition prevent? (3) How do you know an alert is too noisy before people start ignoring it?

### Chapter 11 · Cost and governance (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Cost drivers | Active series, ingest volume, span count, retention, query load; per-service attribution | Build a cost-per-service model for your stack |
| 11.2 Reduction levers | Collector-side filtering and aggregation, tail sampling, log level policy, tiered storage | Cut volume by 60% while keeping every error trace |
| 11.3 Build vs buy | Self-hosted Grafana stack vs SaaS (Datadog, Grafana Cloud, Honeycomb, New Relic, Elastic); lock-in and OTLP portability | Write a one-page decision for a 50-engineer company |
| 11.4 Data governance | PII in telemetry, access control on logs, DPDP Act duties, data location | Run a PII scan on a day of logs and fix the leaks |

**Check your understanding:** (1) Why is OTLP a negotiation tool with vendors? (2) Which telemetry should never leave your country or account? (3) What is the cost of the data you never query?

### Chapter 12 · Observability with and for AI (weeks 12–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Observing LLM features | Token counts, model and version, latency to first token, cost per request; OpenTelemetry generative-AI semantic conventions (check their stability status) | Trace an LLM call path with token and cost attributes |
| 12.2 AI query assistants | Natural language to PromQL/LogQL/TraceQL; Grafana Assistant, Datadog Bits AI; MCP servers such as `mcp-grafana` | Grade 25 AI-written queries against your own answers |
| 12.3 AI conclusions from telemetry | Summaries of traces and logs; hallucinated causation; missing-data blindness | Give an assistant partial data and record what it invents |
| 12.4 Incident replay | Reconstructing an incident from telemetry alone | Replay a fault in the OpenTelemetry Demo and write the timeline |

**Check your understanding:** (1) What attribute would you add to every LLM span to control cost? (2) An AI assistant says "the database caused the spike". What do you check? (3) Why does missing telemetry make AI summaries more confident, not less?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · OpenTelemetry Demo up | Signal map |
| 2 | 2 | Lab 2 · Prometheus from scratch | Scrape config, WAL notes |
| 3 | 3 | Lab 3 · PromQL katas | 20 graded queries; P1 starts |
| 4 | 4 | Lab 4 · Cardinality budget | **P1 due** |
| 5 | 5 | Lab 5 · Logs: Loki vs ClickHouse | Size and speed comparison |
| 6 | 6 | Lab 6 · Tail sampling | Sampling policy evidence |
| 7 | 7 | Lab 7 · Collector gateway | Mid-term (AI off) |
| 8 | 8 | Lab 8 · eBPF and profiling | OBI vs SDK report |
| 9 | 9 | Lab 9 · Dashboards as code | Generated dashboards |
| 10 | 10 | Lab 10 · Alert tests | **P2 due** |
| 11 | 11 | Cost model | Cost report |
| 12 | 12 | AI query grading | Failure log |
| 13 | 12 | Incident replay | Timeline; P3 soak runs |
| 14 | — | P3 on-call trial | **P3 due** |
| 15 | Review | Practical exam and oral | Final |

## Working with AI in this course

- **Use AI for:** drafting Collector configs, recording rules and dashboard JSON; translating a question into PromQL, LogQL or TraceQL as a first draft; summarising a long trace; writing instrumentation boilerplate. Named tools: Grafana Assistant, Datadog Bits AI, Claude Code, GitHub Copilot, `mcp-grafana` with an MCP-capable assistant.
- **Do without AI (drills):** the PromQL katas, cardinality analysis, alert classification, the mid-term and the practical exam. You must be able to read a query and say what it computes.
- **Verify AI output by:** running every query against known data with a hand-computed expected value; `promtool check` and `promtool test rules`; checking units and label sets; comparing an AI summary of an incident against the raw timeline; checking that no generated config sends PII to an external backend.
- **Where AI still fails here (show it):** in Lab 12, collect AI-written queries that average percentiles, apply `rate()` to gauges, forget `sum by (le)`, or invent label names that do not exist. Give an assistant telemetry with a gap and see whether it notices the gap or explains it away.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs 1–10 | 25% |
| Projects P1 / P2 / P3 | 5% / 15% / 25% |
| Mid-term (AI off) | 10% |
| Practical exam (3 hours, AI off) + oral | 20% |

**Mastery gate.** You pass when you can, without AI help: (1) given an unfamiliar service with a planted fault and only its telemetry, identify the faulty component and the triggering change within 20 minutes; (2) write 8 of 10 requested PromQL/LogQL queries correctly on the first run; (3) cut a provided stack's telemetry volume by at least 50% while keeping 100% of error traces and every alert working (proved by alert unit tests).

## Industry reality

Observability is now a specialist title (observability engineer) as well as a daily duty in SRE and platform teams. Zerodha's engineering blog describes a Prometheus, Grafana and VictoriaMetrics stack across data centres and cloud, and a move from ELK to ClickHouse with Vector for logs. Prometheus and OpenTelemetry are both CNCF graduated, and the CNCF offers Prometheus Certified Associate and OpenTelemetry Certified Associate exams. Zerodha's logging post is a public example of the cost pressure: storage growth, slow ingestion at peak and slow long-range queries, not missing features, drove the redesign.

**Interview questions from this course**

1. *Design monitoring for a new payments API.* Strong answer: user-facing SLIs (success rate, latency) measured at the edge; RED per endpoint; traces with tail sampling that keeps all errors; structured logs with trace IDs; dependency metrics; symptom-based pages and cause-based tickets; dashboards per audience; cost and PII controls.
2. *Our Prometheus is running out of memory. What do you do?* Strong answer: find cardinality offenders (`tsdb analyze`, top series by metric), drop or aggregate unbounded labels, set `sample_limit`, recording rules, shard or federate, move long-term data to Thanos/Mimir/VictoriaMetrics; budgets per team.
3. *How does distributed tracing work across a message queue?* Strong answer: context injected into message headers, links vs parent-child for batch consumers, W3C Trace Context, sampling consistency, what breaks it (libraries that drop headers).
4. *What makes a good alert?* Strong answer: user-visible symptom, urgent, actionable, with a runbook; burn-rate rather than static thresholds; grouping and inhibition; measured with actionable rate and pages per shift; tested with unit tests.
5. *How would you cut a ₹1 crore-a-year observability bill by 40%?* Strong answer: measure cost per service and signal; drop unqueried data; sample traces at the tail; reduce log levels and retention by class; cardinality budgets; consider OTLP-based portability and self-hosting for the biggest streams; keep compliance retention (CERT-In 180 days) in a cheap tier.

## Resources (free first)

- **Texts:** Google SRE book, [Monitoring Distributed Systems](https://sre.google/sre-book/monitoring-distributed-systems/); Brendan Gregg, [USE method](https://www.brendangregg.com/usemethod.html); [OpenTelemetry docs](https://opentelemetry.io/docs/) and [OpenTelemetry Demo](https://opentelemetry.io/docs/demo/).
- **Metrics:** [Prometheus docs](https://prometheus.io/docs/introduction/overview/), [rule unit testing](https://prometheus.io/docs/prometheus/latest/configuration/unit_testing_rules/), [PromLabs PromQL cheat sheet](https://promlabs.com/promql-cheat-sheet/), [Thanos](https://thanos.io/), [Grafana Mimir](https://grafana.com/docs/mimir/latest/), [VictoriaMetrics](https://victoriametrics.com/).
- **Logs:** [Grafana Loki](https://grafana.com/docs/loki/latest/), [Vector](https://vector.dev/), [Fluent Bit](https://fluentbit.io/), [ClickHouse docs](https://clickhouse.com/docs).
- **Traces and profiles:** [W3C Trace Context](https://www.w3.org/TR/trace-context/), [Jaeger](https://www.jaegertracing.io/docs/latest/), [Grafana Tempo](https://grafana.com/docs/tempo/latest/), [Grafana Pyroscope](https://grafana.com/docs/pyroscope/latest/), [Parca](https://www.parca.dev/).
- **eBPF:** [ebpf.io](https://ebpf.io/), [OBI](https://opentelemetry.io/docs/zero-code/obi/), [bpftrace](https://bpftrace.org/).
- **Dashboards:** [Grafana docs](https://grafana.com/docs/grafana/latest/), [Perses](https://perses.dev/).
- **Case studies:** Zerodha, [Infrastructure monitoring with Prometheus](https://zerodha.tech/blog/infra-monitoring-at-zerodha/) and [Logging at Zerodha](https://zerodha.tech/blog/logging-at-zerodha/).
- **Practice locally:** the OpenTelemetry Demo on kind or Docker Compose, with its built-in failure flags; everything in this course runs without a cloud account.
- **Paid, optional:** Majors, Fong-Jones and Miranda, *Observability Engineering* (O'Reilly, 2022).

## Sources

All checked 12 Oct 2026.
- CNCF maturity (OpenTelemetry graduated 11 May 2026; Prometheus graduated 2018; Jaeger graduated 2019; Perses sandbox) from the [CNCF landscape](https://github.com/cncf/landscape) data file.
- Release dates from [endoflife.date](https://endoflife.date/prometheus) (Prometheus 3.0 on 14 Nov 2024; 3.15 on 24 Sep 2026) and GitHub releases (Grafana 13.2, Loki 3.7, Tempo 3.1, Jaeger 2.22, OBI 0.14).
- [Jaeger v2 architecture](https://www.jaegertracing.io/docs/latest/) (built on the OpenTelemetry Collector); [Beyla README](https://github.com/grafana/beyla) (donated to OpenTelemetry as OBI).
- Zerodha Tech Blog, [Logging at Zerodha](https://zerodha.tech/blog/logging-at-zerodha/) (index inflation "a minimum of 3-4x") and [Infrastructure monitoring with Prometheus](https://zerodha.tech/blog/infra-monitoring-at-zerodha/).
- Stack Overflow, [2026 survey results](https://stackoverflow.blog/2026/10/06/the-results-of-the-2026-developer-survey-are-here/) (20% use AI to deploy, operate or troubleshoot production), via this repository's [market map](../../../../06_career_and_market_readiness/01_market_map/roles/OPS_devops_sre_platform_engineering.md).
- [Grafana Assistant docs](https://grafana.com/docs/grafana-cloud/machine-learning/assistant/); [Datadog Bits AI investigation](https://www.datadoghq.com/product/ai/bits-ai-sre/); [mcp-grafana](https://github.com/grafana/mcp-grafana).
- [CNCF certifications](https://www.cncf.io/training/certification/) (PCA, OTCA).
- [CERT-In Directions, 28 Apr 2022](https://www.cert-in.org.in/PDF/CERT-In_Directions_70B_28.04.2022.pdf) (180-day logs).

_Last reviewed: 2026-10_
