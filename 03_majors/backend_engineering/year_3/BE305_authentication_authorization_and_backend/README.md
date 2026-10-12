# BE305 · Authentication, Authorization and Backend Security

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 6 | 4 (≈ 120 hours) | L2 → L3 | [CS211](../../../../02_year_2_core_computer_science/semester_4/CS211_database_systems_internals/README.md), [CS212](../../../../02_year_2_core_computer_science/semester_4/CS212_distributed_systems_i/README.md) | [BE401](../../year_4/BE401_payments_grade_systems_transactions_idempotency/README.md), [BE404](../../year_4/BE404_microservices_service_mesh_and_platform_apis/README.md), [SAR402](../../../security_architecture/year_4/SAR402_identity_architecture_at_scale/README.md), [OV10](../../../../04_overlaps/OV10_fintech_systems_engineering/README.md) |

Part of the [Backend Engineering major](../../README.md). Builds on cryptography and threat basics from [CS213 Security Foundations](../../../../02_year_2_core_computer_science/semester_4/CS213_security_foundations/README.md). This course is **defensive**: you build and review protections in systems you own. Every hands-on exercise runs on your own machine or on legal practice platforms (PortSwigger Web Security Academy, OWASP Juice Shop, OWASP crAPI), never against systems you are not authorized to test.

## Why this course matters now

Broken access control is first on both of OWASP's lists. It leads the OWASP Top 10:2025 for web applications, and broken object-level authorization leads the API Security Top 10 (2023 edition, still current). These are logic bugs: a handler forgets to check that the caller owns the object. Code generators reproduce them easily, and scanners rarely find them. The standards changed recently:
- NIST SP 800-63-4 (July 2025) bans password composition rules and forced periodic rotation.
- WebAuthn Level 3 became a W3C Recommendation in August 2026.
- The OAuth 2.0 Security Best Current Practice became RFC 9700 (January 2025), and the browser-apps guidance became RFC 10017 (August 2026). OAuth 2.1 is still an Internet-Draft.
- India's Digital Personal Data Protection Rules were notified in November 2025 with an 18-month phase-in.

Public post-mortems show what is at stake. The US Cyber Safety Review Board traced the 2023 Microsoft Exchange Online intrusion to a stolen signing key and token-validation failures. Okta traced its 2023 support-system breach to a service-account credential saved in an employee's personal Google account. AI assistants generate login flows and JWT middleware quickly. A backend engineer still has to say which checks are missing, which token belongs where, and what happens when a key leaks.

## Learning outcomes

By the end you can:

1. **Threat-model** an API's authentication and authorization surface and **map** the risks to the OWASP Top 10:2025 and API Security Top 10 (2023).
2. **Implement** password storage, login throttling and account recovery that follow NIST SP 800-63B-4 and OWASP guidance.
3. **Choose** between server-side sessions and tokens for a given set of clients, and **implement** either safely: cookie flags, CSRF defence, rotation and revocation.
4. **Validate** JWTs correctly (algorithm allowlists, issuer, audience, expiry, key IDs, key rotation) and **explain** each pitfall in RFC 8725.
5. **Integrate** OAuth 2.x and OpenID Connect as a client and as a resource server: authorization code with PKCE, the backend-for-frontend pattern, client credentials, token exchange and DPoP.
6. **Add** passkeys (WebAuthn) and step-up authentication, and **explain** where synced passkeys fit in NIST's assurance levels.
7. **Design** authorization with RBAC, ABAC and relationship-based models (Zanzibar, OpenFGA, SpiceDB), with policy engines (OPA, Cedar), and **enforce** object-level checks everywhere.
8. **Give** services short-lived workload identities (mTLS, SPIFFE) and **manage** secrets with rotation and no plaintext in code, logs or images.
9. **Apply** data-protection controls (encryption, minimization, redaction, audit logs) that meet India's DPDP Act and CERT-In reporting obligations.
10. **Review** AI-generated auth code and catch missing checks, unsafe token handling and secrets in the wrong place.

## Chapters and lessons

### Chapter 1 · Threats, identities and trust boundaries (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Authentication vs authorization vs accounting | Identities (users, services, agents), credentials, sessions, permissions, audit | Draw the identity flow of a UPI-style app: user, device, app server, bank |
| 1.2 Threat modeling an API | Trust boundaries, data flows, STRIDE (see SAR302), abuse cases | Threat-model a food-delivery API and rank the top five risks |
| 1.3 The OWASP lists | Top 10:2025 (broken access control first; new: software supply chain failures, mishandling of exceptional conditions) and API Security Top 10 (2023) | Map each finding from your threat model to a list item |
| 1.4 Ethics and law | Authorization before testing, scope, India's IT Act and responsible disclosure; legal practice platforms only | Read a real bug bounty policy and list what is in and out of scope |

**Check your understanding:** (1) Why can't an API gateway alone prevent broken object-level authorization? (2) Which identities in a modern backend are not humans? (3) What makes "fail closed" harder than it sounds in exception handling?

### Chapter 2 · Passwords, accounts and recovery (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Storing passwords | Argon2id, scrypt, bcrypt; work factors; pepper; migrating old hashes on login | Tune Argon2id to about 250 ms on your server; migrate an old hash table on login |
| 2.2 NIST SP 800-63B-4 rules | No composition rules, no periodic forced changes, blocklist checks, length minimums (15 for single-factor, 8 with MFA) | Rewrite a legacy password policy to comply, with a test per rule |
| 2.3 Login abuse | Credential stuffing, throttling by account and IP, breached-password checks, bot signals, safe error messages (no account enumeration) | Add layered throttling; prove responses do not reveal which accounts exist |
| 2.4 Recovery and changes | Reset tokens (single-use, short-lived, hashed at rest), email and phone change flows, session invalidation after a reset | Design a reset flow that survives a stolen email inbox for one hour |

**Check your understanding:** (1) Why should a password hash be slow but a session lookup fast? (2) Why did NIST drop forced periodic password changes? (3) What should happen to existing sessions after a password reset?

### Chapter 3 · Sessions, cookies and tokens (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Server-side sessions | Session IDs, `HttpOnly`, `Secure`, `SameSite`, rotation on login (fixation), idle and absolute timeouts, revocation | Implement sessions in Redis with rotation and per-device revocation |
| 3.2 CSRF and CORS | Why cookies need CSRF defence, `SameSite` limits, CORS as a browser relaxation and not a protection | Show a CSRF defence working and a CORS misconfiguration being caught by a test |
| 3.3 JWTs | Structure, signatures (HS256 vs RS256/ES256/EdDSA), claims; RFC 9068 access-token profile; RFC 8725 pitfalls: unpinned algorithms, unchecked `aud`/`iss`/`exp`, untrusted key IDs, long lifetimes | Write a validator that rejects 12 malformed or mis-scoped tokens from a provided test set |
| 3.4 Opaque tokens and revocation | Reference tokens with introspection, short-lived access plus rotating refresh tokens, reuse detection | Detect refresh-token reuse and revoke the whole token family |
| 3.5 Where tokens live | Browser storage risks, the backend-for-frontend pattern, mobile secure storage | Move a single-page app from `localStorage` tokens to a backend-for-frontend with cookies |

**Check your understanding:** (1) What does a JWT's signature prove, and what does it not prove? (2) Why are long-lived JWTs hard to revoke, and what are the standard mitigations? (3) Why does `SameSite=Lax` not remove the need to think about CSRF?

### Chapter 4 · OAuth 2.x and OpenID Connect (weeks 4–5)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Roles and flows | Resource owner, client, authorization server, resource server; authorization code with PKCE (RFC 7636); public vs confidential clients | Trace a "Sign in with Google" flow in browser dev tools and label each step |
| 4.2 OAuth 2.1 and the security BCP | OAuth 2.1 (draft-16) folds in PKCE everywhere and drops implicit and password grants; RFC 9700 threats and countermeasures; exact redirect URI matching | Audit a provided client configuration against RFC 9700 |
| 4.3 Browser-based apps | RFC 10017 (August 2026): backend-for-frontend, token-mediating backend and browser-only patterns, ranked by risk | Implement the backend-for-frontend pattern with Keycloak or another local identity provider |
| 4.4 Resource servers | Validating access tokens, scopes vs permissions, audience restriction, JWKS caching and key rotation | Build a resource server that survives a key rotation without errors |
| 4.5 Service and delegation flows | Client credentials, token exchange (RFC 8693), Pushed Authorization Requests (RFC 9126), Rich Authorization Requests (RFC 9396), DPoP sender-constrained tokens (RFC 9449) | Bind tokens to a client key with DPoP and show a copied token being rejected |
| 4.6 OpenID Connect | ID tokens vs access tokens, discovery, `nonce`, logout; FAPI 2.0 for high-assurance (financial) APIs | Add OIDC login and explain why an ID token must never be used to call an API |

**Check your understanding:** (1) What attack does PKCE prevent, and why is it now required even for confidential clients? (2) Why is an ID token the wrong credential for an API call? (3) When would you choose DPoP or mTLS-bound tokens over bearer tokens?

### Chapter 5 · Passkeys and multi-factor authentication (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 WebAuthn and FIDO2 | Registration and authentication ceremonies, relying party ID, origin binding, why phishing fails against passkeys | Add passkey registration and login to your app with a maintained library |
| 5.2 Synced vs device-bound passkeys | Account recovery trade-offs; NIST allows syncable authenticators up to AAL2, not AAL3; attestation | Decide which user groups get which authenticator, with reasons |
| 5.3 Other factors | TOTP, push approval fatigue, SMS OTP and SIM-swap risk; RBI's 2025 authentication directions for digital payments (effective April 2026) | Compare four factors on phishing resistance, cost and recovery |
| 5.4 Step-up and risk-based authentication | Re-authentication for sensitive actions, `acr` and `amr` claims, device signals | Require a passkey for changing a payout bank account |

**Check your understanding:** (1) Why can't a fake website collect a usable passkey assertion? (2) What is the hardest part of a passkey rollout, and why is it recovery? (3) Which actions deserve step-up authentication in a banking app?

### Chapter 6 · Authorization models (weeks 7–8)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 RBAC and its limits | Roles, permissions, role explosion, tenant-scoped roles | Model admin, manager and agent roles for a multi-tenant SaaS |
| 6.2 ABAC and policy engines | Attributes of subject, resource and context; OPA (Rego) and Cedar; policy as code with tests | Write and unit-test 10 policies in OPA or Cedar |
| 6.3 ReBAC and Zanzibar | Relation tuples, usersets, check and expand, consistency tokens ("zookies") and the new-enemy problem (Pang et al., 2019) | Model folder and document sharing in OpenFGA or SpiceDB |
| 6.4 Enforcing it everywhere | Object-level checks in every handler, list filtering ("which documents can I see?"), row-level security as a backstop | Find and fix five planted object-level authorization bugs in a lab API |
| 6.5 Authorization for agents | Agents acting for users, scoped and short-lived delegated tokens, per-tool permissions, human approval for irreversible actions | Give an AI support agent read-only scopes plus one approved write path |

**Check your understanding:** (1) Why is "filter the list by permission" harder than "check one object"? (2) What does a Zanzibar consistency token protect against? (3) Where should the authorization decision live when five services touch the same document?

### Chapter 7 · Service identity and zero trust (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Workload identity | mTLS, SPIFFE IDs and SPIRE, cloud workload identity federation, no long-lived keys | Issue SPIFFE identities to two services and enforce mTLS |
| 7.2 Propagating the user | Forwarding tokens vs token exchange, the confused-deputy problem | Fix a confused-deputy bug between two services |
| 7.3 Zero trust in practice | Per-request authentication and authorization between services, network position is not identity (see SAR303) | Remove a "trusted internal network" assumption from a lab system |
| 7.4 Non-human identities | Service accounts, CI tokens and AI agents as principals; inventory, ownership, short-lived credentials, rotation | Inventory every non-human identity in your lab system and replace one standing credential with a short-lived one |

**Check your understanding:** (1) Why is an internal IP address not an identity? (2) When is forwarding the user's token to a downstream service wrong? (3) What does mTLS prove, and what does it not?

### Chapter 8 · Secrets and keys (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Secret lifecycle | Creation, distribution, rotation, revocation; why environment variables leak (crash dumps, debug endpoints) | Inventory every secret in a sample app and its blast radius |
| 8.2 Secret managers | HashiCorp Vault (BSL 1.1 since 2023, IBM-owned since 2025), OpenBao (OpenSSF), cloud secret managers; dynamic database credentials | Issue short-lived Postgres credentials from Vault or OpenBao |
| 8.3 Keys and KMS | Envelope encryption, key hierarchies, signing-key rotation with overlapping validity, hardware-backed keys | Rotate a JWT signing key with zero failed requests |
| 8.4 Leak prevention | Secret scanning and push protection, pre-commit hooks, redaction in logs and traces | Plant a secret in a commit and in a log line; catch both automatically |

**Check your understanding:** (1) What made the Storm-0558 key compromise so damaging, according to the CSRB report? (2) Why are dynamic credentials safer than a well-guarded static password? (3) How do you rotate a signing key without invalidating every live token?

### Chapter 9 · Inputs, injection and server-side request forgery (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Injection defences | Parameterized queries, safe ORM use, output encoding, avoiding shell and template injection | Fix four injection-prone code paths in a lab app and add regression tests |
| 9.2 Deserialization and uploads | Safe parsers, size and type limits, storing uploads outside the web root, scanning | Harden an upload endpoint against oversized and mislabeled files |
| 9.3 SSRF defences | Allowlists, blocking internal ranges and cloud metadata endpoints (IMDSv2), egress proxies; webhook URL registration as a risk | Add SSRF protection to a "fetch this URL" feature and test it with local targets |
| 9.4 Failing safely | Exceptions that skip checks, default-deny, error messages without internals (OWASP A10:2025) | Find an authorization check bypassed by an exception path and fix it |

**Check your understanding:** (1) Why do allowlists beat blocklists for SSRF? (2) How can an unhandled exception become an authorization bypass? (3) What should a 500 response never contain?

### Chapter 10 · Data protection and compliance for engineers (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Encryption choices | TLS everywhere, encryption at rest, field-level encryption, tokenization, searchable fields | Encrypt PAN-like and Aadhaar-like fields at the field level with key rotation |
| 10.2 Minimization and redaction | Collect less, retain less; PII in logs and traces; masking in support tools | Add automatic PII redaction to logs and prove it with tests |
| 10.3 India's DPDP Act and Rules | Consent, purpose limitation, data principal rights, breach notification, penalties up to ₹250 crore; Rules notified 14 November 2025 with phased compliance over 18 months | Build a data-export and erasure flow for one user |
| 10.4 Audit and incident duties | Tamper-evident audit logs; CERT-In's 2022 directions (report incidents within 6 hours, keep logs for 180 days) | Design an audit log that meets those directions |

**Check your understanding:** (1) Why is field-level encryption sometimes worth its cost when disk encryption already exists? (2) What makes erasure hard in backups and event logs? (3) What must your logging pipeline guarantee to meet a 6-hour reporting window?

### Chapter 11 · Security in delivery, and lessons from incidents (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 ASVS as requirements | OWASP ASVS 5.0 (May 2025) levels; turning requirements into tests | Pick 25 ASVS requirements for your P3 and automate checks for them |
| 11.2 Pipeline controls | SAST, dependency scanning (supply chain is A03:2025), secret scanning, DAST against a staging build | Add three scanners to CI and triage their findings |
| 11.3 Case studies (defensive) | CSRB on Storm-0558 (key management, token validation), Okta 2023 (service-account credential hygiene), Optus 2022 (ACMA alleged that a coding error left an API's access controls ineffective) | For each, write the control that would have prevented or detected it |
| 11.4 Identity incident response | Detecting token misuse, revoking sessions and refresh tokens at scale, emergency key rotation, CERT-In reporting | Run a tabletop exercise for a leaked signing key against a 6-hour reporting clock |

**Check your understanding:** (1) Which of the three case studies would code review most likely have caught, and why? (2) Why do scanners rarely find object-level authorization bugs? (3) What is the smallest set of controls that would have limited the Okta incident?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Threat model | Ranked risks mapped to OWASP lists |
| 2 | 2 | Lab 1: passwords and throttling | NIST-compliant policy with tests |
| 3 | 3 | Lab 2: sessions and JWT validation (no AI) | Validator rejecting all 12 bad tokens |
| 4 | 4 | Lab 3: OAuth and OIDC (part 1) | Authorization-code flow with PKCE; P1 due |
| 5 | 4 | Lab 3 (part 2) | Backend-for-frontend, key rotation, DPoP |
| 6 | 5 | Lab 4: passkeys and step-up | Passkey login and a step-up flow |
| 7 | 6 | Lab 5: policies | OPA or Cedar policy tests; P2 starts |
| 8 | 6 | Lab 6: ReBAC and object-level checks | Sharing model; 5 fixed authorization bugs |
| 9 | 7 | Lab 7: workload identity | mTLS with SPIFFE identities |
| 10 | 8 | Lab 8: secrets | Dynamic DB credentials; zero-downtime key rotation; P2 due |
| 11 | 9 | Lab 9: inputs and SSRF | Hardened endpoints with regression tests |
| 12 | 10 | Data protection | Redaction, field encryption, export and erasure; P3 design review |
| 13 | 11 | ASVS and CI | Automated checks and triaged findings |
| 14 | — | P3 integration | P3 demo and security review |
| 15 | Review and exam | — | Written exam and live code-review exam |

## Working with AI in this course

- **Use AI for:** explaining specification sections (RFC 9700, RFC 10017, WebAuthn); generating test cases for validators and policies; drafting OPA or Cedar policies that you then test; summarizing scanner output; producing threat-model checklists to compare against your own.
- **Do without AI (drills):** the JWT validator (Lab 2); threat-modeling a new API; spotting object-level authorization gaps in a code review; drawing OAuth flows from memory with every parameter; the live code-review exam.
- **Verify AI output by:** running a negative test suite (expired, wrong audience, wrong issuer, wrong algorithm, unknown key ID, replayed tokens); writing one authorization test per endpoint per role, including "another tenant's object"; checking every generated flow against the RFC text, not a blog post; running secret scanners over generated code and configuration.
- **Where AI still fails here (show it yourself):** ask an assistant for "JWT authentication middleware" and check whether it pins the algorithm and validates `aud` and `iss`. Ask for a CRUD endpoint "with authentication" and check whether it verifies that the caller owns the record. Ask for an OAuth login in a single-page app and check where it stores tokens, comparing with RFC 10017. Ask for a password policy and compare it with NIST SP 800-63B-4. Record every gap with the test that exposed it.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs 1–9 | 30% |
| Projects P1 / P2 / P3 | 5% / 12% / 18% |
| Written exam (flows, token validation, authorization models, standards) | 20% |
| Live code-review exam (find planted flaws, no AI) | 15% |

**Mastery gate:** you pass when you can, without AI help, (a) find at least 5 of 6 planted flaws in an unfamiliar service within 60 minutes: an object-level authorization gap, a JWT validation gap, a secret in the wrong place, a CSRF hole, an account-enumeration leak and a fail-open exception path; (b) draw and explain authorization code with PKCE and the backend-for-frontend pattern, parameter by parameter; and (c) rotate the signing key of your P3 system under load with zero failed requests.

## Industry reality

- **Standards in late 2026:** OAuth 2.1 is draft-16 (an active Internet-Draft); RFC 9700 (January 2025) is the OAuth security best current practice; RFC 10017 (August 2026) covers browser-based apps; FAPI 2.0 has been final since February 2025; WebAuthn Level 3 has been a W3C Recommendation since August 2026; NIST SP 800-63-4 has been final since July 2025.
- **Passkeys:** the FIDO Alliance said over 15 billion user accounts could use a passkey (April 2025) and estimated about 5 billion passkeys in active use (May 2026). These count different things and should not be compared.
- **Authorization infrastructure:** Google's Zanzibar paper (2019) inspired OpenFGA (CNCF incubating since October 2025) and SpiceDB. OPA is a CNCF graduated project, and AWS's Cedar joined the CNCF Sandbox in October 2025.
- **Secrets:** HashiCorp moved its products to the Business Source License in August 2023, and IBM completed its acquisition of HashiCorp in February 2025. OpenBao continues an open-source fork under the OpenSSF.
- **India:** the DPDP Rules were notified on 14 November 2025 with phased compliance over 18 months. CERT-In requires incidents to be reported within 6 hours and logs to be kept for 180 days (April 2022 directions).

Interview questions from this course:

1. **"Sessions or JWTs for a product with a web app and a mobile app?"** A strong answer covers revocation, token lifetime, storage on each client, CSRF vs token theft, the backend-for-frontend pattern for the web, refresh-token rotation for mobile, and the cost of a session store.
2. **"Walk me through authorization code with PKCE. Why PKCE?"** Cover each redirect and parameter (`state`, `code_challenge`, `code_verifier`, `redirect_uri`), the code-interception attack PKCE prevents, and exact redirect matching.
3. **"Design permissions for document sharing like Google Docs."** Cover ReBAC with relation tuples, inherited permissions from folders, list filtering, consistency tokens and the new-enemy problem, caching decisions, and auditing.
4. **"How do you store passwords and stop credential stuffing?"** Cover Argon2id parameters, NIST rules, breached-password checks, layered throttling, safe error messages, MFA and passkeys, and monitoring.
5. **"Your JWT signing key has leaked. What do you do in the first hour?"** Cover rotating to a new key ID and revoking trust in the old key, short token lifetimes, forcing re-authentication, finding the leak's source, auditing what was issued, the lessons from the CSRB Storm-0558 report, and CERT-In reporting duties in India.

## Resources (free first)

- **OWASP:** [Top 10:2025](https://top10.owasp.org/2025); [API Security Top 10 (2023)](https://owasp.org/API-Security/editions/2023/en/0x11-t10/); [ASVS](https://owasp.org/www-project-application-security-verification-standard/); Cheat Sheets on [authentication](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html), [password storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html), [session management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html), [OAuth 2.0](https://cheatsheetseries.owasp.org/cheatsheets/OAuth2_Cheat_Sheet.html) and [SSRF prevention](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html).
- **Standards:** [NIST SP 800-63B-4](https://pages.nist.gov/800-63-4/sp800-63b.html); [OAuth 2.1 draft](https://datatracker.ietf.org/doc/draft-ietf-oauth-v2-1/) and [oauth.net/2.1](https://oauth.net/2.1/); RFCs [9700](https://www.rfc-editor.org/rfc/rfc9700), [10017](https://www.rfc-editor.org/rfc/rfc10017), [7636](https://www.rfc-editor.org/rfc/rfc7636), [8725](https://www.rfc-editor.org/rfc/rfc8725), [9068](https://www.rfc-editor.org/rfc/rfc9068), [9449](https://www.rfc-editor.org/rfc/rfc9449), [8693](https://www.rfc-editor.org/rfc/rfc8693), [9126](https://www.rfc-editor.org/rfc/rfc9126); [OpenID Connect Core](https://openid.net/specs/openid-connect-core-1_0.html); [FAPI 2.0 Security Profile](https://openid.net/specs/fapi-security-profile-2_0-final.html); [WebAuthn Level 3](https://www.w3.org/TR/webauthn-3/) and [passkeys.dev](https://passkeys.dev/).
- **Authorization:** [Zanzibar paper](https://www.usenix.org/conference/atc19/presentation/pang); [OpenFGA docs](https://openfga.dev/docs); [SpiceDB docs](https://authzed.com/docs); [OPA docs](https://www.openpolicyagent.org/docs); [Cedar](https://www.cedarpolicy.com/).
- **Identity and secrets:** [SPIFFE](https://spiffe.io/docs/latest/spiffe-about/overview/); [OpenBao](https://openbao.org/); [Vault docs](https://developer.hashicorp.com/vault/docs); GitHub [push protection](https://docs.github.com/en/code-security/secret-scanning/introduction/about-push-protection).
- **Legal practice:** [PortSwigger Web Security Academy](https://portswigger.net/web-security) (authentication, OAuth, JWT, access-control topics); [OWASP Juice Shop](https://owasp.org/www-project-juice-shop/); [OWASP crAPI](https://owasp.org/www-project-crapi/).
- **Paid, worth it:** Neil Madden, *API Security in Action* (Manning, 2020); Justin Richer and Antonio Sanso, *OAuth 2 in Action* (Manning, 2017).

## Sources

All checked 12 Oct 2026.

- OWASP Top 10:2025: https://top10.owasp.org/2025 (released Nov 2025, per The Register, 11 Nov 2025: https://www.theregister.com/2025/11/11/new_owasp_top_ten_broken/); OWASP API Security Top 10, 2023 edition: https://owasp.org/API-Security/editions/2023/en/0x11-t10/ ; ASVS 5.0.0 (30 May 2025): https://github.com/OWASP/ASVS/releases/tag/v5.0.0_release
- NIST SP 800-63-4 (Jul 2025): https://csrc.nist.gov/pubs/sp/800/63/4/final
- IETF: OAuth 2.1 draft-16 (Sep 2026): https://datatracker.ietf.org/doc/draft-ietf-oauth-v2-1/ ; RFC 9700 (Jan 2025); RFC 10017 (Aug 2026): https://www.rfc-editor.org/info/rfc10017 ; RFC 8725bis status: https://datatracker.ietf.org/doc/draft-ietf-oauth-rfc8725bis/
- FAPI 2.0 Security Profile final (22 Feb 2025): https://openid.net/specs/fapi-security-profile-2_0-final.html ; WebAuthn Level 3 Recommendation (25 Aug 2026): https://www.w3.org/TR/webauthn-3/
- FIDO Alliance, 15 billion accounts (9 Apr 2025): https://fidoalliance.org/fido-alliance-launches-the-passkey-pledge-to-further-accelerate-global-movement-away-from-passwords/ ; 5 billion passkeys (7 May 2026): https://fidoalliance.org/five-billion-passkeys-a-milestone-not-a-finish-line/
- CNCF project pages: OpenFGA https://www.cncf.io/projects/openfga/ ; Cedar https://www.cncf.io/projects/cedar/ ; OPA https://www.cncf.io/projects/open-policy-agent-opa/
- HashiCorp BSL (10 Aug 2023): https://www.hashicorp.com/en/blog/hashicorp-adopts-business-source-license ; IBM completes HashiCorp acquisition (27 Feb 2025): https://newsroom.ibm.com/2025-02-27-IBM-Completes-Acquisition-of-HashiCorp,-Creates-Comprehensive,-End-to-End-Hybrid-Cloud-Platform
- DPDP Rules 2025 (notified 14 Nov 2025; PIB explainer, 17 Nov 2025): https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/nov/doc20251117695301.pdf ; CERT-In directions (28 Apr 2022): https://www.cert-in.org.in/PDF/CERT-In_Directions_70B_28.04.2022.pdf
- RBI authentication directions for digital payments (Sep 2025; effective 1 Apr 2026), as summarized by Khaitan & Co: https://khaitanco.com/thought-leadership/RBI-Authentication-Mechanisms-for-Digital-Payments-Transactions-Directions
- CSRB, Review of the Summer 2023 Microsoft Exchange Online Intrusion (20 Mar 2024): https://www.cisa.gov/sites/default/files/2025-03/CSRBReviewOfTheSummer2023MEOIntrusion508.pdf ; Okta root-cause post (3 Nov 2023): https://sec.okta.com/articles/2023/11/unauthorized-access-oktas-support-case-management-system-root-cause ; Optus allegations by ACMA (CSO Online, 21 Jun 2024): https://www.csoonline.com/article/2492520/optus-breach-occurred-due-to-a-coding-error-alleges-acma.html

_Last reviewed: 2026-10_
