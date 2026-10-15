# NET401 · Data Center and Hybrid Infrastructure

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 7 | 4 (≈ 120 hours) | L2 → L4 | [NET301](../../year_3/NET301_routing_and_switching/README.md) | [NET501](../../year_5/NET501_frontier_seminar_5g_satellite_internet/README.md); pairs with [CLD304](../../../cloud_engineering/year_3/CLD304_cloud_networking_vpcs_dns_load_balancing/README.md) and [CLD402](../../../cloud_engineering/year_4/CLD402_multi_cloud_hybrid_cloud_and_migration/README.md) |

## Why this course matters now

Data centres are being built faster than at any time in India's history. Savills counted 258 MW of IT capacity added in the first half of 2026, 59% more than a year earlier, taking India's operational stock to about 1.8 GW, and projects more than 7 GW by 2030. Much of the new demand comes from AI: GPU clusters need power densities, cooling and network fabrics that older halls were never designed for, and vendors formed the Ultra Ethernet Consortium, which published its 1.0 specification in 2025, to adapt Ethernet for AI and HPC traffic. At the same time, the virtualisation layer under most enterprise data centres is being rethought. After Broadcom bought VMware it ended perpetual licences and moved customers to subscription bundles, and in April 2025 it was reported to have raised the minimum order to 72 cores; a CloudBolt survey reported by Network World in June 2026 found 87% of respondents reducing their VMware footprint but only 4% finished, and a Gartner analyst estimated two to four years to untangle the dependency. Proxmox VE, Hyper-V, Nutanix AHV and Kubernetes-based virtualisation are the realistic alternatives, and each changes the network and storage design. AI tools now generate EVPN configurations and suggest fabric fixes, but the engineer still owns the failure domains, the migration plan, the storage that must not lose data, and the private links to the cloud that carry everything else.

## Learning outcomes

By the end you can:

1. **Size** power, cooling, rack space and optics for a data hall, including high-density AI racks, and **explain** PUE and redundancy tiers.
2. **Design** a spine-leaf fabric with an eBGP underlay, stating oversubscription, failure domains and growth steps.
3. **Build** a VXLAN BGP EVPN fabric with symmetric IRB, anycast gateways, multi-tenancy and EVPN multihoming, and **troubleshoot** it route type by route type.
4. **Operate** hypervisor clusters on at least two platforms (Proxmox VE with KVM and Hyper-V), and **plan** a migration away from a proprietary hypervisor with risks and costs.
5. **Design** block, file and object storage (iSCSI, NVMe/TCP, NFS, Ceph), and **measure** it with fio against requirements.
6. **Choose** between three-tier, converged and hyperconverged designs with evidence.
7. **Connect** on-premises networks to AWS, Azure and Google Cloud with IPsec and dedicated interconnects, with redundant BGP and correct DNS.
8. **Plan and test** disaster recovery between sites, and **explain** why stretched Layer 2 is dangerous.
9. **Describe** how AI training and inference clusters change fabric, power and cooling design.

## Chapters and lessons

### Chapter 1 · Physical foundations (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Power | kW per rack, N, N+1 and 2N designs, UPS and generators, A and B feeds, why a 40 kW AI rack changes everything | Power budget for 20 racks, half general-purpose and half GPU |
| 1.2 Cooling | Hot and cold aisle containment, in-row cooling, direct-to-chip liquid cooling; PUE (The Green Grid) and what it hides | Compute PUE from a meter dataset and explain one misleading case |
| 1.3 Tiers and sites | Uptime Institute Tier I–IV concepts, colocation vs owned, site risks (flood, power grid); India's main DC markets | Compare two colocation offers on redundancy, power price and connectivity |
| 1.4 Cabling and optics | Structured cabling, MPO, single-mode vs multimode, DAC and AOC, 100/400/800G optics, breakouts | Write a cabling and optics BoM for a 4-spine, 16-leaf fabric |

**Check your understanding:** Why can a lower PUE coexist with higher total energy use? What does 2N protect against that N+1 does not? Why do AI racks force a decision about liquid cooling?

### Chapter 2 · Fabric architecture (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 From three-tier to Clos | Access-aggregation-core, the east-west traffic shift, Clos and spine-leaf | Redraw a three-tier DC as spine-leaf and compare failure impact |
| 2.2 Numbers | Oversubscription ratios, bisection bandwidth, ECMP width, port counts and growth steps; super-spines | Calculate oversubscription and maximum servers for 3 designs |
| 2.3 Lessons from hyperscalers | Google's Jupiter papers (SIGCOMM 2015, 2022) and Meta's data-centre fabric: why scale forced these designs | Summarise one paper's design choice and what an enterprise can borrow |
| 2.4 Failure domains | Leaf pairs, spine loss, power-zone alignment, maintenance without outages | Simulate a spine failure; compute remaining capacity |

**Check your understanding:** Why does spine-leaf give predictable latency between any two servers? What does a 3:1 oversubscription mean for a storage-heavy rack? Why should failure domains follow power zones?

### Chapter 3 · The underlay (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 BGP in the data centre | eBGP everywhere (RFC 7938), ASN schemes, BGP unnumbered, why not OSPF at very large scale | Build a 2-spine, 4-leaf eBGP underlay in Containerlab |
| 3.2 Addressing and MTU | Loopbacks, /31 links, jumbo frames end to end; MTU mismatches as the classic fabric bug | Find a planted MTU mismatch with pings of increasing size |
| 3.3 Fast failure | BFD, ECMP rehashing, `maximum-paths`, graceful restart vs fast failover | Measure leaf-spine link failover with and without BFD |
| 3.4 Open networking | SONiC, FRRouting on Linux, vendor NOS; disaggregation trade-offs | Run the same underlay on SR Linux and FRR; compare operations |

**Check your understanding:** Why does eBGP with one ASN per leaf avoid iBGP's full-mesh problem? Why do jumbo frames have to be consistent end to end? When does graceful restart make an outage worse?

### Chapter 4 · VXLAN (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Encapsulation | VXLAN header (RFC 7348), VNIs, VTEPs, UDP port 4789, 50 bytes of overhead | Capture and decode VXLAN packets between two leaves |
| 4.2 Flood and learn | Head-end replication vs multicast underlay, why flood-and-learn does not scale | Build static VXLAN with head-end replication; watch the floods |
| 4.3 Linux VXLAN | `ip link add type vxlan`, bridges and VTEPs on servers | Connect two hosts' namespaces over a Linux VXLAN tunnel |
| 4.4 Why a control plane | MAC learning via BGP instead of flooding; preview of EVPN | List the problems EVPN must solve for this lab |

**Check your understanding:** Why does VXLAN use UDP? What breaks first when the underlay MTU is 1500? Why is flooding unknown unicast across a fabric dangerous?

### Chapter 5 · BGP EVPN (weeks 5–6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 EVPN basics | Address family L2VPN EVPN, route types 2 (MAC/IP), 3 (inclusive multicast), 5 (IP prefix) (RFC 7432, RFC 8365, RFC 9136) | Bring up EVPN on your fabric; read each route type |
| 5.2 Routing in the fabric | Asymmetric vs symmetric IRB (RFC 9135), L3 VNIs, distributed anycast gateway, ARP suppression | Route between two subnets on different leaves with symmetric IRB |
| 5.3 Multi-tenancy | VRFs per tenant, route targets and distinguishers, border leaves, external connectivity | Two tenants with overlapping addresses and controlled leaking through a firewall |
| 5.4 Multihoming | EVPN multihoming with Ethernet segments (ESI), designated forwarder, replacing MLAG | Dual-attach a server with ESI-LAG; fail one leaf |
| 5.5 Troubleshooting EVPN | Following a MAC from host to remote leaf: local table, type-2 route, remote VTEP, forwarding | Fix 5 planted EVPN faults (RT mismatch, VNI mismatch, missing L3 VNI, MTU, ESI mismatch) |

**Check your understanding:** Why does symmetric IRB scale better than asymmetric? What does an anycast gateway give a moving virtual machine? Why do route targets, not route distinguishers, decide where routes are imported?

### Chapter 6 · Fabric operations (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Fabric as code | Generate the fabric from NetBox and templates ([NET303](../../year_3/NET303_network_automation_and_netdevops/README.md)); Batfish checks for EVPN | Rebuild the whole fabric from data in under 15 minutes |
| 6.2 Day-2 work | Adding racks, tenants and VLANs; upgrades with rolling maintenance; checks before and after | Add a rack with zero impact, proven by continuous traffic tests |
| 6.3 Telemetry | gNMI streams for interface, BGP and EVPN state; queue drops and buffer use | Dashboard showing a microburst on a leaf uplink |
| 6.4 Interconnecting sites | Data-centre interconnect with multi-site EVPN and border gateways; when not to stretch | Connect two lab fabrics with route-type-5 only and justify the choice |

**Check your understanding:** What should an upgrade checklist for a spine contain? Why do microbursts hide in 5-minute averages? Why route between sites instead of stretching Layer 2?

### Chapter 7 · Virtualisation and the post-Broadcom landscape (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Hypervisors | Type 1 hypervisors (ESXi, Hyper-V, KVM, Xen), CPU and memory virtualisation, overcommit, NUMA | Measure a VM's performance with and without CPU overcommit |
| 7.2 Virtual networking | Linux bridge, Open vSwitch, Hyper-V virtual switch, SR-IOV; VLAN and VXLAN to the host | Trunk 3 VLANs to Proxmox and Hyper-V hosts |
| 7.3 Clusters | Live migration, HA restart, quorum and witnesses, maintenance mode | Live-migrate a VM under load; fail a host and time HA restart |
| 7.4 Platform choice | Broadcom's VMware changes (subscription only, bundles, minimum cores); alternatives: Proxmox VE 9.x, Hyper-V with Windows Server 2025, Nutanix AHV, OpenStack, KubeVirt/OpenShift Virtualization, XCP-ng | Score 4 platforms for a 300-VM estate on cost, skills, features and risk |
| 7.5 Migration method | Inventory, dependency mapping, conversion tools, pilot, waves, rollback; what usually breaks (drivers, MAC addresses, backups, licences) | Migrate 5 VMs between platforms and log every issue |

**Check your understanding:** Why does a two-node cluster need a witness? What is the hidden cost in a hypervisor migration beyond licences? Why might a team choose Hyper-V over Proxmox, or the reverse?

### Chapter 8 · Storage (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Storage models | Block, file and object; DAS, SAN and NAS; what applications actually need | Classify 10 workloads by the storage they need |
| 8.2 SAN protocols | Fibre Channel concepts (zoning, WWNs), iSCSI (RFC 7143) with multipathing, NVMe over TCP | Build an iSCSI target with multipath on Linux; fail a path |
| 8.3 File and object | NFS and SMB for virtualisation, S3-compatible object storage | Serve the same dataset over NFS and an S3-compatible store; compare |
| 8.4 Protecting data | RAID levels, erasure coding, snapshots, synchronous vs asynchronous replication | Rebuild a degraded array; measure performance during the rebuild |
| 8.5 Measuring | IOPS, latency, throughput, queue depth; fio profiles for databases, VMs and backups | Benchmark your storage with 3 fio profiles and explain the results |
| 8.6 Software-defined storage | Ceph (RADOS, placement groups, replicas), ZFS and TrueNAS | Build a 3-node Ceph cluster on Proxmox; kill a node |

**Check your understanding:** Why does latency matter more than IOPS for many databases? Why is RAID not a backup? What does synchronous replication cost in distance and latency?

### Chapter 9 · Converged and hyperconverged infrastructure (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 HCI architecture | Compute and storage on the same nodes; Nutanix, vSAN, Azure Local (formerly Azure Stack HCI), Proxmox with Ceph | Map each to compute, storage and management planes |
| 9.2 Network requirements | 25/100G, RDMA (RoCEv2) for storage traffic, separate storage networks, PFC and ECN basics | Design the network for a 4-node HCI cluster |
| 9.3 Failure tolerance | Replication factor, fault domains, rebuild times, capacity reserve | Calculate usable capacity and rebuild time for 3 configurations |
| 9.4 When HCI fits | Branch and edge sites, VDI, small DCs vs large shared SANs | Write a recommendation for a hospital group's 3 sites |

**Check your understanding:** Why must an HCI cluster keep free capacity for rebuilds? Why does RDMA need a carefully configured network? Where does HCI become more expensive than separate storage?

### Chapter 10 · Hybrid connectivity to cloud (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 IPsec to cloud | Site-to-site VPN to AWS, Azure and Google Cloud, BGP over tunnels, throughput limits | Build a VPN with BGP from your lab to a free-tier cloud account |
| 10.2 Dedicated interconnects | AWS Direct Connect, Azure ExpressRoute, Google Cloud Interconnect; partner vs dedicated ports; route limits | Design a redundant interconnect for 2 DCs and 2 regions on paper |
| 10.3 Routing and DNS | Route filtering, AS-path prepending across links, avoiding asymmetric paths through firewalls; hybrid DNS with resolvers and conditional forwarding | Make one link primary for a region; fix a planted asymmetric path |
| 10.4 Security and cost | MACsec on interconnects, encryption options, data transfer pricing | Estimate monthly cost for 50 TB of egress via VPN vs interconnect (public prices) |

**Check your understanding:** Why do many designs keep a VPN as backup to a private interconnect? How does asymmetric routing break stateful firewalls? Why must hybrid DNS be designed before the first workload moves?

### Chapter 11 · Resilience, disaster recovery and capacity (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Site models | Active-active vs active-passive, the danger of stretched Layer 2 and split brain | Analyse a stretched-cluster failure scenario step by step |
| 11.2 DR replication | Storage replication, hypervisor replication, application-level replication; RPO/RTO mapping | Replicate VMs between two lab clusters; fail over and back |
| 11.3 Testing DR | Planned failover tests, isolated test failovers, runbooks | Run a test failover and record actual RTO vs target |
| 11.4 Capacity planning | Ports, power, IP space, storage growth, licence counts, lead times | 3-year capacity plan for your lab DC scaled ×100 |

**Check your understanding:** Why is "it fails over automatically" a risky sentence? What happens to a stretched cluster when the inter-site link fails? Which capacity item has the longest lead time in your region?

### Chapter 12 · AI infrastructure and fabric review (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 GPU cluster networks | Collective communication, rail-optimised designs, InfiniBand vs Ethernet with RoCEv2, why tail latency matters; Ultra Ethernet (link to [CLD404](../../../cloud_engineering/year_4/CLD404_ai_infrastructure_in_the_cloud_gpus_inference/README.md)) | Size a fabric for 256 GPUs with 8 NICs per server |
| 12.2 Lossless Ethernet | PFC, ECN, DCQCN concepts, PFC storms and how to prevent them | Configure ECN marking in a lab and show congestion signalling |
| 12.3 AI-assisted operations | Vendor AI for data-centre networks (Cisco announced controlled availability of data-centre agents with "prescriptive recommendations" for June 2026); testing recommendations in a twin | Have an assistant diagnose 3 planted EVPN faults; compare with your method |
| 12.4 Design review | Peer review of P3 designs: failure domains, numbers, migration risks | Defend your design to a panel |

**Check your understanding:** Why does one slow link slow an entire training job? Why can PFC make a fabric fail worse if misconfigured? What evidence would you need before letting AI change a production fabric?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Power, cooling and optics BoM | — |
| 2 | 2 | Lab 2 · Fabric sizing calculator | — |
| 3 | 3 | Lab 3 · eBGP underlay in Containerlab | **P1 due** |
| 4 | 4 | Lab 4 · VXLAN by hand | — |
| 5 | 5 | Lab 5 · EVPN with symmetric IRB | — |
| 6 | 5 | Lab 5 (cont.) multihoming and fault hunt | Mid-term (AI off) |
| 7 | 6 | Lab 6 · Fabric as code and day-2 change | — |
| 8 | 7 | Lab 7 · Proxmox and Hyper-V clusters, VM migration | — |
| 9 | 8 | Lab 8 · iSCSI, Ceph and fio | **P2 due** |
| 10 | 9 | HCI design exercise | — |
| 11 | 10 | Lab 9 · Hybrid VPN with BGP to cloud | — |
| 12 | 11 | Lab 10 · DR failover drill | DR report |
| 13 | 12 | P3 | — |
| 14 | 12 | Design review | **P3 due** |
| 15 | Review | Oral defence of P3 | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** drafting fabric templates and Containerlab topologies; explaining EVPN route output; producing first-draft migration inventories and runbooks; fio profile design; summarising cloud interconnect documentation (then reading the pages).
- **Do without AI (drills):** oversubscription, power and capacity arithmetic; reading EVPN routes and following a MAC across the fabric; storage performance interpretation; DR design. The mid-term and final are AI-off.
- **Verify AI output by:** building it in the Containerlab or hypervisor lab; Batfish and pyATS checks; captures of VXLAN traffic; fio measurements; vendor and cloud documentation for every limit and price; failover drills with measured times.
- **Where AI still fails here:** assistants confuse route distinguishers with route targets, mix vendor EVPN syntax, invent cloud interconnect limits and prices, and give outdated VMware licensing information. In Lab 5 you ask an assistant to generate EVPN configuration for one leaf on two platforms and record every defect; in Lab 7 you check every licensing claim it makes against a dated source.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1–P3 | 35% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) + P3 oral defence | 30% |

**Mastery gate.** You pass when you can, without AI: (1) design a spine-leaf fabric for a stated server count and growth target with correct oversubscription, port, power and optics numbers in 90 minutes; (2) bring up a 2-spine, 4-leaf EVPN fabric with two tenants and symmetric IRB from templates and fix 3 planted faults in 60 minutes; (3) present a defensible migration plan off a proprietary hypervisor, with risks, rollback and costs, to a panel.

## Industry reality

Where this is used: colocation and hyperscale operators expanding in Mumbai, Chennai and other Indian markets; banks, telecoms and large enterprises running private data centres; AI labs and GPU cloud providers building training clusters; every organisation reconsidering VMware. Employers for this work include colocation providers, network vendors and their partners, systems integrators and large enterprises. Certifications that cover parts of this course include Cisco CCNP Data Center and vendor EVPN tracks; hands-on fabric and migration projects carry more weight.

**Interview questions from this course**

1. *Why spine-leaf, and how do you grow it?* Strong answer: predictable east-west latency, ECMP, scale-out; adding leaves until spine ports run out, then adding spines or a super-spine; oversubscription choices.
2. *Two VMs in the same subnet on different leaves cannot talk. Walk through it.* Strong answer: local MAC learning, type-2 route advertised, route-target import, VNI mapping, VTEP reachability in the underlay, MTU; commands at each step.
3. *Explain symmetric vs asymmetric IRB.* Strong answer: where routing happens, L3 VNI, configuration and scale differences, why symmetric is the usual choice.
4. *We want to leave VMware. How would you plan it?* Strong answer: inventory and dependency mapping, platform evaluation with criteria, pilot, backup and DR compatibility, network and storage changes, waves, rollback, skills, licence timing; cites realistic timelines.
5. *Design redundant connectivity from two data centres to Azure.* Strong answer: two ExpressRoute circuits in different peering locations, VPN backup, BGP policy for primary/secondary, route limits, DNS, monitoring, cost.

## Resources (free first)

- **Standards:** RFC 7938 (BGP in large data centres), RFC 7348 (VXLAN), RFC 7432 (EVPN), RFC 8365 (EVPN overlays), RFC 9135 (EVPN IRB), RFC 9136 (EVPN IP prefix routes), RFC 7143 (iSCSI) — https://www.rfc-editor.org/
- **Labs:** Containerlab — https://containerlab.dev/ ; SR Linux EVPN tutorials — https://learn.srlinux.dev/ ; FRRouting EVPN documentation — https://docs.frrouting.org/en/latest/evpn.html ; SONiC — https://sonicfoundation.dev/
- **Virtualisation and storage:** Proxmox VE documentation — https://pve.proxmox.com/pve-docs/ ; Hyper-V on Windows Server — https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/ ; Ceph documentation — https://docs.ceph.com/ ; fio — https://fio.readthedocs.io/ ; TrueNAS documentation — https://www.truenas.com/docs/
- **Hybrid connectivity:** AWS Direct Connect — https://docs.aws.amazon.com/directconnect/ ; Azure ExpressRoute — https://learn.microsoft.com/en-us/azure/expressroute/ ; Google Cloud Interconnect — https://cloud.google.com/network-connectivity/docs/interconnect
- **Papers:** Singh et al., "Jupiter Rising" (SIGCOMM 2015) — https://research.google/pubs/jupiter-rising-a-decade-of-clos-topologies-and-centralized-control-in-googles-datacenter-network/ ; Poutievski et al., "Jupiter Evolving" (SIGCOMM 2022) — https://research.google/pubs/jupiter-evolving-transforming-googles-datacenter-network-via-optical-circuit-switches-and-software-defined-networking/
- **Industry bodies:** The Green Grid (PUE) — https://www.thegreengrid.org/ ; Uptime Institute Tier Standard — https://uptimeinstitute.com/tiers ; Ultra Ethernet Consortium — https://ultraethernet.org/
- **Paid, optional:** Dinesh Dutt, *Cloud Native Data Center Networking* (O'Reilly).

## Sources

- Indian Infrastructure, Savills India report on H1 2026 data-centre additions (22 Jul 2026): 258 MW added, about 1.8 GW IT operational, more than 7 GW by 2030 — https://indianinfrastructure.com/2026/07/22/indias-data-centre-capacity-additions-grow-59-per-cent-in-h1-2026-says-industry-report/ (checked 2026-10)
- Network World, "Will Broadcom's VMware strategy keep paying big dividends?" (3 Jun 2026): perpetual licences eliminated, VCF bundles, CloudBolt survey (87% reducing, 4% completed), Gartner 2–4 year estimate — https://www.networkworld.com/article/4180754/will-broadcoms-vmware-strategy-keep-paying-big-dividends.html (checked 2026-10)
- heise online, VMware 72-core minimum from April 2025 — https://heise.de/-10335733 (checked 2026-10)
- Proxmox press releases (VE 9.0 on Debian 13, 5 Aug 2025; VE 9.2, 21 May 2026) — https://www.proxmox.com/en/about/company-details/press-releases (checked 2026-10)
- Ultra Ethernet Consortium (Specification 1.0, 2025; current 1.0.3 download) — https://ultraethernet.org/ (checked 2026-10)
- Cisco newsroom, AgenticOps announcement (10 Feb 2026): data-centre "prescriptive recommendations", controlled availability June 2026 — https://newsroom.cisco.com/content/r/newsroom/en/us/a/y2026/m02/cisco-expands-agenticops-innovations-across-portfolio.html (checked 2026-10)

_Last reviewed: 2026-10_
