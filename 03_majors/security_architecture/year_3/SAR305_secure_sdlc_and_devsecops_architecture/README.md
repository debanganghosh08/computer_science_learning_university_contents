# SAR305 · Secure SDLC and DevSecOps Architecture

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 6 | 4 (≈ 120 hours) | L2 → L4 | [CS213](../../../../02_year_2_core_computer_science/semester_4/CS213_security_foundations/README.md), [CS212](../../../../02_year_2_core_computer_science/semester_4/CS212_distributed_systems_i/README.md) | [OV03 DevSecOps](../../../../04_overlaps/OV03_devsecops/README.md), [SAR401](../../year_4/SAR401_cloud_security_architecture/README.md), [SAR403](../../year_4/SAR403_security_architecture_for_ai_systems_and_agents/README.md) |

Part of the [Security Architecture major](../../README.md). Taken alongside [SAR304](../SAR304_applied_cryptography_and_pki_for_architects/README.md). CS213 Chapter 9 introduced SBOMs, pinning and signing. [OPS301 CI/CD Engineering](../../../devops_sre_platform_engineering/year_3/OPS301_ci_cd_engineering/README.md) teaches how to build pipelines. This course designs the security system around software delivery for a whole organisation: which controls go where, how they are enforced without stopping developers, how the supply chain is verified, and how you prove it works.

## Why this course matters now

Attackers now target the way software is built, not only the software. The xz-utils backdoor (CVE-2024-3094, March 2024) was planted through a maintainer's trusted position; the compromised `tj-actions/changed-files` GitHub Action (March 2025) leaked CI secrets; the self-spreading "Shai-Hulud" npm worm compromised more than 500 packages in September 2025 and stole developer and cloud credentials ([CISA](https://www.cisa.gov/news-events/alerts/2025/09/23/widespread-supply-chain-compromise-impacting-npm-ecosystem)); CISA issued further alerts on compromises affecting the Axios npm package (April 2026) and Nx Console (May 2026). OWASP's Top 10:2025 made Software Supply Chain Failures a category of its own. Regulation followed: the EU Cyber Resilience Act's vulnerability-reporting obligations for manufacturers apply from 11 September 2026, and CERT-In's 2025 guidelines extend SBOM practice to cryptographic, AI and hardware bills of materials. AI sits on both sides. Models chose insecure implementations in 45% of security-relevant tasks in Veracode's 2025 study, while AWS Security Agent added full-repository code review in May 2026 and GitHub's Copilot Autofix proposes fixes for code-scanning alerts. The architect's job is to decide where each control sits, what blocks and what only warns, and how to keep developers on a paved road that is secure by default.

## Learning outcomes

By the end you can:

1. **Compare** secure SDLC models (Microsoft SDL, NIST SSDF SP 800-218 and 800-218A, OWASP SAMM, CISA Secure by Design) and **design** a programme sized to an organisation.
2. **Map** security controls onto every stage from commit to runtime, with feedback latency, blocking rules and false-positive budgets.
3. **Architect** static analysis, dependency management and secret scanning so findings reach the right owner with low noise.
4. **Implement** build integrity to SLSA v1.2 Build Level 3, signing with Sigstore and verification at deploy time.
5. **Produce** and **consume** SBOMs and VEX documents, and **design** vulnerability management driven by exploitability (CISA KEV, EPSS) rather than raw severity.
6. **Harden** a CI/CD platform against poisoned pipelines, over-privileged tokens and compromised third-party actions.
7. **Define** security and delivery metrics, **assess** a programme with OWASP SAMM, and **present** a roadmap.
8. **Govern** AI coding agents and AI review tools in the SDLC, and **demonstrate** their failure modes with evidence.

## Chapters and lessons

### Chapter 1 · Secure SDLC models (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 The models | Microsoft SDL; NIST SSDF (SP 800-218): prepare the organisation, protect the software, produce well-secured software, respond to vulnerabilities; SP 800-218A for AI model development | Map one team's current process to SSDF practices and mark gaps |
| 1.2 Maturity | OWASP SAMM v2 business functions and maturity levels; BSIMM as descriptive data about what firms do | Run a short SAMM self-assessment on an illustrative startup |
| 1.3 Secure by Design | CISA's Secure by Design principles and the 2024 pledge: ownership of customer security outcomes, transparency, leadership | Score a vendor's public commitments against the pledge goals |
| 1.4 Sizing the programme | Risk tiers for applications; what a 20-person startup, a 500-engineer product firm and a bank each need | Write programme scopes for the three |

**Check your understanding:** (1) What does SSDF describe that SAMM does not, and vice versa? (2) Why is BSIMM not a target? (3) What does "secure by default" mean for a vendor's configuration choices?

### Chapter 2 · Security in requirements and design (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Application risk tiering | Data class, exposure, business criticality; what each tier must do | Tier 20 applications in a provided portfolio |
| 2.2 Champions and triggers | Security champions, threat-model triggers (from SAR302), design review routing (from SAR301) | Design a champions programme with time allocation and incentives |
| 2.3 Paved roads | Golden-path templates, secure frameworks, safe-by-construction APIs; Google's account of memory-safe code reducing Android memory-safety bugs from 76% (2019) to 24% (2024) | Build a service template with secure defaults (headers, auth middleware, logging) |
| 2.4 Requirements in the backlog | ASVS-based acceptance criteria as user-story templates | Write security acceptance criteria for five stories |

**Check your understanding:** (1) Why do paved roads beat policy documents? (2) What should trigger a full design review rather than a template? (3) How do you keep champions from burning out?

### Chapter 3 · The control map: what goes where (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Stages | Pre-commit, pull request, build, artefact registry, deploy admission, runtime; what each stage can see | Draw a control map for a microservice estate |
| 3.2 Block, warn or report | Blocking criteria, break-glass for urgent fixes, exception expiry | Write blocking rules for six control types |
| 3.3 Feedback latency | Why a finding that arrives in 30 seconds gets fixed and one that arrives in 30 days does not | Measure feedback time for three tools in a sample pipeline |
| 3.4 Noise budgets | False-positive rates, deduplication, ownership routing, application security posture management (ASPM) | Set a noise budget and a policy for tools that exceed it |

**Check your understanding:** (1) Which controls must block, and why only those? (2) What is lost when every finding goes to the security team instead of the code owner? (3) Why do unexpiring exceptions destroy programmes?

### Chapter 4 · Static analysis at scale (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 How SAST works | Pattern rules (Semgrep) vs semantic queries with data-flow and taint tracking (CodeQL); sources, sinks, sanitisers | Write a taint rule for an unsafe query builder in your framework |
| 4.2 Custom rules | Encoding your organisation's bugs and banned APIs; testing rules | Write and test five custom rules from past incidents |
| 4.3 Triage governance | Suppressions with reasons and expiry, auditing suppressions, measuring precision | Triage 40 findings and compute precision per rule |
| 4.4 Memory safety strategy | Memory-safe languages for new code, sanitisers and fuzzing for old code (from CS213) | Write a memory-safety roadmap for a C++ codebase |
| 4.5 AI-assisted fixes | Copilot Autofix and similar tools; reviewing fixes for correctness and regression | Evaluate ten AI fixes with tests |

**Check your understanding:** (1) Why does a taint rule need sanitiser definitions? (2) What makes a suppression trustworthy? (3) Why are AI fixes that compile not yet fixes?

### Chapter 5 · Dependencies and open source (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 The dependency graph | Direct vs transitive, lockfiles, reachability analysis, OSV data | Build the graph for a Node.js service and find unreachable vulnerable code |
| 5.2 Intake controls | Registry proxies, allow-lists, minimum package age, OpenSSF Scorecard, the OpenSSF S2C2F framework | Design an intake policy for npm and PyPI |
| 5.3 Malicious packages | Typosquatting, hallucinated package names ("slopsquatting"), compromised maintainers; Shai-Hulud (2025) and Axios (2026) as cases | Write a response playbook for "a package we use was compromised" |
| 5.4 Updates | Dependabot and Renovate, grouped updates, test gates, update SLAs | Configure automated updates with auto-merge only for passing patch releases |

**Check your understanding:** (1) Why does pinning reduce but not remove supply-chain risk? (2) What does a minimum package age protect against? (3) What does a reachability claim need before you trust it?

### Chapter 6 · Build integrity, provenance and signing (weeks 6–7)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 SLSA v1.2 | Build track levels (provenance exists, hosted build, hardened build) and the new Source track; threats each level addresses | Assess a pipeline against Build L1–L3 |
| 6.2 Hardened builds | Ephemeral, isolated runners; hermetic and reproducible builds; separating build from signing | Make one build reproducible and prove it with two builds |
| 6.3 Provenance and attestations | in-toto statements, SLSA provenance, npm provenance, generator choices | Generate and verify provenance for a release |
| 6.4 Signing and verification | Sigstore cosign keyless signing, Rekor transparency log, verification policy at deploy (Kyverno or Sigstore policy-controller) | Block an unsigned image at Kubernetes admission |
| 6.5 The xz lesson | Maintainer trust, release tarballs that differ from the repository, what provenance can and cannot show | Write what each SLSA level would and would not have caught in the xz case |

**Check your understanding:** (1) What does provenance prove about the source, and what does it not? (2) Why separate the signing identity from the build job? (3) Would SLSA Build L3 have stopped the xz backdoor? Explain.

### Chapter 7 · SBOM, VEX and vulnerability management (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 SBOM formats and generation | CycloneDX and SPDX; generating at build time vs scanning images; completeness checks | Generate SBOMs both ways and diff them |
| 7.2 VEX | Stating "not affected" with justification (CSAF VEX, CycloneDX VEX) | Write VEX statements for three CVEs |
| 7.3 Prioritisation | CVSS vs exploitation evidence (CISA KEV) vs probability (FIRST EPSS); asset criticality | Re-rank 50 findings with KEV and EPSS and compare with CVSS-only order |
| 7.4 Regulation and customers | EU Cyber Resilience Act (reporting from 11 September 2026), CERT-In SBOM guidelines, customer SBOM requests | Build the SBOM and disclosure process for a product sold in India and the EU |

**Check your understanding:** (1) Why can two SBOMs of the same image differ? (2) What makes a VEX statement credible? (3) Why does CVSS-only prioritisation waste effort?

### Chapter 8 · CI/CD platform security (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 The pipeline as production | OWASP Top 10 CI/CD Security Risks: poisoned pipeline execution, insufficient flow control, credential hygiene, third-party services | Score a pipeline against the list |
| 8.2 Tokens and identity | Least-privilege job tokens, OIDC federation to clouds, environment protection rules | Cut a workflow's token permissions to the minimum and prove it still works |
| 8.3 Third-party actions | Pinning to full commit SHAs, allow-lists, forking critical actions; the tj-actions case | Pin all actions in a repository and add a check that enforces pinning |
| 8.4 Flow control | Protected branches, required reviews, two-person rule for production, signed commits | Configure a flow where no single person can ship to production |

**Check your understanding:** (1) Why does a pull request from a fork need different pipeline privileges? (2) Why does pinning to a tag not stop a compromised action? (3) Who should be able to change pipeline definitions?

### Chapter 9 · Infrastructure as code and policy guardrails (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 IaC scanning | Checkov, Trivy misconfiguration scanning; custom policies | Write five custom policies for your cloud standards |
| 9.2 Policy as code across stages | Conftest/OPA in pull requests, Kyverno at admission, cloud organisation policies at runtime | Enforce one rule at all three layers and compare bypass paths |
| 9.3 Guardrails over gates | Preventing whole classes of mistakes vs reviewing each change | Replace one manual review step with a guardrail |
| 9.4 Exceptions and drift | Exception workflow with expiry; drift detection between code and cloud | Detect and report a manual console change |

**Check your understanding:** (1) Why enforce the same rule at several layers? (2) When is a gate better than a guardrail? (3) What does drift tell you about your process?

### Chapter 10 · Dynamic testing, disclosure and runtime feedback (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 DAST and API testing | OWASP ZAP baseline and API scans in pipelines against your own staging app; authenticated scans | Add a ZAP scan to a pipeline for your own demo app |
| 10.2 Fuzzing in CI | Coverage-guided fuzzing for parsers; OSS-Fuzz as a model | Add a short fuzz job that runs on every pull request |
| 10.3 Disclosure | `security.txt` (RFC 9116), vulnerability disclosure policies, bug bounty scope (in partnership with [OFF305](../../../ethical_hacking_offensive_security/year_3/OFF305_reporting_remediation_and_bug_bounty_practice/README.md)) | Write a disclosure policy and `security.txt` for a product |
| 10.4 Closing the loop | Mapping runtime findings and incidents back to the stage that should have caught them | Run a root-cause review: which SDLC control failed for three public incidents? |

**Check your understanding:** (1) What can DAST find that SAST cannot? (2) Why must a disclosure policy promise not to pursue good-faith researchers? (3) How does an incident change the control map?

### Chapter 11 · Metrics and programme design (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 What to measure | Time to remediate by exploitability, share of builds with provenance, share of repositories with secret scanning and push protection, escaped defects, rule precision, developer time spent | Define ten metrics with formulas and sources |
| 11.2 Delivery and security together | DORA delivery metrics alongside security metrics; avoiding metrics that punish teams | Build a dashboard design that shows both |
| 11.3 Assessment and roadmap | SAMM assessment, gap analysis, tool consolidation, budget | Write a 12-month roadmap for an illustrative 300-engineer firm |
| 11.4 Communicating the programme | Reporting to engineering leaders and the board; team scorecards without blame; showing bug classes eliminated rather than bugs counted | Write a quarterly programme update for engineering leadership |

**Check your understanding:** (1) Why is "number of vulnerabilities found" a bad metric? (2) How can security metrics harm delivery? (3) What would show that the paved road is used?

### Chapter 12 · AI in the software lifecycle (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 AI coding agents as contributors | Agents that open pull requests: permissions, sandboxed runners, review as untrusted contributions, prompt injection through issues and repository content | Design permissions and review rules for a coding agent with write access to branches only |
| 12.2 AI review and scanning | AWS Security Agent repository reviews, Copilot Autofix, Claude Code's security review, Semgrep's AI triage; where they fit in the control map | Run two AI reviewers on a seeded repository and score them |
| 12.3 Failure modes | Hallucinated packages, insecure defaults, plausible but wrong fixes, missed authorization logic | Build a seeded benchmark of 20 flaws and measure recall per tool |
| 12.4 AI models as artefacts | SP 800-218A practices; model files, datasets and prompts in the SBOM (AI BOM); model signing | Add a model and its dataset to an AIBOM and sign the model |

**Check your understanding:** (1) Why should a coding agent's pull request get the same review as a stranger's? (2) Which flaw class do AI reviewers miss most often in your benchmark? (3) What belongs in an AI BOM?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · SSDF and SAMM assessment | Gap list |
| 2 | 2 | Lab 2 · Secure service template | Template repository |
| 3 | 3 | Lab 3 · Control map and blocking rules | Control map; **P1 due** |
| 4 | 4 | Lab 4 · Custom SAST rules and precision | Rules and triage data |
| 5 | 5 | Lab 5 · Dependency intake and reachability | Intake policy |
| 6 | 6 | Lab 6 · Reproducible build and provenance | Two matching builds |
| 7 | 6 | Lab 6 (cont.) · Signing and admission | Blocked unsigned image; mid-term (AI off) |
| 8 | 7 | Lab 7 · SBOM, VEX and KEV/EPSS ranking | Ranked findings |
| 9 | 8 | Lab 8 · Pipeline hardening (no AI) | Hardened workflow; **P2 due** |
| 10 | 9 | Lab 9 · Guardrails at three layers | Policies and bypass test |
| 11 | 10 | ZAP and fuzz jobs | Pipeline runs |
| 12 | 11 | Metrics and roadmap | Dashboard design |
| 13 | 12 | Lab 10 · AI reviewer benchmark | Recall table |
| 14 | 12 | Project work | **P3 due** |
| 15 | Review | Oral defence and exam | Final exam |

## Working with AI in this course

- **Use AI for:** drafting Semgrep and CodeQL rules from incident descriptions (then testing them); explaining unfamiliar CI configuration; generating policy-as-code skeletons; summarising SBOM diffs; first-pass triage of scanner findings; proposing fixes for review.
- **Do without AI (drills):** the control map and blocking rules; pipeline hardening (Lab 8); triage precision measurement; the xz analysis; the mid-term and final.
- **Verify AI output by:** running every rule against positive and negative test cases; checking every package name on its registry and in OSV before adding it; requiring tests for every AI fix, including a test that failed before the fix; checking SLSA and SSDF claims against the specification text.
- **Where AI still fails here (show it):** your Lab 10 benchmark measures recall of AI reviewers on 20 seeded flaws, including authorization logic and business-rule flaws; record hallucinated package suggestions while generating code; record AI fixes that silence a scanner without removing the flaw.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs 1–10 | 25% |
| Projects P1 / P2 / P3 | 5% / 15% / 25% |
| Mid-term (AI off) | 10% |
| Final: design exam plus oral defence of P3 | 20% |

**Mastery gate.** You pass when you can, without AI and in three hours: (a) produce a control map for an unseen delivery process with block/warn decisions and justifications; (b) find at least four of five planted weaknesses in a provided CI/CD configuration and fix them; and (c) explain, for a described supply-chain incident, which controls would have prevented, detected or limited it, with SLSA and SSDF references.

## Industry reality

- **Supply chain incidents are now routine CISA alerts:** xz-utils (2024), tj-actions (2025), Shai-Hulud (2025), Axios and Nx Console (2026).
- **Regulation and procurement ask for evidence:** the EU CRA reporting duties since September 2026, US federal secure-development attestation built on SSDF, and CERT-In's BOM guidelines in India.
- **Platform vendors build controls in:** GitHub's push protection, artifact attestations and Autofix, and npm provenance make some SLSA practices available to every team.
- **Hiring:** DevSecOps and product security roles ask candidates to design a pipeline and respond to a dependency compromise.

**Interview questions from this course**

1. *"Design security for the delivery pipeline of 200 microservices without slowing developers."* Strong answer: risk tiers, control map with few blocking checks, paved-road templates, owner routing, provenance and signing with admission verification, metrics including developer time.
2. *"A popular npm package you depend on was just compromised. What do you do, and what would have limited the impact?"* Strong answer: identify exposure from SBOMs and lockfiles, freeze updates, rotate credentials reachable from affected builds and laptops, check for propagation, then intake controls, minimum package age, OIDC short-lived credentials, isolated runners.
3. *"What does SLSA Build Level 3 give you, and what doesn't it?"* Strong answer: unforgeable provenance from a hardened, isolated build platform; it does not prove the source is benign or that dependencies are safe; mention the Source track.
4. *"We have 4,000 open SCA findings. Where do we start?"* Strong answer: reachability, KEV and EPSS, asset criticality, VEX for not-affected, update automation, SLAs by risk, and stopping the inflow.
5. *"How should we let an AI coding agent open pull requests?"* Strong answer: its own identity with minimal permissions, sandboxed runner, no secrets, untrusted-input handling for issues and repository content, same review and checks as any contributor, audit logging.

## Resources (free first)

- **Frameworks:** [NIST SSDF SP 800-218](https://csrc.nist.gov/pubs/sp/800/218/final); [SP 800-218A](https://csrc.nist.gov/pubs/sp/800/218/a/final); [OWASP SAMM](https://owaspsamm.org/); [CISA Secure by Design](https://www.cisa.gov/securebydesign); [SLSA](https://slsa.dev/spec/); [OpenSSF S2C2F](https://github.com/ossf/s2c2f); [OWASP Top 10 CI/CD Security Risks](https://owasp.org/www-project-top-10-ci-cd-security-risks/).
- **Supply chain tooling:** [Sigstore](https://www.sigstore.dev/); [in-toto](https://in-toto.io/); [OpenSSF Scorecard](https://scorecard.dev/); [OSV](https://osv.dev/); [CycloneDX](https://cyclonedx.org/); [SPDX](https://spdx.dev/); [npm provenance](https://docs.npmjs.com/generating-provenance-statements); [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog); [FIRST EPSS](https://www.first.org/epss/).
- **Analysis and policy tools:** [Semgrep](https://semgrep.dev/docs/); [CodeQL](https://codeql.github.com/docs/); [OWASP ZAP](https://www.zaproxy.org/); [Trivy](https://trivy.dev/); [Syft](https://github.com/anchore/syft) and [Grype](https://github.com/anchore/grype); [Checkov](https://www.checkov.io/); [Kyverno](https://kyverno.io/docs/); [Conftest](https://www.conftest.dev/); [Renovate](https://docs.renovatebot.com/).
- **Platform guides:** [GitHub Actions security hardening](https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions); [RFC 9116 security.txt](https://www.rfc-editor.org/rfc/rfc9116).
- **Regulation:** [EU Cyber Resilience Act](https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act); CERT-In BOM guidelines v2.0 (see Sources).

## Sources

All checked 12 Oct 2026.

- CISA alerts: xz-utils (29 Mar 2024) — https://www.cisa.gov/news-events/alerts/2024/03/29/reported-supply-chain-compromise-affecting-xz-utils-data-compression-library-cve-2024-3094 ; tj-actions (18 Mar 2025) — https://www.cisa.gov/news-events/alerts/2025/03/18/supply-chain-compromise-third-party-tj-actionschanged-files-cve-2025-30066-and-reviewdogaction ; npm Shai-Hulud (23 Sep 2025) — https://www.cisa.gov/news-events/alerts/2025/09/23/widespread-supply-chain-compromise-impacting-npm-ecosystem ; Axios npm (20 Apr 2026) — https://www.cisa.gov/news-events/alerts/2026/04/20/supply-chain-compromise-impacts-axios-node-package-manager ; Nx Console (28 May 2026) — https://www.cisa.gov/news-events/alerts/2026/05/28/supply-chain-compromises-impact-nx-console-and-github-repositories
- OWASP Top 10:2025 — https://top10.owasp.org/2025
- SLSA specification v1.2 (current, with Build and Source tracks) — https://slsa.dev/spec/
- European Commission, Cyber Resilience Act page (reporting obligations from 11 Sep 2026) — https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act
- CERT-In Technical Guidelines on SBOM, QBOM and CBOM, AIBOM and HBOM v2.0 (9 Jul 2025), as summarised by Khaitan & Co — https://khaitanco.com/thought-leadership/CERT-Ins-Expanded-BOM-Guidelines-Preparing-for-the-Next-Phase-of-Cyber-Regulation
- Veracode 2025 GenAI Code Security Report press release (30 Jul 2025) — https://www.veracode.com/press-release/ai-generated-code-poses-major-security-risks-in-nearly-half-of-all-development-tasks-veracode-research-reveals/
- AWS Security Agent full repository code reviews (May 2026) — https://aws.amazon.com/about-aws/whats-new/2026/05/aws-security-agent-full-repository-code-review/
- Google Security Blog, memory safety in Android (25 Sep 2024) — https://security.googleblog.com/2024/09/eliminating-memory-safety-vulnerabilities-Android.html
- NIST SP 800-53 Release 5.2.0 (27 Aug 2025), software update controls — https://csrc.nist.gov/News/2025/nist-releases-revision-to-sp-800-53-controls

_Last reviewed: 2026-10_
