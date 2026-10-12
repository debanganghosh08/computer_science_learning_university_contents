# SEC304 · Labs and projects

Use your own lab: Windows 11 and Windows Server evaluation VMs, an Ubuntu LTS VM and a RHEL-compatible VM (Rocky or AlmaLinux), plus the SIEM from SEC302. Take snapshots before every hardening change. When a lab asks you to generate suspicious-looking activity to test a detection, use benign test procedures (for example from the open-source Atomic Red Team library) **only inside the isolated lab**, and record exactly what you ran. Each submission includes configuration as code, before/after evidence and a short write-up with numbers.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Endpoint lab and baseline | Build the four VMs, enrol them in the SIEM, record a clean baseline (processes, services, autoruns, listening ports) | Build notes, baseline exports | 4 h |
| 2 · CIS scanning and hardening | Scan Windows and Linux with CIS-CAT Lite or OpenSCAP; apply 20 settings with GPO or Ansible; re-scan | Before/after scores, configuration code, two exceptions with owners and expiry | 5 h |
| 3 · Windows internals | Map a normal process tree; baseline persistence with Autoruns; enable Credential Guard, LSA protection, PowerShell logging and ASR rules in audit mode | Annotated baselines, verification screenshots, one week of ASR audit events reviewed | 6 h |
| 4 · Audit policy and Sysmon | Apply an advanced audit policy; deploy Sysmon with a tuned config; forward to the SIEM; alert on log clearing | Policy with justifications, events-per-hour measurement, alert test | 4 h |
| 5 · Linux hardening, auditd and Falco | Harden SSH and sudo; write 10 `auditd` rules; run Falco and AIDE; detect a change to `/etc/sudoers` | Rules mapped to questions, Lynis before/after, alert evidence | 6 h |
| 6 · EDR evaluation plan and Velociraptor | Write a 20-test EDR evaluation plan; deploy Velociraptor and run a fleet-wide query | Test plan with expected telemetry per test, query results | 4 h |
| 7 · Scanning and prioritisation | Authenticated scan of the lab; validate five findings by hand; prioritise 50 provided CVEs with CVSS 4.0, EPSS, KEV and SSVC | Validated findings, ranked list with reasoning, patch SLA table | 5 h |
| 8 · Application control | Build an App Control for Business policy in audit mode, review events, move one ring to enforcement; enable the vulnerable driver blocklist | Policy XML, event review, zero-break evidence for listed apps | 5 h |
| 9 · Encryption and restore | Enable BitLocker with escrowed keys and recover a VM; back up and restore a server; block unapproved USB storage | Recovery proof, restore time, device-control logs | 4 h |
| 10 · AI hardening test | Ask an AI assistant for 10 hardening changes for a named server role; test each in a ring; record which were wrong, outdated or harmful | Test log and an error classification | 3 h |

## Projects

### P1 · Hardened golden images (L1, ~6 hours)

**Real-world inspiration.** CIS Benchmarks and Microsoft security baselines are the common starting point for hardening in enterprises and in audits; RBI's 2026 directions for commercial banks require assessing information assets against recognised security standards.

**What to build.** Two "golden images" for an illustrative 200-person company: a Windows 11 laptop and an Ubuntu web server. Apply CIS Level 1 through code (GPO export or Intune policy JSON for Windows; Ansible for Linux), keep a deviation register, and produce a compliance report.

**Acceptance criteria**
- Automated scan shows at least 90% of applicable CIS Level 1 checks passing on both images; every failing check is in the deviation register with a reason, owner and review date.
- A provided test application (a browser-based app on the laptop; Nginx with TLS on the server) works after hardening, shown by a scripted smoke test.
- Rebuilding each image from code takes one command and under 30 minutes.

**Stretch goals.** Add drift detection that alerts when a hardened setting changes; add Level 2 settings for administrator laptops.

**What it proves to an employer.** You can harden systems reproducibly and explain every exception, which is what auditors and platform teams expect.

### P2 · Vulnerability prioritisation pipeline after the NVD change (L2, ~15 hours)

**Real-world inspiration.** In April 2026 NIST announced it would fully enrich only CVEs in CISA's KEV catalogue, used by the US federal government, or in critical software, moving older backlogged CVEs to "Not Scheduled". Mandiant's M-Trends 2026 puts the mean time to exploit at about −7 days. Teams therefore need their own prioritisation, combining exploitation evidence and asset context.

**What to build.** A pipeline that takes scanner output (OpenVAS or Nessus Essentials export from your lab plus a provided larger sample), joins it with an asset inventory (criticality, internet exposure, owner), the KEV catalogue and EPSS scores, applies an SSVC-style decision tree, and opens tickets (GitHub Issues or a CSV for a ticketing system) with due dates.

**Acceptance criteria**
- Daily refresh of KEV and EPSS data is automated and logged; the pipeline survives a missing EPSS score or CVSS vector without crashing.
- Every ticket shows why it got its priority (KEV status, EPSS value, exposure, criticality) in one line.
- On the provided sample, the pipeline's top 20 is compared with a CVSS-only top 20, and the write-up explains each difference.
- Unit tests cover the decision tree's branches.
- A one-page SLA policy states due dates per priority and the exception process.

**Stretch goals.** Track time-to-remediate per owner and chart it; add vendor advisory links automatically.

**What it proves to an employer.** You can run vulnerability management by risk, not by raw counts, and adapt when a public data source changes.

### P3 · Endpoint detection and resilience programme for a hospital group (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** The AIIMS Delhi ransomware attack (November 2022) disrupted hospital services for days. Volt Typhoon's living-off-the-land activity (CISA and partners, 2024) shows attackers relying on built-in tools that signatures miss. The July 2024 CrowdStrike content update showed that security software rollouts need the same care as any other change. The hospital group below is illustrative.

**What to build.** For a group with 3,000 Windows endpoints, 200 Linux servers and clinical systems that cannot be patched quickly, produce a programme and prove each part in the lab:
1. **Telemetry design:** audit policy, Sysmon and `auditd` configurations, collection architecture, storage estimate;
2. **Detections:** 12 behaviour detections for living-off-the-land patterns from CISA's 2024 guidance (for example unusual use of built-in remote management, scheduled task creation by unusual parents, credential-store access, log clearing, shadow copy deletion), each tested with a benign procedure in the lab;
3. **Prevention:** App Control for Business enforced on one ring, ASR rules enforced where audit data supports it, local admin removed;
4. **Resilience:** immutable or offline backup design, a timed restore of a server, BitLocker key recovery drill;
5. **Safe security updates:** a ring-based policy for EDR, signature and content updates with canaries, health checks and rollback;
6. **Unpatchable systems:** a risk acceptance and isolation design for two clinical devices.

**Acceptance criteria**
- All 12 detections fire on their lab tests and generate fewer than 10 alerts per day in total over two days of normal lab use; each has a documented false-positive scenario.
- The enforced App Control ring blocks an unapproved test executable and allows all listed business applications.
- Restore time for the test server is measured and compared with a stated recovery time objective.
- The update policy names ring sizes, soak times, the health signals that halt a rollout, and how rollback works if machines cannot boot.
- A three-page executive summary maps each control to the ransomware stage it breaks.

**Stretch goals.** Add macOS endpoints with an MDM baseline; score the programme against CIS Controls v8.1 Controls 4 (secure configuration), 7 (vulnerability management) and 10 (malware defenses).

**What it proves to an employer.** You can run endpoint security as an engineering programme that balances detection, prevention, recovery and operational safety, which is the core of senior endpoint and SOC engineering roles.

## Feeds into

- [SEC404 AI in Security Operations](../../year_4/SEC404_ai_in_security_operations/README.md): endpoint telemetry is the main input for AI triage and its verification.
- [SEC402 Digital Forensics and Incident Response](../../year_4/SEC402_digital_forensics_and_incident_response/README.md): triage collection, Windows and Linux artefacts, recovery.
- [SEC403 Malware Analysis for Defenders](../../year_4/SEC403_malware_analysis_for_defenders/README.md): behaviour you logged here is what dynamic analysis observes.
- [SEC401 Detection Engineering and Threat Hunting](../../year_4/SEC401_detection_engineering_and_threat_hunting/README.md): P3's detections move into detection-as-code.
