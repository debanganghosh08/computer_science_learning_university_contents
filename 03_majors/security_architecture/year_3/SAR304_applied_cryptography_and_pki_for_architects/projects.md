# SAR304 · Labs and projects

Labs run locally (Docker, a `kind` cluster, OpenSSL 3.5 or later, step-ca, OpenBao or Vault in dev mode, a local KMS emulator such as LocalStack or OpenBao's transit engine) or in a personal cloud account with a budget alarm. Systems named below are *illustrative scenarios* unless a source is given. Lab 1 is done without AI assistants. Never paste real keys or secrets into any tool.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Primitive selection and nonce budgets (no AI) | Choose primitives, modes and parameters for eight scenarios (file storage, JWT signing, firmware, webhook verification, password storage, backups, IoT telemetry, inter-service messages); compute the safe message volume for AES-GCM with random nonces | Selection table with reasons and the arithmetic | 3 h |
| 2 · Key ceremony and custody | Script an offline-root key ceremony (roles, dual control, evidence) and compare four custody models for a payment tokenizer | Ceremony script and a scored comparison (cost, latency, control, failure, regulation) | 4 h |
| 3 · Envelope encryption | Implement envelope encryption with encryption context, data-key caching and KEK rotation | Code, tests (including a tampered-context failure), KMS call counts and latency with and without caching | 5 h |
| 4 · Secrets out of the pipeline | Issue 15-minute database credentials from a vault and redesign a CI pipeline so no job holds a long-lived secret | Configuration, a run log, and a table of every secret before and after | 5 h |
| 5 · TLS and mTLS | Configure TLS 1.3 on a server with a 0-RTT policy and mTLS between two services that rejects unknown clients | Configurations, test-tool scores, a rejected-client log | 4 h |
| 6 · Private PKI | Build a three-tier PKI with step-ca: offline root, issuing CA with name constraints; set up Certificate Transparency monitoring for a domain you own | Ceremony log, chain, a refused out-of-constraint issuance, CT alert screenshot | 5 h |
| 7 · Lifecycle automation | Automate issuance and renewal with ACME and cert-manager at one-hour lifetimes for three services | 24 hours of renewal logs with zero failed requests under light load | 4 h |
| 8 · Signing and rotation | Sign a container image keylessly; rotate a JWT signing key with overlap | Verification output; a load-test log showing zero failed token validations during rotation | 4 h |
| 9 · Hybrid post-quantum key exchange | Enable X25519MLKEM768 on a lab TLS server and client; capture handshakes | Packet captures, handshake sizes and latency compared with X25519 alone | 3 h |
| 10 · CBOM and AI code review | Produce a CBOM for a provided service; then review five AI-generated crypto snippets with Wycheproof vectors and Semgrep rules | CBOM file, error classification table, failing vectors | 5 h |

## Projects

### P1 · Encryption design for a document locker (L1, ~6 hours)

**Real-world inspiration:** document wallets such as DigiLocker let people store and share sensitive documents, and India's DPDP Act gives people a right to erasure. The locker is an *illustrative scenario* for a college: students store mark sheets and identity documents and share them with employers.

**What to build:** an encryption design with a key hierarchy diagram, cryptoperiods, envelope encryption, per-user keys for crypto-shredding, a rotation plan and four ADRs; plus a small demo against a local KMS emulator.

**Acceptance criteria:**
- Every cryptoperiod is justified with a reference to NIST SP 800-57 Part 1 Rev. 5.
- The demo shows: encrypt, decrypt, a tampered ciphertext or context rejected, KEK rotation with old data still readable.
- Deleting one user's key makes that user's documents undecryptable while others' still work; the design states what happens to backups.
- Each ADR records the rejected option and a trigger to revisit.

**Stretch goals:** a deterministic token for document lookup that does not reveal the document number; a cost estimate for KMS calls at 1 million documents.

**What it proves to an employer:** you can design data encryption whose keys, rotation and erasure actually work.

### P2 · Private PKI and certificate automation for a service estate (L2, ~15 hours)

**Real-world inspiration:** public TLS certificate lifetimes drop to 100 days in March 2027 and 47 days in March 2029 under CA/Browser Forum Ballot SC-081v3; service meshes already use certificates that live for hours. The estate is an *illustrative scenario*: five services in two environments.

**What to build:** an offline root, one issuing CA per environment with name constraints, automated issuance through ACME and cert-manager, mTLS among the five services with SPIFFE-style identities in SANs, an inventory with owners, expiry monitoring, and a revocation and re-issuance drill.

**Acceptance criteria:**
- Over 72 hours of continuous load with one-hour certificate lifetimes, zero requests fail because of certificate expiry or rotation (show graphs).
- The root key is used only during a recorded ceremony and is offline otherwise (evidence: ceremony log and storage notes).
- An attempt to issue a certificate for a name outside the constraints fails at the CA.
- The inventory lists 100% of issued certificates with owner, purpose and expiry; an alert fires for any certificate within 20% of its lifetime that has not renewed.
- The revocation drill (compromised service key) completes in under 15 minutes with the old certificate refused.

**Stretch goals:** a hybrid post-quantum handshake between two services; issuance policy written as code and tested.

**What it proves to an employer:** you can run PKI as an automated system rather than a spreadsheet, which every organisation will need by 2029.

### P3 · Post-quantum migration programme for a payment aggregator (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** NIST's draft transition plan (IR 8547) targets removal of quantum-vulnerable algorithms by 2035; the UK NCSC asks for discovery by 2028; the EU roadmap targets high-risk systems by 2030; India's DST task force report (2026) urges critical sectors to start formal implementation by 2027. The aggregator is an *illustrative scenario*: merchant onboarding, payment APIs, card and UPI integrations, a mobile SDK, an HSM-backed signing service and partner VPNs. You receive a reference system (code and configuration) with planted cryptographic uses.

**What to build:**
- a CBOM of the reference system from code, configuration, certificates and third-party documentation;
- a Mosca-inequality analysis per data type and a prioritised migration roadmap with dependencies and vendor asks;
- a crypto-agility refactor of one service so its KEM and signature algorithms change by configuration, with version fields in stored formats and downgrade protection;
- hybrid TLS on the lab edge with measurements;
- a vendor questionnaire for HSM, payment-network and SDK suppliers;
- a two-page board summary.

**Acceptance criteria:**
- The CBOM covers at least 95% of the instructor's planted cryptographic uses, with location, algorithm, purpose, owner and replaceability.
- Hybrid TLS measurements report median and 95th-percentile handshake time and bytes over at least 1,000 handshakes, compared with classical key exchange.
- After the agility refactor, switching algorithms by configuration keeps all tests passing, old signatures still verify, and a forced downgrade attempt is rejected (show the test).
- The roadmap passes a dependency check, and every date is tied to a cited external timeline or an explicit internal assumption.
- The board summary states cost ranges, the three biggest risks, and the decisions needed this year.
- You defend the programme in a 20-minute oral; the panel changes one assumption (for example, an earlier quantum timeline) and you re-prioritise live.

**Stretch goals:** ML-DSA certificate chains in the lab with measured size impact; an assessment of stateful hash-based signatures for the mobile SDK's update channel.

**What it proves to an employer:** you can run the inventory-to-roadmap work that banks, payment firms and governments are hiring for now.

## Feeds into

- [SAR401 Cloud Security Architecture](../../year_4/SAR401_cloud_security_architecture/README.md): KMS, data protection and key policy across accounts.
- [SAR404 Resilience and Security Strategy](../../year_4/SAR404_resilience_business_continuity_and_security/README.md): key recovery, immutable backups and the budget case for migration.
- [SAR501 Frontier Seminar](../../year_5/SAR501_frontier_seminar_post_quantum_migration/README.md): P3 becomes the base for the post-quantum migration research project.
- The [flagship industry project](../../../../06_career_and_market_readiness/05_industry_projects/SAR_security_architecture.md): its key management and PKI sections.
