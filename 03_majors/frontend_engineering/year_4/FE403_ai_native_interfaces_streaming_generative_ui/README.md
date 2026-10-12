# FE403 · AI-Native Interfaces: Streaming, Generative UI and Agent UX

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 8 | 4 (≈ 120 hours) | L3 → L4 | [FE303](../../year_3/FE303_css_design_systems_and_accessibility/README.md) (and in practice [FE301](../../year_3/FE301_modern_javascript_and_typescript_in_depth/README.md), [FE302](../../year_3/FE302_react_and_component_architecture/README.md)) | [FE501](../../year_5/FE501_frontier_seminar_multimodal_spatial_and_on/README.md), [OV08A](../../../../04_overlaps/OV08_full_stack_ai_product_engineering/OV08A_shipping_ai_features_end_to_end/README.md), [OV08B](../../../../04_overlaps/OV08_full_stack_ai_product_engineering/OV08B_product_analytics_and_growth_for_ai_apps/README.md) |

Part of the [Frontend Engineering major](../../README.md) and one of the three courses of the [OV08 Full-Stack AI Product Engineering](../../../../04_overlaps/OV08_full_stack_ai_product_engineering/README.md) overlap, alongside [BE403](../../../backend_engineering/year_4/BE403_backends_for_ai_serving_llm_features_vector/README.md) and [AIE404](../../../ai_engineering/year_4/AIE404_ai_product_engineering_and_ux/README.md). This course is about the interface. It treats models as given; prompting and evaluation of the model itself belong to the AIE major.

## Why this course matters now

Most new product features now involve a model somewhere, and the interface decides whether users can trust them. In the 2026 Stack Overflow survey, 48.0% of developers said they trust AI output only when they can easily verify it, and just 6.6% trust it for important decisions. Verification is an interface problem: citations, previews, diffs, undo and approval steps. The interface layer is also being standardised:
- **MCP Apps**, the first official Model Context Protocol extension, became a stable specification in January 2026. It unifies the MCP-UI and OpenAI Apps SDK approaches for interactive UIs inside assistants.
- **Google's A2UI** (v0.9) has agents send declarative JSON that hosts render with native components.
- **WebMCP**, a draft Community Group report of October 2026, lets websites expose tools to browser agents.
- **Chrome** ships built-in on-device models. Its Summarizer, Translator and Language Detector APIs have been stable since Chrome 138, and the Prompt API reached the web in Chrome 148. They do not run on Chrome for Android, and India's web users are mostly on Android phones.

Research shows both the promise and the gap. Generated interfaces were strongly preferred over plain text and matched expert-built ones in about half of cases (Leviathan et al., 2026). Yet on a multi-turn generative-UI benchmark, the best of eight models completed only 37.3% of five-turn tasks correctly (EvoGenUI-Bench, 2026). An engineer who can make streaming, generated and agentic interfaces fast, safe, accessible and honest about uncertainty is in demand. That job did not exist five years ago.

## Learning outcomes

By the end you can:

1. **Apply** published human–AI interaction guidelines (Microsoft HAX, Google PAIR) to design features that set expectations, show uncertainty and support correction.
2. **Implement** streaming over SSE, fetch streams, WebSockets and WebTransport, with cancellation, reconnection, resume and backpressure.
3. **Render** streamed model output incrementally and safely: partial Markdown, sanitisation, Trusted Types, no layout shift, and screen-reader-friendly announcements.
4. **Build** chat and agent interfaces: message parts, branching, regeneration, tool-call visualisation, progress for long tasks, interruption, human approval and undo.
5. **Design and secure** generative UI: model-selected components, declarative specifications (A2UI-style), sandboxed MCP Apps, constrained to a design system.
6. **Hide latency and control cost** with streaming, optimistic UI, speculative work, caching and model routing, and **measure** time-to-first-token and time-to-useful-output.
7. **Integrate** on-device AI (Chrome built-in AI APIs, Transformers.js and WebLLM on WebGPU, WebNN), with feature detection, download UX and cloud fallback.
8. **Evaluate** AI UX with task success, correction rates, trust calibration and red-team tests for prompt injection that surfaces in the interface.

## Chapters and lessons

### Chapter 1 · Foundations of human–AI interaction (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 The model as an unreliable collaborator | Probabilistic output, confident errors, non-determinism; what that means for UI | List the failure modes of 3 AI features you use daily |
| 1.2 Guidelines that hold up | Microsoft's 18 Guidelines for Human-AI Interaction (CHI 2019), Google PAIR Guidebook: set expectations, support correction, explain, scope services when in doubt | Audit an AI feature against the 18 guidelines |
| 1.3 When not to use AI | Deterministic tasks, high-stakes actions, latency-critical paths | Rewrite one "AI-powered" feature as a plain UI; compare task time |
| 1.4 Designing for verification | Citations, source previews, diffs, side-by-side comparisons, "show your working" | Design three verification affordances for a summarisation feature |

**Check your understanding:** Why does a confident tone in AI output raise the cost of errors? What does "support efficient correction" mean for a chat interface? When is an AI feature worse than no feature?

### Chapter 2 · Streaming transports (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Server-Sent Events | `EventSource`, event format, `Last-Event-ID` resume, limits (GET only, connection caps on HTTP/1.1) | Stream tokens over SSE with resume after a dropped connection |
| 2.2 Fetch streams | `ReadableStream`, `TextDecoderStream`, parsing SSE or NDJSON from a `POST` response, `AbortController` to stop generation | Build a streaming client with Stop that also cancels server work |
| 2.3 WebSockets and WebTransport | Bidirectional streams for voice and collaboration; WebTransport (Baseline March 2026) | Compare latency and reconnection behaviour of the three transports |
| 2.4 Infrastructure pitfalls | Proxy and CDN buffering, compression interfering with flushing, serverless timeouts, mobile network handovers | Find and fix a buffering proxy that delivers all tokens at once |

**Check your understanding:** Why does Stop need to cancel work on the server as well as in the browser? Why might tokens arrive in one burst after 10 seconds in production but stream smoothly locally? When would you choose WebSockets over SSE for an AI feature?

### Chapter 3 · Rendering streamed output safely (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Incremental Markdown | Unterminated code fences, tables and lists mid-stream; re-parsing cost; block-level memoisation | Render a 20,000-token stream with at most one re-render per animation frame |
| 3.2 Output is untrusted input | XSS through model output and through retrieved content; sanitising with DOMPurify; Trusted Types (Baseline February 2026); link and image policies | Pass a suite of 30 hostile outputs with zero script execution |
| 3.3 Layout stability | Reserving space, scroll anchoring, "stick to bottom unless the user scrolled up", no CLS from code blocks | Stream into a chat with CLS 0 and correct scroll behaviour |
| 3.4 Accessibility of streams | Not announcing every token; polite live regions on completion; a busy state (`aria-busy`); keyboard access to Stop | Pass an NVDA and TalkBack script for a streamed answer |

**Check your understanding:** Why is model output a security boundary even when your own model produced it? What should a screen reader announce while an answer streams? Why does re-parsing all Markdown on every token make long answers slow?

### Chapter 4 · Chat architecture (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 The message model | Messages made of parts (text, reasoning summaries, tool calls, files, sources); IDs; persistence | Design a typed message schema with Zod; validate every stored message |
| 4.2 Conversation operations | Edit and resend, regenerate, branch and switch branches, delete; what each does to history | Implement branching with a tree; render the active path |
| 4.3 Client libraries | AI SDK (v7 on npm) chat hooks, assistant-ui, CopilotKit; what they decide for you | Build the same chat with two libraries; compare control and bundle size |
| 4.4 Sync and offline | Multi-tab and multi-device sync, optimistic sends, retries, drafts | Keep a draft and a pending message safe across a reload and a network drop |

**Check your understanding:** Why should a message be a list of parts rather than a string? What happens to tool results when a user edits an earlier message? What do chat libraries make easy, and what do they make hard to change later?

### Chapter 5 · Tool calls and agent UX (weeks 5–6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Visualising tool calls | States (pending, running, succeeded, failed), arguments and results shown at the right level of detail | Render tool calls for a search, a calculation and a file edit |
| 5.2 Long-running agents | Plans and checklists, step progress, partial results, background runs with notifications | A research agent UI with a live plan and resumable progress |
| 5.3 Control | Interrupt, steer, pause and resume; queueing user messages during a run | Make "Stop" and "Change direction" work mid-run within 200 ms |
| 5.4 Human approval | Classifying actions by consequence; approval prompts with clear diffs; never auto-approving irreversible actions | Gate payments, emails and deletions behind approval with a preview |
| 5.5 Undo and audit | Reversible actions, compensating actions, audit trails users can read | Undo an agent's last three actions; show an audit log |
| 5.6 Event protocols | Streaming agent events to the UI with AG-UI-style event types; mapping backend agent frameworks to UI state | Drive your UI from a recorded event stream with no live model |

**Check your understanding:** Which agent actions need approval, and who decides? What should the UI show when a tool fails halfway through a plan? Why record and replay agent event streams for UI development?

### Chapter 6 · Generative UI (weeks 7–8)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 What generative UI is | Model-selected components vs model-written markup vs declarative specs; evidence from Leviathan et al. (2026) | Classify 5 products' generative UI by approach |
| 6.2 Tools to components | Mapping tool results to typed components from your design system; schemas as the contract | A travel assistant that returns flight cards, a fare table and a seat map from typed tool results |
| 6.3 Declarative specs | A2UI-style JSON rendered by host-native components; allow-listing components and props | Render A2UI-style payloads with FE303's components; reject unknown components |
| 6.4 MCP Apps | Interactive UI resources delivered by MCP servers, rendered in sandboxed iframes, talking to the host over JSON-RPC; host support (Claude, ChatGPT, VS Code and others) | Build a small MCP App and run it in a reference host |
| 6.5 Security of generated UI | Sandbox attributes, CSP, postMessage origin checks, prompt injection through UI content, consequential actions from generated UI | Threat-model your MCP App; fix three findings |
| 6.6 Keeping state in sync | The failure classes EvoGenUI-Bench found: derived-state propagation, affordance binding, external state | Write tests that check UI state, external state and the assistant's claims agree after each turn |

**Check your understanding:** Why constrain a model to your design system rather than let it write HTML? What can a malicious MCP App do if the host's sandbox is weak? Why does multi-turn editing of generated UI fail much more often than single-turn generation?

### Chapter 7 · Errors, uncertainty and trust (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Failure states | Refusals, rate limits, timeouts, partial failures, content filters, empty retrieval; a message for each | Design and implement 8 failure states with recovery actions |
| 7.2 Showing uncertainty | Citations and source previews, "I don't know" paths, why numeric confidence scores often mislead | Add inline citations with hover previews; test with 5 users |
| 7.3 Correction loops | Edit-to-correct, thumbs with reasons, "this is wrong" flows that change the next answer | Capture corrections as structured feedback events |
| 7.4 Prompt injection in the UI | Untrusted content labelled as such, separating instructions from data visually, no hidden actions | Red-team a summariser with 20 injected documents; confirm no unsafe action fires |

**Check your understanding:** Why can a percentage confidence score be worse than none? How should an interface show content that came from an untrusted web page? What makes user feedback actually useful to the team improving the model?

### Chapter 8 · Latency, cost and perceived performance (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Response-time limits | 0.1 s, 1 s and 10 s thresholds (Nielsen); time-to-first-token vs time-to-useful-output | Measure both for 3 AI features you use |
| 8.2 Hiding latency | Streaming, skeletons shaped like the answer, optimistic UI, showing plans first, progressive disclosure | Cut perceived wait in a summariser without changing the model |
| 8.3 Speculation and caching | Prefetching likely prompts, caching deterministic results, semantic caches (with care) | Add a cache; prove it never serves one user's answer to another |
| 8.4 Cost-aware UX | Routing simple tasks to smaller models, cancelling unneeded generations, limits that users understand | Show the cost per task before and after routing and cancellation |

**Check your understanding:** Why can a slower model with streaming feel faster than a faster model without it? When is a semantic cache unsafe? How do you explain a usage limit without frustrating users?

### Chapter 9 · Multimodal and multilingual input (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Voice | Web Speech API limits and browser differences, realtime voice over WebRTC or WebSockets, push-to-talk vs open mic, barge-in | A voice input with clear listening states and a text fallback |
| 9.2 Images and files | Paste, drop and camera capture; previews; privacy of uploads; size limits on mobile data | Image question flow that works on a low-end Android phone |
| 9.3 Indian languages | Hindi and other Indic input, transliteration (typing Hindi in Latin script), Bhashini as a public language-AI platform, mixed-language answers | A form assistant that accepts Hinglish and answers in the user's script |
| 9.4 Accessible multimodality | Captions, transcripts, alternatives for every modality | Ensure every voice or image feature has an equivalent text path |

**Check your understanding:** What should the UI show while the microphone is open, and why does it matter for trust? Why is transliteration essential for many Indian users? What does an accessible voice feature require beyond speech recognition?

### Chapter 10 · On-device AI in the browser (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Chrome built-in AI | Translator, Language Detector and Summarizer (stable since Chrome 138), Prompt API (web since Chrome 148), Writer, Rewriter and Proofreader (trials); hardware needs (22 GB free disk, a GPU with more than 4 GB VRAM or 16 GB RAM and 4 cores); not on Chrome for Android | Feature-detect and use the Summarizer with a cloud fallback |
| 10.2 Your own models | Transformers.js (WebGPU or WASM, `q4`/`q8` quantisation), WebLLM, ONNX Runtime Web; model size vs quality | Run a small embedding model and a small chat model in the browser; measure load time and tokens per second |
| 10.3 WebNN | The Web Neural Network API (Candidate Recommendation Draft, October 2026) and NPU access | Compare WebNN, WebGPU and WASM backends where available |
| 10.4 Hybrid routing and UX | Download consent and progress, storage, privacy promises, falling back to cloud on low-end devices | Route between on-device and cloud by capability; disclose which ran |

**Check your understanding:** Who in India can use Chrome's built-in models today, and what does that imply for product design? Why might a 1 GB model download be unacceptable even on a fast network? What privacy promise can on-device inference honestly make?

### Chapter 11 · Agent-ready websites and evaluating AI UX (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Websites as tools for agents | WebMCP's draft `document.modelContext.registerTool()`, permission policy, annotations for consequential tools; the accessibility tree as the interface browser agents read | Expose 3 tools from a site; test them with Playwright's WebMCP support |
| 11.2 Risks of agent access | Prompt injection through tool metadata and outputs, over-broad tools, privacy leakage | Threat-model your tools using the risks the WebMCP draft lists |
| 11.3 Measuring AI UX | Task success, time to useful output, edit distance of accepted output, correction and abandonment rates, trust calibration surveys | Instrument an AI feature with these metrics |
| 11.4 Experiments and evals | Offline UI evals with recorded sessions, A/B tests, user studies with 5–8 participants | Run a small study; report findings with quotes and numbers |

**Check your understanding:** Why does good accessibility make a site better for AI agents too? Which metric tells you users over-trust a feature? Why are offline evaluations of AI UX necessary but not sufficient?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Guidelines audit | HAX audit |
| 2 | 2 | Lab 2 · Three transports | Resume and cancel demo |
| 3 | 3 | Lab 3 · Hostile streams | Zero-XSS, zero-CLS renderer; **P1 starts** |
| 4 | 4 | Lab 4 · Branching chat | Typed message store |
| 5 | 5 | Lab 5 · Tool-call UI | Approval and undo; **P1 due** |
| 6 | 5 | Lab 5 (cont.) · Long-running agent | Replayable event stream |
| 7 | 6 | Lab 6 · Tools to components | Typed generative UI; mid-term (AI off) |
| 8 | 6 | Lab 6 (cont.) · MCP App | App plus threat model |
| 9 | 7 | Lab 7 · Failure states and injection | Red-team report; **P2 due** |
| 10 | 8 | Lab 8 · Latency and cost | Before/after report |
| 11 | 9 | Lab 9 · Voice and Indic input | Multimodal form assistant |
| 12 | 10 | Lab 10 · On-device | Hybrid routing; **P3 starts** |
| 13 | 11 | WebMCP and metrics | Tools and dashboards |
| 14 | 11 | User study | **P3 due** |
| 15 | Review | P3 demo and red-team defence | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** everything a product team would, including generating component variants, writing Markdown parsers' test corpora, drafting threat models, simulating users in early tests (never as a replacement for real users), and building MCP servers.
- **Do without AI (drills):** the sanitisation and approval logic (write it and its tests yourself); the guidelines audit; the threat models' final review; the mid-term (design an agent UI on paper for a consequential task) and final.
- **Verify AI output by:** hostile-output test suites (XSS, injection, enormous outputs, malformed streams); Trusted Types enforced in CI; accessibility scripts with NVDA and TalkBack; recorded event-stream replays; latency measured at P75 on a throttled mobile profile; checking protocol details against the current MCP Apps, A2UI and WebMCP documents, because all three changed in 2026.
- **Where AI still fails here (collect your own evidence):** EvoGenUI-Bench reports that the strongest of eight models completed only 37.3% of five-turn generative-UI tasks, with failures in derived-state propagation and affordance binding. In your own work, log generated interfaces whose visible state disagrees with the backend, approval steps that can be bypassed, and output rendered with `innerHTML`. Also log streamed answers announced token by token to screen readers, and AI-written code that trusts tool results or retrieved content as instructions.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1 · P2 · P3 | 10% · 15% · 20% |
| Mid-term (AI off) | 10% |
| Final (AI off, 3 h) and P3 red-team defence | 20% |

**Mastery gate.** You pass when you can, with AI off, in 3 hours, build a streaming assistant UI against a provided mock model and tool server that:
- renders a provided hostile stream with zero script execution and CLS 0;
- stops generation within 200 ms, including server-side cancellation;
- shows tool calls with states;
- blocks every consequential action until the user approves a preview;
- passes a screen-reader script.

You then defend your design against an examiner's prompt-injection attempts.

## Industry reality

The [FE market page](../../../../06_career_and_market_readiness/01_market_map/roles/FE_frontend_engineering.md) names "AI interface engineer" as an emerging specialism and lists AI-native interfaces among the skills growing in value: streaming, partial results, sources, recovery from wrong answers and approval of agent actions. The MCP Apps working group includes members from Anthropic, OpenAI and Google, and Thoughtworks reports host support in Claude, ChatGPT, VS Code and Goose. Google and the MCP Apps creators published patterns for combining A2UI with MCP Apps in June 2026. Browser vendors are standardising agent-facing APIs (WebMCP), and Playwright 1.64 added WebMCP support for testing them.

**Interview questions from this course**

1. *Design the frontend of a chat assistant that streams answers.* A strong answer covers the transport choice (fetch streams or SSE), cancellation end to end, incremental Markdown with sanitisation and Trusted Types, scroll behaviour, CLS, the message-parts model, regenerate and branch, failure states and screen-reader announcements on completion.
2. *How would you show an agent's tool calls and handle risky actions?* A strong answer gives a state per call, a readable plan with progress, interrupt and steer, approval gates for consequential actions with diffs or previews, undo or compensation, and an audit log. It notes that approval must be enforced on the server, not only in the UI.
3. *Model output contains Markdown, HTML and links. How do you render it safely?* A strong answer treats output as untrusted: parse Markdown to a safe tree, sanitise with an allow-list, enforce Trusted Types, apply link and image policies, never use raw `innerHTML`, and test with a hostile corpus.
4. *The model takes 8 seconds. How do you make the feature feel fast?* A strong answer streams early and shows plans and partial results. It uses answer-shaped skeletons, optimistic UI and caching where safe, routes small tasks to faster models and cancels wasted work. It measures time to first token and time to useful output at P75.
5. *How do you know whether an AI feature's UX is working?* A strong answer defines task success and time to useful output, tracks correction, edit and abandonment rates and trust calibration, runs offline evals on recorded sessions and A/B tests, and does a small qualitative study, segmented by device and language.

## Resources (free first)

- **Human–AI interaction:** Amershi et al., [Guidelines for Human-AI Interaction](https://doi.org/10.1145/3290605.3300233) (CHI 2019); [Google PAIR People + AI Guidebook](https://pair.withgoogle.com/guidebook/); [Nielsen Norman Group on AI](https://www.nngroup.com/topic/ai/); Jakob Nielsen, [Response times: the 3 important limits](https://www.nngroup.com/articles/response-times-3-important-limits/).
- **Streaming and safety:** [HTML spec: server-sent events](https://html.spec.whatwg.org/multipage/server-sent-events.html); [MDN Streams API](https://developer.mozilla.org/en-US/docs/Web/API/Streams_API); [MDN using SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events); [OWASP XSS prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html).
- **Protocols and libraries:** [MCP Apps overview](https://modelcontextprotocol.io/extensions/apps/overview) and [working group](https://modelcontextprotocol.io/community/working-groups/apps); [A2UI](https://a2ui.org/); [AG-UI](https://ag-ui.com/); [WebMCP draft](https://webmachinelearning.github.io/webmcp/); [AI SDK chatbot guide](https://ai-sdk.dev/docs/ai-sdk-ui/chatbot).
- **On-device AI:** [Chrome built-in AI](https://developer.chrome.com/docs/ai/built-in) and [API status](https://developer.chrome.com/docs/ai/built-in-apis); [Transformers.js](https://huggingface.co/docs/transformers.js/index); [WebLLM](https://webllm.mlc.ai/); [ONNX Runtime Web](https://onnxruntime.ai/docs/tutorials/web/); [WebNN](https://www.w3.org/TR/webnn/).
- **Multimodal and Indic:** [MDN Web Speech API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API); [Bhashini](https://bhashini.gov.in/).

## Sources

All checked 12 Oct 2026.

- Stack Overflow, 2026 Developer Survey, AI section — https://survey.stackoverflow.co/2026/ai/data
- Leviathan et al., "Generative UI: LLMs are Effective UI Generators" (arXiv 2604.09577, 24 Feb 2026) — https://arxiv.org/abs/2604.09577
- Peng et al., "EvoGenUI-Bench: Evaluating LLMs as Multi-Turn Generative UI Assistants" (arXiv 2608.29387, Aug 2026; EMNLP 2026) — https://arxiv.org/abs/2608.29387
- Model Context Protocol, MCP Apps Working Group charter (SEP-1865 proposed 21 Nov 2025; stable spec 26 Jan 2026) — https://modelcontextprotocol.io/community/working-groups/apps
- Thoughtworks Technology Radar, MCP Apps (host support) — https://www.thoughtworks.com/radar/platforms/mcp-apps
- Google Developers Blog, "A2UI + MCP Apps" (17 Jun 2026) — https://developers.googleblog.com/en/a2ui-and-mcp-apps/
- Web Machine Learning Community Group, WebMCP Draft Community Group Report (9 Oct 2026) — https://webmachinelearning.github.io/webmcp/
- Chrome for Developers, built-in AI API status and requirements — https://developer.chrome.com/docs/ai/built-in-apis · https://developer.chrome.com/docs/ai/get-started
- W3C, Web Neural Network API, Candidate Recommendation Draft (10 Oct 2026) — https://www.w3.org/TR/webnn/
- Hugging Face, Transformers.js documentation (WebGPU and dtypes) — https://huggingface.co/docs/transformers.js/index
- web-features 3.42.0 (WebTransport Baseline Mar 2026; Trusted Types Feb 2026) — https://web-platform-dx.github.io/web-features/
- Playwright release notes (1.64 WebMCP support) — https://playwright.dev/docs/release-notes
- StatCounter, India mobile OS share, Sep 2026 — https://gs.statcounter.com/os-market-share/mobile/india

_Last reviewed: 2026-10_
