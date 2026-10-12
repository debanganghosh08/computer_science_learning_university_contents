# CS213 · Labs and projects

Every lab and project in this course runs on systems you own, on local copies of deliberately vulnerable training apps, or on training platforms that invite practice (PortSwigger Web Security Academy, OWASP Juice Shop, CryptoHack). Never point tools at anything else. Each finding you report must include the **root cause, the fix, and a regression test** that proves the fix. Finding a problem is only half the work.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Threat model | DFD and STRIDE for a document-wallet app inspired by DigiLocker (illustrative) | DFD with trust boundaries; 15+ threats with likelihood, impact and controls | 4 h |
| 2 · Authenticated encryption | A file-encryption tool using AEAD (libsodium or pyca/cryptography), with keys derived from a passphrase by Argon2id | Code, plus tests showing that tampered ciphertext, a wrong key and a truncated file are all rejected | 4 h |
| 3 · TLS and signing | TLS 1.3 on your own server with HSTS; Ed25519-signed release files | SSL Labs report for your domain (or a local scanner report), plus a signature verification script | 4 h |
| 4 · Authentication basics | Argon2id password storage, a breached-password check via the Pwned Passwords k-anonymity API, TOTP, and passkey sign-in | Working demo, tests, and a note on what never leaves the server | 6 h |
| 5 · Access control | Policies in Open Policy Agent or Cedar, plus PostgreSQL row-level security for tenant isolation | Policy unit tests and a cross-tenant test suite with every denial passing | 5 h |
| 6 · Web Security Academy | At least 15 apprentice-level PortSwigger labs across access control, SQL injection, XSS, CSRF and SSRF | For each lab: the vulnerable pattern in one sentence and the server-side fix in code | 8 h |
| 7 · Juice Shop and ASVS | Ten Juice Shop challenges on your local instance; an ASVS 5.0 Level 1 check of 30 requirements | Root cause, fix and regression-test notes; an ASVS sheet with evidence | 6 h |
| 8 · Fuzzing and memory safety | Fuzz a provided C parser with libFuzzer under AddressSanitizer and UBSan, fix every crash, then port it to Rust and fuzz again | Crash list with fixes, coverage numbers, and the Rust port | 6 h |
| 9 · Supply chain | SBOM (CycloneDX or SPDX), OSV-Scanner, Dependabot, GitHub Actions pinned to commit SHAs, OIDC to a cloud account, and a container image signed and verified with Sigstore | Hardened workflow diff and a verification log | 5 h |
| 10 · Incident tabletop | A simulated leaked-cloud-key incident with provided logs | Timeline, containment plan, a CERT-In report draft completed within a simulated 6-hour clock, and a DPDP breach notice for users | 4 h |

## Projects

### P1 · Threat model and security review of an open-source app (L1, ~6 hours)

**Real-world inspiration:** the [Threat Modeling Manifesto](https://www.threatmodelingmanifesto.org/) and the [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/), which teams use to turn security into testable requirements.

**What to build:** choose a self-hosted open-source web app (a wiki, a to-do app or a URL shortener) and run it **on your own machine**. Produce a threat model and a design-and-configuration review based on reading code, documentation and configuration.

**Acceptance criteria:**
- A DFD that marks every trust boundary, including third-party services and admin interfaces.
- At least 15 threats with STRIDE labels, likelihood × impact scores and proposed controls.
- The top 5 risks mapped to OWASP Top 10:2025 categories and specific ASVS 5.0 requirement IDs.
- Three concrete hardening recommendations, each with a configuration or code change you tested locally.
- If you believe you found a real vulnerability, you follow the project's `SECURITY.md` or private disclosure process and never open a public issue first. The write-up records this decision.

**Stretch goals:** a LINDDUN privacy pass; an accepted upstream pull request that hardens a default.

**What it proves to an employer:** you can reason about risk systematically and write findings that engineers act on, which is the daily work of product security teams.

### P2 · Authentication service to NIST SP 800-63B-4 (L2, ~15 hours)

**Real-world inspiration:** NIST SP 800-63B-4 (July 2025) recognizes syncable passkeys. The [FIDO Alliance](https://fidoalliance.org/passkeys/) and platform vendors are moving users from passwords to passkeys. A brokerage or payments app needing strong, phishing-resistant sign-in is the *illustrative scenario*.

**What to build:** a standalone sign-in service with:
- passkeys (WebAuthn) as the primary method;
- an Argon2id-hashed password with TOTP as a second factor for users without passkeys;
- breached-password screening and rate limiting;
- secure sessions and an account-recovery flow;
- an audit log.

**Acceptance criteria:**
- **Passwords:** length, blocklist and rate-limiting rules each cite the SP 800-63B-4 clause they implement. Argon2id parameters are benchmarked to at least 200 ms per hash on the deployment machine.
- **Breached passwords:** screening rejects passwords from a provided breached list, and only hash prefixes leave the server (k-anonymity).
- **Sessions:** cookies are `Secure`, `HttpOnly` and `SameSite`. The session ID rotates at login. Idle and absolute timeouts are enforced. Logout invalidates the session server-side. Each is proven by a test.
- **Passkeys:** registration and sign-in work in two different browsers.
- **Recovery:** cannot be weaker than the strongest factor on the account. Document the threat this blocks.
- **ASVS:** the ASVS 5.0 authentication and session-management requirements are each marked pass, fail or not applicable, with evidence and a test reference.
- **Scanning and logs:** an OWASP ZAP baseline scan of **your own** deployment shows no high-risk alerts. An automated test proves logs never contain passwords, OTPs or session tokens.

**Stretch goals:** expose the service as an OpenID Connect provider for a second app; step-up authentication for sensitive actions; device-bound session signals.

**What it proves to an employer:** you can own the most attacked component of any product and show evidence that it meets a recognized standard.

### P3 · Secure-by-design document vault with a DevSecOps pipeline and incident runbook (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** document wallets such as DigiLocker show the shape of the problem: citizens store and share sensitive documents with organizations. This project is an *illustrative* system, not a copy of any real one. Its legal frame is real: the DPDP Act's security-safeguard and breach-notice duties ([Gazette text](https://www.meity.gov.in/static/uploads/2024/06/2bf1f0e9f04e6fb4f8fef35e82c42aa5.pdf)) and CERT-In's 6-hour reporting rule ([Directions](https://www.cert-in.org.in/PDF/CERT-In_Directions_70B_28.04.2022.pdf)).

**What to build:** a web service where users upload documents and share them through scoped, expiring, revocable links. It needs:
- relationship-based authorization;
- envelope encryption, with a data key per document wrapped by a key-encryption key (cloud KMS free tier or a local emulation);
- a tamper-evident audit log built as a hash chain;
- data minimization and retention rules;
- a CI pipeline with SAST (Semgrep or CodeQL), SCA (OSV-Scanner), secret scanning, SBOM generation, SHA-pinned actions and signed images verified at deploy;
- a threat model;
- an incident runbook.

**Acceptance criteria:**
- **Authorization:** a test matrix of at least 60 cases (cross-user, expired link, revoked share, wrong organization, privilege change mid-session) where every expected denial is enforced.
- **Key rotation:** rotating the key-encryption key causes no downtime and old documents still decrypt. A test proves plaintext data keys are never persisted.
- **Audit log:** editing, deleting or reordering any entry is detected by the verifier.
- **Pipeline gates:** the pipeline fails on a planted critical dependency vulnerability and on a planted hard-coded secret. Unsigned images are refused at deploy.
- **Release findings:** the release has zero high or critical SAST or SCA findings, or a written, dated risk acceptance for each one left.
- **Peer review:** another learner reviews **your** deployment under a written scope document you both sign. You fix or formally accept every finding and publish the before-and-after.
- **Tabletop:** run against a leaked-credential scenario, it produces a timeline, a CERT-In report draft within a simulated 6-hour window, and a plain-language DPDP breach notice.

**Stretch goals:** passkey sign-in from P2; per-organization keys; a LINDDUN privacy review; endpoints for users to export and erase their data.

**What it proves to an employer:** end-to-end security ownership covering design, code, pipeline, compliance and response. That is the overlap of application security, cloud security and governance that security teams hire for, and the peer-review evidence shows you can work under authorization and scope like a professional.

## Feeds into

- [SEC301](../../../03_majors/cybersecurity_defense/year_3/SEC301_network_security_and_defense/README.md), [SEC302](../../../03_majors/cybersecurity_defense/year_3/SEC302_security_operations_soc_siem_and_monitoring/README.md), [SEC303](../../../03_majors/cybersecurity_defense/year_3/SEC303_identity_and_access_management/README.md) and [SEC305](../../../03_majors/cybersecurity_defense/year_3/SEC305_governance_risk_and_compliance/README.md): network defense, SOC work, identity, and governance.
- [OFF301 Ethics, Law, Rules of Engagement and Methodology](../../../03_majors/ethical_hacking_offensive_security/year_3/OFF301_ethics_law_rules_of_engagement_and_methodology/README.md) and [OFF302 Web Application Security Testing](../../../03_majors/ethical_hacking_offensive_security/year_3/OFF302_web_application_security_testing/README.md): authorized testing builds on Chapters 1, 7 and 11.
- [SAR302 Threat Modeling](../../../03_majors/security_architecture/year_3/SAR302_threat_modeling/README.md), [SAR304 Applied Cryptography and PKI](../../../03_majors/security_architecture/year_3/SAR304_applied_cryptography_and_pki_for_architects/README.md) and [SAR305 Secure SDLC and DevSecOps](../../../03_majors/security_architecture/year_3/SAR305_secure_sdlc_and_devsecops_architecture/README.md).
- [BE305 Authentication, Authorization and Backend Security](../../../03_majors/backend_engineering/year_3/BE305_authentication_authorization_and_backend/README.md): P2 is the starting point.
- Overlaps: [OV03A Software Supply Chain Security](../../../04_overlaps/OV03_devsecops/OV03A_software_supply_chain_security/README.md), [OV05A Securing LLM Applications and Agents](../../../04_overlaps/OV05_ai_security_safety/OV05A_securing_llm_applications_and_agents/README.md), [OV07B Data Protection Law for Engineers](../../../04_overlaps/OV07_privacy_engineering/OV07B_data_protection_law_for_engineers_in_practice/README.md).
- [PRO301 Professional Practice: Ethics, Law and Responsible AI](../../../05_shared_years_3_to_5/PRO301_professional_practice_ethics_law_and_responsible/README.md).
