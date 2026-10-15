# NET302 · Labs and projects

Build everything in an isolated lab: Windows Server 2025 and Windows 11 evaluation images on Hyper-V, Proxmox VE or VirtualBox (32 GB of RAM is comfortable; 16 GB works with Server Core), plus a free Microsoft Entra ID tenant and time-limited trials for Intune and Entra ID P1. Never test hardening, restores or scripts against an employer's or college's real domain. Keep every script, GPO backup and runbook in Git.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Build the lab estate | Two-site forest (two DCs at HQ, one at a branch), a Server Core member, a Windows 11 client and an Ubuntu client, with snapshots | Diagram, build runbook, `dcdiag` output | 5 h |
| 2 · PowerShell remoting and JEA | Fan-out health checks to all servers; a JEA endpoint that allows only password resets for one OU | Scripts with Pester tests; transcript proving a JEA user cannot do anything else | 4 h |
| 3 · DNS and DHCP failover | AD-integrated zones, a conditional forwarder, scavenging; DHCP hot-standby failover | Evidence of leases continuing with one DHCP server off; 5 resolved DNS faults | 4 h |
| 4 · Sites, replication and FSMO | Configure sites and site links; measure replication latency; transfer and then seize FSMO roles after a simulated DC loss | Latency measurements, metadata cleanup evidence | 4 h |
| 5 · Delegation and service accounts | AGDLP access model for 3 shares; delegated reset rights; convert 2 services to gMSAs; audit OU create-child rights | Effective-access report, `dsacls` output | 4 h |
| 6 · Group Policy design | Apply the Microsoft security baseline in a test OU, loopback for a computer lab, GPOs backed up and diffed in Git | Predicted vs actual `gpresult` for 6 cases; change diff | 5 h |
| 7 · Hardening and assessment | Windows LAPS, Protected Users, RC4 inventory with events 4768/4769, LDAP and SMB signing; run PingCastle or Purple Knight before and after | Before/after scores and a list of fixes with risk notes | 5 h |
| 8 · Restore drills | Delete and restore an OU (Recycle Bin and authoritative restore); restore a file share from backup; time each | Timed restore log against stated RTOs | 4 h |
| 9 · Hybrid identity and Conditional Access | Cloud Sync or Connect Sync for one OU, password hash sync, 5 Conditional Access policies in report-only mode, a break-glass account with alerting | Sign-in log evidence for each policy decision | 5 h |
| 10 · Automation and AI script review | Build a file server with Ansible twice (idempotence); review 5 AI-drafted admin scripts with `-WhatIf` | Ansible run outputs; defect table with blast radius per defect | 4 h |

## Projects

### P1 · Joiner-mover-leaver automation (L1, ~6 hours)

**Real-world inspiration.** Service desks in large Indian IT services firms and their clients process a steady stream of new joiners, transfers and exits; leavers whose accounts stay active are a common audit finding. The company below is illustrative.

**What to build.** A PowerShell module that reads an HR CSV and creates, moves or disables users: correct OU, group memberships by role, home folder with the right permissions, a random initial password delivered out of band, and on exit: disable, remove from groups, hide from address lists, move to a leavers OU, and record evidence.

**Acceptance criteria**
- Pester tests cover all three paths and pass; every function supports `-WhatIf`.
- Processing a 200-row CSV twice produces no changes on the second run (idempotent).
- Every action is logged with who, what, when and the source row; a leaver's evidence report can be produced in under one minute.
- No credential appears in any file, log or Git history (checked with a secret scanner such as Gitleaks).

**Stretch goals.** Pull the HR data from a REST endpoint; add an approval step for privileged roles; sync the result to Entra ID and verify sign-in is blocked for leavers within 15 minutes.

**What it proves to an employer.** You can remove a repetitive, error-prone task safely and auditably, which is the quickest way for a junior administrator to earn trust.

### P2 · Hardened two-site domain with measured improvement (L2, ~15 hours)

**Real-world inspiration.** The government's reply on the 2022 AIIMS Delhi attack named improper network segmentation; Microsoft's 2026 Kerberos changes broke environments that had never inventoried RC4 use. Assessments with free tools are how many organisations start.

**What to build.** Take the lab domain with planted weaknesses (provided list: stale admin accounts, shared local admin password, RC4-only service account, unconstrained delegation on a server, credentials in a GPO preference, NTLMv1 allowed, no audit policy) and harden it: tiered admin groups and logon restrictions, Windows LAPS, Protected Users for admins, AES-only Kerberos after inventory, LDAP and SMB signing, advanced audit policy forwarded to one collector.

**Acceptance criteria**
- The assessment tool's risk score improves by at least 60% from the baseline, with every remaining finding explained or accepted in a risk register.
- Zero RC4 Kerberos tickets appear in events 4769 over a 24-hour test window after enforcement, and no service fails (shown by a service health check).
- A Tier 0 account cannot log on to a member server or workstation (tested), and every local admin password is unique and rotated.
- Group membership changes to privileged groups produce an alert on the collector within 2 minutes.

**Stretch goals.** Add a privileged access workstation with Credential Guard; write detection queries for the planted weaknesses if they reappear.

**What it proves to an employer.** You can improve an identity estate step by step without breaking it, with numbers that a manager or auditor can read.

### P3 · Hybrid identity estate with a recovery drill (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** The July 2024 CrowdStrike incident affected about 8.5 million Windows devices; recovery depended on access to BitLocker keys, out-of-band management and a clear restore order. Mid-sized organisations in India, such as a hospital group or a manufacturing company with plants and sales offices (illustrative), run exactly this mix of on-premises AD, Entra ID and Intune.

**What to build.** A complete small-enterprise estate as code where possible: two-site AD with DNS and DHCP failover, OU and delegation design, baseline GPOs in Git, hybrid identity with password hash sync, Conditional Access with phishing-resistant MFA for admins, Intune-managed clients with three update rings, file services on DFS, backups with an offline copy, and logging to a collector. Then write and run a recovery drill: the HQ domain controllers are lost and one file server is encrypted (simulated by deletion).

**Acceptance criteria**
- A design document (under 10 pages) covers forest, OU, delegation, tiering, hybrid identity, endpoint and backup decisions, each with an alternative considered.
- The estate can be rebuilt from your runbooks and Ansible/PowerShell code by a classmate in under 8 hours.
- In the drill, AD is restored from backup in an isolated network and service is back within your stated RTO (target 4 hours); the file share is restored within its RPO; krbtgt is reset twice following Microsoft guidance; the timeline is written.
- A staged update ring halts automatically (or by documented manual rule) when a pilot device reports failure, demonstrated with a simulated bad update.
- Every admin action in the drill is visible in the collected logs.

**Stretch goals.** Add a Linux server joined with SSSD and include it in the recovery; measure how long Entra ID sign-in keeps working with on-premises AD down under each authentication method.

**What it proves to an employer.** You can design, run and recover the identity and endpoint layer that a whole company depends on, which is the work that remains when routine administration is automated.

## Feeds into

- [NET402 Network Security Engineering](../../year_4/NET402_network_security_engineering/README.md): 802.1X with AD and certificates, segmentation and logging.
- [NET305 IT Service Management and Operations](../NET305_it_service_management_and_operations/README.md): P1 becomes a service request workflow; P3's drill becomes an incident and problem record.
- [NET404 Enterprise Architecture and Cloud Migration](../../year_4/NET404_enterprise_architecture_and_cloud_migration/README.md): identity is the first dependency of any migration.
- [SEC303 Identity and Access Management](../../../cybersecurity_defense/year_3/SEC303_identity_and_access_management/README.md) and the [OV01 Cloud Security](../../../../04_overlaps/OV01_cloud_security/README.md) overlap.
