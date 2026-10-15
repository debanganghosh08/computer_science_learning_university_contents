# NET501 · Labs and projects

Labs run on one Linux workstation (16–32 GB RAM) with Docker or a small Kubernetes cluster: Open5GS or free5GC with UERANSIM, the P4 tutorial VM with BMv2, a recent Linux kernel for eBPF/XDP and SRv6, and Python for satellite models. Use public datasets only, and never transmit on licensed spectrum: all radio is simulated. The seminar's research project replaces the usual L1/L2 split with staged deliverables, but the three projects below still build in difficulty.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Open-source 5G core | Deploy a 5G core with UERANSIM; register 10 UEs; capture and annotate NGAP, NAS, PFCP and GTP-U | Annotated captures; a sequence diagram of registration and session set-up | 6 h |
| 2 · Slices and edge UPF | Two slices with different QoS; a local UPF for one slice; latency comparison; failure of one network function | Configs, latency table, failure observations | 5 h |
| 3 · LEO latency and coverage model | Python model of one constellation shell; minimum RTT and visible satellites over 5 Indian cities across a day | Code, plots, comparison with published measurements | 5 h |
| 4 · P4 router with telemetry | P4_16 router with longest-prefix match on BMv2 and per-hop queue telemetry | P4 program, test results, telemetry plots | 6 h |
| 5 · XDP filter and Cilium | XDP drop filter benchmarked against nftables; Cilium cluster with inspected eBPF programs | Packets-per-second and CPU results; notes on verifier rejections | 5 h |
| 6 · SRv6 and PQC handshake measurement | SRv6 path in Linux with captures; TLS or IKEv2 handshakes with and without a hybrid post-quantum key exchange where your software supports it | Captures, handshake size and time table | 5 h |

## Projects

### P1 · Critical review and fact-check dossier (L3, ~6 hours)

**Real-world inspiration.** Operators, regulators and investors face a constant stream of 5G, 6G and satellite claims. Analysts who can separate standard text from marketing are valuable to telecom operators, consultancies and policy bodies.

**What to build.** A dossier on one frontier topic (6G timelines, LEO broadband in India, or Open RAN performance): a dated timeline from primary sources (3GPP pages, regulator documents, operator filings), a fact-check of 10 public claims with a verdict and evidence for each, and a 2-page review of the most important paper on the topic.

**Acceptance criteria**
- Every timeline entry cites a primary source with a date; secondary reports are labelled as such.
- Each of the 10 claims has a verdict (supported, partly supported, unsupported, unverifiable) with the exact evidence.
- The paper review identifies the main claim, the strongest evidence and the biggest threat to validity.
- No figure appears without a source and the date it was checked.

**Stretch goals.** Turn the dossier into a public explainer page for the course wiki; update it once mid-semester as new information appears.

**What it proves to an employer.** You can be trusted to brief decision makers on fast-moving technology without spreading hype.

### P2 · A measured comparison study (L4, ~15 hours)

**Real-world inspiration.** Engineers deciding between technologies need numbers from their own environment, not vendor charts: XDP vs nftables for a DDoS filter, a local vs central UPF for an edge application, or LEO vs 4G as a backup link for rural branches.

**What to build.** A controlled experiment comparing two approaches from Labs 2–6, with a clear question, a fixed method, at least 10 repeated trials per condition, confidence intervals, and a discussion of what the results mean for a real deployment in India (for example, a bank's rural branches or a port's private network, illustrative).

**Acceptance criteria**
- The question, method, environment (versions, hardware) and metrics are stated before results.
- Results include repeated trials with confidence intervals; outliers are reported, not removed silently.
- At least one threat to validity is tested with an extra experiment (for example, changing packet size or CPU count).
- A one-command script reproduces the main figure from raw data.

**Stretch goals.** Run the experiment on a second hardware platform and report how conclusions change.

**What it proves to an employer.** You can produce evidence that settles a technical decision, the core of senior engineering and research engineering roles.

### P3 · Reproduction and extension paper (L5, research-grade, ~30 hours)

**Real-world inspiration.** Artifact evaluation at SIGCOMM, NSDI, IMC and CoNEXT rewards papers whose results others can reproduce; many results never get re-tested. Reproducing and extending a result is how new researchers earn credibility and often how theses begin.

**What to build.** Choose one published result from the reading list or approved by the instructor (for example, an XDP performance figure, a LEO latency model result, a P4 telemetry result, a verification result from Batfish, or an LLM network-configuration result from NetConfEval). Reproduce it with documented methods, then extend it with one new question (a new workload, platform, region such as Indian cities, or model). Write a 6–8 page workshop-style paper and publish an artifact.

**Acceptance criteria**
- The reproduction matches the original within stated tolerances, or the paper explains the gap with experiments that isolate its cause.
- The extension asks a question the original did not answer and answers it with repeated, statistically reported measurements.
- The artifact runs from a README with one command on a clean machine; a classmate reproduces the main figure without help.
- The paper follows a standard structure (abstract, introduction, background, method, results, limitations, related work) and passes a peer review in class with all major comments addressed.
- AI assistance, if used, is disclosed, and every number in the paper is traceable to raw data.
- The symposium talk fits 15 minutes and answers questions on method and limitations.

**Stretch goals.** Submit to a student workshop, a reproducibility track, or an arXiv preprint with the instructor's guidance; contribute fixes upstream to the tools you used.

**What it proves to an employer.** You can do research-grade engineering: careful experiments, honest reporting and reusable artifacts, valued by research labs, standards teams and advanced engineering groups.

## Feeds into

- [THS501 Thesis or Capstone I](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) and [THS502 Thesis or Capstone II](../../../../05_shared_years_3_to_5/THS502_thesis_or_capstone_ii/README.md): P3 is designed to become a thesis starting point.
- [RES502 Reading, Reproducing and Extending Papers](../../../../05_shared_years_3_to_5/RES502_reading_reproducing_and_extending_papers/README.md), taken in the same semester.
- [LCH502 Career Launch and Founder Studio](../../../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md): frontier knowledge for telecom, satellite or network-software ventures.
