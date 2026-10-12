# CLD · Cloud Engineering: roles and market (2026)

| Learning path | Interview loop | AI impact | Market overview |
|---|---|---|---|
| [Cloud Engineering major](../../../03_majors/cloud_engineering/README.md) | [AI-driven interviews](../../04_ai_driven_interviews/) | [Matrix row](../ai_impact_matrix.md) | [Market map](../README.md) |

All figures were checked in October 2026. Paragraphs marked **Analysis** are interpretation, not measurement.

## Role titles and seniority ladder

| Level | Common titles |
|---|---|
| Entry | Associate Cloud Engineer, Cloud Support Engineer, Junior DevOps/Cloud Engineer |
| Mid | Cloud Engineer, Cloud Infrastructure Engineer, Kubernetes Engineer |
| Senior | Senior Cloud Engineer, Cloud Solutions Architect, Cloud Security Engineer |
| Staff and above | Principal Cloud Architect, Head of Cloud Platform |

Specialised variants: FinOps engineer (cloud cost), cloud network engineer, migration engineer, and AI infrastructure engineer (GPU clusters, inference serving, CLD404).

## What the work looks like day to day

- Write and review infrastructure as code (Terraform, OpenTofu, Pulumi) (CLD302).
- Design networks: VPCs, subnets, routing, private endpoints, DNS, load balancers (CLD304).
- Design identity and access (IAM) with least privilege.
- Run containers on Kubernetes and managed services (CLD303).
- Migrate workloads from data centres or between clouds (CLD402).
- Track and cut cost; explain the bill to finance (CLD403).
- Plan GPU capacity and inference endpoints for AI workloads (CLD404).

## Demand signals

**No official occupation is called "cloud engineer".** The closest official data and proxy signals:

- **US projections.** Computer network architects +8% from 2025 to 2035; BLS says "continued expansion of cloud computing will increase demand for these workers", and firms adopting AI need to modernise infrastructure ([BLS](https://www.bls.gov/ooh/computer-and-information-technology/computer-network-architects.htm)). Database administrators grow slowly because "fewer of these workers are expected to be needed as many companies operate in the cloud" ([BLS](https://www.bls.gov/ooh/computer-and-information-technology/database-administrators.htm)), which shows work moving from on-premises operations to cloud skills.
- **Skills in AI postings.** In US AI-related job postings, AWS grew 1,358% against a decade earlier and scalability 733% ([AI Index 2026](https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf)).
- **Security overlap.** Cloud security was the second most-cited skills need (36%) in the 2025 ISC2 study ([ISC2 2025](https://www.isc2.org/Insights/2025/12/2025-ISC2-Cybersecurity-Workforce-Study)) and 43% in India ([ISC2 India, Sept 2026](https://www.isc2.org/insights/2026/09/research-india-cybersecurity-workforce-reaches-a-turning-point-skills-ai)).
- **Platforms.** 90% of organisations in DORA's 2025 research had adopted at least one internal platform ([DORA 2025](https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report)).
- **US postings.** Indeed's "IT Systems & Solutions" postings index was 76.4 on 2 Oct 2026 (1 Feb 2020 = 100), up from 69.9 a year earlier ([Indeed Hiring Lab data](https://github.com/hiring-lab/job_postings_tracker)).
- **India.** NASSCOM points to "India's emergence as a datacenter hub" supporting enterprise AI ([NASSCOM 2026](https://nasscom.in/knowledge-center/publications/technology-sector-india-strategic-review-2026)).

## How AI is changing the role

**Automated or mostly automated.** First drafts of Terraform modules, Kubernetes manifests and IAM policies; CLI commands; cost reports; documentation of existing infrastructure.

**Augmented.** Troubleshooting (reading events, logs and config together), migration planning, reviewing infrastructure-as-code changes, explaining unfamiliar services.

**Growing in value.**

- Architecture trade-offs: availability zones and regions, managed against self-run, cost against resilience.
- IAM and network design. A generated policy with a wildcard is a breach waiting to happen.
- Blast-radius thinking: what a single change can break.
- Cost engineering for AI workloads: GPU utilisation, inference cost per request, reserved capacity.
- Data residency and sovereignty rules (CLD501).

**Analysis.** Infrastructure code is easy to generate and expensive to get wrong, because mistakes hit security, availability and the bill at once. AI raises the value of engineers who can review infrastructure changes quickly and understand the failure and cost consequences.

## Pay (indicative)

| Market | Role in source | Figure | Type | Source |
|---|---|---|---|---|
| US | Computer network architects (closest official occupation) | Median $134,050; 10th $79,900; 90th $202,680 (May 2025) | Official survey | [BLS](https://www.bls.gov/ooh/computer-and-information-technology/computer-network-architects.htm) |
| India | Development Operations (DevOps) Engineer (common entry title) | Average base ₹10.0 lakh; base range ₹4.0–30 lakh (896 profiles, Jul 2026) | Self-reported, whole market | [Payscale](https://www.payscale.com/research/IN/Job=Development_Operations_(DevOps)_Engineer/Salary) |
| India | Cloud Solutions Architect (senior) | Average base ₹23.4 lakh (203 profiles, Jul 2026) | Self-reported, whole market | [Payscale](https://www.payscale.com/research/IN/Job=Cloud_Solutions_Architect/Salary) |
| India | Solution Architect | Median total pay ₹46.0 lakh; 25th ₹33.6 lakh; 90th ₹81.9 lakh (373 submissions) | Self-reported, mostly product companies | [Levels.fyi](https://www.levels.fyi/t/solution-architect/locations/india) |

No reliable public source gives pay for the title "cloud engineer" specifically.

## The hiring loop

Typical loop (varies by company):

1. Screen on fundamentals: Linux, networking (TCP, DNS, TLS), one cloud provider's core services.
2. Hands-on exercise: write or fix a Terraform module, or debug a broken Kubernetes deployment.
3. Architecture design: design a highly available web application, a multi-account landing zone, or a migration plan. Strong answers include IAM, networking, observability, cost and failure scenarios.
4. Troubleshooting scenario: "the service returns 502 after a deploy; walk through it".
5. Behavioural: an outage, a cost overrun, a disagreement on architecture.

Vendor certifications (AWS, Azure, Google Cloud) are often used as screening signals for early-career candidates. They help you pass filters; they do not replace hands-on projects. See [AI-driven interviews](../../04_ai_driven_interviews/).

## Durable skills that make you hard to replace

- Networking from packets to load balancers.
- Identity and access design.
- Linux and container internals.
- Infrastructure-as-code review and testing (policy as code).
- Distributed systems failure modes.
- Cost modelling and FinOps practice.
- GPU and inference infrastructure basics.

## Adjacent roles and transitions

- **DevOps, SRE and platform engineering** ([OPS](OPS_devops_sre_platform_engineering.md)).
- **Cloud security**: overlap OV01 ([SEC](SEC_cybersecurity_defense.md), [SAR](SAR_security_architecture.md)).
- **Cloud-native backend**: overlap OV02 ([BE](BE_backend_engineering.md)).
- **MLOps and AI infrastructure**: overlap OV04 ([MLE](MLE_machine_learning_engineering.md)).
- **Network engineering** ([NET](NET_it_infrastructure_networking.md)).

## Sources

All checked October 2026.

- BLS, Occupational Outlook Handbook: Computer Network Architects; Database Administrators and Architects (2025–35; May 2025 pay; modified 27 Aug 2026). https://www.bls.gov/ooh/computer-and-information-technology/computer-network-architects.htm ; https://www.bls.gov/ooh/computer-and-information-technology/database-administrators.htm
- Stanford HAI, AI Index 2026. https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf
- ISC2, 2025 Cybersecurity Workforce Study (4 Dec 2025); India workforce research (24 Sep 2026). https://www.isc2.org/Insights/2025/12/2025-ISC2-Cybersecurity-Workforce-Study ; https://www.isc2.org/insights/2026/09/research-india-cybersecurity-workforce-reaches-a-turning-point-skills-ai
- DORA 2025 (24 Sep 2025). https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report
- Indeed Hiring Lab, job postings tracker (to 2 Oct 2026). https://github.com/hiring-lab/job_postings_tracker
- NASSCOM, Strategic Review 2026. https://nasscom.in/knowledge-center/publications/technology-sector-india-strategic-review-2026
- Payscale India: DevOps Engineer; Cloud Solutions Architect. Levels.fyi India: Solution Architect (self-reported; 12 Oct 2026). https://www.payscale.com/research/IN/Job=Development_Operations_(DevOps)_Engineer/Salary ; https://www.payscale.com/research/IN/Job=Cloud_Solutions_Architect/Salary ; https://www.levels.fyi/t/solution-architect/locations/india

_Last reviewed: 2026-10_
