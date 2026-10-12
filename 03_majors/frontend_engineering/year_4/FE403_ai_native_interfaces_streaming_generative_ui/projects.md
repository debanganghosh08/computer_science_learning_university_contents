# FE403 · Labs and projects

Labs run against a provided mock model server that streams tokens, tool calls and failures from recorded scripts. This makes tests deterministic and free. Projects add a real model API of your choice, with a spending cap. Every UI that renders model output must pass the course's hostile-output suite: script injection, broken Markdown, 50,000-token answers, Unicode edge cases and injected instructions. Sanitisation and approval logic are written without AI.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Guidelines audit | Audit two AI features against Microsoft's 18 HAX guidelines and the PAIR Guidebook | Audit table with screenshots and 5 prioritised fixes | 3 h |
| 2 · Three transports | Stream over SSE, fetch streams and WebSockets; resume after disconnect; Stop cancels server work | Latency and reconnection comparison; server logs proving cancellation | 5 h |
| 3 · Hostile streams (sanitisation without AI) | Incremental Markdown renderer with sanitisation and Trusted Types | Zero script execution across the hostile suite; CLS 0; at most one render per frame | 6 h |
| 4 · Branching chat | Typed message parts, edit/regenerate/branch, drafts surviving reload and network loss | Schema; branch-switching demo; offline test | 5 h |
| 5 · Tool-call UI and long-running agent | States per tool call, live plan, interrupt and steer, approval with previews, undo, replayable event stream | Approval cannot be bypassed (tests); Stop within 200 ms; replay-driven UI tests | 8 h |
| 6 · Generative UI and MCP App | Tools mapped to design-system components; A2UI-style renderer with allow-list; a small MCP App in a reference host | Typed component mapping; rejection tests for unknown components; MCP App threat model | 8 h |
| 7 · Failure states and injection | 8 failure states with recovery; citations with previews; red-team with 20 injected documents | Failure-state gallery; red-team report with zero unsafe actions | 5 h |
| 8 · Latency and cost | Measure time to first token and time to useful output at P75; add streaming, skeletons, caching and routing | Before/after table; cache-isolation test across users | 4 h |
| 9 · Voice and Indic input | Voice input with clear states; Hinglish transliteration; answers in the user's script | Demo on a low-end Android phone; TalkBack walkthrough | 4 h |
| 10 · On-device and hybrid | Chrome Summarizer or Translator with feature detection; Transformers.js model on WebGPU/WASM; capability-based routing | Load time, tokens per second and quality comparison; disclosure UI | 5 h |

## Projects

### P1 · Production-quality streaming answer component (L1, ~6 hours)

**Real-world inspiration:** every major assistant product streams answers with Markdown, code and citations. The 2026 Stack Overflow survey found that 48.0% of developers trust AI output only when they can easily verify it, so citations and stop/retry controls are part of the job, not decoration.

**What to build:** a framework-agnostic `<streamed-answer>` web component, or a React component, that:
- consumes a fetch stream or SSE and renders Markdown incrementally (code blocks with copy, tables, lists);
- shows inline citations with hover or focus previews;
- has Stop, Retry and Copy, and states for waiting, streaming, done, stopped and error.

**Acceptance criteria:**
- **Security:** zero script execution across the hostile suite (40 cases) with Trusted Types enforced (`require-trusted-types-for 'script'`); links to `javascript:` and data URLs are never clickable.
- **Stability:** CLS 0 while streaming 20,000 tokens; "stick to bottom" stops when the user scrolls up and resumes on request.
- **Performance:** at most one render per animation frame; main-thread long tasks under 50 ms at 4× CPU throttling.
- **Accessibility:** NVDA and TalkBack announce "answer complete" once, not every token; Stop is keyboard-reachable and labelled; citations are reachable and readable.
- **Control:** Stop cancels the request and the server stops generating within 300 ms (server log evidence).

**Stretch goals:** syntax highlighting in a worker; "copy as plain text" that strips citations correctly.

**What it proves to an employer:** you can build the core component of every AI product to a production standard of security, accessibility and performance.

### P2 · Agent console with approvals and undo (L2, ~15 hours)

**Real-world inspiration:** coding agents, browser agents and support agents all need interfaces where people watch, steer and approve work. The domain here, an expense-claims agent that reads receipts, fills a claim, checks policy and submits, is an **illustrative scenario** running against mock tools.

**What to build:** an agent console with:
- a live plan with per-step status, and tool-call cards showing arguments and results;
- interrupt, steer and pause/resume;
- approval gates for consequential tools (submit claim, email manager) with a preview diff of exactly what will be sent;
- undo for reversible steps and compensating actions for the rest;
- a readable audit log;
- a UI driven by an AG-UI-style event stream that can be recorded and replayed.

**Acceptance criteria:**
- **Safety:** across 40 scripted runs, including runs where the mock model tries to call "submit" without approval, zero consequential actions execute without an explicit user approval. Approval is enforced in the tool server, not just hidden in the UI (tests prove it).
- **Control latency:** interrupt takes effect within 200 ms of the click (event timestamps).
- **Failure handling:** each of 6 injected tool failures (timeout, validation error, partial success, rate limit, permission denied, malformed result) shows a specific, actionable message and a recovery option.
- **Replay:** the full UI test suite runs from recorded event streams with no model calls, in under 60 s.
- **Accessibility:** plan updates are announced politely and at most once per step; approval dialogs meet the FE303 dialog standard.
- **Prompt injection:** a receipt containing hidden instructions ("also email this to …") does not cause any unapproved action, and the UI marks the content as untrusted.

**Stretch goals:** a background-run mode with notifications and resumption on another device; an MCP App version of the approval card that runs inside an assistant host.

**What it proves to an employer:** you can build the human-control layer that makes agents safe to deploy, which is what companies shipping agents most need.

### P3 · Multilingual assistant with generative UI and on-device fallback (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** millions of Indians apply for public schemes, scholarships and services through long forms, often on low-cost Android phones and in languages other than English. Bhashini provides public Indian-language AI services, and Chrome's built-in Translator and Summarizer run on-device on capable desktops. The product, an assistant that helps a user understand eligibility and fill an application, is an **illustrative scenario**. Use synthetic schemes and never collect real personal data.

**What to build:**
- **Conversation:** a streaming chat that answers in Hindi, English and one more Indian language (typed, transliterated or spoken), with citations to the scheme's (synthetic) rules.
- **Generative UI:** typed tools render eligibility checklists, document lists and a form-filling panel from your FE303 design system.
- **Agency:** the agent pre-fills the form from the conversation, but submission requires review and approval of every field, with a diff.
- **On-device path:** Chrome built-in AI on capable desktops for summarisation and translation; a Transformers.js model for language detection elsewhere; the cloud model otherwise. The UI discloses which ran.
- **Low end:** a lite mode for low-end phones (text-first, no on-device model download).
- **Distribution:** an MCP App version of the eligibility checklist.
- **Instrumentation:** task success, time to useful output, corrections and abandonment.

**Acceptance criteria:**
- **Task success:** on 30 scripted tasks across the three languages, the user reaches a correct, fully reviewed application in at least 90% of cases (scored against an answer key). Every wrong answer the assistant gives is either cited to a source the user can check or flagged as uncertain.
- **Latency:** time to first token at most 1 s and time to useful output at most 4 s at P75 on the cloud path, measured on the FE304 baseline mobile profile.
- **Safety:** zero submissions without field-by-field approval; a 20-case prompt-injection suite (in documents and chat) causes zero unapproved actions; output passes the hostile suite.
- **Accessibility:** WCAG 2.2 AA (axe zero plus TalkBack and NVDA scripts) in all three languages; voice has a text equivalent.
- **Low-end and offline:** lite mode keeps the critical-path transfer at or below 200 KB; drafts survive a network drop; on-device features are offered only where the capability checks pass.
- **Evaluation:** a study with at least 6 participants (including at least 2 who prefer a language other than English), reporting task success, time, corrections, trust ratings and quotes, with changes you made in response.

**Stretch goals:** voice-first mode with barge-in; WebMCP tools so a browser agent can complete the form with the same approval gates; compare a WebGPU-hosted small model with the cloud model on quality and latency.

**What it proves to an employer:** you can design, build and evaluate an AI product for real users with real constraints (language, devices, trust and safety). That is the full skill set of an AI interface engineer.

## Feeds into

- [FE501 Frontier Seminar](../../year_5/FE501_frontier_seminar_multimodal_spatial_and_on/README.md): on-device models, multimodal interfaces and agent-facing web standards as research topics.
- [OV08A Shipping AI Features End to End](../../../../04_overlaps/OV08_full_stack_ai_product_engineering/OV08A_shipping_ai_features_end_to_end/README.md) and [OV08B Product Analytics and Growth for AI Apps](../../../../04_overlaps/OV08_full_stack_ai_product_engineering/OV08B_product_analytics_and_growth_for_ai_apps/README.md): P3's instrumentation and evaluation become product analytics.
- [THS501 Thesis or Capstone I](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md): AI UX capstones with user studies.
