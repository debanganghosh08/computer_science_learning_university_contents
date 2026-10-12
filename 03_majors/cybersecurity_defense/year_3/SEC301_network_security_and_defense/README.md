# SEC301 · Network Security and Defense

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 5 | 4 (≈ 120 hours) | L2 → L3 | [CS213](../../../../02_year_2_core_computer_science/semester_4/CS213_security_foundations/README.md) (and [CS204](../../../../02_year_2_core_computer_science/semester_3/CS204_computer_networks/README.md) through it) | [SEC401](../../year_4/SEC401_detection_engineering_and_threat_hunting/README.md), [SEC302](../SEC302_security_operations_soc_siem_and_monitoring/README.md) (pairs with it), [OV01 Cloud Security](../../../../04_overlaps/OV01_cloud_security/README.md) |

Part of the [Cybersecurity Defense major](../../README.md). This course is **defensive**. You capture and analyse traffic only on networks you own (your home lab) or in legal training environments and published training captures. Capturing other people's traffic without authorization is an offence under the IT Act, 2000 in India and similar laws elsewhere.

## Why this course matters now

Networks are where many intrusions start and where defenders still see the most. In Mandiant's M-Trends 2026, exploits were the top way in for the sixth year running (32% of intrusions), often before a patch existed, and the targets are frequently edge devices: in September 2025 CISA's Emergency Directive 25-03 ordered US agencies to hunt for Cisco ASA firewall implants that survived reboots and upgrades. In India, the government told Parliament that the 2022 ransomware attack on AIIMS Delhi (about 1.3 TB encrypted on five servers) happened "due to improper network segmentation". As TLS 1.3, QUIC and encrypted DNS spread, defenders increasingly work from metadata: Zeek logs, flow records, certificates and fingerprints. AI tools now summarise alerts and logs (Security Onion added an "Onion AI" assistant in 2025–26), but a person still has to design segmentation, decide what to log, read the packet capture when the summary is wrong, and tune detections so analysts are not drowned.

## Learning outcomes

By the end you can:

1. **Build** a working network security monitoring (NSM) lab with a firewall, Suricata, Zeek and a search interface, and **explain** where each sensor sees traffic.
2. **Analyse** packet captures with Wireshark and `tshark` to reconstruct what happened, using display filters, stream reassembly and protocol fields.
3. **Design** network segmentation (zones, DMZ, management network, egress rules) for a stated business, and **audit** an existing firewall rule base for shadowed, overly broad and unused rules.
4. **Write, test and tune** Suricata rules and Zeek scripts against your own captures, and **measure** their false-positive rate on baseline traffic.
5. **Detect** suspicious patterns in Zeek and flow logs (rare destinations, long connections, beaconing, unusual DNS) and **explain** benign causes of each.
6. **Secure** DNS and email-related DNS records (protective DNS, response policy zones, DNSSEC, SPF/DKIM/DMARC) and **explain** the visibility trade-offs of DNS over HTTPS.
7. **Explain** what defenders can and cannot see in TLS 1.3, QUIC and Encrypted Client Hello traffic, and **choose** between TLS inspection and metadata analysis for a given legal and privacy context.
8. **Size** sensor storage and retention for a stated network and legal requirement (for example CERT-In's 180-day log retention).
9. **Contain** a network-level incident (quarantine, sinkhole, egress block) while preserving evidence, and **verify** AI-generated rules and log summaries against raw evidence.

## Chapters and lessons

### Chapter 1 · The defender's view of a network (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 What defenders defend | Assets, trust boundaries, north-south vs east-west traffic; why "inside" is not trusted (NIST SP 800-207 recap from CS213) | Draw your home network with every trust boundary marked |
| 1.2 Where you can see traffic | Network TAP vs SPAN/mirror port, packet loss on SPAN, host-based capture, cloud traffic mirroring | Place three sensors on a given campus diagram and justify each |
| 1.3 The four kinds of network evidence | Full packet capture (PCAP), flow records (NetFlow v9/IPFIX), protocol logs (Zeek), device logs (firewall, VPN, proxy, DNS) | For one web visit, list what each evidence type would record |
| 1.4 Building the lab and its inventory | OPNsense or pfSense firewall, Security Onion 3 (released March 2026; 2.4 reached end of life on 1 Oct 2026), two client VMs; passive inventory from Zeek and DHCP logs vs Nmap scans of *your own* lab | Deploy the lab, prove the sensor sees client traffic, and compare the two inventories |

**Check your understanding:** Why can a SPAN port silently drop packets during a busy hour, and how would you notice? Which evidence type would still be useful three months after an incident, and why? Why is passive inventory safer on a production network than active scanning?

### Chapter 2 · Packet analysis for defenders (weeks 1–2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Wireshark and tshark | Capture vs display filters, coloring rules, Follow TCP/HTTP stream, Statistics → Conversations and Protocol Hierarchy | Answer 10 questions about a training capture using only filters |
| 2.2 TCP/IP in practice | Handshakes, resets, retransmissions, window sizes; reading a slow connection vs a refused one | Diagnose three "the network is broken" captures |
| 2.3 Application protocols | HTTP/1.1 and HTTP/2 headers, DNS queries and answers, TLS ClientHello (SNI, ALPN) and certificates, SMB and RDP at a high level, cleartext credentials in legacy protocols | Find every cleartext credential in a lab capture of FTP and HTTP basic auth you generated |
| 2.4 Working from published training captures | Malware-Traffic-Analysis.net exercises; writing an incident note from a PCAP | Complete two exercises and write a one-page note each |

**Check your understanding:** Why is a display filter safer than a capture filter during an investigation? What does an RST immediately after a SYN tell you, and what does it not? Which TLS fields stay visible in TLS 1.3, and which moved inside the encryption?

### Chapter 3 · Segmentation and firewall design (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Zones and trust | User, server, DMZ, management, OT/medical device and guest zones; default deny; why flat networks let ransomware spread | Design zones for a 500-bed hospital (illustrative scenario, inspired by the AIIMS 2022 finding) |
| 3.2 Stateful firewalls and NGFWs | Stateful inspection, application identification, user-ID, URL categories; NIST SP 800-41 Rev. 1 | Write the rule matrix for 3.1 as source-zone × destination-zone × service |
| 3.3 Egress filtering | Why outbound control matters (command-and-control, exfiltration); proxy-only internet for servers | Block direct internet from the server zone and prove updates still work through a proxy |
| 3.4 Host and micro-segmentation | `nftables`, Windows Defender Firewall with GPO/Intune, identity-based micro-segmentation | Enforce host firewall rules on two lab VMs; test with `nc` |
| 3.5 Rule-base audits | Shadowed rules, any-any rules, unused rules from hit counts, rule owners and expiry dates, change control | Audit a provided 60-rule export and write findings with severity |

**Check your understanding:** Why does segmentation reduce the blast radius even when it does not stop the initial compromise? When is a rule with zero hits in 90 days still needed? What is the risk of allowing ICMP everywhere, and of blocking it everywhere?

### Chapter 4 · Remote access, VPNs and edge devices (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 VPN technologies | IPsec/IKEv2, WireGuard, SSL/TLS VPNs; split vs full tunnel | Build a WireGuard site-to-site tunnel between two lab networks |
| 4.2 Edge devices as targets | Why firewalls and VPN gateways are attacked first: internet-facing, privileged, poorly monitored; CISA ED 24-01 (Ivanti, 2024) and ED 25-03 (Cisco ASA, 2025) as case studies | Summarise ED 25-03's required actions as a checklist for a bank |
| 4.3 Hardening and monitoring the edge | Management interfaces off the internet, MFA, configuration backups and diffing, firmware integrity checks, sending device logs off-box | Write a hardening and logging standard for your lab firewall |
| 4.4 Zero trust network access | ZTNA vs VPN, per-application access, device posture; what ZTNA does not fix | Compare VPN and ZTNA for a 200-person company in a one-page memo |

**Check your understanding:** Why might patching an edge device not remove an existing compromise? What would you log on a VPN gateway to detect stolen credentials? Why is "the appliance is a black box" an unacceptable answer for a defender?

### Chapter 5 · Intrusion detection and prevention with Suricata (weeks 5–6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 How signature IDS works | Packet acquisition (AF_PACKET), flow tracking, protocol parsers, rule matching; IDS vs IPS mode and the cost of a false block | Run Suricata 8 on your sensor; read its `stats.log` for drops |
| 5.2 Rule anatomy | Action, header, `flow`, `content`, sticky buffers (`http.uri`, `dns.query`, `tls.sni`), `metadata`, `sid`/`rev`; Emerging Threats Open ruleset | Explain five ET Open rules line by line |
| 5.3 Writing policy rules | Detect policy violations in your own lab: cleartext FTP logins, TLS 1.0, DNS to unapproved resolvers, unexpected SMB to the internet | Write and test five rules against captures you created |
| 5.4 EVE JSON and alert context | Alert, flow, DNS, TLS and file events; `community_id` to join Suricata and Zeek records | Join one alert to its Zeek connection record by Community ID |
| 5.5 Tuning | Thresholds, suppressions, disabling noisy rules, `suricata-update` sources, measuring alerts per day per rule | Cut a noisy default ruleset's alert volume by 80% without losing your five test detections |

**Check your understanding:** Why is IPS mode riskier for availability than IDS mode? A rule fires 4,000 times a day and has never caught anything real: what are your three options and their costs? Why should every custom rule come with a test capture?

### Chapter 6 · Network security monitoring with Zeek (weeks 6–7)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Zeek's model | Event-driven analysis; `conn`, `dns`, `http`, `ssl`, `x509`, `files`, `notice` and `weird` logs; Zeek 8 LTS | Map one browsing session across five Zeek logs |
| 6.2 Hunting in Zeek logs | Stacking (count by value, look at the rare tail), top talkers, long connections, bytes out vs bytes in | Find the three rarest destinations in a week of lab traffic and explain each |
| 6.3 Beaconing | Regular intervals and similar sizes as a signal; jitter; why update checkers look the same; RITA-style scoring | Score beacon likelihood for all hosts and label false positives |
| 6.4 Zeek scripting, files and certificates | Event handlers, tables, `NOTICE`, the package manager; file hashes from `files.log`; certificate issuer anomalies | Write a script that raises a notice on a new self-signed certificate |

**Check your understanding:** Why is "rare" not the same as "malicious"? Which Zeek fields let you detect large outbound transfers without decrypting anything? How would a defender tell a backup job from data exfiltration?

### Chapter 7 · DNS and email-related DNS security (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 DNS as a control point | Recursive resolvers, logging queries, response policy zones (RPZ), protective DNS services | Configure an RPZ in Unbound or BIND that sinkholes a test domain |
| 7.2 DNS as evidence | Newly observed domains, high-entropy labels, long TXT answers, query volume per host; benign look-alikes (CDNs, telemetry) | Compute label entropy over a week of `dns.log` and review the top 20 |
| 7.3 Encrypted DNS | DoT and DoH; enterprise visibility loss; NSA guidance on adopting encrypted DNS in enterprises; forcing clients to internal resolvers | Block external DoH in the lab and confirm browsers fall back |
| 7.4 DNSSEC and email authentication | What DNSSEC proves and does not; SPF, DKIM, DMARC policies and reports (RBI's 2026 directions for commercial banks make DMARC mandatory) | Publish SPF/DKIM/DMARC for a test domain and read one aggregate report |

**Check your understanding:** Why does DoH help users on café Wi-Fi but complicate enterprise monitoring? What does a DMARC `p=reject` policy protect, and what can still get through? Why is a sinkhole both a defense and a detection?

### Chapter 8 · Encrypted traffic and modern visibility (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 TLS 1.3 and QUIC | What is encrypted; HTTP/3 over UDP 443; why some firewalls force a fallback to TCP | Capture the same site over HTTP/2 and HTTP/3 and compare visible fields |
| 8.2 Encrypted Client Hello | Hiding SNI; what remains (IP, timing, sizes, certificate in some flows) | List detections that break if SNI disappears, and alternatives |
| 8.3 TLS inspection decisions | Forward proxy decryption, privacy and legal limits (employment contracts, DPDP Act 2023 duties), exempt categories (health, banking), certificate pinning breakage | Write an inspection policy with exemptions and a justification |
| 8.4 Fingerprints and metadata analytics | JA4+, certificate transparency monitoring, flow timing and size features | Detect a new, unknown client application in the lab by its fingerprint |

**Check your understanding:** Why can decrypting traffic increase risk? What can you still learn from a flow you cannot decrypt? When is a fingerprint a weak signal?

### Chapter 9 · Monitoring architecture, retention and cloud networks (weeks 10–11)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 NSM architecture | Sensors, managers, search nodes; Security Onion 3 (Oracle Linux 9 base, Suricata now does full packet capture) | Draw and justify a sensor layout for two offices and a data centre |
| 9.2 Sizing and retention | Bandwidth × utilisation × time; PCAP vs metadata storage; CERT-In's 180-day log retention; M-Trends 2026 notes cases with dwell time near 400 days, longer than common 90-day retention | Calculate storage for 1 Gbps at 30% utilisation: 7 days PCAP, 180 days metadata |
| 9.3 Cloud network evidence | Security groups vs network ACLs, VPC/VNet flow logs, cloud firewalls, traffic mirroring, private endpoints | Analyse a sample VPC flow log set for an unexpected outbound pattern |
| 9.4 Feeding the SOC | Shipping Zeek/Suricata to a SIEM, field normalisation, which alerts go to analysts (continues in [SEC302](../SEC302_security_operations_soc_siem_and_monitoring/README.md)) | Forward lab logs to Elastic or Wazuh and build one dashboard |

**Check your understanding:** Why keep metadata much longer than full packet capture? What cloud traffic never appears in flow logs? What breaks if sensor clocks drift by two minutes?

### Chapter 10 · Network attacks through a defender's lens (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Reconnaissance and scanning | What scans look like in Zeek and firewall logs (ATT&CK T1046); internal scanning as a high-value signal | Label scan activity in a published dataset |
| 10.2 Lateral movement evidence | SMB, RDP, WinRM and remote service creation seen from the network (ATT&CK Lateral Movement tactic); east-west visibility gaps | Build a "who talks to whom" graph and flag new admin-protocol edges |
| 10.3 Command and control and exfiltration | Application-layer protocols (T1071), exfiltration over C2 or alternative protocols (T1041, T1048); living off the land (CISA and partners' February 2024 guidance) | Write detection ideas and their likely false positives for each technique |
| 10.4 Legacy authentication on the wire | Cleartext protocols and NTLM/Kerberos traffic as network evidence; relay attacks named, not taught; SMB and LDAP signing as defences | Find cleartext and legacy authentication in a week of lab Zeek `ntlm.log` and `kerberos.log` |

**Check your understanding:** Why are internal scans often more alarming than internet scans? Which lateral-movement evidence disappears if you only monitor the internet edge? Why do living-off-the-land techniques defeat signature-only detection?

### Chapter 11 · Network incident response and AI-assisted analysis (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Network containment | Quarantine VLAN, ACL blocks, DNS sinkholes, disabling VPN accounts, isolating an edge device; business impact of each | Choose containment for three scenarios and state the cost |
| 11.2 Network evidence handling | Preserving PCAP and logs, hashing, chain of custody, exporting from Security Onion (continues in [SEC402](../../year_4/SEC402_digital_forensics_and_incident_response/README.md)) | Export and hash evidence for a lab incident |
| 11.3 AI-assisted network analysis | LLM summaries of Zeek logs, natural-language-to-query, AI-drafted firewall rules; verification against raw logs | Compare an AI summary of a capture with your own and list every error |
| 11.4 Tabletop: edge device compromise | Detection, scoping, vendor and CERT-In coordination, rebuild vs patch | Run a 90-minute tabletop with defined roles and write the after-action report |

**Check your understanding:** Why might a sinkhole be better than a block during an investigation? What must you preserve before rebooting a suspected compromised firewall? How would you prove an AI-written firewall rule does what it claims?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1–2 | Lab 1 · Build the NSM lab | Lab diagram and sensor proof |
| 2 | 2 | Lab 2 · Packet reading | Two incident notes from training captures |
| 3 | 3 | Lab 3 · Segmentation and rule audit | Zone design, audit findings |
| 4 | 4 | Lab 4 · WireGuard and edge logging | Hardening standard; **P1 due** |
| 5 | 5 | Lab 5 · Suricata rules | Five tested rules |
| 6 | 5–6 | Lab 5 (cont.) · Tuning | Before/after alert volumes |
| 7 | 6 | Lab 6 · Zeek hunting | Rare-destination and beaconing report |
| 8 | 7 | Lab 7 · DNS controls | RPZ and DMARC evidence; mid-term (AI off) |
| 9 | 8 | Lab 8 · Encrypted traffic | Fingerprint inventory |
| 10 | 9 | Lab 9 · Sizing and SIEM forwarding | Sizing sheet; **P2 due** |
| 11 | 9 | Lab 9 (cont.) · Cloud flow logs | Flow-log findings |
| 12 | 10 | Lab 10 · Attack evidence | Detection ideas with false-positive notes |
| 13 | 11 | Tabletop | After-action report |
| 14 | 11 | P3 demos | **P3 due** |
| 15 | Review | Practical exam (PCAP + logs) and oral defence of P3 | Final exam |

## Working with AI in this course

- **Use AI for:** explaining unfamiliar protocol fields; drafting Suricata rules and Zeek scripts that you then test against captures; turning a question into a Zeek or SIEM query; summarising a long log export as a starting point; writing documentation for your rule set. Security Onion's assistant, Microsoft Security Copilot, Claude, ChatGPT and Gemini can all do these; Claude Code or GitHub Copilot can help script `tshark` and Zeek log analysis.
- **Do without AI (drills):** weekly 30-minute PCAP challenges; the firewall rule-base audit; the segmentation design; sizing calculations; the mid-term and final practical. You must be able to read a capture when the AI summary is wrong.
- **Verify AI output by:** replaying every rule against a capture that should fire and one that should not; checking every field name against the Suricata or Zeek documentation for your version; re-running any query the AI wrote and comparing counts with a manual `tshark` or `zeek-cut` result; diffing firewall changes in a lab before production.
- **Where AI still fails here (show it, do not assume it):** keep a log of AI outputs that look right but are wrong. Typical findings to test for: rule keywords from an older Suricata version, invented Zeek log fields, summaries that miss low-volume events because they focus on the loudest hosts, and "benign" verdicts on traffic the model cannot see inside. Malware authors have already planted text meant to mislead AI analysis tools (Check Point, June 2025; Google Threat Intelligence Group, November 2025), so treat any text taken from traffic or files as untrusted input to the model.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs 1–10 (evidence, write-ups) | 25% |
| Projects P1 / P2 / P3 | 5% / 15% / 20% |
| Mid-term (AI off, PCAP and design questions) | 10% |
| Final practical (AI off) + oral defence of P3 | 25% |

**Mastery gate.** You pass when you can, with AI tools off and in three hours: (1) given an unseen packet capture and its Zeek logs, identify the compromised host, the external infrastructure and the timeline, with evidence for every claim; (2) audit a 40-rule firewall export and find at least four of five planted problems; (3) write two Suricata rules for stated policy violations that fire on the provided positive capture and stay silent on a provided day of baseline traffic.

## Industry reality

This work sits in SOC, network security engineering and managed detection and response (MDR) teams, using Suricata, Zeek and Security Onion alongside commercial next-generation firewalls and network detection products. Public anchors: CISA's emergency directives for Ivanti (2024) and Cisco ASA (2025); the AIIMS 2022 segmentation finding; and RBI's July 2026 directions for commercial banks, which require firewalls, intrusion detection and DMARC.

**Interview questions from this course**

1. *Walk me through what happens on the wire when a user opens a website, and where you could detect something wrong.* Strong answer: DNS query and answer, TCP and TLS handshakes (SNI, certificate), HTTP request; names the evidence at each step (DNS logs, Zeek `ssl`/`x509`, proxy logs) and what TLS 1.3 and ECH hide.
2. *We have a flat network. Where do you start segmenting?* Strong answer: inventory and data flows first; protect crown jewels and management interfaces; separate user, server, OT and guest zones; default-deny between zones with logged exceptions; phased rollout with monitoring in "log only" mode; measures success by blocked lateral paths, not by rule count.
3. *A Suricata rule fires thousands of times a day. What do you do?* Strong answer: look at what it matches and why, check whether the traffic is expected, fix the rule logic or scope before suppressing, document any suppression with an owner and expiry, keep a test capture so the fix does not remove true detections.
4. *How would you detect command-and-control traffic that is encrypted?* Strong answer: metadata (destinations, certificate and JA4 fingerprints, beacon timing and sizes, rare domains, new domains), DNS evidence, endpoint correlation; acknowledges false positives from update agents and telemetry, and explains how to baseline.
5. *A CISA advisory says your VPN appliance model is being exploited. What do you do in the next 24 hours?* Strong answer: confirm exposure and version, follow vendor and CISA guidance, preserve evidence before reboot or upgrade, check for signs of compromise (unexpected admin sessions, configuration changes, new outbound connections from the device), patch or isolate, rotate credentials that passed through the device, and report under CERT-In's 6-hour rule if an incident is confirmed.

## Resources (free first)

- **Documentation:** [Suricata user guide](https://docs.suricata.io/) · [Zeek documentation](https://docs.zeek.org/) · [Security Onion documentation](https://docs.securityonion.net/) · [Wireshark User's Guide](https://www.wireshark.org/docs/wsug_html_chunked/) · [Community ID specification](https://github.com/corelight/community-id-spec) · [JA4+](https://github.com/FoxIO-LLC/ja4)
- **Standards and guidance:** [NIST SP 800-41 Rev. 1, firewalls](https://csrc.nist.gov/pubs/sp/800/41/r1/final) · [NIST SP 800-94, intrusion detection and prevention systems](https://csrc.nist.gov/pubs/sp/800/94/final) · [NIST SP 800-207, zero trust](https://csrc.nist.gov/pubs/sp/800/207/final) · [CIS Critical Security Controls v8.1](https://www.cisecurity.org/controls/v8-1) · [CISA protective DNS](https://www.cisa.gov/resources-tools/services/protective-domain-name-system-dns-resolver) · [MITRE ATT&CK](https://attack.mitre.org/)
- **Practice (legal):** [Malware-Traffic-Analysis.net exercises](https://www.malware-traffic-analysis.net/training-exercises.html) · [CyberDefenders network forensics labs](https://cyberdefenders.org/blueteam-ctf-challenges/) · [Blue Team Labs Online](https://blueteamlabs.online/) · [TryHackMe](https://tryhackme.com/) (Wireshark and NSM rooms; many are subscription-only) · [Wireshark sample captures](https://wiki.wireshark.org/SampleCaptures)
- **Books (paid, optional):** Bejtlich, *The Practice of Network Security Monitoring* (2013); Sanders, *Practical Packet Analysis*, 3rd ed. (2017).

## Sources

All checked 12 Oct 2026.

- Google Cloud / Mandiant, *M-Trends 2026* (Mar 2026): exploits 32% of initial vectors, mean time to exploit −7 days, dwell times near 400 days in some cases — https://cloud.google.com/blog/topics/threat-intelligence/m-trends-2026
- CISA, Emergency Directive 25-03 on Cisco ASA and Firepower (25 Sep 2025) — https://www.cisa.gov/news-events/directives/ed-25-03-identify-and-mitigate-potential-compromise-cisco-devices
- CISA, Emergency Directive 24-01 on Ivanti Connect Secure and Policy Secure (Jan 2024) — https://www.cisa.gov/news-events/directives/ed-24-01-mitigate-ivanti-connect-secure-and-ivanti-policy-secure-vulnerabilities
- Deccan Herald, report of the Minister of State's reply on AIIMS (16 Dec 2022): five servers, about 1.3 TB, "improper network segmentation" — https://www.deccanherald.com/amp/story/india%2F5-servers-of-aiims-were-affected-about-13-tb-of-data-encrypted-in-cyber-attack-mos-it-1172460.html
- Security Onion blog (Mar 2026): 3.0.0 release, Oracle Linux 9, Suricata full packet capture, 2.4 end of life on 1 Oct 2026 — https://blog.securityonion.net/2026/03
- Suricata 8.0.0 release announcement (2025) — https://forum.suricata.io/t/suricata-8-0-0-released/5854 ; Zeek 8.0.0 feature release (Aug 2025, LTS) — https://community.zeek.org/t/zeek-feature-release-8-0-0/7860
- CERT-In Directions under section 70B(6) (28 Apr 2022): 180-day log retention, 6-hour reporting — https://www.cert-in.org.in/PDF/CERT-In_Directions_70B_28.04.2022.pdf
- DSCI brief on the RBI (Commercial Banks – Cybersecurity, Technology: Risk, Resilience and Assurance Framework) Directions, 2026 (31 Jul 2026): DMARC, firewalls and IDS — https://www.dsci.in/files/content/knowledge-centre/2026/dsci-brief-on-rbi-cybersecurity-commercial-banks-directions-2026.pdf
- CISA and partners, *Identifying and Mitigating Living Off the Land Techniques* (Feb 2024) — https://www.cisa.gov/resources-tools/resources/identifying-and-mitigating-living-land-techniques
- NSA, *Adopting Encrypted DNS in Enterprise Environments* (Jan 2021), as announced by CISA — https://www.cisa.gov/news-events/alerts/2021/01/15/nsa-releases-guidance-encrypted-dns-enterprise-environments
- Check Point Research, "In the Wild: Malware Prototype with Embedded Prompt Injection" (25 Jun 2025) — https://research.checkpoint.com/2025/ai-evasion-prompt-injection/ ; Google Threat Intelligence Group, *AI Threat Tracker* (Nov 2025) — https://cloud.google.com/blog/topics/threat-intelligence/threat-actor-usage-of-ai-tools

_Last reviewed: 2026-10_
