# CLD304 · Labs and projects

Build everything with your CLD302 modules. Hourly-billed parts (NAT gateways, Transit Gateway attachments, interface endpoints, load balancers, VPN connections, public IPv4 addresses) exist only during timed sessions and carry a `ttl` tag that a nightly job enforces. Lab 10 and the address-planning parts of Lab 1 are done without AI.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Address plan and IPv6 | Plan ranges for 3 regions × 4 environments plus on-premises; write an overlap checker; build one dual-stack and one IPv6-only subnet | Plan table, checker code with tests, and proof of IPv6-only egress via DNS64/NAT64 | 4 h |
| 2 · One design, three clouds | Build the same three-tier network on two providers and draw the third | Diagrams and a construct mapping table (regional vs global VPC, subnet scope, firewall model) | 4 h |
| 3 · Egress and endpoints | Measure NAT-processed bytes for a workload pulling images and reading S3; add gateway and interface endpoints | Bytes and estimated cost before and after; endpoint policies | 3 h |
| 4 · Peering, transit and inspection | Peer three VPCs to show non-transitivity; rebuild with a transit hub with prod/non-prod segmentation and a firewall inspection VPC | Reachability matrix (who can reach whom) and proof of symmetric firewall routing | 6 h |
| 5 · Private services | Publish an API from account A to account B with PrivateLink or Private Service Connect; fix a planted DNS problem | Working private call, and the DNS fix explained | 4 h |
| 6 · DNS failover and hybrid DNS | Health-checked failover between two regions; resolver endpoints between cloud and a simulated on-premises DNS | Failover timeline (detection, DNS change, client switch) and resolution tests both ways | 4 h |
| 7 · Load balancers | Compare an L4 and an L7 load balancer for gRPC and WebSockets; deploy during load with draining; measure cross-zone bytes | Results table and zero-drop deployment evidence | 4 h |
| 8 · CDN and WAF | Put a CDN and WAF in front of a site; fix cache keys; run WAF in count mode, then block | Cache-hit ratio before/after, WAF log review with false positives handled | 4 h |
| 9 · VPN with BGP | IPsec tunnels from a cloud VPC to a strongSwan/FRR VM; steer with AS-path prepending; fail a tunnel | BGP tables, failover time, and configuration | 5 h |
| 10 · Break-fix drills (no AI) | Ten planted faults: MTU black hole, asymmetric route, NACL ephemeral ports, wrong endpoint DNS, missing return route, SNAT exhaustion, SG reference loop, blackholed TGW route, IPv6 route missing, DNS search domain | Time and evidence per fault | 5 h |

## Projects

### P1 · Address plan and landing-zone network (L1, ~6 hours)

**Real-world inspiration:** [AWS VPC IPAM](https://docs.aws.amazon.com/vpc/latest/ipam/what-it-is-ipam.html) and the [multi-VPC network whitepaper](https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/welcome.html) describe how organisations avoid overlapping ranges as they grow.

**What to build:** an IPAM pool hierarchy (or a documented plan where IPAM is not available) for your CLD301 landing zone, and network modules that allocate from it: a two-AZ VPC per workload account with public, private and data subnets, dual-stack, and endpoints instead of NAT where possible.

**Acceptance criteria:**
- No overlaps across 12 planned networks, verified by your checker in CI.
- Each VPC is created from IaC with allocations pulled from the plan, not typed by hand.
- Private subnets reach S3 (or the equivalent) with no NAT gateway in the path; show the route.
- **Cost ceiling:** US$3.

**Stretch goals:** IPv6-only workload subnet; a CI check that refuses any new range not taken from the pool.

**What it proves to an employer:** you plan networks that will not need re-addressing in two years.

### P2 · Private, multi-account service connectivity with hybrid DNS (L2, ~15 hours)

**Real-world inspiration:** payment and banking partners in India commonly require private connectivity or fixed source IPs; providers' private connectivity products ([AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html), [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect), [Azure Private Link](https://learn.microsoft.com/en-us/azure/private-link/private-link-overview)) exist for this. The scenario is *illustrative*: a lending app calling a credit-bureau API and an internal KYC service in another account, with an on-premises core system.

**What to build:** a transit hub with segmented route tables; an internal KYC service published privately to two consumer accounts; a stable egress IP path for a partner allow-list; Route 53 Resolver (or equivalent) endpoints with forwarding rules to a simulated on-premises DNS; DNS Firewall blocking a test domain; flow logs to a central account.

**Acceptance criteria:**
- A reachability matrix of 20 source–destination pairs matches the intended policy 100%, checked with reachability tooling, not just pings.
- The KYC API is reachable from consumers only through the private endpoint; a direct path attempt is blocked and visible in flow logs.
- Partner-bound traffic always leaves from the same documented IP addresses across an AZ failure.
- On-premises names resolve from the cloud and cloud private names from on-premises; the blocked test domain returns the firewall response.
- **Cost ceiling:** US$15; tear down hourly components after each session.

**Stretch goals:** VPC Lattice service network with IAM auth policies; IPv6 for the internal services.

**What it proves to an employer:** you can build the private, auditable connectivity regulated companies and their partners require.

### P3 · A global entry layer with failover, hybrid link and a cost model (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:**
- Disney+ Hotstar's request path for live cricket: CDN-based external gateway, internal gateways behind ALBs, then services ([Hotstar](https://blog.hotstar.com/scaling-infrastructure-for-millions-from-challenges-to-triumphs-part-1-6099141a99ef)).
- The October 2025 AWS DNS failure and the November 2025 Cloudflare outage, which show the edge and DNS as dependencies.
- The workload is an *illustrative scenario*: a ticketing site for a cricket final with buyers across India and the Gulf.

**What to build:**
- two regions (for example Mumbai and Hyderabad) with an app tier behind L7 load balancers;
- a CDN and WAF in front, with rate limiting on the purchase path;
- health-checked DNS failover (or a global anycast load balancer) between regions;
- a site-to-site VPN with BGP to a simulated payment-partner data centre;
- full flow logging and a cost model for 1 million page views and 50,000 purchases.

**Acceptance criteria:**
- **Region failover:** with the primary region's app tier stopped, users are served from the secondary within 3 minutes, measured by a synthetic client every 10 seconds.
- **Edge:** cache-hit ratio of at least 90% on static assets; WAF blocks a scripted burst of 1,000 requests per minute from one IP on the purchase path while normal users succeed.
- **Hybrid:** the partner path fails over between two tunnels with BGP in under 60 seconds and no manual change.
- **Cost model:** a priced diagram showing every data-transfer arrow (edge egress, origin fetch, inter-AZ, inter-region, NAT, VPN) and a validated estimate within 20% of the measured bill for a scaled-down test run.
- **AI review:** an AI-generated version of the network module set, with a table of defects your CI checks and reachability tests caught.
- **Cost ceiling:** US$40 total.

**Stretch goals:** IPv6 end to end from browser to app tier; a "CDN down" plan with a second CDN or direct origin path; an SNAT-exhaustion load test and fix.

**What it proves to an employer:** you can design, test and price a resilient global network, the core skill behind cloud network engineer and solutions architect roles.

## Feeds into

- [CLD404 AI Infrastructure in the Cloud](../../year_4/CLD404_ai_infrastructure_in_the_cloud_gpus_inference/README.md): cluster networking for training and inference.
- [CLD402 Multi-Cloud, Hybrid Cloud and Migration](../../year_4/CLD402_multi_cloud_hybrid_cloud_and_migration/README.md): hybrid connectivity at migration scale.
- [CLD403 FinOps](../../year_4/CLD403_finops_and_cloud_cost_engineering/README.md): data-transfer cost engineering.
- [OV01 Cloud Security](../../../../04_overlaps/OV01_cloud_security/README.md) and [NET402 Network Security Engineering](../../../it_infrastructure_networking/year_4/NET402_network_security_engineering/README.md): segmentation and inspection.
