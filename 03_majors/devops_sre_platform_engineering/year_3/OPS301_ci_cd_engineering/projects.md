# OPS301 · Labs and projects

Everything runs on a laptop with Docker and [kind](https://kind.sigs.k8s.io/) or [k3d](https://k3d.io/), plus free GitHub Actions minutes on public repositories. Use a public demo repository: never put real secrets anywhere in this course. Labs 1, 6 and 8 are done without AI assistance. Each lab report states the numbers it was asked for, so that the result can be checked.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Pipeline teardown | Instrument an existing open-source project's pipeline: time-to-green p50/p95, queue time, critical path, flake rate over 30 runs | DAG drawing, metrics table, three ranked improvement ideas | 4 h |
| 2 · Three engines | Implement the same lint → test → build → scan → publish flow in GitHub Actions, GitLab CI and Jenkins (in a container) | Three pipeline files, a comparison of run time and lines of config, migration notes | 6 h |
| 3 · Cache clinic | Add BuildKit cache mounts and a registry cache, then a Bazel or Gradle remote cache; prove correctness by rebuilding with the cache disabled and diffing outputs | Hit-rate graph, before/after timings, artifact diff | 5 h |
| 4 · Flake hunter | Detect flaky tests by repeated runs, quarantine them with owner and expiry date, fix three planted flakes | Detection script, quarantine list, root-cause notes | 4 h |
| 5 · Promote by digest | Build once, sign nothing yet, promote one image digest through three namespaces with Harbor tag-immutability rules | Promotion log proving the same digest everywhere | 3 h |
| 6 · Zero-downtime migration | Rename a column with expand-contract while k6 sends 200 requests/s | Migration scripts, k6 summary with 0 failed requests | 5 h |
| 7 · Canary with analysis | Argo Rollouts canary on kind with an `AnalysisTemplate` on error rate and p95 latency; then push a configuration file through three waves with a size and schema check | Manifests, abort recording, wave log showing the bad file stopped at wave 1 | 8 h |
| 8 · Sign and verify | Generate an SBOM with Syft, sign with cosign (keyless), attach provenance, block unsigned images with Kyverno | Policy, admission denial output, verification transcript | 4 h |
| 9 · DORA dashboard | Compute the five DORA metrics from webhook events of your own repositories over 4 weeks | Event schema, queries, dashboard export, a note on how each metric could be gamed | 5 h |
| 10 · AI-authored PR gauntlet | Let a coding agent with a scoped identity open 10 PRs (including workflow changes); show which guardrails caught what | Ruleset config, agent token scopes, table of 10 PRs and outcomes, AI failure log | 5 h |

## Projects

### P1 · Pipeline speed-run (L1, ~6 hours)

**Real-world inspiration:** DORA lists working in small batches and fast feedback among the capabilities that make AI-accelerated delivery stable ([DORA capabilities](https://dora.dev/capabilities/)). Remote caching in [Bazel](https://bazel.build/remote/caching) and [Gradle](https://docs.gradle.org/current/userguide/build_cache.html) exists because waiting for builds is the main tax on small batches.

**What to build:** take a medium-size open-source repository (at least 3 build targets and 300 tests) whose CI takes at least 10 minutes. Fork it and make its pipeline fast without weakening it.

**Acceptance criteria:**
- **Speed:** p50 time-to-green falls by at least 50% over 20 runs (before and after measured the same way).
- **No-op change:** a README-only change finishes in under 2 minutes, and the build cache hit rate is at least 80% on a one-file code change.
- **Same safety:** the number of tests run for a change that touches shared code is unchanged, and a cache-disabled rebuild produces identical artifacts (checksum diff).
- **Security:** every third-party action is pinned to a full SHA, and each job declares minimal `permissions:` (zizmor reports no high findings).

**Stretch goals:** test sharding balanced by timing data; an "affected targets only" mode with a nightly full run to catch misses.

**What it proves to an employer:** you can make developers faster with measurements and without cutting corners, which is the first task many platform and DevOps engineers get.

### P2 · Progressive delivery with feature flags and safe migrations (L2, ~15 hours)

**Real-world inspiration:** AWS describes one-box and wave deployments with bake times and automatic rollback ([Builders' Library](https://aws.amazon.com/builders-library/automating-safe-hands-off-deployments/)). After its June 2025 outage, Google Cloud committed to feature-flag protect all critical binary changes, disabled by default ([incident report](https://status.cloud.google.com/incidents/ow5i3PPK96RduMcb1SsW)).

**What to build:** a three-service app on kind with:
- Argo Rollouts (or Flagger) canaries judged by Prometheus SLI queries against a baseline;
- an OpenFeature-compatible flag provider (flagd) for a risky code path;
- one expand-contract schema migration;
- a pipeline that builds once, promotes by digest and opens the deployment change.

**Acceptance criteria:**
- **Good release:** promoted to 100% with no human action in under 15 minutes.
- **Bad release:** a release with a 5% error injection is aborted automatically before more than 10% of traffic reaches it, and user-facing errors during the event stay under 1% (k6 evidence).
- **Migration:** zero failed requests at 200 requests/s across the full expand, migrate and contract sequence.
- **Flags:** the risky path can be turned off in under 30 seconds without a deploy, and every flag has an owner and an expiry date.
- **Evidence:** a recording or log of both the good and the bad release, and a one-page design note explaining baseline selection and bake time.

**Stretch goals:** a Mann-Whitney judge that replaces fixed thresholds; header-based routing so testers can reach the canary directly.

**What it proves to an employer:** you can ship continuously without gambling, which is the core promise of a DevOps or release engineer.

### P3 · A release system for a high-stakes service (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** recent large outages came from fast, wide pushes of configuration or data: Cloudflare's doubled feature file ([Nov 2025](https://blog.cloudflare.com/18-november-2025-outage/)), Google Cloud's globally replicated policy ([Jun 2025](https://status.cloud.google.com/incidents/ow5i3PPK96RduMcb1SsW)) and CrowdStrike's content update ([RCA, Aug 2024](https://www.crowdstrike.com/wp-content/uploads/2024/08/Channel-File-291-Incident-Root-Cause-Analysis-08.06.2024.pdf)). For an Indian payment or brokerage service, a bad release is also a compliance event: CERT-In requires incident reports within 6 hours ([Directions, 2022](https://www.cert-in.org.in/PDF/CERT-In_Directions_70B_28.04.2022.pdf)). The service you build is an *illustrative scenario*, not a model of any real company.

**What to build:** a release system for a payment-style API running in three "cells" (three kind clusters or three namespaces with separate ingress):
- code and configuration both flow through the same staged waves: cell 1, bake, cell 2, bake, cell 3;
- configuration files are validated by schema and size limits, and consumers fall back to last-known-good;
- signed images with SLSA provenance, verified at admission in every cell;
- a DORA five-metric dashboard fed by real events;
- a release runbook and a freeze/hotfix policy;
- a written threat model for the pipeline itself.

**Acceptance criteria:**
- **Lead time:** a normal change goes from merge to 100% of cells in under 30 minutes, with bake times included.
- **Containment:** a planted invalid config (double size) and a planted bad binary each stop in cell 1, affecting at most one cell, with automatic halt.
- **Recovery:** in three drills, failed deployment recovery time is under 10 minutes each (timestamps from your event log).
- **Supply chain:** 100% of unsigned or unprovenanced images are rejected at admission in a test of 10 attempts.
- **Metrics:** the dashboard shows all five DORA metrics for at least 2 weeks of activity, including deployment rework rate.
- **Review:** a classmate follows your runbook to perform a hotfix and a rollback without your help.

**Stretch goals:** automatic rollout pause when the error budget of the service (from [OPS304](../OPS304_site_reliability_engineering_slos_error_budgets/README.md)) is burning faster than 2×; a merge queue under a simulated 5× PR rate from an agent.

**What it proves to an employer:** you understand that delivery systems cause and prevent the biggest outages, and you can build one that contains its own failures. This is senior release-engineering and platform work.

## Feeds into

- [OPS305 Configuration Management and GitOps](../OPS305_configuration_management_and_gitops/README.md): your CI hands artifacts to GitOps reconciliation.
- [OPS401 Platform Engineering](../../year_4/OPS401_platform_engineering_and_internal_developer/README.md): P2 and P3 become the delivery part of a golden path.
- Overlap [OV03 DevSecOps](../../../../04_overlaps/OV03_devsecops/README.md): [OV03A Software Supply Chain Security](../../../../04_overlaps/OV03_devsecops/OV03A_software_supply_chain_security/README.md) and [OV03B Policy as Code and Secure CI/CD](../../../../04_overlaps/OV03_devsecops/OV03B_policy_as_code_and_secure_ci_cd/README.md) go deep on Chapter 9.
- The [flagship industry project](../../../../06_career_and_market_readiness/05_industry_projects/OPS_devops_sre_platform_engineering.md) and [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) capstones reuse P3.
