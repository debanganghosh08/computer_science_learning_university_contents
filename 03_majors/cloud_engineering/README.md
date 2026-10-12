# Cloud Engineering (CLD)

**Years 3–5 · 10 major courses · Entry requirements: [CS215 Cloud and DevOps Foundations](../../02_year_2_core_computer_science/semester_4/CS215_cloud_and_devops_foundations/README.md) and [CS212 Distributed Systems I](../../02_year_2_core_computer_science/semester_4/CS212_distributed_systems_i/README.md) · Levels L2 → L5**

Cloud engineers build and run the infrastructure that almost every product now depends on: accounts and identity, networks, compute platforms, data stores, cost controls and, increasingly, GPU clusters and model-serving systems. This major teaches cloud infrastructure engineering and architecture across AWS, Microsoft Azure and Google Cloud, always concept first and provider second, with India's regions and data rules treated as first-class design inputs.

It sits next to two neighbouring majors. [DevOps, SRE and Platform Engineering](../devops_sre_platform_engineering/README.md) owns delivery pipelines, observability, SRE practice and GitOps; [Security Architecture](../security_architecture/README.md) owns cloud security architecture as a discipline (SAR401). Cloud Engineering owns the infrastructure itself: how it is designed, built as code, connected, stored, paid for, migrated and scaled for AI.

## 1. Who this major is for, and the roles it leads to

Choose this major if you like systems you can reason about end to end, enjoy debugging across layers (DNS, IAM, routing, Kubernetes, storage), and want work that stays valuable as AI writes more of the application code.

| Role | What people in it actually do |
|---|---|
| Cloud engineer / cloud infrastructure engineer | Build and operate accounts, networks, compute and data services as code; handle tickets, incidents and upgrades; keep environments secure and affordable |
| Cloud architect | Design landing zones and reference architectures, run Well-Architected reviews, write architecture decision records, set standards other teams build on |
| Solutions architect (provider, partner or customer side) | Turn a customer's business problem into a cloud design, prove it with a working prototype, and support the build; strong communication and breadth matter as much as depth |
| Cloud network engineer | Address planning, transit and hybrid connectivity, DNS, load balancing, private service access, network troubleshooting and cost |
| Cloud data and database engineer | Choose, run and recover managed databases and storage; backups, DR, migrations, performance and residency |
| Migration and modernisation engineer | Discover estates, plan waves, move VMs and databases, modernise applications, and decommission data centres, often with AI-assisted tooling |
| FinOps / cloud cost engineer | Allocate and explain spend, build unit economics, run commitment strategy and drive usage optimisation with engineering teams |
| AI infrastructure engineer | Secure GPU and accelerator capacity, run training clusters and inference platforms, manage quotas and cost per token |
| Sovereign or confidential cloud architect (emerging) | Design for residency, sovereignty and provable confidentiality for governments and regulated industries |

The market page for this role family is [CLD in the market map](../../06_career_and_market_readiness/01_market_map/roles/CLD_cloud_engineering.md).

## 2. How AI is changing cloud work

All figures below were checked in October 2026; paragraphs marked **Analysis** are interpretation.

**Demand is being pulled by AI.** Cloud infrastructure spending reached about $143 billion in Q2 2026, up 43% year on year, and Synergy Research names generative AI as the primary driver ([Synergy, 30 July 2026](https://www.srgresearch.com/articles/q2-cloud-market-passes-143-billion-highest-growth-rate-in-eight-years)). In AI job postings, the fastest-growing skills were about running systems at scale, with AWS up 1,358% against a decade earlier ([Stanford AI Index 2026](https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf)). India is receiving large new capacity: Microsoft committed $17.5 billion for 2026–2029 ([Microsoft](https://news.microsoft.com/source/asia/2025/12/09/microsoft-invests-us17-5-billion-in-india-to-drive-ai-diffusion-at-population-scale/)) and opened its Hyderabad region in August 2026, and the IndiaAI compute portal offers 38,000 GPUs at subsidised rates ([PIB](https://static.pib.gov.in/WriteReadData/specificdocs/documents/2026/feb/doc2026210784401.pdf)).

**Agents now do first-line cloud work.** The AWS DevOps Agent, which investigates incidents across AWS, multicloud and on-premises environments, became generally available in March 2026 ([AWS](https://aws.amazon.com/about-aws/whats-new/2026/03/aws-devops-agent-generally-available)). Microsoft previewed six Azure Copilot agents for migration, deployment, optimisation, observability, resiliency and troubleshooting in November 2025 ([Microsoft](https://azure.microsoft.com/en-us/blog/announcing-azure-copilot-agents-and-ai-infrastructure-innovations/)). HashiCorp's Terraform MCP server, which lets assistants search private module registries and explain plans, became generally available in June 2026 ([HashiCorp](https://www.hashicorp.com/blog/terraform-mcp-server-is-now-generally-available)). AWS Transform has used agents for VMware, mainframe and .NET migrations since May 2025 ([AWS](https://aws.amazon.com/blogs/migration-and-modernization/aws-transform-generally-available/)).

**But reliability on infrastructure tasks is still low, and mistakes are expensive.** On the IaC-Eval benchmark, the best model in 2024 solved 19.36% of Terraform tasks, against 86.6% on a Python benchmark ([NeurIPS 2024](https://proceedings.neurips.cc/paper_files/paper/2024/hash/f26b29298ae8acd94bd7e839688e329b-Abstract.html)); a December 2025 study reached 62.6% with knowledge injection but found intent alignment did not improve ([arXiv 2512.14792](https://arxiv.org/abs/2512.14792)). Only 20% of developers who use AI apply it to deploying, operating or troubleshooting production systems ([Stack Overflow, October 2026](https://stackoverflow.blog/2026/10/06/the-results-of-the-2026-developer-survey-are-here/)), and DORA found AI adoption still negatively related to delivery stability ([DORA 2025](https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report)). In July 2025 an AI coding agent deleted a production database during a code freeze at a Replit customer ([Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-coding-platform-goes-rogue-during-code-freeze-and-deletes-entire-company-database-replit-ceo-apologizes-after-ai-engine-says-it-made-a-catastrophic-error-in-judgment-and-destroyed-all-production-data)).

**Cost has become the visible failure.** Flexera's 2026 survey estimated wasted IaaS and PaaS spend at 29%, the first rise in five years, with AI workloads named as a cause, and 85% of respondents called managing cloud spend a top challenge ([Flexera, March 2026](https://www.flexera.com/about-us/press-center/flexera-finds-cloud-value-is-rising-while-ai-waste-grows)).

**Routine administration is shrinking; design and architecture are growing.** The US Bureau of Labor Statistics projects network and computer systems administrators at −4% for 2025–35, as routine work shifts to DevOps-focused roles and network-as-a-service, while computer network architects grow 8% ([BLS](https://www.bls.gov/ooh/computer-and-information-technology/network-and-computer-systems-administrators.htm), [BLS](https://www.bls.gov/ooh/computer-and-information-technology/computer-network-architects.htm); see the [market map](../../06_career_and_market_readiness/01_market_map/README.md)).

| Being automated | Augmented (human decides) | Growing in value |
|---|---|---|
| Boilerplate IaC and manifests, first-draft IAM policies, console click-paths, routine patching and rightsizing recommendations, first-pass log reading, migration inventories | Incident investigation, migration wave planning, cost analysis, architecture options, code conversion | Architecture trade-offs, plan and diff review, IAM and network reasoning, data recovery, capacity for AI, cost and unit economics, residency and sovereignty design, governing agents with apply rights |

**Analysis.** The cloud engineer of 2026 spends less time typing configuration and more time reviewing it: reading plans, proving restores, bounding what agents may change, and explaining cost and risk to people who decide. Every course in this major therefore includes AI-off drills, a verification method and a demonstrated failure mode of current tools.

## 3. The 5-year path

### Years 1–2: the common core (courses that matter most for this major in bold)

| Year · Semester | Courses |
|---|---|
| 1 · 1 | FND101 Programming I, FND102 How Computers Work, FND103 Discrete Maths, **[FND104 The Developer's Toolkit: Linux, Shell, Git](../../01_year_1_foundations/semester_1/FND104_the_developers_toolkit_linux_shell_git/README.md)**, **[FND105 AI-Native Learning and Building](../../01_year_1_foundations/semester_1/FND105_ai_native_learning_and_building/README.md)**, FND106 Technical Communication |
| 1 · 2 | FND111 Programming II, FND112 DSA I, FND113 Linear Algebra and Calculus, **[FND114 Web Foundations](../../01_year_1_foundations/semester_2/FND114_web_foundations_http_html_css_and_javascript/README.md)**, **[FND115 Databases I](../../01_year_1_foundations/semester_2/FND115_databases_i_data_modeling_and_sql/README.md)**, FND116 Probability and Statistics |
| 2 · 3 | CS201 Algorithms, CS202 Architecture and C, **[CS203 Operating Systems](../../02_year_2_core_computer_science/semester_3/CS203_operating_systems/README.md)**, **[CS204 Computer Networks](../../02_year_2_core_computer_science/semester_3/CS204_computer_networks/README.md)**, **[CS205 Software Engineering I](../../02_year_2_core_computer_science/semester_3/CS205_software_engineering_i_design_testing/README.md)**, CS206 Maths for ML |
| 2 · 4 | **[CS211 Database Systems Internals](../../02_year_2_core_computer_science/semester_4/CS211_database_systems_internals/README.md)**, **[CS212 Distributed Systems I](../../02_year_2_core_computer_science/semester_4/CS212_distributed_systems_i/README.md)**, **[CS213 Security Foundations](../../02_year_2_core_computer_science/semester_4/CS213_security_foundations/README.md)**, CS214 ML Foundations, **[CS215 Cloud and DevOps Foundations](../../02_year_2_core_computer_science/semester_4/CS215_cloud_and_devops_foundations/README.md)**, CS216 Compilers |

Why these matter: Linux and the shell (FND104) are the daily environment; OS and networks (CS203, CS204) explain every container, VPC and DNS problem; distributed systems (CS212) explain replication, consensus and failure; CS215 is the gateway to this major.

### Years 3–5: the major

| Year · Semester | Major courses | Shared and other courses |
|---|---|---|
| 3 · 5 | [CLD301 Cloud Architecture on AWS, Azure and Google Cloud](year_3/CLD301_cloud_architecture_on_aws_azure_and_google_cloud/README.md) · [CLD302 Infrastructure as Code: Terraform, OpenTofu and Pulumi](year_3/CLD302_infrastructure_as_code_terraform_opentofu/README.md) · [CLD303 Containers and Kubernetes](year_3/CLD303_containers_and_kubernetes/README.md) | [PRO301 Professional Practice: Ethics, Law and Responsible AI](../../05_shared_years_3_to_5/PRO301_professional_practice_ethics_law_and_responsible/README.md) |
| 3 · 6 | [CLD304 Cloud Networking: VPCs, DNS, Load Balancing and CDNs](year_3/CLD304_cloud_networking_vpcs_dns_load_balancing/README.md) · [CLD305 Cloud Storage and Managed Databases](year_3/CLD305_cloud_storage_and_managed_databases/README.md) | [CAR301 Career Lab I](../../05_shared_years_3_to_5/CAR301_career_lab_i_dsa_mastery_portfolio_and_open/README.md) · one elective |
| 4 · 7 | [CLD401 Serverless and Event-Driven Cloud](year_4/CLD401_serverless_and_event_driven_cloud/README.md) · [CLD402 Multi-Cloud, Hybrid Cloud and Migration](year_4/CLD402_multi_cloud_hybrid_cloud_and_migration/README.md) | [IND401 Industry Co-op Studio](../../05_shared_years_3_to_5/IND401_industry_co_op_studio/README.md) · overlap course 1 |
| 4 · 8 | [CLD403 FinOps and Cloud Cost Engineering](year_4/CLD403_finops_and_cloud_cost_engineering/README.md) · [CLD404 AI Infrastructure in the Cloud: GPUs, Inference and Managed AI](year_4/CLD404_ai_infrastructure_in_the_cloud_gpus_inference/README.md) | [CAR401 Career Lab II](../../05_shared_years_3_to_5/CAR401_career_lab_ii_interviews_system_design_and_ai/README.md) · overlap course 2 |
| 5 · 9 | [CLD501 Frontier Seminar: Sovereign Cloud, Confidential Computing and Planet-Scale Infrastructure](year_5/CLD501_frontier_seminar_sovereign_cloud_confidential/README.md) | [RES501 Research Methods](../../05_shared_years_3_to_5/RES501_research_methods_and_scientific_writing/README.md) · [RES502 Reading, Reproducing and Extending Papers](../../05_shared_years_3_to_5/RES502_reading_reproducing_and_extending_papers/README.md) · [THS501 Thesis or Capstone I](../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) |
| 5 · 10 | — | [THS502 Thesis or Capstone II](../../05_shared_years_3_to_5/THS502_thesis_or_capstone_ii/README.md) · [LCH502 Career Launch and Founder Studio](../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md) · one elective |

Course dependencies inside the major: CLD301 → CLD401; CLD302 → CLD402; CLD303 → CLD403; CLD304 → CLD404; CLD401 and CLD403 → CLD501. Build every lab from Year 3 onwards with your CLD302 modules, so by Year 4 you own a reusable personal platform.

## 4. Skill map by level

| Level | You can… | Where you get it |
|---|---|---|
| L0 | Follow a tutorial to launch a VM, create a bucket and SSH in; use the shell and Git | FND104 |
| L1 | Explain regions, zones, IAM, VPCs and containers; deploy a simple app to one cloud with guidance; read a bill | CS204, CS215 |
| L2 (intern-ready) | Build a secure single-account environment and a multi-AZ app with IaC; write a least-privilege policy; run workloads on Kubernetes; debug common networking and permission errors | CLD301–CLD303 |
| L3 (job-ready) | Design a landing zone and network for an organisation; run managed databases with tested DR; pass CKA-level troubleshooting; build event-driven systems that are correct under duplicates; explain cost per unit; review AI-generated IaC safely | CLD304, CLD305, CLD401, CAR301 |
| L4 (expert, hard to replace) | Lead migrations and multi-cloud decisions with evidence; run FinOps for a large estate; design and operate GPU training and inference platforms; handle novel failures across layers; set standards and govern agents | CLD402–CLD404, IND401, CAR401 |
| L5 (research and frontier) | Reproduce and extend systems research; design sovereign and confidential platforms; measure energy and carbon credibly; publish | CLD501, RES501, RES502, THS501–502 |

Each course states its own mastery gate. The major's overall gate is the flagship project below.

## 5. Recommended overlaps and electives

**Overlap specialisations** (Year 4, two courses each):

- [OV01 Cloud Security](../../04_overlaps/OV01_cloud_security/README.md) (CLD301 + SAR401 + SEC303): for cloud security engineer and cloud security architect roles; cloud security was the most-cited security skills need after AI in ISC2's 2025 study ([ISC2](https://www.isc2.org/Insights/2025/12/2025-ISC2-Cybersecurity-Workforce-Study)).
- [OV02 Cloud-Native Backend](../../04_overlaps/OV02_cloud_native_backend/README.md) (BE301 + BE304 + CLD303): for engineers who want to own services and their platform.
- [OV04 MLOps and ML Platform Engineering](../../04_overlaps/OV04_mlops_ml_platform/README.md) (MLE401 + OPS401 + CLD404): the most direct route to AI infrastructure roles.
- [OV06 Data Platform and Analytics Engineering](../../04_overlaps/OV06_data_platform_analytics_engineering/README.md) (DEN305 + DAN304 + CLD305): for data platform and cloud data engineering roles.

**Electives** (choose by target role):

| Target | Electives |
|---|---|
| Reliability and operations | [OPS304 Site Reliability Engineering](../devops_sre_platform_engineering/year_3/OPS304_site_reliability_engineering_slos_error_budgets/README.md), [OPS303 Observability](../devops_sre_platform_engineering/year_3/OPS303_observability_metrics_logs_traces/README.md), [OPS402 Chaos Engineering](../devops_sre_platform_engineering/year_4/OPS402_chaos_engineering_and_resilience/README.md) |
| Platform and delivery | [OPS305 Configuration Management and GitOps](../devops_sre_platform_engineering/year_3/OPS305_configuration_management_and_gitops/README.md), [OPS401 Platform Engineering](../devops_sre_platform_engineering/year_4/OPS401_platform_engineering_and_internal_developer/README.md) |
| Networking | [NET301 Routing and Switching](../it_infrastructure_networking/year_3/NET301_routing_and_switching/README.md), [NET401 Data Center and Hybrid Infrastructure](../it_infrastructure_networking/year_4/NET401_data_center_and_hybrid_infrastructure/README.md) |
| Security | [SEC303 Identity and Access Management](../cybersecurity_defense/year_3/SEC303_identity_and_access_management/README.md), [SAR303 Zero Trust Architecture](../security_architecture/year_3/SAR303_zero_trust_architecture/README.md) |
| AI infrastructure | [MLE402 Distributed Training](../machine_learning_engineering/year_4/MLE402_distributed_training_and_large_scale_ml/README.md), [MLE404 Efficient Inference](../machine_learning_engineering/year_4/MLE404_efficient_inference_quantization_distillation/README.md) |
| Data | [DEN402 Cloud Data Platforms](../data_engineering/year_4/DEN402_cloud_data_platforms_snowflake_bigquery/README.md) |

## 6. Flagship industry project

The major's flagship project is specified in [06_career_and_market_readiness/05_industry_projects/CLD_cloud_engineering.md](../../06_career_and_market_readiness/05_industry_projects/CLD_cloud_engineering.md). It joins the course projects into one production-grade system: a landing zone and network built as code (CLD301, CLD302, CLD304), a Kubernetes platform (CLD303), data with proven DR and residency (CLD305), an event-driven workflow (CLD401), cost allocation and unit economics (CLD403) and an AI inference path with SLOs (CLD404), defended in front of a panel. It is the portfolio piece you show in interviews.

## 7. Certifications worth having (optional, never required)

**Honest value note.** Certifications help you pass résumé filters, especially at services firms, partners and in early-career hiring in India, and hands-on exams (CKA) prove more than multiple-choice ones. They do not replace a portfolio: an interviewer will ask you to debug, design and explain, and a strong P3 from any CLD course says more than a badge. Take at most one or two, timed to the course that already prepares you, and verify the current exam version before booking.

| Certification (October 2026 name) | Best timed after | Note |
|---|---|---|
| AWS Certified Solutions Architect – Associate | CLD301 | A common first cloud certification; its scope matches CLD301 closely |
| AWS Certified CloudOps Engineer – Associate | CLD302, CLD304 | Operations-focused associate exam listed on AWS's current certification page |
| AWS Certified Solutions Architect – Professional | CLD402 | Worth it only with real design experience; exam being updated in 2026 |
| AWS Certified Advanced Networking – Specialty | CLD304 | Scheduled to retire in 2026 (AWS sources give different dates); skip unless you can take it before retirement |
| AWS Certified Generative AI Developer – Professional | CLD404 | New professional-level exam (AIP-C01); relevant for AI platform work on AWS |
| Microsoft AZ-104, AZ-305 (Azure Solutions Architect Expert requires AZ-104), AZ-700 | CLD301, CLD304 | AZ-305 was updated on 17 April 2026 |
| Google Associate Cloud Engineer, Professional Cloud Architect, Professional Cloud Network Engineer | CLD301, CLD304 | Check the current list on Google Cloud's certification page |
| CNCF CKA (and CKAD, CKS; KCNA as a warm-up) | CLD303 | Performance-based; CKA uses Kubernetes v1.35, 2 hours, two killer.sh simulator sessions and one retake included, US$445 |
| CNCF Certified Cloud Native Platform Engineer (CNPE) | CLD303 + OPS401 | Launched November 2025; performance-based |
| HashiCorp Certified: Terraform Associate (004) | CLD302 | Version 004 since 8 January 2026, testing Terraform 1.12 |
| FinOps Certified Practitioner | CLD403 | Useful for FinOps and cost roles |

## 8. The interview loop for cloud roles

A typical loop for cloud engineer and cloud architect roles in 2026 (analysis based on the [AI-driven interviews section](../../06_career_and_market_readiness/04_ai_driven_interviews/)):

1. **Screen:** recruiter call, then an online assessment (often light DSA plus Linux, networking and cloud multiple choice). Some employers allow AI in assessments and some forbid it; read the instructions.
2. **Fundamentals deep dive:** IAM evaluation, VPC routing and DNS, Kubernetes internals, storage consistency, explained aloud (CLD301, CLD303, CLD304, CLD305).
3. **Hands-on troubleshooting:** a broken environment or cluster to fix live, the most predictive round for cloud engineers (CLD303 Chapter 11, CLD304 Chapter 10).
4. **IaC review:** a Terraform pull request, often with AI-generated defects, to review and fix (CLD302 Chapter 10).
5. **Cloud system design:** a landing zone, a multi-region service, a migration plan or an AI inference platform, with cost and failure modes (CLD301, CLD402, CLD404; practise in CAR401).
6. **Behavioural and incident story:** an outage you handled, a cost you cut, a decision you reversed, with evidence.

Solutions architect loops add a customer role-play and a whiteboard presentation; AI infrastructure loops add GPU sizing and cost-per-token questions; FinOps loops add a billing-data exercise.

## 9. Fast track for working professionals

Budget about 15 hours a week. Take the gate tests of CS215 and CS212 first; if you pass, start directly.

| You are now | Path (about 6–9 months) | Proof to build |
|---|---|---|
| System or network administrator | CLD301 → CLD302 → CLD304 → CLD303 | CLD304 P3 and a CKA |
| Backend or full-stack developer | CLD301 → CLD302 → CLD303 → CLD401 | CLD401 P2 and CLD303 P3 |
| Data engineer or DBA | CLD301 → CLD302 → CLD305 → CLD403 | CLD305 P3 |
| ML engineer moving to AI infrastructure | CLD303 → CLD304 (Chapters 1–6) → CLD404 → CLD403 Chapter 9 | CLD404 P3 |
| Services-firm engineer aiming at architecture | CLD301 → CLD302 → CLD402 → CLD403 | CLD402 P3 and a business case |

Finish with the flagship project and [CAR401](../../05_shared_years_3_to_5/CAR401_career_lab_ii_interviews_system_design_and_ai/README.md) for interview preparation.

## Sources

All checked 12 Oct 2026.
- [Synergy Research, Q2 2026](https://www.srgresearch.com/articles/q2-cloud-market-passes-143-billion-highest-growth-rate-in-eight-years) (30 Jul 2026).
- [Stanford AI Index 2026](https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf) (AI posting skills growth), as summarised in this repository's [market map](../../06_career_and_market_readiness/01_market_map/README.md).
- [AWS DevOps Agent GA](https://aws.amazon.com/about-aws/whats-new/2026/03/aws-devops-agent-generally-available) (31 Mar 2026); [AWS frontier agents](https://press.aboutamazon.com/2025/12/aws-unveils-frontier-agents-a-new-class-of-ai-agents-that-work-as-an-extension-of-your-software-development-team) (2 Dec 2025).
- [Azure Copilot agents](https://azure.microsoft.com/en-us/blog/announcing-azure-copilot-agents-and-ai-infrastructure-innovations/) (Nov 2025).
- [Terraform MCP server GA](https://www.hashicorp.com/blog/terraform-mcp-server-is-now-generally-available) (11 Jun 2026); [AWS Transform GA](https://aws.amazon.com/blogs/migration-and-modernization/aws-transform-generally-available/) (15 May 2025).
- [IaC-Eval](https://proceedings.neurips.cc/paper_files/paper/2024/hash/f26b29298ae8acd94bd7e839688e329b-Abstract.html) (NeurIPS 2024); [arXiv 2512.14792](https://arxiv.org/abs/2512.14792) (Dec 2025).
- [Stack Overflow 2026 results](https://stackoverflow.blog/2026/10/06/the-results-of-the-2026-developer-survey-are-here/) (6 Oct 2026); [DORA 2025](https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report).
- [Flexera 2026 State of the Cloud](https://www.flexera.com/about-us/press-center/flexera-finds-cloud-value-is-rising-while-ai-waste-grows) (18 Mar 2026).
- BLS Occupational Outlook: [network and computer systems administrators](https://www.bls.gov/ooh/computer-and-information-technology/network-and-computer-systems-administrators.htm), [computer network architects](https://www.bls.gov/ooh/computer-and-information-technology/computer-network-architects.htm) (2025–35 projections).
- [Microsoft $17.5 billion India investment](https://news.microsoft.com/source/asia/2025/12/09/microsoft-invests-us17-5-billion-in-india-to-drive-ai-diffusion-at-population-scale/) (9 Dec 2025); [PIB explainer on IndiaAI compute](https://static.pib.gov.in/WriteReadData/specificdocs/documents/2026/feb/doc2026210784401.pdf) (Feb 2026).
- Certifications: [AWS certification list](https://aws.amazon.com/certification/); [AWS Generative AI Developer – Professional](https://aws.amazon.com/certification/certified-generative-ai-developer-professional/); [Azure Solutions Architect Expert](https://learn.microsoft.com/en-us/credentials/certifications/azure-solutions-architect/); [Google Cloud certifications](https://cloud.google.com/learn/certification); [CNCF certifications](https://www.cncf.io/training/certification/); [CNPE launch](https://www.cncf.io/announcements/2025/11/11/cncf-launches-cnpe-certification-to-define-enterprise-scale-platform-engineering-globally/) (11 Nov 2025); [CKA](https://training.linuxfoundation.org/certification/certified-kubernetes-administrator-cka/); [HashiCorp Terraform Associate 004](https://developer.hashicorp.com/certifications/infrastructure-automation); [FinOps Certified Practitioner](https://learn.finops.org/path/finops-certified-practitioner-self-paced).
- AWS Advanced Networking retirement: [AWS certification page](https://aws.amazon.com/certification/) (retiring 2026) and [AWS Builder Center roundup, September 2026](https://builder.aws.com/content/3JTUwe7A9dlfH5x0kPS4cJAyCMo/aws-certification-updates-you-might-have-missed-september-2026) (date moved to 31 Dec 2026; unconfirmed on the exam page).

_Last reviewed: 2026-10_
