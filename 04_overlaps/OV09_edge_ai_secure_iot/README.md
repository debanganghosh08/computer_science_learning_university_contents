# OV09 · Edge AI and Secure IoT

| Composed of | Overlap courses | Typical entry majors | Market pages |
|---|---|---|---|
| [EMB401](../../03_majors/embedded_systems_iot/year_4/EMB401_edge_ai_and_tinyml/README.md) × [EMB402](../../03_majors/embedded_systems_iot/year_4/EMB402_embedded_and_iot_security/README.md) × [MLE404](../../03_majors/machine_learning_engineering/year_4/MLE404_efficient_inference_quantization_distillation/README.md) | [OV09A](OV09A_deploying_models_on_edge_devices/README.md), [OV09B](OV09B_iot_fleet_security_and_over_the_air_updates/README.md) | EMB, MLE, DLR, SEC, MOB | [EMB](../../06_career_and_market_readiness/01_market_map/roles/EMB_embedded_systems_iot.md) · [MLE](../../06_career_and_market_readiness/01_market_map/roles/MLE_machine_learning_engineering.md) · [SEC](../../06_career_and_market_readiness/01_market_map/roles/SEC_cybersecurity_defense.md) |

## The job this overlap maps to

A camera that counts vehicles at a junction, a vibration sensor that predicts a pump failure, a phone that transcribes speech offline, a smart meter that detects tampering: each runs a model on a device with little memory, a power budget and no engineer nearby. Each device is also a computer on a network for ten years, which attackers will scan, and which must accept updates without ever being bricked.

Common titles: **Edge AI Engineer**, **Embedded ML Engineer**, **On-Device ML Engineer**, **IoT Security Engineer**, **Device Security Engineer**, **Firmware Update (OTA) Engineer**, and **Device Platform Engineer**. At senior levels: **Embedded Architect** or **Product Security Lead (connected devices)**. The [EMB role page](../../06_career_and_market_readiness/01_market_map/roles/EMB_embedded_systems_iot.md) lists Edge AI Engineer among senior embedded titles.

Day to day:

- choosing hardware (microcontroller, Linux board with an NPU, phone, GPU module) for a model and a power budget;
- converting, quantising and benchmarking models on real devices, and proving accuracy did not quietly drop;
- designing device identity, secure boot, signed updates with rollback protection, and staged rollouts across a fleet;
- monitoring a fleet with limited telemetry, handling vulnerabilities, and producing compliance evidence.

**Demand evidence (checked October 2026).**

- Connected IoT devices reached 18.5 billion in 2024 and are forecast to reach 39 billion in 2030 ([IoT Analytics, Oct 2025](https://iot-analytics.com/number-connected-iot-devices/)).
- Internet of Things Specialists are among the fastest-growing jobs employers expect to 2030 ([WEF Future of Jobs 2025](https://reports.weforum.org/docs/WEF_Future_of_Jobs_Report_2025.pdf)).
- US electrical-engineering job postings stood at 152.0 on Indeed's index in October 2026 (February 2020 = 100), against 78.3 for software development ([Indeed Hiring Lab data](https://github.com/hiring-lab/job_postings_tracker), via the [market map](../../06_career_and_market_readiness/01_market_map/README.md)).
- Regulation is turning device security into a market requirement: the UK's consumer connectable product security regime took effect on 29 April 2024 ([GOV.UK](https://www.gov.uk/government/publications/the-uk-product-security-and-telecommunications-infrastructure-product-security-regime)); the EU Cyber Resilience Act requires manufacturers to report actively exploited vulnerabilities from 11 September 2026, with its main obligations from 11 December 2027 ([European Commission](https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act)); India's Telecommunication Engineering Centre published a consumer IoT code of practice (TEC 31318:2021) aligned with ETSI EN 303 645 ([MediaNama, Jan 2022](https://www.medianama.com/2022/01/223-iot-device-manufacturers-code-summary/)).

No official statistics count edge-AI or IoT-security engineers separately.

## Why the overlap exists

| Course | Owns | Typical gap when taken alone |
|---|---|---|
| [EMB401](../../03_majors/embedded_systems_iot/year_4/EMB401_edge_ai_and_tinyml/README.md) Edge AI and TinyML | Fitting models into kilobytes on microcontrollers | Linux-class and phone targets, fleet-scale model delivery |
| [EMB402](../../03_majors/embedded_systems_iot/year_4/EMB402_embedded_and_iot_security/README.md) Embedded and IoT Security | Device threat models, secure boot, signed and rollback-protected updates | Operating thousands of devices: provisioning at scale, staged rollouts, vulnerability programmes, model integrity |
| [MLE404](../../03_majors/machine_learning_engineering/year_4/MLE404_efficient_inference_quantization_distillation/README.md) Efficient Inference | Quantisation, distillation, compilers, serving engines | Real devices with thermal limits, sensors and no network; security of the model as an asset |

Edge AI fails at the joins: a model quantised on a workstation loses 6 points of accuracy on the device's own camera; a model update is signed but the device accepts an older, vulnerable model; an OTA campaign pushes to every device at once and bricks a region; nobody can tell which model version a device in the field is running. [OV09A](OV09A_deploying_models_on_edge_devices/README.md) covers deployment engineering across the edge spectrum; [OV09B](OV09B_iot_fleet_security_and_over_the_air_updates/README.md) covers keeping a fleet secure and updatable for its whole life.

## Composed courses and sequencing

From [`catalog.json`](../../catalog.json): OV09A and OV09B require [EMB301](../../03_majors/embedded_systems_iot/year_3/EMB301_microcontrollers_and_embedded_c/README.md) and [MLE305](../../03_majors/machine_learning_engineering/year_3/MLE305_applied_ml_tabular_vision_and_text/README.md), and list EMB401 and MLE404 as co-requisites.

| Semester | Prerequisites and composing courses | Overlap course | Notes |
|---|---|---|---|
| 5 (Y3) | EMB301 (ML majors take it as an elective) | — | [CS214](../../02_year_2_core_computer_science/semester_4/CS214_machine_learning_foundations/README.md) is already done in Year 2 |
| 6 (Y3) | MLE305 (EMB majors take it as an elective); recommended [EMB304](../../03_majors/embedded_systems_iot/year_3/EMB304_iot_protocols_and_cloud_connectivity/README.md), [EMB305](../../03_majors/embedded_systems_iot/year_3/EMB305_embedded_linux/README.md) | — | EMB305 helps with Linux-class targets in OV09A |
| 7 (Y4) | EMB401, EMB402 | **OV09A** Deploying Models on Edge Devices | OV09A and EMB401 share hardware |
| 8 (Y4) | MLE404 | **OV09B** IoT Fleet Security and Over-the-Air Updates | MLE404 Chapter 11 hands over to OV09B |
| 9–10 (Y5) | [EMB501](../../03_majors/embedded_systems_iot/year_5/EMB501_frontier_seminar_autonomous_systems_and_physical/README.md), [THS501](../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md), [THS502](../../05_shared_years_3_to_5/THS502_thesis_or_capstone_ii/README.md) | Capstone below | |

**If you come from:** ML or deep learning, start soldering early: EMB301 is the hard prerequisite, and the [EMB major's fast track](../../03_majors/embedded_systems_iot/README.md) lists the hardware kit (an ESP32-S3 board and a Raspberry Pi Pico 2 cover most labs). Security majors should take EMB301 and [SAR304](../../03_majors/security_architecture/year_3/SAR304_applied_cryptography_and_pki_for_architects/README.md) before OV09B.

## The two overlap courses

| Course | Semester | What it adds | Projects |
|---|---|---|---|
| [OV09A · Deploying Models on Edge Devices](OV09A_deploying_models_on_edge_devices/README.md) | 7 | Edge hardware selection, conversion toolchains (LiteRT, ExecuTorch, ONNX Runtime, TensorRT, OpenVINO, Core ML), sensor-to-decision pipelines, accuracy parity on device, latency/power/thermal measurement, hardware-in-the-loop CI, small language models on device, on-device monitoring | [labs and projects](OV09A_deploying_models_on_edge_devices/projects.md) |
| [OV09B · IoT Fleet Security and Over-the-Air Updates](OV09B_iot_fleet_security_and_over_the_air_updates/README.md) | 8 | Device identity and provisioning at scale, secure boot chains, signing infrastructure, OTA architectures (A/B, delta, SUIT, TUF, Uptane), rollback protection, staged rollouts, fleet monitoring and attestation, vulnerability programmes, model integrity, regulation (ETSI EN 303 645, UK PSTI, EU CRA) | [labs and projects](OV09B_iot_fleet_security_and_over_the_air_updates/projects.md) |

## Capstone brief: a secure, updatable edge-AI fleet

**Scenario (illustrative).** A cold-storage operator wants door-left-open and compressor-fault detection in 50 warehouses without sending video or audio to the cloud. Build a pilot fleet of at least five devices (for example ESP32-S3 boards with a microphone or camera, or Raspberry Pi boards with an AI accelerator) and the cloud side that manages them.

**Acceptance criteria:**

- **Model on device:** the deployed model's accuracy on a held-out set captured with the devices' own sensors is within 2 percentage points of the float model on the same set, with a confidence interval; p95 inference latency and energy per inference are measured on the device and meet a budget stated in advance.
- **Power:** a measured battery-life estimate (from current measurements, not datasheets) meets the target stated in the spec.
- **Boot and identity:** every device has a unique identity (per-device key or certificate, never shared); secure boot rejects an unsigned image and an image signed with a revoked key (demonstrated).
- **OTA:** signed A/B updates for both firmware and model; cutting power at 10 random points during an update never bricks a device (all 10 recover to a working image); rollback to an older vulnerable version is refused by an anti-rollback counter.
- **Staged rollout:** a campaign goes to 1 device, then 20%, then 100%, with automatic halt on a health-metric regression, demonstrated with a deliberately bad build.
- **Fleet visibility:** a dashboard shows firmware version, model version, health and last check-in for every device; the team can answer "which devices run model v3?" in under one minute.
- **Security programme:** a threat model, an SBOM per release, a vulnerability-disclosure policy and a mapping of the design to the 13 provisions of ETSI EN 303 645 with evidence.
- **Privacy:** no raw audio or video leaves the device; a network capture over 24 hours shows only the declared telemetry fields.

## Roles it leads to

| Role | What you would own | Entry route from this overlap |
|---|---|---|
| Edge AI Engineer / Embedded ML Engineer | Models on microcontrollers and Linux-class devices, from conversion to field monitoring | EMB or MLE major + OV09A P3 |
| On-Device ML Engineer (mobile) | Models in phone apps, runtime choice, size and battery budgets | MLE or MOB major + OV09A |
| IoT Security Engineer / Device Security Engineer | Device threat models, secure boot, keys, vulnerability handling | EMB or SEC major + OV09B P3 |
| OTA / Device Platform Engineer | Update infrastructure, rollout safety, fleet observability | OV09B + [OPS301](../../03_majors/devops_sre_platform_engineering/year_3/OPS301_ci_cd_engineering/README.md) as an elective |
| Product Security Lead (connected devices) | Compliance evidence, disclosure programmes, regulator and customer questions | After several years in the roles above |
| Research engineer in efficient or robust edge ML | TinyML, on-device learning, physical AI | [EMB501](../../03_majors/embedded_systems_iot/year_5/EMB501_frontier_seminar_autonomous_systems_and_physical/README.md) and a thesis |

## Sources

All checked October 2026.

- IoT Analytics, "Number of connected IoT devices" (28 Oct 2025) — https://iot-analytics.com/number-connected-iot-devices/
- World Economic Forum, *Future of Jobs Report 2025* — https://reports.weforum.org/docs/WEF_Future_of_Jobs_Report_2025.pdf
- Indeed Hiring Lab job postings data, via this university's market map — https://github.com/hiring-lab/job_postings_tracker
- GOV.UK, the UK Product Security and Telecommunications Infrastructure (Product Security) regime (in effect 29 Apr 2024) — https://www.gov.uk/government/publications/the-uk-product-security-and-telecommunications-infrastructure-product-security-regime
- European Commission, Cyber Resilience Act (in force 10 Dec 2024; reporting from 11 Sep 2026; main obligations from 11 Dec 2027) — https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act
- MediaNama, summary of TEC's Code of Practice for Securing Consumer IoT (Jan 2022) — https://www.medianama.com/2022/01/223-iot-device-manufacturers-code-summary/
- ETSI EN 303 645 V3.1.3 (2024-09) — https://www.etsi.org/deliver/etsi_en/303600_303699/303645/03.01.03_60/en_303645v030103p.pdf

_Last reviewed: 2026-10_
