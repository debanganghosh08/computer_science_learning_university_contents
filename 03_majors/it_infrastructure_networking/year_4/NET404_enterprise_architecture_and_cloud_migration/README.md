# NET404 · Enterprise Architecture and Cloud Migration

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 8 | 4 (≈ 120 hours) | L2 → L4 | [NET304](../../year_3/NET304_wireless_sd_wan_and_enterprise_networks/README.md); [NET401](../NET401_data_center_and_hybrid_infrastructure/README.md) and [NET305](../../year_3/NET305_it_service_management_and_operations/README.md) recommended | [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md), [LCH502](../../../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md); companion to [CLD402](../../../cloud_engineering/year_4/CLD402_multi_cloud_hybrid_cloud_and_migration/README.md) |

CLD402 teaches the cloud engineer's side of migration (migration factories, rehosting, data migration, replatforming). This course teaches the architect's side, from the estate you already run: what the organisation has, what it should keep, move, replace or retire, how the network, identity and security must change, what it costs, what the regulations require, and how to lead the decision.

## Why this course matters now

The US Bureau of Labor Statistics projects computer network architect jobs to grow 8% between 2025 and 2035, against a 4% decline for administrators, citing new and upgraded networks, AI-driven infrastructure modernisation and the continued expansion of cloud computing. The median US architect earned about $35,000 more than the median administrator in May 2025. The decisions architects face have become harder. Broadcom's VMware licensing changes forced many enterprises to rethink their whole platform at once; Network World reported in June 2026 that most customers are shrinking their VMware estates but few have finished, and a Gartner analyst put the untangling at two to four years for large enterprises. Cloud is no longer automatically cheaper: Flexera's 2026 survey estimated 29% of IaaS and PaaS spend as wasted. In India, regulation now shapes architecture directly: the RBI's 2018 payment-data storage rule, its 2023 IT governance directions, CERT-In's 2022 log-retention directions, and the Digital Personal Data Protection Rules notified in November 2025 with obligations phasing in through 2027. AI agents now generate migration assessments and plans (AWS Transform, Azure Copilot agents), but they work from whatever inventory they are given. The architect who can find the real dependencies, build an honest business case, design the hybrid network and persuade a board is the hardest person in IT to replace.

## Learning outcomes

By the end you can:

1. **Explain** what enterprise, solution and infrastructure architects do, and **apply** a lightweight TOGAF ADM cycle to a real problem without drowning in documents.
2. **Model** an organisation's capabilities, applications and technology in ArchiMate, and **produce** views that different stakeholders understand.
3. **Rationalise** an application portfolio using business value, technical fitness, cost and risk, and **assign** a disposition (tolerate, invest, migrate, eliminate; retain, retire, rehost, replatform, repurchase, refactor) to each application with reasons.
4. **Discover** dependencies from flow data, discovery tools and interviews, and **group** applications into safe migration waves.
5. **Design** the target hybrid network: address plan without overlaps, DNS, identity, connectivity, inspection and segmentation across on-premises and multiple clouds.
6. **Build** a TCO model and business case with sensitivity analysis, and **defend** its assumptions.
7. **Map** Indian regulatory requirements (RBI, CERT-In, DPDP, sector rules) to architecture decisions and exit plans.
8. **Write** a roadmap with transition architectures and decision points, and **run** architecture governance with decision records.
9. **Evaluate** AI-generated assessments and plans against discovery evidence.

## Chapters and lessons

### Chapter 1 · What architecture is for (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Kinds of architect | Enterprise, solution, infrastructure, network and security architects; what each decides | Interview (or read job descriptions for) 3 architects; map their decisions |
| 1.2 Why EA fails | Ivory-tower diagrams, frameworks as goals, no link to budgets; what useful EA produces (decisions, roadmaps, standards) | List 5 symptoms of EA failure and the fix for each |
| 1.3 Architecture as decisions | Quality attributes, trade-offs, constraints, assumptions | Rewrite a vague architecture statement as explicit decisions |
| 1.4 The case organisation | Introduce the semester's case: a mid-sized Indian company with two data centres, 60 branches and 250 applications (illustrative) | Read the case pack and list the 10 questions you must answer |

**Check your understanding:** Why should an architecture document start with decisions rather than diagrams? What makes an enterprise architect useful to a CFO? Which of your case questions can only be answered with data, not interviews?

### Chapter 2 · TOGAF-lite and ArchiMate (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 The ADM cycle | Preliminary, vision, business, information systems, technology, opportunities and solutions, migration planning, implementation governance, change management (TOGAF Standard, 10th Edition) | Map the case to ADM phases; decide which to do lightly |
| 2.2 ArchiMate | Business, application and technology layers; key elements and relationships; viewpoints | Model one business process down to the servers it runs on |
| 2.3 Tools | Archi (free, open source), diagrams as code; keeping models current from CMDB data | Import CMDB data into Archi for one domain |
| 2.4 Just enough | Choosing artefacts by audience; one-page views | Produce three views of the same thing for a CIO, an engineer and an auditor |

**Check your understanding:** Why do teams that try to complete every TOGAF artefact rarely finish? What does a layered ArchiMate model show that a network diagram cannot? Why must an architecture model be fed from operational data?

### Chapter 3 · Capabilities and the current state (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Capability maps | Business capabilities vs organisation charts; heat-mapping by importance and health | Build a capability map for the case with a heat map |
| 3.2 Current-state discovery | CMDB data (NET305), cloud inventories, licence records, interviews | Assemble the current-state inventory from the case data |
| 3.3 Technical debt | End-of-support systems, unsupported hypervisors, manual processes; a debt register with cost of delay | Build a debt register of 15 items with owners |
| 3.4 Data quality | How wrong inventories derail migrations; reconciliation | Find 10 contradictions between case data sources |

**Check your understanding:** Why map capabilities rather than departments? What is "cost of delay" for a piece of technical debt? Why do inventory errors cause the most expensive migration surprises?

### Chapter 4 · Application portfolio rationalisation (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Assessment attributes | Business value, technical fitness, total cost, risk, user base, data classification | Score 40 case applications on 6 attributes |
| 4.2 TIME and the Rs | Tolerate, invest, migrate, eliminate; retain, retire, rehost, relocate, replatform, repurchase, refactor | Assign a disposition to each of the 40 with one-line reasons |
| 4.3 SaaS and consolidation | Replacing custom apps with SaaS; consolidation after mergers; contract timing | Find 5 consolidation candidates and their savings |
| 4.4 Decommissioning | Retiring applications: data retention, access for audits, licence termination | Write a retirement plan for one application with legal retention needs |

**Check your understanding:** Why is "retire" the cheapest migration? When is rehosting the right answer even though it changes nothing? Why does data classification change an application's disposition?

### Chapter 5 · Dependencies and migration waves (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Flow-based discovery | NetFlow/IPFIX and firewall logs from NET303 and NET403 to find who talks to whom | Build a dependency graph from a week of case flow data |
| 5.2 Agent-based and tool discovery | Discovery agents, cloud migration assessment tools, their blind spots (batch jobs, quarterly reports) | Compare tool output with flow data; list what each missed |
| 5.3 Move groups | Grouping by dependency and latency sensitivity; shared databases; "chatty" pairs | Group 40 applications into waves with rules you can explain |
| 5.4 Firewall archaeology | Old rules as dependency evidence; translating rules into cloud security groups or firewalls | Convert 30 legacy rules into a target policy, removing dead ones |

**Check your understanding:** Why does one week of flow data miss month-end dependencies? What happens if two chatty applications land in different regions? Why are old firewall rules both evidence and liability?

### Chapter 6 · Target hybrid architecture (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Landing zones | Account and subscription structure, hub-and-spoke vs cloud WAN services, shared services (see [CLD301](../../../cloud_engineering/year_3/CLD301_cloud_architecture_on_aws_azure_and_google_cloud/README.md), [CLD304](../../../cloud_engineering/year_3/CLD304_cloud_networking_vpcs_dns_load_balancing/README.md)) | Choose a landing-zone pattern for the case with reasons |
| 6.2 Address plan and DNS | One address plan across data centres, branches and clouds with no overlaps; hybrid DNS resolution | Extend the NET301 plan to two clouds; resolve names both ways |
| 6.3 Connectivity | Interconnect sizing, redundancy and cost (NET401), SD-WAN cloud on-ramps (NET304), egress paths | Size and diagram connectivity for wave 1 and the end state |
| 6.4 Identity and security | Entra ID or other identity as the control plane (NET302), inspection points, segmentation carried into cloud (NET402) | Place inspection and segmentation controls on the target diagram |

**Check your understanding:** Why must the address plan be fixed before the first workload moves? What breaks when on-premises clients cannot resolve cloud private names? Where should traffic be inspected, and what does each choice cost?

### Chapter 7 · Cost and the business case (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 On-premises TCO | Hardware refresh, power and space, licences (including hypervisor changes), support contracts, staff time | Build the current-state TCO for the case |
| 7.2 Cloud cost models | On-demand, commitments and savings plans, licence portability, egress, managed-service premiums; FinOps practices (see [CLD403](../../../cloud_engineering/year_4/CLD403_finops_and_cloud_cost_engineering/README.md)) | Model wave-1 cloud cost with public price lists |
| 7.3 The business case | 5-year cash flows, NPV basics, migration costs, double-running costs, benefits you can measure | Write a business case with three options |
| 7.4 Sensitivity | Which assumptions change the answer (utilisation, egress, discount, staff); tornado charts | Show which 3 assumptions flip the decision |

**Check your understanding:** Why does double running during migration often decide the business case? Why is "cloud is cheaper" an incomplete sentence? Which cost does an AI-generated estimate most often leave out?

### Chapter 8 · Risk, regulation and sovereignty in India (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Data protection | Digital Personal Data Protection Act 2023 and Rules notified November 2025 (phased obligations), data mapping, processors and cross-border questions | Build a data map for 10 case applications |
| 8.2 Financial-sector rules | RBI storage of payment system data (April 2018), RBI IT governance directions (2023), outsourcing and cloud expectations; SEBI's March 2023 cloud framework, which requires MeitY-empanelled cloud infrastructure | Mark which case applications are constrained and how |
| 8.3 Security and logging duties | CERT-In directions: 6-hour reporting, 180-day logs within India, NTP; government cloud empanelment by MeitY for public-sector workloads | Check the target design for log location and time sources |
| 8.4 Lock-in and exit | Exit plans, data portability, concentration risk, multi-cloud honestly (see CLD402) | Write an exit plan for one critical SaaS and one cloud platform |

**Check your understanding:** Why does data residency affect the network and logging design, not only storage? What makes an exit plan credible? Why is concentration risk a board-level topic for regulated entities?

### Chapter 9 · Roadmaps and transition architectures (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Transition states | Baseline, transition architectures, target; what must be true at each step | Draw 3 transition states for the case |
| 9.2 The roadmap | Waves, dependencies, decision points, capacity of teams, freeze periods | Build an 18-month roadmap with decision gates |
| 9.3 Coexistence | Running hybrid for years: operations, monitoring and support during the middle state | Design monitoring and support for the hybrid period |
| 9.4 Data-centre exit | Contracts, hardware disposal, data sanitisation (NIST SP 800-88), staff transition | Write a DC-exit checklist with owners and dates |

**Check your understanding:** Why do migrations stall in the middle? What should a decision gate decide, and with what evidence? Why is data sanitisation an architecture concern?

### Chapter 10 · Governance and decision records (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Principles and standards | Architecture principles that decide things; technology standards and a technology radar | Write 8 principles and test each against a real decision |
| 10.2 Decision records | Architecture decision records (ADRs): context, options, decision, consequences | Write 5 ADRs for the case |
| 10.3 Review boards that help | Lightweight review, exceptions with expiry, measuring time to decision | Redesign an architecture review process for speed |
| 10.4 Measuring EA value | Fewer platforms, retired applications, cost avoided, risk reduced, time to deliver | Define 5 EA metrics for the case |

**Check your understanding:** What makes a principle useful rather than decorative? Why record rejected options in an ADR? How can an architecture board slow delivery, and how do you prevent it?

### Chapter 11 · AI in architecture and migration (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 What tools do | AI agents for migration assessment and planning (AWS Transform, Azure Copilot migration agent), LLM summaries of portfolios and documents | Run an assistant over the case inventory and get a disposition for each app |
| 11.2 Checking the output | Compare AI dispositions and dependency claims with your flow data and scoring; classify errors | Score the assistant's 40 dispositions against yours and justify disagreements |
| 11.3 Cost and regulatory claims | Outdated prices, invented regulatory requirements, missing egress or double-running costs | Verify 10 cost or regulatory claims against primary sources |
| 11.4 Using AI well | Drafting ADRs, summarising interviews, generating options you then evaluate | Use AI to draft 2 ADRs; record your edits |

**Check your understanding:** Why can an AI assessment be no better than the inventory it reads? Which AI error would cost the most in the case? When does AI save real architect time?

### Chapter 12 · Communicating and defending architecture (weeks 12–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 One-page architecture | The diagram and text a CEO reads; the appendix an engineer reads | Produce the one-pager for your P3 |
| 12.2 Presenting trade-offs | Options, risks, costs, recommendation; handling hostile questions | Rehearse a 15-minute board presentation |
| 12.3 Stakeholders | Business owners, finance, security, operations, vendors; what each needs | Map stakeholders and their concerns for the case |
| 12.4 Capstone defence | Defending P3 to a panel acting as a board | Final presentation and Q&A |

**Check your understanding:** Why should a recommendation state what would change your mind? What does a CFO need to hear that an engineer does not? Which question in rehearsal exposed a gap in your evidence?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Case analysis | Question list |
| 2 | 2 | Lab 2 · ArchiMate model in Archi | — |
| 3 | 3 | Lab 3 · Capability map and debt register | **P1 due** |
| 4 | 4 | Lab 4 · Portfolio scoring and dispositions | — |
| 5 | 5 | Lab 5 · Dependency graph and waves | — |
| 6 | 6 | Lab 6 · Target hybrid network design | Mid-term (AI off) |
| 7 | 7 | Lab 7 · TCO and business case | — |
| 8 | 8 | Lab 8 · Regulatory mapping and exit plan | — |
| 9 | 9 | Lab 9 · Roadmap and DC-exit checklist | **P2 due** |
| 10 | 10 | ADRs and principles | — |
| 11 | 11 | Lab 10 · AI assessment vs evidence | AI evaluation note |
| 12 | 12 | Stakeholder map and one-pager | — |
| 13 | 12 | P3 | — |
| 14 | 12 | Board rehearsal | **P3 due** |
| 15 | Review | Panel defence of P3 | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** summarising interviews and documents; drafting ADRs, option papers and executive summaries; generating first-pass dispositions and wave groupings to critique; converting tables into ArchiMate import formats.
- **Do without AI (drills):** dependency analysis from raw flow data; TCO arithmetic and sensitivity; regulatory mapping from primary texts; the one-page architecture; the mid-term and final.
- **Verify AI output by:** comparing every dependency claim with flow data; recomputing costs from current public price lists; reading the regulation or direction itself (RBI, CERT-In, MeitY, Gazette) for every regulatory claim; checking each disposition against your scoring.
- **Where AI still fails here:** assistants cannot see dependencies that are not in the data they are given, quote outdated prices and licence terms, and state regulatory requirements that do not exist or apply to the wrong sector. In Lab 10 you measure agreement between an assistant's dispositions and yours, and classify each disagreement as AI error, your error, or genuine judgement call.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1–P3 | 35% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) + P3 panel defence | 30% |

**Mastery gate.** You pass when you can, without AI: (1) from an unseen inventory and flow dataset, produce dispositions and migration waves for 30 applications with reasons in 3 hours; (2) build a 5-year TCO comparison with a sensitivity analysis that identifies the decisive assumptions; (3) present and defend a hybrid target architecture, including regulatory constraints, to a panel in 15 minutes plus questions.

## Industry reality

Where this is used: enterprises and public bodies planning data-centre exits, hypervisor changes and cloud adoption; Indian IT services firms and global capability centres that sell and deliver transformation programmes; banks and insurers under RBI and IRDAI oversight. Architect roles are the growing end of the infrastructure field in the BLS projections. TOGAF certification is common in enterprise-architect job descriptions; cloud architect certifications (see the [CLD major](../../../cloud_engineering/README.md)) are common for solutions architects.

**Interview questions from this course**

1. *We have 300 applications and want to "move to the cloud". Where do you start?* Strong answer: goals and constraints first, inventory and data quality, rationalisation before migration, dependency discovery, regulatory mapping, a pilot wave, a business case with sensitivity, governance.
2. *How do you find dependencies nobody documented?* Strong answer: flow data over a full business cycle, firewall logs, discovery tools, interviews with owners, batch schedules, and test migrations; states the blind spots of each.
3. *Make the case for or against leaving our hypervisor platform.* Strong answer: options, costs over 5 years including migration and double running, skills, risks, timelines from comparable cases, exit points, recommendation with conditions.
4. *What does Indian regulation change about this design?* Strong answer: names the specific rules (RBI payment-data storage, IT governance directions, CERT-In logs, DPDP obligations), maps them to data placement, logging, contracts and exit plans, and says what needs legal confirmation.
5. *Tell me about an architecture decision you got wrong.* Strong answer: the ADR, what evidence was missing, how it was detected, how it was reversed, and what changed in the decision process.

## Resources (free first)

- **Frameworks:** The Open Group, TOGAF Standard (free to read with registration) — https://www.opengroup.org/togaf ; ArchiMate specification — https://www.opengroup.org/archimate-forum/archimate-overview ; Archi modelling tool — https://www.archimatetool.com/
- **Cloud frameworks:** AWS Prescriptive Guidance on migration strategies — https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-guide/migration-strategies.html ; Microsoft Cloud Adoption Framework — https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ ; Google Cloud Architecture Framework — https://cloud.google.com/architecture/framework
- **Decision records:** ADR templates and guidance — https://adr.github.io/
- **India regulation:** RBI IT governance master direction (2023) — https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=12562 ; CERT-In Directions (2022) — https://www.cert-in.org.in/PDF/CERT-In_Directions_70B_28.04.2022.pdf ; DPDP Rules 2025 explainer (PIB) — https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/nov/doc20251117695301.pdf
- **Data sanitisation:** NIST SP 800-88 — https://csrc.nist.gov/pubs/sp/800/88/r1/final
- **Paid, optional:** TOGAF and ArchiMate certification courses; Gregor Hohpe, *The Software Architect Elevator* (O'Reilly).

## Sources

- BLS Occupational Outlook Handbook, computer network architects (+8%, median $134,050) and network and computer systems administrators (−4%, median $99,130), 2025–35 projections and May 2025 pay — https://www.bls.gov/ooh/computer-and-information-technology/computer-network-architects.htm ; https://www.bls.gov/ooh/computer-and-information-technology/network-and-computer-systems-administrators.htm (checked 2026-10)
- Network World, Broadcom VMware strategy (3 Jun 2026) — https://www.networkworld.com/article/4180754/will-broadcoms-vmware-strategy-keep-paying-big-dividends.html (checked 2026-10)
- Flexera, 2026 State of the Cloud (wasted IaaS/PaaS spend 29%, 18 Mar 2026) — https://www.flexera.com/about-us/press-center/flexera-finds-cloud-value-is-rising-while-ai-waste-grows (checked 2026-10)
- RBI, Master Direction on IT Governance, Risk, Controls and Assurance Practices (7 Nov 2023, effective 1 Apr 2024) — https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=12562 (checked 2026-10)
- RBI, "Storage of Payment System Data" (circular, 6 Apr 2018) — https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11244 (checked 2026-10)
- SEBI, "Framework for Adoption of Cloud Services by SEBI Regulated Entities" (6 Mar 2023; requires MeitY-empanelled cloud infrastructure) — https://www.sebi.gov.in/legal/circulars/mar-2023/framework-for-adoption-of-cloud-services-by-sebi-regulated-entities-res-_68740.html (checked 2026-10)
- CERT-In Directions, 28 April 2022 — https://www.cert-in.org.in/PDF/CERT-In_Directions_70B_28.04.2022.pdf (checked 2026-10)
- DPDP Rules 2025 notified 13–14 Nov 2025 with phased implementation; PIB explainer — https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/nov/doc20251117695301.pdf ; Hogan Lovells summary — https://ca.hoganlovells.com/en/publications/indias-digital-personal-data-protection-act-2023-brought-into-force- (checked 2026-10)
- AWS Transform general availability (15 May 2025) — https://aws.amazon.com/blogs/migration-and-modernization/aws-transform-generally-available/ ; Azure Copilot agents (Nov 2025) — https://azure.microsoft.com/en-us/blog/announcing-azure-copilot-agents-and-ai-infrastructure-innovations/ (checked 2026-10)

_Last reviewed: 2026-10_
