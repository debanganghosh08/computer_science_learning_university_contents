# SEC304 · Endpoint and Operating System Security

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 6 | 4 (≈ 120 hours) | L2 → L3 | [CS213](../../../../02_year_2_core_computer_science/semester_4/CS213_security_foundations/README.md) (and [CS203 Operating Systems](../../../../02_year_2_core_computer_science/semester_3/CS203_operating_systems/README.md) through it) | [SEC404](../../year_4/SEC404_ai_in_security_operations/README.md), [SEC402](../../year_4/SEC402_digital_forensics_and_incident_response/README.md), [SEC403](../../year_4/SEC403_malware_analysis_for_defenders/README.md) |

Part of the [Cybersecurity Defense major](../../README.md). This course is about **hardening, monitoring and responding on endpoints you own or manage**. Attacker behaviours are described at the level of what they look like in logs, never as instructions.

## Why this course matters now

Laptops and servers are where attackers run code, steal credentials and encrypt data, and they are also where defenders collect the richest evidence. The 2024 Snowflake customer intrusions started with infostealer malware on ordinary computers, some infected years earlier. "Living off the land", using built-in tools such as PowerShell and WMI instead of malware, is the hallmark of state actors such as Volt Typhoon (CISA and partners, 2024), so detection now depends on good OS logging rather than antivirus signatures. Endpoint security tools are themselves a risk: on 19 July 2024 a faulty CrowdStrike content update crashed about 8.5 million Windows devices (Microsoft's estimate), and Microsoft has since started moving security products out of the Windows kernel. Microsoft also announced in November 2025 that Sysmon, the most widely used free Windows monitoring tool, will ship inside Windows 11 and Windows Server 2025. Patching is a race: Mandiant's M-Trends 2026 puts the mean time to exploit at an estimated −7 days, and in April 2026 NIST stopped enriching most CVEs in the National Vulnerability Database, so teams must prioritise with CISA's Known Exploited Vulnerabilities catalogue and EPSS instead of waiting for NVD scores. AI assistants in EDR consoles (Microsoft Security Copilot in Defender, CrowdStrike Charlotte AI, SentinelOne Purple AI) now explain process trees and suggest hardening. A human still has to decide which change might break production, read the raw telemetry, and roll out controls without stopping the business.

## Learning outcomes

By the end you can:

1. **Harden** Windows and Linux systems to CIS Benchmark Level 1, **measure** compliance automatically, and **justify** each deviation.
2. **Explain** the Windows security architecture defenders depend on (tokens, integrity levels, services, scheduled tasks, LSASS protection, Credential Guard, AMSI, PowerShell logging) and **configure** each.
3. **Design** endpoint logging (Windows advanced audit policy, Sysmon, PowerShell logging, Linux `auditd` and `journald`) that answers named investigation questions, and **collect** it centrally.
4. **Explain** how EDR works (telemetry sources, detection, response actions, tamper protection) and **evaluate** an EDR product against your own test plan.
5. **Run** a vulnerability management cycle with CVSS 4.0, EPSS, the CISA KEV catalogue and SSVC, and **set** patch timelines that a business can meet.
6. **Deploy** application allow-listing (App Control for Business, AppLocker, fapolicyd) in audit mode first and then enforce it.
7. **Protect** data on endpoints (full-disk encryption, backups that survive ransomware, removable-media control) and **prove** recovery works.
8. **Verify** AI-suggested hardening and detections before they reach production.

## Chapters and lessons

### Chapter 1 · The endpoint threat model (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 What counts as an endpoint | Laptops, servers, virtual desktops, mobile devices, build agents, jump hosts; managed vs unmanaged | Classify every device in a 300-person company description (illustrative) |
| 1.2 What attackers want there | Credentials and session cookies (infostealers), persistence, lateral movement, encryption for ransom; ATT&CK tactics as a map | Map the Snowflake 2024 chain to ATT&CK tactics |
| 1.3 Living off the land | Built-in binaries and scripts used for malicious ends; why it defeats signatures; CISA's February 2024 joint guidance | Pick five built-in tools and list the legitimate and suspicious uses of each |
| 1.4 The lab | Windows 11 and Windows Server VMs, Ubuntu and RHEL-compatible VMs, a SIEM from SEC302 | Build the lab and baseline it (snapshots) |

**Check your understanding:** Why does an infostealer infection on a personal laptop matter to a company's cloud data? Why can't you simply block PowerShell? Which endpoint is most valuable to an attacker in a typical company, and why?

### Chapter 2 · Hardening baselines (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Baselines | CIS Benchmarks (Level 1 vs Level 2), Microsoft security baselines, DISA STIGs; choosing one and recording deviations | Compare three baselines for one setting (SMB signing) and their rationales |
| 2.2 Measuring compliance | CIS-CAT Lite, Microsoft Security Compliance Toolkit and Policy Analyzer, OpenSCAP, Lynis | Scan a Windows and a Linux VM; record the score |
| 2.3 Applying at scale | Group Policy, Intune, Ansible; configuration drift detection | Apply 20 settings with GPO or Ansible and re-scan |
| 2.4 Breaking things safely | Test rings, rollback, exception records with owners and expiry | Find two settings that break a lab application and write the exception |

**Check your understanding:** Why is a 100% benchmark score a warning sign? What is the difference between a baseline and a policy? Why must every exception expire?

### Chapter 3 · Windows internals for defenders (weeks 3–4)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Processes and tokens | Process trees, parent-child relationships, access tokens, integrity levels, UAC | Explore a normal boot's process tree in Process Explorer and record what is expected |
| 3.2 Persistence locations | Services, scheduled tasks, Run keys, WMI event subscriptions, startup folders (as places to monitor) | Use Autoruns to baseline persistence on a clean VM |
| 3.3 Credential protection | LSASS, Credential Guard and virtualization-based security, LSA protection (RunAsPPL), Windows Hello for Business | Enable Credential Guard and LSA protection; verify their state |
| 3.4 Script and macro controls | PowerShell script block logging, Constrained Language Mode, AMSI, Office macro blocking from the internet, attack surface reduction (ASR) rules | Enable ASR rules in audit mode and review a week of events |
| 3.5 SMB, RDP and remote management | SMB signing, disabling SMBv1, RDP restrictions and Network Level Authentication, WinRM scope | Restrict remote management to a jump host and test it |

**Check your understanding:** Why is "Word spawned PowerShell" more suspicious than "Explorer spawned PowerShell"? What does Credential Guard protect, and what does it not? Why run ASR rules in audit mode first?

### Chapter 4 · Windows logging and Sysmon (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Security event IDs | 4624/4625 with logon types, 4688 with command line, 4672, 4697/7045 service installs, 4698 scheduled tasks, 4720/4732 account changes, 1102 log cleared | Generate each event in the lab and find it |
| 4.2 Advanced audit policy | Which subcategories to enable, log size, the cost of over-logging | Write and apply an audit policy with justification per subcategory |
| 4.3 Sysmon | Event IDs 1, 3, 7, 8, 10, 11, 13, 22; configuration files (SwiftOnSecurity, Olaf Hartong's sysmon-modular) as starting points; native Sysmon in Windows (announced November 2025, in Insider builds in 2026) | Deploy Sysmon with a tuned config and measure events per hour |
| 4.4 Collection | Windows Event Forwarding, SIEM agents, log loss and tampering | Forward logs to your SIEM and alert on log clearing |

**Check your understanding:** Which single Windows event gives the most investigation value per byte, and why? Why do Sysmon configs exclude so much? What should happen when a host stops sending logs?

### Chapter 5 · Linux and macOS security (weeks 6–7)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Linux hardening | Users and `sudo`, SSH (keys only, no root login), systemd service hardening options, SELinux and AppArmor | Harden an Ubuntu and a RHEL-compatible VM and scan with Lynis |
| 5.2 Linux telemetry | `auditd` rules (execve, identity files, privilege use), `journald`, osquery, Sysmon for Linux | Write 10 audit rules mapped to investigation questions |
| 5.3 eBPF-based runtime security | Falco and Tetragon; container and Kubernetes context | Run Falco and trigger two default rules safely |
| 5.4 File integrity monitoring | AIDE, Wazuh FIM; what to watch and what not to | Detect an unauthorised change to `/etc/sudoers` |
| 5.5 macOS essentials | Gatekeeper, notarisation, XProtect, TCC privacy controls, unified log, Endpoint Security framework, MDM (Intune, Jamf) | Read the macOS Security Compliance Project baseline and pick 10 settings |

**Check your understanding:** Why log `execve` with care on a busy server? What does SELinux stop that file permissions do not? Why is MDM the real control plane for Macs?

### Chapter 6 · EDR concepts and evaluation (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 How EDR sees | Kernel callbacks, Event Tracing for Windows, eBPF, Apple's Endpoint Security framework; user mode vs kernel mode trade-offs | Draw the telemetry path of one EDR product from its documentation |
| 6.2 Detection and response | Behaviour rules, ML models, prevention vs detection, isolation, process kill, file quarantine, remote shell; tamper protection | Compare response actions of three EDRs |
| 6.3 When security software fails | CrowdStrike Channel File 291 (July 2024): a content update with 21 fields where the sensor expected 20 crashed Windows; staged rollouts; Microsoft's Windows Resiliency Initiative and security products outside the kernel | Write a content-update policy (rings, canaries, rollback) for an EDR |
| 6.4 Evaluating EDR | MITRE ATT&CK Evaluations and how to read them (and why some vendors skipped the 2025 round), your own test plan in a lab | Write a 20-test evaluation plan using safe emulation in an isolated lab |
| 6.5 Open-source endpoint visibility | Wazuh, Velociraptor, osquery with Fleet | Deploy Velociraptor and run a fleet-wide query |

**Check your understanding:** Why does running in the kernel give power and risk at the same time? Why is a vendor's evaluation score not your detection rate? What must an EDR do if an attacker tries to disable it?

### Chapter 7 · Vulnerability and patch management (weeks 9–10)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Asset inventory first | You cannot patch what you do not know: inventory sources, software bills of materials | Reconcile three inventory sources in a provided dataset |
| 7.2 Scanning | Authenticated vs unauthenticated scans; Greenbone OpenVAS, Nessus Essentials, Microsoft Defender Vulnerability Management; false positives | Scan the lab and validate five findings by hand |
| 7.3 Prioritisation | CVSS 4.0, EPSS v4 (March 2025), CISA KEV, SSVC decision trees; NIST's April 2026 change to enrich only KEV-listed, federal and critical-software CVEs | Prioritise 50 CVEs with all four and compare the orderings |
| 7.4 Patching at scale | Rings, maintenance windows, emergency changes, reboots, measuring time to remediate; RBI's 2026 directions require vulnerability assessments every six months for banks' critical systems | Design patch SLAs for a bank and a startup and justify the difference |
| 7.5 When you cannot patch | Compensating controls, isolation, virtual patching, retirement | Write a risk acceptance for an unpatchable medical device |

**Check your understanding:** Why can a CVSS 9.8 wait while a CVSS 6.5 cannot? What does a −7-day mean time to exploit mean for your patch SLA? Why is "number of open vulnerabilities" a weak metric?

### Chapter 8 · Application control and privilege reduction (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Allow-listing models | Publisher, path and hash rules; managed installer; App Control for Business (formerly WDAC) vs AppLocker; Smart App Control | Build an App Control policy in audit mode from a reference machine |
| 8.2 Rolling it out | Audit mode, event review, supplemental policies, enforcement rings | Move one lab ring to enforcement with zero blocked business apps |
| 8.3 Drivers and scripts | Microsoft's vulnerable driver blocklist, script enforcement | Enable the driver blocklist and confirm it in event logs |
| 8.4 Removing admin rights | Local admin removal, elevation on demand, Linux `fapolicyd`, macOS Santa | Remove local admin from a lab user and handle three elevation requests |

**Check your understanding:** Why are path rules weak in user-writable folders? Why does removing local admin reduce so many risks at once? What is the operational cost of hash rules?

### Chapter 9 · Data protection and ransomware resilience on endpoints (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Encryption at rest | BitLocker, FileVault, LUKS; key escrow and recovery | Enable BitLocker with escrowed recovery and test a recovery |
| 9.2 Backups that survive | 3-2-1 with an offline or immutable copy; protecting backup credentials; restore testing (RBI 2026 requires regular restore tests for banks) | Restore a VM from backup and time it |
| 9.3 Device control and DLP | USB control, data loss prevention basics, remote wipe | Block unapproved USB storage and log attempts |
| 9.4 Ransomware readiness checklist | Which endpoint controls break which stages | Score the lab against CISA's #StopRansomware guide checklist |

**Check your understanding:** Why are backups often deleted before encryption starts? What does disk encryption protect against, and what not? Why is a restore test more important than a backup report?

### Chapter 10 · Endpoint operations at scale and AI (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Fleet posture | Compliance dashboards, device health attestation, Conditional Access tied to device state ([SEC303](../SEC303_identity_and_access_management/README.md)) | Build a device posture dashboard |
| 10.2 Automatic response | Automatic isolation and "attack disruption" features; when they help and when they hurt | Define which detections may isolate a server automatically |
| 10.3 AI in endpoint security | Copilot in Defender, Charlotte AI, Purple AI: explaining process trees, scripting hunts, suggesting hardening; verification in a test ring | Ask an assistant for 10 hardening changes and test each in the lab |
| 10.4 Endpoint triage | Collecting triage data with Velociraptor; handing evidence to incident response ([SEC402](../../year_4/SEC402_digital_forensics_and_incident_response/README.md)) | Run a triage collection on a lab host and hash the output |

**Check your understanding:** When should automatic isolation be disabled for a server? How would you prove an AI-suggested registry change is safe? Which endpoint metric would you report to a CIO?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Endpoint lab and baseline | Lab build notes |
| 2 | 2 | Lab 2 · CIS scanning and hardening | Before/after scores |
| 3 | 3 | Lab 3 · Windows internals | Process and persistence baselines |
| 4 | 3 | Lab 3 (cont.) · Credential and script controls | ASR audit review; **P1 due** |
| 5 | 4 | Lab 4 · Audit policy and Sysmon | Event volume measurements |
| 6 | 5 | Lab 5 · Linux hardening and auditd | Audit rules |
| 7 | 5 | Lab 5 (cont.) · Falco and FIM | Mid-term (AI off) |
| 8 | 6 | Lab 6 · EDR evaluation plan and Velociraptor | Test plan |
| 9 | 7 | Lab 7 · Scanning and prioritisation | Ranked CVE list |
| 10 | 7 | Lab 7 (cont.) · Patch SLAs | **P2 due** |
| 11 | 8 | Lab 8 · App control | Enforcement evidence |
| 12 | 9 | Lab 9 · Encryption and restore | Restore timings |
| 13 | 10 | Lab 10 · AI hardening test | Test results |
| 14 | 10 | Triage collection | **P3 due** |
| 15 | Review | Practical exam and oral defence of P3 | Final exam |

## Working with AI in this course

- **Use AI for:** explaining Windows event fields, Sysmon configuration and `auditd` syntax; drafting GPO, Intune, Ansible and PowerShell for hardening; summarising scanner output; explaining a process tree in an EDR alert. Copilot in Defender, Charlotte AI, Purple AI, Claude, ChatGPT and Gemini all help; Claude Code or GitHub Copilot can write configuration-as-code.
- **Do without AI (drills):** reading a raw process tree and deciding if it is suspicious; writing an audit policy and justifying each subcategory; prioritising a CVE list with KEV, EPSS and asset context; the mid-term and final.
- **Verify AI output by:** applying every suggested setting in a test ring, re-scanning with CIS-CAT or OpenSCAP, and running the business applications; checking every event ID and Sysmon field in Microsoft's documentation; confirming CVE claims against the vendor advisory and the KEV catalogue, not the model's memory.
- **Where AI still fails here (show it, do not assume it):** log each case where an assistant recommends a deprecated setting (for example old WDAC naming or removed Group Policy paths), invents a registry value, gives a confident CVE score that does not match the advisory, or suggests a change that would lock out remote management. Because models have training cut-offs, they are often wrong about which version fixed what.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs 1–10 | 25% |
| Projects P1 / P2 / P3 | 5% / 15% / 20% |
| Mid-term (AI off) | 10% |
| Final practical (AI off) + oral defence of P3 | 25% |

**Mastery gate.** You pass when you can, without AI tools and in three hours: (1) harden an unseen Windows server to a stated CIS Level 1 score while keeping a provided application working; (2) from raw Sysmon and Security logs, identify the persistence an "attacker" added to a lab host and the account used; (3) prioritise 30 CVEs for a described company and defend the top five in an oral.

## Industry reality

Endpoint security engineers, EDR administrators, vulnerability management analysts and SOC analysts use this material daily. Real anchors: Microsoft's estimate of 8.5 million devices crashed by the July 2024 CrowdStrike update, and the resulting Windows Resiliency Initiative; MITRE ATT&CK Evaluations, from which Microsoft, SentinelOne and Palo Alto Networks withdrew in 2025; NIST's April 2026 NVD prioritisation; RBI's 2026 requirements for banks on vulnerability assessment, restore testing and remote wipe.

**Interview questions from this course**

1. *Which Windows logs would you enable on day one, and why?* Strong answer: process creation with command line (4688 or Sysmon 1), logons (4624/4625 with types), service and task creation, account and group changes, PowerShell script block logging, log clearing; sizes and forwarding; ties each to an investigation question.
2. *How do you decide what to patch first?* Strong answer: asset criticality and exposure, KEV listing, EPSS probability, CVSS as one input, vendor advisories, compensating controls; SLAs by tier; measures time to remediate; mentions NVD enrichment gaps.
3. *What is the difference between antivirus and EDR?* Strong answer: signatures vs behavioural telemetry and response; recording for investigations; isolation and remote actions; tamper protection; operational risk of kernel components (2024 outage).
4. *How would you roll out application allow-listing without breaking the business?* Strong answer: inventory, reference machines, audit mode, review events, managed installer and publisher rules, supplemental policies, rings, exception process, measuring blocks.
5. *A server shows Word launching PowerShell that connects to the internet. What do you do?* Strong answer: treat as high severity; check command line and parent, user, network destination, other hosts; decide on isolation with business owner; collect triage data before remediation; hunt for the same pattern fleet-wide.

## Resources (free first)

- **Baselines and guidance:** [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks) · [Microsoft Security Compliance Toolkit](https://learn.microsoft.com/en-us/windows/security/operating-system-security/device-management/windows-security-configuration-framework/security-compliance-toolkit-10) · [macOS Security Compliance Project](https://github.com/usnistgov/macos_security) · [CISA #StopRansomware guide](https://www.cisa.gov/stopransomware/ransomware-guide) · [CISA KEV catalogue](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) · [FIRST EPSS](https://www.first.org/epss/) · [FIRST CVSS v4.0](https://www.first.org/cvss/v4.0/) · [CISA SSVC](https://www.cisa.gov/resources-tools/resources/stakeholder-specific-vulnerability-categorization-ssvc)
- **Windows:** [Sysinternals Sysmon](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon) · [sysmon-modular](https://github.com/olafhartong/sysmon-modular) · [App Control for Business](https://learn.microsoft.com/en-us/windows/security/application-security/application-control/app-control-for-business/appcontrol) · [Attack surface reduction rules](https://learn.microsoft.com/en-us/defender-endpoint/attack-surface-reduction-rules-reference)
- **Linux and open tools:** [Linux audit documentation (Red Hat)](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/auditing-the-system_security-hardening) · [osquery](https://osquery.io/) · [Falco](https://falco.org/) · [Velociraptor](https://docs.velociraptor.app/) · [Wazuh](https://documentation.wazuh.com/current/index.html) · [Lynis](https://cisofy.com/lynis/) · [OpenSCAP](https://www.open-scap.org/) · [Greenbone OpenVAS](https://greenbone.github.io/docs/latest/)
- **Practice:** [CyberDefenders](https://cyberdefenders.org/) endpoint forensics labs · [Blue Team Labs Online](https://blueteamlabs.online/) · [TryHackMe](https://tryhackme.com/) Windows and Linux hardening rooms (many subscription-only) · [OTRF Security-Datasets](https://github.com/OTRF/Security-Datasets)

## Sources

All checked 12 Oct 2026.

- Mandiant, UNC5537 and Snowflake (Jun 2024): infostealer credentials — https://cloud.google.com/blog/topics/threat-intelligence/unc5537-snowflake-data-theft-extortion
- CISA and partners, *Identifying and Mitigating Living Off the Land Techniques* (Feb 2024) — https://www.cisa.gov/resources-tools/resources/identifying-and-mitigating-living-land-techniques
- CrowdStrike, Channel File 291 root cause analysis (6 Aug 2024) — https://www.crowdstrike.com/en-us/blog/channel-file-291-rca-available/ ; TechCrunch on Microsoft's 8.5 million estimate (20 Jul 2024) — https://techcrunch.com/2024/07/20/microsoft-says-8.5m-windows-devices-were-affected-by-crowdstrike-outage/
- SecurityWeek, Microsoft to preview a Windows endpoint security platform after the CrowdStrike outage (2025) — https://www.securityweek.com/microsoft-to-preview-new-windows-endpoint-security-platform-after-crowdstrike-outage/
- BetaNews, "Microsoft to make Sysmon a native Windows 11 tool" (19 Nov 2025) — https://betanews.com/article/microsoft-to-make-sysmon-a-native-windows-11-tool/
- Google Cloud / Mandiant, *M-Trends 2026*: mean time to exploit −7 days — https://cloud.google.com/blog/topics/threat-intelligence/m-trends-2026
- NIST, "NIST updates NVD operations to address record CVE growth" (15 Apr 2026) — https://www.nist.gov/news-events/news/2026/04/nist-updates-nvd-operations-address-record-cve-growth
- Infosecurity Magazine, vendors pull out of 2025 MITRE ATT&CK Evaluations (Sep 2025) — https://www.infosecurity-magazine.com/news/cyber-vendors-pull-out-mitre/
- DSCI brief on RBI Commercial Banks cybersecurity directions (31 Jul 2026) — https://www.dsci.in/files/content/knowledge-centre/2026/dsci-brief-on-rbi-cybersecurity-commercial-banks-directions-2026.pdf

_Last reviewed: 2026-10_
