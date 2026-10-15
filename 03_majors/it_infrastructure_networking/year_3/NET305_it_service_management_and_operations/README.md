# NET305 · IT Service Management and Operations

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 6 | 4 (≈ 120 hours) | L1 → L3 | [CS204](../../../../02_year_2_core_computer_science/semester_3/CS204_computer_networks/README.md), [CS203](../../../../02_year_2_core_computer_science/semester_3/CS203_operating_systems/README.md) | [NET403](../../year_4/NET403_aiops_and_intent_based_networking/README.md), [NET404](../../year_4/NET404_enterprise_architecture_and_cloud_migration/README.md), [IND401](../../../../05_shared_years_3_to_5/IND401_industry_co_op_studio/README.md); compare with [OPS304](../../../devops_sre_platform_engineering/year_3/OPS304_site_reliability_engineering_slos_error_budgets/README.md) |

## Why this course matters now

Most infrastructure work is delivered as a service under contract: a service desk takes the call, an incident manager runs the outage, a change board decides whether the 2 a.m. upgrade goes ahead, and a service level agreement decides who pays when it goes wrong. India's IT services industry is built on this model, and NASSCOM's 2026 review says providers are moving "away from FTE delivery to outcome-based, risk-sharing constructs", which rewards fewer tickets and faster recovery rather than more people. AI is reshaping the front line first: the US Bureau of Labor Statistics projects computer support specialist jobs to fall 3% between 2025 and 2035, and Salesforce's CEO said in September 2025 that AI let the company cut customer-support headcount from about 9,000 to about 5,000. The framework itself is changing too: PeopleCert introduced ITIL (Version 5) in 2026, describing it as "AI-native" with an eight-stage product and service lifecycle, while ITIL 4 remains available. What does not change is the need for people who can run a major incident calmly, find the real root cause, decide whether a change is safe, keep a configuration database honest, and design monitoring that wakes someone only when it matters. The 2022 Rogers outage review found that the change process failed to flag the bad configuration and that a risk algorithm had downgraded the upgrade's risk rating; process is an engineering control, not paperwork.

## Learning outcomes

By the end you can:

1. **Explain** the ITIL 4 service value system and the main changes in ITIL (Version 5), and **map** them to how a real IT team works.
2. **Run** incident management for a major outage: classify priority, assign roles, communicate, and **produce** a timeline and post-incident review.
3. **Perform** problem management with structured root-cause techniques and **maintain** a known-error database.
4. **Design** a change enablement process with standard, normal and emergency changes, risk assessment and pipeline-based pre-approval, and **measure** change success rate.
5. **Build** a CMDB fed by discovery and reconciled with sources of truth, and **measure** its data quality.
6. **Write** SLAs, OLAs and underpinning contracts with measurable targets, and **calculate** availability and service credits.
7. **Design** infrastructure monitoring with Zabbix or Prometheus that alerts on symptoms, suppresses dependent alerts and avoids alert fatigue.
8. **Write** runbooks and **automate** safe ones, with approvals and audit trails.
9. **Evaluate** AI features in service desks and operations (classification, summarisation, virtual agents) against measured accuracy and risk.

## Chapters and lessons

### Chapter 1 · Services and the ITSM landscape (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 What a service is | Service, product, utility and warranty, service owner, consumer; "value co-creation" | Describe your college's email service as a service with owner, users and outcomes |
| 1.2 ITIL 4 in one lesson | Guiding principles, service value system, value chain, the 34 practices and which ones infrastructure teams use daily | Map 10 tasks from a network team's week to ITIL practices |
| 1.3 ITIL (Version 5) | What PeopleCert says changed in 2026: digital products, AI-native and complexity-native design, an eight-stage lifecycle (Discover, Design, Acquire, Build, Transition, Operate, Deliver, Support), ITIL 4 still valid | Compare an ITIL 4 value-chain view and a Version 5 lifecycle view of one service |
| 1.4 Other frameworks | ISO/IEC 20000-1, COBIT, SRE practices (see [OPS304](../../../devops_sre_platform_engineering/year_3/OPS304_site_reliability_engineering_slos_error_budgets/README.md)); where they overlap and conflict | Write one page: when an infrastructure team should adopt SRE practices and when ITIL processes |
| 1.5 The managed-services model | Offshore delivery, shared NOCs and service desks, outcome-based contracts | Draw the support chain for a global client served from an Indian delivery centre (illustrative) |

**Check your understanding:** Why is "process" not the same as "bureaucracy"? Which ITIL practices would an SRE team say it already does under other names? Why does an outcome-based contract change what a service provider wants to automate?

### Chapter 2 · Service desk and request fulfilment (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Tiers and shift-left | L1/L2/L3, swarming as an alternative, moving fixes to self-service | Classify 50 sample tickets by the lowest tier that could resolve them |
| 2.2 Requests vs incidents | Service catalogue, request models, approvals, fulfilment automation | Design 5 catalogue items with forms, approvals and automated steps |
| 2.3 Knowledge | Knowledge-centred service (KCS): capture in the workflow, reuse, improve | Write 5 knowledge articles and test them on a classmate |
| 2.4 Desk metrics | First-contact resolution, time to resolve, backlog age, CSAT; how metrics get gamed | Pick 4 metrics and name how each can be gamed |
| 2.5 AI at the front line | Virtual agents, ticket classification and routing, summarisation; what customer-support cuts at firms like Salesforce mean for IT desks | Measure an LLM's classification accuracy on 100 labelled tickets |

**Check your understanding:** Why can a high first-contact resolution rate hide a bad service? What is the risk of a virtual agent that answers from an outdated knowledge base? Which tickets should never be closed by AI alone?

### Chapter 3 · Incident management (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Priority | Impact × urgency matrix, P1–P4 definitions, consistent classification | Classify 20 scenarios; compare with classmates and resolve disagreements |
| 3.2 Major incidents | Incident commander, technical lead, communications lead, scribe; bridges; decision log | Run a 45-minute major-incident simulation with assigned roles |
| 3.3 Communication | Status updates on a fixed rhythm, stakeholder lists, status pages, what not to say | Write updates at T+15, T+45 and resolution for a WAN outage |
| 3.4 Regulatory duties | CERT-In's 6-hour reporting for listed cyber incidents and 180-day log retention (April 2022 directions); sector rules such as the RBI IT governance directions for banks | Add regulatory steps to your major-incident checklist |

**Check your understanding:** Why should the incident commander usually not be the person typing commands? What makes an update useful to a business stakeholder? Why must the 6-hour CERT-In clock be in the runbook, not in someone's memory?

### Chapter 4 · Problem management and root cause (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Reactive and proactive | From incident to problem; trend analysis to find problems before outages | Find 3 problem candidates in a 6-month ticket export |
| 4.2 Root-cause techniques | Timelines, change analysis ("what changed?"), fault trees, Ishikawa diagrams; why "5 whys" often stops at a person | Apply two techniques to the same case and compare conclusions |
| 4.3 Contributing factors | Why most outages have several causes; latent conditions; blameless reviews | Rewrite a blaming post-incident report into a blameless one |
| 4.4 Known errors | Workarounds, known-error database, linking to changes that fix them | Create 5 known-error records linked to incidents and fixes |
| 4.5 Case study | Rogers 2022: the removed filter, the change process that did not flag it, the risk score that was downgraded, the missing overload limit, staff without backup connectivity | Write the problem record with 5 corrective actions and owners |

**Check your understanding:** Why is "human error" a starting point for analysis, not a root cause? How do you know a problem is really fixed? Why did the Rogers review look at the risk algorithm as well as the engineer's mistake?

### Chapter 5 · Change enablement (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Change types | Standard (pre-approved), normal, emergency; who authorises each | Define 10 standard changes for a network team |
| 5.2 Risk assessment | Impact, likelihood, blast radius, rollback confidence; how scoring models fail | Score 6 changes; find one your model under-rates |
| 5.3 Approval that helps | CAB vs peer review vs automated approval; evidence over opinion | Redesign a weekly CAB so it reviews only high-risk changes |
| 5.4 Pipelines as controls | Pre-approved changes delivered through tested pipelines (from [NET303](../NET303_network_automation_and_netdevops/README.md)); evidence attached automatically | Connect a pipeline run to a change record with test results attached |
| 5.5 Measuring change | Change success rate, change failure rate (DORA), emergency change ratio, changes causing incidents | Compute these from a sample change log |

**Check your understanding:** Why can a slow, heavy CAB make outages more likely? What makes a change "standard"? Why should the change record contain the post-check results, not just the plan?

### Chapter 6 · Configuration management and the CMDB (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Configuration items | CI classes, attributes, relationships, service maps | Model one business service and all its CIs |
| 6.2 Discovery | Agent and agentless discovery, SNMP, WMI, SSH, cloud APIs; credentials and scope | Run discovery on your lab and list what it missed |
| 6.3 Reconciliation | Sources of truth (NetBox, AD, cloud inventories) vs discovery; identification rules, duplicates | Reconcile NetBox and discovery data for 50 devices |
| 6.4 Data quality | Completeness, correctness, staleness; why most CMDBs decay | Build a CMDB health score and report it weekly |
| 6.5 Asset and licence management | Hardware lifecycle, warranty, software licences and audits; how vendor licensing changes (for example Broadcom's VMware changes) hit budgets | Build a licence and end-of-support register for the lab estate |

**Check your understanding:** Why is a CMDB that is 70% correct often worse than none? Which relationship type matters most during an incident, and why? Why should discovery never be the only source for a CI?

### Chapter 7 · SLAs, contracts and suppliers (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Availability arithmetic | 99.9% ≈ 43.8 minutes a month; serial vs parallel availability; measurement windows and exclusions | Calculate end-to-end availability for a 4-component service |
| 7.2 Writing SLAs | Measurable targets, measurement method, reporting, service credits; experience-level agreements | Write an SLA for a branch WAN service |
| 7.3 OLAs and underpinning contracts | Internal team agreements; ISP and vendor contracts that must support the SLA | Find the gap where an ISP contract cannot support your SLA |
| 7.4 Supplier management | Vendor performance reviews, escalation paths, multi-vendor incidents | Run a mock quarterly review with an under-performing supplier |

**Check your understanding:** Why can three 99.9% components in series not give a 99.9% service? What makes an SLA exclusion fair or unfair? Why do outcome-based contracts need better measurement than headcount contracts?

### Chapter 8 · Infrastructure monitoring (weeks 8–9)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 What to monitor | Availability, performance, capacity, errors, logs, synthetic user checks; symptoms vs causes | List monitors for a branch network, from user experience down |
| 8.2 Zabbix | Hosts, templates, items, triggers, dependencies, SNMP and agent monitoring; Zabbix 7.0 LTS (8.0 LTS planned for Q4 2026) | Monitor the lab network and servers with templates |
| 8.3 Prometheus and Grafana | Exporters (node, SNMP, blackbox), PromQL, Alertmanager routing, grouping and inhibition | Build the same alerts in Prometheus; compare effort and result |
| 8.4 Other tools | PRTG (commercial, with a free tier), LibreNMS, Icinga; when each fits | Write a one-page tool choice for a 200-device estate |
| 8.5 Alert design | Thresholds with hysteresis, dependency suppression (a dead WAN link should page once, not for 40 devices behind it), routing, on-call load | Cut alert volume in a noisy lab by 70% without losing a real failure |
| 8.6 Event management | Correlating events, deduplication, linking alerts to incidents automatically | Auto-create one incident per correlated event group |

**Check your understanding:** Why should you page on symptoms users feel rather than on every cause? What does a dependency tree change during a WAN outage? Why does alert fatigue lead to missed incidents?

### Chapter 9 · Runbooks and operational automation (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Runbook structure | Trigger, checks, decision points, actions, verification, escalation, rollback | Write runbooks for 3 common alerts |
| 9.2 Automating runbooks | Ansible AWX or Rundeck jobs, approvals, audit logs, credentials | Automate the diagnostic half of one runbook |
| 9.3 Auto-remediation with limits | Which actions are safe to automate (restart a service) and which are not (failover a database); rate limits and kill switches | Add auto-remediation with a maximum of 3 runs per hour and a page on the 4th |
| 9.4 ChatOps | Running diagnostics from chat with logged commands | Build a chat command that returns interface status for a site |

**Check your understanding:** Why automate diagnosis before remediation? What can go wrong with auto-remediation during a wider outage? Why must every automated action be visible in the incident timeline?

### Chapter 10 · ITSM tools (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 ServiceNow | Incident, problem, change and CMDB tables, workflows, SLAs; a free Personal Developer Instance for learning | Build an incident-to-problem flow on a developer instance |
| 10.2 Alternatives | Jira Service Management (free tier for small teams), GLPI and iTop (open source) | Set up GLPI with your lab CMDB data |
| 10.3 Integrations | Monitoring to incident, discovery to CMDB, pipeline to change, chat to incident | Connect Zabbix or Alertmanager to your ITSM tool |
| 10.4 AI features | ServiceNow Now Assist, Atlassian's AI features: summaries, suggested resolutions, virtual agents; data protection of ticket content under India's DPDP Act | List what ticket data may be sent to an AI service and under what controls |

**Check your understanding:** Why do ITSM tool rollouts fail more often for process reasons than technical ones? What is the minimum integration that makes a CMDB useful in incidents? Why does ticket data raise personal-data questions?

### Chapter 11 · Continuity, availability and capacity (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Business continuity and DR | Business impact analysis, RPO and RTO, DR tiers, DR tests; RBI directions require BCP/DR for regulated entities | Run a business impact analysis for 5 services |
| 11.2 Availability management | Single points of failure, maintenance design, measuring real availability | Find every single point of failure in the lab |
| 11.3 Capacity management | Trends, forecasting, thresholds, lead times for hardware and circuits | Forecast WAN capacity for 12 months from 6 months of data |
| 11.4 Exercises | Tabletop vs live failover tests; learning from exercises | Run a tabletop for a data-centre power loss |

**Check your understanding:** Why does an untested DR plan usually fail on credentials, DNS or licences rather than on data? How long is the lead time for a new circuit in your city, and how does it change capacity planning? Why are tabletop exercises useful even without touching systems?

### Chapter 12 · Measuring operations and AI in ITSM (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Operational metrics | MTTA, MTTR (repair, recovery, resolve: define which), change success rate, reopen rate, SLA attainment | Build a monthly operations report from your lab data |
| 12.2 Continual improvement | ITIL's continual improvement model; improvement registers; small experiments | Run one improvement cycle on your alert noise |
| 12.3 Evaluating AI in operations | Accuracy, coverage, harm of errors (a misrouted P1), drift; human review sampling | Evaluate an AI summariser and classifier on 100 tickets with a confusion matrix |
| 12.4 The future of the desk | Which tasks move to self-service and agents, which grow (problem, change, service design), how teams are restructured | Write a 2-year plan for a 30-person service desk |

**Check your understanding:** Why must MTTR always be defined before it is compared? What error rate would you accept from an AI ticket router, and why does it depend on priority? Which roles in a service desk grow in value as AI handles L1?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Service model and value-chain map | — |
| 2 | 2 | Lab 2 · Service catalogue and AI classifier test | — |
| 3 | 3 | Lab 3 · Major-incident simulation | **P1 due** |
| 4 | 4 | Lab 4 · Root-cause analysis | Problem record |
| 5 | 5 | Lab 5 · Change process and pipeline link | — |
| 6 | 6 | Lab 6 · CMDB discovery and reconciliation | Mid-term (AI off) |
| 7 | 7 | SLA and availability exercises | — |
| 8 | 8 | Lab 7 · Zabbix monitoring | — |
| 9 | 8 | Lab 8 · Prometheus and alert noise reduction | **P2 due** |
| 10 | 9 | Lab 9 · Runbook automation | — |
| 11 | 10 | Lab 10 · ITSM tool integration | — |
| 12 | 11 | DR tabletop | BIA report |
| 13 | 12 | P3 | — |
| 14 | 12 | P3 drills | **P3 due** |
| 15 | Review | Oral defence of P3 | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** drafting runbooks, knowledge articles, stakeholder updates and post-incident reports (then editing for accuracy); summarising long ticket histories; generating test tickets for classifier evaluation; writing PromQL and Zabbix trigger expressions you then test.
- **Do without AI (drills):** priority classification; running the major-incident simulation; root-cause analysis; availability arithmetic; designing alert dependencies. The mid-term and final are AI-off.
- **Verify AI output by:** checking every fact in a generated incident report against the timeline and logs; testing every alert expression against recorded data; measuring classifier accuracy on labelled tickets, not on impressions; reading the framework's own text for any claim about ITIL or ISO 20000.
- **Where AI still fails here:** summaries of incident bridges drop or invent the decision that mattered; classifiers trained on old tickets misroute new kinds of failures; virtual agents answer confidently from stale knowledge articles. In Lab 2 and Chapter 12 you measure this: confusion matrices for classification, and a count of factual errors in 10 AI-written incident summaries against the true timeline.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1–P3 | 35% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) + P3 oral defence | 30% |

**Mastery gate.** You pass when you can, without AI: (1) act as incident commander in an unseen 45-minute major-incident simulation, with correct priority, roles, three timed stakeholder updates and a decision log; (2) write a blameless problem record for a given case with a defensible root cause and at least 4 corrective actions; (3) design monitoring for a small estate whose alerts, tested against a recorded failure, page once for the real fault and suppress dependent alerts.

## Industry reality

Where this is used: every enterprise IT department, every managed-services contract, and every NOC. Indian IT services firms run large service desks and NOCs for global clients, and NASSCOM describes the industry shifting from headcount to outcome-based contracts. Regulators set minimum process expectations: CERT-In's 2022 directions for incident reporting and logs, and the RBI's November 2023 IT governance directions (in force from April 2024) for banks and other regulated entities. ITIL 4 Foundation remains the most common ITSM certification; ITIL (Version 5) Foundation became available in 2026.

**Interview questions from this course**

1. *Walk me through how you would run the first 30 minutes of a P1 outage.* Strong answer: declare, assign commander and comms, open a bridge, establish scope and impact, timeline, regular updates, focus on restoring service before root cause, regulatory checks, hand-offs.
2. *What is the difference between incident and problem management?* Strong answer: restore service vs remove the cause; known errors and workarounds; how a problem record links to changes; example.
3. *Our CAB meets weekly and changes still cause outages. What would you change?* Strong answer: risk-based routing, standard changes through tested pipelines, evidence-based approval, post-change verification, measuring change failure rate, learning from failed changes.
4. *How do you stop alert fatigue in a NOC?* Strong answer: symptom-based paging, dependencies and suppression, deduplication, thresholds with hysteresis, regular review of noisy alerts, measuring pages per shift.
5. *Would you let an AI agent close tickets?* Strong answer: depends on ticket type and measured accuracy; start with suggestions, sample reviews, never for P1/P2 or security; track reopen rates; data protection for ticket content.

## Resources (free first)

- **Frameworks:** PeopleCert, ITIL (Version 5) explained — https://www.peoplecert.org/news-and-announcements/itil-version-5-explained ; ITIL certifications — https://www.peoplecert.org/browse-certifications/it-governance-and-service-management/ITIL-1
- **Free books and guides:** Google SRE books (free online), especially "Managing Incidents" and "Postmortem Culture" — https://sre.google/books/ ; PagerDuty Incident Response documentation (open) — https://response.pagerduty.com/
- **Monitoring:** Zabbix documentation — https://www.zabbix.com/documentation/current/ ; Prometheus — https://prometheus.io/docs/ ; Grafana — https://grafana.com/docs/ ; LibreNMS — https://docs.librenms.org/
- **ITSM tools:** ServiceNow Developer Program (free Personal Developer Instance) — https://developer.servicenow.com/ ; GLPI — https://glpi-project.org/ ; iTop — https://www.combodo.com/itop ; Ansible AWX — https://github.com/ansible/awx ; Rundeck — https://www.rundeck.com/open-source
- **Regulation (India):** CERT-In Directions (28 Apr 2022) — https://www.cert-in.org.in/PDF/CERT-In_Directions_70B_28.04.2022.pdf ; RBI IT governance master direction (7 Nov 2023) — https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=12562
- **Paid, optional:** official ITIL publications (PeopleCert); ISO/IEC 20000-1 standard text.

## Sources

- NASSCOM, Technology Sector in India: Strategic Review 2026 (shift to outcome-based constructs) — https://nasscom.in/knowledge-center/publications/technology-sector-india-strategic-review-2026 (checked 2026-10)
- BLS Occupational Outlook Handbook, computer support specialists (−3%, 2025–35) — https://www.bls.gov/ooh/computer-and-information-technology/computer-support-specialists.htm (checked 2026-10)
- CNBC, "Salesforce CEO confirms 4,000 layoffs 'because I need less heads' with AI" (2 Sep 2025) — https://www.cnbc.com/2025/09/02/salesforce-ceo-confirms-4000-layoffs-because-i-need-less-heads-with-ai.html (checked 2026-10)
- PeopleCert, "New ITIL Explained for Certified Professionals" — https://www.peoplecert.org/news-and-announcements/itil-version-5-explained ; ITIL Foundation (Version 5) guide (lifecycle stages, AI-native) — https://www.itil.com/Itil-News-and-Announcements/itil-version-5-foundation-whats-new-guide (checked 2026-10)
- Rogers outage review (Xona Partners executive summary, CRTC), reported 5 Jul 2024 — https://mobilesyrup.com/2024/07/05/july-2022-rogers-outage-report-crtc/ (checked 2026-10)
- Zabbix life cycle and release policy (7.0 LTS June 2024; 8.0 LTS planned Q4 2026) — https://www.zabbix.com/life_cycle_and_release_policy (checked 2026-10)
- CERT-In Directions, 28 April 2022 — https://www.cert-in.org.in/PDF/CERT-In_Directions_70B_28.04.2022.pdf (checked 2026-10)
- RBI, Master Direction on IT Governance, Risk, Controls and Assurance Practices (7 Nov 2023, effective 1 Apr 2024) — https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=12562 (checked 2026-10)

_Last reviewed: 2026-10_
