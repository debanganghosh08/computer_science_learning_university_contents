# FDE303 · Labs and projects

Use sandboxes, public test APIs, local mocks and synthetic data only. Never point a lab at a production system or real personal data. Every project repository includes a README a stranger can follow, pinned dependencies, a `.env.example` with no real secrets, automated tests (including chaos tests where stated) and a short integration security note.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Integration inventory | Inventory an illustrative manufacturer's systems (SAP, Tally, Excel trackers, a vendor portal); choose a style per interface; write a read-first plan | Inventory table, style choices with reasons, gated first write | 3 h |
| 2 · Resilient REST client | Client with OAuth client credentials, cursor pagination, timeouts, backoff with full jitter and an error classifier against a mock API | Code, tests for 15 response cases, crash-and-resume demo | 5 h |
| 3 · SOAP and GraphQL | Call a public SOAP service with zeep and handle faults; typed GraphQL queries with partial-error handling | Two clients, notes on cost and depth limits | 4 h |
| 4 · Chaos test for idempotency | Make "create invoice" safe under retries, concurrency and duplicate delivery; run 1,000 randomised chaos runs | Chaos harness, zero-duplicate evidence, design note | 5 h |
| 5 · Webhooks and reconciliation | Signed webhook receiver with replay protection, queue-backed processing and a nightly reconciliation against the provider API | Receiver, reconciliation report on a day of simulated events with planted gaps | 5 h |
| 6 · SFTP and broken files | Exactly-once processing of SFTP drops with manifests, checksums and quarantine; parse ten broken CSV/Excel files and one fixed-width file with a copybook | Poller, parser, change report for every modified row | 5 h |
| 7 · Legacy database and CDC | Reverse-engineer a sample legacy schema; incremental extract with high-water marks; Debezium CDC from Postgres | Data dictionary, extractor, CDC demo with an update and a delete | 5 h |
| 8 · Reproducible pipeline handoff | Build a dlt + DuckDB pipeline with validation and quarantine; a classmate runs it from your README alone | Pipeline, validation suite, the classmate's run log and questions | 4 h |
| 9 · SAML, OIDC and SCIM | Integrate an app with Keycloak via SAML and OIDC (PKCE); group-to-role mapping; minimal SCIM endpoint; diagnose five planted SSO faults | Working logins, token-tampering tests, SCIM tests, fault diagnoses | 8 h |
| 10 · Secrets and mutual TLS | Move secrets to a secret manager, rotate one, set least-privilege scopes, configure mutual TLS | Before/after secret scan, scope matrix, mTLS demo | 3 h |
| 11 · Indian sandboxes | Payment gateway sandbox checkout with webhook verification and reconciliation; IRN generation in the NIC e-invoice sandbox with error and duplicate handling | Both integrations, reconciliation report, error-handling table | 7 h |
| 12 · MCP server and AI code audit | Wrap an API in an MCP server (read tool, approval-gated write tool); audit an AI-generated connector | MCP server, permission notes, defect log with at least five defects | 4 h |

## Projects

### P1 · A resilient connector for a rate-limited API (L1, ~6 hours)

**Real-world inspiration.** Payment providers such as Stripe document idempotency keys for safely retrying requests; the AWS Builders' Library describes backoff with jitter to avoid retry storms; the IETF is standardising `Idempotency-Key` and rate-limit headers.

**What to build.** A connector that syncs records from a mock "vendor master" API (provided OpenAPI file; mock with Prism) into Postgres: OAuth client credentials, cursor pagination, incremental sync by `updated_since`, rate-limit compliance, retries only on retryable errors, idempotent upserts.

**Acceptance criteria**
- Full sync of 100,000 records and an incremental sync of 5,000 changes, with counts reconciled to the source.
- Under a chaos profile (20% 5xx, 5% timeouts, 429s with `Retry-After`), zero duplicates and zero missing records across 20 runs.
- Never exceeds the stated rate limit (measured from the mock's logs).
- Kill the process mid-sync; restart resumes from the last checkpoint.

**Stretch goals.** Run four workers with a shared rate limiter.

**What it proves to an employer.** You write integration code that survives real networks and real APIs.

### P2 · Multi-source integration with enterprise SSO for an illustrative distributor (L2, ~15 hours)

**Real-world inspiration.** Palantir's deployment strategists describe integrating a customer's ERP to resolve shipment discrepancies (2022). Indian distributors commonly combine an ERP, accounting software exports and spreadsheets (illustrative scenario).

**What to build.** For an illustrative Pune-based FMCG distributor: integrate (a) a REST "orders" API, (b) a nightly SFTP drop of Tally-style invoice exports in CSV with encoding problems, (c) a legacy Postgres "warehouse" database through CDC, and (d) a payment gateway sandbox's webhooks. Join them into a shipment-discrepancy view (ordered vs invoiced vs dispatched vs paid). Put a small web app on top with OIDC login through Keycloak (standing in for Entra ID), group-based roles and SCIM deprovisioning.

**Acceptance criteria**
- Every source is ingested incrementally and idempotently; re-running any job changes nothing.
- The discrepancy view matches a hand-checked sample of 50 orders exactly.
- Planted faults (a duplicated file, a replayed webhook, a schema change in the CSV, a deleted warehouse row) are each detected and handled, with tests.
- Login works via OIDC; a user removed via SCIM loses access within one minute; role checks are enforced server-side.
- A one-page integration security note and a data-flow diagram.

**Stretch goals.** Add SAML login as a second option and document the differences in setup.

**What it proves to an employer.** You can connect the four kinds of systems almost every deployment meets, with identity done properly.

### P3 · An India-ready integration kit with AI agent access (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** Razorpay's FDE role covers "custom flows, SDK integration, orchestration logic, server-to-server hooks" for large merchants (2026); the NIC e-invoice system issues IRNs through APIs, and taxpayers with aggregate turnover of ₹10 crore or more must report invoices within 30 days (since April 2025); Anthropic's FDEs deliver MCP servers into customer production workflows.

**What to build.** A reusable, documented kit for an illustrative mid-size manufacturer in Gujarat that sells to distributors across India: (1) payment collection via a gateway sandbox with webhooks and daily reconciliation; (2) GST e-invoice generation in the NIC sandbox with retries, duplicate detection and a 30-day reporting alarm; (3) a vendor-onboarding flow designed around consent-based document fetch (DigiLocker via API Setu, mocked from the published documentation, labelled illustrative); (4) an MCP server that lets an internal AI assistant answer "which invoices are unpaid and why?" with read-only tools plus one approval-gated action ("send payment reminder").

**Acceptance criteria**
- Reconciliation detects 100% of planted mismatches (missing webhook, duplicate webhook, partial refund, amount mismatch) in a test day of 2,000 synthetic transactions.
- E-invoice job: zero duplicate IRN requests under retries; invoices approaching the 30-day limit raise an alert in tests.
- Logs pass a redaction test: no PAN, Aadhaar, phone number or email appears in plain text.
- MCP server: the assistant answers ten scripted questions correctly; the write tool cannot run without approval; every tool call is audit-logged with the user identity.
- A customer-facing runbook (setup, operations, failure handling) that a classmate follows to deploy the kit from scratch in under two hours.

**Stretch goals.** Package connectors so a second illustrative customer can be onboarded by changing configuration only; measure onboarding time.

**What it proves to an employer.** You can deliver the integration backbone of an Indian enterprise deployment, safely open it to AI agents, and leave it runnable by others.

## Feeds into

- [FDE304 Deploying AI in the Enterprise](../FDE304_deploying_ai_in_the_enterprise/README.md): P2 and P3 integrations become the data and tool layer of AI deployments.
- [FDE401 Data Integration and Ontology Modeling](../../year_4/FDE401_data_integration_and_ontology_modeling/README.md): the discrepancy view becomes a canonical model and entity resolution problem.
- [FDE402 Debugging and Operating in Customer Environments](../../year_4/FDE402_debugging_and_operating_in_customer_environments/README.md): SSO and network failures in restricted environments.
- [FDE403 Solution Architecture, Pricing and ROI](../../year_4/FDE403_solution_architecture_pricing_and_roi/README.md): integration effort drives cost estimates.
- [OV12 Agent Infrastructure and Platform Engineering](../../../../04_overlaps/OV12_agent_infrastructure_platform/): MCP servers and agent tool permissions at platform scale.
