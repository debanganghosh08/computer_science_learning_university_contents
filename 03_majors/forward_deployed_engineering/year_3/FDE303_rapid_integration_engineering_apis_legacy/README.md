# FDE303 · Rapid Integration Engineering: APIs, Legacy Systems, SSO and Data Connectors

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 5 | 4 (≈ 120 hours) | L2 → L3 | [CS205](../../../../02_year_2_core_computer_science/semester_3/CS205_software_engineering_i_design_testing/README.md), [CS215](../../../../02_year_2_core_computer_science/semester_4/CS215_cloud_and_devops_foundations/README.md); assumes [FND114](../../../../01_year_1_foundations/semester_2/FND114_web_foundations_http_html_css_and_javascript/README.md), [FND115](../../../../01_year_1_foundations/semester_2/FND115_databases_i_data_modeling_and_sql/README.md), [CS204](../../../../02_year_2_core_computer_science/semester_3/CS204_computer_networks/README.md), [CS213](../../../../02_year_2_core_computer_science/semester_4/CS213_security_foundations/README.md) | [FDE403](../../year_4/FDE403_solution_architecture_pricing_and_roi/README.md), [FDE401](../../year_4/FDE401_data_integration_and_ontology_modeling/README.md), [FDE304](../FDE304_deploying_ai_in_the_enterprise/README.md), [FDE402](../../year_4/FDE402_debugging_and_operating_in_customer_environments/README.md) |

## Why this course matters now

Most of a deployment's first weeks are integration: getting data out of an ERP, logging users in through the customer's identity provider, receiving webhooks from a payment gateway, reading a nightly file from an SFTP server, or querying a twenty-year-old database without slowing it down. Palantir's deployment strategist post describes building "a data pipeline to integrate the customer's ERP system" as ordinary daily work (2022). Anthropic's FDEs now also deliver "MCP servers, sub-agents, and agent skills" that expose customer systems to AI agents. AI coding agents write API clients, mappers and test fixtures quickly, and an analysis of AI services teams lists "system integrations" and "combing through API documentation" as work to automate (a16z, 2025). What still needs a skilled engineer: choosing the least risky integration path, reading what the system actually returns rather than what the documentation claims, making every write idempotent, handling rate limits and partial failures, keeping secrets and identities safe, and leaving behind something the customer can run. This course is about integrating fast without creating the next legacy problem.

## Learning outcomes

By the end you can:

1. **Choose** an integration style (file transfer, shared database, API call, messaging) for a given system and constraint set, and **justify** it in writing.
2. **Build** a resilient client for a REST, SOAP or GraphQL API with authentication, pagination, timeouts, retries with backoff and jitter, rate-limit handling and structured errors.
3. **Make** writes idempotent and event processing safe under duplicates, reordering and replays (idempotency keys, deduplication, outbox).
4. **Receive** webhooks securely (signature verification, replay windows) and reconcile them against the source of truth.
5. **Ingest** files from SFTP and legacy formats (CSV dialects, fixed-width, EBCDIC, Excel) with checksums, manifests and idempotent processing.
6. **Extract** data from legacy databases safely (read replicas, change data capture) and **load** it with a reproducible, incremental pipeline.
7. **Integrate** enterprise single sign-on with SAML 2.0 and OpenID Connect, plus SCIM provisioning, and **debug** common failures.
8. **Integrate** India-specific systems through their official channels: payment gateways for UPI, the GST e-invoice API, DigiLocker via API Setu, and Account Aggregator consent flows.
9. **Expose** a customer system to AI agents through an MCP server with scoped permissions, and **audit** AI-generated integration code.

## Chapters and lessons

### Chapter 1 · Integration triage (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 The four styles | File transfer, shared database, remote procedure invocation, messaging (Hohpe and Woolf, *Enterprise Integration Patterns*); coupling and failure modes of each | Classify ten real integrations you have used (UPI app to bank, college ERP exports) by style |
| 1.2 System inventory | Interfaces available, owners, auth, volumes, change frequency, environments (sandbox, UAT, production) | Fill an inventory template for an illustrative manufacturer with SAP, a Tally ledger and Excel trackers |
| 1.3 Read before write | Start read-only; the blast radius of writes; dry runs and approval steps | Write a read-first plan with the first write gated by a human approval |
| 1.4 Throwaway versus durable | When a one-off script is right; what makes it survivable (logging, config, tests, README) | Turn a 50-line script into a minimal durable job |

**Check your understanding:** Why does a shared-database integration create long-term coupling? What makes an integration "durable enough" for a pilot? Which question about a system should you ask before reading its API documentation?

### Chapter 2 · REST APIs in a hurry (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Reading a contract | OpenAPI documents; generating clients; where generated clients go wrong (nullable fields, enums, date formats) | Generate a client from an OpenAPI file and fix three type mismatches against real responses |
| 2.2 Authentication patterns | API keys, OAuth 2.0 client credentials (RFC 6749), token caching and refresh, scopes | Implement client-credentials auth with token reuse and expiry handling |
| 2.3 Pagination and filtering | Offset, cursor and link-header pagination; consistency during paging; incremental sync with `updated_since` | Sync 100,000 records from a mock API with cursor pagination and resume after a crash |
| 2.4 Errors | HTTP status semantics; problem details (RFC 9457); retryable versus terminal errors | Build an error classifier with tests for 15 response cases |
| 2.5 Observing real traffic | Recording and replaying with mitmproxy; mocking with Prism or WireMock from OpenAPI | Record a session against a sandbox API and replay it offline in tests |

**Check your understanding:** Why can offset pagination skip or duplicate records during a sync? Which errors should never be retried? What do you lose when tests only use the documented examples?

### Chapter 3 · SOAP and GraphQL (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 SOAP and WSDL | Envelopes, XML Schema types, faults; SOAP 1.1 versus 1.2; why banks, insurers and government systems still use it | Call a public SOAP service with zeep; handle a fault |
| 3.2 WS-Security basics | UsernameToken, signed messages, certificate handling; reading a WSDL's policy section | Configure a client certificate and verify the request on a local mock |
| 3.3 GraphQL clients | Introspection, typed queries, fragments, error arrays alongside data, partial success | Write typed queries against a public GraphQL API and handle partial errors |
| 3.4 GraphQL limits | Query cost and depth limits, pagination connections, persisted queries | Measure how query shape changes cost on a rate-limited API |

**Check your understanding:** Why can a GraphQL response contain both data and errors, and what should your client do? What makes SOAP integrations slow to build but stable to run? When does introspection mislead you?

### Chapter 4 · Reliability: timeouts, retries, rate limits, idempotency (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Timeouts | Connect versus read timeouts; budgets across a call chain; why missing timeouts cause outages | Set timeouts on every call in a client and show one hung request recovering |
| 4.2 Retries with backoff and jitter | Exponential backoff, full jitter, retry budgets (AWS Builders' Library); retrying only safe operations | Implement with tenacity; simulate 30% failure and measure load on the server |
| 4.3 Rate limits | 429 Too Many Requests (RFC 6585), `Retry-After`, the IETF RateLimit header draft; client-side token buckets | Respect a 10 requests/second limit across four worker processes |
| 4.4 Idempotency | Idempotency keys for unsafe operations (IETF draft; Stripe's design); deduplication tables; natural keys | Make a "create invoice" call safe under retries; prove no duplicates in 1,000 chaos runs |
| 4.5 Circuit breakers and fallbacks | Open, half-open, closed states; degrading gracefully | Add a circuit breaker and show the system staying responsive while a dependency is down |

**Check your understanding:** Why can retries without jitter make an outage worse? A payment call timed out: did it fail? How do you find out safely? What is the difference between idempotent by design and idempotent by deduplication?

### Chapter 5 · Webhooks and events (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Webhook security | HMAC signatures, timestamps and replay windows, secret rotation (Standard Webhooks specification) | Verify signed webhooks; reject replays older than five minutes |
| 5.2 Delivery semantics | At-least-once delivery, duplicates, out-of-order events, missed events; respond fast, process later | Build a receiver that acknowledges in under 200 ms and processes from a queue |
| 5.3 Reconciliation | Webhooks are notifications, not the source of truth; polling the API to confirm state; nightly reconciliation | Reconcile a day of simulated payment events against the provider's API |
| 5.4 Publishing events | Transactional outbox; CloudEvents envelope; schema versioning | Emit events from a database change with an outbox and a relay |
| 5.5 Gateway specifics | Razorpay distinguishes server-side webhooks from the checkout `callback_url` and recommends webhooks for server-side verification | Implement both in a sandbox and show why the callback alone is unsafe |

**Check your understanding:** Why must a webhook handler be idempotent? What do you do when the provider was down for six hours? Why is a browser redirect not proof of payment?

### Chapter 6 · Files, SFTP and legacy formats (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 File drops | SFTP with key-based auth (paramiko), PGP-encrypted files, arrival windows, manifests and checksums, "done" marker files | Build a poller that processes each file exactly once, even if re-uploaded |
| 6.2 CSV is not a standard | Dialects, quoting, embedded newlines, encodings (UTF-8 with BOM, Windows-1252), decimal commas | Parse ten deliberately broken CSV files; report every row you changed |
| 6.3 Excel traps | Dates as serial numbers, leading zeros on PIN codes and phone numbers, merged cells, hidden sheets, formulas | Load a messy Excel tracker and produce a validation report |
| 6.4 Mainframe-era formats | Fixed-width records, COBOL copybooks, packed decimal, EBCDIC | Decode a sample fixed-width file with a copybook layout |
| 6.5 File contracts | Agreeing schema, naming, timing, failure handling and contacts with the customer's team | Write a one-page file interface agreement |

**Check your understanding:** Why are "done" marker files used? What goes wrong when Excel opens a CSV of Indian PIN codes? How do you prove a file was processed exactly once?

### Chapter 7 · Legacy databases and change data capture (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Safe access | Read-only users, read replicas, query timeouts, off-peak windows, explain plans before running | Write a safe-access checklist and test a query plan on a large table |
| 7.2 Old schemas | Cryptic names, codes stored as strings, soft deletes, local time zones, collations, stored procedures | Reverse-engineer a sample legacy schema into a data dictionary |
| 7.3 Incremental extraction | High-water marks on timestamps or IDs; catching updates and deletes | Build an incremental extract that survives a restart |
| 7.4 Change data capture | Log-based CDC (Debezium) versus triggers versus polling; snapshots; ordering | Stream changes from Postgres with Debezium to a local sink |

**Check your understanding:** Why can a "last updated" column miss changes? What load does an innocent `SELECT *` put on a production ERP database? When is CDC worth its operational cost?

### Chapter 8 · ETL in a hurry (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Local engines | DuckDB and Polars for fast transformations on a laptop; pandas trade-offs | Join three messy sources of 5 million rows locally; record time and memory |
| 8.2 Loading frameworks | dlt for schema inference, incremental loading and normalisation | Load a paginated API into DuckDB with dlt and evolve the schema |
| 8.3 Validation at the edges | Row counts, null checks, referential checks, quarantine tables | Add checks that block a bad load and quarantine failing rows |
| 8.4 Reproducibility | Config files, pinned dependencies, idempotent runs, a README a customer engineer can follow | Hand your pipeline to a classmate who must run it without asking you |

**Check your understanding:** What makes a pipeline idempotent? Why quarantine bad rows instead of dropping them? Which checks catch silent truncation?

### Chapter 9 · Enterprise single sign-on and provisioning (weeks 9–10)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 SAML 2.0 | Service provider and identity provider, SP- and IdP-initiated flows, assertions, signing certificates, metadata, NameID, attributes (OASIS SAML 2.0) | Integrate a sample app with Keycloak via SAML; inspect assertions |
| 9.2 OpenID Connect | Authorization code flow with PKCE (RFC 7636), discovery documents, ID token validation (issuer, audience, expiry, signature); OAuth security best current practice (RFC 9700) | Add OIDC login with Keycloak; write tests that reject tampered tokens |
| 9.3 Enterprise IdPs | Microsoft Entra ID, Okta, Google Workspace; group claims, conditional access, multi-tenant apps | Map groups to application roles; handle a user in 300 groups |
| 9.4 Provisioning | SCIM 2.0 (RFC 7643, RFC 7644); just-in-time provisioning; deprovisioning on exit | Implement a minimal SCIM endpoint and test create, update and deactivate |
| 9.5 Debugging SSO | Clock skew, certificate rotation, wrong audience or ACS URL, encoding of NameID, browser tracers | Diagnose five planted SSO failures from logs and browser traces |

**Check your understanding:** Why does a two-minute clock difference break SAML logins? What must an application do when a user is removed from the IdP? Why is validating an ID token's audience essential?

### Chapter 10 · Secrets, network paths and least privilege (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Secrets | Secret managers, short-lived credentials, rotation, never in code or tickets | Move all secrets from a repo into a secret manager and rotate one |
| 10.2 Service accounts | Least-privilege scopes, per-integration accounts, audit logs | Write the minimum scopes for three integrations and test denials |
| 10.3 Network paths | IP allowlists, VPN and private connectivity, mutual TLS, egress proxies | Configure mutual TLS between two services on a local network |
| 10.4 Security review of an integration | Data flow diagram, data classification, threat list for each interface | Produce a one-page integration security note |

**Check your understanding:** Why should each integration have its own service account? What does mutual TLS prove that an API key does not? What belongs in an integration security note?

### Chapter 11 · India-specific integrations (weeks 12–13)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 UPI through payment gateways | Businesses integrate UPI through a payment aggregator or bank (Razorpay, Cashfree, PayU and others), not directly with NPCI; orders, payments, refunds, webhooks; reconciliation using transaction references | Build a sandbox checkout with webhook verification and a nightly reconciliation report |
| 11.2 GST e-invoicing | The Invoice Registration Portal issues an IRN and signed QR code; the NIC e-invoice API sandbox; e-way bill generation by IRN; for taxpayers with aggregate turnover of ₹10 crore or more, invoices must be reported within 30 days (in force since 1 April 2025) | Generate IRNs in the NIC sandbox from an invoice JSON; handle validation errors and duplicate submissions |
| 11.3 DigiLocker via API Setu | Consent-based document access through OAuth-style authorisation for approved requesters; issued documents versus uploads | Read the API Setu DigiLocker documentation; draw the consent flow and list the approvals a business needs |
| 11.4 Account Aggregator | Consent artefacts, financial information users and providers, the Sahamati ecosystem | Model an AA consent request for a loan underwriting pilot (illustrative) |
| 11.5 What not to touch | Aadhaar numbers and biometrics only through licensed entities and permitted flows; masking; logs that must never hold identifiers | Write a logging policy that redacts PAN, Aadhaar and phone numbers; test it |

**Check your understanding:** Why does a merchant rely on webhooks plus reconciliation rather than the payment page result? What happens to your invoice integration if the job that reports IRNs fails for five weeks? Why do Indian consent-based data flows (DigiLocker, Account Aggregator) change how you design storage?

### Chapter 12 · Integrations for AI agents (week 14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 MCP servers | Exposing customer systems as tools and resources (Model Context Protocol); per-tool permissions, read-only defaults | Wrap your Chapter 2 API in an MCP server with one read and one approval-gated write tool |
| 12.2 Tool design | Narrow tools with clear schemas, errors an agent can act on, idempotent writes | Redesign a "do anything" tool into four narrow ones and compare agent success on ten tasks |
| 12.3 Auditing AI-generated integration code | Invented endpoints and fields, missing pagination, retries on unsafe calls, secrets in code | Review an AI-generated connector against a checklist; file every defect |
| 12.4 Testing agent-facing integrations | Contract tests for tool schemas, injected tool errors and timeouts, per-agent rate limits, checking end state rather than the agent's claim | Write contract tests for your MCP tools; run an agent against injected failures and verify system state afterwards |

**Check your understanding:** Why should agent tools be narrower than human-facing APIs? Which integration bugs do AI coding agents produce most often in your logs? What permission model would you give an agent that can create invoices?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Integration inventory | Read-first plan |
| 2 | 2 | Lab 2 · Resilient REST client | — |
| 3 | 3 | Lab 3 · SOAP and GraphQL | — |
| 4 | 4 | Lab 4 · Chaos test for idempotency | **P1 due** |
| 5 | 5 | Lab 5 · Webhooks and reconciliation | — |
| 6 | 6 | Lab 6 · SFTP and broken files | — |
| 7 | 7 | Lab 7 · Legacy database and CDC | Mid-term (AI off): debugging and design |
| 8 | 8 | Lab 8 · Reproducible pipeline handoff | — |
| 9 | 9 | Lab 9 · SAML and OIDC with Keycloak | — |
| 10 | 9 | Lab 9 (cont.): SCIM and SSO debugging | **P2 due** |
| 11 | 10 | Lab 10 · Secrets and mutual TLS | — |
| 12 | 11 | Lab 11 · Payment gateway sandbox | — |
| 13 | 11 | Lab 11 (cont.): e-invoice sandbox | — |
| 14 | 12 | Lab 12 · MCP server and code audit | **P3 due** |
| 15 | Review | Timed integration exam; P3 defence | Final exam (AI off for the written part) |

## Working with AI in this course

- **Use AI for:** generating clients from OpenAPI or WSDL, writing parsers for odd formats, drafting test fixtures and mock servers, explaining unfamiliar error messages, and searching long API documentation. Claude Code, GitHub Copilot, Cursor and OpenAI Codex all do this well.
- **Do without AI (drills):** a weekly 45-minute timed integration (unknown API, write a paginated, retrying client by hand); SSO debugging from raw SAML and JWTs; idempotency and reconciliation designs; the written part of the final exam.
- **Verify AI output by:** running generated clients against recorded real responses, not documentation examples; chaos tests (injected 429s, timeouts, duplicates) before trusting any retry logic; checking every endpoint and field name against the live sandbox; secret scanning (gitleaks or similar) on every commit.
- **Where AI still fails here (show it):** keep a defect log of AI-generated integration code: invented fields, wrong pagination termination, retries on non-idempotent POSTs, missing timeouts, unverified webhook signatures. Lab 12 requires at least five logged defects with fixes.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (12) | 30% |
| Projects P1–P3 | 35% |
| Timed integration drills | 5% |
| Mid-term (AI off) | 10% |
| Final exam + P3 defence | 20% |

**Mastery gate.** You pass when you can, in one working day with an unfamiliar sandbox system: (1) build a client that syncs all records incrementally with pagination, timeouts, backoff with jitter and rate-limit compliance, and survives a chaos test with zero duplicates and zero lost records; (2) add OIDC or SAML login against a provided IdP and fix two planted SSO faults; (3) explain, AI off, how you would make a payment-confirmation flow correct under duplicate and missing webhooks.

## Industry reality

Integration dominates early deployment work: Palantir's deployment strategists build ERP pipelines (2022); OpenAI's FDE postings ask for full-stack builders who take prototypes to production; Razorpay's FDE posting lists "APIs, webhooks, integration patterns, cloud" and "server-to-server hooks" as core skills (2026); Anthropic's FDEs ship MCP servers. In India, integrations with payment gateways, the GST e-invoice system and consent-based public digital infrastructure (DigiLocker, Account Aggregator) are routine for fintech, lending, logistics and manufacturing deployments.

**Interview questions from this course**

1. *Sync 2 million customer records nightly from a rate-limited API.* Strong answer: incremental sync with a cursor or `updated_since`; respects limits with a token bucket and `Retry-After`; resumable checkpoints; idempotent upserts; reconciliation counts; alerting on drift.
2. *A customer reports duplicate invoices created by your integration. Debug it.* Strong answer: checks retries on non-idempotent calls, webhook duplicates and concurrent workers; adds idempotency keys or unique constraints; writes a cleanup and a reconciliation; adds a chaos test.
3. *Walk me through SP-initiated SAML login and three ways it breaks.* Strong answer: AuthnRequest, IdP authentication, signed assertion posted to the ACS URL, validation; failures: clock skew, certificate rotation, wrong audience or ACS URL, missing attributes.
4. *How do you integrate with a system that only offers a nightly CSV over SFTP?* Strong answer: file interface agreement, key-based auth, manifest and checksum, done markers, idempotent processing keyed by file hash, quarantine, alerts on missing files, encoding handling.
5. *Should our agent call the customer's ERP API directly?* Strong answer: wraps it in narrow tools via MCP or a service; read-only by default; approval gates on writes; per-agent service accounts; audit logs; rate limits; idempotent writes; tests on tool errors.

## Resources (free first)

- **Patterns:** Hohpe and Woolf, *Enterprise Integration Patterns* (site) — https://www.enterpriseintegrationpatterns.com/ ; transactional outbox — https://microservices.io/patterns/data/transactional-outbox.html ; circuit breaker — https://martinfowler.com/bliki/CircuitBreaker.html ; AWS Builders' Library, "Timeouts, retries, and backoff with jitter" — https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/
- **Standards:** OpenAPI — https://spec.openapis.org/oas/latest.html ; GraphQL — https://spec.graphql.org/ ; SOAP 1.2 — https://www.w3.org/TR/soap12/ ; RFC 9457 — https://www.rfc-editor.org/rfc/rfc9457 ; RFC 6585 — https://datatracker.ietf.org/doc/html/rfc6585 ; Idempotency-Key draft — https://datatracker.ietf.org/doc/draft-ietf-httpapi-idempotency-key-header/ ; RateLimit headers draft — https://datatracker.ietf.org/doc/draft-ietf-httpapi-ratelimit-headers/ ; Standard Webhooks — https://standardwebhooks.com/ ; CloudEvents — https://cloudevents.io/ ; Stripe idempotent requests — https://docs.stripe.com/api/idempotent_requests
- **Identity:** OASIS SAML 2.0 core — https://docs.oasis-open.org/security/saml/v2.0/saml-core-2.0-os.pdf ; OpenID Connect Core 1.0 — https://openid.net/specs/openid-connect-core-1_0.html ; RFC 6749 — https://www.rfc-editor.org/rfc/rfc6749 ; RFC 7636 — https://www.rfc-editor.org/rfc/rfc7636 ; RFC 9700 — https://www.rfc-editor.org/rfc/rfc9700 ; RFC 7644 (SCIM) — https://www.rfc-editor.org/rfc/rfc7644 ; Keycloak — https://www.keycloak.org/ ; Okta SAML concepts — https://developer.okta.com/docs/concepts/saml/ ; Microsoft identity platform — https://learn.microsoft.com/en-us/entra/identity-platform/
- **India:** NIC e-invoice API portal (sandbox) — https://einv-apisandbox.nic.in/ ; e-invoice portal — https://einvoice1.gst.gov.in/ ; API Setu, DigiLocker — https://apisetu.gov.in/digilocker ; Sahamati — https://sahamati.org.in/ ; Razorpay webhooks — https://razorpay.com/docs/webhooks/ ; ABDM — https://abdm.gov.in/
- **Tools:** httpx — https://www.python-httpx.org/ ; tenacity — https://tenacity.readthedocs.io/ ; zeep — https://github.com/mvantellingen/python-zeep ; paramiko — https://www.paramiko.org/ ; mitmproxy — https://mitmproxy.org/ ; Prism — https://github.com/stoplightio/prism ; WireMock — https://wiremock.org/ ; Debezium — https://debezium.io/ ; DuckDB — https://duckdb.org/ ; Polars — https://pola.rs/ ; dlt — https://dlthub.com/docs/intro ; Model Context Protocol — https://modelcontextprotocol.io/
- **Paid, optional:** Hohpe and Woolf, *Enterprise Integration Patterns* (Addison-Wesley, 2003).

## Sources

- Palantir, "A Day in the Life of a Palantir Deployment Strategist" (8 Mar 2022) — https://blog.palantir.com/a-day-in-the-life-of-a-palantir-deployment-strategist-951cb59a5a96 (checked 2026-10)
- Anthropic, Forward Deployed Engineer, London — https://job-boards.greenhouse.io/anthropic/jobs/5423029008 ; Razorpay, Forward Deployed Engineer (Aug 2026) — https://portfoliojobs.tcv.com/companies/razorpay/jobs/89918935-forward-deployed-engineer (checked 2026-10)
- a16z, "Trading Margin for Moat" (4 Jun 2025) — https://a16z.com/services-led-growth/ (checked 2026-10)
- Razorpay webhooks documentation (webhooks versus `callback_url`) — https://razorpay.com/docs/webhooks/ (checked 2026-10)
- NIC e-invoice API portal: notices on the 30-day reporting limit for AATO ≥ ₹10 crore and e-way bill limits — https://einv-apisandbox.nic.in/ ; GSTN advisory (5 Nov 2024), mirrored by Maharashtra GST — https://www.mahagst.gov.in/ (checked 2026-10)
- RFCs and specifications as listed under Resources (checked 2026-10)

_Last reviewed: 2026-10_
