# Cybersecurity: Defense, Operations and Governance (SEC)

| Entry requirement | Years | Major courses | Market page | Interview loop |
|---|---|---|---|---|
| [CS213 Security Foundations](../../02_year_2_core_computer_science/semester_4/CS213_security_foundations/README.md) | 3–5 | SEC301–305, SEC401–404, SEC501 | [SEC roles and market (2026)](../../06_career_and_market_readiness/01_market_map/roles/SEC_cybersecurity_defense.md) | [AI-driven interviews](../../06_career_and_market_readiness/04_ai_driven_interviews/) |

This major trains **defenders**: the people who watch systems, detect and investigate attacks, respond to incidents, harden identities and endpoints, and run the governance that keeps an organisation within the law. It is the blue-team, SOC, DFIR and GRC path. It differs from two neighbouring majors:

- [Ethical Hacking and Offensive Security (OFF)](../ethical_hacking_offensive_security/README.md) trains authorised testers who find weaknesses.
- [Security Architecture (SAR)](../security_architecture/README.md) trains the people who design secure systems before they are built.

Defenders work with both, especially in purple-team exercises and design reviews.

**Safety and law.** Every course in this major is defensive. You practise only on your own lab, on test tenants you control, and on legal platforms. Attack techniques are named so you can detect them, never taught step by step. In India, unauthorised access is an offence under the IT Act, 2000; most countries have similar laws.

## 1. Who this major is for, and the roles it leads to

It suits people who like investigating, enjoy understanding how systems really behave, stay calm under pressure, and write clearly. You do not need to love breaking things; you need to love finding out what happened and making sure it does not happen again.

| Role | What people in it actually do | Where this major prepares you |
|---|---|---|
| SOC analyst, Tier 1 | Triage alerts in a SIEM, enrich them, close false positives, escalate real ones, write clear tickets | [SEC302](year_3/SEC302_security_operations_soc_siem_and_monitoring/README.md), [SEC301](year_3/SEC301_network_security_and_defense/README.md) |
| SOC analyst, Tier 2–3 | Investigate across identity, endpoint, network and cloud logs; scope incidents; lead containment | SEC302, [SEC303](year_3/SEC303_identity_and_access_management/README.md), [SEC304](year_3/SEC304_endpoint_and_operating_system_security/README.md), [SEC402](year_4/SEC402_digital_forensics_and_incident_response/README.md) |
| Detection engineer | Build, test and maintain detection rules as code; measure coverage and noise | [SEC401](year_4/SEC401_detection_engineering_and_threat_hunting/README.md) |
| Threat hunter | Search for attackers that detections missed, starting from hypotheses | SEC401, [SEC501](year_5/SEC501_frontier_seminar_threat_intelligence/README.md) |
| Incident responder / DFIR analyst | Lead incidents, acquire and analyse evidence, evict attackers, write regulator and executive reports | SEC402, [SEC403](year_4/SEC403_malware_analysis_for_defenders/README.md) |
| Malware analyst (defensive) | Triage and analyse samples safely, write YARA and behavioural detections | SEC403 |
| Threat intelligence analyst | Turn reporting and telemetry into decisions; manage sharing | SEC501 |
| IAM / identity security engineer | Run identity lifecycle, MFA, privileged access, AD and Entra ID security, identity threat detection | SEC303 |
| Security engineer (endpoint, network, SOC engineering) | Harden and monitor fleets, run vulnerability management, build pipelines and automation | SEC301, SEC304, [SEC404](year_4/SEC404_ai_in_security_operations/README.md) |
| GRC analyst / IT auditor / risk manager | Map controls to frameworks and laws, assess risk and vendors, run audits and evidence | [SEC305](year_3/SEC305_governance_risk_and_compliance/README.md) |
| SOC manager → Head of Security → CISO | Run teams, budgets and programmes; report risk to the board; own regulatory relationships | All of the above, plus [PRO301](../../05_shared_years_3_to_5/PRO301_professional_practice_ethics_law_and_responsible/README.md), [LCH502](../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md) |

**Market in one paragraph (details and sources on the [SEC market page](../../06_career_and_market_readiness/01_market_map/roles/SEC_cybersecurity_defense.md), checked October 2026).** The US Bureau of Labor Statistics projects information security analyst jobs to grow 21% from 2025 to 2035. ISC2's 2025 study found skills needs, not headcount, to be the main problem: 59% of respondents reported critical or significant skills needs, while 24% saw layoffs and 39% hiring freezes. Its September 2026 India study found "skills shortages have overtaken staffing shortages", with AI (52%) and cloud security (43%) the top needs. Entry is hard: in 2024, 31% of respondents said their teams had no entry-level staff. So this major front-loads hands-on engineering, identity, cloud and AI skills.

## 2. How AI is changing defensive security

All facts below were checked in October 2026; vendor statements are labelled as claims.

**What has changed (measured or documented).**

- **AI is in mainstream SOC products.**
  - Microsoft made Security Copilot, with AI agents for tasks such as phishing triage, part of Microsoft 365 E5 in November 2025.
  - Google's Security Operations Triage and Investigation agent investigates alerts in about a minute (Google documentation) and became generally available in 2026.
  - Elastic's Attack Discovery uses a language model to group alerts into attack narratives.
- **Adoption is real but partial.** ISC2's 2025 study: 28% of organisations had integrated AI security tools, 19% were testing them and 22% were evaluating them.
- **Evidence on value is mixed.**
  - Microsoft's randomised trial of its Phishing Triage Agent (Microsoft authors, November 2025) found up to 6.5 times as many true positives per analyst-minute and 77% better verdict accuracy. Most of the gain came from prioritising the queue.
  - On ExCyTIn-Bench (2025), multi-step investigations over 57 Sentinel log tables, the best model scored 0.606.
  - CyberSOCEval (Meta and CrowdStrike, 2025) found models far from saturating malware-analysis and threat-intelligence reasoning tasks.
- **Attackers use AI, but most breaches still come from basics.**
  - Anthropic reported in November 2025 that a Chinese state-sponsored group used an AI agent to do 80–90% of the tactical work in an espionage campaign against about 30 organisations. The same report noted that the AI "occasionally hallucinated credentials".
  - Google's Threat Intelligence Group documented the first malware querying a language model in live operations (PROMPTSTEAL, November 2025).
  - Mandiant's M-Trends 2026 nonetheless states it does "not consider 2025 to be the year where breaches were the direct result of AI". Exploits (32%) and voice phishing (11%) led initial access.
- **AI tools are a new attack surface.** EchoLeak (CVE-2025-32711, June 2025) let a crafted email make Microsoft 365 Copilot leak data with no user click. Malware samples now carry text meant to mislead AI analysis tools (Check Point, June 2025; Google, November 2025).

**What is being automated (analysis).** Alert enrichment, first-pass triage of high-volume alert types (reported phishing, impossible travel), query writing, incident summaries, compliance evidence collection, questionnaire drafting and first drafts of detection rules.

**What is growing in value (analysis).**

1. Investigation judgement and containment decisions with business impact.
2. Detection engineering as tested software.
3. Identity, SaaS and cloud security, where most modern intrusions start.
4. Evaluating and securing AI tools themselves.
5. Clear writing to executives and regulators under deadline.

India's regulators added deadlines that reward speed and accuracy:

- CERT-In: 6 hours for listed incidents.
- RBI's July 2026 directions: 6 hours on DAKSH for commercial banks.
- DPDP Rules 2025: a detailed report to the Data Protection Board within 72 hours.

**How this major responds.** Every course says which AI tools do what, sets AI-off drills, and requires you to verify AI output against evidence. SEC404 is a full course on building, evaluating, securing and governing AI in security operations.

## 3. The 5-year path

### Years 1–2: common core (courses that matter most for this major in bold)

| Semester | Courses (bold = critical for SEC) | Why it matters here |
|---|---|---|
| 1 | **[FND101](../../01_year_1_foundations/semester_1/FND101_programming_i_computational_thinking_with_python/README.md)** Python, **[FND102](../../01_year_1_foundations/semester_1/FND102_how_computers_work_bits_hardware/README.md)** How Computers Work, FND103 Discrete Maths, **[FND104](../../01_year_1_foundations/semester_1/FND104_the_developers_toolkit_linux_shell_git/README.md)** Linux, Shell and Git, [FND105](../../01_year_1_foundations/semester_1/FND105_ai_native_learning_and_building/README.md) AI-Native Learning, **[FND106](../../01_year_1_foundations/semester_1/FND106_technical_communication_and_professional_skills/README.md)** Technical Communication | Scripting for automation; Linux fluency; incident writing |
| 2 | FND111 Programming II, FND112 DSA I, FND113 Linear Algebra and Calculus, **[FND114](../../01_year_1_foundations/semester_2/FND114_web_foundations_http_html_css_and_javascript/README.md)** Web Foundations, **[FND115](../../01_year_1_foundations/semester_2/FND115_databases_i_data_modeling_and_sql/README.md)** SQL, **[FND116](../../01_year_1_foundations/semester_2/FND116_probability_and_statistics_i/README.md)** Probability and Statistics | HTTP for web attacks and logs; SQL for every SIEM query language; statistics for detection and risk |
| 3 | CS201 Algorithms, **[CS202](../../02_year_2_core_computer_science/semester_3/CS202_computer_architecture_and_systems_programming/README.md)** Architecture and C, **[CS203](../../02_year_2_core_computer_science/semester_3/CS203_operating_systems/README.md)** Operating Systems, **[CS204](../../02_year_2_core_computer_science/semester_3/CS204_computer_networks/README.md)** Computer Networks, CS205 Software Engineering I, CS206 Maths for ML | OS and network internals are the defender's foundation; C and architecture for malware analysis |
| 4 | **[CS213](../../02_year_2_core_computer_science/semester_4/CS213_security_foundations/README.md)** Security Foundations (entry requirement), **[CS215](../../02_year_2_core_computer_science/semester_4/CS215_cloud_and_devops_foundations/README.md)** Cloud and DevOps, [CS212](../../02_year_2_core_computer_science/semester_4/CS212_distributed_systems_i/README.md) Distributed Systems, [CS214](../../02_year_2_core_computer_science/semester_4/CS214_machine_learning_foundations/README.md) ML Foundations, CS211 Database Internals, CS216 Compilers | Threat modelling, crypto, auth, incident basics, law; cloud for modern incidents; ML for SEC404 |

### Years 3–5: the major

| Year · Semester | Major courses | Shared and overlap courses | Typical electives |
|---|---|---|---|
| 3 · 5 | [SEC301 Network Security and Defense](year_3/SEC301_network_security_and_defense/README.md) · [SEC302 Security Operations: SOC, SIEM and Monitoring](year_3/SEC302_security_operations_soc_siem_and_monitoring/README.md) · [SEC303 Identity and Access Management](year_3/SEC303_identity_and_access_management/README.md) | [PRO301 Professional Practice: Ethics, Law and Responsible AI](../../05_shared_years_3_to_5/PRO301_professional_practice_ethics_law_and_responsible/README.md) | [NET302 Windows Server and AD](../it_infrastructure_networking/year_3/NET302_windows_server_active_directory_and_enterprise/README.md) or [OFF301 Ethics, Law and RoE](../ethical_hacking_offensive_security/year_3/OFF301_ethics_law_rules_of_engagement_and_methodology/README.md) |
| 3 · 6 | [SEC304 Endpoint and OS Security](year_3/SEC304_endpoint_and_operating_system_security/README.md) · [SEC305 Governance, Risk and Compliance](year_3/SEC305_governance_risk_and_compliance/README.md) | [CAR301 Career Lab I](../../05_shared_years_3_to_5/CAR301_career_lab_i_dsa_mastery_portfolio_and_open/README.md) | [SAR302 Threat Modeling](../security_architecture/year_3/SAR302_threat_modeling/README.md) or [OPS303 Observability](../devops_sre_platform_engineering/year_3/OPS303_observability_metrics_logs_traces/README.md) |
| 4 · 7 | [SEC401 Detection Engineering and Threat Hunting](year_4/SEC401_detection_engineering_and_threat_hunting/README.md) · [SEC402 Digital Forensics and Incident Response](year_4/SEC402_digital_forensics_and_incident_response/README.md) | [IND401 Industry Co-op Studio](../../05_shared_years_3_to_5/IND401_industry_co_op_studio/README.md); overlap course A | [OFF401 Purple Teaming](../ethical_hacking_offensive_security/year_4/OFF401_red_teaming_adversary_emulation_and_purple/README.md) |
| 4 · 8 | [SEC403 Malware Analysis for Defenders](year_4/SEC403_malware_analysis_for_defenders/README.md) · [SEC404 AI in Security Operations](year_4/SEC404_ai_in_security_operations/README.md) | [CAR401 Career Lab II](../../05_shared_years_3_to_5/CAR401_career_lab_ii_interviews_system_design_and_ai/README.md); overlap course B | [SAR404 Resilience and Security Strategy](../security_architecture/year_4/SAR404_resilience_business_continuity_and_security/README.md) |
| 5 · 9 | [SEC501 Frontier Seminar: Threat Intelligence and Security Research](year_5/SEC501_frontier_seminar_threat_intelligence/README.md) | [RES501 Research Methods](../../05_shared_years_3_to_5/RES501_research_methods_and_scientific_writing/README.md) · [RES502 Reproducing Papers](../../05_shared_years_3_to_5/RES502_reading_reproducing_and_extending_papers/README.md) · [THS501 Thesis or Capstone I](../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) | — |
| 5 · 10 | — | [THS502 Thesis or Capstone II](../../05_shared_years_3_to_5/THS502_thesis_or_capstone_ii/README.md) · [LCH502 Career Launch and Founder Studio](../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md) | One advanced elective from another major |

Prerequisite chains inside the major (from [`catalog.json`](../../catalog.json)): SEC301 → SEC401; SEC302 → SEC402; SEC303 → SEC403; SEC304 → SEC404; SEC401 + SEC403 → SEC501. All Year 3 courses need only CS213.

**Mastery gates by stage.**

- **End of Year 3:** you can triage 20 unseen alerts in 90 minutes with 90% correct verdicts; harden and monitor Windows and Linux to a stated baseline; produce a correct incident reporting matrix for India.
- **End of Year 4:** you can run a six-hour forensic investigation on unseen evidence; ship tested detections as code; analyse a malware sample safely; evaluate an AI security tool with real metrics.
- **End of Year 5:** you can produce a peer-reviewable research or intelligence product that others can reproduce.

## 4. Skill map by level

| Level | You can… | Evidence |
|---|---|---|
| L0 · Absolute beginner | Use Linux and a terminal, read a log line, explain CIA (confidentiality, integrity, availability) and what a firewall does | FND104 labs; a home network diagram |
| L1 · Foundations | Explain TCP/IP, DNS, HTTP, processes and permissions; read packet captures; script small log parsers in Python; explain common attacks by root cause | CS203, CS204, CS213 labs |
| L2 · Practitioner (intern-ready) | Build a home SOC lab (Security Onion, Wazuh or Elastic, Sysmon); write SIEM queries in KQL or SPL; triage standard alerts; harden a host to CIS Level 1 | SEC301–302 labs; SEC302 P2 |
| L3 · Professional (job-ready) | Investigate incidents across identity, endpoint, network and cloud; write tested detections; run phishing-resistant MFA and privileged access programmes; map controls to ISO 27001, NIST CSF 2.0 and Indian law; meet 6-hour and 72-hour reporting duties | SEC303–305 P3s; SEC401 P2 |
| L4 · Expert (senior, hard to replace) | Lead major incidents and evictions; run detection and hunting programmes with honest coverage metrics; analyse malware and turn it into durable detections; build, evaluate and secure AI agents in the SOC; brief boards | SEC401–404 P3s; IND401 |
| L5 · Research and frontier | Produce intelligence assessments with calibrated judgements; design and publish reproducible security studies; work on open problems (AI-enabled adversaries, detection measurement, vulnerability ecosystem strain) | SEC501 P3; THS501–502 |

## 5. Recommended overlaps and electives

Choose one overlap in Year 4 (two overlap courses). Each maps to a real job family.

| Overlap | Composed of | Why a defender takes it | Job it maps to |
|---|---|---|---|
| [OV01 Cloud Security](../../04_overlaps/OV01_cloud_security/README.md) | CLD301, SAR401, SEC303 | Most incidents now touch cloud identity, keys and SaaS | Cloud security engineer, cloud detection and response |
| [OV03 DevSecOps](../../04_overlaps/OV03_devsecops/README.md) | OPS301, SAR305, SEC302 | Supply-chain and CI/CD attacks (build servers, actions, packages) | DevSecOps engineer, product security |
| [OV05 AI Security and Safety Engineering](../../04_overlaps/OV05_ai_security_safety/README.md) | AIE305, OFF403, SAR403 | Securing the AI systems that SOCs and businesses now run | AI security engineer |
| [OV07 Privacy Engineering](../../04_overlaps/OV07_privacy_engineering/README.md) | DEN404, SEC305, PRO301 | DPDP Act and GDPR duties become engineering work | Privacy engineer, data protection officer track |
| [OV10 FinTech Systems Engineering](../../04_overlaps/OV10_fintech_systems_engineering/README.md) | BE401, SEC305, DEN303 | RBI and SEBI frameworks, payments fraud | Security and risk roles in banks and fintechs |

**Electives worth taking:**

- [NET302 Windows Server and Active Directory](../it_infrastructure_networking/year_3/NET302_windows_server_active_directory_and_enterprise/README.md), because AD is still where many intrusions are won or lost.
- [NET402 Network Security Engineering](../it_infrastructure_networking/year_4/NET402_network_security_engineering/README.md).
- [OPS303 Observability](../devops_sre_platform_engineering/year_3/OPS303_observability_metrics_logs_traces/README.md), for log pipelines.
- [OPS304 SRE and Incident Response](../devops_sre_platform_engineering/year_3/OPS304_site_reliability_engineering_slos_error_budgets/README.md), for incident command practice.
- [OFF401 Purple Teaming](../ethical_hacking_offensive_security/year_4/OFF401_red_teaming_adversary_emulation_and_purple/README.md).
- [SAR302 Threat Modeling](../security_architecture/year_3/SAR302_threat_modeling/README.md) and [SAR303 Zero Trust](../security_architecture/year_3/SAR303_zero_trust_architecture/README.md).
- [AIE305 Evaluating LLM Systems](../ai_engineering/year_3/AIE305_evaluating_llm_systems/README.md), which strengthens SEC404.
- [OPS403 AIOps and Agentic Operations](../devops_sre_platform_engineering/year_4/OPS403_aiops_and_agentic_operations/README.md).

## 6. Flagship industry project

The [SEC flagship project](../../06_career_and_market_readiness/05_industry_projects/SEC_cybersecurity_defense.md) combines the major into one portfolio piece: a working SOC for an illustrative regulated Indian company, built in a home lab and cloud test tenants. It includes:

- onboarded log sources and tested detections as code;
- an identity threat detection layer;
- an evaluated AI triage assistant with prompt-injection tests;
- a full incident investigation with forensic evidence;
- CERT-In, DPDP and RBI-style reports;
- a board-level risk summary.

The best course projects to reuse are SEC302 P3, SEC303 P3, SEC401 P3, SEC402 P3 and SEC404 P3.

## 7. Certifications worth having (optional, never required)

Certifications are filters, not proof of skill. Labs, write-ups and the flagship project show skill. Names, versions and prices change often: check the vendor page before paying.

| Certification | Stage | Honest value note (checked October 2026) |
|---|---|---|
| CompTIA Security+ | End of Year 2–3 | Common early-career filter (see the market page). Current exam SY0-701; training providers expect SY0-801, with AI topics, around late 2026 (unconfirmed by CompTIA). Knowledge-based, so pair it with labs |
| ISC2 Certified in Cybersecurity (CC) | Year 2–3 | Entry-level and widely recognised. The free "One Million Certified in Cybersecurity" programme closed to new enrolments on 20 May 2026; paid exams continue |
| CompTIA CySA+ | Year 3–4 | Analyst-focused; CS0-004 launched 23 June 2026 with security operations at 34% of the exam and an objective on AI in security operations. Good fit for SOC roles |
| Blue Team Level 1 (BTL1) | Year 3–4 | 24-hour practical incident response exam, now run by Centri (Security Team Training Ltd); about £399 including training. Practical, respected by SOC hiring managers |
| HTB Certified Defensive Security Analyst (CDSA) | Year 4 | 7-day practical lab plus a written report, after the HTB Academy SOC Analyst path. Hands-on and report-heavy, which is closer to the real job |
| Microsoft SC-200 (Security Operations Analyst) | Year 4 | Worth it if you target Microsoft-centred SOCs: covers Defender XDR, Sentinel, KQL and Security Copilot |
| GIAC GCIH / GCFA | Year 4–5 or employer-paid | Highly respected incident handling (GCIH, linked to SANS SEC504) and forensics (GCFA, linked to SANS FOR508) certifications with hands-on CyberLive questions. Expensive; usually employer-funded |
| ISO/IEC 27001 Lead Implementer / Lead Auditor | Year 4–5 for GRC track | Commonly requested for ISO 27001 implementation, consulting and audit work; choose a provider whose course is accredited. Pair it with SEC305 P2 |
| CISSP | After 5 years' experience | Management-level credential; ISC2 requires five years of relevant paid work experience. A goal for senior and CISO-track roles, not for students |
| CEH (EC-Council) | Optional | Offensive-oriented, and EC-Council markets an AI-integrated v13 (vendor claims). Resellers cite recognition under the US DoD 8140 framework, so it appears in some job filters, but for defenders CySA+, BTL1 or CDSA show more relevant skill. Offensive students should compare it with OFF-major options |

## 8. The interview loop

Typical loop (varies by employer; details on the [SEC market page](../../06_career_and_market_readiness/01_market_map/roles/SEC_cybersecurity_defense.md)):

1. Fundamentals screen: networking, Windows and Linux internals, authentication.
2. Scenario: an alert plus logs; what happened and what next.
3. Hands-on: write a SIEM query, analyse a packet capture or event log.
4. Incident response tabletop.
5. Behavioural round: ethics, pressure, explaining risk.

Increasingly, take-home or live exercises allow AI tools and assess how you verify their output. Prepare with:

- the interview questions at the end of every SEC course README;
- [CAR401](../../05_shared_years_3_to_5/CAR401_career_lab_ii_interviews_system_design_and_ai/README.md);
- the [AI-driven interviews](../../06_career_and_market_readiness/04_ai_driven_interviews/) section.

## 9. Fast track for working professionals

For people already working in IT support, network or system administration, or software development. Budget 12–18 months at 12–15 hours a week. Skip what you already know and prove it with the course mastery gates.

| Months | Do | Notes |
|---|---|---|
| 0–2 | CS213 (skim what you know); build the SEC301 home lab | Network admins already have most of CS204; sysadmins most of CS203 |
| 2–5 | SEC302 and SEC304 labs and P2s | This is the shortest path to a SOC Tier 1–2 role; take Security+ or CySA+ if your target employers filter on it |
| 5–7 | SEC303 (identity) | Very high return for anyone who has administered AD or Microsoft 365 |
| 7–10 | SEC401 or SEC402, depending on target role (detection engineering or incident response) | Build P3 as your portfolio centrepiece |
| 10–12 | SEC404 Chapters 3–4 and 7; the flagship project | Shows you can use and evaluate AI tools, which is now asked in interviews |
| Optional | SEC305 if moving into GRC; BTL1, CDSA or SC-200 as a practical credential | Auditors and IT governance staff can start with SEC305 and SEC302 |

**Common transitions.**

- **IT support → SOC Tier 1:** SEC302 plus SEC304.
- **Network administrator → network security or SOC:** SEC301 plus SEC302.
- **Windows or Microsoft 365 administrator → IAM or identity threat detection:** SEC303 plus SEC302.
- **Developer → detection engineer or SOC automation:** SEC302, SEC401 and SEC404.
- **Auditor → GRC analyst:** SEC305 plus SEC302 Chapter 1.

## Sources

All checked 12 Oct 2026.

- SEC market page and its sources (BLS, ISC2 2024, 2025 and India 2026 studies, WEF, Payscale) — [roles/SEC_cybersecurity_defense.md](../../06_career_and_market_readiness/01_market_map/roles/SEC_cybersecurity_defense.md)
- Microsoft Security blog, Security Copilot with Microsoft 365 E5 (18 Nov 2025) — https://www.microsoft.com/en-us/security/blog/2025/11/18/agents-built-into-your-workflow-get-security-copilot-with-microsoft-365-e5/
- Google Cloud documentation, Triage and Investigation agent — https://docs.cloud.google.com/chronicle/docs/secops/triage-investigation-agent
- Elastic, Attack Discovery GA — https://www.elastic.co/blog/production-ready-ai-capabilities
- Randomized Controlled Trials for Phishing Triage Agent, arXiv 2511.13860 — https://arxiv.org/abs/2511.13860 ; ExCyTIn-Bench, arXiv 2507.14201 — https://arxiv.org/abs/2507.14201 ; CyberSOCEval, arXiv 2509.20166 — https://arxiv.org/abs/2509.20166
- Anthropic, "Disrupting the first reported AI-orchestrated cyber espionage campaign" (13 Nov 2025) — https://www.anthropic.com/news/disrupting-AI-espionage
- Google Threat Intelligence Group, *AI Threat Tracker* (Nov 2025) — https://cloud.google.com/blog/topics/threat-intelligence/threat-actor-usage-of-ai-tools
- Google Cloud / Mandiant, *M-Trends 2026* — https://cloud.google.com/blog/topics/threat-intelligence/m-trends-2026
- The Hacker News, EchoLeak, CVE-2025-32711 (12 Jun 2025) — https://thehackernews.com/2025/06/zero-click-ai-vulnerability-exposes.html ; Check Point Research (25 Jun 2025) — https://research.checkpoint.com/2025/ai-evasion-prompt-injection/
- CERT-In Directions (28 Apr 2022) — https://www.cert-in.org.in/PDF/CERT-In_Directions_70B_28.04.2022.pdf ; DPDP Rules, Rule 7 — https://dpdpa.com/dpdparules/rule7.html ; DSCI brief on RBI 2026 directions — https://www.dsci.in/files/content/knowledge-centre/2026/dsci-brief-on-rbi-cybersecurity-commercial-banks-directions-2026.pdf
- CompTIA CySA+ V4 (CS0-004) — https://www.comptia.org/en/certifications/cybersecurity-analyst/v4/ ; Security+ SY0-801 expectations (training provider, unconfirmed) — https://trainingcamp.com/articles/comptia-security-sy0-801-release-date-and-everything-we-know-so-far/
- ISC2, One Million Certified in Cybersecurity conclusion (Apr 2026) — https://www.isc2.org/insights/2026/04/one-million-certified-cyber-conclusion ; ISC2 CISSP experience requirement — https://www.isc2.org/certifications/cissp
- Centri, BTL1 — https://www.centri.org/certifications/blue-team-level-1 ; Hack The Box, CDSA announcement — https://www.hackthebox.com/blog/defensive-security-analyst-certification ; GIAC GCIH — https://www.giac.org/certifications/certified-incident-handler-gcih/ ; Microsoft SC-200 study guide — https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-200

_Last reviewed: 2026-10_
