# OV01 · Cloud Security

| Composed of | Overlap courses | When | Typical entry majors | Market pages |
|---|---|---|---|---|
| [CLD301](../../03_majors/cloud_engineering/year_3/CLD301_cloud_architecture_on_aws_azure_and_google_cloud/README.md) · [SAR401](../../03_majors/security_architecture/year_4/SAR401_cloud_security_architecture/README.md) · [SEC303](../../03_majors/cybersecurity_defense/year_3/SEC303_identity_and_access_management/README.md) | [OV01A](OV01A_cloud_security_posture_detection_and_response/README.md) · [OV01B](OV01B_kubernetes_and_container_security/README.md) | Year 4 (semesters 7–8) | Cloud Engineering, Cybersecurity Defense, Security Architecture, DevOps/SRE | [CLD](../../06_career_and_market_readiness/01_market_map/roles/CLD_cloud_engineering.md) · [SEC](../../06_career_and_market_readiness/01_market_map/roles/SEC_cybersecurity_defense.md) · [SAR](../../06_career_and_market_readiness/01_market_map/roles/SAR_security_architecture.md) |

## The job this overlap maps to

A **cloud security engineer** keeps an organisation's cloud estate (AWS, Azure, Google Cloud, Kubernetes and the SaaS around them) safe while hundreds of engineers change it every day. In practice the job has four parts:

1. **Posture.** Know every account, subscription, project, cluster and identity; find the misconfigurations and over-privileged roles that matter; get them fixed in code, not in the console.
2. **Detection.** Turn audit logs (AWS CloudTrail, Azure Activity and Entra ID logs, Google Cloud Audit Logs, Kubernetes audit logs) and runtime signals into detections that fire on real attacks and stay quiet otherwise.
3. **Response.** Contain a leaked key, a hijacked role or a compromised pod in minutes without destroying evidence or production.
4. **Workloads.** Harden containers and Kubernetes clusters: RBAC, admission control, Pod Security Standards, network policy, image verification and runtime detection.

Common titles: Cloud Security Engineer, Cloud Detection and Response Engineer, Kubernetes / Container Security Engineer, Cloud Security Architect (more senior), and in product companies "Infrastructure Security Engineer". Security architecture is rarely an entry-level job; people usually arrive after several years as security, cloud or backend engineers ([SAR market page](../../06_career_and_market_readiness/01_market_map/roles/SAR_security_architecture.md)).

## Why this overlap exists

The job sits between three fields, and each one alone leaves a gap:

- A **cloud engineer** knows the services but often treats IAM, logging and guardrails as someone else's problem.
- A **SOC analyst** knows triage but may not know what `AssumeRoleWithWebIdentity` or a Kubernetes `ClusterRoleBinding` means.
- A **security architect** designs guardrails but does not always run detections or incidents.

Public incidents keep landing exactly in that gap. In 2019 an attacker used server-side request forgery to obtain an instance role's credentials and read Capital One's data from storage; the US regulator fined the bank $80 million ([OCC, Aug 2020](https://www.occ.gov/news-issuances/news-releases/2020/nr-occ-2020-101.html)). In 2024 a threat actor used credentials stolen by infostealer malware to access Snowflake customer instances that had no multi-factor authentication ([Mandiant, Jun 2024](https://cloud.google.com/blog/topics/threat-intelligence/unc5537-snowflake-data-theft-extortion)). The US Cyber Safety Review Board traced the 2023 Exchange Online intrusion to a "cascade of security failures" around a cloud signing key ([CSRB, 2024](https://www.cisa.gov/sites/default/files/2025-03/CSRBReviewOfTheSummer2023MEOIntrusion508.pdf)). Each one needed cloud architecture, identity and detection skills together.

**Demand evidence (checked October 2026).**

| Signal | Figure | Source |
|---|---|---|
| Cloud security as a skills need (global) | 36%, second only to AI (41%), among 16,029 security professionals | [ISC2 2025](https://www.isc2.org/Insights/2025/12/2025-ISC2-Cybersecurity-Workforce-Study) |
| Cloud security as a skills need (India) | 43% of 524 respondents; "skills shortages have overtaken staffing shortages" | [ISC2 India, Sept 2026](https://www.isc2.org/insights/2026/09/research-india-cybersecurity-workforce-reaches-a-turning-point-skills-ai) |
| US information security analysts | +21% projected, 2025–35 | [BLS](https://www.bls.gov/ooh/computer-and-information-technology/information-security-analysts.htm) |
| Security Management Specialists | Fifth fastest-growing job to 2030 (global employer survey), also listed for India | [WEF 2025](https://reports.weforum.org/docs/WEF_Future_of_Jobs_Report_2025.pdf) |
| Counter-signal | 24% of security professionals saw layoffs and 39% hiring freezes in 2025 | [ISC2 2025](https://www.isc2.org/Insights/2025/12/2025-ISC2-Cybersecurity-Workforce-Study) |

**Analysis.** The demand is for specific, demonstrable skills, not for any certificate holder. A portfolio that shows a working detection pipeline, a hardened cluster and a written incident timeline is what separates candidates.

## Before you start

You need the overlap prerequisites from [catalog.json](../../catalog.json): **CLD301** (cloud architecture, IAM models, landing zones) and **SEC303** (identity, federation, privileged access, identity threat detection). **SAR401** is a corequisite: take it in semester 7 alongside OV01A. Strongly recommended: [CLD303 Containers and Kubernetes](../../03_majors/cloud_engineering/year_3/CLD303_containers_and_kubernetes/README.md) before OV01B, and [SEC302 Security Operations](../../03_majors/cybersecurity_defense/year_3/SEC302_security_operations_soc_siem_and_monitoring/README.md) for SIEM and triage skills.

## How to sequence the courses

| Semester | From your major | Composed courses | Overlap course |
|---|---|---|---|
| 5 (Y3) | Major core | **CLD301** and **SEC303** (take whichever is outside your major as an elective) | — |
| 6 (Y3) | Major core | CLD303 recommended (elective) | — |
| 7 (Y4) | Major advanced | **SAR401** (corequisite) | **OV01A** Cloud Security Posture, Detection and Response |
| 8 (Y4) | Major advanced | — | **OV01B** Kubernetes and Container Security |
| 9–10 (Y5) | Thesis or capstone | — | OV01 capstone as [THS501](../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md)/[THS502](../../05_shared_years_3_to_5/THS502_thesis_or_capstone_ii/README.md) topic, or in [IND401](../../05_shared_years_3_to_5/IND401_industry_co_op_studio/README.md) |

How the pieces divide the work, so nothing is taught twice:

- **CLD301** teaches how the clouds work, including IAM policy evaluation and landing zones.
- **SEC303** teaches identity: federation, tokens, privileged access, identity detection.
- **SAR401** designs the guardrails, data perimeters and logging architecture.
- **OV01A** operates them: inventory, posture scanning, attack-path prioritisation, detection-as-code on cloud logs, and cloud incident response.
- **OV01B** goes deep on the workload layer: Kubernetes RBAC, admission, isolation, supply chain at the cluster door, runtime detection and CKS-level hardening.

## The two overlap courses

| Course | Semester | What you can do at the end |
|---|---|---|
| [OV01A · Cloud Security Posture, Detection and Response](OV01A_cloud_security_posture_detection_and_response/README.md) | 7 | Inventory a multi-account estate, prioritise findings by attack path, ship tested detections on cloud audit logs, and lead a cloud incident from first alert to regulator-ready report |
| [OV01B · Kubernetes and Container Security](OV01B_kubernetes_and_container_security/README.md) | 8 | Harden a cluster to CIS and Pod Security Standards, enforce policy at admission, verify signed images, detect runtime threats with Falco, and respond to a compromised pod |

## Capstone: secure a multi-account cloud and its Kubernetes platform

**Brief.** Build a small but realistic estate in your own sandbox accounts (AWS Organizations, or the Azure or Google Cloud equivalent): at least four accounts (security tooling, log archive, workload-prod, workload-dev) and one managed Kubernetes cluster running a three-service application. Then secure, monitor and defend it. The scenario is illustrative; use only accounts you own.

**Acceptance criteria (all measurable).**

1. **Inventory.** A query (Steampipe, CloudQuery or a provider inventory service) lists 100% of resources in all accounts with owner and data-class tags; untagged resources appear as findings.
2. **Posture.** A scheduled CIS benchmark scan (for example Prowler) covers all accounts; every critical and high finding is either fixed through an infrastructure-as-code pull request or has a recorded exception with an expiry date. Final report shows zero unexcepted critical findings.
3. **Guardrails.** At least five preventive guardrails (for example SCPs or RCPs, Azure Policy deny, organisation policy constraints) with automated tests proving each blocks its target action.
4. **Detection.** At least 15 detections as code (Sigma or native rule format) on cloud and Kubernetes audit logs, each with a unit test on recorded log samples and a validation run using emulation in your own sandbox (for example Stratus Red Team). Report detection rate, median time from event to alert, and false-positive rate over one week of normal activity.
5. **Cluster.** The cluster passes kube-bench with no failed checks that are in your control; all application namespaces enforce the `restricted` Pod Security Standard; only images signed by your pipeline are admitted (a test shows an unsigned image rejected).
6. **Runtime.** Falco or Tetragon alerts on at least five defined runtime behaviours (for example a shell in a container, writes below `/etc`, unexpected outbound connection), routed to the same alert queue as cloud detections.
7. **Response.** A timed game day (run by a classmate as an announced exercise): a planted "leaked access key" and a "compromised pod" scenario. You contain both within 30 minutes of the first alert, preserve evidence (CloudTrail extract, volume snapshot, pod logs), and deliver a timeline and a regulator-style notification draft within 6 hours, matching CERT-In's reporting window ([CERT-In Directions, Apr 2022](https://www.cert-in.org.in/PDF/CERT-In_Directions_70B_28.04.2022.pdf)).
8. **Cost and teardown.** Monthly run cost is documented; everything is torn down by script and the teardown is verified.

**What it proves.** You can do the whole job on a small scale: see the estate, fix what matters, detect what gets through, and respond calmly with evidence.

## Roles it leads to

| Role | What people in it do | Typical first step after this overlap |
|---|---|---|
| Cloud Security Engineer | Posture management, guardrails, IAM reviews, security tooling as code | Junior or mid-level cloud security role, or a cloud engineer role with a security remit |
| Cloud Detection and Response Engineer | Detections on cloud and identity logs, investigations, cloud incident response | SOC Tier 2 or detection engineering role on a cloud-heavy team |
| Kubernetes / Container Security Engineer | Cluster hardening, admission policy, runtime detection, image supply chain | Platform security role; the CKS exam is a useful signal after OV01B |
| Cloud Security Architect (later) | Reference architectures, data perimeters, risk decisions | Usually after several years in one of the roles above |

Interview loops for these roles combine a cloud troubleshooting scenario, an IAM policy review, a detection-writing exercise and an incident walkthrough; see the [CLD](../../06_career_and_market_readiness/01_market_map/roles/CLD_cloud_engineering.md) and [SEC](../../06_career_and_market_readiness/01_market_map/roles/SEC_cybersecurity_defense.md) market pages.

## Sources

All checked 12 Oct 2026.

- ISC2, 2025 Cybersecurity Workforce Study (4 Dec 2025) — https://www.isc2.org/Insights/2025/12/2025-ISC2-Cybersecurity-Workforce-Study ; India study (24 Sep 2026) — https://www.isc2.org/insights/2026/09/research-india-cybersecurity-workforce-reaches-a-turning-point-skills-ai
- US BLS, Information security analysts (2025–35 projections) — https://www.bls.gov/ooh/computer-and-information-technology/information-security-analysts.htm
- World Economic Forum, Future of Jobs Report 2025 — https://reports.weforum.org/docs/WEF_Future_of_Jobs_Report_2025.pdf
- OCC, civil money penalty against Capital One (6 Aug 2020) — https://www.occ.gov/news-issuances/news-releases/2020/nr-occ-2020-101.html
- Mandiant, UNC5537 targets Snowflake customer instances (Jun 2024) — https://cloud.google.com/blog/topics/threat-intelligence/unc5537-snowflake-data-theft-extortion
- Cyber Safety Review Board, review of the Summer 2023 Microsoft Exchange Online intrusion (Mar 2024) — https://www.cisa.gov/sites/default/files/2025-03/CSRBReviewOfTheSummer2023MEOIntrusion508.pdf
- CERT-In Directions (28 Apr 2022) — https://www.cert-in.org.in/PDF/CERT-In_Directions_70B_28.04.2022.pdf

_Last reviewed: 2026-10_
