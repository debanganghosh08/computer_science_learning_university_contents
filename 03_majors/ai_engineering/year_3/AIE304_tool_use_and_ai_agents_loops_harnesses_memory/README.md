# AIE304 · Tool Use and AI Agents: Loops, Harnesses, Memory and Persistence

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 6 | 4 (≈ 120 hours) | L1 → L3 | [CS214](../../../../02_year_2_core_computer_science/semester_4/CS214_machine_learning_foundations/README.md), [CS205](../../../../02_year_2_core_computer_science/semester_3/CS205_software_engineering_i_design_testing/README.md); assumes [AIE301](../AIE301_llm_fundamentals_for_engineers/README.md) and [AIE302](../AIE302_prompt_and_context_engineering/README.md) | [AIE404](../../year_4/AIE404_ai_product_engineering_and_ux/README.md), [AIE401](../../year_4/AIE401_multi_agent_systems_mcp_and_orchestration/README.md), [AIE501](../../year_5/AIE501_frontier_seminar_long_horizon_autonomous_agents/README.md), [OV12](../../../../04_overlaps/OV12_agent_infrastructure_platform/) |

## Why this course matters now

An agent is a model running in a loop: it calls tools, reads the results and decides what to do next until a stop condition is met. The loop itself is small. mini-swe-agent's agent class is about 100 lines of Python, and its README reports a score above 74% on SWE-bench Verified (checked 2026-10). What decides whether an agent is useful and safe is the **harness** around the loop: the tools and their descriptions, the sandbox, the permissions, context management, memory, checkpoints and stop rules. Agents are already everyday tools for developers. In the 2026 Stack Overflow survey, 26.2% of respondents used AI agents at work, and among agent users 65.5% used Claude Code and 58.7% GitHub Copilot. Reliability still lags capability: METR's best measured model in early 2026 succeeded half the time on tasks that take a human expert about 12 hours, but its 80%-success horizon was about 70 minutes. Harness failures are public. In July 2025 an AI coding agent deleted a company's production database during a code freeze, and the vendor responded by separating development and production databases automatically. This course teaches you to build the loop from scratch, take apart real harnesses, and engineer the parts that keep an agent useful when it runs for hours with real permissions.

## Learning outcomes

By the end you can:

1. **Implement** the tool-use loop from raw API calls (tool schemas, `tool_use` → `tool_result`, parallel calls, stop reasons) without a framework.
2. **Design** tools an agent can use well (names, descriptions, parameters, error messages, output size), and **measure** the effect of tool design on task success.
3. **Choose** between a fixed workflow and an autonomous agent for a task, using cost, reliability and controllability evidence.
4. **Dissect** an open-source harness (mini-swe-agent, OpenHands, Codex CLI, Gemini CLI or Aider) and **document** its loop, tools, permissions, context strategy and failure handling.
5. **Sandbox** tool execution (containers, gVisor or Firecracker microVMs), **scope** permissions, and **justify** each capability against a threat model.
6. **Manage** context over long runs with compaction, tool-result clearing, progress files and sub-agents.
7. **Build** short- and long-term memory and **evaluate** it for recall, staleness and poisoning.
8. **Make** agents durable: checkpoint, resume after a crash and pause for human approval, without repeating side effects.
9. **Evaluate** agents with task success, pass^k reliability and cost per success, and **debug** them from traces.

## Chapters and lessons

### Chapter 1 · The agentic loop (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Workflows vs agents | Workflows follow predefined code paths; agents direct their own process and tool use (Anthropic, "Building effective agents", Dec 2024) | Classify 10 product ideas as workflow, agent or neither; justify each |
| 1.2 Reason and act | ReAct (Yao et al., 2022): interleaving reasoning and actions; observations as new context | Re-implement a ReAct loop for a calculator + search task with raw API calls |
| 1.3 The loop in code | Messages array, tool definitions, executing calls, returning `tool_result` with IDs, handling `end_turn`, `max_tokens`, errors; parallel tool calls | Write a 100-line agent with a bash tool; log every turn as JSONL |
| 1.4 Reading mini-swe-agent | Bash-only action space, linear history, environment abstraction, why minimal works | Annotate mini-swe-agent's source; run it on 5 SWE-bench Lite tasks in a container |

**Check your understanding:** What is the minimum state an agent loop must keep? Why can a bash-only agent do as well as one with dozens of tools? What should the loop do when the model requests a tool that does not exist?

### Chapter 2 · Designing tools for agents (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Tools are prompts | Names, descriptions and parameter docs steer behaviour; consolidating overlapping tools; returning meaningful context (Anthropic, "Writing effective tools for agents", Sept 2025) | Rewrite three badly described tools; measure success on 30 tasks before and after |
| 2.2 The agent–computer interface | SWE-agent's ACI (Yang et al., 2024): search, file viewer and editor commands designed for models, with linting feedback | Compare a raw `sed`-editing agent with an editor tool that validates syntax |
| 2.3 Output design | Truncation, pagination, summaries vs raw output, error messages that suggest the fix, token cost per call | Cap a tool's output at 2k tokens with a "more" cursor; measure success and cost |
| 2.4 Code as action | CodeAct (Wang et al., 2024): actions as executable code; programmatic tool calling; when code actions beat JSON calls | Implement one task with JSON tools and with a Python-execution action; compare steps |
| 2.5 Benchmarks of tool calling | Toolformer (2023), Gorilla (2023), Berkeley Function Calling Leaderboard | Run 50 BFCL-style cases against two models; categorise errors |

**Check your understanding:** A tool returns a 40k-token JSON blob. What happens to the agent over 20 turns? Why is a precise error message worth more than a retry? When should two tools be merged into one?

### Chapter 3 · Workflows first (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Five workflow patterns | Prompt chaining, routing, parallelisation, orchestrator–workers, evaluator–optimiser | Implement routing + chaining for a support-ticket pipeline |
| 3.2 Agentless | A fixed localise–repair–validate pipeline solved 32% of SWE-bench Lite at $0.70 per issue (Xia et al., 2024) | Reproduce Agentless's pipeline shape on 10 issues; compare with your Chapter 1 agent |
| 3.3 Choosing autonomy | Task variance, cost of error, need for exploration, observability; autonomy as a dial, not a switch | Write a decision record for one real-world task (e.g. GST invoice reconciliation) |
| 3.4 Human-in-the-loop points | Approval gates, review queues, escalation paths | Add an approval gate to the pipeline for any refund above a threshold |

**Check your understanding:** Why might a fixed pipeline beat an agent on a benchmark and lose in production, or the reverse? Which of the five patterns would you use for translating 10,000 product listings into six Indian languages? Where does a human add most value in a workflow?

### Chapter 4 · Harness anatomy: take real ones apart (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 What a harness contains | System prompt, tool set, permission model, environment, context policy, hooks, sub-agents, project memory files (AGENTS.md, CLAUDE.md) | Draw the component diagram of Claude Code from its public docs (hooks, sub-agents, permissions) |
| 4.2 Open-source teardown | OpenHands (MIT), OpenAI Codex CLI (Apache 2.0, rewritten in Rust in 2025), Gemini CLI (Apache 2.0, TypeScript), Aider (Apache 2.0) | Pick one; trace one full task through its source; write a 2-page teardown |
| 4.3 Hooks and policies | Pre/post tool-use hooks, blocking dangerous commands, formatting after edits, audit logs | Write a pre-tool hook that blocks writes outside the project directory |
| 4.4 Sub-agents | Isolated context windows for search or review, returning condensed results; cost of delegation | Add a "research" sub-agent; measure main-context tokens saved |

**Check your understanding:** Which harness component would you change first if an agent keeps editing the wrong files? Why do project memory files matter more as tasks get longer? What does a sub-agent cost you, and what does it buy?

### Chapter 5 · Sandboxes and permissions (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Isolation levels | Process, container, gVisor user-space kernel, Firecracker microVMs (as used by E2B); what each protects against | Run the same agent in Docker and in a microVM sandbox; compare start-up time and isolation |
| 5.2 Capability scoping | Filesystem roots, network egress allow-lists, secrets never in context, read-only defaults, separate dev and prod credentials | Write the permission manifest for a coding agent; test it with forbidden actions |
| 5.3 Dangerous combinations | Private data + untrusted content + an outbound channel (Willison, June 2025); Meta's "Agents Rule of Two" (Oct 2025) | Audit three agent designs; remove one leg from each |
| 5.4 Approval modes | Read-only, ask-before-write, auto with allow-lists; approval fatigue and how to design around it | Measure how many approvals a 30-minute task needs under three policies |
| 5.5 Learning from incidents | The July 2025 production-database deletion and the vendor's response (dev/prod separation, planning-only mode, rollback) | Write a blameless post-incident review of it from public reports |

**Check your understanding:** Why is "the model will ask before doing anything dangerous" not a control? What would you never give an agent that reads email? Approval prompts are ignored after the tenth one: what design change fixes that?

### Chapter 6 · Context management for long runs (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Why long runs fail | Context growth, distraction and context rot; repeated mistakes after summarisation | Run a 2-hour task; plot tokens per turn and the point where quality drops |
| 6.2 Compaction and clearing | Summarising history; clearing old tool results; server-side compaction and context editing in the Claude API | Implement threshold compaction; test that key facts survive with probes |
| 6.3 Progress files and git | An initializer agent writes a feature list and progress file; each session builds one feature and commits (Anthropic, Nov 2025) | Apply the pattern to a 10-feature app; measure completed features per session |
| 6.4 Just-in-time context | Loading by reference (paths, IDs) and searching with tools instead of pre-loading | Replace pre-loaded docs with a search tool; compare cost and success |

**Check your understanding:** What should a progress file contain so that a fresh context can continue without re-reading everything? Why does git make long-running agents safer? When does compaction lose exactly the detail you need?

### Chapter 7 · Memory (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Kinds of memory | Working, episodic, semantic and procedural memory (CoALA, Sumers et al., 2023) | Map each memory type onto a concrete store in your agent |
| 7.2 Virtual context | MemGPT (Packer et al., 2023): paging between context and external storage; Letta | Implement two-tier memory with explicit read/write tools |
| 7.3 Memory products | Mem0 on LOCOMO (Chhikara et al., 2025, self-reported); Anthropic's file-based memory tool; Zep temporal knowledge graph (2025) | Compare full-context, RAG-over-history and an extracted-facts store on 40 probe questions |
| 7.4 Reflection and skills | Generative Agents' reflection (Park et al., 2023); Voyager's skill library (Wang et al., 2023); Agent Workflow Memory (2024) | Save successful procedures as reusable skills; measure reuse on new tasks |
| 7.5 Memory risks | Stale facts, contradictions, memory poisoning by untrusted input, privacy and the right to erasure under India's DPDP Act | Add provenance, expiry and a delete path; test a poisoning attempt in a sandbox |

**Check your understanding:** Why is "store everything and retrieve later" a poor memory design? How would you detect that a stored fact is out of date? What must happen when a user asks the agent to forget them?

### Chapter 8 · Persistence and durable execution (weeks 8–9)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Failure is normal | Process crashes, deploys, rate limits and timeouts in the middle of a 40-step run | Kill your agent at a random step 20 times; record what is lost |
| 8.2 Checkpoints and threads | LangGraph persistence: checkpointers, threads, state snapshots, time travel; interrupts for human input (LangGraph 1.0, Oct 2025) | Rebuild the agent as a LangGraph graph with a Postgres checkpointer; resume after a kill |
| 8.3 Durable workflows | Temporal workflows vs activities, deterministic replay, retries with backoff; the Temporal + OpenAI Agents SDK integration (preview Jul 2025, GA Mar 2026); DBOS | Run the same agent on Temporal; show replay after a crash |
| 8.4 Side effects | Idempotency keys, at-least-once execution, compensation (sagas), "exactly once" as an illusion | Make a payment-like tool idempotent; prove no double charge under 100 injected crashes |
| 8.5 Long waits | Pausing for hours or days for approvals or external events; timers; versioning running workflows | Implement a 24-hour approval wait with a timeout path |

**Check your understanding:** Why must workflow code be deterministic under replay while activities need not be? A tool call timed out: did it run or not, and how does your design handle both? What breaks when you deploy new agent code while 500 runs are paused mid-way?

### Chapter 9 · Stop conditions, guardrails and recovery (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Budgets | Limits on steps, tokens, wall-clock time and money; graceful degradation when a budget runs out | Add four budgets; show the agent ends cleanly with a useful partial result |
| 9.2 Loops and stalls | Detecting repeated actions, oscillation and no-progress states | Build a detector over the last N actions; measure false positives |
| 9.3 Verification | Tests as ground truth, self-review, Reflexion-style retries (Shinn et al., 2023), and why self-correction without new evidence often fails | Require passing tests before `done`; compare outcomes |
| 9.4 Reward hacking in agents | Special-casing tests, deleting assertions, hard-coding outputs; vendor guidance warns against focusing on passing tests | Plant a task where hard-coding passes the tests; detect it with a hidden test set |
| 9.5 Guardrails | Input, tool-call and output checks; human escalation; "ask for help" as a first-class action | Add a policy check that blocks out-of-scope tool calls; log every block |

**Check your understanding:** Why is "until the model says it's done" a dangerous stop condition? How can a passing test suite hide a failed task? What should an agent hand back when it hits its budget?

### Chapter 10 · Frameworks vs from scratch (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 The landscape | Claude Agent SDK, OpenAI Agents SDK (agents, handoffs, guardrails, sessions, tracing), LangGraph, Pydantic AI, smolagents, Google ADK, Microsoft Agent Framework | Build the same 3-tool agent in two frameworks; compare code, traces and control |
| 10.2 What frameworks hide | Prompt templates, retry logic, context policy, tracing formats | Find three behaviours a framework changed silently; document them |
| 10.3 Lock-in and portability | Provider-specific features, migration cost, keeping the core loop testable | Write an adapter layer so the agent runs on two providers |
| 10.4 Upgrading frameworks safely | Pinning versions, reading changelogs, running the task suite on every framework upgrade, keeping traces comparable across versions | Upgrade one framework in a branch; run your 20-task suite; document every behaviour change |

**Check your understanding:** When does a framework save more time than it costs? Which parts of an agent would you never hand to a framework? How do you test an agent whose framework changes behaviour between versions?

### Chapter 11 · Evaluating and debugging agents (weeks 12–13)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Success and reliability | Task success, pass@k vs pass^k (τ-bench, Yao et al., 2024), cost per success (Kapoor et al., "AI Agents That Matter", 2024) | Run 20 tasks × 5 trials; report pass@1, pass^5 and cost per success |
| 11.2 Traces | Turn-by-turn logs, tool inputs/outputs, token and latency per step; OpenTelemetry GenAI agent spans (still in development status) | Instrument your agent; find the slowest and the most expensive step |
| 11.3 Failure analysis | Wrong tool, wrong arguments, misread output, premature stop, looping, environment errors | Classify 50 failed trajectories; fix the top category; re-measure |
| 11.4 Benchmarks honestly | SWE-bench Verified (500 human-screened tasks), contamination concerns ("The SWE-Bench Illusion", 2025), Terminal-Bench 2.0 | Run mini-swe-agent on 20 Verified tasks; discuss what the score does and does not show |

**Check your understanding:** An agent succeeds 80% of the time on one try but only 40% on five consecutive tries. What does that mean for a product? Why report cost per success instead of cost per run? What would make you distrust a SWE-bench number?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · 100-line agent from raw API calls | — |
| 2 | 2 | Lab 1 (cont.): Tool design A/B test | — |
| 3 | 3 | Lab 2 · Workflow vs agent bake-off | **P1 due** |
| 4 | 4 | Lab 3 · Harness teardown | Teardown report |
| 5 | 5 | Lab 4 · Sandbox and permission manifest | Threat model |
| 6 | 6 | Lab 5 · Long-run context management | Mid-term (AI off): read a trace, explain the failure |
| 7 | 7 | Lab 6 · Memory bake-off | — |
| 8 | 8 | Lab 7 · Checkpoint and resume | — |
| 9 | 8 | Lab 7 (cont.): idempotent side effects | **P2 due** |
| 10 | 9 | Lab 8 · Budgets, loops and reward hacking | — |
| 11 | 10 | Lab 9 · Same agent, two frameworks | — |
| 12 | 11 | Lab 10 · pass^k and cost per success | — |
| 13 | 11 | Lab 10 (cont.): trajectory failure analysis | Failure taxonomy |
| 14 | Integration | P3 demo day | **P3 due** |
| 15 | Review | Oral defence of P3 | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** pair-building with a coding agent (Claude Code, Codex CLI, Gemini CLI, Cursor) while you study how it behaves; generating test tasks and fixtures; summarising long traces; reading unfamiliar harness source with an assistant at your side.
- **Do without AI (drills):** write the tool-use loop from memory in 30 minutes; draw the message array after five turns, including tool IDs; write a permission manifest and threat model for a new agent; trace a crash-and-resume by hand and mark every side effect; label 30 trajectories as success, partial or failure.
- **Verify AI output by:** running every agent change against a fixed task suite with several trials (pass^k), not one demo; checking traces for silent tool errors the agent glossed over; running hidden tests the agent cannot see; inspecting the diff, not the agent's summary of the diff.
- **Where AI still fails here (show it):** agents report success when tests were skipped or weakened (catch it with hidden tests in Lab 8); they repeat failing actions after compaction (show it in Lab 5); they follow instructions embedded in files and web pages they read (show it in a sandbox with a benign canary instruction, never against real systems); reliability drops sharply from pass@1 to pass^k (show it in Lab 10).

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10, each with traces and numbers) | 25% |
| Projects P1–P3 | 35% |
| Harness teardown + threat model | 10% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) + oral defence of P3 | 20% |

**Mastery gate.** You pass when you can: (1) in 4 hours and without a framework, build an agent with a sandboxed shell tool, a permission policy, step/token/cost budgets and checkpoint-resume, and report pass^3 and cost per success on a 20-task suite; (2) given an unfamiliar open-source harness, produce in 2 hours a correct diagram of its loop, tools, permissions and context strategy; (3) given a trace of a failed run, name the root cause and the harness change that prevents it.

## Industry reality

Coding agents are the most visible agents in production. Anthropic, OpenAI and Google publish their agent harnesses or SDKs (Claude Code docs and Claude Agent SDK, Codex CLI, Gemini CLI), and the open-source OpenHands, Aider and mini-swe-agent projects make harness design inspectable. Durable execution moved from backend infrastructure into agent tooling: LangGraph 1.0 (Oct 2025) centres on persistence and human-in-the-loop, and Temporal's OpenAI Agents SDK integration became generally available in March 2026. Security guidance has converged on architecture rather than prompts: limit what an agent can do when it reads untrusted input (Meta's Rule of Two, Oct 2025; Willison's "lethal trifecta", June 2025; OWASP's Top 10 for Agentic Applications, Dec 2025). In India, Razorpay, NPCI and OpenAI piloted agentic payments over UPI in ChatGPT in October 2025, a reminder that agents increasingly touch money, where idempotency and approvals are not optional.

**Interview questions from this course**

1. *Write the agent loop on the whiteboard and list its stop conditions.* Strong answer: messages, tool schemas, execute, append `tool_result` with matching IDs, loop on `tool_use`; stops on `end_turn`, budgets (steps, tokens, time, cost), loop detection, errors and human escalation; partial results on stop.
2. *Design permissions for an agent that runs shell commands in a customer's repository.* Strong answer: isolated sandbox (container or microVM), filesystem root, egress allow-list, no production credentials, read-only by default, approvals for destructive commands, hooks and audit logs, and a threat model covering untrusted repo content.
3. *Your agent crashed at step 37 of 60, after a payment tool call timed out. How should resume work?* Strong answer: durable state/checkpoints; idempotency keys on side-effecting tools; query the payment status before retrying; deterministic replay; compensation if needed; tests with injected crashes.
4. *When would you not build an agent?* Strong answer: low-variance tasks where a workflow is cheaper, more reliable and easier to observe; cites Agentless-style results; autonomy only where exploration pays; measure pass^k and cost per success first.
5. *How should a support agent remember customers across sessions?* Strong answer: separate memory types; extract facts with provenance and expiry; retrieve on demand; handle contradictions; consent, deletion and DPDP obligations; defend against memory poisoning from user-supplied content.

## Resources (free first)

- **Essential reading:** Anthropic, "Building effective agents" — https://www.anthropic.com/engineering/building-effective-agents ; "Writing effective tools for agents — with agents" — https://www.anthropic.com/engineering/writing-tools-for-agents ; "Effective context engineering for AI agents" — https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents ; "Effective harnesses for long-running agents" — https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents ; Lilian Weng, "LLM Powered Autonomous Agents" — https://lilianweng.github.io/posts/2023-06-23-agent/
- **Courses:** Berkeley LLM Agents MOOC (Fall 2024) — https://llmagents-learning.org/f24 ; Advanced LLM Agents (Spring 2025) — https://llmagents-learning.org/sp25 ; Agentic AI MOOC (Fall 2025) — https://agenticai-learning.org/f25 ; Hugging Face Agents Course — https://huggingface.co/learn/agents-course
- **Harnesses to read:** mini-swe-agent — https://github.com/SWE-agent/mini-swe-agent ; OpenHands — https://github.com/OpenHands/OpenHands ; Codex CLI — https://github.com/openai/codex ; Gemini CLI — https://github.com/google-gemini/gemini-cli ; Aider — https://github.com/Aider-AI/aider ; Claude Code hooks — https://code.claude.com/docs/en/hooks , sub-agents — https://code.claude.com/docs/en/sub-agents , permissions — https://code.claude.com/docs/en/permissions
- **SDKs and frameworks:** Claude Agent SDK — https://code.claude.com/docs/en/agent-sdk/overview ; OpenAI Agents SDK — https://openai.github.io/openai-agents-python/ ; LangGraph persistence — https://docs.langchain.com/oss/python/langgraph/persistence ; smolagents — https://github.com/huggingface/smolagents ; Pydantic AI — https://pydantic.dev/docs/ai/overview/ ; Google ADK — https://adk.dev/ ; Microsoft Agent Framework — https://github.com/microsoft/agent-framework
- **Durability and sandboxes:** Temporal + OpenAI Agents SDK — https://temporal.io/blog/announcing-openai-agents-sdk-integration ; DBOS for agents — https://docs.dbos.dev/integrations/openai-agents ; E2B — https://e2b.dev/ ; Firecracker — https://firecracker-microvm.github.io/ ; gVisor — https://gvisor.dev/
- **Memory:** Letta docs — https://docs.letta.com/ ; Mem0 — https://github.com/mem0ai/mem0 ; Anthropic memory tool — https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool ; Graphiti — https://github.com/getzep/graphiti
- **Security (defensive):** Willison, "The lethal trifecta for AI agents" — https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/ ; Meta, "Agents Rule of Two" — https://ai.meta.com/blog/practical-ai-agent-security/ ; OWASP Top 10 for Agentic Applications — https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
- **Benchmarks:** SWE-bench — https://www.swebench.com/ ; τ²-bench — https://github.com/sierra-research/tau2-bench ; Terminal-Bench — https://www.tbench.ai/ ; BFCL — https://gorilla.cs.berkeley.edu/leaderboard.html

## Sources

- mini-swe-agent README ("some 100 lines of python", ">74% on the SWE-bench verified benchmark") — https://github.com/SWE-agent/mini-swe-agent (checked 2026-10)
- Stack Overflow Developer Survey 2026, AI section (26.2% use agents at work; Claude Code 65.5%, Copilot 58.7% among agent users) — https://survey.stackoverflow.co/2026/ai/data (checked 2026-10)
- METR time-horizon data file (Claude Opus 4.6: ~12 h at 50%, ~70 min at 80%) — https://metr.org/assets/benchmark_results_1_1.yaml (checked 2026-10)
- Fortune, "AI coding tool Replit wiped database…" (23 Jul 2025) — https://fortune.com/2025/07/23/ai-coding-tool-replit-wiped-database-called-it-a-catastrophic-failure/ (checked 2026-10)
- Anthropic engineering posts: "Building effective agents" (19 Dec 2024), "Writing effective tools for agents" (11 Sept 2025), "Effective context engineering" (29 Sept 2025), "Effective harnesses for long-running agents" (26 Nov 2025) — URLs above (checked 2026-10)
- Yao et al., ReAct (2022) — https://arxiv.org/abs/2210.03629 ; Yang et al., SWE-agent (2024) — https://arxiv.org/abs/2405.15793 ; Wang et al., CodeAct (2024) — https://arxiv.org/abs/2402.01030 ; Xia et al., Agentless (2024) — https://arxiv.org/abs/2407.01489 ; Wang et al., OpenHands (2024) — https://arxiv.org/abs/2407.16741 (checked 2026-10)
- Schick et al., Toolformer (2023) — https://arxiv.org/abs/2302.04761 ; Patil et al., Gorilla (2023) — https://arxiv.org/abs/2305.15334 ; Shinn et al., Reflexion (2023) — https://arxiv.org/abs/2303.11366 ; Huang et al. (2023) — https://arxiv.org/abs/2310.01798 (checked 2026-10)
- Sumers et al., CoALA (2023) — https://arxiv.org/abs/2309.02427 ; Packer et al., MemGPT (2023) — https://arxiv.org/abs/2310.08560 ; Chhikara et al., Mem0 (2025) — https://arxiv.org/abs/2504.19413 ; Rasmussen et al., Zep (2025) — https://arxiv.org/abs/2501.13956 ; Park et al. (2023) — https://arxiv.org/abs/2304.03442 ; Wang et al., Voyager (2023) — https://arxiv.org/abs/2305.16291 ; Wang et al., Agent Workflow Memory (2024) — https://arxiv.org/abs/2409.07429 (checked 2026-10)
- LangChain, "LangChain and LangGraph Agent Frameworks Reach v1.0 Milestones" (22 Oct 2025) — https://www.langchain.com/blog/langchain-langgraph-1dot0 ; Temporal integration (preview 30 Jul 2025, GA 23 Mar 2026) — https://temporal.io/blog/announcing-openai-agents-sdk-integration (checked 2026-10)
- Codex CLI, "Codex CLI is Going Native" (30 May 2025) — https://github.com/openai/codex/discussions/1174 (checked 2026-10)
- Yao et al., τ-bench (2024) — https://arxiv.org/abs/2406.12045 ; Kapoor et al., "AI Agents That Matter" (2024) — https://arxiv.org/abs/2407.01502 ; Liang et al., "The SWE-Bench Illusion" (2025) — https://arxiv.org/abs/2506.12286 ; OpenAI, "Introducing SWE-bench Verified" (Aug 2024) — https://openai.com/index/introducing-swe-bench-verified/ ; Terminal-Bench 2.0 (Nov 2025) — https://www.tbench.ai/news/announcement-2-0 (checked 2026-10)
- OpenTelemetry GenAI agent spans (status: Development) — https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-agent-spans.md (checked 2026-10)
- Razorpay newsroom, agentic payments with NPCI and OpenAI (Oct 2025) — https://razorpay.com/newsroom/razorpay-npci-and-openai-come-together-to-launch-agentic-payments-ushering-in-ai-driven-commerce-at-national-scale/ (checked 2026-10)

_Last reviewed: 2026-10_
