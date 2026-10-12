# OPS305 · Configuration Management and GitOps

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 6 | 4 (≈ 120 hours) | L2 → L3 (P3 reaches L4) | [CS215](../../../../02_year_2_core_computer_science/semester_4/CS215_cloud_and_devops_foundations/README.md), [CS203](../../../../02_year_2_core_computer_science/semester_3/CS203_operating_systems/README.md); strongly recommended: [OPS301](../OPS301_ci_cd_engineering/README.md), [OPS302](../OPS302_linux_systems_administration_in_depth/README.md) | [OPS401](../../year_4/OPS401_platform_engineering_and_internal_developer/README.md), [OV03B](../../../../04_overlaps/OV03_devsecops/OV03B_policy_as_code_and_secure_ci_cd/README.md) |

Part of the [DevOps, SRE and Platform Engineering major](../../README.md). Provisioning cloud resources with Terraform or OpenTofu is taught in [CLD302](../../../cloud_engineering/year_3/CLD302_infrastructure_as_code_terraform_opentofu/README.md), and writing Helm charts and Kustomize overlays in [CLD303](../../../cloud_engineering/year_3/CLD303_containers_and_kubernetes/README.md). This course covers what happens next: keeping thousands of hosts and dozens of clusters in a known, reviewed, reproducible state, and changing that state safely through Git. Network-device automation is covered in [NET303](../../../it_infrastructure_networking/year_3/NET303_network_automation_and_netdevops/README.md).

## Why this course matters now

Most production changes are configuration changes, and configuration causes some of the largest outages. In June 2025, a policy change at Google Cloud "was replicated globally within seconds" and crashed API serving. In November 2025, a permissions change caused a generated Cloudflare configuration file to double in size before it was pushed network-wide. Facebook's 2015 paper on holistic configuration management described treating configuration changes like code, with review, canaries and automated testing, years earlier.

The tools have consolidated:

- **GitOps (OpenGitOps):** system state is declared, versioned and immutable, pulled automatically and continuously reconciled. Argo CD (3.5 in August 2026) and Flux (2.9) are both CNCF graduated, and promotion tools such as Kargo sit on top.
- **Configuration management:** Ansible (ansible-core 2.21, May 2026) remains the default for hosts. When Perforce stopped public Puppet packaging in late 2024, the community forked it as OpenVox.

AI assistants write playbooks, values files and Argo CD manifests in seconds, and agents now open pull requests against environment repositories. That is exactly why GitOps matters: every change, human or agent, becomes a reviewed, auditable, revertible commit. The engineer who designs the repository layout, promotion flow, secrets model and drift policy decides whether that safety is real.

## Learning outcomes

By the end you can:

1. **Explain** desired-state configuration, convergence, idempotency and drift, and **choose** mutable configuration management, immutable images or GitOps for a given system.
2. **Write** idempotent Ansible roles and collections with tests (Molecule), linting and safe rolling execution across a fleet.
3. **Build** immutable golden images (Packer, cloud-init) and **replace** hosts instead of patching them in place where that fits.
4. **Design** GitOps repositories (structure, environments, promotion by pull request, rendered manifests) that scale to many teams and clusters.
5. **Operate** Argo CD and Flux in depth: sync policies, health, waves and hooks, ApplicationSets, multi-cluster, image automation.
6. **Use** Helm and Kustomize inside GitOps with pinned versions, rendered-output review and policy checks.
7. **Manage** secrets without plaintext in Git (SOPS with age or KMS, Sealed Secrets, External Secrets Operator with Vault or OpenBao) and **compare** their threat models.
8. **Detect and resolve** drift, run break-glass changes safely, and **rebuild** an environment from Git after total loss.
9. **Govern** AI- and agent-authored configuration changes with review rules, policy checks and staged propagation.

## Chapters and lessons

### Chapter 1 · Configuration as a discipline (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Desired state | Imperative scripts vs declarative state; convergence loops; idempotency as a property you can test | Turn a 30-line setup script into declarative state and run it three times |
| 1.2 Drift and snowflakes | How drift happens (hotfixes, consoles, auto-updates); pets vs cattle | Introduce drift on a VM and detect it |
| 1.3 Config is code and data | Static config, dynamic config, feature flags, generated config; who reviews each | Classify 20 config items from a real project by type and risk |
| 1.4 Config incidents | Facebook's Configerator (SOSP 2015); Google Cloud June 2025; Cloudflare November 2025 | List the validation each incident lacked |

**Check your understanding:** (1) Why is "run the script again" not the same as idempotency? (2) Which kind of config change deserves a canary? (3) What makes generated config riskier than hand-written config?

### Chapter 2 · Ansible done right (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Inventory | Static and dynamic inventories (cloud plugins), groups, host and group vars | Build a dynamic inventory from VM labels |
| 2.2 Modules over shell | Why `command`/`shell` break idempotency; `creates`, `changed_when`, `check_mode` | Rewrite 10 shell tasks as idempotent module calls |
| 2.3 Variables and templates | Precedence rules, Jinja2, facts, `--diff` | Explain the precedence of one variable defined in 4 places |
| 2.4 Handlers and ordering | Notify, flush, restart storms | Make a config change restart a service exactly once |

**Check your understanding:** (1) What does `changed=0` on a second run prove, and what not? (2) Why is `--check` unreliable with shell tasks? (3) How can variable precedence cause a production incident?

### Chapter 3 · Ansible at scale (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Roles and collections | Structure, defaults vs vars, Galaxy, versioning | Package the OPS302 hardening as a role |
| 3.2 Testing | `ansible-lint`, Molecule scenarios across distributions, idempotency test | Test the role on Ubuntu 26.04 and a RHEL-compatible 10.x image |
| 3.3 Safe fleet execution | `serial`, `max_fail_percentage`, health checks between batches, `run_once` | Roll a change across 12 hosts in batches of 3 with a health gate |
| 3.4 Running Ansible as a service | Execution environments, AWX, pull mode, secrets with Ansible Vault | Run playbooks from AWX with RBAC and an audit log |

**Check your understanding:** (1) Why test roles on two distributions? (2) What should stop a rolling playbook? (3) Why is running Ansible from a laptop a governance problem?

### Chapter 4 · The configuration management landscape (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Agent-based tools | Puppet and its community fork OpenVox, Chef, Salt: catalogs, agents, pull intervals | Compare one task in Ansible and OpenVox |
| 4.2 First boot | cloud-init, Ignition (Flatcar), user data limits | Bootstrap a VM entirely from cloud-init |
| 4.3 Declarative operating systems | NixOS and image-based OSes as an alternative to configuration management | Read and summarise one NixOS configuration |
| 4.4 Choosing | Fleet size, change rate, team skills, licence risk | Write a tool choice for a bank, a startup and a game studio |

**Check your understanding:** (1) What problem does an agent's pull interval create during an incident? (2) Why did the Puppet licensing change matter to operators? (3) When is cloud-init enough?

### Chapter 5 · Immutable infrastructure (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Golden images | Packer templates, versioning, CIS-hardened bases, image promotion | Build a versioned image with your Ansible role inside |
| 5.2 Replace, don't patch | Rolling replacement of fleets, instance refresh, blue-green fleets | Replace 6 VMs with a new image with no failed requests |
| 5.3 Immutable OS for nodes | Talos Linux, Flatcar, Bottlerocket: API-managed, no SSH | Run a Talos cluster locally; change config through its API |
| 5.4 Where mutability stays | Databases, bare metal, long-lived appliances | Draw the mutable/immutable boundary for a whole system |

**Check your understanding:** (1) Why does immutable infrastructure make incident forensics both easier and harder? (2) What breaks when an image is rebuilt with "latest" packages? (3) Why remove SSH from nodes?

### Chapter 6 · GitOps principles and repository design (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 OpenGitOps | Declarative; versioned and immutable; pulled automatically; continuously reconciled | Map your CS215 deploy against the four principles |
| 6.2 Push vs pull | CI pushing with credentials vs in-cluster agents pulling; security and scale trade-offs | Remove cluster credentials from CI entirely |
| 6.3 Repository layouts | Monorepo vs app/config split, folder-per-environment (not branch-per-environment), app-of-apps | Design a layout for 8 teams, 3 environments, 4 clusters |
| 6.4 Rendered manifests | Committing rendered output for review; Argo CD's source hydrator; diffs reviewers can read | Render Helm output into a branch and review a diff |

**Check your understanding:** (1) Why is branch-per-environment an anti-pattern? (2) What does a pull model remove from your attack surface? (3) Why might reviewers approve a Helm values change they do not understand, and how does rendering help?

### Chapter 7 · Argo CD in depth (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Applications and Projects | Source, destination, sync status vs health status, AppProjects for multi-tenancy | Isolate two teams with AppProjects |
| 7.2 Sync behaviour | Auto-sync, prune, self-heal, sync waves and hooks, `ignoreDifferences`, server-side apply | Order a database migration before an app with waves |
| 7.3 ApplicationSets | Git, cluster, list and matrix generators; templating many apps | Deploy one app to 4 clusters from one ApplicationSet |
| 7.4 Health and diffing | Custom health checks (Lua), out-of-sync loops, noisy diffs | Fix a perpetual out-of-sync caused by a mutating webhook |
| 7.5 Operating Argo CD | HA, RBAC, SSO, scaling the application controller, upgrades | Upgrade Argo CD one minor version with no app disruption |

**Check your understanding:** (1) What is the difference between "Synced" and "Healthy"? (2) When is auto-prune dangerous? (3) What causes a sync loop, and how do you find it?

### Chapter 8 · Flux and promotion (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Flux controllers | Source, Kustomize, Helm and notification controllers; OCI artifacts as sources | Bootstrap Flux and deploy from an OCI artifact |
| 8.2 Image automation | Image reflector and automation controllers writing tags back to Git | Auto-update dev on new images; require PRs for prod |
| 8.3 Argo CD vs Flux | UI, multi-tenancy, architecture, ecosystem; when to choose each | Write a one-page comparison with evidence from your labs |
| 8.4 Promotion pipelines | Kargo stages and freight, verification between stages, promotion by PR | Promote dev → staging → prod with Kargo and a verification step |

**Check your understanding:** (1) Why should prod not auto-update image tags? (2) What does an OCI artifact source give you that a Git source does not? (3) What should be verified before a promotion?

### Chapter 9 · Helm and Kustomize inside GitOps (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Pinning and values | Chart versions pinned, values per environment, values schemas (Helm 4) | Upgrade a chart with a schema that catches a bad value |
| 9.2 Kustomize overlays and components | Bases, overlays, components for optional features, replacements | Add an optional feature to 2 of 3 environments |
| 9.3 Checking rendered output | `kubeconform`, Kyverno CLI, `argocd app diff`, `flux diff` in pull requests | Fail a PR that would remove resource limits |
| 9.4 Third-party charts | Vendoring, upstream changes, supply-chain checks | Vendor and review an upstream chart upgrade |

**Check your understanding:** (1) Why check the rendered manifests rather than the values file? (2) What risk does an unpinned chart add? (3) When should you vendor a chart?

### Chapter 10 · Secrets in GitOps (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 The rule | No plaintext secrets in Git, ever, including history; scanning with gitleaks | Find and purge a planted secret from history |
| 10.2 Encrypted in Git | SOPS (CNCF sandbox) with age or cloud KMS; Sealed Secrets | Encrypt per-environment secrets with SOPS and decrypt in Flux |
| 10.3 References in Git | External Secrets Operator with Vault, OpenBao or a cloud secret manager; rotation | Rotate a database password without a deploy |
| 10.4 Threat models | Who can decrypt, key rotation, blast radius, audit, disaster recovery of keys | Compare three approaches in a threat table |

**Check your understanding:** (1) Why is deleting a secret in a later commit not enough? (2) What happens to SOPS-encrypted secrets if the age key is lost? (3) When is External Secrets better than encrypted-in-Git?

### Chapter 11 · Drift, fleets and recovery (weeks 11–12)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Detecting drift | Reconciler status, scheduled `terraform plan` drift jobs (from CLD302), Ansible check runs | Build a daily drift report across hosts and clusters |
| 11.2 Break-glass | Emergency manual changes, pausing reconciliation, writing the change back to Git | Practise a break-glass fix and reconcile it |
| 11.3 Staged propagation | Waves across clusters, progressive syncs, health gates; the config-incident lessons from Chapter 1 | Push a config change to 4 clusters in waves; stop a bad one at wave 1 |
| 11.4 Policy guardrails | Kyverno (CNCF graduated 2026) or Gatekeeper on what may be deployed | Block privileged pods and unpinned images cluster-wide |
| 11.5 Rebuild from Git | Disaster recovery: new cluster, bootstrap, reconcile everything | Delete a cluster and rebuild it from Git; time it |

**Check your understanding:** (1) Why must break-glass changes be written back to Git quickly? (2) What would stop a bad config at wave 1? (3) What is not in Git that you still need to rebuild a cluster?

### Chapter 12 · Agents and AI in a GitOps world (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Agents as committers | Agents opening PRs to environment repos; identities, scopes, CODEOWNERS | Let an agent propose a scaling change; require human approval for prod |
| 12.2 Verifying generated config | Lint, schema, policy, rendered diff, dry-run, staged rollout | Catch 5 planted errors in AI-generated playbooks and values |
| 12.3 Reverting is a commit | Fast rollback with `git revert`, its limits (migrations, external state) | Revert a bad change in under 5 minutes; list what revert cannot undo |
| 12.4 Audit and compliance | Mapping every production change to a reviewed commit and an identity (human or agent); evidence an auditor accepts | Produce a one-month change audit from Git history and Argo CD or Flux events |

**Check your understanding:** (1) Why is a GitOps repo a better interface for an agent than direct cluster access? (2) What can `git revert` not undo? (3) Which changes should never be auto-merged?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Declarative rewrite | Drift demo |
| 2 | 2 | Lab 2 · Idempotent Ansible | Second run `changed=0` |
| 3 | 3 | Lab 3 · Molecule and rolling | Tested role; P1 starts |
| 4 | 4 | Landscape comparison | **P1 due** |
| 5 | 5 | Lab 4 · Golden image | Image + fleet replacement |
| 6 | 6 | Repository design review | Layout doc; P2 starts |
| 7 | 7 | Lab 5 · Argo CD deep dive | Mid-term (AI off) |
| 8 | 8 | Lab 6 · Flux and Kargo | Promotion demo |
| 9 | 9 | Lab 7 · Rendered-output checks | Failing PR demo |
| 10 | 10 | Lab 8 · Secrets | **P2 due** |
| 11 | 11 | Lab 9 · Drift and waves | Drift report |
| 12 | 11 | Lab 10 · Rebuild from Git | Timed rebuild; P3 design review |
| 13 | 12 | Agent PR gauntlet | Verification log |
| 14 | 12 | P3 DR drill | **P3 due** |
| 15 | Review | Practical exam and oral | Final |

## Working with AI in this course

- **Use AI for:** first drafts of Ansible tasks, Molecule scenarios, Argo CD Applications, ApplicationSets and Kustomize overlays; explaining a confusing sync diff; converting shell scripts to modules. Named tools: Claude Code, GitHub Copilot, Ansible Lightspeed, Cursor.
- **Do without AI (drills):** variable-precedence puzzles; designing a repository layout; reading a rendered diff and predicting what will change in the cluster; the secrets threat table; the mid-term and practical exam.
- **Verify AI output by:** `ansible-lint` and a Molecule idempotency test (second run must report no changes); `--check --diff`; `kubeconform` and Kyverno CLI on rendered manifests; `argocd app diff` or `flux diff` before merge; gitleaks on every PR; rolling out in waves.
- **Where AI still fails here (show it):** generated playbooks often use `shell` where a module exists (breaking idempotency), target `hosts: all` by default, or put secrets in plain variables. Generated Argo CD manifests often turn on auto-prune for everything. Log each occurrence you find in Lab 12.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs 1–10 | 25% |
| Projects P1 / P2 / P3 | 5% / 15% / 25% |
| Mid-term (AI off) | 10% |
| Practical exam (3 hours, AI off) + oral | 20% |

**Mastery gate.** You pass when you can, without AI help: (1) write an Ansible role from a specification that passes Molecule on two distributions and reports zero changes on the second run, in 90 minutes; (2) rebuild a deleted cluster's workloads from a GitOps repository in under 30 minutes, including secrets; (3) given a repository with five planted problems (plaintext secret in history, branch-per-environment drift, unpinned chart, auto-prune on a stateful app, missing health check), find and fix all five in 45 minutes.

## Industry reality

GitOps with Argo CD or Flux is the default delivery model for Kubernetes in many product companies. The CNCF offers the Certified Argo Project Associate (CAPA) and GitOps Certified Associate (CGOA) exams. Ansible remains common in enterprises and Indian IT services firms for hosts and network devices (unconfirmed as a measured share). Facebook's Configerator paper (SOSP 2015) describes the same ideas at very large scale: configuration in source control, automated validation and canarying of config changes.

**Interview questions from this course**

1. *How would you structure GitOps for 20 teams and 3 environments?* Strong answer: separate app and environment config, folder-per-environment, AppProjects or tenants per team, ApplicationSets for fan-out, promotion by PR (or Kargo), rendered-diff review, policy checks, and clear ownership via CODEOWNERS.
2. *How do you handle secrets with GitOps?* Strong answer: never plaintext; compares SOPS/age, Sealed Secrets and External Secrets with a vault; key management and rotation; history scanning; DR of keys; least privilege for decryption.
3. *Someone fixed production by hand with `kubectl edit`. What happens next?* Strong answer: self-heal reverts it unless paused; break-glass process; write the change back to Git; review why the normal path was too slow; drift alerts.
4. *What makes an Ansible playbook production-quality?* Strong answer: modules over shell, idempotency proven by a second run, check/diff support, roles with defaults, Molecule tests, linting, `serial` with health checks, vaulted secrets, run from a controlled runner with audit.
5. *A config change took down every region at once. Design the controls.* Strong answer: schema and size validation in CI, canary config, waves with health gates, consumer-side validation and last-known-good fallback, fast revert path, separate rate of change for config vs binaries; cites Google Cloud 2025 or Cloudflare 2025.

## Resources (free first)

- **Principles and papers:** [OpenGitOps](https://opengitops.dev/); Tang et al., [Holistic Configuration Management at Facebook](https://research.facebook.com/publications/holistic-configuration-management-at-facebook/) (SOSP 2015); Akuity, [The Rendered Manifests Pattern](https://akuity.io/blog/the-rendered-manifests-pattern); SRE workbook, [Configuration Design and Best Practices](https://sre.google/workbook/configuration-design/).
- **Tools:** [Argo CD](https://argo-cd.readthedocs.io/en/stable/), [Flux](https://fluxcd.io/flux/), [Kargo](https://docs.kargo.io/), [Ansible docs](https://docs.ansible.com/), [Molecule](https://ansible.readthedocs.io/projects/molecule/), [Packer](https://developer.hashicorp.com/packer), [Talos Linux](https://www.talos.dev/), [Flatcar](https://www.flatcar.org/), [OpenVox](https://voxpupuli.org/openvox/).
- **Secrets:** [SOPS](https://github.com/getsops/sops), [External Secrets Operator](https://external-secrets.io/latest/), [OpenBao](https://openbao.org/), [Sealed Secrets](https://github.com/bitnami-labs/sealed-secrets), [gitleaks](https://github.com/gitleaks/gitleaks).
- **Policy:** [Kyverno](https://kyverno.io/), [OPA Gatekeeper](https://open-policy-agent.github.io/gatekeeper/website/).
- **Practice locally:** several kind or k3d clusters on one laptop for multi-cluster labs; Multipass or Vagrant VMs for Ansible fleets.
- **Certifications:** [CNCF CAPA and CGOA](https://www.cncf.io/training/certification/).

## Sources

All checked 12 Oct 2026.
- Google Cloud, [incident report](https://status.cloud.google.com/incidents/ow5i3PPK96RduMcb1SsW) (12 Jun 2025); Cloudflare, [18 November 2025 outage](https://blog.cloudflare.com/18-november-2025-outage/).
- [OpenGitOps principles](https://opengitops.dev/).
- CNCF maturity (Argo graduated 6 Dec 2022; Flux graduated 30 Nov 2022; SOPS sandbox 2023; Kyverno graduated 16 Mar 2026) from the [CNCF landscape](https://github.com/cncf/landscape) data file.
- Versions on 12 Oct 2026: Argo CD 3.5 (released 4 Aug 2026) and ansible-core 2.21 (31 May 2026) from [endoflife.date](https://endoflife.date/); Flux 2.9.6 and Kargo 1.12.3 from GitHub releases.
- Vox Pupuli, [OpenVox](https://voxpupuli.org/openvox/) (Perforce discontinued public Puppet packaging in late 2024; community soft-fork).
- Akuity, [The Rendered Manifests Pattern](https://akuity.io/blog/the-rendered-manifests-pattern) (updated July 2026; covers Argo CD source hydrator).
- [CNCF certifications](https://www.cncf.io/training/certification/) (CAPA, CGOA).

_Last reviewed: 2026-10_
