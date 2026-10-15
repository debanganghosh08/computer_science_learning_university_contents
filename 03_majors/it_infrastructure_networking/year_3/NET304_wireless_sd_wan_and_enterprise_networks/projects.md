# NET304 · Labs and projects

Wireless labs need little hardware: a laptop with a Wi-Fi adapter that supports monitor mode (many USB adapters do; check the chipset), two low-cost access points that run OpenWrt, and a free survey or analyser app. Survey only buildings where you have written permission, and capture only your own lab network's traffic. WAN labs run on Linux VMs with `tc netem`, WireGuard or strongSwan, and FRRouting; the Cisco DevNet Catalyst SD-WAN sandbox gives you a vendor platform for free.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · RF measurements and dB maths | Measure RSSI and noise at 10 points through walls; compare with free-space path loss predictions | Measurement table, predicted vs measured with explanation of the gap | 3 h |
| 2 · Channel plans and airtime | Plan 2.4/5/6 GHz channels for a 3-floor building; capture beacons and retries in a busy space | Channel plan; annotated capture with overhead percentages | 4 h |
| 3 · WPA3 and EAP-TLS | WPA3-Personal SSID; WPA3-Enterprise with EAP-TLS against FreeRADIUS or NPS using your NET302 CA; OWE guest SSID with isolation | Configs, capture of a successful EAP-TLS exchange, isolation test | 5 h |
| 4 · OpenWrt roaming | Two OpenWrt APs with 802.11k/v/r; measure roam times for a voice-like UDP stream | Roam-time table with and without 802.11r | 4 h |
| 5 · Predictive design and validation | Predictive design of one real floor; validation survey; AI-generated estimate compared with both | Design report, heatmaps or measurement grid, error table | 6 h |
| 6 · Over-the-air troubleshooting | Six planted failures (wrong PSK, expired certificate, DHCP exhaustion, DNS failure, weak signal, wrong VLAN) found from captures and client logs | Fault log with frames or log lines as evidence | 4 h |
| 7 · Path measurement and netem profiles | 24-hour latency/jitter/loss measurement of two real internet paths; 4 reusable netem profiles | Plots, profile files, one-page interpretation | 4 h |
| 8 · DIY SD-WAN | Three sites joined by WireGuard overlays over two impaired underlays; a Python controller that probes and steers voice-class traffic | Code, failover timings, logs of path changes | 6 h |
| 9 · Segmentation and breakout | Corporate, guest and POS segments carried over the overlay; local breakout for SaaS vs backhaul through HQ | Leakage tests (none allowed), latency comparison | 4 h |
| 10 · Branch templates and handover pack | Small/medium/large branch templates with BoM, diagrams, IP plan, runbooks | Handover pack another student operates from without asking questions | 5 h |

## Projects

### P1 · Wi-Fi health assessment of a real space (L1, ~6 hours)

**Real-world inspiration.** College hostels, libraries and coaching centres in Indian cities often run consumer-grade APs added one at a time; users experience "slow Wi-Fi" that is really co-channel interference and too many APs on 2.4 GHz. The space you assess is your own choice, with written permission.

**What to build.** A measured assessment of one floor or building: AP inventory, channel and power map, RSSI/SNR grid at 20+ points, channel utilisation and retry rates at 3 busy times, client-side reports, and a prioritised list of fixes with expected effect.

**Acceptance criteria**
- At least 20 measurement points with RSSI, noise, SNR and a throughput test, plotted on the floor plan.
- Every recommendation is linked to a measurement (for example, "APs 3 and 4 both on channel 6 at −62 dBm at point 12").
- If any fix is applied (with the owner's agreement), a re-test shows the change in median SNR and throughput.
- The report is under 6 pages and readable by a non-engineer owner.

**Stretch goals.** Repeat at three times of day and show the capacity limit; estimate the cost of the recommended changes.

**What it proves to an employer.** You base wireless decisions on measurements, not guesses, which is the first habit of a wireless engineer.

### P2 · DIY SD-WAN with application-aware failover (L2, ~15 hours)

**Real-world inspiration.** Pharmacy chains, bank branches and dealerships in India often combine a fibre broadband link with a 4G/5G link; commercial SD-WAN products steer applications across them by measured quality. This project rebuilds the core mechanism openly.

**What to build.** A three-site overlay (HQ plus two branches) using WireGuard or IPsec over two emulated underlays per site, FRRouting for routing, and your own controller that probes each path every second, classifies traffic (voice, business app, bulk), and steers each class to the best path that meets its SLA, with hold-down timers to prevent flapping. Include segmentation for corporate and guest traffic.

**Acceptance criteria**
- When the primary path degrades past the voice SLA (for example, jitter above 30 ms or loss above 1%), voice moves to the other path within 3 seconds; a simulated call loses no more than 2 seconds of audio packets.
- With a path flapping every 5 seconds, the controller does not change paths more than once per hold-down period (measured over 10 minutes).
- Bulk transfers continue on the cheaper path unless it fails completely.
- Guest traffic can never reach corporate prefixes (tested with 100 probes).
- A README explains the design so another student can rebuild it in under 2 hours.

**Stretch goals.** Add zero-touch provisioning for a new branch from a template; export path metrics to Prometheus and Grafana.

**What it proves to an employer.** You understand what SD-WAN products actually do under the marketing, and you can test failover with numbers.

### P3 · Hospital campus network design: wireless, wired and WAN (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** Hospitals combine some of the hardest wireless environments (metal, lead-lined rooms, dense wards) with life-critical devices and strict segmentation needs; the 2022 AIIMS Delhi incident was attributed in Parliament to improper network segmentation. The hospital below (a 300-bed hospital with two satellite clinics, illustrative) is a composite.

**What to build.** A complete design pack: requirements by area (wards, ICU, OT, OPD, imaging, admin, guest), a predictive Wi-Fi 6E/7 design using India's 2026 lower-6 GHz rules with a validated sample area (survey a comparable real space you may access), security (EAP-TLS for staff devices, OWE guest, separate segments for medical devices, CCTV and building systems), wired design with PoE and multigigabit budgets, SD-WAN to the clinics over two diverse links plus a cellular backup, SASE or firewall choice with justification, out-of-band access, and a phased rollout plan with metrics.

**Acceptance criteria**
- Every area has stated requirements (devices, applications, minimum RSSI/SNR, capacity) and the design meets them on paper; the surveyed sample area meets them in measurement or the gap is explained.
- The segmentation matrix lists every device class and every allowed flow; a lab model (Lab 9 setup) passes 100% of allowed and denied flow tests.
- WAN failover for a clinic is demonstrated in the lab: loss of the primary link moves clinical application traffic within 3 seconds, and loss of both wired links falls back to cellular for priority traffic only.
- A bill of materials with power (PoE watts per switch) and a 5-year cost estimate is included, using public list prices where available and labelled estimates elsewhere.
- A risk register lists at least 10 risks (for example, DFS events near radar, interference with medical telemetry, PoE switch failure) with mitigations.
- The design is defended to a panel in 20 minutes.

**Stretch goals.** Add a location services or asset tracking requirement and assess its impact on AP density; include an evaluation plan for a vendor's AI-driven RF management with before/after metrics.

**What it proves to an employer.** You can design an enterprise edge end to end for a demanding customer and defend every number, the work of a senior network or solutions engineer.

## Feeds into

- [NET404 Enterprise Architecture and Cloud Migration](../../year_4/NET404_enterprise_architecture_and_cloud_migration/README.md): branch and WAN designs become part of hybrid-cloud architecture and migration plans.
- [NET402 Network Security Engineering](../../year_4/NET402_network_security_engineering/README.md): 802.1X, NAC and segmentation are implemented in depth.
- [NET403 AIOps and Intent-Based Networking](../../year_4/NET403_aiops_and_intent_based_networking/README.md): wireless and WAN telemetry feed anomaly detection.
- The [OV09 Edge AI and Secure IoT](../../../../04_overlaps/OV09_edge_ai_secure_iot/README.md) overlap, for IoT onboarding and segmentation.
