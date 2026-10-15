# OV03 · DevSecOps

| Composed of | Overlap courses | When | Typical entry majors | Market pages |
|---|---|---|---|---|
| [OPS301](../../03_majors/devops_sre_platform_engineering/year_3/OPS301_ci_cd_engineering/README.md) · [SAR305](../../03_majors/security_architecture/year_3/SAR305_secure_sdlc_and_devsecops_architecture/README.md) · [SEC302](../../03_majors/cybersecurity_defense/year_3/SEC302_security_operations_soc_siem_and_monitoring/README.md) | [OV03A](OV03A_software_supply_chain_security/README.md) · [OV03B](OV03B_policy_as_code_and_secure_ci_cd/README.md) | Year 4 (semesters 7–8) | DevOps/SRE (default overlap), Cybersecurity Defense, Security Architecture, Software Engineering | [OPS](../../06_career_and_market_readiness/01_market_map/roles/OPS_devops_sre_platform_engineering.md) · [SEC](../../06_career_and_market_readiness/01_market_map/roles/SEC_cybersecurity_defense.md) · [SAR](../../06_career_and_market_readiness/01_market_map/roles/SAR_security_architecture.md) |

## The job this overlap maps to

A **DevSecOps engineer** (also titled Product Security Engineer, Software Supply Chain Security Engineer, Security Platform Engineer or Application Security Engineer on a platform team) makes the path from a developer's commit to production trustworthy. Concretely they:

- Run and harden the CI/CD system itself: runners, tokens, secrets, third-party actions.
- Control what code and packages come in: dependency intake, malicious-package defence, update policy.
- Prove what went out: provenance attestations, signatures, SBOMs and VEX.
- Encode rules as policy that runs automatically in pull requests, pipelines, Kubernetes admission and cloud organisation guardrails.
- Respond when the supply chain is attacked: find every affected build and deployment, rotate what leaked, and ship clean.

The job is engineering, not auditing. Its output is pipelines, policies and tooling that thousands of developers use without thinking about it.

## Why this overlap exists

The software supply chain became one of the main ways into organisations, and each attack crossed the line between delivery engineering, security architecture and security operations:

| Year | Incident | What it showed |
|---|---|---|
| 2020 | SolarWinds Orion build compromise | A trusted vendor's build system can ship an implant to thousands of customers ([CISA ED 21-01](https://www.cisa.gov/news-events/directives/ed-21-01-mitigate-solarwinds-orion-code-compromise)) |
| 2024 | xz-utils backdoor (CVE-2024-3094) | Malicious code was in the release tarballs, not in the visible repository history ([NVD](https://nvd.nist.gov/vuln/detail/CVE-2024-3094), [CISA](https://www.cisa.gov/news-events/alerts/2024/03/29/reported-supply-chain-compromise-affecting-xz-utils-data-compression-library-cve-2024-3094)) |
| 2025 | tj-actions/changed-files (CVE-2025-30066) | One compromised GitHub Action exposed CI secrets in many repositories ([CISA](https://www.cisa.gov/news-events/alerts/2025/03/18/supply-chain-compromise-third-party-tj-actionschanged-files-cve-2025-30066-and-reviewdogaction)) |
| 2025 | Shai-Hulud npm worm | Self-spreading malware through stolen npm publishing tokens ([CISA](https://www.cisa.gov/news-events/alerts/2025/09/23/widespread-supply-chain-compromise-impacting-npm-ecosystem)) |
| 2026 | Axios npm compromise | Two releases of a very widely used HTTP client pulled in a malicious dependency that downloaded a remote access trojan ([CISA, Apr 2026](https://www.cisa.gov/news-events/alerts/2026/04/20/supply-chain-compromise-impacts-axios-node-package-manager)) |
| 2026 | Nx Console extension and GitHub repositories | A poisoned VS Code extension led to theft of internal GitHub repositories; CISA flagged campaigns targeting CI/CD pipelines ([CISA, May 2026](https://www.cisa.gov/news-events/alerts/2026/05/28/supply-chain-compromises-impact-nx-console-and-github-repositories)) |

A delivery engineer alone may not see these as security events; a SOC alone cannot fix a pipeline; an architect alone does not run the build fleet. The overlap produces people who can do all three.

**Demand evidence (checked October 2026).**

- In India, application security is the third most-cited security skills need (38%), after AI (52%) and cloud security (43%) ([ISC2 India, Sept 2026](https://www.isc2.org/insights/2026/09/research-india-cybersecurity-workforce-reaches-a-turning-point-skills-ai)).
- "DevOps Engineer" is among the 15 fastest-growing jobs to 2030 in the WEF employer survey ([WEF 2025](https://reports.weforum.org/docs/WEF_Future_of_Jobs_Report_2025.pdf)); US information security analysts are projected to grow 21% from 2025 to 2035 ([BLS](https://www.bls.gov/ooh/computer-and-information-technology/information-security-analysts.htm)).
- Regulation is creating work: the EU Cyber Resilience Act's vulnerability reporting obligations apply from 11 September 2026 ([European Commission](https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act)), and CERT-In published SBOM, AIBOM and related guidelines in July 2025 (summarised in [SAR305](../../03_majors/security_architecture/year_3/SAR305_secure_sdlc_and_devsecops_architecture/README.md)).
- Only 20% of developers who use AI use it for deploying, operating or troubleshooting production systems ([Stack Overflow, Oct 2026](https://stackoverflow.blog/2026/10/06/the-results-of-the-2026-developer-survey-are-here/)): the delivery path remains a human-owned control point.

## Before you start

Prerequisites for both courses (from [catalog.json](../../catalog.json)): **OPS301** CI/CD Engineering, **SAR305** Secure SDLC and DevSecOps Architecture, **SEC302** Security Operations. SAR305 already covers the *architecture*: SSDF, SAMM, the control map, SLSA levels, SBOM and VEX in outline, and the xz lesson. OV03A and OV03B are the *engineering*: you build, break-test and operate these controls.

## How to sequence the courses

| Semester | Composed courses | Overlap course | Notes |
|---|---|---|---|
| 5 (Y3) | **OPS301**, **SEC302** | — | DevOps majors take SEC302 as an elective; security majors take OPS301 |
| 6 (Y3) | **SAR305** | — | Elective for DevOps and security-defence majors |
| 7 (Y4) | — | **OV03A** Software Supply Chain Security | Pairs with [OPS401](../../03_majors/devops_sre_platform_engineering/year_4/OPS401_platform_engineering_and_internal_developer/README.md) for DevOps majors |
| 8 (Y4) | — | **OV03B** Policy as Code and Secure CI/CD | — |
| 9–10 (Y5) | — | Capstone via [THS501](../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md)/[THS502](../../05_shared_years_3_to_5/THS502_thesis_or_capstone_ii/README.md) or [IND401](../../05_shared_years_3_to_5/IND401_industry_co_op_studio/README.md) | [OFF501](../../03_majors/ethical_hacking_offensive_security/year_5/OFF501_frontier_seminar_ai_driven_vulnerability/README.md) or [QAE501](../../03_majors/software_quality_test_engineering/year_5/QAE501_frontier_seminar_property_based_testing_fuzzing/README.md) as research follow-ons |

## The two overlap courses

| Course | Semester | What you can do at the end |
|---|---|---|
| [OV03A · Software Supply Chain Security](OV03A_software_supply_chain_security/README.md) | 7 | Run dependency intake that stops malicious packages, produce SLSA Build Level 3 provenance and keyless signatures, generate complete SBOMs with VEX, verify all of it at deploy time, and respond to a compromised dependency within hours |
| [OV03B · Policy as Code and Secure CI/CD](OV03B_policy_as_code_and_secure_ci_cd/README.md) | 8 | Write and test policies in Rego, CEL and Kyverno across pull requests, pipelines, admission and cloud guardrails; harden GitHub Actions or GitLab CI against the OWASP CI/CD Top 10; and run compliance evidence as code |

## Capstone: a secure software factory

**Brief.** Build a "software factory" for an organisation with at least six repositories (three services, a shared library, an infrastructure repository, a GitHub Actions or GitLab CI template repository) and deploy to a Kubernetes cluster you own. Every artefact that reaches the cluster must be traceable to reviewed source, built on hardened infrastructure, scanned, signed and admitted by policy. Then defend it in a supply-chain incident drill.

**Acceptance criteria (all measurable).**

1. **Provenance.** 100% of container images and packages produced by the factory carry SLSA Build Level 3 provenance and a keyless Sigstore signature; `slsa-verifier` or `cosign verify-attestation` succeeds for each, bound to the expected repository and workflow identity.
2. **SBOM and VEX.** Every image has an SBOM generated at build time (SPDX or CycloneDX) that lists ≥ 95% of the packages found by an independent image scan; VEX statements suppress at least five non-exploitable findings with written justifications.
3. **Intake.** A dependency firewall or proxy blocks packages younger than a configured age and known-malicious packages from the OSV malicious-packages feed; a test shows a planted malicious package is blocked.
4. **CI hardening.** OpenSSF Scorecard ≥ 8.0 on every repository; zizmor reports no high-severity findings; every third-party action is pinned to a full commit SHA; default `GITHUB_TOKEN` permissions are read-only.
5. **Policy.** At least 20 policies across four enforcement points (pull request, pipeline, admission, cloud organisation), each with passing and failing tests in CI; exceptions are records with owners and expiry dates.
6. **Admission.** The cluster rejects an unsigned image, an image signed by the wrong workflow, and an image whose SBOM shows a CISA KEV vulnerability without a VEX statement.
7. **Incident drill.** In an announced drill, the instructor reveals a "compromised" version of an internal library. Within 4 hours you list every affected build, image and running workload (using SBOMs or a GUAC graph), rotate exposed CI credentials, rebuild and redeploy clean versions, and write an incident report.
8. **Developer experience.** Median pipeline time increases by no more than 20% compared with the unsecured baseline, and the change is measured, not estimated.

## Roles it leads to

| Role | What people in it do | Entry route |
|---|---|---|
| DevSecOps Engineer | Hardens pipelines, runs scanners and policy gates, supports developers | Direct entry; DevOps majors with this overlap are strong candidates |
| Software Supply Chain Security Engineer | Provenance, signing, SBOM programmes, dependency intake, ecosystem response | Often from DevSecOps after one or two years |
| Product / Application Security Engineer (platform track) | Secure defaults, paved roads, security tooling as a product | Direct entry with strong coding evidence |
| Security Platform Engineer | Builds and runs policy engines, secret management and security infrastructure | From platform or SRE roles |

Interview loops typically include a pipeline threat-modelling exercise, a "review this workflow file" task, a policy-writing exercise and an incident scenario; see the [OPS](../../06_career_and_market_readiness/01_market_map/roles/OPS_devops_sre_platform_engineering.md) and [SEC](../../06_career_and_market_readiness/01_market_map/roles/SEC_cybersecurity_defense.md) market pages.

## Sources

All checked 12 Oct 2026.

- CISA Emergency Directive 21-01 (SolarWinds Orion) — https://www.cisa.gov/news-events/directives/ed-21-01-mitigate-solarwinds-orion-code-compromise
- NVD, CVE-2024-3094 (published 29 Mar 2024) — https://nvd.nist.gov/vuln/detail/CVE-2024-3094 ; CISA alert — https://www.cisa.gov/news-events/alerts/2024/03/29/reported-supply-chain-compromise-affecting-xz-utils-data-compression-library-cve-2024-3094
- CISA alerts: tj-actions (18 Mar 2025) — https://www.cisa.gov/news-events/alerts/2025/03/18/supply-chain-compromise-third-party-tj-actionschanged-files-cve-2025-30066-and-reviewdogaction ; npm (23 Sep 2025) — https://www.cisa.gov/news-events/alerts/2025/09/23/widespread-supply-chain-compromise-impacting-npm-ecosystem ; Axios (20 Apr 2026) — https://www.cisa.gov/news-events/alerts/2026/04/20/supply-chain-compromise-impacts-axios-node-package-manager ; Nx Console (28 May 2026) — https://www.cisa.gov/news-events/alerts/2026/05/28/supply-chain-compromises-impact-nx-console-and-github-repositories
- ISC2, India cybersecurity workforce study (24 Sep 2026) — https://www.isc2.org/insights/2026/09/research-india-cybersecurity-workforce-reaches-a-turning-point-skills-ai
- World Economic Forum, Future of Jobs Report 2025 — https://reports.weforum.org/docs/WEF_Future_of_Jobs_Report_2025.pdf ; US BLS, Information security analysts — https://www.bls.gov/ooh/computer-and-information-technology/information-security-analysts.htm
- European Commission, Cyber Resilience Act — https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act
- Stack Overflow blog, 2026 Developer Survey results (6 Oct 2026) — https://stackoverflow.blog/2026/10/06/the-results-of-the-2026-developer-survey-are-here/

_Last reviewed: 2026-10_
