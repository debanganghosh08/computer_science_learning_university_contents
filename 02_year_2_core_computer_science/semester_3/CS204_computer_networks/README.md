# CS204 · Computer Networks

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 2 · 3 | 4 (≈ 120 hours) | L1 → L3 | [FND102](../../../01_year_1_foundations/semester_1/FND102_how_computers_work_bits_hardware/README.md), [FND104](../../../01_year_1_foundations/semester_1/FND104_the_developers_toolkit_linux_shell_git/README.md) | [CS212](../../semester_4/CS212_distributed_systems_i/README.md), [CS213](../../semester_4/CS213_security_foundations/README.md), [CS215](../../semester_4/CS215_cloud_and_devops_foundations/README.md), [NET301](../../../03_majors/it_infrastructure_networking/year_3/NET301_routing_and_switching/README.md), [NET303](../../../03_majors/it_infrastructure_networking/year_3/NET303_network_automation_and_netdevops/README.md) |

## Why this course matters now

India runs some of the largest network workloads on Earth. UPI processed 24.51 billion transactions in August 2026, an average of about 9,150 per second (24.51 billion ÷ 31 days ÷ 86,400 s), and JioHotstar reported a peak of 6.12 crore (61.2 million) concurrent viewers for the 2025 Champions Trophy final. India also had the highest IPv6 share of any country in Cloudflare's 2025 measurements: 67% of dual-stack requests from India arrived over IPv6. The protocols underneath are changing: HTTP/3 over QUIC carried 21% of requests on Cloudflare's network in 2025, and by December 2025 more than half of human web traffic to Cloudflare used post-quantum key agreement. AI assistants now decode packet captures and write socket code in seconds, but they cannot see your network. The engineer who can reason from the RFC, read the capture, compute the bandwidth-delay product and find the one misconfigured hop is the one who fixes the outage.

## Learning outcomes

By the end you can:

1. **Explain** every step of loading a web page, from DNS to rendering, and **attribute** its latency to DNS, TCP, TLS, server time and transfer using real measurements.
2. **Write** robust TCP and UDP clients and servers with the sockets API, including framing, timeouts and event-driven concurrency.
3. **Implement** a reliable byte-stream transport (reassembly, flow control, retransmission) that passes tests under loss and reordering.
4. **Compare** congestion-control algorithms (CUBIC, BBR) under controlled delay and loss, and **explain** bufferbloat and active queue management.
5. **Analyse** TLS 1.3, QUIC and HTTP/3 handshakes in Wireshark and **explain** what each round trip achieves.
6. **Design** IPv4 and IPv6 addressing plans, and **implement** longest-prefix-match forwarding.
7. **Explain** link-state, distance-vector and BGP routing, including how a route leak or withdrawal can take a company offline.
8. **Debug** broken networks layer by layer with `dig`, `curl`, `ss`, `mtr`, `tcpdump` and Wireshark, and **plan** capacity for a large live event.

## Chapters and lessons

### Chapter 1 · How the Internet is built (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Packets and layers | Packet switching; the Internet's five layers vs OSI; encapsulation | Capture one page load in Wireshark; label every header |
| 1.2 Performance vocabulary | Propagation, transmission, queuing and processing delay; throughput; bandwidth-delay product; Little's law | Compute the BDP for a 1 Gbit/s Mumbai–Singapore path; measure its RTT |
| 1.3 A network of networks | ISPs, autonomous systems, transit vs peering, internet exchanges (NIXI in India), submarine cables | Traceroute to 5 sites; map each hop to its AS |
| 1.4 Measurement toolkit | `ping`, `mtr`, `dig`, `curl -w` timings, `iperf3`, `ss` | "Why is this site slow?" breakdown: DNS, connect, TLS, first byte, transfer |

**Check your understanding:** Why does doubling bandwidth barely speed up loading a small page from far away? Why can a traceroute hop show high latency while later hops look fine? What does peering at an internet exchange change for users?

### Chapter 2 · HTTP and the application layer (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 HTTP semantics | Methods, status codes, headers, idempotency, content negotiation (RFC 9110) | Send raw HTTP/1.1 requests with `nc` and read every response header |
| 2.2 HTTP/1.1 and HTTP/2 | Persistent connections; HTTP/2 binary framing, streams, HPACK; TCP head-of-line blocking (RFC 9113) | Compare one page over h1 and h2 in browser dev tools |
| 2.3 Caching | `Cache-Control`, `ETag`, revalidation, shared vs private caches, `stale-while-revalidate` (RFC 9111) | Set cache headers on a static site; prove behaviour with `curl` |
| 2.4 APIs and real time | REST conventions, WebSockets, Server-Sent Events, gRPC over HTTP/2 | A small SSE price-ticker server and client |

**Check your understanding:** Why is `PUT` idempotent but `POST` not, and why do payment APIs care? What problem does HTTP/2 multiplexing solve, and which one does it leave? When can a CDN serve a response without contacting the origin?

### Chapter 3 · DNS and content delivery (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 How DNS works | Root, TLD and authoritative servers; recursive resolvers; A, AAAA, CNAME, MX, TXT, NS, SOA, HTTPS records; TTLs | `dig +trace` five domains; draw each resolution path |
| 3.2 Securing DNS | Cache poisoning (concept), DNSSEC chain of trust, DNS over TLS and HTTPS (RFC 7858, RFC 8484) | Validate a signed domain with `dig +dnssec` |
| 3.3 CDNs and anycast | Edge caches, anycast routing, GeoDNS, hit ratio, origin shielding | Measure latency to two anycast resolvers from two networks |
| 3.4 When DNS fails | Meta's October 2021 outage: a maintenance command cut its backbone, its DNS servers then withdrew their BGP routes, and its domains stopped resolving | Write the incident timeline and two mitigations |

**Check your understanding:** Why does lowering a TTL before a migration matter, and what does it cost? What does DNSSEC protect, and what does it not hide? How did a routing change make DNS look broken?

### Chapter 4 · Sockets programming (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 The sockets API | `socket`, `bind`, `listen`, `accept`, `connect`; TCP vs UDP sockets; `getaddrinfo` for IPv4 and IPv6 | Echo client and server in C and Python |
| 4.2 Framing and byte order | A TCP stream has no message boundaries; length prefixes, delimiters; `htons`; partial reads and writes | Framed chat protocol with tests that deliver one byte at a time |
| 4.3 Server concurrency | Threads, `select`/`poll`/`epoll`, async runtimes (asyncio, Go); the C10K problem | Load-test three server designs with `wrk` or `oha` |
| 4.4 Timeouts and failure | Connect and read timeouts, keepalive, FIN vs RST, half-close, `SO_REUSEADDR`, graceful shutdown | Inject delay and loss with `tc netem`; keep the server healthy |

**Check your understanding:** Why does a server that calls `recv` once per message work on localhost and fail on a real network? Why does a restarted server sometimes fail with "address already in use"? What should a client do when a read times out on a non-idempotent request?

### Chapter 5 · Reliable transport and TCP (weeks 5–6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Reliability from scratch | Checksums, ACKs, stop-and-wait, Go-Back-N, selective repeat | Simulate each under 5% loss; compare throughput |
| 5.2 TCP connections | Segment format, sequence numbers, three-way handshake, FIN, RST, TIME_WAIT, the state machine (RFC 9293) | Capture and annotate a full connection lifecycle |
| 5.3 Receiver and flow control | Reassembly, receive window, window scaling, SACK | Stream reassembler and TCP receiver (Stanford CS144 style) |
| 5.4 Sender and timers | RTT estimation and RTO (RFC 6298), exponential back-off, fast retransmit | TCP sender passing the lab's test suite |
| 5.5 Small-packet traps | Nagle's algorithm meets delayed ACKs; buffer sizes; reading `ss -ti` | Reproduce a ~40 ms stall; fix it with `TCP_NODELAY` |

**Check your understanding:** Why does TCP need both sequence numbers and a receive window? Why does TIME_WAIT exist, and why is it on the side that closes first? How does a duplicate ACK signal loss faster than a timeout?

### Chapter 6 · Congestion control (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 The problem | Congestion collapse, AIMD, fairness, slow start, congestion window | Plot `cwnd` over time from a simulation |
| 6.2 Loss-based control | Reno, NewReno, CUBIC (RFC 9438, the Linux default) | `iperf3` under `netem` delay and loss; record `cwnd` with `ss` |
| 6.3 Model-based control | BBR: estimate bottleneck bandwidth and minimum RTT; its IETF draft status | CUBIC vs BBR on a lossy, long-RTT emulated link |
| 6.4 Queues and latency | Bufferbloat; CoDel (RFC 8289), fq_codel (RFC 8290); ECN (RFC 3168) | Latency under load with and without fq_codel |

**Check your understanding:** Why does loss-based control fill buffers, and who pays for it? Why can BBR outperform CUBIC on a path with random (non-congestion) loss? What does ECN let a router do instead of dropping packets?

### Chapter 7 · TLS, QUIC and HTTP/3 (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 TLS 1.3 | Handshake (RFC 8446), key exchange and forward secrecy, certificates, chain validation, SNI, resumption, 0-RTT replay risk | Decrypt your own browser session in Wireshark using `SSLKEYLOGFILE` |
| 7.2 Certificates in practice | ACME and Let's Encrypt, Certificate Transparency, expiry outages; hybrid post-quantum key exchange (X25519 + ML-KEM) | Inspect a chain with `openssl s_client`; look the domain up in CT logs |
| 7.3 QUIC | Transport over UDP (RFC 9000/9001/9002), independent streams, connection IDs and migration, encrypted transport headers | Record a qlog; visualise the handshake in qvis |
| 7.4 HTTP/3 | QPACK, discovery through `Alt-Svc` and HTTPS records, fallback to TCP when UDP is blocked (RFC 9114) | `curl --http3` vs `--http2` on a lossy link |

**Check your understanding:** Why does TLS 1.3 need one round trip where TLS 1.2 needed two? Why was QUIC built on UDP rather than as a new kernel transport? What does connection migration give a phone user moving from Wi-Fi to mobile data?

### Chapter 8 · IP and forwarding (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 IPv4 addressing | Header fields, CIDR, subnetting, private ranges, NAT and carrier-grade NAT | 20 subnetting problems, AI off |
| 8.2 IPv6 | Header (RFC 8200), address types, SLAAC, neighbour discovery, dual stack, Happy Eyeballs | Check your connection's IPv6 path; enable IPv6 in a home lab |
| 8.3 Forwarding | Longest-prefix match, router architecture, TTL, ICMP, MTU and path-MTU discovery | Binary-trie longest-prefix match; benchmark 10⁶ lookups |
| 8.4 The first hop | DHCP, ARP and neighbour discovery, default gateways | Capture DHCP and ARP when a laptop joins a network |

**Check your understanding:** Why did NAT extend IPv4's life, and what did it break? Why does a blocked ICMP "packet too big" message cause connections that hang only for large responses? Why is longest-prefix match harder than exact-match lookup?

### Chapter 9 · Routing (weeks 10–11)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Link-state | Dijkstra (see [CS201](../CS201_algorithms_and_complexity/README.md)), OSPF areas and LSAs | Implement link-state routing in a simulator |
| 9.2 Distance-vector | Bellman-Ford, RIP, count-to-infinity, split horizon | Simulate and break, then fix, count-to-infinity |
| 9.3 BGP | Path-vector routing, policy (customer, peer, provider), route leaks and hijacks, RPKI route-origin validation (RFC 6811) | Read real routes on a looking glass; check a prefix's ROV status |
| 9.4 Data-centre routing and SDN | Control vs data plane, ECMP, Clos fabrics, the SDN idea | ECMP across a leaf-spine topology in containerlab or Mininet |

**Check your understanding:** Why does BGP choose routes by policy rather than shortest path? What is the difference between a route leak and a hijack, and what does RPKI catch? Why do data centres use many equal-cost paths instead of one big link?

### Chapter 10 · Link layer, LANs and data centres (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Ethernet and switching | Frames, MAC addresses, CRC, MAC learning, VLANs (802.1Q), spanning tree | Build a two-VLAN topology and prove isolation |
| 10.2 Wireless and cellular | 802.11 CSMA/CA, hidden terminals, Wi-Fi 6/7 ideas; the 4G/5G core at a high level | Measure latency and jitter on Wi-Fi vs wired |
| 10.3 Data-centre fabrics | Leaf-spine, oversubscription, RDMA over Converged Ethernet and InfiniBand for AI training (concepts) | Compute bisection bandwidth for a given fabric |
| 10.4 Virtual networks | Linux bridges, `veth` pairs, network namespaces, VXLAN overlays | Connect two namespaces through a bridge with NAT to the Internet |

**Check your understanding:** Why does a switch flood a frame for an unknown MAC address? Why do Wi-Fi devices avoid collisions instead of detecting them? Why do AI training clusters care so much about tail latency in the network?

### Chapter 11 · Networks at scale and in operations (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Load balancing | L4 vs L7 balancing, consistent hashing, health checks, connection draining | Compare an L7 proxy (HAProxy or Nginx) with a minimal L4 proxy |
| 11.2 Designing for India-scale peaks | Adaptive bitrate streaming (HLS/DASH), multi-CDN, capacity arithmetic for live cricket and payments | Back-of-envelope capacity plan for a live event (illustrative scenario) |
| 11.3 Debugging method | Layer-by-layer isolation, `tcpdump` filters, MTU black holes, conntrack and ephemeral-port exhaustion | Diagnose 5 broken-network scenarios |
| 11.4 Defensive basics | Stateful firewalls with `nftables`, DDoS concepts and mitigations (anycast absorption, rate limiting), zero-trust idea | Firewall policy for a web server; verify it by scanning only your own VM |

**Check your understanding:** Why does consistent hashing reduce cache misses when a node is added? Six crore people press play in the same minute: which layer fails first, and how would you know? Why is "it's always DNS" a useful first check, and when is it a trap?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Measurement toolkit | — |
| 2 | 2 | Lab 2 · HTTP by hand | — |
| 3 | 3 | Lab 3 · DNS resolver | **P1 due** |
| 4 | 4 | Lab 4 · Framed chat server | — |
| 5 | 5 | Lab 5 · Reassembler and receiver | — |
| 6 | 5 | Lab 6 · TCP sender | — |
| 7 | 6 | Lab 7 · Congestion experiments | Mid-term (AI off) |
| 8 | 7 | Lab 8 · TLS and QUIC captures | — |
| 9 | 8 | Lab 9 · Longest-prefix match | **P2 due** |
| 10 | 9 | Lab 10 · Routing simulator | — |
| 11 | 9 | P3 | — |
| 12 | 10 | Namespaces and VLANs (part of Lab 10) | — |
| 13 | 11 | P3 | — |
| 14 | 11 | Debugging scenarios | **P3 due** |
| 15 | Review | Oral defence of P3 | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** explaining a field in a packet capture; summarising an RFC section (then reading that section yourself); writing socket boilerplate, load-test scripts and `tc netem` experiment scripts; turning a messy `tcpdump` into a timeline you then check.
- **Do without AI (drills):** subnetting; decoding IPv4, TCP and DNS headers from hex; tracing TCP state transitions; bandwidth-delay and latency arithmetic; building a routing table by hand. These are on the exams.
- **Verify AI output by:** the RFC text on rfc-editor.org (quote the section number); a capture of the real behaviour; interoperability with real tools (`curl`, `dig`, browsers, `openssl`); tests under loss, delay and reordering with `tc netem`.
- **Where AI still fails here:** an assistant cannot observe your network, so its diagnosis is a hypothesis until a capture confirms it. Protocol details are easy to state confidently and wrongly (for example, mixing HTTP/2 and HTTP/3 frame types, or TCP and QUIC handshake steps). In Lab 2 you ask an assistant ten protocol questions, check each against the RFC, and submit the verified-or-refuted table.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1–P3 | 35% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) + P3 oral defence | 30% |

**Mastery gate.** You pass when you can, without AI: (1) from a packet capture of a page load, explain every packet of the DNS, TCP or QUIC, TLS and HTTP exchanges and attribute the total latency; (2) your transport implementation passes the test suite at 10% loss with reordering; (3) diagnose a planted network fault (DNS, MTU, firewall, routing or congestion) in a lab topology within 45 minutes and explain the evidence.

## Industry reality

Where this is used (public sources): UPI's monthly volumes (NPCI data, reported for August 2026); JioHotstar's 6.12 crore peak concurrency (company-reported, March 2025); Cloudflare's 2025 measurements of HTTP/3, IPv6 and post-quantum adoption; Meta's 2021 outage report showing how a routing change took down DNS. Network engineers, SREs, backend engineers, cloud architects and security analysts are all expected to debug across these layers.

**Interview questions from this course**

1. *What happens when you type a URL and press Enter?* Strong answer: browser and OS DNS caches, recursive resolution, HTTPS records; TCP + TLS 1.3 or QUIC; HTTP request to a CDN edge, cache hit or origin fetch; rendering; puts rough numbers on each step.
2. *Why does QUIC run over UDP instead of being a new transport protocol?* Strong answer: middleboxes and kernels ossify new protocols; UDP passes through; user-space deployment speed; streams without TCP head-of-line blocking; encrypted transport headers resist ossification.
3. *Transfers between Mumbai and the US east coast are slow on 1 Gbit/s links. Why?* Strong answer: bandwidth-delay product vs window sizes; loss-based congestion control at long RTT; checks `ss -ti` for `cwnd` and retransmissions; options include window tuning, BBR and parallel streams.
4. *How does TLS 1.3 set up a secure connection?* Strong answer: key share in ClientHello; server's certificate and signature over the transcript; Finished messages; forward secrecy; one round trip; 0-RTT and replay; certificate validation steps.
5. *After a deploy, some users see intermittent timeouts. How do you investigate?* Strong answer: scope (which users, regions, IP versions); DNS, connect, TLS and application timings; load-balancer health checks; MTU issues; conntrack or ephemeral-port exhaustion; captures on both sides; roll back while investigating.

## Resources (free first)

- **Primary text:** Peterson and Davie, *Computer Networks: A Systems Approach* (free, open source) — https://book.systemsapproach.org/
- **Courses:** Stanford CS144 Introduction to Computer Networking — https://cs144.github.io/ ; NPTEL Computer Networks and Internet Protocol (IIT Kharagpur) — https://nptel.ac.in/courses/106105183 ; Kurose and Ross companion site with free Wireshark labs — https://gaia.cs.umass.edu/kurose_ross/index.php
- **Programming:** Beej's Guide to Network Programming — https://github.com/beejjorgensen/bgnet ; Ilya Grigorik, *High Performance Browser Networking* (free online) — https://hpbn.co/
- **Standards:** RFC Editor — https://www.rfc-editor.org/ (RFC 9110, 9111, 9113, 9114, 9000, 9293, 8446, 6298, 9438, 8289, 8290, 8200, 6811); BBR draft — https://datatracker.ietf.org/doc/draft-ietf-ccwg-bbr/
- **Tools:** Wireshark documentation — https://www.wireshark.org/docs/ ; iperf3 — https://github.com/esnet/iperf ; containerlab — https://containerlab.dev/ ; Mininet — https://mininet.org/ ; qvis — https://qvis.quictools.info/ ; crt.sh — https://crt.sh/ ; bgp.tools — https://bgp.tools/
- **Explainers:** Cloudflare Learning Center — https://www.cloudflare.com/learning/
- **Paid, optional:** Kurose and Ross, *Computer Networking: A Top-Down Approach*; Fall and Stevens, *TCP/IP Illustrated, Volume 1*, 2nd ed.

## Sources

- UPI volume for August 2026 (NPCI data), Outlook Business — https://www.outlookbusiness.com/news/upi-transactions-near-record-level-of-298-lakh-cr-in-aug-volume-at-all-time-high-of-2451-bn (checked 2026-10); NPCI UPI statistics — https://www.npci.org.in/what-we-do/upi/product-statistics
- JioHotstar Champions Trophy 2025 viewership (company-reported), Outlook Business — https://www.outlookbusiness.com/news/jiohotstar-sets-new-records-of-viewership-in-champions-trophy (checked 2026-10)
- Cloudflare, "Cloudflare Radar 2025 Year in Review" (Dec 2025) — https://blog.cloudflare.com/radar-2025-year-in-review/ (checked 2026-10)
- Meta Engineering, "More details about the October 4 outage" (Oct 2021) — https://engineering.fb.com/2021/10/05/networking-traffic/outage-details/ (checked 2026-10)
- National Internet Exchange of India (NIXI) — https://nixi.in/ (checked 2026-10)
- RFC 9000 (QUIC) — https://www.rfc-editor.org/rfc/rfc9000 ; RFC 9114 (HTTP/3) — https://www.rfc-editor.org/rfc/rfc9114 ; RFC 9293 (TCP) — https://www.rfc-editor.org/rfc/rfc9293 ; RFC 8446 (TLS 1.3) — https://www.rfc-editor.org/rfc/rfc8446 ; RFC 9438 (CUBIC) — https://www.rfc-editor.org/rfc/rfc9438 (checked 2026-10)

_Last reviewed: 2026-10_
