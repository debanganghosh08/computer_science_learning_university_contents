# SEC402 · Labs and projects

Practise only on your own lab VMs and test tenants, on forensic images published for training (NIST CFReDS, CyberDefenders, Blue Team Labs Online, The DFIR Report's companion material where provided), and on scenarios your instructor builds. Work on copies, never on originals; hash everything; keep a case notebook with times in UTC and IST. Every submission includes the case notebook, hashes, tool versions and a report that someone else could reproduce.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Roles, severity and clocks | Severity matrix, RACI and a reporting clock sheet (CERT-In, DPDP, RBI, GDPR, SEC) for a given detection time | Matrix, RACI, clock sheet with sources | 3 h |
| 2 · Readiness and tabletop | Score the lab's forensic readiness; run a 60-minute tabletop with injects | Readiness score with gaps, tabletop findings | 4 h |
| 3 · Acquisition and custody | Acquire memory (WinPmem, AVML) and disk (E01) from lab VMs; verify hashes; complete custody forms; draft a section 63 BSA-style certificate | Hash logs, custody forms, certificate draft | 5 h |
| 4 · Triage at scale | Velociraptor hunt for a persistence artefact across lab hosts; UAC collection from Linux; export a test tenant's audit and sign-in logs | Hunt results, collection archives with hashes | 5 h |
| 5 · Windows artefacts | On a published image, prove which programs ran and which files a user opened, with at least three artefacts each; find planted timestomping | Findings table citing artefact paths, tool outputs | 7 h |
| 6 · Memory | Analyse a published memory image with Volatility 3 and MemProcFS; identify the suspicious process, its parent, network connections and injected regions | Memory report with plugin outputs | 5 h |
| 7 · Cloud and Microsoft 365 | Scope a business-email-compromise scenario in your test tenant from sign-in, audit and mailbox logs | Scope report and timeline | 5 h |
| 8 · Super-timeline | Build a Plaso super-timeline of a lab incident; load it into Timesketch; tag key events; write findings with confidence levels | Timesketch export, findings | 5 h |
| 9 · Eviction plan | Use CISA's Eviction Strategies Tool to build an eviction plan for a domain-compromise scenario; write the credential reset order | Plan export, reset order with reasons | 4 h |
| 10 · AI in DFIR | Have an assistant summarise your Lab 8 timeline; mark every unsupported or wrong claim; write the AI-use section of your DFIR procedure | Annotated summary, error count by type, procedure | 3 h |

## Projects

### P1 · Court-ready evidence package (L1, ~6 hours)

**Real-world inspiration.** Since 1 July 2024, electronic evidence in India is governed by section 63 of the Bharatiya Sakshya Adhiniyam, 2023, whose certificate includes the record's hash value and the algorithm used; the Supreme Court upheld the hash requirement in May 2026. Internationally, RFC 3227 and ISO/IEC 27037 describe evidence collection and handling.

**What to build.** From a lab Windows VM running a scripted "suspicious" scenario (created by a classmate), acquire memory and disk, collect triage data, and package the evidence: acquisition notes, hashes (SHA-256 plus one other), custody forms for every transfer, storage controls, and a draft section 63-style certificate.

**Acceptance criteria**
- A second person re-verifies every hash from the package alone and gets matching results.
- Acquisition order follows the order of volatility, and any deviation is justified in writing.
- Every transfer of every item has a custody entry (who, when, why, hash before and after).
- The notes are complete enough that the second person can repeat the acquisition steps on a fresh VM.

**Stretch goals.** Acquire a cloud disk snapshot and audit-log export from a free-tier account with the same discipline.

**What it proves to an employer.** Your evidence will survive scrutiny from lawyers, auditors and courts.

### P2 · Business email compromise investigation (L2, ~15 hours)

**Real-world inspiration.** Microsoft's January 2024 guidance on Midnight Blizzard describes an intrusion that moved from a test account without MFA to a legacy OAuth application and then to corporate mailboxes. Business email compromise in Microsoft 365 and Google Workspace remains one of the most common incidents IR teams handle. The scenario below is illustrative and runs only in your own test tenant.

**What to build.** A partner sets up a scenario in your test tenant using only normal administrative and user actions (for example: sign-ins from a VPN location, an OAuth app consent, a new inbox forwarding rule, mail searches and file downloads). You investigate with Microsoft-Extractor-Suite or native exports and deliver: timeline, scope (accounts, mailboxes, files, apps), persistence found, containment and eviction steps, and notification analysis under the DPDP Act.

**Acceptance criteria**
- Your timeline matches the partner's hidden action log on at least 90% of actions, with every finding citing a log record.
- All persistence (rules, consents, new MFA methods, app credentials) is found and listed with the removal step.
- The containment plan revokes sessions and tokens in the right order, and a test shows the attacker's session no longer works.
- The report includes a one-page executive summary and a DPDP notification assessment with reasons.

**Stretch goals.** Repeat in Google Workspace; write Sigma or KQL detections for every step you found.

**What it proves to an employer.** You can investigate the cloud and SaaS incidents that dominate modern IR work, end to end.

### P3 · Ransomware intrusion: investigation, recovery and reporting (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** KPMG's advisory on the July 2024 C-Edge Technologies attack, which cut about 300 small Indian banks off retail payments, traced the intrusion to a misconfigured Jenkins server. The government told Parliament the AIIMS Delhi attack (2022) spread because of improper network segmentation. UnitedHealth's CEO testified that the Change Healthcare attack (2024) began with stolen credentials on a portal without MFA. The case below is built by your instructor (or from a published multi-host training scenario) and is illustrative.

**What to build.** A complete case on a multi-host lab intrusion (build server, domain controller, file server, two workstations, cloud storage) that ends in simulated encryption:
1. evidence collection plan and custody records;
2. analysis of disk, memory, event logs and cloud logs: initial access, privilege escalation, lateral movement, data accessed or staged, and encryption timing, each with confidence levels;
3. a super-timeline in Timesketch;
4. an eviction plan (CISA Eviction Strategies Tool) and an identity reset order;
5. a prioritised restore order with validation steps;
6. reports: a CERT-In incident report draft, DPDP Board and individual notices, an RBI-style 6-hour report as if the victim served banks, and a board briefing;
7. a blameless post-incident review with at least eight action items;
8. an audit of an AI-generated summary of your case, counting unsupported claims.

**Acceptance criteria**
- Initial access, the first privileged account compromised, every compromised host, and the encryption start time are identified correctly against the instructor's ground truth, each backed by at least two independent artefacts.
- The timeline is reproducible from your notes by an examiner within two hours.
- All regulatory drafts are consistent with each other and with the timeline (checked line by line), and deadlines are computed from the stated detection time.
- The eviction plan addresses every persistence mechanism found; the restore order puts identity and security tooling first and states validation criteria.
- The post-incident review assigns each action an owner, a date and a measurable outcome.

**Stretch goals.** Write detections for each stage and test them against the case data; brief a non-technical audience in 10 minutes and collect their questions.

**What it proves to an employer.** You can run a serious incident from first evidence to regulator report and lessons learned, which is what incident response leads and DFIR consultants are hired to do.

## Feeds into

- [SEC501 Frontier Seminar](../../year_5/SEC501_frontier_seminar_threat_intelligence/README.md): incident findings become intelligence and research questions.
- [SEC403 Malware Analysis for Defenders](../SEC403_malware_analysis_for_defenders/README.md): samples found during investigations are analysed safely there.
- [IND401 Industry Co-op Studio](../../../../05_shared_years_3_to_5/IND401_industry_co_op_studio/README.md): IR firms and MDR providers are common co-op hosts.
- [THS501 Thesis or Capstone I](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md): forensic artefact research and AI-assisted DFIR evaluation are strong capstone topics.
