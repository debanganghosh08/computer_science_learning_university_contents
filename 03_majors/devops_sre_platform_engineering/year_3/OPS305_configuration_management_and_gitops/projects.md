# OPS305 · Labs and projects

Labs run on local VMs (Multipass, Vagrant or libvirt) for Ansible and on two to four kind or k3d clusters for GitOps. Use a public Git host with free private repositories and a local [Gitea](https://about.gitea.com/) if you want to practise offline. Never commit a real secret: use generated test credentials. Labs 2, 7 and 9 are done without AI assistance.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Declarative rewrite | Convert a provided imperative setup script to Ansible; introduce drift by hand and detect it with `--check --diff` | Playbook, drift report | 3 h |
| 2 · Idempotent Ansible | Rewrite 10 `shell` tasks as modules; prove the second run reports `changed=0` | Playbook, two run logs | 3 h |
| 3 · Molecule and rolling | Turn the OPS302 hardening into a role; test it with Molecule on two distributions; roll it to 12 VMs in batches of 3 with a health gate | Role repository, Molecule output, rolling-run log showing a halted batch | 6 h |
| 4 · Golden image | Packer image with the role baked in; replace a 6-VM fleet with zero failed requests under load | Packer template, version tags, k6 summary | 5 h |
| 5 · Argo CD deep dive | App-of-apps, AppProjects for two teams, sync waves for a migration, a custom health check, a fixed sync loop | Manifests, screenshots of health, root cause of the loop | 6 h |
| 6 · Flux and Kargo | Bootstrap Flux; image automation for dev; Kargo promotion dev → staging → prod with a verification step | Repository, promotion history | 5 h |
| 7 · Rendered-output checks | CI that renders Helm/Kustomize, runs kubeconform and Kyverno CLI, and posts a diff; three planted bad changes must fail | Workflow, three failing PR logs | 4 h |
| 8 · Secrets | Same app with SOPS+age, Sealed Secrets and External Secrets+OpenBao; rotate a password in each; purge a planted secret from history | Threat table, rotation timings, gitleaks report | 5 h |
| 9 · Drift and waves | Daily drift report across hosts and clusters; push a config change to 4 clusters in waves; stop a bad one at wave 1 | Report, wave log | 4 h |
| 10 · Rebuild from Git | Delete a cluster; rebuild it with all workloads and secrets from Git | Timed recording, list of things not in Git | 4 h |

## Projects

### P1 · A hardened-host Ansible role worth publishing (L1, ~6 hours)

**Real-world inspiration:** CIS Benchmarks hardening, which many organisations automate with Ansible roles, and Molecule, the standard way to test roles ([Molecule docs](https://ansible.readthedocs.io/projects/molecule/)).

**What to build:** a reusable role (in a collection) that hardens a Linux host (SSH, sudo, firewall, auditd, time sync, automatic security updates), with variables for exceptions, documentation and tests.

**Acceptance criteria:**
- **Idempotency:** the Molecule idempotence step passes; the second run reports `changed=0`.
- **Portability:** the tests pass on Ubuntu 26.04 and a RHEL-compatible 10.x image.
- **Quality:** `ansible-lint` passes in its production profile; no `shell` or `command` task lacks `changed_when` and `creates` or equivalent.
- **Evidence:** an OpenSCAP or Lynis scan after applying the role shows at least the OPS302 P2 score.
- **Docs:** a README lists every variable, its default and its security impact.

**Stretch goals:** publish the collection to Ansible Galaxy; add a check-mode-only "audit" playbook that reports drift without changing anything.

**What it proves to an employer:** you write automation that is safe to run on a fleet more than once, which is the minimum bar for operations code.

### P2 · GitOps for three environments and two clusters (L2, ~15 hours)

**Real-world inspiration:** the [OpenGitOps](https://opengitops.dev/) principles; the [rendered manifests pattern](https://akuity.io/blog/the-rendered-manifests-pattern) used to make GitOps changes reviewable.

**What to build:** a GitOps setup with Argo CD or Flux (your choice, justified) for a three-service app:
- dev, staging and prod environments across two clusters;
- promotion by pull request or Kargo;
- Helm or Kustomize with pinned versions and rendered-diff review in CI;
- secrets through SOPS or External Secrets;
- Kyverno policies;
- notifications to chat.

**Acceptance criteria:**
- **New environment:** adding a fourth environment takes one pull request and is running in under 15 minutes after merge.
- **Self-heal:** a manual `kubectl edit` to a prod Deployment is reverted within 3 minutes, and a notification records it.
- **Rollback:** a bad release is rolled back with `git revert` in under 5 minutes from decision to healthy.
- **Secrets:** gitleaks over the full history finds zero secrets; one secret is rotated without redeploying the app.
- **Policy:** a PR that adds a privileged container or an unpinned image fails CI and would also be denied at admission.
- **Docs:** a classmate deploys a new service by following your README alone.

**Stretch goals:** both Argo CD and Flux managing different layers; image automation for dev only.

**What it proves to an employer:** you can run Kubernetes delivery the way most cloud-native teams do in 2026, with review, audit and fast recovery.

### P3 · Fleet configuration platform with a disaster-recovery drill (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** Facebook's Configerator ([SOSP 2015](https://research.facebook.com/publications/holistic-configuration-management-at-facebook/)) validated and canaried configuration changes. Google Cloud's June 2025 report ([incident](https://status.cloud.google.com/incidents/ow5i3PPK96RduMcb1SsW)) committed to propagating globally replicated data incrementally with validation.

**What to build:** one control repository that defines everything for a small company (an *illustrative scenario*):
- a VM fleet (golden images plus Ansible) for a database and legacy services;
- three Kubernetes clusters managed by GitOps;
- staged configuration propagation in waves with automatic health gates;
- secrets through External Secrets and OpenBao;
- policy guardrails;
- a daily drift report;
- a documented break-glass procedure;
- a full disaster-recovery runbook.

**Acceptance criteria:**
- **DR:** from total loss of one cluster and its VMs, everything is rebuilt and serving in under 45 minutes, timed and recorded, with the manual steps listed (target: fewer than 5).
- **Containment:** a planted invalid configuration (bad schema and doubled size) is stopped at wave 1, affects at most one cluster, and is reported automatically.
- **Drift:** the drift report finds 5 of 5 planted drifts (two on VMs, three in clusters) within 24 hours.
- **Audit:** every production change in the project period maps to a reviewed commit, and the break-glass drill's change is written back to Git within 1 hour.
- **Agent test:** an AI agent with a scoped identity opens 5 change PRs; none reaches prod without human approval and all pass the same checks as human PRs.

**Stretch goals:** Talos Linux nodes managed entirely through its API; an error-budget-aware promotion gate using [OPS304](../OPS304_site_reliability_engineering_slos_error_budgets/README.md) burn rates.

**What it proves to an employer:** you can run configuration for a whole organisation reproducibly, contain configuration incidents and recover from disaster. That is senior platform and infrastructure work.

## Feeds into

- [OPS401 Platform Engineering](../../year_4/OPS401_platform_engineering_and_internal_developer/README.md): P2 and P3 become the delivery backbone of an internal developer platform.
- [OPS402 Chaos Engineering](../../year_4/OPS402_chaos_engineering_and_resilience/README.md): rebuild-from-Git is a disaster-recovery experiment.
- [OV03B Policy as Code and Secure CI/CD](../../../../04_overlaps/OV03_devsecops/OV03B_policy_as_code_and_secure_ci_cd/README.md): Chapter 11's guardrails go deeper there.
- [OV01B Kubernetes and Container Security](../../../../04_overlaps/OV01_cloud_security/OV01B_kubernetes_and_container_security/README.md): secrets and admission policy.
