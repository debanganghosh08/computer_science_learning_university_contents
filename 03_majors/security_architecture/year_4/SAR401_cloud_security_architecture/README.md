# SAR401 · Cloud Security Architecture

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 7 | 4 (≈ 120 hours) | L3 → L4 | [SAR301](../../year_3/SAR301_security_architecture_principles_and_frameworks/README.md) (also recommended: [SAR303](../../year_3/SAR303_zero_trust_architecture/README.md), [SAR304](../../year_3/SAR304_applied_cryptography_and_pki_for_architects/README.md)) | [SAR501](../../year_5/SAR501_frontier_seminar_post_quantum_migration/README.md), [OV01 Cloud Security](../../../../04_overlaps/OV01_cloud_security/README.md) |

Part of the [Security Architecture major](../../README.md), and the core of the [OV01 Cloud Security](../../../../04_overlaps/OV01_cloud_security/README.md) overlap with [CLD301](../../../cloud_engineering/year_3/CLD301_cloud_architecture_on_aws_azure_and_google_cloud/README.md) and [SEC303](../../../cybersecurity_defense/year_3/SEC303_identity_and_access_management/README.md). CLD301 teaches how to build a landing zone; this course teaches how to make a cloud estate of hundreds of accounts hard to breach, hard to exfiltrate from and quick to recover, across AWS, Microsoft Azure and Google Cloud. Concepts come first; each is mapped to all three providers.

## Why this course matters now

Cloud security was the most-cited security skills need after AI in ISC2's 2025 study (36%), and 43% in its 2026 India study ([ISC2](https://www.isc2.org/Insights/2025/12/2025-ISC2-Cybersecurity-Workforce-Study); [ISC2 India](https://www.isc2.org/insights/2026/09/research-india-cybersecurity-workforce-reaches-a-turning-point-skills-ai)). The big cloud breaches are architecture failures, not exotic attacks. In 2019 a server-side request forgery let an attacker use a Capital One server's role credentials to read storage, and the US OCC fined the bank $80 million. In 2024 attackers used stolen credentials to log in to Snowflake customer instances that lacked MFA and network allow-lists ([Mandiant](https://cloud.google.com/blog/topics/threat-intelligence/unc5537-snowflake-data-theft-extortion)). The CSRB found that, in the 2023 Exchange Online intrusion, the logging that revealed the attack was available only at a premium licence tier ([CSRB](https://www.cisa.gov/sites/default/files/2025-03/CSRBReviewOfTheSummer2023MEOIntrusion508.pdf)). AI is now inside cloud operations: agents investigate incidents and propose changes, and AWS Security Agent offers on-demand penetration testing of your own applications. An architect has to decide what such agents may change, design guardrails that hold when someone has valid credentials, and prove that data cannot leave the organisation by an unintended path.

## Learning outcomes

By the end you can:

1. **Design** an organisation structure with preventive, detective and proactive guardrails (AWS SCPs and RCPs, Azure Policy, Google Cloud organisation policies) and **test** them with a policy test matrix.
2. **Design** IAM at scale: federated human access, permission sets, attribute-based access, permission boundaries, workload identity, and cross-account trust without confused deputies.
3. **Build** data perimeters (trusted identities, trusted resources, expected networks) and **show** which exfiltration paths remain.
4. **Architect** network security: centralised inspection, egress control, private service access, edge protection and metadata-service hardening.
5. **Design** data protection with key policies, customer-managed and external keys, data discovery and residency controls for Indian regulation.
6. **Build** a logging and detection architecture with organisation-wide audit trails, immutable archives, retention that meets CERT-In's 180 days, and forensic readiness.
7. **Evaluate** CSPM, CNAPP and CIEM tooling vendor-neutrally, and **run** open-source posture tools against your own estate.
8. **Govern** AI agents and AI-drafted policies in cloud operations, and **verify** policies with automated reasoning tools.

## Chapters and lessons

### Chapter 1 · The cloud threat landscape (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 What is different | Control-plane APIs, identity as the perimeter, misconfiguration, credential theft, the shared responsibility line moving per service | Classify 15 cloud incidents as identity, configuration, software or supply chain |
| 1.2 Case studies | Capital One (2019): SSRF to instance-role credentials; Snowflake customers (2024): stolen credentials without MFA; Exchange Online (2023): key scope and logging tiers | For each, name the guardrail that would have broken the chain |
| 1.3 Technique catalogues | MITRE ATT&CK cloud matrices; provider threat technique catalogues (the AWS Threat Technique Catalog is updated quarterly) | Map ten techniques to the preventive and detective control you would want |
| 1.4 Legal practice | Deliberately vulnerable cloud labs in your own account (CloudGoat) and public CTFs (flaws.cloud); never test others' tenants | Complete two flaws.cloud levels and write the defensive lesson for each |

**Check your understanding:** (1) Why do valid credentials defeat most network controls? (2) Which part of the Capital One chain was an architecture decision? (3) Why must logging decisions be made before an incident?

### Chapter 2 · Organisation structure and guardrails (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Accounts as blast-radius boundaries | Security, log archive, network, shared services, workload, sandbox and suspended branches; equivalents in Azure management groups and Google Cloud folders | Design an organisation tree for an illustrative insurer with 80 workloads |
| 2.2 Preventive guardrails | AWS service control policies and resource control policies; Azure Policy deny effects; Google Cloud organisation policy constraints | Write six guardrails (region restriction, log protection, root denial, public access block, key deletion protection, approved services) |
| 2.3 Detective and proactive guardrails | Config rules, Azure Policy audit, Security Command Center findings; pre-deployment hooks | Pair each preventive guardrail with a detective one |
| 2.4 Testing guardrails | A policy test matrix run automatically; how guardrails fail silently | Build a 20-case matrix and run it in CI |
| 2.5 Break-glass | Emergency access that bypasses guardrails safely: storage of credentials, alerting, review | Design and test break-glass for the organisation |

**Check your understanding:** (1) Why can't a guardrail in a member account be trusted? (2) What is the difference between an SCP and an RCP in what they constrain? (3) Why test guardrails continuously rather than once?

### Chapter 3 · IAM design at scale (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Human access | Federation from the corporate IdP, permission sets, just-in-time elevation (Azure PIM, AWS and Google equivalents), no IAM users | Design permission sets for five roles across 80 accounts |
| 3.2 Policy evaluation in depth | Identity, resource, boundary, session and organisation policies; explicit deny; Azure RBAC with deny assignments; Google IAM deny policies | Predict 15 allow/deny outcomes, then test |
| 3.3 Attribute-based access | Tags and attributes as policy conditions; tag governance so users cannot re-tag themselves into access | Implement ABAC for project-based access and try to bypass it |
| 3.4 Workload identity | Instance roles, EKS Pod Identity, GKE Workload Identity, Azure workload identity; federation from CI and other clouds | Remove all access keys from a three-service deployment |
| 3.5 Cross-account and third-party trust | Confused deputy and external IDs; vendor access patterns; reviewing who can assume what | Find three risky trust policies in a provided estate |

**Check your understanding:** (1) Why do permission boundaries exist when policies already limit access? (2) What stops a user from changing their own tags to gain ABAC access? (3) What does an external ID protect against?

### Chapter 4 · Data perimeters (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 The three perimeters | Only trusted identities, only trusted resources, only from expected networks; AWS data perimeter guidance | Write the policy set for one perimeter in AWS |
| 4.2 Provider mechanisms | Organisation-ID condition keys and VPC endpoint policies (AWS); VPC Service Controls (Google Cloud); Private Link and policy (Azure) | Build a service perimeter around a storage bucket and a database |
| 4.3 Exfiltration paths | Writing to an attacker-owned bucket, cross-tenant sharing, public snapshots, managed AI services, presigned URLs | Enumerate ten paths and which perimeter closes each |
| 4.4 Exceptions | Partners, public datasets, third-party SaaS; documenting and monitoring holes | Design a reviewed exception for a partner data feed |

**Check your understanding:** (1) Which perimeter stops a stolen credential used from the internet? (2) Why does a resource perimeter matter when identities are trusted? (3) Which exfiltration path is hardest to close?

### Chapter 5 · Network security architecture (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Topologies | Hub and spoke, transit gateways, Virtual WAN, shared VPC; where inspection sits | Draw a topology for 80 accounts with central inspection |
| 5.2 Egress control | FQDN-based egress filtering, NAT, DNS firewalls, blocking direct internet from workloads | Allow egress to two payment endpoints and nothing else |
| 5.3 Private service access | Gateway and interface endpoints, Private Service Connect, Private Link; DNS for private endpoints | Remove public paths from a workload's dependencies |
| 5.4 Edge protection | WAF, DDoS protection (AWS Shield, Google Cloud Armor, Azure DDoS Protection), bot management, API gateways | Design edge protection for a ticket-sale spike |
| 5.5 Metadata services | Instance metadata hardening (IMDSv2 hop limits, Google and Azure equivalents) as SSRF defence | Enforce IMDSv2 organisation-wide and prove old calls fail |

**Check your understanding:** (1) Why is egress filtering more valuable than ingress filtering for data theft? (2) What breaks when you remove public endpoints? (3) How would IMDSv2 have changed the Capital One chain?

### Chapter 6 · Data protection and residency (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Key policy design | KMS key policies, grants, cross-account use, separation between key administrators and key users | Write key policies for three data classes |
| 6.2 Key custody options | Provider-managed, customer-managed, imported and external keys (AWS XKS, Azure and Google external key managers); availability coupling | Choose custody for a regulated workload and document the outage risk |
| 6.3 Data discovery | Amazon Macie, Microsoft Purview, Google Sensitive Data Protection; false positives on Indian identifiers | Scan a test bucket with synthetic Aadhaar-like and PAN-like data and tune detection |
| 6.4 Residency in India | DPDP Act cross-border transfer rules, RBI payment-data localisation (2018), SEBI's 2023 cloud framework, MeitY empanelment for government workloads | Build a residency control set for a payments workload in Mumbai and Hyderabad regions |

**Check your understanding:** (1) Why separate key administrators from key users? (2) What does an external key store buy you, and what does it cost? (3) Which residency rules constrain backups and logs, not only primary data?

### Chapter 7 · Logging, detection and forensic readiness (weeks 7–8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Audit logs | Organisation trails, Azure activity and Entra logs, Google Cloud audit logs including data-access logs; what is off by default | Enable organisation-wide audit logging and list the data-plane logs you still lack |
| 7.2 The log archive | Separate account, write-once storage (S3 Object Lock or equivalents), retention to meet CERT-In's 180 days, cost tiers | Prove the workload admin cannot delete or alter archived logs |
| 7.3 Security data lakes | Normalising with OCSF (Amazon Security Lake), SIEM ingestion choices, cost control | Route three log types into a normalised store |
| 7.4 Native detection | GuardDuty, Microsoft Defender for Cloud, Security Command Center; tuning and routing findings to owners | Generate benign test findings and route them |
| 7.5 Forensic readiness | Forensic accounts, snapshot and memory capture workflows, credential revocation at scale, the 6-hour CERT-In reporting clock | Write and dry-run a "compromised role" containment runbook |

**Check your understanding:** (1) Why does the log archive need its own account and keys? (2) What did the Exchange Online case teach about default logging? (3) What must be prepared before an incident to capture evidence in the cloud?

### Chapter 8 · Posture management: CSPM, CNAPP and CIEM (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Benchmarks | CIS Benchmarks, provider benchmarks (Microsoft cloud security benchmark), CSA Cloud Controls Matrix | Run Prowler against your organisation and triage the top 20 findings |
| 8.2 Attack paths | Combining exposure, identity and vulnerability into paths; prioritising by reachability | Draw three attack paths from your findings and cut each with one change |
| 8.3 Entitlements | Unused permissions and access analysis (IAM Access Analyzer, Azure and Google recommenders) | Reduce one role to used permissions and prove nothing broke |
| 8.4 Automated remediation | Cloud Custodian and provider automation; when automatic fixes cause outages | Automate one safe remediation and one notify-only rule |
| 8.5 Buying tools | A vendor-neutral rubric: coverage, accuracy, attack-path quality, integration, cost | Score two products or open-source stacks with the rubric |

**Check your understanding:** (1) Why do raw finding counts mislead? (2) Which remediations should never be automatic? (3) What makes an attack-path claim trustworthy?

### Chapter 9 · Containers and Kubernetes (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Managed Kubernetes responsibility | Control plane vs node vs workload responsibilities on EKS, AKS and GKE | Fill a responsibility matrix for the three |
| 9.2 Cluster identity and access | Cloud IAM to Kubernetes RBAC mapping, pod identity, least-privilege service accounts | Remove cluster-admin from all humans and pipelines in a lab cluster |
| 9.3 Workload hardening | Pod Security Standards, admission policies (Kyverno), image verification (from SAR305), secrets | Enforce the restricted profile and signed images |
| 9.4 Runtime detection | Falco rules, audit logs, multi-tenancy limits | Write three Falco rules and trigger them with benign actions |

**Check your understanding:** (1) Why is the node a trust boundary? (2) What does namespace-based multi-tenancy not isolate? (3) Where should image verification happen?

### Chapter 10 · Serverless, PaaS and cloud AI services (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Functions and events | Per-function roles, event injection, event source permissions, concurrency as a denial-of-wallet control | Threat-model an event-driven order flow and fix three permissions |
| 10.2 Managed AI services | Amazon Bedrock, Google Vertex AI, Azure AI Foundry: private networking, model access policies, content filters, prompt and response logging with privacy limits | Put a managed model behind private endpoints with logging and access policy |
| 10.3 Cost and quota abuse | Stolen keys used for model inference; budgets, quotas and alerts as security controls | Set quotas and an alert that fires on abnormal token spend |
| 10.4 PaaS defaults | Public-by-default settings, admin consoles, managed database exposure (the Snowflake lesson) | Audit five PaaS services for public exposure and MFA enforcement |

**Check your understanding:** (1) Why is spend a security signal for AI services? (2) What is the blast radius of one over-privileged function? (3) Which PaaS settings should be guardrails rather than guidance?

### Chapter 11 · Reference architectures, multi-cloud and regulated estates (weeks 12–13)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Provider references | AWS Security Reference Architecture, Microsoft cloud security benchmark and Azure landing zones, Google Cloud enterprise foundations blueprint, Well-Architected security pillars | Compare how the three place logging, security tooling and network inspection |
| 11.2 Multi-cloud identity and policy | One IdP, per-cloud roles, consistent guardrails, policy as code across clouds | Express one guardrail in all three clouds and test each |
| 11.3 Regulated estates in India | Mapping guardrails to RBI, SEBI, CERT-In and DPDP duties; evidence collection | Build a control-to-regulation map with evidence sources |
| 11.4 Sovereignty | Residency vs sovereignty vs operational control (see [CLD501](../../../cloud_engineering/year_5/CLD501_frontier_seminar_sovereign_cloud_confidential/README.md)) | Write the sovereignty section of an architecture for a government client |

**Check your understanding:** (1) Why do reference architectures place security tooling in separate accounts? (2) What gets harder in multi-cloud besides tooling? (3) What evidence will a regulator ask for first?

### Chapter 12 · AI in cloud security operations (week 14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Agents with change rights | Read-only investigation vs proposed changes via pull request vs direct apply; scoping agent roles; approval and logging | Design the permission model for an operations agent in your organisation |
| 12.2 AI-drafted policies | Common errors: wildcards, missing conditions, wrong condition keys, missing explicit denies | Have an assistant draft five policies; validate and fix them |
| 12.3 Automated reasoning as a check | IAM Access Analyzer policy checks and external-access findings, policy simulators, unit tests for policies | Gate policy changes in CI on automated checks |
| 12.4 AI-assisted testing of your own apps | Provider AI penetration testing services for your own applications, within the provider's testing policy | Read a provider's testing policy and write the authorisation checklist you would require |

**Check your understanding:** (1) Why should an agent propose rather than apply in production? (2) Which policy errors do automated checks catch, and which do they not? (3) What authorisation do you need before any testing, even of your own cloud apps?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Case chains and flaws.cloud | Guardrail per case |
| 2 | 2 | Lab 2 · Guardrails and test matrix | Matrix in CI |
| 3 | 3 | Lab 3 · IAM evaluation and ABAC (no AI) | Predictions vs results; **P1 due** |
| 4 | 4 | Lab 4 · Data perimeter | Perimeter policies and blocked paths |
| 5 | 5 | Lab 5 · Egress control and IMDSv2 | Egress rules, failing legacy calls |
| 6 | 6 | Lab 6 · Key policies and discovery | Key policies, tuned scan |
| 7 | 7 | Lab 7 · Immutable log archive | Denied deletion evidence; mid-term (AI off) |
| 8 | 7 | Containment runbook dry run | Runbook |
| 9 | 8 | Lab 8 · Prowler and attack paths | Triage and fixes; **P2 due** |
| 10 | 9 | Lab 9 · Kubernetes hardening | Policies and Falco rules |
| 11 | 10 | Managed AI service lockdown | Private endpoint and quotas |
| 12 | 11 | Multi-cloud guardrail | Three implementations |
| 13 | 11 | Regulation map | Control-to-regulation map |
| 14 | 12 | Lab 10 · AI policy audit and CI gate | **P3 due** |
| 15 | Review | Design exam and oral | Final exam |

## Working with AI in this course

- **Use AI for:** translating a guardrail between providers; drafting policies and their tests; explaining unfamiliar findings; summarising provider documentation; generating Prowler or Custodian rules.
- **Do without AI (drills):** IAM evaluation predictions (Lab 3); the organisation tree design; the data-perimeter exfiltration enumeration; the mid-term and final.
- **Verify AI output by:** running IAM Access Analyzer validation and policy simulators; testing every policy against a matrix that includes deny cases; checking condition keys and service names in current provider documentation; diffing effective permissions before and after.
- **Where AI still fails here (show it):** ask for a policy "allowing read access to one bucket from our organisation only" and check whether it uses the right organisation condition key and whether it also allows listing all buckets; ask for an Azure Policy or Google organisation constraint by name and check it exists. Record each defect in Lab 10.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs 1–10 | 25% |
| Projects P1 / P2 / P3 | 5% / 15% / 25% |
| Mid-term (AI off) | 10% |
| Final: design exam plus oral defence of P3 | 20% |

**Mastery gate.** You pass when you can, without AI and in three hours: (a) design guardrails, IAM and data perimeters for an unseen multi-account organisation and show which of ten listed exfiltration paths each control closes; (b) predict the outcome of ten IAM evaluation cases with at least nine correct; and (c) design a logging architecture that meets CERT-In's retention and immutability needs within a stated budget.

## Industry reality

- Providers publish the reference designs reviewers use: the AWS Security Reference Architecture, Microsoft's cloud security benchmark and Google Cloud's enterprise foundations blueprint.
- Organisation-level controls keep expanding (AWS resource control policies since 2024), so guardrail design is a core architect skill.
- Indian regulators (RBI, SEBI, CERT-In, MeitY) set residency, logging and audit expectations that cloud architectures must evidence.
- Cloud security architect interviews include a design round ("secure this multi-account estate") and a scenario round ("stolen credentials were used from the internet").

**Interview questions from this course**

1. *"Design guardrails for a 200-account organisation."* Strong answer: account structure as blast radius, preventive guardrails for the few things that must never happen, detective pairs, tested matrix, exceptions with expiry, break-glass, ownership.
2. *"An insider with valid credentials copies data to their personal bucket. How do you prevent that?"* Strong answer: resource and identity perimeters (organisation conditions on the principal and the resource), endpoint policies, egress control, detection on cross-account writes, residual paths.
3. *"How would you have prevented the 2024 Snowflake customer breaches in your own estate?"* Strong answer: MFA and SSO enforced on all SaaS and PaaS admin access, network allow-lists, credential hygiene on endpoints, detection of logins from new infrastructure, guardrails rather than guidance.
4. *"Design our cloud logging so it survives an attacker with admin rights in a workload account."* Strong answer: organisation trail to a separate account, write-once storage with its own keys, retention, data-plane logs where needed, cost tiers, access for responders.
5. *"How should an AI operations agent be allowed to change our cloud?"* Strong answer: its own role, read-only by default, changes as pull requests with automated policy checks, approval for production, blast-radius limits, full logging, a kill switch.

## Resources (free first)

- **Reference architectures:** [AWS Security Reference Architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/welcome.html); [AWS security pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html); [AWS data perimeters](https://aws.amazon.com/identity/data-perimeters-on-aws/); [Microsoft cloud security benchmark](https://learn.microsoft.com/en-us/security/benchmark/azure/introduction); [Azure Well-Architected security](https://learn.microsoft.com/en-us/azure/well-architected/security/); [Azure landing zones](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/); [Google Cloud enterprise foundations](https://cloud.google.com/architecture/security-foundations); [Google Cloud Architecture Framework](https://docs.cloud.google.com/architecture/framework).
- **Benchmarks and controls:** [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks); [CSA Cloud Controls Matrix](https://cloudsecurityalliance.org/research/cloud-controls-matrix); [MITRE ATT&CK](https://attack.mitre.org/).
- **Open-source tools:** [Prowler](https://docs.prowler.com/); [Cloud Custodian](https://cloudcustodian.io/docs/); [Steampipe](https://steampipe.io/); [Falco](https://falco.org/docs/); [Kyverno](https://kyverno.io/docs/).
- **Legal practice:** [flaws.cloud](http://flaws.cloud/) and [flaws2.cloud](http://flaws2.cloud/); [CloudGoat](https://github.com/RhinoSecurityLabs/cloudgoat) in your own account only.
- **Paid, optional:** provider security specialty courses; the free provider documentation above covers the syllabus.

## Sources

All checked 12 Oct 2026.

- ISC2, 2025 Cybersecurity Workforce Study (4 Dec 2025) — https://www.isc2.org/Insights/2025/12/2025-ISC2-Cybersecurity-Workforce-Study ; India study (24 Sep 2026) — https://www.isc2.org/insights/2026/09/research-india-cybersecurity-workforce-reaches-a-turning-point-skills-ai
- OCC, civil money penalty against Capital One (6 Aug 2020) — https://www.occ.gov/news-issuances/news-releases/2020/nr-occ-2020-101.html
- Mandiant, UNC5537 targets Snowflake customer instances (Jun 2024) — https://cloud.google.com/blog/topics/threat-intelligence/unc5537-snowflake-data-theft-extortion
- CSRB report on the 2023 Exchange Online intrusion (Mar 2024) — https://www.cisa.gov/sites/default/files/2025-03/CSRBReviewOfTheSummer2023MEOIntrusion508.pdf
- AWS Security Agent updates, including threat modeling and penetration testing (2026) — https://aws.amazon.com/blogs/aws/aws-security-agent-adds-threat-modeling-kiro-power-and-claude-code-plugin-and-more/
- AWS Threat Technique Catalog update (June 2026) — https://aws.amazon.com/blogs/security/what-the-june-2026-threat-technique-catalog-update-means-for-your-aws-environment/
- CERT-In Directions (28 Apr 2022): 180-day log retention, 6-hour reporting — https://www.cert-in.org.in/PDF/CERT-In_Directions_70B_28.04.2022.pdf

_Last reviewed: 2026-10_
