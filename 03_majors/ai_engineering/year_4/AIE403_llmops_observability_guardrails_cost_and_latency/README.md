# AIE403 · LLMOps: Observability, Guardrails, Cost and Latency

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 8 | 4 (≈ 120 hours) | L2 → L4 | [AIE303](../../year_3/AIE303_retrieval_augmented_generation_and_search/README.md); assumes [AIE305](../../year_3/AIE305_evaluating_llm_systems/README.md), [CS215](../../../../02_year_2_core_computer_science/semester_4/CS215_cloud_and_devops_foundations/README.md); [OPS303](../../../devops_sre_platform_engineering/year_3/OPS303_observability_metrics_logs_traces/README.md) recommended | [AIE501](../../year_5/AIE501_frontier_seminar_long_horizon_autonomous_agents/README.md), [OV04 MLOps and ML Platform](../../../../04_overlaps/OV04_mlops_ml_platform/), [OV12 Agent Infrastructure](../../../../04_overlaps/OV12_agent_infrastructure_platform/) |

## Why this course matters now

Shipping an LLM feature is the easy part. Running it for a year, with quality, cost, latency and safety under control, is where teams struggle. The failure modes are public. A delivery company's support chatbot began swearing at a customer after a system update and had to be switched off (DPD, January 2024). A Canadian tribunal held Air Canada liable for its chatbot's wrong refund advice, rejecting the argument that the chatbot was responsible for its own words (February 2024). The tooling has matured. OpenTelemetry defines GenAI semantic conventions, including agent spans, though they are still marked "development". Open-source tracing (Langfuse, Arize Phoenix, OpenLLMetry), gateways (LiteLLM) and guardrail models (Llama Guard 4, Llama Prompt Guard 2, NeMo Guardrails) are widely used. The cost levers are large: batch APIs cost 50% less at Anthropic, OpenAI and Google, and Anthropic bills cached prompt reads at 10% or less of the base input price. Regulation is now operational too. EU obligations for general-purpose AI models apply from 2 August 2025, India's DPDP Rules were notified in November 2025 with phased deadlines, and India's AI Governance Guidelines followed the same month. AI tools now triage traces and draft postmortems. The human work is setting the SLOs, designing layered defences, owning the incident and saying no to a launch when the evidence is weak.

## Learning outcomes

By the end you can:

1. **Instrument** an LLM application with OpenTelemetry GenAI conventions and **build** dashboards for quality, latency, cost and safety per feature and tenant.
2. **Define** SLOs for LLM features (TTFT, success rate, judged quality, cost per task) and **operate** error budgets for them.
3. **Run** online evaluation on sampled production traffic and **detect** drift and silent provider changes.
4. **Design** layered guardrails (input, retrieval, tool, output) and **measure** their catch rate, false-positive rate and added latency.
5. **Engineer** cost: attribution, budgets, caching, batching, routing and output control, and **report** unit economics such as cost per resolved ticket.
6. **Engineer** latency: TTFT and tail latency analysis, streaming, parallelism, caching and model choice.
7. **Operate** reliability controls (gateways, rate limits, quotas, multi-provider failover, circuit breakers, load shedding) and **defend** against unbounded consumption.
8. **Release** prompt, model and configuration changes safely (eval gates, shadow, canary, rollback) and **run** an AI incident from detection to postmortem.
9. **Map** a system's controls to DPDP, the EU AI Act, NIST AI RMF and ISO/IEC 42001, and **maintain** the evidence an auditor will ask for.

## Chapters and lessons

### Chapter 1 · What LLMOps adds (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 New deployables | Prompts, model IDs, retrieval indexes, tool schemas and guardrail configs all change behaviour; provider-side changes you do not control | Inventory every behaviour-changing artefact in your AIE303 system |
| 1.2 SLOs for LLM features | Availability, TTFT p95, full-response p95, task success, judged quality, safety violation rate, cost per task; error budgets (Google SRE books) | Write SLOs and error-budget policy for a support assistant |
| 1.3 The LLMOps loop | Trace → evaluate → alert → triage → fix → regression test → release | Draw the loop for your team; mark owners |
| 1.4 Failure catalogue | Public incidents (DPD 2024, Air Canada 2024, Chevrolet dealer chatbot 2023), AI Incident Database, OECD AI incidents monitor | Classify 10 public incidents by root cause and missing control |

**Check your understanding:** Why is "the model provider changed something" an operational risk you must monitor, not just a vendor issue? Which SLO would you page someone for at 3 a.m.? Why is quality an SLO and not only a test?

### Chapter 2 · Tracing and observability (weeks 2–3)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 GenAI semantic conventions | `gen_ai.*` attributes (operation, provider, request and response model, token usage), inference vs agent vs tool spans (`invoke_agent`, `execute_tool`); status: development | Instrument a RAG + tool app; validate attribute names against the spec repo |
| 2.2 Tooling | OpenInference, OpenLLMetry, Langfuse (MIT core, self-hostable), Arize Phoenix (Elastic License 2.0) | Self-host Langfuse or Phoenix; send traces from two services |
| 2.3 Content in traces | Prompt and completion capture, PII redaction, sampling, retention limits, access control on traces | Add redaction before export; prove no phone numbers or Aadhaar-like IDs reach the store |
| 2.4 Dashboards | Per-feature and per-tenant views of tokens, cost, latency percentiles, error codes, cache hit rate | Build a dashboard that answers "why did cost double yesterday?" |
| 2.5 Linking traces to quality | Attaching eval scores and user feedback to trace IDs | Join judged scores to traces; find the slowest low-quality path |

**Check your understanding:** Why should prompts in traces be treated as sensitive data? What attributes do you need to compute cost per tenant? Why adopt a semantic convention that is still in development?

### Chapter 3 · Online evaluation and monitoring (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Sampling production | Stratified sampling of traces for LLM judges and human review; cost control | Run a calibrated judge on 2% of traffic; report daily quality with CIs |
| 3.2 Drift | Input drift (topics, languages, length), output drift (length, refusal rate, citation rate), embedding-based topic tracking | Detect a simulated shift from English to Hinglish queries |
| 3.3 Provider canaries | Fixed probe prompts run hourly to detect silent model or tokenizer changes | Build a canary job and alert on output-distribution changes |
| 3.4 Feedback loops | Thumbs, edits, escalations; joining them to traces; their biases | Add escalation-rate alerts tied to specific prompt versions |

**Check your understanding:** Why might quality fall while every infrastructure metric stays green? What is a good canary prompt? How do you know a drift alert is real and not seasonal?

### Chapter 4 · Guardrails (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Layered defence | Input checks, retrieval filters, tool-call policy, output checks, human escalation; no single layer is sufficient | Draw the guardrail stack for an assistant that can issue refunds |
| 4.2 Classifier guardrails | Llama Guard 4 (hazard categories), Llama Prompt Guard 2 (injection and jailbreak detection) and their limits; constitutional classifiers (Anthropic, 2025) | Measure precision, recall and latency of two classifiers on your labelled set |
| 4.3 Programmable rails | NeMo Guardrails (Colang flows), Guardrails AI validators, schema validation, groundedness checks (as in DoorDash's two-tier guardrail) | Implement a groundedness check that blocks unsupported answers |
| 4.4 PII and data loss prevention | Redaction (Presidio), Indian identifiers (Aadhaar, PAN, UPI IDs), output scanning for secrets | Build a redaction pipeline; test it on 200 synthetic Indian records |
| 4.5 Trade-offs | False positives, added latency, user frustration, bypasses; evaluating guardrails like any model | Tune thresholds to a target false-positive rate; report the safety cost |

**Check your understanding:** Why can a prompt-injection classifier never be your only control? What happens to user trust at a 5% false-block rate? Which guardrail belongs on tool calls rather than on text?

### Chapter 5 · Cost engineering (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Attribution | Cost per request, feature, tenant and user from token usage and price tables; showback | Build per-tenant cost reports from traces |
| 5.2 Caching | Provider prompt caching (prefix design, hit-rate monitoring); response and semantic caching and their staleness and privacy risks | Restructure prompts for caching; report hit rate and savings |
| 5.3 Batch and async | Moving evals, enrichment and backfills to batch APIs (50% off, results within 24 h) | Move one nightly job to batch; report savings and delay |
| 5.4 Routing and cascades | FrugalGPT cascades (2023), RouteLLM (2024), rule-based routing by intent; quality guards on routes | Route easy intents to a small model; prove no quality loss on the golden set |
| 5.5 Unit economics | Cost per resolved ticket or per successful task; margins; pricing AI features | Write the unit-economics page for the application behind your P2 gateway |

**Check your understanding:** Why can a semantic cache leak one user's answer to another? A cheaper model raised cost per resolved ticket: how? Which cost metric would you show a CFO?

### Chapter 6 · Latency engineering (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Anatomy | Network, queueing, prefill (TTFT), decode, tool calls, retrieval, guardrails; p50 vs p99 | Build a waterfall of a slow request from its trace |
| 6.2 Perceived latency | Streaming, early partial results, progress events; response-time limits (0.1 s, 1 s, 10 s; Nielsen) | Add streaming and progress events; measure time to first useful content |
| 6.3 Structural fixes | Parallel tool calls and retrieval, prompt caching for TTFT, smaller first-hop models, precomputation, regional endpoints | Cut p95 by 40% without quality loss; document each change's contribution |
| 6.4 Tail latency | Long outputs, retries, cold caches, provider congestion; hedged requests and timeouts | Simulate provider slowness; add hedging; measure the cost |

**Check your understanding:** Why does adding a guardrail call in series hurt p99 more than p50? When is a hedged request worth paying for twice? What makes a 30-second agent run feel acceptable to users?

### Chapter 7 · Reliability: gateways, quotas and failover (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 LLM gateways | Central credentials, routing, logging, budgets and policy (LiteLLM proxy; gateway patterns in vendor docs) | Deploy a gateway; route two apps through it with per-app budgets |
| 7.2 Rate limits and quotas | Provider RPM/TPM limits, per-tenant quotas, token buckets, priority queues | Implement per-tenant quotas; load-test a noisy neighbour |
| 7.3 Failover | Multi-provider and multi-region fallback, circuit breakers, degraded modes (smaller model, cached answers, human handoff) | Kill the primary provider in a test; verify graceful degradation |
| 7.4 Unbounded consumption | OWASP LLM10:2025 (denial of wallet, resource exhaustion); input-size limits; per-user caps; anomaly alerts | Add spend anomaly detection; trigger it with a synthetic burst |

**Check your understanding:** Why does failover between providers need its own eval? What is the cheapest degraded mode that still helps users? How can one user make your monthly bill explode?

### Chapter 8 · Release engineering (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Registries | Versioned prompts, model IDs, retrieval index versions and guardrail configs, deployed together | Create a release manifest that pins every artefact |
| 8.2 Gates | Offline eval thresholds, safety suites, cost and latency budgets before deploy | Wire a release gate into CI/CD |
| 8.3 Progressive delivery | Shadow traffic, canary percentages, automatic rollback on SLO breach, feature flags | Canary a prompt change at 5%; roll back automatically on a quality drop |
| 8.4 Provider lifecycle | Deprecation and retirement calendars, pinned snapshots, upgrade evals | Build a calendar of every model your org uses and its retirement date |

**Check your understanding:** Why must the retrieval index version be part of a release? What does shadow traffic tell you that an offline eval cannot? Who signs off a model upgrade?

### Chapter 9 · Incident response for AI features (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Incident types | Harmful or offensive output, wrong advice with legal effect, data leakage, injection exploitation, cost spike, quality regression, provider outage | Write severity definitions for each type |
| 9.2 Kill switches and containment | Feature flags, disabling tools, forcing human handoff, rate-limiting a tenant | Practise a 10-minute containment drill |
| 9.3 Investigation | Reconstructing a conversation from traces; which version answered; was it reproducible | Investigate a planted incident from traces alone |
| 9.4 Postmortems | Blameless reviews, contributing factors, regression tests, customer communication | Write the postmortem for the drill, including the new regression tests |

**Check your understanding:** What must be logged today so that you can investigate next month's incident? Why does the Air Canada decision matter to engineers, not only lawyers? When do you switch a feature off rather than patch it?

### Chapter 10 · Operating self-hosted inference (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Serving metrics | vLLM metrics: running/waiting requests, KV-cache usage, prefix-cache hit rate, TTFT and inter-token latency | Scrape vLLM metrics into Prometheus; build a GPU serving dashboard |
| 10.2 Autoscaling | Scaling on queue depth and KV-cache pressure, not CPU; cold-start costs of large models | Autoscale a deployment under a stepped load test |
| 10.3 Capacity and cost | Utilisation targets, batch sizes, quantisation, reserved vs on-demand GPUs (deeper in [CLD404](../../../cloud_engineering/year_4/CLD404_ai_infrastructure_in_the_cloud_gpus_inference/README.md)) | Compute cost per million tokens at three utilisation levels |
| 10.4 Multi-model fleets | Several models and LoRA adapters behind one endpoint, per-tenant routing, GPU sharing, canary rollout of new weights | Add a second model behind your endpoint; route by tenant; roll out new weights to 10% with automatic rollback |

**Check your understanding:** Why is CPU utilisation a poor autoscaling signal for LLM serving? What happens to latency as KV-cache usage approaches 100%? When does reserved GPU capacity pay off?

### Chapter 11 · Governance, privacy and compliance (weeks 12–13)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Data handling | Provider data retention and zero-data-retention options, regional processing, logging minimisation | Map your system's data flows and retention periods |
| 11.2 India | DPDP Act 2023 and Rules 2025 (notified Nov 2025; consent-manager provisions after 12 months, most obligations after 18 months); India AI Governance Guidelines (Nov 2025) | Write the DPDP section of your system's design doc |
| 11.3 EU and international | EU AI Act: general-purpose AI obligations from 2 Aug 2025; transparency obligations from Aug 2026; Annex III high-risk obligations moved to 2 Dec 2027 by the 2026 AI Omnibus; NIST AI RMF and AI 600-1; ISO/IEC 42001 management systems | Classify three products under the EU AI Act risk tiers |
| 11.4 Evidence | Model and prompt inventory, eval records, incident logs, change history, access reviews | Assemble an audit evidence pack for your P3 system |

**Check your understanding:** What does zero data retention not protect you from? Which DPDP obligation most affects your logging design? What evidence would prove your AI feature was tested before launch?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Artefact inventory and SLOs | SLO document |
| 2 | 2 | Lab 2 · OTel GenAI instrumentation | — |
| 3 | 2 | Lab 2 (cont.): redaction and dashboards | **P1 due** |
| 4 | 3 | Lab 3 · Online judges, drift and canaries | — |
| 5 | 4 | Lab 4 · Guardrail evaluation | — |
| 6 | 5 | Lab 5 · Cost attribution, caching and routing | Mid-term (AI off): cost and latency analysis |
| 7 | 6 | Lab 5 (cont.): Latency waterfall and fixes | — |
| 8 | 7 | Lab 6 · Gateway, quotas and failover | **P2 due** |
| 9 | 8 | Lab 7 · Release gates and canaries | — |
| 10 | 9 | Lab 8 · Incident drill | Postmortem |
| 11 | 10 | Lab 9 · vLLM serving dashboard and autoscaling | — |
| 12 | 11 | Lab 10 · Data-flow map and DPDP design section | — |
| 13 | 11 | Lab 10 (cont.): audit evidence pack | Evidence pack |
| 14 | Integration | P3 demo day | **P3 due** |
| 15 | Review | Oral defence of P3 | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** writing instrumentation and dashboard code; summarising clusters of traces; drafting runbooks and postmortems for you to correct; generating synthetic PII test data (never real data); explaining unfamiliar metrics.
- **Do without AI (drills):** compute a feature's monthly cost and the savings from caching and routing by hand; read a trace waterfall and name the bottleneck; write SLOs and severity levels; run the incident drill's first 10 minutes without assistants; map a data flow and its retention periods.
- **Verify AI output by:** checking generated attribute names against the GenAI semantic-convention repo; replaying traffic to confirm a claimed cost or latency improvement; testing guardrails on labelled sets for both misses and false blocks; having a second person review any compliance statement against the primary legal text.
- **Where AI still fails here (show it):** assistants confidently state regulatory dates that changed (the EU AI Act high-risk timeline moved in 2026; compare three model answers with the Commission page); they write instrumentation using older attribute names; and AI-drafted postmortems tend to blame "the model" instead of missing controls (rewrite one to name the control that failed).

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1–P3 | 35% |
| SLO document, postmortem, evidence pack | 10% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) + oral defence of P3 | 20% |

**Mastery gate.** You pass when you can: (1) take an uninstrumented LLM service and, in one working day, deliver traces, a cost-and-quality dashboard, three SLOs with alerts and a release gate; (2) during a live drill, contain a planted AI incident within 15 minutes and produce a postmortem with regression tests within 24 hours; (3) cut a service's cost per successful task by at least 30% with no statistically significant quality loss, and show the evidence.

## Industry reality

LLMOps practices are converging on familiar SRE foundations with new signals. Observability vendors and open-source projects implement the OpenTelemetry GenAI conventions, which now define agent spans as well. Guardrail stacks combine classifiers (Llama Guard 4, Prompt Guard 2), programmable rails (NeMo Guardrails) and domain checks; DoorDash's support system uses a semantic-similarity check followed by an LLM evaluator (2024). Cost work is a product discipline: provider batch discounts, prompt caching and model routing (FrugalGPT, RouteLLM) are standard levers. Legal liability is real (Moffatt v. Air Canada, 2024), and in India the DPDP Rules' 18-month phase-in ends around May 2027, so logging, consent and retention designs made now must comply then.

**Interview questions from this course**

1. *Our LLM bill doubled last week with flat traffic. Investigate.* Strong answer: per-feature and per-tenant attribution from traces; check output length, cache hit rate, retries, routing changes, agent step counts, a new prompt version, tokenizer or model change, abuse; fix and add an anomaly alert.
2. *Design guardrails for an assistant that can issue refunds up to ₹5,000.* Strong answer: least-privilege tool with server-side limits, idempotency and approval above a threshold; injection-aware design; output checks for policy and PII; logging and review; measured false-positive rate; human escalation.
3. *What SLOs would you set for an LLM support assistant?* Strong answer: availability, TTFT and full-response p95, resolved-without-escalation rate, judged quality on sampled traffic, safety violation rate, cost per resolved ticket; error-budget policy and owners.
4. *A provider silently changed its model and quality dropped. How would you have caught it, and what now?* Strong answer: hourly canaries, online judges with CIs, pinned snapshots; now: confirm with traces, roll to a pinned or alternate model through the gateway, run the regression suite, talk to the provider, add the case to the suite.
5. *What changes for us under DPDP and the EU AI Act?* Strong answer: data-flow mapping, consent and purpose limitation, retention and erasure, breach reporting, processor contracts; EU risk-tier classification, GPAI obligations for model providers, transparency duties, high-risk timeline after the 2026 Omnibus; evidence and owners.

## Resources (free first)

- **Observability:** OpenTelemetry GenAI semantic conventions — https://github.com/open-telemetry/semantic-conventions-genai ; OpenInference — https://github.com/Arize-ai/openinference ; OpenLLMetry — https://github.com/traceloop/openllmetry ; Langfuse — https://langfuse.com/docs ; Arize Phoenix — https://github.com/Arize-ai/phoenix ; vLLM metrics — https://docs.vllm.ai/en/latest/usage/metrics/
- **SRE foundations:** Google SRE books (free online) — https://sre.google/books/
- **Guardrails:** NeMo Guardrails — https://github.com/NVIDIA-NeMo/Guardrails ; Llama Guard 4 — https://huggingface.co/meta-llama/Llama-Guard-4-12B ; Llama Prompt Guard 2 — https://dev.meta.ai/llama/docs/model-cards-and-prompt-formats/prompt-guard ; Guardrails AI — https://github.com/guardrails-ai/guardrails ; Presidio — https://github.com/data-privacy-stack/presidio ; Anthropic, constitutional classifiers — https://www.anthropic.com/research/constitutional-classifiers
- **Cost and reliability:** LiteLLM proxy — https://docs.litellm.ai/docs/simple_proxy ; LLM gateway concepts — https://code.claude.com/docs/en/llm-gateway ; Anthropic prompt caching — https://platform.claude.com/docs/en/build-with-claude/prompt-caching ; OpenAI batch — https://developers.openai.com/api/docs/guides/batch ; OWASP LLM10:2025 — https://genai.owasp.org/llmrisk/llm102025-unbounded-consumption/
- **Incidents:** AI Incident Database — https://incidentdatabase.ai/ ; OECD AI Incidents Monitor — https://oecd.ai/en/incidents
- **Governance:** EU AI Act policy page — https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai ; NIST AI RMF — https://www.nist.gov/itl/ai-risk-management-framework ; NIST AI 600-1 — https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf ; ISO/IEC 42001 — https://www.iso.org/standard/42001 ; India AI Governance Guidelines — https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/nov/doc2025115685601.pdf ; Anthropic API data retention — https://platform.claude.com/docs/en/manage-claude/api-and-data-retention

## Sources

- TIME, DPD chatbot incident (Jan 2024) — https://time.com/6564726/ai-chatbot-dpd-curses-criticizes-company/ ; CTV News, Moffatt v. Air Canada, 2024 BCCRT 149 (Feb 2024) — https://www.ctvnews.ca/vancouver/article/air-canadas-chatbot-gave-a-bc-man-the-wrong-information-now-the-airline-has-to-pay-for-the-mistake/ ; VentureBeat, Chevrolet dealer chatbot (Dec 2023) — https://venturebeat.com/ai/a-chevy-for-1-car-dealer-chatbots-show-perils-of-ai-for-customer-service (checked 2026-10)
- OpenTelemetry GenAI semantic conventions repository and agent spans (status: development) — https://github.com/open-telemetry/semantic-conventions-genai (checked 2026-10)
- Langfuse licence (MIT except `ee`) — https://github.com/langfuse/langfuse ; Phoenix licence (Elastic License 2.0) — https://github.com/Arize-ai/phoenix ; LiteLLM — https://github.com/BerriAI/litellm (checked 2026-10)
- Anthropic prompt caching and batch pricing; models overview (cache reads at 2.5–10% of input price) — https://platform.claude.com/docs/en/about-claude/models/overview ; OpenAI batch (50%, 24 h) — https://developers.openai.com/api/docs/guides/batch ; Gemini batch (50%) — https://ai.google.dev/gemini-api/docs/batch-api (checked 2026-10)
- DoorDash, LLM-based Dasher support automation (Sept 2024) — https://careersatdoordash.com/blog/large-language-modules-based-dasher-support-automation/ (checked 2026-10)
- Chen et al., FrugalGPT (2023) — https://arxiv.org/abs/2305.05176 ; Ong et al., RouteLLM (2024) — https://arxiv.org/abs/2406.18665 ; Sharma et al., Constitutional Classifiers (2025) — https://arxiv.org/abs/2501.18837 (checked 2026-10)
- Nielsen Norman Group, "Response Times: The 3 Important Limits" — https://www.nngroup.com/articles/response-times-3-important-limits/ (checked 2026-10)
- European Commission, AI Act regulatory framework page (GPAI obligations from 2 Aug 2025; Annex III high-risk moved to 2 Dec 2027 by the AI Omnibus) — https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai (checked 2026-10)
- PIB, DPDP Rules 2025 notified (Nov 2025) — https://www.pib.gov.in/PressReleasePage.aspx?PRID=2190014 ; India AI Governance Guidelines (5 Nov 2025) — https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/nov/doc2025115685601.pdf (checked 2026-10)
- NIST AI 600-1 (Jul 2024) — https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf ; ISO/IEC 42001:2023 — https://www.iso.org/standard/42001 (checked 2026-10)

_Last reviewed: 2026-10_
