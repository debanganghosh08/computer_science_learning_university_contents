# CLD302 · Infrastructure as Code: Terraform, OpenTofu and Pulumi

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 5 | 4 (≈ 120 hours) | L2 → L3 | [CS215](../../../../02_year_2_core_computer_science/semester_4/CS215_cloud_and_devops_foundations/README.md), [CS212](../../../../02_year_2_core_computer_science/semester_4/CS212_distributed_systems_i/README.md) | [CLD402](../../year_4/CLD402_multi_cloud_hybrid_cloud_and_migration/README.md), every later CLD course |

Part of the [Cloud Engineering major](../../README.md). Taken with [CLD301 Cloud Architecture](../CLD301_cloud_architecture_on_aws_azure_and_google_cloud/README.md) (whose landing zone you rebuild here as code) and [CLD303 Containers and Kubernetes](../CLD303_containers_and_kubernetes/README.md). Pipelines that *run* IaC at company scale (CI/CD, GitOps) are taught in the DevOps major ([OPS301](../../../devops_sre_platform_engineering/year_3/OPS301_ci_cd_engineering/README.md), [OPS305](../../../devops_sre_platform_engineering/year_3/OPS305_configuration_management_and_gitops/README.md)); this course owns the code itself: language, state, modules, tests and policy.

## Why this course matters now

In a professional cloud team, almost nothing is created by clicking. Infrastructure is declared in code, reviewed in a pull request, planned, checked by policy and applied by a pipeline. The tools changed hands recently: HashiCorp moved Terraform to the Business Source License in August 2023, the community fork OpenTofu joined the CNCF as a sandbox project in April 2025, IBM completed its acquisition of HashiCorp in February 2025, and HashiCorp retired CDK for Terraform in December 2025. Engineers who understand the shared concepts (desired state, a state file, a plan, a dependency graph) move between these tools in days.

AI changed the writing, not the responsibility. Assistants generate Terraform in seconds, the [Terraform MCP server](https://www.hashicorp.com/blog/terraform-mcp-server-is-now-generally-available) (generally available June 2026) lets agents search private module registries and explain plans, and [Pulumi Neo](https://www.pulumi.com/blog/pulumi-neo/) runs infrastructure tasks as an agent. But measured accuracy is low: on the IaC-Eval benchmark the best model in 2024 passed only 19.36% of Terraform tasks, against 86.6% on a Python benchmark ([NeurIPS 2024](https://proceedings.neurips.cc/paper_files/paper/2024/hash/f26b29298ae8acd94bd7e839688e329b-Abstract.html)); a December 2025 study raised overall success from 27.1% to 62.6% with knowledge injection but found intent alignment stayed flat ([arXiv 2512.14792](https://arxiv.org/abs/2512.14792)). An engineer who can read a plan and catch the one line that destroys a database is worth more than ever.

## Learning outcomes

By the end you can:

1. **Explain** declarative, convergent infrastructure management (desired state, plan, apply, dependency graph) and **compare** Terraform, OpenTofu, Pulumi, CloudFormation/CDK, Bicep and Crossplane.
2. **Write** idiomatic HCL with `for_each`, dynamic blocks, lifecycle rules, and `moved`, `import` and `removed` blocks, and **refactor** without destroying resources.
3. **Operate** remote state safely: backends, locking, encryption, state surgery, secrets, and **recover** from a corrupted or lost lock.
4. **Design** a module library with stable interfaces, semantic versioning and documentation, and **publish** it to a registry.
5. **Test** IaC at four levels: static analysis, `terraform test`/`tofu test` with mocks, Terratest integration tests and policy tests.
6. **Enforce** policy as code with OPA/Conftest and a scanner (Checkov or Trivy) on plan JSON in CI.
7. **Detect and fix** drift, and **import** existing hand-built infrastructure into code.
8. **Review** AI-generated IaC with a written checklist and **show** concrete defects it introduced.

## Chapters and lessons

### Chapter 1 · Why infrastructure as code (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Desired state and convergence | Declarative versus imperative, idempotence, reconciliation loops, mutable versus immutable infrastructure | Rebuild a CLD301 lab VPC twice with a shell script and with Terraform; compare re-runs |
| 1.2 The plan and the graph | Resource graph, implicit and explicit dependencies, parallelism, create/update/replace/destroy | Run `terraform graph` and explain why two resources are created in parallel |
| 1.3 The tool landscape | Terraform (BSL 1.1 since 2023, IBM since 2025), OpenTofu (MPL 2.0, CNCF sandbox), Pulumi, CloudFormation and CDK, Bicep, Crossplane; provisioning versus configuration management (Ansible) | Write a one-page tool choice for a bank, a startup and a Kubernetes-centric platform team |
| 1.4 Licences and governance | What BSL restricts, why the fork happened, compatibility between Terraform 1.x and OpenTofu 1.x, when they diverge | List three features present in one and not the other in 2026 |

**Check your understanding:** (1) Why is a second `apply` with no changes a correctness test? (2) What makes a resource "replace" rather than "update"? (3) Why does licensing matter to a company building a product on top of the tool, but rarely to its users?

### Chapter 2 · HCL in depth (weeks 2–3)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Providers and resources | Provider configuration, aliases for multi-region, version constraints, the lock file `.terraform.lock.hcl` | Deploy the same bucket to `ap-south-1` and `ap-south-2` with provider aliases |
| 2.2 Variables, locals, outputs | Types, validation blocks, sensitive values, precedence of variable sources | Add validation that rejects non-India regions |
| 2.3 Iteration | `count` versus `for_each` (and why index shifts destroy resources), `for` expressions, dynamic blocks | Convert a `count` list to `for_each` without recreating anything |
| 2.4 Lifecycle | `create_before_destroy`, `prevent_destroy`, `ignore_changes`, `replace_triggered_by`, preconditions and postconditions | Protect a database with `prevent_destroy` and show the blocked plan |
| 2.5 Refactoring blocks | `moved`, `import` (including `for_each` imports), `removed`; Terraform 1.16 allows `import` blocks inside modules | Rename and move resources into a module with zero destroys in the plan |

**Check your understanding:** (1) Why can removing the first item from a `count` list destroy every resource after it? (2) When is `ignore_changes` a smell? (3) What does the lock file protect you from?

### Chapter 3 · State (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 What state is | Mapping from code to real IDs, cached attributes, why state can contain secrets | Read a state file and find every secret in it |
| 3.2 Remote backends and locking | S3 (native lock file with `use_lockfile`, DynamoDB locking deprecated), GCS, azurerm, HCP Terraform; lock contention | Configure an S3 backend with native locking and force a lock conflict |
| 3.3 Protecting state | Bucket versioning, encryption, least-privilege access; OpenTofu client-side state encryption (1.7); ephemeral values and write-only arguments in Terraform 1.10–1.11 | Pass a database password as write-only and prove it never reaches state |
| 3.4 State surgery | `state mv`, `state rm`, `import`, `force-unlock`, restoring a previous state version | Recover from a deleted state file using bucket versioning |

**Check your understanding:** (1) Why should almost no human have write access to the state bucket? (2) When is `force-unlock` safe? (3) What does an ephemeral value change about secret handling?

### Chapter 4 · Modules and composition (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Module design | Inputs as an API, sensible defaults, outputs, avoiding "god modules", composition over configuration | Split a monolithic config into network, data and app modules |
| 4.2 Versioning and registries | Semantic versioning, Git tags, public and private registries, OpenTofu registry and OCI-hosted modules (OpenTofu 1.10) | Publish v1.0.0 of your VPC module and consume it by version |
| 4.3 Community modules | `terraform-aws-modules`, Azure Verified Modules, Google Cloud Foundation Fabric; reading before trusting | Audit one popular module's IAM and network defaults |
| 4.4 Documentation | `terraform-docs`, examples as tests, changelogs, upgrade notes | Generate docs and a working example for your module |

**Check your understanding:** (1) Which module change is a breaking change? (2) Why pin module versions but not always provider patch versions? (3) What do you check before using a module with 50 million downloads?

### Chapter 5 · Environments and layout (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Workspaces versus directories | CLI workspaces, directory-per-environment, per-environment state, blast radius | Model dev, staging and prod both ways and compare plans |
| 5.2 Layering | Separate stacks for foundation, network, data and apps; `terraform_remote_state` versus data sources versus outputs in a parameter store | Wire app stacks to network outputs without remote state |
| 5.3 Orchestrators | Terragrunt (1.x), Terraform Stacks, OpenTofu provider `for_each` (1.9) for multi-region | Deploy one module to three regions with provider iteration |
| 5.4 Promotion | Same module version promoted through environments, variable files, change windows | Promote a module change from dev to prod with recorded plans |

**Check your understanding:** (1) Why do workspaces make it easy to apply to the wrong environment? (2) What is the cost of too many small stacks? (3) How do you prove prod ran the same code that staging tested?

### Chapter 6 · Plan, review, apply (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Plans as artefacts | Saved plans, `terraform show -json`, reading replacements and destroys, plan summaries in pull requests | Write a script that fails CI on any destroy of a stateful resource |
| 6.2 Run platforms | Atlantis, HCP Terraform (free tier capped at 500 managed resources after the legacy free plan ended on 31 March 2026), Spacelift, env0 | Run plans on pull requests with Atlantis or a GitHub Action |
| 6.3 Least-privilege runners | Separate plan and apply roles, OIDC federation, approval gates | Give the plan job read-only access and prove it cannot apply |
| 6.4 Drift | Refresh-only plans, scheduled drift detection, deciding whether code or cloud is right | Change a security group in the console and catch it within an hour |

**Check your understanding:** (1) Why should the plan job not hold apply permissions? (2) What does "plan says no changes" not guarantee? (3) Who decides how drift is resolved?

### Chapter 7 · Testing infrastructure code (weeks 8–9)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Static checks | `fmt`, `validate`, TFLint with provider rulesets | Add pre-commit hooks that block unformatted code |
| 7.2 Native tests | `.tftest.hcl` files, `run` blocks with `command = plan` or `apply`, assertions, mock providers, `tofu test` | Test your VPC module's CIDR maths with a mocked provider |
| 7.3 Integration tests | Terratest (Go): deploy, probe, destroy; retries; parallel tests and quotas | Prove a deployed load balancer returns 200 and destroy afterwards |
| 7.4 Ephemeral environments | Per-pull-request environments, TTL tags, automatic clean-up, cost caps | Create and auto-destroy an environment per PR |
| 7.5 Cost tests | Infracost on plans, cost diff in PR comments, thresholds | Fail CI if a change adds more than US$50 a month |

**Check your understanding:** (1) What can a mocked test prove, and what can only a real apply prove? (2) Why do integration tests fail more on Fridays (quotas, shared accounts)? (3) Why test cost at all?

### Chapter 8 · Policy as code and supply-chain safety (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 OPA and Rego | Policies over plan JSON, Conftest, unit tests for policies | Write a policy: every bucket encrypted, public access blocked, mandatory tags |
| 8.2 Scanners | Checkov, Trivy (which absorbed tfsec), KICS; false positives and suppressions with reasons | Scan a sample repository and triage 20 findings |
| 8.3 Sentinel and platform policy | Sentinel in HCP Terraform, Azure Policy, organisation policies as the last line | Show the same rule enforced in CI and in the cloud |
| 8.4 Supply chain | Provider checksums and signatures, pinned module sources, private mirrors, reviewing provider upgrades | Reproduce a provider install from a private mirror |

**Check your understanding:** (1) Why enforce the same rule in CI and in the cloud? (2) When is a scanner suppression acceptable? (3) What could a malicious module do during `plan`?

### Chapter 9 · Beyond HCL: Pulumi, CloudFormation, Bicep and Crossplane (weeks 11–12)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Pulumi | Infrastructure in TypeScript, Python or Go; stacks; Pulumi ESC for configuration and secrets; Automation API | Port your VPC module to Pulumi and compare the plan output |
| 9.2 CloudFormation and CDK | Stacks, change sets, drift detection, IaC generator; CDK constructs synthesising CloudFormation | Deploy a CDK app and read the generated template |
| 9.3 Bicep | ARM templates, Bicep modules, deployment stacks, what-if | Deploy the same storage account with Bicep and Terraform |
| 9.4 Kubernetes-native IaC | Crossplane compositions, controllers reconciling cloud resources | Provision a bucket through a Crossplane claim on kind |
| 9.5 Lessons from CDKTF | Why HashiCorp archived CDK for Terraform (10 December 2025) and what migration looked like | Write a risk note on depending on a single-vendor tool |

**Check your understanding:** (1) What do general-purpose languages make easier, and what do they make easier to get wrong? (2) Why is CloudFormation's rollback behaviour different from Terraform's? (3) When does a continuously reconciling controller beat a one-shot apply?

### Chapter 10 · AI and IaC (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 What generation gets wrong | IaC-Eval results; intent mismatch; deprecated arguments; over-broad IAM; missing encryption; wrong region services | Generate 10 modules with an assistant, run your full test and policy suite, log failures by category |
| 10.2 Agents with apply rights | The July 2025 Replit incident (an agent deleted a production database during a code freeze); why agents need plan-only roles, approvals and `prevent_destroy` | Design an agent permission model: what it may plan, what a human must approve |
| 10.3 MCP and registries | Terraform MCP server (private registry search, plan explanation), Pulumi Neo; keeping agents on approved modules | Connect an assistant to your private registry and require approved modules only |
| 10.4 A review checklist | Destroys and replaces, IAM wildcards, public exposure, encryption, tags, cost delta, provider versions | Write and apply your checklist to a classmate's AI-generated PR |

**Check your understanding:** (1) Why is intent alignment harder to test than syntax? (2) What is the minimum guardrail before an agent can run `apply`? (3) How do you measure whether AI-assisted IaC is making your team faster *and* safer?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1: script versus Terraform | Re-run comparison |
| 2 | 2 | Lab 2: multi-region with aliases | Two-region bucket |
| 3 | 2 | Lab 3: refactor with `moved` | Zero-destroy plan; P1 starts |
| 4 | 3 | Lab 4: backend, locking, recovery | Restored state; P1 due |
| 5 | 4 | Lab 5: publish a module | v1.0.0 with docs |
| 6 | 5 | Lab 6: three environments | Promotion log; P2 starts |
| 7 | 6 | Lab 7: PR plans and drift | Drift caught in CI |
| 8 | 7 | Lab 8: native tests with mocks | Test suite |
| 9 | 7 | Lab 8 continued: Terratest and Infracost | Green pipeline; P2 due |
| 10 | 8 | Lab 9: policy as code | Policies with unit tests |
| 11 | 9 | Lab 10: Pulumi and Bicep ports | Comparison note; P3 starts |
| 12 | 9 | P3 build | Landing zone as code |
| 13 | 10 | AI generation audit | Failure table |
| 14 | 10 | P3 completion | Demo and review |
| 15 | Review and exam | — | Written exam and plan-reading oral |

## Working with AI in this course

- **Use AI for:** first drafts of modules and variables, translating between HCL, Pulumi, Bicep and CloudFormation, writing Rego from an English rule (then testing it), explaining unfamiliar provider arguments, summarising a 2,000-line plan, and generating Terratest boilerplate. Named tools: Claude Code, GitHub Copilot, the Terraform MCP server, Pulumi Neo, Amazon Q Developer.
- **Do without AI (drills):** reading plans and predicting their effect; the `count`-to-`for_each` refactor; state recovery; writing the review checklist; the oral exam.
- **Verify AI output by:** running `validate`, TFLint, your policy suite and a scanner; reading the full plan for destroys and replacements; checking every argument against the provider's documentation for your pinned version; applying in a throwaway account first; checking IAM with Access Analyzer.
- **Where AI still fails here (show it):** benchmark accuracy is far below general coding (19.36% pass@1 in IaC-Eval; 62.6% even with knowledge injection, with intent alignment not improving). Generate code for "a private S3 bucket readable by one role" and count how many of your policies it fails. Ask for a refactor and check whether the plan destroys anything. Keep the results as evidence in P3.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs 1–10 | 25% |
| Projects P1 / P2 / P3 | 5% / 15% / 25% |
| Written exam (HCL semantics, state, testing, policy) | 20% |
| Plan-reading oral | 10% |

**Mastery gate:** you pass when you can, without AI help, (a) read an unseen 300-line `terraform plan` and state within 10 minutes every resource that will be destroyed or replaced and why; (b) refactor a provided configuration into modules with a plan showing zero destroys; and (c) recover a working setup from a deleted lock table, a stale lock and an overwritten state file, using only versioned backups and state commands.

## Industry reality

Terraform-style IaC is the default in job descriptions for cloud, platform and DevOps roles, and the Terraform Associate certification moved to exam version 004 on 8 January 2026, testing Terraform 1.12 ([HashiCorp](https://developer.hashicorp.com/certifications/infrastructure-automation)). Zerodha described building its Kubernetes infrastructure on AWS with Terraform, Packer and `eksctl` ([CNCF case study](https://www.cncf.io/case-studies/zerodha/)). Large organisations run thousands of state files and depend on module libraries, policy gates and drift detection; the hard problems are refactoring safely and keeping humans and agents from destroying stateful resources.

Interview questions from this course:

1. **"Your plan shows the production database will be replaced. What do you do?"** Cover reading the attribute that forces replacement, `ignore_changes` versus fixing the code, `moved` blocks, `prevent_destroy`, snapshots before any change, and the review that should have caught it.
2. **"Two engineers apply at the same time and state is corrupted. Walk me through recovery."** Cover locking, backend versioning, identifying the last good version, `state pull/push`, re-import, and preventing it with CI-only applies.
3. **"How do you structure Terraform for 50 teams and three environments?"** Cover layered stacks, module registry and versioning, per-environment state, ownership boundaries, policy gates, and how promotion works.
4. **"How do you test infrastructure code?"** Cover static checks, `terraform test` with mocks, Terratest, ephemeral environments, policy tests, cost tests, and what each level can and cannot prove.
5. **"Would you let an AI agent run `terraform apply` in production?"** Cover plan-only roles, approvals, `prevent_destroy`, policy gates, audit logs, blast-radius limits, and evidence about generation accuracy.

## Resources (free first)

- **Documentation:** [Terraform language](https://developer.hashicorp.com/terraform/language), [Terraform tests](https://developer.hashicorp.com/terraform/language/tests), [S3 backend](https://developer.hashicorp.com/terraform/language/backend/s3), [OpenTofu docs](https://opentofu.org/docs/), [Pulumi docs](https://www.pulumi.com/docs/), [Bicep](https://learn.microsoft.com/en-us/azure/azure-resource-manager/bicep/overview), [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html), [Crossplane](https://docs.crossplane.io/).
- **Tutorials:** [HashiCorp Terraform tutorials](https://developer.hashicorp.com/terraform/tutorials) and the [Terraform Associate 004 study guide](https://developer.hashicorp.com/terraform/tutorials/certification-004/associate-study-004).
- **Testing and policy:** [Terratest](https://terratest.gruntwork.io/), [TFLint](https://github.com/terraform-linters/tflint), [Open Policy Agent](https://www.openpolicyagent.org/docs/latest/), [Conftest](https://www.conftest.dev/), [Checkov](https://www.checkov.io/), [Trivy](https://trivy.dev/), [Infracost](https://www.infracost.io/docs/).
- **Module libraries:** [terraform-aws-modules](https://github.com/terraform-aws-modules), [Azure Verified Modules](https://azure.github.io/Azure-Verified-Modules/), [Cloud Foundation Fabric](https://github.com/GoogleCloudPlatform/cloud-foundation-fabric).
- **Papers:** [IaC-Eval](https://proceedings.neurips.cc/paper_files/paper/2024/hash/f26b29298ae8acd94bd7e839688e329b-Abstract.html) (NeurIPS 2024); [IaC generation error taxonomy](https://arxiv.org/abs/2512.14792) (2025).
- **Practising without a big bill:** most of this course runs on plans, mocks and free-tier resources. Use `terraform test` with mock providers for logic, a dedicated sandbox account with a budget alarm for applies, TTL tags plus a nightly destroy job, and never apply NAT gateways, load balancers or databases outside a timed lab session.
- **Paid, worth it:** *Terraform: Up & Running*, 3rd edition (Yevgeniy Brikman, O'Reilly).

## Sources

All checked 12 Oct 2026.
- [IBM completes acquisition of HashiCorp](https://newsroom.ibm.com/2025-02-27-ibm-completes-acquisition-of-hashicorp,-creates-comprehensive,-end-to-end-hybrid-cloud-platform) (27 Feb 2025).
- [OpenTofu CNCF project page](https://www.cncf.io/projects/opentofu/) (accepted 23 Apr 2025); [OpenTofu 1.7 state encryption](https://opentofu.org/blog/opentofu-1-7-0/); [1.9 provider for_each](https://opentofu.org/blog/opentofu-1-9-0/); [1.10 OCI registries and S3 locking](https://opentofu.org/blog/opentofu-1-10-0/).
- [Terraform v1.14.0 release](https://discuss.hashicorp.com/t/terraform-v1-14-0-released/76808) (Nov 2025: list resources, actions); [Terraform v1.16.0 release](https://discuss.hashicorp.com/t/terraform-v1-16-0-released/77683) (Aug 2026).
- [CDK for Terraform repository (archived)](https://github.com/hashicorp/terraform-cdk) (10 Dec 2025).
- [HCP Terraform enhanced free tier](https://www.hashicorp.com/blog/continuing-hcp-terraform-s-enhanced-free-tier-experience) (legacy free plan ended 31 Mar 2026).
- [Terraform MCP server GA](https://www.hashicorp.com/blog/terraform-mcp-server-is-now-generally-available) (11 Jun 2026); [Pulumi Neo](https://www.pulumi.com/blog/pulumi-neo/) (16 Sep 2025).
- [IaC-Eval, NeurIPS 2024](https://proceedings.neurips.cc/paper_files/paper/2024/hash/f26b29298ae8acd94bd7e839688e329b-Abstract.html); [Nekrasov et al., arXiv 2512.14792](https://arxiv.org/abs/2512.14792) (Dec 2025).
- [Tom's Hardware on the Replit database deletion](https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-coding-platform-goes-rogue-during-code-freeze-and-deletes-entire-company-database-replit-ceo-apologizes-after-ai-engine-says-it-made-a-catastrophic-error-in-judgment-and-destroyed-all-production-data) (Jul 2025).
- [HashiCorp certification: Terraform Associate 004](https://developer.hashicorp.com/certifications/infrastructure-automation).
- [CNCF Zerodha case study](https://www.cncf.io/case-studies/zerodha/).
- Tool versions from GitHub releases on 12 Oct 2026: Terraform 1.16.5, OpenTofu 1.13.1, Terragrunt 1.1.6, Pulumi 3.268, Checkov 3.3, Trivy 0.75.

_Last reviewed: 2026-10_
