# CLD501 · Frontier Seminar: Sovereign Cloud, Confidential Computing and Planet-Scale Infrastructure

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 5 · 9 | 4 (≈ 120 hours) | L4 → L5 | [CLD401](../../year_4/CLD401_serverless_and_event_driven_cloud/README.md), [CLD403](../../year_4/CLD403_finops_and_cloud_cost_engineering/README.md) | [RES502](../../../../05_shared_years_3_to_5/RES502_reading_reproducing_and_extending_papers/README.md), [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md), [THS502](../../../../05_shared_years_3_to_5/THS502_thesis_or_capstone_ii/README.md) |

Part of the [Cloud Engineering major](../../README.md). Taken alongside [RES501 Research Methods](../../../../05_shared_years_3_to_5/RES501_research_methods_and_scientific_writing/README.md). Builds on every earlier CLD course, especially [CLD404](../../year_4/CLD404_ai_infrastructure_in_the_cloud_gpus_inference/README.md) for AI infrastructure. Cloud security architecture as a practice is taught in [SAR401](../../../security_architecture/year_4/SAR401_cloud_security_architecture/README.md); this seminar studies the frontier questions that will shape cloud platforms over the next decade.

## Why this course matters now

Three forces are reshaping the cloud at once. **Sovereignty:** governments want control over where data lives and who can reach it. AWS opened an independent European Sovereign Cloud in Brandenburg in January 2026 ([Amazon](https://press.aboutamazon.com/aws/2026/1/aws-launches-aws-european-sovereign-cloud-and-announces-expansion-across-europe)), Microsoft announced sovereign public and private cloud offerings in June 2025 ([Microsoft](https://blogs.microsoft.com/blog/2025/06/16/announcing-comprehensive-sovereign-solutions-empowering-european-organizations/)), and India notified its Digital Personal Data Protection Rules in November 2025 with most duties phased in over 18 months. **Confidentiality:** customers increasingly want proof that even the provider cannot see their data or models, which hardware trusted execution environments and attestation now make possible for CPUs and GPUs. **Scale and energy:** the IEA estimates data centres used about 415 TWh of electricity in 2024 (around 1.5% of global consumption) and projects about 945 TWh by 2030, with AI the main driver ([IEA, April 2025](https://www.iea.org/reports/energy-and-ai/executive-summary)).

None of these have settled answers, and AI tools are weakest exactly where answers are unsettled: they summarise yesterday's documentation confidently. This seminar trains you to read primary sources (papers, regulations, post-mortems, attestation specifications), reproduce measurements, and produce original work: the step from expert practitioner (L4) to someone who creates new knowledge (L5).

## Learning outcomes

By the end you can:

1. **Read and critique** systems papers on planet-scale infrastructure (cluster management, storage, networks, isolation) and **explain** which ideas transferred into public cloud products.
2. **Analyse** large outages as research data and **identify** recurring failure classes (metastable failures, configuration propagation, hidden control-plane dependencies).
3. **Distinguish** data residency, data sovereignty and operational sovereignty, and **map** Indian, EU and sector rules onto concrete architecture requirements.
4. **Explain** trusted execution environments (Intel TDX, AMD SEV-SNP, Arm CCA, NVIDIA confidential GPUs), remote attestation and their threat models and limits.
5. **Measure** and **report** the energy and carbon of cloud workloads using the Software Carbon Intensity standard (ISO/IEC 21031:2024), and **design** carbon-aware scheduling.
6. **Reproduce** a published result or measurement on cloud infrastructure and **report** deviations honestly.
7. **Write** a research proposal and a short paper in workshop format, and **present** it for critique.

## Chapters and lessons

### Chapter 1 · How to do research on cloud systems (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Reading a systems paper | Problem, insight, design, evaluation, limits; three-pass reading | Read the Borg paper and write a one-page critique |
| 1.2 Measuring the cloud | Variance between runs, noisy neighbours, regions and instance generations; reporting medians and intervals | Measure the same benchmark on 5 instances and report variance properly |
| 1.3 Ethics and safety | Responsible disclosure, terms of service for testing, never probing other tenants | Write the ethics section of your project proposal |

**Check your understanding:** (1) Why is a single cloud benchmark run not evidence? (2) What does a paper's evaluation usually leave out? (3) What testing is off-limits on shared infrastructure?

### Chapter 2 · Planet-scale compute (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Cluster managers | Borg (EuroSys 2015), the Borg–Omega–Kubernetes lineage (ACM Queue 2016), Meta's Twine (OSDI 2020) | Present one paper and map its ideas to Kubernetes features |
| 2.2 Isolation at scale | Firecracker microVMs (NSDI 2020), gVisor; isolation for AI-generated code (Lambda MicroVMs, June 2026) | Measure microVM boot time and memory overhead with Firecracker on a bare-metal or nested-virtualisation host |
| 2.3 Tail latency | "The Tail at Scale" (CACM 2013): hedged requests, tied requests | Reproduce tail amplification with a fan-out simulation |

**Check your understanding:** (1) Which Borg idea did Kubernetes deliberately not copy, and why? (2) Why do microVMs suit multi-tenant functions? (3) Why does fan-out make tail latency dominate?

### Chapter 3 · Planet-scale data (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Global databases | Spanner (OSDI 2012), Aurora (SIGMOD 2017), DynamoDB (USENIX ATC 2022) | Compare their consistency and failure models in a table |
| 3.2 Cell-based control planes | "Millions of tiny databases" (Physalia, NSDI 2020), cells, shuffle sharding, static stability | Design a cell-based control plane for a regional service |
| 3.3 From papers to products | Aurora DSQL and DynamoDB multi-Region strong consistency (2025) as descendants of research ideas | Trace one product feature back to its research roots |

**Check your understanding:** (1) What problem did Physalia solve that a single consensus group could not? (2) Why does Aurora ship logs instead of pages? (3) What did DynamoDB's paper say about predictability versus raw speed?

### Chapter 4 · Planet-scale networks and AI supercomputers (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Data-centre networks | Jupiter Rising (SIGCOMM 2015) and Jupiter Evolving with optical circuit switches (SIGCOMM 2022) | Present the shift from Clos fabrics to OCS |
| 4.2 AI supercomputers | TPU v4 with optical interconnect (ISCA 2023), Ironwood's 9,216-chip superpods, Meta's RoCE training networks (SIGCOMM 2024) | Compare the three designs' failure domains |
| 4.3 Limits | Power, cooling, failure rates (Llama 3's interruption data), supply chains | Estimate power for a 100,000-GPU cluster from public specs |

**Check your understanding:** (1) Why do optical circuit switches suit AI traffic? (2) What sets the size of a scale-up domain? (3) Which resource will limit AI clusters first: chips, power or network?

### Chapter 5 · Outages as research data (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Failure classes | Metastable failures (HotOS 2021), retry storms, configuration propagation, control-plane dependencies | Classify 10 public post-mortems |
| 5.2 Three recent case studies | AWS us-east-1 (October 2025, DynamoDB DNS automation race), Google Cloud (June 2025, policy with blank fields), Cloudflare (November 2025, oversized generated file) | Write a comparative analysis with one shared root pattern |
| 5.3 Verification and simulation | Formal methods at AWS (CACM 2015), deterministic simulation, staged rollouts | Propose a verification method that would have caught one of the three |

**Check your understanding:** (1) What makes a failure metastable? (2) Why do global configuration systems need the same rollout discipline as code? (3) What is a hidden control-plane dependency?

### Chapter 6 · Sovereign cloud: concepts and Europe (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Definitions | Residency (where data is), sovereignty (whose law applies), operational sovereignty (who can operate and access), the US CLOUD Act debate | Classify five offerings on the three axes |
| 6.2 European offerings | AWS European Sovereign Cloud (GA January 2026, separate partition, more than €7.8 billion planned in Germany), Microsoft Sovereign Cloud (public, private on Azure Local, national partner clouds), Google's sovereign and air-gapped offerings | Compare architecture and operating models from primary sources |
| 6.3 Regulation | EU Data Act switching rules (charges abolished from 12 January 2027); EU cloud certification schemes (status: check before citing) | Write a one-page brief on what the Data Act changes for architects |

**Check your understanding:** (1) Does data in a local region guarantee sovereignty? (2) What does a separate partition change technically? (3) Why might sovereign clouds lag in features?

### Chapter 7 · Sovereignty and data rules in India (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 DPDP Act 2023 and Rules 2025 | Data fiduciaries, consent, breach intimation, significant data fiduciaries, cross-border transfer (permitted unless restricted by notification); phased commencement to about May 2027 | Map DPDP duties onto a cloud architecture's data flows |
| 7.2 Sector rules | RBI's 2018 payment-data localisation; CERT-In's April 2022 directions (incident reports within 6 hours, 180-day log retention); SEBI's 2023 cloud framework (MeitY-empanelled providers, ownership of data, logs and keys) | Build a compliance matrix for a fintech's cloud estate |
| 7.3 National compute | MeitY empanelment, government cloud, IndiaAI compute (38,000 GPUs, plus a planned secure national cluster of 3,000 GPUs), hyperscaler investments in Indian regions | Write a policy brief: what would "sovereign AI compute" mean technically for India? |

**Check your understanding:** (1) Which Indian rule constrains backups most? (2) Why does a 6-hour reporting rule change monitoring design? (3) What would make a cloud "sovereign" for Indian public-sector AI?

### Chapter 8 · Confidential computing I: hardware and attestation (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Threat models | Protecting data in use from the host OS, hypervisor and operators; what TEEs do not protect (side channels, the code inside) | Write a threat model for a confidential ML inference service |
| 8.2 CPU TEEs | Intel SGX and TDX, AMD SEV-SNP, Arm CCA; memory encryption and integrity | Compare the three on trust boundary and performance overhead from published data |
| 8.3 Attestation | Measured boot, attestation reports, verifiers, key release on successful attestation | Run a confidential VM and verify its attestation report |
| 8.4 Research frontier | Published side-channel and physical memory-bus attacks on TEEs (study the papers and vendor advisories only; never attempt them on real systems), formal verification of attestation flows | Present one attack paper's threat model and the mitigations, without reproducing the attack |

**Check your understanding:** (1) Why is attestation the heart of confidential computing? (2) What does a TEE not protect against? (3) Why does key release depend on attestation?

### Chapter 9 · Confidential computing II: cloud and AI (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Cloud offerings | AWS Nitro System (no operator access by design, assessed by NCC Group) and Nitro Enclaves; Azure confidential VMs and containers; Google Confidential VMs, Confidential GKE nodes and Confidential Space | Deploy a workload that releases a key only to an attested enclave or confidential VM |
| 9.2 Confidential GPUs | NVIDIA Hopper and Blackwell confidential computing modes, GPU attestation, performance cost | Read the vendor architecture paper and summarise limits |
| 9.3 Verifiable AI privacy | Apple Private Cloud Compute (2024) as a design for verifiable server-side privacy; confidential inference for regulated data | Critique PCC's design claims in writing |

**Check your understanding:** (1) What is the difference between "no operator access by design" and a hardware TEE? (2) Why is GPU confidentiality harder than CPU confidentiality? (3) What would convince a bank regulator that a provider cannot see model inputs?

### Chapter 10 · Sustainability I: energy and carbon accounting (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 The energy picture | IEA's 2024 baseline and 2030 projection; PUE and WUE; where AI changes the curve | Reconcile three public estimates of data-centre energy and explain gaps |
| 10.2 Carbon accounting | Scopes 1–3, location-based versus market-based emissions, embodied carbon, provider carbon tools and their lags | Compare provider carbon reports for the same workload |
| 10.3 Software Carbon Intensity | SCI formula (energy × grid intensity + embodied, per functional unit), ISO/IEC 21031:2024 | Compute an SCI score for your CLD404 inference service |

**Check your understanding:** (1) Why can a "100% renewable" claim coexist with high location-based emissions? (2) Why is the functional unit the most important SCI choice? (3) What does embodied carbon mean for GPU refresh cycles?

### Chapter 11 · Sustainability II: carbon-aware computing (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Shifting in time and space | Carbon-intelligent computing at Google (2021 paper), grid-intensity signals (Electricity Maps, India's CEA CO2 baseline data), Green Software Foundation Carbon Aware SDK | Schedule a batch job by forecast carbon intensity and measure the saving |
| 11.2 Measuring energy | Kepler (Kubernetes energy estimates), RAPL, GPU power telemetry; accuracy limits | Compare Kepler estimates with GPU power readings |
| 11.3 Trade-offs | Carbon versus latency, cost and residency; rebound effects | Write the trade-off section of your project |

**Check your understanding:** (1) Why does time-shifting help more in some grids than others? (2) What residency rule might block location-shifting in India? (3) Why are software energy estimates uncertain?

### Chapter 12 · Emerging directions (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Autonomous operations | AI agents that investigate and remediate (AWS DevOps Agent GA March 2026), safety cases for autonomous infrastructure | Write a safety case for an agent allowed to roll back deployments |
| 12.2 New hardware and places | Memory disaggregation (CXL), rack-scale systems, space-based compute research (Google's Project Suncatcher, November 2025) | Present one proposal and its open problems |
| 12.3 What will the cloud look like in 2035? | Structured debate with evidence | Two-page position paper |

**Check your understanding:** (1) What evidence would justify giving an agent write access to production? (2) Which constraint does space-based compute address, and which does it worsen? (3) Which of today's frontier topics is most likely to become a default product feature?

### Chapter 13 · Research project (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 13.1 Writing | Workshop-paper structure, figures, threats to validity, artefact appendix | Draft and peer-review |
| 13.2 Presenting | 15-minute talk, handling hostile questions | Final presentation |

**Check your understanding:** (1) What is your paper's one claim? (2) What would falsify it? (3) What did you not measure?

## Weekly rhythm

| Week | Chapter | Seminar activity | Deliverable |
|---|---|---|---|
| 1 | 1 | Paper-reading workshop | Borg critique; project ideas |
| 2 | 2 | Presentations: Borg, Twine, Firecracker | Microbenchmark |
| 3 | 3 | Presentations: Spanner, Aurora, DynamoDB, Physalia | Comparison table; proposal draft |
| 4 | 4 | Presentations: Jupiter, TPU v4, RoCE | Power estimate; P1 due |
| 5 | 5 | Outage analysis workshop | Comparative analysis |
| 6 | 6 | Sovereignty debate (Europe) | Brief |
| 7 | 7 | India regulation workshop | Compliance matrix; P2 starts |
| 8 | 8 | TEE lab and attack-paper presentation | Attestation verified |
| 9 | 9 | Confidential AI | Key-release demo; P2 due |
| 10 | 10 | Carbon accounting | SCI score |
| 11 | 11 | Carbon-aware scheduling | Measured saving; P3 milestone |
| 12 | 12 | Futures debate | Position paper |
| 13 | 13 | Paper drafts and peer review | Draft |
| 14 | 13 | Mini-conference | Final paper and talk |
| 15 | Review | — | Oral examination on readings |

## Working with AI in this course

- **Use AI for:** first-pass summaries of papers and regulations (always followed by your own reading of the primary text), finding related work (then verifying each citation exists and says what is claimed), drafting simulation code, and critiquing your drafts as a hostile reviewer. Named tools: Claude, ChatGPT, Gemini, Semantic Scholar, Elicit.
- **Do without AI (drills):** the three-pass reading of each assigned paper, your presentation slides' claims, the oral examination, and the threat model in Chapter 8.
- **Verify AI output by:** opening every cited paper, regulation and post-mortem; checking quoted numbers against the source; re-running any analysis code on your own data; asking whether a regulation summary reflects the notified text and its commencement date.
- **Where AI still fails here (show it):** assistants misstate commencement dates of the DPDP Rules, invent paper titles and numbers, conflate residency with sovereignty, and overstate what TEEs protect. Keep a log of every such error you find during the seminar and include it as an appendix to your paper.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Paper presentations and critiques | 20% |
| Projects P1 / P2 / P3 | 10% / 15% / 35% |
| Oral examination on the readings | 20% |

**Mastery gate:** you pass when you (a) present one assigned paper and survive 15 minutes of questions on its design and evaluation; (b) produce a reproducible measurement or reproduction study, with artefacts, that a classmate can rerun from your instructions and get results within your stated error bounds; and (c) write a workshop-format paper (6–8 pages) that states a falsifiable claim, evaluates it honestly, and is judged by two reviewers as ready to submit to a workshop or student research track.

## Industry reality

Sovereign-cloud architects, confidential-computing engineers and sustainability engineers are emerging specialisms at hyperscalers, regulated enterprises and governments. In India, the DPDP Rules, CERT-In directions, SEBI's cloud framework and IndiaAI's national compute programme create demand for engineers who can turn legal text into architecture. Research labs and cloud providers hire people who can read and reproduce systems papers.

Interview questions from this course:

1. **"A government client wants a 'sovereign' AI platform. What do you ask, and what do you build?"** Cover residency versus sovereignty versus operational control, applicable law, key ownership, operator access, attestation, supply chain, air-gapped options and feature trade-offs.
2. **"How would you prove to an auditor that our cloud provider cannot read our model inputs?"** Cover confidential VMs or GPUs, attestation-gated key release, threat model limits, logging, and independent assessments.
3. **"Explain a metastable failure and how you would prevent one."** Cover sustaining effects such as retry storms and cache misses, load shedding, retry budgets, and testing beyond normal load.
4. **"How would you reduce the carbon of our batch platform without breaking SLAs?"** Cover measurement, SCI, time and location shifting within residency rules, rightsizing, and reporting honestly.
5. **"Pick a systems paper you admire and tell me what it got wrong."** Cover the paper's claims, evaluation gaps, what changed since, and how you would test it today.

## Resources (free first)

- **Planet-scale papers:** [Borg](https://research.google/pubs/large-scale-cluster-management-at-google-with-borg/) (EuroSys 2015); [Borg, Omega, and Kubernetes](https://queue.acm.org/detail.cfm?id=2898444) (2016); [Twine](https://www.usenix.org/conference/osdi20/presentation/tang) (OSDI 2020); [Firecracker](https://www.usenix.org/conference/nsdi20/presentation/agache) (NSDI 2020); [The Tail at Scale](https://research.google/pubs/the-tail-at-scale/) (CACM 2013); [Spanner](https://www.usenix.org/conference/osdi12/technical-sessions/presentation/corbett) (OSDI 2012); [Amazon Aurora](https://www.amazon.science/publications/amazon-aurora-design-considerations-for-high-throughput-cloud-native-relational-databases) (SIGMOD 2017); [Amazon DynamoDB](https://www.usenix.org/conference/atc22/presentation/elhemali) (ATC 2022); [Millions of Tiny Databases](https://www.usenix.org/conference/nsdi20/presentation/brooker) (NSDI 2020); [Jupiter Rising](https://research.google/pubs/jupiter-rising-a-decade-of-clos-topologies-and-centralized-control-in-googles-datacenter-network/) (SIGCOMM 2015); [Jupiter Evolving](https://research.google/pubs/jupiter-evolving-transforming-googles-datacenter-network-via-optical-circuit-switches-and-software-defined-networking/) (SIGCOMM 2022); [TPU v4](https://arxiv.org/abs/2304.01433) (ISCA 2023); [Metastable Failures in Distributed Systems](https://sigops.org/s/conferences/hotos/2021/papers/hotos21-s11-bronson.pdf) (HotOS 2021); [How Amazon Web Services uses formal methods](https://www.amazon.science/publications/how-amazon-web-services-uses-formal-methods) (CACM 2015).
- **Confidential computing:** [Confidential Computing Consortium](https://confidentialcomputing.io/); [The Security Design of the AWS Nitro System](https://docs.aws.amazon.com/whitepapers/latest/security-design-of-aws-nitro-system/security-design-of-aws-nitro-system.html); [Azure confidential computing](https://learn.microsoft.com/en-us/azure/confidential-computing/overview); [Google Confidential Computing](https://cloud.google.com/security/products/confidential-computing); [Apple Private Cloud Compute](https://security.apple.com/blog/private-cloud-compute/).
- **Sovereignty and law:** [PIB: DPDP Rules notified](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2190014) (14 Nov 2025) and [the DPDP Rules, 2025 (MeitY PDF)](https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf); [CERT-In directions, April 2022](https://www.cert-in.org.in/PDF/CERT-In_Directions_70B_28.04.2022.pdf); [RBI payment-data storage](https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11244); [EU Data Act](https://eur-lex.europa.eu/eli/reg/2023/2854/oj); [Overview of the AWS European Sovereign Cloud](https://docs.aws.amazon.com/whitepapers/latest/overview-aws-european-sovereign-cloud/introduction.html).
- **Sustainability:** [IEA Energy and AI](https://www.iea.org/reports/energy-and-ai/executive-summary); [Software Carbon Intensity specification](https://sci.greensoftware.foundation/); [Carbon Aware SDK](https://github.com/Green-Software-Foundation/carbon-aware-sdk); [Kepler](https://github.com/sustainable-computing-io/kepler); [Carbon-aware computing for datacenters](https://arxiv.org/abs/2106.11750) (Google, 2021); the CO2 Baseline Database for the Indian Power Sector, published yearly by the [Central Electricity Authority](https://cea.nic.in/) (version 22.0, August 2026).
- **Frontier:** [Exploring a space-based, scalable AI infrastructure system design](https://research.google/blog/exploring-a-space-based-scalable-ai-infrastructure-system-design/) (Google Research, 4 Nov 2025).
- **Practising without a big bill:** most work is reading and analysis. Confidential VMs, Firecracker experiments and carbon-aware scheduling run on small instances for short sessions; use providers' free tiers and credits, and university or IndiaAI research compute for anything larger.

## Sources

All checked 12 Oct 2026.
- [AWS launches the AWS European Sovereign Cloud](https://press.aboutamazon.com/aws/2026/1/aws-launches-aws-european-sovereign-cloud-and-announces-expansion-across-europe) (15 Jan 2026).
- [Microsoft sovereign solutions for Europe](https://blogs.microsoft.com/blog/2025/06/16/announcing-comprehensive-sovereign-solutions-empowering-european-organizations/) (16 Jun 2025) and [February 2026 update](https://blogs.microsoft.com/blog/2026/02/24/microsoft-sovereign-cloud-adds-governance-productivity-and-support-for-large-ai-models-securely-running-even-when-completely-disconnected/).
- [PIB: Government notifies DPDP Rules](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2190014) (14 Nov 2025; 18-month phased compliance timeline); [DPDP Rules, 2025 text](https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf); phase-by-phase summary by [Hogan Lovells](https://www.hoganlovells.com/en/publications/indias-digital-personal-data-protection-act-2023-brought-into-force-).
- [CERT-In directions under section 70B](https://www.cert-in.org.in/PDF/CERT-In_Directions_70B_28.04.2022.pdf) (28 Apr 2022).
- [PIB explainer on IndiaAI compute](https://static.pib.gov.in/WriteReadData/specificdocs/documents/2026/feb/doc2026210784401.pdf) (Feb 2026).
- [IEA Energy and AI, executive summary](https://www.iea.org/reports/energy-and-ai/executive-summary) (Apr 2025).
- [AWS Nitro System independent affirmation](https://aws.amazon.com/blogs/compute/aws-nitro-system-gets-independent-affirmation-of-its-confidential-compute-capabilities/) (NCC Group review).
- [AWS DevOps Agent GA](https://aws.amazon.com/about-aws/whats-new/2026/03/aws-devops-agent-generally-available) (Mar 2026); [Lambda MicroVMs](https://aws.amazon.com/about-aws/whats-new/2026/06/aws-lambda-microvms) (Jun 2026).
- [AWS us-east-1 event](https://aws.amazon.com/message/101925/); [Google Cloud incident](https://status.cloud.google.com/incidents/ow5i3PPK96RduMcb1SsW); [Cloudflare outage](https://blog.cloudflare.com/18-november-2025-outage/).
- [Google Research: Project Suncatcher](https://research.google/blog/exploring-a-space-based-scalable-ai-infrastructure-system-design/) (4 Nov 2025).

_Last reviewed: 2026-10_
