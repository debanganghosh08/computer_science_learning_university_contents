# EMB402 · Labs and projects

All work is on hardware you own or on deliberately vulnerable practice targets (OWASP IoTGoat), within a written scope. Use **development keys** for every lab; irreversible steps (eFuse or OTP programming, permanent debug lock) are optional, done only on a spare board after a peer-reviewed written procedure. Hardware: your EMB301/EMB304 boards, a secure element breakout (for example ATECC608 or SE050) or a TrustZone-M target (board or Arm Corstone simulator), and your EMB305 Linux board. Private keys never enter a repository; CI uses a secret scanner.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Threat model a device | STRIDE threat model of your EMB304 P2 logger, with data-flow diagram and top-5 mitigations | Threat model document; ranked risk table | 4 h |
| 2 · Crypto on an MCU | AES-GCM records, ECDSA sign/verify, HKDF per-device keys, constant-time comparison; measure cycles | Code with test vectors passing; timing table; constant-time evidence | 4 h |
| 3 · Secure boot with MCUboot | Boot only signed images; block a signed but older image | Test log for unsigned, tampered, wrong-key and downgraded images; boot-time overhead | 4 h |
| 4 · Keys in hardware | TLS client authentication with a key inside a secure element or TF-M partition; flash encryption on an ESP32 dev board | Proof the key is non-exportable (API calls and results); flash dump showing ciphertext | 5 h |
| 5 · Debug lifecycle policy | Define and demonstrate debug states for development, production and repair (readout protection on a spare board optional) | Policy document; demonstration log | 3 h |
| 6 · Signing pipeline and manifests | CI signing step with the key outside CI logs; manifest parser rejecting 10 crafted invalid manifests | Pipeline config; negative test results | 4 h |
| 7 · TLS and pairing done right, and an AI audit | Device rejects self-signed, expired and wrong-hostname servers; BLE requires authenticated pairing; audit AI-written TLS and signature-check code | Test results; audit table (disabled verification, `memcmp`, weak randomness, hard-coded keys) | 4 h |
| 8 · Fuzz your parser | Host-build libFuzzer harness with sanitizers for your command parser; then run under emulation | Crash list, fixes, 1-hour clean run, coverage report | 4 h |
| 9 · dm-verity and least privilege | Add dm-verity to your EMB305 image; sandbox services with systemd options | Tampered-root test; `systemd-analyze security` before/after | 5 h |
| 10 · SBOM and CVE triage | SBOMs for your firmware and Linux image; triage 10 CVEs with VEX-style statements | SBOMs (SPDX or CycloneDX); triage table with reasoning | 4 h |

## Projects

### P1 · A signed, rollback-protected boot chain (L1, ~6 hours)

**Real-world inspiration.** Regulators and buyers now expect devices to accept only authentic updates; a bootloader that verifies signatures and refuses older vulnerable versions is the first building block (ETSI EN 303 645 includes provisions on secure updates).

**What to build.** MCUboot (or ESP32 Secure Boot v2, or RP2350 signed boot) with development keys on your board, an application that reports its version, and a test script that tries every bad image class.

**Acceptance criteria**
- 100% rejection, over at least 20 attempts, of: unsigned images, images with one flipped byte, images signed with a different key, and correctly signed images with a lower security version.
- A correctly signed newer image boots; boot-time overhead of verification measured and reported.
- A written, peer-reviewed procedure for moving from development to production keys (whether or not you perform irreversible steps).
- All keys outside the repository; secret scanner passes in CI.

**Stretch goals.** Hash-based (LMS) signature verification and a footprint comparison with ECDSA; redundant verification checks in the bootloader.

**What it proves to an employer.** You can implement the root of every device security story and test it with negative cases, not only the happy path.

### P2 · Secure identity and communication for a connected device (L2, ~15 hours)

**Real-world inspiration.** Consumer-IoT rules (UK PSTI, ETSI EN 303 645, India's TEC 31318) converge on unique credentials, secure communication and protected storage; a device built this way avoids the default-password failures that enabled Mirai.

**What to build.** Upgrade your EMB304 device: a per-device private key generated inside a secure element or TF-M partition; a factory-provisioning script that creates certificates for a batch of devices; mutual TLS to your broker with full validation; BLE configuration protected by LE Secure Connections; flash encryption for stored credentials; a fuzzed command parser running unprivileged.

**Acceptance criteria**
- The private key cannot be exported: the export attempt fails, and the README explains why by design.
- 10 virtual devices provisioned by your script receive unique identities; a revoked identity is refused by the broker.
- The device refuses servers with self-signed, expired or wrong-hostname certificates (automated tests).
- An unpaired or "Just Works" phone cannot change configuration.
- A flash dump shows no plaintext credentials.
- One hour of fuzzing of the command parser with sanitizers finds no crashes; the parser runs without privilege.
- An updated threat model shows which threats each change mitigates.

**Stretch goals.** Device attestation token (PSA) verified by the backend at connection; certificate rotation without downtime.

**What it proves to an employer.** You can build devices that meet modern IoT security baselines, with the tests to prove it.

### P3 · An end-to-end secure update system with a compliance evidence pack (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** EV chargers, smart meters and medical devices need to patch vulnerabilities quickly for years, and from 2026–27 products sold in the EU must handle vulnerabilities and report them under the Cyber Resilience Act. Vehicle makers use Uptane-style designs so that a compromised server cannot push malicious updates (illustrative of common practice; see the Uptane specification).

**What to build.** A secure update system for your device fleet (from EMB304 P3): an offline root key and online signing keys with separate roles (TUF-inspired), signed manifests with version, hardware ID and expiry, device-side verification before install, anti-rollback counters, A/B with automatic fallback, staged rollout with a kill switch, key rotation and revocation, SBOM plus VEX for every release, a published vulnerability-disclosure policy, an EN 303 645 and CRA compliance matrix, and a self-assessment report on your own device.

**Acceptance criteria**
- **Negative tests:** an automated suite of at least 30 bad-update cases (unsigned, tampered, expired metadata, wrong hardware ID, downgrade, mix-and-match of old and new metadata) with 100% rejection.
- **Power safety:** 50 power cuts at random points during updates leave every device bootable.
- **Key-compromise drill:** after simulating a leaked online signing key, you rotate it using the offline root; devices accept the rotation and reject images signed with the old key.
- **Emergency patch:** a patch reaches 20 devices (real plus simulated) through a canary stage within 30 minutes, with update-health telemetry.
- **Evidence:** SBOMs and VEX statements for two releases; every ETSI EN 303 645 provision mapped to evidence or justified as not applicable; a CRA readiness checklist; a disclosure policy and response runbook.
- **Self-assessment:** a scoped assessment of your own device (firmware inventory, interface fuzzing, TLS and pairing checks, debug-state check) with every high-severity finding fixed and retested.

**Stretch goals.** dm-verity and TPM-sealed keys on your Linux gateway in the same update system; delta updates with signature over the reconstructed image; a hash-based-signature option for post-quantum readiness.

**What it proves to an employer.** You can own device security end to end: design, implementation, operations and regulatory evidence. Product-security, automotive cybersecurity and IoT platform teams hire for exactly this, and it is a credible base for a security-focused hardware startup.

## Feeds into

- [OV09B IoT Fleet Security and Over-the-Air Updates](../../../../04_overlaps/OV09_edge_ai_secure_iot/OV09B_iot_fleet_security_and_over_the_air_updates/README.md): P3 at fleet scale.
- [EMB501 Frontier Seminar: Autonomous Systems and Physical AI](../../year_5/EMB501_frontier_seminar_autonomous_systems_and_physical/README.md): security as part of safety cases for autonomous systems.
- [SAR501 Post-Quantum Migration and Securing Autonomous Systems](../../../security_architecture/year_5/SAR501_frontier_seminar_post_quantum_migration/README.md): post-quantum signatures for long-lived devices.
- The [EMB flagship industry project](../../../../06_career_and_market_readiness/05_industry_projects/EMB_embedded_systems_iot.md): its secure boot and update chain.
