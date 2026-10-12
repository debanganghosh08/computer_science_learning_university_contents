# CS204 · Labs and projects

Use Linux (a VM or WSL2 works). `tc netem` emulates delay, loss and reordering on your own machine, so you never need to disturb a real network. Capture only traffic you own or are authorised to capture, and scan only your own machines.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Measurement toolkit | Break down page-load timing (DNS, connect, TLS, first byte, transfer) for 10 sites, including Indian services, from broadband and from mobile data | Timing tables from `curl -w`, `mtr` paths, and three conclusions you can defend | 3 h |
| 2 · HTTP by hand + RFC check | Speak HTTP/1.1 with `nc`; test caching headers; ask an AI assistant 10 protocol questions and check every answer against the RFC | Transcripts and a verified-or-refuted table with RFC section numbers | 3 h |
| 3 · Iterative DNS resolver | Resolve A, AAAA and CNAME chains from the root servers with TTL-based caching, using raw UDP packets you encode and decode yourself | Resolver matching `dig` on 50 domains; a cache-hit benchmark | 6 h |
| 4 · Framed chat server | Event-driven chat server (`epoll` or asyncio) with length-prefixed messages, timeouts and graceful shutdown | Code, tests that deliver one byte at a time, load-test results | 4 h |
| 5 · Reassembler and receiver | Byte-stream reassembler and TCP receiver with windowing (Stanford CS144 checkpoint style) | Implementation passing the provided tests | 6 h |
| 6 · TCP sender | Retransmission timer, exponential back-off and fast retransmit; connect to your receiver | Passing tests; a capture of your stack talking to itself | 6 h |
| 7 · Congestion experiments | CUBIC vs BBR with `iperf3` under emulated delay and loss; latency under load with and without fq_codel | Plots of throughput, `cwnd` and RTT; a one-page explanation | 4 h |
| 8 · TLS and QUIC captures | Decrypt your own TLS 1.3 session with `SSLKEYLOGFILE`; record a QUIC qlog; inspect certificate chains and CT logs | Annotated handshakes for TLS over TCP and for QUIC; RTT counts for each | 4 h |
| 9 · Longest-prefix match | Binary and path-compressed tries over a public BGP table snapshot (RouteViews or RIPE RIS) | Correctness against a linear-scan oracle; lookups per second; memory use | 4 h |
| 10 · Routing and virtual networks | Link-state and distance-vector simulators; then a leaf-spine topology in containerlab with ECMP, plus two network namespaces bridged with NAT | Simulator output (including count-to-infinity), topology files, captures proving ECMP spreading | 6 h |

## Projects

### P1 · `netcheck`, a site-health command-line tool (L1, ~6 hours)

**Real-world inspiration.** `mtr`, `curl -w`, SSL checkers and uptime monitors combine a handful of measurements that on-call engineers run first in any incident.

**What to build.** Given a URL, `netcheck` resolves A and AAAA records, times TCP connects to each address, performs a TLS handshake and reports version, cipher, certificate issuer and days to expiry, checks ALPN and `Alt-Svc` for HTTP/2 and HTTP/3 support, fetches headers and summarises caching policy. Output is a readable table and JSON.

**Acceptance criteria**
- On 10 public sites, each timing is within 10% of `curl -w` (median of 5 runs).
- Correctly flags expired, self-signed and wrong-host certificates on the badssl.com test hosts.
- IPv6-only, unreachable and slow hosts produce clear errors within the configured timeout, never a hang.
- Unit tests run offline against recorded fixtures.

**Stretch goals.** A traceroute mode that labels each hop's autonomous system; a watch mode that alerts when a certificate is within 14 days of expiry.

**What it proves to an employer.** You understand what each layer contributes to latency and failure, and you can build the tool an on-call team reaches for.

### P2 · Reliable transport over UDP (L2, ~15 hours)

**Real-world inspiration.** TCP and QUIC both turn an unreliable packet service into a reliable, congestion-controlled stream; QUIC does it in user space over UDP.

**What to build.** A library that provides a reliable byte stream over UDP sockets: connection set-up and teardown, sliding window with selective acknowledgements, RTT estimation and retransmission timeout following RFC 6298, exponential back-off, flow control and AIMD congestion control. Build a file-transfer tool on top.

**Acceptance criteria**
- A 100 MB file arrives with a matching SHA-256 hash under `netem` profiles of 0%, 5% and 10% loss, and 100 ms delay with jitter and reordering.
- At 0% loss and 50 ms RTT, throughput reaches at least 50% of Linux TCP (CUBIC) on the same emulated link.
- Two simultaneous transfers through a shared bottleneck reach a Jain's fairness index of at least 0.9.
- Retransmitted bytes are logged and stay below three times the configured loss rate.
- A design document explains each timer and the state machine, with a diagram.

**Stretch goals.** Pacing and a BBR-style bandwidth estimator; multiple independent streams in one connection, QUIC-style, with a test showing no head-of-line blocking between streams.

**What it proves to an employer.** You can build and test a protocol under realistic impairment, which is the core of transport, streaming and real-time systems work.

### P3 · A mini CDN edge: caching reverse proxy (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** CDNs such as Cloudflare, Akamai and Fastly serve web content from edge caches close to users; live streaming platforms (JioHotstar reported 6.12 crore peak concurrent viewers in March 2025) depend on many viewers requesting the same new video segment at the same moment. The load scenario below is illustrative.

**What to build.** A caching reverse proxy that implements RFC 9111 semantics (`max-age`, `s-maxage`, `no-store`, `private`, `ETag` revalidation, `Vary`), request coalescing (concurrent misses for one key cause a single origin fetch), `stale-while-revalidate` and `stale-if-error`, TLS termination, and consistent hashing across three edge nodes in front of an origin shield. Export metrics (hit ratio, p50 and p99 latency, origin requests) and structured access logs. Include a load generator that imitates HLS clients fetching the newest segment.

**Acceptance criteria**
- Passes the provided caching-semantics suite (40 cases derived from RFC 9111).
- With 1,000 clients requesting the same new segment at once, the origin receives exactly one request per segment (shown in origin logs).
- At 10,000 requests per second on a stated machine, cache-hit p99 latency is under 10 ms; CPU and memory use are reported.
- In an origin-outage drill, clients keep receiving content for the configured `stale-if-error` window, and revalidation resumes when the origin returns.
- Adding a fourth edge node remaps close to one quarter of keys, measured and compared with naive modulo hashing.
- The write-up includes a back-of-envelope capacity plan for a 6-crore-viewer live event, with every assumption (bitrate ladder, segment length, hit ratio) stated.

**Stretch goals.** HTTP/3 on the client side using a QUIC library (quiche or quic-go); a purge API; per-client rate limiting.

**What it proves to an employer.** You can build infrastructure that protects an origin under a thundering herd, prove it with load tests, and reason about capacity at Indian scale. CDN, streaming, SRE and backend platform teams hire for this.

## Feeds into

- [CS212 Distributed Systems I](../../semester_4/CS212_distributed_systems_i/README.md): RPC, timeouts, retries and partial failure build on Chapters 4–5.
- [CS213 Security Foundations](../../semester_4/CS213_security_foundations/README.md): TLS, PKI, DNS security and firewalls from the defender's side.
- [CS215 Cloud and DevOps Foundations](../../semester_4/CS215_cloud_and_devops_foundations/README.md): virtual networks, load balancers and DNS in the cloud.
- The IT Infrastructure and Network Engineering major: [NET301](../../../03_majors/it_infrastructure_networking/year_3/NET301_routing_and_switching/README.md), [NET303](../../../03_majors/it_infrastructure_networking/year_3/NET303_network_automation_and_netdevops/README.md), [NET304](../../../03_majors/it_infrastructure_networking/year_3/NET304_wireless_sd_wan_and_enterprise_networks/README.md).
- [CLD304 Cloud Networking](../../../03_majors/cloud_engineering/year_3/CLD304_cloud_networking_vpcs_dns_load_balancing/README.md) and [BE301 API Design](../../../03_majors/backend_engineering/year_3/BE301_api_design_rest_grpc_and_graphql/README.md): P3 is a direct precursor.
