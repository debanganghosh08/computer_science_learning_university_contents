# EMB402 · Embedded and IoT Security

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 7 | 4 (≈ 120 hours) | L3 → L4 | [EMB302](../../year_3/EMB302_real_time_operating_systems/README.md) (with [CS213](../../../../02_year_2_core_computer_science/semester_4/CS213_security_foundations/README.md), [EMB301](../../year_3/EMB301_microcontrollers_and_embedded_c/README.md) and [EMB304](../../year_3/EMB304_iot_protocols_and_cloud_connectivity/README.md) assumed) | [OV09B](../../../../04_overlaps/OV09_edge_ai_secure_iot/OV09B_iot_fleet_security_and_over_the_air_updates/README.md), [EMB501](../../year_5/EMB501_frontier_seminar_autonomous_systems_and_physical/README.md), [SAR501](../../../security_architecture/year_5/SAR501_frontier_seminar_post_quantum_migration/README.md) |

**Scope and ethics.** This course is defensive. It teaches how to design, build and verify devices that resist attack, and how to assess **your own** devices or legal practice targets (for example OWASP IoTGoat) with written scope. It does not teach attacks on devices you do not own or are not authorised in writing to test.

## Why this course matters now

Devices live for years in places nobody watches, and a single design mistake is copied into every unit. The 2016 Mirai botnet spread by logging in to cameras and routers with factory-default passwords and then flooded major internet services; a decade later, regulation has caught up. The UK's product security regime has required unique or user-set passwords, a published way to report vulnerabilities and a stated security-update period since 29 April 2024; the EU Cyber Resilience Act's vulnerability-reporting obligations apply from 11 September 2026 and its main obligations from 11 December 2027; ETSI EN 303 645 (v3.1.3, 2024) is the common baseline; and India's TEC 31318:2021 code of practice aligns with it. Chips now ship with the building blocks (the RP2350's signed boot with a key hash in OTP, TrustZone-M, secure elements, flash encryption), but they only help if the boot chain, keys, update path and vulnerability process are designed together. AI assistants are a real risk in this area: they readily suggest disabling certificate checks to "fix" a connection, comparing MACs with `memcmp`, or a one-time eFuse sequence that can permanently brick a board. This course teaches you to design, implement and evidence device security across the whole product life.

## Learning outcomes

By the end you can:

1. **Threat-model** a connected device (assets, attackers, entry points including radio, debug ports, update channel, app and cloud) and **prioritise** mitigations.
2. **Apply** cryptography correctly on constrained devices (AEAD, signatures, KDFs, random numbers, constant-time comparison) through vetted libraries and the PSA Crypto API.
3. **Implement** a hardware root of trust and secure boot chain with anti-rollback, on an MCU (MCUboot, ESP32 Secure Boot v2 or RP2350 signed boot) and on embedded Linux (verified boot to dm-verity).
4. **Protect** keys with secure elements, TPM 2.0, TrustZone-M and flash encryption, and **design** factory key provisioning.
5. **Design** a secure OTA system: offline signing, manifests, version and rollback protection, A/B fallback, and resilience to a compromised update server (TUF and Uptane concepts).
6. **Harden** firmware and embedded Linux: debug-port lifecycle, isolation, fuzzing of parsers, least privilege.
7. **Run** a vulnerability-handling process: SBOMs, CVE monitoring, coordinated disclosure, CERT-In reporting.
8. **Map** a product to ETSI EN 303 645, the EU Cyber Resilience Act, the UK PSTI regime, IEC 62443-4-2, ISO/SAE 21434 and India's TEC 31318, and **produce** the evidence.
9. **Assess** your own device within a written scope and **write** a security report with remediation.

## Chapters and lessons

### Chapter 1 · Device threats and threat modelling (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Why devices are different | Long life, physical access, shared firmware across a fleet, weak update paths, constrained crypto | List 10 ways a smart plug differs from a web server as a security target |
| 1.2 Case studies | Mirai (default credentials at scale), insecure update channels, leaked signing keys; lessons, not techniques | Write a one-page lessons-learned from the Mirai paper |
| 1.3 Threat modelling for devices | Assets, trust boundaries, data-flow diagrams, STRIDE per element, physical vs remote attackers | Threat-model your EMB304 P2 logger |
| 1.4 Prioritising | Likelihood and impact, attack cost, fleet-wide vs single-unit impact, residual risk | Rank your threats and choose the top 5 mitigations |

**Check your understanding:** Why is a vulnerability that needs physical access still serious for a fleet product? What made Mirai possible at scale, and which single requirement in today's regulations addresses it? Where are the trust boundaries in a phone-provisioned BLE device?

### Chapter 2 · Cryptography for constrained devices (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Symmetric primitives | AES-GCM and AES-CCM, ChaCha20-Poly1305, nonce rules, hardware AES engines | Encrypt records with AES-GCM; show what nonce reuse breaks (on your own data) |
| 2.2 Signatures and key exchange | ECDSA P-256, Ed25519, ECDH; signature size and verify time on an MCU | Measure sign and verify cycles on a Cortex-M4F |
| 2.3 Randomness and derivation | TRNG sources, health tests, seeding DRBGs, HKDF, per-device key derivation | Find the weak seeding in a provided driver and fix it |
| 2.4 Side-channel-aware coding | Constant-time comparison, avoiding secret-dependent branches, zeroising keys | Replace `memcmp` MAC checks with a constant-time compare; show timing difference |
| 2.5 Libraries and post-quantum awareness | Mbed TLS / PSA Crypto API, wolfSSL; NIST FIPS 203/204/205 (2024); LMS/XMSS hash-based signatures for firmware (NIST SP 800-208) | Compare footprint of ECDSA and LMS verification for a bootloader |

**Check your understanding:** Why is a CRC not an integrity check against an attacker? What does nonce reuse in AES-GCM give away? Why are hash-based signatures attractive for firmware even before quantum computers exist?

### Chapter 3 · Root of trust and secure boot (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Chains of trust | Immutable boot ROM, public-key hashes in OTP or eFuses, verified vs measured boot | Draw the boot chain of three chips from their datasheets |
| 3.2 MCU secure boot | MCUboot (image format, signature types, swap modes), ESP32 Secure Boot v2, RP2350 signed boot | Enable MCUboot with ECDSA signatures on your board; boot only signed images |
| 3.3 Anti-rollback | Monotonic counters, security version numbers in OTP, why version checks must be in the bootloader | Block a downgrade to a vulnerable signed image |
| 3.4 Irreversible steps | OTP/eFuse programming, development vs production keys, sacrificial boards, documented sequences | Write and peer-review an eFuse/OTP procedure before running it on a spare board |

**Check your understanding:** Why must the first verifier be immutable? What attack does anti-rollback stop that signatures alone do not? Why do teams test fuse-burning sequences on sacrificial boards first?

### Chapter 4 · Keys and hardware security (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Secure elements | Microchip ATECC608, NXP SE050, Infineon OPTIGA Trust M: keys that never leave the chip | Do TLS client authentication with a key inside a secure element |
| 4.2 TrustZone-M and TF-M | Secure and non-secure worlds, secure services via the PSA APIs, attestation tokens | Move a signing key into a TF-M secure partition (board or Corstone simulator) |
| 4.3 TPM 2.0 on Linux | Sealing keys to boot measurements, `tpm2-tools` | Seal a disk key to PCR values; show it fails after a boot change |
| 4.4 Flash encryption and storage | ESP32 flash encryption, encrypted NVS, protecting credentials at rest | Show credentials are unreadable in a flash dump of your own board |
| 4.5 Factory provisioning | Key generation inside the device vs injection, certificate signing at the factory, audit logs, PSA Certified levels | Design the provisioning station flow for 10,000 units |

**Check your understanding:** What does a secure element protect that flash encryption does not? Why generate keys on the device rather than inject them? What does a PSA Certified level tell a buyer, and what does it not?

### Chapter 5 · Debug ports and physical threats (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Debug lifecycle | JTAG/SWD locking, readout protection levels (for example STM32 RDP), authenticated debug, RMA flows | Define the debug policy for development, production and returns |
| 5.2 Physical threat classes | Fault injection and side-channel analysis as concepts; who can afford them; which assets they threaten | Classify your device's assets by physical-attack exposure |
| 5.3 Mitigations | Redundant checks, glitch detectors, constant-time code, tamper switches, removing test points | Add redundant signature checks and flow integrity to your bootloader |
| 5.4 Choosing chips for security | Reading a security datasheet, certifications, vendor advisories | Compare 3 MCUs' security features for a smart lock |

**Check your understanding:** Why is "lock the debug port" not a complete answer for a product that has returns and repairs? Why does a single `if (verified)` check become two in hardened bootloaders? When is a physical attack worth defending against?

### Chapter 6 · Secure firmware updates (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 The signing pipeline | Offline or HSM-held keys, CI signing services, key separation, key rotation and revocation | Build a signing step that never exposes the private key to CI logs |
| 6.2 Manifests and checks | Version, hardware compatibility, dependencies, hashes; check-then-install ordering; power-fail safety | Reject 10 crafted invalid manifests in tests |
| 6.3 Surviving server compromise | The Update Framework roles, thresholds and expiry; Uptane for vehicles | Map TUF roles onto your EMB304 P3 OTA service |
| 6.4 Fleet rollout security | Staged rollouts, kill switches, telemetry for update health, emergency patching | Run a security-patch campaign with a canary group |

**Check your understanding:** Why should the key that signs firmware not live on the update server? What does metadata expiry protect against? How do you revoke a leaked signing key without bricking the fleet?

### Chapter 7 · Secure communication (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 TLS done right on devices | Certificate validation, hostname checks, trust-store updates, mutual TLS | Make your device refuse a self-signed server and an expired certificate |
| 7.2 Pinning trade-offs | Pin to CA vs leaf, rotation plans, what breaks when certificates change | Design a pinning policy that survives a CA change |
| 7.3 BLE and Matter security | LE Secure Connections, out-of-band pairing, Matter device attestation and operational certificates | Enforce authenticated pairing; verify a Matter device attestation chain |
| 7.4 LoRaWAN security | Root keys, session keys, frame counters, join server role | Show why counter resets must be rejected |

**Check your understanding:** Why do devices fail years later when a CA certificate expires? What does certificate pinning buy and cost? Why does LoRaWAN rely on frame counters?

### Chapter 8 · Secure firmware engineering (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Memory-safety bugs in firmware | Parsers for radio, USB and network input; CWE-787, CWE-125, CWE-416 in C firmware | Find and fix planted bugs in a TLV parser |
| 8.2 Fuzzing firmware | Host builds with libFuzzer and sanitizers, harnesses for parsers, fuzzing under emulation (Renode, QEMU) | Fuzz your EMB304 command parser for 1 hour; fix every crash |
| 8.3 Isolation | MPU regions, unprivileged tasks, TrustZone partitions, Rust for parsers | Move the parser into an unprivileged task or a Rust module |
| 8.4 Coding standards and analysis | CERT C, MISRA security-relevant rules, static analysers, compiler hardening flags available on MCUs | Add a security-focused static-analysis gate to CI |

**Check your understanding:** Why are radio and USB parsers the highest-risk code on a device? What can fuzzing on the host miss that emulation catches? What does isolation buy if a parser bug still exists?

### Chapter 9 · Hardening embedded Linux (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Verified boot to user space | Signed FIT images, U-Boot verified boot, dm-verity root filesystem | Extend your EMB305 P3 with dm-verity; show a modified root refuses to mount |
| 9.2 Least privilege | Non-root services, systemd sandboxing options, capabilities, AppArmor or SELinux awareness | Score your services with `systemd-analyze security`; fix the worst |
| 9.3 Attack-surface reduction | Removing consoles, debug tools, unused services and kernel features | Diff dev and production images; justify every remaining service |
| 9.4 Secrets on Linux devices | TPM-sealed keys, encrypted data partitions, no secrets in images | Prove no secrets are present in your shipped image |

**Check your understanding:** Why is a read-only root not enough without dm-verity? Which of your services needs network and root, and why? Where do secrets go if not in the image?

### Chapter 10 · Supply chain, SBOMs and vulnerability handling (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 SBOMs | SPDX and CycloneDX, generating them for firmware (Zephyr, ESP-IDF, Yocto), VEX statements | Produce an SBOM for your firmware and your Linux image |
| 10.2 Monitoring and triage | CVE feeds, affected vs exploitable, patch decisions for devices | Triage 10 CVEs against your SBOM with written reasoning |
| 10.3 Disclosure and response | PSIRTs, ISO/IEC 29147 and 30111, security.txt, bug-bounty scope; CERT-In's 2022 directions on incident reporting | Write a vulnerability-disclosure policy and a response runbook |
| 10.4 Build integrity | Reproducible builds, signed commits and artefacts, provenance (SLSA concepts) | Make your firmware build reproducible and attach provenance |

**Check your understanding:** What does a VEX statement add to an SBOM? Why is "the library has a CVE" not the same as "the device is vulnerable"? Why does a regulator care how long you will ship updates?

### Chapter 11 · Standards and regulation (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Consumer IoT baselines | ETSI EN 303 645 provisions; UK PSTI regime (in force April 2024); India's TEC 31318:2021 | Map your device to every EN 303 645 provision with evidence |
| 11.2 The EU Cyber Resilience Act | Scope, essential requirements, reporting from September 2026, full application December 2027, support periods | Write a CRA readiness checklist for a smart-home product |
| 11.3 Industrial and automotive | IEC 62443-4-1/4-2; ISO/SAE 21434 and UN Regulations No. 155 and 156 for vehicles | Compare what 62443-4-2 and EN 303 645 ask for the same device |
| 11.4 Other regimes | NIST IR 8259A baseline, EU radio-equipment cybersecurity requirements, India's testing and certification schemes for telecom and IoT equipment (check current notifications), DPDP Act 2023 for personal data | Build a one-page compliance matrix for your P3 |

**Check your understanding:** Which three requirements appear in almost every consumer-IoT regime? Why does the CRA change the economics of long-term updates? How does automotive regulation tie security to type approval?

### Chapter 12 · Assessing your own device (weeks 12–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Authorisation and method | Written scope and permission, rules of engagement, OWASP ISVS and FSTM as checklists | Write the scope document for assessing your P3 |
| 12.2 Firmware inventory | Unpacking your own images, component and secret inventory, configuration review | Inventory your firmware; confirm no keys, passwords or debug features ship |
| 12.3 Interface verification | Fuzzing your own interfaces, checking pairing and TLS behaviour, verifying debug locks | Verify each threat-model mitigation with a test |
| 12.4 Reporting and remediation | Findings with severity, evidence and fixes; retesting; practice on OWASP IoTGoat | Write a security report for your P3 and close every high finding |

**Check your understanding:** Why does an assessment start with a written scope even on your own product? What makes a finding actionable for a firmware team? How do you prove a fix works?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Threat model a device | Threat model |
| 2 | 2 | Lab 2 · Crypto on an MCU | — |
| 3 | 3 | Lab 3 · Secure boot with MCUboot | — |
| 4 | 4 | Lab 4 · Keys in hardware | **P1 due** |
| 5 | 5 | Lab 5 · Debug lifecycle policy | — |
| 6 | 6 | Lab 6 · Signing pipeline and manifests | — |
| 7 | 7 | Lab 7 · TLS and pairing done right, and an AI audit | Mid-term (AI off) |
| 8 | 8 | Lab 8 · Fuzz your parser | — |
| 9 | 9 | Lab 9 · dm-verity and least privilege | — |
| 10 | 10 | Lab 10 · SBOM and CVE triage | **P2 due** |
| 11 | 11 | Compliance matrix (in P3) | — |
| 12 | 12 | Assessment of your own P3 | Scope document |
| 13 | 12 | Remediation and retest | Security report |
| 14 | — | — | **P3 due** |
| 15 | Review | Oral defence of P3 | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** first drafts of threat models (STRIDE tables) that you then challenge; SBOM and CVE triage scripts; mapping documents (EN 303 645 provisions to your evidence); explaining standards text; reviewing your code for obvious issues; writing test cases for manifest parsing.
- **Do without AI (drills):** drawing boot chains and trust boundaries; choosing crypto primitives and modes; deciding key storage for a product; triaging a CVE against an SBOM; writing the eFuse/OTP procedure. The mid-term and final are AI-off.
- **Verify AI output by:** checking crypto usage against the library's documentation and test vectors; testing negative cases (expired, self-signed, tampered, downgraded inputs must all be rejected); checking chip-specific security steps against the vendor's security guide for your exact chip revision; running static analysis and fuzzing; having a second person review any irreversible step.
- **Where AI still fails here (show it yourself):** in Lab 7 you ask an assistant to fix a TLS connection failure and to write a firmware-signature check. Log the defects. Typical ones: disabling certificate verification or hostname checks, embedding private keys or passwords in source, `memcmp` for MAC or signature comparison, `rand()` or a fixed seed for nonces, treating a CRC or hash as authentication, version checks done after installation, and confident eFuse/OTP sequences for the wrong chip revision. Each is a test case in your CI afterwards.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1–P3 | 35% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) + P3 oral defence | 30% |

**Mastery gate.** You pass when you can, with AI off: (1) produce a threat model and a prioritised mitigation plan for an unseen device in 45 minutes; (2) demonstrate on your board a secure boot and update chain that rejects unsigned, tampered and downgraded images and survives a power cut mid-update; (3) map your P3 to ETSI EN 303 645 and the EU Cyber Resilience Act with evidence for each claim, and defend it orally.

## Industry reality

Where this is used: every connected product sold in the UK since April 2024 must meet the PSTI baseline, and products sold in the EU face Cyber Resilience Act reporting from September 2026; vehicles in the EU need a certified cybersecurity management system under UN Regulation No. 155 for type approval; industrial buyers increasingly ask for IEC 62443-4-2 evidence. Chip vendors now build in the primitives (signed boot, OTP key hashes, TrustZone, secure elements), so the scarce skill is designing and evidencing the whole chain (analysis). In India, CERT-In's 2022 directions set incident-reporting duties for organisations, and TEC 31318:2021 sets a consumer-IoT baseline aligned with ETSI EN 303 645.

**Interview questions from this course**

1. *Design the secure boot chain for a new IoT product.* Strong answer: immutable ROM verifying a bootloader with a key hash in OTP; bootloader verifying the application signature and version (anti-rollback counter); A/B slots; debug locked in production with an authenticated RMA path; key management and rotation; how each failure is handled.
2. *Where would you store a device's private key, and why?* Strong answer: generated inside a secure element or TrustZone secure partition and never exported; flash encryption as a weaker fallback; trade-offs of cost, certification and provisioning; never a shared key across devices.
3. *How do you make OTA updates secure?* Strong answer: offline or HSM signing, signed manifests with version and hardware ID, verification before install, rollback protection, power-fail-safe A/B, staged rollout, key compromise recovery (TUF/Uptane ideas), telemetry.
4. *A researcher reports a vulnerability in your shipped device. What happens next?* Strong answer: acknowledge per your disclosure policy, reproduce, assess severity and fleet exposure via SBOM and telemetry, fix and test, staged patch rollout, coordinated disclosure date, regulatory reporting where required (for example CERT-In in India, CRA reporting in the EU), lessons learned.
5. *Threat-model a BLE smart lock.* Strong answer: assets (unlock capability, keys, logs), entry points (BLE, app, cloud, physical case, debug port, batteries), STRIDE threats (relay attacks, replay, weak pairing, key extraction, update tampering), mitigations (authenticated pairing, per-session challenges, distance bounding where available, secure element, signed updates, tamper detection, rate limiting), residual risks.

## Resources (free first)

- **Standards and guidance (free):** ETSI EN 303 645 — https://www.etsi.org/deliver/etsi_en/303600_303699/303645/ ; NIST IR 8259A — https://csrc.nist.gov/pubs/ir/8259/a/final ; EU Cyber Resilience Act — https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act ; UK PSTI regime — https://www.gov.uk/government/publications/the-uk-product-security-and-telecommunications-infrastructure-product-security-regime ; CERT-In directions under section 70B — https://www.cert-in.org.in/Directions70B.jsp ; NIST FIPS 203 — https://csrc.nist.gov/pubs/fips/203/final ; NIST SP 800-208 (LMS/XMSS) — https://csrc.nist.gov/pubs/sp/800/208/final
- **Implementation:** MCUboot — https://docs.mcuboot.com/ ; Trusted Firmware-M — https://www.trustedfirmware.org/projects/tf-m/ ; PSA Certified — https://www.psacertified.org/ ; ESP-IDF security guide (Secure Boot v2, flash encryption) — https://docs.espressif.com/projects/esp-idf/en/latest/esp32/security/security.html ; RP2350 datasheet (security chapter) — https://datasheets.raspberrypi.com/rp2350/rp2350-datasheet.pdf ; The Update Framework — https://theupdateframework.io/ ; Uptane — https://uptane.org/
- **Verification and practice:** OWASP IoT Security Verification Standard — https://github.com/OWASP/IoT-Security-Verification-Standard-ISVS ; OWASP Firmware Security Testing Methodology — https://github.com/scriptingxss/owasp-fstm ; OWASP IoTGoat (deliberately insecure firmware for legal practice) — https://github.com/OWASP/IoTGoat ; SPDX — https://spdx.dev/ ; CycloneDX — https://cyclonedx.org/
- **Case study:** Antonakakis et al., "Understanding the Mirai Botnet", USENIX Security 2017 — https://www.usenix.org/conference/usenixsecurity17/technical-sessions/presentation/antonakakis
- **Paid, optional:** Jasper van Woudenberg and Colin O'Flynn, *The Hardware Hacking Handbook* (No Starch, 2021), for understanding physical threats; practise only on hardware you own.

## Sources

- UK government, PSTI product security regime (in effect 29 Apr 2024; passwords, vulnerability reporting, update periods) — https://www.gov.uk/government/publications/the-uk-product-security-and-telecommunications-infrastructure-product-security-regime (checked 2026-10)
- European Commission, Cyber Resilience Act (in force 10 Dec 2024; reporting 11 Sep 2026; main obligations 11 Dec 2027) — https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act (checked 2026-10)
- ETSI EN 303 645 version listing (v3.1.3, Sep 2024) — https://www.etsi.org/deliver/etsi_en/303600_303699/303645/ (checked 2026-10)
- TEC presentation on TEC 31318:2021 (ETSI Security Conference 2023) — https://docbox.etsi.org/Workshop/2023/10_ETSISECURITYCONFERENCE/D13_REGULATION/TEC_Kumar.pdf (checked 2026-10)
- CERT-In, Directions under section 70B(6) of the IT Act (28 Apr 2022) — https://www.cert-in.org.in/Directions70B.jsp (checked 2026-10)
- Raspberry Pi Pico 2 product page (RP2350 security features) — https://www.raspberrypi.com/products/raspberry-pi-pico-2/ (checked 2026-10)
- Antonakakis et al., Mirai (USENIX Security 2017) — link above (checked 2026-10)

_Last reviewed: 2026-10_
