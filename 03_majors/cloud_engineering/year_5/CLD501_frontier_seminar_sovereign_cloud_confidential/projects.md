# CLD501 · Labs and projects

This is a seminar, so labs are short experiments that support the readings, and the projects build towards a workshop-format paper. All experiments run on your own accounts and resources only. Security work is limited to configuring and verifying protections; attack papers are studied, never reproduced on real systems. Paper presentations and the threat model in Lab 6 are prepared without AI.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Measuring the cloud honestly | Run one CPU and one network benchmark on 5 instances of the same type in two regions; report medians, intervals and outliers | Data, plots and a methods paragraph | 4 h |
| 2 · MicroVM overheads | Boot Firecracker microVMs on a bare-metal or nested-virtualisation host; measure boot time, memory overhead and density | Measurements compared with the Firecracker paper's claims | 4 h |
| 3 · Tail at scale | Simulate fan-out of 1 to 1,000 backends with a heavy-tailed latency distribution; add hedged requests | Plots showing tail amplification and the hedging effect | 3 h |
| 4 · Cell-based control plane | Design and simulate a cell-based configuration service with shuffle-sharded clients; inject a poison configuration | Blast-radius numbers with and without cells | 4 h |
| 5 · Post-mortem classification | Classify 10 public post-mortems into failure classes with a shared rubric; inter-rater agreement with a classmate | Rubric, labels and agreement score | 3 h |
| 6 · Threat model (no AI) | Threat model for confidential inference of patient data: assets, adversaries (including the operator), trust boundaries, what TEEs do and do not cover | Threat model document | 3 h |
| 7 · Attestation-gated key release | Launch a confidential VM (or Nitro Enclave); verify its attestation report; release a KMS key only when measurements match | Policy, verification code and a denied release for a modified image | 5 h |
| 8 · SCI measurement | Compute the Software Carbon Intensity of your CLD404 inference service per 1,000 requests, using energy telemetry or estimates and grid intensity | SCI calculation with uncertainty | 4 h |
| 9 · Carbon-aware batch scheduling | Shift a batch workload in time (and, where residency allows, between Indian regions) using grid-intensity forecasts | Measured or estimated emissions saving and its effect on completion time | 4 h |
| 10 · Compliance matrix | Map DPDP Rules, RBI, CERT-In and SEBI obligations to concrete controls for a fintech cloud estate | Matrix with control owners and evidence | 4 h |

## Projects

### P1 · A reading-and-reproduction brief (L4, ~6 hours)

**Real-world inspiration:** systems research advances by reproducing claims under new conditions; the [Firecracker](https://www.usenix.org/conference/nsdi20/presentation/agache) and [Tail at Scale](https://research.google/pubs/the-tail-at-scale/) papers make measurable claims that can be tested on today's cloud.

**What to build:** choose one assigned paper. Write a 3-page brief: claims, method, what has changed since publication (hardware, products), and a small reproduction of one quantitative claim on current cloud infrastructure.

**Acceptance criteria:**
- The reproduction includes at least 5 runs with medians and intervals, and states every difference from the original setup.
- The brief states whether the claim holds, partially holds or fails today, with evidence.
- Artefacts (scripts, data) are in a public repository with a README that lets a classmate rerun them.
- **Cost ceiling:** US$10.

**Stretch goals:** submit the reproduction to a reproducibility initiative or student track.

**What it proves to an employer:** you can test claims instead of repeating them, which research and platform teams value.

### P2 · A sovereignty and confidentiality design for an Indian public-sector AI service (L4, ~15 hours)

**Real-world inspiration:**
- India's DPDP Rules 2025, CERT-In's 2022 directions and SEBI's cloud framework.
- IndiaAI's planned secure national GPU cluster ([PIB, February 2026](https://static.pib.gov.in/WriteReadData/specificdocs/documents/2026/feb/doc2026210784401.pdf)).
- Europe's sovereign-cloud offerings from [AWS](https://press.aboutamazon.com/aws/2026/1/aws-launches-aws-european-sovereign-cloud-and-announces-expansion-across-europe) and [Microsoft](https://blogs.microsoft.com/blog/2025/06/16/announcing-comprehensive-sovereign-solutions-empowering-european-organizations/) as comparison points.
- The service is an *illustrative scenario*: a citizen-grievance assistant for a state government that processes personal data in several Indian languages.

**What to build:** a design document with:
- the legal and regulatory requirements traced to their primary texts;
- a residency, sovereignty and operational-control analysis of three deployment options (Indian hyperscaler region, MeitY-empanelled Indian provider, on-premises or air-gapped);
- a confidential-computing design (attested confidential VMs or GPUs with key release) and its residual risks;
- a logging and incident-reporting design that meets the 6-hour CERT-In requirement;
- a small working prototype of attestation-gated key release from Lab 7.

**Acceptance criteria:**
- Every requirement cites a primary source (regulation, notified rule or official guidance), with its commencement date.
- The three options are compared on at least eight criteria, including feature availability, cost, operator access and exit.
- The prototype releases the key only to an attested environment and refuses a modified image.
- A one-page residual-risk statement a non-technical official could sign.
- **Cost ceiling:** US$15.

**Stretch goals:** confidential GPU inference with attestation; a formal model of the key-release protocol in TLA+ or ProVerif.

**What it proves to an employer:** you can turn law and threat models into a buildable, defensible architecture, the core of sovereign-cloud and security-architecture roles.

### P3 · Workshop paper: an original measurement or system study (L5, portfolio-grade, ~30 hours)

**Real-world inspiration:** workshop and student-track papers at venues such as HotOS, HotCloud-style workshops, SoCC, EuroSys and SIGCOMM workshops often start as careful measurement studies. Recent public material provides rich data: the [Llama 3 reliability data](https://arxiv.org/abs/2407.21783), the [IEA Energy and AI report](https://www.iea.org/reports/energy-and-ai/executive-summary), and post-mortems from AWS, Google Cloud and Cloudflare.

**What to build:** a 6–8 page paper with artefacts. Suggested topics (or propose your own):
- The carbon and cost of serving one LLM response in Indian regions versus other regions, using SCI and measured throughput, under residency constraints.
- Performance overhead of confidential VMs or confidential GPUs for inference, across two providers.
- A taxonomy of hidden control-plane dependencies from 30 public post-mortems, with a proposed detection method.
- Cold-start and isolation trade-offs of microVM sandboxes for AI-generated code.
- Accuracy of AI agents at diagnosing injected cloud faults, measured against ground truth.

**Acceptance criteria:**
- **Claim:** one clearly stated, falsifiable claim in the abstract.
- **Method:** experiments repeated enough to report intervals; threats to validity discussed; all costs and configurations listed.
- **Related work:** at least 12 verified citations, each read; no citation you have not opened.
- **Artefacts:** code and data public, with a script that regenerates every figure.
- **Review:** two peer reviews received and a response letter showing how you addressed them.
- **Presentation:** a 15-minute talk at the end-of-term mini-conference.
- **Cost ceiling:** US$40, or use research credits and IndiaAI compute where eligible.

**Stretch goals:** submit to a workshop or student research competition; turn the study into the first chapter of your THS501 thesis.

**What it proves to an employer:** you can create new, checkable knowledge about cloud systems, which opens research-engineering roles and strengthens any senior application.

## Feeds into

- [RES502 Reading, Reproducing and Extending Papers](../../../../05_shared_years_3_to_5/RES502_reading_reproducing_and_extending_papers/README.md): P1 is a first reproduction.
- [THS501 Thesis or Capstone I](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) and [THS502 Thesis or Capstone II](../../../../05_shared_years_3_to_5/THS502_thesis_or_capstone_ii/README.md): P3 is designed to become a thesis chapter.
- [LCH502 Career Launch and Founder Studio](../../../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md): sovereign and confidential AI infrastructure is a credible start-up niche in India.
