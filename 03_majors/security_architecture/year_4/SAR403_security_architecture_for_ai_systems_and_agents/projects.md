# SAR403 · Labs and projects

Labs use a local or hosted model through an API, an agent framework of your choice, a vector store, OPA or Cedar for tool policies, a sandbox runtime (Docker with gVisor, or Firecracker) and OpenTelemetry tracing. **All tests use benign canaries**: content that asks the agent to do something harmless and observable (reply with a marker word, call a no-op "canary" tool, write to a dummy file) so that you can measure whether untrusted content can steer the agent. You never build attack payloads, never target systems you do not own, and never use real personal data. Lab 3 is done without AI assistance. All organisations below are *illustrative scenarios* unless a source is given.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Anatomy and taxonomies | Diagram an email assistant's components and trust boundaries; map 12 risks to NIST AI 100-2, OWASP LLM 2025 and OWASP Agentic 2026 | Diagram and mapping table | 3 h |
| 2 · Detectors and evaluation | Build a 100-case benign canary set (emails, web pages, documents, tool outputs); measure a guardrail detector's false-negative rate; run an AgentDojo-style utility and security evaluation of your agent | Canary set, detector results, utility vs security numbers | 5 h |
| 3 · Patterns and trifecta (no AI) | Choose an injection-resistant pattern for five agents and audit six designs for the lethal trifecta | ADRs and a trifecta table with the leg removed for each | 3 h |
| 4 · Permission-aware retrieval | Filter retrieval by the requesting user's document permissions using an authorization service; test cross-user and cross-tenant leakage | Code, 200-query leakage test results | 5 h |
| 5 · Tool authorization and approval | Put a refund tool behind per-call policy (amount, customer, ticket) and a system-enforced approval step | Policies, tests, approval screen, a canary that tries to trigger the refund and fails | 5 h |
| 6 · Sandboxes and egress | Run a code-executing agent in two sandboxes with default-deny egress and read-only mounts | Isolation and latency comparison; blocked egress logs | 4 h |
| 7 · MCP review | Review a provided MCP server against the MCP security best practices; fix token passthrough and audience validation | Findings table; a rejected token issued for another resource | 4 h |
| 8 · Memory and kill switch | Add provenance and expiry to agent memory; implement and test a kill switch under load | Memory schema, a rejected unprovenanced memory, kill-switch timing | 4 h |
| 9 · Model supply chain | Convert a model to safetensors, sign it, refuse to load unsigned or modified models; produce an AIBOM | Verification logs, AIBOM file | 3 h |
| 10 · Telemetry, canaries in CI, playbook | Trace tasks end to end; run the canary suite on every change; write and dry-run an AI incident playbook | Traces, CI results, playbook with timings | 5 h |

## Projects

### P1 · Design review of a support chatbot (L1, ~6 hours)

**Real-world inspiration:** the OWASP Top 10 for LLM Applications 2025 lists prompt injection, sensitive information disclosure and excessive agency as top risks for exactly this kind of product ([OWASP](https://genai.owasp.org/llm-top-10/)). The chatbot is an *illustrative scenario*: a telecom's support bot that answers plan questions, looks up a customer's bill and can raise a SIM-replacement request.

**What to build:** a design review: component and boundary diagram, OWASP LLM and Agentic mapping, the five most important design changes, and a 20-case canary suite run against a small prototype.

**Acceptance criteria:**
- Every trust boundary in the diagram has at least one threat and one control.
- The SIM-replacement action requires re-authentication of the customer and cannot be triggered from retrieved content (canary test shown).
- Bill lookup is scoped to the authenticated customer; a canary asking for another customer's bill fails.
- The five design changes are each linked to an OWASP entry and a test.

**Stretch goals:** an approval-screen design for agents in the contact centre; a prompt-log retention policy under the DPDP Act.

**What it proves to an employer:** you can review an AI feature with the same rigour as any other system.

### P2 · A secure retrieval assistant for a hospital (L2, ~15 hours)

**Real-world inspiration:** hospitals are adopting AI assistants over clinical guidelines and patient notes, where a retrieval mistake is a privacy breach. The hospital is an *illustrative scenario* with three departments and synthetic patient records.

**What to build:** a retrieval assistant with permission-aware retrieval through an authorization service, department isolation, safe output handling, prompt and trace logging with redaction, an AIBOM, and an evaluation suite in CI.

**Acceptance criteria:**
- In 500 test queries across roles and departments, zero responses contain content from documents the user cannot open in the source system.
- In 100 benign canary documents planted in the knowledge base, the assistant reveals no other patient's data and makes no outbound request (logs shown).
- 100% of synthetic identifiers (Aadhaar-like, phone numbers, ABHA-like numbers) are redacted in traces and logs.
- Model output rendered in the web UI cannot execute script (show a test with a benign HTML canary).
- The AIBOM lists the model, embedding model, vector store, prompts and data sources with versions and owners.

**Stretch goals:** provenance-checked ingestion with a review queue; a comparison of separate vs shared indexes for isolation and cost.

**What it proves to an employer:** you can deliver an AI assistant that a hospital's privacy officer can approve.

### P3 · Enterprise agent platform for a fintech (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** the Five Eyes guide *Careful adoption of agentic AI services* (2026) asks for incremental deployment, limited agent privileges and human approval ([CISA](https://www.cisa.gov/news-events/news/cisa-us-and-international-partners-release-guide-secure-adoption-agentic-ai)); CaMeL and the design-patterns paper show architectural defences ([arXiv 2503.18813](https://arxiv.org/abs/2503.18813), [arXiv 2506.08837](https://arxiv.org/abs/2506.08837)); the MCP security best practices define connector duties. The fintech is an *illustrative scenario* with three agents: a customer-support agent that can propose refunds, a collections-reminder agent that drafts messages, and an internal coding agent.

**What to build:**
- a reference architecture with a model gateway, agent identities, a tool PDP, an MCP gateway with an allow-listed registry, a sandbox runtime, an approval service, memory with provenance, telemetry, an evaluation pipeline and a kill switch;
- a working slice implementing at least the support agent and the coding agent on that platform;
- a governance pack: agent inventory, risk tiers, launch review, mappings to NIST AI RMF, ISO/IEC 42001, the OWASP Agentic Top 10, the EU AI Act and India's AI Governance Guidelines, with evidence links;
- an incident playbook and a 12-month staged-autonomy roadmap.

**Acceptance criteria:**
- In a 200-case canary suite spread across emails, tickets, web pages, repository files and tool outputs, zero cases lead to an approval-gated action, an outbound message to an unlisted destination, or a write outside the agent's sandbox.
- Every tool call in the traces has an agent identity, a user (where delegated), a PDP decision and parameters; a sampled audit of 50 calls finds no gaps.
- The coding agent cannot push to protected branches, read production secrets or reach the internet except an allow-listed package mirror (tests shown).
- Every MCP server accepts only tokens issued for it; a token issued for another resource is rejected; a changed tool definition is blocked until reviewed.
- The kill switch stops all agent actions within 30 seconds under load.
- Utility on your task set is reported next to security results, with the trade-off explained.
- You defend the platform in a 25-minute oral; the panel proposes a new agent capability and you decide, with reasons, whether and how to allow it.

**Stretch goals:** a CaMeL-style planner for the support agent; red-team findings from an authorised OFF403 team incorporated with fixes.

**What it proves to an employer:** you can design and evidence an agent platform that a regulated company could actually run, which is the frontier of security architecture work in 2026.

## Feeds into

- [OV05 AI Security and Safety](../../../../04_overlaps/OV05_ai_security_safety/README.md), together with [AIE305](../../../ai_engineering/year_3/AIE305_evaluating_llm_systems/README.md) and [OFF403](../../../ethical_hacking_offensive_security/year_4/OFF403_ai_and_llm_red_teaming/README.md).
- [SAR501 Frontier Seminar](../../year_5/SAR501_frontier_seminar_post_quantum_migration/README.md): securing autonomous systems builds directly on P3.
- The [flagship industry project](../../../../06_career_and_market_readiness/05_industry_projects/SAR_security_architecture.md): its AI and agent layer.
