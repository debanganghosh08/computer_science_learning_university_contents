# OV03B · Policy as Code and Secure CI/CD

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 8 | 4 (≈ 120 hours) | L3 → L4 | [OPS301](../../../03_majors/devops_sre_platform_engineering/year_3/OPS301_ci_cd_engineering/README.md), [SAR305](../../../03_majors/security_architecture/year_3/SAR305_secure_sdlc_and_devsecops_architecture/README.md), [SEC302](../../../03_majors/cybersecurity_defense/year_3/SEC302_security_operations_soc_siem_and_monitoring/README.md); recommended [OV03A](../OV03A_software_supply_chain_security/README.md) | [OPS501](../../../03_majors/devops_sre_platform_engineering/year_5/OPS501_frontier_seminar_autonomous_infrastructure/README.md), [SAR501](../../../03_majors/security_architecture/year_5/SAR501_frontier_seminar_post_quantum_migration/README.md), [THS501](../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) |

Part of the [OV03 DevSecOps overlap](../README.md). SAR305 decided *where* controls belong (its control map and "guardrails over gates"); OPS301 Chapter 9 introduced pipeline hardening. This course makes the rules executable, tested and fast, and treats the CI/CD system as production infrastructure that attackers target.

## Why this course matters now

CI/CD systems hold the keys to production, so attackers go after them directly. Codecov's bash uploader was modified to exfiltrate CI environment variables in 2021 ([Codecov](https://about.codecov.io/security-update/)); in December 2024 an attacker used a `pull_request_target` workflow and the GitHub Actions cache to publish malicious Ultralytics releases to PyPI ([PyPI blog](https://blog.pypi.org/posts/2024-12-11-ultralytics-attack-analysis/)); in 2025 the tj-actions compromise leaked secrets from workflows across many repositories ([CISA](https://www.cisa.gov/news-events/alerts/2025/03/18/supply-chain-compromise-third-party-tj-actionschanged-files-cve-2025-30066-and-reviewdogaction)); and in May 2026 CISA warned of campaigns "specifically CI/CD pipelines, code extensions and workflows" ([CISA](https://www.cisa.gov/news-events/alerts/2026/05/28/supply-chain-compromises-impact-nx-console-and-github-repositories)). Platforms responded: GitHub added policies to enforce SHA-pinned actions (August 2025) and changed `pull_request_target` to always run the default branch's workflow from 8 December 2025 ([GitHub changelog](https://github.blog/changelog/2025-11-07-actions-pull_request_target-and-environment-branch-protections-changes/)). At the same time, policy as code matured: OPA 1.0 made Rego v1 the default (December 2024), Kubernetes made ValidatingAdmissionPolicy and MutatingAdmissionPolicy stable, and Kyverno graduated in the CNCF (March 2026). AI assistants write Rego, CEL and workflow YAML fluently and often subtly wrong. The human job is to design policies that are correct, tested, explainable to developers, and fast enough not to be bypassed.

## Learning outcomes

By the end you can:

1. **Design** a policy architecture: decision points, enforcement points, data sources, distribution and decision logging across pull requests, pipelines, admission and cloud organisations.
2. **Write and test** policies in Rego (OPA 1.0), CEL (Kubernetes admission) and Kyverno, with unit tests, coverage and linting, and **choose** the right language per context.
3. **Gate** infrastructure changes with plan-time policy and **back them** with cloud organisation guardrails, then **prove** each control with tests.
4. **Roll out** admission policies safely at fleet scale with audit, warn and enforce stages, exceptions with expiry, and tested failure modes.
5. **Threat-model** a CI/CD system against the OWASP Top 10 CI/CD Security Risks and **harden** GitHub Actions or GitLab CI accordingly.
6. **Run** runners and secrets so that one compromised job cannot reach production credentials, and **measure** blast radius per job.
7. **Produce** continuous compliance evidence from policy decisions mapped to control frameworks.
8. **Govern** AI agents that open pull requests or run in pipelines with identity, path and review policies.

## Chapters and lessons

### Chapter 1 · Policy as code: the architecture (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Decisions and enforcement | Policy decision points versus enforcement points; decision = f(input, data); fail-open versus fail-closed | Draw the policy architecture for an organisation with Git, CI, Kubernetes and two clouds |
| 1.2 Where policies run | Pre-commit, pull request, pipeline, registry, admission, runtime, cloud organisation; latency and bypass risk of each (from SAR305) | Place 15 rules at the cheapest effective point |
| 1.3 The policy lifecycle | Authoring, review, testing, versioning, distribution (bundles, OCI artefacts), decision logs, retirement | Write a policy RFC template |
| 1.4 Developer experience | Deny messages that say what and how to fix, links to docs, local evaluation | Rewrite five unhelpful deny messages |

**Check your understanding:** When should an enforcement point fail closed? Why is the cheapest point not always the right one? What makes a developer bypass a policy?

### Chapter 2 · Rego in depth (weeks 2–3)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Rego v1 | Rules, sets and objects, `if` and `contains`, `every`, comprehensions, defaults; what OPA 1.0 changed | Port five pre-1.0 policies to Rego v1 |
| 2.2 Data and context | `input` versus `data`, external data, bundles, `http.send` risks | Write a policy that uses an owner directory as data |
| 2.3 Testing | `opa test`, table tests, coverage, fixtures from real configurations | Reach 100% rule coverage on a 10-rule policy |
| 2.4 Linting and performance | Regal linter, `opa eval --profile`, indexing-friendly rules | Halve evaluation time of a slow policy |
| 2.5 Conftest | Policies over Terraform plan JSON, Kubernetes YAML, Dockerfiles and workflow files | Gate Dockerfiles: no `latest`, non-root user, pinned base digest |

**Check your understanding:** Why should policies read Terraform *plans* rather than HCL? What does a policy test suite need beyond "the good case passes"? When is `http.send` inside a policy a reliability risk?

### Chapter 3 · Other policy languages (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 CEL | Common Expression Language in Kubernetes ValidatingAdmissionPolicy and MutatingAdmissionPolicy; cost limits and type checking | Write three admission rules in CEL with parameters |
| 3.2 Kyverno | Validate, mutate, generate and verify-images policies; CEL-based policy types; policy reports; `kyverno test` | Implement the same three rules in Kyverno |
| 3.3 Cedar | Authorisation language with formal analysis; Amazon Verified Permissions; when application authorisation belongs in a policy engine | Model an internal admin tool's permissions in Cedar |
| 3.4 Choosing | Expressiveness, performance, operational burden, team skills, analysability | Write the language decision record for your organisation |

**Check your understanding:** What does native CEL admission remove compared with a webhook engine? Why does formal analysability matter for authorisation policies? When is Rego the better tool despite its learning curve?

### Chapter 4 · Infrastructure policy (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Plan-time checks | OPA or Conftest on plan JSON, Checkov and Trivy misconfiguration rules, custom organisation rules | Block a public bucket and an unencrypted database in plan |
| 4.2 Policy in IaC workflows | Atlantis, HCP Terraform or Spacelift policy hooks, approval for risky changes, drift jobs | Add a policy stage to a pull-request IaC workflow |
| 4.3 Cloud guardrails as the last line | SCPs and RCPs, Azure Policy deny, Google Cloud custom organisation policy constraints (designed in SAR401) | Prove a guardrail blocks what a skipped pipeline would have allowed |
| 4.4 Testing guardrails | Automated tests that attempt forbidden actions in a sandbox account and expect denial | Build a guardrail test suite that runs nightly |

**Check your understanding:** Why keep a cloud guardrail if the pipeline already checks the plan? What does a plan-time check miss that a guardrail catches? How do you test a deny policy without causing harm?

### Chapter 5 · Admission policy at fleet scale (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Gatekeeper | ConstraintTemplates, constraints, audit, external data, `gator verify` | Port two Kyverno rules to Gatekeeper and compare |
| 5.2 Staged rollout | Audit → warn → enforce by namespace and cluster; measuring violations before enforcing | Roll out a rule across three namespaces with a violation report at each stage |
| 5.3 Exceptions | Kyverno PolicyException, Gatekeeper exemptions; owners, reasons and expiry; alerting on expired exceptions | Build an exception workflow with automatic expiry |
| 5.4 Failure modes | Webhook timeouts and `failurePolicy`, system namespaces, engine availability and latency | Measure admission latency and deploy behaviour during an engine outage |

**Check your understanding:** What happens to a cluster when an enforcing webhook is down? Why do exceptions need expiry dates rather than reviews? How do you know a rule is ready to enforce?

### Chapter 6 · The CI/CD threat model (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 OWASP Top 10 CI/CD Security Risks | Insufficient flow control, inadequate identity and access management, dependency chain abuse, poisoned pipeline execution, insufficient pipeline-based access controls, credential hygiene, insecure system configuration, ungoverned third-party services, improper artefact integrity validation, insufficient logging | Score a sample organisation against all ten |
| 6.2 Case studies | Codecov 2021, CircleCI 2023 (session token theft; customers told to rotate secrets), Ultralytics 2024, tj-actions 2025, Nx Console 2026: defensive lessons | For each, name the control that would have limited the damage |
| 6.3 Poisoned pipeline execution | Concept: untrusted code or configuration running with trusted credentials; triggers that mix the two (described for defence, not exploitation) | Find risky triggers in ten sample workflows |
| 6.4 Logging the pipeline | Audit logs for the CI platform, workflow run logs, alerting on new secrets, new runners and permission changes | Ship CI audit events to the SEC302 SIEM with three detections |

**Check your understanding:** Why is the CI system a production system? Which risk in the OWASP list does SHA pinning address, and which does it not? What does a pipeline audit log tell you that a run log does not?

### Chapter 7 · Hardening GitHub Actions and GitLab CI (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Token permissions | Read-only default `GITHUB_TOKEN`, per-job `permissions:`, GitLab job token allow-lists | Reduce every workflow to minimal permissions |
| 7.2 Triggers and untrusted input | `pull_request` versus `pull_request_target` (and GitHub's December 2025 change), script injection through untrusted context in `run:` steps, environment protection rules | Fix five unsafe workflows found by zizmor |
| 7.3 Third-party actions | Full-SHA pinning (enforceable by policy since August 2025), allow-lists, forking critical actions, update bots | Pin and allow-list all actions in the organisation |
| 7.4 OIDC to clouds | Federated credentials with tight subject claims (repository, branch, environment), no long-lived cloud keys | Allow production deploys only from the `production` environment on `main` |
| 7.5 Static analysis of workflows | zizmor and actionlint in CI; OpenSSF Scorecard checks (Token-Permissions, Pinned-Dependencies, Dangerous-Workflow) | Raise Scorecard to ≥ 8 on three repositories |

**Check your understanding:** Why must an OIDC trust policy pin more than the repository name? What makes interpolating a pull-request title into a shell step dangerous? What does pinning to a SHA protect against, and what remains?

### Chapter 8 · Runners and secrets (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Runner isolation | Ephemeral runners, Actions Runner Controller, one job per VM or pod, no self-hosted runners for public repositories | Deploy ephemeral runners and prove no state survives a job |
| 8.2 Network egress | Egress allow-lists and monitoring (for example StepSecurity Harden-Runner), blocking metadata endpoints | Detect an unexpected outbound call in a test workflow |
| 8.3 Secrets | Environment-scoped secrets, dynamic secrets from Vault or OpenBao, short TTLs, masking limits | Replace three static secrets with dynamic ones |
| 8.4 Blast-radius mapping | Which jobs can reach which secrets and clouds; rotation drills | Produce a job-to-secret map and rotate everything in one drill |

**Check your understanding:** Why does an ephemeral runner limit damage from a compromised action? Why is log masking not a secrets strategy? Which single secret in your organisation has the largest blast radius?

### Chapter 9 · Pipeline gates and exceptions (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Required checks | Rulesets, required status checks, CODEOWNERS for workflow and policy files, merge queues | Protect workflow files with a two-person rule |
| 9.2 Evidence-based gates | OPA policies over provenance, SBOM and scan results from OV03A; risk tiers from SAR305 | Gate releases on provenance plus "no KEV without VEX" |
| 9.3 Break-glass | Emergency releases with logging, after-the-fact review and automatic expiry | Run a break-glass release and its review |
| 9.4 Measuring friction | DORA metrics before and after gates (from OPS301), time spent blocked, override rates | Report the delivery impact of your gates |

**Check your understanding:** Why should workflow files have stricter review than application code? What makes a break-glass process safe? Which metric would show a gate is being worked around?

### Chapter 10 · Compliance as code (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Mapping controls to policies | NIST SP 800-53, ISO/IEC 27001 Annex A, SOC 2 criteria, sector rules (RBI, SEBI) mapped to executable checks | Map 15 controls to policies and evidence |
| 10.2 Machine-readable compliance | NIST OSCAL for control catalogues, system security plans and assessment results | Generate an OSCAL assessment-results file from policy decisions |
| 10.3 Continuous evidence | Decision logs as evidence, retention, tamper resistance | Produce an auditor-ready evidence pack for one quarter of simulated activity |
| 10.4 What compliance as code cannot do | Judgement controls, process controls, people; avoiding checkbox automation | List five controls that need human evidence and why |

**Check your understanding:** Why are decision logs better evidence than screenshots? What does an auditor need to trust automated evidence? Which controls should never be "automated green"?

### Chapter 11 · Policy for AI agents and AI in pipelines (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Agents as contributors | Coding agents opening pull requests: identities, token scopes, required human review, forbidden paths (workflows, policies, infrastructure) | Write and test policies for agent-authored pull requests |
| 11.2 Case: a poisoned AI extension | The Amazon Q Developer extension incident (AWS security bulletin AWS-2025-015): untrusted contribution to a release, defensive lessons | Identify the controls that would have stopped the release |
| 11.3 Model and prompt artefacts | Policies for model signatures, eval-gate results and prompt versions as release requirements | Gate a model release on signature and eval results |
| 11.4 AI-written policies | Testing AI-drafted Rego and CEL against adversarial test cases; mutation testing of policies | Find the defects in five AI-drafted policies |

**Check your understanding:** Why should an agent never be able to edit the policy that governs it? What test would catch a policy that never matches? Which release artefacts should be signed in an AI product?

### Chapter 12 · Operating a policy platform (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Repository and versioning | Monorepo of policies, semantic versioning, bundles and OCI distribution, staged promotion | Promote a policy bundle from staging to all clusters |
| 12.2 Reliability | SLOs for decision latency and engine availability, caching, scale testing | Load-test the decision service at 1,000 decisions per second |
| 12.3 Metrics and reporting | Violations by team, exception age, time to fix, bypass rate, policy coverage | Build the policy programme dashboard |
| 12.4 Integration | Everything together in P3 | Final integration review |

**Check your understanding:** Why version policies like software? What is the decision-latency budget for admission, and why? Which metric best shows that a policy programme reduces risk?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Policy architecture | Architecture diagram |
| 2 | 2 | Lab 2 · Rego v1 and tests | — |
| 3 | 2 | Lab 2 (cont.) · Conftest gates | — |
| 4 | 3 | Lab 3 · CEL, Kyverno and Cedar | **P1 due** |
| 5 | 4 | Lab 4 · Plan-time policy and guardrail tests | — |
| 6 | 5 | Lab 5 · Staged admission rollout | Mid-term (AI off): policy reading and writing |
| 7 | 6 | Lab 6 · CI/CD threat model and CI audit logs | — |
| 8 | 7 | Lab 7 · Workflow hardening | Scorecard report |
| 9 | 8 | Lab 8 · Ephemeral runners and dynamic secrets | **P2 due** |
| 10 | 9 | Lab 9 · Evidence-based release gates | — |
| 11 | 10 | Lab 10 · OSCAL evidence pack | — |
| 12 | 11 | Agent policy lab | — |
| 13 | 12 | Policy bundle promotion and load test | — |
| 14 | 12 | Integration | **P3 due** |
| 15 | Review | Timed hardening exercise and oral defence of P3 | Final exam |

## Working with AI in this course

- **Use AI for:** drafting Rego, CEL and Kyverno policies from plain-language rules; generating passing and failing test fixtures; explaining zizmor and Scorecard findings; mapping controls to frameworks as a first draft.
- **Do without AI (drills):** reading a workflow file and naming its risks; writing a Rego policy with tests from scratch; designing an OIDC trust condition; the mid-term and final.
- **Verify AI output by:** running every AI-drafted policy against a fixture suite that includes edge cases (missing fields, lists, unusual kinds) and checking coverage; mutation testing (change one condition and confirm a test fails); evaluating workflows with zizmor and actionlint; never deploying an AI-drafted policy straight to enforce.
- **Where AI still fails here:** log each AI-drafted policy that passed its own tests but failed yours. Expect policies that never match because of wrong field paths, deny rules that skip lists, OIDC conditions that match any branch, and workflows that interpolate untrusted input into shell commands.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1–P3 | 35% |
| Mid-term (AI off) | 10% |
| Final: timed hardening exercise (AI off) + oral defence of P3 | 30% |

**Mastery gate.** You pass when you can, with AI tools off, in three hours: (1) find and fix every high-risk issue in a provided set of five CI workflows; (2) write a tested Rego or CEL policy for a new rule with deny messages developers can act on; (3) configure OIDC deployment so only one branch and environment can reach production, and prove a fork cannot.

## Industry reality

Platform and security teams now treat pipelines as tier-0 infrastructure. The public post-incident guidance is consistent: pin third-party actions, restrict token permissions, avoid untrusted code in privileged triggers, use short-lived credentials and rotate quickly (PyPI's Ultralytics analysis explicitly recommends zizmor and avoiding `pull_request_target` and shared caches in release workflows). Policy-as-code engines (OPA, Kyverno, Gatekeeper, cloud-native policies) are standard in platform job descriptions, and interviewers ask candidates to write a policy and review a workflow live.

**Interview questions from this course**

1. *Review this workflow* (one using `pull_request_target`, checking out the PR head, with write permissions and a cloud secret). Strong answer: identifies untrusted code running with privileged token and secrets; fixes with `pull_request` for untrusted code, minimal permissions, environments with reviewers, OIDC with tight claims, and no cache sharing across trust levels.
2. *How would you enforce "all production images must come from our release workflow"?* Strong answer: provenance plus keyless signature verified at admission with identity constraints; a cloud or registry policy as a second layer; exceptions with expiry; monitoring for policy-engine availability.
3. *Write a Rego rule that denies Terraform plans creating public S3 buckets.* Strong answer: iterates `resource_changes`, handles create and update actions, checks ACL and public-access-block resources, gives a clear message, and includes tests for both cases and for missing fields.
4. *Your admission policy engine went down and blocked all deployments. What do you change?* Strong answer: high availability and resource limits for the engine, exclude system namespaces, choose `failurePolicy` per rule criticality, move simple rules to native CEL, add SLOs and alerts, and practise the failure.
5. *How would you let an AI coding agent open pull requests safely?* Strong answer: separate identity with minimal scopes, no access to secrets, forbidden paths enforced by rulesets and CODEOWNERS, required human review, CI on untrusted code without secrets, audit of agent actions.

## Resources (free first)

- **Policy engines:** OPA documentation — https://www.openpolicyagent.org/docs/latest/ ; Conftest — https://www.conftest.dev/ ; Gatekeeper — https://open-policy-agent.github.io/gatekeeper/website/docs/ ; Kyverno — https://kyverno.io/docs/ ; Kubernetes ValidatingAdmissionPolicy — https://kubernetes.io/docs/reference/access-authn-authz/validating-admission-policy/ ; Cedar — https://www.cedarpolicy.com/
- **CI/CD security:** OWASP Top 10 CI/CD Security Risks — https://owasp.org/www-project-top-10-ci-cd-security-risks/ ; GitHub Actions security hardening — https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions ; zizmor — https://docs.zizmor.sh/ ; OpenSSF Scorecard — https://scorecard.dev/ ; Harden-Runner — https://github.com/step-security/harden-runner
- **Compliance as code:** NIST OSCAL — https://pages.nist.gov/OSCAL/
- **Primary incident sources:** PyPI's Ultralytics analysis — https://blog.pypi.org/posts/2024-12-11-ultralytics-attack-analysis/ ; CircleCI incident report (Jan 2023) — https://circleci.com/blog/jan-4-2023-incident-report/ ; AWS security bulletin AWS-2025-015 — https://aws.amazon.com/security/security-bulletins/AWS-2025-015/
- **Paid, optional:** none required.

## Sources

All checked 12 Oct 2026.

- Codecov security update (2021) — https://about.codecov.io/security-update/
- PyPI blog, Ultralytics attack analysis (11 Dec 2024) — https://blog.pypi.org/posts/2024-12-11-ultralytics-attack-analysis/
- CISA alerts: tj-actions (18 Mar 2025) — https://www.cisa.gov/news-events/alerts/2025/03/18/supply-chain-compromise-third-party-tj-actionschanged-files-cve-2025-30066-and-reviewdogaction ; Nx Console and CI/CD campaigns (28 May 2026) — https://www.cisa.gov/news-events/alerts/2026/05/28/supply-chain-compromises-impact-nx-console-and-github-repositories
- GitHub changelog: SHA-pinning policy (15 Aug 2025) — https://github.blog/changelog/2025-08-15-github-actions-policy-now-supports-blocking-and-sha-pinning-actions/ ; `pull_request_target` and environment branch protection changes (7 Nov 2025, effective 8 Dec 2025) — https://github.blog/changelog/2025-11-07-actions-pull_request_target-and-environment-branch-protections-changes/
- Open Policy Agent, "Announcing OPA 1.0" (Dec 2024) — https://blog.openpolicyagent.org/announcing-opa-1-0-a-new-standard-for-policy-as-code-a6d8427ee828
- Kubernetes documentation: MutatingAdmissionPolicy stable since v1.36 — https://kubernetes.io/docs/reference/access-authn-authz/mutating-admission-policy/ ; ValidatingAdmissionPolicy — https://kubernetes.io/docs/reference/access-authn-authz/validating-admission-policy/
- CNCF landscape data (Kyverno graduated 16 Mar 2026) — https://github.com/cncf/landscape
- CircleCI, January 4, 2023 security incident report — https://circleci.com/blog/jan-4-2023-incident-report/
- AWS security bulletin AWS-2025-015 (Amazon Q Developer extension) — https://aws.amazon.com/security/security-bulletins/AWS-2025-015/

_Last reviewed: 2026-10_
