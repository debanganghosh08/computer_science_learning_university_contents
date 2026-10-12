# SWE403 · Labs and projects

The labs run on a provided 4-service system ("order → payment → inventory → notification", with Postgres and Kafka) on a local Kubernetes cluster (kind or k3d), with the OpenTelemetry Collector, Prometheus, Grafana, Tempo, Loki and Pyroscope. Faults are injected with Toxiproxy, chaos scripts and planted bugs. The mid-term, the incident drills and the final game day are AI-off for the person in the incident-commander role; other roles may use assistants with read-only access to telemetry.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Postmortem analysis | Classify 10 public postmortems (Cloudflare, Google Cloud, AWS, GitHub and others) by trigger, latent cause, detection and mitigation | Table plus the 3 developer practices that would have prevented the most impact | 3 h |
| 2 · SLOs and burn-rate alerts | SLIs and SLOs for 2 services; multi-window burn-rate alerts | Recording and alert rules; a fault-injection run showing alerts fire at the expected budget burn and stay silent on noise | 5 h |
| 3 · Structured and canonical logs | Convert logging to structured events; add canonical log lines; build a PII redaction filter | 5 operational questions answered with one query each; redaction test catching 100% of planted PII patterns | 4 h |
| 4 · Metrics without cardinality explosions | RED metrics with histograms; exemplars; fix a planted label explosion | Dashboard, series count before/after, and a correct fleet p99 | 4 h |
| 5 · Tracing across a queue | Propagate W3C Trace Context through HTTP, gRPC and Kafka; tail sampling that keeps slow and failed traces | A single trace spanning all 4 services; sampling config with kept-trace statistics | 5 h |
| 6 · Telemetry-only debugging (AI off for the graded run) | Three planted incidents (N+1 query, retry storm, lock contention); find each from telemetry only; then compare with an assistant's analysis | Cause, evidence chain and time-to-cause for each; graded table of the assistant's hypotheses | 5 h |
| 7 · Resilience and config validation | Deadlines, retry budgets, circuit breakers, bulkheads; fail-open/closed per dependency; reject a malformed config and keep the last good one | Chaos results (dependency latency 2 s, 50% errors) showing healthy endpoints stay within SLO | 6 h |
| 8 · Flags and config pipeline | OpenFeature flags with ownership and expiry; a config pipeline with schema validation, size limits, canary and automatic rollback | A doubled-size config (as in Cloudflare 2025) blocked at validation; a bad-but-valid config auto-rolled back at canary | 5 h |
| 9 · Canary analysis | Argo Rollouts or Flagger with metric-based analysis; three-step compatible schema change | Automatic rollback of a release with a planted 2% error regression; zero errors during the schema change | 5 h |

## Projects

### P1 · Make a service observable (L1, ~6 hours)

**Real-world inspiration:** teams adopting OpenTelemetry across existing services, and the common situation of being on call for a service you cannot see inside.

**What to build:** take an existing open-source web application or your SWE303 service. Add structured logs with trace IDs, RED metrics, OpenTelemetry traces with manual spans around business steps, health/readiness endpoints, and a dashboard. Write a one-page runbook.

**Acceptance criteria:**
- Every request produces exactly one canonical log line containing trace ID, route, status, duration and user tier (no PII).
- A trace for the main flow shows every external call (database, cache, HTTP) as a span with useful attributes.
- Five questions given by the instructor are answerable from telemetry within 10 minutes each (recorded).
- Telemetry overhead: p99 latency increase under 5% at a stated load (benchmark with and without instrumentation).

**Stretch goals:** continuous profiling with Pyroscope; a log-volume budget with dynamic sampling.

**What it proves to an employer:** you build services other people can operate, which is part of every senior engineer's job.

### P2 · Safe change pipeline for code and configuration (L2, ~15 hours)

**Real-world inspiration:** the 2025 Cloudflare and Google Cloud outages and the 2024 CrowdStrike incident, all triggered by changes (configuration, data or code) that reached everything too fast. The service is **illustrative**.

**What to build:** for the 4-service system, a delivery pipeline where code, feature flags and configuration/data pushes all go through validation, staged rollout and automatic rollback. Include SLO-based canary analysis, a kill switch per risky feature, and a config schema with size and semantic limits.

**Acceptance criteria:**
- Six planted bad changes (2 code, 2 flag, 2 config/data, including an oversized generated file and a blank-field policy) are each stopped at validation or rolled back at canary before reaching more than 10% of traffic.
- Rollback time under 2 minutes for code and under 30 seconds for flags and config, measured over 5 drills each.
- Every flag has an owner and an expiry; CI fails on expired flags.
- Schema changes follow expand–contract; a 30-minute load test during a migration shows zero errors.
- A written policy: what may change without review, what needs a second approver, and what needs a change window.

**Stretch goals:** cell-based rollout (one cell at a time); a "change freeze" automation tied to error-budget exhaustion.

**What it proves to an employer:** you understand that most outages come from changes, and you can build the system that makes changes safe.

### P3 · Two weeks on call for your own service (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** "you build it, you run it" teams at product companies, where developers carry the pager for their services.

**What to build:** run your P2 system (or a capstone service) for two weeks under realistic synthetic traffic with SLOs, burn-rate alerts, runbooks and an on-call rotation in your team. The instructor injects at least three unannounced failures (dependency slowdown, bad config push, resource exhaustion, data corruption in one partition). Handle each as a real incident, then hold a final game day.

**Acceptance criteria:**
- SLO report for the two weeks: budget consumed per incident, alerts fired, false pages (target ≤ 2), missed incidents (target 0).
- For each injected failure: time to detect, time to mitigate, roles used, and a status-update log; mitigation within the agreed target for at least 2 of 3.
- A blameless postmortem per incident, with contributing factors at code, process and tooling levels and at least one action item implemented and verified before the end of the project.
- Runbooks updated after each incident, with diffs.
- A final report comparing designed behaviour with observed behaviour, including what an AI assistant got right and wrong when given the telemetry.

**Stretch goals:** an incident-review meeting with another team as facilitators; a "learning across incidents" analysis of all teams' postmortems.

**What it proves to an employer:** you can own a production service end to end, under pressure, and make it better after every failure.

## Feeds into

- [SWE501 Frontier Seminar](../../year_5/SWE501_frontier_seminar_agentic_software_engineering/README.md): verification of changes and agents that act in production are open research areas.
- [SWE404 Engineering Leadership and Technical Strategy](../SWE404_engineering_leadership_and_technical_strategy/README.md): incident command and postmortem culture as leadership practice.
- [OPS403 AIOps and Agentic Operations](../../../devops_sre_platform_engineering/year_4/OPS403_aiops_and_agentic_operations/README.md) and [OV12 Agent Infrastructure and Platform Engineering](../../../../04_overlaps/OV12_agent_infrastructure_platform/README.md): automated operations built on these signals.
- [SWE flagship industry project](../../../../06_career_and_market_readiness/05_industry_projects/SWE_software_engineering.md): P3 is its reliability section.
