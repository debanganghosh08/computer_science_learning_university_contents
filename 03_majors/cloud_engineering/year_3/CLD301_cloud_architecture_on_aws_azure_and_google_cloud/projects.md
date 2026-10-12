# CLD301 · Labs and projects

Labs run on one provider of your choice unless stated; P3 needs two. Before Lab 1, create a budget alarm at a small amount (for example US$5) and an alert at 50%, 80% and 100%. Tear down every lab the same day. Labs 4 and 8 are done without AI assistants.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Account safety and API tracing | Secure a fresh account (MFA on root/global admin, SSO user, budget alarm, audit logging on), then trace one VM-create call per provider with `--debug` | CLI output of budget and audit-log settings, and an annotated list of API endpoints hit | 3 h |
| 2 · Arm versus x86 | Run the same HTTP service on an Arm and an x86 instance of similar size and load-test both with `k6` or `hey` | Requests per second, p99 latency and cost per 1,000 requests for each, with a recommendation | 4 h |
| 3 · Two-AZ VPC by hand | Build public, private and data subnets in two AZs with route tables and one NAT, through the console or CLI (no IaC yet) | Diagram, `describe` output, and proof that a private instance reaches the internet only through NAT | 4 h |
| 4 · IAM evaluation drills (no AI) | Predict allow/deny for 12 prepared requests involving identity, resource, boundary and SCP/RCP policies; then test | Your predictions, the actual results and an explanation of every miss | 4 h |
| 5 · OIDC federation and data perimeter | Replace a CI key with GitHub Actions OIDC; then add an RCP or VPC endpoint policy that blocks access from outside your organisation | Workflow file, trust policy with repository and branch conditions, and a denied request log from a second account | 5 h |
| 6 · Well-Architected review | Review a provided sample workload with the AWS WA Tool or the Azure assessment, then repeat the reliability questions with the Google framework | A review report: top 5 high-risk issues, evidence, owner, fix and date | 5 h |
| 7 · Static stability game day | Run a two-AZ service, then simulate an AZ loss (stop all instances in one AZ and deny scaling API calls to the app role) | Request success rate and latency before, during and after, and a note on whether the design stayed statically stable | 4 h |
| 8 · Shuffle sharding simulation (no AI) | Simulate 8 workers and 100 customers in Python; inject one poison customer under plain sharding and shuffle sharding (2 of 8) | A plot of customers affected in each scheme and the combinatorics behind it | 3 h |

## Projects

### P1 · A safe personal cloud foundation (L1, ~6 hours)

**Real-world inspiration:** AWS, Azure and Google all document account-security baselines for new environments (root MFA, SSO, audit logs, budgets). The [AWS multi-account whitepaper](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.html) recommends separating workloads into accounts from day one.

**What to build:** a personal organisation with a management account, a sandbox account and a log-archive account (or the Azure/Google equivalents), with SSO login, MFA, organisation-wide audit logging to the log-archive account, a budget with alerts, and one preventive guardrail that blocks all regions except `ap-south-1`/`ap-south-2` (or Central India/South India, or `asia-south1`/`asia-south2`).

**Acceptance criteria:**
- No IAM users with access keys exist; `aws iam list-users` (or equivalent) shows only break-glass, which has MFA.
- Audit logs from the sandbox arrive in the log-archive bucket, and the sandbox admin cannot delete them (show the denied call).
- Launching a VM in a non-India region from the sandbox fails with a guardrail denial.
- A budget alert fires in a test (lower the threshold temporarily).
- **Cost ceiling:** US$2 for the whole project.

**Stretch goals:** a second guardrail that denies disabling audit logging; an automated weekly report of IAM credentials age.

**What it proves to an employer:** you start every environment safely, which is the first thing a cloud team lead checks in a new hire.

### P2 · A landing zone for a regulated startup (L2, ~15 hours)

**Real-world inspiration:** SEBI's cloud framework (March 2023) requires regulated entities to process data only in MeitY-empanelled providers' data centres and to keep ownership of data, logs and keys. [AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/aws-multi-account-landing-zone.html), [Azure landing zones](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/) and Google's enterprise foundations blueprint are the reference designs. The startup is an *illustrative scenario*: a broking app with prod, staging, a data platform and a payments scope.

**What to build:** an OU/management-group/folder tree with Security, Infrastructure, Workloads (prod and non-prod), Sandbox and Suspended branches; guardrails for region restriction, audit-log protection, root-user denial and mandatory tags; central logging and security findings; SSO with three permission sets (read-only, developer, platform-admin); and an account-vending runbook. Use Control Tower or the Landing Zone Accelerator if on AWS, or build with plain Organizations; reproduce the core tree on a second provider on paper.

**Acceptance criteria:**
- A test matrix of at least 15 actions (for example "developer deletes a log bucket", "anyone launches in `us-east-1`", "platform-admin creates a VPC in prod") with expected and actual results; 100% must match.
- A new workload account can be vended in under 30 minutes by following your runbook, and arrives with logging, guardrails and SSO already applied.
- Every resource in the workload accounts carries `owner`, `env` and `cost-centre` tags, enforced by policy.
- A one-page mapping of each guardrail to the SEBI framework clause or DPDP principle it supports.
- **Cost ceiling:** US$10; delete Control Tower managed resources when done if you used them.

**Stretch goals:** detective controls with automatic remediation; a quarterly break-glass test script that alerts the security channel.

**What it proves to an employer:** you can set up the foundation every regulated Indian company needs before its first workload goes live.

### P3 · A reviewed, failure-tested reference architecture (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:**
- Disney+ Hotstar's scaling series describes the limits of self-managed Kubernetes clusters at 25 million concurrency and the redesign for 59 million ([Hotstar](https://blog.hotstar.com/scaling-infrastructure-for-millions-from-challenges-to-triumphs-part-1-6099141a99ef)).
- The AWS October 2025 and Google Cloud June 2025 outages show why regional dependencies and generated configuration must be designed for.
- The workload is an *illustrative scenario*: a ticketing platform for a cricket final in Mumbai, with a 20× traffic spike at sale opening.

**What to build:**
- a multi-AZ architecture on one provider, running for real at small scale: load balancer, stateless app tier with autoscaling, managed database with a standby, a queue for order processing and object storage;
- the same design mapped to a second provider on paper, with every service named;
- a written package: C4 diagrams, at least eight ADRs, a threat list, a DR plan with stated RPO/RTO, a quota and dependency sheet, a cost estimate per 1,000 orders, and a Well-Architected review of your own design.

**Acceptance criteria:**
- **Zone loss:** with one AZ removed under steady load, the error rate stays below 1% and p99 latency within 2× of baseline, with no manual action. Show the graphs.
- **Spike:** a 20× step load sustained for 5 minutes is absorbed with fewer than 0.5% failed requests (pre-warming and queue buffering allowed; document them).
- **DR:** restore the database into a second region or account from backup and measure the actual RPO and RTO against your targets.
- **Security:** no long-lived keys; IAM Access Analyzer (or equivalent) reports no unintended external access; all data stores encrypted with customer-managed keys.
- **AI review:** include an AI-generated version of the architecture and a table of at least five defects you found in it, each with a documentation link.
- **Cost ceiling:** US$40 total; run load tests in short windows and destroy everything after each session.

**Stretch goals:** cell-based design with two cells and tenant routing; a static-stability proof with the scaling API denied; carbon estimate per 1,000 orders using the provider's carbon tool.

**What it proves to an employer:** you can take a vague business requirement to a tested, documented, defensible architecture, which is the core of the cloud architect and solutions architect roles.

## Feeds into

- [CLD302 Infrastructure as Code](../CLD302_infrastructure_as_code_terraform_opentofu/README.md): P2's landing zone is rebuilt as code.
- [CLD304 Cloud Networking](../CLD304_cloud_networking_vpcs_dns_load_balancing/README.md) and [CLD305 Storage and Managed Databases](../CLD305_cloud_storage_and_managed_databases/README.md): deeper versions of Chapter 3.
- [CLD401 Serverless and Event-Driven Cloud](../../year_4/CLD401_serverless_and_event_driven_cloud/README.md): the event-driven reference architecture.
- [OV01 Cloud Security](../../../../04_overlaps/OV01_cloud_security/README.md) and [SAR401 Cloud Security Architecture](../../../security_architecture/year_4/SAR401_cloud_security_architecture/README.md): IAM, perimeters and guardrails in depth.
- [CAR401 Career Lab II](../../../../05_shared_years_3_to_5/CAR401_career_lab_ii_interviews_system_design_and_ai/README.md): P3 is a ready-made system-design interview story.
