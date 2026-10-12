# CLD402 · Multi-Cloud, Hybrid Cloud and Migration

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 7 | 4 (≈ 120 hours) | L3 → L4 | [CLD302](../../year_3/CLD302_infrastructure_as_code_terraform_opentofu/README.md) | [CLD501](../../year_5/CLD501_frontier_seminar_sovereign_cloud_confidential/README.md), [IND401](../../../../05_shared_years_3_to_5/IND401_industry_co_op_studio/README.md), [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) |

Part of the [Cloud Engineering major](../../README.md). Uses the networking of [CLD304](../../year_3/CLD304_cloud_networking_vpcs_dns_load_balancing/README.md) and the data skills of [CLD305](../../year_3/CLD305_cloud_storage_and_managed_databases/README.md). The enterprise-IT view of migration (data-centre estates, ITSM, enterprise architecture) is in [NET404](../../../it_infrastructure_networking/year_4/NET404_enterprise_architecture_and_cloud_migration/README.md); this course is the engineering of moving and running workloads across clouds and on-premises.

## Why this course matters now

Much of a cloud engineer's paid work is moving things: data centres closing, VMware estates re-evaluated after Broadcom ended perpetual VMware licences in favour of subscriptions in December 2023 ([SiliconANGLE](https://siliconangle.com/2023/12/12/broadcom-accelerates-vmware-transformation-killing-off-perpetual-software-licenses/)), mergers joining two clouds, regulated workloads staying on-premises next to cloud services, and a few companies leaving the cloud entirely. AWS launched Amazon Elastic VMware Service (generally available August 2025, in the Hyderabad region from December 2025), Microsoft and Google run their own VMware services, and the EU Data Act abolishes cloud switching charges, including egress, from 12 January 2027 ([Regulation (EU) 2023/2854](https://eur-lex.europa.eu/eli/reg/2023/2854/oj)). Going the other way, 37signals reported cutting roughly $2 million a year by moving compute out of AWS and planned to replace an AWS storage bill of about $1.5 million a year with under $200,000 of its own hardware ([The Register, May 2025](https://www.theregister.com/2025/05/09/37signals_cloud_repatriation_storage_savings)).

AI is now aimed squarely at this work. AWS Transform (generally available May 2025) uses agents for VMware, mainframe and .NET migrations and claims project timelines shortened four-fold on average ([AWS](https://aws.amazon.com/blogs/migration-and-modernization/aws-transform-generally-available/)); Azure's Copilot migration agent is in preview. These are vendor claims. The engineer who owns the outcome must still verify dependency maps, prove data equivalence after cutover, and decide honestly whether multi-cloud or an exit is worth its cost.

## Learning outcomes

By the end you can:

1. **Build** a migration business case and total-cost-of-ownership model that a finance team will accept.
2. **Run** discovery and dependency mapping for an estate and **assign** each application one of the 7 Rs with evidence.
3. **Plan** migration waves with landing-zone readiness, runbooks, cutover windows and rollback criteria.
4. **Execute** rehost, relocate and replatform migrations, including VMware estates and Windows/SQL Server workloads.
5. **Migrate** databases and bulk data online with change data capture, and **prove** equivalence after cutover.
6. **Design** hybrid architectures with Outposts, EKS Hybrid Nodes, Azure Arc and Azure Local, or Google Distributed Cloud, and **justify** when hybrid is permanent.
7. **Evaluate** multi-cloud strategies honestly, including when lock-in is the cheaper choice, and **design** an exit plan regulators would accept.
8. **Use** AI migration agents and **verify** their output with tests, reconciliation and dependency validation.

## Chapters and lessons

### Chapter 1 · Why organisations move (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Drivers | Data-centre exits, hardware refresh, VMware licence changes, scale and AI capacity, mergers, regulation | Interview-style exercise: extract the real driver from a vague brief |
| 1.2 TCO and business cases | On-premises cost categories (power, space, staff, licences, refresh), cloud cost categories, migration one-time costs, funding programmes | Build a TCO model for 300 VMs over 5 years |
| 1.3 Repatriation honestly | 37signals' published numbers, Dropbox's Magic Pocket, PhonePe's own data centres; steady versus spiky workloads; what cloud costs buy | Write the strongest case for and against leaving the cloud for one workload |
| 1.4 Stakeholders | Finance, security, application owners, vendors; migration as an organisational change | Draft a RACI for a migration programme |

**Check your understanding:** (1) Which on-premises costs are usually missing from TCO spreadsheets? (2) Why can a steady workload be cheaper on owned hardware? (3) What does a migration programme fail on more often than technology?

### Chapter 2 · Discovery and portfolio assessment (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Inventory | Agent and agentless discovery, CMDB quality, utilisation data, licence inventory | Run discovery on a lab estate and reconcile with a stale CMDB |
| 2.2 Dependency mapping | Network flow analysis, process-level mapping, hidden dependencies (DNS, NTP, file shares, batch jobs, hard-coded IPs) | Find three dependencies the CMDB missed |
| 2.3 The 7 Rs | Retire, retain, rehost, relocate, repurchase, replatform, refactor; AWS's guidance that refactoring during large migrations is rarely wise; zombie (under 5% use) and idle applications | Assign Rs to 20 applications with written evidence |
| 2.4 Assessment tools | AWS Transform and Migration Evaluator, Azure Migrate, Google Migration Center; right-sizing from utilisation | Compare tool recommendations with your manual sizing |

**Check your understanding:** (1) Why is "lift and shift then optimise" usually safer than refactoring during migration? (2) Which dependency is most often forgotten? (3) Why retire before you migrate?

### Chapter 3 · Planning and the migration factory (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Waves and move groups | Grouping by dependency and risk, pilot waves, velocity tracking | Plan 5 waves for 80 applications |
| 3.2 Readiness | Landing zone, networking and hybrid DNS, identity, security tooling, operations model ready before wave 1 | Write the wave-1 readiness checklist |
| 3.3 Runbooks and cutover | Freeze windows, data sync, DNS switch, smoke tests, go/no-go criteria, rollback plans | Write and rehearse a cutover runbook |
| 3.4 The factory | Automation of repeatable steps, tracking, communication, lessons per wave | Automate one runbook step with IaC |

**Check your understanding:** (1) What must be true before you can roll back after cutover? (2) Why run a pilot wave of low-risk apps? (3) What metric tells you the factory is working?

### Chapter 4 · Rehost and relocate (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Block-level replication | AWS Application Migration Service, Azure Migrate server migration, Migrate to Virtual Machines; test and cutover instances | Rehost a VM with continuous replication and a test cutover |
| 4.2 VMware relocations | Amazon EVS, Azure VMware Solution, Google Cloud VMware Engine; HCX-style moves; what you still operate | Compare the three on operations, licensing and exit paths |
| 4.3 Licensing | Windows and SQL Server licence models, bring-your-own-licence, dedicated hosts, Oracle in the cloud | Price a SQL Server estate under two licensing options |
| 4.4 Post-move fixes | Drivers, time sync, hard-coded IPs, licence activation, performance differences | Fix a planted post-migration failure |

**Check your understanding:** (1) Why is relocation fast but rarely the end state? (2) When do dedicated hosts make sense? (3) Which post-migration failures appear only days later?

### Chapter 5 · Data migration (weeks 5–6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Transfer maths | Bandwidth, time and cost; 1 PB over a fully used 10 Gbps link takes about 9 days; offline devices (Snowball, Data Box, Transfer Appliance) | Choose online or offline for 5 datasets |
| 5.2 Bulk object and file moves | DataSync, Storage Transfer Service, AzCopy, rclone; checksums and incremental sync | Move 1 TB of mixed files with verified checksums |
| 5.3 Database migration with CDC | AWS DMS and DMS Schema Conversion (with generative AI assistance), Google Database Migration Service, Azure DMS, native logical replication | Migrate a live Postgres with CDC and under 1 minute of write downtime |
| 5.4 Heterogeneous moves | Oracle or SQL Server to Postgres, schema and code conversion, the long tail of stored procedures | Convert a schema with a tool, then fix what it could not |
| 5.5 Proving equivalence | Row counts, checksums per partition, sampling, reconciliation of business totals | Write a reconciliation suite that catches a planted data drift |

**Check your understanding:** (1) Why does CDC need a consistent snapshot to start from? (2) What does a row-count match not prove? (3) When is a shipped device faster than the network?

### Chapter 6 · Replatform and refactor (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Replatform patterns | VMs to containers, self-managed to managed databases, Windows to Linux for .NET | Containerise a legacy app without code changes |
| 6.2 Strangler fig | Routing slices of traffic to new services, anti-corruption layers, data synchronisation | Carve one feature out of a monolith behind a router |
| 6.3 Mainframe modernisation | COBOL estates, rehost versus refactor to Java, AWS Transform for mainframe, test-data capture | Read a COBOL program and write a test oracle for it |
| 6.4 Measuring modernisation | Deployment frequency, cost, incident rates before and after | Define success metrics for a modernisation |

**Check your understanding:** (1) Why do modernisations stall at 80%? (2) What makes mainframe code conversion hard to verify? (3) How do you keep data consistent during a strangler migration?

### Chapter 7 · Hybrid platforms (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Cloud in your data centre | AWS Outposts, Azure Local (renamed from Azure Stack HCI in November 2024), Google Distributed Cloud (connected and air-gapped) | Compare the three on control plane location and disconnected operation |
| 7.2 One control plane, many places | Azure Arc for servers and Kubernetes, EKS Hybrid Nodes, GKE attached clusters; policy and identity across locations | Attach an on-premises Kubernetes cluster to a cloud control plane |
| 7.3 When hybrid is permanent | Latency to factories and hospitals, residency, sunk cost, specialised hardware, disconnected sites | Write a decision for a hospital chain with 40 sites |
| 7.4 Hybrid operations | Monitoring, patching, backups and identity across both worlds | Design the ops model for a hybrid estate |

**Check your understanding:** (1) What happens to an Outposts or Arc-managed site when the WAN link drops? (2) Why is identity the hardest part of hybrid? (3) When is a "temporary" hybrid state really permanent?

### Chapter 8 · Multi-cloud, honestly (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Definitions and patterns | Multi-cloud by accident (mergers, teams' choices), segmented (workload per cloud), choice per workload, parallel (same app on two clouds), portable; Gregor Hohpe's decision model | Classify five real or illustrative companies |
| 8.2 The costs of portability | Lowest-common-denominator designs, duplicated skills and tooling, data gravity and egress; when lock-in is the cheaper risk | Price a "run anywhere" design against a native one |
| 8.3 What actually ports | Containers and Kubernetes, Terraform/OpenTofu, OpenTelemetry, Postgres; what does not (IAM, networking, managed data services) | List what you would rewrite to move P2 to another cloud |
| 8.4 Cross-cloud plumbing | Workload identity federation across clouds, Cross-Cloud Interconnect and partner interconnects, DNS, central logging and FinOps (FOCUS) | Federate a workload on one cloud to read storage on another without keys |

**Check your understanding:** (1) When is running the same app on two clouds worth it? (2) Why does Kubernetes not make you cloud-independent? (3) What is data gravity, and how does it decide architecture?

### Chapter 9 · Exit, switching and sovereignty (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Exit plans | Regulators' expectations (SEBI's cloud framework covers vendor lock-in and exit), data export formats, contracts | Write an exit plan for a regulated workload |
| 9.2 Egress and switching rules | Google (January 2024) and AWS (March 2024) waive egress when leaving, with conditions; EU Data Act switching rules from 2027 | Estimate the real cost of leaving with and without waivers |
| 9.3 Sovereignty requirements | Residency versus sovereignty, government clouds, India's empanelment regime (deep dive in CLD501) | Map residency rules onto a migration plan |

**Check your understanding:** (1) Why is an untested exit plan a compliance risk? (2) What do egress waivers usually require you to do? (3) What is the difference between residency and sovereignty?

### Chapter 10 · After the move (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Hypercare | Stabilisation, performance baselines, incident readiness | Run a one-week hypercare plan in simulation |
| 10.2 Optimise | Right-sizing from real cloud metrics, commitments after stabilisation (CLD403), storage tiers | Cut the migrated estate's cost by 25% |
| 10.3 Decommission | Turning off the source, data retention, licence termination; why "temporary" duplicates linger | Write a decommissioning checklist with sign-offs |

**Check your understanding:** (1) Why buy commitments only after stabilisation? (2) What happens if the source is never turned off? (3) Who signs off a decommission?

### Chapter 11 · AI-assisted migration and modernisation (weeks 12–13)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 What the agents do | AWS Transform (VMware discovery and wave planning, mainframe decomposition, .NET porting), Azure Copilot migration agent, schema conversion with generative AI; reading vendor claims | Run an AI-assisted assessment on the lab estate and diff it against your manual one |
| 11.2 Verifying AI dependency maps | Flow-log ground truth, missing low-frequency dependencies (month-end batch jobs), false edges | Find a dependency the tool missed using flow logs |
| 11.3 Verifying AI code conversion | Characterisation tests, golden datasets, differential testing old against new | Convert a legacy module with an assistant and prove equivalence on 10,000 cases |
| 11.4 Governance | Human approval of wave plans, audit trails, rollback criteria for AI-generated changes | Write an AI-use policy for a migration programme |

**Check your understanding:** (1) Why do monthly jobs break AI-generated dependency maps? (2) What does a differential test prove? (3) Which decisions must stay human in a migration?

### Chapter 12 · Capstone defence (week 14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Presenting a migration | Business case, risk register, wave plan, evidence of cutover success | Present P3 to a panel playing CFO, CISO and app owner |

**Check your understanding:** (1) What evidence convinces a CFO? (2) What evidence convinces a CISO? (3) What would make you stop a migration?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1: TCO model | 5-year comparison |
| 2 | 2 | Lab 2: discovery and dependencies | Corrected inventory |
| 3 | 3 | Lab 3: wave plan and runbook | Rehearsed cutover; P1 starts |
| 4 | 4 | Lab 4: rehost with replication | Test cutover; P1 due |
| 5 | 5 | Lab 5: bulk data move | Checksum report |
| 6 | 5 | Lab 6: CDC database migration | Cutover under 1 minute; P2 starts |
| 7 | 6 | Lab 7: strangler fig | One feature carved out |
| 8 | 7 | Lab 8: hybrid control plane | Attached cluster |
| 9 | 8 | Lab 9: cross-cloud federation | Keyless cross-cloud read; P2 due |
| 10 | 9 | Exit plan | Plan and cost |
| 11 | 10 | Optimisation sprint | 25% saving; P3 starts |
| 12 | 11 | AI assessment versus manual | Diff report |
| 13 | 11 | AI code conversion with equivalence tests | Test results |
| 14 | 12 | P3 defence | Panel presentation |
| 15 | Review and exam | — | Written exam |

## Working with AI in this course

- **Use AI for:** first-pass application classification from inventory data, drafting runbooks, schema and code conversion, summarising vendor documentation, generating reconciliation queries, and producing wave-plan drafts. Named tools: AWS Transform, Azure Migrate with Copilot, DMS Schema Conversion, Claude Code, GitHub Copilot.
- **Do without AI (drills):** TCO arithmetic, transfer-time maths, the 7 Rs assignment for the Lab 2 estate, go/no-go decisions in the cutover rehearsal.
- **Verify AI output by:** comparing dependency maps with flow logs collected over a full business cycle; running reconciliation suites after every data move; differential testing of converted code; checking every vendor claim of speed or saving against your own measured results.
- **Where AI still fails here (show it):** tools miss low-frequency dependencies and undocumented integrations; converted code passes happy-path tests but fails on edge cases such as date handling and rounding. In P3, measure how many of your discovered dependencies and conversion defects the AI-assisted path missed.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs | 25% |
| Projects P1 / P2 / P3 | 5% / 15% / 25% |
| Written exam (7 Rs, TCO, data migration, hybrid and multi-cloud trade-offs) | 20% |
| Panel defence of P3 | 10% |

**Mastery gate:** you pass when you can, without AI help, (a) take an unseen inventory of 30 applications and produce a 7 Rs assignment and wave plan with stated evidence and risks in 90 minutes; (b) migrate a live database with change data capture, cut over with under 1 minute of write downtime and prove equivalence with a reconciliation suite; and (c) argue both for and against a multi-cloud or exit proposal with a cost model.

## Industry reality

Migration and modernisation are a large part of services and consulting work in India's IT industry, and global capability centres run migrations for their parent companies. Regulated Indian entities must plan for exit and lock-in risk under SEBI's 2023 cloud framework, and AWS's Hyderabad region now hosts Amazon EVS for VMware relocations. Vendor programmes fund migrations, so a cloud engineer often works alongside partners and must judge their plans critically.

Interview questions from this course:

1. **"We have 500 VMs in a data centre that closes in 12 months. What's your plan?"** Cover discovery, dependency mapping, 7 Rs triage, landing zone readiness, waves, factory automation, rehost first and modernise later, cutover and rollback, and decommissioning.
2. **"How do you migrate a 5 TB production database with minimal downtime?"** Cover snapshot plus CDC, replication lag monitoring, schema compatibility, cutover sequence, reconciliation, and rollback by reverse replication.
3. **"Should we be multi-cloud?"** Cover the driver behind the question, segmented versus portable patterns, the cost of portability, data gravity, skills, and when lock-in is acceptable.
4. **"Our regulator asks for an exit plan. What goes in it?"** Cover data export formats, contracts, alternative providers, rehearsal, timelines, egress costs and waivers, and key and log ownership.
5. **"An AI tool produced our migration wave plan. How do you trust it?"** Cover validating dependencies with flow logs over a full cycle, pilot waves, go/no-go criteria, and measuring the tool's accuracy.

## Resources (free first)

- **Guidance:** [AWS migration strategies (the 7 Rs)](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-guide/migration-strategies.html), [Azure Cloud Adoption Framework: migrate](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/migrate/), [Google Cloud migration center](https://docs.cloud.google.com/migration-center/docs/migration-center-overview).
- **Services:** [AWS Transform](https://aws.amazon.com/transform/), [AWS Application Migration Service](https://docs.aws.amazon.com/mgn/latest/ug/what-is-application-migration-service.html), [AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html), [Amazon EVS](https://aws.amazon.com/evs/faqs/), [Azure Arc](https://learn.microsoft.com/en-us/azure/azure-arc/overview), [Azure Local](https://learn.microsoft.com/en-us/azure/azure-local/), [EKS Hybrid Nodes](https://docs.aws.amazon.com/eks/latest/userguide/hybrid-nodes-overview.html), [Google Distributed Cloud](https://cloud.google.com/distributed-cloud).
- **Strategy:** Gregor Hohpe, [*Cloud Strategy*](https://leanpub.com/cloudstrategy) (Leanpub; paid, with free sample chapters), whose multi-cloud and lock-in chapters set out the decision model used in Chapter 8; Martin Fowler, [Strangler Fig Application](https://martinfowler.com/bliki/StranglerFigApplication.html).
- **Case studies:** [37signals cloud exit coverage](https://www.theregister.com/2025/05/09/37signals_cloud_repatriation_storage_savings) (The Register); [Dropbox Magic Pocket](https://dropbox.tech/infrastructure/magic-pocket-infrastructure).
- **Law:** [EU Data Act, Regulation (EU) 2023/2854](https://eur-lex.europa.eu/eli/reg/2023/2854/oj).
- **Practising without a big bill:** build the "legacy estate" as local VMs (VirtualBox, Multipass) or containers on your laptop, discover and migrate it into a sandbox account with free-tier instance sizes, use Postgres-to-Postgres for CDC labs, and stop replication servers between sessions because migration services bill per replicating server per hour.
- **Paid, worth it:** *Cloud Strategy* (above), and *Monolith to Microservices* (Sam Newman, O'Reilly) for strangler-fig migrations.

## Sources

All checked 12 Oct 2026.
- [AWS 7 Rs](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-guide/migration-strategies.html).
- [AWS Transform GA](https://aws.amazon.com/blogs/migration-and-modernization/aws-transform-generally-available/) (15 May 2025) and [AWS Transform for VMware GA](https://aws.amazon.com/about-aws/whats-new/2025/05/aws-transform-vmware-generally-available).
- [Amazon EVS GA](https://aws.amazon.com/blogs/migration-and-modernization/run-vmware-your-way-amazon-elastic-vmware-service-is-now-generally-available/) (5 Aug 2025) and [additional regions incl. Hyderabad](https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-evs-available-in-additional-regions/) (Dec 2025).
- [Azure Copilot agents including migration](https://azure.microsoft.com/en-us/blog/announcing-azure-copilot-agents-and-ai-infrastructure-innovations/) (Nov 2025, preview).
- [Rename of Azure Stack HCI to Azure Local](https://learn.microsoft.com/en-us/azure/azure-local/rename-to-azure-local); [EKS Hybrid Nodes deep dive](https://aws.amazon.com/blogs/multicloud/a-deep-dive-into-amazon-eks-hybrid-nodes).
- [AWS free data transfer out when moving out of AWS](https://aws.amazon.com/blogs/aws/free-data-transfer-out-to-internet-when-moving-out-of-aws/) (5 Mar 2024); [Google Cloud eliminates data transfer fees for switching](https://cloud.google.com/blog/products/networking/eliminating-data-transfer-fees-when-migrating-off-google-cloud) (Jan 2024).
- [EU Data Act](https://eur-lex.europa.eu/eli/reg/2023/2854/oj) (switching charges abolished from 12 Jan 2027).
- [The Register on 37signals](https://www.theregister.com/2025/05/09/37signals_cloud_repatriation_storage_savings) (9 May 2025).
- [Business Today on PhonePe's data centres](https://www.businesstoday.in/latest/corporate/story/phonepe-invests-200-mn-on-data-centres-350429-2022-10-20) (Oct 2022); [Dropbox Magic Pocket](https://dropbox.tech/infrastructure/magic-pocket-infrastructure).
- [SiliconANGLE on Broadcom ending VMware perpetual licences](https://siliconangle.com/2023/12/12/broadcom-accelerates-vmware-transformation-killing-off-perpetual-software-licenses/) (12 Dec 2023).

_Last reviewed: 2026-10_
