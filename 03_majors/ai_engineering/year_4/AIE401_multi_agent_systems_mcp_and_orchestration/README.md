# AIE401 · Multi-Agent Systems, MCP and Orchestration

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 7 | 4 (≈ 120 hours) | L2 → L4 | [AIE301](../../year_3/AIE301_llm_fundamentals_for_engineers/README.md); assumes [AIE304](../../year_3/AIE304_tool_use_and_ai_agents_loops_harnesses_memory/README.md) and [AIE305](../../year_3/AIE305_evaluating_llm_systems/README.md) | [AIE501](../../year_5/AIE501_frontier_seminar_long_horizon_autonomous_agents/README.md), [OV12 Agent Infrastructure and Platform Engineering](../../../../04_overlaps/OV12_agent_infrastructure_platform/), [OPS403](../../../devops_sre_platform_engineering/year_4/OPS403_aiops_and_agentic_operations/README.md) |

## Why this course matters now

Agents are only as useful as the systems they can reach, and connecting every model to every tool by hand does not scale. The Model Context Protocol (MCP) was introduced by Anthropic in November 2024. OpenAI adopted it in March 2025, and in December 2025 it was donated to the Linux Foundation's new Agentic AI Foundation alongside Block's goose and OpenAI's AGENTS.md. Its current specification (2026-07-28) made requests stateless, deprecated roots, sampling and logging, and moved long-running Tasks into an extension. Agent-to-agent communication has its own standard: the A2A protocol reached v1.0 in March 2026 and joined the same foundation in August 2026. Multi-agent designs can be powerful and expensive. Anthropic reported that its multi-agent research system beat a single agent by 90.2% on an internal evaluation while using about 15× the tokens of a chat (June 2025). Cognition's "Don't Build Multi-Agents" (June 2025) argues that agents which do not share full context make conflicting decisions. Coding assistants can generate an MCP server in minutes. The engineering judgement is about the rest: where agent boundaries go, how authorization flows across hops, how to stop a confused-deputy attack, and when one well-tooled agent beats five.

## Learning outcomes

By the end you can:

1. **Explain** MCP's architecture (hosts, clients, servers, JSON-RPC 2.0) and the 2026-07-28 changes, and **migrate** a server from the 2025-11-25 revision.
2. **Build** production MCP servers exposing tools, resources and prompts over stdio and Streamable HTTP, with tests and the MCP Inspector.
3. **Implement** MCP authorization correctly (OAuth 2.1, RFC 9728 protected resource metadata, RFC 8707 resource indicators, client ID metadata documents) and **explain** why token passthrough is forbidden.
4. **Threat-model** an MCP and multi-agent deployment (confused deputy, tool-description poisoning, SSRF, supply chain, excessive agency) and **apply** defensive controls.
5. **Use** A2A Agent Cards, tasks and artifacts to connect agents across organisations, and **position** A2A, MCP, AG-UI and agentic-commerce protocols correctly.
6. **Implement** orchestrator–worker, handoff, agents-as-tools, parallel fan-out and evaluator patterns, with durable state.
7. **Decide**, with token-cost and failure-mode evidence, when not to use multiple agents.
8. **Trace and evaluate** multi-agent runs end to end, attributing failures and costs to individual agents.

## Chapters and lessons

### Chapter 1 · Why protocols (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 The N × M problem | Every app × every tool integration; function calling inside one app vs a protocol across apps; the Language Server Protocol as MCP's stated inspiration | Count the integrations needed for 5 assistants × 12 internal systems with and without a protocol |
| 1.2 MCP architecture | Hosts (LLM applications), clients (connectors inside the host), servers (context and capabilities); JSON-RPC 2.0 messages | Capture and annotate the raw JSON-RPC traffic of one MCP session |
| 1.3 Governance and ecosystem | Anthropic launch (Nov 2024), OpenAI adoption (Mar 2025), Agentic AI Foundation (Dec 2025); official registry (preview since Sept 2025); SDKs | Write a one-page history with dates and what each step changed for builders |
| 1.4 Reading a spec | Normative language (BCP 14 MUST/SHOULD), schema-as-source-of-truth (`schema.ts`), changelogs | Find five MUST requirements a server you use violates or meets |

**Check your understanding:** What problem does MCP solve that function calling alone does not? Why does protocol governance under a neutral foundation matter to an enterprise buyer? Why read the changelog before the tutorial?

### Chapter 2 · Server features: tools, resources, prompts (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Tools | Input schemas, structured output, annotations (untrusted unless from a trusted server), error reporting, progress and cancellation | Wrap a ticketing API as three MCP tools with typed schemas |
| 2.2 Resources | URIs, read vs subscribe, binary vs text, when to expose data as resources rather than tools | Expose a document store as resources with URI templates |
| 2.3 Prompts | User-invoked templated workflows; arguments; discoverability | Add two prompt templates for common support workflows |
| 2.4 Client features and extensions | Elicitation (server asks the user for input); Tasks extension for long-running operations; MCP Apps for inline UI; Skills over MCP | Implement elicitation for a missing parameter; implement one long-running task with polling |

**Check your understanding:** When should a capability be a resource rather than a tool? Why does the spec treat tool annotations as untrusted? What problem does the Tasks extension solve that a long tool call cannot?

### Chapter 3 · Transports, statelessness and versions (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 stdio vs Streamable HTTP | Local subprocess servers vs remote servers; HTTP+SSE deprecated since 2025-03-26 | Run the same server over both transports; compare latency and failure modes |
| 3.2 The 2026-07-28 model | Stateless, self-contained requests; no `initialize` handshake or session IDs; `server/discover`; multi round-trip requests replacing server-initiated requests | Migrate a 2025-11-25 server; write the migration notes |
| 3.3 Deprecations | Roots, sampling and logging deprecated (eligible for removal on or after 2027-07-28); dynamic client registration deprecated | Audit an open-source server for deprecated features; propose replacements |
| 3.4 Scaling remote servers | Stateless horizontal scaling, load balancers, timeouts, retries, rate limits, observability | Deploy two replicas behind a load balancer; kill one mid-request |

**Check your understanding:** What does statelessness make easier for operators, and what did it make harder for server authors? Why would a protocol deprecate a feature like sampling? How do you support clients on two spec versions at once?

### Chapter 4 · Authorization and MCP security (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 OAuth 2.1 for MCP | Servers as protected resources (RFC 9728 metadata), resource indicators (RFC 8707), authorization server discovery (RFC 8414), client ID metadata documents | Add OAuth to your HTTP server using an open-source authorization server; pass the spec checklist |
| 4.2 Confused deputy and token passthrough | Why a server must not forward client tokens to upstream APIs; audience validation; per-user consent | Draw the token flow of a server that calls GitHub on behalf of users; fix the passthrough |
| 4.3 Supply chain and tool poisoning | Untrusted servers, malicious or changed tool descriptions, typosquatted packages, pinning and allow-lists, registry trust | Write an allow-list and pinning policy for an organisation's MCP servers |
| 4.4 Local server risks and SSRF | Local servers with filesystem access, server-side request forgery from URL-fetching tools, scope minimisation (MCP Security Best Practices) | Threat-model a "fetch URL" tool; add egress controls and test them in a sandbox |
| 4.5 Excessive agency | OWASP LLM06; least privilege per tool; human consent before invocation, as the spec requires of hosts | Classify 15 tools by blast radius; set approval rules |

**Check your understanding:** Why is a valid token for the wrong audience a vulnerability? What can a malicious tool description do even if the tool is never called? Which single control would you add first to a company rolling out 40 community MCP servers?

### Chapter 5 · Building and shipping MCP servers (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 SDKs | Official Python and TypeScript SDKs; typed handlers; schema generation | Build a server for a mock railway-booking API (search trains, hold seat, cancel) |
| 5.2 Tool design for agents | Applying AIE304 tool design: fewer, richer tools; actionable errors; bounded outputs | A/B two tool designs with an agent on 30 tasks |
| 5.3 Testing | MCP Inspector, contract tests against the schema, fuzzing inputs, golden transcripts | Write a test suite that runs in CI against the server |
| 5.4 Shipping | Packaging, versioning, changelogs, registry metadata, deprecation of tools | Publish to a private registry; deprecate one tool without breaking clients |

**Check your understanding:** What makes an MCP server "agent-friendly" beyond being spec-compliant? How do you change a tool's schema without breaking existing clients? What belongs in a server's README for a security reviewer?

### Chapter 6 · Clients and hosts at scale (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Writing a client | Discovery, capability checks, tool invocation, consent prompts | Add an MCP client to your AIE304 agent |
| 6.2 Too many tools | Context cost of hundreds of tool definitions; namespacing; tool search and dynamic loading | Connect 8 servers; measure tokens spent on tool definitions; add tool search |
| 6.3 Consent UX | Showing what a tool will do, batching approvals, remembering decisions safely | Design and test an approval UI with five users |
| 6.4 Gateways | Central MCP gateways for auth, logging, rate limits and policy | Put a gateway in front of three servers; enforce a per-user policy |

**Check your understanding:** Why do tool definitions become a cost and accuracy problem as servers multiply? What should a host log for every tool call? Where should policy live: in the server, the host or a gateway?

### Chapter 7 · Agent-to-agent and adjacent protocols (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 A2A | Agent Cards at `/.well-known/agent-card.json`; tasks, messages and artifacts; JSON-RPC, gRPC and HTTP+JSON bindings; v1.0 (Mar 2026); IBM's ACP merged into A2A (2025) | Expose your agent over A2A; call it from a second agent in another process |
| 7.2 MCP vs A2A | Tools and context for one agent vs collaboration between opaque agents; when each fits | Write a decision table for five integration scenarios |
| 7.3 Agent–UI | AG-UI event streams between agents and front ends | Stream an agent's progress events to a web UI |
| 7.4 Agentic commerce | Google's Agent Payments Protocol (AP2, Sept 2025), the Agentic Commerce Protocol (OpenAI and Stripe, Sept 2025), the UPI agentic payments pilot (Razorpay, NPCI, OpenAI, Oct 2025) | Compare how each represents user intent and authorisation |

**Check your understanding:** Why does A2A treat remote agents as opaque? What must be true before an agent can spend a user's money? Which protocol would you use to let a partner company's agent book appointments in your system?

### Chapter 8 · Orchestration patterns (weeks 8–9)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Orchestrator–worker | A lead agent plans and spawns workers with clear tasks, output formats and budgets; synthesis (Anthropic, June 2025) | Build a research orchestrator with 3 parallel workers |
| 8.2 Handoffs and agents-as-tools | Transferring control vs calling a sub-agent and getting a result back (OpenAI Agents SDK) | Implement a triage → specialist handoff for a bank-support scenario |
| 8.3 Graph orchestration | Explicit state graphs, conditional edges, checkpoints (LangGraph); durable orchestration (Temporal) | Rebuild 8.1 as a graph with checkpoints; resume after a crash |
| 8.4 Debate and ensembles | Multi-agent debate (Du et al., 2023), mixture-of-agents (Wang et al., 2024), evaluator–optimiser loops; their costs | Measure accuracy and cost of debate vs self-consistency on 100 questions |
| 8.5 Sharing context | Full traces vs summaries; conflicting implicit decisions (Cognition, 2025); shared state stores | Show a failure caused by summary-only handoff; fix it by sharing the decision log |

**Check your understanding:** What must a lead agent tell a worker so that the worker does not duplicate or contradict others? When is a handoff better than an agent-as-tool call? Why can debate cost three times more without being more accurate?

### Chapter 9 · When not to use multiple agents (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Token economics | Agents use about 4× the tokens of chat and multi-agent systems about 15× (Anthropic, 2025); token usage explained 80% of performance variance on BrowseComp in their analysis | Cost your 8.1 system per task; find the break-even value per answer |
| 9.2 Failure taxonomy | Multi-agent failures cluster in specification, inter-agent misalignment and verification (Cemri et al., "Why Do Multi-Agent LLM Systems Fail?", 2025) | Label 40 failed runs with the taxonomy |
| 9.3 Good fits and bad fits | Breadth-first, parallelisable, read-heavy tasks vs tightly coupled tasks such as most coding | Argue for and against multi-agent for three real products |
| 9.4 The single-agent baseline | One agent with good tools, compaction and sub-agents for isolated reads | Beat or match your multi-agent system with a single agent; report both |

**Check your understanding:** Why are writes harder to parallelise across agents than reads? What would you need to see before approving a 15× token budget? What is the cheapest experiment that tells you whether multi-agent helps your task?

### Chapter 10 · Observability and evaluation of multi-agent runs (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Distributed traces | OpenTelemetry GenAI agent spans (`invoke_agent`, `execute_tool`; status: development); trace context across MCP and A2A hops | Propagate trace context through orchestrator, workers and MCP servers |
| 10.2 Attribution | Which agent caused the failure; per-agent cost and latency; critical path | Build a per-agent cost and latency breakdown dashboard |
| 10.3 Evaluating coordination | Handoff accuracy, duplicated work, contradiction rate, end-state checks | Add three coordination metrics to your eval suite |
| 10.4 Replay and debugging | Replaying multi-agent runs from traces and checkpoints; comparing two runs step by step to find where they diverge | Replay a failed run with one worker's model swapped; locate the first divergent decision |

**Check your understanding:** Why are logs per agent insufficient? How do you tell a bad plan from a bad worker? What is the multi-agent equivalent of a flaky test?

### Chapter 11 · Enterprise integration and governance (weeks 12–13)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Identity for agents | Service identities, on-behalf-of flows, scoped and short-lived credentials, audit trails | Design identity for an agent acting for 5,000 employees |
| 11.2 Policy and approvals | Central policy, allow-listed servers, data-classification rules, approvals by risk tier | Write a policy file and enforce it at the gateway |
| 11.3 Agentic risk frameworks | OWASP Top 10 for Agentic Applications (Dec 2025), NIST AI 600-1, India's AI Governance Guidelines (Nov 2025) | Map your P3 system's controls to the OWASP agentic list |
| 11.4 Operating the fleet | Versioning servers and agents, deprecation, incident response for agent misbehaviour | Write the runbook for "an MCP server is returning malicious tool descriptions" |

**Check your understanding:** Why should an agent never reuse a human's long-lived token? Which governance control most reduces blast radius? What evidence would an auditor ask for after an agent incident?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · JSON-RPC traffic capture | — |
| 2 | 2 | Lab 1 (cont.): First MCP server (tools, resources, prompts) | — |
| 3 | 3 | Lab 2 · Transport and 2026-07-28 migration | **P1 due** |
| 4 | 4 | Lab 3 · OAuth for MCP and token-flow review | Threat model |
| 5 | 5 | Lab 4 · Server testing and registry publishing | — |
| 6 | 6 | Lab 5 · Client with tool search and consent UX | Mid-term (AI off): spec and auth reasoning |
| 7 | 7 | Lab 6 · A2A between two agents | — |
| 8 | 8 | Lab 7 · Orchestrator–worker and handoffs | — |
| 9 | 8 | Lab 7 (cont.): durable graph orchestration | **P2 due** |
| 10 | 9 | Lab 8 · Single agent vs multi-agent shoot-out | Cost–quality report |
| 11 | 10 | Lab 9 · Distributed tracing across hops | — |
| 12 | 11 | Lab 10 · Identity, policy and gateway | — |
| 13 | 11 | Lab 10 (cont.): incident runbook drill | Runbook |
| 14 | Integration | P3 demo day | **P3 due** |
| 15 | Review | Oral defence of P3 | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** generating server boilerplate from an OpenAPI spec; writing contract tests; explaining spec sections; simulating client behaviours; drafting orchestration prompts for lead and worker agents.
- **Do without AI (drills):** draw the OAuth token flow for an MCP server calling an upstream API, labelling every audience; read a changelog and list breaking changes; design agent boundaries for a scenario on a whiteboard; estimate token cost of a multi-agent design before building it.
- **Verify AI output by:** running the MCP Inspector and your contract tests against the current spec version; checking generated auth code against the authorization spec's MUST list; load-testing statelessness claims by killing replicas; comparing every multi-agent design against a single-agent baseline on the same eval.
- **Where AI still fails here (show it):** assistants trained before 2026 generate session-based MCP servers with `initialize` handshakes and HTTP+SSE transport (log every instance you catch); generated servers often pass client tokens straight through to upstream APIs (find it in a code review); models propose multi-agent architectures for tasks that a single agent handles more cheaply (show it in Lab 8).

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1–P3 | 35% |
| Threat model + runbook | 10% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) + oral defence of P3 | 20% |

**Mastery gate.** You pass when you can: (1) build and deploy a remote, OAuth-protected MCP server that passes your contract tests and the MCP Inspector on the current spec in one working day; (2) review an unfamiliar MCP server and find its authorization and supply-chain weaknesses with a written fix for each; (3) given a product scenario, present a single-agent and a multi-agent design with measured cost per success and failure modes, and defend which one ships.

## Industry reality

MCP is supported across the major model providers and developer tools, and its governance moved to the Linux Foundation's Agentic AI Foundation in December 2025, whose founding projects were MCP, goose and AGENTS.md. A2A has been a Linux Foundation project since June 2025 and joined the same foundation in August 2026. Production multi-agent systems are real but selective. Anthropic's Research feature uses an orchestrator–worker design and documents the token cost openly, while Cognition argues for single-threaded agents with shared context in coding. Payments are the frontier where protocol design meets regulation: AP2, the Agentic Commerce Protocol, and in India the UPI agentic payments pilot with Razorpay, NPCI and OpenAI (Oct 2025) all deal with how an agent proves it acts on a user's authority.

**Interview questions from this course**

1. *Design an MCP server that lets an assistant act on users' GitHub repositories.* Strong answer: remote server with OAuth 2.1; protected-resource metadata; tokens issued for the server's audience, never passed through; per-user scopes; tool design with bounded outputs; consent for writes; audit logs; rate limits; contract tests.
2. *What changed in MCP's 2026-07-28 revision and how would you migrate?* Strong answer: stateless requests without initialize or session IDs, `server/discover`, multi round-trip requests, deprecated roots/sampling/logging, Tasks as an extension, dynamic client registration deprecated; supports both versions during migration with tests.
3. *MCP or A2A for connecting to a partner's booking system?* Strong answer: MCP if you consume their capabilities as tools within your agent; A2A if their agent remains autonomous and opaque and negotiates tasks; covers auth, trust boundaries and failure handling either way.
4. *Should our research assistant be multi-agent?* Strong answer: depends on parallelisable breadth; cites token multipliers and failure taxonomies; proposes a single-agent baseline and a measured comparison of cost per success; designs worker briefs and shared context if multi-agent wins.
5. *An MCP server your company uses starts returning altered tool descriptions. What do you do?* Strong answer: incident response: disable via gateway, pin to known-good version, review logs for tool calls influenced, rotate credentials, notify users, add description-change detection and pinning to policy.

## Resources (free first)

- **MCP:** Specification 2026-07-28 — https://modelcontextprotocol.io/specification/2026-07-28 ; changelog — https://modelcontextprotocol.io/specification/2026-07-28/changelog ; transports — https://modelcontextprotocol.io/specification/2026-07-28/basic/transports ; authorization — https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization ; security best practices — https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices ; Tasks extension — https://modelcontextprotocol.io/extensions/tasks/overview ; MCP Apps — https://modelcontextprotocol.io/extensions/apps/overview ; Python SDK — https://github.com/modelcontextprotocol/python-sdk ; TypeScript SDK — https://github.com/modelcontextprotocol/typescript-sdk ; Inspector — https://github.com/modelcontextprotocol/inspector ; Registry — https://registry.modelcontextprotocol.io/ ; Hugging Face MCP Course — https://huggingface.co/learn/mcp-course
- **Standards:** JSON-RPC 2.0 — https://www.jsonrpc.org/specification ; OAuth 2.1 draft — https://datatracker.ietf.org/doc/html/draft-ietf-oauth-v2-1-13 ; RFC 9728 — https://datatracker.ietf.org/doc/html/rfc9728 ; RFC 8707 — https://datatracker.ietf.org/doc/html/rfc8707 ; Language Server Protocol — https://microsoft.github.io/language-server-protocol/
- **A2A and adjacent:** A2A specification — https://a2a-protocol.org/latest/specification/ ; A2A releases — https://github.com/a2aproject/A2A/releases ; AG-UI — https://docs.ag-ui.com/introduction ; AP2 — https://cloud.google.com/blog/products/ai-machine-learning/announcing-agents-to-payments-ap2-protocol ; Agentic Commerce Protocol — https://www.agenticcommerce.dev/ ; AGENTS.md — https://agents.md/
- **Orchestration:** Anthropic, "How we built our multi-agent research system" — https://www.anthropic.com/engineering/multi-agent-research-system ; Cognition, "Don't Build Multi-Agents" — https://cognition.com/blog/dont-build-multi-agents ; OpenAI Agents SDK handoffs — https://openai.github.io/openai-agents-python/handoffs/ ; LangChain multi-agent docs — https://docs.langchain.com/oss/python/langchain/multi-agent ; Temporal + Agents SDK — https://temporal.io/blog/announcing-openai-agents-sdk-integration
- **Security and governance:** OWASP Top 10 for Agentic Applications — https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/ ; OWASP LLM Top 10 2025 — https://genai.owasp.org/llm-top-10/ ; NIST AI 600-1 — https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf

## Sources

- Anthropic, "Introducing the Model Context Protocol" (25 Nov 2024) — https://www.anthropic.com/news/model-context-protocol ; TechCrunch, "OpenAI adopts rival Anthropic's standard…" (26 Mar 2025) — https://techcrunch.com/2025/03/26/openai-adopts-rival-anthropics-standard-for-connecting-ai-models-to-data/ (checked 2026-10)
- Anthropic, "Donating the Model Context Protocol and establishing the Agentic AI Foundation" (9 Dec 2025) — https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation (checked 2026-10)
- MCP Specification 2026-07-28 and changelog (stateless requests, `server/discover`, deprecations, extensions; LSP inspiration; security principles) — https://modelcontextprotocol.io/specification/2026-07-28 (checked 2026-10)
- MCP Registry preview (8 Sept 2025) — https://blog.modelcontextprotocol.io/posts/2025-09-08-mcp-registry-preview/ (checked 2026-10)
- Linux Foundation, A2A project launch (23 Jun 2025) — https://www.linuxfoundation.org/press/linux-foundation-launches-the-agent2agent-protocol-project-to-enable-secure-intelligent-communication-between-ai-agents ; A2A releases (v1.0.0 Mar 2026, v1.0.1 May 2026) — https://github.com/a2aproject/A2A/releases ; "A2A joins AAIF" (Aug 2026) — https://aaif.io/blog/a2a-joins-aaif ; IBM, ACP now part of A2A — https://research.ibm.com/projects/agent-communication-protocol (checked 2026-10)
- Anthropic, "How we built our multi-agent research system" (13 Jun 2025): +90.2%, ~4× and ~15× tokens, 80% of variance — https://www.anthropic.com/engineering/multi-agent-research-system (checked 2026-10)
- Cognition, "Don't Build Multi-Agents" (12 Jun 2025) — https://cognition.com/blog/dont-build-multi-agents (checked 2026-10)
- Cemri et al., "Why Do Multi-Agent LLM Systems Fail?" (2025) — https://arxiv.org/abs/2503.13657 ; Du et al., multi-agent debate (2023) — https://arxiv.org/abs/2305.14325 ; Wang et al., Mixture-of-Agents (2024) — https://arxiv.org/abs/2406.04692 (checked 2026-10)
- Google Cloud, AP2 (17 Sept 2025) — https://cloud.google.com/blog/products/ai-machine-learning/announcing-agents-to-payments-ap2-protocol ; Stripe, Instant Checkout and the Agentic Commerce Protocol (29 Sept 2025) — https://stripe.com/newsroom/news/stripe-openai-instant-checkout ; Razorpay, agentic payments with NPCI and OpenAI (Oct 2025) — https://razorpay.com/newsroom/razorpay-npci-and-openai-come-together-to-launch-agentic-payments-ushering-in-ai-driven-commerce-at-national-scale/ (checked 2026-10)
- OWASP Top 10 for Agentic Applications (published 9 Dec 2025) — https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/ (checked 2026-10)
- OpenTelemetry GenAI agent spans (development status) — https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-agent-spans.md (checked 2026-10)

_Last reviewed: 2026-10_
