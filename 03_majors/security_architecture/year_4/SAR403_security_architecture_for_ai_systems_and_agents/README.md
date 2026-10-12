# SAR403 · Security Architecture for AI Systems and Agents

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 8 | 4 (≈ 120 hours) | L3 → L4 | [SAR303](../../year_3/SAR303_zero_trust_architecture/README.md) (also recommended: [SAR302](../../year_3/SAR302_threat_modeling/README.md), [SAR402](../SAR402_identity_architecture_at_scale/README.md)) | [SAR501](../../year_5/SAR501_frontier_seminar_post_quantum_migration/README.md), [OV05 AI Security and Safety](../../../../04_overlaps/OV05_ai_security_safety/README.md) |

Part of the [Security Architecture major](../../README.md), and one of the three courses of the [OV05 AI Security and Safety](../../../../04_overlaps/OV05_ai_security_safety/README.md) overlap with [AIE305 Evaluating LLM Systems](../../../ai_engineering/year_3/AIE305_evaluating_llm_systems/README.md) and [OFF403 AI and LLM Red Teaming](../../../ethical_hacking_offensive_security/year_4/OFF403_ai_and_llm_red_teaming/README.md). The AI Engineering major teaches how to build agents ([AIE304](../../../ai_engineering/year_3/AIE304_tool_use_and_ai_agents_loops_harnesses_memory/README.md), [AIE401](../../../ai_engineering/year_4/AIE401_multi_agent_systems_mcp_and_orchestration/README.md)); OFF403 tests them under authorization. This course designs them so that untrusted content, a compromised connector or a confused model cannot turn into stolen data or unauthorised actions. Everything here is defensive: you study attack classes to design them out, and every test uses benign canaries on systems you own.

## Why this course matters now

AI was the top security skills need in ISC2's 2025 study (41%) and in its 2026 India study (52%) ([ISC2](https://www.isc2.org/Insights/2025/12/2025-ISC2-Cybersecurity-Workforce-Study); [ISC2 India](https://www.isc2.org/insights/2026/09/research-india-cybersecurity-workforce-reaches-a-turning-point-skills-ai)). Agents combine three things that were rarely together before: access to private data, exposure to content written by strangers, and the ability to act. In June 2025 Microsoft fixed CVE-2025-32711 ("EchoLeak"), an information-disclosure flaw in Microsoft 365 Copilot in which content arriving by email could lead the assistant to leak data ([NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-32711)). OWASP published a Top 10 for Agentic Applications in December 2025, and in April–May 2026 six national cyber agencies including CISA, NSA and the UK NCSC published *Careful adoption of agentic AI services*, advising incremental deployment, limited agent privileges and human approval for decision-making steps ([CISA](https://www.cisa.gov/news-events/news/cisa-us-and-international-partners-release-guide-secure-adoption-agentic-ai)). The Model Context Protocol, now governed by the Linux Foundation's Agentic AI Foundation, ships detailed security best practices for connector servers. Research shows architecture works where filters do not: Google DeepMind's CaMeL achieved provable security on 77% of AgentDojo tasks while an undefended agent completed 84% ([arXiv 2503.18813](https://arxiv.org/abs/2503.18813)). The scarce skill is designing these trade-offs for a real business and proving the result.

## Learning outcomes

By the end you can:

1. **Decompose** an AI system (model, context, retrieval, tools, memory, orchestrator, connectors, logs) into trust boundaries and **map** its risks to NIST AI 100-2, the OWASP LLM Top 10 (2025) and the OWASP Agentic Top 10 (2026).
2. **Explain** why prompt injection has no complete filter-based fix, and **apply** injection-resistant design patterns (plan-then-execute, dual LLM, action selector, context minimisation, CaMeL-style capability tracking).
3. **Design** data boundaries for retrieval-augmented systems: permission-aware retrieval, tenant isolation, output handling and prompt-log retention.
4. **Design** tool permissions with least agency, per-call authorization, parameter validation and human approval enforced outside the model.
5. **Select** and **configure** sandboxes (containers, gVisor, Firecracker microVMs, WebAssembly) for code-executing and browsing agents, with egress control.
6. **Govern** MCP servers and other connectors: authorization, consent, token audience, SSRF controls, allow-listing and version pinning.
7. **Secure** the AI supply chain (models, datasets, prompts, tools) with provenance, signing, safe formats and AI bills of materials.
8. **Build** an AI security governance and monitoring layer mapped to NIST AI RMF, ISO/IEC 42001, the EU AI Act and India's AI Governance Guidelines, with evidence.

## Chapters and lessons

### Chapter 1 · AI systems as an attack surface (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Anatomy | Model, system prompt, context window, retrieval, tools, memory, orchestrator, connectors, UI, logs and evaluation; where each crosses a trust boundary | Draw the component diagram of an email assistant and mark boundaries |
| 1.2 The instruction–data confusion | Why a model cannot reliably tell instructions from data in its context; why this makes the model call itself a trust boundary | Explain in one page why escaping and delimiters reduce but do not remove the risk |
| 1.3 Taxonomies | NIST AI 100-2 E2025, OWASP LLM Top 10 2025 (LLM01–LLM10), OWASP Agentic Top 10 (ASI01 agent goal hijack to ASI10 rogue agents), MITRE ATLAS | Map 12 described risks to all three lists |
| 1.4 Cases | EchoLeak (2025), an agent deleting a production database during a code freeze (2025), integration-token theft (Salesloft Drift, 2025); what each says about design | Write the architectural lesson for each case |

**Check your understanding:** (1) Why is an LLM call a trust boundary even inside one process? (2) Which OWASP Agentic entry describes a legitimate tool used harmfully? (3) What design decision would have contained the database-deletion case?

### Chapter 2 · Prompt injection as a design problem (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Direct and indirect injection | User-supplied vs content-supplied instructions (web pages, emails, documents, tool outputs); why indirect injection matters most for agents | Classify ten agent inputs by who controls them |
| 2.2 Detection and its limits | Classifiers and guardrail services (Azure AI Content Safety Prompt Shields, Amazon Bedrock Guardrails, NeMo Guardrails) as probabilistic layers; false negatives under adaptation | Measure a detector's false-negative rate on a benign-canary test set you build |
| 2.3 Measuring defences | Benchmarks such as AgentDojo (97 tasks, 629 security test cases); utility vs security trade-off | Run a small AgentDojo-style evaluation on your own agent |
| 2.4 Architecture over prompts | Why system-prompt rules are not controls; where controls must live instead | Move three "the model must never…" rules into enforcement outside the model |

**Check your understanding:** (1) Why can't a better system prompt fix indirect injection? (2) What does a detector's false-negative rate mean for an agent that can send money? (3) Why measure utility alongside security?

### Chapter 3 · Injection-resistant design patterns (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 The pattern catalogue | Beurer-Kellner et al. (2025): action selector, plan-then-execute, LLM map-reduce, dual LLM, code-then-execute, context minimisation; what each gives up | Pick a pattern for five agents and justify the trade-off |
| 3.2 CaMeL | Separating control flow (from the trusted query) from data flow (untrusted content); capabilities attached to data; policy checks before tool calls | Sketch a CaMeL-style design for an email-and-calendar assistant |
| 3.3 Dangerous combinations | The "lethal trifecta" (private data, untrusted content, external communication); Meta's "Agents Rule of Two" | Audit six agent designs and remove one leg from each |
| 3.4 Choosing for a business | When reduced capability is acceptable; staged autonomy; read-only first | Write an ADR for an agent's autonomy level |

**Check your understanding:** (1) What does plan-then-execute protect, and what can still go wrong? (2) Why does the Rule of Two allow at most two of the three properties without human oversight? (3) When is the dual LLM pattern too costly?

### Chapter 4 · Data boundaries and retrieval security (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Permission-aware retrieval | Filtering by the requesting user's access at retrieval time, not after generation; reusing the authorization service from SAR402 | Build retrieval that respects document ACLs and prove a user cannot retrieve others' files |
| 4.2 Tenant isolation | Separate indexes vs filtered shared indexes; metadata integrity; cache and log isolation | Test cross-tenant leakage in a shared vector store |
| 4.3 Knowledge-base poisoning | Who can write to sources the agent reads; provenance and review for ingested content | Add provenance tags and an ingestion review step |
| 4.4 Output handling | Treating model output as untrusted input (LLM05): encoding for HTML, SQL and shell contexts; system prompt leakage (LLM07) | Fix three output-handling flaws in a demo app |
| 4.5 Logs and retention | Prompt and response logging for security vs privacy duties under the DPDP Act; redaction | Design a prompt-log policy with redaction and retention |

**Check your understanding:** (1) Why is post-generation filtering too late for access control? (2) What makes embeddings sensitive? (3) Who should be allowed to write to an agent's knowledge base?

### Chapter 5 · Tool permissions and least agency (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Excessive agency | LLM06 and ASI02 tool misuse: too many tools, too broad tools, too much autonomy | Reduce an agent's toolset to the minimum for its tasks |
| 5.2 Per-call authorization | Every tool call checked by a PDP with user, agent, tool, parameters and context (from SAR402); parameter validation and allow-lists | Enforce per-call policies for a refund tool |
| 5.3 Human approval | Approval for irreversible or high-value actions, enforced by the system; approval fatigue and good approval screens | Design an approval screen that shows exactly what will happen |
| 5.4 Rate, volume and budgets | Limits on actions, spend and data volume per task; unbounded consumption (LLM10) | Add per-task limits and an alert |

**Check your understanding:** (1) Why must approval be enforced outside the model? (2) What information must an approval screen show? (3) How does a budget limit act as a security control?

### Chapter 6 · Sandboxing and execution isolation (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Why agents need sandboxes | Code execution, file handling, browsing; ASI05 unexpected code execution | List what a code-running agent can reach by default on a developer laptop |
| 6.2 Isolation options | Containers, gVisor, Firecracker microVMs, WebAssembly runtimes; isolation strength vs start-up cost | Run the same task in two sandboxes and compare isolation and latency |
| 6.3 Egress and filesystem control | Default-deny network, allow-listed destinations, read-only mounts, no secrets inside | Configure a sandbox that can reach one package mirror and nothing else |
| 6.4 Coding and browsing agents | Permission modes, dev containers, separate browser profiles, credential isolation | Write a policy for coding agents on developer machines |

**Check your understanding:** (1) Why is a container alone weak isolation for untrusted code? (2) What should never be mounted into an agent sandbox? (3) How do you let a browsing agent sign in without exposing the user's main session?

### Chapter 7 · MCP and connector trust (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 MCP architecture | Hosts, clients, servers, tools and resources; the stateless 2026-07-28 revision | Diagram an assistant with four MCP servers and their trust levels |
| 7.2 Authorization | OAuth-based authorization, protected resource metadata (RFC 9728), resource indicators (RFC 8707), audience validation, client ID metadata documents | Configure an MCP server to accept only tokens issued for it |
| 7.3 The security best practices | Per-client consent for proxy servers (confused deputy), no token passthrough, SSRF controls in discovery, state-handle binding, local server consent and sandboxing, scope minimisation | Review a provided MCP server against each practice |
| 7.4 Server governance | Allow-listed registries, version pinning, reviewing tool descriptions for embedded instructions, detecting definition changes, MCP gateways | Design an enterprise MCP allow-list and change-review process |

**Check your understanding:** (1) Why is a tool description untrusted input? (2) What goes wrong when an MCP server forwards the client's token downstream? (3) Why does a one-click local server install need to show the full command?

### Chapter 8 · Multi-agent systems and memory (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Inter-agent communication | ASI07: authenticating agents to each other, message integrity, least privilege between agents | Add identities and signed messages between two agents |
| 8.2 Memory and context poisoning | ASI06: persistent memory as an attack path; provenance, expiry and review of memories | Design a memory store with provenance and expiry |
| 8.3 Cascading failures and rogue agents | ASI08 and ASI10: blast radius between agents, circuit breakers, kill switches, budgets | Implement a kill switch and test it under load |
| 8.4 Human–agent trust | ASI09: over-reliance, persuasive outputs, approval fatigue | Write UI rules that keep users in control |

**Check your understanding:** (1) Why should one agent not trust another's output as instructions? (2) What makes memory poisoning persistent? (3) How do you test a kill switch safely?

### Chapter 9 · The AI supply chain (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Models and formats | Unsafe serialisation (pickle) vs safetensors; model provenance; model cards | Convert a model to a safe format and verify its hash |
| 9.2 Signing and transparency | OpenSSF model signing (Sigstore-based); verifying before load | Sign a model and refuse to load an unsigned one |
| 9.3 Data and fine-tuning | Dataset provenance, poisoning, fine-tuning pipelines, NIST SP 800-218A practices | Write provenance requirements for a fine-tuning dataset |
| 9.4 AI bills of materials | CycloneDX ML-BOM, SPDX 3.0 AI profile, CERT-In's AIBOM guidance; prompts and tools as components (ASI04) | Produce an AIBOM for your agent |
| 9.5 Third-party model APIs | Data-use terms, residency, retention, regional endpoints | Compare three providers' enterprise data terms for a regulated workload |

**Check your understanding:** (1) Why can loading a model file run code? (2) What belongs in an AIBOM beyond the model? (3) Which contract terms matter most for a bank using a hosted model?

### Chapter 10 · Monitoring, evaluation and incident response (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Telemetry | Tracing prompts, retrievals and tool calls with OpenTelemetry GenAI conventions; privacy-aware logging | Instrument your agent and trace one task end to end |
| 10.2 Security evaluation | Canary suites, regression tests for injection, results from authorised red teaming (OFF403) | Build a 50-case benign canary suite and run it in CI |
| 10.3 Detection | Signals: unusual tool sequences, data volume, new destinations, approval anomalies | Write five detection rules over your traces |
| 10.4 AI incident response | Containment (revoke agent tokens, disable tools, kill switch), evidence, notification duties | Write and dry-run an AI incident playbook |

**Check your understanding:** (1) What must a trace contain to investigate an agent incident? (2) Why are evaluations regression tests, not one-off audits? (3) What is the first containment step for a compromised connector?

### Chapter 11 · Governance and regulation (weeks 11–12)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Risk frameworks | NIST AI RMF 1.0 (govern, map, measure, manage) and the generative AI profile (NIST AI 600-1); NIST IR 8596 Cyber AI Profile (preliminary draft, December 2025) | Map your agent's controls to AI RMF functions |
| 11.2 Management systems | ISO/IEC 42001:2023 AI management systems; how it relates to ISO/IEC 27001 | Draft the scope and risk process for an AI management system |
| 11.3 Law and policy | EU AI Act (general-purpose AI obligations from August 2025; high-risk timeline changed in 2026, so check the Commission page); India AI Governance Guidelines (November 2025); DPDP Act | Classify three products under the EU AI Act and write the India section |
| 11.4 Frameworks for practitioners | Google SAIF, CSA MAESTRO, the Five Eyes agentic guidance | Turn the Five Eyes recommendations into a checklist with evidence fields |
| 11.5 Inventory and approval | AI system and agent inventories, risk tiers, launch reviews | Design an AI launch review for your organisation |

**Check your understanding:** (1) What evidence shows that an AI risk is "managed"? (2) Why do AI regulatory dates need checking every term? (3) What belongs in an agent inventory entry?

### Chapter 12 · Reference architecture for an enterprise agent platform (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Platform components | Model gateway (policy, DLP, logging, routing), agent identity, tool PDP, MCP gateway and registry, sandbox runtime, memory with provenance, approval service, evaluation pipeline, monitoring | Draw the reference architecture and its trust boundaries |
| 12.2 Shared vs per-agent controls | What the platform enforces for every agent vs what each team configures | Write the platform's non-negotiable controls |
| 12.3 AI securing AI | AI-based reviewers, classifiers and judges in the loop; their measured error rates; human ownership | Compare an AI reviewer's findings on your design with your own |
| 12.4 Roadmap | Staged autonomy, from read-only assistants to approval-gated actions to limited autonomy | Write a 12-month rollout plan with gates |

**Check your understanding:** (1) Which controls must be platform-level? (2) When is it safe to raise an agent's autonomy? (3) How do you know an AI reviewer is good enough to rely on?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Anatomy and taxonomy mapping | Boundary diagram |
| 2 | 2 | Lab 2 · Detector false negatives and AgentDojo-style evaluation | Measurements |
| 3 | 3 | Lab 3 · Pattern selection and trifecta audit (no AI drafting) | ADRs; **P1 due** |
| 4 | 4 | Lab 4 · Permission-aware retrieval | Leakage tests |
| 5 | 5 | Lab 5 · Per-call authorization and approval | Enforced refund tool |
| 6 | 6 | Lab 6 · Sandboxes and egress | Comparison report |
| 7 | 7 | Lab 7 · MCP server review and audience validation | Findings; mid-term (AI off) |
| 8 | 8 | Lab 8 · Memory provenance and kill switch | Tested kill switch |
| 9 | 9 | Lab 9 · Signed models and AIBOM | Refused unsigned model; **P2 due** |
| 10 | 10 | Lab 10 · Telemetry, canary suite and playbook | CI suite |
| 11 | 11 | Framework mapping | AI RMF and 42001 maps |
| 12 | 11 | Regulation workshop | EU and India sections |
| 13 | 12 | Reference architecture | Architecture draft |
| 14 | 12 | Project work | **P3 due** |
| 15 | Review | Design exam and oral | Final exam |

## Working with AI in this course

- **Use AI for:** generating benign canary test cases and evaluation harnesses; drafting policies for tool calls; summarising specifications (MCP, OWASP lists, NIST documents); producing first-draft AIBOMs and framework mappings; acting as the system under test in your own lab.
- **Do without AI (drills):** the pattern selection and trifecta audit (Lab 3); the MCP review checklist on first pass; the mid-term and final; approval-screen design.
- **Verify AI output by:** running every policy against deny cases; measuring false-negative rates of any detector on your own canary suite; checking OWASP, NIST and MCP references at the source; testing designs with canaries in emails, documents, web pages and tool outputs, not only in chat.
- **Where AI still fails here (show it):** ask an assistant to "secure" an agent and record how often it proposes prompt wording as the main control; have it review an MCP server that forwards client tokens and record whether it flags passthrough; measure how often your agent follows a benign canary instruction placed in a retrieved document before and after your architectural changes.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs 1–10 | 25% |
| Projects P1 / P2 / P3 | 5% / 15% / 25% |
| Mid-term (AI off) | 10% |
| Final: design exam plus oral defence of P3 | 20% |

**Mastery gate.** You pass when you can, without AI and in three hours: (a) design the security architecture of an unseen agent (data boundaries, tool permissions, sandbox, connector trust, approval, monitoring) and show that no path exists from untrusted content to a high-impact action without human approval; (b) find at least four of five planted flaws in a provided agent design (for example token passthrough, retrieval without ACL filtering, approval enforced only in the prompt, a sandbox with open egress, an unsigned model loaded from a public hub); and (c) map the design to NIST AI RMF and the OWASP Agentic Top 10 with evidence fields.

## Industry reality

- Agencies now publish agent-specific guidance (Five Eyes, 2026), OWASP maintains LLM and agentic risk lists, and the MCP specification carries normative security requirements.
- Vendors ship guardrail services (Prompt Shields, Bedrock Guardrails) and agent identity products; research (CaMeL, design patterns, Rule of Two) shows architectural defences that trade capability for provable safety.
- In India, the AI Governance Guidelines (November 2025) and the DPDP Act shape enterprise AI deployments, and CERT-In's 2025 BOM guidance includes AI bills of materials.
- Employers hiring for AI security architecture ask candidates to secure a concrete agent in a design round.

**Interview questions from this course**

1. *"Design a customer-support agent that can issue refunds. How do you make sure prompt injection cannot move money?"* Strong answer: separate planning from untrusted content, per-call PDP checks with amount limits, human approval enforced outside the model, refund tool scoped to the ticket's customer, canary testing, logging and kill switch.
2. *"Employees want to connect MCP servers to their AI assistant. What is your policy?"* Strong answer: allow-listed registry, version pinning and definition-change review, OAuth with audience validation and no passthrough, per-client consent, sandboxed local servers with full-command consent, scope minimisation, monitoring.
3. *"We are building RAG over HR documents. How do we stop employees seeing others' salaries?"* Strong answer: permission-aware retrieval using the same authorization service as the source systems, no post-hoc filtering, tenant and document metadata integrity, tests for leakage, prompt-log redaction.
4. *"What is in our AI supply chain and how do we secure it?"* Strong answer: models, datasets, fine-tuning code, prompts, tools and connectors, third-party APIs; safe formats, signing and verification, provenance, AIBOM, contract terms, change review.
5. *"How would you show an auditor that our agent platform is governed?"* Strong answer: inventory and risk tiers, launch reviews, mapping to NIST AI RMF and ISO/IEC 42001 with evidence (traces, eval results, approvals), incident playbook, regulatory classification with dates checked.

## Resources (free first)

- **Risk lists and frameworks:** [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/); [OWASP Top 10 for Agentic Applications](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/); [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework); [NIST AI 600-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf); [NIST AI 100-2 E2025](https://csrc.nist.gov/pubs/ai/100/2/e2025/final); [NIST IR 8596 (draft)](https://csrc.nist.gov/pubs/ir/8596/iprd); [MITRE ATLAS](https://atlas.mitre.org/); [CSA MAESTRO](https://cloudsecurityalliance.org/blog/2025/02/06/agentic-ai-threat-modeling-framework-maestro); [Five Eyes agentic guidance](https://www.cyber.gov.au/business-government/secure-design/artificial-intelligence/careful-adoption-of-agentic-ai-services).
- **Design research:** Debenedetti et al., [CaMeL](https://arxiv.org/abs/2503.18813); Beurer-Kellner et al., [Design Patterns for Securing LLM Agents against Prompt Injections](https://arxiv.org/abs/2506.08837); [AgentDojo](https://arxiv.org/abs/2406.13352); Willison, [the lethal trifecta](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) and [prompt injection series](https://simonwillison.net/series/prompt-injection/); Meta, [Agents Rule of Two](https://ai.meta.com/blog/practical-ai-agent-security/).
- **Connectors and platforms:** [MCP specification](https://modelcontextprotocol.io/specification/2026-07-28) and [security best practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices); [OpenTelemetry GenAI conventions](https://github.com/open-telemetry/semantic-conventions-genai).
- **Supply chain and isolation:** [OpenSSF model signing](https://github.com/sigstore/model-transparency); [safetensors](https://huggingface.co/docs/safetensors); [CycloneDX](https://cyclonedx.org/); [gVisor](https://gvisor.dev/docs/); [Firecracker](https://firecracker-microvm.github.io/); [NeMo Guardrails](https://docs.nvidia.com/nemo/guardrails/).
- **Policy and law:** [EU AI Act](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai); [India AI Governance Guidelines](https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/nov/doc2025115685601.pdf); [ISO/IEC 42001](https://www.iso.org/standard/42001) (standard text is paid; the NIST documents cover the concepts free).

## Sources

All checked 12 Oct 2026.

- ISC2, 2025 Cybersecurity Workforce Study — https://www.isc2.org/Insights/2025/12/2025-ISC2-Cybersecurity-Workforce-Study ; India study (24 Sep 2026) — https://www.isc2.org/insights/2026/09/research-india-cybersecurity-workforce-reaches-a-turning-point-skills-ai
- NVD, CVE-2025-32711 (Microsoft 365 Copilot information disclosure, June 2025) — https://nvd.nist.gov/vuln/detail/CVE-2025-32711
- CISA and partners, *Careful adoption of agentic AI services* (1 May 2026); NSA release (30 Apr 2026) — https://www.cisa.gov/news-events/news/cisa-us-and-international-partners-release-guide-secure-adoption-agentic-ai ; https://www.nsa.gov/Press-Room/Press-Releases-Statements/Press-Release-View/Article/4475134/nsa-joins-the-asds-acsc-and-others-to-release-guidance-on-agentic-artificial-in/
- OWASP Top 10 for Agentic Applications (9 Dec 2025); entry names as summarised by Cycode — https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/ ; https://cycode.com/blog/owasp-top-10-agentic-applications/
- Anthropic, donation of MCP to the Agentic AI Foundation (9 Dec 2025) — https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation ; MCP 2026-07-28 security best practices — https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices
- Debenedetti et al., CaMeL (77% of AgentDojo tasks with provable security vs 84% undefended) — https://arxiv.org/abs/2503.18813 ; AgentDojo (97 tasks, 629 security test cases) — https://arxiv.org/abs/2406.13352
- Agent database deletion during a code freeze (July 2025), Tom's Hardware — https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-coding-platform-goes-rogue-during-code-freeze-and-deletes-entire-company-database-replit-ceo-apologizes-after-ai-engine-says-it-made-a-catastrophic-error-in-judgment-and-destroyed-all-production-data
- EU AI Act timeline (high-risk obligations moved by the 2026 omnibus; check before citing) — https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai ; India AI Governance Guidelines (5 Nov 2025) — https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/nov/doc2025115685601.pdf
- NIST IR 8596 preliminary draft (16 Dec 2025) — https://csrc.nist.gov/pubs/ir/8596/iprd
- CERT-In BOM guidelines v2.0 including AIBOM (9 Jul 2025), as summarised by Khaitan & Co — https://khaitanco.com/thought-leadership/CERT-Ins-Expanded-BOM-Guidelines-Preparing-for-the-Next-Phase-of-Cyber-Regulation

_Last reviewed: 2026-10_
