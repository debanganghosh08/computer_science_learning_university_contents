# SAR404 · Resilience, Business Continuity and Security Strategy

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 8 | 4 (≈ 120 hours) | L3 → L4 | [SAR304](../../year_3/SAR304_applied_cryptography_and_pki_for_architects/README.md) (also recommended: [SAR301](../../year_3/SAR301_security_architecture_principles_and_frameworks/README.md), [SAR401](../SAR401_cloud_security_architecture/README.md)) | [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md), [LCH502](../../../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md), [SAR501](../../year_5/SAR501_frontier_seminar_post_quantum_migration/README.md) |

Part of the [Security Architecture major](../../README.md). [SEC305](../../../cybersecurity_defense/year_3/SEC305_governance_risk_and_compliance/README.md) introduced business impact analysis, DR testing, ransomware resilience and board reporting as governance topics; [OPS402](../../../devops_sre_platform_engineering/year_4/OPS402_chaos_engineering_and_resilience/README.md) covers chaos engineering. This course is where they become architecture and strategy: recovery designs that work when identity, backups and the network are all under attack; dependency maps that reveal concentration risk; crisis decision systems; and the multi-year security strategy, budget and board conversation that a security architecture lead, deputy CISO or CISO owns.

## Why this course matters now

Recent incidents show that the hard part is recovery, not prevention alone:

- **NotPetya (2017):** Maersk rebuilt its global network after the malware destroyed its domain controllers; recovery depended on one domain controller in Ghana that happened to be offline during the attack ([Wired](https://www.wired.com/story/notpetya-cyberattack-ukraine-russia-code-crashed-the-world/)).
- **Change Healthcare (2024):** attackers entered through a remote-access portal without MFA, and claims processing across the US health system was disrupted for weeks ([TechTarget](https://www.techtarget.com/cybersecurity/news/366582824/Change-Healthcare-breached-via-Citrix-portal-with-no-MFA)).
- **CrowdStrike (July 2024):** a faulty content update, not an attack, crashed about 8.5 million Windows devices, by Microsoft's estimate ([Microsoft](https://blogs.microsoft.com/blog/2024/07/20/helping-our-customers-through-the-crowdstrike-outage/)).
- **C-Edge (2024):** a ransomware attack on a technology provider disrupted payments at about 300 Indian co-operative and regional rural banks ([CSO Online](https://www.csoonline.com/article/3480250/over-300-indian-banks-suffer-payment-disruption-from-ransomware-attack.html)).

Regulators now test recovery rather than accept plans. RBI's 2026 directions for commercial banks expect disaster-recovery drills that run DR as primary for a full business day ([DSCI summary](https://www.dsci.in/files/content/knowledge-centre/2026/dsci-brief-on-rbi-cybersecurity-commercial-banks-directions-2026.pdf)). The EU's DORA has applied to financial entities since January 2025. Boards face disclosure duties such as US SEC Form 8-K Item 1.05. AI can draft runbooks, run tabletop simulations and summarise incidents, but deciding which services come back first, what the company can live without, and how much to spend is the accountable human work this course trains.

## Learning outcomes

By the end you can:

1. **Map** an organisation's critical business services to their technical, people and supplier dependencies, and **set** impact tolerances, RTOs and RPOs that drive architecture.
2. **Design** backup and recovery architectures with immutability, separate identity and keys, isolated recovery environments and tested restores.
3. **Design** ransomware-resilient architectures that protect Tier 0 (identity, backups, management planes) and support rebuild from known-good sources.
4. **Choose** disaster-recovery patterns (backup and restore, pilot light, warm standby, active-active) by cost and tolerance, and **avoid** hidden control-plane dependencies.
5. **Analyse** third-party and concentration risk, and **design** technical and contractual mitigations and exit plans.
6. **Design** crisis management: decision rights, communications, regulatory clocks and exercises that test them.
7. **Write** a threat-informed, multi-year security strategy with an operating model, roadmap, budget and metrics.
8. **Communicate** risk and strategy to a board in business terms, and **defend** recommendations under questioning.

## Chapters and lessons

### Chapter 1 · Resilience as a design goal (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Terms | Availability, reliability, resilience, recoverability; fault vs failure vs disaster | Classify ten outages by which property failed |
| 1.2 Frameworks | NIST CSF 2.0 Recover function; SP 800-160 Vol. 2 Rev. 1 cyber resiliency goals (anticipate, withstand, recover, adapt) and techniques | Map a company's current controls to the four goals and find the empty one |
| 1.3 Case studies | Maersk 2017, Change Healthcare 2024, CrowdStrike 2024, C-Edge 2024 | For each, write: what failed, what saved them (or would have), the architecture lesson |
| 1.4 Designing for the worst day | Assume identity, backups and the network are compromised at once; "minimum viable company" | List what a hospital must run with no network for 72 hours |

**Check your understanding:** (1) Why can a highly available system still be non-resilient? (2) What made Maersk's recovery possible, and was it designed? (3) Which resiliency goal do most organisations neglect?

### Chapter 2 · From business impact to architecture requirements (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Critical business services | Services as customers experience them (pay a merchant, admit a patient), not systems | Identify five critical services of an illustrative payment bank |
| 2.2 Dependency mapping | People, processes, technology, data, suppliers, facilities; graph models; single points of failure | Build a dependency graph in code and compute nodes whose loss stops each service |
| 2.3 Tolerances and objectives | Impact tolerance, maximum tolerable downtime, RTO, RPO; operational-resilience regimes (EU DORA; UK impact-tolerance approach) | Set tolerances and derive RTO and RPO per system |
| 2.4 Requirements that follow | Turning tolerances into architecture requirements and test criteria | Write ten resilience requirements with tests |

**Check your understanding:** (1) Why define services from the customer's view? (2) Why can a supporting system need a tighter RTO than the service it supports? (3) What does a dependency graph reveal that a BIA spreadsheet hides?

### Chapter 3 · Backup and recovery architecture (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Principles | Multiple copies, media, locations; at least one immutable or offline copy; verified restores ("3-2-1-1-0") | Audit a provided backup design against the principles |
| 3.2 Immutability | S3 Object Lock compliance mode, AWS Backup Vault Lock and logically air-gapped vaults, Azure immutable storage, Google Cloud backup vaults; what admins can and cannot undo | Configure a locked backup and prove an administrator cannot delete it |
| 3.3 Separate trust | Backups in a separate account or tenant with separate identity and keys (from SAR304) | Design backup identity and key separation for an estate |
| 3.4 Replication is not backup | Replication copies corruption and encryption; point-in-time recovery; SaaS backup gaps | Show corruption replicating to a standby, then recover from a point in time |
| 3.5 Restore at scale | Restore throughput, ordering, data validation, rehearsals | Measure restore time for a 100 GB dataset and extrapolate to production size |

**Check your understanding:** (1) Why must backup credentials not live in the production identity system? (2) When does replication make recovery worse? (3) What is a restore test actually proving?

### Chapter 4 · Ransomware-resilient architecture (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 The adversary's playbook (defender's view) | Identity compromise, backup destruction, data theft, encryption, extortion; CISA's #StopRansomware Guide | Map the guide's recommendations to architecture controls |
| 4.2 Protecting Tier 0 | Identity systems, backup systems, hypervisors and management planes as Tier 0; separate admin paths | Draw Tier 0 for an illustrative hospital and its admin paths |
| 4.3 Isolated recovery environments | Cyber vaults and clean rooms: isolated network, separate identity, known-good images, forensic validation before reconnecting | Design an isolated recovery environment and its entry procedure |
| 4.4 Rebuild from known good | Infrastructure as code, golden images, configuration baselines, identity recovery (directory and IdP) | Rebuild a three-tier app from code into a clean account and time it |
| 4.5 Data integrity | NIST SP 1800-11, 1800-25 and 1800-26 practice guides on recovering from and detecting data-integrity attacks | Summarise the reference designs and pick components for your case |

**Check your understanding:** (1) Why do attackers target backups first? (2) What must be validated before restored systems reconnect? (3) Why is identity recovery often the longest step?

### Chapter 5 · Disaster recovery patterns (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Patterns and cost | Backup and restore, pilot light, warm standby, active-active; cost vs RTO and RPO | Choose patterns for five systems and estimate cost |
| 5.2 Hidden dependencies | Control planes, DNS, identity, certificate authorities, licence servers; static stability | Find three hidden dependencies in a provided DR design |
| 5.3 Data consistency in failover | Asynchronous replication loss windows, split brain, reconciliation (link to payments-grade reconciliation in [BE401](../../../backend_engineering/year_4/BE401_payments_grade_systems_transactions_idempotency/README.md)) | Write the reconciliation procedure after a failover with lost writes |
| 5.4 Regulatory expectations | RBI's 2026 expectation of running DR as primary for a full business day; CERT-In reporting during outages | Plan a full-day DR-as-primary drill |

**Check your understanding:** (1) Why is active-active not automatically more resilient? (2) What fails in DR if the identity provider lives only in the primary region? (3) What must be reconciled after a failover with data loss?

### Chapter 6 · Third-party and concentration risk (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Critical suppliers | Cloud, endpoint security, payment switches, core banking providers, SaaS; fourth parties | Rank 20 suppliers by impact if they fail for 48 hours |
| 6.2 Lessons from 2024 | CrowdStrike's faulty update (staged rollout, kernel-level access) and C-Edge (shared provider for many banks) | Write controls for "a trusted vendor pushes a bad update" |
| 6.3 Technical mitigations | Staged updates, update rings, diversity where it matters, offline fallbacks, manual operating modes | Design update rings for 10,000 endpoints |
| 6.4 Contractual and exit | Resilience clauses, notification, audit rights, exit plans and data portability; EU DORA's register of ICT providers | Write an exit plan for one critical SaaS |

**Check your understanding:** (1) When is vendor diversity worth its cost? (2) Why did a non-malicious update cause a resilience crisis? (3) What makes an exit plan credible?

### Chapter 7 · Crisis management and communication (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Crisis structure | Crisis team, incident command, decision rights, escalation; separation of technical response and business crisis management | Design a crisis team and its decision log |
| 7.2 Out-of-band operations | Communications when email, chat and identity are down; printed runbooks; contact trees | Build an out-of-band communication plan and test it |
| 7.3 Clocks and audiences | CERT-In 6-hour reporting, DPDP breach notices, sector regulators, SEC 8-K for US-listed firms; customers, staff, media | Build a notification matrix for one scenario |
| 7.4 Exercises | Tabletop design, injects, observers, after-action reports; AI-facilitated tabletops and their limits | Run a 90-minute ransomware tabletop with classmates |

**Check your understanding:** (1) Why separate technical responders from business crisis leaders? (2) What must exist before email goes down? (3) What makes a tabletop useful rather than theatrical?

### Chapter 8 · Proving resilience (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Test types | Restore tests, failover drills, chaos experiments, assumed-breach exercises (with [OFF401](../../../ethical_hacking_offensive_security/year_4/OFF401_red_teaming_adversary_emulation_and_purple/README.md) teams under authorization) | Choose test types for five requirements |
| 8.2 Measuring recovery | Time to detect, contain, restore and fully recover; data loss measured, not assumed | Instrument a drill and report measured RTO and RPO |
| 8.3 Evidence for regulators and boards | What evidence shows recovery capability | Assemble an evidence pack from your drill |
| 8.4 Continuous assurance | Automating restore tests and failover checks so evidence is produced every week, not once a year | Schedule an automated weekly restore test with a pass/fail report |

**Check your understanding:** (1) Why is a passed tabletop weak evidence? (2) Which metric best represents recovery capability? (3) How often should restores be tested, and how do you decide?

### Chapter 9 · Security strategy (weeks 9–10)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 What a strategy is | Diagnosis, guiding policy and coherent actions (Rumelt); strategy vs plan vs budget | Critique two public security strategies for these elements |
| 9.2 Threat- and business-informed diagnosis | Business model, regulators, adversaries, current CSF 2.0 profile, technical debt | Write a two-page diagnosis for an illustrative insurer |
| 9.3 Capability maps and target state | Capabilities (identity, data protection, detection, resilience, product security, AI security), maturity targets | Build a capability map with current and target levels |
| 9.4 Operating model | Central vs federated security, platform and paved-road teams, product security, security champions, managed services | Choose an operating model and justify it |
| 9.5 Roadmap | Sequencing, dependencies, quick wins vs foundations, what not to do | Write a three-year roadmap |

**Check your understanding:** (1) Why is a list of projects not a strategy? (2) What should the diagnosis include that a risk register does not? (3) What did you decide not to do, and why?

### Chapter 10 · Budgets, economics and metrics (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Budgeting approaches | Risk-based, capability-based and benchmark-based budgets, and why benchmarks mislead | Build a budget for the roadmap with ranges |
| 10.2 Quantifying risk reduction | FAIR-style loss ranges (from SEC305), cost of controls, diminishing returns | Compare two investments by expected loss reduction per rupee |
| 10.3 Cyber insurance | What insurers ask for (MFA, backups, endpoint detection), coverage limits, how insurance changes decisions | Map insurer questions to your controls |
| 10.4 Metrics | Outcome vs activity metrics, key risk indicators, leading indicators, trend over targets | Define eight board-level metrics |

**Check your understanding:** (1) Why does "percent of IT budget" say little about adequacy? (2) What makes a metric decision-useful? (3) How can insurance distort security priorities?

### Chapter 11 · Board and executive communication (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 What boards need | Oversight duties, risk appetite, decisions, disclosure obligations; RBI's quarterly board reporting for banks | Write the agenda for a board cyber session |
| 11.2 The one-page report | Risk in money and time, trend, decisions required, no jargon | Write a one-page report for your insurer |
| 11.3 Presenting and defending | Ten-minute briefings, handling hostile or naive questions, saying "I don't know yet" | Present to a panel playing the board |
| 11.4 After an incident | Briefing a board during and after a crisis; lessons without blame | Write a post-incident board briefing for your tabletop |

**Check your understanding:** (1) What does a board decide that management cannot? (2) Why should a board report contain decisions, not only status? (3) How do you present uncertainty honestly?

### Chapter 12 · The leadership path and AI in resilience (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Security leadership roles | Head of security architecture, deputy CISO, CISO; reporting lines (RBI requires CISO independence for banks); building and keeping a team | Write a 90-day plan for a new head of security architecture |
| 12.2 AI in resilience work | AI-drafted runbooks and plans, AI tabletop facilitators, AI agents in incident response with bounded permissions | Generate a runbook with an assistant and test it in a drill |
| 12.3 AI failure modes | Invented recovery steps, outdated vendor procedures, confident timelines without evidence, missing dependencies | Log every defect found in the AI runbook during the drill |
| 12.4 Your strategy defence | Pulling P3 together | Final rehearsal with peer feedback |

**Check your understanding:** (1) What changes in your job between architect and CISO? (2) Which recovery steps should never be delegated to an AI agent? (3) How do you keep AI-drafted runbooks current?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Case lessons and minimum viable company | Lesson table |
| 2 | 2 | Lab 2 · Dependency graph and tolerances (no AI) | Graph and tolerances |
| 3 | 3 | Lab 3 · Locked backups and corruption replay | Denied deletion, PITR restore; **P1 due** |
| 4 | 4 | Lab 4 · Rebuild into a clean account | Timed rebuild |
| 5 | 5 | Lab 5 · DR pattern choice and hidden dependencies | Findings |
| 6 | 6 | Lab 6 · Update rings and exit plan | Ring design, exit plan |
| 7 | 7 | Lab 7 · Out-of-band plan and tabletop | After-action report; mid-term (AI off) |
| 8 | 8 | Lab 8 · Instrumented recovery drill | Measured RTO/RPO; **P2 due** |
| 9 | 9 | Strategy diagnosis | Diagnosis |
| 10 | 9 | Lab 9 · Capability map and roadmap | Roadmap |
| 11 | 10 | Budget and metrics | Budget with ranges |
| 12 | 11 | Board briefing practice | One-page report |
| 13 | 12 | Lab 10 · AI runbook drill | Defect log |
| 14 | 12 | Project work | **P3 due** |
| 15 | Review | Board defence and exam | Final exam |

## Working with AI in this course

- **Use AI for:** drafting runbooks, crisis communications and board papers for you to correct; generating tabletop injects; summarising post-incident reports; turning dependency data into graphs; producing alternative strategy options to argue against.
- **Do without AI (drills):** dependency mapping and tolerances (Lab 2); the tabletop decisions; the mid-term; the final board defence.
- **Verify AI output by:** executing runbooks in drills and timing each step; checking every vendor procedure against the vendor's current documentation; checking regulatory clocks against the regulation text (CERT-In directions, DPDP Rules, SEC rules); asking for the evidence behind every number in a board paper.
- **Where AI still fails here (show it):** in Lab 10 you will run an AI-drafted ransomware recovery runbook in a drill and log steps that are wrong, missing (identity recovery, key access, isolated environment) or impossible in your environment; ask two assistants for India's incident-reporting deadlines and compare with CERT-In's directions and the DPDP Rules.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs 1–10 | 25% |
| Projects P1 / P2 / P3 | 5% / 15% / 25% |
| Mid-term (AI off) | 10% |
| Final: board defence of P3 plus written scenario exam | 20% |

**Mastery gate.** You pass when you can, without AI and in three hours: (a) take an unseen organisation description, identify its critical services and dependencies, and set defensible tolerances, RTOs and RPOs; (b) design a ransomware-resilient recovery architecture for it, including identity recovery, immutable backups with separate trust and an isolated recovery environment; and (c) write a one-page board paper with the three decisions you need and their costs, which a panel judges clear to a non-specialist.

## Industry reality

- **Regulators test recovery.** RBI's 2026 directions for banks, the EU's DORA and similar regimes expect tested recovery, not only plans.
- **Vendors sell immutable backups and recovery vaults** because ransomware made backup destruction standard practice for attackers.
- **The 2024 CrowdStrike outage made concentration risk a board topic,** even though no attacker was involved.
- **Senior security roles combine architecture and communication:** interview loops for deputy CISO and head of security architecture include a strategy presentation and a crisis scenario ([SAR market page](../../../../06_career_and_market_readiness/01_market_map/roles/SAR_security_architecture.md)).

**Interview questions from this course**

1. *"Design ransomware-resilient backup and recovery for a hospital network."* Strong answer: critical services and tolerances first, immutable backups with separate identity and keys, Tier 0 protection, isolated recovery environment, rebuild from code, identity recovery, restore testing, clinical downtime procedures.
2. *"Our main cloud region is down for eight hours. What should our architecture have done, and what do you decide now?"* Strong answer: pattern by tolerance, static stability, identity and DNS outside the region, data consistency and reconciliation, decision rights and communications.
3. *"Present a three-year security strategy to our board in ten minutes."* Strong answer: diagnosis in business terms, guiding policy, three to five coherent initiatives, cost ranges, metrics, decisions needed, what you will not do.
4. *"How do you decide how much to spend on security?"* Strong answer: risk and capability based, loss ranges, regulatory floors, diminishing returns, avoiding benchmark-only arguments, tying spend to outcomes.
5. *"A critical vendor pushed a faulty update that took down our endpoints. What would have limited it?"* Strong answer: staged update rings, vendor change controls in contracts, manual fallback, rapid recovery tooling, concentration analysis, exercise of the scenario.

## Resources (free first)

- **Standards and guides:** [NIST CSF 2.0](https://www.nist.gov/cyberframework); [NIST SP 800-34 Rev. 1](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final); [SP 800-160 Vol. 2 Rev. 1](https://csrc.nist.gov/pubs/sp/800/160/v2/r1/final); [NIST IR 8374](https://csrc.nist.gov/pubs/ir/8374/final) (ransomware risk management profile); [SP 1800-11](https://csrc.nist.gov/pubs/sp/1800/11/final), [SP 1800-25](https://csrc.nist.gov/pubs/sp/1800/25/final), [SP 1800-26](https://csrc.nist.gov/pubs/sp/1800/26/final); [CISA #StopRansomware Guide](https://www.cisa.gov/stopransomware/ransomware-guide); [EU DORA](https://eur-lex.europa.eu/eli/reg/2022/2554/oj).
- **Architecture:** [AWS disaster recovery whitepaper](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.html); [S3 Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html); [AWS Backup Vault Lock](https://docs.aws.amazon.com/aws-backup/latest/devguide/vault-lock.html); [Azure immutable storage](https://learn.microsoft.com/en-us/azure/storage/blobs/immutable-storage-overview); [Google SRE books](https://sre.google/books/) (free).
- **Regulation (India):** [CERT-In Directions (2022)](https://www.cert-in.org.in/PDF/CERT-In_Directions_70B_28.04.2022.pdf); [PIB on DPDP Rules](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2190014); RBI 2026 directions via the DSCI summary in Sources.
- **Paid, optional:** Richard Rumelt, *Good Strategy/Bad Strategy* (2011); ISO 22301:2019 (business continuity management systems; standard text is paid).

## Sources

All checked 12 Oct 2026.

- Wired, "The Untold Story of NotPetya" (22 Aug 2018) — https://www.wired.com/story/notpetya-cyberattack-ukraine-russia-code-crashed-the-world/
- TechTarget, Change Healthcare breached via Citrix portal with no MFA (2024) — https://www.techtarget.com/cybersecurity/news/366582824/Change-Healthcare-breached-via-Citrix-portal-with-no-MFA
- Microsoft, "Helping our customers through the CrowdStrike outage" (20 Jul 2024): about 8.5 million devices — https://blogs.microsoft.com/blog/2024/07/20/helping-our-customers-through-the-crowdstrike-outage/
- CSO Online, C-Edge ransomware and about 300 Indian banks (Aug 2024) — https://www.csoonline.com/article/3480250/over-300-indian-banks-suffer-payment-disruption-from-ransomware-attack.html
- DSCI brief on RBI's 2026 cybersecurity directions for commercial banks (31 Jul 2026) — https://www.dsci.in/files/content/knowledge-centre/2026/dsci-brief-on-rbi-cybersecurity-commercial-banks-directions-2026.pdf
- EU DORA, Regulation (EU) 2022/2554 (applies from 17 Jan 2025) — https://eur-lex.europa.eu/eli/reg/2022/2554/oj
- US SEC press release 2023-139 on cybersecurity disclosure rules (26 Jul 2023) — https://www.sec.gov/news/press-release/2023-139
- CISA #StopRansomware Guide — https://www.cisa.gov/stopransomware/ransomware-guide
- DPDP Rules (Rule 7 breach notices), as summarised in this curriculum's [SEC305](../../../cybersecurity_defense/year_3/SEC305_governance_risk_and_compliance/README.md) — https://www.pib.gov.in/PressReleasePage.aspx?PRID=2190014

_Last reviewed: 2026-10_
