# OV03B · Labs and projects

Labs use the course GitHub organisation (or GitLab group) from OV03A, a sandbox cloud account and a Kubernetes cluster you own. Unsafe workflow examples are run only in throwaway repositories with no secrets. Every lab ships policies or workflows with tests, measured results and a short note.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Policy architecture | Design decision and enforcement points for Git, CI, registry, Kubernetes and two clouds; place 15 rules | Architecture diagram, rule placement table with reasons | 3 h |
| 2 · Rego v1, tests and Conftest | Write 10 Rego rules over Terraform plans, Kubernetes YAML and Dockerfiles; 100% rule coverage; Regal clean | Policies, tests, coverage report, profiling result for one slow rule | 7 h |
| 3 · CEL, Kyverno and Cedar | Implement three admission rules in CEL and Kyverno; model an admin tool's permissions in Cedar | Policies, `kyverno test` output, Cedar schema and tests, language decision record | 5 h |
| 4 · Plan-time policy and guardrail tests | Gate IaC pull requests with policy; write cloud guardrails; nightly tests that try forbidden actions in a sandbox account | Blocked-plan evidence, guardrail test suite results | 5 h |
| 5 · Staged admission rollout | Roll out two rules audit → warn → enforce across namespaces; exceptions with expiry; webhook outage experiment | Violation reports per stage, exception records, outage behaviour notes | 5 h |
| 6 · CI/CD threat model and audit logs | Score the organisation against the OWASP CI/CD Top 10; ship CI audit events to a SIEM with three detections | Scorecard against the ten risks, detections with test events | 4 h |
| 7 · Workflow hardening | Fix permissions, triggers, script injection and pinning across all workflows; OIDC to a cloud with environment-bound claims | zizmor before/after, Scorecard ≥ 8 on three repositories, OIDC trust policy with negative tests | 6 h |
| 8 · Ephemeral runners and dynamic secrets | Deploy ephemeral runners with ARC; egress monitoring; replace static secrets with Vault or OpenBao dynamic secrets | Proof that no state survives a job, egress alert sample, job-to-secret map | 6 h |
| 9 · Evidence-based release gates | OPA gate over provenance, SBOM and scan results; break-glass with expiry and review | Gate decisions for five releases, break-glass audit trail | 4 h |
| 10 · OSCAL evidence pack | Map 15 controls to policies; emit OSCAL assessment results from decision logs | OSCAL files, mapping table, list of controls needing human evidence | 4 h |

## Projects

### P1 · Policy library with tests (L1, ~6 hours)

**Real-world inspiration.** Platform teams keep a shared policy library so every repository and cluster enforces the same rules; untested policies are a common cause of both outages and silent gaps.

**What to build.** A policy library of at least 12 rules across Terraform plans, Kubernetes manifests, Dockerfiles and CI workflow files, with tests, linting and documentation, published as a versioned bundle.

**Acceptance criteria**
- Every rule has at least two failing and one passing fixture; `opa test` (or the engine's equivalent) reports 100% rule coverage.
- Mutation check: for each rule, flipping one condition makes at least one test fail (script provided).
- Every deny message names the resource, the violated rule and the fix, and links to a docs page.
- The bundle is versioned, built in CI and consumed by a sample repository's pipeline in under 5 seconds of evaluation time.

**Stretch goals.** Publish the bundle as a signed OCI artefact; add a local pre-commit hook using the same bundle.

**What it proves to an employer.** You treat policy as software: tested, versioned and usable by developers.

### P2 · Hardened CI/CD for an organisation (L2, ~15 hours)

**Real-world inspiration.** The Ultralytics (2024) and tj-actions (2025) compromises turned weak workflow configuration into stolen tokens and malicious releases; post-incident guidance from PyPI, GitHub and CISA is a checklist this project implements.

**What to build.** Take a provided organisation of six repositories with deliberately weak workflows (privileged triggers on untrusted code, write-all tokens, unpinned actions, long-lived cloud keys, shared caches) and harden it.

**Acceptance criteria**
- zizmor reports zero high-severity findings across all workflows; actionlint passes.
- OpenSSF Scorecard ≥ 8.0 on every repository, with Token-Permissions, Pinned-Dependencies and Dangerous-Workflow at the maximum score.
- No long-lived cloud credentials remain; OIDC trust policies allow production deploys only from `main` in the `production` environment, and a test from a fork or another branch is denied.
- Release workflows run on ephemeral runners with no cache shared with untrusted pull requests; a test proves cache isolation.
- An organisation policy enforces SHA-pinned actions from an allow-list; an attempt to use an unlisted action fails.
- Median pipeline duration changes by less than +15% from the baseline (measured over 20 runs).

**Stretch goals.** A GitLab CI port of two repositories with equivalent controls; detections in the SIEM for new self-hosted runners and permission changes.

**What it proves to an employer.** You can secure the system that ships everything else, without slowing it down.

### P3 · Policy platform with compliance evidence (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** Regulated organisations (banks under RBI rules, listed firms under SEBI frameworks, SaaS vendors with SOC 2 and ISO/IEC 27001 audits) must show auditors that controls run continuously. Policy decisions can be that evidence if they are complete, tamper-resistant and mapped to controls. The organisation here is illustrative.

**What to build.** A policy platform that enforces the P1 library and new rules at four points (pull request, pipeline, admission, cloud organisation), with staged rollout, an exception service with expiry, decision logging to tamper-resistant storage, a dashboard, an OSCAL evidence export, and policies for AI agents that open pull requests.

**Acceptance criteria**
- At least 25 rules active across the four points; each has tests and an owner.
- Admission decisions: p99 latency < 100 ms at 50 pods per second; system namespaces keep working during a policy-engine outage drill.
- Exceptions expire automatically; an expired exception produces an alert and a failing check within 1 hour.
- Decision logs for a simulated quarter are stored write-once; an OSCAL assessment-results export covers at least 15 mapped controls; a classmate acting as auditor can trace three controls from requirement to decision log in under 10 minutes each.
- Agent policy: a test agent identity can open pull requests but cannot modify workflows, policies or infrastructure paths, and its pull requests cannot merge without a human review (all demonstrated by tests).
- The dashboard shows violations by team, exception age, time to fix and bypass rate.

**Stretch goals.** Policy impact analysis: before merging a new rule, evaluate it against the last 30 days of recorded inputs and report how many decisions would change.

**What it proves to an employer.** You can build and run a policy platform that security, platform and audit teams all rely on.

## Feeds into

- The [OV03 capstone](../README.md): P2 and P3 are its CI hardening and policy components.
- [OV01A Cloud Security Posture, Detection and Response](../../OV01_cloud_security/OV01A_cloud_security_posture_detection_and_response/README.md): guardrail tests and CI audit detections connect to cloud detection.
- [OV12 Agent Infrastructure and Platform Engineering](../../OV12_agent_infrastructure_platform/README.md): agent identity and path policies generalise to agent platforms.
- [OPS501 Frontier Seminar: Autonomous Infrastructure and Self-Healing Systems](../../../03_majors/devops_sre_platform_engineering/year_5/OPS501_frontier_seminar_autonomous_infrastructure/README.md): policy as the safety boundary for autonomous operations.
