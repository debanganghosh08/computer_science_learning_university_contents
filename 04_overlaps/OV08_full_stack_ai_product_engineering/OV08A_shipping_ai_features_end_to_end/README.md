# OV08A · Shipping AI Features End to End

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 7 | 4 (≈ 120 hours) | L2 → L4 | [FE302](../../../03_majors/frontend_engineering/year_3/FE302_react_and_component_architecture/README.md), [BE301](../../../03_majors/backend_engineering/year_3/BE301_api_design_rest_grpc_and_graphql/README.md), [AIE302](../../../03_majors/ai_engineering/year_3/AIE302_prompt_and_context_engineering/README.md); co-requisites [FE403](../../../03_majors/frontend_engineering/year_4/FE403_ai_native_interfaces_streaming_generative_ui/README.md), [BE403](../../../03_majors/backend_engineering/year_4/BE403_backends_for_ai_serving_llm_features_vector/README.md), [AIE404](../../../03_majors/ai_engineering/year_4/AIE404_ai_product_engineering_and_ux/README.md) (semester 8; this course gives "just enough" of each layer first) | [OV08B](../OV08B_product_analytics_and_growth_for_ai_apps/README.md), [THS501](../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md), [LCH502](../../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md) |

## Why this course matters now

Building an AI demo takes an afternoon; shipping an AI feature that stays correct, affordable and debuggable takes a team discipline. LinkedIn's engineers reported reaching 80% of the basic experience they wanted within the first month of building a generative AI product, then spending four more months trying to pass 95% of the full experience ([LinkedIn Engineering, Apr 2024](https://www.linkedin.com/blog/engineering/generative-ai/musings-on-building-a-generative-ai-product)). GitHub runs more than 4,000 offline tests, most in CI, before changing the models behind Copilot ([GitHub, Jan 2025](https://github.blog/ai-and-ml/generative-ai/how-we-evaluate-models-for-github-copilot/)). Coding agents such as Claude Code, Cursor, GitHub Copilot and OpenAI Codex now generate most of the boilerplate in a feature like this: the chat component, the API route, the retrieval call. What they do not do reliably is keep the contracts between layers consistent, write tests that catch a quality regression rather than a syntax error, or connect a user's complaint to the exact model call that caused it. This course is about those joins.

## Learning outcomes

By the end you can:

1. **Write** an AI feature spec that includes users, a success metric, a guardrail metric, an evaluation plan, an autonomy level and a fallback.
2. **Define** typed contracts (JSON Schema or Zod) shared by the UI, the API, tool definitions and structured model outputs, and **detect** contract drift in CI.
3. **Build** a streaming vertical slice with cancellation that propagates from the browser to the model provider, and persist partial results safely.
4. **Implement** permission-aware retrieval and tool calls that act on behalf of the signed-in user, and **show** that one tenant cannot reach another's data.
5. **Test** AI features with fake models, recorded responses, contract tests, end-to-end browser tests and evaluation suites, each at the right layer.
6. **Gate** releases on evaluation results with statistical thresholds, and **roll out** prompt and model changes behind flags with canaries and kill switches.
7. **Trace** a request from the browser to model and tool spans, and **join** user feedback to traces.
8. **Operate** an AI feature: budgets, alerts, runbooks, incident response and post-incident reviews.

## Chapters and lessons

### Chapter 1 · Anatomy of an AI feature (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 The vertical slice | UI → API → context assembly → retrieval → model → tools → post-processing → UI; where state, cost and failure live | Draw the slice for a "summarise this ticket" feature with latency and cost per hop |
| 1.2 The spec | Problem, users, success and guardrail metrics, eval plan, autonomy level, fallback, rollout (AIE404 deepens) | Write a one-page spec before any code |
| 1.3 The last 20% | Why demos mislead: long-tail inputs, latency at peak, cost at scale, trust; LinkedIn's lessons (2024) | List the ten inputs your demo never tried |
| 1.4 Build or buy per layer | Hosted model APIs vs open weights; managed vector stores vs Postgres; framework vs plain code | Decision record for each layer of your slice |

**Check your understanding:** Which hop in your slice dominates cost, and which dominates latency? Why must the fallback be designed before the happy path? What would make you abandon the AI approach for this feature?

### Chapter 2 · Contracts across the stack (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 One schema, many consumers | JSON Schema or Zod as the source of truth for API payloads, tool inputs and structured outputs; code generation for TypeScript and Python | Generate client, server and tool types from one schema |
| 2.2 Message models | Messages made of parts (text, tool call, tool result, citation, file); IDs and versions; why UI and storage must agree | Design and version a message-part schema |
| 2.3 Structured outputs | Strict JSON Schema modes in provider APIs; refusals and truncation as valid outcomes; validating partial output while streaming | Handle valid, refused and truncated outputs in one parser |
| 2.4 Contract drift | Breaking vs non-breaking changes; consumer-driven contract tests; schema diff in CI | Make a CI job fail on a breaking tool-schema change |

**Check your understanding:** Why is a model's structured output a contract you do not fully control? What breaks if the UI and the database disagree on message-part types? Which schema changes can ship without a coordinated release?

### Chapter 3 · The streaming slice (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Server-Sent Events end to end | Provider stream → backend → browser; event IDs; flushing through proxies (FE403 and BE403 go deeper) | Stream tokens through nginx with buffering off; measure time to first token |
| 3.2 Cancellation | `AbortController` in the browser → closed connection → cancelled upstream request → stop paying | Prove with logs that a cancel stops upstream billing within 1 s |
| 3.3 Persistence | Saving partial and final output; resuming after reload; idempotent submits | Reload mid-stream and resume without a duplicate model call |
| 3.4 Libraries | The AI SDK's chat and streaming primitives; what they decide for you; when plain `fetch` is clearer | Rebuild one screen with and without the library; compare code and behaviour |

**Check your understanding:** Where can a stream be buffered without your code knowing? Why must cancellation be tested, not assumed? What does a double-click on "Send" cost you without idempotency?

### Chapter 4 · Context, retrieval and permissions (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Ingestion for a feature | Loading, chunking, metadata (tenant, owner, ACL, freshness), re-embedding only what changed | Ingest 10,000 documents with ACL metadata |
| 4.2 Permission-aware retrieval | Filtering by the caller's permissions before ranking; tenant isolation (OWASP LLM08:2025) | Test that 100 cross-tenant queries return zero foreign chunks |
| 4.3 Citations end to end | Carrying chunk IDs from retrieval through generation to clickable UI citations; verifying quotes | Show a citation that fails verification and how the UI handles it |
| 4.4 Acting on behalf of the user | Tool calls with the user's scoped token, not a service super-user; approval for consequential actions | Implement an on-behalf-of tool call with scope checks |
| 4.5 Personal data in context | Redacting before the model call, what goes into logs, retention (DPDP Act duties) | Add redaction and prove raw phone numbers never reach logs |

**Check your understanding:** Why must filtering happen before ranking? A citation points to a document the user cannot open: what went wrong? Why is a service account with full access dangerous behind an LLM?

### Chapter 5 · Abuse, injection and safe rendering (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Prompt injection as untrusted input | Instructions inside documents, web pages and tool results (OWASP LLM01:2025); privilege separation | Run a provided injection set against your slice; record what gets through |
| 5.2 Output handling | Model output as untrusted (LLM05:2025): sanitising Markdown and HTML, link and image policies | Zero XSS findings on a rendered-output test set |
| 5.3 Excessive agency | Least privilege per tool, confirmation for irreversible actions (LLM06:2025) | Classify every tool by consequence; add approvals |
| 5.4 Quotas and abuse | Per-user rate and token limits, abuse signals, cost-based denial of service (LLM10:2025) | Load-test a single abusive user; show other users unaffected |

**Check your understanding:** Why can no prompt fully stop prompt injection? Which tools in your slice could cause harm if called with attacker-chosen arguments? How does a quota show up in the UI without confusing honest users?

### Chapter 6 · Testing AI features (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 The AI test pyramid | Unit tests with fake models; recorded-response tests; contract tests; end-to-end browser tests; evaluation suites; what each catches | Map 20 past bugs (provided) to the layer that should catch them |
| 6.2 Recording and replaying model calls | VCR-style fixtures (vcrpy, Mock Service Worker); refreshing recordings; secrets in cassettes | Record 30 calls; replay deterministically in CI |
| 6.3 End-to-end tests | Playwright against a deterministic model stub; streaming assertions; accessibility checks with axe-core | E2E test that sends, streams, cancels and retries |
| 6.4 Property-based tests for parsers | Generating malformed partial JSON and Markdown; shrinking failures | Find a crash in your stream parser with Hypothesis or fast-check |

**Check your understanding:** Which bugs can only an evaluation suite catch? Why do recorded responses go stale, and how do you notice? What should never be asserted with exact string equality?

### Chapter 7 · Evaluations as release gates (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Feature-level eval sets | Golden cases from real usage, edge cases, adversarial cases; labelling guides ([AIE305](../../../03_majors/ai_engineering/year_3/AIE305_evaluating_llm_systems/README.md) for method) | Build a 150-case set for your feature |
| 7.2 Graders | Code checks first; calibrated LLM judges second; human review for the rest | Calibrate one judge against 50 human labels; report agreement |
| 7.3 Gating with statistics | Paired comparisons, confidence intervals, minimum detectable change; blocking vs warning checks | CI gate that blocks a planted 3-point regression and passes noise |
| 7.4 Prompts and models as artefacts | Versioned prompts and configs; changelogs; provider model deprecations and pinned versions | Upgrade a model version through the gate with a written diff |

**Check your understanding:** Why should the eval gate compare paired results rather than two averages? A judge agrees with humans 90% of the time; is that good enough to gate on? What is the release process for a one-word prompt change?

### Chapter 8 · Rollouts, flags and fallbacks (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Feature flags | Flag types, targeting, lifecycle and cleanup; OpenFeature (a CNCF incubating project since Nov 2023) as a vendor-neutral API | Put the model choice and the prompt version behind flags |
| 8.2 Shadow and canary | Shadow traffic for new models (log, do not show); canaries by percentage and cohort; automatic rollback on guardrail breach | Canary a new model to 5%; trigger rollback on a latency guardrail |
| 8.3 Fallbacks and degradation | Secondary model, cached answer, non-AI path, "AI unavailable" UI | Kill the primary provider in staging; measure user-visible impact |
| 8.4 Kill switches | Who can pull them, how fast, what users see; testing them regularly | Kill-switch drill under 60 s |

**Check your understanding:** Why does shadow traffic need its own privacy review? What is the difference between a flag and a kill switch in practice? Which metrics should trigger an automatic rollback?

### Chapter 9 · Observability from browser to model (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Trace context | W3C Trace Context (`traceparent`) from the browser through APIs, queues and model calls; OpenTelemetry browser and server SDKs | One trace from click to tool call in a local collector |
| 9.2 GenAI spans | OpenTelemetry GenAI semantic conventions (status: Development, maintained in a separate repository since 2026): operation names, provider, token usage | Instrument model and tool spans; check attribute names against the spec |
| 9.3 Feedback joined to traces | Thumbs, edits, copies and retries carrying the trace ID; tools such as Langfuse | Query: "show the traces behind yesterday's thumbs-down" |
| 9.4 Dashboards that answer questions | Time to first token, error and refusal rates, cost per request, quality samples; per tenant and per release | Build a dashboard and use it to explain one anomaly |

**Check your understanding:** Why must the trace ID be created in the browser, not the backend? What should you never store in span attributes? Which single chart would have caught your last bug?

### Chapter 10 · Cost and latency budgets (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Unit costs | Tokens per request, cost per successful task, cost per active user; per-feature attribution | Cost report by feature and tenant from traces |
| 10.2 Budgets and alerts | Daily budgets, anomaly alerts, per-tenant caps, graceful limits | Alert that fires on a simulated retry storm within 10 minutes |
| 10.3 Cheaper and faster | Prompt caching with stable prefixes, routing simple requests to smaller models, response caching with care (BE403 goes deeper) | Cut cost per task by at least 30% with no eval regression |
| 10.4 Perceived latency | Streaming, showing plans first, skeletons, optimistic UI (FE403 goes deeper) | A/B two loading designs with 5 users each; record perceived wait |

**Check your understanding:** Why is cost per request a misleading metric? Which caching is safe for a personalised answer? What latency matters more than time to first token for your feature?

### Chapter 11 · Operating AI features (weeks 11–12)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Incident classes | Provider outage, quality regression, injection exploit, cost spike, data leak, model deprecation | Write a runbook for each class |
| 11.2 On-call for AI | Alerts on quality samples, refusal spikes and cost, not only errors; severity definitions | Set up alerting with three severities and owners |
| 11.3 Post-incident reviews | Blameless reviews; turning failures into eval cases and tests | Review a simulated quality regression and add 10 eval cases |
| 11.4 Retention and deletion | Keeping traces long enough to debug and short enough to respect purpose; deleting a user's traces | Implement trace retention and per-user deletion |
| 11.5 Liability and disclosure | Telling users they are using AI; responsibility for answers (Moffatt v. Air Canada, 2024, in AIE404); EU AI Act Article 50 duties | Add disclosures and a correction path to your UI |

**Check your understanding:** Why do quality incidents rarely page anyone, and how do you fix that? What makes a post-incident action item real? Which traces would you keep for 90 days and why?

### Chapter 12 · Launch (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Launch readiness | Checklist: evals and thresholds, guardrails, observability, runbooks, kill switch, disclosure, accessibility, privacy review | Run the checklist on P3 with a reviewer |
| 12.2 Documentation | Design doc, API reference, runbook, user help | Write the docs a new teammate needs |
| 12.3 Demo and defence | Showing a feature honestly: failure cases, cost, limits | 10-minute demo with live failure handling |
| 12.4 Retrospective | What the spec predicted vs what happened | Retrospective feeding OV08B |

**Check your understanding:** Which checklist item would you most likely skip under deadline, and what would it cost? What does an honest demo show that a sales demo hides? What will OV08B need from your instrumentation?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Spec and slice map | Feature spec |
| 2 | 2 | Lab 2 · Shared schemas and drift checks | — |
| 3 | 3 | Lab 3 · Streaming with cancellation | **P1 due** |
| 4 | 4 | Lab 4 · Permission-aware retrieval | Isolation test report |
| 5 | 5 | Lab 5 · Injection and rendering tests (no AI for the fixes) | Findings and fixes |
| 6 | 6 | Lab 6 · Recorded responses and E2E tests | Test suite |
| 7 | 7 | Lab 7 · Eval gate in CI | Mid-term (AI off) |
| 8 | 8 | Lab 8 · Flags, canary and kill switch | **P2 due** |
| 9 | 9 | Lab 9 · Browser-to-model tracing | Dashboard |
| 10 | 10 | Lab 10 · Cost reduction without regression | Cost report |
| 11 | 11 | Incident drill | Runbooks |
| 12 | 11 | Post-incident review | Review document |
| 13 | 12 | Launch readiness review | — |
| 14 | 12 | Demo day | **P3 due** |
| 15 | Review | Oral defence of P3 | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** generating UI components, API routes and boilerplate with a coding agent (Claude Code, Cursor, GitHub Copilot, OpenAI Codex); drafting eval cases that you then label; writing test scaffolding; summarising traces during debugging. Expect to use these tools daily: the course measures what you ship, not what you type.
- **Do without AI (drills):** the Lab 5 security fixes; the contract design in Lab 2; the mid-term and final; the incident-drill decisions. You must be able to explain every line you ship and find a bug in an AI-written change.
- **Verify AI output by:** running the contract tests and the eval gate on every AI-written change; reading diffs for silent behaviour changes (retries, timeouts, logging of personal data); checking that generated tests fail when the code is broken (mutation testing on a sample); asking for and checking the trace of a generated feature in staging.
- **Where AI still fails here (collect your own evidence):** keep a log of AI-generated changes that passed review but broke a join: schema drift between layers, cancellations that did not propagate, personal data written to logs, tests that asserted mocks rather than behaviour. The log is part of P3.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1–P3 | 40% |
| Incident drill and post-incident review | 5% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) + oral defence of P3 | 20% |

**Mastery gate.** You pass when you can: (1) given an unfamiliar AI feature's repository, add a new tool end to end (schema, backend, permission check, UI rendering, tests, eval cases) in four hours with AI tools allowed, with all gates green; (2) with AI tools off, find a planted cross-layer bug (contract drift, missing cancellation or a tenant leak) from traces and code in 30 minutes; (3) explain your release gate's statistics and defend a ship or no-ship decision on a provided eval report.

## Industry reality

Where this work is visible publicly: GitHub's offline evaluation programme for Copilot model changes (Jan 2025); LinkedIn's account of the long tail of a generative AI product (Apr 2024); Uber's GenAI Gateway as a shared layer for many product teams (Jul 2024, see [BE403](../../../03_majors/backend_engineering/year_4/BE403_backends_for_ai_serving_llm_features_vector/README.md)); OWASP's Top 10 for LLM Applications 2025 as the shared vocabulary for AI feature risks. In India, product companies, global capability centres and AI start-ups hire for this full-stack profile under "AI engineer", "product engineer" and "founding engineer" titles (**analysis**; no public statistics separate these titles).

**Interview questions from this course**

1. *Design a "chat with your documents" feature for a multi-tenant SaaS.* Strong answer: ingestion with ACL metadata, filter-before-rank retrieval, streaming with cancellation, citations carried end to end, quotas per tenant, eval plan, tracing, and a fallback.
2. *A model upgrade improved offline evals but users complain. How do you investigate?* Strong answer: joins feedback to traces; checks eval-set representativeness against production inputs; compares slices; uses shadow or canary data; adds failing cases to the eval set; considers latency or format changes the eval missed.
3. *How do you test a feature whose output changes every time?* Strong answer: layered tests: fakes and recorded responses for logic, contract tests for structure, property tests for parsers, eval suites with statistical gates for quality, E2E with stubs for flows.
4. *Our AI feature's cost tripled overnight. What do you check?* Strong answer: cost by tenant and feature from traces; retry loops and missing cancellation; prompt growth (context accumulation); cache hit rate; model routing change; abuse; then budget caps and alerts.
5. *How would you roll out a new model safely?* Strong answer: offline eval gate, shadow traffic, canary by cohort with guardrails (quality samples, latency, cost, refusals), automatic rollback, kill switch, communication plan, pinned versions and a deprecation calendar.

## Resources (free first)

- **Engineering accounts:** GitHub, How we evaluate models for Copilot — https://github.blog/ai-and-ml/generative-ai/how-we-evaluate-models-for-github-copilot/ ; LinkedIn, Musings on building a generative AI product — https://www.linkedin.com/blog/engineering/generative-ai/musings-on-building-a-generative-ai-product
- **Standards and specs:** W3C Trace Context — https://www.w3.org/TR/trace-context/ ; OpenTelemetry GenAI semantic conventions — https://github.com/open-telemetry/semantic-conventions-genai ; JSON Schema — https://json-schema.org/ ; OWASP Top 10 for LLM Applications 2025 — https://genai.owasp.org/llm-top-10/ ; WCAG 2.2 — https://www.w3.org/TR/WCAG22/
- **Tools:** AI SDK — https://ai-sdk.dev/docs/introduction ; Zod — https://zod.dev/ ; Playwright — https://playwright.dev/ ; Mock Service Worker — https://mswjs.io/ ; vcrpy — https://vcrpy.readthedocs.io/ ; axe-core — https://github.com/dequelabs/axe-core ; promptfoo — https://www.promptfoo.dev/docs/intro/ ; Inspect — https://inspect.aisi.org.uk/ ; OpenFeature — https://openfeature.dev/ ; Langfuse — https://langfuse.com/docs ; OpenTelemetry browser SDK — https://opentelemetry.io/docs/languages/js/getting-started/browser/
- **Paid, optional:** none required.

## Sources

All checked October 2026.

- LinkedIn Engineering, "Musings on building a Generative AI product" (Apr 2024) — https://www.linkedin.com/blog/engineering/generative-ai/musings-on-building-a-generative-ai-product
- GitHub Blog, "How we evaluate AI models and LLMs for GitHub Copilot" (17 Jan 2025): more than 4,000 offline tests; about 100 containerised repositories — https://github.blog/ai-and-ml/generative-ai/how-we-evaluate-models-for-github-copilot/
- CNCF, OpenFeature project page (accepted 17 Jun 2022; incubating since 21 Nov 2023) — https://www.cncf.io/projects/openfeature/
- OpenTelemetry, GenAI semantic conventions moved to a dedicated repository; status Development — https://opentelemetry.io/docs/specs/semconv/gen-ai/ and https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-spans.md
- OWASP Top 10 for LLM Applications 2025 — https://genai.owasp.org/llm-top-10/
- Uber GenAI Gateway, Moffatt v. Air Canada and EU AI Act Article 50: see the sources of [BE403](../../../03_majors/backend_engineering/year_4/BE403_backends_for_ai_serving_llm_features_vector/README.md) and [AIE404](../../../03_majors/ai_engineering/year_4/AIE404_ai_product_engineering_and_ux/README.md)

_Last reviewed: 2026-10_
