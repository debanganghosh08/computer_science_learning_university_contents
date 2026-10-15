# NET404 · Labs and projects

The semester uses one case pack: a mid-sized Indian company (illustrative) with two data centres, 60 branches, about 250 applications, a CMDB export, licence records, one month of flow and firewall logs, interview notes and a budget. All data is synthetic. Tools are free: Archi for ArchiMate, Python or a spreadsheet for analysis, NetBox for the address plan, and cloud providers' public pricing calculators. Where a project uses real organisations as inspiration, only public facts are used.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Case analysis | Read the case pack; list stakeholders, constraints and the 10 questions the architecture must answer | Question list with the data needed for each | 3 h |
| 2 · ArchiMate model | Model 3 business processes down to applications, servers and networks in Archi; produce 3 viewpoints | Archi model file, views for CIO, engineer and auditor | 4 h |
| 3 · Capability map and debt register | Capability heat map; technical debt register with cost of delay | Map and register | 4 h |
| 4 · Portfolio scoring | Score 40 applications on 6 attributes; assign TIME and R dispositions with reasons | Scored portfolio with dispositions | 5 h |
| 5 · Dependency graph and waves | Build a dependency graph from flow and firewall logs; compare with a discovery-tool export; group into waves | Graph, comparison of blind spots, wave plan with rules | 5 h |
| 6 · Target hybrid network | Address plan across 2 DCs, branches and 2 clouds; DNS, identity, connectivity, inspection and segmentation on one diagram | Design with NetBox export and diagram | 5 h |
| 7 · TCO and business case | 5-year TCO for current state and 3 options; NPV; tornado chart of assumptions | Model with every assumption labelled sourced or estimated | 5 h |
| 8 · Regulatory mapping and exit plan | Map DPDP, RBI, SEBI and CERT-In requirements to 10 applications; exit plans for one SaaS and one cloud | Mapping table citing primary texts; two exit plans | 4 h |
| 9 · Roadmap and DC exit | 18-month roadmap with transition states and decision gates; DC-exit checklist | Roadmap, checklist with owners | 4 h |
| 10 · AI assessment vs evidence | Run an assistant over the inventory; compare its dispositions, dependencies and cost claims with your evidence | Agreement rate, classified disagreements, verified claims table | 4 h |

## Projects

### P1 · Current-state architecture and debt assessment (L1, ~6 hours)

**Real-world inspiration.** Most transformation programmes start with an assessment that a consulting team delivers in weeks; Indian IT services firms and global capability centres run many of these. The quality of this document decides whether later decisions are grounded.

**What to build.** A current-state architecture pack for the case: capability map with heat map, ArchiMate views of 3 critical processes, application and infrastructure inventory reconciled across sources, technical debt register (end-of-support systems, licence exposure, single points of failure), and a 2-page summary of the top 5 risks.

**Acceptance criteria**
- Every application in the inventory has an owner, criticality, data classification and hosting location, or is flagged as unknown with an action.
- At least 10 contradictions between data sources are found and resolved or logged.
- Each top-5 risk has evidence from the case data and a cost-of-delay estimate with stated assumptions.
- A reader who has not seen the case can explain the estate's biggest problem after reading the 2-page summary.

**Stretch goals.** Generate the inventory views automatically from the CMDB export; add a dependency view for one capability.

**What it proves to an employer.** You can establish the truth about an estate quickly and clearly, the first skill an architect is judged on.

### P2 · Portfolio rationalisation and migration wave plan (L2, ~15 hours)

**Real-world inspiration.** After Broadcom's VMware changes, many enterprises had to decide quickly which workloads to keep, move or retire; Network World reported in June 2026 that most are reducing their footprint but few have finished. Good rationalisation turns a forced migration into a chance to retire applications.

**What to build.** Dispositions for all case applications with a scoring model, dependency-based wave plan from flow data, and the wave-1 target design (landing zone, connectivity, DNS, identity, security). Include a decommissioning plan for at least 5 retired applications.

**Acceptance criteria**
- Every application has a disposition, a score breakdown and a one-line reason; at least 10% are retired or consolidated, or the report explains why not.
- No wave splits an application from a dependency with more than a stated traffic or latency threshold, verified by a script against the flow data.
- Wave 1 contains low-risk applications with a stated reason and success metrics.
- The wave-1 target design has a non-overlapping address plan (checked by script), hybrid DNS resolution in both directions, and an inspection point for all north-south traffic.
- An assistant's dispositions are compared with yours, with agreement rate and the 5 most significant disagreements explained.

**Stretch goals.** Simulate the plan's effect on data-centre power and licence costs per wave; add a rollback plan for wave 1.

**What it proves to an employer.** You can make the hard portfolio decisions with evidence and translate them into an executable plan.

### P3 · Board-ready transformation architecture (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** Regulated Indian organisations must align architecture with the RBI's 2018 payment-data storage rule, its 2023 IT governance directions, SEBI's 2023 cloud framework, CERT-In's logging directions and the DPDP Rules phasing in to 2027, while controlling cost (Flexera's 2026 survey estimated 29% of cloud spend as wasted). The case company (illustrative) has asked for a recommendation it can take to its board.

**What to build.** A full architecture recommendation: current state (P1), target state with ArchiMate views and a hybrid network design across on-premises, branches and at least one cloud, three options (for example, hybrid with private cloud refresh, cloud-first with retained core, and a two-cloud option), 5-year TCO and NPV with sensitivity, regulatory mapping with exit plans, an 18-month roadmap with transition architectures and decision gates, 8 architecture principles and 10 ADRs, and a governance model for the programme. Present it in 15 minutes to a panel acting as the board, with a one-page summary.

**Acceptance criteria**
- Each option is costed with the same assumptions; the sensitivity analysis names the 3 assumptions that could change the recommendation and the break-even values.
- Every regulatory constraint cited links to a primary text (RBI, SEBI, CERT-In, MeitY or the Gazette), and every application with personal or payment data has a compliant placement.
- The hybrid network design passes automated checks: no address overlaps, DNS resolution matrix complete, every flow from Lab 5 has a path and an inspection decision.
- The roadmap has at least 3 decision gates with measurable criteria (for example, wave-1 incident count, cost variance under 10%, user satisfaction).
- The ADRs record rejected options and consequences; at least one ADR shows a decision changed by evidence during the project.
- In the panel, you answer cost, risk and regulatory questions with evidence from the pack; the panel's scoring rubric (clarity, evidence, risk handling) averages at least 3 out of 4.

**Stretch goals.** Add an AI-assisted operations model for the hybrid estate (link to NET403) with costs and risks; add a sustainability view (energy and carbon) with sourced factors.

**What it proves to an employer.** You can lead a technology decision at board level with evidence, the defining skill of infrastructure, solutions and enterprise architects.

## Feeds into

- [THS501 Thesis or Capstone I](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) and [THS502](../../../../05_shared_years_3_to_5/THS502_thesis_or_capstone_ii/README.md): P3 is a natural industry capstone.
- [LCH502 Career Launch and Founder Studio](../../../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md): the assessment and business-case skills underpin an independent infrastructure consultancy.
- [CLD402 Multi-Cloud, Hybrid Cloud and Migration](../../../cloud_engineering/year_4/CLD402_multi_cloud_hybrid_cloud_and_migration/README.md) and [CLD403 FinOps](../../../cloud_engineering/year_4/CLD403_finops_and_cloud_cost_engineering/README.md) as electives.
- The major's [flagship industry project](../../../../06_career_and_market_readiness/05_industry_projects/NET_it_infrastructure_networking.md).
