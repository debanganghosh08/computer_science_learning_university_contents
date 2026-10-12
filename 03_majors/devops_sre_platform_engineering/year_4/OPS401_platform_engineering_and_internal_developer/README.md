# OPS401 · Platform Engineering and Internal Developer Platforms

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 7 | 4 (≈ 120 hours) | L3 → L4 | [OPS301](../../year_3/OPS301_ci_cd_engineering/README.md); strongly recommended: [OPS303](../../year_3/OPS303_observability_metrics_logs_traces/README.md), [OPS305](../../year_3/OPS305_configuration_management_and_gitops/README.md) | [OPS501](../../year_5/OPS501_frontier_seminar_autonomous_infrastructure/README.md), [OV04A](../../../../04_overlaps/OV04_mlops_ml_platform/OV04A_ml_platform_engineering/README.md), [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) |

Part of the [DevOps, SRE and Platform Engineering major](../../README.md). In Year 3 you built pipelines ([OPS301](../../year_3/OPS301_ci_cd_engineering/README.md)), telemetry ([OPS303](../../year_3/OPS303_observability_metrics_logs_traces/README.md)), SLOs ([OPS304](../../year_3/OPS304_site_reliability_engineering_slos_error_budgets/README.md)) and GitOps ([OPS305](../../year_3/OPS305_configuration_management_and_gitops/README.md)). This course turns them into a product that hundreds of developers, and now coding agents, use without filing tickets: an internal developer platform (IDP). Cloud landing zones and infrastructure modules are owned by the Cloud major ([CLD301](../../../cloud_engineering/year_3/CLD301_cloud_architecture_on_aws_azure_and_google_cloud/README.md), [CLD302](../../../cloud_engineering/year_3/CLD302_infrastructure_as_code_terraform_opentofu/README.md)). This course is about the developer-facing layer built on top of them.

## Why this course matters now

DORA's 2025 research found that 90% of organisations have adopted at least one internal platform. It also found "a direct correlation between a high quality internal platform and an organization's ability to unlock the value of AI", and lists quality internal platforms among its seven AI capabilities. The 2024 report gave the warning: platforms improved individual productivity, team performance and organisational performance, but "can also lead to decreased change stability and throughput" when built badly.

The ecosystem has matured:

- **Backstage**, created at Spotify, is a CNCF incubating project.
- **Crossplane** graduated in the CNCF in October 2025 and is now on its 2.x line.
- **CNCF certifications:** the CNCF launched Cloud Native Platform Engineering Associate (CNPA) and Certified Cloud Native Platform Engineer (CNPE) exams.
- **Team Topologies**, the book that named the "platform team", came out in a second edition in September 2025.

A new user has arrived. Coding agents now create services, read documentation and call platform APIs. A platform with machine-readable golden paths, scoped permissions and audit trails makes them safe and productive; a ticket queue makes them useless. Platform engineers who can treat both humans and agents as users, measure whether the platform helps, and say no to features are among the hardest people to replace in operations.

## Learning outcomes

By the end you can:

1. **Explain** why platforms exist (cognitive load, Team Topologies' team types and interaction modes), and **decide** when an organisation should not build one.
2. **Run** platform product management: user research, journey maps, a roadmap, adoption metrics and deprecations.
3. **Measure** developer experience with DORA, SPACE, DevEx and DX Core 4, combining survey and system data, and **avoid** the known misuses.
4. **Design and ship** golden paths (templates for service, pipeline, telemetry, SLO and security defaults) and **keep** generated services up to date.
5. **Operate** Backstage: software catalog entity model, scaffolder, TechDocs, plugins, permissions and scorecards.
6. **Build** self-service infrastructure as a platform API with Crossplane compositions (or a Terraform-based alternative) with guardrails.
7. **Design** multi-tenancy, policy, identity, secrets and cost visibility defaults for a shared platform.
8. **Run** the platform as a production service with its own SLOs, upgrade strategy and support model.
9. **Expose** platform capabilities safely to AI agents (machine-readable docs, MCP tools, scoped identities, approvals, audit).

## Chapters and lessons

### Chapter 1 · Why platforms (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Cognitive load | Why "you build it, you run it" overloads stream-aligned teams; intrinsic, extraneous and germane load | Count the tools a new developer must learn in a sample company |
| 1.2 Team Topologies | Stream-aligned, platform, enabling and complicated-subsystem teams; collaboration, X-as-a-service and facilitating modes | Redraw an org chart of a 60-engineer company in Team Topologies terms |
| 1.3 Thinnest viable platform | A wiki page can be a platform; the CNCF Platforms white paper's attributes | Design the thinnest viable platform for a 15-engineer startup |
| 1.4 When not to build | Small teams, a managed PaaS that fits, missing product ownership | Write a "no platform yet" memo for one scenario |

**Check your understanding:** (1) What is the difference between a platform team and a renamed operations team? (2) Why can a platform increase cognitive load? (3) When is a wiki page the right platform?

### Chapter 2 · Platform as a product (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Users and research | Developer interviews, shadowing, journey maps from idea to production | Interview 3 developers; build a journey map with timings |
| 2.2 Roadmaps and saying no | Prioritising by user pain and adoption, not by technology | Turn 20 requests into a ranked quarterly roadmap |
| 2.3 Golden paths vs paved roads | Spotify's golden paths and Netflix's paved road: supported, optional, opinionated | Define what is supported, tolerated and unsupported |
| 2.4 Adoption and deprecation | Internal marketing, documentation, migration campaigns, sunset policies | Plan the deprecation of an old deploy tool |

**Check your understanding:** (1) Why should golden paths be optional? (2) What is a sign that you are building for yourselves, not your users? (3) How do you deprecate something 40 teams depend on?

### Chapter 3 · Measuring developer experience (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 DORA | The five delivery metrics and DORA's capabilities (from OPS301) as platform outcomes | Pick which DORA metric each roadmap item should move |
| 3.2 SPACE | Satisfaction, performance, activity, communication and collaboration, efficiency and flow (ACM Queue, 2021) | Map 10 existing metrics onto SPACE; find the gaps |
| 3.3 DevEx and DX Core 4 | Feedback loops, cognitive load and flow state (ACM Queue, 2023); DX Core 4 combining DORA, SPACE and DevEx | Design a 12-question survey and the system metrics paired with it |
| 3.4 Platform metrics | Time to first deploy, onboarding time, template adoption, ticket volume, user satisfaction | Build a platform scorecard with baselines |
| 3.5 Misuse | Ranking individuals, Goodhart's law, survey fatigue, vanity adoption numbers | Critique a "lines of code per engineer" dashboard |

**Check your understanding:** (1) Why pair perception data with system data? (2) Which metric would show that your platform made delivery less stable, as DORA warned? (3) Why must developer-experience data never be used for individual performance reviews?

### Chapter 4 · Golden paths and templates (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 What a golden path contains | Repo, CI, container, deployment, telemetry, SLO, runbook, ownership, security defaults | Write the specification for a "new HTTP service" path |
| 4.2 Templates | Backstage scaffolder actions, Cookiecutter or Copier; parameters and validation | Build a template that creates a repository with CI |
| 4.3 Template drift | Updating hundreds of generated services: Copier updates, automated upgrade PRs, Renovate-style bots | Push a template change to 10 generated repos as PRs |
| 4.4 Workload specifications | Score (CNCF sandbox) and similar developer-facing specs, translated to Kubernetes or Compose | Describe one service in Score; render it two ways |

**Check your understanding:** (1) Why do templates become a liability after a year? (2) What belongs in the template vs in a shared library? (3) What is the risk of a workload spec that hides Kubernetes completely?

### Chapter 5 · Backstage in depth (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Software catalog | Entity kinds (Component, API, Resource, System, Domain, Group, User), `catalog-info.yaml`, relations, ingestion | Model 15 services with owners, APIs and dependencies |
| 5.2 TechDocs and search | Docs-as-code next to services; search across catalog and docs | Publish docs for 3 services and find them by search |
| 5.3 Plugins | New frontend and backend systems, plugin development, Kubernetes and CI plugins | Write a small backend plugin that shows SLO status |
| 5.4 Permissions and scorecards | Permission framework, ownership-based access, production-readiness scorecards | Score every catalog entity against 6 readiness checks |
| 5.5 Running Backstage | It is a framework you operate (upgrades, database, auth), vs commercial portals (Port, Cortex, others) | Upgrade Backstage one minor version; record breakage |

**Check your understanding:** (1) Why is catalog accuracy the hardest part of a portal? (2) What should be true before you show a scorecard to teams? (3) When does buying a portal beat running Backstage?

### Chapter 6 · Self-service infrastructure (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Platform APIs | Declarative requests ("I need a Postgres database, small, in Mumbai") vs tickets | Write the API for 3 resource types |
| 6.2 Crossplane | Composite resource definitions, compositions with functions, providers; Crossplane 2.x namespaced resources | Provision a database and a bucket via a composite resource on kind |
| 6.3 Alternatives | Terraform modules behind a portal or pull-request automation; Kratix promises; managed IDP orchestrators | Implement the same request with Terraform modules; compare |
| 6.4 Guardrails in the API | Allowed regions (data residency), sizes, encryption, tags and owners enforced by schema and policy | Reject a request for a non-approved region |

**Check your understanding:** (1) Why is a composite resource a contract, and how do you version it? (2) What do you lose by hiding cloud details? (3) How does the platform API enforce data-location rules?

### Chapter 7 · Tenancy, identity, policy and cost (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Multi-tenancy | Namespaces, quotas, network policies, virtual clusters (vCluster), cluster-per-team trade-offs | Give 3 teams isolated environments on one cluster |
| 7.2 Identity defaults | Workload identity, SSO, short-lived credentials, least-privilege templates | Make every generated service use workload identity |
| 7.3 Policy | Kyverno or Gatekeeper policies as platform defaults; exceptions with expiry | Ship 8 policies with an exception workflow |
| 7.4 Cost visibility | OpenCost (CNCF incubating) per team and service; showback | Show each team its monthly cost in the portal |

**Check your understanding:** (1) When is a namespace not enough isolation? (2) Why must policy exceptions expire? (3) What changes when teams can see their own costs?

### Chapter 8 · Paved roads for delivery and runtime (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Delivery | OPS301 pipelines and OPS305 GitOps as reusable building blocks | Wire the template to your reusable workflows |
| 8.2 Telemetry and SLOs by default | OpenTelemetry, dashboards and SLO templates generated with the service | Generate an SLO and alerts for each new service |
| 8.3 Ownership and on-call metadata | Owners, escalation and runbooks in the catalog | Page the right team from catalog metadata |
| 8.4 Production readiness | Automated checks replacing a PRR meeting where possible | Block promotion to prod for services failing readiness |

**Check your understanding:** (1) What should every new service get "for free"? (2) Why should ownership live in the catalog, not in a wiki? (3) Which readiness checks still need a human?

### Chapter 9 · The platform is production (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Platform SLOs | CI time-to-green, provisioning time, portal availability, deployment success | Define and alert on 4 platform SLOs |
| 9.2 Blast radius | One bad template or policy affects every team; staged platform changes | Roll a policy change to 10% of namespaces first |
| 9.3 Upgrades | Kubernetes, Backstage, Crossplane and providers on a schedule; compatibility matrices | Write an upgrade calendar for a year |
| 9.4 Support model | Office hours, documentation first, ticket triage, platform on-call | Design a support model with response targets |

**Check your understanding:** (1) Why can a platform outage be worse than an application outage? (2) How do you test a template change before everyone gets it? (3) What should the platform team page for?

### Chapter 10 · Platforms for AI and data workloads (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 GPU self-service | Requesting accelerators, quotas, Dynamic Resource Allocation (GA in Kubernetes 1.34), queueing for shared GPUs | Template a GPU job with quota and expiry |
| 10.2 Model serving paths | A golden path for inference services with autoscaling and SLOs (see [CLD404](../../../cloud_engineering/year_4/CLD404_ai_infrastructure_in_the_cloud_gpus_inference/README.md)) | Generate an inference service from a template |
| 10.3 LLM gateways as platform services | Central keys, rate limits, cost attribution, model allow-lists | Put two model providers behind one gateway with per-team budgets |
| 10.4 Data platform touchpoints | Self-service databases, streams and buckets with ownership and retention | Add a "managed topic" resource to the platform API |

**Check your understanding:** (1) Why should model API keys be a platform concern? (2) What does a GPU quota without expiry lead to? (3) Which AI workloads do not fit a stateless service template?

### Chapter 11 · Platforms for agents (weeks 11–12)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Agents as users | Coding agents creating services, reading docs and calling APIs; DORA's "AI-accessible internal data" capability | Watch an agent use your portal; log where it fails |
| 11.2 Machine-readable platforms | Catalog APIs, structured docs, templates with validated parameters | Make your golden path usable from a CLI with JSON output |
| 11.3 Exposing tools safely | MCP servers for platform actions, scoped agent identities, approvals for risky actions, audit | Build an MCP tool "create preview environment" with approval for prod |
| 11.4 Guardrails | Policies apply to agents as to humans; rate limits; separate dev and prod credentials (the 2025 Replit production-database deletion as a cautionary case) | Prove an agent cannot touch prod data from a dev task |

**Check your understanding:** (1) Why is a golden path more important for an agent than for a senior engineer? (2) What should an agent never be able to do without a human? (3) How would you audit everything agents did on your platform last week?

### Chapter 12 · Strategy and the business case (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Build, buy or assemble | Backstage plus open source vs commercial portals and orchestrators; total cost | Write a decision record with three options |
| 12.2 Funding and ROI | Time saved, incidents avoided, onboarding speed; honest uncertainty | Build an ROI estimate with ranges, not single numbers |
| 12.3 Migrations | Strangler approach for old tooling, migration campaigns, reporting | Plan a 2-quarter migration for 40 services |
| 12.4 The platform team's operating model | Skills mix, a product manager for the platform, quarterly reviews with users, a team charter | Write the charter for a 5-person platform team |

**Check your understanding:** (1) Why do ROI numbers for platforms need ranges? (2) What is the risk of "buy" for a platform core? (3) How do you know the migration is done?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Cognitive-load audit | Team Topologies map |
| 2 | 2 | Lab 2 · User research | Journey map; P1 starts |
| 3 | 3 | Lab 3 · DevEx survey design | **P1 due** |
| 4 | 4 | Lab 4 · Template and drift | Template + upgrade PRs |
| 5 | 5 | Lab 5 · Backstage catalog | Catalog of 15 services; P2 starts |
| 6 | 6 | Lab 6 · Crossplane composition | Self-service DB |
| 7 | 7 | Lab 7 · Tenancy, policy, cost | Mid-term (AI off) |
| 8 | 8 | Paved-road integration | **P2 due** |
| 9 | 9 | Lab 8 · Platform SLOs | SLO dashboard |
| 10 | 10 | Lab 9 · GPU and LLM gateway | Template + budgets |
| 11 | 11 | Lab 10 · MCP tool with approvals | Audit log |
| 12 | 11 | Agent usability study | Failure log; P3 design review |
| 13 | 12 | Decision record and ROI | Strategy memo |
| 14 | — | P3 user test and demo day | **P3 due** |
| 15 | Review | Design exam and oral | Final |

## Working with AI in this course

- **Use AI for:** generating Backstage plugin scaffolds, template boilerplate and Crossplane compositions; summarising interview notes into themes (then checking against the transcripts); drafting docs; acting as a simulated "new developer" to test your golden path. Named tools: Claude Code, GitHub Copilot, Cursor, any MCP-capable assistant.
- **Do without AI (drills):** user interviews (people, not models, are your users); the roadmap ranking; the decision record's trade-off section; the mid-term and design exam.
- **Verify AI output by:** running every template end to end in CI with a fresh repository; testing compositions against the provider with policy checks; checking that generated docs match behaviour by having a classmate follow them; checking agent access with negative tests (it must fail to reach prod).
- **Where AI still fails here (show it):** in Lab 10 and the agent usability study, record where an agent misuses your platform: inventing template parameters, skipping required ownership fields, retrying a failing provisioning request in a loop, or asking for broader permissions. Each failure is a design input: fix the platform, not just the prompt.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs 1–10 | 20% |
| Projects P1 / P2 / P3 | 5% / 15% / 30% |
| Mid-term (AI off) | 10% |
| Design exam (3 hours, AI off) + oral | 20% |

**Mastery gate.** You pass when you can: (1) take an unfamiliar organisation description and, in 3 hours without AI, produce a platform strategy (team topology, thinnest viable platform, first three golden paths, metrics, and what not to build) that two examiners judge feasible; (2) show a working golden path that takes a new developer from nothing to a service running in a dev environment, with CI, telemetry and an SLO, in under 15 minutes; (3) show evidence from at least 5 real users (classmates) that your platform improved one measured developer-experience metric.

## Industry reality

Platform engineer is now a common title next to DevOps and SRE ([market map](../../../../06_career_and_market_readiness/01_market_map/roles/OPS_devops_sre_platform_engineering.md)). Spotify created Backstage and released it as open source; it is now a CNCF incubating project. The CNCF publishes a [Platforms white paper](https://tag-app-delivery.cncf.io/whitepapers/platforms/) and a [Platform Engineering Maturity Model](https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/), and runs CNPA, CNPE and Certified Backstage Associate exams. DORA's 2024 and 2025 research gives you language for the trade-off interviewers probe: platforms help, but only if they are built as products and measured.

**Interview questions from this course**

1. *We have 30 teams deploying differently. How would you start a platform?* Strong answer: user research before tools; map journeys and pain; thinnest viable platform; one golden path for the most common service type; measure baseline (DORA, time to first deploy, survey); X-as-a-service interaction; adoption by attraction, not mandate.
2. *How do you measure whether a platform is working?* Strong answer: DORA metrics for teams on and off the platform, DevEx survey (feedback loops, cognitive load, flow), adoption and retention, time to first deploy, platform SLOs, ticket volume; pairs perception with system data; warns about ranking teams.
3. *Design self-service databases for developers.* Strong answer: a declarative API (Crossplane composite or Terraform module), sizes and regions as enums, encryption and backups by default, ownership and cost tags, policy enforcement, connection secrets delivered via external secrets, day-2 operations (resize, restore, delete protection), versioning of the API.
4. *How do you roll out a change to a template used by 300 services?* Strong answer: versioned templates, automated upgrade PRs, canary group first, tests in each generated repo, scorecard tracking of adoption, deprecation dates, support for laggards.
5. *How would you let coding agents use your platform safely?* Strong answer: same golden paths and policies as humans; scoped, short-lived agent identities; read-only by default; approvals for prod or destructive actions; dev and prod separation; audit logs; rate limits; machine-readable docs and validated parameters.

## Resources (free first)

- **Core reading:** CNCF TAG App Delivery, [Platforms white paper](https://tag-app-delivery.cncf.io/whitepapers/platforms/) and [Platform Engineering Maturity Model](https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/); [DORA capabilities](https://dora.dev/capabilities/) (including platform engineering and the AI capabilities) and [2024 report](https://dora.dev/research/2024/dora-report/); Forsgren et al., [The SPACE of Developer Productivity](https://queue.acm.org/detail.cfm?id=3454124) (ACM Queue, 2021); Noda et al., [DevEx: What Actually Drives Productivity](https://queue.acm.org/detail.cfm?id=3595878) (ACM Queue, 2023); [DX Core 4](https://getdx.com/research/measuring-developer-productivity-with-the-dx-core-4/); [Team Topologies key concepts](https://teamtopologies.com/key-concepts).
- **Tools:** [Backstage docs](https://backstage.io/docs/overview/what-is-backstage), [Crossplane docs](https://docs.crossplane.io/), [Score](https://score.dev/), [Kratix](https://kratix.io/), [vCluster](https://www.vcluster.com/), [OpenCost](https://github.com/opencost/opencost), [Kyverno](https://kyverno.io/).
- **Practice locally:** Backstage's local development setup, Crossplane with provider-kubernetes or LocalStack on kind; no cloud account needed.
- **Certifications:** [CNPA, CNPE and Certified Backstage Associate](https://www.cncf.io/training/certification/).
- **Paid, worth it:** Skelton and Pais, *Team Topologies*, 2nd ed. (IT Revolution, 2025); Camille Fournier and Ian Nowland, *Platform Engineering* (O'Reilly, 2024).

## Sources

All checked 12 Oct 2026.
- Google Cloud, [Announcing the 2025 DORA report](https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report) (90% platform adoption; platform quality and AI value); DORA, [AI capabilities in the capabilities catalog](https://dora.dev/capabilities/).
- DORA, [Accelerate State of DevOps Report 2024](https://dora.dev/research/2024/dora-report/) (platform engineering can decrease change stability and throughput).
- CNCF maturity (Backstage incubating 15 Mar 2022; Crossplane graduated 28 Oct 2025; OpenCost incubating; Score sandbox; KubeVela incubating) from the [CNCF landscape](https://github.com/cncf/landscape) data file; Backstage 1.55 and Crossplane 2.4 from GitHub releases.
- [CNCF certifications](https://www.cncf.io/training/certification/) (CNPA, CNPE, CBA).
- Team Topologies, [book page](https://teamtopologies.com/book) (second edition published 23 Sep 2025).
- DX, [DX Core 4](https://getdx.com/research/measuring-developer-productivity-with-the-dx-core-4/) (encapsulates DORA, SPACE and DevEx).
- Kubernetes, [DRA GA in v1.34](https://kubernetes.io/blog/2025/09/01/kubernetes-v1-34-dra-updates/).
- heise online, [Replit deletes production database](https://heise.de/-10499597) (July 2025).

_Last reviewed: 2026-10_
