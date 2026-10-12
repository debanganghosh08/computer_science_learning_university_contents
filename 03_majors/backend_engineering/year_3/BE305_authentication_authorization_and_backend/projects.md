# BE305 · Labs and projects

Every lab runs on your own machine against your own code, a local identity provider (Keycloak or another open-source server) and deliberately vulnerable training apps (OWASP Juice Shop, OWASP crAPI). Labs are defensive: you build protections and write tests that prove them, and you review code for flaws. Do not test any system you do not own or have written permission to test. Lab 2 and the live code-review exam are done without AI assistants.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Passwords and throttling | Argon2id storage with on-login rehashing; NIST SP 800-63B-4 policy (length, blocklist, no composition rules); layered throttling; enumeration-safe responses | Tests for every rule; a timing comparison showing responses do not reveal which accounts exist | 5 h |
| 2 · Sessions and token validation (no AI) | Redis sessions with rotation and revocation; a JWT validator with algorithm allowlist, `iss`/`aud`/`exp`/`nbf` checks and key-ID lookup against a JWKS | Validator that accepts the 3 good tokens and rejects all 12 bad tokens in the provided set | 6 h |
| 3 · OAuth and OIDC | Authorization code with PKCE; a backend-for-frontend per RFC 10017; a resource server with JWKS caching; signing-key rotation; DPoP-bound tokens | Sequence diagrams from captured traffic; a rotation run with zero failed requests; a test showing a copied DPoP-bound token is rejected | 10 h |
| 4 · Passkeys and step-up | WebAuthn registration and login with a maintained library; passkey step-up for changing a payout account | Working demo, recovery-path design note, and tests for the step-up gate | 6 h |
| 5 · Policies as code | 10 authorization policies in OPA (Rego) or Cedar with unit tests, including tenant isolation and time-bound access | Policy files, 40+ tests, and a decision log for one request | 5 h |
| 6 · ReBAC and object-level checks | Folder and document sharing in OpenFGA or SpiceDB; fix 5 planted object-level authorization bugs in a lab API | Authorization model, fixed code, and an automated "every endpoint × every role × another tenant's object" test matrix | 8 h |
| 7 · Workload identity | Two services with SPIFFE identities via SPIRE and mTLS; fix a confused-deputy bug with token exchange | Proof that a service without a valid identity is refused; before/after for the confused deputy | 5 h |
| 8 · Secrets | Dynamic Postgres credentials from OpenBao or Vault; envelope encryption with a local KMS; secret scanning in CI | A leaked-secret drill: a planted secret is caught in a commit and in a log line | 5 h |
| 9 · Inputs and SSRF | Harden an upload endpoint and a "fetch URL" feature (allowlist, internal-range blocking, metadata endpoint protection); fix a fail-open exception path | Regression tests for each fix, run only against local targets | 5 h |

## Projects

### P1 · Accounts service done to the standard (L1, ~6 hours)

**Real-world inspiration:** NIST SP 800-63B-4 (July 2025) changed long-standing password advice: no composition rules, no forced periodic changes, blocklist checks ([NIST](https://pages.nist.gov/800-63-4/sp800-63b.html)). Many production systems still use the old rules.

**What to build:** an accounts service with sign-up, login, logout, password change, password reset by email (to a local mail sink), session listing and per-device revocation. Follow NIST SP 800-63B-4 and the OWASP Authentication and Password Storage cheat sheets.

**Acceptance criteria:**
- Passwords are stored with Argon2id at parameters that take 150–400 ms on your machine. Legacy bcrypt hashes in a seeded table are upgraded on next login (test included).
- The password policy enforces length and a blocklist (at least 100,000 known-breached passwords) with no composition rules, and a test proves each rule.
- Login responses and timings do not reveal whether an account exists: the median timing difference is under 10 ms over 1,000 attempts.
- After 10 failed attempts on one account, further attempts slow down progressively without locking the real user out permanently. IP-based limits work alongside, and both are tested.
- Reset tokens are single-use, expire in 15 minutes and are stored hashed. A completed reset ends all other sessions.
- Session cookies are `HttpOnly`, `Secure` and `SameSite=Lax` or stricter, rotate on login, and have idle and absolute timeouts.

**Stretch goals:** add TOTP; add passkey login; check passwords against a breach corpus with k-anonymity range queries instead of a local list.

**What it proves to an employer:** you can build the most-attacked part of any product to current standards, not to folklore.

### P2 · Multi-tenant authorization service (L2, ~15 hours)

**Real-world inspiration:** Google's Zanzibar ([Pang et al., 2019](https://www.usenix.org/conference/atc19/presentation/pang)) handles authorization for sharing across Google products. OpenFGA and SpiceDB bring the model to everyone else. Broken object-level authorization is the top risk in the [OWASP API Security Top 10](https://owasp.org/API-Security/editions/2023/en/0x11-t10/).

**What to build:** a B2B document platform with organizations, teams, folders and documents. Permissions are owner, editor, commenter and viewer, inherited from folders and teams, with link sharing inside an organization. Use OpenFGA or SpiceDB for relationships, and OPA or Cedar for contextual rules (for example, no external sharing for "restricted" documents; contractors only during working hours). Add PostgreSQL row-level security as a backstop. Every API endpoint enforces object-level checks, and list endpoints filter by permission.

**Acceptance criteria:**
- **Isolation:** a generated test matrix (every endpoint × every role × own object, another user's object and another tenant's object, with at least 500 cases) passes with zero unauthorized access.
- **Backstop:** with application checks disabled in a test build, row-level security still blocks every cross-tenant read.
- **Performance:** permission checks take under 10 ms at p99 with 1 million relationship tuples. Listing "documents I can see" for a user with 50,000 accessible documents returns the first page in under 200 ms.
- **Revocation:** after a user loses access, no read succeeds once the consistency token from the revocation is used, and you document the window when it is not used.
- **Policy tests:** every contextual policy has at least 3 tests, including a negative test.
- **Audit:** every allow and deny decision is logged with subject, object, relation and policy version, and logs contain no document content.

**Stretch goals:** an "explain why I can see this" endpoint; delegated, time-bound access for an AI agent with read-only scopes; a comparison of OpenFGA and SpiceDB on the same model.

**What it proves to an employer:** you can design and enforce authorization for a real multi-tenant product, where the most damaging bugs live.

### P3 · Identity platform for a fintech-style app (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** high-assurance APIs in finance use profiles such as FAPI 2.0 ([OpenID Foundation, 2025](https://openid.net/specs/fapi-security-profile-2_0-final.html)). In India, digital payments must use two factors, one of them dynamic, under RBI's authentication directions effective April 2026 (see the Sources section of the README). The app is an **illustrative scenario**, not a regulated product.

**What to build:** an identity and access layer for a wallet-style app with a web client, a mobile client (an emulator or a script is enough), three backend services and an AI support agent:
- **Identity provider:** an OIDC provider you configure (Keycloak or similar), or a minimal one you write.
- **Clients:** authorization code with PKCE for both clients, and a backend-for-frontend for the web client following RFC 10017.
- **Tokens:** DPoP-bound access tokens, refresh-token rotation with reuse detection, and token exchange when services call each other.
- **Authentication:** passkeys as the primary method, plus step-up authentication for adding a payee and for transfers above a threshold.
- **Authorization and identity:** relationship-based authorization for shared family wallets; SPIFFE identities with mTLS between services.
- **Secrets and keys:** dynamic database credentials, and signing-key rotation.
- **Data and agent:** PII redaction in logs, and a tamper-evident audit log. The AI support agent gets narrowly scoped, short-lived delegated tokens and cannot move money.

**Acceptance criteria:**
- **Standards conformance:** a checklist maps each OWASP ASVS 5.0 requirement you selected (at least 40, Level 2) to an automated test or a documented review. All pass.
- **Token security:** the negative suite rejects 100% of tampered, expired, wrong-audience, wrong-issuer, unknown-key, replayed and stolen-but-DPoP-bound tokens. Refresh-token reuse revokes the whole token family within 1 second.
- **Key rotation:** rotating the signing key and the database credentials under 300 requests/s causes zero failed requests.
- **Step-up:** adding a payee or transferring above the threshold without a fresh passkey assertion is refused 100% of the time in tests, including direct API calls that skip the UI.
- **Agent safety:** in a 30-task agent suite, the support agent performs zero money-moving or payee-changing actions, and every tool call carries the agent's own identity in the audit log.
- **Audit and privacy:** a log scan finds zero raw PII or tokens; the audit log detects a deliberately modified entry.
- **Write-up:** a threat model, an architecture diagram with trust boundaries, an incident runbook for "signing key leaked" that covers CERT-In's 6-hour reporting window, and a review of your own system against the CSRB Storm-0558 recommendations.

**Stretch goals:** FAPI 2.0 conformance testing with the OpenID Foundation's open-source suite; Pushed Authorization Requests; a consent and data-export flow aligned with the DPDP Rules.

**What it proves to an employer:** you can own identity and access for a sensitive product end to end, which is one of the hardest skills in backend work to replace.

## Feeds into

- [BE401 Payments-Grade Systems](../../year_4/BE401_payments_grade_systems_transactions_idempotency/README.md): step-up authentication, audit logs and secrets in a payments flow.
- [BE404 Microservices, Service Mesh and Platform APIs](../../year_4/BE404_microservices_service_mesh_and_platform_apis/README.md): mTLS and identity in a mesh, authorization at gateways.
- [BE403 Backends for AI](../../year_4/BE403_backends_for_ai_serving_llm_features_vector/README.md): scoped identities and budgets for agents.
- [SAR402 Identity Architecture at Scale](../../../security_architecture/year_4/SAR402_identity_architecture_at_scale/README.md) and [OV10 FinTech Systems Engineering](../../../../04_overlaps/OV10_fintech_systems_engineering/README.md).
