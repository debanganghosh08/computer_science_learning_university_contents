# SAR402 · Labs and projects

Labs run locally with Keycloak (two or more realms acting as separate IdPs), OpenFGA or SpiceDB, OPA and Cedar, SPIRE, SoftHSM as an HSM stand-in, and small demo applications you write. Aadhaar and DigiLocker integrations are **simulated** with mock services that follow the public specifications; never use real Aadhaar numbers, and generate synthetic numbers that only pass the Verhoeff check digit. Lab 2 is done without AI assistants. All organisations below are *illustrative scenarios* unless a source is given.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Trust graph | Build the identity trust graph of an illustrative bank and mark the broken edge for four public incidents (Exchange Online 2023, Okta 2023, Midnight Blizzard 2024, Salesloft Drift 2025) | Graph with mint-capable edges, incident overlays | 3 h |
| 2 · e-KYC and DigiLocker design (no AI) | Design an AUA/KUA integration with HSM placement and an Aadhaar Data Vault per UIDAI Circular 14 of 2025, plus a DigiLocker document fetch with OAuth and PKCE | Sequence diagrams, vault layout, data retention table, each choice cited to a UIDAI or DigiLocker document | 4 h |
| 3 · Federation after an acquisition | Broker two Keycloak realms (acquirer and acquired) with home realm discovery and an attribute-release policy | Configuration, login traces from both populations, a blocked over-release | 5 h |
| 4 · OAuth audit and FAPI 2.0 | Audit a provided OAuth deployment against RFC 9700; build a payment-initiation flow with PAR and DPoP-bound tokens | Findings table; a test showing a copied DPoP-bound token is rejected | 5 h |
| 5 · Passkeys and recovery | Add passkeys to a demo app with fallback; design and implement recovery with re-proofing | Rollout plan, recovery flow, three failed social-engineering test scripts against your own help-desk procedure | 5 h |
| 6 · Rego and Cedar | Write the same ten rules in both languages with tests, then run Cedar's analysis tooling to check a property | Policies, tests, the analysis result | 4 h |
| 7 · ReBAC and the new-enemy problem | Model folder and document sharing in OpenFGA or SpiceDB; reproduce a new-enemy race in a toy cache and fix it with consistency tokens | Schema, race reproduction, fix and test | 5 h |
| 8 · SPIRE and federation | Issue SPIFFE identities to three workloads; federate two trust domains and authorise one cross-domain call | Configuration, a refused call without identity, a permitted federated call | 5 h |
| 9 · Agents and MCP | Design identities for three agents; review a provided MCP server design against the MCP security best practices | Identity design with token exchange; review findings (passthrough, audience, consent, SSRF) | 4 h |
| 10 · Shared signals and IdP outage | Send CAEP-style session-revoked events between two lab systems; simulate an IdP outage and run the degraded mode | Event logs with latency; outage test record | 4 h |

## Projects

### P1 · Identity architecture brief for a university (L1, ~6 hours)

**Real-world inspiration:** universities manage students, staff, alumni, recruiters and research partners, often across several identity systems after mergers. The university is an *illustrative scenario*.

**What to build:** a brief with identity domains, IdP and federation topology (including a partner university), assurance levels per service under NIST SP 800-63-4, token flows for three applications, and an authorization model for course and grade data.

**Acceptance criteria:**
- Every identity domain has a named source of truth, lifecycle trigger and owner.
- IAL, AAL and FAL choices are justified for at least five services.
- Token flows avoid the implicit grant and browser storage of refresh tokens, consistent with RFC 9700 and RFC 10017.
- The authorization model handles "a teaching assistant can see grades only for sections they assist", and you show three test cases.
- Partner federation releases only the attributes listed in a written attribute contract.

**Stretch goals:** an alumni identity that survives graduation without keeping student privileges; a SCIM provisioning design.

**What it proves to an employer:** you can design identity for a realistic organisation, not just configure one login.

### P2 · Onboarding identity for a digital lender (L2, ~15 hours)

**Real-world inspiration:** UIDAI requires HSM custody of authentication signing and e-KYC decryption keys and an Aadhaar Data Vault with non-derivable reference keys ([UIDAI FAQ](https://uidai.gov.in/images/FAQs_Aadhaar_Data_Vault_03112025_v10.pdf)); DigiLocker's partner APIs use OAuth 2.0 with PKCE ([DigiLocker](https://img1.digitallocker.gov.in/assets/img/Digital%20Locker%20Authorized%20Partner%20API%20Specification%20v1.11.pdf)); RBI's 2026 authentication directions apply to payment steps. The lender is an *illustrative scenario*.

**What to build:** an onboarding and sign-in system with mock UIDAI and DigiLocker services: e-KYC with an Aadhaar Data Vault (SoftHSM-backed keys), DigiLocker document fetch, passkey sign-in with risk-based step-up, consent records, and erasure.

**Acceptance criteria:**
- An automated scan of every database, log, cache and trace store finds zero synthetic Aadhaar numbers outside the vault after 200 onboarding runs.
- Signing and decryption keys are generated in SoftHSM and marked non-exportable; an export attempt fails.
- Reference keys are random, not derived from the number (show the generation code and a test).
- A consent record exists for every data use, and an erasure request removes or crypto-shreds the person's KYC artefacts within the stated period, with evidence.
- Account recovery requires re-proofing; three scripted social-engineering attempts against your help-desk procedure fail.

**Stretch goals:** Virtual ID support; a sub-AUA isolation design with per-entity keys and logs.

**What it proves to an employer:** you can integrate India's identity rails the way regulated companies must, with evidence rather than promises.

### P3 · Identity and authorization platform for a multi-tenant SaaS with agents (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** Zanzibar-style authorization (Pang et al., 2019) and its open implementations; OpenID AuthZEN (2026) for PEP–PDP interoperability; the MCP authorization model and its ban on token passthrough; enterprise customers who insist on their own SSO. The SaaS is an *illustrative scenario*: a project-management product with enterprise tenants, each using its own IdP, and AI agents that act for users.

**What to build:**
- customer identity with per-tenant SAML or OIDC federation and passkeys for non-federated users;
- a ReBAC authorization service (OpenFGA or SpiceDB) behind an AuthZEN-style API, with PEPs in three services;
- SPIFFE workload identity between services;
- agent identities with RFC 8693 token exchange, per-tool scopes and an approval step enforced at the PDP;
- shared-signals revocation across services, an IdP outage mode and signing-key monitoring;
- an architecture document with ADRs and a threat model.

**Acceptance criteria:**
- A cross-tenant isolation suite of at least 50 cases passes 100%.
- With 1 million relation tuples on a laptop-class machine, authorization checks meet a p99 latency you state in advance (for example under 20 ms), shown in a load-test report.
- A new-enemy test (remove access, then add content) never shows the new content to the removed user.
- An agent cannot perform any action outside the user's delegated scope, and a benign canary instruction in task content cannot trigger the approval-gated action without a human approval record.
- A session-revoked event reaches all three services and stops access within 60 seconds.
- A token signed by a key not in the current key set raises an alert and is rejected.
- You defend the platform in a 25-minute oral; the panel adds a requirement (for example, "auditors need read-only access to one tenant for 7 days") and you design it live.

**Stretch goals:** Cedar policies for attribute conditions on top of ReBAC; a migration plan from the product's old role tables.

**What it proves to an employer:** you can design the identity and authorization core of a modern SaaS product, including AI agents, which few engineers have done.

## Feeds into

- [SAR403 Security Architecture for AI Systems and Agents](../SAR403_security_architecture_for_ai_systems_and_agents/README.md): agent identity, delegation and approval.
- [OV07 Privacy Engineering](../../../../04_overlaps/OV07_privacy_engineering/README.md): consent, minimisation and erasure from P2.
- [SAR501 Frontier Seminar](../../year_5/SAR501_frontier_seminar_post_quantum_migration/README.md): post-quantum signatures for tokens and identity for autonomous systems.
- The [flagship industry project](../../../../06_career_and_market_readiness/05_industry_projects/SAR_security_architecture.md): its identity and authorization layer.
