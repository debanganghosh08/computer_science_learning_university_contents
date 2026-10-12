# SAR402 · Identity Architecture at Scale

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 7 | 4 (≈ 120 hours) | L3 → L4 | [SAR302](../../year_3/SAR302_threat_modeling/README.md) (also recommended: [SAR303](../../year_3/SAR303_zero_trust_architecture/README.md)) | [SAR403](../SAR403_security_architecture_for_ai_systems_and_agents/README.md), [SAR501](../../year_5/SAR501_frontier_seminar_post_quantum_migration/README.md), [OV07 Privacy Engineering](../../../../04_overlaps/OV07_privacy_engineering/README.md) |

Part of the [Security Architecture major](../../README.md). [SEC303](../../../cybersecurity_defense/year_3/SEC303_identity_and_access_management/README.md) teaches how to operate identity (lifecycle, PAM, Conditional Access, identity threat detection); [BE305](../../../backend_engineering/year_3/BE305_authentication_authorization_and_backend/README.md) teaches how to implement authentication and authorization in one service. This course designs identity for a whole organisation and its customers: which identity providers exist and how they trust each other, how tokens flow across hundreds of services and partners, how authorization works for millions of objects, how workloads and AI agents get identities, how Indian e-KYC rails are integrated without hoarding personal data, and what happens when the identity provider itself fails.

## Why this course matters now

Identity is where most large intrusions now start or end. Forged tokens from a stolen signing key opened enterprise mailboxes in 2023 ([CSRB](https://www.cisa.gov/sites/default/files/2025-03/CSRBReviewOfTheSummer2023MEOIntrusion508.pdf)); session tokens taken from support files exposed Okta customers the same year; OAuth tokens held by a sales-automation integration were used to pull data from many Salesforce instances in 2025 ([Mandiant](https://cloud.google.com/blog/topics/threat-intelligence/data-theft-salesforce-instances-via-salesloft-drift)). The standards moved fast: NIST SP 800-63-4 (July 2025) recognises syncable passkeys; the OpenID Foundation finalised the Shared Signals, CAEP and RISC specifications (2025) and the AuthZEN Authorization API 1.0 (January 2026) ([OpenID](https://openid.net/authorization-api-1-0-final-specification-approved/)); WebAuthn Level 3 became a W3C Recommendation in August 2026, and the FIDO Alliance counted 5 billion passkeys in May 2026. Identities are multiplying: workloads, bots and now AI agents that act for users through connectors such as MCP servers. In India, regulated entities integrate Aadhaar authentication and e-KYC under UIDAI rules that require HSM-held keys and an Aadhaar Data Vault ([UIDAI FAQ](https://uidai.gov.in/images/FAQs_Aadhaar_Data_Vault_03112025_v10.pdf)). AI drafts policies and analyses access graphs well; it cannot decide who should trust whom, or carry responsibility when that trust is abused.

## Learning outcomes

By the end you can:

1. **Design** an identity architecture spanning workforce, customers, partners, workloads and AI agents, with explicit sources of truth and trust relationships.
2. **Select** identity assurance, authentication assurance and federation assurance levels using NIST SP 800-63-4, and **justify** them by risk.
3. **Integrate** India's identity rails (Aadhaar authentication and e-KYC, DigiLocker partner APIs) with data minimisation, HSM custody and an Aadhaar Data Vault as UIDAI requires.
4. **Design** federation and token architectures with OAuth 2.1 (draft), RFC 9700, RFC 10017, FAPI 2.0, sender-constrained tokens and token exchange.
5. **Architect** customer identity for tens of millions of users: passkeys, risk-based authentication, account takeover defences and recovery that resists social engineering.
6. **Design** authorization services (RBAC, ABAC, ReBAC) with correct PDP/PEP placement, consistency and latency, including a Zanzibar-style system.
7. **Implement** workload identity with SPIFFE/SPIRE and cloud federation, and **design** agent identity with delegation, down-scoping and approval.
8. **Make** identity resilient and continuously evaluated (Shared Signals, IdP failover, signing-key protection), and **audit** AI-generated identity designs.

## Chapters and lessons

### Chapter 1 · Identity as architecture (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Identity domains | Workforce, customer, partner, workload, device and agent identities; why each needs different assurance and lifecycle | Draw the identity domains of an illustrative bank and where they touch |
| 1.2 Sources of truth and trust | HR systems, customer registries, workload registries; trust relationships as a graph | Build a trust graph and mark every edge that can mint tokens |
| 1.3 Incident chains | Exchange Online 2023 (signing key scope), Okta support system 2023 (session tokens in files), Midnight Blizzard 2024 (OAuth application abuse), Salesloft Drift 2025 (integration tokens) | For each, locate the broken trust edge in a diagram |
| 1.4 Identity as Tier 0 | IdPs, signing keys, directory sync servers and admin portals as the most critical assets | List the Tier 0 assets of your illustrative bank |

**Check your understanding:** (1) Why is an integration token often more dangerous than a user password? (2) What makes a trust edge "mint-capable"? (3) Why must Tier 0 assets be administered from Tier 0 devices?

### Chapter 2 · Assurance and identity proofing (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 NIST SP 800-63-4 | Identity assurance (IAL), authenticator assurance (AAL) and federation assurance (FAL) levels; digital identity risk management | Choose IAL, AAL and FAL for five services and justify each |
| 2.2 Remote proofing | Document checks, liveness, video-based KYC (permitted by RBI's KYC directions), supervised vs unsupervised proofing | Compare two proofing flows for a lending app |
| 2.3 Proofing under AI-generated media | Presentation and injection attacks on liveness checks (concepts only), defence in depth with device signals and step-up | Write requirements a proofing vendor must evidence |
| 2.4 Assurance across the lifecycle | Binding authenticators to proofed identities, re-proofing on recovery | Design re-proofing for a lost-phone recovery |

**Check your understanding:** (1) Why can a high AAL not compensate for a low IAL? (2) Where does federation weaken assurance? (3) What evidence should a liveness vendor give you?

### Chapter 3 · India's identity rails (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Aadhaar authentication ecosystem | Authentication user agencies (AUA), e-KYC user agencies (KUA), sub-AUAs and authentication service agencies (ASA); authentication modes (demographic, OTP, biometric, face) | Draw the request path from a lending app to UIDAI |
| 3.2 UIDAI security requirements | Circular 14 of 2025: HSM for signing authentication requests and decrypting e-KYC responses; Aadhaar Data Vault with non-derivable reference keys; restricted network zones; sub-AUA isolation | Design the HSM and vault layout for an AUA with three sub-AUAs |
| 3.3 Minimisation and legal limits | Virtual IDs and tokens instead of Aadhaar numbers, offline verification, masking; the Supreme Court's 2018 judgment and later amendments on who may use Aadhaar authentication (check the current rules before designing) | Remove every unnecessary Aadhaar number from a provided data flow |
| 3.4 DigiLocker integration | Partner and requester APIs using OAuth 2.0 with PKCE (since API specification v1.8); issued documents as verifiable evidence; consent and retention | Model a DigiLocker document-fetch flow and its retention policy |
| 3.5 DPDP Act duties | Purpose limitation, notice, consent, erasure and breach duties applied to KYC data | Write the data lifecycle for KYC artefacts |

**Check your understanding:** (1) Why does UIDAI forbid hashing the Aadhaar number to create reference keys? (2) What does a Virtual ID protect against? (3) When should a business keep a KYC document, and for how long?

### Chapter 4 · Federation architecture (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Protocols compared | SAML 2.0 and OpenID Connect; metadata, signing keys and rollover; attribute release | Map one partner integration in both protocols |
| 4.2 Topologies | Hub-and-spoke vs mesh; brokered federation; home realm discovery; multi-IdP after mergers | Design federation for a group of three companies after an acquisition |
| 4.3 B2B and partner access | Partner IdPs, guest accounts, attribute contracts, offboarding partners | Write a partner federation contract (attributes, assurance, notice) |
| 4.4 Provisioning | SCIM 2.0 as the companion to federation; deprovisioning gaps | Find the deprovisioning gap in a provided partner flow |

**Check your understanding:** (1) Why does a broker IdP become a single point of compromise? (2) What attributes should a partner never receive? (3) Why does federation without deprovisioning fail?

### Chapter 5 · OAuth and token architecture (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 The current baseline | OAuth 2.1 (Internet-Draft, draft-16 in September 2026): PKCE everywhere, no implicit grant; RFC 9700 security BCP; RFC 10017 for browser-based apps (backend-for-frontend) | Audit a provided OAuth deployment against RFC 9700 |
| 5.2 Strong tokens | Sender-constrained tokens (DPoP RFC 9449, mTLS RFC 8705), pushed authorization requests (RFC 9126), rich authorization requests (RFC 9396), FAPI 2.0 (final February 2025) | Design a FAPI 2.0 flow for a payment initiation API |
| 5.3 Token exchange and down-scoping | RFC 8693 for service chains; audience restriction; avoiding token passthrough | Design a three-hop service chain where each hop holds only the scope it needs |
| 5.4 Token formats and lifetimes | JWT vs opaque with introspection; signing-key rotation; revocation and lifetimes as a trade-off | Choose formats and lifetimes for six token types |

**Check your understanding:** (1) What does a sender-constrained token stop that a short lifetime does not? (2) Why is passing a user's token to a downstream API a confused-deputy risk? (3) When is introspection worth the latency?

### Chapter 6 · Customer identity at scale (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 CIAM requirements | Sign-up conversion, latency, availability, fraud, privacy; differences from workforce identity | Write CIAM requirements for a 50-million-user consumer app |
| 6.2 Passkeys at scale | WebAuthn Level 3, syncable vs device-bound passkeys, rollout and fallback design | Design a passkey rollout with metrics and fallback paths |
| 6.3 Account takeover defences | Credential stuffing, SIM-swap risk to OTPs, bot defences, risk-based step-up; RBI's 2026 authentication directions for digital payments | Design layered defences and the signals each uses |
| 6.4 Recovery | Recovery as the weakest path; help-desk social engineering (CISA advisory on Scattered Spider); re-proofing | Design recovery that a voice-cloned caller cannot pass |
| 6.5 Consent and privacy | DPDP notices, consent records, progressive profiling, data minimisation | Map consent records to product events |

**Check your understanding:** (1) Why does adding passkeys not help until recovery is fixed? (2) What signals are reliable for risk-based step-up? (3) Why is OTP-only authentication fragile in markets with frequent SIM changes?

### Chapter 7 · Authorization models and architecture (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Models | RBAC (role explosion), ABAC (attribute quality), ReBAC (relationships); hybrids | Model a hospital's access rules in all three and compare |
| 7.2 Components | Policy decision, enforcement, information and administration points; centralised vs embedded vs sidecar PDPs | Place PDPs and PEPs for an estate of 60 services |
| 7.3 Policy languages | OPA/Rego, Cedar (designed for analysis; Amazon Verified Permissions), policy testing and analysis | Write the same ten rules in Rego and Cedar and test both |
| 7.4 Interoperability | OpenID AuthZEN Authorization API 1.0 (January 2026) between PEPs and PDPs | Put an AuthZEN-style API in front of your PDP |
| 7.5 Performance | Latency budgets, caching decisions, partial evaluation, availability of the PDP | Load-test a PDP and set a caching policy |

**Check your understanding:** (1) When does RBAC break down? (2) What does a standard PEP–PDP API change for an organisation? (3) Which authorization decisions must never be cached?

### Chapter 8 · Zanzibar-style authorization (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 The Zanzibar model | Relation tuples, namespaces, userset rewrites; check, expand and list APIs (Pang et al., USENIX ATC 2019) | Model folder and document sharing with inheritance |
| 8.2 Consistency | The "new enemy" problem, consistency tokens ("zookies"), snapshot reads | Reproduce a new-enemy race in a toy system and fix it |
| 8.3 Open implementations | OpenFGA (CNCF incubating since October 2025) and SpiceDB; schema design and migration | Implement the sharing model in OpenFGA or SpiceDB |
| 8.4 Reverse queries and scale | "Which documents can this user see?"; indexing; multi-tenant schemas | Benchmark list queries at 1 million tuples |

**Check your understanding:** (1) What is the new-enemy problem, and why does it matter for document sharing? (2) Why are reverse lookups expensive? (3) How do you migrate from RBAC to ReBAC without downtime?

### Chapter 9 · Workload identity (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 SPIFFE and SPIRE | SPIFFE IDs, X.509 and JWT SVIDs, node and workload attestation, rotation | Deploy SPIRE and issue identities to three workloads |
| 9.2 Federation across trust domains | SPIFFE federation, cloud workload identity federation, CI identities | Federate two clusters and authorise one cross-domain call |
| 9.3 Standards in progress | The IETF WIMSE working group on workload identity in multi-system environments | Summarise WIMSE's problem statement and what it adds to SPIFFE |
| 9.4 Secret-less architecture | Replacing API keys and shared secrets; what still needs a secret | Remove every static secret from a four-service app |

**Check your understanding:** (1) What does attestation prove about a workload? (2) Why are workload identities short-lived? (3) What breaks when two trust domains federate?

### Chapter 10 · Machine and agent identity (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Non-human identity sprawl | Service accounts, bots, integrations, CI, now agents; ownership and expiry | Inventory non-human identities in a provided tenant export |
| 10.2 Agent identity patterns | Agent acting as itself vs on behalf of a user; delegation chains; token exchange for down-scoping; Microsoft Entra Agent ID as one vendor model | Design identities for a support agent, a coding agent and a scheduling agent |
| 10.3 Connector authorization | MCP authorization built on OAuth: protected resource metadata (RFC 9728), resource indicators (RFC 8707), audience validation, the ban on token passthrough, per-client consent for proxy servers | Review an MCP server design against the MCP security best practices |
| 10.4 Approval and step-up for agents | Human approval as an authorization decision, not a prompt; OWASP Agentic risk ASI03 (identity and privilege abuse) | Add an approval step to one high-risk agent tool at the PDP |

**Check your understanding:** (1) Why should an agent's token differ from its user's token? (2) What is token passthrough, and why does the MCP specification forbid it? (3) Where should approval be enforced?

### Chapter 11 · Continuous evaluation and resilience (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Shared signals | OpenID Shared Signals Framework, CAEP and RISC (final 2025): session revoked, credential changed, account disabled across systems | Send and receive CAEP events between two lab systems |
| 11.2 IdP availability | Regional failover, cached credentials, degraded modes, what fails when the IdP is down | Design an IdP outage mode for a hospital where clinicians must still work |
| 11.3 Signing-key protection | HSM custody, key separation by audience and tenant, rotation, monitoring for tokens signed by unexpected keys | Write detection logic for "token signed by a key not in the current JWKS" |
| 11.4 Break-glass identity | Accounts outside the federated path, storage, monitoring, testing | Test a break-glass path during a simulated IdP outage |

**Check your understanding:** (1) Why can't revocation rely on short token lifetimes alone? (2) Which systems should keep working during an IdP outage, and how? (3) What would have detected forged tokens earlier in 2023?

### Chapter 12 · Programmes, migrations and AI (weeks 12–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Migrations | Legacy LDAP, Kerberos and custom login to a modern IdP; strangler pattern; dual-running; merging IdPs after acquisitions | Plan a migration of 40 applications with waves and rollback |
| 12.2 Metrics | Phishing-resistant coverage, standing privilege, orphaned identities, time to deprovision, account takeover rate, recovery fraud rate | Define a CIAM and workforce metrics set |
| 12.3 AI in identity work | Drafting policies, analysing access graphs, suggesting role mining; verifying in report-only modes | Have an assistant propose role consolidation and test the effect |
| 12.4 AI failure modes | Deprecated flows (implicit grant), missing `aud` or `iss` checks, invented OAuth parameters, over-broad scopes | Find the flaws in three AI-generated identity designs |

**Check your understanding:** (1) Why do identity migrations fail at the long tail of applications? (2) Which metric best predicts account takeover? (3) Which AI identity error is most dangerous, and how do you catch it?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Trust graph and incident edges | Trust graph |
| 2 | 2 | Assurance level selection | Justified levels |
| 3 | 3 | Lab 2 · e-KYC and DigiLocker design (no AI) | Flow and vault layout; **P1 due** |
| 4 | 4 | Lab 3 · Federation after an acquisition | Federation design |
| 5 | 5 | Lab 4 · OAuth audit and FAPI 2.0 flow | Findings and flow |
| 6 | 6 | Lab 5 · Passkeys and recovery | Rollout and recovery design |
| 7 | 7 | Lab 6 · Rego and Cedar | Tested policies; mid-term (AI off) |
| 8 | 8 | Lab 7 · ReBAC and the new-enemy problem | Fixed race |
| 9 | 9 | Lab 8 · SPIRE and federation | Cross-domain call; **P2 due** |
| 10 | 10 | Lab 9 · Agent identities and MCP review | Review findings |
| 11 | 11 | Lab 10 · CAEP and IdP outage mode | Event flow, outage test |
| 12 | 12 | Migration plan | Wave plan |
| 13 | 12 | AI design audit | Flaw log |
| 14 | 12 | Project work | **P3 due** |
| 15 | Review | Design exam and oral | Final exam |

## Working with AI in this course

- **Use AI for:** explaining RFC sections and UIDAI or DigiLocker specifications; drafting Rego, Cedar and OpenFGA models with tests; generating sequence diagrams of token flows; analysing exported access data for role candidates.
- **Do without AI (drills):** the e-KYC and DigiLocker design (Lab 2); assurance level selection; the new-enemy race analysis; the mid-term and final.
- **Verify AI output by:** checking every flow and parameter against the RFC or specification text; testing policies with deny cases you wrote first; checking claims about UIDAI rules against UIDAI's own circulars and FAQs; capturing real token flows in the lab and comparing them with the AI's diagram.
- **Where AI still fails here (show it):** ask an assistant to design "login for a single-page app" and record whether it proposes the implicit grant or tokens in browser storage, contrary to RFC 9700 and RFC 10017; ask for an MCP server design that calls a third-party API and record whether it forwards the client's token; ask about current Aadhaar storage rules and compare with Circular 14 of 2025.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs 1–10 | 25% |
| Projects P1 / P2 / P3 | 5% / 15% / 25% |
| Mid-term (AI off) | 10% |
| Final: design exam plus oral defence of P3 | 20% |

**Mastery gate.** You pass when you can, without AI and in three hours: (a) design the identity architecture of an unseen organisation (domains, IdPs, federation, token flows, authorization placement, workload and agent identity) with every trust edge justified; (b) find at least four of five planted flaws in a provided token architecture (for example token passthrough, missing audience checks, a shared signing key across tenants, an implicit grant, a recovery path weaker than login); and (c) design an e-KYC integration that meets UIDAI's vault and HSM requirements and keeps no Aadhaar number outside the vault.

## Industry reality

- **Product companies run authorization as a platform:** Google described Zanzibar in 2019, and OpenFGA, SpiceDB, OPA and Cedar are now CNCF projects used by many SaaS firms.
- **Indian regulated entities** integrate Aadhaar e-KYC and DigiLocker under UIDAI and sector rules; the HSM and vault requirements shape their architecture.
- **Financial APIs** worldwide converge on FAPI 2.0-style profiles; consumer apps are moving to passkeys at scale.
- **Agent identity is new architecture work:** vendors ship agent identity products, and the MCP specification now carries detailed authorization and security guidance.

**Interview questions from this course**

1. *"Design sign-in and account recovery for a 50-million-user consumer app in India."* Strong answer: passkeys first with fallback, OTP risks and RBI authentication rules, risk-based step-up, bot and stuffing defences, recovery with re-proofing and help-desk controls, metrics, DPDP consent.
2. *"Design authorization for document sharing like Google Docs."* Strong answer: ReBAC tuples with inheritance, check and list APIs, consistency tokens and the new-enemy problem, caching rules, PEP placement, multi-tenant schema, audit.
3. *"An AI agent needs to read a user's email and calendar through MCP servers. Design the identity flow."* Strong answer: OAuth with per-resource audiences, delegated and down-scoped tokens, no passthrough, consent per client, approval for sending, short lifetimes, logging, revocation.
4. *"We suspect our IdP's token-signing key leaked. What now, and how should the architecture have limited this?"* Strong answer: rotate and revoke, invalidate sessions, hunt for tokens signed by the old key, inform relying parties; HSM custody, key separation by audience and tenant, monitoring for unexpected key IDs.
5. *"Integrate Aadhaar e-KYC and DigiLocker into a lending app."* Strong answer: AUA/KUA or sub-AUA route, HSM for signing and decryption, Aadhaar Data Vault with reference keys, VIDs and masking, DigiLocker OAuth with PKCE, purpose-bound retention and erasure, audit.

## Resources (free first)

- **Standards:** [NIST SP 800-63-4](https://csrc.nist.gov/pubs/sp/800/63/4/final); [OAuth 2.1 draft](https://datatracker.ietf.org/doc/draft-ietf-oauth-v2-1/); RFCs [9700](https://www.rfc-editor.org/rfc/rfc9700), [10017](https://www.rfc-editor.org/info/rfc10017), [9449](https://www.rfc-editor.org/rfc/rfc9449), [8705](https://www.rfc-editor.org/rfc/rfc8705), [8693](https://www.rfc-editor.org/rfc/rfc8693), [9126](https://www.rfc-editor.org/rfc/rfc9126), [9396](https://www.rfc-editor.org/rfc/rfc9396), [9728](https://www.rfc-editor.org/rfc/rfc9728), [8707](https://www.rfc-editor.org/rfc/rfc8707), [7644 (SCIM)](https://www.rfc-editor.org/rfc/rfc7644); [OpenID Connect Core](https://openid.net/specs/openid-connect-core-1_0.html); [FAPI 2.0](https://openid.net/specs/fapi-security-profile-2_0-final.html); [CAEP](https://openid.net/specs/openid-caep-1_0-final.html); [AuthZEN Authorization API 1.0](https://openid.net/specs/authorization-api-1_0.html); [WebAuthn Level 3](https://www.w3.org/TR/webauthn-3/).
- **Authorization and workload identity:** [Zanzibar paper](https://www.usenix.org/conference/atc19/presentation/pang); [OpenFGA](https://openfga.dev/docs); [SpiceDB](https://authzed.com/docs); [OPA](https://www.openpolicyagent.org/docs); [Cedar](https://www.cedarpolicy.com/); [SPIFFE](https://spiffe.io/docs/latest/spiffe-about/overview/); [IETF WIMSE](https://datatracker.ietf.org/wg/wimse/about/).
- **Agents and connectors:** [MCP security best practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices); [OWASP Top 10 for Agentic Applications](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/).
- **India:** [UIDAI Circular 14 of 2025](https://uidai.gov.in/images/Circular-No.14_of-2025.pdf); [UIDAI Aadhaar Data Vault FAQ](https://uidai.gov.in/images/FAQs_Aadhaar_Data_Vault_03112025_v10.pdf); [DigiLocker Authorized Partner API Specification](https://img1.digitallocker.gov.in/assets/img/Digital%20Locker%20Authorized%20Partner%20API%20Specification%20v1.11.pdf); [PIB on DPDP Rules](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2190014).
- **Lab tools:** [Keycloak](https://www.keycloak.org/documentation); [SPIRE](https://spiffe.io/docs/latest/spire-about/).

## Sources

All checked 12 Oct 2026.

- CSRB report on the 2023 Exchange Online intrusion (Mar 2024) — https://www.cisa.gov/sites/default/files/2025-03/CSRBReviewOfTheSummer2023MEOIntrusion508.pdf ; Okta root-cause post (3 Nov 2023) — https://sec.okta.com/articles/2023/11/unauthorized-access-oktas-support-case-management-system-root-cause ; Microsoft on Midnight Blizzard (25 Jan 2024) — https://www.microsoft.com/en-us/security/blog/2024/01/25/midnight-blizzard-guidance-for-responders-on-nation-state-attack/ ; Mandiant on Salesloft Drift (Aug 2025) — https://cloud.google.com/blog/topics/threat-intelligence/data-theft-salesforce-instances-via-salesloft-drift
- OpenID Foundation: AuthZEN Authorization API 1.0 final (approved Jan 2026) — https://openid.net/authorization-api-1-0-final-specification-approved/ ; Shared Signals, CAEP and RISC final — https://openid.net/three-shared-signals-final-specifications-approved/
- NIST SP 800-63-4 (Jul 2025) — https://csrc.nist.gov/pubs/sp/800/63/4/final
- OAuth 2.1 draft-16 (Sep 2026), RFC 10017 (Aug 2026), WebAuthn Level 3 Recommendation (25 Aug 2026), FIDO 5 billion passkeys (7 May 2026), OpenFGA CNCF incubation and Cedar CNCF Sandbox (Oct 2025): as sourced in this curriculum's [BE305](../../../backend_engineering/year_3/BE305_authentication_authorization_and_backend/README.md) — https://datatracker.ietf.org/doc/draft-ietf-oauth-v2-1/ ; https://www.rfc-editor.org/info/rfc10017 ; https://www.w3.org/TR/webauthn-3/ ; https://fidoalliance.org/five-billion-passkeys-a-milestone-not-a-finish-line/ ; https://www.cncf.io/projects/openfga/ ; https://www.cncf.io/projects/cedar/
- UIDAI Circular 14 of 2025 and ADV FAQ (3 Nov 2025) — https://uidai.gov.in/images/Circular-No.14_of-2025.pdf ; https://uidai.gov.in/images/FAQs_Aadhaar_Data_Vault_03112025_v10.pdf
- DigiLocker Authorized Partner API Specification v1.11 (PKCE added in v1.8, 2020) — https://img1.digitallocker.gov.in/assets/img/Digital%20Locker%20Authorized%20Partner%20API%20Specification%20v1.11.pdf
- MCP security best practices (2026-07-28 revision) — https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices
- Microsoft Entra Agent ID (May 2025), as reported by Redmond Magazine — https://redmondmag.com/articles/2025/05/19/microsoft-unveils-future-for-ai-agents-at-build-2025.aspx
- CISA advisory AA23-320A, Scattered Spider (updated Jul 2025) — https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-320a
- RBI authentication directions for digital payments (effective 1 Apr 2026), as summarised by Khaitan & Co — https://khaitanco.com/thought-leadership/RBI-Authentication-Mechanisms-for-Digital-Payments-Transactions-Directions

_Last reviewed: 2026-10_
