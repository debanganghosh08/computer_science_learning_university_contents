# NET305 · Labs and projects

Use free tools: a ServiceNow Personal Developer Instance or GLPI/iTop (open source) for ITSM, Zabbix and Prometheus with Grafana for monitoring, and the lab networks and servers you built in NET301–NET303. Ticket datasets are synthetic or public; never paste real users' tickets into an AI service without the data owner's approval.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Service model and value-chain map | Describe 3 services (email, Wi-Fi, a business app) with owners, CIs, users and outcomes; map them to ITIL 4 and Version 5 views | Service definitions and two diagrams | 3 h |
| 2 · Catalogue and AI classifier test | 5 catalogue items with approvals; measure an LLM's ticket classification on 100 labelled synthetic tickets | Catalogue config; confusion matrix and error analysis | 4 h |
| 3 · Major-incident simulation | Run a scripted WAN outage with assigned roles, bridge, decision log and timed updates | Timeline, decision log, three stakeholder updates | 4 h |
| 4 · Root-cause analysis | Apply change analysis and a fault tree to a provided case; write a blameless problem record | Problem record with corrective actions, owners and dates | 4 h |
| 5 · Change process and pipeline link | Define standard/normal/emergency changes; attach NET303 pipeline evidence to change records automatically | Process document; screenshots or API logs of linked records | 4 h |
| 6 · CMDB discovery and reconciliation | Discover the lab, reconcile with NetBox and AD, compute a CMDB health score | Health report before and after reconciliation | 5 h |
| 7 · Zabbix monitoring | Templates for network devices and servers, triggers with dependencies, maintenance windows | Zabbix export; a test showing one alert for a WAN failure | 4 h |
| 8 · Prometheus and noise reduction | SNMP, node and blackbox exporters; Alertmanager grouping and inhibition; cut a noisy rule set by 70% | Alert counts before and after against a recorded failure replay | 5 h |
| 9 · Runbook automation | Three runbooks; automate diagnostics in AWX or Rundeck with approvals and logs | Runbooks, job definitions, audit log | 4 h |
| 10 · ITSM tool integration | Monitoring → incident, discovery → CMDB, pipeline → change in one tool | Working integrations with a demo script | 5 h |

## Projects

### P1 · Major-incident playbook and simulation kit (L1, ~6 hours)

**Real-world inspiration.** Public reviews of the 2022 Rogers outage found that staff could not even talk to each other because they lacked backup connectivity from other providers; CERT-In requires certain cyber incidents to be reported within 6 hours. A playbook decides how the first hour goes.

**What to build.** A major-incident playbook for a mid-sized organisation (illustrative: a regional bank with 60 branches): priority matrix, roles and their checklists, out-of-band communication plan, update templates, regulatory notification steps, hand-off and closure criteria; plus a simulation kit (scenario, injects every 5 minutes, observer scoring sheet).

**Acceptance criteria**
- Three classmates who did not write it run a 45-minute simulation from the kit alone, and the observer sheet shows every role filled within 10 minutes.
- Stakeholder updates go out on the stated rhythm (for example, every 30 minutes) with no missed update.
- The regulatory decision ("is this reportable, to whom, by when?") is made and logged within the simulation.
- The playbook fits in 8 pages; each role's checklist fits on one page.

**Stretch goals.** Add a cyber-incident variant coordinated with a security team; integrate the update templates into your ITSM tool.

**What it proves to an employer.** You can bring order to an outage, the skill operations managers look for when promoting engineers to leads.

### P2 · Monitoring that pages once (L2, ~15 hours)

**Real-world inspiration.** NOCs serving many clients from Indian delivery centres handle thousands of alerts a day; most are noise, and real failures get lost. The estate below is your NET301–NET303 lab treated as a client network.

**What to build.** Full monitoring for the lab estate in Zabbix or Prometheus: user-facing synthetic checks, device and server health, interface errors and saturation, BGP and OSPF state, certificate expiry, with dependency trees, alert routing by service, maintenance windows and dashboards. Replay 5 recorded failure scenarios (WAN loss, core switch failure, disk full, certificate expiry, BGP flap) and tune until each produces the right page.

**Acceptance criteria**
- For each of the 5 scenarios, exactly one page reaches the on-call engineer for the root failure, and dependent alerts are suppressed or grouped (shown in Alertmanager or Zabbix logs).
- Time from failure to page is under 2 minutes for every scenario.
- Over a 24-hour run with normal lab activity, there are zero pages (no false positives).
- Each alert links to a runbook from Lab 9.
- A one-page design explains thresholds and why each alert exists.

**Stretch goals.** Export the same alerts into your ITSM tool as incidents with CI links; measure what happens to page volume if one dependency is removed.

**What it proves to an employer.** You can run a monitoring system that people trust, which separates a NOC lead from a NOC operator.

### P3 · An operations-in-a-box service with measured outcomes (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** NASSCOM describes Indian providers moving to outcome-based, risk-sharing contracts; ITIL (Version 5) positions itself as AI-native. A provider that can show fewer incidents, faster recovery and safe AI assistance wins those contracts. The client and contract below are illustrative.

**What to build.** A complete managed-service operation for the lab estate: an SLA and OLA set with measurable targets; an ITSM tool configured for incidents, problems, changes, requests and CMDB with discovery and reconciliation; monitoring from P2 integrated as event management; automated runbooks with approvals; an AI assistant that classifies and summarises tickets and suggests knowledge articles, evaluated and limited; and monthly service reporting. Then run a two-week operating period (compressed into scheduled drills) with injected failures, requests and changes.

**Acceptance criteria**
- At least 10 injected incidents, 20 requests and 8 changes are processed; the monthly report shows SLA attainment, MTTA, MTTR (with the definition used), change success rate and reopen rate.
- Mean time to restore in fault drills improves by at least 30% between the first and second week, with the reason documented (runbook, automation or alert change).
- CMDB health score stays above 90% across the period, measured by your Lab 6 method.
- The AI assistant's ticket classification reaches at least 90% accuracy on a held-out set of 100 tickets, P1/P2 tickets are never auto-routed without human confirmation, and all assistant suggestions are logged.
- No change is executed without a linked record and evidence; one deliberately failed change is detected by post-checks and rolled back within its window.
- A client-facing service review (20 minutes) presents results, problems found and the improvement plan.

**Stretch goals.** Price the service per device per month with assumptions; model the effect of AI automation on staffing with explicit, labelled assumptions.

**What it proves to an employer.** You can design and run an IT operation with numbers that a client can verify, including safe use of AI, which is what infrastructure-management leaders are hired to deliver.

## Feeds into

- [NET403 AIOps and Intent-Based Networking](../../year_4/NET403_aiops_and_intent_based_networking/README.md): event management and alert data become AIOps inputs.
- [NET404 Enterprise Architecture and Cloud Migration](../../year_4/NET404_enterprise_architecture_and_cloud_migration/README.md): CMDB and service maps are the base for application portfolio analysis.
- [IND401 Industry Co-op Studio](../../../../05_shared_years_3_to_5/IND401_industry_co_op_studio/README.md): most co-op placements in infrastructure start inside these processes.
- [OPS304 Site Reliability Engineering](../../../devops_sre_platform_engineering/year_3/OPS304_site_reliability_engineering_slos_error_budgets/README.md) as an elective for SLO-based operations.
