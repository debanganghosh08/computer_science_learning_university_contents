# BE301 · Labs and projects

Every lab starts from a written design (an OpenAPI, protobuf or GraphQL schema) and ends with automated checks: a linter, contract tests, a breaking-change check, or a load or concurrency test. Implementations can use any BE302 stack. Lab 4 (idempotency) and the live design review are done without AI assistants, because they are where generated code most often looks right and is wrong.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Design-first spec | Write an OpenAPI 3.2 document for a small domain before any code; serve a mock; add 10 Spectral style rules | Spec, mock server, lint config with zero errors | 5 h |
| 2 · HTTP semantics | Map 15 failure cases to status codes; add `ETag` and `If-Match` to a resource | Status-code table with reasoning; a test proving a lost update is rejected with `412` | 4 h |
| 3 · Errors and cursors | RFC 9457 error catalogue; opaque, signed cursor pagination over 10M rows | Catalogue, implementation, latency plot by page depth (cursor vs offset) | 5 h |
| 4 · Idempotency keys (no AI) | Claim-store-replay idempotency with request fingerprints, in-flight locking and expiry | Code passing the provided suite: concurrent duplicates, key reuse with a different body, crash between commit and response | 8 h |
| 5 · Breaking-change CI | oasdiff and `buf breaking` in a pipeline; a deprecation with `Deprecation` and `Sunset` headers and usage telemetry | Pipeline run that fails on 5 planted breaking changes and passes on 5 safe ones | 4 h |
| 6 · gRPC | Protobuf evolution over three versions; deadline propagation across three services; load balancing with long-lived HTTP/2 connections | Compatibility tests, a trace showing cancellation, before/after load distribution | 8 h |
| 7 · Webhooks | Signed sender with per-endpoint retries and dead-lettering; verifier using the raw body, constant-time comparison and a timestamp window | Outage test: consumer down for 1 hour, zero events lost, duplicates handled | 6 h |
| 8 · Limits and OWASP review | Token bucket and GCRA limiters; review a provided API design against the OWASP API Security Top 10 (2023) | Limiter tests, findings report with severity and fixes for planted flaws (local lab only) | 5 h |
| 9 · Agent tools | Expose an API as MCP tools with strict schemas; run a 30-task agent suite before and after redesign | Tool definitions, task-success and wrong-call rates, and the changes that moved them | 6 h |

## Projects

### P1 · Design-first public-service API (L1, ~6 hours)

**Real-world inspiration:** India's [API Setu](https://apisetu.gov.in/), run under MeitY's National e-Governance Division, asks providers to publish government and partner APIs in standard formats such as OpenAPI. Your domain is a city bus-pass renewal service, which is an **illustrative scenario**.

**What to build:** a complete OpenAPI 3.2 specification, with no implementation. It covers citizens, passes, renewals, payments-pending states and document uploads. It includes:
- resource names and custom methods (`:renew`, `:cancel`);
- an RFC 9457 error catalogue;
- cursor pagination and field-level validation errors;
- examples for every operation;
- a mock server and a 10-rule Spectral style guide.

**Acceptance criteria:**
- Spectral reports zero errors with your 10 custom rules plus the OpenAPI recommended ruleset.
- Every operation has a request example, at least one success example and at least two error examples. A script checks this.
- A provided contract-test suite (30 cases) passes against your mock server.
- Two classmates complete a "renew a pass" task using only your docs and mock, in under 15 minutes each.
- A one-page design note explains three decisions you rejected and why.

**Stretch goals:** describe the renewal flow as an Arazzo workflow; add an AsyncAPI description for `pass.renewed` events; generate a typed client and use it in a test.

**What it proves to an employer:** you design APIs on paper first, consistently, in a form other teams can review and build against.

### P2 · Idempotent payouts with signed webhooks (L2, ~15 hours)

**Real-world inspiration:** Razorpay makes `X-Payout-Idempotency` mandatory on payouts and signs webhooks with HMAC-SHA256 over the raw body ([Razorpay docs](https://razorpay.com/docs/api/x/payout-idempotency/make-request/)). Stripe's idempotency design replays the first response for a retried key ([Stripe docs](https://docs.stripe.com/api/idempotent_requests)).

**What to build:** a payouts API (`POST /payouts`, `GET /payouts/{id}`, `GET /payouts` with cursors). Payouts go to a simulated bank that randomly times out, succeeds late or fails. The API also needs:
- idempotency keys;
- signed webhooks (`payout.processed`, `payout.failed`, `payout.reversed`) delivered with retries and a replay tool;
- per-merchant rate limits with `429` and `Retry-After`;
- a merchant-side sample consumer that verifies signatures and deduplicates.

**Acceptance criteria:**
- **Idempotency under concurrency:** 1,000 pairs of identical requests sent within 10 ms of each other create exactly 1,000 payouts. Each duplicate gets the original response, or a `409` while the original is still in flight, as you document.
- **Key misuse:** reusing a key with a different body returns `422` (or your documented code) and moves no money.
- **Crash safety:** killing the server at 20 random points during request handling, then retrying, never creates a duplicate payout (verified by an invariant query).
- **Webhook durability:** with the consumer down for 60 minutes, every event is delivered within 10 minutes of recovery. Zero are lost, duplicates are absorbed by the consumer, and out-of-order delivery is handled with a version field.
- **Signature security:** requests with a bad signature, a modified body or a timestamp older than 5 minutes are rejected; a test proves each.
- **Rate limits:** a merchant over its limit gets `429` with a correct `Retry-After`, and other merchants' p99 is unaffected (load-test evidence).

**Stretch goals:** Standard Webhooks headers and an ed25519 signature option; a webhook endpoint health dashboard with automatic disabling; an SDK that generates idempotency keys and retries safely.

**What it proves to an employer:** you can build the money-moving edge of an API, which needs correct retries, duplicates and notifications, and you can prove it with adversarial tests.

### P3 · One domain, three protocols and an agent interface (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** large platforms expose the same domain in several ways: a public REST API for partners, gRPC between internal services, a GraphQL backend-for-frontend for mobile, and now tool interfaces for AI agents. MCP is the common agent interface ([MCP spec](https://modelcontextprotocol.io/specification/versioning)). In Postman's 2025 survey, 24% of respondents already design APIs with agents in mind ([Postman, Oct 2025](https://www.postman.com/state-of-api/2025/)). The domain, a food-delivery dispatch platform, is an **illustrative scenario**.

**What to build:**
- a public REST API (OpenAPI 3.2) for orders and tracking;
- an internal gRPC service with server-streaming rider locations;
- a GraphQL backend-for-frontend for the customer app;
- an MCP server with 6–8 task-shaped tools for a support agent (look up order, explain delay, issue goodwill credit up to a limit, escalate);
- governance: Spectral and `buf` lint, oasdiff and `buf breaking` gates, a versioning and deprecation policy with headers, a generated SDK and a quick-start guide.

**Acceptance criteria:**
- **Performance:** REST p99 under 100 ms at 1,000 requests/s; the gRPC stream fans out 5,000 rider updates/s to 500 subscribers with p99 delivery under 200 ms; GraphQL queries for the home screen issue at most 5 database queries (DataLoader evidence).
- **Evolution:** the CI pipeline blocks 5 planted breaking changes across OpenAPI and protobuf, and a v1-to-v2 change ships with deprecation headers while v1 clients keep passing their contract tests.
- **Security review:** an OWASP API Security Top 10 (2023) review of your own design with zero open high-severity findings, including object-level authorization tests for every endpoint that takes an ID.
- **Agent evaluation:** a 40-task agent suite (run with at least two different models) reaches at least 90% task success. The agent makes zero goodwill credits above the limit and zero irreversible actions without a confirmation step. Every tool call is in an audit log.
- **Documentation:** a new developer completes the quick-start in under 10 minutes (observed with two testers).
- **Write-up:** a design document explaining which protocol serves which consumer and why, with one decision you would reverse given more time.

**Stretch goals:** describe the support workflow in Arazzo and test it; add per-agent budgets and anomaly alerts; serve the gRPC service to browsers through ConnectRPC.

**What it proves to an employer:** you can design and govern an API platform, not just an endpoint, including the interface that AI agents will use.

## Feeds into

- [BE401 Payments-Grade Systems](../../year_4/BE401_payments_grade_systems_transactions_idempotency/README.md): P2's idempotency and webhooks become a full payments flow with ledgers and reconciliation.
- [BE404 Microservices, Service Mesh and Platform APIs](../../year_4/BE404_microservices_service_mesh_and_platform_apis/README.md): contract testing, API gateways and platform APIs.
- [BE403 Backends for AI](../../year_4/BE403_backends_for_ai_serving_llm_features_vector/README.md): streaming responses and agent-facing tools.
- [OV02 Cloud-Native Backend](../../../../04_overlaps/OV02_cloud_native_backend/README.md) and [AIE401 Multi-Agent Systems, MCP and Orchestration](../../../ai_engineering/year_4/AIE401_multi_agent_systems_mcp_and_orchestration/README.md).
