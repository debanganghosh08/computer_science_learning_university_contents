# OV03A · Software Supply Chain Security

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 7 | 4 (≈ 120 hours) | L3 → L4 | [OPS301](../../../03_majors/devops_sre_platform_engineering/year_3/OPS301_ci_cd_engineering/README.md), [SAR305](../../../03_majors/security_architecture/year_3/SAR305_secure_sdlc_and_devsecops_architecture/README.md), [SEC302](../../../03_majors/cybersecurity_defense/year_3/SEC302_security_operations_soc_siem_and_monitoring/README.md) | [OV03B](../OV03B_policy_as_code_and_secure_ci_cd/README.md), [OFF501](../../../03_majors/ethical_hacking_offensive_security/year_5/OFF501_frontier_seminar_ai_driven_vulnerability/README.md), [THS501](../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) |

Part of the [OV03 DevSecOps overlap](../README.md). SAR305 placed SLSA, SBOM, signing and the xz lesson on the architect's control map, and OPS301 Chapter 9 introduced them to pipeline engineers. This course implements them end to end, measures them, and uses them in an incident.

## Why this course matters now

Attackers increasingly go after the things software is built from and with: packages, maintainers, build systems, CI actions and developer tools. In March 2024 a backdoor was found in xz-utils release tarballs after a multi-year effort to gain maintainer trust ([NVD](https://nvd.nist.gov/vuln/detail/CVE-2024-3094)); in March 2025 a compromised GitHub Action exposed CI secrets across many repositories ([CISA](https://www.cisa.gov/news-events/alerts/2025/03/18/supply-chain-compromise-third-party-tj-actionschanged-files-cve-2025-30066-and-reviewdogaction)); in September 2025 the Shai-Hulud worm spread through stolen npm tokens, and GitHub responded with a plan for trusted publishing, short-lived granular tokens and FIDO-based 2FA on npm ([GitHub, Sept 2025](https://github.blog/security/supply-chain-security/our-plan-for-a-more-secure-npm-supply-chain/)); in 2026 two Axios releases pulled in a malicious dependency, and a poisoned VS Code extension led to theft of internal GitHub repositories ([CISA, Apr 2026](https://www.cisa.gov/news-events/alerts/2026/04/20/supply-chain-compromise-impacts-axios-node-package-manager), [CISA, May 2026](https://www.cisa.gov/news-events/alerts/2026/05/28/supply-chain-compromises-impact-nx-console-and-github-repositories)). The defences have matured: SLSA v1.2 with Build and Source tracks, Sigstore keyless signing, GitHub artifact attestations, PyPI attestations and npm trusted publishing are all production features. AI coding agents add a new risk (they choose dependencies, sometimes ones that do not exist) and a new help (they triage scanner output). The human job is to decide what to trust, prove it with evidence, and respond fast when trust breaks.

## Learning outcomes

By the end you can:

1. **Threat-model** a software supply chain with the SLSA threat model and **map** real incidents to the stage they attacked.
2. **Run** dependency intake that combines SCA, reachability, OpenSSF Scorecard, release-age cooldowns and malicious-package feeds, and **measure** what it blocks.
3. **Produce** SLSA Build Level 3 provenance on hosted, isolated builders and **verify** it with policy bound to repository and workflow identity.
4. **Sign and verify** artefacts with Sigstore (Fulcio, Rekor, TUF) and ecosystem mechanisms (npm provenance, PyPI attestations), and **explain** what a signature does and does not prove.
5. **Generate** complete SBOMs at build time, **measure** their completeness, and **publish** VEX statements with justifications.
6. **Reduce** container attack surface with minimal base images and a rebuild cadence, and **track** exposure by exploitability rather than CVE counts.
7. **Secure** the ML and AI artefact supply chain: model formats, model signing and AI BOMs.
8. **Lead** response to a compromised dependency: scope affected builds and deployments within hours using SBOMs or a dependency graph, rotate secrets, rebuild and report.

## Chapters and lessons

### Chapter 1 · The supply chain as an attack surface (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 The SLSA threat model | Source, build, dependency and distribution threats (SLSA's threat categories); producers versus consumers | Draw your organisation's supply chain and mark each threat |
| 1.2 A decade of incidents | event-stream (2018), SolarWinds Orion (2020), Codecov uploader (2021), PyTorch nightly `torchtriton` dependency confusion (2022), 3CX (2023), xz-utils (2024), tj-actions (2025), Shai-Hulud (2025), Axios and Nx Console (2026): what was compromised and what control would have helped (defensive view only) | Build an incident table: stage, entry point, detection, missing control |
| 1.3 Who is responsible | Producers, maintainers, registries, consumers; the NIST SSDF and CISA's Secure Software Development Attestation Form; EU Cyber Resilience Act duties (reporting from 11 Sep 2026) | Write the obligations memo for an illustrative Indian SaaS company selling into the EU |
| 1.4 Measuring today's state | OpenSSF Scorecard on your repositories and top dependencies; inventory of build systems and publishing credentials | Score 20 dependencies; list every place a publish token exists |

**Check your understanding:** Which incidents in the table would SLSA build provenance alone not have stopped, and why? Why is a publishing token a supply-chain asset? What does a consumer owe its own users when a dependency is compromised?

### Chapter 2 · Case study: xz-utils, defensively (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 What happened | A long social-engineering campaign for maintainership; malicious code shipped in release tarballs but not visible in the repository history; discovered by Andres Freund while investigating a performance anomaly (oss-security, 29 March 2024) | Write a timeline from primary sources: the oss-security post, NVD, CISA |
| 2.2 Where the controls were | Distribution build processes, tarball versus repository divergence, test fixtures as code, maintainer burnout and funding | List five controls and who would own each |
| 2.3 Tarball-to-tag verification | Comparing release artefacts with tagged source; reproducible builds as an independent check | Diff a benign project's release tarball against its tag; explain every difference |
| 2.4 What provenance can and cannot show | Provenance proves where and how something was built, not that the source was benign | Write a one-page "limits of provenance" note for leadership |

**Check your understanding:** Why did code review of the repository not catch the backdoor? Which signal led to discovery, and what does that say about monitoring? What would you change in your own release process tomorrow?

### Chapter 3 · Dependency intake and governance (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Software composition analysis | OSV-Scanner, Trivy, Grype, Dependabot; purl identifiers; reachability analysis | Scan three services; compare tools on the same lockfiles |
| 3.2 Intake decisions | OpenSSF Scorecard checks, maintainer activity, licence, transitive weight; an intake rubric | Accept or reject five candidate packages with the rubric |
| 3.3 Proxies and cooldowns | Registry proxies (Artifactory, Nexus, pull-through caches), allow-lists, release-age cooldowns such as Renovate's `minimumReleaseAge` | Configure a seven-day cooldown and measure how many updates it delays |
| 3.4 Updates without fear | Grouped updates, test gates, update SLAs by severity, lockfile hygiene | Run a month of Renovate PRs in a fork with auto-merge for safe classes |

**Check your understanding:** Why would a cooldown have reduced exposure to the 2025–26 npm incidents, and what does it cost? Why is reachability not a reason to ignore a vulnerability forever? Who should approve a new direct dependency?

### Chapter 4 · Malicious packages and ecosystem defences (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 The patterns | Typosquatting, dependency confusion, compromised maintainer accounts, install-time scripts, self-spreading worms (names and defences only) | Classify 20 entries from the OpenSSF malicious-packages dataset by pattern |
| 4.2 Ecosystem controls | npm trusted publishing (generally available July 2025), granular short-lived tokens, FIDO 2FA; PyPI Trusted Publishers; scoped registries for internal names | Move a package's publishing to trusted publishing with no long-lived token |
| 4.3 Consumer controls | `--ignore-scripts` and script allow-lists, scoped registries against dependency confusion, lockfile-only installs in CI | Make CI installs deterministic and script-free; measure breakage |
| 4.4 AI-chosen dependencies | Hallucinated package names ("slopsquatting"), agents running installs; policies for agent-added dependencies | Audit dependencies added by an AI agent in a sample repository |

**Check your understanding:** Why does an internal package name need a reserved public name or a scoped registry? What does trusted publishing remove from an attacker's options? How should a pipeline treat a dependency added by an agent?

### Chapter 5 · Build integrity and SLSA (weeks 5–6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 SLSA v1.2 in practice | Build Levels 1–3 and the Source track; requirements as engineering tasks | Gap-assess one pipeline against Build L3 |
| 5.2 Hosted, isolated builders | Ephemeral runners, isolation between builds, secrets not reachable by build steps, reusable workflows as trusted builders | Restructure a workflow so build and signing are isolated |
| 5.3 Generating provenance | GitHub artifact attestations (generally available June 2024), the SLSA GitHub generator, GitLab provenance; in-toto statements | Produce provenance for an image and a package |
| 5.4 Hermetic and reproducible builds | Pinned toolchains, network-off builds, `SOURCE_DATE_EPOCH`, Reproducible Builds project; checking with diffoscope | Make one artefact bit-for-bit reproducible across two builders |
| 5.5 Verifying provenance | `slsa-verifier`, `gh attestation verify`, expected builder and source identity | Reject an artefact built from a fork |

**Check your understanding:** What does Build Level 3 add over Level 2, in one sentence each? Why does reproducibility give consumers an independent check that provenance cannot? What exactly should a verifier compare?

### Chapter 6 · Signing and transparency (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Sigstore internals | Fulcio short-lived certificates from OIDC identities, Rekor transparency log, TUF-distributed trust roots | Trace one keyless signature through Fulcio and Rekor entries |
| 6.2 Verifying identities | Certificate identity and issuer constraints; why "signed" means nothing without "by whom" | Write verification commands that accept only your release workflow |
| 6.3 Ecosystem signatures | npm provenance, PyPI attestations (PEP 740, November 2024), Maven Central signatures, container signatures in OCI registries | Verify provenance for three packages you depend on |
| 6.4 Key-based signing and its place | KMS-backed keys for air-gapped or regulated environments; rotation and revocation | Compare operational burden of keyless and KMS-key signing |

**Check your understanding:** What can an attacker who steals a CI token do in a keyless world, and what will the log show? Why is a transparency log useful even if nobody watches it in real time? When is a long-lived key still justified?

### Chapter 7 · Attestations and consumption policy (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 The attestation framework | in-toto statements and predicates: SLSA provenance, SBOM, vulnerability scan, test results | Attach four attestation types to one image |
| 7.2 Policy at deploy | Kyverno `verifyImages` and Sigstore policy-controller requiring signature plus provenance from specific workflows | Block an image built outside the release workflow |
| 7.3 Graph queries | GUAC (Graph for Understanding Artifact Composition) to answer "where is package X running?" | Load SBOMs and attestations into GUAC; query a dependency's blast radius |
| 7.4 Third-party software | Requesting SBOMs and attestations from vendors; what to do when they cannot provide them | Write vendor requirements for an illustrative procurement |

**Check your understanding:** Why verify attestations at deploy time rather than trusting the registry? What question can a graph answer in minutes that would otherwise take days? What is a reasonable request to a vendor that cannot produce SBOMs?

### Chapter 8 · SBOM quality and VEX (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Formats and minimum elements | SPDX 3.0 and CycloneDX 1.6; NTIA minimum elements (2021) and CISA's SBOM work; CERT-In's 2025 SBOM, AIBOM and related guidelines | Generate both formats for one image; compare fields |
| 8.2 Completeness | Build-time versus image-scan SBOMs, missing native libraries and vendored code, quality scoring | Measure SBOM completeness against an independent scan |
| 8.3 Matching to vulnerabilities | purl versus CPE, OSV data, false matches | Explain five false-positive matches and fix their root cause |
| 8.4 VEX | OpenVEX and CSAF VEX; statuses and justifications; who may issue them | Publish VEX for five non-exploitable findings with evidence |

**Check your understanding:** Why does an SBOM generated by scanning an image miss things a build-time SBOM catches, and vice versa? When is "not affected" an honest VEX status? Who should be allowed to sign a VEX document?

### Chapter 9 · Containers and base images (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Minimal images | Distroless, Wolfi-based and scratch images; package counts and attack surface | Rebuild three images on minimal bases; compare size, packages and findings |
| 9.2 Rebuild cadence | Automatic base-image updates, digest pinning with bots, rebuild triggers | Automate weekly rebuilds with tests |
| 9.3 Prioritising by exploitability | CISA KEV, FIRST EPSS, reachability, exposure; why CVE counts mislead | Rank 50 findings; defend the top five |
| 9.4 Registry controls | Immutable tags, retention, quarantine of unscanned images, replication | Configure quarantine-until-scanned in a registry |

**Check your understanding:** Why can a "zero CVE" image still be risky? What breaks when you pin by digest, and how do bots fix it? Which finding would you patch first: high CVSS unreachable, or medium in KEV and exposed?

### Chapter 10 · Source and developer environment security (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 The SLSA Source track | Branch protection and rulesets, required reviews, history protection, source provenance | Meet the Source track's first level on one repository |
| 10.2 Commit and tag signing | gitsign (keyless), SSH and GPG signing, verifying in CI | Require signed commits on a protected branch |
| 10.3 Secrets in source | Push protection, secret scanning, rotation playbooks | Plant a test secret; measure time to block and rotate |
| 10.4 Developer machines and extensions | IDE extension risk (the 2026 Nx Console case), dev containers, least-privilege tokens on laptops | Write an extension policy and a laptop token inventory |

**Check your understanding:** Why are developer laptops part of the supply chain? What does a signed commit prove? Which token on your laptop would hurt most if stolen?

### Chapter 11 · ML and AI artefacts (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Model file risks | Pickle-based formats can execute code on load; safetensors as a data-only format; scanning model hubs | Convert a model to safetensors and verify outputs match |
| 11.2 Model signing | OpenSSF model signing v1.0 (April 2025) built on Sigstore; signing datasets and prompts | Sign and verify a model before loading it in a serving container |
| 11.3 AI bills of materials | CycloneDX ML-BOM and SPDX AI and dataset profiles; CERT-In AIBOM guidance | Produce an AI BOM for one model service |
| 11.4 Agents in the pipeline | AI coding agents adding dependencies and editing workflow files; review and policy requirements | Define rules for agent-authored dependency changes |

**Check your understanding:** Why is loading an untrusted pickle equivalent to running untrusted code? What should a model-serving service verify before loading weights? Which agent action in a repository needs a human every time?

### Chapter 12 · Response and running the programme (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Compromised-dependency response | Scope with SBOMs or GUAC, freeze builds, identify exposed CI secrets (the tj-actions lesson), rotate, rebuild, redeploy, notify | Run the drill for a planted compromised internal library |
| 12.2 Metrics | Share of artefacts with provenance and signatures, SBOM coverage and completeness, time to patch KEV findings, Scorecard trends, cooldown exceptions | Build the programme dashboard |
| 12.3 Regulation and customers | CRA vulnerability reporting, CERT-In guidance, customer SBOM requests, secure development attestations | Answer a customer security questionnaire with evidence links |
| 12.4 Roadmap | Sequencing controls by risk reduction per unit of developer friction | Present a 12-month roadmap to a panel |

**Check your understanding:** In the first hour of a dependency compromise, what do you need to know, and where does each answer come from? Which metric would you show a board, and why not CVE counts? What is the cheapest control with the largest effect in your estate?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Supply chain map and Scorecard | Incident table |
| 2 | 2 | Lab 2 · Tarball-to-tag verification | xz timeline |
| 3 | 3 | Lab 3 · Intake and cooldowns | — |
| 4 | 4 | Lab 4 · Trusted publishing and script-free installs | **P1 due** |
| 5 | 5 | Lab 5 · Provenance on isolated builders | — |
| 6 | 5 | Lab 5 (cont.) · Reproducible build | Mid-term (AI off): pipeline threat model |
| 7 | 6 | Lab 6 · Keyless signing and verification | — |
| 8 | 7 | Lab 7 · Deploy-time verification and GUAC | — |
| 9 | 8 | Lab 8 · SBOM completeness and VEX | **P2 due** |
| 10 | 9 | Lab 9 · Minimal images and rebuilds | — |
| 11 | 10 | Lab 10 · Source track and secrets | — |
| 12 | 11 | Model signing lab | AI BOM |
| 13 | 12 | Compromised-dependency drill | Incident report |
| 14 | 12 | Programme dashboard and roadmap | **P3 due** |
| 15 | Review | Timed response exercise and oral defence of P3 | Final exam |

## Working with AI in this course

- **Use AI for:** explaining scanner findings and advisories; drafting VEX justifications for you to verify; writing verification scripts and Renovate configuration; summarising long incident write-ups.
- **Do without AI (drills):** reading an attestation and a Rekor entry by hand; the pipeline threat model; the compromised-dependency drill's scoping step; the mid-term and final.
- **Verify AI output by:** checking every package name an AI suggests against the registry, its age and its Scorecard before use; running verification commands rather than trusting claims of "signed" or "SLSA 3"; reproducing any exploitability claim in a VEX draft with your own reachability evidence.
- **Where AI still fails here:** record AI-suggested packages that do not exist or are very new, AI-drafted VEX statements without evidence, and AI triage that dismissed a finding later shown to be reachable. Studies of AI-generated code report security flaws in a large share of outputs (Veracode's 2025 report found issues in nearly half of tasks; see [SAR305](../../../03_majors/security_architecture/year_3/SAR305_secure_sdlc_and_devsecops_architecture/README.md) for the source).

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1–P3 | 35% |
| Mid-term (AI off) | 10% |
| Final: timed response exercise (AI off) + oral defence of P3 | 30% |

**Mastery gate.** You pass when you can, with AI tools off: (1) verify a container image's signature and provenance and state exactly what the verification proves; (2) given an advisory for a compromised package version and an estate's SBOMs, list affected artefacts and running workloads within 60 minutes; (3) take an unhardened repository to SLSA Build Level 3 provenance with keyless signing in one working day.

## Industry reality

Registries and platforms now ship the controls this course teaches: GitHub artifact attestations (June 2024), PyPI attestations (November 2024), npm trusted publishing (July 2025), and SHA-pinning enforcement for Actions (August 2025). CISA's alerts in 2025–26 repeatedly ask organisations to find which builds pulled a compromised version and to rotate CI credentials, which is only fast with SBOMs, provenance and a graph. Interviewers for supply-chain and DevSecOps roles ask candidates to reason about these incidents and to explain verification precisely.

**Interview questions from this course**

1. *What does a Sigstore keyless signature on an image prove?* Strong answer: that an identity (for example a specific GitHub workflow in a specific repository, via OIDC) obtained a short-lived certificate and signed this digest, logged in Rekor; it does not prove the source was safe; verification must pin issuer and identity.
2. *An advisory says version 1.14.1 of a popular package was malicious for three hours yesterday. What do you do?* Strong answer: query SBOMs or GUAC and lockfiles for that version; check CI logs for installs in the window; isolate affected runners and developer machines; rotate secrets those environments held; rebuild and redeploy; add cooldowns and intake policy; report.
3. *Explain SLSA Build Level 3 to a developer.* Strong answer: builds run on a hosted, isolated platform; provenance is generated by the platform and cannot be forged by the build steps; secrets used for signing are not accessible to user-defined steps; consumers verify it.
4. *Why might an SBOM be incomplete, and how would you measure it?* Strong answer: vendored code, static binaries, OS packages missed by language tools, build-time downloads; compare build-time SBOM with an independent image scan and binary analysis; track a completeness metric.
5. *How would you stop dependency confusion for internal packages?* Strong answer: scoped or namespaced registries, reserving names publicly, registry proxy configuration that never resolves internal names upstream, lockfiles with integrity hashes, and CI that installs only from the proxy.

## Resources (free first)

- **Frameworks:** SLSA specification — https://slsa.dev/spec/ ; NIST SSDF SP 800-218 — https://csrc.nist.gov/pubs/sp/800/218/final ; CISA SBOM resources — https://www.cisa.gov/sbom ; CISA Secure Software Development Attestation Form — https://www.cisa.gov/resources-tools/resources/secure-software-development-attestation-form
- **Tools and projects:** Sigstore — https://www.sigstore.dev/ ; in-toto — https://in-toto.io/ ; OpenSSF Scorecard — https://scorecard.dev/ ; GUAC — https://guac.sh/ ; OSV — https://osv.dev/ ; OpenSSF malicious packages — https://github.com/ossf/malicious-packages ; OpenVEX — https://openvex.dev/ ; Reproducible Builds — https://reproducible-builds.org/ ; Trivy — https://trivy.dev/
- **Ecosystems:** GitHub artifact attestations — https://github.blog/changelog/2024-06-25-artifact-attestations-is-generally-available/ ; PyPI attestations — https://blog.pypi.org/posts/2024-11-14-pypi-now-supports-digital-attestations/ ; npm trusted publishing — https://github.blog/changelog/2025-07-31-npm-trusted-publishing-with-oidc-is-generally-available/
- **Primary incident sources:** xz-utils disclosure on oss-security — https://www.openwall.com/lists/oss-security/2024/03/29/4 ; PyTorch `torchtriton` — https://pytorch.org/blog/compromised-nightly-dependency/ ; Codecov — https://about.codecov.io/security-update/ ; 3CX (Mandiant) — https://cloud.google.com/blog/topics/threat-intelligence/3cx-software-supply-chain-compromise
- **Paid, optional:** none required.

## Sources

All checked 12 Oct 2026.

- NVD, CVE-2024-3094 (published 29 Mar 2024) — https://nvd.nist.gov/vuln/detail/CVE-2024-3094 ; Andres Freund, oss-security post (29 Mar 2024) — https://www.openwall.com/lists/oss-security/2024/03/29/4
- CISA alerts: tj-actions (18 Mar 2025) — https://www.cisa.gov/news-events/alerts/2025/03/18/supply-chain-compromise-third-party-tj-actionschanged-files-cve-2025-30066-and-reviewdogaction ; npm (23 Sep 2025) — https://www.cisa.gov/news-events/alerts/2025/09/23/widespread-supply-chain-compromise-impacting-npm-ecosystem ; Axios (20 Apr 2026) — https://www.cisa.gov/news-events/alerts/2026/04/20/supply-chain-compromise-impacts-axios-node-package-manager ; Nx Console (28 May 2026) — https://www.cisa.gov/news-events/alerts/2026/05/28/supply-chain-compromises-impact-nx-console-and-github-repositories
- GitHub, "Our plan for a more secure npm supply chain" (22 Sep 2025) — https://github.blog/security/supply-chain-security/our-plan-for-a-more-secure-npm-supply-chain/
- GitHub changelog: artifact attestations GA (25 Jun 2024) — https://github.blog/changelog/2024-06-25-artifact-attestations-is-generally-available/ ; npm trusted publishing GA (31 Jul 2025) — https://github.blog/changelog/2025-07-31-npm-trusted-publishing-with-oidc-is-generally-available/ ; Actions SHA-pinning policy (15 Aug 2025) — https://github.blog/changelog/2025-08-15-github-actions-policy-now-supports-blocking-and-sha-pinning-actions/
- PyPI blog, digital attestations (14 Nov 2024) — https://blog.pypi.org/posts/2024-11-14-pypi-now-supports-digital-attestations/
- SLSA specification index (v1.2 current) — https://slsa.dev/spec/
- OpenSSF, model signing v1.0 (4 Apr 2025) — https://openssf.org/blog/2025/04/04/launch-of-model-signing-v1-0-openssf-ai-ml-working-group-secures-the-machine-learning-supply-chain/
- CISA ED 21-01 (SolarWinds) — https://www.cisa.gov/news-events/directives/ed-21-01-mitigate-solarwinds-orion-code-compromise ; PyTorch (Dec 2022) — https://pytorch.org/blog/compromised-nightly-dependency/ ; Codecov (2021) — https://about.codecov.io/security-update/ ; Mandiant 3CX (2023) — https://cloud.google.com/blog/topics/threat-intelligence/3cx-software-supply-chain-compromise
- European Commission, Cyber Resilience Act — https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act

_Last reviewed: 2026-10_
