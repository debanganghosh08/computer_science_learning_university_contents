# NET304 · Wireless, SD-WAN and Enterprise Networks

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 6 | 4 (≈ 120 hours) | L1 → L3 | [CS204](../../../../02_year_2_core_computer_science/semester_3/CS204_computer_networks/README.md), [CS203](../../../../02_year_2_core_computer_science/semester_3/CS203_operating_systems/README.md); [NET301](../NET301_routing_and_switching/README.md) strongly recommended | [NET404](../../year_4/NET404_enterprise_architecture_and_cloud_migration/README.md); feeds [NET402](../../year_4/NET402_network_security_engineering/README.md) |

## Why this course matters now

For most people at work, "the network" means Wi-Fi in the building and the link from their branch to the applications. Both are changing fast. IEEE published 802.11be (Wi-Fi 7) on 22 July 2025, and the next amendment, 802.11bn ("Wi-Fi 8", ultra high reliability), was in draft ballot in 2026. In India, the government delicensed the lower 6 GHz band (5925–6425 MHz) for indoor Wi-Fi in January 2026, after years of debate, so Wi-Fi 6E and Wi-Fi 7 designs with clean 6 GHz channels are now possible in Indian offices, campuses and hospitals. On the wide-area side, branches are moving from single MPLS circuits to SD-WAN over broadband, 5G and satellite links, with security delivered from the cloud (SASE). AI is already inside these products: in February 2026 Cisco described agents that "autonomously" tune RF, QoS and paths in campus and branch networks. The skills that stay with a human are the ones those agents depend on: RF physics, a design that meets requirements on paper and in a validation survey, honest measurement of WAN paths, and judging whether an "AI recommendation" actually made users' experience better.

## Learning outcomes

By the end you can:

1. **Calculate** link budgets, EIRP, free-space path loss and SNR, and **predict** coverage and capacity before deployment.
2. **Explain** 802.11 PHY and MAC behaviour (OFDMA, MU-MIMO, BSS colouring, multi-link operation) and **choose** channel widths and bands for a given density.
3. **Design** an enterprise WLAN for coverage and capacity, **validate** it with a survey, and **document** it so another engineer can maintain it.
4. **Secure** wireless with WPA3, 802.1X/EAP-TLS, protected management frames and Enhanced Open, and **detect** rogue access points.
5. **Troubleshoot** client problems over the air with packet captures and separate RF, association, authentication, DHCP and application failures.
6. **Measure** WAN paths (latency, jitter, loss) and **design** an SD-WAN with application-aware routing, segmentation and zero-touch provisioning.
7. **Plan** a migration from MPLS to SD-WAN in waves with success metrics and rollback.
8. **Compare** SASE and traditional branch security architectures and **justify** a choice for a given organisation.
9. **Evaluate** vendor AI features for RF and WAN with before/after metrics rather than dashboard claims.

## Chapters and lessons

### Chapter 1 · RF fundamentals (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Waves and units | Frequency, wavelength, dB, dBm, mW; the 3 dB and 10 dB rules | 20 dB conversions in 10 minutes, AI off |
| 1.2 Propagation | Free-space path loss, attenuation by drywall, brick, concrete, glass and metal; reflection, multipath, the Fresnel zone | Compute expected signal at 5, 15 and 30 metres through two walls |
| 1.3 Signal quality | RSSI, noise floor, SNR, interference vs noise; why −67 dBm is a common voice design target | Measure RSSI and noise with a laptop tool at 10 points; compute SNR |
| 1.4 Antennas and power | Gain, beamwidth, EIRP, why more transmit power is often worse (client asymmetry) | Calculate EIRP for 3 AP and antenna combinations |

**Check your understanding:** Why does doubling distance cost about 6 dB in free space? Why can raising AP power make roaming worse? Why is SNR a better design metric than RSSI alone?

### Chapter 2 · 802.11 from Wi-Fi 5 to Wi-Fi 7 (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Bands and channels | 2.4 GHz (channels 1, 6, 11), 5 GHz UNII bands and DFS, 6 GHz and preferred scanning channels; India's lower-6 GHz rules (2026) | Build a channel plan for 2.4, 5 and 6 GHz for a 3-floor building |
| 2.2 PHY rates | MCS, spatial streams, guard interval, channel width; why data rate is not throughput | Explain why a 1.2 Gbit/s link gives 400 Mbit/s of TCP |
| 2.3 Airtime and the MAC | CSMA/CA (from [CS204](../../../../02_year_2_core_computer_science/semester_3/CS204_computer_networks/README.md)), contention, retries, management overhead, the slow-client problem | Capture and count beacon and retry overhead in a busy room |
| 2.4 Wi-Fi 6 and 6E | OFDMA, uplink and downlink MU-MIMO, BSS colouring, target wake time for IoT | Compare a dense test with OFDMA on and off (where supported) |
| 2.5 Wi-Fi 7 and beyond | 320 MHz channels, 4096-QAM, multi-link operation (MLO), preamble puncturing; 802.11bn goals | Decide where MLO helps and where 320 MHz channels are a bad idea |

**Check your understanding:** Why are 2.4 GHz networks limited to three non-overlapping channels? Why does one slow client hurt everyone on the same channel? When is a 40 MHz channel better than an 80 MHz one?

### Chapter 3 · Wireless security (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 WPA2 to WPA3 | PSK weaknesses, SAE in WPA3-Personal, WPA3-Enterprise, transition modes and their risks; 6 GHz requires WPA3 or Enhanced Open | Configure WPA3-Personal and a transition-mode SSID; document the trade-off |
| 3.2 802.1X for Wi-Fi | EAP-TLS, PEAP, RADIUS (FreeRADIUS or Windows NPS), certificate validation on clients | Authenticate a laptop with EAP-TLS against your NET302 AD and CA |
| 3.3 Management frames and guests | Protected management frames (802.11w), Enhanced Open (OWE), captive portals, guest isolation | Build a guest SSID with OWE and client isolation; prove isolation |
| 3.4 Rogue detection | Wireless intrusion detection, rogue and evil-twin detection, containment policy and its legal limits | Detect a planted rogue AP in your own lab and write the response procedure |

**Check your understanding:** Why does PEAP without server-certificate validation give a false sense of security? Why does a WPA2/WPA3 transition SSID keep some WPA2 risks? Why must containment of rogue APs be limited to your own premises and policy?

### Chapter 4 · WLAN architectures (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Control models | Autonomous APs, controller-based (tunnelled vs local switching), cloud-managed (Juniper Mist, Cisco Meraki, HPE Aruba Networking Central) | Map one vendor's architecture: where data, control and management planes live |
| 4.2 Roaming | 802.11k, 802.11v, 802.11r (fast BSS transition), sticky clients, roaming thresholds | Measure roam time with and without 802.11r on a voice client |
| 4.3 Wired side | AP uplinks, PoE budgets (802.3at, 802.3bt), multigigabit ports, VLAN mapping, AP management VLAN | Size switch PoE and uplinks for 60 Wi-Fi 7 APs |
| 4.4 Open alternatives | OpenWrt on commodity APs, 802.11r and 802.1X with hostapd | Build a 2-AP OpenWrt network with fast roaming |

**Check your understanding:** Why do cloud-managed networks keep working when the cloud is unreachable, and what stops working? Why can 802.11r break older clients? Why does a Wi-Fi 7 AP need a multigigabit switch port?

### Chapter 5 · Wireless design and surveys (weeks 5–6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Requirements | Users, devices per user, applications (voice, video, scanners, medical devices), coverage vs capacity; "design for the weakest important client" | Write requirements for a hospital ward floor (illustrative) |
| 5.2 Predictive design | Floor plans, wall materials, AP placement, channel and power plans; free and paid tools (Ekahau and Hamina are commercial; check for free tiers) | Predictive design for a college hostel block |
| 5.3 Validation surveys | AP-on-a-stick surveys, passive vs active surveys, post-deployment validation | Survey a real floor of your building with permission; compare to prediction |
| 5.4 High density | Lecture halls, auditoriums, stadium-style seating; directional antennas, minimum data rates, band steering | Design a 600-seat auditorium |
| 5.5 Hard environments | Hospitals (metal, lead-lined rooms, medical devices), warehouses (racking), outdoor links | List the 10 risks of a hospital WLAN and the design response to each |

**Check your understanding:** Why does disabling low data rates often improve a dense network? Why must a validation survey follow every predictive design? What makes a hospital ward harder than an office floor?

### Chapter 6 · Wireless troubleshooting and assurance (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 The client journey | Probe, authentication, association, 4-way handshake, DHCP, DNS, application; where each fails | Diagnose 6 planted failures, one at each stage |
| 6.2 Over-the-air capture | Monitor mode on Linux (`iw`, Wireshark), reading 802.11 frames, retries and reason codes | Capture and explain a failed 802.1X authentication |
| 6.3 Client-side evidence | `netsh wlan show wlanreport`, macOS Wireless Diagnostics, Android Wi-Fi verbose logging | Build a "Wi-Fi is slow" checklist from client data |
| 6.4 Assurance platforms | What vendor AI assurance claims to do (root cause, RF tuning) and how to test the claims | Compare an assurance platform's root cause with your own capture for 3 incidents |

**Check your understanding:** Why are many "Wi-Fi problems" really DHCP or DNS problems? What do disassociation reason codes tell you that RSSI cannot? How would you test whether an AI assurance tool's root cause is right?

### Chapter 7 · The WAN and its links (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 MPLS from the customer's side | L3VPN, CE-PE routing, QoS classes, SLAs, cost and lead times | Read an MPLS SLA and list what it does not promise |
| 7.2 Internet and wireless links | Broadband, dedicated internet access, 4G/5G fixed wireless access, LEO satellite as backup (see NET501) | Compare link types for a rural branch on cost, latency and failure modes |
| 7.3 Measuring paths | Latency, jitter, loss, MOS for voice; active probes, `iperf3`, TWAMP concepts | Measure two real internet paths for 24 hours; plot jitter |
| 7.4 Emulating bad links | `tc netem` profiles for broadband, congested 4G and satellite | Build 4 reusable link profiles for later labs |

**Check your understanding:** Why does an MPLS SLA rarely cover the last mile? Why is jitter more harmful than latency for voice? Why should a backup link use a different physical path, not just a different provider?

### Chapter 8 · SD-WAN architecture (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Planes | Orchestrator, controllers, edges; overlay tunnels (IPsec) over any underlay; the MEF 70 SD-WAN service definition | Map Cisco Catalyst SD-WAN or Fortinet SD-WAN onto the generic model |
| 8.2 Application-aware routing | Application identification, SLA classes, path probes, steering and failover thresholds | Steer voice to the lowest-jitter path in a lab with netem impairment |
| 8.3 Zero-touch provisioning | Bootstrap, certificates, templates, what can go wrong when a device phones home | Provision a lab edge with ZTP from a template |
| 8.4 Build one yourself | A do-it-yourself overlay: WireGuard or strongSwan tunnels, FRRouting, a Python controller that probes paths and changes routes | Build a 3-site DIY SD-WAN and fail a path |

**Check your understanding:** Why does SD-WAN separate the overlay from the underlay? What can go wrong if failover thresholds are too sensitive? Why is zero-touch provisioning also a security problem?

### Chapter 9 · SD-WAN design and migration (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Topologies | Hub-and-spoke, full mesh, regional hubs; where traffic should break out to the internet | Choose a topology for 200 branches in 4 regions |
| 9.2 Segmentation | VRFs carried across the overlay for corporate, guest, POS and IoT | Carry 3 segments across your DIY overlay with no leakage |
| 9.3 Cloud access | Direct internet access vs backhaul, cloud on-ramps, SaaS path optimisation | Measure SaaS latency with backhaul vs local breakout |
| 9.4 Migration | Pilot sites, waves, coexistence with MPLS, success metrics (incidents, user experience, cost), rollback | Write a migration plan for 40 branches with metrics per wave |

**Check your understanding:** Why can local internet breakout improve SaaS performance but increase security work? Why keep MPLS during migration, and when do you turn it off? Which metric would convince a sceptical CFO?

### Chapter 10 · SASE and SSE (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 The idea | Secure access service edge: networking plus cloud-delivered security; security service edge (SWG, CASB, ZTNA, firewall as a service) | Draw the traffic path for a branch user with and without SASE |
| 10.2 ZTNA vs VPN | Per-application access based on identity and device posture vs network-level VPN access (concepts; depth in [SAR303](../../../security_architecture/year_3/SAR303_zero_trust_architecture/README.md)) | Compare access for a contractor under VPN and ZTNA |
| 10.3 Practical constraints | Points of presence near Indian cities, latency added, TLS inspection trade-offs, data residency, cost | Evaluate two SASE vendors' public PoP lists for an India-heavy workforce |
| 10.4 Single vs multi-vendor | One vendor for SD-WAN and security vs best of breed; operational ownership | Write a one-page recommendation for a mid-sized company |

**Check your understanding:** What problem does SASE solve that branch firewalls do not? Why does PoP location matter for users in tier-2 cities? What do you lose when TLS inspection is turned off, and what do you risk when it is on?

### Chapter 11 · Branch and campus design end to end (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Standard designs | Small, medium and large branch templates: WAN, switching, Wi-Fi, security, power | Write the three templates with a bill of materials |
| 11.2 IoT and building systems | CCTV, access control, building management, medical and retail devices: segmentation and onboarding | Segment CCTV and POS devices with an access policy matrix |
| 11.3 Out-of-band and power | Cellular console access, UPS sizing, PoE failure impact | Design OOB access for 50 branches |
| 11.4 Documentation and handover | Diagrams, survey reports, as-built records, runbooks | Produce a handover pack another team could operate from |

**Check your understanding:** Why should every branch look the same? Why is out-of-band access the first thing you want during a WAN outage? Why must CCTV never share a segment with point-of-sale terminals?

### Chapter 12 · AI at the enterprise edge and design review (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Automated RF management | Radio resource management, AI-driven channel and power changes, and how to measure their effect | Compare automatic RF with your static plan on interference and client SNR |
| 12.2 AI assistants for operations | Natural-language troubleshooting in vendor platforms; failure modes: confident wrong root cause, missing context about building changes | Run 5 incident tickets through an assistant and your method; compare |
| 12.3 Using AI in design | Drafting requirements, BoMs and migration plans; never trusting an AI-generated coverage estimate without a survey | Ask an assistant for an AP count for a floor; compare with your predictive design |
| 12.4 Design review | Peer review of P3 designs against requirements, risks and costs | Defend your design to a panel |

**Check your understanding:** What would convince you that an automatic RF change helped users? Why can't an assistant know that a new metal partition went up last week? What is the most dangerous number in an AI-generated BoM?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · RF measurements and dB maths | — |
| 2 | 2 | Lab 2 · Channel plans and airtime capture | — |
| 3 | 3 | Lab 3 · WPA3 and EAP-TLS | **P1 due** |
| 4 | 4 | Lab 4 · OpenWrt roaming lab | — |
| 5 | 5 | Lab 5 · Predictive design | — |
| 6 | 5 | Lab 5 (cont.) validation survey | Mid-term (AI off) |
| 7 | 6 | Lab 6 · Over-the-air troubleshooting | — |
| 8 | 7 | Lab 7 · Path measurement and netem profiles | — |
| 9 | 8 | Lab 8 · DIY SD-WAN | **P2 due** |
| 10 | 9 | Lab 9 · Segmentation and breakout | Migration plan |
| 11 | 10 | SASE evaluation exercise | — |
| 12 | 11 | Lab 10 · Branch templates and handover pack | — |
| 13 | 12 | P3 | — |
| 14 | 12 | Design review | **P3 due** |
| 15 | Review | Oral defence of P3 | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** explaining 802.11 frame fields in a capture; drafting requirements documents, BoMs and migration plans; generating netem profiles and probe scripts; summarising vendor design guides (then reading the sections). Claude, ChatGPT and Gemini work here; vendor assistants (Juniper Mist's Marvis, Cisco AI Assistant) appear in their dashboards.
- **Do without AI (drills):** dB and link-budget arithmetic; channel planning; reading a 4-way handshake in a capture; drawing SD-WAN traffic paths; the mid-term and final.
- **Verify AI output by:** a validation survey for any coverage claim; captures for any root-cause claim; measured jitter and loss before and after for any WAN claim; vendor data sheets for AP and PoE figures; the regulator's text for any channel or power rule.
- **Where AI still fails here:** assistants cannot see walls, materials or furniture, so AP counts and coverage estimates are guesses; they often apply US or EU channel and power rules to India; they repeat vendor marketing figures for Wi-Fi 7 throughput as if they were real-world numbers. In Lab 5 you ask an assistant for an AP count and channel plan for your surveyed floor and record the error against your measured design.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1–P3 | 35% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) + P3 oral defence | 30% |

**Mastery gate.** You pass when you can, without AI: (1) produce a WLAN design for an unseen floor (requirements, AP count and placement, channel and power plan, security) in 3 hours and defend every number; (2) diagnose 4 planted wireless and WAN faults from captures and measurements in 60 minutes; (3) draw and explain the traffic path, failover behaviour and security controls of an SD-WAN branch with SASE.

## Industry reality

Where this is used: every campus, office, hospital, hotel and store; retail and banking branch networks; India's growing number of global capability centres and co-working floors. Wi-Fi 6E and Wi-Fi 7 adoption in India depends on the 2026 6 GHz rules. Cisco's CCNP Wireless and the vendor-neutral CWNP certifications (CWNA) cover this field.

**Interview questions from this course**

1. *Users on the third floor complain Wi-Fi is slow at lunch. How do you investigate?* Strong answer: separates coverage, interference, capacity (airtime, client count, slow clients) and wired causes; checks channel utilisation and retries; captures if needed; proposes design changes, not just more APs.
2. *Design Wi-Fi for a 400-seat lecture hall.* Strong answer: capacity-led design, devices per seat, 5 and 6 GHz with narrower channels, directional or under-seat APs, minimum data rates, band steering, validation survey.
3. *Why WPA3-Enterprise with EAP-TLS instead of PEAP?* Strong answer: mutual certificate authentication, no passwords to phish, server validation; operational cost of certificates and how to manage it with MDM.
4. *How does SD-WAN decide which path a video call takes?* Strong answer: application identification, SLA classes, continuous probes for latency, jitter and loss, thresholds and hold-down timers, failover and fail-back behaviour.
5. *We are replacing MPLS at 150 branches. What is your plan?* Strong answer: baseline measurements, pilot sites, waves, coexistence, segmentation, security for local breakout (SASE or branch firewalls), success metrics, rollback, contract timing.

## Resources (free first)

- **Standards and regulation:** IEEE 802.11 working group — https://www.ieee802.org/11/ ; Wi-Fi Alliance — https://www.wi-fi.org/ ; Department of Telecommunications, India — https://dot.gov.in/
- **Vendor design guides (free):** Cisco Catalyst SD-WAN design guide and wireless design guides — https://www.cisco.com/c/en/us/solutions/design-zone.html ; Juniper Mist documentation — https://www.juniper.net/documentation/product/us/en/mist/ ; HPE Aruba Networking validated solution guides — https://arubanetworking.hpe.com/techdocs/VSG/
- **Open tools:** OpenWrt — https://openwrt.org/ ; hostapd — https://w1.fi/hostapd/ ; FreeRADIUS — https://www.freeradius.org/ ; Wireshark 802.11 capture setup — https://wiki.wireshark.org/CaptureSetup/WLAN ; WireGuard — https://www.wireguard.com/ ; strongSwan — https://strongswan.org/ ; Mininet-WiFi — https://mininet-wifi.github.io/
- **Free practice:** Cisco DevNet sandboxes (Catalyst SD-WAN) — https://developer.cisco.com/site/sandbox/
- **Paid, optional:** CWNA study guide (CWNP); Ekahau or Hamina survey tools for professional survey work.

## Sources

- IEEE 802.11 working group page: 802.11be-2024 "published on July 22, 2025"; TGbn (Wi-Fi 8) D2.0 initial ballot — https://www.ieee802.org/11/ (checked 2026-10)
- Indian Infrastructure, "Centre delicenses 6 GHz spectrum band for indoor Wi-Fi use" (22 Jan 2026) — https://indianinfrastructure.com/?p=265331 ; draft rules of May 2025 reported by The Week — https://www.theweek.in/wire-updates/business/2025/05/19/dcm89-biz-dot-spectrum-wifi.html (checked 2026-10)
- Cisco newsroom, "Cisco Expands AgenticOps Innovations Across Portfolio" (10 Feb 2026): "autonomously tuning RF, QoS, path, and control planes" — https://newsroom.cisco.com/content/r/newsroom/en/us/a/y2026/m02/cisco-expands-agenticops-innovations-across-portfolio.html (checked 2026-10)
- Cisco certifications page (CCNP Wireless) — https://www.cisco.com/site/us/en/learn/training-certifications/certifications/index.html (checked 2026-10)

_Last reviewed: 2026-10_
