# CLD302 · Labs and projects

Use Terraform 1.16 or OpenTofu 1.13 (pin the version in `required_version`), one cloud sandbox account with a budget alarm, and a Git repository with CI. Every lab ends with `destroy` unless it says otherwise. Labs 3 and 4 are done without AI assistants.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Script versus declarative | Build a small VPC with a shell script and with Terraform; run each three times and change one subnet | A table of what each approach did on re-run and on change, with the plan output | 3 h |
| 2 · Providers and regions | Deploy encrypted buckets to two India regions with provider aliases and a validation that rejects other regions | Code, the rejected-variable error, and `state list` | 3 h |
| 3 · Refactor without destroys (no AI) | Convert a `count`-based config to `for_each` and move resources into a module using `moved` blocks | A plan with zero destroys and a short explanation of each `moved` block | 4 h |
| 4 · State: lock, lose, recover (no AI) | S3/GCS/azurerm backend with locking and versioning; force a lock conflict; delete the current state object; recover | Commands used, before-and-after `state list`, and a recovery runbook | 4 h |
| 5 · Module publishing | Turn your network code into a versioned module with docs and an example; publish to a private registry or Git tags | Module repository with v1.0.0 and v1.1.0, changelog and generated docs | 4 h |
| 6 · Environments | Deploy dev, staging and prod from one module version using directories (not workspaces); promote a change | Three plans and a promotion log showing the same module version | 3 h |
| 7 · PR plans and drift | Atlantis or a GitHub Action posts plans on PRs; a scheduled refresh-only plan detects a console change | A PR with the plan comment and a drift alert | 4 h |
| 8 · Tests | `.tftest.hcl` tests with mock providers, one Terratest integration test and an Infracost threshold check | Green CI run plus one deliberately failing run for each test type | 6 h |
| 9 · Policy as code | Rego policies with unit tests run by Conftest on plan JSON; a Checkov or Trivy scan with justified suppressions | Policies, tests and a triage table of scanner findings | 4 h |
| 10 · Other tools | Port one module to Pulumi (TypeScript or Python) and to Bicep or CDK | Side-by-side comparison of code size, plan readability and drift handling | 5 h |

## Projects

### P1 · Your CLD301 foundation, as code (L1, ~6 hours)

**Real-world inspiration:** every regulated cloud team rebuilds its first hand-made account as code before scaling. The [AWS multi-account whitepaper](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.html) and [Azure landing zones](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/) assume IaC.

**What to build:** Terraform or OpenTofu code that recreates your CLD301 P1 foundation: budget and alerts, audit logging to a protected bucket, SSO permission sets or role assignments, and the India-only region guardrail. Remote state with locking.

**Acceptance criteria:**
- `apply` on an empty account produces the full foundation; a second `apply` reports no changes.
- `destroy` followed by `apply` restores it, except for the protected log bucket, which `prevent_destroy` keeps.
- TFLint and `validate` pass with zero warnings; all variables have descriptions and types.
- **Cost ceiling:** US$2.

**Stretch goals:** the same foundation in Pulumi; a README badge from CI.

**What it proves to an employer:** you do not click-build infrastructure, and your code is idempotent.

### P2 · A tested, policy-checked module library (L2, ~15 hours)

**Real-world inspiration:** [terraform-aws-modules](https://github.com/terraform-aws-modules), [Azure Verified Modules](https://azure.github.io/Azure-Verified-Modules/) and [Cloud Foundation Fabric](https://github.com/GoogleCloudPlatform/cloud-foundation-fabric) show how organisations publish reusable, versioned building blocks. The consumer is an *illustrative scenario*: an Indian health-tech start-up that must keep patient data in India and encrypted.

**What to build:** three modules (network, encrypted object store, managed Postgres) with versioned releases, generated docs and examples; a CI pipeline running fmt, validate, TFLint, native tests with mocks, a Terratest smoke test, Conftest policies and an Infracost diff on every PR.

**Acceptance criteria:**
- Each module has at least 8 native test assertions and one integration test; CI is green.
- Policies reject: unencrypted storage, public buckets, databases without backups or deletion protection, resources outside `ap-south-1`/`ap-south-2` (or the equivalent), and missing `owner`/`env` tags. Each rule has a passing and a failing unit test.
- A breaking change in a module bumps the major version, and the changelog explains the upgrade.
- An Infracost comment appears on every PR, and CI fails when a change adds more than a set monthly amount.
- **Cost ceiling:** US$10; integration tests must destroy what they create, and a nightly job deletes anything tagged `ttl` that has expired.

**Stretch goals:** publish to an OCI registry with OpenTofu; Sentinel equivalents of two policies; signed release tags.

**What it proves to an employer:** you build the internal platform pieces other teams depend on, with tests and policy rather than hope.

### P3 · Brownfield import, drift control and an AI-safety gate (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:**
- Most companies have years of console-built infrastructure; Terraform 1.14 added list resources and `terraform query` to help find and bulk-import it ([release notes](https://discuss.hashicorp.com/t/terraform-v1-14-0-released/76808)).
- In July 2025 an AI coding agent deleted a production database during a code freeze at a Replit customer, which is why agent permissions matter ([Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-coding-platform-goes-rogue-during-code-freeze-and-deletes-entire-company-database-replit-ceo-apologizes-after-ai-engine-says-it-made-a-catastrophic-error-in-judgment-and-destroyed-all-production-data)).
- Benchmarks show AI-generated IaC is often wrong ([IaC-Eval](https://proceedings.neurips.cc/paper_files/paper/2024/hash/f26b29298ae8acd94bd7e839688e329b-Abstract.html)).

**What to build:**
1. A "legacy" environment built by hand (by a classmate or a provided script): VPC, instances, a database, buckets and IAM roles, with some deliberate inconsistencies.
2. Import all of it into your module library using `import` blocks (and `terraform query` where the provider supports it), reaching a clean plan without recreating anything.
3. Scheduled drift detection that opens an issue with the diff.
4. An "AI change gate" in CI for PRs labelled as AI-generated: it blocks any destroy or replace of stateful resources, any IAM wildcard, any public exposure, and any cost increase above a threshold, and requires a named human approver.
5. An evaluation: generate 15 changes with an assistant against your repository, run them through the gate, and report what was caught and what slipped through.

**Acceptance criteria:**
- 100% of the legacy resources are under management, and the first plan after import shows zero creates, zero destroys and only documented in-place updates.
- Drift introduced in the console is reported within 60 minutes.
- The gate blocks 100% of a prepared set of 10 dangerous changes and passes 10 safe ones (no false blocks).
- The evaluation report lists every AI-generated defect with its category, whether the gate caught it, and a proposed new rule for each miss.
- A plan-only CI role exists, and only a separate, approval-gated job can apply.
- **Cost ceiling:** US$25; legacy and imported environments run only during work sessions.

**Stretch goals:** the same import done with OpenTofu and a written comparison; state encryption with a KMS key provider; an MCP-connected assistant restricted to approved private modules.

**What it proves to an employer:** you can bring a messy real estate under control and make AI-assisted infrastructure changes safe, which is exactly what platform teams need in 2026.

## Feeds into

- [CLD303 Containers and Kubernetes](../CLD303_containers_and_kubernetes/README.md) and [CLD304 Cloud Networking](../CLD304_cloud_networking_vpcs_dns_load_balancing/README.md): every later lab is built with these modules.
- [CLD402 Multi-Cloud, Hybrid Cloud and Migration](../../year_4/CLD402_multi_cloud_hybrid_cloud_and_migration/README.md): P3's import workflow becomes the migration factory.
- [OPS301 CI/CD Engineering](../../../devops_sre_platform_engineering/year_3/OPS301_ci_cd_engineering/README.md) and [OPS305 Configuration Management and GitOps](../../../devops_sre_platform_engineering/year_3/OPS305_configuration_management_and_gitops/README.md): pipelines and GitOps at company scale.
- [OV01 Cloud Security](../../../../04_overlaps/OV01_cloud_security/README.md): policy as code as a security control.
