# NET401 · Labs and projects

Fabrics run in Containerlab (Nokia SR Linux, Arista cEOS, FRRouting or SONiC images) on a Linux host with 32 GB of RAM. Virtualisation and storage labs use nested virtualisation: three Proxmox VE VMs and two Hyper-V VMs (Windows Server evaluation) on one workstation, or older donated servers if your college has them. Cloud labs use free-tier or student credits; delete VPN gateways after each lab because they are billed by the hour.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Power, cooling and optics BoM | Power, cooling and optics plan for 20 racks (10 at 8 kW, 10 at 40 kW) with redundancy | Spreadsheet with assumptions and a one-page explanation | 3 h |
| 2 · Fabric sizing calculator | Python tool that outputs leaves, spines, oversubscription, optics and power for given server counts and NIC speeds | Tool with tests against 3 hand-calculated designs | 4 h |
| 3 · eBGP underlay | 2-spine, 4-leaf eBGP underlay with BFD, ECMP and jumbo MTU; a planted MTU fault to find | Topology, configs, failover timings, fault evidence | 5 h |
| 4 · VXLAN by hand | Static VXLAN with head-end replication on Linux and on a NOS; captures of encapsulated traffic | Annotated captures; MTU calculation | 4 h |
| 5 · EVPN with symmetric IRB | Two tenants, anycast gateways, ESI multihoming; then 5 planted faults; then an AI-drafted leaf config reviewed | Route-type evidence for each fault; AI defect table | 7 h |
| 6 · Fabric as code and day-2 | Generate the fabric from NetBox; add a rack and a tenant through the pipeline with zero packet loss | Pipeline log; continuous-traffic loss report | 5 h |
| 7 · Hypervisor clusters and migration | Proxmox VE 3-node cluster with Ceph and a 2-node Hyper-V failover cluster with a witness; migrate 5 VMs between platforms | HA restart times, migration issue log | 7 h |
| 8 · iSCSI, Ceph and fio | iSCSI with multipath, a Ceph pool, fio profiles for database, VM and backup workloads; a node failure during load | fio results with latency percentiles; rebuild-time measurement | 5 h |
| 9 · Hybrid VPN with BGP | IPsec tunnels with BGP from the lab to one cloud provider; primary/backup policy; hybrid DNS with conditional forwarding | Route tables both sides, failover test, DNS resolution tests | 5 h |
| 10 · DR failover drill | Replicate VMs between two lab clusters; planned failover and failback with a runbook | Measured RTO and RPO vs targets; runbook corrections | 5 h |

## Projects

### P1 · Fabric design and sizing report (L1, ~6 hours)

**Real-world inspiration.** Savills reported 258 MW of data-centre IT capacity added in India in the first half of 2026. Each new hall starts with a fabric design that fixes power, optics and growth for years. The tenant below (a fintech moving from a single colocation cage to two halls, illustrative) is typical.

**What to build.** Using your Lab 2 calculator, a design report for a fabric of 600 servers growing to 1,500 in three years, with 25G and 100G server ports and a separate small GPU pod: topology, oversubscription per rack type, growth steps, optics and cabling BoM, power per rack, failure-domain analysis and a one-page summary for a non-technical decision maker.

**Acceptance criteria**
- All numbers reproduce from the calculator and from a hand calculation for one rack type.
- The design reaches 1,500 servers without replacing spines, or explains exactly when and how they change.
- The failure analysis states remaining bandwidth after loss of one spine and one leaf, as percentages.
- Every assumption (NIC speeds, server power, optics prices) is listed and labelled as an estimate or sourced.

**Stretch goals.** Compare a 2-tier design with a 3-tier super-spine design for 5,000 servers; add a cost model per server port.

**What it proves to an employer.** You can turn requirements into a fabric that grows predictably, with numbers a manager can check.

### P2 · EVPN fabric with tenants, multihoming and a migration of real workloads (L2, ~15 hours)

**Real-world inspiration.** Enterprises replacing ageing three-tier networks move to VXLAN EVPN fabrics while migrating virtual machines off older platforms; Network World reported in June 2026 that most VMware customers are reducing their footprint but few have finished.

**What to build.** A 2-spine, 4-leaf EVPN fabric generated from NetBox, with two tenants, symmetric IRB, anycast gateways, ESI multihoming for hypervisor hosts, and a border leaf to an external router. Attach a Proxmox VE cluster and a Hyper-V host (nested), and migrate 5 VMs from one platform to the other across the fabric while traffic runs.

**Acceptance criteria**
- Leaf or spine failure causes under 500 ms of traffic loss between tenants' VMs (measured with 10 ms probes); ESI member-link failure causes under 300 ms.
- Tenants with overlapping address ranges stay isolated (1,000 cross-tenant probes, all blocked) and reach each other only through the defined firewall path.
- A VM live-migrated between leaves keeps its gateway and loses fewer than 5 probes.
- The 5 cross-platform migrations each have a recorded checklist, duration and issue list; all 5 boot and pass an application check.
- The fabric can be destroyed and rebuilt from NetBox and templates in under 20 minutes.

**Stretch goals.** Add a second fabric and connect the two with route-type-5 interconnect; stream EVPN state with gNMI to a dashboard.

**What it proves to an employer.** You can build and operate the fabric modern enterprise data centres run on, and move workloads across it safely.

### P3 · Hybrid data-centre platform with proven DR and a hypervisor exit plan (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** Indian banks and hospital groups run private data centres under RBI or sector rules while connecting to public clouds; many are reconsidering their hypervisor after Broadcom's licensing changes. The organisation below (a mid-sized bank with a primary DC, a DR site and Azure, illustrative) combines these constraints.

**What to build.** Two lab "sites", each with an EVPN fabric, a hypervisor cluster (Proxmox VE with Ceph at one, Hyper-V at the other, or the same platform at both), and storage; replication between sites; a VPN with BGP to a cloud provider standing in for a private interconnect, with hybrid DNS; and a written hypervisor exit plan for a 300-VM estate, including your measured migration data.

**Acceptance criteria**
- A planned DR failover of a 3-tier application (web, app, database VMs) completes within an RTO of 30 minutes and an RPO of 15 minutes, measured in two drills; failback also succeeds.
- The two sites are connected by routing, not stretched Layer 2, and the design document explains why.
- Loss of the cloud VPN's primary tunnel shifts traffic to the backup within 30 seconds; DNS for cloud and on-premises names resolves correctly from both sides.
- Storage benchmarks meet stated requirements (for example, database profile p99 latency under 5 ms in the lab), or the gap is analysed.
- The exit plan includes inventory method, platform scoring, wave plan, rollback, staffing and a 3-year cost comparison using public list prices or clearly labelled estimates; every licensing claim cites a dated source.
- A runbook lets a classmate perform the failover without help.

**Stretch goals.** Add a small GPU-style pod design to the fabric (on paper with numbers) and explain how its network differs; add Batfish checks for the inter-site routing policy.

**What it proves to an employer.** You can design, run and prove a hybrid infrastructure platform end to end, which is senior infrastructure engineer and architect work.

## Feeds into

- [NET501 Frontier Seminar](../../year_5/NET501_frontier_seminar_5g_satellite_internet/README.md): programmable data planes, AI fabrics and telco clouds build on this course.
- [NET404 Enterprise Architecture and Cloud Migration](../NET404_enterprise_architecture_and_cloud_migration/README.md): P3's exit plan becomes part of a portfolio-level migration decision.
- [CLD402 Multi-Cloud, Hybrid Cloud and Migration](../../../cloud_engineering/year_4/CLD402_multi_cloud_hybrid_cloud_and_migration/README.md) and [CLD404 AI Infrastructure in the Cloud](../../../cloud_engineering/year_4/CLD404_ai_infrastructure_in_the_cloud_gpus_inference/README.md) as electives.
- The major's [flagship industry project](../../../../06_career_and_market_readiness/05_industry_projects/NET_it_infrastructure_networking.md).
