# AIE403 · Labs and projects

Every lab and project runs against a real LLM application you own: your AIE303 RAG system, your AIE304 agent, or the course's reference app. Deliverables include dashboards (exported JSON or screenshots with queries), alert rules, runbooks and a write-up with before/after numbers. Never put real personal data into traces; use synthetic Indian records for PII tests.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Artefact inventory and SLOs | List every behaviour-changing artefact (prompts, model IDs, indexes, tool schemas, guardrail configs); write SLOs and an error-budget policy | Inventory, SLO document, owners | 3 h |
| 2 · OpenTelemetry GenAI instrumentation, redaction and dashboards | Instrument inference, retrieval, tool and agent spans; self-host Langfuse or Phoenix; redact PII before export; build per-feature and per-tenant dashboards | Traces validated against the convention repo, redaction tests, dashboard answering "why did cost double?" | 7 h |
| 3 · Online judges, drift and canaries | Run a calibrated judge on 2% of traffic with daily CIs; detect a simulated shift to Hinglish; hourly canary prompts with output-distribution alerts | Quality time series, drift alert, canary job and alert rule | 5 h |
| 4 · Guardrail evaluation | Measure Llama Guard 4 and Prompt Guard 2 (or equivalents) on labelled sets; add a groundedness check and a PII redaction pipeline | Precision, recall, latency per guardrail; threshold choice for a target false-block rate | 5 h |
| 5 · Cost and latency engineering | Attribute cost per tenant; restructure prompts for caching; move a nightly job to batch; route easy intents to a small model; build a latency waterfall and cut p95 | Savings table, cache hit rate, quality check on the golden set, p95 before/after with each change's contribution | 8 h |
| 6 · Gateway, quotas and failover | Deploy LiteLLM proxy or your own gateway with per-app budgets, per-tenant quotas, circuit breakers and a secondary provider; trigger a spend anomaly | Config, load-test results with a noisy neighbour, failover test log | 5 h |
| 7 · Release gates and canaries | Release manifest pinning all artefacts; CI gate with eval, safety, cost and latency budgets; 5% canary with automatic rollback | Pipeline config, a rollback triggered by a planted regression | 5 h |
| 8 · Incident drill | Contain a planted incident (harmful output after a prompt change) in 15 minutes with kill switches; investigate from traces; write a postmortem | Drill timeline, postmortem, new regression tests | 4 h |
| 9 · vLLM serving dashboard and autoscaling | Scrape vLLM metrics into Prometheus; autoscale on queue depth and KV-cache use under stepped load | Dashboard, autoscaling policy, cost per million tokens at three utilisation levels | 5 h |
| 10 · Data-flow map, DPDP design and evidence pack | Map data flows and retention; write the DPDP and EU AI Act sections of the design doc; assemble an audit evidence pack | Diagram, design-doc sections, evidence index | 5 h |

## Projects

### P1 · Make an LLM app observable (L1, ~6 hours)

**Real-world inspiration.** OpenTelemetry's GenAI semantic conventions define attributes for model calls and spans for agents and tools (status: development). Open-source tools such as Langfuse, Arize Phoenix and OpenLLMetry build on them, so teams can answer cost and quality questions without vendor lock-in.

**What to build.** Instrument an existing LLM application end to end and stand up a self-hosted tracing backend with three dashboards: cost (per feature, tenant and model), latency (TTFT, total, per span) and quality (judge scores and feedback joined to traces).

**Acceptance criteria**
- 100% of model calls produce spans with model, token usage and cost; attribute names match the current convention repository.
- A redaction test with 200 synthetic records (phone numbers, Aadhaar-like and PAN-like IDs, UPI IDs) shows zero leaks into the trace store.
- The cost dashboard reproduces the provider's billed usage for one day within 2%.
- A short note answers three operational questions from the dashboards alone (for example, the slowest step and the most expensive tenant).

**Stretch goals.** Trace context across an MCP or A2A hop; trace sampling that keeps all error traces.

**What it proves to an employer.** You can make an AI system measurable, the first job any LLMOps team gives a new engineer.

### P2 · An LLM gateway with budgets, routing and failover (L2, ~15 hours)

**Real-world inspiration.** Teams centralise model access behind gateways for credentials, budgets, routing and audit (LiteLLM, vendor gateway guidance). OWASP lists unbounded consumption (LLM10:2025) among the top LLM risks. Batch discounts (50% at Anthropic, OpenAI and Google) and cascades such as FrugalGPT (2023) are among the biggest cost levers.

**What to build.** A gateway in front of two applications and two providers (one may be a local vLLM server). It enforces per-app budgets and per-tenant quotas, routes by intent with quality guards, uses prompt-caching-friendly request shaping, sends offline work to batch, fails over on provider errors with circuit breakers, and alerts on spend anomalies. Include a degraded mode (smaller model or cached answer plus a human-handoff message).

**Acceptance criteria**
- Under a replayed traffic mix, cost per successful task drops by at least 30% versus the ungoverned baseline, with no statistically significant quality loss on the golden set.
- A noisy tenant at 10× normal traffic cannot push other tenants' p95 latency above their SLO.
- With the primary provider failing 50% of requests, availability stays ≥ 99% for interactive traffic (measured), using failover or the degraded mode.
- A synthetic spend burst triggers an alert within 5 minutes and an automatic per-tenant cap.
- All routing decisions are logged and visible in traces.

**Stretch goals.** Learned routing; semantic caching with tenant isolation and a measured staleness rate.

**What it proves to an employer.** You can control the three things finance, product and SRE all care about: cost, reliability and fairness between customers.

### P3 · Two weeks of production: a game-day operated LLM service (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** Public incidents show what goes wrong without operations discipline: a chatbot swearing after a system update (DPD, Jan 2024), legal liability for a chatbot's wrong policy advice (Moffatt v. Air Canada, Feb 2024), and a dealer chatbot talked into absurd "deals" (Dec 2023). India's DPDP Rules phase in most obligations by about May 2027, and EU general-purpose AI obligations have applied since August 2025. The service and its traffic are simulated, and the incidents are planted by the instructor.

**What to build.** Operate your RAG system or agent as a service for two weeks under replayed and synthetic traffic, with SLOs and error budgets, online evaluation and canaries, layered guardrails, the P2 gateway, a release pipeline with gates and canaries, an on-call rotation (with classmates), and an audit evidence pack. During the two weeks, the instructor injects at least four incidents without warning: a provider behaviour change, a cost spike, a harmful-output regression and a document-borne injection attempt using a benign canary.

**Acceptance criteria**
- All four injected incidents are detected by alerts (not by the instructor telling you), contained within 15 minutes of the alert, and covered by blameless postmortems with regression tests merged.
- SLO compliance reported daily; error-budget decisions (for example freezing releases) are documented.
- At least three releases ship through the gated pipeline, including one automatic rollback.
- Cost per successful task and p95 latency improve by stated targets agreed in week 1, with evidence.
- The evidence pack maps controls to DPDP obligations, the EU AI Act risk tier analysis, NIST AI 600-1 and ISO/IEC 42001 clauses, with links to traces, eval runs and change history.

**Stretch goals.** Chaos experiments on the vector store and retrieval path; a public status page with incident history.

**What it proves to an employer.** You have operated an AI service through real failures and can show the paper trail. That experience usually takes a year on the job to collect.

## Feeds into

- [AIE501 Frontier Seminar](../../year_5/AIE501_frontier_seminar_long_horizon_autonomous_agents/README.md): oversight and monitoring of long-running agents.
- [OV04B LLMOps at Scale](../../../../04_overlaps/OV04_mlops_ml_platform/OV04B_llmops_at_scale/README.md) and [OV12A Running Agents in Production](../../../../04_overlaps/OV12_agent_infrastructure_platform/OV12A_running_agents_in_production_sandboxes_durable/README.md): platform-scale operations.
- [IND401 Industry Co-op Studio](../../../../05_shared_years_3_to_5/IND401_industry_co_op_studio/README.md): the on-call and postmortem practice transfers directly to co-op teams.

## Sources

- OpenTelemetry GenAI semantic conventions — https://github.com/open-telemetry/semantic-conventions-genai ; Langfuse — https://github.com/langfuse/langfuse ; Phoenix — https://github.com/Arize-ai/phoenix ; OpenLLMetry — https://github.com/traceloop/openllmetry (checked 2026-10)
- OWASP LLM10:2025 Unbounded Consumption — https://genai.owasp.org/llmrisk/llm102025-unbounded-consumption/ ; LiteLLM — https://github.com/BerriAI/litellm ; Chen et al., FrugalGPT (2023) — https://arxiv.org/abs/2305.05176 (checked 2026-10)
- TIME on DPD (Jan 2024) — https://time.com/6564726/ai-chatbot-dpd-curses-criticizes-company/ ; CTV News on Moffatt v. Air Canada (Feb 2024) — https://www.ctvnews.ca/vancouver/article/air-canadas-chatbot-gave-a-bc-man-the-wrong-information-now-the-airline-has-to-pay-for-the-mistake/ ; VentureBeat on the Chevrolet dealer chatbot (Dec 2023) — https://venturebeat.com/ai/a-chevy-for-1-car-dealer-chatbots-show-perils-of-ai-for-customer-service (checked 2026-10)
- PIB, DPDP Rules 2025 — https://www.pib.gov.in/PressReleasePage.aspx?PRID=2190014 ; European Commission AI Act page — https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai ; ISO/IEC 42001 — https://www.iso.org/standard/42001 (checked 2026-10)
