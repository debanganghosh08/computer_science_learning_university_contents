# OPS · DevOps, SRE and Platform Engineering: roles and market (2026)

| Learning path | Interview loop | AI impact | Market overview |
|---|---|---|---|
| [DevOps, SRE and Platform Engineering major](../../../03_majors/devops_sre_platform_engineering/README.md) | [AI-driven interviews](../../04_ai_driven_interviews/) | [Matrix row](../ai_impact_matrix.md) | [Market map](../README.md) |

All figures were checked in October 2026. Paragraphs marked **Analysis** are interpretation, not measurement.

## Role titles and seniority ladder

| Level | Common titles |
|---|---|
| Entry | Junior DevOps Engineer, Build and Release Engineer, Associate SRE, Systems Engineer |
| Mid | DevOps Engineer, Site Reliability Engineer (SRE), Platform Engineer |
| Senior | Senior SRE, Senior Platform Engineer, Observability Engineer, Production Engineer |
| Staff and above | Staff SRE, Principal Platform Engineer, Head of Infrastructure |

Three related jobs share this family:

- **DevOps engineer**: builds and runs CI/CD pipelines and infrastructure automation.
- **Site reliability engineer**: owns reliability targets (SLOs), incident response and capacity.
- **Platform engineer**: builds the internal developer platform that other teams use to ship.

## What the work looks like day to day

- Build and speed up CI/CD pipelines (OPS301).
- Maintain Linux hosts, containers and Kubernetes clusters (OPS302).
- Instrument services with metrics, logs and traces using OpenTelemetry (OPS303).
- Define service level objectives (SLOs) and error budgets; tune alerts so on-call is humane (OPS304).
- Lead or support incident response, then write blameless postmortems.
- Manage configuration and deployments through GitOps (OPS305).
- Build golden paths, templates and self-service tools for developers (OPS401).

## Demand signals

- **Global employer survey.** "DevOps Engineer" is among the 15 fastest-growing jobs to 2030 ([WEF 2025](https://reports.weforum.org/docs/WEF_Future_of_Jobs_Report_2025.pdf)).
- **Platform adoption.** 90% of organisations in DORA's 2025 research had adopted at least one internal platform ([DORA 2025](https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report)).
- **Shift from classic administration.** BLS projects network and computer systems administrators to decline 4% from 2025 to 2035, partly because tasks shift to "DevOps-focused software developers" and outsourced network services ([BLS](https://www.bls.gov/ooh/computer-and-information-technology/network-and-computer-systems-administrators.htm)). The work moves into code; it does not disappear.
- **US postings.** Indeed's "IT Infrastructure, Operations & Support" index was 69.3 on 2 Oct 2026 (1 Feb 2020 = 100), up from 64.0 a year earlier ([Indeed Hiring Lab data](https://github.com/hiring-lab/job_postings_tracker)).
- **Least-automated area of development.** Only 20% of AI users use AI for "deploying, operating, or troubleshooting production systems", against 67% for generating code ([Stack Overflow, Oct 2026](https://stackoverflow.blog/2026/10/06/the-results-of-the-2026-developer-survey-are-here/)).

## How AI is changing the role

**Automated or mostly automated.** Pipeline YAML, Dockerfiles, Helm values, dashboard queries, alert rule drafts, runbook drafts, log and incident-timeline summaries.

**Augmented.** Incident triage (correlating alerts, deploys and logs), root-cause hypotheses, capacity forecasts, postmortem writing. This is the AIOps and agentic operations area (OPS403).

**Growing in value.**

- Reliability engineering for AI-accelerated delivery. DORA found AI adoption positively related to throughput but still negatively related to delivery stability; "AI doesn't fix a team; it amplifies what's already there" ([DORA 2025](https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report)). More code shipped faster means more need for safe rollouts, tests in the pipeline and fast rollback.
- Incident command and judgement under pressure.
- Safe automation: giving operations agents the right permissions, dry-runs and approval gates (OPS501).
- Platform product thinking: treating developers as users.

**Analysis.** Operations is where AI output meets real consequences. That keeps humans in charge of production changes for now, and it makes reliability skills more valuable as the volume of AI-written code grows.

## Pay (indicative)

| Market | Role in source | Figure | Type | Source |
|---|---|---|---|---|
| US | Network and computer systems administrators (closest official occupation for operations work) | Median $99,130; 10th $62,640; 90th $155,050 (May 2025) | Official survey | [BLS](https://www.bls.gov/ooh/computer-and-information-technology/network-and-computer-systems-administrators.htm) |
| US | Software developers (many SRE and platform engineers are counted here) | Median $135,980 (May 2025) | Official survey | [BLS](https://www.bls.gov/ooh/computer-and-information-technology/software-developers.htm) |
| India | DevOps Engineer | Average base ₹10.0 lakh; base range ₹4.0–30 lakh; under 1 year ≈₹4.5 lakh total (896 profiles, Jul 2026) | Self-reported, whole market | [Payscale](https://www.payscale.com/research/IN/Job=Development_Operations_(DevOps)_Engineer/Salary) |
| India | Site Reliability Engineer | Average base ₹17.5 lakh; base range ₹4.05–30 lakh (272 profiles, Jun 2026) | Self-reported, whole market | [Payscale](https://www.payscale.com/research/IN/Job=Site_Reliability_Engineer_(SRE)/Salary) |

The official US data has no DevOps or SRE category, so US figures here are proxies.

## The hiring loop

Typical loop (varies by company):

1. Linux and networking troubleshooting: "a server is slow", "DNS fails intermittently". Interviewers watch your method, not memorised commands.
2. Coding or scripting: automation in Python, Go or Bash; sometimes a DSA round for SRE roles at product companies.
3. System design with a reliability focus: design monitoring and alerting for a service, a deployment pipeline, or a multi-region failover.
4. Incident scenario: you are on call, alerts fire, the dashboard is red. What do you do, in what order, and how do you communicate?
5. Behavioural: an outage you caused or fixed; how you improved on-call.

See [AI-driven interviews](../../04_ai_driven_interviews/).

## Durable skills that make you hard to replace

- Linux internals: processes, memory, file systems, networking stack.
- Networking and TLS.
- Observability design and query languages (PromQL, LogQL or equivalent).
- SLO maths and error-budget policy.
- Incident management and calm communication.
- Kubernetes internals and failure modes.
- Writing automation that is tested, reviewed and safe to rerun.

## Adjacent roles and transitions

- **Cloud engineering** ([CLD](CLD_cloud_engineering.md)).
- **DevSecOps**: overlap OV03 ([SEC](SEC_cybersecurity_defense.md)).
- **MLOps and ML platform**: overlap OV04 ([MLE](MLE_machine_learning_engineering.md)).
- **Agent infrastructure**: overlap OV12 ([AIE](AIE_ai_engineering.md)).
- **Backend**: reliability-minded backend engineering ([BE](BE_backend_engineering.md)).

## Sources

All checked October 2026.

- WEF, Future of Jobs Report 2025. https://reports.weforum.org/docs/WEF_Future_of_Jobs_Report_2025.pdf
- DORA 2025 (24 Sep 2025). https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report
- BLS, Occupational Outlook Handbook: Network and Computer Systems Administrators; Software Developers (2025–35; May 2025 pay; modified 27 Aug 2026). https://www.bls.gov/ooh/computer-and-information-technology/network-and-computer-systems-administrators.htm ; https://www.bls.gov/ooh/computer-and-information-technology/software-developers.htm
- Indeed Hiring Lab, job postings tracker (to 2 Oct 2026). https://github.com/hiring-lab/job_postings_tracker
- Stack Overflow, 2026 survey results blog (6 Oct 2026). https://stackoverflow.blog/2026/10/06/the-results-of-the-2026-developer-survey-are-here/
- Payscale India: DevOps Engineer; Site Reliability Engineer (self-reported; 12 Oct 2026). https://www.payscale.com/research/IN/Job=Development_Operations_(DevOps)_Engineer/Salary ; https://www.payscale.com/research/IN/Job=Site_Reliability_Engineer_(SRE)/Salary

_Last reviewed: 2026-10_
