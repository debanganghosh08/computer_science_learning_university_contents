# OV01A · Labs and projects

All work happens in sandbox accounts you own (AWS Organizations, or an Azure tenant with management groups, or a Google Cloud organisation), with a budget alarm and a teardown script from Lab 1. Never scan, emulate attacks against, or "test" resources you do not own. Every lab ships code in a repository, a short write-up with measured numbers, and the teardown proof.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Sandbox organisation and case mapping | Create a four-account sandbox (security, log archive, prod, dev) with budgets; map Capital One, Snowflake, Exchange Online and Salesloft Drift to ATT&CK techniques and log sources | Account diagram, budget alarm screenshot, teardown script, ATT&CK mapping table | 4 h |
| 2 · Multi-account inventory | Build an asset table with Steampipe or CloudQuery across all accounts; resolve owners from tags and IaC repositories | SQL queries, coverage figure (resources with owner ÷ all resources), list of ownerless resources | 4 h |
| 3 · Posture scanning and custom checks | Run Prowler with the CIS profile across accounts; write three custom checks for organisation rules | Scan output, three tested checks, a top-20 list with reasons | 5 h |
| 4 · Attack-path graph | Load identities, trust policies, network exposure and data stores into a graph (Cartography + Neo4j or your own model); deploy one CloudGoat scenario in your account and find its path | Graph queries, the path explained in plain English, the single change that breaks it | 5 h |
| 5 · Remediation by pull request | Fix five findings in Terraform/OpenTofu; add a drift job; auto-remediate public snapshots with Cloud Custodian in dry-run mode first | Merged PRs, drift alert evidence, dry-run log and the go/no-go decision | 5 h |
| 6 · Logging pipeline | Organisation trail (or equivalents) into a write-once log-archive bucket; ship to an open-source SIEM (Wazuh or Elastic) or a SIEM free tier | Architecture note, measured event-to-index delay (median and p95), monthly cost estimate, tamper test result | 5 h |
| 7 · Detection repository with CI | Ten Sigma (or native) rules with unit tests on recorded events; CI converts and deploys them; validate with Stratus Red Team techniques run in your sandbox | Repo, CI run, table of rule × emulated technique (fired / missed) with reasons for misses | 8 h |
| 8 · Identity hunts | Detect a role credential used outside its workload; build a key-age report; hunt admin activations without ticket references in a test Entra ID tenant | Queries, findings, rotation runbook | 4 h |
| 9 · Incident response game day | A partner plants a "leaked key" incident in your sandbox (announced exercise); you contain it, collect evidence and rebuild from code | Timeline, evidence bundle (log extract, snapshot IDs, hashes), containment duration, rebuild duration, 6-hour notification draft | 6 h |
| 10 · Workload and AI-service detections | Ingest Kubernetes control-plane audit logs; add detections for function permission changes and model invocations from unexpected principals | Four new tested rules, sample alerts | 4 h |

## Projects

### P1 · Posture baseline for a small organisation (L1, ~6 hours)

**Real-world inspiration.** CISA and NSA's March 2024 cloud information sheets and the CIS Foundations Benchmarks are the baseline that auditors and customers ask about first. Teams that pass audits still get breached through toxic combinations a checklist cannot see.

**What to build.** A repeatable posture assessment of your sandbox organisation: inventory, CIS scan, custom checks, and a prioritised report that a manager can act on.

**Acceptance criteria**
- One command (script or Makefile target) runs inventory and scan across all accounts and writes results to a dated folder.
- Inventory coverage ≥ 98% of resources with owner and environment tags, and the remaining resources listed by ID.
- The report contains a top-10 list where each item states exposure, identity, data affected and the fix; at least two items are combinations of individually "medium" findings.
- Every critical finding is either fixed by a PR or has a written exception with an owner and an expiry date.
- A second run after fixes shows the change in critical/high counts and the median age of open findings.

**Stretch goals.** Add a second cloud provider; publish the report as a static site generated from the scan data.

**What it proves to an employer.** You can turn a noisy scan into decisions, and you fix in code rather than by hand.

### P2 · Detection pack for cloud audit logs (L2, ~15 hours)

**Real-world inspiration.** The Snowflake customer intrusions (Mandiant, 2024) and the SSE-C ransom pattern AWS described in January 2025 were both visible in audit logs to teams that logged the right events and had detections ready.

**What to build.** A detection-as-code repository of at least 20 rules covering initial access, persistence, privilege escalation, defence evasion and exfiltration in the cloud control plane, with tests, CI deployment, and emulation-based validation.

**Acceptance criteria**
- At least 20 rules, each mapped to an ATT&CK technique, each with at least one true-positive and one benign test event; CI fails if any test fails.
- Validation: at least 12 rules confirmed firing on emulated techniques in your sandbox; every miss explained (log not enabled, field mismatch, rule logic).
- Over seven days of normal sandbox activity (scripted benign workload), the pack produces ≤ 5 false-positive alerts in total; each is tuned with an allow-list entry that has an expiry.
- Median time from event to alert is measured and reported, with the main source of delay identified.
- A silent-failure check alerts within 1 hour if any account stops sending audit logs.

**Stretch goals.** Rules for Azure and Google Cloud equivalents of five AWS rules; a coverage heat map generated from rule metadata.

**What it proves to an employer.** You can build detections the way software is built: tested, reviewed, deployed and measured.

### P3 · Cloud incident response kit and game day (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** The AWS Security Incident Response Guide and NIST SP 800-61 Rev. 3 describe preparation, containment and recovery; CERT-In's 6-hour reporting window and the DPDP Rules 2025 make timing a legal requirement in India. The scenario you exercise is illustrative and runs only in your own sandbox.

**What to build.** An incident response kit for your estate:
1. Runbooks (as code where possible) for leaked access key, hijacked role, public data exposure and SSE-C style re-encryption.
2. Automated containment actions (quarantine security group, session revocation for a role, key deactivation, snapshot and tag for evidence) behind a human approval step.
3. A timeline builder that turns audit-log extracts into a sorted, annotated timeline.
4. A blast-radius query over your Chapter 4 graph for any principal.
5. A one-hour game day run by a classmate with two injected scenarios.

**Acceptance criteria**
- Containment actions are idempotent, logged, and reversible; tests prove each action on a dummy resource.
- In the game day, both scenarios are contained within 30 minutes of the first alert; evidence bundle includes hashes of collected files and a chain-of-custody log.
- The blast-radius report lists every data store and role reachable from the compromised principal and matches a manual check on at least one scenario.
- The workload is rebuilt from IaC in under 60 minutes with no manual console steps.
- Deliverables include a 6-hour notification draft, a 72-hour report, and a blameless after-action review with at least five dated improvement actions.

**Stretch goals.** A read-only AI investigation assistant that drafts the timeline from logs, evaluated against your manual timelines (precision of claimed events, missed events), with injection tests using planted text in resource tags.

**What it proves to an employer.** You can lead a cloud incident under time pressure, preserve evidence, and recover from code. This is the core skill of cloud detection and response teams.

## Feeds into

- [OV01B Kubernetes and Container Security](../OV01B_kubernetes_and_container_security/README.md): the logging pipeline and detection repository receive Kubernetes audit and runtime alerts.
- The [OV01 capstone](../README.md): P2 and P3 become the detection and response parts of the capstone estate.
- [SEC501 Frontier Seminar: Threat Intelligence and Security Research](../../../03_majors/cybersecurity_defense/year_5/SEC501_frontier_seminar_threat_intelligence/README.md): emulation coverage data and incident timelines are research material.
- [THS501 Thesis or Capstone I](../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md): detection quality measurement and AI-assisted investigation are thesis-sized questions.
