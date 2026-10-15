# NET402 · Network Security Engineering

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 7 | 4 (≈ 120 hours) | L2 → L4 | [NET302](../../year_3/NET302_windows_server_active_directory_and_enterprise/README.md); [NET301](../../year_3/NET301_routing_and_switching/README.md) and [CS213](../../../../02_year_2_core_computer_science/semester_4/CS213_security_foundations/README.md) assumed | [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) capstones; complements [SEC301](../../../cybersecurity_defense/year_3/SEC301_network_security_and_defense/README.md) and [SAR303](../../../security_architecture/year_3/SAR303_zero_trust_architecture/README.md) |

This course is defensive. It teaches how to design, build, operate and verify network security controls. All testing happens in your own lab or under written authorisation. It complements SEC301, which focuses on monitoring and detection (Suricata, Zeek, packet analysis); here you engineer the controls those analysts depend on.

## Why this course matters now

Network devices are now targets in their own right. In December 2024, CISA, the NSA, the FBI and partner agencies in Australia, Canada and New Zealand published hardening guidance for communications infrastructure after intrusions into telecom networks; its first recommendations were basic engineering: an out-of-band management network, default-deny access lists, disabling unused and plaintext services, and SNMPv3 only. In India, the government's reply in Parliament on the November 2022 AIIMS Delhi ransomware attack said servers were compromised "due to improper network segmentation". CERT-In's 2022 directions require organisations to report specified incidents within 6 hours and keep logs of their ICT systems for a rolling 180 days within India, which makes logging design a legal requirement rather than an option. Even core protocols need attention: the 2024 "BlastRADIUS" research showed that RADIUS over UDP could be forged in some deployments unless the Message-Authenticator attribute is enforced. AI assistants now draft firewall rules and explain policies, and vendors build assistants into their firewall managers, but a rule that is "almost right" is an open door. Employers need engineers who can design segmentation, keep a firewall policy clean for years, roll out 802.1X without locking out a hospital, and prove with evidence that the controls work.

## Learning outcomes

By the end you can:

1. **Harden** routers, switches and firewalls across the management, control and data planes, and **audit** them against CISA and CIS guidance.
2. **Design** firewall policy with zones, default deny and clear ownership, and **operate** its lifecycle: requests, review, recertification and cleanup.
3. **Configure** NGFW features (application and user identity, IPS, URL filtering, TLS decryption with exceptions) and **justify** where each belongs.
4. **Design and test** segmentation (VRFs, east-west firewalls, microsegmentation), with a segmentation matrix and evidence that only allowed flows pass.
5. **Deploy** 802.1X with EAP-TLS and MAC authentication bypass in phases, and **secure** the RADIUS infrastructure itself.
6. **Design** site-to-site and remote-access VPNs (IKEv2, WireGuard), and **plan** the move to zero trust network access.
7. **Explain** DDoS attack classes at a conceptual level and **prepare** defences: upstream scrubbing, RTBH, Flowspec, rate limits and an ISP runbook.
8. **Design** logging from network controls into a SIEM that meets CERT-In retention and time-sync requirements, and **hand off** useful detections to a SOC.
9. **Analyse** firewall and ACL policy with tools such as Batfish, and **review** AI-drafted rules for over-permissive or shadowed entries.

## Chapters and lessons

### Chapter 1 · The defensive engineer's view (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Threats to infrastructure | Why network devices and VPN gateways are targets; what CISA's December 2024 guidance says and why | Build a threat model for your NET301 lab network |
| 1.2 Principles | Defence in depth, least privilege, default deny, zero trust tenets (NIST SP 800-207) applied to networks | Map each principle to one control in your lab |
| 1.3 Rules of engagement | Authorisation, scope, testing only your own assets; Indian law (IT Act, CERT-In directions) | Write a lab testing authorisation and scope document |
| 1.4 Where this course sits | SEC301 (monitoring), SAR303 (zero trust architecture), SEC302 (SOC); the network engineer's part | Draw who owns which control in a mid-sized company |

**Check your understanding:** Why are edge VPN appliances high-value targets? What does default deny change about how you write rules? Why is written scope required even in a lab you share with others?

### Chapter 2 · Hardening the network itself (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Management plane | Out-of-band management, SSH only, AAA with TACACS+ or RADIUS, per-user accounts, command authorisation and accounting, local fallback | Configure TACACS+ (open-source tac_plus) with command logging |
| 2.2 Control plane | Control-plane policing, routing-protocol authentication, GTSM, BGP max-prefix | Protect a router's control plane from a lab traffic flood |
| 2.3 Data plane | Infrastructure ACLs, anti-spoofing with uRPF (BCP 38), disabling unused services and protocols | Apply BCP 38 filtering at your lab edge and prove spoofed sources are dropped |
| 2.4 Lifecycle | Firmware integrity, patching edge devices, tracking actively exploited vulnerabilities (CISA KEV catalogue), end-of-life replacement | Build a patch-priority list for a mixed estate using the KEV catalogue |
| 2.5 Auditing | CIS Benchmarks for network devices, configuration compliance as code (from NET303) | Audit lab devices against 15 hardening rules automatically |

**Check your understanding:** Why does out-of-band management reduce risk even when in-band access is encrypted? What attack does uRPF prevent, and where can it break legitimate traffic? Why should edge devices be patched on a faster cycle than internal switches?

### Chapter 3 · Firewall fundamentals and policy design (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Stateful inspection | Connection tracking, state tables, timeouts, how NAT order interacts with rules | Trace a flow through an OPNsense or nftables firewall step by step |
| 3.2 Zones and rule design | Zone-based policy, object groups, rule ordering, explicit deny with logging; NIST SP 800-41 | Design a zone model and 20-rule policy for a branch |
| 3.3 Asymmetry and HA | Asymmetric routing and stateful firewalls, active/passive and active/active clusters, state sync | Break and fix asymmetric routing through a firewall pair |
| 3.4 Host firewalls | `nftables` and Windows Defender Firewall managed by policy as a second layer | Apply host firewall rules to servers through GPO and Ansible |

**Check your understanding:** Why does a stateful firewall drop the return traffic of an asymmetric flow? Why should the last rule be an explicit, logged deny? When is a host firewall the only control that sees east-west traffic?

### Chapter 4 · Next-generation firewall capabilities (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Application and user identity | Application signatures vs ports, user-ID from AD or identity providers | Write rules by application and group instead of port and IP |
| 4.2 Intrusion prevention | Signature and anomaly-based prevention inline; tuning to avoid blocking business traffic | Enable an IPS profile in a lab and tune 3 false positives |
| 4.3 TLS decryption | How inspection works, certificate deployment, exceptions for health, banking and personal data, performance cost, legal and privacy questions | Write a decryption policy with exceptions and a privacy justification |
| 4.4 Placement | Internet edge, data-centre core, cloud, branch; what each NGFW feature is worth where | Decide which features to enable at 4 locations and why |

**Check your understanding:** Why are port-based rules weak against modern applications? What is lost if you do not decrypt, and what is risked if you do? Why might IPS be turned on in detect-only mode first?

### Chapter 5 · Policy lifecycle and policy as code (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Requests and ownership | Rule requests through ITSM (NET305), business owner, expiry dates | Process 10 rule requests, rejecting the unsafe ones with reasons |
| 5.2 Hygiene | Shadowed, redundant, overly broad and unused rules; hit counts; recertification | Clean a 200-rule policy with planted problems; document each removal |
| 5.3 Analysis tools | Batfish for ACL and firewall analysis: which flows are allowed, what a change will alter | Prove a proposed change permits only the requested flow |
| 5.4 Policy as code | Rules in Git, review, CI checks, deployment through APIs | Move a lab firewall's policy into Git with a CI check that blocks "any-any" |
| 5.5 Reviewing AI-drafted rules | Typical defects: overly broad objects, wrong direction, wrong NAT stage, ignoring existing deny rules | Review 10 AI-drafted rules with Batfish; log each defect |

**Check your understanding:** Why do firewall policies grow without limit unless rules have owners and expiry? What does a shadowed rule tell you about a policy's history? Why must analysis consider NAT before deciding whether a flow is allowed?

### Chapter 6 · Segmentation (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Macro-segmentation | VLANs and VRFs, east-west firewalls between zones, carrying segments across campus, WAN and fabric | Separate user, server, management, IoT and guest zones in the lab |
| 6.2 Microsegmentation | Host-based policy, hypervisor-level policy, identity or tag-based policy (for example group tags) | Restrict a 3-tier application so only required tiers talk |
| 6.3 The segmentation matrix | Every source zone × destination zone × allowed service, with owners | Write the matrix for a hospital (illustrative) |
| 6.4 Testing segmentation | Automated allowed/denied flow tests from inside each zone, using only your own lab | Run 500 flow tests; reconcile any unexpected result |
| 6.5 Lessons | AIIMS Delhi 2022 (improper segmentation); IoT and building systems on flat networks | Write what a segmentation review should have flagged |

**Check your understanding:** Why does a flat network turn one compromised server into a whole-organisation incident? What does microsegmentation give you that VLANs cannot? Why must segmentation be tested continuously, not once?

### Chapter 7 · Network access control and 802.1X (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 802.1X roles | Supplicant, authenticator, authentication server; EAP methods (EAP-TLS preferred) with certificates from your NET302 CA | Wired 802.1X with EAP-TLS against FreeRADIUS |
| 7.2 Headless devices | MAC authentication bypass (MAB), profiling, its weakness, compensating controls | Put printers and cameras into a restricted segment by MAB |
| 7.3 Authorisation results | Dynamic VLANs, downloadable ACLs, change of authorisation (CoA), posture concepts | Move a non-compliant laptop to a remediation VLAN automatically |
| 7.4 Rollout without outages | Monitor mode → low-impact mode → closed mode; fallback when RADIUS is unreachable | Plan a phased rollout for 3,000 ports with success criteria per phase |
| 7.5 Securing RADIUS and links | BlastRADIUS (CVE-2024-3596): require Message-Authenticator, prefer RADIUS over TLS (RadSec); MACsec (802.1AE) for link encryption | Enforce Message-Authenticator and RadSec in the lab; verify with captures |

**Check your understanding:** Why is MAB the weakest part of most NAC deployments? Why start 802.1X in monitor mode? What did BlastRADIUS change about how RADIUS should be deployed?

### Chapter 8 · VPN design (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Site-to-site IPsec | IKEv2 (RFC 7296), proposals, PFS, AES-GCM, route-based vs policy-based VPNs, dead-peer detection | Build route-based IKEv2 tunnels between two sites with BGP over them |
| 8.2 Post-quantum readiness | Hybrid key exchange in IKEv2 (RFC 9370), crypto agility, inventory of VPN crypto | Inventory the crypto in your lab VPNs and rate migration effort |
| 8.3 WireGuard | Simple modern design, key distribution, where it fits and where enterprise features are missing | Compare WireGuard and IPsec for a 20-site design |
| 8.4 Remote access | TLS and IPsec remote-access VPNs, MFA, split vs full tunnel, device posture | Configure remote access with MFA on an open-source VPN |
| 8.5 Edge exposure | Why internet-facing VPN gateways are frequent targets; reducing exposure; patch cadence; migration to ZTNA | Write an exposure-reduction plan for a VPN concentrator |

**Check your understanding:** Why are route-based VPNs easier to run at scale? What does crypto agility mean for a VPN estate expected to last 10 years? Why does ZTNA reduce the impact of a stolen VPN credential?

### Chapter 9 · DDoS protection (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Attack classes (concepts) | Volumetric, protocol (state exhaustion) and application-layer attacks; reflection and amplification as concepts | Classify 6 public incident descriptions by type |
| 9.2 Upstream defences | ISP and cloud scrubbing, anycast absorption, remotely triggered blackholing with the BLACKHOLE community (RFC 7999), BGP Flowspec (RFC 8955) | Configure RTBH signalling to a simulated ISP in the lab |
| 9.3 Local defences | Rate limits, SYN cookies, connection limits on firewalls and load balancers, protecting the firewall's own state table | Tune state-table limits under a lab load test against your own server |
| 9.4 The runbook | Contacts, thresholds, decision points, communication with ISPs and CERT-In when required | Write and tabletop a DDoS runbook |

**Check your understanding:** Why can't an on-premises firewall stop a volumetric attack larger than the internet link? What does RTBH sacrifice to save the rest of the network? Why must the ISP contacts be tested before an attack?

### Chapter 10 · Logging, visibility and SIEM integration (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 What to log | Firewall allow/deny, NAC decisions, VPN sessions, admin commands, configuration changes, flow records | Write a logging standard by device type |
| 10.2 Getting logs there reliably | Syslog over TLS (RFC 5425), NTP sync to NIC or NPL sources (CERT-In), buffering, loss detection | Prove no log loss during a collector restart |
| 10.3 Normalising and storing | Parsing to a common schema (for example Elastic Common Schema), 180-day retention within India, storage sizing | Size storage for 180 days of logs from 500 devices |
| 10.4 Feeding the SOC | Use cases a SOC needs from network controls (admin login from a new source, mass denies, VPN anomalies), alert hand-off ([SEC302](../../../cybersecurity_defense/year_3/SEC302_security_operations_soc_siem_and_monitoring/README.md)) | Ship lab logs to Wazuh or Elastic and build 5 detections |

**Check your understanding:** Why is time synchronisation a security control? How do you know logs are not being silently dropped? Which network log would you keep if you could keep only one?

### Chapter 11 · Privileged, third-party and zero trust access (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Admin access paths | Bastion hosts, privileged access management, session recording, just-in-time access | Force all device administration through one logged bastion |
| 11.2 Vendor access | Time-bound, monitored vendor sessions; contracts and evidence | Design vendor access for a firewall support contract |
| 11.3 ZTNA in practice | Identity- and device-aware access per application; integration with NET302 identity and NET304 SASE | Replace VPN access to one internal app with an open-source identity-aware proxy |
| 11.4 Measuring exposure | External attack surface of your own organisation; reducing open ports and services | Inventory and reduce the lab's externally reachable services |

**Check your understanding:** Why should vendor access expire automatically? What does a bastion give you during an incident investigation? Which applications are hardest to move behind ZTNA, and why?

### Chapter 12 · Verification, audit and AI (weeks 12–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Control validation | Configuration audits, segmentation tests, NAC tests, log-coverage tests, all on your own lab | Run a full validation suite and produce an evidence pack |
| 12.2 Audits and compliance | Mapping controls to CIS Controls, CERT-In directions, RBI IT governance directions and PCI DSS segmentation requirements | Map your controls to two frameworks |
| 12.3 Edge compromise tabletop | Assume a VPN gateway is compromised: containment, evidence, reporting, rebuild | Run the tabletop with SOC and network roles |
| 12.4 AI in network security engineering | Assistants for policy analysis and rule drafting; failure modes (over-broad suggestions, ignored NAT, invented features); guardrails: Batfish and CI checks before any rule ships | Evaluate an assistant on 15 policy tasks with Batfish as the judge |
| 12.5 Capstone review | Peer review of P3 designs and evidence | Defend your evidence pack to a panel |

**Check your understanding:** What is the difference between a control existing and a control working? Why must AI-drafted rules pass the same automated analysis as human ones? What would you report to CERT-In and when, in the tabletop scenario?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Threat model and scope | Authorisation document |
| 2 | 2 | Lab 2 · Device hardening and AAA | — |
| 3 | 3 | Lab 3 · Firewall policy and HA | **P1 due** |
| 4 | 4 | Lab 4 · NGFW features and decryption policy | — |
| 5 | 5 | Lab 5 · Policy cleanup and policy as code | — |
| 6 | 6 | Lab 6 · Segmentation and flow tests | Mid-term (AI off) |
| 7 | 7 | Lab 7 · 802.1X, MAB and RadSec | — |
| 8 | 8 | Lab 8 · IKEv2, WireGuard and remote access | — |
| 9 | 9 | Lab 9 · RTBH and DDoS runbook | **P2 due** |
| 10 | 10 | Lab 10 · Logging to SIEM | — |
| 11 | 11 | Bastion and ZTNA exercise | — |
| 12 | 12 | Validation suite and tabletop | — |
| 13 | 12 | P3 | AI evaluation report |
| 14 | 12 | Capstone review | **P3 due** |
| 15 | Review | Oral defence of P3 | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** explaining a policy or a log line; drafting rule requests, decryption-exception justifications and runbooks; generating flow-test scripts; summarising vendor hardening guides (then reading the cited sections). Vendor assistants in firewall managers, Microsoft Security Copilot, Claude and ChatGPT are all usable within your organisation's data rules.
- **Do without AI (drills):** writing a zone policy from requirements; reading a stateful flow trace with NAT; designing the segmentation matrix; planning an 802.1X rollout; the mid-term and final.
- **Verify AI output by:** Batfish analysis of every proposed rule; allowed/denied flow tests in the lab; captures for VPN and RADIUS claims; vendor documentation and primary guidance (CISA, NIST, CERT-In) for every hardening claim.
- **Where AI still fails here:** assistants propose broad objects ("any" service, large subnets) to make something work, misplace rules relative to NAT, and describe features from the wrong product version. Never paste real configurations, keys or logs into an external AI service without approval. In Lab 5 and Chapter 12 you measure this: a defect table for AI-drafted rules, judged by Batfish.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1–P3 | 35% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) + P3 oral defence | 30% |

**Mastery gate.** You pass when you can, without AI: (1) design zones, a segmentation matrix and a firewall policy for an unseen organisation in 2 hours, and prove with flow tests that only allowed flows pass; (2) harden a router and a switch to a 15-point standard and show the audit evidence; (3) plan an 802.1X rollout and a VPN design for the same organisation, with phases, fallbacks and logging that meet CERT-In requirements.

## Industry reality

Where this is used: every enterprise and public-sector network; managed security and network service providers in India serving global clients; telecom operators responding to the 2024 hardening guidance; banks under RBI directions. Network security engineers, firewall engineers and NAC engineers are distinct roles in large organisations, and the work is a common route from infrastructure into security (ISC2's 2025 study found 38% of security professionals aged 21–29 entered through IT).

**Interview questions from this course**

1. *Design segmentation for a hospital network.* Strong answer: zones for clinical systems, medical devices, IoT/building, users, guests, management; a matrix of allowed flows; east-west firewalls or microsegmentation; NAC for device placement; testing; references the AIIMS lesson.
2. *A rule request asks for "any to the database server on all ports". What do you do?* Strong answer: find the real flows (application owner, logs), propose specific source/destination/service, time limit, owner, logging; analyse with tooling; escalate if pushed.
3. *How would you roll out 802.1X to 5,000 wired ports?* Strong answer: certificates and MDM first, monitor mode with reporting, MAB plus profiling for headless devices, low-impact then closed mode by site, RADIUS redundancy and fallback, help-desk readiness, metrics per phase.
4. *Our VPN gateway is internet-facing and a critical vulnerability was announced today. What now?* Strong answer: check exposure and KEV status, apply vendor mitigations or patch on an emergency change, look for signs of compromise with the SOC, credential resets if indicated, plan to reduce exposure (ZTNA), report as required.
5. *What should a firewall log to the SIEM and how long do you keep it in India?* Strong answer: allow and deny decisions with identity and application, admin actions, configuration changes, VPN sessions; reliable transport, NTP to NIC/NPL-traceable sources, 180-day rolling retention in India per CERT-In; storage sizing.

## Resources (free first)

- **Guidance:** CISA et al., Enhanced Visibility and Hardening Guidance for Communications Infrastructure (Dec 2024) — https://www.cisa.gov/resources-tools/resources/enhanced-visibility-and-hardening-guidance-communications-infrastructure ; CISA Known Exploited Vulnerabilities catalogue — https://www.cisa.gov/known-exploited-vulnerabilities-catalog ; NIST SP 800-41 Rev. 1 (firewalls) — https://csrc.nist.gov/pubs/sp/800/41/r1/final ; NIST SP 800-207 (zero trust) — https://csrc.nist.gov/pubs/sp/800/207/final ; NIST SP 800-77 Rev. 1 (IPsec VPNs) — https://csrc.nist.gov/pubs/sp/800/77/r1/final ; CIS Benchmarks — https://www.cisecurity.org/cis-benchmarks
- **India:** CERT-In Directions (28 Apr 2022) — https://www.cert-in.org.in/PDF/CERT-In_Directions_70B_28.04.2022.pdf
- **Standards:** RFC 7296 (IKEv2), RFC 9370 (multiple key exchanges in IKEv2), RFC 2827 (BCP 38), RFC 7999 (BLACKHOLE community), RFC 8955 (Flowspec), RFC 5425 (syslog over TLS), RFC 6614 (RADIUS over TLS) — https://www.rfc-editor.org/
- **Open-source tools:** OPNsense — https://docs.opnsense.org/ ; nftables — https://wiki.nftables.org/ ; FreeRADIUS — https://www.freeradius.org/ ; PacketFence — https://www.packetfence.org/ ; WireGuard — https://www.wireguard.com/ ; strongSwan — https://strongswan.org/ ; Batfish — https://batfish.org/ ; Wazuh — https://documentation.wazuh.com/
- **Research:** BlastRADIUS (CVE-2024-3596) — https://www.blastradius.fail/
- **Practice (legal environments):** your own Containerlab and VM labs; for attacker perspective, only authorised platforms listed in [SEC301](../../../cybersecurity_defense/year_3/SEC301_network_security_and_defense/README.md).

## Sources

- CISA, NSA, FBI, ASD's ACSC, CCCS and NCSC-NZ, "Enhanced Visibility and Hardening Guidance for Communications Infrastructure" (3–4 Dec 2024) — https://www.cisa.gov/resources-tools/resources/enhanced-visibility-and-hardening-guidance-communications-infrastructure (checked 2026-10)
- The Wire, government reply in Rajya Sabha on the AIIMS cyberattack (Dec 2022) — https://thewire.in/government/aiims-servers-cyberattack-ransomware-rajya-sabha (checked 2026-10)
- CERT-In Directions under section 70B(6), 28 April 2022 (6-hour reporting, 180-day logs within India, NTP to NIC/NPL) — https://www.cert-in.org.in/PDF/CERT-In_Directions_70B_28.04.2022.pdf (checked 2026-10)
- BlastRADIUS disclosure, CVE-2024-3596 (Jul 2024) — https://www.blastradius.fail/ (checked 2026-10)
- ISC2, 2025 Cybersecurity Workforce Study (38% of professionals aged 21–29 entered via IT), as summarised in the [NET market page](../../../../06_career_and_market_readiness/01_market_map/roles/NET_it_infrastructure_networking.md) — https://www.isc2.org/Insights/2025/12/2025-ISC2-Cybersecurity-Workforce-Study (checked 2026-10)

_Last reviewed: 2026-10_
