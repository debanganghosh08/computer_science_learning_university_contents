# OPS401 · Labs and projects

Everything runs locally: Backstage in development mode, two kind or k3d clusters, Crossplane with provider-kubernetes (and optionally LocalStack for cloud-like resources), Argo CD or Flux from [OPS305](../../year_3/OPS305_configuration_management_and_gitops/README.md), and the telemetry stack from [OPS303](../../year_3/OPS303_observability_metrics_logs_traces/README.md). Classmates act as your users: you will interview them, watch them use your platform and measure the result. Labs 1, 2 and 3 are done without AI assistance.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Cognitive-load audit | Count tools, steps and handoffs a new developer faces in a sample company (or your own Year 3 projects); map it to Team Topologies | Tool inventory, team map, top 5 sources of extraneous load | 3 h |
| 2 · User research | Interview 3 developers; shadow one deploying a change; build a timed journey map | Interview notes, journey map with minutes per step | 4 h |
| 3 · DevEx survey design | Design a 12-question survey (feedback loops, cognitive load, flow) and pair each question with a system metric | Survey, metric pairing, analysis plan | 3 h |
| 4 · Template and drift | Scaffolder template for an HTTP service; change the template; push upgrade PRs to 10 generated repos | Template, 10 PR links, merge rate | 5 h |
| 5 · Backstage catalog | Catalog 15 services with owners, APIs, systems and dependencies; TechDocs for 3 | `catalog-info.yaml` files, dependency graph screenshot | 5 h |
| 6 · Crossplane composition | A composite resource for "database" (and "bucket") with sizes as enums, region allow-list and connection secrets | XRD, composition, a rejected bad request | 6 h |
| 7 · Tenancy, policy, cost | Three tenants on one cluster with quotas, network policies, 8 Kyverno policies and OpenCost showback | Policies, exception workflow, cost per tenant | 5 h |
| 8 · Platform SLOs | SLOs and alerts for CI time-to-green, provisioning time, portal availability and deploy success | SLO specs, alert tests, dashboard | 4 h |
| 9 · GPU template and LLM gateway | A GPU job template with quota and expiry (simulated on CPU if needed); two model providers behind one gateway with per-team budgets | Template, gateway config, budget-exceeded evidence | 5 h |
| 10 · MCP tool with approvals | An MCP server exposing "create preview environment" and "get service status"; prod actions need human approval; everything audited | Server code, negative tests, audit log | 5 h |

## Projects

### P1 · Developer journey audit (L1, ~6 hours)

**Real-world inspiration:** DORA's 2024 finding that platforms can reduce stability and throughput when built without a user focus ([DORA 2024](https://dora.dev/research/2024/dora-report/)), and the DevEx framework's focus on feedback loops, cognitive load and flow ([ACM Queue, 2023](https://queue.acm.org/detail.cfm?id=3595878)).

**What to build:** a measured audit of how a new developer gets a new service to production in an existing setup (your Year 3 projects, a classmate's team, or an open-source project's contributor flow), with a proposal for the first golden path.

**Acceptance criteria:**
- **Measured journey:** at least 10 steps, each timed from observation (not estimate), with waits separated from work.
- **Users:** at least 3 interviews and 1 observed session, with quotes linked to steps.
- **Findings:** the top 3 friction points are quantified (minutes or failure rate) and ranked by impact on all users.
- **Proposal:** a one-page thinnest-viable-platform plan with a success metric and a baseline value for it.

**Stretch goals:** run the DevEx survey from Lab 3 with at least 8 respondents and report results with honest caveats about sample size.

**What it proves to an employer:** you start platform work from users and evidence, not from tools, which is the main thing that separates platform engineers from tool administrators.

### P2 · Golden path v1 (L2, ~15 hours)

**Real-world inspiration:** Spotify's golden paths and its open-source [Backstage](https://backstage.io/docs/overview/what-is-backstage) scaffolder.

**What to build:** a Backstage template that creates a production-ready service: repository, CI from [OPS301](../../year_3/OPS301_ci_cd_engineering/README.md), GitOps deployment from [OPS305](../../year_3/OPS305_configuration_management_and_gitops/README.md), OpenTelemetry instrumentation, a dashboard, an SLO with burn-rate alerts from [OPS304](../../year_3/OPS304_site_reliability_engineering_slos_error_budgets/README.md), a runbook stub, catalog registration with owner and on-call, and security defaults (non-root, pinned actions, policies).

**Acceptance criteria:**
- **Speed:** from clicking "create" to the service answering in the dev environment takes under 15 minutes, with zero tickets or manual steps.
- **Unaided use:** 3 classmates who did not build it complete the path using only the portal and docs; you record their times and every point of confusion.
- **Readiness:** the generated service passes 100% of your 6 production-readiness scorecard checks on day one.
- **Upgradability:** a template change reaches all services generated during the project as automated PRs that pass CI.

**Stretch goals:** a second golden path (worker consuming a queue); a Score-based workload spec rendered to Kubernetes.

**What it proves to an employer:** you can build the most visible artefact of a platform team and prove that real users can use it.

### P3 · An internal developer platform MVP, ready for humans and agents (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** DORA 2025 found that 90% of organisations have adopted at least one internal platform and tied platform quality to getting value from AI ([announcement](https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report)). The CNCF [Platforms white paper](https://tag-app-delivery.cncf.io/whitepapers/platforms/) lists the capabilities. The July 2025 Replit incident, in which an agent deleted a production database ([heise](https://heise.de/-10499597)), shows why agent access must be designed in. The company you design for is an *illustrative scenario*.

**What to build:** an IDP for an imagined 60-developer company with:
- the P2 golden path;
- self-service databases and buckets through Crossplane compositions with region allow-lists (for example, only Indian regions for personal data);
- multi-tenancy with policies and exceptions;
- per-team cost showback;
- platform SLOs;
- an MCP server so coding agents can create services and preview environments through the same golden path, with scoped identities, human approval for anything touching prod, and a complete audit log;
- a support model and a 2-quarter roadmap.

**Acceptance criteria:**
- **Self-service:** a team gets a database with backups, encryption, ownership tags and connection secrets in under 10 minutes with no ticket.
- **Guardrails:** a test suite of 10 non-compliant requests (wrong region, no owner, oversized, privileged pod, unpinned image) is rejected 10/10, each with a clear error message.
- **Agents:** an agent completes "create a new service and a preview environment" end to end; a negative test suite of 6 attempts (prod data access, deleting resources, escalating its own permissions) is blocked 6/6 and logged.
- **Platform SLOs:** four platform SLOs are defined, alerted on and met for a 7-day soak.
- **Users:** at least 5 users complete a task script; the System Usability Scale score is 70 or higher, or you show what you changed after a lower score and the re-test result.
- **Evolution:** a template upgrade is rolled out to at least 10 generated services through automated PRs, with a canary group first.

**Stretch goals:** a GPU or LLM-gateway golden path from Lab 9; a DORA-metrics view per team in the portal.

**What it proves to an employer:** you can build a platform as a product, with guardrails for both humans and agents and evidence that it works. This is staff-level platform work and a strong portfolio piece for the [flagship industry project](../../../../06_career_and_market_readiness/05_industry_projects/OPS_devops_sre_platform_engineering.md).

## Feeds into

- [OPS501 Frontier Seminar](../../year_5/OPS501_frontier_seminar_autonomous_infrastructure/README.md): platforms as the substrate for autonomous operations.
- [OV04A ML Platform Engineering](../../../../04_overlaps/OV04_mlops_ml_platform/OV04A_ml_platform_engineering/README.md) and [OV04B LLMOps at Scale](../../../../04_overlaps/OV04_mlops_ml_platform/OV04B_llmops_at_scale/README.md): Chapter 10 extended to ML platforms.
- [OV12A Running Agents in Production](../../../../04_overlaps/OV12_agent_infrastructure_platform/OV12A_running_agents_in_production_sandboxes_durable/README.md): Chapter 11 extended to agent infrastructure.
- [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) and [LCH502](../../../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md): P3 is a natural capstone or startup seed.
