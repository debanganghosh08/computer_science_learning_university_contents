# OV01A · Cloud Security Posture, Detection and Response

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 7 | 4 (≈ 120 hours) | L3 → L4 | [CLD301](../../../03_majors/cloud_engineering/year_3/CLD301_cloud_architecture_on_aws_azure_and_google_cloud/README.md), [SEC303](../../../03_majors/cybersecurity_defense/year_3/SEC303_identity_and_access_management/README.md); corequisite [SAR401](../../../03_majors/security_architecture/year_4/SAR401_cloud_security_architecture/README.md); recommended [SEC302](../../../03_majors/cybersecurity_defense/year_3/SEC302_security_operations_soc_siem_and_monitoring/README.md) | [OV01B](../OV01B_kubernetes_and_container_security/README.md), [SEC501](../../../03_majors/cybersecurity_defense/year_5/SEC501_frontier_seminar_threat_intelligence/README.md), [CLD501](../../../03_majors/cloud_engineering/year_5/CLD501_frontier_seminar_sovereign_cloud_confidential/README.md), [THS501](../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) |

Part of the [OV01 Cloud Security overlap](../README.md). SAR401 designs the guardrails, data perimeters and logging architecture; this course operates them day to day.

## Why this course matters now

Most cloud breaches are not exotic. They start with a stolen credential, a leaked access key, an over-privileged role or a misconfigured service: Capital One (2019) lost data after an attacker reached an instance role's credentials through server-side request forgery ([OCC](https://www.occ.gov/news-issuances/news-releases/2020/nr-occ-2020-101.html)); the 2024 Snowflake customer intrusions used infostealer credentials against accounts without MFA ([Mandiant](https://cloud.google.com/blog/topics/threat-intelligence/unc5537-snowflake-data-theft-extortion)); in January 2025 AWS warned customers about attackers using compromised credentials to re-encrypt S3 objects with customer-provided keys (SSE-C) for ransom ([AWS Security Blog](https://aws.amazon.com/blogs/security/preventing-unintended-encryption-of-amazon-s3-objects/)). Cloud security was the most-cited skills need after AI in ISC2's 2025 study (36%), and 43% in India ([ISC2 2025](https://www.isc2.org/Insights/2025/12/2025-ISC2-Cybersecurity-Workforce-Study), [ISC2 India 2026](https://www.isc2.org/insights/2026/09/research-india-cybersecurity-workforce-reaches-a-turning-point-skills-ai)). AI tools now correlate findings into attack sequences (Amazon GuardDuty Extended Threat Detection), triage alerts (Microsoft Security Copilot agents, Google SecOps triage agent) and draft queries and policies. What still needs a skilled engineer is deciding which finding is actually exploitable, writing detections that survive real traffic, and running a response that contains an attacker without destroying evidence or production.

## Learning outcomes

By the end you can:

1. **Build** a continuously updated inventory of a multi-account, multi-cloud estate with owners and data classes, and **measure** its coverage.
2. **Run** CIS-benchmark posture scans across accounts, **write** custom checks, and **cut** findings to those that matter using attack-path reasoning over identity, network and data.
3. **Remediate** findings through infrastructure-as-code pull requests and safe auto-remediation, and **measure** time to remediate and recurrence.
4. **Design** a cloud logging pipeline that captures the events detections need, at a cost you can justify, with tamper evidence.
5. **Write, test and validate** detections as code on CloudTrail, Azure Activity and Entra ID, and Google Cloud audit logs, using emulation in your own sandbox to prove they fire.
6. **Investigate** a cloud intrusion by building a timeline from audit logs and computing the blast radius of a compromised identity.
7. **Lead** containment, eradication and recovery for leaked keys, hijacked roles and data theft, and **write** a regulator-ready report within legal clocks.
8. **Evaluate** AI-generated findings, detections and remediation proposals against evidence before acting on them.

## Chapters and lessons

### Chapter 1 · How cloud intrusions actually happen (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 The defender's case file | Capital One 2019 (SSRF to instance credentials), Snowflake customers 2024 (stolen credentials, no MFA), Exchange Online 2023 (signing key scope; CSRB report), Salesloft Drift 2025 (stolen OAuth tokens to SaaS) | Write a one-page "initial access → impact" chain for each, naming the control that would have broken it |
| 1.2 Technique catalogues | MITRE ATT&CK cloud matrices (IaaS, SaaS, Identity Provider, Office Suite); the AWS Threat Technique Catalog | Map the four cases to ATT&CK techniques; list the log source that would show each step |
| 1.3 A baseline to measure against | CISA and NSA's March 2024 cloud security information sheets (IAM, key management, network segmentation, data, managed services) | Score a sample estate against the sheets; record gaps |
| 1.4 The legal lab | A sandbox organisation with budgets and alerts; deliberately vulnerable labs in your own account (CloudGoat) and public CTFs (flaws.cloud); never test another tenant | Build the course sandbox with a budget alarm and an automated teardown script |

**Check your understanding:** Why do so many cloud breaches begin with identity rather than a software vulnerability? Which of the four cases would a perfect CIS benchmark score not have prevented, and why? What makes testing against someone else's cloud tenant illegal even if a resource is "public"?

### Chapter 2 · Inventory: you cannot secure what you cannot list (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Native inventory | AWS Config aggregators, Azure Resource Graph, Google Cloud Asset Inventory; organisation-wide views; update latency | Query all three for internet-facing resources |
| 2.2 SQL over cloud APIs | Steampipe and CloudQuery: tables for resources, joins across accounts and clouds | Build an `assets` table joining compute, storage and identities |
| 2.3 Owners and data classes | Tag policies, owner resolution from IaC repositories and the service catalogue, data classification tags | Report untagged and ownerless resources as findings |
| 2.4 SaaS and shadow assets | OAuth applications, SaaS tenants, CISA's ScubaGear baselines for Microsoft 365 | Inventory third-party OAuth apps with high-privilege scopes in a test tenant |

**Check your understanding:** Why is an inventory that is 95% complete dangerous to trust? How would you discover a production account nobody registered? Which SaaS integration in your estate holds tokens that bypass your MFA?

### Chapter 3 · Posture management: benchmarks and engines (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Benchmarks | CIS Foundations Benchmarks for AWS, Azure and Google Cloud; AWS Foundational Security Best Practices; Microsoft cloud security benchmark; what a configuration check can and cannot prove | Run Prowler across the sandbox; classify findings by benchmark section |
| 3.2 Custom checks | Writing checks for your own rules (Cloud Custodian policies, Prowler custom checks, Steampipe queries) | Encode three organisation-specific rules and test them |
| 3.3 Tool categories | CSPM, CIEM, DSPM, CNAPP; native services (AWS Security Hub, Microsoft Defender for Cloud, Google Security Command Center) versus third-party platforms | Compare native and open-source results on the same account; explain differences |
| 3.4 Noise control | Severity versus exploitability, deduplication across tools, suppressions with reasons and expiry dates | Cut a 400-finding report to a defensible top 20 |

**Check your understanding:** Two tools disagree on whether a bucket is public; how do you decide which is right? Why should every suppression expire? What is lost when a team optimises for a posture score?

### Chapter 4 · Attack paths and prioritisation (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Toxic combinations | Exposure + exploitable workload + over-privileged identity + sensitive data; why each alone is "medium" | Find two toxic combinations in the CloudGoat scenario you deployed |
| 4.2 Graphs of reachability | Modelling identities, trust policies, network paths and data stores as a graph (Cartography into Neo4j; principal-mapping tools for IAM) | Query "which identities can reach the customer-data bucket" |
| 4.3 Effective and unused permissions | IAM Access Analyzer external and unused-access findings; Azure and Google role recommenders | Shrink one role to used permissions; prove nothing breaks with a test suite |
| 4.4 Prioritising workloads | CISA KEV and FIRST EPSS for vulnerable hosts and images; asset criticality; writing the "why this first" note | Rank 30 findings and defend the order in five minutes |

**Check your understanding:** Why can a low-severity finding be the most urgent one? What does a trust policy add to the attack graph that a security group cannot show? When does removing unused permissions cause an outage?

### Chapter 5 · Remediation at scale (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Routing to owners | Tickets with owner, evidence and fix; SLAs by severity; correlation across tools | Build a routing rule from the inventory owner tags |
| 5.2 Fix in code | Pull requests to Terraform or OpenTofu instead of console changes; drift detection | Fix five findings by PR; show the drift job catching a console change |
| 5.3 Safe auto-remediation | Cloud Custodian actions with dry runs, rate limits, notifications and rollback; when automatic fixes cause outages | Auto-remediate public snapshots with a dry-run week first |
| 5.4 Push recurring findings left | Turning repeat findings into preventive guardrails designed in SAR401 (SCPs/RCPs, Azure Policy deny, organisation policy constraints) | Convert one recurring finding into a guardrail with a test |
| 5.5 Measuring posture | Median time to remediate by severity, recurrence rate, coverage, exception age | Build the posture dashboard used in P1 |

**Check your understanding:** Why do console fixes come back? Which findings should never be auto-remediated, and why? How would you show leadership that posture improved without quoting a vendor score?

### Chapter 6 · Cloud logging for detection (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 What each log says | CloudTrail management and data events; Azure Activity log and Entra ID sign-in and audit logs; Google Cloud Admin Activity and Data Access audit logs; VPC flow logs, DNS query logs, storage access logs | For ten attacker actions, name the log line that records each |
| 6.2 Off by default | Data events and Data Access logs are not on by default; cost of enabling them; sampling choices | Estimate monthly cost of enabling S3 data events for three buckets |
| 6.3 The pipeline | Organisation trails into a log-archive account, Amazon Security Lake and OCSF, SIEM ingestion (Microsoft Sentinel, Google SecOps, Splunk, Elastic); ingestion delay versus event time | Ship sandbox logs to an open-source SIEM; measure end-to-end delay |
| 6.4 Integrity and retention | Detecting `StopLogging` and trail deletion; write-once storage (S3 Object Lock); CERT-In's 180-day retention | Prove that a log-deletion attempt both fails and alerts |

**Check your understanding:** An attacker reads 50 GB from a bucket; which logs show it, and which do not unless you enabled them? Why does ingestion delay matter for a 6-hour reporting clock? What would you log less of if the budget halved?

### Chapter 7 · Detection engineering for cloud (weeks 7–8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Detection as code | Sigma rules for cloud logs, version control, unit tests on recorded events, deployment pipeline to the SIEM | Set up the detection repository with CI |
| 7.2 High-value detections | Root or break-glass use, access-key creation for privileged users, MFA removal, trust policy granting an external account, logging disabled, unusual regions, mass object reads, SSE-C use where not expected, risky OAuth consent | Write ten detections with tests |
| 7.3 Behavioural detections | First-seen API calls per principal, rare networks and user agents, impossible travel; what managed detections (GuardDuty, Defender for Cloud, Security Command Center) cover and miss | Build a first-seen baseline over two weeks of sandbox logs |
| 7.4 Validating with emulation | Running documented techniques in your own sandbox with Stratus Red Team to prove rules fire; coverage mapped to ATT&CK | Measure which of your rules fire on ten emulated techniques |
| 7.5 Tuning | Precision per rule, allow-lists with expiry, false-positive budgets, feedback from triage | Tune three noisy rules; report precision before and after |

**Check your understanding:** Why is a detection without a test a liability? What can an emulation run prove, and what can it not? How do you write a rule for an action that is legitimate 99% of the time?

### Chapter 8 · Identity threats in the cloud control plane (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Workload credential abuse | Instance and pod credentials used from outside their workload (GuardDuty finding types), role chaining, federated web identity | Detect a sandbox role credential used from your laptop |
| 8.2 Human identity in the cloud | Entra ID risky sign-ins, token replay, consent phishing indicators, privileged role activation (from SEC303, applied to cloud admin planes) | Hunt for admin activations without a ticket reference |
| 8.3 Long-lived keys | Finding, rotating and eliminating access keys; leaked keys in public repositories and secret-scanning partner notifications | Build a key-age report and a rotation runbook |
| 8.4 Third-party and SaaS tokens | The Salesloft Drift lesson; inventory, scope review and revocation of integration tokens | Revoke and re-issue an integration token in a test tenant with no downtime |

**Check your understanding:** Why does a role assumed from an unexpected network deserve more attention than a failed login? What evidence shows a token was replayed rather than used by its owner? Which keys in your estate cannot be rotated today, and what is the plan?

### Chapter 9 · Cloud incident response (weeks 10–11)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Preparation | NIST SP 800-61 Rev. 3 (April 2025) and the AWS Security Incident Response Guide; IR roles, a forensic account, pre-approved runbooks and break-glass access | Write runbooks for leaked key, hijacked role and public data exposure |
| 9.2 Containment that keeps evidence | Order of operations: snapshot volumes, isolate with a quarantine security group, revoke active role sessions, disable keys, quarantine policies; what not to delete | Contain a planted incident while preserving an evidence bundle |
| 9.3 Investigation and scoping | Timeline from audit logs; blast radius from the Chapter 4 graph: what the stolen principal could read, change or assume | Produce a timeline and a blast-radius statement for a recorded incident |
| 9.4 Eradication and recovery | Rotating everything reachable, rebuilding from known-good IaC, restoring from immutable backups; recovering from SSE-C style re-encryption | Rebuild a compromised workload from code in under one hour |
| 9.5 Legal clocks and reporting | CERT-In 6-hour reporting, DPDP Rules 2025 breach intimation, RBI rules for banks; writing for regulators and executives | Draft the 6-hour notification and the 72-hour report for the exercise |

**Check your understanding:** Why might deleting a malicious IAM user be the wrong first move? How do you decide that an incident is contained? What do you tell the regulator at hour 6 when you do not yet know the scope?

### Chapter 10 · Workloads, serverless and AI services in the detection picture (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Kubernetes audit logs in the SIEM | EKS, AKS and GKE control-plane logs; high-value events (exec into pods, new cluster-admin bindings); hand-off to runtime detection in OV01B | Ingest cluster audit logs and write two detections |
| 10.2 Serverless | Function invocation and configuration-change events, environment-variable secrets, event-source permission changes | Detect a function whose role gained new permissions |
| 10.3 Managed AI services | Stolen keys used for model inference ("LLMjacking", Sysdig, May 2024); invocation logging, quotas and budgets as detections | Alert on model invocations from an unexpected principal or region |
| 10.4 Container images and hosts | Linking image vulnerability findings to running workloads and exposure | Join scan results to the inventory to list exposed vulnerable workloads |

**Check your understanding:** Why are budgets and quotas security controls for AI services? Which Kubernetes events should page someone at night? How does exposure change the priority of the same CVE?

### Chapter 11 · AI in cloud security operations (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 What the tools do | GuardDuty Extended Threat Detection attack sequences, Microsoft Security Copilot agents, Google SecOps triage agent, AI features in CNAPP products; what each sees | Compare an AI incident summary with your own timeline; list disagreements |
| 11.2 Verifying AI output | Re-running AI-written queries, testing AI-drafted detections on labelled log sets and emulations, checking AI-drafted IAM policies with policy analysers | Accept or reject five AI-drafted detections with evidence |
| 11.3 Agents with change rights | Read-only investigation versus pull-request remediation versus direct apply; scoped roles, approvals, audit; prompt injection through log fields and resource tags | Design the permission model for a remediation agent |
| 11.4 The programme | Metrics (coverage, time to detect, time to contain, remediation SLA), tabletop exercises, reporting to leadership | Run a 60-minute tabletop and write the after-action report |

**Check your understanding:** What would make you trust an AI triage verdict without re-checking it, and is that ever acceptable? Why is a resource tag an injection channel for an AI analyst? Which remediation actions must always need a human?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Sandbox organisation and case mapping | ATT&CK map of four cases |
| 2 | 2 | Lab 2 · Multi-account inventory | Asset table with owners |
| 3 | 3 | Lab 3 · Posture scanning and custom checks | — |
| 4 | 4 | Lab 4 · Attack-path graph | **P1 due** |
| 5 | 5 | Lab 5 · Remediation by pull request | Posture dashboard |
| 6 | 6 | Lab 6 · Logging pipeline | Logging cost estimate |
| 7 | 7 | Lab 7 · Detection repository with CI | — |
| 8 | 7 | Lab 7 (cont.) · Emulation runs | Mid-term (AI off): log reading and policy review |
| 9 | 8 | Lab 8 · Identity hunts | — |
| 10 | 9 | Lab 9 · Incident response game day I | **P2 due** |
| 11 | 9 | Lab 9 (cont.) · Recovery from code | Regulator notification draft |
| 12 | 10 | Lab 10 · Workload and AI-service detections | — |
| 13 | 11 | Tabletop exercise | After-action report |
| 14 | 11 | Programme review | **P3 due** |
| 15 | Review | Live incident simulation and oral defence of P3 | Final exam |

## Working with AI in this course

- **Use AI for:** drafting Sigma rules and SIEM queries from a description; explaining unfamiliar API calls in a log; summarising a long CloudTrail extract; generating Cloud Custodian policy skeletons; first drafts of runbooks and incident reports. Claude, ChatGPT and Gemini handle these well; Security Copilot, Google SecOps and GuardDuty add estate-specific context.
- **Do without AI (drills):** reading raw audit-log JSON and building a timeline by hand; evaluating an IAM policy and trust policy by hand; containment decisions under time pressure; the mid-term and the final simulation are AI-off.
- **Verify AI output by:** running every AI-drafted detection against recorded true-positive and benign samples before merge; checking AI-drafted IAM or guardrail policies with IAM Access Analyzer policy validation or a policy simulator; demanding event IDs or query results for every claim in an AI summary and re-running the query yourself.
- **Where AI still fails here:** in this course you collect your own evidence. Log every AI-drafted detection that passed review but failed on the emulation run, and every AI summary that mis-stated scope or time. Known risks you will test: wrong condition keys in drafted policies, rules that match field names your SIEM does not use, and AI analysts following instructions planted in log fields (Google's threat intelligence group reported malware with prompts aimed at AI-based analysis, [Nov 2025](https://cloud.google.com/blog/topics/threat-intelligence/threat-actor-usage-of-ai-tools)).

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10, with tests and short write-ups) | 25% |
| Projects P1–P3 | 35% |
| Mid-term (AI off) | 10% |
| Final: live incident simulation (AI off) + oral defence of P3 | 30% |

**Mastery gate.** You pass when you can, with AI tools off: (1) given raw audit logs from a simulated intrusion, produce a correct timeline and blast-radius statement within 90 minutes; (2) write a detection for a described attacker action, with a passing test, in 20 minutes; (3) given an estate with 200 findings, name the five that matter most and defend the order against questioning.

## Industry reality

Cloud detection and response is now a distinct team in large organisations, often separate from the SOC that handles endpoints. Public material shows the shape of the work: Mandiant's Snowflake report lists the indicators and hardening steps customers had to apply; the CSRB report on Exchange Online shows how key management and logging decisions became board-level findings; AWS's SSE-C advisory shows a provider publishing detections and mitigations for an attack pattern seen across customers. M-Trends 2026 reports 52% of intrusions detected internally ([Mandiant](https://cloud.google.com/blog/topics/threat-intelligence/m-trends-2026)), which means nearly half are still found by someone else. Detection depth and cloud logging are where that number moves.

**Interview questions from this course**

1. *An access key belonging to a CI role appears in a public GitHub repository. Walk me through the first hour.* Strong answer: confirm and scope via CloudTrail (calls by that key, from where); deactivate the key, then check for persistence (new users, keys, roles, trust-policy changes, Lambda functions); revoke sessions of roles it assumed; snapshot affected resources; root cause in the pipeline; rotate secrets reachable from that role; start the reporting clock.
2. *Your CSPM shows 3,000 findings. What do you do this week?* Strong answer: deduplicate, join to inventory and exposure, find toxic combinations and paths to sensitive data, fix the top ones by PR, turn recurring classes into guardrails, set SLAs and exceptions with expiry; refuses to chase the score.
3. *Write a detection for a trust policy that newly allows an external account to assume a role.* Strong answer: names the API events (`UpdateAssumeRolePolicy`, `CreateRole`), parses the policy for principals outside the organisation ID, allow-lists known vendors with expiry, includes a test, and mentions IAM Access Analyzer external-access findings as a second signal.
4. *How do you know your detections work?* Strong answer: unit tests on recorded events, emulation in a sandbox, ATT&CK coverage map, precision per rule from triage feedback, and silent-failure monitoring for missing log sources.
5. *Should an AI agent be allowed to remediate findings automatically?* Strong answer: depends on reversibility and blast radius; read-only by default, PR-based changes for most, direct action only for narrow, reversible classes with rate limits and audit; addresses injection through tags and logs and how to measure the agent's precision.

## Resources (free first)

- **Frameworks and guidance:** MITRE ATT&CK cloud matrix — https://attack.mitre.org/matrices/enterprise/cloud/ ; CISA and NSA cloud security information sheets (Mar 2024) — https://www.cisa.gov/news-events/alerts/2024/03/07/cisa-and-nsa-release-cybersecurity-information-sheets-cloud-security-best-practices ; CIS Benchmarks (free PDFs with registration) — https://www.cisecurity.org/cis-benchmarks ; NIST SP 800-61 Rev. 3 — https://csrc.nist.gov/pubs/sp/800/61/r3/final ; AWS Security Incident Response Guide — https://docs.aws.amazon.com/whitepapers/latest/aws-security-incident-response-guide/aws-security-incident-response-guide.html
- **Provider documentation:** Amazon GuardDuty — https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html ; Amazon Security Lake — https://docs.aws.amazon.com/security-lake/latest/userguide/what-is-security-lake.html ; Microsoft Defender for Cloud — https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-cloud-introduction ; Google Security Command Center — https://cloud.google.com/security/products/security-command-center
- **Open-source tools:** Prowler — https://github.com/prowler-cloud/prowler ; Cloud Custodian — https://cloudcustodian.io/ ; Sigma — https://github.com/SigmaHQ/sigma ; OCSF schema — https://schema.ocsf.io/ ; Stratus Red Team — https://stratus-red-team.cloud/ ; ScubaGear — https://github.com/cisagov/ScubaGear
- **Practice (own accounts or public CTFs only):** CloudGoat — https://github.com/RhinoSecurityLabs/cloudgoat ; flaws.cloud — http://flaws.cloud/
- **Paid, optional:** vendor CNAPP trials and provider security specialty certifications; not required for any lab.

## Sources

All checked 12 Oct 2026.

- OCC, Capital One civil money penalty (6 Aug 2020) — https://www.occ.gov/news-issuances/news-releases/2020/nr-occ-2020-101.html
- Mandiant, UNC5537 and Snowflake customer instances (Jun 2024) — https://cloud.google.com/blog/topics/threat-intelligence/unc5537-snowflake-data-theft-extortion
- AWS Security Blog, "Preventing unintended encryption of Amazon S3 objects" (Jan 2025; SSE-C misuse) — https://aws.amazon.com/blogs/security/preventing-unintended-encryption-of-amazon-s3-objects/
- ISC2, 2025 Cybersecurity Workforce Study — https://www.isc2.org/Insights/2025/12/2025-ISC2-Cybersecurity-Workforce-Study ; India study (Sep 2026) — https://www.isc2.org/insights/2026/09/research-india-cybersecurity-workforce-reaches-a-turning-point-skills-ai
- CISA and NSA, cloud security best practices information sheets (7 Mar 2024) — https://www.cisa.gov/news-events/alerts/2024/03/07/cisa-and-nsa-release-cybersecurity-information-sheets-cloud-security-best-practices
- Google Threat Intelligence Group, data theft from Salesforce instances via Salesloft Drift (Aug 2025) — https://cloud.google.com/blog/topics/threat-intelligence/data-theft-salesforce-instances-via-salesloft-drift
- CSRB review of the Summer 2023 Exchange Online intrusion — https://www.cisa.gov/sites/default/files/2025-03/CSRBReviewOfTheSummer2023MEOIntrusion508.pdf
- NIST SP 800-61 Rev. 3 (Apr 2025) — https://csrc.nist.gov/pubs/sp/800/61/r3/final
- Sysdig, "LLMjacking: Stolen Cloud Credentials Used in New AI Attack" (6 May 2024) — https://www.sysdig.com/blog/llmjacking-stolen-cloud-credentials-used-in-new-ai-attack
- AWS, GuardDuty Extended Threat Detection — https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-extended-threat-detection.html
- Google Cloud / Mandiant, M-Trends 2026 — https://cloud.google.com/blog/topics/threat-intelligence/m-trends-2026
- Google Threat Intelligence Group, AI threat tracker (Nov 2025) — https://cloud.google.com/blog/topics/threat-intelligence/threat-actor-usage-of-ai-tools
- CERT-In Directions (28 Apr 2022) — https://www.cert-in.org.in/PDF/CERT-In_Directions_70B_28.04.2022.pdf ; DPDP Rules 2025 notification (14 Nov 2025) — https://www.pib.gov.in/PressReleasePage.aspx?PRID=2190014

_Last reviewed: 2026-10_
