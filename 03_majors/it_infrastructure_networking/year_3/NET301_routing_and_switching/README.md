# NET301 · Routing and Switching

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 5 | 4 (≈ 120 hours) | L1 → L3 | [CS204](../../../../02_year_2_core_computer_science/semester_3/CS204_computer_networks/README.md), [CS203](../../../../02_year_2_core_computer_science/semester_3/CS203_operating_systems/README.md) | [NET401](../../year_4/NET401_data_center_and_hybrid_infrastructure/README.md); taken alongside [NET303](../NET303_network_automation_and_netdevops/README.md), and the base for [NET304](../NET304_wireless_sd_wan_and_enterprise_networks/README.md) and [NET402](../../year_4/NET402_network_security_engineering/README.md) |

## Why this course matters now

Every office, campus, hospital, factory and data centre still runs on Ethernet switching, VLANs, OSPF and BGP, and the biggest outages are still routing changes. In July 2022 a Rogers engineer removed a route filter during a staged core upgrade; routing information flooded and crashed the core, and Canada lost mobile, internet and payment services for about a day. The review found that the change process did not catch the error and the core had no overload limit as a backstop. In October 2021 a backbone maintenance command at Meta led its DNS servers to withdraw their BGP routes, and its services vanished from the internet. AI assistants now draft switch and router configurations in seconds, but researchers who tested GPT-4 on router configuration tasks found "egregious errors in topology, syntax, and semantics" unless verifiers checked every draft (Mondal et al., 2023). The US Bureau of Labor Statistics projects network architect jobs to grow 8% between 2025 and 2035 while administrator jobs shrink 4%. Employers pay for people who can design the addressing, predict how the network fails, and prove a change is safe before it goes live.

## Learning outcomes

By the end you can:

1. **Design** IPv4 and IPv6 addressing plans with VLSM and summarisation for a multi-site organisation, and **verify** them with a script that finds overlaps.
2. **Build** switched networks with 802.1Q trunks, RSTP or MSTP, LACP bundles and first-hop redundancy, and **predict** the spanning-tree topology before you look at the switch.
3. **Configure** single-area and multi-area OSPFv2 and OSPFv3, and **explain** every LSA in the database of a given router.
4. **Configure** eBGP and iBGP for a dual-homed enterprise edge, **apply** inbound and outbound policy with prefix-lists, route-maps and communities, and **walk** the best-path algorithm step by step.
5. **Implement** NAT44, PAT and NAT64, plus edge services (NTP, syslog, SNMPv3, DHCP relay) and first-hop security (DHCP snooping, dynamic ARP inspection, port security).
6. **Measure** convergence after link, node and gateway failures, and **reduce** it with BFD, timer tuning and design changes.
7. **Troubleshoot** planted faults with a stated method (follow the path, divide and conquer, compare with a baseline), within a time limit, and **write** the evidence.
8. **Plan** a change with pre-checks, post-checks and a tested rollback, and **review** an AI-generated configuration for errors before it reaches a device.

## Chapters and lessons

### Chapter 1 · The lab, the CLI and the troubleshooting method (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Your free lab | Cisco Packet Tracer (free with a Networking Academy account), Cisco Modeling Labs Free (up to 5 running nodes), GNS3 (open source), Containerlab with FRRouting, Nokia SR Linux and Arista cEOS; EVE-NG Community Edition reached end of support in June 2026, so check what you install | Install two platforms; build a 3-router triangle on each and compare effort |
| 1.2 Three CLIs | Cisco IOS modes and `running-config` vs `startup-config`; Junos candidate configuration, `commit`, `commit confirmed`, `rollback`; Arista EOS sessions | Make the same interface change on IOS, Junos and EOS; note how each undoes it |
| 1.3 Reading a device | `show interfaces`, counters (CRC, input errors, drops), `show ip interface brief`, LLDP/CDP neighbours, logs | Draw a topology using only neighbour tables |
| 1.4 Troubleshooting methods | Top-down, bottom-up, divide and conquer, follow the path, compare with a known-good baseline, swap components; hypothesis and evidence | Solve 3 single-fault labs and write which method found each fault |

**Check your understanding:** Why does a structured method beat intuition when two faults exist at once? Why is Junos `commit confirmed` a safety feature, and what is the IOS equivalent? Which interface counter tells you a cable or optic is bad, and which tells you the link is congested?

### Chapter 2 · Addressing plans (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 IPv4 subnetting to speed | Binary masks, block sizes, VLSM, supernetting; RFC 1918 and shared address space (RFC 6598) | 20 subnetting problems in 20 minutes, AI off |
| 2.2 Summarisation | Choosing blocks so each site summarises to one route; why a bad plan grows the routing table forever | Fix an addressing plan whose sites cannot be summarised |
| 2.3 IPv6 plans | Global unicast, link-local, ULA (RFC 4193); /48 per site, /64 per VLAN, /127 on point-to-point links (RFC 6164); nibble boundaries | Write the IPv6 plan for a 5-site organisation |
| 2.4 DHCP and IPAM | DHCPv4 relay (`ip helper-address`), SLAAC vs DHCPv6, reservations; IP address management in NetBox (preview of NET303) | Load your plan into NetBox and export it |
| 2.5 Checking plans with code | Python `ipaddress` module: overlap detection, summarisation, free-space reports | A 40-line script that rejects overlapping prefixes |

**Check your understanding:** Why is a /64 the right size for a LAN in IPv6 even though it wastes addresses? A site grows from 4 VLANs to 40: what in your plan has to change if you did not leave room? What breaks when two merged companies both use 10.0.0.0/16?

### Chapter 3 · Ethernet switching and VLANs (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 How a switch forwards | MAC learning, flooding of unknown unicast, ageing, CAM table limits | Watch a MAC table fill as hosts talk; capture the floods |
| 3.2 VLANs and trunks | 802.1Q tags, access vs trunk ports, allowed-VLAN lists, native VLAN risks, voice VLANs | Build 4 VLANs across 3 switches; prove isolation with pings and captures |
| 3.3 Inter-VLAN routing | Router-on-a-stick, switched virtual interfaces (SVIs), Layer 3 switches, where the gateway should live | Move the gateway from a router to an SVI; measure the difference in hops |
| 3.4 Campus design | Access, distribution and core layers; collapsed core; Layer 2 vs Layer 3 access; failure domains | Redraw a flat 2,000-host network into a two-tier design |

**Check your understanding:** Why does a VLAN mismatch on a trunk produce no error message but broken traffic? Why do modern campus designs push routing down to the access layer? What happens to a network when one access port loops back into itself and nothing stops it?

### Chapter 4 · Spanning tree (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Why loops kill Layer 2 | Broadcast storms, MAC flapping, no TTL in Ethernet | Create a loop with STP off in the lab only; watch CPU and counters |
| 4.2 802.1D election | Bridge ID, root bridge, root port, designated port, path cost | Predict roles on 4 topologies by hand, then check |
| 4.3 RSTP and MSTP | 802.1w proposal/agreement, edge ports; 802.1s instances and regions | Convert to MSTP with 2 instances; load-share VLANs |
| 4.4 Protection features | PortFast, BPDU Guard, Root Guard, Loop Guard, UDLD, storm control | Plug a "rogue switch" into an access port and show each guard reacting |
| 4.5 Living with STP | Where STP still exists in 2026 and how routed access and EVPN (NET401) reduce it | Write a one-page STP standard for a campus |

**Check your understanding:** Why should you choose the root bridge yourself instead of letting the lowest MAC address win? Why does RSTP converge faster than 802.1D? Which guard stops a user's home switch from becoming root, and which stops a one-way fibre link from creating a loop?

### Chapter 5 · Link aggregation and first-hop redundancy (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 LACP | IEEE 802.1AX, active/passive modes, hashing on MAC/IP/port, why one flow never exceeds one member link | Bundle 2 links; show uneven load with one big flow |
| 5.2 Multi-chassis bundles | Stacking, MLAG, vPC; split-brain and peer-link failure | Fail the peer link in a lab and record what happens |
| 5.3 HSRP and VRRP | Virtual IP and MAC, priority, preemption, VRRPv3 (RFC 9568) for IPv4 and IPv6 | Fail the active gateway; measure lost pings at 10 ms intervals |
| 5.4 Tracking and BFD | Object tracking of uplinks; BFD (RFC 5880) for sub-second failure detection | Cut failover time with tracking and BFD; tabulate before and after |

**Check your understanding:** A 10 Gbit/s backup copy runs on a 2 × 10 Gbit/s bundle and still crawls: why? Why is preemption sometimes turned off on purpose? Why can BFD detect a failure faster than a routing protocol's hello timer?

### Chapter 6 · The routing table and static routing (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 RIB and FIB | Routing information base vs forwarding table; CEF; recursive next-hop lookup | Trace a packet through RIB and FIB output |
| 6.2 Route selection | Longest prefix first, then administrative distance, then metric; ECMP | Predict the chosen route in 10 mixed-source cases |
| 6.3 Static routes done right | Default routes, floating statics, null routes for summaries, static routes with tracking | Build a branch with a primary link and a floating static backup |
| 6.4 Policy-based routing | Steering by source or application; why PBR makes troubleshooting harder | Send guest traffic out a second ISP; document the exception |

**Check your understanding:** A /24 learned by OSPF and a /16 static route both match a destination: which wins and why? Why does a summary route usually need a matching null route? When does ECMP cause out-of-order packets, and why do most platforms hash per flow?

### Chapter 7 · OSPF (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Adjacency | Hello and dead timers, neighbour states (Down to Full), DR/BDR on broadcast links, point-to-point networks | Debug 5 adjacencies stuck in different states |
| 7.2 The database | LSA types 1, 2, 3, 4, 5 and 7; SPF (see [CS201](../../../../02_year_2_core_computer_science/semester_3/CS201_algorithms_and_complexity/README.md)); cost and reference bandwidth (RFC 2328) | Rebuild a topology from `show ip ospf database` output alone |
| 7.3 Areas | Backbone area 0, ABRs and ASBRs, stub, totally stubby and NSSA areas, inter-area summarisation | Convert a single-area network to 3 areas; compare LSA counts |
| 7.4 OSPFv3 | IPv6 OSPF (RFC 5340), link-local next hops, address families | Run OSPFv2 and OSPFv3 side by side |
| 7.5 Authentication | OSPF cryptographic authentication; why plaintext keys are not enough | Enable and verify authentication without dropping adjacencies |

**Check your understanding:** Why does an MTU mismatch leave OSPF neighbours stuck in ExStart? Why does a type 5 LSA flood the whole domain but a type 3 does not? What does a totally stubby area give up, and what does it gain?

### Chapter 8 · OSPF at scale, IS-IS and convergence (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Convergence anatomy | Detection, propagation, SPF calculation, FIB update; SPF and LSA throttling timers | Measure each phase with timestamps from logs and pings |
| 8.2 Tuning safely | BFD with OSPF, incremental SPF, why aggressive timers can make a flapping link worse | Tune a ring until failover is under 300 ms; then flap a link and observe |
| 8.3 IS-IS in one lesson | Levels, NET addresses, TLVs; why service providers and data centres often prefer it | Build a 4-router IS-IS lab in FRRouting |
| 8.4 Redistribution | Static and connected into OSPF, route tags, the classic two-point redistribution loop | Create and then fix a redistribution loop with tags |

**Check your understanding:** Which convergence phase dominates in a large network, and how would you measure it? Why can redistribution at two points create a loop? When would you choose IS-IS over OSPF for a new design?

### Chapter 9 · BGP for the enterprise edge (weeks 9–10)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Sessions | BGP-4 (RFC 4271) over TCP port 179, eBGP vs iBGP, states (Idle to Established), multihop, TTL security | Bring up eBGP to two simulated ISPs |
| 9.2 Attributes and best path | Weight, local preference, AS path, origin, MED, eBGP over iBGP, IGP cost to next hop, router ID | Predict the best path in 8 scenarios, then verify |
| 9.3 Policy | Prefix-lists, AS-path filters, route-maps, communities (RFC 1997), max-prefix limits; announce only your own prefixes | Make ISP-A primary inbound and outbound, ISP-B backup |
| 9.4 iBGP inside | Full mesh vs route reflectors (RFC 4456), next-hop-self | Replace a 5-router full mesh with route reflectors |
| 9.5 Routing security | Route leaks and hijacks, RPKI route origin validation (RFC 6811), MANRS actions for network operators | Run Routinator against a lab RPKI setup; reject an invalid route |

**Check your understanding:** Why must an enterprise never re-advertise routes learned from one ISP to the other, and which filter enforces it? Why does local preference control outbound traffic while AS-path prepending only influences inbound? What does RPKI route origin validation catch, and what does it not catch?

### Chapter 10 · NAT and edge services (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 NAT44 and PAT | Static, dynamic and overload translation; inside/outside; translation tables and timeouts | Publish a server with static NAT; let 50 hosts share one address |
| 10.2 IPv6 transition | Dual stack first; NAT64/DNS64 (RFC 6146, RFC 6147); why carrier-grade NAT exists in Indian mobile networks | Give an IPv6-only VLAN access to an IPv4-only server |
| 10.3 Management services | NTP (CERT-In directions of 28 April 2022 require clocks synced to NIC or NPL servers or sources traceable to them), syslog, SNMPv3 | Sync every lab device to one NTP source; prove log timestamps align |
| 10.4 First-hop security | DHCP snooping, dynamic ARP inspection, IPv6 RA Guard, port security | Plug in a rogue DHCP server; show snooping blocking it |

**Check your understanding:** Why does NAT break protocols that carry IP addresses inside their payload? Why do incident timelines fall apart when device clocks drift? Why is DHCP snooping a prerequisite for dynamic ARP inspection?

### Chapter 11 · QoS and multicast essentials (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 QoS model | Classification and marking (DSCP), queuing (LLQ, CBWFQ), policing vs shaping, trust boundaries | Protect a voice call on a congested 10 Mbit/s branch link |
| 11.2 Measuring quality | Latency, jitter, loss; `iperf3` UDP tests; why QoS cannot create bandwidth | Show voice quality with and without the policy |
| 11.3 Multicast basics | IGMP snooping, PIM sparse mode and the rendezvous point, where enterprises still use it (video, trading, imaging) | Stream one multicast source to 3 VLANs |
| 11.4 Wide-area basics | MPLS L3VPN from the customer's view, internet underlay, preview of SD-WAN in NET304 | Map a real branch WAN design to the concepts |

**Check your understanding:** Why must marking happen close to the source and be re-checked at the trust boundary? Why does shaping suit a link to a slower provider while policing suits an SLA? What happens to multicast when IGMP snooping is off?

### Chapter 12 · Change, failure and the troubleshooting practical (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Change plans | Method of procedure (MOP): pre-checks, steps, post-checks, rollback, maintenance windows; Junos `commit confirmed`, IOS `configure replace` | Write and execute a MOP for an OSPF area change |
| 12.2 Case studies | Rogers 2022 (filter removed, no overload backstop), Meta 2021 (backbone change, BGP withdrawal); what pre-checks would have caught | Write a one-page review of each with two missing safeguards |
| 12.3 Capture on the wire | SPAN and RSPAN, `tcpdump` on Linux routers, Wireshark filters for OSPF and BGP | Diagnose a BGP flap from a capture |
| 12.4 Reviewing AI-drafted configs | Common defects: wrong vendor syntax, missing filters, wrong wildcard masks, invented commands | Review 5 AI-drafted configs; log every defect with severity |
| 12.5 Troubleshooting gauntlet | Mixed faults across VLANs, STP, OSPF, BGP and NAT | Timed practical: 3 faults in 45 minutes |

**Check your understanding:** What makes a rollback plan trustworthy, and how do you test it before the window? In the Rogers case, which single control would have limited the damage most? Why should a reviewer treat an AI-drafted configuration like one from a new hire?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Lab platform and CLIs | Troubleshooting method notes |
| 2 | 2 | Lab 2 · Addressing plan and overlap checker | — |
| 3 | 3 | Lab 3 · VLANs and trunks | **P1 due** |
| 4 | 4 | Lab 4 · Spanning tree prediction and guards | — |
| 5 | 5 | Lab 5 · LACP and gateway failover timing | — |
| 6 | 6 | Lab 5 (cont.) and static routing drills | Mid-term troubleshooting practical (AI off) |
| 7 | 7 | Lab 6 · Multi-area OSPF | — |
| 8 | 8 | Lab 7 · OSPF fault hunt and convergence | — |
| 9 | 9 | Lab 8 · BGP dual-homed edge | — |
| 10 | 9 | Lab 8 (cont.) with RPKI | **P2 due** |
| 11 | 10 | Lab 9 · NAT, NAT64 and edge services | — |
| 12 | 11 | QoS and multicast exercises | — |
| 13 | 12 | Lab 10 · Troubleshooting gauntlet | MOP and change review |
| 14 | 12 | P3 | **P3 due** |
| 15 | Review | Oral defence of P3 | Final practical lab exam (AI off) + subnetting test |

## Working with AI in this course

- **Use AI for:** explaining unfamiliar `show` output; translating a configuration between IOS, Junos and EOS (then checking every line); generating Containerlab topology files and test scripts; producing practice scenarios ("give me an OSPF fault to find"); turning your notes into flashcards. Claude, ChatGPT and Gemini handle this; vendor assistants such as Cisco AI Assistant are appearing inside management platforms.
- **Do without AI (drills):** subnetting and summarisation; predicting spanning-tree roles; reading an OSPF database; walking BGP best-path selection; writing core configurations from memory. The mid-term, final and gate are AI-off because an interviewer or an outage gives you no assistant.
- **Verify AI output by:** applying it in the emulator first; recording `show ip route`, `show ip ospf neighbor` and `show bgp summary` before and after; checking reachability against an intended matrix; reading the vendor configuration guide for every unfamiliar command; for BGP policy, testing that the filter rejects what it should, not only that it accepts what it should.
- **Where AI still fails here:** Mondal et al. (2023) found GPT-4 router configurations contained errors in topology, syntax and semantics, and only reached useful results when verifiers fed errors back. In Lab 10 you reproduce this on a small scale: ask an assistant for configurations for 5 tasks (VLANs, OSPF areas, BGP policy, NAT, HSRP), apply them in the lab, and classify each failure (wrong vendor syntax, invented command, missing filter, wrong mask, correct but unsafe). Assistants also cannot see your topology; they guess interface names and neighbours.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10, with configuration files and evidence) | 25% |
| Projects P1–P3 | 30% |
| Mid-term troubleshooting practical (AI off) | 10% |
| Final practical lab exam (AI off) + P3 oral defence | 25% |
| Subnetting and protocol written test (AI off) | 10% |

**Mastery gate.** You pass when you can, without AI: (1) from a blank emulator, build a two-site network with VLANs, RSTP, an LACP uplink, VRRP, multi-area OSPF, a dual-ISP eBGP edge with correct filters, and PAT, within 3 hours, with a passing reachability matrix; (2) find and fix 3 planted faults in 45 minutes and explain the evidence for each; (3) solve 10 subnetting and summarisation problems in 10 minutes with no errors.

## Industry reality

Where this is used: every enterprise LAN and WAN; internet exchange points such as NIXI in India; every bank branch network; the edge of every data centre. Public incident reviews show the stakes: the CRTC-published review of the 2022 Rogers outage blamed a removed routing filter and a change process that did not flag it; Meta's 2021 outage review describes how a backbone change cut its DNS off from the internet. MANRS publishes concrete routing-security actions for network operators. Vendor certifications are used as screens in this field more than in software roles (see the [NET market page](../../../../06_career_and_market_readiness/01_market_map/roles/NET_it_infrastructure_networking.md)).

**Interview questions from this course**

1. *A user in VLAN 20 cannot reach anything, but users in VLAN 10 on the same switch can. Walk me through it.* Strong answer: checks the port's access VLAN, the trunk's allowed-VLAN list and native VLAN, the SVI or gateway state, DHCP relay, and ARP; follows the path rather than guessing; names the command for each check.
2. *Subnet 172.16.0.0/22 for VLANs of 300, 120, 60 and 2 hosts, and give the summary route.* Strong answer: largest first with VLSM, correct boundaries and broadcast addresses, leaves room for growth, and states the /22 summary.
3. *Two OSPF routers are stuck in ExStart. Why?* Strong answer: MTU mismatch first, then duplicate router IDs or unicast reachability problems; explains what ExStart exchanges and how to confirm with debug or capture.
4. *You have two ISPs. How do you make one primary for both directions?* Strong answer: local preference (or weight) for outbound; AS-path prepending, MED or ISP communities for inbound, with the caveat that inbound is only influenced; filters so you never become transit; max-prefix limits; how you test failover.
5. *Describe a change that went wrong and how you would prevent it.* Strong answer: a concrete MOP with pre-checks, staged rollout, `commit confirmed` or equivalent, post-checks with numbers, and a tested rollback; references a public incident such as Rogers 2022.

## Resources (free first)

- **Lab platforms:** Cisco Packet Tracer via Networking Academy — https://www.netacad.com/cisco-packet-tracer ; Cisco Modeling Labs Free — https://developer.cisco.com/docs/modeling-labs/cml-free/ ; GNS3 — https://www.gns3.com/ ; Containerlab — https://containerlab.dev/ ; FRRouting documentation — https://docs.frrouting.org/ ; EVE-NG downloads (check support status) — https://www.eve-ng.net/index.php/download/
- **Text:** Peterson and Davie, *Computer Networks: A Systems Approach* (free; routing and switching chapters) — https://book.systemsapproach.org/
- **Free courses:** Jeremy's IT Lab CCNA course (YouTube) — https://www.youtube.com/@JeremysITLab ; NPTEL Computer Networks and Internet Protocol — https://nptel.ac.in/courses/106105183
- **Standards:** RFC 2328 (OSPFv2), RFC 5340 (OSPFv3), RFC 4271 (BGP-4), RFC 4456 (route reflection), RFC 1997 (communities), RFC 6811 (route origin validation), RFC 5880 (BFD), RFC 9568 (VRRPv3), RFC 6164 (/127 links), RFC 4193 (ULA), RFC 6146 and RFC 6147 (NAT64/DNS64) — all at https://www.rfc-editor.org/
- **Routing security:** MANRS — https://manrs.org/ ; Routinator — https://routinator.docs.nlnetlabs.nl/
- **Vendor documentation:** Cisco IOS XE configuration guides — https://www.cisco.com/c/en/us/support/ios-nx-os-software/ios-xe-17/series.html ; Juniper Junos documentation — https://www.juniper.net/documentation/ ; Arista EOS manual — https://www.arista.com/en/um-eos
- **Paid, optional:** Cisco Press CCNA and CCNP ENCOR official cert guides; the free resources above cover the concepts.

## Sources

- Rogers outage review (Xona Partners, executive summary published by the CRTC), reported 5 Jul 2024 — https://mobilesyrup.com/2024/07/05/july-2022-rogers-outage-report-crtc/ (checked 2026-10)
- Meta Engineering, "More details about the October 4 outage" (Oct 2021) — https://engineering.fb.com/2021/10/05/networking-traffic/outage-details/ (checked 2026-10)
- Mondal, Tang, Beckett, Millstein and Varghese, "What do LLMs need to Synthesize Correct Router Configurations?" (arXiv 2307.04945, Jul 2023) — https://arxiv.org/abs/2307.04945 (checked 2026-10)
- BLS Occupational Outlook Handbook, computer network architects (+8%) and network and computer systems administrators (−4%), 2025–35 — https://www.bls.gov/ooh/computer-and-information-technology/computer-network-architects.htm ; https://www.bls.gov/ooh/computer-and-information-technology/network-and-computer-systems-administrators.htm (checked 2026-10)
- Cisco Modeling Labs Free, 5-node limit (CML 2.9 docs) — https://developer.cisco.com/docs/modeling-labs/cml-free/ (checked 2026-10)
- EVE-NG download page: Community Edition 6.2.0-4 "End of Support & End of Life June, 2026" — https://www.eve-ng.net/index.php/download/ (checked 2026-10)
- CERT-In Directions under section 70B(6) of the IT Act, 28 April 2022 (NTP synchronisation) — https://www.cert-in.org.in/PDF/CERT-In_Directions_70B_28.04.2022.pdf (checked 2026-10)

_Last reviewed: 2026-10_
