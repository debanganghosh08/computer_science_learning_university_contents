# NET301 · Labs and projects

Everything runs on free emulators on your own machine: Containerlab with FRRouting, Nokia SR Linux or Arista cEOS (free container images), Cisco Packet Tracer or Cisco Modeling Labs Free (5 running nodes), or GNS3. A laptop with 16 GB of RAM runs every lab below; P3 fits within the CML-Free node limit if you use FRRouting containers for the simulated ISPs. Never connect lab routers to a production network or announce lab prefixes to the internet.

Every lab submission includes the topology file, final configurations, and before/after evidence (`show` output or captures) in a Git repository.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Lab platform and three CLIs | Build the same 3-router OSPF triangle in Containerlab (FRR) and in Packet Tracer or CML; make one change on IOS, Junos-style and EOS syntax and roll it back | Topology files, a table comparing commit and rollback on each platform | 3 h |
| 2 · Addressing plan and overlap checker | IPv4 and IPv6 plan for a 5-site organisation; Python script that rejects overlaps and prints per-site summaries | Plan (CSV), script with tests, summary output | 3 h |
| 3 · VLANs and trunks | 4 VLANs across 3 switches with an SVI gateway; a deliberate native-VLAN mismatch to find and fix | Reachability matrix, captures showing 802.1Q tags | 4 h |
| 4 · Spanning tree prediction | Predict root and port roles for 4 topologies, then verify; enable BPDU Guard and Root Guard and trigger each with a "rogue switch" | Predictions vs actual, logs of each guard firing | 4 h |
| 5 · LACP and gateway failover | LACP bundle, VRRP pair, object tracking and BFD; measure packet loss during failures with 10 ms probes | Loss table for 6 failure types, before and after tuning | 5 h |
| 6 · Multi-area OSPF | Three areas including an NSSA; summarisation at ABRs; OSPFv3 in parallel | LSA counts per area before and after summarisation; annotated database | 5 h |
| 7 · OSPF fault hunt and convergence | Ten adjacency and routing faults (MTU, timers, area, authentication, passive interface, redistribution loop); time each convergence phase | Fault log with method and evidence; convergence breakdown | 5 h |
| 8 · BGP dual-homed edge | eBGP to two simulated ISPs, inbound and outbound policy, max-prefix, RPKI validation with Routinator | Policy tests that show what is rejected as well as accepted | 6 h |
| 9 · NAT, NAT64 and edge services | PAT for 50 hosts, static NAT for a server, NAT64/DNS64 for an IPv6-only VLAN; NTP, syslog and SNMPv3 on every device | Translation tables, aligned log timestamps, SNMPv3 walk | 4 h |
| 10 · Troubleshooting gauntlet and AI review | Three timed rounds of mixed faults; then apply 5 AI-drafted configurations in the lab and classify every defect | Fault times and evidence; AI defect table (type, severity, how found) | 5 h |

## Projects

### P1 · Campus addressing and VLAN design (L1, ~6 hours)

**Real-world inspiration.** College campuses in India often grow building by building: a new hostel or lab block is added with its own flat network, and years later nobody can summarise or segment it. This scenario is illustrative: a campus of 4 buildings, 2,500 users, hostel Wi-Fi, labs, administration and CCTV.

**What to build.** An IPv4 and IPv6 addressing plan, a VLAN table (data, voice, CCTV, guest, management), a two-tier topology with routed distribution, and a working model in an emulator. Load the plan into NetBox or a CSV that your Lab 2 script checks.

**Acceptance criteria**
- The overlap checker passes; every building summarises to one IPv4 and one IPv6 prefix.
- At least 50% free space remains in every building block for growth, shown by the script.
- A reachability matrix of 20 source-destination pairs matches the intended policy (guest reaches only the internet gateway; CCTV reaches only the recorder) with 100% agreement.
- The design document explains the choice of root bridge and gateway placement in under one page.

**Stretch goals.** Generate switch configurations from the CSV with a Jinja2 template (a preview of NET303). Add a /127 point-to-point plan for all routed links.

**What it proves to an employer.** You can plan a network that still makes sense after five years of growth, which is the first thing a senior engineer looks for in a junior.

### P2 · Resilient HQ and branches with measured convergence (L2, ~15 hours)

**Real-world inspiration.** Hospitals, banks and factories expect the network to survive a failed switch, link or gateway without users noticing. The setting is illustrative: a district hospital with a main block and two clinics.

**What to build.** HQ with a redundant distribution pair (LACP to each access switch, VRRP for IPv4 and IPv6), multi-area OSPF to two branches with floating static backups over a second link, and BFD where it helps. Write a failure test plan of at least 8 cases (link, switch, gateway, uplink, branch WAN) and run it with continuous probes.

**Acceptance criteria**
- For every case, measured packet loss is recorded from 10 ms probes (`fping` or equivalent); gateway failover loses no more than 1 second of traffic, and link failures with BFD lose under 300 ms.
- No spanning-tree topology change propagates outside the access block where a failure happens (shown in logs).
- A branch WAN failure moves traffic to the backup path and back after recovery without manual action.
- Every test is repeatable from a script, and the results table can be regenerated in under 10 minutes.

**Stretch goals.** Replace the Layer 2 distribution with routed access and compare convergence. Add QoS so a simulated voice flow keeps under 30 ms jitter while the backup link is congested.

**What it proves to an employer.** You do not just claim a design is redundant; you measure it, which is what operations managers and network architects ask for.

### P3 · Dual-ISP enterprise edge with a change you can defend (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** The 2022 Rogers outage began with a route filter removed during a staged upgrade; the review found the change process did not flag the error and the core had no overload backstop. MANRS lists filtering, anti-spoofing and coordination as baseline actions for operators. The enterprise below is illustrative.

**What to build.** An enterprise edge with two border routers, eBGP to two simulated ISPs (FRRouting), iBGP between borders, a provider-independent IPv4 and IPv6 prefix announced only from the edge, inbound and outbound policy (primary and backup), max-prefix limits, RPKI route origin validation with a local validator, PAT and static NAT, NAT64 for an IPv6-only segment, and logging to a central syslog server with synchronised NTP. Then write and execute a method of procedure for a risky change: migrating from ISP-A primary to ISP-B primary with zero unplanned loss.

**Acceptance criteria**
- Policy tests prove the edge never becomes a transit path: routes from ISP-A are never sent to ISP-B (tested by injecting 1,000 test prefixes).
- An RPKI-invalid route injected by a simulated ISP is rejected, and a valid one is accepted.
- A max-prefix breach shuts the session as configured and raises a syslog alert within 5 seconds.
- Full failure of the primary ISP shifts outbound traffic within 3 seconds with BFD and recovers automatically.
- The MOP includes pre-checks, numbered steps, post-checks with expected values and a rollback that you tested in a rehearsal; the live change completes with no loss beyond the window you predicted.
- In three fault drills run by a classmate (for example, a removed prefix-list, a wrong next-hop, a broken NAT rule), your mean time to repair is under 20 minutes, with evidence for each fix.

**Stretch goals.** Add a pre-change check with Batfish that proves the new policy still blocks transit before you touch a device (a bridge into NET303). Add BGP communities so the ISP can blackhole a prefix under attack, and document when you would ask for it.

**What it proves to an employer.** You can run the part of the network where one mistake takes a company offline, and you can show the evidence and the rollback, not just the configuration.

## Feeds into

- [NET401 Data Center and Hybrid Infrastructure](../../year_4/NET401_data_center_and_hybrid_infrastructure/README.md): BGP, ECMP and failure domains become spine-leaf with EVPN.
- [NET303 Network Automation and NetDevOps](../NET303_network_automation_and_netdevops/README.md): P1's CSV and P3's MOP become a source of truth and an automated pipeline.
- [NET304 Wireless, SD-WAN and Enterprise Networks](../NET304_wireless_sd_wan_and_enterprise_networks/README.md): P2's branch design is the starting point for SD-WAN.
- [NET402 Network Security Engineering](../../year_4/NET402_network_security_engineering/README.md): segmentation and edge filtering.
- The major's [flagship industry project](../../../../06_career_and_market_readiness/05_industry_projects/NET_it_infrastructure_networking.md).
