# SAR305 · Labs and projects

Labs use GitHub (or a self-hosted Gitea or GitLab), a local `kind` cluster and open-source tools. All organisations below are *illustrative scenarios* unless a source is given. Dynamic scans and fuzzing run only against applications you built and host yourself. Lab 8 is done without AI assistants.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · SSDF and SAMM assessment | Map a described team's process to NIST SSDF practices and score it with a short OWASP SAMM assessment | Gap list with evidence and three priorities | 3 h |
| 2 · Paved-road template | Build a service template with secure defaults: security headers, authentication middleware, structured logging without secrets, dependency pinning, pre-configured pipeline | Template repository and a checklist proving each default | 5 h |
| 3 · Control map | Map controls from commit to runtime for a microservice estate with block, warn and report decisions | Control map diagram, blocking rules, exception workflow | 3 h |
| 4 · Custom SAST rules | Write five Semgrep or CodeQL rules from past incident descriptions; test them on positive and negative cases; measure precision on a sample codebase | Rules, test cases, precision per rule | 5 h |
| 5 · Dependency intake | Configure a registry proxy with an allow-list and a minimum package age; run reachability analysis on a Node.js service | Proxy configuration, a blocked young package, reachability report | 4 h |
| 6 · Provenance, signing and admission | Make one build reproducible; generate SLSA provenance; sign the image keylessly; block unsigned or unverified images at admission | Two matching build digests, provenance, a rejected deployment log | 6 h |
| 7 · SBOM, VEX and ranking | Generate SBOMs at build time and by image scan, diff them; write three VEX statements; re-rank 50 findings with KEV and EPSS | SBOM diff, VEX files, ranked list compared with CVSS order | 4 h |
| 8 · Pipeline hardening (no AI) | Fix a deliberately weak GitHub Actions setup: broad tokens, unpinned actions, secrets exposed to fork pull requests, no environment protection | Before/after workflow files and a test showing a fork pull request cannot reach secrets | 4 h |
| 9 · Guardrails at three layers | Enforce "no public storage buckets" in pull requests (Conftest), at admission or deploy, and at runtime (organisation policy or a detective rule) | Policies and a table of bypass attempts and which layer caught each | 4 h |
| 10 · AI reviewer benchmark | Seed 20 flaws (including two authorization logic flaws and two hallucinated dependencies) in a repository and run two AI reviewers | Recall and precision per tool, every missed flaw classified | 5 h |

## Projects

### P1 · A secure pipeline for your own project (L1, ~6 hours)

**Real-world inspiration:** GitHub's Actions hardening guide recommends least-privilege tokens and pinning actions to full commit SHAs, advice that the 2025 `tj-actions` compromise made concrete ([GitHub](https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions)).

**What to build:** a pipeline for one of your earlier projects with secret scanning and push protection, SAST, dependency scanning, automated updates, an SBOM on every release, actions pinned to SHAs and a read-only default token.

**Acceptance criteria:**
- A test commit containing a fake secret is blocked by push protection or fails the pipeline.
- Every third-party action is pinned to a full commit SHA, enforced by a check that fails on an unpinned action.
- The workflow's default token is read-only; jobs that need write access declare it explicitly.
- Each release has an SBOM attached and the SBOM lists all direct dependencies.
- Feedback on a pull request arrives in under 10 minutes.

**Stretch goals:** OIDC deployment to a cloud account; an OpenSSF Scorecard run with improvements.

**What it proves to an employer:** you secure your own work by default.

### P2 · Verifiable supply chain for a library and a service (L2, ~15 hours)

**Real-world inspiration:** SLSA v1.2 defines build levels for provenance and hardened builds; Sigstore makes keyless signing and transparency logs free to use; the xz-utils backdoor (2024) showed why provenance and release integrity matter ([CISA](https://www.cisa.gov/news-events/alerts/2024/03/29/reported-supply-chain-compromise-affecting-xz-utils-data-compression-library-cve-2024-3094)).

**What to build:** a small library and a service that depends on it, both built on hosted, isolated runners with SLSA provenance, signed with Sigstore, published with SBOM and VEX, verified at Kubernetes admission; plus a compromised-dependency drill.

**Acceptance criteria:**
- Provenance for both artefacts meets SLSA Build Level 3 requirements as written in the specification; your write-up quotes each requirement and the evidence.
- The cluster refuses an image that is unsigned, signed by a different identity, or built from a different repository (three failing deployments shown).
- The library build is reproducible: two independent builds produce the same digest.
- In the drill, you identify every deployment that includes a named "compromised" version from SBOM data in under 15 minutes and roll back.
- OpenSSF Scorecard improves by at least 2 points from your starting score, with the changes listed.

**Stretch goals:** source-track controls (protected branches, two-person review) assessed against SLSA's Source track; VEX consumed by your scanner to suppress a not-affected finding.

**What it proves to an employer:** you can make a release verifiable end to end, a requirement in more and more procurement.

### P3 · DevSecOps reference architecture for a 300-engineer SaaS company (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** Indian SaaS companies selling into Europe face the EU Cyber Resilience Act's reporting duties (from September 2026) and CERT-In's BOM guidelines at home. The company is an *illustrative scenario*: 300 engineers, 120 repositories, three languages, Kubernetes on one cloud, and a new AI coding agent rollout.

**What to build:**
- a SAMM baseline and a 12-month roadmap;
- a control map with blocking rules, noise budgets and an exception workflow;
- a paved-road template and organisation-wide rulesets enforcing it on ten seeded repositories;
- central aggregation of findings with ownership routing (for example DefectDojo);
- supply-chain controls: registry proxy, provenance, signing, admission verification, SBOM and VEX publishing;
- an AI coding agent policy: identity, permissions, sandboxed runners, review rules, logging;
- a metrics dashboard and a CRA and CERT-In evidence pack.

**Acceptance criteria:**
- All ten seeded repositories have the required controls enforced by organisation policy, not by per-repository settings (show that a repository admin cannot disable them).
- Blocking rules have measured precision of at least 80% on a labelled sample of 100 findings; rules below that are moved to warn.
- Median pull-request feedback time is under 10 minutes across the ten repositories.
- A supply-chain drill (named compromised package version) identifies affected services and owners within 30 minutes, with a timeline.
- The AI coding agent cannot push to protected branches, cannot read production secrets and has every action logged; a benign canary instruction placed in an issue does not change its permissions or trigger a merge.
- The dashboard shows at least eight metrics with formulas, including time to remediate known-exploited vulnerabilities and share of builds with verified provenance.
- You defend the architecture in a 20-minute oral; the panel introduces a new regulation or incident and you show which controls and metrics change.

**Stretch goals:** a cost model for tools and staff; an ASPM product evaluation with a vendor-neutral rubric.

**What it proves to an employer:** you can design and run a product security programme for a real-sized company, the core of product security engineering and security engineering lead roles.

## Feeds into

- [OV03 DevSecOps](../../../../04_overlaps/OV03_devsecops/README.md), combining this course with [OPS301](../../../devops_sre_platform_engineering/year_3/OPS301_ci_cd_engineering/README.md) and [SEC302](../../../cybersecurity_defense/year_3/SEC302_security_operations_soc_siem_and_monitoring/README.md).
- [SAR401 Cloud Security Architecture](../../year_4/SAR401_cloud_security_architecture/README.md): guardrails and policy as code across accounts.
- [SAR403 Security Architecture for AI Systems and Agents](../../year_4/SAR403_security_architecture_for_ai_systems_and_agents/README.md): AI supply chain and agent governance.
- The [flagship industry project](../../../../06_career_and_market_readiness/05_industry_projects/SAR_security_architecture.md): its delivery pipeline and supply-chain evidence.
