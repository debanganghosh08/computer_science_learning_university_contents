# BE301 · API Design: REST, gRPC and GraphQL

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 5 | 4 (≈ 120 hours) | L2 → L3 | [CS211](../../../../02_year_2_core_computer_science/semester_4/CS211_database_systems_internals/README.md), [CS212](../../../../02_year_2_core_computer_science/semester_4/CS212_distributed_systems_i/README.md) | [BE401](../../year_4/BE401_payments_grade_systems_transactions_idempotency/README.md), [BE404](../../year_4/BE404_microservices_service_mesh_and_platform_apis/README.md), [OV02](../../../../04_overlaps/OV02_cloud_native_backend/README.md) |

Part of the [Backend Engineering major](../../README.md). Uses the HTTP knowledge from [FND114](../../../../01_year_1_foundations/semester_2/FND114_web_foundations_http_html_css_and_javascript/README.md) and [CS204](../../../../02_year_2_core_computer_science/semester_3/CS204_computer_networks/README.md). Taught alongside [BE302](../BE302_backend_frameworks_and_service_internals/README.md), where you implement what you design here.

## Why this course matters now

An API is a promise that other people's code depends on. Once published, you can only change it slowly. Stripe has kept old integrations working for years through dated API versions. It now ships a non-breaking version every month and breaking "major" versions twice a year. Razorpay made idempotency keys mandatory on payouts from 15 March 2025, so that a retried request cannot pay twice. The consumers are changing too. In Postman's 2025 survey of over 5,700 respondents, 24% already design APIs with AI agents in mind. The top security worry, named by 51%, was unauthorized or excessive API calls from agents. The Model Context Protocol (MCP), now governed under the Linux Foundation, has become a common way to expose tools to agents. AI assistants generate OpenAPI files, handlers and SDKs in minutes. What they do not do reliably is choose resource boundaries, error semantics, idempotency rules and evolution policies that stay correct for years. That judgement is what this course builds.

## Learning outcomes

By the end you can:

1. **Design** a resource-oriented HTTP API from a domain model, with correct methods, status codes, caching headers and conditional requests (RFC 9110).
2. **Specify** it design-first in OpenAPI 3.2, lint it against a style guide, and **detect** breaking changes automatically in CI.
3. **Implement** RFC 9457 problem details, cursor pagination, filtering and partial updates consistently across an API.
4. **Build** idempotency-key handling that is correct under concurrent retries and server crashes, and **explain** why "exactly once" means exactly-once effects.
5. **Evolve** an API through versioning, deprecation (`Deprecation` and `Sunset` headers) and consumer-driven contracts without breaking existing clients.
6. **Design** gRPC services with Protocol Buffers that stay wire-compatible, with deadlines, status codes and streaming used correctly.
7. **Build** a GraphQL API with DataLoader batching, cost limits and persisted queries, and **argue** when GraphQL is the wrong choice.
8. **Deliver** signed, retried, replay-protected webhooks, and **verify** incoming ones safely.
9. **Apply** rate limits, quotas and the OWASP API Security Top 10 (2023) as design-time checks.
10. **Design** tool interfaces that AI agents can use safely (MCP tools, strict JSON schemas, dry runs and confirmations), and **evaluate** them with an agent in the loop.

## Chapters and lessons

### Chapter 1 · APIs as contracts (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Who consumes an API | Mobile apps, browsers, partners, internal services and agents; each one's constraints (latency, upgrade speed, trust) | List the consumers of a public API you use (UPI app, GitHub) and their constraints |
| 1.2 Hyrum's law and compatibility | Every observable behaviour becomes a dependency; what "breaking" really means | Find three undocumented behaviours of a real API that clients probably rely on |
| 1.3 Design-first with OpenAPI | OpenAPI 3.2 structure, schemas, examples, `$ref` hygiene, generated docs and mocks | Write an OpenAPI document before any code; serve a mock with Prism |
| 1.4 Style guides | Google AIPs, Microsoft REST API Guidelines, Zalando guidelines; why consistency beats cleverness | Encode five style rules as Spectral lint rules and run them in CI |

**Check your understanding:** (1) Why is changing a field from always-present to sometimes-absent a breaking change even if the schema says "optional"? (2) What does design-first buy you that code-first does not, and what does it cost? (3) Which consumer of your API upgrades slowest, and how does that limit your evolution policy?

### Chapter 2 · HTTP semantics for API designers (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Methods | Safe and idempotent methods (RFC 9110), why `POST` is neither, `PUT` vs `PATCH` | Classify 20 operations from real APIs by method and defend each choice |
| 2.2 Status codes | 2xx/3xx/4xx/5xx families, `201` with `Location`, `202` for async work, `409` vs `412` vs `422`, `429` (RFC 6585) | Map 15 failure cases of an orders API to codes |
| 2.3 Caching and conditional requests | `Cache-Control`, `ETag`, `If-None-Match`, `If-Match` and `412` for optimistic concurrency | Add ETags to a resource; prove a lost update is prevented |
| 2.4 Headers and content negotiation | `Accept`, `Content-Type`, `Vary`, `Retry-After`, `Location`, request IDs | Audit a provided API for header mistakes |

**Check your understanding:** (1) Why is `PUT` idempotent but a `PATCH` that appends to a list not? (2) When do you return `202 Accepted`, and what must the response contain? (3) What does `If-Match` prevent that a database transaction alone cannot?

### Chapter 3 · Resource modeling (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Resources and collections | Nouns, identifiers, hierarchy vs references, resource names (AIP-122) | Model a food-delivery API: orders, items, riders, payments |
| 3.2 Actions that are not CRUD | Custom methods (AIP-136, `POST /orders/{id}:cancel`), state machines exposed as transitions | Design cancel, refund and reassign without inventing verbs in paths |
| 3.3 Long-running operations | Operation resources (AIP-151), polling vs callbacks, progress and cancellation | Design a report-export endpoint that takes 10 minutes |
| 3.4 Partial updates and bulk | JSON Merge Patch (RFC 7396) vs JSON Patch (RFC 6902), field masks, batch endpoints and partial failure | Implement field-mask updates; return per-item results for a batch |

**Check your understanding:** (1) Why is `/cancelOrder` a smell, and what replaces it? (2) How should a batch endpoint report 3 failures out of 100? (3) When do you expose a state machine's transitions instead of letting clients set `status`?

### Chapter 4 · Errors, pagination and filtering (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Problem details | RFC 9457 (`type`, `title`, `status`, `detail`, `instance`, extensions); AIP-193 `ErrorInfo` reasons | Define an error catalogue with machine-readable `type` URIs |
| 4.2 Errors that help the caller | Actionable messages, retryable vs not, field-level validation errors, never leaking internals | Rewrite 10 bad error responses so a client (or agent) knows what to do next |
| 4.3 Pagination | Offset vs cursor (AIP-158 `page_token`), stable ordering, page size limits, total counts and their cost | Implement opaque, signed cursors over a 10M-row table |
| 4.4 Filtering and sorting | Filter languages (AIP-160 style vs ad hoc), allowlisted fields, index-aware filters | Design filters that cannot trigger a full table scan |

**Check your understanding:** (1) Why should a cursor be opaque to clients? (2) Which error responses should carry `Retry-After`? (3) Why can "return the total count" become the slowest part of a list endpoint?

### Chapter 5 · Idempotency and safe retries (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Why retries happen | Timeouts with unknown outcomes; client, proxy and SDK retries; the network can fail after the server commits | Draw the three failure points of a payment request |
| 5.2 Idempotency keys | Stripe (keys up to 255 characters, prunable after 24 h, replays the first response) and Razorpay (`X-Payout-Idempotency`, mandatory since March 2025); the IETF `Idempotency-Key` draft expired without becoming an RFC | Compare two providers' semantics in a table |
| 5.3 Implementing them correctly | Key + request fingerprint + stored response, in-flight locking, `409` for concurrent duplicates, `422` for key reuse with a different body, expiry | Lab 4: build it and pass a concurrent-retry test suite |
| 5.4 Exactly-once effects | At-least-once delivery + idempotent processing; natural idempotency (`PUT`, conditional writes) vs keys | Make three non-idempotent endpoints safe without keys where possible |

**Check your understanding:** (1) A client times out and retries while the first request is still running. What should the second request return? (2) Why must the server compare the request body, not just the key? (3) What should happen if the first attempt failed with a `500`?

### Chapter 6 · Versioning and evolution (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Compatible and breaking changes | Additive change rules, enum expansion, tolerant readers, default values | Classify 20 proposed changes as safe or breaking |
| 6.2 Versioning strategies | Path, header, media-type and date-based versions; Stripe's monthly versions and twice-yearly majors; version pinning per account | Design a versioning policy for a payments API |
| 6.3 Deprecation | `Deprecation` (RFC 9745) and `Sunset` (RFC 8594) headers, usage telemetry per version, migration guides | Deprecate a field and measure which clients still use it |
| 6.4 Automated breaking-change checks | oasdiff for OpenAPI, `buf breaking` for protobuf, consumer-driven contracts (preview of BE404) | Fail a CI build on a breaking OpenAPI change |

**Check your understanding:** (1) Why is adding a value to a response enum risky? (2) What does date-based versioning make easy, and what does it make expensive inside the server? (3) How do you know when it is safe to remove a deprecated endpoint?

### Chapter 7 · gRPC and Protocol Buffers (weeks 7–8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Protobuf schemas | Field numbers, wire types, `reserved`, `optional`, editions (2023 baseline, 2024 latest) and features | Evolve a message three times without breaking old readers; prove it with tests |
| 7.2 Service design | Unary, server-streaming, client-streaming and bidirectional RPCs; request/response wrappers; AIP-style resource methods | Design a rider-location streaming service |
| 7.3 Deadlines and status codes | No default deadline, `DEADLINE_EXCEEDED`, propagation across hops; the 17 status codes; the rich error model | Propagate a 300 ms deadline across three services and observe cancellation |
| 7.4 Operating gRPC | HTTP/2 long-lived connections and load balancing, keepalives, retries and hedging policies, interceptors | Show uneven load behind an L4 balancer; fix with client-side or L7 balancing |
| 7.5 gRPC for browsers and beyond | gRPC-Web, ConnectRPC (CNCF Sandbox), JSON transcoding | Serve one service as gRPC and as JSON over HTTP from one definition |

**Check your understanding:** (1) Why must you never reuse a protobuf field number? (2) What goes wrong when a gRPC client sets no deadline? (3) Why does gRPC load balancing behave differently from REST behind the same L4 load balancer?

### Chapter 8 · GraphQL (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Schema and resolvers | Types, queries, mutations, subscriptions; the September 2025 spec edition; GraphQL-over-HTTP (still a draft) | Build a schema for a restaurant catalogue |
| 8.2 The N+1 problem | DataLoader batching and caching per request | Measure queries per request before and after DataLoader |
| 8.3 Protecting the server | Depth and cost limits, persisted queries, pagination with connections, disabling introspection in production | Add cost analysis that rejects a deliberately expensive query |
| 8.4 When to use it | Backend-for-frontend aggregation, federation, caching difficulties, error semantics (`200` with `errors`) | Write a decision record: REST, gRPC or GraphQL for three stated clients |

**Check your understanding:** (1) Why is HTTP caching harder for GraphQL than for REST? (2) How can one GraphQL query cause thousands of database queries? (3) When is GraphQL a poor fit for public partner APIs?

### Chapter 9 · Webhooks and event APIs (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Delivery semantics | At-least-once delivery, retries with backoff, ordering not guaranteed, consumer deduplication by event ID | Write the consumer contract a merchant must follow |
| 9.2 Signatures and replay protection | HMAC-SHA256 over the raw body (GitHub `X-Hub-Signature-256`, Razorpay `X-Razorpay-Signature`), constant-time comparison, timestamps; Standard Webhooks headers | Implement signing and verification; show why parsing the body before verifying breaks it |
| 9.3 Sender design | Per-endpoint queues, circuit breaking unhealthy endpoints, retry schedules, dead-lettering, replay tools | Lab 7: build a sender that survives a consumer outage of 1 hour |
| 9.4 Event payload design | Thin vs fat events, event versioning, AsyncAPI descriptions | Design `payment.captured` v1 and v2 so both can coexist |

**Check your understanding:** (1) Why must a webhook consumer be idempotent even if the sender "never" duplicates? (2) Why compare signatures in constant time? (3) When should an event carry the full resource, and when only an ID?

### Chapter 10 · Rate limits, quotas and API security (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Rate-limiting algorithms | Fixed and sliding windows, token bucket, GCRA; per key, per tenant, per route; distributed counters | Implement token bucket and GCRA; compare burst behaviour |
| 10.2 Telling clients the rules | `429` + `Retry-After`; the IETF RateLimit header fields (an active draft, not yet an RFC); quotas and plans | Return correct headers and verify a client backs off |
| 10.3 OWASP API Security Top 10 (2023) | Broken object-level and property-level authorization, broken authentication, unrestricted resource consumption, unsafe consumption of APIs, and the rest, as design reviews (defensive only) | Review a provided API design against all ten and file findings |
| 10.4 Design-time defences | Object-level checks in every handler, allowlisted response fields, request size limits, server-side request forgery guards for user-supplied URLs (such as webhook endpoints) | Fix three planted authorization bugs in a lab API on your own machine |

**Check your understanding:** (1) Why is broken object-level authorization the top API risk, and why can't a gateway catch it? (2) What should a rate limiter key on for unauthenticated endpoints? (3) Why is registering a webhook URL a security-relevant operation?

### Chapter 11 · APIs for AI agents (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 How agents call APIs | Function calling, strict JSON Schema (`additionalProperties: false`, all fields required), structured outputs | Turn three REST endpoints into strict tool definitions |
| 11.2 MCP | The 2026-07-28 protocol version, Streamable HTTP, tools with `inputSchema`, `outputSchema` and `structuredContent`, errors with `isError`; Origin validation | Expose your orders API as an MCP server |
| 11.3 Tool-friendly design | Small, task-shaped tools; enums over free text; descriptions as documentation; idempotent actions; dry-run and confirmation for side effects; errors that say what to do next | Redesign a 40-endpoint API as 8 agent tools; justify the cut |
| 11.4 Safety and limits for agent traffic | Scoped credentials per agent, per-agent rate limits and budgets, human approval for irreversible actions, audit logs | Add an approval step to a refund tool and log every call |
| 11.5 Evaluating an API with an agent | Task suites, success rate, wrong-call rate, retries; Arazzo for describing multi-step workflows | Measure an agent's success on 30 tasks before and after your redesign |

**Check your understanding:** (1) Why do agents do better with fewer, task-shaped tools than with a full CRUD surface? (2) What should an error message tell an agent that a human-oriented message might not? (3) Which actions should never be callable by an agent without a confirmation step?

### Chapter 12 · Documentation, SDKs and governance (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Documentation that works | Reference vs guides vs recipes, runnable examples, changelogs | Write a "first payment in 5 minutes" guide and test it on a classmate |
| 12.2 SDKs | Generated vs hand-written SDKs, retries and idempotency built into SDKs, pagination helpers | Generate an SDK from OpenAPI and fix three ergonomic problems |
| 12.3 API review and governance | Design reviews, lint gates, breaking-change gates, API inventory (OWASP API9) | Run a design review of a classmate's P3 with a checklist |
| 12.4 Developer experience metrics | Time to first successful call, error rates by client and version, sandbox environments, status pages | Instrument time-to-first-successful-call for your P3 quick-start and improve it |

**Check your understanding:** (1) Why should SDKs generate idempotency keys automatically? (2) What belongs in an API changelog entry? (3) How do you find APIs nobody remembers exposing?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1: design-first spec | OpenAPI document, mock server, lint rules |
| 2 | 2 | Lab 2: HTTP semantics | Status-code map; ETag lost-update test |
| 3 | 3 | Resource model | API design review notes |
| 4 | 4 | Lab 3: errors and cursors | Problem-details catalogue; cursor pagination; P1 due |
| 5 | 5 | Lab 4: idempotency (no AI) | Passing concurrent-retry suite |
| 6 | 6 | Lab 5: breaking-change CI | Pipeline that fails on breaking changes |
| 7 | 7 | Lab 6: gRPC (part 1) | Protobuf evolution tests |
| 8 | 7 | Lab 6 (part 2) | Deadline propagation and load-balancing demo; P2 starts |
| 9 | 8 | GraphQL | DataLoader and cost-limit measurements |
| 10 | 9 | Lab 7: webhooks | Sender and verifier; outage replay |
| 11 | 10 | Lab 8: rate limits and OWASP review | Limiter tests; findings report; P2 due |
| 12 | 11 | Lab 9: agent tools | MCP server and agent task-suite results; P3 design review |
| 13 | 12 | SDK and docs | Generated SDK, quick-start guide |
| 14 | — | P3 integration | P3 demo and write-up |
| 15 | Review and exam | — | Written exam and live design review |

## Working with AI in this course

- **Use AI for:** first drafts of OpenAPI and protobuf files from your resource model; generating examples and mock data; writing Spectral rules; producing client SDK stubs; drafting docs; acting as the agent in Chapter 11's task suite (Claude, GPT and Gemini models through their tool-calling APIs).
- **Do without AI (drills):** the resource model and status-code map for a new domain; the idempotency implementation (Lab 4); classifying changes as breaking or safe; the OWASP API design review; the live design review in the exam.
- **Verify AI output by:** linting every generated spec and running oasdiff or `buf breaking` against the previous version; running generated handlers against contract tests built from the spec; testing idempotency with concurrent duplicate requests and a crash in the middle; checking webhook verification against a captured raw body; measuring agent success rates rather than reading tool descriptions and guessing.
- **Where AI still fails here (show it yourself):** ask an assistant for an "idempotent payment endpoint" and test it with two identical requests sent 5 ms apart: check whether both pass the "key not found" check. Ask it to verify a webhook signature in a web framework and check whether it signs the parsed and re-serialized JSON instead of the raw bytes. Ask it to "add a field" to a protobuf message and check whether it renumbers existing fields. Ask it to generate an MCP tool from a REST endpoint and count the free-text parameters an agent could fill wrongly. Record each failure and the test that caught it.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs 1–9 | 30% |
| Projects P1 / P2 / P3 | 5% / 12% / 18% |
| Written exam (HTTP semantics, idempotency, evolution, protocol trade-offs) | 20% |
| Live design review (a new domain, 90 minutes, no AI) | 15% |

**Mastery gate:** you pass when you can, without AI help, (a) design a resource model, error catalogue, pagination and idempotency policy for an unfamiliar domain in 90 minutes and defend it in review; (b) find at least 4 of 5 planted problems in a provided API (a breaking change, an object-level authorization gap, a non-idempotent retry path, a webhook verification flaw, an unbounded list endpoint); and (c) show your P3 API passing its contract, idempotency and breaking-change suites in CI.

## Industry reality

- **Stripe** pins each account to an API version. Since `2024-09-30.acacia` it releases a new version every month without breaking changes, and twice a year a major release with breaking changes; the current version in October 2026 is `2026-09-30.endive`. Its idempotency keys have been documented since its 2017 engineering post.
- **Razorpay** requires `X-Payout-Idempotency` on payouts (since 15 March 2025) and signs webhooks with HMAC-SHA256 over the raw request body.
- **Google** publishes its API design rules as AIPs (resource names, custom methods, long-running operations, pagination, errors), and **Microsoft** and **Zalando** publish theirs openly.
- **Standards moved in 2025–2026:** OpenAPI 3.2.0 (September 2025) and 3.2.1 (September 2026), Arazzo 1.1.0 (May 2026), the GraphQL September 2025 edition, RFC 9745 for the `Deprecation` header, and MCP version 2026-07-28. The IETF `Idempotency-Key` header draft expired without becoming an RFC, so providers still differ in details.
- **The OWASP API Security Top 10** is still the 2023 edition in October 2026. Its first item, broken object-level authorization, is a design flaw that code generation reproduces easily.

Interview questions from this course:

1. **"Design the API for a food-delivery order lifecycle."** A strong answer covers resources and identifiers, state transitions as custom methods, status codes, idempotency for order creation, cursor pagination for history, webhooks or streaming for status updates, and versioning.
2. **"How do you implement idempotency keys?"** Cover the storage schema (key, fingerprint, status, response), atomic insert to claim the key, handling concurrent duplicates, replaying stored responses, expiry, and what happens if the server crashes mid-request.
3. **"REST, gRPC or GraphQL for this system?"** Cover consumers (browser, mobile, internal), streaming needs, schema evolution tooling, caching, load balancing with HTTP/2, and the team's operational experience. A strong answer allows mixing them.
4. **"How would you make breaking changes to a public API?"** Cover the compatibility rules, versioning strategy, deprecation headers and telemetry, migration guides, contract tests, and the long tail of clients that never upgrade.
5. **"How would you expose your product to AI agents?"** Cover task-shaped tools vs raw CRUD, strict schemas, MCP, scoped credentials, per-agent rate limits and budgets, confirmations for irreversible actions, audit logs, and measuring agent task success.

## Resources (free first)

- **Standards:** [RFC 9110 HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110); [RFC 9457 Problem Details](https://www.rfc-editor.org/rfc/rfc9457); [RFC 9745 Deprecation header](https://www.rfc-editor.org/rfc/rfc9745); [RFC 8594 Sunset header](https://www.rfc-editor.org/rfc/rfc8594); [RFC 7396 JSON Merge Patch](https://www.rfc-editor.org/rfc/rfc7396); [OpenAPI Specification](https://spec.openapis.org/oas/latest.html); [Arazzo](https://spec.openapis.org/arazzo/latest.html); [GraphQL spec](https://spec.graphql.org/); [AsyncAPI](https://www.asyncapi.com/docs); [Standard Webhooks](https://www.standardwebhooks.com/).
- **Style guides:** [Google AIPs](https://google.aip.dev/) (especially [158](https://google.aip.dev/158), [136](https://google.aip.dev/136), [151](https://google.aip.dev/151), [193](https://google.aip.dev/193)); [Microsoft REST API Guidelines](https://github.com/microsoft/api-guidelines); [Zalando RESTful API Guidelines](https://opensource.zalando.com/restful-api-guidelines/).
- **gRPC and GraphQL:** [gRPC deadlines](https://grpc.io/docs/guides/deadlines/) and [status codes](https://grpc.io/docs/guides/status-codes/); [Protobuf editions](https://protobuf.dev/editions/overview/); [ConnectRPC](https://connectrpc.com/); [GraphQL learn](https://graphql.org/learn/); [DataLoader](https://github.com/graphql/dataloader).
- **Idempotency and versioning in practice:** Stripe, [Designing robust and predictable APIs with idempotency](https://stripe.com/blog/idempotency) (2017) and [API versioning](https://stripe.com/blog/api-versioning) (2017); Stripe docs on [idempotent requests](https://docs.stripe.com/api/idempotent_requests) and [versioning](https://docs.stripe.com/api/versioning); Razorpay [payout idempotency](https://razorpay.com/docs/api/x/payout-idempotency/make-request/) and [webhook validation](https://razorpay.com/docs/webhooks/validate-test/).
- **Security:** [OWASP API Security Top 10 (2023)](https://owasp.org/API-Security/editions/2023/en/0x11-t10/); practice on deliberately vulnerable labs such as OWASP crAPI or PortSwigger Web Security Academy's API testing topics, on your own machine or the provider's platform only.
- **Agents:** [MCP specification and versioning](https://modelcontextprotocol.io/specification/versioning); OpenAI [function calling](https://developers.openai.com/api/docs/guides/function-calling) and [structured outputs](https://developers.openai.com/api/docs/guides/structured-outputs).
- **Tooling:** [Spectral](https://stoplight.io/open-source/spectral), [oasdiff](https://github.com/oasdiff/oasdiff), [buf breaking](https://buf.build/docs/breaking/).
- **Paid, worth it:** JJ Geewax, *API Design Patterns* (Manning, 2021), written by an author of Google's AIPs.

## Sources

All checked 12 Oct 2026.

- RFC 9457 (Jul 2023), RFC 9110 (Jun 2022), RFC 6585 (Apr 2012), RFC 9745 (2025): https://www.rfc-editor.org/
- IETF `Idempotency-Key` draft (-07, Oct 2025, expired): https://datatracker.ietf.org/doc/draft-ietf-httpapi-idempotency-key-header/ ; RateLimit header fields draft (-11, active): https://datatracker.ietf.org/doc/draft-ietf-httpapi-ratelimit-headers/
- OpenAPI 3.2.0 (19 Sep 2025) and 3.2.1 (10 Sep 2026): https://spec.openapis.org/oas/latest.html ; Arazzo 1.1.0 (17 May 2026): https://spec.openapis.org/arazzo/latest.html
- GraphQL September 2025 edition: https://spec.graphql.org/ ; GraphQL-over-HTTP draft: https://github.com/graphql/graphql-over-http
- Protobuf editions (2024 latest): https://protobuf.dev/editions/overview/ ; ConnectRPC CNCF Sandbox (Apr 2024): https://www.cncf.io/projects/connect-rpc/
- Stripe idempotency and versioning docs (current version `2026-09-30.endive`): https://docs.stripe.com/api/idempotent_requests ; https://docs.stripe.com/api/versioning
- Razorpay payout idempotency (mandatory since 15 Mar 2025) and webhook validation: https://razorpay.com/docs/api/x/payout-idempotency/make-request/ ; https://razorpay.com/docs/webhooks/validate-test/
- GitHub webhook validation: https://docs.github.com/en/webhooks/using-webhooks/validating-webhook-deliveries
- MCP versioning (2026-07-28 current): https://modelcontextprotocol.io/specification/versioning ; Anthropic, donation of MCP to the Agentic AI Foundation (9 Dec 2025): https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation
- Postman, 2025 State of the API (8 Oct 2025): https://www.postman.com/state-of-api/2025/
- OWASP API Security Top 10, 2023 edition: https://owasp.org/API-Security/editions/2023/en/0x11-t10/

_Last reviewed: 2026-10_
