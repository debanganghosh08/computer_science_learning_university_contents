# FE501 · Frontier Seminar: Multimodal, Spatial and On-Device AI Interfaces

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 5 · 9 | 4 (≈ 120 hours) | L4 → L5 | [FE401](../../year_4/FE401_full_stack_frameworks_rendering_data_fetching/README.md), [FE403](../../year_4/FE403_ai_native_interfaces_streaming_generative_ui/README.md) (and in practice [FE402](../../year_4/FE402_advanced_ui_animation_graphics_webgl_and_webgpu/README.md)) | [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md), [THS502](../../../../05_shared_years_3_to_5/THS502_thesis_or_capstone_ii/README.md), [LCH502](../../../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md) |

Part of the [Frontend Engineering major](../../README.md). Taken alongside [RES501](../../../../05_shared_years_3_to_5/RES501_research_methods_and_scientific_writing/README.md) (research methods) and [RES502](../../../../05_shared_years_3_to_5/RES502_reading_reproducing_and_extending_papers/README.md) (reproducing papers). The topics are the frontier as of late 2026, so the reading list is reviewed every term. The seminar format is the same each week: read, present, build a small probe, and write.

## Why this course matters now

The interface layer is changing faster than at any time since the smartphone:
- **On-device models in the browser.** Chrome ships them (Summarizer, Translator and Language Detector since Chrome 138; the Prompt API on the web since Chrome 148). WebNN, a W3C API for hardware-accelerated neural-network inference, is a Candidate Recommendation Draft (October 2026). Libraries such as WebLLM and Transformers.js run models on WebGPU.
- **Generated interfaces.** Generated UIs matched expert-built interfaces in about half of cases in one 2026 study, yet the best model completed only 37.3% of five-turn generative-UI tasks on another benchmark.
- **The agentic web.** Agents are becoming users of websites: WebMCP drafts how pages expose tools to them, and MCP Apps and A2UI define how agents show UI.
- **Spatial computing.** The WebXR Device API is a W3C Candidate Recommendation Draft (June 2026), and headset browsers have added new input models such as gaze-and-pinch.
- **Local-first software.** Ink & Switch's research programme has produced new collaboration algorithms (Eg-walker, Fugue).

None of this is settled, and much of it fails on the devices most Indian users own. The frontier engineer's job is to separate demos from durable change with measurements, to build prototypes that test claims, and to contribute to the standards and open-source projects that decide what ships.

## Learning outcomes

By the end you can:

1. **Read** specifications, standards positions and research papers critically, and **summarise** what is proven, what is claimed and what is missing.
2. **Measure** on-device model performance in the browser (load time, tokens per second, memory, energy, quality) across backends and devices, and **decide** between on-device, cloud and hybrid with evidence.
3. **Evaluate** generative and malleable interfaces with task-based studies and benchmarks, and **identify** their failure modes.
4. **Prototype** agent-facing web interfaces (WebMCP tools, MCP Apps, A2UI renderers), and **threat-model** them.
5. **Build** multimodal (voice, vision) and spatial (WebXR) interactions that meet accessibility and comfort requirements.
6. **Explain** local-first architectures and the trade-offs of current CRDT algorithms, and **reproduce** a published result.
7. **Design and run** a small study with sound methods and ethics, and **write** it up as a short paper with reproducible artifacts.
8. **Contribute** to a standard, a browser bug tracker or an open-source project in this area.

## Chapters and lessons

### Chapter 1 · Reading the frontier (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 How the web platform changes | W3C working groups and community groups, WHATWG, TC39; Chromium "intent to ship"; Mozilla and WebKit standards positions; Interop | Trace one feature (for example WebGPU) from proposal to shipping in three engines |
| 1.2 Reading papers | Venues (CHI, UIST, CSCW, Onward!, EuroSys, NeurIPS/EMNLP for benchmarks), arXiv preprints vs peer review, reading for claims and threats to validity | One-page critical summary of the Generative UI paper (Leviathan et al., 2026) |
| 1.3 Hype filters | Demo vs deployment, cherry-picked devices, missing baselines, benchmark contamination | Rewrite 3 product announcements as testable claims |
| 1.4 Setting up a probe | A small, falsifiable experiment per week with a written prediction | Pre-register a prediction for next week's probe |

**Check your understanding:** What is the difference between a feature shipping in Chrome and a feature being part of the web? Why should a benchmark result on arXiv change your plans less than a shipped standard? What makes a prediction falsifiable?

### Chapter 2 · On-device AI interfaces (weeks 2–3)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 The landscape | Chrome built-in AI APIs and their hardware needs; WebGPU-based engines (WebLLM, Transformers.js); WebNN and NPUs | Inventory which of these run on your laptop and on a low-cost Android phone |
| 2.2 Measuring | Model download and compile time, tokens per second, memory, thermal throttling over minutes, battery drain | Reproduce one throughput figure from the WebLLM paper on your hardware; explain the gap |
| 2.3 Quality vs size | Quantisation (`q4`, `q8`, `fp16`), small vs large models, task-specific evaluation | Compare 3 quantisation levels on a summarisation task with a rubric |
| 2.4 Hybrid design | Capability detection, routing, privacy claims you can honestly make, consent for large downloads | Design a routing policy for a product used mainly on Android phones in India |
| 2.5 Indic languages on-device | Language coverage of small models, tokenisation cost of Indic scripts, transliteration | Measure tokens per sentence for Hindi vs English with one tokenizer |

**Check your understanding:** Why might on-device inference be slower and still better for a user? What does a 1 GB model download cost a user on a metered connection? Which Indian users can use Chrome's built-in models today, and what follows for product design?

### Chapter 3 · Generative and malleable interfaces (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Generative UI evidence | Leviathan et al. (2026) on preference and expert parity; EvoGenUI-Bench (2026) on multi-turn failure | Present one paper; propose an experiment it did not run |
| 3.2 Design-to-code research | Design2Code (NAACL 2025) and Interaction2Code: what models get wrong (layout recall, interaction logic) | Run 20 Design2Code-style cases with one current model; categorise errors |
| 3.3 Malleable software | Ink & Switch's essay on malleable software; end-user programming; who gets to change an interface | Prototype one "user-modifiable" feature on top of a generated UI |
| 3.4 Risks | Inconsistency, accessibility regressions, dark patterns at generation time, accountability | Audit 10 generated interfaces for accessibility; compare with hand-built ones |

**Check your understanding:** Why does a preference study that ignores generation speed overstate real-world value? What would a fair benchmark of generative UI measure? Who is responsible when a generated interface misleads a user?

### Chapter 4 · The agentic web (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Agents as users | Browser agents reading the accessibility tree and screenshots; why semantic HTML and ARIA now matter twice | Run a browser agent on an accessible and an inaccessible version of one site; compare success |
| 4.2 Sites exposing tools | WebMCP draft: `document.modelContext`, tool schemas, annotations, permission policy | Expose 3 tools from a site and test them |
| 4.3 Agents showing UI | MCP Apps (stable January 2026), A2UI (declarative JSON), AG-UI events; how they combine | Render the same tool result as an MCP App and as an A2UI payload |
| 4.4 Security and governance | Prompt injection through tool metadata and outputs, consent, auditability, rate limits | Write a standards-position-style review of one draft |

**Check your understanding:** Why might accessibility work become the cheapest way to make a site agent-ready? What new attack surface does a tool-exposing website create? Should a declarative UI format or sandboxed HTML win, and for which hosts?

### Chapter 5 · Multimodal interaction (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Voice-first interfaces | Turn-taking, barge-in, latency budgets for conversation, realtime speech APIs over WebRTC or WebSockets | A voice interface with interruption; measure end-to-end latency |
| 5.2 Vision as input | Camera capture, on-device vision models, privacy indicators | A camera-based form-filling probe that runs on-device |
| 5.3 Multimodal accessibility | Alternatives for every modality, captions and transcripts, users who cannot speak or see | Accessibility review of your voice probe with a disabled user if possible, or with expert guidance |
| 5.4 Multilingual voice in India | Code-mixed speech (Hinglish), regional languages, public resources such as Bhashini | Measure recognition errors on 20 code-mixed utterances across two services |

**Check your understanding:** What latency makes a voice conversation feel natural, and where does the time go? Why is code-mixing a hard problem for speech systems? What must every voice-first feature provide for users who cannot use voice?

### Chapter 6 · Spatial computing on the web (weeks 7–8)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 WebXR fundamentals | Sessions (`immersive-vr`, `immersive-ar`), reference spaces, frames and poses; the AR module; layers | A WebXR scene with feature detection and a 2D fallback |
| 6.2 Input | Controllers, hands, gaze-and-pinch with the `transient-pointer` input mode (WebKit on Apple Vision Pro) | Selection that works with controllers, hands and transient pointers |
| 6.3 Spatial UI design | Comfort (frame rate, motion sickness), text legibility at distance, depth and occlusion, ergonomics | Port a 2D dashboard into a comfortable spatial layout; test for 10 minutes |
| 6.4 XR accessibility | W3C XR Accessibility User Requirements (XAUR): alternatives to motion, captions, seated modes | Audit your scene against XAUR; fix 5 issues |
| 6.5 Platforms and reach | Headset browsers, Android XR, phone-based AR; why most users meet "spatial" through a phone | Build a phone AR preview with a non-AR fallback |

**Check your understanding:** Why is frame rate an accessibility and comfort requirement in XR, not just a performance target? What does the transient-pointer model protect, and what does it make harder? Who in India can use a WebXR feature today, and what should everyone else see?

### Chapter 7 · Local-first software (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Principles | The local-first essay's seven ideals; data ownership and longevity | Score your FE404 P2 against the ideals |
| 7.2 Algorithms | Fugue (interleaving), Eg-walker (event graphs), Peritext (rich text); performance and memory trade-offs | Reproduce one benchmark from the Eg-walker paper within a stated tolerance |
| 7.3 Sync infrastructure | Relay servers, end-to-end encryption, access control in a peer-to-peer setting | Design access revocation for an encrypted, local-first document |
| 7.4 Open problems | Schema evolution, very long histories, authorisation, hosting economics | Write a 1-page research question for one open problem |

**Check your understanding:** What does a user gain and lose when their data lives first on the device? Why is revoking access hard in local-first systems? Which open problem would most help Indian users on low-end devices?

### Chapter 8 · The platform frontier (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 WebAssembly for UI | Wasm for compute-heavy features, JavaScript Promise Integration (an Interop 2026 focus area), compile-to-Wasm UI experiments | Move one hot path to Wasm; measure the real gain including transfer |
| 8.2 New transports | WebTransport (Baseline March 2026) for low-latency streams | Compare WebSocket and WebTransport for a realtime probe |
| 8.3 Engines and interop | New engines and the role of Interop; investigation areas such as accessibility and mobile testing in Interop 2026 | Report one interoperability bug you find, with a minimal test case |
| 8.4 Contributing upstream | Filing good browser bugs, writing web-platform-tests, joining community groups (open to anyone) | File one bug or one web-platform-test pull request |

**Check your understanding:** When does WebAssembly make a page slower? What makes a browser bug report get fixed? Why are web-platform-tests a high-leverage contribution?

### Chapter 9 · Research methods for interface work (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Study design | Within- vs between-subjects, tasks, measures (success, time, errors, workload, trust), sample size and its limits | Design a study for your seminar project |
| 9.2 Benchmarks | Building a benchmark: task selection, scoring, contamination, reporting variance | Draft 20 tasks for a small benchmark in your area |
| 9.3 Ethics | Consent, privacy, vulnerable participants, compensation, institutional review where required | Write a consent form and data-handling plan |
| 9.4 Reproducibility | Artifacts, versions, seeds, hardware disclosure, negative results | Package last week's probe so a classmate reproduces it in 30 minutes |

**Check your understanding:** Why are five participants enough for some usability findings but not for statistical claims? How do you keep a benchmark meaningful when models may have seen it? What must a paper disclose about hardware for on-device results?

### Chapter 10 · Seminar project and paper (weeks 12–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Building the prototype | Scope, risk-first prototyping, measurement harness | Prototype with an evaluation harness |
| 10.2 Running the evaluation | Pilot, run, analyse; reporting honestly, including failures | Completed study or benchmark run |
| 10.3 Writing | A 6–8 page workshop-style paper: problem, related work, method, results, limitations | Paper draft with artifacts |
| 10.4 Presenting and defending | 15-minute talk, live demo, questions | Seminar conference day |

**Check your understanding:** What is the single claim your paper makes, and what evidence would falsify it? Which limitation would a reviewer raise first? How does your work change what a product team should do?

## Weekly rhythm

| Week | Chapter | Seminar | Deliverable |
|---|---|---|---|
| 1 | 1 | Standards and papers | Feature trace; critical summary |
| 2 | 2 | On-device AI I | Device inventory; **P1 starts** |
| 3 | 2 | On-device AI II | WebLLM reproduction; **P1 due** |
| 4 | 3 | Generative and malleable UI | Design2Code-style error study |
| 5 | 4 | Agentic web | WebMCP tools; standards-position review |
| 6 | 5 | Multimodal | Voice latency probe |
| 7 | 6 | Spatial I | WebXR scene with fallback; **P2 starts** |
| 8 | 6 | Spatial II | XAUR audit; project proposal due |
| 9 | 7 | Local-first | Eg-walker reproduction; **P2 due** |
| 10 | 8 | Platform frontier | Bug report or web-platform-test PR |
| 11 | 9 | Methods and ethics | Study plan and consent form; **P3 starts** |
| 12 | 10 | Project work | Pilot results |
| 13 | 10 | Project work | Paper draft |
| 14 | 10 | Seminar conference | **P3 due**: paper, artifacts, talk |
| 15 | Review | Oral examination | Final defence |

## Working with AI in this course

- **Use AI for:** literature search and summaries (always checked against the paper itself); drafting probes and harnesses; analysing logs; first drafts of related-work sections that you then verify citation by citation.
- **Do without AI (drills):** the critical summaries; the study design and ethics plan; the final oral defence; checking every citation in your paper against the source.
- **Verify AI output by:** opening every cited paper, specification and version (models invent citations and misstate API status for fast-moving drafts); re-running every measurement on named hardware; comparing against the published numbers you are reproducing; recording model versions used anywhere in your pipeline.
- **Where AI still fails here (collect your own evidence):** in this course the main failure is temporal. Models describe drafts as shipped, cite superseded API names (for example earlier WebMCP or MCP-UI shapes), and invent benchmark numbers. Keep a log of each claim you checked and what you found; it is an appendix of your paper.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Weekly probes and critical summaries | 20% |
| Paper presentations (2) | 10% |
| Projects P1 · P2 | 10% · 15% |
| P3: paper, artifacts and talk | 30% |
| Final oral defence | 15% |

**Mastery gate.** You pass when you can:
1. reproduce one published result (from WebLLM, Eg-walker, Design2Code or another paper approved by the instructor) within a stated tolerance, or explain the discrepancy with evidence;
2. deliver a 6–8 page paper with reproducible artifacts that a classmate can run in under an hour;
3. defend the paper's central claim and its limitations in a 20-minute oral examination.

## Industry reality

Frontier interface work happens at browser vendors, AI labs, design-tool companies, standards bodies and open-source projects, and increasingly inside product teams deciding whether to ship on-device or agentic features. The [FE market page](../../../../06_career_and_market_readiness/01_market_map/roles/FE_frontend_engineering.md) lists creative developer (WebGL, WebGPU) and AI interface engineer among the specialisms. The working group page for MCP Apps lists members from Anthropic, OpenAI and Google. WebMCP's draft is edited by people from Microsoft and Google. Community groups at W3C are open to individuals, so a student can take part in the work that defines these interfaces. For founders ([LCH502](../../../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md)), the measurement skills in this course separate a product idea from a demo that only works on a flagship laptop.

**Interview questions from this course**

1. *Should this feature run on-device or in the cloud?* A strong answer measures capability coverage on the real user device mix (for example, Chrome's built-in models do not run on Chrome for Android) and model download size against data costs, quality on the task, latency, privacy and cost. It proposes hybrid routing with disclosure.
2. *How would you evaluate a generative UI system?* A strong answer gives task-based success across multiple turns (citing failure on multi-turn edits), state-consistency checks, accessibility audits, expert comparison, latency, and user studies, with contamination controls for benchmarks.
3. *What makes a website usable by AI agents, and what are the risks?* A strong answer covers semantic HTML and an accurate accessibility tree, explicit tools with schemas (WebMCP draft) and consequence annotations. It names prompt injection through tool outputs, over-broad tools and privacy leakage as risks, and adds permission policies and audit logs.
4. *Design an accessible WebXR interaction for selecting objects.* A strong answer supports controllers, hands and transient-pointer input, gives a seated mode and a non-motion alternative, uses legible text sizes at distance, holds a stable frame rate, and provides a 2D fallback, citing XAUR.
5. *When would you not use CRDTs for collaboration?* A strong answer names cases: when a central authority must validate every change (money, inventory), when metadata growth matters on small devices, or when OT or server locking is simpler for the product. It explains revocation and schema-evolution problems in local-first systems.

## Resources (free first)

- **On-device AI:** [Chrome built-in AI](https://developer.chrome.com/docs/ai/built-in) and [API status](https://developer.chrome.com/docs/ai/built-in-apis); [WebNN](https://www.w3.org/TR/webnn/); Ruan et al., [WebLLM](https://arxiv.org/abs/2412.15803); [Transformers.js](https://huggingface.co/docs/transformers.js/index); [ONNX Runtime Web](https://onnxruntime.ai/docs/tutorials/web/).
- **Generative and malleable UI:** Leviathan et al., [Generative UI](https://arxiv.org/abs/2604.09577); Peng et al., [EvoGenUI-Bench](https://arxiv.org/abs/2608.29387); Si et al., [Design2Code](https://arxiv.org/abs/2403.03163); [Interaction2Code](https://arxiv.org/abs/2411.03292); Ink & Switch, [Malleable software](https://www.inkandswitch.com/essay/malleable-software/); Amershi et al., [Guidelines for Human-AI Interaction](https://doi.org/10.1145/3290605.3300233).
- **Agentic web:** [WebMCP draft](https://webmachinelearning.github.io/webmcp/); [MCP Apps](https://modelcontextprotocol.io/extensions/apps/overview); [A2UI](https://a2ui.org/); [AG-UI](https://ag-ui.com/); [Google: A2UI + MCP Apps](https://developers.googleblog.com/en/a2ui-and-mcp-apps/).
- **Spatial:** [WebXR Device API](https://www.w3.org/TR/webxr/); [MDN WebXR](https://developer.mozilla.org/en-US/docs/Web/API/WebXR_Device_API); [WebXR samples](https://immersive-web.github.io/webxr-samples/); [WebKit: natural input for WebXR on Apple Vision Pro](https://webkit.org/blog/15162/introducing-natural-input-for-webxr-in-apple-vision-pro/); [XR Accessibility User Requirements](https://www.w3.org/TR/xaur/); [Android XR developer docs](https://developer.android.com/develop/xr).
- **Local-first:** [Local-first software](https://www.inkandswitch.com/essay/local-first/); [Eg-walker](https://arxiv.org/abs/2409.14252); [Fugue](https://arxiv.org/abs/2305.00583); [Peritext](https://www.inkandswitch.com/peritext/); [crdt.tech](https://crdt.tech/).
- **Platform:** [webstatus.dev](https://webstatus.dev/); [Interop 2026 dashboard](https://wpt.fyi/interop-2026); [TC39 proposals](https://github.com/tc39/proposals); [Bhashini](https://bhashini.gov.in/).

## Sources

All checked 12 Oct 2026.

- Chrome for Developers, built-in AI API status and hardware requirements — https://developer.chrome.com/docs/ai/built-in-apis · https://developer.chrome.com/docs/ai/get-started
- W3C, Web Neural Network API, Candidate Recommendation Draft (10 Oct 2026) — https://www.w3.org/TR/webnn/
- W3C, WebXR Device API, Candidate Recommendation Draft (9 Jun 2026) — https://www.w3.org/TR/webxr/
- WebKit, "Introducing Natural Input for WebXR in Apple Vision Pro" (19 Mar 2024) — https://webkit.org/blog/15162/introducing-natural-input-for-webxr-in-apple-vision-pro/
- Leviathan et al., arXiv 2604.09577 (Feb 2026) — https://arxiv.org/abs/2604.09577 · Peng et al., arXiv 2608.29387 (Aug 2026) — https://arxiv.org/abs/2608.29387 · Si et al., arXiv 2403.03163 (NAACL 2025) — https://arxiv.org/abs/2403.03163 · Interaction2Code, arXiv 2411.03292 — https://arxiv.org/abs/2411.03292 · WebLLM, arXiv 2412.15803 — https://arxiv.org/abs/2412.15803
- Web Machine Learning CG, WebMCP Draft Community Group Report (9 Oct 2026) — https://webmachinelearning.github.io/webmcp/
- MCP Apps Working Group charter (stable spec 26 Jan 2026; membership) — https://modelcontextprotocol.io/community/working-groups/apps
- Google Developers Blog, A2UI + MCP Apps (17 Jun 2026) — https://developers.googleblog.com/en/a2ui-and-mcp-apps/
- Mozilla Hacks, "Launching Interop 2026" — https://hacks.mozilla.org/2026/02/launching-interop-2026/
- web-features 3.42.0 (WebTransport Baseline Mar 2026) — https://web-platform-dx.github.io/web-features/
- Ink & Switch, Local-first software (2019) — https://www.inkandswitch.com/essay/local-first/ · Eg-walker, arXiv 2409.14252 — https://arxiv.org/abs/2409.14252 · Fugue, arXiv 2305.00583 — https://arxiv.org/abs/2305.00583

_Last reviewed: 2026-10_
