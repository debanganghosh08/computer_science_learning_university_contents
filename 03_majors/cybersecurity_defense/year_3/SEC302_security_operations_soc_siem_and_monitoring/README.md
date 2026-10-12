# SEC302 · Security Operations: SOC, SIEM and Monitoring

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 5 | 4 (≈ 120 hours) | L2 → L3 | [CS213](../../../../02_year_2_core_computer_science/semester_4/CS213_security_foundations/README.md) | [SEC402](../../year_4/SEC402_digital_forensics_and_incident_response/README.md), [SEC401](../../year_4/SEC401_detection_engineering_and_threat_hunting/README.md), [SEC404](../../year_4/SEC404_ai_in_security_operations/README.md), [OV03 DevSecOps](../../../../04_overlaps/OV03_devsecops/README.md) |

Part of the [Cybersecurity Defense major](../../README.md). Pairs with [SEC301](../SEC301_network_security_and_defense/README.md) in the same semester. All practice uses your own lab, public datasets recorded for training, and legal practice platforms.

## Why this course matters now

A security operations centre (SOC) is the team that watches an organisation's logs and alerts, decides what is real, and starts the response. The job is changing fast. Microsoft made Security Copilot part of every Microsoft 365 E5 licence in November 2025 and shipped AI agents for phishing triage; Google made its Security Operations "Triage and Investigation agent" available in 2026; Elastic's Attack Discovery groups hundreds of alerts into a few attack narratives with a large language model (LLM). In a Microsoft-run randomised trial, analysts using the phishing triage agent found up to 6.5 times as many true positives per analyst-minute, most of it from better queue ordering. But Microsoft's own investigation benchmark, ExCyTIn-Bench, showed the best model scoring 0.606 on realistic multi-step investigations over 57 Sentinel log tables, so a human still has to finish the hard ones. Attackers are also faster: Mandiant measured the median time from initial access to hand-off between criminal groups falling from more than 8 hours (2022) to 22 seconds (2025). In India, CERT-In wants listed incidents reported within 6 hours and RBI's July 2026 directions require commercial banks to report on its DAKSH platform within 6 hours, so detection and triage speed now have legal deadlines.

## Learning outcomes

By the end you can:

1. **Explain** SOC models (in-house, managed security service provider (MSSP), managed detection and response (MDR), hybrid) and the work of each tier, and **choose** one for a stated organisation.
2. **Onboard** log sources (Windows, Linux, firewall, DNS, proxy, identity provider, cloud audit logs, email) into a SIEM, **normalise** them to a schema (ECS, OCSF or ASIM), and **detect** when a source goes silent.
3. **Write** investigation queries in at least two of KQL, SPL and ES|QL, including joins, time windows and aggregations.
4. **Triage** alerts with a repeatable method, **classify** them as true positive, benign true positive or false positive, and **document** the evidence.
5. **Investigate** the six most common alert families (phishing, suspicious sign-in, malware on an endpoint, privilege change, cloud key misuse, data movement) and **scope** them.
6. **Design** playbooks and SOAR automations with safe approval steps.
7. **Measure** SOC performance (MTTD, MTTA, MTTR, true-positive rate, coverage) and **explain** how each can be gamed.
8. **Evaluate** an AI SOC assistant on a labelled alert set and **report** its error types.
9. **Write** a clear escalation, shift handover and regulator-ready incident summary.

## Chapters and lessons

### Chapter 1 · The SOC and its people (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 What a SOC is for | Detect, triage, respond, improve; MITRE's *11 Strategies of a World-Class Cybersecurity Operations Center* (2022) | Write the mission and scope statement for a 2,000-employee fintech SOC (illustrative) |
| 1.2 Models | In-house, MSSP, MDR, hybrid, follow-the-sun; what is outsourced and what never can be (business context, decisions) | Compare costs and risks of three models in a table |
| 1.3 Roles and tiers | Tier 1 triage, Tier 2 investigation, Tier 3 and incident response, detection engineering, threat intelligence, SOC manager | Map 10 real job postings to tiers and skills |
| 1.4 Maturity | SOC-CMM self-assessment; why tooling maturity ≠ capability | Score a described SOC and propose three improvements |

**Check your understanding:** Why can an MSSP not decide whether to shut down a payment system? What breaks when Tier 1 never gets feedback on escalations? Why is "number of tools" a poor maturity measure?

### Chapter 2 · Log sources and telemetry quality (weeks 1–2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 What to collect | Windows Security log and Sysmon, Linux `auth`/`journald`/`auditd`, firewall, proxy, DNS, EDR, identity provider sign-ins (Entra ID, Okta), cloud audit (AWS CloudTrail, Azure Activity), SaaS and email logs | Build a log-source inventory with owner, volume and use case for each |
| 2.2 Time and integrity | Clock sync (CERT-In requires NTP to NIC or NPL servers), time zones, ingestion delay vs event time, tamper resistance | Measure the ingestion delay for three lab sources |
| 2.3 Normalisation | Elastic Common Schema (ECS), Open Cybersecurity Schema Framework (OCSF), Microsoft ASIM; why field names matter for detections | Map 20 raw fields from two sources to ECS |
| 2.4 Retention and cost | Hot/warm/cold tiers, data lakes (Microsoft Sentinel data lake GA September 2025), CERT-In's 180-day retention, Mandiant's observation that some intrusions outlast 90-day retention | Write a retention policy that meets legal duties at a stated budget |
| 2.5 Silent failures | Detecting missing sources, parsing errors and agent outages | Build an alert that fires when a source stops sending for 30 minutes |

**Check your understanding:** Which log source would you onboard first for a cloud-only startup, and why? Why does event time vs ingestion time matter for a 6-hour reporting clock? What do you lose by dropping "noisy" logs to save money?

### Chapter 3 · SIEM architecture and platforms (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 The pipeline | Agents (Elastic Agent, Wazuh agent, Splunk forwarder, Azure Monitor Agent), shippers, parsing, enrichment, indexing, search | Trace one event from a lab VM to the search UI and time each stage |
| 3.2 Open-source stack | Wazuh (agents, decoders, rules, file integrity monitoring) and Elastic Security (detection rules, timelines, cases) | Deploy Wazuh or Elastic in the lab with two agents |
| 3.3 Commercial platforms | Splunk Enterprise Security, Microsoft Sentinel (moving fully into the Defender portal; Azure portal support ends 31 March 2027), Google Security Operations | Read each vendor's architecture page and compare data model, query language and pricing basis |
| 3.4 Correlation and risk | Single-event rules vs correlation over time windows; risk-based alerting (scores accumulate per entity before an alert) | Write one correlation rule and one risk rule for the same behaviour |

**Check your understanding:** Why does parsing at ingest vs at search time change both cost and flexibility? What is the risk of a SIEM that only the vendor's consultants can change? When does risk-based alerting hide a real attack?

### Chapter 4 · Query languages for investigations (weeks 4–5)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 KQL | `where`, `summarize`, `bin`, `join`, `make-series`, `mv-expand`; Microsoft Sentinel and Defender advanced hunting | Answer 10 questions on a sample Sentinel dataset |
| 4.2 SPL | `search`, `stats`, `eval`, `transaction`, `tstats`; Splunk's free Boss of the SOC (BOTS) datasets | Solve 10 BOTS v3 questions |
| 4.3 ES\|QL and Lucene/KQL in Elastic | Piped queries, `STATS ... BY`, enrich policies | Rewrite five SPL answers in ES\|QL |
| 4.4 Query craft | Start broad then narrow; time-box; count before you read; avoid joins on high-cardinality fields; saved searches | Optimise a slow query and report the before/after runtime |

**Check your understanding:** Why should you count events before reading them? When is a `join` the wrong tool? How do you check that a query returns nothing because nothing happened, not because the field name is wrong?

### Chapter 5 · Alert triage (weeks 5–6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 The triage method | What fired, on what entity, when, why it matters; what would make it benign; enrichment (asset owner, user role, threat intel, history) | Triage 30 lab alerts with a written template |
| 5.2 Verdict classes | True positive, benign true positive (real activity, authorised), false positive (logic wrong); escalation criteria and severity | Re-label 20 historical alerts and justify each |
| 5.3 Alert fatigue | Alahmadi et al., *99% False Positives* (USENIX Security 2022): why analysts distrust tools; feedback loops to detection engineering | Write three tuning requests with evidence |
| 5.4 Bias and pressure | Confirmation bias, anchoring on the first hypothesis, end-of-shift closure; peer review of closures | Review a peer's 10 closures and find disagreements |

**Check your understanding:** Why is "benign true positive" a separate class from "false positive"? What evidence would make you escalate an alert you think is probably benign? Why must closed alerts be sampled and reviewed?

### Chapter 6 · Investigation patterns for common alert families (weeks 7–8)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Phishing reports | Header analysis, URL and attachment detonation in a sandbox, who else received it, who clicked, mailbox rule checks | Investigate five reported emails in a lab mail dataset |
| 6.2 Suspicious sign-ins | Impossible travel, new device, MFA fatigue patterns, token reuse; identity-provider logs (continues in [SEC303](../SEC303_identity_and_access_management/README.md)) | Scope a compromised-account scenario across sign-in and audit logs |
| 6.3 Endpoint malware alerts | Process tree, parent-child anomalies, network connections, persistence checks, EDR isolation decision ([SEC304](../SEC304_endpoint_and_operating_system_security/README.md)) | Investigate two EDR-style alerts from a public dataset |
| 6.4 Privilege and configuration changes | New admin, group changes, disabled logging, new OAuth app consent | Build a "who changed what" timeline for a privilege escalation |
| 6.5 Cloud and data movement | Leaked access keys, unusual API calls, large downloads, SaaS exports; the 2024 Snowflake customer intrusions (stolen credentials, no MFA) | Investigate a CloudTrail scenario from a public dataset |

**Check your understanding:** In a phishing case, why do you search for all recipients before contacting the reporter? What is the first thing to check when a VPN login comes from a new country? Why can a single cloud API call be more serious than 1,000 failed logins?

### Chapter 7 · Playbooks, case management and SOAR (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Playbooks | Trigger, scope, steps, decision points, escalation, evidence, closure; CISA federal incident and vulnerability response playbooks; NIST SP 800-61 Rev. 3 | Write a playbook for a reported phishing email |
| 7.2 Case management | Cases vs alerts, observables, tasks, audit trail; TheHive as an example | Run three lab alerts through a case tool |
| 7.3 SOAR | Enrichment automation, ticketing, notifications, containment actions; Shuffle (open source), Sentinel automation rules and playbooks, Splunk SOAR | Automate enrichment of IP, domain and hash observables |
| 7.4 Safe automation | Which actions may run without approval, rate limits, rollback, blast radius; the July 2024 CrowdStrike outage as a reminder that security automation can cause outages | Classify 15 response actions as auto, approve or never-auto |

**Check your understanding:** Why should account disablement usually need approval but enrichment should not? What must a playbook record so a regulator report can be written later? How do you test a SOAR playbook without touching production?

### Chapter 8 · SOC metrics and reporting (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Time metrics | Mean and median time to detect, acknowledge, contain and resolve; why medians and percentiles beat means | Compute MTTD/MTTR distributions from a provided case export |
| 8.2 Quality metrics | True-positive rate per rule, escalation accuracy, reopen rate, coverage mapped to MITRE ATT&CK | Rank rules by value and cost |
| 8.3 Gaming and Goodhart's law | Closing fast to hit targets; splitting incidents; "coverage" that never fired | Find three ways each metric could be gamed and a counter-metric |
| 8.4 Reporting upward | Monthly report for a CISO and board: trends, risks, decisions needed; M-Trends 2026 benchmarks (52% of intrusions detected internally, global median dwell time 14 days) used carefully | Write a one-page monthly SOC report |

**Check your understanding:** Why can MTTR improve while security gets worse? Which metric would you show a board, and which only to the team? What does "internal detection" measure that dwell time does not?

### Chapter 9 · AI copilots and agents in the SOC (weeks 11–12)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 What the tools do | Microsoft Security Copilot and its agents, Google SecOps Triage and Investigation agent, Elastic Attack Discovery and AI Assistant, CrowdStrike Charlotte AI, open models run locally | Compare three products' documented capabilities and limits |
| 9.2 Evidence on value | Microsoft's randomised trial of the Phishing Triage Agent (arXiv 2511.13860; authors are Microsoft staff): up to 6.5× true positives per analyst-minute, 77% better verdict accuracy, 83% of the gain from queue prioritisation | Read the paper; list what it does and does not prove |
| 9.3 How to verify an AI verdict | Ask for cited evidence (event IDs, query results), re-run queries, sample AI closures daily, compare with a labelled set, track disagreement rate | Audit 25 AI-closed alerts from a lab run |
| 9.4 AI-specific risks | Prompt injection through log fields, email bodies and file contents (Google found malware with hard-coded prompts aimed at AI analysis, 2025); hallucinated fields; over-trust; data leaving the tenant | Plant an injected instruction in a lab log line and test whether your assistant obeys it |
| 9.5 What humans keep | Business-impact calls, containment approval, novel investigations, regulator reporting, feedback to detections (continues in [SEC404](../../year_4/SEC404_ai_in_security_operations/README.md)) | Write the SOC's AI usage policy in one page |

**Check your understanding:** Why does queue prioritisation alone improve analyst output even if verdicts do not change? How would you notice that an AI assistant has started rubber-stamping benign verdicts? Why is a log field written by an attacker a prompt-injection channel?

### Chapter 10 · Shifts, escalation, legal clocks and human factors (week 13)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Handover | Shift logs, open cases, watch items, "what I would do next" | Write a handover for a shift with two live incidents |
| 10.2 Escalation and communication | When to page incident response; writing for engineers vs executives; one-line situation summaries | Escalate a scenario in writing in under 10 minutes |
| 10.3 Reporting duties | CERT-In 6-hour reporting (Directions, April 2022), RBI DAKSH 6-hour reporting for banks (2026), DPDP Rules 2025 breach notices (72-hour detailed report to the Board); GDPR 72 hours | Draft the facts needed for each report from one incident |
| 10.4 Sustaining people | Burnout, night shifts, rotation into engineering work, learning when AI handles Tier 1 | Design a 12-month growth plan for a Tier 1 analyst |

**Check your understanding:** What is the minimum a handover must contain? Who starts the regulatory clock, and when? How should a SOC train juniors if AI now closes most simple alerts?

### Chapter 11 · SOC simulation (week 14)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Running a shift | Queue management, prioritisation, parallel cases | 4-hour simulated shift on BOTS or a CyberDefenders SIEM lab |
| 11.2 Incident hand-off | Packaging evidence for incident response | Hand one case to a "Tier 3" peer with a complete package |
| 11.3 Retrospective | What the shift taught about tooling and rules | Write five improvement tickets |
| 11.4 Peer review of the shift | Reviewing another analyst's closures and escalations against evidence; calibrating severity across the team | Review a classmate's simulation cases and record agreements and disagreements |

**Check your understanding:** What did you deprioritise during the simulation, and was it right? Which of your queries would you save as a detection? What would you automate first?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1–2 | Lab 1 · SIEM build | Log-source inventory |
| 2 | 2 | Lab 2 · Onboarding and silent-source alert | Normalisation map |
| 3 | 3 | Lab 3 · Correlation and risk rules | Rule pair |
| 4 | 4 | Lab 4 · KQL and SPL | 20 answered questions; **P1 due** |
| 5 | 4–5 | Lab 5 · Triage method | 30 triaged alerts |
| 6 | 5 | Lab 5 (cont.) | Tuning requests |
| 7 | 6 | Lab 6 · Phishing and sign-in cases | Two investigation reports; mid-term (AI off) |
| 8 | 6 | Lab 7 · Endpoint and cloud cases | Two investigation reports |
| 9 | 7 | Lab 8 · Playbook and SOAR | Playbook and automation; **P2 due** |
| 10 | 8 | Lab 9 · Metrics | Monthly SOC report |
| 11 | 9 | Lab 10 · AI assistant audit | Audit of AI-closed alerts |
| 12 | 9 | Lab 10 (cont.) · Prompt-injection test | Test results and policy |
| 13 | 10 | Escalation and reporting drill | Regulator fact sheet |
| 14 | 11 | SOC simulation | **P3 due** |
| 15 | Review | Timed practical triage exam, oral defence of P3 | Final exam |

## Working with AI in this course

- **Use AI for:** translating a question into KQL, SPL or ES|QL; explaining an unfamiliar log field or event ID; drafting playbooks; summarising a case for handover; first-pass enrichment. Microsoft Security Copilot, Google SecOps Gemini features, Elastic AI Assistant, Claude, ChatGPT and Gemini all do this; Claude Code or GitHub Copilot can help write SOAR integrations.
- **Do without AI (drills):** the triage of every alert in Labs 5–7 the first time; weekly 45-minute "blind" investigations; writing escalations and handovers; the mid-term and final. A Tier 1 analyst who cannot triage without AI cannot check AI triage.
- **Verify AI output by:** re-running every AI-written query and comparing counts with a query you wrote; demanding event IDs or record links for each claim; checking field names against the schema; sampling AI closures daily against a human verdict; logging disagreements by type.
- **Where AI still fails here (show it, do not assume it):** ExCyTIn-Bench reports a best score of 0.606 on multi-step investigations; CyberSOCEval (Meta and CrowdStrike, 2025) found models far from saturating malware-analysis and threat-intelligence reasoning tasks. In your own labs, record cases where the assistant invented a field, missed a low-volume event, followed an instruction hidden in data, or gave a confident verdict without evidence.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs 1–10 | 25% |
| Projects P1 / P2 / P3 | 5% / 15% / 20% |
| Mid-term (AI off) | 10% |
| Final timed triage practical (AI off) + oral defence of P3 | 25% |

**Mastery gate.** You pass when you can, with AI tools off: (1) triage 20 unseen alerts in 90 minutes with at least 90% correct verdicts and written evidence for each; (2) fully investigate one compromised-account incident across identity, endpoint and cloud logs and produce a timeline, scope and containment recommendation in two hours; (3) given an AI assistant's closure of 10 alerts, find every wrong verdict and explain why it was wrong.

## Industry reality

SOC analyst is the most common entry role in defensive security (see the [SEC market page](../../../../06_career_and_market_readiness/01_market_map/roles/SEC_cybersecurity_defense.md)). The ISC2 2025 workforce study found 28% of organisations had integrated AI security tools, 19% were testing them and 22% were evaluating them. Real platforms in this course: Microsoft Sentinel and Defender XDR, Splunk Enterprise Security, Google Security Operations, Elastic Security and Wazuh. Real Indian context: CERT-In's 6-hour rule and RBI's 2026 DAKSH reporting mean Indian bank and fintech SOCs run against regulatory clocks.

**Interview questions from this course**

1. *A user reports a phishing email. Walk me through your response.* Strong answer: preserve the original, analyse headers and URLs/attachments safely, find all recipients and clickers, check sign-ins and mailbox rules for clickers, block and purge, reset or revoke sessions if credentials were entered, document and feed detections.
2. *You get an impossible-travel alert for the CFO. What do you check?* Strong answer: VPN or proxy egress, known travel, device and browser details, MFA method and result, token reuse vs fresh sign-in, actions after sign-in (mail rules, downloads, OAuth consents); contacts the user out of band; revokes sessions if in doubt.
3. *Write a query to find accounts with more than 20 failed logins followed by a success within 10 minutes.* Strong answer: correct grouping by account and time window, ordering, handles service accounts and lockouts, explains false positives, and states which log source and fields.
4. *How do you measure whether a SOC is getting better?* Strong answer: medians and percentiles of detect/contain times, true-positive rates per rule, coverage tested by emulation, escalation quality, analyst workload; explains how each can be gamed and pairs metrics.
5. *An AI agent now auto-closes 70% of alerts. How do you know it is safe?* Strong answer: labelled evaluation set, daily sampling of closures, disagreement tracking, evidence citations, red-team tests with injected content, rollback plan, clear rules on which alert types it may close.

## Resources (free first)

- **SOC practice:** [MITRE, *11 Strategies of a World-Class Cybersecurity Operations Center*](https://www.mitre.org/news-insights/publication/11-strategies-world-class-cybersecurity-operations-center) · [SOC-CMM](https://www.soc-cmm.com/) · [CISA federal incident and vulnerability response playbooks](https://www.cisa.gov/resources-tools/resources/federal-government-cybersecurity-incident-and-vulnerability-response-playbooks) · [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final)
- **Platforms and docs:** [Wazuh documentation](https://documentation.wazuh.com/current/index.html) · [Elastic Security](https://www.elastic.co/docs/solutions/security) · [Kusto Query Language](https://learn.microsoft.com/en-us/kusto/query/) · [Splunk SPL search reference](https://help.splunk.com/en/splunk-enterprise/search/spl-search-reference/10.6/introduction/welcome-to-the-search-reference) · [OCSF schema](https://schema.ocsf.io/) · [Elastic Common Schema](https://www.elastic.co/docs/reference/ecs) · [Shuffle SOAR](https://shuffler.io/) · [TheHive](https://strangebee.com/thehive/)
- **Datasets and labs:** [Splunk BOTS v3 dataset](https://github.com/splunk/botsv3) · [OTRF Security-Datasets](https://github.com/OTRF/Security-Datasets) · [CyberDefenders](https://cyberdefenders.org/) · [Blue Team Labs Online](https://blueteamlabs.online/) · [LetsDefend](https://letsdefend.io/) (SOC simulator; part of Hack The Box since September 2025) · [TryHackMe SOC Level 1 path](https://tryhackme.com/path/outline/soclevel1) (subscription)
- **Research:** [Alahmadi, Axon and Martinovic, "99% False Positives", USENIX Security 2022](https://www.usenix.org/conference/usenixsecurity22/presentation/alahmadi) · [ExCyTIn-Bench, arXiv 2507.14201](https://arxiv.org/abs/2507.14201) · [Phishing Triage Agent RCT, arXiv 2511.13860](https://arxiv.org/abs/2511.13860) · [CyberSOCEval, arXiv 2509.20166](https://arxiv.org/abs/2509.20166)

## Sources

All checked 12 Oct 2026.

- Microsoft Security blog, "Agents built into your workflow: Get Security Copilot with Microsoft 365 E5" (18 Nov 2025) — https://www.microsoft.com/en-us/security/blog/2025/11/18/agents-built-into-your-workflow-get-security-copilot-with-microsoft-365-e5/
- Google Cloud documentation, Triage and Investigation agent — https://docs.cloud.google.com/chronicle/docs/secops/triage-investigation-agent
- Elastic blog, production-ready AI capabilities (Attack Discovery GA) — https://www.elastic.co/blog/production-ready-ai-capabilities
- Randomized Controlled Trials for Phishing Triage Agent, arXiv 2511.13860 (Nov 2025) — https://arxiv.org/abs/2511.13860
- ExCyTIn-Bench: Evaluating LLM agents on Cyber Threat Investigation, arXiv 2507.14201 (2025) — https://arxiv.org/abs/2507.14201
- CyberSOCEval, arXiv 2509.20166 (Sep 2025) — https://arxiv.org/abs/2509.20166
- Google Cloud / Mandiant, *M-Trends 2026*: 22-second hand-off, 52% internal detection, 14-day median dwell time — https://cloud.google.com/blog/topics/threat-intelligence/m-trends-2026
- Google Threat Intelligence Group, *AI Threat Tracker* (Nov 2025): FRUITSHELL hard-coded prompts aimed at LLM-based analysis — https://cloud.google.com/blog/topics/threat-intelligence/threat-actor-usage-of-ai-tools
- Microsoft Learn, Microsoft Sentinel in the Defender portal (Azure portal retirement 31 Mar 2027) — https://learn.microsoft.com/en-us/azure/sentinel/microsoft-sentinel-defender-portal
- Microsoft Sentinel data lake general availability (30 Sep 2025), as reported by SecurityBrief — https://securitybrief.news/story/microsoft-launches-sentinel-data-lake-to-cut-storage-costs
- ISC2, 2025 Cybersecurity Workforce Study (4 Dec 2025) — https://www.isc2.org/Insights/2025/12/2025-ISC2-Cybersecurity-Workforce-Study
- CERT-In Directions (28 Apr 2022) — https://www.cert-in.org.in/PDF/CERT-In_Directions_70B_28.04.2022.pdf
- DSCI brief on the RBI Commercial Banks cybersecurity directions (31 Jul 2026), DAKSH 6-hour reporting — https://www.dsci.in/files/content/knowledge-centre/2026/dsci-brief-on-rbi-cybersecurity-commercial-banks-directions-2026.pdf
- DPDP Rules 2025, Rule 7 text — https://dpdpa.com/dpdparules/rule7.html ; PIB notification (14 Nov 2025) — https://www.pib.gov.in/PressReleasePage.aspx?PRID=2190014
- Hack The Box acquires LetsDefend (16 Sep 2025) — https://www.hackthebox.com/blog/hack-the-box-acquires-letsdefend
- Mandiant, UNC5537 targets Snowflake customer instances (Jun 2024) — https://cloud.google.com/blog/topics/threat-intelligence/unc5537-snowflake-data-theft-extortion

_Last reviewed: 2026-10_
