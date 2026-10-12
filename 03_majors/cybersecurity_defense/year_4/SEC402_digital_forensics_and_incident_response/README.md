# SEC402 · Digital Forensics and Incident Response

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 7 | 4 (≈ 120 hours) | L3 → L4 | [SEC302](../../year_3/SEC302_security_operations_soc_siem_and_monitoring/README.md) (and [SEC304](../../year_3/SEC304_endpoint_and_operating_system_security/README.md), [SEC305](../../year_3/SEC305_governance_risk_and_compliance/README.md) recommended) | [SEC501](../../year_5/SEC501_frontier_seminar_threat_intelligence/README.md), [IND401](../../../../05_shared_years_3_to_5/IND401_industry_co_op_studio/README.md), [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) |

Part of the [Cybersecurity Defense major](../../README.md). Digital forensics and incident response (DFIR) means investigating what happened on systems and leading the organisation through containment, eviction and recovery. You practise only on your own lab systems, published forensic images and legal training platforms. You never examine a device or account without the owner's written authorisation, and you learn to detect anti-forensics, never to use it.

## Why this course matters now

Incidents are now judged on speed and evidence. NIST replaced its 2012 incident response guide in April 2025 with SP 800-61 Rev. 3, a Cybersecurity Framework 2.0 Community Profile that builds response into everyday cybersecurity risk management. In India, CERT-In wants listed incidents reported within 6 hours, the DPDP Rules 2025 require a detailed breach report to the Data Protection Board within 72 hours, and RBI's 2026 directions give commercial banks 6 hours to report on DAKSH. Courts care how evidence was handled: since July 2024 the Bharatiya Sakshya Adhiniyam (section 63) governs electronic records, and its certificate requires the hash value of the record, a requirement the Supreme Court upheld in May 2026. Attackers make response harder: in Cisco's ASA case (CISA ED 25-03, September 2025) the implant survived reboots and upgrades, and Mandiant saw intrusions with dwell times near 400 days, longer than many log retention periods. Indian incidents show the stakes: the AIIMS Delhi ransomware attack (2022) and the July 2024 C-Edge Technologies attack that cut about 300 small banks off retail payments. AI now summarises timelines, parses artefacts and drafts reports, and attackers use it too: Anthropic reported in November 2025 that an AI agent carried out 80–90% of a state-sponsored espionage campaign's tactical work. Yet that same report notes the AI "occasionally hallucinated credentials". In DFIR every claim must trace back to evidence, and that is a human's job.

## Learning outcomes

By the end you can:

1. **Lead** an incident using an incident command structure, a severity model and NIST SP 800-61 Rev. 3, and **run** the reporting clocks for India and key foreign regimes.
2. **Acquire** memory, disk, cloud and SaaS evidence in order of volatility, **hash** and **document** it with chain of custody that would meet a section 63 BSA certificate.
3. **Collect** triage data at scale with Velociraptor and KAPE-style targets, and **decide** when a full image is needed.
4. **Analyse** Windows artefacts (event logs, Prefetch, Amcache, Shimcache, SRUM, LNK and Jump Lists, ShellBags, registry, `$MFT` and USN journal) and Linux artefacts to reconstruct user and attacker activity.
5. **Analyse** memory with Volatility 3 and MemProcFS to find suspicious processes, network connections and injected code.
6. **Investigate** cloud and Microsoft 365 / Entra ID incidents from audit logs.
7. **Build** super-timelines with Plaso and Timesketch and **state** findings with confidence levels.
8. **Plan** containment, eviction and recovery, including ransomware decisions, and **write** executive, regulator and post-incident reports.
9. **Verify** AI-assisted analysis against raw evidence and **protect** evidence confidentiality when using AI tools.

## Chapters and lessons

### Chapter 1 · Incident response foundations (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 NIST SP 800-61 Rev. 3 | Response mapped to CSF 2.0 functions (Govern to Recover); what changed from Rev. 2's four-phase lifecycle; ISO/IEC 27035 | Map your SEC302 playbook to Rev. 3's structure |
| 1.2 Roles | Incident commander, investigation lead, scribe, communications, legal, business owner; RACI | Assign roles for a 10-person company and a bank |
| 1.3 Severity and declaration | Impact-based severity, who can declare an incident, escalation triggers | Write a severity matrix with five worked examples |
| 1.4 Reporting clocks | CERT-In 6 hours; DPDP Rule 7 (individuals without delay, Board within 72 hours); RBI DAKSH 6 hours for banks; GDPR 72 hours; US SEC four business days after materiality | Build a clock sheet starting from a detection time |

**Check your understanding:** Why is the scribe one of the most important roles? Who should be allowed to declare a major incident? What starts each reporting clock?

### Chapter 2 · Preparation and forensic readiness (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Readiness | Logging and retention that answers incident questions, time sync, asset and identity inventories, out-of-band communication | Score your lab's readiness against 20 questions an investigator will ask |
| 2.2 Jump kit and tooling | Collection tools, write blockers, clean analysis workstation, evidence storage, licences | Assemble and document a jump kit |
| 2.3 Retainers and third parties | IR retainers, insurers, law enforcement, legal privilege | Write the contact and decision list for the first hour |
| 2.4 Exercises | CISA Tabletop Exercise Packages; injects; measuring exercise outcomes | Run a 60-minute tabletop and write findings |

**Check your understanding:** Which logs do investigators ask for first, and why? Why must the communications channel be out of band? What makes an exercise more than theatre?

### Chapter 3 · Evidence acquisition and handling (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Order of volatility | RFC 3227; memory before disk; live response vs pulling the plug | Order 12 evidence sources for a running server |
| 3.2 Acquisition | Memory with WinPmem and AVML; disk images (E01, raw) with FTK Imager or `dc3dd`; cloud snapshots; log exports | Acquire memory and disk from a lab VM and verify hashes |
| 3.3 Chain of custody | Who, what, when, where, hash, transfer records; ISO/IEC 27037; NIST SP 800-86 | Complete custody forms for every item from 3.2 |
| 3.4 Indian evidence law | Bharatiya Sakshya Adhiniyam 2023 section 63 (replaced Evidence Act section 65B from 1 July 2024): certificate with hash value and algorithm | Draft a section 63-style evidence certificate for your lab image |

**Check your understanding:** Why acquire memory before shutting a machine down? What does a matching hash prove, and what does it not? Why record the hash algorithm, not only the value?

### Chapter 4 · Triage collection at scale (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Why triage | Minutes per host vs hours per image; scoping 1,000 machines | Decide triage vs full image for five scenarios |
| 4.2 Velociraptor | Artifacts, hunts across endpoints, VQL basics, offline collectors | Hunt for a persistence artefact across lab hosts |
| 4.3 Target-based collection | KAPE targets and modules (check its licence for your use), Unix-like Artifacts Collector (UAC) for Linux and macOS | Collect from a Windows and a Linux VM and compare outputs |
| 4.4 Cloud and SaaS collection | Microsoft-Extractor-Suite for Microsoft 365 and Entra ID, AWS CloudTrail export, SaaS audit APIs | Export a test tenant's audit and sign-in logs |

**Check your understanding:** Why can triage miss evidence a full image would show? Why collect from all hosts before cleaning any? Which SaaS logs expire fastest by default?

### Chapter 5 · Windows forensics (weeks 5–6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Event logs | Security, System, PowerShell Operational, Sysmon, RDP-related logs; reconstructing logons and lateral movement | Build a logon timeline from EVTX with EvtxECmd |
| 5.2 Execution evidence | Prefetch, Amcache, Shimcache, SRUM, BAM; what each proves and its pitfalls | Prove or disprove that a program ran, using three artefacts |
| 5.3 File and folder activity | `$MFT`, USN journal, LNK files, Jump Lists, ShellBags, Recycle Bin | Reconstruct a user's file access on a published image |
| 5.4 Registry | Hives, persistence keys, USB device history, user assist | Parse hives with Registry Explorer or RECmd |
| 5.5 Detecting anti-forensics | Timestomping, log clearing (event 1102), deleted files; how artefacts contradict each other | Find planted timestomping in a lab image |

**Check your understanding:** Why does Shimcache presence not prove execution on modern Windows? How can the USN journal reveal a deleted file? What does a cleared log still tell you?

### Chapter 6 · Memory forensics (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Why memory | Running processes, network connections, decrypted data, injected code; what disk never shows | List five questions only memory can answer |
| 6.2 Volatility 3 | Process listing and trees, command lines, network objects, handles, `malfind` for suspicious memory regions; Volatility 2 deprecated since 2025 | Analyse a published memory image and identify the suspicious process |
| 6.3 MemProcFS | Memory as a file system; timeline and forensic mode | Repeat 6.2 with MemProcFS and compare |
| 6.4 Linux memory | AVML acquisition, symbol tables, Volatility 3 Linux plugins | Analyse a Linux memory sample from the lab |

**Check your understanding:** Why can a process be hidden from the task manager but visible in memory? What makes a `malfind` hit a lead rather than a verdict? Why do Linux memory analyses need matching symbols?

### Chapter 7 · Linux, cloud and SaaS investigations (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Linux artefacts | Auth logs, `journald`, shell history, cron and systemd persistence, SSH keys, web server logs | Investigate a compromised lab web server |
| 7.2 AWS and Azure | CloudTrail, GuardDuty, Azure Activity Log, storage access logs; access-key misuse patterns | Investigate a CloudTrail dataset for key misuse |
| 7.3 Microsoft 365 and Entra ID | Unified Audit Log, sign-in logs, mailbox rules, OAuth consents; the Midnight Blizzard (2024) and Salesloft Drift (2025) cases | Scope a business-email-compromise scenario in a test tenant |
| 7.4 Edge devices | Collecting from appliances, vendor integrity tools, why reboots and upgrades can destroy evidence or leave implants (CISA ED 25-03) | Write an evidence plan for a suspected firewall compromise |

**Check your understanding:** Why are cloud logs often the only evidence in a SaaS incident? What must you collect before revoking an attacker's tokens? Why is an appliance harder to investigate than a server?

### Chapter 8 · Timelines and analysis (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Super-timelines | Plaso (`log2timeline`), filtering, Timesketch for collaborative analysis | Build a super-timeline of a lab incident and tag key events |
| 8.2 Scoping | Patient zero, blast radius, accounts and hosts touched, data accessed | Write a scope statement with evidence |
| 8.3 Reasoning | Hypotheses, analysis of competing hypotheses, confidence levels, gaps | Write findings at "confirmed", "likely" and "possible" levels |
| 8.4 Public case studies | The DFIR Report's free intrusion write-ups as models | Reconstruct one public report's timeline in your own words |

**Check your understanding:** Why should every finding carry a confidence level? What is the risk of anchoring on the first suspicious event? How do you show what you could not see?

### Chapter 9 · Containment, eviction and recovery (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Containment options | Host isolation, account disablement, token revocation, network blocks, taking systems offline; business cost | Choose containment for four scenarios |
| 9.2 Eviction planning | Removing all access at once vs in stages; CISA's Eviction Strategies Tool (Playbook-NG and COUN7ER countermeasures, July 2025) | Build an eviction plan with the tool for a lab scenario |
| 9.3 Identity recovery | Order of credential resets, krbtgt twice, service accounts, MFA re-registration, OAuth app review | Write a reset sequence for a domain compromise |
| 9.4 Rebuild vs clean | When to rebuild, golden images, validating restored systems, monitoring for return | Write recovery acceptance criteria for a server |

**Check your understanding:** Why can piecemeal containment warn an attacker? Why reset krbtgt twice? What evidence shows an eviction worked?

### Chapter 10 · Ransomware response (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 The ransomware playbook | CISA #StopRansomware guide: detection, scoping, containment, recovery; double extortion and leak sites | Run the first 24 hours of a ransomware tabletop |
| 10.2 Decisions | Restore vs rebuild, paying (legal, sanctions and ethical questions; decided by leadership with counsel), law enforcement, insurers | Write a decision memo with options and consequences |
| 10.3 Indian and global cases | AIIMS Delhi (2022), C-Edge Technologies (2024), Change Healthcare (2024) | Compare the three: entry, impact, response lessons |
| 10.4 Recovery at speed | Prioritised restore order, clean-room recovery, validating backups before use | Produce a restore order for an illustrative hospital |

**Check your understanding:** Why restore identity systems first? What must be true before restoring from backup? Why should technical staff not negotiate alone?

### Chapter 11 · Communication, reporting and learning (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Updates | Situation reports for executives and engineers: known, unknown, next steps, decisions needed | Write three successive situation reports for a scenario |
| 11.2 Regulator and customer reports | CERT-In report fields, DPDP notices, customer statements; one fact base | Draft all three from one timeline |
| 11.3 Post-incident review | Blameless reviews, contributing factors, action items with owners; US Cyber Safety Review Board reports on Lapsus$ (2023) and the Microsoft Exchange Online intrusion (2024) as models (the board was disbanded in January 2025) | Write a post-incident review of a lab incident |
| 11.4 Law enforcement and insurers | India's National Cyber Crime Reporting Portal and police cyber cells, CERT-In coordination, preserving evidence for prosecution, insurer panels and approvals, legal privilege | Write the hand-off checklist for law-enforcement and insurer contact |

**Check your understanding:** What should never appear in an early customer statement? Why are blameless reviews more accurate? How do you make action items actually happen?

### Chapter 12 · AI in DFIR (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Useful AI tasks | Summarising timelines, explaining artefacts, drafting reports, parsing unusual log formats; Security Copilot incident summaries | Summarise a timeline with an assistant and mark every unsupported claim |
| 12.2 Evidence discipline | Every AI statement must cite an artefact; never let AI output into evidence without review; logging AI use in the case notes | Write the AI-use section of your DFIR procedure |
| 12.3 Confidentiality | Evidence may contain personal data (DPDP Act) and privileged material; approved tools, local models | Decide which evidence may go to which tool |
| 12.4 Investigating AI-enabled attacks | Agentic intrusions (Anthropic's GTG-1002 report, November 2025), malware that calls LLM APIs (Google, November 2025); evidence such as API keys and calls to model endpoints | List the artefacts an AI-orchestrated intrusion would leave |

**Check your understanding:** Why must AI output never enter the evidence chain unreviewed? What would you look for to show an intrusion was AI-orchestrated? When is a local model required?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Roles, severity and clocks | Clock sheet |
| 2 | 2 | Lab 2 · Readiness and tabletop | Readiness score, tabletop findings |
| 3 | 3 | Lab 3 · Acquisition and custody | Images, hashes, custody forms |
| 4 | 4 | Lab 4 · Velociraptor and UAC | Hunt results; **P1 due** |
| 5 | 5 | Lab 5 · Windows artefacts | Execution proof |
| 6 | 5 | Lab 5 (cont.) · Registry and anti-forensics | Findings |
| 7 | 6 | Lab 6 · Memory | Memory report; mid-term (AI off) |
| 8 | 7 | Lab 7 · Cloud and M365 | BEC scope report |
| 9 | 8 | Lab 8 · Super-timeline | Timeline and findings; **P2 due** |
| 10 | 9 | Lab 9 · Eviction plan | Plan |
| 11 | 10 | Ransomware tabletop | Decision memo |
| 12 | 11 | Reporting lab | Three reports, post-incident review |
| 13 | 12 | AI-in-DFIR lab | Annotated summary |
| 14 | 12 | P3 presentation | **P3 due** |
| 15 | Review | 6-hour practical investigation and oral defence | Final exam |

## Working with AI in this course

- **Use AI for:** explaining artefacts and tool output; writing parsing scripts for unusual logs; drafting situation reports and post-incident reviews from your verified timeline; generating Velociraptor or KQL queries you then test. Security Copilot, Claude, ChatGPT and Gemini all help; local open-weights models are preferred for real evidence.
- **Do without AI (drills):** artefact interpretation in Labs 5–6; building the timeline; confidence levels; the eviction order; the mid-term and the 6-hour final.
- **Verify AI output by:** requiring an artefact path, record ID or log line for every statement; re-running every query; comparing AI-produced timestamps with raw data and time zones; never accepting an AI explanation of an artefact without checking the tool documentation.
- **Where AI still fails here (show it, do not assume it):** in Lab 13 you count the unsupported claims in an AI timeline summary. Watch for invented times, merged events from different hosts, confident attribution with no evidence, and misread time zones. Anthropic's own report on an AI-run intrusion noted its agent "occasionally hallucinated credentials" and overstated findings: assistants on the defender's side make the same kind of errors.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs 1–10 | 25% |
| Projects P1 / P2 / P3 | 5% / 15% / 20% |
| Mid-term (AI off) | 10% |
| Final 6-hour practical (AI off) + oral defence of P3 | 25% |

**Mastery gate.** You pass when you can, without AI tools, in one six-hour session on an unseen case (disk image, memory image and cloud logs): (1) identify initial access, persistence, lateral movement and data accessed, with evidence and confidence levels; (2) produce a defensible chain of custody; (3) write a containment and eviction plan and the CERT-In and DPDP report drafts. An examiner must be able to reproduce every key finding from your notes.

## Industry reality

DFIR analysts, incident responders and IR consultants work in-house, at IR firms and MDR providers, and at CERTs (CERT-In, sector CSIRTs). Real anchors: NIST SP 800-61 Rev. 3; CISA's #StopRansomware guide and Eviction Strategies Tool; The DFIR Report's public intrusion write-ups; Indian cases (AIIMS 2022, C-Edge 2024) and India's reporting clocks.

**Interview questions from this course**

1. *You get a call: ransomware on file servers at 3 a.m. What do you do in the first hour?* Strong answer: declare and assemble roles, preserve evidence (memory, logs) while containing spread, protect backups and identity systems, scope, start reporting clocks, out-of-band communications, do not reboot everything blindly.
2. *How do you prove a program executed on a Windows host?* Strong answer: multiple artefacts (Prefetch, Amcache, SRUM, event 4688/Sysmon 1, BAM), their limits and versions, corroboration, timestamps and time zones.
3. *Walk me through chain of custody.* Strong answer: acquisition method, hashes and algorithm, documentation of every transfer, storage controls, working on copies, India's section 63 BSA certificate.
4. *An attacker has domain admin. How do you evict them?* Strong answer: scope first, plan a coordinated eviction, reset in the right order (krbtgt twice, privileged and service accounts), revoke tokens, remove persistence, rebuild Tier 0 where needed, monitor for return.
5. *How would you use AI in an investigation without risking the case?* Strong answer: approved tools only, no sensitive evidence to public models, AI output as leads not findings, artefact citations, logged AI use, human verification of every claim.

## Resources (free first)

- **Guides and standards:** [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) · [NIST SP 800-86](https://csrc.nist.gov/pubs/sp/800/86/final) · [RFC 3227](https://www.rfc-editor.org/rfc/rfc3227) · [CISA #StopRansomware guide](https://www.cisa.gov/stopransomware/ransomware-guide) · [CISA Eviction Strategies Tool](https://www.cisa.gov/resources-tools/resources/eviction-strategies-tool) · [CISA Tabletop Exercise Packages](https://www.cisa.gov/resources-tools/services/cisa-tabletop-exercise-packages) · [India's National Cyber Crime Reporting Portal](https://cybercrime.gov.in/)
- **Tools:** [Velociraptor](https://docs.velociraptor.app/) · [Eric Zimmerman's tools](https://ericzimmerman.github.io/) · [Volatility 3](https://github.com/volatilityfoundation/volatility3) · [MemProcFS](https://github.com/ufrisk/MemProcFS) · [WinPmem](https://github.com/Velocidex/WinPmem) · [AVML](https://github.com/microsoft/avml) · [Autopsy](https://github.com/sleuthkit/autopsy) · [Plaso](https://plaso.readthedocs.io/) · [Timesketch](https://timesketch.org/) · [UAC](https://github.com/tclahr/uac) · [Microsoft-Extractor-Suite](https://github.com/invictus-ir/Microsoft-Extractor-Suite)
- **Case material:** [The DFIR Report](https://thedfirreport.com/) · [CSRB review of the summer 2023 Microsoft Exchange Online intrusion](https://www.cisa.gov/resources-tools/resources/CSRB-Review-Summer-2023-MEO-Intrusion) · [CSRB review of Lapsus$](https://www.cisa.gov/resources-tools/resources/review-attacks-associated-lapsus-and-related-threat-groups-report)
- **Practice:** [CyberDefenders DFIR labs](https://cyberdefenders.org/blueteam-ctf-challenges/) · [Blue Team Labs Online](https://blueteamlabs.online/) · [NIST CFReDS forensic images](https://cfreds.nist.gov/)
- **Paid, optional:** SANS FOR500/FOR508 (GCFE/GCFA) are the best-known commercial courses; the free tools and images above cover the same artefacts.

## Sources

All checked 12 Oct 2026.

- NIST SP 800-61 Rev. 3 (Apr 2025) — https://csrc.nist.gov/pubs/sp/800/61/r3/final
- LiveLaw, Supreme Court rejects challenge to section 63(4) BSA hash-value requirement (May 2026) — https://www.livelaw.in/amp/top-stories/supreme-court-rejects-challenge-to-s634-bsa-mandating-hash-value-disclosure-for-electronic-evidence-535950
- CISA ED 25-03 (25 Sep 2025) — https://www.cisa.gov/news-events/directives/ed-25-03-identify-and-mitigate-potential-compromise-cisco-devices
- Google Cloud / Mandiant, *M-Trends 2026* (BRICKSTORM dwell near 400 days vs 90-day retention) — https://cloud.google.com/blog/topics/threat-intelligence/m-trends-2026
- Anthropic, "Disrupting the first reported AI-orchestrated cyber espionage campaign" (13 Nov 2025) — https://www.anthropic.com/news/disrupting-AI-espionage
- Google Threat Intelligence Group, *AI Threat Tracker* (Nov 2025) — https://cloud.google.com/blog/topics/threat-intelligence/threat-actor-usage-of-ai-tools
- CISA, Eviction Strategies Tool release (Jul 2025) — https://www.cisa.gov/news-events/news/cisa-releases-open-source-eviction-strategies-tool-cyber-incident-response
- Volatility 3 parity and Volatility 2 deprecation (May 2025), Volatility users mailing list — https://lists.volatilityfoundation.org/mailman3/hyperkitty/list/vol-users@lists.volatilityfoundation.org/2025/5/
- Cybersecurity Dive, DHS disbands the CSRB (Jan 2025) — https://www.cybersecuritydive.com/news/dhs-disbands-advisory-board-csrb/737976/
- Deccan Herald on AIIMS (Dec 2022) — https://www.deccanherald.com/amp/story/india/5-servers-of-aiims-were-affected-about-13-tb-of-data-encrypted-in-cyber-attack-mos-it-1172460.html ; CSO Online on C-Edge (Aug 2024) — https://www.csoonline.com/article/3480250/over-300-indian-banks-suffer-payment-disruption-from-ransomware-attack.html ; TechTarget on Change Healthcare (2024) — https://www.techtarget.com/cybersecurity/news/366582824/Change-Healthcare-breached-via-Citrix-portal-with-no-MFA
- CERT-In Directions (28 Apr 2022); DPDP Rules Rule 7; DSCI brief on RBI 2026 directions — links in [SEC305](../../year_3/SEC305_governance_risk_and_compliance/README.md#sources).

_Last reviewed: 2026-10_
