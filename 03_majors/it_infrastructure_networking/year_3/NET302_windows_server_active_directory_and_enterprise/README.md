# NET302 · Windows Server, Active Directory and Enterprise IT

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 5 | 4 (≈ 120 hours) | L1 → L3 | [CS204](../../../../02_year_2_core_computer_science/semester_3/CS204_computer_networks/README.md), [CS203](../../../../02_year_2_core_computer_science/semester_3/CS203_operating_systems/README.md) | [NET402](../../year_4/NET402_network_security_engineering/README.md); pairs with [SEC303](../../../cybersecurity_defense/year_3/SEC303_identity_and_access_management/README.md) and [NET305](../NET305_it_service_management_and_operations/README.md) |

## Why this course matters now

In most companies, identity is the network's real perimeter, and for most companies that identity still starts in Active Directory, now synchronised to Microsoft Entra ID in the cloud. When it fails, everything fails: on 19 July 2024 a faulty CrowdStrike update crashed about 8.5 million Windows devices, and recovery depended on people who could reach machines, find BitLocker recovery keys and restore servers in order. In November 2022, five servers at AIIMS Delhi were encrypted after attackers exploited what the government's reply in Parliament called improper network segmentation, and data came back from an unaffected backup server. The platform keeps changing under administrators' feet: Microsoft moved Kerberos away from RC4 encryption in phases through 2026 (audit from January, enforcement from April, rollback removed from July), and environments that never inventoried their old service accounts found out the hard way. AI now drafts PowerShell, Group Policy settings and Intune profiles quickly, and Microsoft builds Copilot experiences into its admin centres; the US Bureau of Labor Statistics expects system administrator jobs to shrink 4% from 2025 to 2035 as routine work is automated or outsourced. The work that stays valuable is identity design, delegation, hardening, recovery, and the judgement to know which AI-drafted change could lock out ten thousand users.

## Learning outcomes

By the end you can:

1. **Deploy** Windows Server 2025 (Server Core and Desktop Experience) and **manage** it remotely with PowerShell 7 and Windows Admin Center.
2. **Design** an Active Directory forest, OU structure, site topology and delegation model for a multi-site organisation, and **justify** it in writing.
3. **Operate** AD-integrated DNS and DHCP with failover, and **diagnose** replication, name-resolution and authentication failures from event logs and command output.
4. **Build** a Group Policy design with clear precedence, and **troubleshoot** why a setting does or does not apply.
5. **Harden** AD with a tiered administration model, Windows LAPS, Protected Users, AES-only Kerberos and reduced NTLM, and **measure** progress with a free assessment tool.
6. **Implement** hybrid identity with Entra Connect or Cloud Sync, Conditional Access and phishing-resistant MFA.
7. **Manage** Windows endpoints with Intune: Autopilot, compliance, update rings and staged rollout.
8. **Back up and restore** AD, file services and servers, including an authoritative restore and a documented forest-recovery plan, and **prove** recovery time in a drill.
9. **Automate** administration with tested, logged PowerShell, and **review** AI-generated scripts for destructive mistakes.

## Chapters and lessons

### Chapter 1 · Windows Server as a platform (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Editions and installation options | Standard vs Datacenter, Server Core vs Desktop Experience, why Core reduces patching and attack surface; 180-day evaluation media for labs | Install two Windows Server 2025 VMs (one Core) on Hyper-V, Proxmox or VirtualBox |
| 1.2 Roles, features and lifecycle | Server Manager vs `Install-WindowsFeature`; Microsoft's fixed lifecycle (Windows Server 2016 extended support ends in January 2027) | Inventory roles on a server with PowerShell; build a lifecycle table for a fictional estate |
| 1.3 Remote management | Windows Admin Center, WinRM, PowerShell remoting, PowerShell 7 over SSH | Manage the Core server only from the other VM |
| 1.4 The lab you will keep | One forest, two sites, a Windows 11 client, a Linux client; snapshots before every risky step | Build and document the lab; it is used all semester |

**Check your understanding:** Why does Server Core usually need fewer reboots? What does the end of extended support mean for a server that still "works"? Why should lab snapshots never replace a real backup strategy?

### Chapter 2 · PowerShell for administrators (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Objects and the pipeline | Cmdlets return objects, not text; `Select-Object`, `Where-Object`, `Group-Object`, calculated properties | Report the 10 largest folders on a share as CSV |
| 2.2 Remoting at scale | `Invoke-Command` fan-out, sessions, CIM over WinRM | Collect uptime and pending reboots from 5 servers in one command |
| 2.3 Safe scripting | `-WhatIf`, `-Confirm`, `SupportsShouldProcess`, `try/catch`, `Set-StrictMode`, logging with transcripts | Turn a one-liner into a function that supports `-WhatIf` |
| 2.4 Execution policy is not security | Execution policy vs script signing; Just Enough Administration (JEA) endpoints; script block logging | Build a JEA endpoint that lets help-desk staff only reset passwords |
| 2.5 Testing scripts | Pester tests, mocking AD cmdlets, running in a test OU first | Write Pester tests for a user-offboarding script |

**Check your understanding:** Why is parsing the text output of a command fragile, and how do objects fix that? What exactly does `-WhatIf` protect you from, and what does it not? Why is JEA safer than adding help-desk staff to Domain Admins "just for resets"?

### Chapter 3 · DNS and DHCP in a Windows estate (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 AD-integrated DNS | Zones stored in AD, secure dynamic updates, SRV records that clients use to find domain controllers | Break and repair a DC's SRV records; find DCs with `nltest /dsgetdc` |
| 3.2 Resolution design | Forwarders vs conditional forwarders, split-brain DNS, scavenging and aging | Add a conditional forwarder to a partner domain; clean stale records safely |
| 3.3 DHCP with failover | Scopes, reservations, options, load-balance vs hot-standby failover, DHCP relay from NET301 | Fail one DHCP server and keep leases flowing |
| 3.4 Troubleshooting names | `Resolve-DnsName`, `ipconfig /displaydns`, event logs, the "it's always DNS" checklist | Diagnose 5 name-resolution faults |

**Check your understanding:** Why does a domain join fail if the client uses a public DNS resolver? What can go wrong if scavenging is enabled without aging being understood? Why might hot-standby DHCP failover suit a branch better than load balancing?

### Chapter 4 · Active Directory Domain Services (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Logical structure | Forests, domains, trees, OUs, the schema; why most organisations need one forest | Draw the logical structure of your lab and of a 3-company merger |
| 4.2 Physical structure | Sites, subnets, site links, the KCC, replication intervals, global catalogs, read-only DCs for branches | Add a branch site; measure replication latency for a change |
| 4.3 Operations masters | The five FSMO roles, what breaks when each is down, seizing vs transferring | Transfer all roles; then simulate a dead DC and seize safely |
| 4.4 Time and Kerberos | PDC emulator time hierarchy, the 5-minute Kerberos skew limit, `w32tm` | Skew a client's clock and watch logons fail |
| 4.5 Health checks | `dcdiag`, `repadmin /replsummary`, SYSVOL replication with DFSR, functional levels | Write a daily health-check script with a pass/fail summary |

**Check your understanding:** Why does a missing subnet-to-site mapping make branch logons slow? Which FSMO role failure would users notice first, and which might go unnoticed for weeks? Why must the forest root PDC emulator use a reliable external time source?

### Chapter 5 · AD design and delegation (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 OU design | Design OUs for delegation and policy, not for the org chart | Redesign a "department per OU" tree into one that supports delegation |
| 5.2 Groups | Global, domain local and universal groups; the AGDLP pattern; nesting limits; access reviews | Grant access to a share using AGDLP; audit who really has access |
| 5.3 Delegation of control | Granular permissions on OUs, `dsacls`, avoiding broad "Full Control" | Delegate password resets for one OU only; prove it cannot be used elsewhere |
| 5.4 Service accounts | Group managed service accounts (gMSA), delegated managed service accounts (dMSA) in Windows Server 2025; Akamai's 2025 "BadSuccessor" research showed why the right to create objects in an OU must be audited | Convert a service from a password account to a gMSA; audit OU create-child rights |
| 5.5 Trusts and mergers | Forest and external trusts, selective authentication, SID filtering | Create a forest trust with selective authentication between two lab forests |

**Check your understanding:** Why does mirroring the org chart in OUs lead to messy Group Policy? Which delegated permission looks harmless but effectively grants control of the domain? Why is selective authentication a sensible default after a merger?

### Chapter 6 · Group Policy (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Processing | Local, site, domain, OU order; inheritance, block, enforced; computer vs user settings; refresh intervals | Predict the winning setting in 6 layered cases, then check with `gpresult /h` |
| 6.2 Targeting | Security filtering, WMI filters, item-level targeting in Preferences, loopback processing for kiosks and labs | Configure a computer-lab OU with loopback replace mode |
| 6.3 Administrative templates | ADMX central store, Microsoft security baselines, CIS Benchmarks as a reference | Import the Microsoft security baseline into a test OU and record what breaks |
| 6.4 Preferences and their traps | Drive maps, printers, registry items; never store passwords in preferences (the old cpassword problem) | Search SYSVOL for embedded credentials in a planted lab |
| 6.5 Troubleshooting and change | `gpresult`, RSoP, Group Policy operational logs; backing up and versioning GPOs | Back up all GPOs to Git with PowerShell; diff a change |

**Check your understanding:** A setting is linked at the domain with Enforced and blocked at an OU: which wins and why? Why can a WMI filter slow logons? Why should Group Policy changes go through the same change process as firewall changes?

### Chapter 7 · Securing Active Directory (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Tiered administration | Microsoft's enterprise access model, Tier 0 assets (DCs, AD CS, Entra Connect, backup servers), privileged access workstations | Map every Tier 0 asset in the lab and who can log on to it |
| 7.2 Credentials | Windows LAPS for local admin passwords, the Protected Users group, removing stale privileged accounts | Deploy Windows LAPS; rotate and retrieve a password with auditing |
| 7.3 Protocol hardening | AES-only Kerberos and the 2026 RC4 changes (find dependencies with events 4768 and 4769), NTLM reduction, LDAP signing and channel binding, SMB signing | Find and fix RC4 use in the lab before enforcing AES-only |
| 7.4 Assess and audit | Advanced audit policy, key event IDs (4624, 4625, 4720, 4728, 4768, 4769), free assessment tools such as PingCastle and Purple Knight (check licence terms) | Run an assessment; fix the top 5 findings; re-run and compare scores |
| 7.5 AD Certificate Services basics | What an enterprise CA does, why misconfigured certificate templates are a Tier 0 risk (concept only) | Inventory templates and who can enrol in each |

**Check your understanding:** Why is the server that runs Entra Connect a Tier 0 asset? Why does enforcing AES-only Kerberos without an inventory cause outages? What makes a privileged access workstation different from an ordinary admin laptop?

### Chapter 8 · File services and storage (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 SMB and permissions | SMB 3.x features (encryption, signing, multichannel), NTFS vs share permissions, access-based enumeration | Build a departmental share where effective permissions match a written policy |
| 8.2 DFS | DFS Namespaces for one path across servers; DFS Replication and its conflict behaviour | Move a share to a new server without changing users' paths |
| 8.3 Quotas, screening and versions | FSRM quotas and file screens, Volume Shadow Copies for user self-restore | Block executable files on a share; restore a deleted file from shadow copies |
| 8.4 Printing safely | Print servers, driver isolation, the PrintNightmare lesson (2021) and Point and Print restrictions | Lock down driver installation with policy; verify a user cannot add drivers |

**Check your understanding:** Why are share permissions usually set broadly while NTFS permissions do the real work? Why is DFS Replication a poor choice for files several users edit at the same time? Why did a print-spooler bug become a domain-wide risk?

### Chapter 9 · Backup, recovery and ransomware resilience (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Backup design | RPO and RTO, the 3-2-1 rule with an offline or immutable copy, separate credentials for backup systems | Write the backup policy for the lab with RPO/RTO per system |
| 9.2 Restoring AD | System state backups, the AD Recycle Bin, non-authoritative vs authoritative restore, DSRM | Delete an OU of 50 users; restore it two ways and time each |
| 9.3 Forest recovery | Microsoft's AD forest recovery guidance: isolated recovery network, first DC restore, metadata cleanup | Write and rehearse a forest-recovery runbook in an isolated lab network |
| 9.4 Lessons from incidents | AIIMS Delhi 2022 (poor segmentation, restored from an unaffected backup); CrowdStrike 2024 (BitLocker keys and out-of-band access) | For each incident, list three controls this course teaches that would have shortened recovery |

**Check your understanding:** Why is a backup you have never restored only a hope? Why must backup servers not be joined to the production domain with ordinary admin accounts? When is an authoritative restore required instead of a normal one?

### Chapter 10 · Hybrid identity with Microsoft Entra ID (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Synchronisation | Entra Connect Sync vs Entra Cloud Sync, source of authority, UPN suffix alignment, filtering | Sync one OU to a free Entra ID tenant; fix a UPN mismatch |
| 10.2 Authentication methods | Password hash sync, pass-through authentication, federation; why hash sync is a common resilient default | Write a one-page comparison with failure modes of each |
| 10.3 Conditional Access and MFA | Policies by user, app, device and risk; break-glass accounts; phishing-resistant methods (FIDO2 security keys, passkeys, Windows Hello for Business) | Design 5 Conditional Access policies and test them in report-only mode |
| 10.4 Licensing and limits | What Entra ID Free, P1 and P2 include; designing within a budget | Price a design for 500 users with Free vs P1 (use current public prices) |

**Check your understanding:** If the on-premises sync server dies, what keeps working under each authentication method? Why must break-glass accounts be excluded from some Conditional Access policies, and how do you watch them? Why is SMS-based MFA weaker than a passkey?

### Chapter 11 · Endpoint management and patching (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Join types | Entra join, hybrid join, workgroup; which identity a laptop uses where | Join one client each way; compare sign-in behaviour offline |
| 11.2 Intune basics | Windows Autopilot, configuration profiles, compliance policies, app deployment | Autopilot-provision a VM and push a compliance policy (trial tenant) |
| 11.3 Update rings | Windows Update for Business rings, deferrals, pilot groups; servers with Azure Update Manager or WSUS (deprecated, still in use) | Build 3 rings (pilot 5%, early 25%, broad) with a halt rule |
| 11.4 Staged rollout as a principle | The CrowdStrike lesson: any change pushed to every device at once is a single point of failure | Write a rollout standard: who approves, how big each ring is, what stops it |

**Check your understanding:** Why does a pilot ring only help if someone watches it and can stop the rollout? What does a compliance policy enforce, and what does Conditional Access do with the result? Why do servers usually need a different patch process from laptops?

### Chapter 12 · Automation, interoperability and operations (weeks 12–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Configuration as code for Windows | Ansible `ansible.windows` modules over WinRM, PowerShell DSC concepts, idempotence | Build a file server from scratch with Ansible; run it twice and show no changes the second time |
| 12.2 Joiner-mover-leaver | Automating onboarding and offboarding from an HR CSV, with approvals and logging | A tested offboarding script: disable, remove groups, move mailbox flag, record evidence |
| 12.3 Logging that helps | Windows Event Forwarding, Sysmon with a community configuration, shipping to a SIEM (see [SEC302](../../../cybersecurity_defense/year_3/SEC302_security_operations_soc_siem_and_monitoring/README.md)) | Forward logon and group-change events from all lab machines to one collector |
| 12.4 Linux in a Windows estate | Joining Linux to AD with `realmd` and SSSD; Samba as an open-source AD-compatible domain controller | Join an Ubuntu VM to the domain; log on with a domain account |
| 12.5 Reviewing AI-drafted admin scripts | Typical defects: missing `-WhatIf`, unscoped `Get-ADUser -Filter *` piped to a destructive cmdlet, plaintext credentials, wrong module | Review 5 AI-drafted scripts in a test OU; log each defect and its blast radius |

**Check your understanding:** Why is idempotence the property that makes configuration safe to re-run? What should an offboarding script record so an auditor can trust it? Which single line in an AI-drafted script would you look for first, and why?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Build the lab estate | Lab diagram and runbook |
| 2 | 2 | Lab 2 · PowerShell remoting and JEA | — |
| 3 | 3 | Lab 3 · DNS and DHCP failover | — |
| 4 | 4 | Lab 4 · Sites, replication and FSMO | **P1 due** |
| 5 | 5 | Lab 5 · Delegation and service accounts | — |
| 6 | 6 | Lab 6 · Group Policy design and troubleshooting | Mid-term practical (AI off) |
| 7 | 7 | Lab 7 · Hardening and assessment | Before/after assessment report |
| 8 | 8 | File services exercises | — |
| 9 | 9 | Lab 8 · Restore drills | **P2 due** |
| 10 | 10 | Lab 9 · Hybrid identity and Conditional Access | — |
| 11 | 11 | Intune and update rings exercises | Rollout standard |
| 12 | 12 | Lab 10 · Automation and AI script review | — |
| 13 | 12 | P3 | — |
| 14 | 12 | P3 recovery drill | **P3 due** |
| 15 | Review | Oral defence of P3 | Final practical exam (AI off) |

## Working with AI in this course

- **Use AI for:** first drafts of PowerShell functions and Pester tests; explaining an event ID or a `dcdiag` failure; summarising Microsoft documentation pages (then opening them); drafting user communications for a change. Microsoft Copilot experiences in Intune and the Entra admin centre, GitHub Copilot in VS Code, Claude and ChatGPT are all usable here.
- **Do without AI (drills):** predicting Group Policy results; reading replication and authentication errors; designing OU and delegation models; the restore drills; writing the offboarding script's core logic. The mid-term and final are AI-off.
- **Verify AI output by:** running every script with `-WhatIf` in a test OU first; checking each cmdlet and parameter in Microsoft Learn documentation; Pester tests; comparing `gpresult` output with the intended design; confirming any security setting against the Microsoft security baseline or CIS Benchmark text.
- **Where AI still fails here:** assistants mix cmdlets from the old MSOnline and AzureAD modules (retired) with Microsoft Graph PowerShell, invent parameters, and propose broad filters on destructive commands. Their knowledge also lags product changes such as the 2026 Kerberos RC4 enforcement. In Lab 10 you collect evidence: run 5 AI-drafted scripts against a test OU with `-WhatIf`, and record each defect, how you caught it, and how many objects it would have touched in production.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1–P3 | 35% |
| Mid-term practical (AI off) | 10% |
| Final practical exam (AI off) + P3 oral defence | 30% |

**Mastery gate.** You pass when you can, without AI: (1) build a two-site AD forest with DNS, DHCP failover, a delegated OU design and a baseline-hardened GPO set in 4 hours; (2) diagnose and fix 3 planted faults (for example, a broken SRV record, a blocked GPO, a replication failure) in 60 minutes with evidence; (3) restore a deleted OU authoritatively and bring a failed DC's roles back, meeting a stated RTO.

## Industry reality

Where this is used: almost every enterprise and public-sector body that runs Windows endpoints, including the large estates that Indian IT services firms manage for global clients under infrastructure-management contracts. The CrowdStrike incident (8.5 million devices, July 2024, per Microsoft) showed that endpoint fleets fail together; the AIIMS Delhi incident showed segmentation and backups decide recovery. Microsoft's own role certification for this work is now Microsoft Certified: Windows Server Administrator Associate (exam AZ-802).

**Interview questions from this course**

1. *Users at a branch take two minutes to log on. What do you check?* Strong answer: subnet-to-site mapping and which DC answers (`nltest`, `echo %LOGONSERVER%`), DNS settings, slow GPOs (WMI filters, drive maps), replication health, WAN latency; uses logs rather than guesses.
2. *Design AD and hybrid identity for a 5,000-person company with 20 branches.* Strong answer: single forest, OU design for delegation, sites and RODCs where justified, tiered admin, password hash sync with Conditional Access and phishing-resistant MFA, break-glass accounts, backup and forest-recovery plan.
3. *A GPO is linked but its setting does not apply to one computer. Walk through it.* Strong answer: `gpresult`, scope (OU, security filtering, WMI filter), computer vs user section, block/enforce, replication of SYSVOL, client event logs, loopback.
4. *Ransomware encrypted your file servers and you suspect a domain admin account. What are your first hours?* Strong answer: isolate, preserve evidence, involve incident response (and CERT-In reporting within 6 hours for Indian entities), assume Tier 0 compromise, recover from offline backups into a clean environment, reset krbtgt twice per Microsoft guidance, no paying for keys as a plan.
5. *How do you patch 3,000 laptops and 200 servers without causing an outage?* Strong answer: rings with pilot groups, monitoring and a halt rule, maintenance windows for servers, rollback plans, reporting compliance, and the CrowdStrike lesson about staged rollout.

## Resources (free first)

- **Microsoft Learn:** Windows Server documentation — https://learn.microsoft.com/en-us/windows-server/ ; AD DS — https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/active-directory-domain-services ; Microsoft Entra documentation — https://learn.microsoft.com/en-us/entra/ ; Intune — https://learn.microsoft.com/en-us/intune/ ; PowerShell — https://learn.microsoft.com/en-us/powershell/
- **Security guidance:** Detect and remediate RC4 usage in Kerberos — https://learn.microsoft.com/en-us/windows-server/security/kerberos/detect-remediate-rc4-kerberos ; Microsoft Security Compliance Toolkit (baselines) — https://learn.microsoft.com/en-us/windows/security/operating-system-security/device-management/windows-security-configuration-framework/security-compliance-toolkit-10 ; CIS Benchmarks (free PDFs with registration) — https://www.cisecurity.org/cis-benchmarks
- **Lab software:** Windows Server evaluation — https://www.microsoft.com/en-us/evalcenter/ ; Pester — https://pester.dev/ ; Ansible Windows guide — https://docs.ansible.com/ansible/latest/os_guide/windows.html ; Samba AD — https://wiki.samba.org/
- **Certification:** Microsoft Certified: Windows Server Administrator Associate (AZ-802) — https://learn.microsoft.com/en-us/credentials/certifications/windows-server-hybrid-administrator/
- **Paid, optional:** *Learn PowerShell in a Month of Lunches* (Manning); Microsoft Learn covers the same ground for free.

## Sources

- Microsoft, "Helping our customers through the CrowdStrike outage" (20 Jul 2024): 8.5 million Windows devices — https://blogs.microsoft.com/blog/2024/07/20/helping-our-customers-through-the-crowdstrike-outage/ (checked 2026-10)
- Microsoft Support, "How to manage Kerberos KDC usage of RC4 for service account ticket issuance changes related to CVE-2026-20833" (phases January, April and July 2026) — https://support.microsoft.com/en-us/topic/how-to-manage-kerberos-kdc-usage-of-rc4-for-service-account-ticket-issuance-changes-related-to-cve-2026-20833-1ebcda33-720a-4da8-93c1-b0496e1910dc (checked 2026-10)
- The Wire, government reply in Rajya Sabha on the AIIMS cyberattack (Dec 2022): five servers, about 1.3 TB encrypted, "improper network segmentation" — https://thewire.in/government/aiims-servers-cyberattack-ransomware-rajya-sabha (checked 2026-10)
- BLS Occupational Outlook Handbook, network and computer systems administrators (−4%, 2025–35) — https://www.bls.gov/ooh/computer-and-information-technology/network-and-computer-systems-administrators.htm (checked 2026-10)
- Microsoft Learn, Windows Server Administrator Associate certification page (exam AZ-802; updated Jan 2026) — https://learn.microsoft.com/en-us/credentials/certifications/windows-server-hybrid-administrator/ (checked 2026-10)
- Akamai Security Research, "BadSuccessor" dMSA research (May 2025) — https://www.akamai.com/blog/security-research/abusing-dmsa-for-privilege-escalation-in-active-directory (checked 2026-10)
- CERT-In Directions, 28 April 2022 (6-hour incident reporting) — https://www.cert-in.org.in/PDF/CERT-In_Directions_70B_28.04.2022.pdf (checked 2026-10)

_Last reviewed: 2026-10_
