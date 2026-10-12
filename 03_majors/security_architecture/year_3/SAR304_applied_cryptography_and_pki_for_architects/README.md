# SAR304 · Applied Cryptography and PKI for Architects

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 6 | 4 (≈ 120 hours) | L2 → L4 | [CS213](../../../../02_year_2_core_computer_science/semester_4/CS213_security_foundations/README.md), [CS212](../../../../02_year_2_core_computer_science/semester_4/CS212_distributed_systems_i/README.md) | [SAR404](../../year_4/SAR404_resilience_business_continuity_and_security/README.md), [SAR401](../../year_4/SAR401_cloud_security_architecture/README.md), [SAR501](../../year_5/SAR501_frontier_seminar_post_quantum_migration/README.md) |

Part of the [Security Architecture major](../../README.md). Taken alongside [SAR305 Secure SDLC and DevSecOps Architecture](../SAR305_secure_sdlc_and_devsecops_architecture/README.md). CS213 Chapters 3–4 taught how primitives, TLS and PKI work. This course is about the decisions an architect owns: which primitive, which key custody, which certificate hierarchy, how rotation and revocation work at scale, and how an organisation moves to post-quantum cryptography without breaking itself. You never design ciphers here; you design systems that use vetted ones correctly.

## Why this course matters now

Most cryptographic failures in production are key-management and lifecycle failures, not broken algorithms. The 2023 Exchange Online intrusion began with a stolen signing key that should not have been valid where it was used ([CSRB](https://www.cisa.gov/sites/default/files/2025-03/CSRBReviewOfTheSummer2023MEOIntrusion508.pdf)). Three shifts make this work urgent:

- **Post-quantum migration has started.** NIST published FIPS 203 (ML-KEM), FIPS 204 (ML-DSA) and FIPS 205 (SLH-DSA) in August 2024, selected HQC as a backup KEM in 2025, and its draft transition plan (NIST IR 8547) says quantum-vulnerable algorithms will be deprecated and removed by 2035 ([NIST](https://csrc.nist.gov/projects/post-quantum-cryptography)). India's Department of Science and Technology published a task-force report on a quantum-safe ecosystem in February 2026, urging critical sectors to begin formal implementation by 2027 ([DST](https://dst.gov.in/sites/default/files/Report_TaskForce_PQMigration_4Feb26%20%28v1%29.pdf)).
- **Certificates are getting short-lived.** Under CA/Browser Forum Ballot SC-081v3, the maximum lifetime of public TLS certificates fell to 200 days on 15 March 2026 and falls to 100 days in March 2027 and 47 days in March 2029 ([DNSimple summary](https://support.dnsimple.com/articles/announcement-ssl-certificate-validity-changes/)). Manual renewal stops being possible.
- **AI writes crypto code.** In Veracode's 2025 study, models chose the insecure option in 45% of security-relevant tasks (see [CS213](../../../../02_year_2_core_computer_science/semester_4/CS213_security_foundations/README.md)). AI also helps build cryptographic inventories quickly.

What still needs an architect is the judgement about custody, blast radius, agility and sequencing, written down so that others can implement it.

## Learning outcomes

By the end you can:

1. **Choose** primitives, modes and parameters for stated requirements (including FIPS 140-3 constraints), and **write** the choice as an ADR with its failure conditions.
2. **Design** a key hierarchy and lifecycle following NIST SP 800-57, and **choose** between HSM, cloud KMS, external key stores and software keys with explicit trade-offs.
3. **Implement** envelope encryption with encryption context, data-key caching limits, rotation and crypto-shredding.
4. **Architect** secrets management so that most services hold no long-lived secret at all.
5. **Design** TLS 1.3 and mTLS deployments, including termination points, 0-RTT policy and internal service certificates.
6. **Build** a private PKI with an offline root and automated issuance, and **operate** certificate lifecycles that survive 47-day validity.
7. **Plan** a post-quantum migration: inventory (CBOM), prioritisation by data lifetime, hybrid key exchange, signature strategy and crypto agility.
8. **Audit** AI-generated cryptographic code and configuration with test vectors and static analysis, and **show** its typical errors.

## Chapters and lessons

### Chapter 1 · What architects decide about cryptography (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Decide, never invent | Kerckhoffs's principle; vetted libraries (libsodium, Google Tink, AWS Encryption SDK, pyca/cryptography); misuse-resistant APIs | Rank five libraries by misuse resistance for one language |
| 1.2 Crypto threat models | Algorithm break vs key compromise vs implementation bug vs operational error; which one each control answers | Classify ten public crypto failures by type |
| 1.3 Security levels | 128-bit and 256-bit targets, key sizes, what "112-bit" means in NIST transition documents | Convert six key sizes into security levels |
| 1.4 Crypto decisions as ADRs | Recording primitive, library, parameters, key custody, rotation and the trigger to revisit | Write ADRs for two encryption decisions in an illustrative telemedicine app |

**Check your understanding:** (1) Why do most crypto incidents not involve breaking an algorithm? (2) What makes an API misuse-resistant? (3) What should trigger revisiting a crypto ADR?

### Chapter 2 · Choosing primitives (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Authenticated encryption | AES-GCM and its nonce and data limits, AES-GCM-SIV for nonce-misuse resistance, ChaCha20-Poly1305; associated data | Calculate when random 96-bit nonces become unsafe for a given message volume |
| 2.2 Hashes, MACs and KDFs | SHA-2, SHA-3, HMAC, HKDF; domain separation | Design key derivation for three subkeys from one master secret |
| 2.3 Signatures and key agreement | Ed25519, ECDSA (nonce risks), RSA-PSS; X25519 and ECDH P-256 | Choose a signature scheme for firmware, JWTs and release artefacts and justify each |
| 2.4 Compliance constraints | FIPS 140-3 validated modules, NIST SP 800-131A transitions; Indian sector rules that reference them | Decide which systems in a bank need validated modules |
| 2.5 Randomness | OS CSPRNGs, entropy at boot in VMs and containers, why userland RNGs fail | Review three code samples for randomness errors |

**Check your understanding:** (1) Why is AES-GCM with a repeated nonce catastrophic for both confidentiality and integrity? (2) When is a FIPS-validated module required, and what does validation not guarantee? (3) Why does ECDSA need more care than Ed25519?

### Chapter 3 · Key management architecture (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 The lifecycle | NIST SP 800-57 Part 1 Rev. 5: generation, distribution, storage, use, rotation, suspension, revocation, archival, destruction; cryptoperiods | Write cryptoperiods for six key types with reasons |
| 3.2 Hierarchies and separation | Root, key-encryption and data keys; separation of duties; dual control; key ceremonies | Design a key ceremony for an offline root |
| 3.3 Custody options | HSMs (FIPS 140-3 levels), cloud KMS (AWS KMS, Google Cloud KMS, Azure Key Vault and Managed HSM), bring-your-own-key, external key stores | Compare four custody models for a payment tokenizer on cost, latency, control and failure |
| 3.4 Regulated custody in India | UIDAI's requirement that Aadhaar authentication signing and e-KYC decryption keys stay in an HSM (Circular 14 of 2025) | Design HSM placement for an e-KYC service following the UIDAI FAQ |
| 3.5 Key compromise | Detecting misuse, revoking, re-keying, re-signing; the Exchange Online signing-key lessons | Write a key-compromise runbook for a token-signing key |

**Check your understanding:** (1) What does an HSM protect against that a KMS policy does not? (2) Why should signing keys for different trust domains never be interchangeable? (3) What is the hardest step of recovering from a root-key compromise?

### Chapter 4 · Envelope encryption and data protection at scale (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Envelope encryption | Data encryption keys wrapped by key-encryption keys; why it scales; encryption context as authenticated metadata | Implement envelope encryption with a cloud KMS or a local KMS emulator |
| 4.2 Caching and blast radius | Data-key caching for cost and latency vs exposure; per-tenant keys | Measure KMS calls and latency with and without caching |
| 4.3 Rotation | Rotating KEKs without re-encrypting data; re-encryption jobs when required | Rotate a KEK and prove old data still decrypts |
| 4.4 Crypto-shredding | Deleting keys to make data unrecoverable; erasure duties under India's DPDP Act; backups and replicas | Design per-user keys that make erasure provable |
| 4.5 Field-level and client-side encryption | When to encrypt in the application; tokenization vs encryption; the limits of searchable encryption | Encrypt PAN-like fields with deterministic tokens for lookup and randomised encryption for storage |

**Check your understanding:** (1) What does encryption context prevent? (2) When is per-tenant keying worth its cost? (3) Why might crypto-shredding fail to erase data?

### Chapter 5 · Secrets management (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Secrets vs keys | API keys, passwords, tokens and certificates; the "secret zero" problem | Inventory every secret in a sample application |
| 5.2 Secret stores | HashiCorp Vault and OpenBao (dynamic secrets, leases), cloud secret managers, SOPS for files, Kubernetes secrets with etcd encryption and external secret operators | Issue 15-minute database credentials from a vault |
| 5.3 Removing secrets | Workload identity federation, managed identities, SPIFFE; what still needs a secret | Remove three static secrets from a deployment |
| 5.4 Secrets in CI/CD | The tj-actions (March 2025) and npm Shai-Hulud (September 2025) compromises harvested CI and developer secrets; scoping, short lifetimes, OIDC | Redesign a pipeline so a compromised step can steal nothing long-lived |
| 5.5 Detection and rotation | Secret scanning and push protection; rotation runbooks that are actually rehearsed | Rotate every secret of a demo app in under 30 minutes |

**Check your understanding:** (1) What is the minimum secret a workload must hold, and how do you protect it? (2) Why did CISA tell users of a compromised CI action to rotate secrets even without evidence of misuse? (3) What makes a rotation runbook trustworthy?

### Chapter 6 · TLS 1.3 design (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 The protocol for designers | TLS 1.3 re-specified as RFC 9846 (July 2026); handshake, key schedule, resumption, cipher suites | Annotate a captured handshake against the RFC |
| 6.2 0-RTT | Replay risk and which requests may use early data | Write a 0-RTT policy for a payments API |
| 6.3 Termination points | Edge, load balancer, sidecar or application; re-encryption; what each placement exposes | Choose termination for a three-tier app and an API gateway |
| 6.4 mTLS for services | Client certificates, identity in SANs (SPIFFE IDs), authorization after authentication | Configure mTLS between two services and reject an unknown client |
| 6.5 Configuration baselines | Mozilla server-side TLS profiles, HSTS, Encrypted Client Hello status | Score your own server with public testers and fix findings |

**Check your understanding:** (1) Why is 0-RTT unsafe for non-idempotent requests? (2) What does terminating TLS at the edge cost you in trust? (3) Why is mTLS authentication without authorization incomplete?

### Chapter 7 · PKI architecture (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Hierarchies | Offline root, issuing CAs, name constraints, path length, cross-signing | Design a three-tier private PKI for a company with two clouds |
| 7.2 Private CA options | AWS Private CA, Google Certificate Authority Service, Smallstep step-ca, EJBCA; cost and operational load | Stand up step-ca with an offline root in the lab |
| 7.3 Revocation reality | CRLs, OCSP and their failure modes; short-lived certificates as the practical answer | Compare revocation latency for three designs |
| 7.4 Transparency | Certificate Transparency (RFC 9162) logs; monitoring issuance for your domains | Set up CT monitoring for a domain you own |
| 7.5 India's PKI | The Controller of Certifying Authorities, the Root Certifying Authority of India, licensed CAs and eSign under the IT Act, 2000 | Draw the trust chain for an Aadhaar-based eSign signature |

**Check your understanding:** (1) Why keep the root offline if issuing CAs do all the work? (2) Why does revocation fail open in many clients? (3) What does CT detect, and what does it not prevent?

### Chapter 8 · Certificate lifecycle automation (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Shrinking lifetimes | SC-081v3 schedule (200, 100, then 47 days) and shorter domain-validation reuse | Calculate renewals per year for an estate of 5,000 certificates under each phase |
| 8.2 ACME | RFC 8555, challenge types, ACME Renewal Information (RFC 9773) | Automate issuance and renewal with ACME for two services |
| 8.3 Kubernetes and services | cert-manager, SPIFFE SVIDs with hour-scale lifetimes | Issue certificates to workloads with cert-manager and rotate them |
| 8.4 Inventory and outage prevention | Discovering certificates, owners, expiry alerts, failure drills | Find and fix five certificates nobody owns in a provided inventory |

**Check your understanding:** (1) Why do short lifetimes improve security even without revocation? (2) What breaks first when lifetimes drop to 47 days? (3) What should an expiry alert contain?

### Chapter 9 · Signing: code, tokens and artefacts (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Release and code signing | Key custody for signing, timestamping, Sigstore keyless signing (Fulcio, Rekor) | Sign and verify a container image with keyless signing |
| 9.2 Token signing | JWKS, key IDs, rotation overlap, audience and issuer separation | Rotate a token-signing key with zero failed validations |
| 9.3 Firmware and devices | Secure boot chains, update signing, device identity keys | Design the signing chain for an IoT device fleet (illustrative) |
| 9.4 Signing key compromise | Revoking trust, re-signing, transparency logs as evidence | Tabletop: your release-signing key leaked |

**Check your understanding:** (1) What does keyless signing replace, and what new trust does it add? (2) Why must rotation keep old and new keys valid for a while? (3) Why is a timestamp important for long-lived signatures?

### Chapter 10 · Post-quantum cryptography (weeks 10–11)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 The threat | Shor's algorithm and public-key crypto; Grover and symmetric keys; harvest now, decrypt later; Mosca's inequality (data lifetime + migration time vs time to a relevant quantum computer) | Apply Mosca's inequality to five data types in a bank |
| 10.2 The standards | FIPS 203 ML-KEM, FIPS 204 ML-DSA, FIPS 205 SLH-DSA; HQC as backup KEM; FN-DSA (Falcon) still being standardised; SP 800-227 KEM guidance (September 2025) | Compare key, ciphertext and signature sizes with classical equivalents |
| 10.3 Hybrid key exchange | X25519MLKEM768 in TLS; support in Chrome, OpenSSL 3.5 and OpenSSH 10.0; middlebox and packet-size issues | Enable hybrid key exchange on a lab server and capture the handshake |
| 10.4 Signatures and certificates | Why PQ certificates are harder (size, chains, constrained devices); stateful hash-based signatures for firmware | Estimate handshake size growth with ML-DSA certificate chains |
| 10.5 Timelines | NIST IR 8547 draft (deprecation and removal by 2035), NSA CNSA 2.0, UK NCSC milestones (2028, 2031, 2035), the EU roadmap (high-risk by 2030), India's DST task force report (2026) | Build a timeline table for an Indian bank with EU customers |

**Check your understanding:** (1) Why migrate key exchange before signatures? (2) Why use hybrid rather than pure PQ key exchange today? (3) Which systems have the least time under Mosca's inequality?

### Chapter 11 · Crypto inventory and agility (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Inventory | Discovering crypto in code, binaries, protocols, certificates, HSMs and third parties | Scan a sample codebase and a host for algorithms in use |
| 11.2 CBOM | Cryptographic bills of materials (CycloneDX); CERT-In's 2025 BOM guidelines covering SBOM, CBOM, QBOM, AIBOM and HBOM | Produce a CBOM for one service |
| 11.3 Agility patterns | Algorithm identifiers in data formats, negotiation, crypto behind interfaces, configuration not code; NIST CSWP 39 on crypto agility | Refactor a service so its signature algorithm changes by configuration |
| 11.4 Prioritisation | Data lifetime, exposure, replaceability, vendor dependency | Rank 20 inventory items for migration |

**Check your understanding:** (1) Why is the inventory the hardest part of PQC migration? (2) What does a version field in a ciphertext format buy you? (3) Where does agility create new risks (downgrade)?

### Chapter 12 · Crypto in AI-era systems, and AI for crypto work (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Protecting AI assets | Model weights under KMS-wrapped keys; embeddings are personal data when derived from it; signing models (OpenSSF model signing) | Design key custody for a fine-tuned model and its vector store |
| 12.2 AI-generated crypto code | Typical errors: static or reused IVs, ECB mode, unauthenticated encryption, outdated parameters, home-made key derivation | Review five AI-generated snippets and classify each error |
| 12.3 Verification | Known-answer and edge-case vectors (Project Wycheproof), Semgrep and CodeQL crypto rules, property tests | Run Wycheproof vectors against a wrapper library |
| 12.4 AI for inventories | Using assistants to read configs and code at scale for CBOM drafts; checking their misses | Compare an AI-drafted CBOM with your scan results |

**Check your understanding:** (1) Why are embeddings not safely "anonymous"? (2) Which crypto bugs do unit tests that encrypt-then-decrypt never catch? (3) How do you measure what an AI inventory missed?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Library comparison (in class) | Two crypto ADRs |
| 2 | 2 | Lab 1 · Primitive selection and nonce budgets (no AI) | Selection table |
| 3 | 3 | Lab 2 · Key ceremony and custody comparison | Ceremony script; **P1 due** |
| 4 | 4 | Lab 3 · Envelope encryption with rotation | Working code and measurements |
| 5 | 5 | Lab 4 · Dynamic secrets and pipeline redesign | Secret-free deployment |
| 6 | 6 | Lab 5 · TLS and mTLS | Scored configurations |
| 7 | 7 | Lab 6 · Private PKI with offline root | PKI and CT monitor; mid-term (AI off) |
| 8 | 8 | Lab 7 · ACME and cert-manager automation | Renewal evidence |
| 9 | 9 | Lab 8 · Signing and key rotation | Zero-failure rotation; **P2 due** |
| 10 | 10 | Lab 9 · Hybrid post-quantum key exchange | Handshake capture and sizes |
| 11 | 10 | PQ timeline workshop | Timeline table |
| 12 | 11 | Lab 10 · CBOM and agility (part 1) | CBOM |
| 13 | 12 | Lab 10 (part 2) · AI crypto code review | Error classification |
| 14 | 12 | Project work | **P3 due** |
| 15 | Review | Oral defence and exam | Final exam |

## Working with AI in this course

- **Use AI for:** explaining RFC and NIST sections; drafting envelope-encryption and rotation code that you test against vectors; generating cert-manager and ACME configuration; summarising vendor KMS documentation into comparison tables; drafting CBOM entries from configuration files.
- **Do without AI (drills):** primitive and parameter selection (Lab 2); nonce-budget calculations; key-ceremony design; Mosca's inequality analysis; the mid-term and final.
- **Verify AI output by:** running known-answer and Wycheproof vectors; checking parameters against NIST SP 800-57, SP 800-131A and FIPS documents; checking that code uses an AEAD with unique nonces and authenticates associated data; reading every library call's documentation; testing rotation and failure paths, not just the happy path.
- **Where AI still fails here (show it):** ask two assistants for "encrypt a file with AES in Python" and record IV handling, mode and authentication; ask for a "post-quantum TLS configuration" and check algorithm names against the current IETF draft and your OpenSSL version; ask for FIPS 206 status and compare with NIST's site. Keep the error log; it is part of Lab 10.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs 1–10 | 25% |
| Projects P1 / P2 / P3 | 5% / 15% / 25% |
| Mid-term (AI off): primitives, keys, PKI | 10% |
| Final: design exam plus oral defence of P3 | 20% |

**Mastery gate.** You pass when you can, without AI and in three hours: (a) design encryption, key custody and rotation for an unseen multi-tenant system with a key hierarchy diagram and cryptoperiods; (b) find at least four of five planted errors in a provided crypto design (for example a shared signing key across domains, nonce reuse risk, missing encryption context, revocation that fails open, a secret in CI); and (c) produce a prioritised PQC migration plan for that system with stated assumptions and timelines.

## Industry reality

- Browsers and major libraries already negotiate hybrid post-quantum key exchange by default (Chrome since 2024; OpenSSL 3.5 and OpenSSH 10.0 in April 2025), so many organisations are partly migrated without knowing it, and their middleboxes must cope.
- Regulators are setting dates: the UK NCSC (2028 discovery, 2031 priority migrations, 2035 completion), the EU roadmap (high-risk systems by 2030) and India's DST task force report.
- UIDAI requires HSM custody for Aadhaar authentication keys, and India's CCA runs the root of the national digital-signature PKI.
- Certificate automation is now mandatory engineering because of the 47-day schedule.

**Interview questions from this course**

1. *"Design encryption for a multi-tenant SaaS that stores personal data, including tenant offboarding."* Strong answer: envelope encryption with per-tenant KEKs, encryption context with tenant ID, caching limits, rotation, crypto-shredding with backup caveats, key custody choice and access policy, audit of key use.
2. *"How would you plan post-quantum migration for a bank?"* Strong answer: inventory and CBOM, Mosca-based prioritisation, hybrid key exchange first, signature and PKI plan, vendor requirements, crypto agility, timelines from NIST, regulators and India's DST report, testing for size and middlebox issues.
3. *"Certificate lifetimes are going to 47 days. What changes for us?"* Strong answer: full ACME or equivalent automation, inventory and ownership, ARI-based renewal, monitoring, private PKI for internal names, failure drills.
4. *"HSM, cloud KMS or external key store: how do you choose?"* Strong answer: threat model (provider insider, compelled access, regulation), latency and availability coupling, cost, operational skill, FIPS level, failure modes such as an external key store outage stopping all decryption.
5. *"A CI action you use was compromised and dumped secrets. What architecture would have limited the damage?"* Strong answer: OIDC short-lived credentials, least-privilege per job, no long-lived secrets in runners, pinned actions, secret scanning, rehearsed rotation.

## Resources (free first)

- **Books and courses:** Boneh and Shoup, [A Graduate Course in Applied Cryptography](https://toc.cryptobook.us/) (free); [CryptoHack](https://cryptohack.org/) (legal practice); Google, [Building Secure and Reliable Systems](https://sre.google/books/) (key management chapters).
- **Standards:** [FIPS 203](https://csrc.nist.gov/pubs/fips/203/final), [FIPS 204](https://csrc.nist.gov/pubs/fips/204/final), [FIPS 205](https://csrc.nist.gov/pubs/fips/205/final); [NIST PQC project](https://csrc.nist.gov/projects/post-quantum-cryptography); [SP 800-227](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-227.pdf); [SP 800-57 Part 1 Rev. 5](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final); [SP 800-131A Rev. 2](https://csrc.nist.gov/pubs/sp/800/131/a/r2/final); [CSWP 39 crypto agility](https://www.nist.gov/news-events/news/2025/12/nist-publishes-cswp-39-considerations-achieving-crypto-agility); [RFC 9846 (TLS 1.3)](https://www.rfc-editor.org/rfc/rfc9846); [RFC 8555 (ACME)](https://www.rfc-editor.org/rfc/rfc8555); [RFC 9773 (ACME ARI)](https://www.rfc-editor.org/rfc/rfc9773); [RFC 9162 (CT)](https://www.rfc-editor.org/rfc/rfc9162); [Mozilla SSL Configuration Generator](https://ssl-config.mozilla.org/).
- **Migration guidance:** [UK NCSC PQC migration timelines](https://www.ncsc.gov.uk/guidance/pqc-migration-timelines); [EU PQC policy page](https://digital-strategy.ec.europa.eu/en/policies/post-quantum-cryptography); [NSA CNSA 2.0](https://media.defense.gov/2022/Sep/07/2003071834/-1/-1/0/CSA_CNSA_2.0_ALGORITHMS_.PDF); [DST quantum-safe ecosystem report](https://dst.gov.in/sites/default/files/Quantum-Safe-Ecosystem-in-India.pdf); [CCA India](https://cca.gov.in/).
- **Tools:** [Google Tink](https://developers.google.com/tink), [libsodium](https://doc.libsodium.org/), [AWS Encryption SDK](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/introduction.html), [Project Wycheproof](https://github.com/C2SP/wycheproof), [Open Quantum Safe](https://openquantumsafe.org/), [step-ca](https://smallstep.com/docs/step-ca/), [cert-manager](https://cert-manager.io/docs/), [OpenBao](https://openbao.org/), [SOPS](https://getsops.io/), [Sigstore](https://www.sigstore.dev/).
- **Paid, optional:** David Wong, *Real-World Cryptography* (Manning, 2021); Jean-Philippe Aumasson, *Serious Cryptography*, 2nd edition (No Starch, 2024).

## Sources

All checked 12 Oct 2026.

- NIST PQC project page (FIPS 203–205 final August 2024; HQC selected 2025; IR 8547 initial public draft; page updated 5 Aug 2026) — https://csrc.nist.gov/projects/post-quantum-cryptography
- FN-DSA (FIPS 206) status: not yet final as of October 2026 per the IETF LAMPS draft referencing a forthcoming FIPS 206 (May 2026) — https://datatracker.ietf.org/doc/html/draft-ietf-lamps-fn-dsa-certificates (exact NIST draft status unconfirmed)
- NIST SP 800-227 final (18 Sep 2025) — https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-227.pdf ; NIST CSWP 39 (Dec 2025; updated version CSWP 39-upd1 in 2026) — https://www.nist.gov/news-events/news/2025/12/nist-publishes-cswp-39-considerations-achieving-crypto-agility ; https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.39-upd1.pdf
- DST, task force report on PQC migration (4 Feb 2026) and *Quantum-Safe Ecosystem in India* (May 2026); 2027 start for critical sectors as summarised by The Quantum Insider (9 Feb 2026) — https://dst.gov.in/sites/default/files/Report_TaskForce_PQMigration_4Feb26%20%28v1%29.pdf ; https://thequantuminsider.com/2026/02/09/india-reveals-national-plan-for-quantum-safe-security/
- CA/Browser Forum Ballot SC-081v3 (approved 11 Apr 2025), schedule as summarised by DNSimple — https://support.dnsimple.com/articles/announcement-ssl-certificate-validity-changes/
- CSRB report on the 2023 Exchange Online intrusion (Mar 2024) — https://www.cisa.gov/sites/default/files/2025-03/CSRBReviewOfTheSummer2023MEOIntrusion508.pdf
- CISA alerts: tj-actions (18 Mar 2025) — https://www.cisa.gov/news-events/alerts/2025/03/18/supply-chain-compromise-third-party-tj-actionschanged-files-cve-2025-30066-and-reviewdogaction ; npm Shai-Hulud (23 Sep 2025) — https://www.cisa.gov/news-events/alerts/2025/09/23/widespread-supply-chain-compromise-impacting-npm-ecosystem
- UIDAI Circular 14 of 2025 and ADV FAQ (3 Nov 2025) — https://uidai.gov.in/images/FAQs_Aadhaar_Data_Vault_03112025_v10.pdf
- CERT-In BOM guidelines v2.0 (9 Jul 2025), as summarised by Khaitan & Co — https://khaitanco.com/thought-leadership/CERT-Ins-Expanded-BOM-Guidelines-Preparing-for-the-Next-Phase-of-Cyber-Regulation
- Hybrid PQ defaults: Google Security Blog on ML-KEM in Chrome (Sep 2024) — https://security.googleblog.com/2024/09/a-new-path-for-kyber-on-web.html ; OpenSSL 3.5.0 release — https://github.com/openssl/openssl/releases/tag/openssl-3.5.0 ; OpenSSH 10.0 release notes — https://www.openssh.com/txt/release-10.0
- EU PQC roadmap timelines (end-2026 plans, high-risk by 2030, 2035) — https://digital-strategy.ec.europa.eu/en/policies/post-quantum-cryptography ; UK NCSC timelines (Mar 2025) — https://www.ncsc.gov.uk/guidance/pqc-migration-timelines
- RFC 9846 (TLS 1.3, July 2026), as cited in this curriculum's [FND114](../../../../01_year_1_foundations/semester_2/FND114_web_foundations_http_html_css_and_javascript/README.md) — https://www.rfc-editor.org/rfc/rfc9846

_Last reviewed: 2026-10_
