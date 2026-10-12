# SAR501 · Labs and projects

This is a research seminar, so labs are short experiments that feed discussion, and the projects build towards a workshop-quality paper. All experiments run on your own machines, your own cloud accounts or public datasets. Do not scan or probe systems you do not own; for internet-wide questions use published datasets (for example Cloudflare Radar or academic access to scan datasets) and follow your institution's ethics process. Everything named below is an *illustrative scenario* unless a source is given.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 0a · SoK critique and reproduction | Critique one SoK paper and reproduce one figure from a public artefact | One-page critique; reproduced figure with notes on differences | 4 h |
| 0b · Mosca workshop | Apply Mosca's inequality to four data types under three timeline assumptions; compare with Gidney's 2019 and 2025 resource estimates | Table and a one-page position on what to assume | 3 h |
| 1 · Hybrid TLS measurement | Measure handshake bytes and latency for X25519 vs X25519MLKEM768 on local and high-latency links (simulated with `tc netem`) | Scripts, raw data, median and 95th percentile plots, comparison with a published study | 5 h |
| 2 · Hash-based firmware signing | Sign firmware images with LMS; simulate state loss and show why it is dangerous; design state management | Lab report with the failure demonstration and a state-management design | 4 h |
| 3 · Control protocol | Design and test a trusted-monitoring protocol for a deployment agent in a sandbox: a weaker trusted model or rule set reviews each action; benign canaries attempt out-of-scope actions | Protocol design, results table (caught, missed, false alarms) | 5 h |
| 4 · Attestation-gated key release | Release a decryption key only to a confidential VM (or a simulated attester) whose measurements match policy; then change the workload and show refusal | Policy, logs of release and refusal | 5 h |
| 5 · Automated reasoning | Either prove a property of three access policies with Z3, model a toy key exchange in Tamarin and find the planted flaw, or check a key-rotation invariant with TLA+ | Model files, tool output, a one-page explanation | 5 h |

## Projects

### P1 · Replicating a post-quantum TLS measurement (L4, ~6 hours)

**Real-world inspiration:** hybrid ML-KEM key exchange is now on by default in major browsers and in OpenSSL 3.5, and published studies report its handshake costs. Replication on different hardware and networks is how the community checks such claims.

**What to build:** a replication of one published PQ TLS performance result, extending Lab 1: same metrics, your hardware, at least two network conditions, and a discussion of differences.

**Acceptance criteria:**
- At least 1,000 handshakes per configuration, reported with median, 95th percentile and confidence intervals.
- A table comparing your numbers with the paper's, with every difference explained or marked unexplained.
- Scripts and environment captured so a peer reproduces your main plot within 30 minutes.
- A one-paragraph practical recommendation for an architect, limited to what your data supports.

**Stretch goals:** add an ML-DSA certificate chain and measure the authentication cost; test through a middlebox you control.

**What it proves to an employer:** you can turn a migration claim into measured evidence.

### P2 · Systematisation paper (L4, ~15 hours)

**Real-world inspiration:** SoK papers organise a fast-moving field so practitioners can choose designs. Two fields need them now: identity and accountability for autonomous agents, and PQC migration for payment systems. Choose one (or propose another with instructor approval).

**What to build:** a 6–8 page SoK-style paper: scope, a taxonomy, a comparison of at least 15 primary sources (standards, papers, published specifications), gaps and research questions. For the agent topic, cover agent identity, delegation, authorization, audit and payments (for example AP2 and its published analysis). For the payments topic, cover inventory, protocols, HSMs, cards and terminals, supplier timelines and India's DST report.

**Acceptance criteria:**
- Every cited source is primary and checked (title, authors, venue or publisher, date, link); zero invented citations, verified by a peer who checks ten at random.
- The taxonomy classifies every surveyed approach, and a peer can classify two new approaches with it consistently.
- At least three open research questions, each stated so that an experiment could test it.
- The paper states its own limits (coverage, date of survey).

**Stretch goals:** a public companion table of surveyed work; a short talk version.

**What it proves to an employer or supervisor:** you can map a frontier quickly and accurately, which is what research groups and strategy teams need.

### P3 · Research project with artefact (L5, portfolio-grade, ~30 hours)

**Real-world inspiration:** workshops at venues such as IEEE S&P, USENIX Security, CCS and Real World Crypto publish short papers with reproducible artefacts. Example topics (choose one or propose your own):

- accuracy of open-source CBOM and crypto-discovery tools against a labelled corpus you build;
- crypto-agility failure modes: downgrade and negotiation bugs in a set of open-source libraries, tested on your own builds;
- post-quantum readiness of Indian banking and government websites using published scan data (no active scanning of third parties);
- a policy language or analysis for agent tool permissions with SMT-based verification;
- attestation-bound credentials for AI agents running in confidential VMs;
- state management strategies for hash-based firmware signatures across a simulated device fleet;
- evaluation of control protocols for deployment agents under adaptive benign-canary tests.

**What to build:** a research question, method, experiments or proofs, a 6–8 page paper in a standard template, an artefact (code, data, models) with a README, and a 15-minute talk.

**Acceptance criteria:**
- The paper has a clear contribution statement, related work with at least ten checked primary sources, a threats-to-validity section and an ethics statement.
- The artefact reproduces the main result on a clean machine following the README (checked by a peer).
- Quantitative claims include variability (intervals or repeated runs); formal claims include the tool output.
- Negative or partial results are reported honestly with what they rule out.
- You answer questions for 10 minutes after the talk, including one on how your result changes an architect's decision.

**Stretch goals:** submit to a student workshop or a preprint server after supervisor review; continue the work in [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md).

**What it proves:** you can create new knowledge in security architecture, the L5 bar, and you have a citable artefact for research roles, PhD applications or a specialist consulting practice.

## Feeds into

- [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) and [THS502](../../../../05_shared_years_3_to_5/THS502_thesis_or_capstone_ii/README.md): P3 is designed to grow into a thesis or capstone.
- [RES502 Reading, Reproducing and Extending Papers](../../../../05_shared_years_3_to_5/RES502_reading_reproducing_and_extending_papers/README.md): P1 is a reproduction in the same format.
- [LCH502 Career Launch and Founder Studio](../../../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md): PQC migration and agent security are viable consulting and product niches.
