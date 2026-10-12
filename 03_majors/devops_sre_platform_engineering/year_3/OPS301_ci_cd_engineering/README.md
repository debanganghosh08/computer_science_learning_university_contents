# OPS301 · CI/CD Engineering

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 5 | 4 (≈ 120 hours) | L2 → L3 (P3 reaches L4) | [CS215](../../../../02_year_2_core_computer_science/semester_4/CS215_cloud_and_devops_foundations/README.md), [CS203](../../../../02_year_2_core_computer_science/semester_3/CS203_operating_systems/README.md) | [OPS401](../../year_4/OPS401_platform_engineering_and_internal_developer/README.md), [OV03A](../../../../04_overlaps/OV03_devsecops/OV03A_software_supply_chain_security/README.md), [OV03B](../../../../04_overlaps/OV03_devsecops/OV03B_policy_as_code_and_secure_ci_cd/README.md) |

Part of the [DevOps, SRE and Platform Engineering major](../../README.md). [CS215](../../../../02_year_2_core_computer_science/semester_4/CS215_cloud_and_devops_foundations/README.md) taught you to build one pipeline with tests, caching, a canary and the DORA four keys. This course treats the delivery system itself as production software: fast, measurable, safe at company scale, and able to absorb the extra change volume that AI coding agents create. GitOps delivery is taught in [OPS305](../OPS305_configuration_management_and_gitops/README.md), deep supply-chain security in [OV03A](../../../../04_overlaps/OV03_devsecops/OV03A_software_supply_chain_security/README.md), and test design in [QAE304](../../../software_quality_test_engineering/year_3/QAE304_testing_in_ci_cd_and_test_infrastructure/README.md).

## Why this course matters now

Code is getting cheaper to write; changing production safely is not. DORA's 2025 research found AI adoption now positively related to delivery throughput, but warned that "without robust control systems, like strong automated testing, mature version control practices, and fast feedback loops, an increase in change volume leads to instability". DORA now measures delivery with five metrics, adding deployment rework rate and replacing MTTR with failed deployment recovery time. The largest outages of recent years were delivery failures, and many shipped configuration or data rather than code:

- **CrowdStrike (July 2024):** a sensor content update crashed Windows hosts; the root-cause analysis lists "Template Instances should have staged deployment" among its mitigations.
- **Google Cloud (June 2025):** a policy change "was replicated globally within seconds" and hit a code path that was not protected by a feature flag.
- **Cloudflare (November 2025):** a generated feature file doubled in size and was pushed across the network.

The pipeline is also an attack surface. A compromised GitHub Action leaked secrets in March 2025, and an inappropriately scoped token let an attacker commit code that shipped in the Amazon Q Developer VS Code extension (July 2025). Agents such as GitHub Copilot's coding agent, GitLab Duo Agent Platform and Claude Code now write pipeline YAML and open pull requests. The engineer who stays valuable designs the gates those changes pass through, and can prove that the gates work.

## Learning outcomes

By the end you can:

1. **Design** a pipeline as a dependency graph with explicit time budgets, and **measure** time-to-green, its critical path, queue time and flake rate.
2. **Implement** the same delivery flow in GitHub Actions, GitLab CI and Jenkins, and **explain** where each engine's model helps or hurts.
3. **Cut** build time with hermetic, content-addressed caching (BuildKit, Bazel or Gradle remote cache), and **prove** the cache is correct.
4. **Build once and promote** immutable, digest-addressed artifacts through environments, with retention and mirroring policies.
5. **Choose and implement** rolling, blue-green, canary, shadow and feature-flag releases, including expand-contract database migrations with zero failed requests.
6. **Automate** canary analysis with Argo Rollouts or Flagger, using SLI queries and statistical comparison, with automatic abort.
7. **Treat** configuration and data pushes as deployments: staged, validated, size-bounded and reversible.
8. **Generate** SBOMs, sign artifacts keylessly, attach SLSA provenance and **verify** it at admission (intro level).
9. **Compute** the five DORA metrics from Git and deployment events, and **explain** how each can be gamed.
10. **Govern** AI-authored changes with rulesets, required checks, CODEOWNERS and least-privilege agent identities.

## Chapters and lessons

### Chapter 1 · The pipeline as a product (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Pipelines as DAGs | Stages vs `needs:` graphs; critical path; fan-out/fan-in; why a 30-minute pipeline means people batch changes | Draw your CS215 pipeline as a DAG and mark the critical path |
| 1.2 Pipeline SLOs | Time-to-green p50/p95, queue time, flake rate, red-main minutes per week | Instrument a pipeline to emit these four numbers |
| 1.3 Trunk-based development | Short-lived branches, merge queues (GitHub merge queue, GitLab merge trains), keeping `main` releasable | Enable a merge queue and show it catches a semantic conflict |
| 1.4 Value stream mapping | Wait time vs work time from commit to production; DORA's "working in small batches" capability | Map one change end to end; find the longest wait |

**Check your understanding:** (1) Why can adding parallel jobs make time-to-green worse? (2) What does a merge queue protect that branch protection alone does not? (3) Why is queue time often a bigger win than faster tests?

### Chapter 2 · Pipeline engines in depth (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 GitHub Actions internals | Events, contexts and expressions, reusable workflows vs composite actions, `concurrency:` groups, environments with protection rules | Build a reusable deploy workflow called by three repos |
| 2.2 GitLab CI | `rules:`, `needs:` DAGs, parent-child and multi-project pipelines, CI/CD components and the CI catalog | Port the same pipeline to GitLab CI with components |
| 2.3 Jenkins, honestly | Controller/agent model, declarative Jenkinsfile, shared libraries, plugin sprawl; how to migrate without a big bang | Run Jenkins in a container; port the pipeline; list three migration risks |
| 2.4 Containers as the pipeline | Tekton (a CNCF incubating project since March 2026) and Dagger: pipelines as Kubernetes resources or as code in an SDK | Run one stage locally with Dagger and in CI unchanged |
| 2.5 Runners at scale | Ephemeral self-hosted runners, Actions Runner Controller on Kubernetes, autoscaling, cost per runner-minute | Deploy ARC on kind; prove each job gets a fresh runner |

**Check your understanding:** (1) Why are long-lived self-hosted runners a security problem for public repositories? (2) When is a reusable workflow better than a composite action? (3) What makes "works on my laptop, fails in CI" disappear with container-native pipelines, and what does it not fix?

### Chapter 3 · Builds and caching (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Hermetic and reproducible builds | Pinned toolchains, lockfiles, `SOURCE_DATE_EPOCH`, why non-hermetic builds poison caches | Build the same commit twice and diff the artifacts byte by byte |
| 3.2 Content-addressed caching | Cache keys from input hashes; local vs remote cache; cache poisoning risks | Design keys for a Python and a Java project; break one on purpose |
| 3.3 Container build caching | BuildKit cache mounts, `--cache-from`/`--cache-to` registry cache, layer ordering | Cut a Docker build from minutes to seconds on a no-op change |
| 3.4 Monorepo builds | Bazel remote cache and remote execution, Gradle build cache, Nx/Turborepo "affected" graphs | Run only affected targets for a one-file change; measure hit rate |

**Check your understanding:** (1) A cache hit produced a wrong binary. Name two causes. (2) Why does a remote cache need write access control? (3) When does test selection by "affected" targets miss a real break?

### Chapter 4 · Testing stages and flake control (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Test portfolio as a cost model | Which tests run per commit, per merge, nightly; cost and signal per test class | Classify 50 tests by speed and the bugs they caught |
| 4.2 Sharding and test impact analysis | Parallel shards balanced by timing data; selecting tests from the change graph | Shard a suite into 4 balanced jobs (max/min runtime ≤ 1.2) |
| 4.3 Flaky tests | Detection by reruns, quarantine with owners and deadlines, root causes (time, order, network, shared state) | Find and fix three planted flakes |
| 4.4 Contracts and ephemeral environments | Consumer-driven contracts (Pact), per-PR preview environments and their teardown | Spin up and destroy a preview environment per PR |

**Check your understanding:** (1) Why is "retry failed tests twice" dangerous as a permanent policy? (2) What does a contract test catch that an end-to-end test catches too late? (3) How do you decide that a test belongs in the nightly run?

### Chapter 5 · Artifact management (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Build once, promote by digest | Tags are mutable, digests are not; promotion as metadata, not rebuild | Promote one digest through dev, staging and prod |
| 5.2 Registries | Harbor (CNCF graduated 2020), Artifactory, Nexus, GHCR; replication, quotas, immutability rules | Run Harbor locally with tag immutability on `release-*` |
| 5.3 OCI artifacts | Helm charts, SBOMs and signatures stored next to images (ORAS) | Push an SBOM as an OCI artifact referencing an image |
| 5.4 Dependency proxies and retention | Pull-through caches, upstream rate limits and outages, garbage collection, legal holds | Survive an "upstream registry down" drill with a mirror |

**Check your understanding:** (1) Why does rebuilding for production break the evidence chain? (2) What should a retention policy never delete? (3) How does a pull-through cache change your blast radius during an upstream outage?

### Chapter 6 · Deployment strategies (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 The strategy menu | Recreate, rolling, blue-green, canary, shadow (dark) traffic, A/B; cost and rollback speed of each | Fill a decision table for five services |
| 6.2 Deploy is not release | Feature flags with OpenFeature (CNCF incubating), kill switches, flag debt | Ship a dark feature and release it to 5% of users |
| 6.3 Database changes | Expand-contract (parallel change), backfills, online schema change; tools such as Flyway, Liquibase, Atlas | Rename a column under load with zero failed requests |
| 6.4 Compatibility windows | N/N-1 API and message compatibility, mixed-version fleets during rollout | Break compatibility on purpose; catch it with a contract test |

**Check your understanding:** (1) Why is blue-green unsafe when the database schema changes in the same release? (2) What new failure mode do feature flags introduce? (3) A rollback is impossible after the contract phase: how do you design around that?

### Chapter 7 · Progressive delivery and automated analysis (weeks 7–8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Argo Rollouts | `Rollout` steps, `AnalysisTemplate` with Prometheus queries, traffic shaping through Gateway API or a mesh | Canary with automatic abort on error-rate SLI |
| 7.2 Flagger | Canary, A/B and blue-green with metric checks and webhooks | Repeat 7.1 with Flagger; compare the models |
| 7.3 Automated canary analysis | Baseline vs canary (not vs old fleet), metric selection, statistical tests (Mann-Whitney), bake time; Netflix and Google's Kayenta | Write a judge that compares canary and baseline distributions |
| 7.4 Waves and cells | One-box, then waves by region or cell, with bake times; AWS's published "hands-off deployment" practice | Model a 4-wave rollout and compute time to 100% |
| 7.5 Configuration and data rollouts | Config is code: validation, size limits, staged propagation, last-known-good fallback (CrowdStrike 2024, Google Cloud 2025, Cloudflare 2025) | Stage a config file push; make a doubled-size file stop at wave 1 |

**Check your understanding:** (1) Why compare a canary against a fresh baseline instead of the existing fleet? (2) Google Cloud's faulty code passed a region-by-region rollout. Why did that not protect it? (3) What should a consumer of a generated config file do when the file is invalid?

### Chapter 8 · Release engineering (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Release models | Continuous deployment vs release trains; mobile staged rollouts; on-premise and air-gapped releases | Choose a model for three products and defend it |
| 8.2 Versioning and changelogs | SemVer, calendar versions, Conventional Commits, automated release notes | Automate versioning and notes from commit history |
| 8.3 Hotfixes and freezes | Hotfix branches, cherry-picks, change freezes before peak events and their hidden risk (big-batch thaw) | Write a freeze policy with an exception process |
| 8.4 Release engineering at Google | Hermetic builds, self-service releases, release engineers as a role (SRE book, ch. 8) | Summarise the chapter's four principles and apply one |

**Check your understanding:** (1) Why can a long change freeze increase risk afterwards? (2) What makes a hotfix process safe under pressure? (3) When is a release train better than continuous deployment?

### Chapter 9 · Supply-chain basics (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 SBOMs | SPDX and CycloneDX formats; generating with Syft; what an SBOM cannot tell you | Generate and diff SBOMs for two releases |
| 9.2 Signing and provenance | Sigstore cosign keyless signing, SLSA v1.2 build levels, GitHub artifact attestations | Sign an image and attach build provenance |
| 9.3 Verify at the door | Kyverno (CNCF graduated March 2026) `verifyImages` and admission policies | Block an unsigned image in a kind cluster |
| 9.4 Hardening the pipeline | SHA pinning (enforceable by GitHub policy since August 2025), `permissions:`, `pull_request_target` risks, actionlint and zizmor, egress control on runners; tj-actions, Amazon Q and xz case studies | Score a real workflow with zizmor and fix every high finding |

**Check your understanding:** (1) What does a signature prove, and what does it not prove? (2) Which SLSA level stops a developer from altering a build on their laptop? (3) Why did a scoped token matter in the Amazon Q extension incident?

### Chapter 10 · Measuring delivery (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 DORA's five metrics | Change lead time, deployment frequency, failed deployment recovery time, change fail rate, deployment rework rate | Define each precisely for one service |
| 10.2 Data plumbing | Events from Git, CI, deploy tools and incidents; joining commits to deployments | Build a pipeline that computes all five from webhooks |
| 10.3 Misuse | Goodhart's law, comparing teams, averages hiding tails, gaming by splitting deploys | Show how to game each metric, then design a guard |
| 10.4 Cost and footprint | Runner minutes, cache storage, artifact storage; cost per deploy | Produce a monthly cost report for your pipelines |

**Check your understanding:** (1) Why did DORA move away from MTTR? (2) How can deployment frequency rise while delivery gets worse? (3) Which metric would reveal that AI-authored changes are causing rework?

### Chapter 11 · Delivery for infrastructure, data and models (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Infrastructure pipelines | Plan in PR, policy check, approval, apply from the pipeline only; drift jobs ([CLD302](../../../cloud_engineering/year_3/CLD302_infrastructure_as_code_terraform_opentofu/README.md) owns the code) | Wire a plan/apply pipeline with OIDC and approval |
| 11.2 Database migration pipelines | Migrations as versioned artifacts, dry runs against a production-size copy, lock-time budgets | Fail a migration that would hold a lock over 2 s |
| 11.3 Model and prompt releases | Model and prompt versions as artifacts, eval gates, shadow traffic ([MLE401](../../../machine_learning_engineering/year_4/MLE401_mlops_deployment_monitoring_and_retraining/README.md)) | Add an eval gate that blocks a regressed prompt |
| 11.4 Handing off to GitOps | CI produces artifacts and opens a PR to the environment repo; CD reconciles ([OPS305](../OPS305_configuration_management_and_gitops/README.md)) | Make CI update an image digest in an environment repo |

**Check your understanding:** (1) Why must `apply` run only from the pipeline? (2) What is the equivalent of a canary for a database migration? (3) Why should a prompt change go through the same gates as code?

### Chapter 12 · AI in the delivery loop (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Agents as contributors | Copilot coding agent, GitLab Duo Agent Platform and Claude Code opening PRs; agent identities and token scopes | Give an agent a scoped identity; prove it cannot merge |
| 12.2 AI review and triage | AI code review, failed-job root-cause suggestions, flaky-test explanations: measure precision before trusting | Score 20 AI CI-failure explanations against ground truth |
| 12.3 Rulesets as guardrails | Required checks, CODEOWNERS, signed commits, path-based approvals for pipeline files | Block an agent PR that edits a workflow without owner review |
| 12.4 Capacity for more change | Smaller batches, faster pipelines and better rollback as the answer to higher change volume (DORA 2025) | Load-test your pipeline with 5× the PR rate; find the bottleneck |

**Check your understanding:** (1) Why should workflow files have stricter review than application code? (2) An AI reviewer approves 95% of PRs: what do you need to know before trusting it? (3) What is the first pipeline metric to break when agents double the PR rate?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Pipeline teardown | Baseline pipeline SLO report |
| 2 | 2 | Lab 2 · Three engines | Same pipeline in three engines |
| 3 | 3 | Lab 3 · Cache clinic | Cache hit-rate evidence; P1 starts |
| 4 | 4 | Lab 4 · Flake hunter | **P1 due** |
| 5 | 5 | Lab 5 · Promote by digest | Promotion log |
| 6 | 6 | Lab 6 · Zero-downtime migration | Load-test evidence |
| 7 | 7 | Lab 7 · Canary with analysis | P2 design review |
| 8 | 7 | Lab 7 (cont.) · Config rollout | Mid-term (AI off) |
| 9 | 8 | Release policy writing | Freeze and hotfix policy |
| 10 | 9 | Lab 8 · Sign and verify | **P2 due** |
| 11 | 10 | Lab 9 · DORA dashboard | Five-metric dashboard |
| 12 | 11 | Infra and migration pipelines | P3 design review |
| 13 | 12 | Lab 10 · AI-authored PR gauntlet | Guardrail evidence |
| 14 | 12 | P3 integration | **P3 due**, demo |
| 15 | Review | Practical exam and oral | Final |

## Working with AI in this course

- **Use AI for:** first drafts of workflow YAML, Jenkinsfiles, Rollout and AnalysisTemplate manifests; translating a pipeline between engines; explaining a failed job log; drafting release notes. Named tools: GitHub Copilot (chat, code review, coding agent), GitLab Duo, Claude Code, Cursor.
- **Do without AI (drills):** draw a pipeline DAG and its critical path from a YAML file; read a 300-line workflow and list every secret it can reach; design an expand-contract migration on paper; compute DORA metrics by hand from a 30-row event table; the mid-term and practical exam.
- **Verify AI output by:** `actionlint` and `zizmor` on every workflow; `kubectl apply --dry-run=server` for Rollout manifests; a deliberately bad release that must abort; checking every third-party action is SHA-pinned and every job has minimal `permissions:`; diffing two builds for reproducibility.
- **Where AI still fails here (show it):** ask an assistant for "a GitHub Actions workflow that deploys to Kubernetes on PR" and count the issues zizmor reports. Typical findings are unpinned actions, `pull_request_target` with checkout of untrusted code, and broad token permissions. Ask for a canary analysis and check whether it compares against a baseline or against the old fleet. Record every case in a failure log; it is part of the Lab 10 grade.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs 1–10 | 25% |
| Projects P1 / P2 / P3 | 5% / 15% / 25% |
| Mid-term (written, AI off) | 10% |
| Practical exam (3 hours, AI off) + oral | 20% |

**Mastery gate.** You pass when you can, without AI help: (1) take an unfamiliar repository with a pipeline slower than 20 minutes and cut its time-to-green by at least 40% in 3 hours, with no test removed and the cache proven correct; (2) implement a canary that automatically aborts a planted bad release before more than 10% of traffic reaches it; (3) find the three security weaknesses an examiner planted in a workflow file within 20 minutes and explain how each could be exploited and fixed.

## Industry reality

Delivery engineering is a named job (build and release engineer, developer productivity engineer) and a core part of every DevOps, SRE and platform role ([market map](../../../../06_career_and_market_readiness/01_market_map/roles/OPS_devops_sre_platform_engineering.md)). AWS describes automated one-box and wave deployments with bake times and automatic rollback in its Builders' Library. Google Cloud's June 2025 report committed to "enforce all changes to critical binaries to be feature flag protected and disabled by default" and to propagate globally replicated data incrementally. CrowdStrike's July 2024 root-cause analysis lists staged deployment of content as a mitigation. In India, the CERT-In directions of April 2022 require cyber incidents to be reported within 6 hours, so a bad release that leaks data has a regulatory clock as well as a technical one.

**Interview questions from this course**

1. *Our CI takes 45 minutes. What do you do in your first two weeks?* Strong answer: measure first (critical path, queue time, flake rate, cache hits); quick wins (caching, sharding by timing data, affected-only builds, ephemeral autoscaled runners); guards against cache poisoning; a pipeline SLO and a weekly report.
2. *Design deployments for a payment API that must not lose requests.* Strong answer: immutable artifacts promoted by digest; canary against a baseline with SLI-based automatic abort; expand-contract migrations; idempotency during mixed-version windows; feature flags for risky paths; waves with bake time; tested rollback.
3. *A config change took down production globally. How do you stop it happening again?* Strong answer: treat config as a deployment (schema validation, size and range limits, staged propagation, health-gated waves, last-known-good fallback in consumers, fail-open or fail-closed by design); cites Cloudflare 2025 or Google Cloud 2025.
4. *How would you secure a GitHub Actions setup for 200 repositories?* Strong answer: org-level SHA-pinning and allow-list policy, OIDC instead of stored secrets, minimal `permissions:`, no untrusted checkout in `pull_request_target`, ephemeral runners, CODEOWNERS on workflow files, provenance and signing, a scanner (zizmor) in CI.
5. *What are DORA's metrics, and how would you roll them out without harming teams?* Strong answer: names all five and their definitions; collects them from system events, not surveys alone; uses them per service, for improvement and not for ranking teams; pairs them with qualitative data; watches for gaming.

## Resources (free first)

- **Core texts:** Google SRE book, [ch. 8 Release Engineering](https://sre.google/sre-book/release-engineering/) and SRE workbook [Canarying Releases](https://sre.google/workbook/canarying-releases/); AWS Builders' Library, [Automating safe, hands-off deployments](https://aws.amazon.com/builders-library/automating-safe-hands-off-deployments/); [DORA metrics guide](https://dora.dev/guides/dora-metrics/) and [DORA capabilities](https://dora.dev/capabilities/).
- **Engines:** [GitHub Actions docs](https://docs.github.com/en/actions), [merge queue](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue), [Actions Runner Controller](https://docs.github.com/en/actions/concepts/runners/actions-runner-controller); [GitLab CI/CD components](https://docs.gitlab.com/ci/components/); [Jenkins docs](https://www.jenkins.io/doc/); [Tekton](https://github.com/tektoncd/pipeline); [Dagger](https://github.com/dagger/dagger).
- **Builds:** [Docker build cache](https://docs.docker.com/build/cache/), [Bazel remote caching](https://bazel.build/remote/caching), [Gradle build cache](https://docs.gradle.org/current/userguide/build_cache.html), [Reproducible Builds](https://reproducible-builds.org/).
- **Release and progressive delivery:** [Argo Rollouts](https://argo-rollouts.readthedocs.io/en/stable/), [Flagger](https://docs.flagger.app/), [OpenFeature](https://openfeature.dev/), [Spinnaker canary analysis (Kayenta)](https://spinnaker.io/docs/guides/user/canary/), [Pact](https://pact.io/), [Atlas](https://atlasgo.io/), [Flyway](https://flywaydb.org/).
- **Artifacts and supply chain:** [Harbor](https://goharbor.io/), [ORAS](https://oras.land/), [SPDX](https://spdx.dev/), [CycloneDX](https://cyclonedx.org/), [Syft](https://github.com/anchore/syft), [Sigstore](https://www.sigstore.dev/), [SLSA v1.2](https://slsa.dev/spec/v1.2/), [GitHub artifact attestations](https://docs.github.com/en/actions/concepts/security/artifact-attestations), [actionlint](https://github.com/rhysd/actionlint), [zizmor](https://github.com/zizmorcore/zizmor), [harden-runner](https://github.com/step-security/harden-runner).
- **Practice locally:** [kind](https://kind.sigs.k8s.io/) or [k3d](https://k3d.io/) for Rollouts and Kyverno; [act](https://github.com/nektos/act) to run Actions workflows locally; GitHub Actions is free for public repositories.
- **Paid, optional:** Humble and Farley, *Continuous Delivery* (2010), still the clearest statement of the deployment pipeline idea.

## Sources

All checked 12 Oct 2026.
- DORA, [software delivery performance metrics](https://dora.dev/guides/dora-metrics/) (five metrics; move from MTTR to failed deployment recovery time) and [Announcing the 2025 DORA report](https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report) (24 Sep 2025; quotation on control systems).
- CrowdStrike, [Channel File 291 root cause analysis](https://www.crowdstrike.com/wp-content/uploads/2024/08/Channel-File-291-Incident-Root-Cause-Analysis-08.06.2024.pdf) (6 Aug 2024).
- Google Cloud, [incident report, 12 June 2025](https://status.cloud.google.com/incidents/ow5i3PPK96RduMcb1SsW).
- Cloudflare, [outage on 18 November 2025](https://blog.cloudflare.com/18-november-2025-outage/).
- CISA, [tj-actions/changed-files compromise](https://www.cisa.gov/news-events/alerts/2025/03/18/supply-chain-compromise-third-party-tj-actionschanged-files-cve-2025-30066-and-reviewdogaction) (Mar 2025); AWS security bulletin [AWS-2025-015](https://aws.amazon.com/security/security-bulletins/AWS-2025-015/) (Amazon Q Developer extension 1.84); CISA, [xz utils CVE-2024-3094](https://www.cisa.gov/news-events/alerts/2024/03/29/reported-supply-chain-compromise-affecting-xz-utils-data-compression-library-cve-2024-3094).
- GitHub changelog, [policy for blocking and SHA-pinning actions](https://github.blog/changelog/2025-08-15-github-actions-policy-now-supports-blocking-and-sha-pinning-actions/) (15 Aug 2025).
- CNCF project maturity (Harbor graduated 15 Jun 2020; Kyverno graduated 16 Mar 2026; Tekton incubating 13 Mar 2026; OpenFeature incubating) from the [CNCF landscape](https://github.com/cncf/landscape) data file.
- SLSA [specification index](https://slsa.dev/spec/) (v1.2 current).
- Release versions on 12 Oct 2026 from GitHub releases: Argo Rollouts 1.10.0, Flagger 1.45.0.
- [CERT-In Directions, 28 Apr 2022](https://www.cert-in.org.in/PDF/CERT-In_Directions_70B_28.04.2022.pdf) (6-hour reporting).

_Last reviewed: 2026-10_
