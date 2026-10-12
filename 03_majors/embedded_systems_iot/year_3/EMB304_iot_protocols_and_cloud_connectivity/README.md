# EMB304 · IoT Protocols and Cloud Connectivity

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 6 | 4 (≈ 120 hours) | L2 → L3 | [CS202](../../../../02_year_2_core_computer_science/semester_3/CS202_computer_architecture_and_systems_programming/README.md) (with [CS204](../../../../02_year_2_core_computer_science/semester_3/CS204_computer_networks/README.md), [EMB301](../EMB301_microcontrollers_and_embedded_c/README.md) and [EMB302](../EMB302_real_time_operating_systems/README.md) assumed) | [EMB404](../../year_4/EMB404_hardware_software_co_design_and_fpga_basics/README.md), [EMB402](../../year_4/EMB402_embedded_and_iot_security/README.md), [OV09B](../../../../04_overlaps/OV09_edge_ai_secure_iot/OV09B_iot_fleet_security_and_over_the_air_updates/README.md) |

## Why this course matters now

Connected IoT devices numbered about 18.5 billion in 2024 and are forecast to reach 39 billion by 2030 (IoT Analytics, October 2025), and India alone had installed 7.24 crore smart meters by June 2026. Each device must pick a radio, join a network without a keyboard, prove its identity, send data over links that drop for hours, and accept updates for a decade. The protocols keep moving: Matter 1.5 (November 2025) added cameras, closures and energy management to the smart-home standard; MQTT 5 is supported by mainstream brokers and cloud IoT platforms; and the EU Cyber Resilience Act's reporting obligations started on 11 September 2026. Platforms move too: Google shut down Cloud IoT Core in August 2023, giving customers a year to migrate entire fleets. AI assistants write MQTT clients and cloud rules in minutes; what they do not do is size a battery for a radio's airtime, design topic and identity schemes that scale to a million devices, or plan what happens when 100,000 devices reconnect at the same second. That is this course.

## Learning outcomes

By the end you can:

1. **Choose** a radio and protocol stack (BLE, Wi-Fi, Thread, LoRaWAN, NB-IoT/LTE-M) for a product from range, energy, data rate, cost and regulatory constraints, with numbers.
2. **Implement** MQTT 5 and CoAP clients on a microcontroller with TLS or DTLS, and **measure** their memory, energy and latency cost.
3. **Build** BLE peripherals with custom GATT services and **tune** advertising and connection parameters for power.
4. **Implement** Wi-Fi and BLE provisioning flows that a non-technical user can complete, with secure credential storage.
5. **Build** a LoRaWAN node and **calculate** airtime, duty-cycle limits and battery life.
6. **Explain** Thread and Matter (mesh, border routers, commissioning, data model) and **build** a simple Matter device.
7. **Design** device identity and provisioning for a fleet (per-device X.509 certificates, fleet provisioning, rotation).
8. **Operate** a fleet: device shadows or twins, jobs, staged OTA rollouts, crash and connectivity telemetry.
9. **Design** for unreliable networks and scale: store-and-forward, idempotent messages, jittered reconnects, broker load tests and a cost model.

## Chapters and lessons

### Chapter 1 · IoT system architecture (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Device, gateway, cloud | Direct-to-cloud vs gateway architectures; edge processing; where state lives | Draw the architecture of a smart meter, a fitness band and a cold-chain logger |
| 1.2 Constraints that drive design | Energy per bit, duty cycle, intermittent links, RAM for TLS, unit cost, certification | Fill a constraint sheet for 3 products |
| 1.3 Choosing a radio | BLE, Wi-Fi, Thread/Zigbee (802.15.4), LoRaWAN, NB-IoT/LTE-M, cellular; licensed vs unlicensed bands | Build a decision table with range, data rate, energy and cost for each |
| 1.4 Data modelling for devices | Telemetry vs events vs commands vs configuration; schemas, units, timestamps, versioning | Define a versioned message schema (CBOR or JSON) for a sensor node |

**Check your understanding:** Why does a 1 KB JSON message cost more battery than its byte count suggests? When is a gateway better than direct-to-cloud? Why must every message carry a schema version?

### Chapter 2 · Networking stacks on microcontrollers (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 IP on a microcontroller | lwIP and Zephyr networking, sockets API, buffers and memory pools | Measure RAM used by the stack at idle and under load |
| 2.2 IPv6 and 6LoWPAN | Header compression for 802.15.4, link-local addresses, why Thread uses IPv6 | Capture and decode a 6LoWPAN frame |
| 2.3 Time and naming | SNTP, DNS on devices, clock drift and timestamps without a network | Measure drift of the MCU clock over 24 hours; correct it with SNTP |
| 2.4 TLS on constrained devices | Mbed TLS, certificate chains, cipher suites, session resumption, RAM and handshake energy | Measure handshake time and energy with ECDSA vs RSA certificates |

**Check your understanding:** Why does TLS often need more RAM than the rest of the application? What breaks if a device's clock is wrong by a year? Why does Thread insist on IPv6?

### Chapter 3 · MQTT (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Publish/subscribe | Broker, topics, wildcards, topic design for fleets (`tenant/site/device/stream`) | Design a topic tree with access rules for 3 tenants |
| 3.2 Delivery semantics | QoS 0/1/2, duplicates, retained messages, Last Will and Testament, persistent sessions | Kill the network mid-publish; count losses and duplicates at each QoS |
| 3.3 MQTT 5 features | Reason codes, user properties, message expiry, topic aliases, shared subscriptions, request/response | Use message expiry and shared subscriptions in a backend consumer group |
| 3.4 Brokers | Mosquitto, EMQX, managed brokers; authentication and ACLs; MQTT-SN for sensor networks | Run Mosquitto with TLS and per-device ACLs |

**Check your understanding:** Why is QoS 1 "at least once" and what must the consumer do about it? When is a retained message harmful? Why do topic names belong in your security design?

### Chapter 4 · CoAP and LwM2M (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 CoAP | REST over UDP (RFC 7252), confirmable vs non-confirmable, tokens, Observe (RFC 7641), block-wise transfer (RFC 7959) | Build a CoAP sensor server on Zephyr; observe it from a laptop |
| 4.2 Security for CoAP | DTLS 1.2/1.3 (RFC 9147), OSCORE object security (RFC 8613) | Compare message sizes and handshakes with DTLS vs OSCORE |
| 4.3 LwM2M device management | Objects and resources, bootstrap, registration, firmware-update object | Register a device with an open-source LwM2M server; push a config change |
| 4.4 MQTT vs CoAP vs HTTP | Energy, NAT traversal, firewall friendliness, tooling | Measure energy per reading for each over the same link |

**Check your understanding:** Why does CoAP fit NB-IoT better than MQTT over TCP? What does OSCORE protect that DTLS does not, when there is a proxy? Why use a standard object model like LwM2M instead of inventing one?

### Chapter 5 · Bluetooth Low Energy (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 GAP | Advertising, scanning, connections, roles; advertising interval vs discovery time vs current | Measure current at 3 advertising intervals |
| 5.2 GATT | Services, characteristics, descriptors, notifications vs indications, MTU and throughput | Build a custom service for a sensor; read it from nRF Connect on a phone |
| 5.3 Connection parameters | Connection interval, peripheral latency, supervision timeout, PHY (1M, 2M, Coded) | Tune parameters for a 2-year coin-cell target; measure |
| 5.4 BLE security | Pairing methods, LE Secure Connections, bonding, privacy (resolvable addresses), Just Works risks | Enforce authenticated pairing for a write characteristic |
| 5.5 Phones as gateways | iOS and Android background limits, Web Bluetooth, the Bluetooth Core 6.0 features (for example Channel Sounding for distance) | Relay sensor data through a phone app or a Web Bluetooth page |

**Check your understanding:** Why is "Just Works" pairing unsafe for a door lock? What sets BLE throughput in practice? Why does a phone app that works in the foreground stop receiving data in the background?

### Chapter 6 · Wi-Fi devices and provisioning (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Wi-Fi on MCUs | Station mode, power-save modes, DTIM, Target Wake Time (Wi-Fi 6 parts such as the ESP32-C6) | Measure average current with modem sleep, light sleep and TWT |
| 6.2 Provisioning flows | SoftAP, BLE-based provisioning (ESP-IDF unified provisioning), QR codes, Wi-Fi Easy Connect (DPP) | Implement BLE provisioning with a proof-of-possession code |
| 6.3 Credentials on the device | Encrypted NVS, factory reset, credential rotation | Show credentials are not readable in a flash dump with encryption enabled |
| 6.4 Reconnection logic | Exponential backoff with jitter, router reboots, captive portals, IP changes | Survive 50 random router reboots with no manual intervention |

**Check your understanding:** Why does SoftAP provisioning confuse users on modern phones? What must a factory reset erase, and what must it keep? Why add jitter to backoff?

### Chapter 7 · LoRaWAN and cellular IoT (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 LoRa physical layer | Chirp spread spectrum, spreading factor vs range vs airtime, link budget | Compute airtime for SF7 and SF12 payloads; verify with a calculator |
| 7.2 LoRaWAN | Classes A/B/C, OTAA vs ABP, adaptive data rate, frame counters, India's IN865 regional parameters and duty limits | Join The Things Network or a ChirpStack server; send sensor data |
| 7.3 NB-IoT and LTE-M | Power-saving mode (PSM), eDRX, coverage enhancement, SIMs and eSIM/iSIM, operator choices | Estimate battery life for a meter reporting hourly over NB-IoT |
| 7.4 Choosing LPWAN | Private gateways vs operator networks; ownership, cost per device per year, coverage risk | Write a recommendation for a 10,000-node agricultural deployment (illustrative) |

**Check your understanding:** Why does ABP with reset frame counters break security? Why does SF12 drain batteries even though it reaches further? When is NB-IoT worth the SIM cost?

### Chapter 8 · Thread and Matter (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Thread | IEEE 802.15.4 mesh, routers and end devices, sleepy end devices, border routers, OpenThread | Form a 3-node Thread network; ping across it from a laptop |
| 8.2 Matter's data model | Nodes, endpoints, clusters, attributes and commands; device types | Map a smart plug onto Matter clusters |
| 8.3 Commissioning and fabrics | BLE-assisted commissioning, setup codes, device attestation certificates, multi-admin | Commission a Matter example device with `chip-tool` |
| 8.4 What changed in Matter 1.5 | Cameras (WebRTC), closures, soil sensors, energy management; certification cost and process | Read the 1.5 release notes; decide whether a product idea needs them |

**Check your understanding:** Why does a Thread network need a border router to reach the internet? What problem does multi-admin solve for users? Why does Matter require device attestation?

### Chapter 9 · Cloud IoT platforms (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Managed platforms | AWS IoT Core (registry, X.509, policies, rules, shadows, jobs), Azure IoT Hub and Device Provisioning Service | Connect a device to AWS IoT Core free tier or Azure IoT Hub free tier |
| 9.2 Open-source stacks | EMQX or Mosquitto + a time-series database + ThingsBoard or Grafana | Build the same pipeline on open-source parts on a laptop or small VM |
| 9.3 Ingest pipelines | Rules engines, queues (see [BE304](../../../backend_engineering/year_3/BE304_asynchronous_systems_queues_streams_and_event/README.md)), time-series storage and retention | Store and chart 1 week of telemetry with downsampling |
| 9.4 Lock-in and exit plans | Google's 2023 retirement of Cloud IoT Core; portable designs (standard MQTT, own identity) | Write a 1-page exit plan for your pipeline |

**Check your understanding:** What did Cloud IoT Core customers have to change, and what design choices would have made it easier? Why store raw telemetry separately from aggregates? Which managed-platform features are hardest to leave?

### Chapter 10 · Identity and provisioning at scale (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Device identity | Per-device keys and X.509 certificates, device IDs, avoiding shared secrets | Generate a CA and per-device certificates with OpenSSL |
| 10.2 Manufacturing provisioning | Key injection on the line, claim certificates, just-in-time registration | Simulate a factory line provisioning 100 devices from a script |
| 10.3 Fleet provisioning | Exchanging a claim certificate for an identity; DPS-style enrolment groups | Implement fleet provisioning on your board |
| 10.4 Lifecycle | Certificate rotation, revocation, decommissioning, ownership transfer | Rotate a device certificate over the air without downtime |

**Check your understanding:** Why is one shared password per product a fleet-wide vulnerability? Who should be able to revoke a device, and how fast? What happens to a device whose certificate expires while it is on a shelf for two years?

### Chapter 11 · Fleet management and OTA (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Shadows and twins | Desired vs reported state, versioning, conflict handling | Change a reporting interval from the cloud while the device is offline |
| 11.2 OTA mechanics | A/B slots, MCUboot or ESP-IDF OTA, image confirmation and rollback, delta updates | OTA your device from the cloud; force a rollback with a bad image |
| 11.3 Rollouts | Cohorts, canaries, staged percentages, halt conditions, campaign metrics | Run a staged rollout to 20 simulated devices with an automatic halt |
| 11.4 Device observability | Reset reasons, crash dumps, heap and stack metrics, connectivity statistics; tools such as Memfault or Golioth | Ship crash reports from your device to a dashboard |

**Check your understanding:** Why must a device confirm a new image only after it reaches the cloud? What metric would halt your rollout automatically? Why is "the device stopped reporting" the hardest field failure to debug?

### Chapter 12 · Reliability, scale and cost (weeks 12–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Offline-first devices | Store-and-forward, bounded buffers, priorities when the buffer fills, idempotent message IDs | Survive a 24-hour outage with no data loss and no duplicates in the database |
| 12.2 Reconnect storms | Thundering herds after outages, jittered backoff, broker connection limits | Simulate 10,000 clients reconnecting; compare with and without jitter |
| 12.3 Load testing brokers | Message rates, fan-out, persistence; tools such as emqtt-bench | Find your broker's knee point on a small VM |
| 12.4 Cost and data protection | Messages per month, data transfer, storage; personal data under India's Digital Personal Data Protection Act 2023; data minimisation | Build a cost model for 50,000 devices for 3 years |
| 12.5 Regulation preview | EU Cyber Resilience Act timelines, ETSI EN 303 645, India's TEC 31318:2021 (detailed in EMB402) | Map your product's obligations to a checklist |

**Check your understanding:** Why can a 5-minute cloud outage cause a 30-minute recovery? What is the cheapest message, and how do you design for it? Which telemetry fields might be personal data?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Radio decision table | — |
| 2 | 2 | Lab 2 · TLS cost on an MCU | — |
| 3 | 3 | Lab 3 · MQTT semantics under failure | — |
| 4 | 4 | Lab 4 · CoAP and LwM2M | **P1 due** |
| 5 | 5 | Lab 5 · BLE power tuning | — |
| 6 | 6 | Lab 6 · Provisioning and reconnects | — |
| 7 | 7 | Lab 7 · LoRaWAN node | Mid-term (AI off) |
| 8 | 8 | Lab 8 · Thread and Matter | — |
| 9 | 9 | Lab 9 · Two pipelines, one device | — |
| 10 | 10 | Lab 10 · Fleet provisioning | **P2 due** |
| 11 | 11 | OTA and rollouts (in P3) | — |
| 12 | 12 | Outage and reconnect-storm tests (in P3) | — |
| 13 | 12 | Load test and cost model (in P3) | — |
| 14 | — | — | **P3 due** |
| 15 | Review | Oral defence of P3 | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** generating MQTT/CoAP client scaffolding, cloud rules and infrastructure templates; writing load-test and simulator scripts (10,000 fake devices); explaining RFC sections; drafting provisioning scripts with OpenSSL; summarising long platform documentation into a checklist.
- **Do without AI (drills):** airtime and battery-life calculations; QoS failure scenarios on paper; topic and ACL design; drawing provisioning sequence diagrams; deciding the radio for a brief. The mid-term and final are AI-off.
- **Verify AI output by:** capturing traffic (Wireshark for IP, nRF Sniffer or a phone app for BLE, the LoRaWAN network server's frame log); measuring energy per message with a current probe; running failure tests (pull the network, reboot the router, kill the broker); checking the exact SDK version's API (ESP-IDF, Zephyr and cloud SDKs change between major versions); load-testing claims about scale.
- **Where AI still fails here (show it yourself):** EmbedBench found the best model at 29.4% pass@1 migrating Arduino code to ESP-IDF (arXiv 2506.11003), and IoT code is mostly vendor-SDK code. In Lab 3 and Lab 6 you log the defects in assistant-written clients. Typical ones: deprecated SDK calls, hard-coded credentials and certificates in source, disabled certificate verification "to make it work", missing reconnect backoff, QoS 1 consumers that are not idempotent, and LoRaWAN code that ignores duty-cycle limits.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1–P3 | 35% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) + P3 oral defence | 30% |

**Mastery gate.** You pass when you can, with AI off: (1) given a product brief, choose a radio and protocol stack and justify it with airtime, energy and cost numbers in 30 minutes; (2) draw the full provisioning and identity flow for a fleet from factory to decommissioning, including rotation and revocation; (3) demonstrate your P3 surviving a 24-hour outage and a reconnect storm with no lost or duplicated readings and an OTA rollout that halts itself on a bad image.

## Industry reality

Where this is used: smart meters (India's RDSS rollout), connected two-wheelers and fleet trackers, cold-chain logistics, smart-home devices, industrial monitoring and agriculture. The standards are open and stable enough to build on (MQTT 5 at OASIS; CoAP and OSCORE at the IETF; Matter at the Connectivity Standards Alliance, whose 1.5 release added cameras and energy features). Platform risk is real: Google gave Cloud IoT Core customers a year's notice before shutting it down in August 2023 (RCR Wireless, 2022). Regulation is tightening for every connected product sold in Europe from 2026–27 (EU Cyber Resilience Act).

**Interview questions from this course**

1. *Explain MQTT QoS levels and what your backend must do for each.* Strong answer: QoS 0 at most once, QoS 1 at least once (duplicates possible, so consumers must be idempotent using message IDs), QoS 2 exactly once between client and broker only; persistent sessions; why end-to-end exactly-once needs application design.
2. *How would you provision a million devices securely?* Strong answer: unique per-device keys generated or injected in manufacturing (ideally in a secure element), certificates signed by a manufacturing CA, claim-to-identity flow on first connect, enrolment groups, rotation and revocation, audit logs; never shared secrets.
3. *BLE or Wi-Fi for a battery wearable that syncs once an hour?* Strong answer: BLE via the phone for energy and cost; quantifies average current; discusses phone background limits, data size per sync, and when Wi-Fi direct-to-cloud is justified.
4. *LoRaWAN or NB-IoT for water meters in a city?* Strong answer: coverage (deep indoor), ownership (private gateways vs operator), per-device recurring cost, downlink needs, firmware updates over the link, battery life at the reporting interval, regulatory duty cycle; recommends with numbers and a pilot.
5. *After a 10-minute cloud outage, your broker falls over when devices reconnect. Fix it.* Strong answer: jittered exponential backoff on devices, connection-rate limiting and autoscaling on the broker, shedding non-critical traffic, staged reconnection, store-and-forward with bounded buffers, and a load test that reproduces the storm.

## Resources (free first)

- **Specifications:** MQTT 5.0 (OASIS) — https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html ; RFC 7252 (CoAP) — https://www.rfc-editor.org/rfc/rfc7252 ; RFC 8613 (OSCORE) — https://www.rfc-editor.org/rfc/rfc8613 ; RFC 9147 (DTLS 1.3) — https://www.rfc-editor.org/rfc/rfc9147 ; Bluetooth specifications — https://www.bluetooth.com/specifications/specs/ ; LoRa Alliance resource hub — https://resources.lora-alliance.org/
- **Courses and guides:** HiveMQ MQTT Essentials — https://www.hivemq.com/mqtt/ ; Nordic DevAcademy (Bluetooth LE, Wi-Fi and cellular IoT fundamentals) — https://academy.nordicsemi.com/ ; The Things Network documentation — https://www.thethingsnetwork.org/docs/
- **Thread and Matter:** OpenThread — https://openthread.io/ ; Matter SDK (connectedhomeip) — https://github.com/project-chip/connectedhomeip ; CSA, "Matter 1.5 introduces cameras, closures and enhanced energy management" — https://csa-iot.org/newsroom/matter-1-5-introduces-cameras-closures-and-enhanced-energy-management-capabilities/
- **Platforms:** AWS IoT Core Developer Guide — https://docs.aws.amazon.com/iot/latest/developerguide/ ; Azure IoT Hub documentation — https://learn.microsoft.com/en-us/azure/iot-hub/ ; Eclipse Mosquitto — https://mosquitto.org/ ; EMQX — https://www.emqx.io/ ; ThingsBoard Community Edition — https://thingsboard.io/
- **Device SDKs:** ESP-IDF provisioning and OTA guides — https://docs.espressif.com/projects/esp-idf/en/latest/ ; Zephyr networking — https://docs.zephyrproject.org/latest/connectivity/networking/index.html ; MCUboot — https://docs.mcuboot.com/
- **Tools:** Wireshark — https://www.wireshark.org/ ; nRF Connect for Mobile (Nordic) ; Renode multi-node radio simulation — https://antmicro.com/platforms/renode/

## Sources

- IoT Analytics, "Number of connected IoT devices" (28 Oct 2025) — https://iot-analytics.com/number-connected-iot-devices/ (checked 2026-10)
- T&D India, smart meter installations to 30 Jun 2026 — https://www.tndindia.com/indias-smart-meter-population-at-7-24-crore-parliament/amp/ (checked 2026-10)
- CSA, Matter 1.5 announcement (Nov 2025) and Matter 1.5.1 — https://csa-iot.org/newsroom/matter-1-5-introduces-cameras-closures-and-enhanced-energy-management-capabilities/ ; https://csa-iot.org/newsroom/matter-1-5-1-enhancing-camera-performance-and-expanding-device-flexibility/ (checked 2026-10)
- European Commission, Cyber Resilience Act — https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act (checked 2026-10)
- RCR Wireless, "Google Cloud to shut down IoT Core service next year" (16 Aug 2022; shutdown 16 Aug 2023) — https://www.rcrwireless.com/20220816/internet-of-things/google-cloud-to-shut-down-iot-core-service-next-year (checked 2026-10)
- Xu et al., EmbedAgent/EmbedBench (arXiv 2506.11003) — https://arxiv.org/abs/2506.11003 (checked 2026-10)

_Last reviewed: 2026-10_
