# OPS302 · Labs and projects

All work runs on local virtual machines (VirtualBox, KVM/libvirt or Multipass): one Ubuntu 26.04 LTS guest and one RHEL-compatible 10.x guest (Rocky Linux or AlmaLinux). Take a snapshot before every lab so a mistake costs one minute. Labs 1, 4, 6 and 7 are done without AI assistance. Fault-injection scripts for drills are written by one student and solved by another.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Boot recovery | Recover from three planted faults: wrong root UUID in fstab, missing initramfs module, forgotten root password | Recovery log with the command sequence and why each step was needed | 4 h |
| 2 · Hardened units | Write a unit for a small web service with restart limits, `MemoryMax`, sandboxing and a timer for its cleanup job | Unit files, `systemd-analyze security` score below 3.0, crash-restart evidence | 4 h |
| 3 · Memory and OOM | Trigger a cgroup OOM and a global OOM; read PSI before each; tune `oom_score_adj` for a critical process | Evidence pack (kernel log, `memory.events`, PSI graph) and a one-page explanation | 4 h |
| 4 · Space mysteries | Solve four scenarios: deleted open file, inode exhaustion, files under a mount point, reserved blocks | Diagnosis notes with the proving command for each | 3 h |
| 5 · LVM and restore drill | Extend a mounted XFS volume online; snapshot a PostgreSQL volume; back up with restic; restore to a fresh VM | Commands, timed restore (target under 15 minutes), checksum proof | 5 h |
| 6 · Network faults | Fix five planted faults: wrong route, ndots delay, nftables drop, MTU black hole, expired certificate | `tcpdump` or `ss` evidence for each diagnosis | 5 h |
| 7 · USE checklist | Run USE and the 60-second checklist on three mystery workloads (CPU-bound, I/O-bound, lock contention) | Filled USE tables naming the bottleneck, with numbers | 3 h |
| 8 · Flame graphs and eBPF | Profile a slow service with `perf`; produce on-CPU and off-CPU flame graphs; find a fork storm with `execsnoop` | Flame graphs, the fix, before/after p99 | 5 h |
| 9 · CIS hardening | Bring both VMs to CIS Level 1 with OpenSCAP or Lynis; keep SELinux/AppArmor enforcing | Scan reports before and after, exception list with reasons | 5 h |
| 10 · Script clinic | Rewrite a fragile 150-line backup script to production standard | Script, ShellCheck clean report, bats tests, a demo of two concurrent runs | 4 h |

## Projects

### P1 · A production-grade service on one host (L1, ~6 hours)

**Real-world inspiration:** systemd's sandboxing and resource controls ([systemd.io](https://systemd.io/)) and the [Google Shell Style Guide](https://google.github.io/styleguide/shellguide.html) turn a "runs on my VM" service into something an on-call engineer can trust.

**What to build:** deploy a small HTTP service (any language) as a systemd service with socket activation, a dedicated user, sandboxing, resource limits, log rotation through journald, and a backup timer that calls your own script.

**Acceptance criteria:**
- **Exposure:** `systemd-analyze security` reports an exposure score of 3.0 or lower for the service.
- **Self-healing:** after `kill -9`, the service answers again within 5 seconds; a crash loop stops after 5 failures in 60 seconds and is visible in the journal.
- **Limits:** a memory leak mode is contained by `MemoryMax` without affecting other services (evidence from `memory.events`).
- **Script quality:** the backup script has zero ShellCheck warnings, at least 8 bats tests, and is safe to run twice concurrently (`flock`).
- **Idempotent install:** running your install script twice changes nothing the second time.

**Stretch goals:** a `Type=notify` service with a watchdog; the same service hardened under SELinux with a custom policy module.

**What it proves to an employer:** you can run a service properly on Linux without a platform hiding the details, which most cloud and SRE work assumes.

### P2 · Hardened, compliant three-VM fleet (L2, ~15 hours)

**Real-world inspiration:** the CERT-In directions of April 2022 require Indian organisations to sync clocks with NIC or NPL time servers and keep ICT logs for 180 days ([CERT-In](https://www.cert-in.org.in/PDF/CERT-In_Directions_70B_28.04.2022.pdf)). The xz backdoor ([CISA, 2024](https://www.cisa.gov/news-events/alerts/2024/03/29/reported-supply-chain-compromise-affecting-xz-utils-data-compression-library-cve-2024-3094)) showed why you need to know exactly which package versions run where.

**What to build:** three VMs (web, app, database) built from a golden image with cloud-init, hardened to CIS Level 1, with central log forwarding, time sync, automatic security updates with a canary host, an LVM layout with snapshot-based backups, and a package inventory you can query.

**Acceptance criteria:**
- **Compliance:** OpenSCAP CIS Level 1 pass rate of at least 90% on every VM, with each failure listed and justified.
- **Rebuild:** a VM is rebuilt from the image to a working state in under 20 minutes with no manual steps.
- **Time and logs:** clock offset under 100 ms on all hosts (chrony evidence); every host's auth and system logs arrive at the log host within 60 seconds; the retention configuration covers 180 days, with a storage estimate.
- **Restore:** the database is restored from backup to a new VM in under 15 minutes with data verified by checksum.
- **Inventory:** one command answers "which hosts run xz-utils version X?" in under 10 seconds.
- **Patch drill:** a security update reaches the canary host first, is verified, and then reaches the others one at a time.

**Stretch goals:** SSH certificates from a small CA instead of authorised keys; AIDE alerts forwarded to the log host.

**What it proves to an employer:** you can run a small, secure, auditable fleet the way regulated companies need it, and you can prove it with evidence.

### P3 · Break-fix gauntlet and a performance investigation (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** [SadServers](https://sadservers.com/) teaches troubleshooting with broken real machines; Netflix's [60-second checklist](https://netflixtechblog.com/linux-performance-analysis-in-60-000-milliseconds-accc10403c55) and Brendan Gregg's [USE method](https://www.brendangregg.com/usemethod.html) are the standard first response; LinkedIn's [School of SRE](https://github.com/linkedin/school-of-sre) publishes its training openly.

**What to build:** two linked deliverables.
1. **An open troubleshooting lab:** 12 reproducible fault scenarios (at least 4 "hard" ones: D-state storage hang, conntrack drops, intermittent DNS, OOM loop) with inject, verify and reset scripts, hints at three levels, and a written solution for each. It must run from one command on a fresh VM.
2. **A performance investigation report:** take a slow open-source service (or one you write) under load, and find and fix at least two bottlenecks with the USE method, `perf`, flame graphs and eBPF tools.

**Acceptance criteria:**
- **Reproducibility:** each scenario injects and resets cleanly 10 times in a row (automated check).
- **Peer test:** three classmates attempt the lab; at least 8 of 12 scenarios are solved within 20 minutes using at most one hint, and you record their times.
- **Your speed:** your own median time-to-diagnose across 12 unseen scenarios written by classmates is under 10 minutes.
- **Performance:** p99 latency at the same request rate improves by at least 30%, shown with before/after flame graphs, USE tables and load-test output.
- **Write-up:** the report reads like a public engineering blog post: symptom, method, dead ends, evidence, fix, and what you would monitor.

**Stretch goals:** publish the lab as an open-source repository with a CI job that tests every scenario; add Kubernetes-node scenarios (eviction, kubelet failure).

**What it proves to an employer:** you can debug Linux under pressure and teach others to do it. That is the bar for senior SRE and production engineering roles.

## Feeds into

- [OPS305 Configuration Management and GitOps](../OPS305_configuration_management_and_gitops/README.md): P2's hardening becomes an Ansible role and a Packer image.
- [OPS402 Chaos Engineering and Resilience](../../year_4/OPS402_chaos_engineering_and_resilience/README.md): fault injection builds on the P3 lab.
- [OPS404 Performance and Capacity Engineering](../../year_4/OPS404_performance_and_capacity_engineering/README.md): P3's investigation method scales up to fleets.
- [OV01B Kubernetes and Container Security](../../../../04_overlaps/OV01_cloud_security/OV01B_kubernetes_and_container_security/README.md): host hardening is its foundation.
