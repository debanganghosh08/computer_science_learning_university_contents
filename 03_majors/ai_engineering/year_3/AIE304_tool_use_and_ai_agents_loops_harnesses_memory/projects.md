# AIE304 · Labs and projects

Every lab and project ships the agent code, a sandbox definition (Dockerfile or microVM config), a permission manifest, full JSONL traces of every run, and a task suite with automatic checkers. Report task success over several trials (pass^k) and cost per success, never a single demo run. All agents run only in sandboxes you control; no agent gets credentials to real production systems.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · The 100-line agent and tool design | Build the tool-use loop from raw API calls with a sandboxed bash tool; then A/B two versions of three tools (descriptions, outputs, errors) on 30 tasks | Code, traces, success rates per tool design | 6 h |
| 2 · Workflow vs agent bake-off | Implement a fixed localise–repair–validate pipeline and your agent on 10 SWE-bench Lite tasks in containers | Success, cost and time per approach; a decision record | 5 h |
| 3 · Harness teardown | Trace one task through an open-source harness (OpenHands, Codex CLI, Gemini CLI, Aider or mini-swe-agent) | 2-page teardown: loop, tools, permissions, context policy, failure handling, with source links | 5 h |
| 4 · Sandbox and permission manifest | Run your agent in a container and a microVM sandbox; write a manifest (filesystem root, egress allow-list, approvals); write a pre-tool hook that blocks out-of-scope writes | Manifest, hook, a test log of 20 forbidden actions all blocked, start-up time comparison | 5 h |
| 5 · Long-run context management | Run a 2-hour task; add compaction, tool-result clearing and a progress file; probe for retained facts | Tokens-per-turn plot, success with and without each technique | 5 h |
| 6 · Memory bake-off | Compare full context, retrieval over history and an extracted-facts store on 40 probe questions; add provenance, expiry and deletion | Probe accuracy per design; a sandboxed poisoning test and its result | 5 h |
| 7 · Checkpoint, resume and idempotent side effects | Rebuild the agent on LangGraph with a Postgres checkpointer or on Temporal; kill it at random steps; make a payment-like tool idempotent | Resume correctness over 50 kills; zero duplicate side effects over 100 injected crashes | 7 h |
| 8 · Budgets, loops and reward hacking | Add step/token/time/cost budgets and a loop detector; plant a task where hard-coding passes visible tests | Clean-stop demonstrations; detector false-positive rate; hidden-test results | 4 h |
| 9 · Same agent, two frameworks | Build one 3-tool agent with two of: Claude Agent SDK, OpenAI Agents SDK, LangGraph, Pydantic AI, smolagents | Code, traces, list of behaviours each framework changed silently | 4 h |
| 10 · pass^k, cost per success and failure analysis | Run 20 tasks × 5 trials; classify 50 failed trajectories; fix the top category and re-measure | pass@1, pass^5, cost per success before and after; failure taxonomy | 6 h |

## Projects

### P1 · A minimal coding agent you fully understand (L1, ~6 hours)

**Real-world inspiration.** mini-swe-agent shows that an agent class of about 100 lines of Python, using only bash, can score above 74% on SWE-bench Verified with a strong model (README, checked 2026-10). The harness is small; the environment and model do the heavy lifting.

**What to build.** A coding agent under 200 lines (excluding tests) that uses only raw API calls and a single bash tool executed inside a Docker container. It keeps a linear message history, enforces step and token budgets, and writes a JSONL trace.

**Acceptance criteria**
- Runs on 10 SWE-bench Lite tasks (or 10 tasks from a suite you write with hidden tests) inside containers; reports resolved count and cost per resolved task.
- Every run ends with a clear stop reason (done, budget, error) and a final summary.
- No command escapes the container (verified by a host-side canary file that must remain untouched).
- The README explains each line of the loop and compares the design with mini-swe-agent's.

**Stretch goals.** Add a file-viewer/editor tool with syntax checking (SWE-agent-style) and measure the difference.

**What it proves to an employer.** You understand agents from first principles and do not need a framework to build or debug one.

### P2 · A durable refunds agent with approvals (L2, ~15 hours)

**Real-world inspiration.** Agents increasingly touch money: Razorpay, NPCI and OpenAI piloted agentic payments over UPI in ChatGPT in October 2025. In July 2025 an AI coding agent deleted a company's production database during a code freeze, and the vendor responded with automatic dev/prod separation and a planning-only mode. Durable execution frameworks such as Temporal (OpenAI Agents SDK integration GA in March 2026) and LangGraph (1.0, Oct 2025) exist because long agent runs fail midway. The system below uses a mock API and is illustrative.

**What to build.** An agent that processes cancellation and refund requests for a mock railway or food-delivery booking API that you write (bookings, fare rules, refund endpoint with idempotency keys). The agent reads the policy, computes the refund, asks for human approval above ₹2,000, and issues the refund. It runs on LangGraph with a Postgres checkpointer or on Temporal.

**Acceptance criteria**
- 40 scripted requests (including ambiguous and policy-edge cases) with expected outcomes; pass^3 ≥ 0.85.
- 200 injected crashes at random steps produce zero duplicate refunds and zero lost requests; every run resumes or ends with a recorded reason.
- 100% of refunds above ₹2,000 wait for approval; a 24-hour approval timeout path is tested with a simulated clock.
- The agent has no credentials beyond the mock API; a permission manifest and threat model are included.
- Traces show every tool call with idempotency keys.

**Stretch goals.** Handle partial refunds with compensation (saga); expose the agent's progress to a small UI.

**What it proves to an employer.** You can build agents that survive crashes, respect money and wait for humans: the properties that let agents run in fintech and operations.

### P3 · A domain agent harness, measured against off-the-shelf agents (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** Anthropic's guidance for long-running agents uses an initializer agent, a progress file and git so each session can continue the work (Nov 2025). Its multi-agent research post reports that token usage explained most of the performance variance on a browsing benchmark (2025). τ-bench introduced pass^k to measure reliability across repeated trials (2024). Teams constantly ask whether to build a custom harness or use Claude Code, Codex CLI or OpenHands. This project answers that question with data for one domain.

**What to build.** A harness for a "data analyst agent" that answers questions over public Indian datasets from data.gov.in. It loads the data into DuckDB or Postgres and runs Python in a sandbox. The harness includes purpose-built tools (schema browser, SQL runner with row limits, sandboxed Python, chart export), a system prompt and project memory file, hooks (block writes, log every query), compaction and a progress file, a research sub-agent, long-term memory of verified dataset facts with provenance, and budgets.

**Acceptance criteria**
- A 40-task suite with programmatic checkers (numeric answers within tolerance, required chart properties), including 10 multi-step tasks needing over 20 tool calls.
- Report pass@1, pass^3, cost per success and median time for your harness and for one off-the-shelf agent (Claude Code, Codex CLI, Gemini CLI or OpenHands) given the same sandbox and data.
- A failure taxonomy of at least 40 failed trajectories and two harness changes justified by it, with before/after numbers.
- Memory improves success on a second batch of 10 related tasks, measured against memory disabled.
- Security: the agent cannot reach the internet except an allow-listed data mirror; a benign canary instruction planted in a dataset description never changes its behaviour across 3 runs.

**Stretch goals.** Expose the tools as an MCP server so the off-the-shelf agent can use them too, and measure again; add trace export with OpenTelemetry GenAI spans.

**What it proves to an employer.** You can design, evaluate and justify an agent harness with evidence. Agent platform teams, AI-native startups and forward-deployed roles hire for exactly this.

## Feeds into

- [AIE401 Multi-Agent Systems, MCP and Orchestration](../../year_4/AIE401_multi_agent_systems_mcp_and_orchestration/README.md): your tools become MCP servers and your agent becomes an orchestrator or worker.
- [AIE404 AI Product Engineering and UX](../../year_4/AIE404_ai_product_engineering_and_ux/README.md): P2's approval flows get a real interface and user testing.
- [AIE501 Frontier Seminar](../../year_5/AIE501_frontier_seminar_long_horizon_autonomous_agents/README.md): long-horizon harness experiments extend P3.
- [OV12 Agent Infrastructure and Platform Engineering](../../../../04_overlaps/OV12_agent_infrastructure_platform/): sandboxes, durable execution and agent reliability at platform scale.

## Sources

- mini-swe-agent README — https://github.com/SWE-agent/mini-swe-agent ; SWE-bench Lite — https://huggingface.co/datasets/princeton-nlp/SWE-bench_Lite (checked 2026-10)
- Razorpay agentic payments (Oct 2025) — https://razorpay.com/newsroom/razorpay-npci-and-openai-come-together-to-launch-agentic-payments-ushering-in-ai-driven-commerce-at-national-scale/ ; Fortune on the July 2025 database deletion — https://fortune.com/2025/07/23/ai-coding-tool-replit-wiped-database-called-it-a-catastrophic-failure/ (checked 2026-10)
- Temporal + OpenAI Agents SDK (GA 23 Mar 2026) — https://temporal.io/blog/announcing-openai-agents-sdk-integration ; LangGraph 1.0 (22 Oct 2025) — https://www.langchain.com/blog/langchain-langgraph-1dot0 (checked 2026-10)
- Anthropic, "Effective harnesses for long-running agents" (Nov 2025) — https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents ; "How we built our multi-agent research system" (Jun 2025) — https://www.anthropic.com/engineering/multi-agent-research-system ; Yao et al., τ-bench (2024) — https://arxiv.org/abs/2406.12045 (checked 2026-10)
- Open Government Data Platform India — https://www.data.gov.in/ (checked 2026-10)
