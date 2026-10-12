# CLD304 · Cloud Networking: VPCs, DNS, Load Balancing and CDNs

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 6 | 4 (≈ 120 hours) | L2 → L3 | [CS215](../../../../02_year_2_core_computer_science/semester_4/CS215_cloud_and_devops_foundations/README.md), [CS212](../../../../02_year_2_core_computer_science/semester_4/CS212_distributed_systems_i/README.md) | [CLD404](../../year_4/CLD404_ai_infrastructure_in_the_cloud_gpus_inference/README.md), [CLD402](../../year_4/CLD402_multi_cloud_hybrid_cloud_and_migration/README.md), [OV01 Cloud Security](../../../../04_overlaps/OV01_cloud_security/README.md) |

Part of the [Cloud Engineering major](../../README.md). Assumes the TCP/IP, TLS, DNS and BGP fundamentals of [CS204 Computer Networks](../../../../02_year_2_core_computer_science/semester_3/CS204_computer_networks/README.md), and builds every lab with your [CLD302](../CLD302_infrastructure_as_code_terraform_opentofu/README.md) modules. Physical routing and switching are covered in [NET301](../../../it_infrastructure_networking/year_3/NET301_routing_and_switching/README.md); this course is about networks you build from cloud APIs.

## Why this course matters now

Most cloud outages, surprise bills and security findings trace back to the network: an empty DNS record took down DynamoDB's regional endpoint in us-east-1 on 19–20 October 2025 ([AWS](https://aws.amazon.com/message/101925/)); a generated configuration file crashed Cloudflare's proxies worldwide on 18 November 2025 ([Cloudflare](https://blog.cloudflare.com/18-november-2025-outage/)); and NAT gateway processing at $0.045 per GB, public IPv4 addresses at $0.005 per hour and cross-AZ transfer quietly dominate many AWS bills ([AWS VPC pricing](https://aws.amazon.com/vpc/pricing/)). The platforms keep changing: AWS added regional NAT gateways in November 2025, and new Azure virtual networks became private by default after 31 March 2026, so VMs no longer get implicit internet access ([Microsoft Learn](https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/default-outbound-access)).

AI assistants can generate a VPC module or a route table in seconds. They routinely produce overlapping CIDRs, routes that black-hole traffic, security groups open to `0.0.0.0/0` and DNS setups that work in one VPC but not across accounts. A network engineer who can read a flow log, run a reachability analysis and explain exactly why a packet was dropped is one of the hardest people to replace on a cloud team.

## Learning outcomes

By the end you can:

1. **Plan** IPv4 and IPv6 address space for an organisation across accounts, regions and on-premises, with no overlaps and room to grow.
2. **Design** VPCs and VNets with tiered subnets, routing, stateful and stateless filtering, and controlled egress, on AWS, Azure and Google Cloud.
3. **Connect** many networks with peering, transit hubs (Transit Gateway, Cloud WAN, Virtual WAN, Network Connectivity Center) and inspection, and **explain** transitive routing.
4. **Expose and consume** services privately with PrivateLink, Private Service Connect and Private Endpoints, including the DNS that makes them work.
5. **Configure** public, private and hybrid DNS with routing policies, resolver endpoints and DNS firewalls.
6. **Choose and configure** L4 and L7 load balancers, CDNs and WAFs for latency, availability and cost.
7. **Build** hybrid connectivity with IPsec VPN and BGP and **design** a redundant dedicated-connection topology.
8. **Troubleshoot** connectivity with flow logs, reachability tools and packet captures, and **calculate** the data-transfer cost of a design.

## Chapters and lessons

### Chapter 1 · Address planning (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 CIDR without a calculator | Prefix lengths, subnetting, summarisation; reserved addresses per subnet (AWS reserves five) | Split a /16 into tiered /20s and /24s by hand |
| 1.2 Private ranges | RFC 1918, RFC 6598 (100.64.0.0/10) for overflow and pod ranges, why `10.0.0.0/16` everywhere breaks mergers | Detect overlaps across 12 VPC ranges with a script |
| 1.3 Organisation IPAM | AWS VPC IPAM pools, Azure IPAM, allocation per region and environment | Design a pool hierarchy for 3 regions × 4 environments |
| 1.4 IPv6 | RFC 8200 basics, /56 per VPC and /64 per subnet, dual-stack and IPv6-only subnets, egress-only gateways, ULA (RFC 4193); public IPv4 is now a metered resource | Build a dual-stack subnet and reach the internet from an IPv6-only instance through DNS64/NAT64 |

**Check your understanding:** (1) Why is a /28 too small for most subnets? (2) What breaks when two acquired companies both use 10.0.0.0/16? (3) Why does IPv6 remove the need for NAT but not for egress control?

### Chapter 2 · VPC and VNet design (weeks 2–3)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Constructs across providers | AWS VPCs are regional with subnets per AZ; Google VPCs are global with regional subnets; Azure VNets are regional with subnets spanning zones | Map one three-tier design to all three |
| 2.2 Routing | Route tables, longest-prefix match, internet gateways, local routes, blackholes | Predict next hops for 10 destinations, then check |
| 2.3 Filtering | Security groups (stateful) versus NACLs (stateless), Azure NSGs and application security groups, Google firewall rules and hierarchical firewall policies | Allow HTTPS in and break return traffic with a NACL; fix it |
| 2.4 Egress | Zonal and regional NAT gateways (AWS, November 2025), Cloud NAT, Azure NAT Gateway; NAT cost per GB; egress proxies and network firewalls | Measure NAT-processed bytes for a workload and price them |
| 2.5 Avoiding NAT | Free gateway endpoints for S3 and DynamoDB, interface endpoints, Private Google Access, service endpoints | Move S3 traffic off NAT and show the cost line drop |

**Check your understanding:** (1) Why can a stateless rule block a response even when the request was allowed? (2) Why does a single NAT gateway create both a cost and an availability problem? (3) What changed for Azure VMs in new VNets after 31 March 2026?

### Chapter 3 · Connecting networks (weeks 4–5)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Peering | VPC and VNet peering, non-transitivity, overlapping-CIDR limits, cross-account and cross-region peering | Peer A–B and B–C and prove A cannot reach C |
| 3.2 Transit hubs | AWS Transit Gateway (attachments, route tables, propagation, segmentation), AWS Cloud WAN, Azure Virtual WAN, Google Network Connectivity Center | Build prod/non-prod/shared-services segmentation on a transit hub |
| 3.3 Shared networks | Shared VPC (Google), AWS Resource Access Manager subnet sharing, hub-and-spoke VNets | Share subnets to two workload accounts |
| 3.4 Centralised inspection | Inspection VPCs, Gateway Load Balancer, symmetric routing, appliance mode | Route east–west traffic through a firewall and keep it symmetric |
| 3.5 Overlapping ranges | Private NAT, NAT between networks, re-addressing plans | Connect two overlapping VPCs through private NAT |

**Check your understanding:** (1) Why does transit routing need explicit route-table design for segmentation? (2) What causes asymmetric routing through a stateful firewall? (3) When is peering still better than a hub?

### Chapter 4 · Private access to services (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Interface endpoints | AWS PrivateLink, Google Private Service Connect, Azure Private Endpoint; per-AZ ENIs; endpoint policies | Reach a cloud API with no internet path at all |
| 4.2 Publishing your own service | Endpoint services behind an NLB, Private Link Service, PSC producer; SaaS connectivity patterns | Expose an API from one account to another privately |
| 4.3 DNS for private endpoints | Private hosted zones, Azure private DNS zones, split-horizon pitfalls | Fix a private endpoint that resolves to the public IP |
| 4.4 Service networks | Amazon VPC Lattice for service-to-service connectivity and auth across VPCs and accounts | Connect two services in different accounts through a service network |

**Check your understanding:** (1) Why does a private endpoint often fail because of DNS rather than routing? (2) What does an endpoint policy add beyond IAM? (3) When would you choose PrivateLink over peering?

### Chapter 5 · DNS (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Resolution end to end | Stub, recursive and authoritative servers; TTLs and negative caching; the VPC resolver | Trace a lookup with `dig +trace` and explain each hop |
| 5.2 Routing policies | Route 53 weighted, latency, failover, geolocation, geoproximity; health checks; Cloud DNS routing policies; Azure Traffic Manager | Fail a region over with health-checked DNS and time it |
| 5.3 Hybrid DNS | Route 53 Resolver inbound/outbound endpoints and rules, Azure DNS Private Resolver, Cloud DNS forwarding and peering zones | Resolve an on-premises name from the cloud and back |
| 5.4 DNS security and failure | DNSSEC, DNS Firewall, DNS as a dependency; the October 2025 empty-record outage | Write a DNS dependency map for P3 |

**Check your understanding:** (1) Why does DNS failover take longer than the TTL? (2) What can a DNS firewall stop that a security group cannot? (3) Why can a DNS automation bug take down services that never changed?

### Chapter 6 · Load balancing (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 L4 and L7 | Connection versus request balancing; AWS NLB, ALB, GWLB; Azure Load Balancer and Application Gateway; Google passthrough and proxy Network LBs, global external Application LB with anycast | Pick a load balancer for gRPC, WebSockets, raw TCP and static IPs |
| 6.2 Health and draining | Health checks, slow start, deregistration delay, connection draining | Deploy during load and show zero dropped connections |
| 6.3 TLS | Termination versus pass-through, certificates (ACM, Key Vault, Certificate Manager), mTLS, HTTP/2 and HTTP/3 | Enable mTLS on an L7 load balancer |
| 6.4 Cross-zone behaviour | Cross-zone balancing, inter-AZ transfer charges, zonal shift, client IP preservation and proxy protocol | Measure inter-AZ bytes with cross-zone on and off |

**Check your understanding:** (1) Why can't an L4 load balancer route by URL path? (2) What does cross-zone balancing cost on AWS? (3) Why does a global anycast load balancer change your failure model?

### Chapter 7 · The edge: CDN, WAF and DDoS (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 CDNs | CloudFront, Cloud CDN, Azure Front Door, Cloudflare; cache keys, TTLs, origin shield, invalidation, signed URLs | Raise the cache-hit ratio of a site from under 50% to over 90% |
| 7.2 WAF | Managed rule sets, rate limiting, bot control, false positives, count mode before block | Deploy a WAF in count mode, review logs, then block |
| 7.3 DDoS and global entry | AWS Shield, Google Cloud Armor, Azure DDoS Protection; anycast, Global Accelerator | Design an entry layer for a cricket-final ticket sale |
| 7.4 Edge as a dependency | Hotstar's CDN-based external gateway; the Cloudflare November 2025 outage | Write a failure-mode table for your edge layer |

**Check your understanding:** (1) Why can a bad cache key leak one user's page to another? (2) Why run a WAF in count mode first? (3) What is your plan if your CDN provider fails?

### Chapter 8 · Hybrid connectivity (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 IPsec VPN | Site-to-site tunnels, IKEv2, two tunnels per connection, HA VPN on Google Cloud | Build a VPN between a cloud VPC and a VM running strongSwan |
| 8.2 BGP for cloud engineers | ASNs, advertisements, local preference, AS-path prepending, MED, BFD | Steer traffic to a primary tunnel with prepending and fail over |
| 8.3 Dedicated connections | AWS Direct Connect, Azure ExpressRoute, Google Cloud Interconnect and Cross-Cloud Interconnect; dedicated versus partner; MACsec | Design 99.99% connectivity from two Indian data centres to two regions |
| 8.4 Hybrid DNS and routing at scale | Route limits, summarisation, transitive routing through the cloud | Calculate route counts for your design against quotas |

**Check your understanding:** (1) Why does a VPN need two tunnels and BGP rather than static routes? (2) What single failure does a "redundant" connection in one colocation facility not survive? (3) Why summarise routes?

### Chapter 9 · Kubernetes and service networking (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Pod IPs in a VPC | VPC-native pods (AWS VPC CNI, Azure CNI, GKE VPC-native), IP exhaustion, prefix delegation, overlay modes, IPv6 clusters | Exhaust a subnet with pods, then fix it with prefix delegation or a secondary range |
| 9.2 Cluster ingress and egress | Gateway API backed by cloud load balancers, egress gateways, fixed egress IPs for partner allow-lists | Give a cluster a stable egress IP for a bank partner |
| 9.3 East–west traffic | Service meshes in outline, VPC Lattice and multi-cluster services; when a mesh is worth it (deep dive in BE404) | Write a one-page mesh/no-mesh decision |

**Check your understanding:** (1) Why do VPC-native pods use up subnet space so fast? (2) Why do banks ask for fixed source IPs, and what does that cost you? (3) What does a mesh give you that NetworkPolicy does not?

### Chapter 10 · Troubleshooting and cost (weeks 12–13)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Visibility | VPC Flow Logs, Traffic Mirroring, Reachability Analyzer and Network Access Analyzer, Google Connectivity Tests, Azure Network Watcher | Find a planted drop with flow logs and confirm with a reachability check |
| 10.2 Classic failures | MTU and PMTUD black holes, asymmetric routing, ephemeral port NACLs, SNAT port exhaustion, DNS search domains | 10 timed break-fix scenarios (no AI) |
| 10.3 Data-transfer economics | Internet egress (first 100 GB a month free on AWS), inter-AZ at $0.01 per GB each way, NAT processing, endpoints, CDN offload | Price the arrows in your P3 diagram and cut the bill by 30% |
| 10.4 Network as code and tests | Network modules, policy tests for open ports, reachability assertions in CI | Add an "no `0.0.0.0/0` on port 22" test and a reachability test to CI |

**Check your understanding:** (1) Why do large packets fail while ping works? (2) Why can a busy NAT gateway drop new connections while CPU is low? (3) Which single change usually cuts NAT cost the most?

### Chapter 11 · AI and networking (week 14)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Reviewing generated network code | Overlaps, open rules, missing routes, wrong endpoint DNS; automated checks before apply | Run your Chapter 10 checks on 10 AI-generated network modules and tally defects |
| 11.2 Agents in network operations | Incident agents reading flow logs and configs; read-only access; verifying a suggested root cause | Compare an agent's diagnosis with yours on three faults |
| 11.3 Networks for AI clusters (preview) | Why training needs EFA or InfiniBand and inference needs fast egress and private model endpoints (CLD404) | Draw the network for a private model endpoint used from Mumbai |

**Check your understanding:** (1) Which network mistakes can static analysis catch, and which only a live test can? (2) What evidence do you need before accepting an agent's root cause? (3) Why do model endpoints add new egress and DNS paths to secure?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1: address plan and IPv6 | Plan + overlap checker |
| 2 | 2 | Lab 2: three-provider VPC mapping | Diagrams |
| 3 | 2 | Lab 3: egress and endpoints | NAT cost before/after; P1 starts |
| 4 | 3 | Lab 4: peering and transit | Segmentation proof; P1 due |
| 5 | 3 | Lab 4 continued: inspection | Symmetric firewall path |
| 6 | 4 | Lab 5: PrivateLink/PSC and DNS | Private API across accounts; P2 starts |
| 7 | 5 | Lab 6: DNS failover and hybrid DNS | Failover timing |
| 8 | 6 | Lab 7: load balancers and draining | Zero-drop deploy |
| 9 | 7 | Lab 8: CDN and WAF | Cache-hit report; P2 due |
| 10 | 8 | Lab 9: VPN with BGP | Failover by prepending |
| 11 | 9 | Pod IP exhaustion lab | Fix evidence; P3 starts |
| 12 | 10 | Lab 10: break-fix drills | Scenario times |
| 13 | 10 | P3 build and cost model | Priced diagram |
| 14 | 11 | P3 completion | Demo and review |
| 15 | Review and exam | — | Written exam and troubleshooting practical |

## Working with AI in this course

- **Use AI for:** subnet maths checks (after you do them yourself), drafting network modules, translating designs between providers, summarising flow-log queries, writing `dig`/`mtr` test scripts, and explaining unfamiliar BGP output. Named tools: Claude Code, GitHub Copilot, Amazon Q Developer, Gemini Cloud Assist, Azure Copilot.
- **Do without AI (drills):** CIDR planning, predicting route-table next hops, the break-fix scenarios in Chapter 10, and pricing a design's data transfer.
- **Verify AI output by:** running reachability analysis or connectivity tests before and after every change; scanning for overlapping CIDRs and open ports in CI; resolving every private endpoint name from every VPC that needs it; reading the pricing page for every data path it proposes.
- **Where AI still fails here (show it):** ask an assistant for a hub-and-spoke design for six accounts and check for overlapping ranges, missing return routes and non-transitive peering assumptions. Ask it why a private endpoint returns a public IP and see whether it asks about DNS. Record each miss for your P3 report.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs | 25% |
| Projects P1 / P2 / P3 | 5% / 15% / 25% |
| Written exam (addressing, routing, DNS, load balancing, cost) | 15% |
| Troubleshooting practical (no AI) | 15% |

**Mastery gate:** you pass when you can, without AI help, (a) produce a non-overlapping address plan for a given organisation in 30 minutes; (b) find and fix four planted faults (routing, filtering, DNS, MTU or NAT) in an unfamiliar multi-VPC environment within 60 minutes, explaining the evidence for each; and (c) price the monthly data-transfer cost of a given architecture to within 20% of the actual bill.

## Industry reality

Large Indian platforms depend on careful edge and network design: Disney+ Hotstar describes a request path of CDN-based external gateway, internal gateway behind Application Load Balancers, then services and databases, and scaled it for 59 million concurrent streams ([Hotstar](https://blog.hotstar.com/scaling-infrastructure-for-millions-from-challenges-to-triumphs-part-1-6099141a99ef)). Banks and payment companies connect to partners through allow-listed IPs and private links, and regulated entities must keep data within India, which shapes region and interconnect choices. Network engineers who know cloud APIs are scarce because the role needs both classic networking (BGP, MTU, DNS) and cloud constructs.

Interview questions from this course:

1. **"Design the network for 30 accounts in two regions, with on-premises connectivity."** Cover IPAM, transit hub with segmentation, shared services, inspection, hybrid DNS, dedicated connectivity with redundancy, and egress control.
2. **"An instance in a private subnet cannot reach an S3 bucket. Debug it."** Cover route tables, NAT or gateway endpoint, endpoint and bucket policies, security groups and NACLs, DNS, and reachability tools.
3. **"Our NAT gateway bill doubled. What do you do?"** Cover flow-log analysis of top talkers, endpoints for cloud services, regional or zonal NAT design, cross-AZ paths, and image-pull caching.
4. **"When would you use an NLB versus an ALB, and why?"** Cover L4 versus L7, static IPs, TLS pass-through, gRPC and WebSockets, client IP preservation, health checks and cost.
5. **"Walk me through what happens when a user in Chennai opens our site."** Cover DNS resolution and routing policy, CDN edge, TLS, load balancer, target selection, private service calls, and where latency and failures occur.

## Resources (free first)

- **Documentation:** [Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html), [Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html), [Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html), [Google Cloud VPC](https://docs.cloud.google.com/vpc/docs/overview), [Cloud Load Balancing](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview), [Azure Virtual Network](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview), [Azure networking design guide: outbound egress](https://learn.microsoft.com/en-us/azure/networking/design-guide/outbound-egress).
- **Whitepapers:** [Building a Scalable and Secure Multi-VPC AWS Network Infrastructure](https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/welcome.html); [Hybrid connectivity](https://docs.aws.amazon.com/whitepapers/latest/hybrid-connectivity/hybrid-connectivity.html).
- **Standards:** [RFC 1918](https://www.rfc-editor.org/rfc/rfc1918), [RFC 6598](https://www.rfc-editor.org/rfc/rfc6598), [RFC 8200](https://www.rfc-editor.org/rfc/rfc8200), [RFC 4193](https://www.rfc-editor.org/rfc/rfc4193), [RFC 4271 (BGP-4)](https://www.rfc-editor.org/rfc/rfc4271).
- **Practice:** [containerlab](https://containerlab.dev/) for free local BGP and routing labs; [Killercoda](https://killercoda.com/) for Kubernetes networking.
- **Practising without a big bill:** do Chapters 1, 8 (BGP) and 10 locally with containerlab and strongSwan. In the cloud, peering, route tables, security groups and gateway endpoints are free, but NAT gateways, Transit Gateway attachments, interface endpoints, load balancers and public IPv4 addresses are billed by the hour: create them only inside a timed session, tag them with a TTL and run a destroy job.
- **Paid, worth it:** *AWS Certified Advanced Networking Official Study Guide* (Wiley) for depth on hybrid design, even if you never take the exam.

## Sources

All checked 12 Oct 2026.
- [AWS VPC pricing](https://aws.amazon.com/vpc/pricing/) (NAT gateway $0.045/h and $0.045/GB in US East (Ohio); public IPv4 $0.005/h; regional NAT gateway $0.045/h per AZ).
- [AWS regional NAT gateway](https://aws.amazon.com/about-aws/whats-new/2025/11/aws-nat-gateway-regional-availability/) (Nov 2025) and [docs](https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateways-regional.html).
- [EC2 on-demand pricing: data transfer](https://aws.amazon.com/ec2/pricing/on-demand/) (inter-AZ and internet egress rates).
- [Azure default outbound access](https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/default-outbound-access).
- [AWS us-east-1 event, Oct 2025](https://aws.amazon.com/message/101925/); [Cloudflare outage, Nov 2025](https://blog.cloudflare.com/18-november-2025-outage/).
- [Disney+ Hotstar scaling, part 1](https://blog.hotstar.com/scaling-infrastructure-for-millions-from-challenges-to-triumphs-part-1-6099141a99ef).
- Google Cloud Interconnect colocation facilities in Mumbai and Delhi: [choosing colocation facilities](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/choosing-colocation-facilities).

_Last reviewed: 2026-10_
