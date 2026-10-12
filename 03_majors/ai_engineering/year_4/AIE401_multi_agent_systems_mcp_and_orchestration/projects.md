# AIE401 · Labs and projects

Every lab and project targets the current MCP specification (2026-07-28 at the time of writing; check the changelog before you start) and ships contract tests, MCP Inspector screenshots or logs, distributed traces, and a threat model. Multi-agent work always includes a single-agent baseline measured on the same tasks.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · JSON-RPC capture and first MCP server | Capture and annotate the raw traffic of an existing MCP session; then wrap a ticketing API as tools, resources and prompts | Annotated capture; server code with typed schemas | 6 h |
| 2 · Transports and spec migration | Run one server over stdio and Streamable HTTP; migrate a 2025-11-25 server to 2026-07-28 (stateless requests, `server/discover`, deprecations) | Latency and failure comparison; migration notes | 5 h |
| 3 · OAuth for MCP and token-flow review | Protect the HTTP server with OAuth 2.1, protected-resource metadata (RFC 9728) and resource indicators (RFC 8707); review a server that calls an upstream API for token passthrough | Spec checklist; token-flow diagram with audiences; fix for the passthrough | 6 h |
| 4 · Server testing and registry publishing | Contract tests against the schema, input fuzzing, golden transcripts; publish to a private registry; deprecate a tool safely | CI test suite; registry entry; deprecation plan | 4 h |
| 5 · Client with tool search and consent UX | Add an MCP client to your AIE304 agent; connect 8 servers; measure tool-definition tokens; add tool search; prototype approvals | Token measurements before/after; consent UI test with 5 users | 5 h |
| 6 · A2A between two agents | Publish an Agent Card and expose your agent over A2A; call it from another agent in a separate process; stream progress over AG-UI | Working demo, message logs, decision table MCP vs A2A | 5 h |
| 7 · Orchestrator–worker, handoffs and durable graphs | Build a research orchestrator with 3 parallel workers; implement a triage → specialist handoff; rebuild as a checkpointed graph and resume after a kill | Code, traces, resume test log | 7 h |
| 8 · Single agent vs multi-agent shoot-out | Run both designs on 30 tasks; label failures with the MAST taxonomy | Success, cost per success, latency; failure labels; recommendation | 5 h |
| 9 · Distributed tracing across hops | Propagate trace context through orchestrator, workers, MCP servers and an A2A call using OpenTelemetry GenAI spans | Dashboard of per-agent cost and latency; one failure attributed end to end | 4 h |
| 10 · Identity, policy, gateway and incident drill | Design on-behalf-of identity for 5,000 users; enforce a policy file at a gateway; rehearse "a server returns altered tool descriptions" | Identity design, policy tests, runbook and drill log | 6 h |

## Projects

### P1 · An MCP server for Indian public data (L1, ~6 hours)

**Real-world inspiration.** MCP standardises how AI applications reach tools and data, much as the Language Server Protocol standardised editor support for programming languages. India's Open Government Data platform publishes thousands of datasets that assistants could use if they were reachable through a standard interface.

**What to build.** An MCP server, built with an official SDK, that exposes a curated set of data.gov.in datasets (for example crop prices, rainfall or railway statistics): tools for search and filtered queries with bounded outputs, resources for dataset descriptions, and two prompt templates. It runs over stdio and Streamable HTTP, on the current spec.

**Acceptance criteria**
- Passes the MCP Inspector and your contract tests on the current spec version; no deprecated features used.
- Tool outputs are capped (for example 2,000 tokens) with pagination; errors tell the caller how to fix the request.
- An agent using the server answers 20 test questions with ≥ 85% accuracy (checked against direct queries).
- README documents tools, limits, data licences and a security note.

**Stretch goals.** Add the Tasks extension for slow dataset downloads; publish to a registry.

**What it proves to an employer.** You can make any data source agent-ready using the industry-standard protocol.

### P2 · A research orchestrator across MCP and A2A (L2, ~15 hours)

**Real-world inspiration.** Anthropic's research system uses a lead agent that plans and spawns parallel sub-agents. It outperformed a single agent by 90.2% on an internal evaluation while using about 15× the tokens of a chat (June 2025). Cognition argues that agents must share full context, because actions carry implicit decisions (June 2025). A2A (v1.0, March 2026) lets agents from different systems collaborate.

**What to build.** An orchestrator that answers research questions about Indian policy or markets. A lead agent writes a plan and briefs 2–4 workers (with task, output format, tool list and budget). Workers use MCP tools (your P1 server, a web-search tool, a document store), and one worker is a remote agent reached over A2A. State is checkpointed so the run can resume. A single-agent baseline with the same tools is measured on the same questions.

**Acceptance criteria**
- 30 research questions with rubrics (key facts, citations); both systems graded by a calibrated judge plus human spot checks on 10.
- Report quality, cost per answer, latency and failure labels for both designs, with a recommendation backed by CIs.
- Killing the orchestrator mid-run and restarting completes the task without repeating finished worker calls.
- Distributed traces show per-agent token use; total tokens per question are capped and the cap is enforced.

**Stretch goals.** Shared decision log between workers and a measured reduction in contradictions.

**What it proves to an employer.** You can build multi-agent systems and, just as importantly, prove when they are worth their cost.

### P3 · A governed agent platform slice for an enterprise (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** Enterprises roll out MCP servers to thousands of employees and need identity, policy and audit around them. The MCP specification requires hosts to obtain user consent before invoking tools and treats tool annotations as untrusted unless the server is trusted. The MCP security best practices cover confused deputies, token passthrough and SSRF, and OWASP published a Top 10 for Agentic Applications in December 2025. The company below is illustrative.

**What to build.** A slice of an internal agent platform for an imagined 5,000-person Indian bank. It includes an MCP gateway (authentication, per-user policy, rate limits, audit logs, tool-description pinning and change detection); two remote OAuth-protected MCP servers (a mock core-banking read API and a ticketing API); an agent host with consent UX; an orchestrated workflow such as "investigate a customer complaint and draft a response" with a human approval step; distributed tracing; and an incident runbook.

**Acceptance criteria**
- No token passthrough: upstream calls use tokens issued for the server's audience, verified by tests that reject wrong-audience tokens.
- The policy file enforces at least 5 rules (for example "read-only for tier-1 staff", "no customer PII leaves region"), each with passing and failing tests.
- A changed tool description from a pinned server is detected and blocked within one request, and an alert fires.
- The workflow completes ≥ 85% of 25 scripted complaint cases with approvals recorded; no write happens without approval.
- A mapping of controls to the OWASP agentic list and NIST AI 600-1, and a 30-minute live incident drill with a postmortem.

**Stretch goals.** Short-lived, scoped credentials per agent run; an A2A interface for a partner organisation's agent with separate trust policy.

**What it proves to an employer.** You can design agent infrastructure that a bank's security team would approve. Platform, security-architecture and forward-deployed roles need this.

## Feeds into

- [AIE501 Frontier Seminar](../../year_5/AIE501_frontier_seminar_long_horizon_autonomous_agents/README.md): agent security architecture and multi-agent failure research.
- [OV12A Running Agents in Production](../../../../04_overlaps/OV12_agent_infrastructure_platform/OV12A_running_agents_in_production_sandboxes_durable/README.md) and [OV12B Agent Evaluation and Reliability](../../../../04_overlaps/OV12_agent_infrastructure_platform/OV12B_agent_evaluation_and_reliability_engineering/README.md): P3 becomes the base platform.
- [AIE403 LLMOps](../AIE403_llmops_observability_guardrails_cost_and_latency/README.md): gateways, tracing and incident response.
- [SAR403 Security Architecture for AI Systems and Agents](../../../security_architecture/year_4/SAR403_security_architecture_for_ai_systems_and_agents/README.md): deeper threat modelling.

## Sources

- MCP Specification 2026-07-28 (LSP inspiration; consent and tool-safety principles) — https://modelcontextprotocol.io/specification/2026-07-28 ; MCP security best practices — https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices (checked 2026-10)
- Anthropic, "How we built our multi-agent research system" (13 Jun 2025) — https://www.anthropic.com/engineering/multi-agent-research-system ; Cognition, "Don't Build Multi-Agents" (12 Jun 2025) — https://cognition.com/blog/dont-build-multi-agents (checked 2026-10)
- A2A releases — https://github.com/a2aproject/A2A/releases ; Cemri et al., MAST (2025) — https://arxiv.org/abs/2503.13657 (checked 2026-10)
- OWASP Top 10 for Agentic Applications (Dec 2025) — https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/ ; NIST AI 600-1 — https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf (checked 2026-10)
- Open Government Data Platform India — https://www.data.gov.in/ ; MCP Inspector — https://github.com/modelcontextprotocol/inspector (checked 2026-10)
