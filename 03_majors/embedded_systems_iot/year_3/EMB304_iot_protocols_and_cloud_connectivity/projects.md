# EMB304 · Labs and projects

Hardware: an ESP32-C6 (Wi-Fi 6, BLE and 802.15.4 radio) and a second radio board (another ESP32-C6, an nRF52/nRF54 board, or a LoRa module such as an SX1262 board), plus a current measurement set-up from EMB301. Cloud: free tiers of AWS IoT Core or Azure IoT Hub, or an open-source stack (Mosquitto or EMQX, a time-series database, Grafana or ThingsBoard) on a laptop or small VM. No credentials, keys or certificates are ever committed to a repository; every submission's README explains how secrets are provided.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Radio decision table | Compare BLE, Wi-Fi, Thread, LoRaWAN and NB-IoT for 3 product briefs with range, energy, data rate and cost | Decision table with sources for each number; one-page recommendation per brief | 3 h |
| 2 · TLS cost on an MCU | Measure RAM, flash, handshake time and handshake energy for TLS with ECDSA and RSA certificates, with and without session resumption | Measurement table and current traces | 4 h |
| 3 · MQTT semantics under failure, and an AI audit | Kill the network mid-publish at QoS 0, 1 and 2; count loss and duplicates; audit an AI-generated MQTT client | Loss/duplicate table; audit table (deprecated APIs, disabled TLS verification, missing backoff) | 4 h |
| 4 · CoAP and LwM2M | Build a CoAP server with Observe on Zephyr; register with an LwM2M server and change a resource remotely | Packet captures; energy per reading vs MQTT | 5 h |
| 5 · BLE power tuning | Custom GATT service; tune advertising and connection parameters to a coin-cell budget | Current traces per setting; predicted life | 4 h |
| 6 · Provisioning and reconnects | BLE provisioning with proof of possession; survive 50 random router reboots | Video or log of a provisioning run by a non-technical tester; reconnect log | 4 h |
| 7 · LoRaWAN node | Join TTN or ChirpStack via OTAA on IN865; send sensor data within duty-cycle limits | Airtime and duty-cycle calculation; network-server frame log; RSSI/SNR at 3 distances | 5 h |
| 8 · Thread and Matter | Form a Thread network; commission a Matter example device with `chip-tool` | Topology diagram; commissioning log; cluster map of your device | 5 h |
| 9 · Two pipelines, one device | Send the same telemetry to a managed platform and to an open-source stack | Architecture diagrams; cost and effort comparison; exit plan | 4 h |
| 10 · Fleet provisioning | Factory-script 100 virtual device identities; implement claim-to-identity provisioning on your board | Provisioning sequence diagram; logs; revocation demonstration | 4 h |

## Projects

### P1 · A secure MQTT telemetry node (L1, ~6 hours)

**Real-world inspiration.** Connected appliances and industrial sensors commonly report over MQTT to a broker; reconnection and credential handling, not the happy path, are where early products tend to fail in the field (illustrative scenario).

**What to build.** ESP32-C6 firmware that publishes versioned sensor messages over MQTT 5 with TLS and a per-device certificate, uses Last Will and Testament for online status, accepts a configuration command, and a dashboard that shows readings and online/offline state.

**Acceptance criteria**
- TLS with server-certificate verification enabled and a unique device certificate; no secrets in the repository (checked with a secret scanner in CI).
- 20 forced Wi-Fi drops: no crash, reconnection within 60 seconds each time, using exponential backoff with jitter (log shows varying intervals).
- Broker marks the device offline within 1.5× the keep-alive interval after power is pulled.
- Energy per published message measured (current trace) and reported in mJ.
- Message schema has a version field; the dashboard handles two schema versions.

**Stretch goals.** Add MQTT 5 request/response for commands with correlation data; add a CoAP variant and compare energy.

**What it proves to an employer.** You build connected firmware that handles credentials and failures correctly from the first version.

### P2 · A provisioned, remotely configured cold-chain logger (L2, ~15 hours)

**Real-world inspiration.** Vaccines and many foods must stay within temperature limits from factory to shop; loggers that a pharmacist can set up with a phone, and that keep data during network gaps, are common products (illustrative scenario).

**What to build.** A battery-powered logger that is provisioned over BLE from a phone or Web Bluetooth page, then uploads over Wi-Fi or LoRaWAN; supports remote configuration through a device shadow or twin (reporting interval, alarm thresholds); buffers readings in flash during outages; raises a local and remote alarm on excursions; lets a phone read the last 24 hours over BLE without the network.

**Acceptance criteria**
- 5 of 5 non-technical testers complete provisioning in under 3 minutes each, following only the printed instructions.
- BLE writes require authenticated pairing (LE Secure Connections); an unpaired phone cannot change configuration.
- A configuration change made while the device is offline is applied within one reporting interval after reconnection, and the reported state confirms it.
- A 6-hour network outage loses zero readings; the backend has no duplicates after recovery (message IDs).
- A measured charge-per-cycle trace supports a projected battery life of at least 1 year at a 5-minute interval; for LoRaWAN, the airtime and duty-cycle calculation for IN865 is included.
- An excursion alarm reaches the dashboard within 2 reporting intervals in 10 of 10 trials.

**Stretch goals.** Add Matter or Thread support for an in-home variant; add an LwM2M management path; sign configuration documents.

**What it proves to an employer.** You can deliver the full device journey (unboxing, provisioning, configuration, outage, alarm), which is what IoT product companies ship.

### P3 · A fleet backend with identity, staged OTA and reconnect-storm resilience (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** India's smart-meter rollout reached 7.24 crore installed meters by June 2026 ([T&D India](https://www.tndindia.com/indias-smart-meter-population-at-7-24-crore-parliament/amp/)); fleets of this size need factory identity, remote configuration, safe updates and recovery from mass outages. Two-wheeler telematics and fleet trackers face the same problems (illustrative).

**What to build.** A fleet system for at least 2 real devices plus up to 10,000 simulated devices (a load generator you write): per-device identity issued through a fleet-provisioning flow; device shadows; a telemetry pipeline into a time-series database with retention and downsampling; dashboards for fleet health (online count, firmware versions, reset reasons, RSSI); a staged OTA campaign service with cohorts and automatic halt rules; certificate rotation and revocation; and a written cost model and exit plan.

**Acceptance criteria**
- **Identity:** every device has a unique certificate from your provisioning flow; a revoked device is refused at its next connection; a certificate is rotated on a live device without data loss.
- **Reconnect storm:** after a broker restart, 10,000 simulated devices are all reconnected within 5 minutes without the broker crashing; a comparison run without jitter is included.
- **Outage:** a 24-hour outage of the backend causes zero lost and zero duplicated readings from the real devices (bounded buffers sized in the README).
- **OTA:** a campaign to 20 devices (real plus simulated) with a deliberately bad image halts automatically at the canary stage with at most 2 devices affected, and those devices roll back to the previous image on their own.
- **Observability:** a dashboard shows per-version crash and reset counts; one injected crash appears with its reset reason within 5 minutes.
- **Cost model:** a 3-year cost for 50,000 devices (messages, storage, data transfer, certificates), with the assumptions stated.
- **Exit plan:** the steps and effort to move the fleet to another platform, tested by pointing one real device at a second broker.

**Stretch goals.** Delta updates; LwM2M firmware-update object as an alternative path; a multi-tenant topic and ACL design with an access test suite.

**What it proves to an employer.** You can run devices as a fleet, not as demos: identity, updates, outages and cost, with evidence. IoT platform, telematics and energy companies hire for exactly this.

## Feeds into

- [EMB402 Embedded and IoT Security](../../year_4/EMB402_embedded_and_iot_security/README.md): identity, provisioning and OTA become a signed, rollback-protected, auditable chain.
- [OV09B IoT Fleet Security and Over-the-Air Updates](../../../../04_overlaps/OV09_edge_ai_secure_iot/OV09B_iot_fleet_security_and_over_the_air_updates/README.md): P3 is its starting fleet.
- [EMB404 Hardware-Software Co-Design and FPGA Basics](../../year_4/EMB404_hardware_software_co_design_and_fpga_basics/README.md): protocol processing as a candidate for hardware offload.
- [EMB401 Edge AI and TinyML](../../year_4/EMB401_edge_ai_and_tinyml/README.md): sending inferences instead of raw data changes the cost model.
- The [EMB flagship industry project](../../../../06_career_and_market_readiness/05_industry_projects/EMB_embedded_systems_iot.md): its connectivity and fleet backend.
