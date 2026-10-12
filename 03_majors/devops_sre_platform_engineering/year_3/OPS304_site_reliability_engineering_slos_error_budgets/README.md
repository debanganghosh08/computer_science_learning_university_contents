# OPS304 · Site Reliability Engineering: SLOs, Error Budgets and Incident Response

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 6 | 4 (≈ 120 hours) | L2 → L3 (P3 reaches L4) | [CS215](../../../../02_year_2_core_computer_science/semester_4/CS215_cloud_and_devops_foundations/README.md), [CS203](../../../../02_year_2_core_computer_science/semester_3/CS203_operating_systems/README.md); strongly recommended: [OPS303](../OPS303_observability_metrics_logs_traces/README.md) | [OPS404](../../year_4/OPS404_performance_and_capacity_engineering/README.md), [OPS402](../../year_4/OPS402_chaos_engineering_and_resilience/README.md), [OPS403](../../year_4/OPS403_aiops_and_agentic_operations/README.md) |

Part of the [DevOps, SRE and Platform Engineering major](../../README.md). [CS215](../../../../02_year_2_core_computer_science/semester_4/CS215_cloud_and_devops_foundations/README.md) introduced SLOs, burn-rate alerts and one blameless post-mortem. This course turns those ideas into a working reliability practice: SLOs people agree to, error budgets that change decisions, on-call that does not burn people out, incident command that works under pressure, and learning that prevents the next outage. The core texts are Google's three SRE books, which are free online. Distributed-systems failure theory is in [CS212](../../../../02_year_2_core_computer_science/semester_4/CS212_distributed_systems_i/README.md); IT service management (ITIL-style change and problem management) is in [NET305](../../../it_infrastructure_networking/year_3/NET305_it_service_management_and_operations/README.md).

## Why this course matters now

Large outages keep coming from the interaction of automation, configuration and load, not from single broken servers:

- **AWS us-east-1 (October 2025):** a race condition in DynamoDB's DNS automation left an empty DNS record. EC2 launch errors continued until 1:50 PM PDT the next day while lease backlogs drained.
- **Google Cloud (June 2025):** a globally replicated policy change crashed a control plane; restarting tasks created a "herd effect" on its database.
- **Cloudflare (November 2025):** a database permission change doubled a generated file and took down core traffic for hours.
- **UPI (March–May 2025):** India's payment network had four outages, which NPCI linked to payment service provider banks sending "check transaction status" requests at very high speed, repeatedly. NPCI responded with API limits and peak-hour rules.

DORA replaced MTTR with "failed deployment recovery time", and incident researchers argue that mean time to resolve misleads because incident durations are heavily skewed. AI tools now draft incident timelines and post-mortems and suggest causes. What remains human, and is growing in value, is choosing the right reliability target, commanding an incident when the facts are unclear, and deciding what the organisation should learn ([market map](../../../../06_career_and_market_readiness/01_market_map/roles/OPS_devops_sre_platform_engineering.md)).

## Learning outcomes

By the end you can:

1. **Derive** availability and dependency budgets ("nines" to minutes, serial and parallel dependencies), and **explain** why 100% is the wrong target.
2. **Choose** user-centric SLIs (availability, latency, freshness, correctness, durability), and **specify** where and how each is measured.
3. **Set** SLOs from data and user needs, **write** an error budget policy, and **use** it to make release decisions.
4. **Implement** multiwindow, multi-burn-rate alerts from an SLO specification (OpenSLO, Sloth or Pyrra), including for low-traffic services.
5. **Measure and cut** toil, and **design** an on-call rotation with load limits, handoffs, escalation and runbooks.
6. **Command** an incident using defined roles (incident commander, operations lead, communications lead, scribe), and **communicate** status internally, to customers and to regulators (CERT-In's 6-hour rule).
7. **Facilitate** a blameless post-incident review that finds contributing factors and produces tracked actions, and **critique** MTTR-style metrics.
8. **Analyse** public post-mortems (AWS, Cloudflare, GitHub, Google, Meta, Slack, CrowdStrike, UPI) and **extract** design lessons.
9. **Run** production readiness reviews and basic capacity plans for launches and peak events.

## Chapters and lessons

### Chapter 1 · Reliability as a product decision (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 What SRE is | Google's model: software engineers doing operations, a 50% cap on operational work, SRE vs DevOps vs platform teams | Compare three SRE job descriptions against the SRE book's model |
| 1.2 Embracing risk | Why 100% is wrong (users cannot tell 99.99% from 100% through their own networks); cost of each extra nine | Price an extra nine for a sample service |
| 1.3 Availability arithmetic | Nines to downtime per 30 days; serial dependencies multiply; redundancy and correlated failure | Compute the ceiling on availability for a service with 6 critical dependencies |
| 1.4 Reliability is a feature | Product owners trade reliability against velocity explicitly | Write a one-paragraph reliability requirement for a UPI-style payment flow |

**Check your understanding:** (1) A service depends on five 99.9% services in series. What can it promise, and how could it promise more? (2) Why is a 99.999% target for a consumer mobile app usually waste? (3) Who should own the reliability target: SRE or product?

### Chapter 2 · Service level indicators (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 SLI types | Request-based (good/total) vs window-based; availability, latency, quality, freshness, correctness, coverage, durability | Define 4 SLIs for an API, a batch pipeline and a storage system |
| 2.2 Where to measure | Server metrics vs load-balancer logs vs client telemetry (RUM) vs synthetic probes | Measure the same SLI three ways; explain the differences |
| 2.3 Specification vs implementation | "Fraction of checkouts completed in under 2 s" vs the exact PromQL and exclusions | Write both for 3 SLIs |
| 2.4 Critical user journeys | SLIs for journeys (search → cart → pay), not for components | Map a journey and choose its SLIs |

**Check your understanding:** (1) Why can server-side latency look perfect while users suffer? (2) What should count as a "bad" request: a 4xx, a 5xx, a slow 200? (3) Why is CPU never an SLI?

### Chapter 3 · SLOs and error budgets (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Setting targets | Start from historical performance and user expectations; aspirational vs achievable SLOs | Set SLOs from 30 days of data for 3 services |
| 3.2 Windows | Rolling 28/30-day vs calendar windows; effects on behaviour | Simulate both windows over a quarter of incidents |
| 3.3 Error budget policy | What happens when budget is exhausted (freeze, reliability sprint), who decides, exceptions; the SRE workbook's sample policy | Write and get "sign-off" on a policy in a role-play |
| 3.4 SLAs vs SLOs | Contracts and credits; SLOs tighter than SLAs; dependency SLOs | Read a public cloud SLA and find its exclusions |
| 3.5 SLOs as code | OpenSLO specification; Sloth and Pyrra generating recording and alert rules | Generate rules for 3 SLOs from YAML |

**Check your understanding:** (1) Your service met its SLO but customers complained. What went wrong? (2) Why should an error budget policy be written before the budget runs out? (3) What does a team that never spends its error budget tell you?

### Chapter 4 · Alerting on SLOs (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Burn rate | Burn rate = observed error rate ÷ budgeted error rate; time to exhaustion | Compute exhaustion time for burn rates 1, 6, 14.4 |
| 4.2 Multiwindow, multi-burn-rate | Page at 14.4× over 1 h and 5 min (2% of budget), page at 6× over 6 h and 30 min (5%), ticket at 1× over 3 days and 6 h (10%), per the SRE workbook | Implement and unit-test all three |
| 4.3 Low-traffic services | Too few events for ratios; synthetic traffic, longer windows, combining services | Design alerting for a service with 50 requests an hour |
| 4.4 Precision, recall, reset time | Trade-offs among alerting strategies, as compared in the workbook | Score 4 alerting strategies on a replayed incident set |

**Check your understanding:** (1) Why does a short window alone cause flapping? (2) What does the 5-minute window add to the 1-hour one? (3) Why would you ticket rather than page at 1×?

### Chapter 5 · Toil and automation (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Defining toil | Manual, repetitive, automatable, tactical, without enduring value, growing with the service | Audit a week of your own operational work |
| 5.2 Measuring toil | Toil surveys, ticket analysis, interrupt tracking | Classify 100 tickets; estimate hours per month |
| 5.3 Eliminating, not just automating | Fix the cause, self-service, delete the task; automation that is safe to re-run | Remove one toil source entirely and measure the saving |
| 5.4 Automation risk | Automation outages (AWS 2017 S3 command, AWS 2025 DNS automation race); rate limits and safety checks on tools | Add input validation and a blast-radius limit to a script |

**Check your understanding:** (1) Why can automation make outages bigger? (2) Which toil should you not automate? (3) What safety check would have limited the 2017 S3 command's impact?

### Chapter 6 · On-call design (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Rotations | Primary/secondary, follow-the-sun vs single site; the SRE book's arithmetic (no more than 25% on-call; minimum eight engineers for a single-site 24/7 rotation) | Design rotations for a team of 6 in Bengaluru and 4 in Europe |
| 6.2 Load limits | At most 2 incidents per 12-hour shift (SRE book); page budgets; what to do when exceeded | Compute page load from a month of alerts and propose cuts |
| 6.3 Runbooks and playbooks | Structure (symptoms, checks, mitigations, escalation), links from alerts, keeping them alive | Write runbooks for 5 alerts; test them with a classmate |
| 6.4 Humane on-call | Handoffs, compensation and time off, escalation policies, paging tools (PagerDuty, incident.io, Opsgenie, Grafana IRM) | Write an on-call policy including compensation |

**Check your understanding:** (1) Why does a single-site 24/7 rotation need so many people? (2) A runbook says "restart the service". What is missing? (3) How do you detect on-call burnout before people quit?

### Chapter 7 · Incident response and command (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Declaring | Severity levels, declare early, one channel, one commander | Write a severity matrix for a fintech product |
| 7.2 Roles | Incident command system roles (IC, ops lead, comms lead, scribe), handover of command; Google's and PagerDuty's published models | Tabletop with rotating roles |
| 7.3 Mitigate first | Roll back, drain, fail over, flag off, shed load; root cause later | Pick mitigations for 6 scenarios with incomplete data |
| 7.4 Communication | Internal updates on a cadence, status pages, customer messages; CERT-In 6-hour reporting for cyber incidents in India | Write three updates for an evolving incident |
| 7.5 Wheel of Misfortune | Role-play of past incidents (SRE book, ch. 28) | Run and debrief two sessions |

**Check your understanding:** (1) Why should the incident commander not be the one typing commands? (2) When is rolling back the wrong mitigation? (3) What must the first customer update say even if you know nothing yet?

### Chapter 8 · Post-incident learning (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Blameless post-mortems | Structure, timeline, impact, contributing factors, actions; the SRE book's example post-mortem | Write one for an incident from your labs |
| 8.2 Beyond root cause | Multiple contributing factors, "5 whys" limits, hindsight bias, Safety-II thinking | Rewrite a "human error" post-mortem without blame |
| 8.3 Actions that close | Owners, priorities, deadlines, tracking; why action items rot | Audit 10 public post-mortems' action items |
| 8.4 Metrics critique | MTTR's skewed distributions; DORA's failed deployment recovery time; near misses as data | Plot incident durations from a public data set and show why the mean misleads |

**Check your understanding:** (1) Why is "human error" a starting point, not a conclusion? (2) What does a skewed duration distribution do to MTTR? (3) How do you learn from an incident that almost happened?

### Chapter 9 · Reading real post-mortems (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Partitions and failover | GitHub, 21 Oct 2018: a 43-second network partition, Orchestrator failover across coasts, 24 h 11 min of degraded service | Draw the timeline; mark each decision point |
| 9.2 Automation and control planes | AWS S3 (Feb 2017) command removing too many servers; AWS DynamoDB DNS race (Oct 2025); Google Cloud Service Control (Jun 2025) | Compare the three as "automation without guard rails" |
| 9.3 Global config and edge | Cloudflare WAF regex CPU exhaustion (Jul 2019) and feature file (Nov 2025); Meta BGP withdrawal (Oct 2021) | List the safety mechanisms each lacked |
| 9.4 Cascades and recovery | Slack (Jan 2021) scaling under load; CrowdStrike (Jul 2024) content update | Find the recovery bottleneck in each |
| 9.5 India: UPI 2025 | Repeated status-check calls; NPCI's 90-second rule for status checks, 50 balance enquiries per app per customer per day, peak hours 10 am–1 pm and 5–9:30 pm | Model retry load before and after the circular |

**Check your understanding:** (1) What do the AWS 2025 and Google 2025 incidents have in common in their recovery phase? (2) Why did Meta's engineers struggle to reach their own data centres? (3) What does NPCI's rule teach about client behaviour as a reliability problem?

### Chapter 10 · Capacity and launches (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Demand | Organic growth vs events (sale days, IPL matches, festival peaks, tax deadlines) | Forecast next quarter from 12 months of synthetic traffic |
| 10.2 Provisioning | N+2, headroom per zone, quotas and lead times; intent-based planning (SRE book, ch. 18, Auxon) | Size a service to survive a zone loss at peak |
| 10.3 Production readiness | PRR checklists, launch coordination (SRE book, ch. 27 and Appendix E) | Run a PRR on a classmate's service |
| 10.4 Data integrity and DR | Backups vs restores, RTO/RPO, the GitLab 2017 lesson from CS215 | Time a restore and compare with the stated RTO |

**Check your understanding:** (1) Why is "N+1" often not enough during a deploy? (2) What belongs on a launch checklist that developers forget? (3) Why is restore time, not backup success, the metric?

### Chapter 11 · SRE in organisations and in the AI era (weeks 11–12)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Engagement models | Embedded, consulting, platform-owned reliability; "you build it, you run it" | Recommend a model for a 40-engineer startup |
| 11.2 Reporting reliability | SLO reviews, quarterly reliability reports, error budget politics | Present a reliability review to a "VP" role-player |
| 11.3 AI in incidents | AI-drafted timelines, summaries and post-mortems (incident.io, PagerDuty, Rootly-style tools); measuring their accuracy | Compare an AI post-mortem draft with your own; list omissions |
| 11.4 SLOs for AI features | Quality SLIs (eval pass rate), latency to first token, cost per request, provider dependency | Define SLOs for an LLM-backed support bot |

**Check your understanding:** (1) Why can an AI-written post-mortem be fluent and still wrong? (2) What does an SRE team owe a product team that keeps exceeding its error budget? (3) How would you measure "quality" for an LLM feature as an SLI?

### Chapter 12 · Game days and integration (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Planning a game day | Scope, safety, abort criteria, observers | Plan the P3 game day |
| 12.2 Running it | Live incident command with injected faults | Run P3's game day |
| 12.3 Learning review | Facilitated review, actions, follow-up | Publish the review |
| 12.4 Closing the loop | Verifying that actions are done, re-running the scenario, sharing lessons across teams | Re-run one game-day scenario after its fix and compare the two timelines |

**Check your understanding:** (1) What makes a game day safe to stop? (2) Who should not be told the scenario in advance? (3) How do you prove an action item fixed the problem?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Availability arithmetic | Dependency budget sheet |
| 2 | 2 | Lab 2 · SLIs three ways | SLI comparison |
| 3 | 3 | Lab 3 · SLOs and policy | Policy document; P1 starts |
| 4 | 4 | Lab 4 · Burn-rate alerts | **P1 due** |
| 5 | 5 | Lab 5 · Toil audit | Toil report |
| 6 | 6 | Lab 6 · Rotation and runbooks | On-call policy; P2 starts |
| 7 | 7 | Lab 7 · Incident command tabletop | Mid-term (AI off) |
| 8 | 8 | Lab 8 · Post-mortem rewrite | Blameless rewrite |
| 9 | 9 | Post-mortem presentations | Case analysis |
| 10 | 10 | Lab 9 · PRR and restore timing | **P2 due** |
| 11 | 11 | Reliability review role-play | Quarterly review deck |
| 12 | 11 | Lab 10 · AI post-mortem audit | Omission list |
| 13 | 12 | P3 game day | Game day log |
| 14 | 12 | P3 learning review | **P3 due** |
| 15 | Review | Incident simulation exam and oral | Final |

## Working with AI in this course

- **Use AI for:** drafting SLO YAML and runbooks; summarising long incident channels into a first timeline; checking a post-mortem draft for blame language; generating realistic synthetic incident data. Named tools: incident.io and PagerDuty's AI features, Claude, ChatGPT, Gemini.
- **Do without AI (drills):** availability and burn-rate arithmetic; the incident command tabletop and the final simulation (you command; nobody else thinks for you); writing the first draft of every post-mortem's contributing-factors section.
- **Verify AI output by:** checking every timeline entry against a log line or message with a timestamp; recomputing every number; checking that each stated cause is supported by evidence and not only by correlation; reading the post-mortem as the engineer who made the change would read it.
- **Where AI still fails here (show it):** in Lab 10, give an assistant the raw channel of a simulated incident. Record when it confuses the first symptom with the cause, omits mitigation steps that failed, or assigns blame to a person. In OPS403 you will measure this systematically.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs 1–10 | 25% |
| Projects P1 / P2 / P3 | 5% / 15% / 25% |
| Mid-term (AI off) | 10% |
| Final: live incident simulation as incident commander (AI off) + oral | 20% |

**Mastery gate.** You pass when you can: (1) take a service with only raw telemetry and, in 2 hours, produce SLIs, SLOs, an error budget policy and tested multiwindow burn-rate alerts; (2) command a 45-minute simulated incident with injected surprises, holding roles, mitigating before diagnosing and sending three correct updates on cadence, as judged by two examiners; (3) write a blameless post-mortem within 24 hours whose action items an examiner agrees would have prevented or shortened the incident.

## Industry reality

SRE is a standard title in Indian product companies, global capability centres and cloud providers. The Google SRE books are the shared vocabulary in interviews. PagerDuty's incident response documentation is public and widely adopted. India adds regulatory clocks: CERT-In's directions require reporting listed cyber incidents within 6 hours. In payments, NPCI's 2025 circulars show a network operator turning client retry behaviour into a compliance requirement. Pay data for SREs in India is in the [market map](../../../../06_career_and_market_readiness/01_market_map/roles/OPS_devops_sre_platform_engineering.md).

**Interview questions from this course**

1. *Define an SLO for our checkout service and the alerts that go with it.* Strong answer: journey-based SLIs measured at the edge, good/total definition with exclusions, a target derived from data, 28-day rolling window, multiwindow burn-rate pages and tickets with the actual numbers, an error budget policy.
2. *You are on call; error rate jumps to 20% after a deploy. Walk me through the first 15 minutes.* Strong answer: acknowledge, declare, assign roles if needed, check recent changes, roll back first, verify recovery with the SLI, communicate on cadence, preserve evidence, hand over cleanly, schedule the review.
3. *What is toil and how do you reduce it?* Strong answer: the SRE book's definition, measurement (tickets, surveys), eliminate before automate, self-service, the 50% cap, safety of automation.
4. *Tell me about a public outage you studied and what you would change.* Strong answer: picks one (for example AWS October 2025 or Cloudflare November 2025), explains trigger, propagation, detection, mitigation and recovery bottleneck, and proposes specific controls (validation, staged propagation, backoff, static stability).
5. *Why is MTTR a poor metric, and what would you report instead?* Strong answer: skewed durations make means unstable; incidents differ in kind; DORA's failed deployment recovery time; SLO attainment and error budget burn; time to detect and to mitigate per incident; qualitative learning.

## Resources (free first)

- **Core texts (free):** [*Site Reliability Engineering*](https://sre.google/sre-book/table-of-contents/) (2016), [*The Site Reliability Workbook*](https://sre.google/workbook/table-of-contents/) (2018), [*Building Secure and Reliable Systems*](https://sre.google/books/building-secure-reliable-systems/) (2020). Key chapters: [Embracing Risk](https://sre.google/sre-book/embracing-risk/), [Service Level Objectives](https://sre.google/sre-book/service-level-objectives/), [Implementing SLOs](https://sre.google/workbook/implementing-slos/), [Alerting on SLOs](https://sre.google/workbook/alerting-on-slos/), [Error budget policy](https://sre.google/workbook/error-budget-policy/), [Eliminating Toil](https://sre.google/sre-book/eliminating-toil/), [Being On-Call](https://sre.google/sre-book/being-on-call/), [Managing Incidents](https://sre.google/sre-book/managing-incidents/), [Incident Response](https://sre.google/workbook/incident-response/), [Postmortem Culture](https://sre.google/sre-book/postmortem-culture/), [example post-mortem](https://sre.google/sre-book/example-postmortem/), [Launch checklist](https://sre.google/sre-book/launch-checklist/).
- **Incident practice:** [PagerDuty Incident Response](https://response.pagerduty.com/), [Atlassian incident handbook](https://www.atlassian.com/incident-management/handbook), [incident.io guide](https://incident.io/guide), [LinkedIn School of SRE](https://github.com/linkedin/school-of-sre), [collected post-mortems](https://github.com/danluu/post-mortems), [How they SRE](https://github.com/upgundecha/howtheysre).
- **SLO tooling:** [OpenSLO](https://openslo.com/), [Sloth](https://sloth.dev/), [Pyrra](https://github.com/pyrra-dev/pyrra).
- **Post-mortems used in Chapter 9:** [GitHub 2018](https://github.blog/news-insights/company-news/oct21-post-incident-analysis/), [AWS S3 2017](https://aws.amazon.com/message/41926/), [AWS 2025](https://aws.amazon.com/message/101925/), [Google Cloud 2025](https://status.cloud.google.com/incidents/ow5i3PPK96RduMcb1SsW), [Cloudflare 2019](https://blog.cloudflare.com/details-of-the-cloudflare-outage-on-july-2-2019/), [Cloudflare 2025](https://blog.cloudflare.com/18-november-2025-outage/), [Meta 2021](https://engineering.fb.com/2021/10/05/networking-traffic/outage-details/), [Slack 2021](https://slack.engineering/slacks-outage-on-january-4th-2021/), [CrowdStrike 2024](https://www.crowdstrike.com/wp-content/uploads/2024/08/Channel-File-291-Incident-Root-Cause-Analysis-08.06.2024.pdf).
- **Practice locally:** Prometheus, Grafana, Sloth and Alertmanager on kind; a free PagerDuty developer account or a self-hosted chat (Mattermost) for paging drills.
- **Paid, optional:** Alex Hidalgo, *Implementing Service Level Objectives* (O'Reilly, 2020).

## Sources

All checked 12 Oct 2026.
- AWS, [Summary of the Amazon DynamoDB service disruption](https://aws.amazon.com/message/101925/) (19–20 Oct 2025).
- Google Cloud, [incident report](https://status.cloud.google.com/incidents/ow5i3PPK96RduMcb1SsW) (12 Jun 2025).
- Cloudflare, [18 November 2025 outage](https://blog.cloudflare.com/18-november-2025-outage/).
- GitHub, [October 21 post-incident analysis](https://github.blog/news-insights/company-news/oct21-post-incident-analysis/) (2018).
- MediaNama, [NPCI orders banks to show balance after UPI payments amid outages](https://www.medianama.com/2025/05/223-npci-banks-balance-upi-transaction-guidelines/) (May 2025): four outages March–May 2025; status checks limited to 90 seconds after the transaction (circular dated 26 Apr 2025); 50 balance enquiries per app per customer per 24 hours; peak hours defined.
- DORA, [software delivery performance metrics](https://dora.dev/guides/dora-metrics/) (failed deployment recovery time replaces MTTR).
- InfoQ, [Is MTTR an effective metric?](https://www.infoq.com/news/2022/10/mttr-effective-metric/) (Oct 2022), reporting the VOID's finding that incident durations are positively skewed.
- Google SRE book, [Being On-Call](https://sre.google/sre-book/being-on-call/) (25% on-call cap; eight engineers minimum for a single-site rotation; 2 incidents per 12-hour shift) and [Alerting on SLOs](https://sre.google/workbook/alerting-on-slos/) (burn-rate table).
- [CERT-In Directions, 28 Apr 2022](https://www.cert-in.org.in/PDF/CERT-In_Directions_70B_28.04.2022.pdf) (6-hour reporting).

_Last reviewed: 2026-10_
