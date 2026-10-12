# SEC301 · Labs and projects

All work happens in your own home lab (a laptop or desktop with 16 GB RAM or more running VirtualBox, VMware Workstation Player, Proxmox or Hyper-V) or with published training captures. Keep the lab network isolated from your home network except through the lab firewall. Every lab submission has three parts: evidence (screenshots, exported logs, rule files in a Git repository), a short write-up with measured numbers, and a "what would fool this" paragraph.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Build the NSM lab | OPNsense firewall, Security Onion 3 standalone sensor, one Windows and one Linux client on an isolated network; mirror client traffic to the sensor | Network diagram, proof that Suricata alerts and Zeek logs appear for client traffic, packet-drop statistics | 5 h |
| 2 · Packet reading | Answer structured questions on two Malware-Traffic-Analysis.net training exercises using Wireshark and `tshark` only | Two one-page incident notes (host, user, external infrastructure, timeline, evidence) | 4 h |
| 3 · Segmentation and rule audit | Design zones for an illustrative hospital; audit a provided 60-rule firewall export | Zone diagram, rule matrix, audit findings ranked by severity with the fix for each | 4 h |
| 4 · VPN and edge logging | WireGuard site-to-site tunnel; send firewall and VPN logs to the sensor; back up and diff configurations daily | Hardening and logging standard, config-diff script, a sample alert for an admin login from a new IP | 4 h |
| 5 · Suricata rules and tuning | Write five policy rules (cleartext FTP login, TLS 1.0, external DNS resolvers, SMB to the internet, a new self-signed certificate) with positive and negative test captures; then tune ET Open | Rules, test captures, a script that replays captures and checks results, before/after alerts-per-day table | 6 h |
| 6 · Zeek hunting | One week of lab baseline traffic: stack destinations, find long connections, score beaconing | Notebook or script, top-20 findings each labelled benign or suspicious with the reason | 5 h |
| 7 · DNS controls | Response policy zone sinkhole in Unbound or BIND; block external DoH; SPF/DKIM/DMARC on a test domain | Config files, proof of sinkhole hits, a parsed DMARC aggregate report | 4 h |
| 8 · Encrypted traffic | Capture the same services over HTTP/2 and HTTP/3; build a JA4 inventory of lab applications | Field-visibility comparison table, fingerprint inventory, one detection idea that survives Encrypted Client Hello | 3 h |
| 9 · Sizing, SIEM forwarding and cloud flow logs | Size sensors for a stated network; forward lab logs to Elastic or Wazuh; analyse a published or self-generated VPC flow log sample | Sizing sheet with assumptions, one dashboard, flow-log findings | 5 h |
| 10 · Attack evidence | Label scanning, lateral movement and exfiltration patterns in a public dataset (for example OTRF Security-Datasets or a CyberDefenders network lab) | Evidence table mapping each observation to an ATT&CK technique, with likely false positives | 4 h |

## Projects

### P1 · Segmentation review for a hospital network (L1, ~6 hours)

**Real-world inspiration.** The Government of India told Parliament in December 2022 that the AIIMS Delhi ransomware attack (five servers, about 1.3 TB encrypted) happened due to improper network segmentation. Hospitals run clinical systems, medical devices, billing, guest Wi-Fi and research networks side by side. The network below is an illustrative scenario, not AIIMS's real design.

**What to build.** Given a flat /16 network description with 12 systems (electronic health records, PACS imaging, lab analysers, pharmacy, billing, HR, staff laptops, guest Wi-Fi, building management, a VPN, a backup server, Active Directory), produce: a zone design, a zone-to-zone rule matrix with business justification for every allowed flow, a migration plan in phases, and a test plan.

**Acceptance criteria**
- Every allowed flow names source, destination, port, protocol, business owner and justification; there is no "any" in source, destination or service.
- Management interfaces and backups sit in zones that user laptops cannot reach; the test plan proves it with at least 10 concrete connection tests.
- Medical devices and building management sit in isolated zones with explicit, minimal flows.
- The migration plan starts in log-only mode and defines the metric that allows moving to enforcement.
- A one-page summary explains which ransomware spread paths are now blocked.

**Stretch goals.** Implement the design in OPNsense in your lab and run the test plan; add host-firewall rules for the backup server.

**What it proves to an employer.** You can turn a vague "segment the network" goal into a testable design that clinicians and auditors can both follow.

### P2 · Network detection pack with tests (L2, ~15 hours)

**Real-world inspiration.** Mature SOC teams keep their Suricata and Zeek detections in version control with test captures, so a rule change never silently breaks detection. Emerging Threats publishes rules openly; Zeek packages are shared through its package manager.

**What to build.** A Git repository with at least 10 Suricata rules and 3 Zeek scripts for policy violations and suspicious-but-legal patterns that you generate in your own lab (for example: new self-signed certificates, DNS to resolvers outside policy, long-lived outbound connections from servers, SMB leaving the network, beacon-like periodic connections from a script you wrote). Add a test harness that replays captures through Suricata and Zeek and asserts which detections fire.

**Acceptance criteria**
- Each detection has a description, ATT&CK mapping where relevant, a positive capture that fires it and a negative capture that does not; the harness runs all tests in one command and reports pass/fail.
- Over 48 hours of normal lab baseline traffic, the pack produces fewer than 20 alerts in total, and each one is explained.
- A CI workflow (GitHub Actions or similar) runs the tests on every change.
- The README states the Suricata and Zeek versions tested and the known blind spots of each detection.

**Stretch goals.** Add Community ID to join Suricata alerts with Zeek connection records in the report; export the pack as Sigma rules where a log-based equivalent exists.

**What it proves to an employer.** You treat detections as tested software, which is exactly what detection engineering teams hire for ([SEC401](../../year_4/SEC401_detection_engineering_and_threat_hunting/README.md)).

### P3 · Edge device monitoring and response programme (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** CISA's Emergency Directive 24-01 (Ivanti, January 2024) and 25-03 (Cisco ASA, September 2025) ordered agencies to inventory, collect forensic data from and patch or disconnect VPN and firewall appliances under active exploitation; in the Cisco case the attacker's persistence survived reboots and upgrades. Mandiant's M-Trends 2026 reports exploits as the top initial infection vector and exploitation often before a patch exists. RBI's July 2026 directions require commercial banks to report cyber incidents within six hours.

**What to build.** For an illustrative mid-size Indian company (two offices, one data centre, one cloud VPC, 600 staff, a VPN appliance and two perimeter firewalls), deliver a complete programme, implemented in your lab where possible:
1. an inventory of edge devices with versions, owners and support status;
2. a logging design: what each device sends, where, retention (meeting CERT-In's 180 days), and clock synchronisation;
3. at least eight detections for edge-device compromise signals that do not depend on a specific vulnerability: administrator logins from new sources, configuration changes outside change windows, new outbound connections initiated *by* the appliance, VPN logins for disabled users, impossible-travel VPN sessions, firmware or image hash changes, log gaps from a device, and certificate changes on the device;
4. a response runbook: evidence to collect before reboot or upgrade, vendor and CERT-In coordination, credential rotation for everything that passed through the device, rebuild-versus-patch decision criteria;
5. a 60-minute tabletop exercise with an after-action report.

**Acceptance criteria**
- All eight detections are implemented in your lab (OPNsense and WireGuard logs, Zeek and Suricata on the sensor, Elastic or Wazuh as the SIEM) and each is demonstrated with a recorded test you triggered yourself.
- A log-gap detection alerts within 15 minutes when you stop a device's log forwarding.
- The runbook lists, in order, the first ten actions with an owner and a time target, and states how the 6-hour CERT-In clock is met.
- The tabletop report records decisions, disagreements and three concrete improvements.
- The repository includes an architecture diagram, all configs, detections and a two-page executive summary.

**Stretch goals.** Add a cloud VPN gateway and its logs; score the programme against CIS Controls v8.1 Controls 12 (network infrastructure management) and 13 (network monitoring and defense).

**What it proves to an employer.** You can protect the most attacked part of a modern network end to end: visibility, detection, response and reporting. This is the work of a senior SOC analyst or network security engineer.

## Feeds into

- [SEC302 Security Operations](../SEC302_security_operations_soc_siem_and_monitoring/README.md): your sensor and SIEM forwarding become the data sources for SOC triage.
- [SEC401 Detection Engineering and Threat Hunting](../../year_4/SEC401_detection_engineering_and_threat_hunting/README.md): P2's tested detection pack is the starting point for detection-as-code.
- [SEC402 Digital Forensics and Incident Response](../../year_4/SEC402_digital_forensics_and_incident_response/README.md): network evidence handling and the edge-device runbook.
- [OV01 Cloud Security](../../../../04_overlaps/OV01_cloud_security/README.md): cloud flow logs and network controls at scale.
