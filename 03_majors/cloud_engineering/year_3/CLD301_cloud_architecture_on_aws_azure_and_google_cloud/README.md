# CLD301 · Cloud Architecture on AWS, Azure and Google Cloud

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 5 | 4 (≈ 120 hours) | L2 → L3 | [CS215](../../../../02_year_2_core_computer_science/semester_4/CS215_cloud_and_devops_foundations/README.md), [CS212](../../../../02_year_2_core_computer_science/semester_4/CS212_distributed_systems_i/README.md) | [CLD401](../../year_4/CLD401_serverless_and_event_driven_cloud/README.md), [OV01 Cloud Security](../../../../04_overlaps/OV01_cloud_security/README.md), [CLD501](../../year_5/CLD501_frontier_seminar_sovereign_cloud_confidential/README.md) |

Part of the [Cloud Engineering major](../../README.md). Taken alongside [CLD302 Infrastructure as Code](../CLD302_infrastructure_as_code_terraform_opentofu/README.md) and [CLD303 Containers and Kubernetes](../CLD303_containers_and_kubernetes/README.md). Networking and data get their own courses ([CLD304](../CLD304_cloud_networking_vpcs_dns_load_balancing/README.md), [CLD305](../CLD305_cloud_storage_and_managed_databases/README.md)); here you learn enough of each to make architecture decisions.

## Why this course matters now

A cloud architect decides where a workload runs, how it fails, who can touch it and what it costs, and then defends those decisions in writing. In Q2 2026 the three largest providers held 28% (AWS), 20% (Microsoft) and 15% (Google) of a cloud infrastructure market worth about $143 billion a quarter, growing 43% a year, with generative AI named as the main driver ([Synergy Research, July 2026](https://www.srgresearch.com/articles/q2-cloud-market-passes-143-billion-highest-growth-rate-in-eight-years)). Most real organisations touch at least two of them, so this course teaches each concept once, provider-neutrally, and then maps it to all three.

AI assistants now draft architecture diagrams, IAM policies and Well-Architected answers in seconds, and agents such as the [AWS DevOps Agent](https://aws.amazon.com/about-aws/whats-new/2026/03/aws-devops-agent-generally-available) (generally available March 2026) and the [Azure Copilot agents](https://azure.microsoft.com/en-us/blog/announcing-azure-copilot-agents-and-ai-infrastructure-innovations/) (preview since November 2025) investigate incidents and propose deployments. What they cannot do is own the trade-off: whether a payment workload in Mumbai needs a second region, whether an IAM policy is least-privilege for *your* organisation, or what happens to your design when a regional control plane fails, as us-east-1's DynamoDB DNS automation did on 19–20 October 2025 ([AWS](https://aws.amazon.com/message/101925/)). That judgement is what this course builds.

## Learning outcomes

By the end you can:

1. **Explain** the physical and logical structure of a hyperscale cloud (regions, availability zones, edge locations, control plane versus data plane) and **choose** a region for a workload using latency, service availability, data residency and price.
2. **Compare** compute options (VMs, containers, functions, bare metal, Arm versus x86, Spot) and **justify** a choice with numbers.
3. **Write and debug** least-privilege IAM policies on AWS, Azure and Google Cloud, and **trace** a request through each provider's policy evaluation logic.
4. **Design** a multi-account (or multi-subscription, multi-project) landing zone with guardrails, central logging and break-glass access.
5. **Calculate** composite availability, and **design** for zonal and regional failure using static stability, cells and shuffle sharding.
6. **Run** a Well-Architected review on a real workload using the AWS, Azure or Google Cloud framework, and **write** prioritised findings.
7. **Produce** a reference architecture with diagrams, architecture decision records (ADRs), a threat list, a cost estimate and a DR plan.
8. **Review** AI-generated architecture and IAM output, and **show** at least one failure it missed.

## Chapters and lessons

### Chapter 1 · What a cloud actually is (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 From data centre to API | Virtualisation, hypervisors and offload cards (the AWS Nitro System as an example), multi-tenancy, everything as an API call | Trace one `RunInstances` / `az vm create` / `gcloud compute instances create` call with `--debug` and list the API endpoints it hits |
| 1.2 Regions, zones and edge | Region = independent geography; availability zone (AZ) = one or more isolated data centres; edge PoPs; AWS reports 39 regions and 124 AZs; India has AWS Mumbai and Hyderabad, Azure Pune, Chennai, Mumbai and Hyderabad (India South Central, August 2026), Google Mumbai and Delhi | Build a table of India regions with zone counts and three services missing from the newest region |
| 1.3 Control plane vs data plane | Why creating a VM can fail while running VMs keep serving; regional versus global services; dependency on IAM, DNS and STS | Classify 15 API calls as control or data plane and mark which ones a running app needs at 3 a.m. |
| 1.4 Shared responsibility | What the provider secures (facilities, hypervisor, managed-service internals) and what you secure (identity, data, configuration), and how the line moves from IaaS to SaaS | Fill a shared-responsibility matrix for a VM, a managed database and a function on all three providers |
| 1.5 Service models and lock-in gradient | IaaS, PaaS, serverless, SaaS; portability cost versus operating cost | Rank ten services by portability and by operational toil, then argue the ranking |

**Check your understanding:** (1) Why can a workload in one AZ survive another AZ's power failure but not a regional IAM outage? (2) Which of your responsibilities stays the same when you move a database from a VM to a managed service? (3) A new region lacks a GPU type you need: what are your three options?

### Chapter 2 · Compute primitives and how to choose (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Instance families | General, compute, memory, storage and accelerator families; naming schemes (`m7g.large`, `Standard_D4s_v5`, `n2-standard-4`); vCPU versus physical core | Decode 10 instance names across three providers |
| 2.2 Arm and x86 | Graviton, Azure Cobalt, Google Axion; price-performance; multi-arch images | Benchmark one service on Arm and x86 and compute cost per 1,000 requests |
| 2.3 Purchase models | On-demand, reserved/committed, Savings Plans, Spot/preemptible and their interruption notices | Design which tier of a three-tier app can run on Spot |
| 2.4 Elasticity | Auto Scaling groups, VM scale sets, managed instance groups; launch templates; health checks; warm pools | Configure target-tracking scaling and record scale-out time |
| 2.5 Containers and functions in context | When a VM, a container platform or a function is the right unit; cold start and execution limits as design inputs | Write a one-page decision for three workloads (batch, API, cron) |

**Check your understanding:** (1) Why can two instance types with the same vCPU count perform very differently? (2) What breaks if a stateful service runs on Spot without draining? (3) When is a bigger instance cheaper than more instances?

### Chapter 3 · Storage, data and networking for architects (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Block, file and object | Durability versus availability; S3's 11-nines durability design and strong read-after-write consistency; EBS versus instance store | Pick storage for logs, a Postgres data directory, shared ML datasets and user uploads |
| 3.2 Managed databases in one hour | Managed SQL, key-value, document, analytical stores; what "managed" removes and what it leaves | Map one workload's data to services on all three clouds |
| 3.3 VPC basics | CIDR, public and private subnets, route tables, NAT, security groups versus NACLs; Azure's new private-by-default subnets after 31 March 2026 | Draw a two-AZ VPC with public, private and data subnets |
| 3.4 Getting traffic in and out | L4 and L7 load balancers, DNS, CDN, private endpoints | Trace a user request from browser to database, naming every hop |

**Check your understanding:** (1) Why is "11 nines of durability" not an availability promise? (2) What does a NAT gateway cost you besides money? (3) Why do private endpoints matter for both security and egress cost?

### Chapter 4 · Identity and access I: the model (weeks 4–5)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Principals, resources, actions | Users, groups, roles, service accounts, managed identities; authentication versus authorisation | Draw the identity graph of a small team's account |
| 4.2 AWS policy evaluation | Identity, resource, permission-boundary, session, SCP and RCP policies; explicit deny wins; the evaluation flow chart | Predict allow/deny for 12 requests, then check with the IAM policy simulator |
| 4.3 Azure RBAC and Entra ID | Role definitions, scopes (management group → subscription → resource group → resource), deny assignments, Azure Policy, Privileged Identity Management | Assign a custom role at the narrowest scope and prove it with `az role assignment list` |
| 4.4 Google Cloud IAM | Resource hierarchy (organisation → folders → projects), roles and bindings, IAM deny policies, organisation policies, conditions | Write a binding with a time-bound condition and test it |
| 4.5 Workload identity | Instance roles, managed identities, workload identity federation (GitHub Actions OIDC to all three clouds), why long-lived keys are the top finding in most audits | Replace a CI access key with OIDC federation and delete the key |

**Check your understanding:** (1) An SCP allows `s3:*` and the role policy allows `s3:GetObject`: what can the role do? (2) Why is a resource policy dangerous when you forget it exists? (3) What does workload identity federation remove from your threat model?

### Chapter 5 · Identity and access II: least privilege in practice (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Generating and tightening policies | Access Analyzer policy generation and unused-access findings, Azure and Google role recommenders | Start from `*`, run a workload for a day, generate a policy and cut it to the minimum |
| 5.2 Data perimeters | SCPs on principals and RCPs on resources (AWS, November 2024; S3, STS, KMS, SQS, Secrets Manager at launch, DynamoDB from February 2026), `aws:PrincipalOrgID`, VPC endpoint policies | Write a perimeter that blocks access from outside your organisation and test it from a second account |
| 5.3 Human access | SSO (IAM Identity Center, Entra ID, Cloud Identity), MFA, just-in-time elevation, break-glass accounts | Design break-glass with alerting and a quarterly test |
| 5.4 Secrets and keys | KMS key policies, envelope encryption, customer-managed keys, rotation, secrets managers | Encrypt an object with a customer-managed key and show a denied decrypt from another role |

**Check your understanding:** (1) Why is "least privilege" a process rather than a policy? (2) What attack does an RCP stop that an SCP cannot? (3) Who should be able to delete a KMS key, and how do you stop everyone else?

### Chapter 6 · Landing zones and organisation design (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Why many accounts | Blast radius, quotas, billing and permission boundaries; AWS's multi-account whitepaper (April 2025) | Split a single-account startup into accounts and justify each one |
| 6.2 AWS foundations | Organizations, OUs (Security, Infrastructure, Workloads, Sandbox), Control Tower, Landing Zone Accelerator, log-archive and audit accounts | Sketch the OU tree for a fintech with prod, non-prod and a PCI scope |
| 6.3 Azure and Google foundations | Management groups and Azure Landing Zones (Cloud Adoption Framework), platform versus application landing zones; Google's resource hierarchy, enterprise foundations blueprint and Cloud Foundation Fabric | Map your AWS design onto Azure and Google Cloud |
| 6.4 Guardrails | Preventive (SCP, Azure Policy deny, org policy) versus detective (Config, Defender, Security Command Center); tagging policy; region restriction for data residency | Write three preventive guardrails, including "only India regions for this OU" |
| 6.5 Vending and lifecycle | Account/subscription vending, baselines, decommissioning | Write a runbook for creating and closing a workload account |

**Check your understanding:** (1) Why should the log-archive account be one almost nobody can log in to? (2) What breaks if you restrict regions but forget global services? (3) When is one account per team better than one per environment?

### Chapter 7 · Designing for failure (weeks 8–9)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Availability arithmetic | SLA versus SLO; serial and parallel composition; why 99.99% × 99.99% × 99.95% is worse than any part | Compute composite availability for a three-tier app with and without a second AZ |
| 7.2 Multi-AZ and static stability | Pre-provisioned capacity so a zone loss needs no control-plane calls (AWS Builders' Library) | Show your design still serves when the scaling API is unavailable |
| 7.3 Cells and shuffle sharding | Cell-based architecture, blast-radius reduction, shuffle sharding of customers to workers | Simulate 8 workers, 100 customers, one poison customer: compare plain and shuffle sharding |
| 7.4 Regional failure and DR | RPO and RTO; backup and restore, pilot light, warm standby, multi-site active-active; region pairs (Azure pairs India South Central with Central India) | Choose a DR pattern for four workloads with stated RPO/RTO and cost |
| 7.5 Quotas, limits and dependencies | Service quotas as an outage cause; hidden global dependencies (DNS, IAM, STS, certificate issuance) | Build a dependency map and quota sheet for your P3 design |
| 7.6 Learning from outages | AWS October 2025 (empty DNS record from an automation race), Google Cloud June 2025 (blank policy fields crashing Service Control), Cloudflare November 2025 (oversized generated config) | One-page analysis: trigger, latent cause, which design pattern would have contained it |

**Check your understanding:** (1) Why can adding a dependency lower availability even if it is highly available? (2) What does static stability cost you every day? (3) Why is "active-active across regions" rarely the right first answer?

### Chapter 8 · Well-Architected frameworks and reviews (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 AWS Well-Architected | Six pillars (operational excellence, security, reliability, performance efficiency, cost optimisation, sustainability), lenses (serverless, SaaS, generative AI, machine learning), the free Well-Architected Tool | Run a review of a sample workload in the WA Tool |
| 8.2 Azure Well-Architected | Five pillars, workload guides (AI, mission-critical, SaaS), the Azure Well-Architected Review assessment and Advisor | Score the same workload with the Azure assessment |
| 8.3 Google Cloud Well-Architected | Six pillars including sustainability, plus AI and ML and financial-services perspectives (updated January 2026) | Compare the three frameworks' reliability questions side by side |
| 8.4 Running a review that changes something | Interviewing owners, evidence over opinion, high-risk issues, an improvement plan with owners and dates | Lab 6: a full review report |

**Check your understanding:** (1) Why do frameworks say a review is "not an audit"? (2) Which pillar trade-offs conflict most often, and how do you record the decision? (3) What evidence would convince you a workload meets its RTO?

### Chapter 9 · Reference architectures (weeks 11–12)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Three-tier and its failure modes | Web, app and data tiers; sessions; connection pooling; read replicas | Draw and price a three-tier app in Mumbai on two providers |
| 9.2 Event-driven and serverless | Queues, event buses, functions, idempotent consumers | Re-draw the same app with an event-driven order pipeline |
| 9.3 Multi-tenant SaaS | Silo, pool and bridge tenancy; noisy neighbours; per-tenant cost | Choose tenancy for a B2B SaaS with 5 large and 2,000 small customers |
| 9.4 Generative AI application | Model endpoints (Amazon Bedrock, Microsoft Foundry, Gemini Enterprise Agent Platform), retrieval stores, guardrails, quotas, cost per request | Draw a retrieval-augmented support bot with data staying in India |
| 9.5 Scale case study | Disney+ Hotstar's 59 million concurrent streams and the move away from two self-managed Kubernetes clusters | List the architectural limits they hit and the cloud pattern for each |

**Check your understanding:** (1) What is the first bottleneck when a three-tier app gets 10× traffic in one minute? (2) Why does pooled tenancy make cost allocation hard? (3) Which part of a GenAI architecture has the strictest quota?

### Chapter 10 · Architecture as a written practice (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 ADRs and diagrams | Architecture decision records, C4 model, diagrams as code | Write five ADRs for P3 |
| 10.2 Cost as a design input | Unit cost, data transfer, NAT and inter-AZ charges as architecture drivers (deep dive in CLD403) | Find the most expensive arrow in your diagram |
| 10.3 Compliance and residency | DPDP Act 2023 and its 2025 Rules, RBI payment-data storage, SEBI cloud framework at outline level (deep dive in CLD501) | Mark every data store in P3 with its residency rule |
| 10.4 Reviewing AI-drafted designs | Prompting for options, not answers; checking claims against docs; red-teaming a design | Critique an AI-generated architecture and log every error |

**Check your understanding:** (1) Why write down rejected options? (2) Which arrows on a diagram cost money? (3) What residency question must be answered before choosing a region?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1: account safety and API tracing | Budget alarm + region table |
| 2 | 2 | Lab 2: Arm versus x86 benchmark | Cost per 1,000 requests |
| 3 | 3 | Lab 3: two-AZ VPC | Diagram and working VPC; P1 starts |
| 4 | 4 | Lab 4: IAM evaluation drills | 12 predictions checked; P1 due |
| 5 | 4 | Lab 4 continued: OIDC federation | CI with no stored keys |
| 6 | 5 | Lab 5: data perimeter | Blocked cross-org access log |
| 7 | 6 | P2 build: landing zone | OU tree and guardrails; P2 starts |
| 8 | 7 | Lab 7: static stability game day | Zone-loss evidence |
| 9 | 7 | Lab 8: shuffle sharding simulation | Blast-radius plot; P2 due |
| 10 | 8 | Lab 6: Well-Architected review | Review report |
| 11 | 9 | P3 design review | Diagrams and ADR drafts; P3 starts |
| 12 | 9 | P3 build | Working core path |
| 13 | 10 | P3 DR test and cost estimate | DR evidence |
| 14 | 10 | P3 presentation | Architecture defence |
| 15 | Review and exam | — | Written exam and design oral |

## Working with AI in this course

- **Use AI for:** generating first-draft diagrams-as-code (Mermaid, Diagrams), translating a design between providers ("map this AWS design to Azure and name every service"), explaining an IAM evaluation result, summarising long docs and post-mortems, generating test requests for policy drills, and drafting Well-Architected answers that you then evidence. Named tools: Claude Code, GitHub Copilot, Amazon Q Developer, Gemini Cloud Assist, Azure Copilot.
- **Do without AI (drills):** IAM allow/deny prediction (Lab 4); composite availability arithmetic; drawing a two-AZ VPC from memory; the oral design defence; writing ADRs for your own decisions.
- **Verify AI output by:** testing every generated IAM policy in the policy simulator or with real requests from a second principal; checking each service it names against the provider's regional service list for your India region; asking for the official doc link for every limit it quotes, then opening it; running Access Analyzer or the provider's recommender on its policies.
- **Where AI still fails here (show it):** ask an assistant for a "least-privilege" S3 policy for an app that reads one prefix, then run Access Analyzer: wildcard actions or missing `Condition` keys are common. Ask for India-region designs and check whether every named service exists in Hyderabad or Delhi. Ask it to compare SLAs and verify each number. Record the error rate in a table for your P3 report. Survey data supports caution: only 20% of AI users apply it to deploying or operating production systems ([Stack Overflow blog, October 2026](https://stackoverflow.blog/2026/10/06/the-results-of-the-2026-developer-survey-are-here/)).

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs 1–8 | 25% |
| Projects P1 / P2 / P3 | 5% / 15% / 25% |
| Written exam (IAM evaluation, availability maths, DR selection, framework questions) | 20% |
| Design oral (defend P3 against an examiner) | 10% |

**Mastery gate:** you pass when you can, without AI help, (a) predict correctly the outcome of 10 out of 10 unseen IAM requests on one provider, given the identity, resource, SCP/RCP or equivalent policies; (b) design on a whiteboard, in 45 minutes, a landing zone and a multi-AZ architecture for a brief you have not seen, including composite availability and an RPO/RTO-matched DR pattern; and (c) take an AI-generated architecture for that brief and identify at least three concrete defects with references to official documentation.

## Industry reality

Landing zones, guardrails and least-privilege IAM are the first work a cloud team does in any regulated Indian company, because SEBI's cloud framework (March 2023) requires regulated entities to keep data in MeitY-empanelled providers' data centres and to retain ownership of data, logs and keys. Hyperscalers are investing heavily in Indian capacity: Microsoft announced $17.5 billion for 2026–2029 ([Microsoft, December 2025](https://news.microsoft.com/source/asia/2025/12/09/microsoft-invests-us17-5-billion-in-india-to-drive-ai-diffusion-at-population-scale/)) and opened its fourth India region in Hyderabad in August 2026. Large Indian platforms run at scale on public cloud: Swiggy reports 10 Kubernetes clusters with more than 400 EC2 instances ([Swiggy Bytes](https://bytes.swiggy.com/how-swiggy-migrated-its-k8s-workload-to-graviton-d2643bbc7871)) and Disney+ Hotstar served 59 million concurrent streams ([Hotstar](https://blog.hotstar.com/scaling-infrastructure-for-millions-from-challenges-to-triumphs-part-1-6099141a99ef)). Others, such as PhonePe, run their own data centres ([Business Today, October 2022](https://www.businesstoday.in/latest/corporate/story/phonepe-invests-200-mn-on-data-centres-350429-2022-10-20)), which is why an architect must be able to argue both sides.

Interview questions from this course:

1. **"Design the AWS (or Azure, or GCP) account structure for a 200-person fintech."** Cover OUs or management groups, prod/non-prod separation, security and log-archive accounts, SCP/RCP guardrails, SSO with MFA, break-glass, region restriction for residency, and account vending.
2. **"An app in one AZ is down. Walk me through making it survive an AZ loss."** Cover multi-AZ load balancing, stateless tiers, database failover, static stability (pre-provisioned capacity), health checks, and how you would test it.
3. **"Explain how AWS decides whether this request is allowed."** Cover explicit deny, SCPs, RCPs, resource policies, identity policies, permission boundaries and session policies, cross-account differences, and how you would debug with CloudTrail and the simulator.
4. **"What is the composite availability of this design, and how would you raise it?"** Cover serial versus parallel components, removing dependencies, redundancy at the weakest link, and why a higher SLA number may not be worth its cost.
5. **"Our CI pipeline uses long-lived cloud keys. What do you change?"** Cover OIDC workload identity federation, short-lived credentials, scoping trust conditions to repository and branch, key deletion, and detection of any remaining keys.

## Resources (free first)

- **Frameworks:** [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html), [Azure Well-Architected Framework](https://learn.microsoft.com/en-us/azure/well-architected/), [Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework).
- **Organisation design:** [Organizing Your AWS Environment Using Multiple Accounts](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.html), [Azure landing zones](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/), [Google Cloud resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy).
- **IAM:** [AWS policy evaluation logic](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html), [Resource control policies](https://aws.amazon.com/blogs/aws/introducing-resource-control-policies-rcps-a-new-authorization-policy/), [Azure RBAC overview](https://learn.microsoft.com/en-us/azure/role-based-access-control/overview), [Google Cloud IAM overview](https://docs.cloud.google.com/iam/docs/overview).
- **Reliability:** AWS Builders' Library: [Static stability using Availability Zones](https://aws.amazon.com/builders-library/static-stability-using-availability-zones/), [Workload isolation using shuffle-sharding](https://aws.amazon.com/builders-library/workload-isolation-using-shuffle-sharding/); [Reducing the scope of impact with cell-based architecture](https://docs.aws.amazon.com/wellarchitected/latest/reducing-scope-of-impact-with-cell-based-architecture/reducing-scope-of-impact-with-cell-based-architecture.html).
- **Architecture centres:** [AWS Architecture Center](https://aws.amazon.com/architecture/), [Azure Architecture Center](https://learn.microsoft.com/en-us/azure/architecture/), [Google Cloud Architecture Center](https://docs.cloud.google.com/architecture).
- **Courses:** [AWS Skill Builder](https://skillbuilder.aws/) (free tier), [Microsoft Learn](https://learn.microsoft.com/en-us/training/), [Google Cloud Skills Boost](https://www.cloudskillsboost.google/), NPTEL [Cloud Computing](https://nptel.ac.in/courses/106105167) (IIT Kharagpur).
- **Practising without a big bill:** new AWS accounts since 15 July 2025 get up to $200 in credits on a 6-month free plan ([AWS](https://aws.amazon.com/about-aws/whats-new/2025/07/aws-free-tier-credits-month-free-plan/)); Azure gives $200 for 30 days and Azure for Students $100 with no card ([Azure](https://azure.microsoft.com/en-us/pricing/free-services)); Google Cloud gives $300 for 90 days plus a Free Tier ([Google Cloud](https://docs.cloud.google.com/free/docs/free-cloud-features)). AWS Organizations, IAM, SCPs and the Well-Architected Tool cost nothing. Set a budget alarm before anything else, destroy labs the same day, and never create NAT gateways or load balancers you will not delete.
- **Paid, worth it:** *Fundamentals of Software Architecture* (Richards and Ford, O'Reilly) for trade-off thinking.

## Sources

All checked 12 Oct 2026.
- [Synergy Research Q2 2026 cloud market](https://www.srgresearch.com/articles/q2-cloud-market-passes-143-billion-highest-growth-rate-in-eight-years) (30 Jul 2026).
- [AWS Global Infrastructure: regions and AZs](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/) (39 regions, 124 AZs).
- [Microsoft India South Central region goes live](https://news.microsoft.com/source/asia/features/microsofts-newest-india-datacenter-region-goes-live-to-power-the-countrys-ai-economy-and-enable-frontier-firms/) (6 Aug 2026) and [Azure region pairs](https://learn.microsoft.com/en-us/azure/reliability/regions-paired).
- [Google Cloud regions and zones (Filestore table listing asia-south1 and asia-south2)](https://docs.cloud.google.com/filestore/docs/regions).
- [AWS us-east-1 event summary, 19–20 Oct 2025](https://aws.amazon.com/message/101925/); [Google Cloud incident, 12 Jun 2025](https://status.cloud.google.com/incidents/ow5i3PPK96RduMcb1SsW); [Cloudflare outage, 18 Nov 2025](https://blog.cloudflare.com/18-november-2025-outage/).
- [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) (publication date 6 Nov 2024); [Azure WAF hub](https://learn.microsoft.com/en-us/azure/well-architected/) (11 Sep 2026); [Google Cloud WAF](https://docs.cloud.google.com/architecture/framework) (28 Jan 2026).
- [RCP launch](https://aws.amazon.com/blogs/aws/introducing-resource-control-policies-rcps-a-new-authorization-policy/) (Nov 2024) and [RCP support for DynamoDB](https://aws.amazon.com/about-aws/whats-new/2026/02/aws-expands-resource-control-policies-amazon/) (Feb 2026).
- [Azure default outbound access](https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/default-outbound-access) (private subnets by default after 31 Mar 2026).
- [AWS DevOps Agent GA](https://aws.amazon.com/about-aws/whats-new/2026/03/aws-devops-agent-generally-available) (Mar 2026); [Azure Copilot agents](https://azure.microsoft.com/en-us/blog/announcing-azure-copilot-agents-and-ai-infrastructure-innovations/) (Nov 2025).
- [Stack Overflow 2026 survey results blog](https://stackoverflow.blog/2026/10/06/the-results-of-the-2026-developer-survey-are-here/) (6 Oct 2026).
- [Swiggy: migrating Kubernetes workloads to Graviton](https://bytes.swiggy.com/how-swiggy-migrated-its-k8s-workload-to-graviton-d2643bbc7871); [Disney+ Hotstar: scaling infrastructure for millions, part 1](https://blog.hotstar.com/scaling-infrastructure-for-millions-from-challenges-to-triumphs-part-1-6099141a99ef); [Business Today on PhonePe data centres](https://www.businesstoday.in/latest/corporate/story/phonepe-invests-200-mn-on-data-centres-350429-2022-10-20) (Oct 2022).
- [Microsoft $17.5 billion India investment](https://news.microsoft.com/source/asia/2025/12/09/microsoft-invests-us17-5-billion-in-india-to-drive-ai-diffusion-at-population-scale/) (9 Dec 2025).
- SEBI, *Framework for Adoption of Cloud Services by SEBI Regulated Entities* (March 2023), [sebi.gov.in circulars](https://www.sebi.gov.in/legal/circulars/mar-2023/framework-for-adoption-of-cloud-services-by-sebi-regulated-entities-res-_68740.html).
- Free tiers: [AWS](https://aws.amazon.com/about-aws/whats-new/2025/07/aws-free-tier-credits-month-free-plan/), [Azure](https://azure.microsoft.com/en-us/pricing/free-services), [Google Cloud](https://docs.cloud.google.com/free/docs/free-cloud-features).

_Last reviewed: 2026-10_
