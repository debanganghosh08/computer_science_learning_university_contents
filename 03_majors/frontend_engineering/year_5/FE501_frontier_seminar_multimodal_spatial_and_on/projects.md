# FE501 · Labs and projects

This seminar's labs are weekly probes: small, pre-registered experiments with a written prediction, a measurement harness and a one-page result. Projects build toward a workshop-style paper. Every measurement names the device, browser version, model version and settings. Results that do not match a published claim are welcome if they are documented carefully.

## Labs (weekly probes)

| Probe | Goal | You submit | Time |
|---|---|---|---|
| 1 · Feature trace | Trace one web feature from proposal to shipping (or not) in three engines, using specs, intents and standards positions | Timeline with links; a one-paragraph prediction of its future | 3 h |
| 2 · Device inventory | Which on-device AI paths (Chrome built-in APIs, WebGPU engines, WebNN, WASM) run on your laptop and on a low-cost Android phone | Capability table with versions; screenshots of feature detection | 3 h |
| 3 · WebLLM reproduction | Reproduce one throughput result from the WebLLM paper on your hardware | Measured tokens/s with spread; explanation of the gap to the paper | 5 h |
| 4 · Generated-UI error study | 20 Design2Code-style screenshot-to-code cases with a current model; categorise errors; audit accessibility | Error taxonomy; axe results compared with hand-built references | 5 h |
| 5 · Agent-ready site | Expose 3 WebMCP tools; run a browser agent on accessible vs inaccessible versions of one page | Success rates; a standards-position-style review of one draft | 5 h |
| 6 · Voice latency | Voice loop with barge-in; measure each stage of end-to-end latency; 20 code-mixed utterances | Latency breakdown; recognition error table | 4 h |
| 7 · WebXR scene | Scene with controller, hand and transient-pointer selection; 2D fallback; XAUR audit | Demo video; audit with 5 fixes | 6 h |
| 8 · Eg-walker reproduction | Reproduce one benchmark from the Eg-walker paper within a stated tolerance | Numbers, scripts and explanation of differences | 5 h |
| 9 · Upstream contribution | File a reduced browser bug or submit a web-platform-test | Link and summary | 3 h |
| 10 · Study plan | Study design, measures, consent form and data plan for your project | Pre-registration document | 3 h |

## Projects

### P1 · On-device vs cloud: a measured comparison (L1 of this seminar, ~6 hours)

**Real-world inspiration:** product teams now choose between Chrome's built-in models, models they ship themselves on WebGPU, and cloud APIs. Chrome's own documentation lists the hardware those built-in models need and states that the model-based APIs do not run on Chrome for Android.

**What to build:** a test page that runs one task (summarising a 600-word article, in English and in Hindi) through three paths: a Chrome built-in API where available, a Transformers.js or WebLLM model on WebGPU (with WASM fallback), and a cloud model. Measure each path on at least two devices.

**Acceptance criteria:**
- **Metrics:** cold start (download plus compile), warm latency, throughput, peak memory and quality, scored by a written rubric on 20 articles by two raters with agreement reported.
- **Rigour:** at least 5 runs per condition with median and spread; device, browser, model and quantisation stated.
- **Honesty:** a clear statement of which users each path can serve, using your device inventory and the Indian device mix (mostly Android).
- **Output:** a 2-page report with a routing recommendation.

**Stretch goals:** energy measurement on a phone (battery drop over a fixed workload); a WebNN backend where available.

**What it proves to an employer:** you can make an on-device AI decision with evidence instead of enthusiasm.

### P2 · Spatial or agentic prototype with an evaluation (L2 of this seminar, ~15 hours)

**Real-world inspiration:** WebXR (Candidate Recommendation Draft, June 2026) and agent-facing proposals (WebMCP draft, MCP Apps, A2UI) are open for builders and reviewers now. Choose one track.

**Track A, spatial:** an accessible WebXR interface for a real task, such as exploring a 3D model of a heritage site or a lab instrument, with:
- controller, hand and transient-pointer input;
- a seated mode, comfort settings and captions;
- a phone AR mode and a 2D fallback.

**Track B, agentic:** a website that exposes WebMCP tools and an MCP App for the same task (for example booking a slot at a community clinic, an **illustrative scenario**). It includes consequence annotations, approval gates and an audit log, and is evaluated with two different agents.

**Acceptance criteria (both tracks):**
- **Evaluation:** a task-based evaluation with at least 5 participants (Track A) or at least 50 agent runs across two agents (Track B), reporting success, time, errors and, for Track B, unsafe-action attempts blocked.
- **Accessibility:** Track A passes your XAUR checklist and holds the target frame rate (72 Hz or the device's native rate) for 10 minutes. Track B passes WCAG 2.2 AA for human users, so agents and people share one accessible interface.
- **Security (Track B):** a 20-case prompt-injection suite causes zero unapproved consequential actions.
- **Reproducibility:** a classmate reproduces your evaluation from your artifacts in under an hour.
- **Write-up:** a 4-page report that includes what failed and why.

**Stretch goals:** Track A, shared multi-user sessions; Track B, the same tool surface rendered as A2UI in a second host.

**What it proves to an employer:** you can build on draft standards and judge them with data, a skill browser, platform and AI-product teams look for.

### P3 · Seminar paper with reproducible artifacts (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** workshop papers at venues such as CHI, UIST and CSCW, and arXiv preprints with released code, are how new interface ideas are tested in public. Several sources in this course (WebLLM, Eg-walker, Design2Code, Generative UI) are examples of the format.

**What to build:** a research prototype and a 6–8 page paper on a question from the seminar. Example questions:
- How much quality and latency do Indic-language users lose when on-device models replace cloud models on mid-range phones?
- Does making a site agent-ready through accessibility improvements alone match the success rate of explicit WebMCP tools?
- Which interaction technique reduces errors for multi-turn editing of generated UI?
- How large does CRDT metadata grow for a year of realistic Hindi/English document editing on low-end devices, and which algorithm handles it best?

**Acceptance criteria:**
- **Claim and method:** one clearly stated claim; a pre-registered method (from Probe 10); appropriate baselines; at least one result that could have come out the other way.
- **Evidence:** either a user study with at least 8 participants and ethics approval as required by your institution, or a benchmark of at least 50 tasks or runs with variance reported.
- **Artifacts:** code, data (or synthetic data with a generator) and scripts released under an open licence; a classmate reproduces the main figure in under one hour.
- **Writing:** related work that cites only sources you have read; limitations and threats to validity; a statement of AI tools used in the research and how outputs were checked.
- **Presentation:** a 15-minute talk with a live demo; 20-minute oral defence.
- **Upstream (strongly encouraged):** one issue, test or pull request to a relevant standard or open-source project that came from your findings.

**Stretch goals:** submit to a workshop or post on arXiv; continue the work as your [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) thesis.

**What it proves to an employer or a research group:** you can create new knowledge about interfaces with sound methods, and share it in a form others can check. That is the L5 bar.

## Feeds into

- [THS501 Thesis or Capstone I](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) and [THS502 Thesis or Capstone II](../../../../05_shared_years_3_to_5/THS502_thesis_or_capstone_ii/README.md): P3 can become the thesis proposal.
- [RES502 Reading, Reproducing and Extending Papers](../../../../05_shared_years_3_to_5/RES502_reading_reproducing_and_extending_papers/README.md): Probes 3 and 8 count as reproduction practice.
- [LCH502 Career Launch and Founder Studio](../../../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md): P1 and P2 are evidence for founder or frontier-role applications.
