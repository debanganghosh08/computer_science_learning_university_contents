# OPS302 · Linux Systems Administration in Depth

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 5 | 4 (≈ 120 hours) | L2 → L3 (P3 reaches L4) | [CS215](../../../../02_year_2_core_computer_science/semester_4/CS215_cloud_and_devops_foundations/README.md), [CS203](../../../../02_year_2_core_computer_science/semester_3/CS203_operating_systems/README.md) | [OPS402](../../year_4/OPS402_chaos_engineering_and_resilience/README.md), [OPS404](../../year_4/OPS404_performance_and_capacity_engineering/README.md), [OPS305](../OPS305_configuration_management_and_gitops/README.md) |

Part of the [DevOps, SRE and Platform Engineering major](../../README.md). [CS203](../../../../02_year_2_core_computer_science/semester_3/CS203_operating_systems/README.md) explained how the kernel works and [FND104](../../../../01_year_1_foundations/semester_1/FND104_the_developers_toolkit_linux_shell_git/README.md) taught the shell. This course makes you the person who keeps Linux machines healthy, secure and fast, and who finds the fault when the dashboard is red and nobody else can. Kubernetes node internals are in [CLD303](../../../cloud_engineering/year_3/CLD303_containers_and_kubernetes/README.md); this course is about the host underneath.

## Why this course matters now

Every container, Kubernetes node and cloud VM you will operate is a Linux process tree on a Linux kernel. The kernel reached 7.2 in August 2026, Ubuntu 26.04 LTS shipped in April 2026, RHEL 10 in May 2025 and Debian 13 in August 2025. The job title "system administrator" is shrinking: the US BLS projects a 4% decline from 2025 to 2035, as tasks move to DevOps-focused developers. The skill is not shrinking. The SRE hiring loop still opens with "a server is slow" or "DNS fails intermittently", and interviewers watch your method ([market map](../../../../06_career_and_market_readiness/01_market_map/roles/OPS_devops_sre_platform_engineering.md)).

Security incidents land on hosts. The xz utils backdoor (CVE-2024-3094, March 2024) was hidden in a compression library linked into OpenSSH on some distributions. The "regreSSHion" bug (CVE-2024-6387, July 2024) was a remote code execution race in OpenSSH's server.

AI assistants explain commands and draft scripts well, and agents can now run shell commands themselves. That makes a human who can read `/proc`, interpret `vmstat` and spot a dangerous `rm -rf "$DIR/"` with an empty variable more valuable, not less. The Linux Foundation's LFCS exam is two hours of hands-on tasks at a live command line, with no assistant.

## Learning outcomes

By the end you can:

1. **Recover** a machine that does not boot (bootloader, initramfs, fstab, root password) using rescue and emergency targets.
2. **Write** systemd units with correct dependencies, restart policies, resource limits and sandboxing, and **score** them with `systemd-analyze security`.
3. **Diagnose** process, memory and I/O problems using `/proc`, PSI, cgroup v2 statistics and the OOM killer's log.
4. **Operate** storage: partitioning, ext4/XFS choices, LVM online resize and snapshots, software RAID replacement, and tested backup and restore.
5. **Debug** host networking (routes, DNS resolution path, nftables, conntrack, MTU, TLS) with `ip`, `ss`, `tcpdump` and `openssl`.
6. **Apply** the USE method and Netflix's 60-second checklist, then **go deeper** with `perf`, flame graphs and eBPF tools.
7. **Harden** a host to CIS Level 1 (SSH, sudo, SELinux or AppArmor, auditd, patching) and **prove** it with OpenSCAP or Lynis.
8. **Write** shell scripts to production standard: quoted, idempotent, locked, logged, linted with ShellCheck and tested with bats.
9. **Solve** unseen break-fix scenarios at LFCS speed with a written, repeatable method.

## Chapters and lessons

### Chapter 1 · From power-on to login (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Boot chain | UEFI, GRUB 2 or systemd-boot, kernel command line, initramfs, PID 1 | Trace a boot with `journalctl -b` and `systemd-analyze critical-chain` |
| 1.2 Rescue and emergency modes | `rescue.target` vs `emergency.target`, `rd.break`, `init=/bin/bash`; read-only root | Recover a lost root password on Ubuntu and on a RHEL-family VM |
| 1.3 Broken fstab and modules | UUIDs vs device names, `nofail`, `x-systemd.device-timeout`, module blacklisting | Boot a VM whose fstab names a missing disk; fix it |
| 1.4 Kernel parameters | `sysctl`, `/proc/sys`, persistent config, kernel live patching overview | Change `vm.swappiness` persistently and justify it with evidence |

**Check your understanding:** (1) Why does a typo in `/etc/fstab` stop a boot, and which option prevents it for a data disk? (2) What runs before the real root filesystem is mounted? (3) Why is changing a sysctl without measurement a bad habit?

### Chapter 2 · systemd in depth (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Units and dependencies | `Wants`/`Requires`/`BindsTo` vs `After`/`Before`; targets; drop-in overrides | Fix a service that starts before its network is ready |
| 2.2 Service lifecycle | `Type=simple/notify/oneshot`, `Restart=`, `StartLimitBurst`, watchdogs, graceful stop | Make a crashing service restart, then stop restart loops |
| 2.3 Timers and socket activation | Timers vs cron (missed runs, randomized delay), socket-activated services | Replace a cron job with a timer that survives reboots |
| 2.4 Resource control | cgroup v2 via `MemoryMax`, `CPUQuota`, `IOWeight`; slices | Contain a memory hog without touching its code |
| 2.5 Sandboxing | `ProtectSystem`, `PrivateTmp`, `NoNewPrivileges`, `CapabilityBoundingSet`, `systemd-analyze security` | Reduce a unit's exposure score below 3.0 |

**Check your understanding:** (1) What is the difference between ordering and requirement dependencies? (2) Why can `Restart=always` hide a real fault? (3) Which sandboxing option would have limited damage from a compromised web service writing to `/etc`?

### Chapter 3 · Processes, signals and memory (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Process states | R, S, D, Z, T; `/proc/<pid>/` (status, stack, fd, limits) | Create a zombie and a D-state process; explain each |
| 3.2 Signals and shutdown | SIGTERM vs SIGKILL, PID 1 in containers (no default signal handlers), `tini` | Fix a container that takes 30 s to stop |
| 3.3 Memory | Page cache, anonymous memory, overcommit, swap and zram, `free` misread | Show why "free memory" near zero is often healthy |
| 3.4 OOM and pressure | OOM killer scoring, `oom_score_adj`, cgroup OOM vs global OOM; PSI (`/proc/pressure/*`) | Trigger both OOM types and read the evidence for each |
| 3.5 Limits | `ulimit`, `LimitNOFILE`, file-descriptor exhaustion | Reproduce "too many open files" and fix it at the right layer |

**Check your understanding:** (1) Why does load average rise when CPU is idle? (2) What tells you whether an OOM kill came from a cgroup limit or from the whole host? (3) Why does a process ignore SIGTERM when it runs as PID 1 in a container?

### Chapter 4 · Filesystems (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Block devices and partitions | GPT, `lsblk`, `blkid`, alignment, NVMe naming | Partition and format a new disk safely |
| 4.2 Choosing a filesystem | ext4 vs XFS (cannot shrink) vs Btrfs; mount options (`noatime`, `discard`) | Write a one-paragraph choice for a database, a log volume and a build cache |
| 4.3 Space and inodes | `df` vs `du` gaps, deleted-but-open files (`lsof +L1`), inode exhaustion | Solve "disk full but `du` says 40% used" |
| 4.4 Integrity and repair | `fsck`, `xfs_repair`, journaling, read-only remounts after errors | Repair a corrupted image in a loop device |

**Check your understanding:** (1) Why can deleting a log file not free space? (2) When is XFS the wrong choice? (3) What does a kernel remounting a filesystem read-only tell you?

### Chapter 5 · LVM, RAID and backups (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 LVM | PVs, VGs, LVs; online extend; thin pools and their over-commit risk | Grow a mounted filesystem with no downtime |
| 5.2 Snapshots | LVM snapshots for consistent backups; copy-on-write cost | Snapshot a database volume, back it up, measure the write penalty |
| 5.3 Software RAID | `mdadm` RAID 1/5/6/10, rebuild time, write hole, monitoring; RAID is not a backup | Fail and replace a disk in a RAID 1 |
| 5.4 Backups that restore | 3-2-1, restic or BorgBackup, encryption, retention, restore drills with timed RTO | Restore a server's data to a new VM and time it |
| 5.5 Network storage clients | NFS mount options (`hard` vs `soft`), iSCSI basics, stale handles | Recover a host hung on an unreachable NFS mount |

**Check your understanding:** (1) Why is a backup that has never been restored not a backup? (2) What does a thin pool hitting 100% do to every volume in it? (3) Why might a RAID 5 rebuild fail on large disks?

### Chapter 6 · Host networking (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Interfaces and routes | `ip addr/route/rule`, bonding, bridges, VLANs; netplan and NetworkManager | Add a second route table for a second NIC |
| 6.2 Name resolution | `nsswitch.conf`, `/etc/hosts`, systemd-resolved, `ndots` and search domains in Kubernetes | Explain a 5-second DNS delay from `ndots:5` and fix it |
| 6.3 Firewalls and conntrack | nftables tables/chains/sets; conntrack table limits and drops | Fill the conntrack table and read the kernel message |
| 6.4 Packets and MTU | `tcpdump` filters, Wireshark, MTU/PMTUD black holes, TCP retransmits (`ss -ti`) | Diagnose a connection that hangs only for large responses |
| 6.5 TLS on the wire | `openssl s_client`, certificate chains, SNI, expiry checks, `curl -w` timing breakdown | Find which hop adds 300 ms to an HTTPS call |

**Check your understanding:** (1) Small requests work, large ones hang: what do you suspect and how do you prove it? (2) Why can DNS look "intermittent" under load? (3) What does a full conntrack table look like from the application's side?

### Chapter 7 · Performance methodology (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 The USE method | Utilization, saturation, errors for every resource; a checklist instead of guessing | Fill a USE table for a loaded VM |
| 7.2 The 60-second analysis | `uptime`, `dmesg`, `vmstat`, `mpstat`, `pidstat`, `iostat -xz`, `free`, `sar -n DEV,TCP,ETCP`, `top` | Run the checklist on 3 mystery workloads; name the bottleneck |
| 7.3 Virtualization effects | CPU steal, noisy neighbours, burstable instance credits | Show steal time on a throttled VM |
| 7.4 Saturation signals | Run-queue length, PSI, I/O queue depth, `await` | Tell CPU saturation from I/O saturation using PSI alone |

**Check your understanding:** (1) Why does 100% utilization not always mean saturation? (2) What would you check first when only p99 latency is bad? (3) How does CPU steal mislead application profiling?

### Chapter 8 · Deep performance tools (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 `perf` and flame graphs | Sampling, symbols, CPU flame graphs, off-CPU analysis | Find the hot function in a slow service and fix it |
| 8.2 eBPF tools | BCC tools (`execsnoop`, `opensnoop`, `biolatency`, `tcpretrans`), bpftrace one-liners | Find a process spawning thousands of short-lived children |
| 8.3 System call tracing | `strace` and its overhead; `ltrace`; when to prefer eBPF | Measure strace's slowdown on a busy process |
| 8.4 Scheduling and tuning | CFS/EEVDF basics, `nice`, CPU affinity, `sched_ext` (merged in Linux 6.12) as a research direction | Pin a latency-sensitive process and measure p99 |

**Check your understanding:** (1) Why can strace be unsafe on a production database? (2) What does an off-CPU flame graph show that an on-CPU one hides? (3) What evidence would justify changing a scheduler setting?

### Chapter 9 · Security hardening (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Accounts and privilege | Users, groups, `sudoers` with least privilege, PAM basics, service accounts | Write sudo rules that allow restarting one service only |
| 9.2 SSH | Key-only login, no root login, SSH certificates, `AllowGroups`, fail2ban limits; regreSSHion case | Move a host to SSH certificates signed by a CA |
| 9.3 Mandatory access control | SELinux (RHEL family) and AppArmor (Ubuntu): modes, contexts, profiles; reading denials with `ausearch`/`audit2why` | Fix a web server blocked by SELinux without disabling it |
| 9.4 Audit and integrity | auditd rules, AIDE file integrity, journald forwarding | Detect and report a change to `/etc/passwd` |
| 9.5 Benchmarks and patching | CIS Benchmarks, OpenSCAP and Lynis scans, unattended upgrades, live patching, reboot policy; xz backdoor timeline | Raise a host's OpenSCAP CIS Level 1 score above 90% with documented exceptions |

**Check your understanding:** (1) Why is `setenforce 0` an incident, not a fix? (2) What would have limited the xz backdoor's impact on a hardened host? (3) Why do you need a reboot policy even with live patching?

### Chapter 10 · Packages, images and fleets (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Package management | apt and dnf internals, repository signing keys, pinning and holds, local mirrors | Pin a package and survive an upstream bad release |
| 10.2 Lifecycles | LTS and support windows (Ubuntu LTS, RHEL, Debian), end-of-life planning | Build an EOL calendar for a 20-host fleet |
| 10.3 Golden images | cloud-init, image builds (Packer), versioned images, CIS-hardened bases | Build an image that boots hardened with no manual steps |
| 10.4 Fleet operations | Rolling reboots, kernel upgrades, canary hosts, maintenance windows | Upgrade the kernel on 5 VMs one at a time with health checks |

**Check your understanding:** (1) Why are repository signing keys a supply-chain control? (2) What breaks when half a fleet runs a different kernel? (3) Why patch a canary host first?

### Chapter 11 · Shell scripting to production standard (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Safe Bash | Quoting, arrays, `set -euo pipefail` and its traps, `[[ ]]`, `${var:?}` | Fix 10 planted bugs that would delete the wrong files |
| 11.2 Robust scripts | `trap` cleanup, `flock` locking, idempotency, exit codes, logging to journald | Make a backup script safe to run twice at once |
| 11.3 Quality tools | ShellCheck, `shfmt`, bats tests, Google Shell Style Guide | Reach zero ShellCheck warnings and 90% branch coverage with bats |
| 11.4 When to stop using Bash | Size and complexity limits; Python or Go for automation with real error handling | Port a 200-line script to Python and compare failure handling |

**Check your understanding:** (1) Why can `set -e` fail to stop a script? (2) What makes an operational script idempotent? (3) At what point should a script become a program?

### Chapter 12 · Troubleshooting drills (weeks 12–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 A repeatable method | Symptom, scope, recent changes, hypotheses ranked by likelihood and cost to test, bisect by layer, write as you go | Write your method on one page; use it in every drill |
| 12.2 Classic failures | Disk full, inode exhaustion, wrong permissions, expired certificate, clock skew (chrony; CERT-In requires syncing to NIC or NPL time servers), port conflicts | 10 timed drills at 15 minutes each |
| 12.3 Hard failures | D-state hangs on storage, intermittent DNS, conntrack drops, OOM loops, kernel soft lockups | 5 timed drills at 30 minutes each |
| 12.4 Hosts under Kubernetes | kubelet and containerd logs, node-pressure eviction, cgroup v2 limits seen from the host | Explain a pod eviction from the node's point of view |
| 12.5 AI as a second opinion | Using an assistant to suggest hypotheses without letting it run commands; checking each claim | Solve 3 drills with AI suggestions only; log wrong suggestions |

**Check your understanding:** (1) Why write hypotheses down before running commands? (2) A drill was solved by rebooting. Why is that not a pass? (3) What do you check first when "nothing changed" but something broke?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Boot recovery | Recovery log |
| 2 | 2 | Lab 2 · Hardened units | Unit files + security scores; P1 starts |
| 3 | 3 | Lab 3 · Memory and OOM | Evidence pack |
| 4 | 4 | Lab 4 · Space mysteries | **P1 due** |
| 5 | 5 | Lab 5 · LVM and restore drill | Timed restore |
| 6 | 6 | Lab 6 · Network faults | Debug logs |
| 7 | 7 | Lab 7 · USE checklist | USE tables; mid-term (AI off) |
| 8 | 8 | Lab 8 · Flame graphs and eBPF | Before/after profile |
| 9 | 9 | Lab 9 · CIS hardening | Scan reports |
| 10 | 10 | Golden image | **P2 due** |
| 11 | 11 | Lab 10 · Script clinic | ShellCheck and bats reports |
| 12 | 12 | Drill block A | Drill times |
| 13 | 12 | Drill block B | Drill times |
| 14 | 12 | P3 hand-in and peer testing | **P3 due** |
| 15 | Review | LFCS-style practical (2 h) and oral | Final |

## Working with AI in this course

- **Use AI for:** explaining unfamiliar commands, man-page options and kernel messages; drafting systemd units, nftables rulesets and bats tests; turning your drill notes into a runbook. Named tools: Claude, ChatGPT, Gemini in chat; Claude Code, GitHub Copilot or Warp in the terminal.
- **Do without AI (drills):** every timed drill in Chapter 12, boot recovery, the USE checklist, reading SELinux denials, the mid-term and the final practical. LFCS and RHCSA-style exams allow no assistant, and neither does a 3 a.m. outage with a broken laptop.
- **Verify AI output by:** running scripts first in a disposable VM or container; ShellCheck and bats on every script; `systemd-analyze verify` and `systemd-analyze security` on units; `nft -c -f` before loading rules; `visudo -c` before saving sudoers; keeping a second SSH session open whenever you change SSH or firewall settings.
- **Where AI still fails here (show it):** ask an assistant to "free disk space on a full server" and check whether it suggests deleting logs that are still open (space not freed) or running destructive commands without a dry run. Ask for an SELinux fix and count how often it proposes `setenforce 0`. Never let an agent run commands on a host you care about without a sandbox and an allow-list; you will see why in [OPS403](../../year_4/OPS403_aiops_and_agentic_operations/README.md).

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs 1–10 | 25% |
| Projects P1 / P2 / P3 | 5% / 15% / 20% |
| Drill record (Chapter 12, timed) | 10% |
| Mid-term (AI off) | 5% |
| Final practical (2 hours, AI off) + oral | 20% |

**Mastery gate.** You pass when you can, without AI help: (1) complete an LFCS-style practical of 20 tasks in 2 hours with at least 75% correct (the real exam is also 2 hours and performance-based); (2) diagnose 4 of 5 unseen break-fix scenarios within 20 minutes each, stating the evidence for each diagnosis; (3) take a stock VM to a CIS Level 1 OpenSCAP score above 90% in 90 minutes, with every exception justified in writing.

## Industry reality

Linux depth is what separates an operations engineer from someone who only edits YAML. Netflix published its "Linux Performance Analysis in 60,000 Milliseconds" checklist, which many SRE teams still use as a first response. LinkedIn's free School of SRE starts with Linux and networking fundamentals. In India, the CERT-In directions of April 2022 require ICT systems to synchronise clocks with NIC or NPL time servers and to keep logs for 180 days, which turns time sync and log forwarding from good practice into a compliance duty. Hands-on certifications (LFCS, RHCSA) test exactly this course's material.

**Interview questions from this course**

1. *A server is slow. Walk me through your first five minutes.* Strong answer: clarifies symptom and scope; checks recent changes; runs the 60-second checklist (load, dmesg, vmstat, mpstat, pidstat, iostat, free, sar); uses USE per resource; separates CPU, memory, disk and network saturation; states what each number would mean.
2. *`df` says the disk is full but `du` adds up to half. Why?* Strong answer: deleted-but-open files (`lsof +L1`), files hidden under a mount point, reserved blocks, filesystem metadata; the safe fix (restart or truncate via `/proc/<pid>/fd`), and prevention (log rotation with copytruncate or signals).
3. *DNS resolution fails intermittently on some hosts.* Strong answer: walks the resolution path (nsswitch, resolved, resolv.conf, search and ndots); UDP drops, conntrack exhaustion, upstream rate limits, IPv6 AAAA timeouts; proves the cause with `tcpdump` and timing; proposes caching and monitoring.
4. *How do you harden a new Linux server before it goes on the internet?* Strong answer: minimal packages, patched image, key-only SSH with no root, least-privilege sudo, firewall default deny, SELinux/AppArmor enforcing, auditd, log forwarding, time sync, automatic security updates, a CIS scan with exceptions documented.
5. *What happens when a container exceeds its memory limit?* Strong answer: cgroup v2 `memory.max`, reclaim then cgroup OOM kill of a process in that cgroup, exit code 137, how this differs from host OOM; how to see it (`memory.events`, kernel log, `kubectl describe`); right-sizing and PSI-based alerting.

## Resources (free first)

- **Texts:** William Shotts, [*The Linux Command Line*](https://linuxcommand.org/tlcl.php) (free PDF); Brendan Gregg's [USE method](https://www.brendangregg.com/usemethod.html), [Linux performance](https://www.brendangregg.com/linuxperf.html) and [flame graphs](https://www.brendangregg.com/flamegraphs.html) pages; Netflix, [Linux Performance Analysis in 60,000 Milliseconds](https://netflixtechblog.com/linux-performance-analysis-in-60-000-milliseconds-accc10403c55); [School of SRE](https://github.com/linkedin/school-of-sre) (LinkedIn).
- **Documentation:** [systemd](https://systemd.io/) and its man pages; [kernel cgroup v2](https://docs.kernel.org/admin-guide/cgroup-v2.html); [kernel documentation](https://www.kernel.org/doc/html/latest/); [Ubuntu Server docs](https://ubuntu.com/server/docs); [Arch Wiki LVM](https://wiki.archlinux.org/title/LVM) (distribution-neutral and excellent); [BCC tutorial](https://github.com/iovisor/bcc/blob/master/docs/tutorial.md); [bpftrace](https://bpftrace.org/).
- **Security:** [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks) (free PDFs after registration), [OpenSCAP](https://www.open-scap.org/), [Lynis](https://cisofy.com/lynis/).
- **Scripting:** [ShellCheck](https://www.shellcheck.net/), [Google Shell Style Guide](https://google.github.io/styleguide/shellguide.html), [Bash Guide (Greg's wiki)](https://mywiki.wooledge.org/BashGuide).
- **Practice:** [SadServers](https://sadservers.com/) (troubleshooting scenarios on real VMs), [OverTheWire Bandit](https://overthewire.org/wargames/bandit/), [Linux Upskill Challenge](https://linuxupskillchallenge.org/), [Killercoda](https://killercoda.com/); local VMs with VirtualBox, KVM or Multipass, one Ubuntu 26.04 and one RHEL-compatible 10.x guest.
- **Certification:** [LFCS](https://training.linuxfoundation.org/certification/linux-foundation-certified-sysadmin-lfcs/) (Linux Foundation, 2 hours, performance-based).
- **Paid, worth it:** Brendan Gregg, *Systems Performance*, 2nd ed. (2020) and *BPF Performance Tools* (2019).

## Sources

All checked 12 Oct 2026.
- Release dates from [endoflife.date](https://endoflife.date/): Linux 7.2 (16 Aug 2026), Ubuntu 26.04 LTS (23 Apr 2026), RHEL 10 (20 May 2025), Debian 13 (9 Aug 2025).
- US BLS, [Network and Computer Systems Administrators](https://www.bls.gov/ooh/computer-and-information-technology/network-and-computer-systems-administrators.htm) (−4%, 2025–35).
- CISA, [xz utils CVE-2024-3094](https://www.cisa.gov/news-events/alerts/2024/03/29/reported-supply-chain-compromise-affecting-xz-utils-data-compression-library-cve-2024-3094) (29 Mar 2024); Qualys, [regreSSHion CVE-2024-6387](https://www.qualys.com/2024/07/01/cve-2024-6387/regresshion.txt) (1 Jul 2024).
- Linux Foundation, [LFCS exam page](https://training.linuxfoundation.org/certification/linux-foundation-certified-sysadmin-lfcs/) (online, proctored, performance-based, 2 hours; domains include essential commands, operations deployment, users and groups, networking, storage).
- [CERT-In Directions, 28 Apr 2022](https://www.cert-in.org.in/PDF/CERT-In_Directions_70B_28.04.2022.pdf) (NTP sync to NIC/NPL; 180-day log retention).

_Last reviewed: 2026-10_
