# CS213 · Security Foundations

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 2 · 4 | 4 (≈ 120 hours) | L1 → L3 | [CS203](../../semester_3/CS203_operating_systems/README.md), [CS204](../../semester_3/CS204_computer_networks/README.md) | [SEC301](../../../03_majors/cybersecurity_defense/year_3/SEC301_network_security_and_defense/README.md), [SEC303](../../../03_majors/cybersecurity_defense/year_3/SEC303_identity_and_access_management/README.md), [OFF301](../../../03_majors/ethical_hacking_offensive_security/year_3/OFF301_ethics_law_rules_of_engagement_and_methodology/README.md), [SAR302](../../../03_majors/security_architecture/year_3/SAR302_threat_modeling/README.md), [BE305](../../../03_majors/backend_engineering/year_3/BE305_authentication_authorization_and_backend/README.md), [PRO301](../../../05_shared_years_3_to_5/PRO301_professional_practice_ethics_law_and_responsible/README.md) |

Part of [Year 2 · Core Computer Science](../../README.md). This course is **defensive and conceptual**. Hands-on practice happens only in legal training environments (PortSwigger Web Security Academy, OWASP Juice Shop run on your own machine, CryptoHack, picoCTF) and on systems you own. Testing anything else without written authorization is a crime in India under the IT Act, 2000 and in most other countries.

## Why this course matters now

Every engineer now ships security decisions, whether they know it or not. The OWASP Top 10:2025 added **Software Supply Chain Failures** (A03) and **Mishandling of Exceptional Conditions** (A10). In March 2025 a compromised GitHub Action (`tj-actions/changed-files`, CVE-2025-30066) leaked CI secrets, including access keys, into the build logs of workflows that ran it. Memory safety is shifting the field too: Google reported that memory-safety bugs fell from 76% of Android vulnerabilities in 2019 to 24% in 2024 as new code moved to memory-safe languages. AI cuts both ways:

- **AI as a source of flaws:** in Veracode's July 2025 study, LLMs given 80 coding tasks chose the insecure implementation in 45% of cases. Code-generating models also recommend packages that do not exist (a USENIX Security 2025 study).
- **AI as a defender:** in DARPA's AI Cyber Challenge final (August 2025), finalist systems found 86% of the 63 planted vulnerabilities and patched 68% (DARPA's corrected count).

In India, CERT-In requires many incidents to be reported within 6 hours. The DPDP Rules notified in November 2025 make breach notification a legal duty, with penalties up to ₹250 crore for failing to keep reasonable security safeguards. Someone has to understand all of this well enough to make the right call.

## Learning outcomes

By the end you can:

1. **Threat-model** a system with data-flow diagrams and STRIDE, and **rank** risks by likelihood and impact.
2. **Choose and use** cryptographic primitives correctly: AEAD encryption, hashing, MACs, KDFs, password hashing and signatures. You can also **explain** why each misuse breaks security.
3. **Explain** the TLS 1.3 handshake and PKI, and **configure** a server that scores well on public TLS tests.
4. **Implement** authentication that follows NIST SP 800-63B-4 (passkeys, MFA, session management) and authorization that denies by default.
5. **Explain** each OWASP Top 10:2025 category by root cause and defense, and **find and fix** them in legal practice labs.
6. **Use** sanitizers, fuzzers, SAST, SCA and SBOMs, and **triage** their findings into true and false positives.
7. **Respond** to a simulated incident: build a timeline, contain it, and draft the CERT-In report and the DPDP breach notice.
8. **Explain** what Indian and international law permit, and **work** only within written scope.

## Chapters and lessons

### Chapter 1 · Security thinking (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Goals | Confidentiality, integrity, availability; authenticity, accountability, privacy | Classify ten real incidents by which goal failed |
| 1.2 Risk vocabulary | Assets, threats, vulnerabilities, exploits, controls, residual risk; attacker economics | Write a risk statement for a UPI app's PIN-entry screen |
| 1.3 Design principles | Saltzer and Schroeder (1975): least privilege, fail-safe defaults, complete mediation, economy of mechanism, open design, separation of privilege, psychological acceptability | Find which principle each of five design flaws violates |
| 1.4 Ethics and authorization | Scope, rules of engagement, responsible disclosure, bug bounty terms; why "I was just testing" is no defense | Read one public bug bounty policy and list what is out of scope |

**Check your understanding:** (1) Why is "open design" not the same as "publish your secrets"? (2) Give a case where availability and confidentiality pull in opposite directions. (3) Why does complete mediation conflict with caching?

### Chapter 2 · Threat modeling (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 The four questions | What are we working on? What can go wrong? What will we do about it? Did we do a good job? (Threat Modeling Manifesto) | Run the four questions on a college attendance app |
| 2.2 Data-flow diagrams | Processes, data stores, external entities, trust boundaries | Draw the DFD of a document-wallet app inspired by DigiLocker (illustrative) |
| 2.3 STRIDE and attack trees | Spoofing, tampering, repudiation, information disclosure, denial of service, elevation of privilege; attack trees for one goal | Produce 15 threats with STRIDE labels for the DFD |
| 2.4 Privacy threats and adversary vocabulary | LINDDUN for privacy; MITRE ATT&CK as a shared defender vocabulary | Map three threats to ATT&CK tactics and name the detection you would want |

**Check your understanding:** (1) Why do most serious threats sit on trust boundaries? (2) What does repudiation threaten, and which control answers it? (3) When should a threat model be updated?

### Chapter 3 · Cryptography I: symmetric primitives (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Ground rules | Kerckhoffs's principle, security levels, why you never design your own cipher | Explain 128-bit security in terms of work factor |
| 3.2 Authenticated encryption | AES-GCM, ChaCha20-Poly1305, nonces and why reuse is catastrophic, associated data | Encrypt files with libsodium or Python `cryptography`, and write a test that rejects a tampered file |
| 3.3 Hashes, MACs and KDFs | SHA-2 and SHA-3, length extension (conceptually), HMAC, HKDF | Verify webhook signatures with HMAC and constant-time comparison |
| 3.4 Password hashing and randomness | Argon2id (RFC 9106), scrypt, bcrypt; salts, peppers, cost tuning; CSPRNGs | Tune Argon2id so one hash costs about 250 ms on your server, and justify the parameters |

**Check your understanding:** (1) Why does encryption without authentication fail even if the cipher is strong? (2) Why is SHA-256 a bad password hash but a good file checksum? (3) What property does constant-time comparison protect?

### Chapter 4 · Cryptography II: public keys, TLS and the post-quantum shift (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Key exchange and signatures | Diffie–Hellman, X25519, Ed25519, RSA in outline; signing vs encrypting | Sign and verify a release file with Ed25519 |
| 4.2 PKI | Certificates, chains, CAs, revocation, Certificate Transparency, Let's Encrypt and ACME | Inspect a certificate chain of an Indian bank's site and list each field's purpose |
| 4.3 TLS 1.3 | 1-RTT handshake, ECDHE, forward secrecy, what TLS does not hide (RFC 8446) | Configure TLS on your own server, test with SSL Labs, add HSTS (RFC 6797) |
| 4.4 Post-quantum cryptography | FIPS 203 (ML-KEM), FIPS 204 (ML-DSA), FIPS 205 (SLH-DSA), August 2024; harvest-now-decrypt-later; hybrid key exchange | Write an inventory of where a small company uses public-key crypto and which items to migrate first |

**Check your understanding:** (1) What does forward secrecy protect against, and what does it not? (2) Why does a browser trust a certificate it has never seen? (3) Why migrate key exchange to post-quantum before signatures?

### Chapter 5 · Authentication (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Passwords done right | NIST SP 800-63B-4 (July 2025): length over composition rules, blocklists of breached passwords, no forced periodic changes, rate limiting | Implement a breached-password check with the Pwned Passwords k-anonymity range API |
| 5.2 MFA and phishing resistance | SMS and TOTP vs push vs FIDO2; why phishing-resistant factors matter; authenticator assurance levels | Rank five MFA options for a brokerage app and justify the ranking |
| 5.3 Passkeys | WebAuthn Level 3, public-key credentials, syncable passkeys | Add passkey sign-in to a demo app |
| 5.4 Sessions and tokens | Cookies (`Secure`, `HttpOnly`, `SameSite`), session fixation, JWT pitfalls, OAuth 2.0 and OpenID Connect; OAuth Security BCP (RFC 9700, January 2025) | Review a JWT-based login and list three design flaws |

**Check your understanding:** (1) Why are passkeys resistant to phishing sites when TOTP codes are not? (2) What does `SameSite=Lax` stop, and what does it not? (3) Why should account recovery be treated as an authentication path?

### Chapter 6 · Authorization and access control (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Models | DAC, MAC, RBAC, ABAC, relationship-based access (Zanzibar-style) | Model a hospital records app in RBAC, then in ABAC; compare |
| 6.2 Broken access control | Object-level checks (IDOR), function-level checks, multi-tenant isolation; OWASP A01:2025 | PortSwigger access-control labs; write the server-side fix for each |
| 6.3 Policy as code | Central policy engines (Open Policy Agent, Cedar), deny-by-default, testable policies | Write and unit-test ten policies for a document-sharing app |
| 6.4 Least privilege in practice | Database roles, PostgreSQL row-level security, service accounts, short-lived credentials | Enforce tenant isolation with row-level security and prove it with tests |

**Check your understanding:** (1) Why is hiding a button not access control? (2) Why should authorization live in one place? (3) What does a cross-tenant test suite need to cover?

### Chapter 7 · Web application security (weeks 7–8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 The OWASP Top 10:2025 | A01 Broken Access Control to A10 Mishandling of Exceptional Conditions; what changed since 2021 and why | Map 20 real CVE summaries to categories |
| 7.2 Injection as a class | Untrusted data interpreted as code: SQL, OS command, template injection; defenses: parameterized queries, safe APIs, allow-lists (A05) | PortSwigger SQL-injection labs, then rewrite the vulnerable code with parameterized queries |
| 7.3 Browser security model | Same-origin policy, CORS, cross-site scripting as an output-encoding failure, CSRF; defenses: contextual encoding, Content Security Policy Level 3, `SameSite`, anti-CSRF tokens | Deploy a strict CSP on a demo app and fix what it breaks |
| 7.4 Server-side request forgery and misconfiguration | Why servers fetching URLs is dangerous; allow-lists, network egress control, cloud metadata hardening; insecure defaults (A02) | Harden a URL-preview feature and document each control |
| 7.5 Verification standards | OWASP ASVS 5.0 levels, Cheat Sheet Series, security headers | Assess a demo app against 30 ASVS requirements |
| 7.6 Juice Shop practice | Run OWASP Juice Shop locally; for each challenge solved, write root cause, fix and regression test | Ten challenges with fix notes |

**Check your understanding:** (1) Why do parameterized queries fix SQL injection while input "sanitizing" often fails? (2) Why is CORS not a protection for the server? (3) Why did "exceptional conditions" earn its own category in 2025?

### Chapter 8 · Memory safety and secure coding (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Memory-safety bug classes | Out-of-bounds access, use-after-free, double free, integer overflow, type confusion (concepts, not exploitation) | Classify ten CWE Top 25 entries as memory-safety or not |
| 8.2 Mitigations | Stack canaries, ASLR, non-executable memory, control-flow integrity; why mitigations are not fixes | Explain which mitigation raises cost for which bug class |
| 8.3 Finding bugs early | AddressSanitizer, UndefinedBehaviorSanitizer, libFuzzer, OSS-Fuzz | Fuzz a small C parser, fix every crash ASan reports |
| 8.4 Memory-safe languages | Rust ownership, Go and Java safety; Android's results; CISA/NSA memory-safe roadmap guidance | Rewrite the fuzzed parser in Rust and rerun the fuzzer |
| 8.5 Secure coding habits | Input validation, safe error handling, secrets out of code, logging without sensitive data | Review a pull request with a checklist and file three findings |

**Check your understanding:** (1) Why did Android's memory-safety share fall without rewriting old C++ code? (2) Why does a fuzzer find bugs that unit tests miss? (3) What should an error message tell a user, and what must it never reveal?

### Chapter 9 · Supply chain and pipeline security (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Dependencies as attack surface | Transitive dependencies, typosquatting, hallucinated package names, OSV vulnerability data | Generate an SBOM (CycloneDX or SPDX) and scan it with OSV-Scanner |
| 9.2 CI/CD as a target | The March 2025 `tj-actions/changed-files` compromise; pinning actions to commit SHAs; least-privilege tokens; OIDC instead of long-lived secrets | Harden a GitHub Actions workflow and document each change |
| 9.3 Provenance and signing | SLSA levels, Sigstore signing and verification | Sign a container image and verify it before deploy |
| 9.4 Static and dynamic analysis | Semgrep, CodeQL, OWASP ZAP baseline scans on your own app; triage, false positives, risk acceptance | Triage 20 SAST findings into true and false positives with reasons |

**Check your understanding:** (1) Why does pinning to a tag not stop a compromised action? (2) What does an SBOM let you do on the day a new CVE is announced? (3) When is accepting a SAST finding as a risk the right call?

### Chapter 10 · Network and system security (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Network controls | Segmentation, firewalls, VPNs (WireGuard), bastions, egress filtering | Design network zones for a three-tier app and write the firewall rules |
| 10.2 Zero trust | NIST SP 800-207: per-request authentication and authorization, device posture, no implicit trust from location | Rewrite a VPN-based access design as zero trust |
| 10.3 Host hardening | Patching, minimal services, SSH keys only, `sudo` policy, file permissions, CIS-style baselines | Harden a fresh Linux VM and verify with a checklist script |
| 10.4 Logging and detection basics | What to log, clock synchronization, centralization, alerting; OWASP A09:2025 | Build a log pipeline that flags repeated failed logins |

**Check your understanding:** (1) Why is "inside the VPN" a weak trust signal? (2) Why does CERT-In require clocks synced to NIC or NPL time sources? (3) What makes an alert actionable?

### Chapter 11 · Incident response, law and ethics (weeks 12–13)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Incident response lifecycle | NIST SP 800-61 Rev. 3 (April 2025) aligned with CSF 2.0: prepare, detect, respond, recover; evidence handling | Tabletop: a leaked cloud key in a public repository |
| 11.2 India's IT Act, 2000 | Sections 43 and 66 (unauthorized access and damage), 72A (disclosure in breach of contract), 70B (CERT-In); section 43A is omitted by the DPDP Act once its section 44(2) commences | Explain which sections apply to three described scenarios |
| 11.3 CERT-In Directions (28 April 2022) | Report listed incidents within 6 hours; keep ICT logs for 180 days within India; sync clocks to NIC or NPL NTP servers | Draft a 6-hour incident report for the tabletop |
| 11.4 DPDP Act 2023 and Rules 2025 | Duties of Data Fiduciaries, reasonable security safeguards, breach notice to the Board and each affected person; rules notified in November 2025 with an 18-month phased timeline, so most duties apply from May 2027; penalties up to ₹250 crore | Draft a plain-language breach notice for affected users |
| 11.5 Global context and ethics | GDPR breach notification in outline, coordinated disclosure, ethics of dual-use knowledge | Write your personal rules of engagement |

**Check your understanding:** (1) Why preserve evidence before "cleaning up"? (2) Which two clocks start when a breach is discovered at an Indian company, and how do they differ? (3) Why does authorization need to be written, not verbal?

### Chapter 12 · Security in the AI era (week 14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Risks of LLM applications | OWASP Top 10 for LLM Applications 2025: prompt injection (LLM01), sensitive information disclosure, improper output handling, excessive agency, system prompt leakage | Threat-model a support chatbot that can issue refunds |
| 12.2 Securing agents and tools | Treat model output as untrusted input; least-privilege tools; human approval for irreversible actions; sandboxing | Redesign the refund bot so prompt injection cannot move money |
| 12.3 AI-written code | Insecure defaults, hallucinated dependencies; review and test as for any untrusted contributor | Generate a login handler with an assistant and review it against ASVS |
| 12.4 AI for defenders | Autofix in code scanning, AI-assisted vulnerability discovery (Big Sleep, AIxCC), triage assistants; their limits | Compare an AI triage of 20 findings with your manual triage from Chapter 9 |

**Check your understanding:** (1) Why is prompt injection hard to solve with better prompts? (2) What is "excessive agency" in plain words? (3) What evidence would convince you an AI-suggested fix is correct?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Kick-off: incident classification | Risk statements |
| 2 | 2 | Lab 1: threat model | DFD and STRIDE table; P1 starts |
| 3 | 3 | Lab 2: authenticated encryption | Tamper-rejecting file tool |
| 4 | 4 | Lab 3: TLS and signing | SSL Labs report, signed release; P1 due |
| 5 | 5 | Lab 4: auth basics | Breached-password check, passkey sign-in |
| 6 | 6 | Lab 5: access control | Row-level security tests; P2 starts |
| 7 | 7 | Lab 6: PortSwigger | Labs completed with fix notes |
| 8 | 7 | Lab 7: Juice Shop and ASVS | Fix notes and ASVS sheet |
| 9 | 8 | Lab 8: fuzzing | Crash fixes, Rust port |
| 10 | 9 | Lab 9: supply chain | SBOM, hardened workflow, signed image; P2 due |
| 11 | 10 | Host and network hardening | Checklist script; P3 design review |
| 12 | 11 | Lab 10: incident tabletop | Timeline and 6-hour report |
| 13 | 11 | Law workshop | Breach notice, rules of engagement |
| 14 | 12 | Agent threat model | P3 demo |
| 15 | Review and exam | — | Written exam and design review oral |

## Working with AI in this course

- **Use AI for:** explaining CVE advisories and RFC sections; drafting threat models that you then critique against the DFD; writing security unit tests and regression tests; first-pass triage of scanner output; drafting incident reports and plain-language breach notices for review.
- **Do without AI (drills):** STRIDE on a whiteboard; choosing primitives and parameters for a stated need; hand review of authentication and authorization code; manual triage of scanner findings; drafting the 6-hour CERT-In report under time pressure.
- **Verify AI output by:** checking cryptographic advice against NIST publications, RFCs and the OWASP Cheat Sheet Series; proving every fix with a regression test and a re-run of the relevant legal practice lab; checking every suggested package name exists and is the one you meant (on the registry and on OSV) before installing; never accepting "this is secure" without a stated threat and control.
- **Where AI still fails here:** in Veracode's 2025 study, models chose the insecure option in 45% of security-relevant tasks. Hallucinated package names averaged at least 5.2% for commercial models and 21.7% for open-source models. Prompt injection is still the top LLM application risk in OWASP's 2025 list, and there is no known complete fix.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs 1–10 (with fix notes and evidence) | 30% |
| Projects P1 / P2 / P3 | 5% / 15% / 20% |
| Written exam (crypto choices, threat models, law scenarios) | 20% |
| Design review oral (defend P3's threat model) | 10% |

**Mastery gate:** you pass when you can, without AI help and in one sitting of three hours, (a) threat-model an unseen two-service application and identify its three highest risks with controls; (b) review 300 lines of authentication and authorization code, find the planted flaws (at least four of five) and write correct fixes; and (c) given an incident scenario, produce a timeline, containment steps, a CERT-In report draft and a DPDP breach notice that meet the legal requirements in this course.

## Industry reality

Security work spans product engineering (secure design, code review), cloud and identity, security operations, and governance. Examples from this course's sources:

- **Google:** credits safe coding and memory-safe languages for the Android improvement.
- **NIST:** SP 800-63B-4 recognizes syncable passkeys.
- **CISA:** issued an alert on the `tj-actions` compromise telling users to treat exposed secrets as compromised and rotate them.
- **India:** CERT-In's 6-hour rule and the DPDP penalties mean breach handling is a board-level and legal concern, not only a technical one.

Interview questions from this course:

1. **"How should we store passwords?"** Cover Argon2id, scrypt or bcrypt with per-user salts and tuned cost; why fast hashes fail; peppers; rehash-on-login migration; breached-password checks; and moving users towards passkeys.
2. **"What does TLS 1.3 protect, and what doesn't it?"** Cover ECDHE key exchange, certificate validation, forward secrecy and 1-RTT. Then the limits: compromised endpoints, metadata, and server-side trust decisions.
3. **"How do you prevent broken access control in a multi-tenant API?"** Cover object-level checks on every request, deny-by-default central policy, tenant IDs taken from the session and not from input, row-level security, cross-tenant test suites, and logging of denials.
4. **"A third-party CI action you use was compromised. What do you do?"** Cover scoping the exposure window, rotating every secret the workflow could read, reviewing logs, pinning by SHA, moving to OIDC short-lived credentials, and legal reporting checks (CERT-In timelines, DPDP if personal data was affected).
5. **"How would you secure an LLM feature that can call tools?"** Cover prompt injection as an unsolved problem, model output treated as untrusted, least-privilege tools, confirmation for irreversible actions, output encoding, rate limits and audit logs, mapped to the OWASP LLM Top 10.

## Resources (free first)

- **Courses:**
  - [Stanford CS155](https://cs155.stanford.edu/)
  - [Berkeley CS161](https://cs161.org/) and its [free textbook](https://textbook.cs161.org/)
  - [MIT 6.5660](https://css.csail.mit.edu/6.5660/)
  - NPTEL [Foundations of Cryptography](https://nptel.ac.in/courses/106106221) (Prof. Ashish Choudhury, IIIT Bangalore)
- **Books:** Boneh and Shoup, [A Graduate Course in Applied Cryptography](https://toc.cryptobook.us/); Ross Anderson, [Security Engineering, 3rd edition](https://www.cl.cam.ac.uk/archive/rja14/book.html) (chapters free); Saltzer and Schroeder, [The Protection of Information in Computer Systems](https://web.mit.edu/Saltzer/www/publications/protection/).
- **Standards and guides:**
  - [OWASP Top 10:2025](https://top10.owasp.org/2025)
  - [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/)
  - [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/)
  - [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/)
  - [CWE Top 25](https://cwe.mitre.org/top25/)
  - [NIST SP 800-63B-4](https://csrc.nist.gov/pubs/sp/800/63/b/4/final)
  - [NIST CSF 2.0](https://www.nist.gov/cyberframework)
  - [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final)
  - [NIST SP 800-207](https://csrc.nist.gov/pubs/sp/800/207/final)
  - [FIPS 203](https://csrc.nist.gov/pubs/fips/203/final)
  - [RFC 8446](https://www.rfc-editor.org/rfc/rfc8446), [RFC 9700](https://www.rfc-editor.org/rfc/rfc9700), [RFC 9106](https://www.rfc-editor.org/rfc/rfc9106)
  - [WebAuthn Level 3](https://www.w3.org/TR/webauthn-3/), [CSP Level 3](https://www.w3.org/TR/CSP3/)
  - [Threat Modeling Manifesto](https://www.threatmodelingmanifesto.org/), [LINDDUN](https://www.linddun.org/), [MITRE ATT&CK](https://attack.mitre.org/)
- **Law (India):**
  - [IT Act, 2000 (MeitY)](https://www.meity.gov.in/content/information-technology-act-2000)
  - [CERT-In Directions, 28 April 2022](https://www.cert-in.org.in/PDF/CERT-In_Directions_70B_28.04.2022.pdf)
  - [DPDP Act, 2023 (Gazette text)](https://www.meity.gov.in/static/uploads/2024/06/2bf1f0e9f04e6fb4f8fef35e82c42aa5.pdf)
  - [PIB: DPDP Rules notified](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2190014)
- **Legal practice environments:** [PortSwigger Web Security Academy](https://portswigger.net/web-security), [OWASP Juice Shop](https://owasp.org/www-project-juice-shop/), [CryptoHack](https://cryptohack.org/), [picoCTF](https://picoctf.org/), [OverTheWire](https://overthewire.org/wargames/), [pwn.college](https://pwn.college/), [TryHackMe](https://tryhackme.com/).
- **Tools:** [libsodium](https://doc.libsodium.org/), [pyca/cryptography](https://cryptography.io/), [Semgrep](https://semgrep.dev/docs/), [CodeQL](https://codeql.github.com/docs/), [OWASP ZAP](https://www.zaproxy.org/), [OSV-Scanner](https://github.com/google/osv-scanner), [Sigstore](https://www.sigstore.dev/), [AddressSanitizer](https://clang.llvm.org/docs/AddressSanitizer.html), [libFuzzer](https://llvm.org/docs/LibFuzzer.html), [Open Policy Agent](https://www.openpolicyagent.org/).

## Sources

All checked 12 Oct 2026.
- [OWASP Top 10:2025 list](https://top10.owasp.org/2025) (first published November 2025).
- [CISA alert on tj-actions/changed-files (CVE-2025-30066)](https://www.cisa.gov/news-events/alerts/2025/03/18/supply-chain-compromise-third-party-tj-actionschanged-files-cve-2025-30066-and-reviewdogaction) (18 Mar 2025).
- [Google Security Blog: Eliminating memory safety vulnerabilities at the source](https://security.googleblog.com/2024/09/eliminating-memory-safety-vulnerabilities-Android.html) (25 Sep 2024): 76% (2019) to 24% (2024).
- [Veracode 2025 GenAI Code Security Report press release](https://www.veracode.com/press-release/ai-generated-code-poses-major-security-risks-in-nearly-half-of-all-development-tasks-veracode-research-reveals/) (30 Jul 2025).
- [We Have a Package for You! (USENIX Security 2025)](https://arxiv.org/abs/2406.10279): package hallucination rates.
- [DARPA AIxCC results](https://www.darpa.mil/news/2025/aixcc-results) (Aug 2025; corrected count checked Oct 2026): 54 of 63 synthetic vulnerabilities found (86%), 43 patched (68%).
- [Google Project Zero: From Naptime to Big Sleep](https://googleprojectzero.blogspot.com/2024/10/from-naptime-to-big-sleep.html) (2024).
- [NIST SP 800-63B-4 final](https://csrc.nist.gov/pubs/sp/800/63/b/4/final) (31 Jul 2025).
- [CERT-In Directions under section 70B(6)](https://www.cert-in.org.in/PDF/CERT-In_Directions_70B_28.04.2022.pdf) (28 Apr 2022): 6-hour reporting, 180-day logs within India, NIC/NPL time sync.
- [DPDP Act 2023 Gazette](https://www.meity.gov.in/static/uploads/2024/06/2bf1f0e9f04e6fb4f8fef35e82c42aa5.pdf): section 8(6) breach intimation; section 44(2) omits IT Act section 43A; Schedule penalties up to ₹250 crore (security safeguards) and ₹200 crore (breach notice).
- [PIB, 14 Nov 2025](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2190014): DPDP Rules notified with an 18-month phased compliance timeline.
- [GitHub Actions security hardening guide](https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions): pinning actions to full-length commit SHAs.
- [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/llm-top-10/).

_Last reviewed: 2026-10_
