# NET303 · Labs and projects

The lab is a Containerlab topology of free network operating systems (Nokia SR Linux, Arista cEOS, FRRouting; Juniper vJunos and Cisco images where you have legal access), plus Cisco DevNet always-on sandboxes for IOS XE and NX-OS APIs. Run everything on Linux or WSL2 with at least 16 GB of RAM. Automation code, data and pipelines live in one Git repository from week 1. Never point lab automation at a network you do not own.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Multi-vendor Containerlab and Git | Bring up a 6-node, 3-vendor topology from YAML; put it under Git | Topology file, README with bring-up steps | 3 h |
| 2 · Data, templates and validation | YAML data validated with Pydantic; Jinja2 templates for 3 vendors; tests that reject bad data | Templates, models, 10 passing and 5 deliberately failing test cases | 4 h |
| 3 · Netmiko audit and parsing | Compliance audit for 5 rules across all devices; output parsed with ntc-templates or Genie | JSON report; run time for 6 and for 60 simulated devices | 4 h |
| 4 · NAPALM and Nornir | Vendor-neutral facts report; full configuration replace with diff and rollback; stop-after-5%-failure rule | Diffs, rollback evidence, failure-injection results | 5 h |
| 5 · Ansible resource modules | Manage VLANs, interfaces and BGP neighbours with resource modules; idempotence test in CI | Playbooks and a CI log showing zero changes on the second run | 5 h |
| 6 · NETCONF transactions and RESTCONF | Candidate datastore change on 3 devices with all-or-nothing behaviour; confirmed commit that rolls back on timeout | ncclient scripts; captures of the RPCs; rollback proof | 6 h |
| 7 · gNMI telemetry pipeline | gnmic → Prometheus → Grafana for interface counters and BGP state; compare with 5-minute SNMP polling during a link flap | Dashboard JSON, detection-time comparison table | 5 h |
| 8 · NetBox source of truth and drift | Model the lab in NetBox; generate inventory and configurations from it; nightly drift report | NetBox export, rendered configs, drift report | 5 h |
| 9 · Batfish and pyATS testing | Batfish checks for reachability, ACLs and BGP sessions; pyATS before/after snapshots of a change | Test suite with at least 12 assertions; a diff report | 5 h |
| 10 · CI/CD with canary and rollback | Pipeline: lint, render, Batfish, deploy to twin, tests, approval, canary deploy, waves, automatic rollback on failed post-check | Pipeline file, run logs of one good and one deliberately bad change | 6 h |

## Projects

### P1 · Fleet compliance auditor (L1, ~6 hours)

**Real-world inspiration.** Indian regulators and auditors ask for evidence of basic controls: CERT-In's April 2022 directions require clock synchronisation to NIC or NPL time sources and log retention for 180 days, and most security baselines forbid Telnet and SNMPv1/v2c. Teams that audit by hand do it once a year; teams with a tool do it every night.

**What to build.** A Python command-line tool (Nornir or Netmiko) that checks every device against a YAML rule file: NTP servers present and synchronised, syslog destination set, SNMPv3 only, Telnet disabled, login banner present, AAA configured. It outputs JSON and a readable HTML or Markdown report, and returns a non-zero exit code when any rule fails.

**Acceptance criteria**
- Works on at least 3 platforms in the lab through one code path; adding a rule requires only YAML, no code change.
- Audits 60 simulated devices in under 2 minutes with concurrency, and reports unreachable devices separately from failed rules.
- Unit tests use recorded command output so the suite runs offline in under 30 seconds.
- No credentials are stored in the repository (checked with Gitleaks in CI).

**Stretch goals.** Add a `--fix` mode that generates (but does not apply) remediation configuration per device; trend results over time.

**What it proves to an employer.** You can turn a policy into an automated, repeatable check, which is the usual first automation a network team trusts.

### P2 · Source-of-truth-driven branch builder (L2, ~15 hours)

**Real-world inspiration.** Retail chains, banks and logistics companies in India open many similar branches; each one should get the same design with different addresses. The chain below (a pharmacy chain opening 40 stores, illustrative) is the scale where copy-and-paste starts to fail.

**What to build.** A workflow where adding a branch in NetBox (site, prefix, devices, circuits) generates complete configurations for the branch router and switch, validates them with Batfish, deploys them to a Containerlab twin with Ansible or Nornir, and runs post-checks (routing adjacency, DHCP scope reachable, internet path).

**Acceptance criteria**
- Creating a new branch from NetBox to verified working configuration in the twin takes under 10 minutes and no manual edits.
- Batfish confirms the new branch's prefixes do not overlap and that guest VLAN traffic cannot reach the corporate VLANs; a planted overlap is caught and blocks deployment.
- Running the deployment twice produces no changes on the second run.
- A drift report detects a manual change made on a deployed device within one nightly run.

**Stretch goals.** Decommission a branch from NetBox and prove all its routes and configuration are removed cleanly; add RESTCONF or NETCONF for at least one device type.

**What it proves to an employer.** You can make the network a function of data, the core skill of NetDevOps and the path from administrator to automation engineer.

### P3 · A network change pipeline with guarded AI assistance (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** AWS's October 2025 DynamoDB DNS incident (an automation race that applied an empty record) and Cloudflare's November 2025 outage (a generated file that grew past a limit) show what unguarded automation does. Cisco's February 2026 AgenticOps announcement describes agents that validate network changes against live topology and telemetry while "keeping teams firmly in control". This project builds that pattern openly, at small scale.

**What to build.** A complete pipeline for a 10–12 node multi-vendor network: NetBox as source of truth; templates; Batfish and template tests; deployment to a Containerlab twin; pyATS or custom post-checks; human approval; canary and wave deployment to the "production" lab with automatic halt and rollback; gNMI telemetry with change annotations on dashboards; a run lock to prevent concurrent pipelines; size and schema checks on every generated file. Add an AI assistant with read-only tools (NetBox query, Batfish query, read-only `show` commands) that can open a pull request but never deploy directly.

**Acceptance criteria**
- Across 20 scripted change requests (including 6 deliberately bad ones: overlapping prefix, ACL that blocks management, BGP policy that leaks routes, oversized generated file, concurrent run, wrong vendor syntax), the pipeline blocks all 6 bad changes before production and deploys all 14 good ones; change success rate in production is 100%.
- A post-check failure in the canary stage halts the rollout and rolls back within 60 seconds, shown in logs and telemetry.
- Mean time from approved pull request to verified production change is under 15 minutes.
- The AI assistant is evaluated on 20 tasks (diagnose a planted fault, propose a fix, write a test); the report states pass rate, failure types and every tool call it made; no assistant action reaches production without passing the same gates as a human change.
- A short threat model lists what the assistant's credentials can and cannot do.

**Stretch goals.** Add intent checks written as Batfish assertions ("no host in guest VRF reaches the server VRF") that run on every change; publish the pipeline as a reusable template with documentation.

**What it proves to an employer.** You can build the delivery system for network change, measure it, and integrate AI under guardrails, which is exactly the senior network automation role that the market is moving towards.

## Feeds into

- [NET403 AIOps and Intent-Based Networking](../../year_4/NET403_aiops_and_intent_based_networking/README.md): the telemetry pipeline, the twin and the guarded assistant become closed-loop automation.
- [NET401 Data Center and Hybrid Infrastructure](../../year_4/NET401_data_center_and_hybrid_infrastructure/README.md): EVPN fabrics are built from the same source of truth.
- [NET304 Wireless, SD-WAN and Enterprise Networks](../NET304_wireless_sd_wan_and_enterprise_networks/README.md): controller APIs for SD-WAN and Wi-Fi.
- [OPS305 Configuration Management and GitOps](../../../devops_sre_platform_engineering/year_3/OPS305_configuration_management_and_gitops/README.md) and the [OV03 DevSecOps](../../../../04_overlaps/OV03_devsecops/README.md) overlap.
- The major's [flagship industry project](../../../../06_career_and_market_readiness/05_industry_projects/NET_it_infrastructure_networking.md).
