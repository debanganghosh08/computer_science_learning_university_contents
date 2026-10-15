# OV03A · Labs and projects

Labs use a GitHub organisation (or GitLab group) you create for the course, a private registry, and a local or sandbox Kubernetes cluster. Malicious-package examples come only from published datasets and are inspected as data, never installed outside a disposable, network-isolated VM. Every lab ships code, verification output and a short write-up.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Supply chain map and Scorecard | Map your course organisation's supply chain; run OpenSSF Scorecard on your repos and 20 dependencies; inventory every publishing credential | Map, Scorecard table, credential inventory | 4 h |
| 2 · Tarball-to-tag verification | For two benign open-source projects, compare release tarballs with tagged source; script the comparison | Diff reports with every difference explained, reusable script | 4 h |
| 3 · Intake and cooldowns | Set up a registry proxy with a release-age cooldown and an intake rubric; run Renovate for a month of simulated updates | Configuration, count of updates delayed or blocked, rubric decisions | 5 h |
| 4 · Trusted publishing and script-free installs | Publish a test package to npm or TestPyPI with trusted publishing; make CI installs lockfile-only with scripts disabled | Publish logs showing no long-lived token, provenance on the package page, CI breakage notes | 4 h |
| 5 · Provenance on isolated builders | Restructure a workflow so build and signing are isolated; generate SLSA provenance; make one artefact reproducible on two builders | Gap assessment against Build L3, provenance files, reproducibility proof (matching digests) | 7 h |
| 6 · Keyless signing and verification | Sign images and blobs with cosign keyless; write verification that accepts only your release workflow identity | Rekor entry IDs, verification commands, a failed verification for a fork-built image | 4 h |
| 7 · Deploy-time verification and GUAC | Enforce signature and provenance at admission; load SBOMs and attestations into GUAC; query a dependency's blast radius | Admission test results, GUAC queries and outputs | 5 h |
| 8 · SBOM completeness and VEX | Generate build-time SBOMs (SPDX and CycloneDX); measure completeness against an independent scan; publish OpenVEX for five findings | Completeness metric per image, VEX documents with evidence | 5 h |
| 9 · Minimal images and rebuilds | Rebuild three images on minimal bases; automate weekly rebuilds with digest-pinning bots; rank 50 findings by exploitability | Before/after table (size, packages, findings), ranking with reasons | 4 h |
| 10 · Source track and secrets | Apply rulesets and signed commits; enable push protection; plant a test secret and measure block and rotation time | Ruleset export, measured times, rotation playbook | 4 h |

## Projects

### P1 · Dependency intake service (L1, ~6 hours)

**Real-world inspiration.** The npm incidents of 2025–26 (Shai-Hulud, Axios) were short-lived malicious releases; organisations with release-age cooldowns and intake checks avoided pulling them.

**What to build.** A small service or CI action that evaluates a dependency change (lockfile diff) and returns allow, warn or block, with reasons: release age, OpenSSF Scorecard score, OSV vulnerabilities, presence in the OSV malicious-packages data, install scripts, and licence.

**Acceptance criteria**
- Runs on every pull request that changes a lockfile and posts a summary comment in under 60 seconds for 50 changed packages.
- Blocks a test change that introduces a package listed in the malicious-packages dataset (inspected as data only) and a package younger than the configured cooldown.
- Every decision is explained in one line per package; overrides require a named approver and expire.
- False-block rate measured over 100 real historical dependency updates from an open-source project: ≤ 5%.

**Stretch goals.** Reachability for the ecosystem you use; a weekly report of overrides by team.

**What it proves to an employer.** You can turn supply-chain risk signals into a fast, explainable developer-facing control.

### P2 · SLSA Level 3 release pipeline (L2, ~15 hours)

**Real-world inspiration.** GitHub artifact attestations, PyPI attestations and npm provenance let consumers check where an artefact was built; most organisations still ship artefacts that nobody can verify.

**What to build.** A release pipeline for one service and one library: hosted isolated builds, SLSA provenance, keyless signatures, build-time SBOMs, attestations attached in the registry, and a consumer-side verification script and admission policy.

**Acceptance criteria**
- `slsa-verifier` (or `gh attestation verify`) succeeds for every release artefact with the expected source repository, ref and builder; it fails for an artefact built from a fork and for a tampered digest.
- Build steps cannot read the signing identity's credentials (demonstrated by a test step that tries and fails).
- The library build is reproducible: two independent builds produce the same digest.
- SBOM completeness ≥ 95% against an independent image scan.
- The cluster admits only artefacts that pass verification; tests show three rejection cases.
- Pipeline time increase over the baseline is measured and reported.

**Stretch goals.** Publish VEX alongside releases; verify provenance of your top five upstream dependencies where available.

**What it proves to an employer.** You can implement the producer side of supply-chain security to a recognised standard and prove it with verification.

### P3 · Supply-chain incident response kit (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** After the tj-actions, Shai-Hulud and Axios compromises, CISA's guidance asked organisations to find every affected pipeline and machine, rotate secrets and rebuild. Teams with SBOMs and dependency graphs did this in hours; others took weeks. The exercise scenario is illustrative.

**What to build.** A kit and a drill:
1. A pipeline that publishes SBOMs and attestations for every artefact in a six-repository organisation into GUAC (or your own graph).
2. A "what is affected?" command that takes a package and version range (or a compromised GitHub Action reference) and returns affected repositories, builds, images, clusters and the CI secrets those builds could access.
3. Playbooks for compromised package, compromised CI action and compromised maintainer token.
4. A timed drill run by the instructor.

**Acceptance criteria**
- The affected-artefact query returns complete results (checked against a hidden answer key) for three planted scenarios, each in under 5 minutes.
- In the drill, the team freezes affected pipelines, rotates every exposed credential, rebuilds and redeploys clean artefacts, and verifies them at admission within 4 hours.
- Secret exposure is mapped: for the compromised action, the kit lists every secret available to workflows that used it during the exposure window.
- The incident report includes a timeline, scope, root cause, customer communication draft and at least five dated improvements.

**Stretch goals.** Automatic pull requests that pin or downgrade the compromised dependency across all repositories; a dashboard of exposure-window metrics.

**What it proves to an employer.** You can lead the response to the kind of supply-chain incident that now happens several times a year, with evidence instead of guesswork.

## Feeds into

- [OV03B Policy as Code and Secure CI/CD](../OV03B_policy_as_code_and_secure_ci_cd/README.md): provenance, SBOM and signature checks become policies at every enforcement point.
- The [OV03 capstone](../README.md): P2 and P3 are its provenance and incident-drill components.
- [OV01B Kubernetes and Container Security](../../OV01_cloud_security/OV01B_kubernetes_and_container_security/README.md): the admission side of verification.
- [OFF501 Frontier Seminar: AI-Driven Vulnerability Discovery and Defense](../../../03_majors/ethical_hacking_offensive_security/year_5/OFF501_frontier_seminar_ai_driven_vulnerability/README.md) and [THS501](../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md): SBOM completeness and ecosystem-scale measurement are research topics.
