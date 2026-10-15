# NET501 · Frontier Seminar: 5G, Satellite Internet and Programmable Networks

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 5 · 9 | 4 (≈ 120 hours) | L3 → L5 | [NET401](../../year_4/NET401_data_center_and_hybrid_infrastructure/README.md), [NET403](../../year_4/NET403_aiops_and_intent_based_networking/README.md) | [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md), [THS502](../../../../05_shared_years_3_to_5/THS502_thesis_or_capstone_ii/README.md); taken with [RES501](../../../../05_shared_years_3_to_5/RES501_research_methods_and_scientific_writing/README.md) and [RES502](../../../../05_shared_years_3_to_5/RES502_reading_reproducing_and_extending_papers/README.md) |

This is a seminar. Each week has readings, a short lab, and a student-led discussion; the semester ends with a reproduction or extension of a published result, written up as a workshop-style paper.

## Why this course matters now

Three changes are reshaping networks at once. Mobile networks: India went from 1,40,623 5G base stations in March 2023 to 5,62,971 by 30 June 2026, with 5G available in 99.9% of districts, and BSNL launched an indigenous 4G stack in September 2025 (C-DOT core, Tejas radio, TCS integration) described as 5G-upgradable. Globally, 3GPP Release 20 is the last release focused only on 5G-Advanced and carries the first 6G studies; in June 2026 3GPP fixed Release 21, the first normative 6G release, for a Stage-3 freeze in December 2028. Satellite internet: Jonathan McDowell's tracking showed 11,117 working Starlink satellites in orbit on 11 October 2026, out of 12,988 launched; in India, Starlink received its GMPCS licence in June 2025 and IN-SPACe authorisation in July 2025, with commercial service depending on spectrum allocation and security compliance. Programmable networks: Intel halted development of its next-generation Tofino P4 switch chip in 2023, yet P4 and especially eBPF/XDP now run load balancers, DDoS defences and Kubernetes networking at very large scale, and AI clusters are pushing new Ethernet designs (Ultra Ethernet 1.0, 2025). AI tools can summarise every paper in this course in seconds; they cannot run the experiment, notice that a result does not reproduce, or design the measurement that settles an argument. That is the work of this seminar.

## Learning outcomes

By the end you can:

1. **Read** networking research critically (SIGCOMM, NSDI, IMC, CoNEXT, HotNets, MobiCom) and **write** structured reviews that separate claims, evidence and threats to validity.
2. **Explain** the 5G system architecture (RAN splits, service-based core, user plane, slicing, edge), and **run** an open-source 5G core with a simulated RAN, reading its signalling and user-plane traffic.
3. **Describe** the path to 6G in 3GPP and ITU (Release 20 studies, Release 21 normative work, IMT-2030) and **evaluate** claims about 6G with dates and sources.
4. **Model** LEO constellation latency and coverage, and **compare** measured satellite performance from published studies with terrestrial alternatives for Indian use cases.
5. **Write** P4 programs on the BMv2 software switch and eBPF/XDP programs on Linux, and **measure** their performance and limits.
6. **Explain** SRv6 network programming, AI-fabric Ethernet changes and post-quantum migration for network protocols.
7. **Reproduce** a published networking result (or explain precisely why it does not reproduce) and **extend** it with a new experiment.
8. **Communicate** research in a 6–8 page paper and a conference-style talk.

## Chapters and lessons

### Chapter 1 · Reading and reproducing networking research (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Venues and genres | Systems, measurement, position and dataset papers; artifact evaluation badges | Classify 10 recent papers by genre |
| 1.2 Reading method | Three-pass reading; claims, evidence, assumptions, threats to validity | Write a one-page review of the Batfish paper (NSDI 2015) |
| 1.3 Reproducibility | Artifacts, versions, hardware sensitivity, statistical reporting | List what you would need to reproduce one figure from a paper |
| 1.4 AI as a reading aid | Summaries vs reading; checking every claimed number against the paper | Compare an AI summary of a paper with your review; count errors |

**Check your understanding:** What makes a measurement paper's conclusion fragile? Why is a reproduction that fails still a contribution? Which part of a paper do AI summaries most often get wrong?

### Chapter 2 · 5G system architecture (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 RAN | gNB, CU/DU/RU splits, fronthaul and midhaul, NSA vs SA deployments | Draw an Indian operator's likely NSA-to-SA path from public statements |
| 2.2 The service-based core | AMF, SMF, UPF, AUSF, UDM, NRF, PCF; HTTP/2-based service interfaces (3GPP TS 23.501) | Map a registration procedure to the functions it touches |
| 2.3 User plane | PDU sessions, GTP-U tunnels, PFCP between SMF and UPF, QoS flows and 5QI | Trace a packet from phone to internet through the user plane |
| 2.4 India's rollout | Base-station growth, coverage claims and what they do and do not say about capacity | Critique the "99.9% of districts" metric in one paragraph |

**Check your understanding:** Why did the 5G core adopt service-based interfaces? What does the UPF do that a router does not? Why can coverage by district say little about user experience?

### Chapter 3 · A 5G core in the lab (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Open-source cores | Open5GS, free5GC, OpenAirInterface; what each implements | Deploy Open5GS or free5GC on Kubernetes or Docker |
| 3.2 Simulated RAN | UERANSIM for gNB and UE simulation | Register 10 simulated UEs and open PDU sessions |
| 3.3 Signalling and captures | NGAP, NAS, PFCP and GTP-U in Wireshark | Annotate a full registration and session set-up |
| 3.4 Operating a cloud-native core | Scaling the UPF, observability, failure of one network function | Kill the SMF and record what users experience |

**Check your understanding:** Why is the UPF usually scaled separately from control-plane functions? What does a PFCP session establishment tell the UPF? What failure in your lab surprised you most?

### Chapter 4 · Slicing, edge and private 5G (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Network slicing | S-NSSAI (slice/service type and differentiator), slice selection, isolation levels | Configure two slices with different QoS in the lab core |
| 4.2 Multi-access edge computing | Local breakout, UPF placement, latency budgets | Measure latency with a local vs central UPF in the lab |
| 4.3 Private 5G | Factories, ports, campuses; private networks vs Wi-Fi 7 for industrial use | Write a comparison for a port terminal (illustrative) |
| 4.4 Reading | A survey or measurement paper on slicing or MEC chosen with the instructor | Lead the discussion |

**Check your understanding:** What is actually isolated in a network slice, and what is shared? When does edge computing fail to reduce latency? Why might a factory choose Wi-Fi over private 5G?

### Chapter 5 · Open RAN and indigenous stacks (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 O-RAN architecture | Open fronthaul, near-real-time and non-real-time RAN intelligent controllers, xApps and rApps | Map O-RAN interfaces onto your Chapter 2 diagram |
| 5.2 AI in the RAN | Use cases (traffic steering, energy saving), evaluation problems, risks of opaque control loops | Critique one published AI-RAN result |
| 5.3 India's stack | BSNL's indigenous 4G stack (2025): C-DOT core, Tejas RAN, TCS integration; trusted-source policies | Summarise what is public and what is unknown about its architecture |
| 5.4 Integration reality | Multi-vendor testing, performance parity, operations cost | Write the 5 questions you would ask before buying an open RAN system |

**Check your understanding:** What problem does open fronthaul solve, and what does it make harder? Why is evaluating AI in the RAN harder than in an enterprise network? What evidence would show an indigenous stack performs at parity?

### Chapter 6 · Toward 6G (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 The standards timeline | 3GPP Release 20 (6G studies, TR 22.870 use cases), Release 21 (first normative 6G: Stage-3 freeze December 2028, ASN.1 March 2029), ITU IMT-2030 | Build a dated timeline with sources |
| 6.2 Technical directions | AI-native air interface, integrated sensing and communication, new spectrum, energy efficiency | Assess one direction: what is studied, what is promised |
| 6.3 Security | Post-quantum cryptography studies in Release 20, AEAD algorithms | List network protocols in a 6G system that need PQC migration |
| 6.4 Hype check | Separating standard text from marketing | Fact-check 5 public 6G claims against 3GPP pages |

**Check your understanding:** Why does a Stage-3 freeze date matter more than a "6G launch" headline? What does "AI-native" mean in a standard, if anything? Which 6G claim you checked had the weakest evidence?

### Chapter 7 · LEO satellite internet (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Orbits and latency | LEO vs MEO vs GEO, propagation delay, elevation angles, handovers | Compute minimum RTT for GEO and a 550 km LEO path |
| 7.2 Constellations | Shells, inclinations, inter-satellite laser links, ground stations, capacity per cell; Starlink counts from McDowell's tracking | Model coverage over India for one shell with a simple simulator |
| 7.3 Measured performance | Measurement studies of Starlink (for example Michel et al., IMC 2022); variability, handover spikes | Reproduce one figure's trend from a public dataset |
| 7.4 Routing in space | Low-latency routing with laser links (Handley, HotNets 2018); when space beats fibre | Compare a London–Singapore path via fibre and via a modelled constellation |

**Check your understanding:** Why can a LEO path beat fibre over long distances? Why does LEO latency vary every few seconds? What limits capacity in a dense city cell?

### Chapter 8 · Satellite meets terrestrial (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Non-terrestrial networks in 3GPP | NTN support from Release 17 onward; direct-to-device service | Explain what changes in the 5G stack for satellite links |
| 8.2 Enterprise use | Satellite as SD-WAN backup (NET304), remote sites, disaster recovery | Design a backup plan for 50 rural branches with cost assumptions labelled |
| 8.3 India's regulatory path | GMPCS licences, IN-SPACe authorisation, spectrum allocation debate (TRAI recommendations, DoT decision), security conditions | Build a dated timeline from sources; mark what is unconfirmed |
| 8.4 Governance | Spectrum coordination, space debris, astronomy impact | Write a one-page policy brief |

**Check your understanding:** Why is satellite a good backup but often a poor primary link for a branch? What steps remain before commercial LEO service in India, according to your timeline? What are the strongest arguments on each side of administrative vs auctioned satellite spectrum?

### Chapter 9 · Programmable data planes with P4 (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Why programmable | Reconfigurable match-action tables (Bosshart et al., SIGCOMM 2013), P4 (CCR 2014) | Read both papers; present one design decision |
| 9.2 P4_16 | Parsers, match-action tables, deparsers; BMv2; P4Runtime | Write a P4 router with longest-prefix match on BMv2 |
| 9.3 In-network telemetry | INT headers, queue-depth reporting, what it reveals | Add per-hop queue telemetry to your P4 program |
| 9.4 Where P4 lives now | Intel's Tofino halt (2023), open-sourced Tofino software (2025), SmartNICs and DPUs, research use | Write a 1-page assessment of P4's future with sources |

**Check your understanding:** What can a programmable switch do that a fixed-function switch cannot? Why did losing Tofino matter so much to P4 research? Where is programmable packet processing most likely to grow?

### Chapter 10 · eBPF and XDP (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 The fast path in the kernel | XDP (Høiland-Jørgensen et al., CoNEXT 2018) vs kernel bypass (DPDK); hooks, maps, the verifier | Write an XDP program that counts and drops packets by rule |
| 10.2 Production uses | Load balancing (Meta's Katran), DDoS mitigation at the edge, Kubernetes networking (Cilium) | Run Cilium in a lab cluster and inspect its eBPF programs |
| 10.3 Performance | Packets per second, CPU cost, driver vs generic mode | Benchmark your XDP filter against nftables on the same VM |
| 10.4 Limits and safety | Verifier limits, debugging, upgrades, security of loading programs | Document 3 programs the verifier rejects and why |

**Check your understanding:** Why does XDP run before the kernel allocates a socket buffer, and what does that give you? When is DPDK still the better choice? Why does the verifier exist?

### Chapter 11 · Segment routing, AI fabrics and post-quantum networking (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 SRv6 | Segment routing over IPv6, network programming functions (RFC 8986), traffic engineering without per-flow state | Build an SRv6 path in Linux and capture its headers |
| 11.2 AI-fabric Ethernet | Ultra Ethernet goals (packet spraying, congestion control, reliability) vs RoCEv2 and InfiniBand | Compare the three on a written table with sources |
| 11.3 Post-quantum migration | ML-KEM (NIST FIPS 203, 2024), hybrid key exchange in TLS and IKEv2 (RFC 9370), operational impact | Measure handshake size and time with and without a hybrid key exchange in a lab |
| 11.4 Choosing a project | Scoping a reproduction or extension for the final project | Submit a 2-page proposal |

**Check your understanding:** What state does SRv6 remove from the core, and what does it add to packets? Why do AI training fabrics care about packet spraying? What breaks first when key-exchange messages get bigger?

### Chapter 12 · Research project and symposium (weeks 12–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Running the experiment | Experiment logs, versions, seeds, repeated trials, confidence intervals | Weekly progress notes with raw data |
| 12.2 Writing | Workshop-paper structure, figures that answer one question, honest limitations | Draft and peer-review a 6–8 page paper |
| 12.3 Presenting | 15-minute talk, handling questions | Symposium presentation |
| 12.4 Artifacts | Packaging code and data so others can reproduce your work | Publish an artifact with a README and a one-command run |

**Check your understanding:** What would a reviewer ask first about your results? Which limitation of your work matters most to a reader? Could a classmate reproduce your main figure from your artifact alone?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Paper review practice | Review of a classic paper |
| 2 | 2 | 5G architecture mapping | Reading response |
| 3 | 3 | Lab 1 · Open-source 5G core and UERANSIM | Annotated captures |
| 4 | 4 | Lab 2 · Slices and edge UPF | Presentation 1 (students) |
| 5 | 5 | O-RAN mapping | Reading response |
| 6 | 6 | 6G timeline and fact-check | — |
| 7 | 7 | Lab 3 · LEO latency and coverage model | Presentation 2 |
| 8 | 8 | Satellite backup design and India timeline | Policy brief |
| 9 | 9 | Lab 4 · P4 router with telemetry on BMv2 | — |
| 10 | 10 | Lab 5 · XDP filter and Cilium | Presentation 3 |
| 11 | 11 | Lab 6 · SRv6 and PQC handshake measurement | **Project proposal due** |
| 12 | 12 | Project | Reproduction report |
| 13 | 12 | Project | Paper draft and peer review |
| 14 | 12 | Symposium | **Final paper and artifact due** |
| 15 | Review | Oral examination on readings and project | Final grade |

## Working with AI in this course

- **Use AI for:** first-pass summaries to decide what to read closely; explaining unfamiliar 3GPP terms (then checking the specification); scaffolding P4, eBPF and simulation code; drafting figures and LaTeX; checking your paper's clarity.
- **Do without AI (drills):** your reviews and reading responses; RTT and coverage calculations; the analysis section of your paper; the oral examination.
- **Verify AI output by:** checking every number and claim against the paper or specification (with page or section); running code and comparing with the paper's method; asking a classmate to reproduce your figure from your artifact.
- **Where AI still fails here:** summaries invent results and mix papers; 3GPP release contents and dates are often wrong or outdated; generated P4 and eBPF code frequently fails the compiler or the verifier. Disclose any AI assistance in your paper's acknowledgements and keep a log of what you verified, following the rules in [RES501](../../../../05_shared_years_3_to_5/RES501_research_methods_and_scientific_writing/README.md).

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Reading responses and reviews | 15% |
| Seminar presentations (3) | 15% |
| Labs (6) | 20% |
| Research project (proposal, reproduction report, paper, artifact) | 40% |
| Oral examination | 10% |

**Mastery gate.** You pass when you can: (1) reproduce a published networking result within stated tolerances, or explain with evidence exactly why it does not reproduce; (2) write a 6–8 page paper with a correct experimental method, honest limitations and a working artifact; (3) critique an unseen paper in a 20-minute oral, identifying its main claim, its strongest evidence and its biggest threat to validity.

## Industry reality

Where this is used: telecom operators and vendors in India and worldwide (5G cores, Open RAN, private networks); satellite operators and their enterprise and government customers; hyperscalers and CDNs running eBPF and programmable data planes; AI infrastructure teams building GPU fabrics; standards bodies (3GPP, IETF, ITU) and research labs. Roles include telecom core engineer, RAN engineer, network software engineer, research engineer and standards delegate.

**Interview questions from this course**

1. *Walk through what happens when a phone attaches to a 5G standalone network.* Strong answer: RRC connection, registration via AMF, authentication with AUSF/UDM, PDU session via SMF, UPF selection and PFCP, GTP-U tunnel, QoS flows.
2. *When would you recommend LEO satellite for an enterprise?* Strong answer: remote and backup connectivity, measured latency and variability, capacity limits, cost, regulatory status in the country, SD-WAN integration.
3. *eBPF/XDP or DPDK for a 100 Gbit/s packet filter?* Strong answer: XDP for in-kernel coexistence, safety and simpler operations; DPDK for full user-space control at the highest rates; measurements, NIC support and team skills decide.
4. *What will post-quantum migration change in network protocols?* Strong answer: larger key-exchange messages, hybrid modes, fragmentation and MTU issues, performance and middlebox compatibility, inventory and crypto agility.
5. *Tell me about a result you could not reproduce.* Strong answer: what was tried, what differed (versions, hardware, data), how the gap was isolated, what was learned, how it was reported.

## Resources (free first)

- **Standards:** 3GPP Release 20 — https://www.3gpp.org/specifications-technologies/releases/release-20 ; Release 21 — https://www.3gpp.org/specifications-technologies/releases/release-21 ; 3GPP specifications (TS 23.501 and others) — https://www.3gpp.org/specifications-technologies ; O-RAN Alliance — https://www.o-ran.org/ ; RFC 8986 (SRv6 network programming), RFC 9370 (IKEv2 multiple key exchanges) — https://www.rfc-editor.org/ ; NIST FIPS 203 (ML-KEM) — https://csrc.nist.gov/pubs/fips/203/final
- **Open-source labs:** Open5GS — https://open5gs.org/ ; free5GC — https://free5gc.org/ ; UERANSIM — https://github.com/aligungr/UERANSIM ; OpenAirInterface — https://openairinterface.org/ ; P4 tutorials and BMv2 — https://github.com/p4lang/tutorials ; eBPF documentation — https://ebpf.io/ ; XDP tutorial — https://github.com/xdp-project/xdp-tutorial ; Cilium — https://docs.cilium.io/
- **Satellite data:** Jonathan McDowell's Starlink statistics — https://planet4589.org/space/con/star/stats.html
- **Reading list:** Bosshart et al., "Forwarding Metamorphosis" (RMT, SIGCOMM 2013) and "P4: Programming Protocol-Independent Packet Processors" (ACM SIGCOMM CCR, 2014); Høiland-Jørgensen et al., "The eXpress Data Path" (CoNEXT 2018); Handley, "Delay is Not an Option: Low Latency Routing in Space" (HotNets 2018); Michel et al., "A First Look at Starlink Performance" (IMC 2022); Jain et al., "B4" (SIGCOMM 2013); Poutievski et al., "Jupiter Evolving" (SIGCOMM 2022); Fogel et al., "Batfish" (NSDI 2015); Mondal et al. (arXiv 2023); Wang et al., "NetConfEval" (CoNEXT 2024). Most are free on the ACM Digital Library (open access), USENIX or authors' pages.
- **Paid, optional:** Sauter, *From GSM to LTE-Advanced Pro and 5G* (Wiley), for a full mobile-network reference.

## Sources

- Indian Infrastructure, Minister of State for Communications' figures (27 Jul 2026): 5G BTS 1,40,623 (31 Mar 2023) to 5,62,971 (30 Jun 2026), 99.9% of districts — https://indianinfrastructure.com/2026/07/27/india-crosses-0-56-million-5g-base-stations-136-telecom-rd-projects-approved-says-minister-of-state-for-communications/ (checked 2026-10)
- Developing Telecoms, "BSNL, TCS, C-DOT and Tejas unveil indigenous 4G stack" (Sep 2025) — https://www.developingtelecoms.com/telecom-technology/wireless-networks/19125-bsnl-tcs-c-dot-and-tejas-unveil-indigenous-4g-stack.html (checked 2026-10)
- 3GPP Release 20 and Release 21 pages (Release 21 dates agreed at TSG#112, June 2026) — https://www.3gpp.org/specifications-technologies/releases/release-20 ; https://www.3gpp.org/specifications-technologies/releases/release-21 (checked 2026-10)
- Jonathan McDowell, Starlink statistics (data updated 11 Oct 2026: 12,988 launched, 11,131 in orbit, 11,117 working) — https://planet4589.org/space/con/star/stats.html (checked 2026-10)
- RCR Wireless, Starlink GMPCS licence in India (Jun 2025) — https://rcrwireless.com/20250609/5g/starlink-satellite-in-india ; IN-SPACe authorisation (Jul 2025) — https://www.rcrwireless.com/20250717/carriers/starlink-india ; commercial launch status after mid-2025 (unconfirmed) (checked 2026-10)
- Systems Approach, "The Future of P4, Revisited" (Intel's Tofino halt, 2023) — https://systemsapproach.substack.com/p/the-future-of-p4-one-perspective ; Phoronix, Intel open-sources Tofino P4 software (Jan 2025) — https://www.phoronix.com/news/Intel-Tofino-P4-Open-Source (checked 2026-10)
- Ultra Ethernet Consortium (Specification 1.0, 2025) — https://ultraethernet.org/ (checked 2026-10)

_Last reviewed: 2026-10_
