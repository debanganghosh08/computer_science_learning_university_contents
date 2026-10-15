# OV08A · Labs and projects

All labs build on one product you choose in week 1 (for example a support assistant over a public documentation set, a notice-answering tool for a college department, or a catalogue-drafting tool for a small shop). Use free or student tiers of model APIs, or a small open-weights model served locally; every lab must also run against a deterministic stub so CI does not need paid calls. Lab 5's fixes, the mid-term and the final are done without AI assistants.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Spec and slice map | One-page spec (metrics, eval plan, autonomy level, fallback) and a slice diagram with latency and cost per hop | Spec, diagram, decision records | 4 h |
| 2 · Shared schemas and drift checks | One schema for API, message parts, tools and structured outputs; generated types; CI schema diff | Repo with a failing build on a planted breaking change | 5 h |
| 3 · Streaming with cancellation | SSE from provider to browser through a proxy; cancel propagates upstream; resume after reload | Logs proving upstream cancel within 1 s; TTFT measurement | 6 h |
| 4 · Permission-aware retrieval | ACL metadata at ingestion; filter-before-rank; on-behalf-of tool call | Isolation test: 100 cross-tenant queries, zero foreign chunks | 6 h |
| 5 · Injection and rendering tests | Run the course injection and XSS sets; fix rendering and tool privileges by hand | Before/after findings; zero XSS; documented residual injection risk | 5 h |
| 6 · Recorded responses and E2E | Record 30 model calls; replay in CI; Playwright test of send, stream, cancel, retry; axe-core checks | Green CI with no network calls; zero serious accessibility issues | 6 h |
| 7 · Eval gate in CI | 150-case eval set, one calibrated judge, paired comparison gate | CI run blocking a planted 3-point regression, passing a no-op change in 5 of 5 runs | 7 h |
| 8 · Flags, canary and kill switch | Model and prompt behind OpenFeature flags; 5% canary with automatic rollback; kill switch | Rollback log on a latency guardrail breach; kill-switch time under 60 s | 5 h |
| 9 · Browser-to-model tracing | W3C trace context from the browser; GenAI spans; feedback events joined to traces | One trace screenshot from click to tool span; feedback-to-trace query | 5 h |
| 10 · Cost reduction without regression | Cost per successful task by feature; caching and routing changes | ≥ 30% lower cost per task with the eval gate still green | 5 h |

## Projects

### P1 · Streaming feature with contracts and cancellation (L1, ~6 hours)

**Real-world inspiration:** streaming chat interfaces in production AI products, and the cost of not cancelling upstream generations.

**What to build:** one AI feature (for example "summarise this document") with a shared schema, streaming output, cancellation, persistence of partial results and a deterministic stub for tests.

**Acceptance criteria:**
- p95 time to first token under 1.5 s over 50 requests against a hosted model, measured in the browser.
- Cancelling in the UI stops the upstream request within 1 s in 20 of 20 trials (provider logs or token counts as evidence).
- Reloading mid-stream shows the saved partial output and never triggers a duplicate model call (tested).
- The schema is the single source for UI, API and structured output types; a CI check fails on a breaking change.

**Stretch goals:** resumable streams after network loss; structured partial output rendered as it arrives.

**What it proves to an employer:** you can build the basic AI interaction correctly, including the parts demos skip.

### P2 · Multi-tenant assistant with tests and an eval gate (L2, ~15 hours)

**Real-world inspiration:** GitHub's practice of running thousands of offline tests before changing Copilot's models (Jan 2025); OWASP LLM08:2025 on vector and embedding weaknesses.

**What to build:** a retrieval-backed assistant for at least three tenants with ACL-aware ingestion, citations, one on-behalf-of tool, quotas, the full test pyramid and an eval gate.

**Acceptance criteria:**
- **Isolation:** 500 generated cross-tenant and cross-user queries return zero unauthorised chunks or tool results.
- **Citations:** 95% of answers in the eval set carry at least one citation whose quoted text appears verbatim in the cited chunk (checked by code).
- **Tests:** CI runs unit, recorded-response, contract, property and E2E tests without network access in under 10 minutes; mutation testing on the parser kills at least 80% of mutants.
- **Eval gate:** a 150-case suite with a calibrated judge (agreement with human labels ≥ 85% on 50 cases) blocks a planted regression and passes a no-op change.
- **Abuse:** one user hitting the API at 50 requests/s cannot raise other users' p95 latency by more than 20%.

**Stretch goals:** approval UI for a consequential tool with an audit log; per-tenant prompt overrides with their own eval subset.

**What it proves to an employer:** you can ship an AI feature that is safe for more than one customer and protected against silent regressions.

### P3 · Production-grade AI feature with rollout and operations (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** LinkedIn's account of the last 20% of a generative AI product (Apr 2024); standard SRE practice of canaries, kill switches and post-incident reviews.

**What to build:** take P2 (or a new feature) to a launch-ready state for real users: flags, shadow and canary rollouts, fallbacks, end-to-end tracing with feedback, cost budgets and alerts, runbooks, an incident drill, retention and deletion of traces, AI disclosure, and a launch readiness review. Launch it to at least 15 real users who consent.

**Acceptance criteria:**
- **Release safety:** a model or prompt change goes through eval gate → shadow → 5% canary → 100%, with automatic rollback demonstrated on a planted guardrail breach.
- **Observability:** 100% of AI requests have a trace from the browser to model and tool spans; any feedback event can be joined to its trace in under one minute.
- **Resilience:** with the primary model provider blocked, the feature degrades to the documented fallback within 5 s, and users see a clear state.
- **Cost:** cost per successful task reported daily; a simulated retry storm triggers an alert within 10 minutes; a per-tenant cap holds.
- **Operations:** runbooks for six incident classes; one drill with a written post-incident review that adds at least 10 eval cases.
- **Privacy:** traces are redacted and deleted per a written retention policy; deleting a user removes their traces (tested).
- **Users:** at least 15 consenting users; their feedback summarised with links to traces.
- **AI-error log:** at least five AI-generated changes that broke a cross-layer join, with the check that caught each one.

**Stretch goals:** a generative-UI component with an allow-list; a second model provider behind the same contract; a public write-up.

**What it proves to an employer:** you can own an AI feature in production, not just build one.

## Feeds into

[OV08B](../OV08B_product_analytics_and_growth_for_ai_apps/README.md) instruments and grows the product built here. [FE403](../../../03_majors/frontend_engineering/year_4/FE403_ai_native_interfaces_streaming_generative_ui/README.md), [BE403](../../../03_majors/backend_engineering/year_4/BE403_backends_for_ai_serving_llm_features_vector/README.md) and [AIE404](../../../03_majors/ai_engineering/year_4/AIE404_ai_product_engineering_and_ux/README.md) take each layer deeper in semester 8. The OV08 capstone in the [overlap README](../README.md) launches the same product to a wider user base.
