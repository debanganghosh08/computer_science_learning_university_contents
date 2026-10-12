# SWE304 · AI-Assisted Software Engineering: Agents in the SDLC

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 6 | 4 (≈ 120 hours) | L2 → L4 | [CS205](../../../../02_year_2_core_computer_science/semester_3/CS205_software_engineering_i_design_testing/README.md), [CS201](../../../../02_year_2_core_computer_science/semester_3/CS201_algorithms_and_complexity/README.md) | [SWE404](../../year_4/SWE404_engineering_leadership_and_technical_strategy/README.md); feeds [SWE402](../../year_4/SWE402_legacy_modernization_and_refactoring_with_ai/README.md) and [SWE501](../../year_5/SWE501_frontier_seminar_agentic_software_engineering/README.md) |

## Why this course matters now

Coding agents are now ordinary tools. In the 2026 Stack Overflow survey, 65.9% of developers use AI coding assistants or agents at work; among agent users, Claude Code (65.5%) and GitHub Copilot (58.7%) lead. The tools read whole repositories, run commands and tests, open pull requests from an issue, review other pull requests, and run on schedules in the cloud: Claude Code runs in the terminal, IDEs, a desktop app, the web and CI; OpenAI Codex has a CLI, IDE extension, cloud tasks, an SDK and a GitHub Action; GitHub's Copilot cloud agent works on one repository per task with a 59-minute session limit; Cursor builds its own Composer models into an agent-first editor. Yet reliability lags capability: METR measured Claude Opus 4.6 at about 12 hours of human-expert work at 50% success but about 70 minutes at 80%, Anthropic estimates about 61% of software requests to Claude succeed, and DORA 2025 found AI adoption still goes with lower delivery stability. CS205 taught you what an agent is and how to delegate one task. This course teaches you to run agents as an engineering system: specification, context, test-first verification, security, review pipelines, parallel work, team policy and honest measurement.

## Learning outcomes

By the end you can:

1. **Explain** how an agent harness works (loop, tools, context management, permissions, sandbox) and **build** a minimal one that resolves real issues.
2. **Engineer** repository context (`AGENTS.md`/`CLAUDE.md` hierarchies, skills, MCP servers, hooks) and **measure** its effect on task success.
3. **Write** specifications, plans and task breakdowns that agents execute correctly, using spec-driven tooling (GitHub Spec Kit, Kiro) and EARS-style requirements.
4. **Run** test-first loops where agents cannot weaken the tests, and **check** agent-written tests with mutation testing and property-based oracles.
5. **Design** a review pipeline for agent pull requests (evidence requirements, AI reviewers, SAST, human approval) and **measure** its catch rate.
6. **Secure** agent workflows against prompt injection, secret leakage, package hallucination and over-broad permissions.
7. **Orchestrate** parallel agents with worktrees and subagents, and **decide** when parallelism costs more than it saves.
8. **Measure** productivity and quality effects of AI tools on a team with a defensible design, and **critique** published studies.
9. **Write** a team AI policy covering data, licensing, ownership, review, onboarding and interviews.

## Chapters and lessons

### Chapter 1 · The 2026 tool landscape (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Kinds of tools | Completion, chat, local agents (Claude Code, Codex CLI, Copilot CLI, Gemini CLI), cloud/background agents (Claude Code on the web, Codex cloud, Copilot cloud agent), AI code review, agent-first editors (Cursor) | Map 8 tools onto these categories from their official docs; note each one's limits |
| 1.2 What changes and what lasts | Models change every few months; the loop, context, verification and permissions do not | Diff two model generations on the same 5 tasks; separate model effects from workflow effects |
| 1.3 Adoption and trust data | Stack Overflow 2026 (65.9% use at work; 6.6% trust for important decisions); DORA 2025 (90% use; "amplifier") | Survey 20 engineers you know with 5 questions; compare with the published data |
| 1.4 Capability vs reliability | METR time horizons at 50% and 80%; benchmark contamination (OpenAI dropped SWE-bench Verified in Feb 2026) | Estimate which of your last 10 tasks fall inside an 80%-reliability horizon |

**Check your understanding:** Why does an agent that succeeds 50% of the time on 12-hour tasks still need close supervision on 2-hour tasks? Which tool category fits an overnight dependency upgrade, and which fits exploratory debugging? What would make a benchmark score irrelevant to your codebase?

### Chapter 2 · Inside an agent harness (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 The loop | Model call → tool call → observation → repeat; stop conditions; step and cost budgets | Trace one agent session; label every step as explore, edit, verify or wasted |
| 2.2 Agent-computer interfaces | SWE-agent's finding that interface design (file viewer, search, edit commands) changes success rates; Agentless's fixed localise–repair–validate pipeline as the contrast | Run mini-SWE-agent and an Agentless-style script on the same 10 issues |
| 2.3 Context management | Compaction, subagents with fresh context, scratch files, retrieval by grep vs embeddings | Make a session exceed its context; compare outcomes with and without subagents |
| 2.4 Permissions and sandboxes | Allow/deny lists, approval modes, containers, network egress rules | Configure an agent that can run tests but cannot reach the internet or write outside the repo |
| 2.5 Build a minimal harness | A 200-line agent with read, search, edit and run-tests tools | Resolve 5 seeded issues in a toy repo; log success and cost |

**Check your understanding:** Why can a simpler fixed pipeline beat a free-form agent on some benchmarks? What information is lost when a harness compacts context? Which permission would you never grant an unattended agent, and why?

### Chapter 3 · Context engineering for codebases (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Context files that work | Hierarchical `AGENTS.md`/`CLAUDE.md`; build/test commands, conventions, module map, "never do" rules; keeping them short and current | Rewrite a bloated 600-line context file into 80 lines; measure task success before and after |
| 3.2 Skills and reusable workflows | Packaging repeatable procedures (review, release, migration) as skills or commands | Write a `/review-pr` skill with an evidence checklist |
| 3.3 Hooks | Running formatters, linters, boundary tests and secret scanners automatically before or after agent actions | Add hooks that block commits failing lint or touching protected paths |
| 3.4 Tools via MCP | Model Context Protocol servers for issue trackers, docs and databases; read-only by default | Connect a read-only issue-tracker MCP server; restrict its scopes |
| 3.5 Measuring context | A fixed task set replayed with context variants; success, steps, cost | Ablation: no context file, full file, module map only |

**Check your understanding:** Why does a longer context file often make results worse? Which rules belong in a hook instead of prose? What makes an MCP server a security boundary?

### Chapter 4 · Specification-driven development (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Spec → plan → tasks | GitHub Spec Kit's flow; Kiro's requirements, design and tasks documents | Take one feature through Spec Kit end to end |
| 4.2 Requirements agents can execute | EARS patterns ("When <trigger>, the <system> shall <response>"); explicit non-goals; examples as specs | Rewrite 10 vague tickets in EARS form; check each has a test |
| 4.3 Sizing tasks | Agent-sized tasks (minutes to a couple of hours of human work); dependency ordering; checkpoints | Split a 3-day feature into tasks; predict which will fail and why |
| 4.4 Design docs as agent input | Which design decisions the human must make first (data model, boundaries, failure handling) | Same feature with and without a 1-page design; compare diffs |

**Check your understanding:** Why does an agent need explicit non-goals? What is the cost of tasks that are too small? Which decisions in a spec should never be left for the agent to make?

### Chapter 5 · Test-first prompting and verification loops (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Tests as the contract | Write acceptance tests first; the agent's job is to make them pass without touching them | Protect `tests/` with permissions and a hook; run a feature through it |
| 5.2 Reward hacking | Agents special-casing tests, weakening assertions or skipping tests to "pass"; METR's 2025 reports of reward hacking by frontier models | Seed a hard task; catch and document any test tampering in the diff |
| 5.3 Oracles beyond examples | Property-based tests (Hypothesis, fast-check, jqwik); differential testing against a reference | Add 3 properties that catch a bug the example tests missed |
| 5.4 Testing the tests | Mutation testing on agent-written tests; Meta's TestGen-LLM filters (builds, passes reliably, increases coverage) and mutation-guided generation (ACH) | Raise the mutation score of agent-written tests from baseline to ≥ 70% |

**Check your understanding:** Why is "all tests pass" weak evidence when the same agent wrote code and tests? How do you detect an assertion that was quietly weakened? What does a surviving mutant tell you about an agent's tests?

### Chapter 6 · Review pipelines for agent pull requests (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Evidence requirements | PR template: spec link, test diff, run output, screenshots/traces, risk notes; size limits | Enforce the template with a CI check |
| 6.2 Automated gates | Lint, type-check, SAST (Semgrep, CodeQL), secret scanning, dependency allow-lists | Build the gate chain; plant one issue per gate and confirm each blocks |
| 6.3 AI reviewers | Copilot code review, Claude Code's GitHub code review, Codex code review: configuration, noise, false positives | Run two AI reviewers on 20 PRs; measure precision and recall against a key |
| 6.4 Human review at volume | Reviewer fatigue; risk-based routing; who may approve agent PRs (reading craft is in [SWE302](../SWE302_low_level_design_and_clean_code_at_scale/README.md)) | Design routing rules: which PRs need a senior, which need a second human |

**Check your understanding:** If an AI reviewer has high recall but low precision, how do you deploy it? Which defects will never be caught by gates and must be caught by a human? Why does reviewer fatigue grow faster than PR count?

### Chapter 7 · Security of AI-generated code and of agents (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 What studies found | Pearce et al. (2021): about 40% of 1,689 Copilot-generated programs vulnerable; Perry et al. (2022/CCS 2023): assistant users wrote less secure code and were more confident in it; Veracode (2025): flaws in 45% of cases | Generate code for 10 CWE-prone tasks; scan with CodeQL; triage by hand |
| 7.2 Package hallucination | Spracklen et al. (USENIX Security 2025): at least 5.2% (commercial) and 21.7% (open models) hallucinated packages; "slopsquatting" | Write a CI check that every new dependency exists, is old enough and is on an allow-list |
| 7.3 Prompt injection against agents | Indirect injection through issues, READMEs, web pages, tool output (OWASP Top 10 for LLM Applications: LLM01) — defences only | Threat-model your agent: list every untrusted input it reads and what it could do next |
| 7.4 Containment | Least-privilege tokens, sandboxed execution, egress allow-lists, human approval for irreversible actions, audit logs | Harden the Chapter 2 harness; red-team it with a planted malicious issue in a sandbox |
| 7.5 Secrets and data | Keeping secrets out of context; enterprise data controls; personal data under India's DPDP Act 2023 | Scan agent transcripts for secrets; write a data-handling rule |

**Check your understanding:** Why are assistant users more confident in less secure code, and what process counteracts it? What can an agent with shell access and network egress do after reading a poisoned issue? Why must dependency checks run in CI rather than rely on the developer?

### Chapter 8 · Agents across the lifecycle (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Triage and reproduction | Agents that label issues, reproduce bugs as failing tests, and propose minimal fixes | Agent turns 10 bug reports into failing tests; you grade them |
| 8.2 Headless agents in CI | Claude Code GitHub Actions, Codex GitHub Action, Copilot cloud agent assigned from issues; budgets and timeouts | Agent that proposes a fix PR when nightly tests fail, with a cost cap |
| 8.3 Maintenance work | Dependency upgrades, flaky-test fixes, docs sync, release notes; scheduled routines | Weekly dependency-upgrade routine with a test gate |
| 8.4 Where agents should not act alone | Schema migrations, auth changes, payments, production access | Write the "human required" list for a fintech repo, with reasons |

**Check your understanding:** Why is "reproduce as a failing test" the most valuable first step for a bug-fixing agent? What should a CI agent do when it cannot fix the failure? Which repository areas would you block from unattended agents?

### Chapter 9 · Parallel and multi-agent workflows (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Isolation | Git worktrees or cloud sandboxes per task; independent branches | Run 4 agents on 4 issues in parallel worktrees |
| 9.2 Coordination | Lead agent with subagents; shared plan files; merge order | One lead agent splits a feature into 3 subagent tasks; you merge |
| 9.3 Conflicts and integration | Semantic conflicts that merge cleanly; integration tests after each merge | Plant a semantic conflict; see whether CI catches it |
| 9.4 The cost of parallelism | Review becomes the bottleneck; token cost; context duplication | Measure wall-clock, review time and cost for 1 vs 4 parallel agents |

**Check your understanding:** Why can four parallel agents finish slower than one? What is a semantic merge conflict and why do tests sometimes miss it? Who owns the integration when agents work in parallel?

### Chapter 10 · Measuring real productivity (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Reading the studies | Copilot RCT (Peng et al., 2023), Google enterprise RCT (Paradis et al., 2024), field experiments (+26% PRs), METR RCT (−19% for experts in mature repos), METR's 2026 selection-effect problem, DORA's throughput-vs-stability finding | One-page critique of each: population, task, measure, threats to validity |
| 10.2 The perception gap | METR developers predicted +24%, believed +20%, measured −19% | Log your own predicted vs actual time for 15 tasks |
| 10.3 Team metrics that mean something | DORA metrics, SPACE, review time, rework rate, change failure rate, escaped defects; why "share of code written by AI" has no standard definition | Build a dashboard from a team repo's PR and deploy data |
| 10.4 Designing an evaluation | Matched tasks, randomisation, crossover designs, interrupted time series; replaying past issues SWE-bench-style | Write and pilot a 4-week evaluation plan for a 10-person team |

**Check your understanding:** Why might less experienced developers gain more in some studies and experts lose time in others? What would make you distrust a "40% faster" claim from your own team? Why is change failure rate a necessary companion to throughput?

### Chapter 11 · Team workflows and policy (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 A clear AI stance | DORA's AI Capabilities Model: clear and communicated AI stance, healthy data ecosystems, AI-accessible internal data, strong version control, small batches, user-centric focus, quality internal platforms | Score a team (yours or an open-source project) on the seven capabilities |
| 11.2 Ownership and licensing | "The person who merges owns it"; code provenance and duplicate-detection filters; open-source licence obligations | Draft ownership and provenance rules |
| 11.3 Growing junior engineers | Learning penalties under heavy AI reliance (Shen and Tamkin, cited in AI Index 2026); fewer mentoring conversations (Anthropic internal survey, Dec 2025) | Design an onboarding plan with AI-off weeks and paired reviews |
| 11.4 Writing the policy | Allowed tools and data, approval rules, security controls, measurement, review cadence | Write a 2-page AI engineering policy for a 30-person startup |

**Check your understanding:** Why does DORA put "small batches" and "version control" in an AI capability model? How can a team use agents heavily and still grow juniors? Which policy clause would you enforce in tooling rather than on paper?

### Chapter 12 · Your own agent workflow, evaluated (weeks 12–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Custom agents | Agent SDKs, custom subagents, skills and MCP tools for internal systems | Build a project-specific "bug reproducer" agent |
| 12.2 A private benchmark | Mining your repo's closed issues with tests into a replayable task set | Build 20 tasks with hidden tests from a real repo's history |
| 12.3 Running and reporting | Success rate with confidence intervals, cost, time, failure taxonomy | Evaluate 2 workflows on your benchmark |
| 12.4 Presenting to leadership | What the numbers do and do not justify | 10-minute P3 presentation with a recommendation |

**Check your understanding:** Why is a benchmark built from your own repository more useful to your team than SWE-bench, and what is its main risk? How many tasks do you need before a 10-point difference means anything? What would make you recommend against wider agent use?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Tool map and model diff | — |
| 2 | 2 | Lab 2 · Build a minimal harness | — |
| 3 | 3 | Lab 3 · Context ablation | **P1 due** |
| 4 | 4 | Lab 4 · Spec Kit end to end | — |
| 5 | 5 | Lab 5 · Tests the agent cannot touch | — |
| 6 | 6 | Lab 6 · Review pipeline | — |
| 7 | 7 | Lab 7 · Agent security (sandboxed) | Mid-term (AI off): spec, review and threat model |
| 8 | 8 | Lab 8 · CI agent with a budget | — |
| 9 | 9 | Lab 9 · Parallel agents | — |
| 10 | 10 | Lab 10 · Evaluation design | **P2 due** |
| 11 | 11 | Policy workshop | Team AI policy |
| 12 | 12 | Private benchmark | — |
| 13 | 12 | P3 runs | — |
| 14 | 12 | P3 report | **P3 due** |
| 15 | Review | Presentation | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** everything the labs ask, deliberately, with logs. This course is about using agents well, so you will use Claude Code, Codex, Copilot, Cursor and at least one open-source harness (mini-SWE-agent, OpenHands or Aider) and compare them.
- **Do without AI (drills):** writing specifications and acceptance tests for the first feature in each lab; threat models; reviewing a PR fully before any AI reviewer runs; the mid-term and final (spec writing, diff review, policy reasoning). The skill being trained is judgement about agent output, which you cannot outsource to the agent.
- **Verify AI output by:** protected tests written before the code; mutation testing; property-based and differential oracles; SAST, secret scanning and dependency checks in CI; running the change; reading the whole diff; comparing every claimed tool feature with the official docs on the date you use it.
- **Where AI still fails here (show it):** each lab has a failure log. You will record test tampering (Lab 5), invented APIs or packages (Lab 6–7), unsafe actions after reading untrusted input (Lab 7, sandboxed), semantic merge conflicts (Lab 9), and the gap between your predicted and measured time (Chapter 10). The final report classifies your failures; you are graded on the quality of evidence.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) with failure logs | 20% |
| P1, P2, P3 | 10%, 20%, 25% |
| Mid-term (AI off) | 5% |
| Final exam (AI off) + P3 presentation | 20% |

**Mastery gate.** You pass when you can: (1) set up an agent workflow on an unfamiliar repository in half a day (context file, hooks, protected tests, sandbox, CI gates) and ship 5 agent-assisted changes that pass review by a senior engineer with no security findings; (2) with AI off, review an agent PR with planted test tampering, a hallucinated dependency and an injection-driven change, and find all three within 45 minutes; (3) present an evaluation of two workflows on at least 20 tasks with confidence intervals and a recommendation a sceptical reviewer accepts.

## Industry reality

Where this is used (public sources): Google reported that 80% of code modifications in one large migration were AI-authored, with an estimated 50% time saving ([Nikolov et al., 2025](https://arxiv.org/abs/2501.06972)). Meta deployed LLM test generation with automatic filters: 75% of generated test cases built, 57% passed reliably, 25% increased coverage, and 73% of recommendations were accepted ([Alshahwan et al., FSE 2024](https://arxiv.org/abs/2402.09171)). Canva runs an AI-assisted coding interview that asks whether candidates can "identify and fix issues in AI-generated code" ([Canva, 2025](https://www.canva.dev/blog/engineering/yes-you-can-use-ai-in-our-interviews/)). Anthropic's own engineers reported using Claude in about 60% of their work in an August 2025 survey ([Anthropic, Dec 2025](https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic)).

**Interview questions from this course**

1. *You may use any AI tool. Add this feature to this unfamiliar repo in 45 minutes.* Strong answer (behaviour): reads the code and tests first, writes or asks for a failing test, gives the agent a narrow task, reviews every line, runs tests, explains what the agent got wrong and why the result is correct.
2. *How do you stop an agent from passing tests by changing them?* Strong answer: tests written first and write-protected (permissions plus hooks), CI check on test-file diffs, mutation testing, review that reads test diffs first.
3. *Your CTO wants to know whether AI tools are paying off. What do you measure?* Strong answer: DORA metrics plus review time, rework and escaped defects; a controlled comparison or interrupted time series; warns against "percentage of code by AI"; cites the METR perception gap.
4. *What are the security risks of giving an agent access to your repo and CI?* Strong answer: prompt injection from untrusted content, secret exposure, hallucinated dependencies, over-broad tokens, destructive commands; mitigations: sandbox, least privilege, egress allow-lists, approval gates, audit logs, SAST and dependency checks.
5. *How would you write a spec for an agent to implement a refund API?* Strong answer: EARS-style requirements, explicit non-goals, idempotency and failure cases, data model decided by a human, acceptance tests, task breakdown with checkpoints.

## Resources (free first)

- **Tool documentation:** Claude Code — https://code.claude.com/docs/en/overview ; OpenAI Codex — https://developers.openai.com/codex ; GitHub Copilot — https://docs.github.com/en/copilot ; Cursor — https://cursor.com/docs ; Gemini CLI — https://github.com/google-gemini/gemini-cli
- **Open-source harnesses:** SWE-agent and mini-SWE-agent — https://github.com/SWE-agent ; OpenHands — https://github.com/OpenHands/OpenHands ; Aider — https://aider.chat/
- **Specs and context:** GitHub Spec Kit — https://github.com/github/spec-kit ; Kiro — https://kiro.dev/ ; AGENTS.md — https://agents.md/ ; Model Context Protocol — https://modelcontextprotocol.io/
- **Engineering guides:** Anthropic, "Building effective agents" (Dec 2024) — https://www.anthropic.com/engineering/building-effective-agents ; Anthropic, "Effective context engineering for AI agents" (2025) — https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- **Security:** OWASP Top 10 for LLM Applications — https://genai.owasp.org/llm-top-10/ ; Semgrep — https://semgrep.dev/docs/ ; CodeQL — https://codeql.github.com/
- **Research:** Yang et al., SWE-agent (2024) — https://arxiv.org/abs/2405.15793 ; Xia et al., Agentless (2024) — https://arxiv.org/abs/2407.01489 ; METR research — https://metr.org/ ; DORA — https://dora.dev/
- **Testing tools:** Hypothesis — https://hypothesis.readthedocs.io/ ; PIT — https://pitest.org/ ; Stryker — https://stryker-mutator.io/ ; mutmut — https://github.com/boxed/mutmut

## Sources

- Stack Overflow, 2026 Developer Survey: AI (6 Oct 2026) — https://survey.stackoverflow.co/2026/ai/data (checked 2026-10)
- METR, data file v1.1 — https://metr.org/assets/benchmark_results_1_1.yaml ; RCT (10 Jul 2025) — https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ ; update (24 Feb 2026) — https://metr.org/blog/2026-02-24-uplift-update/ ; "Recent frontier models are reward hacking" (Jun 2025) — https://metr.org/blog/2025-06-05-recent-reward-hacking/ (checked 2026-10)
- Anthropic Economic Index, Jan 2026 — https://www.anthropic.com/research/anthropic-economic-index-january-2026-report ; "How AI is transforming work at Anthropic" (2 Dec 2025) — https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic (checked 2026-10)
- Google Cloud, DORA 2025 report announcement (24 Sep 2025) and AI Capabilities Model (24 Sep 2025) — https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report , https://cloud.google.com/blog/products/ai-machine-learning/introducing-doras-inaugural-ai-capabilities-model (checked 2026-10)
- OpenAI, "Why we no longer evaluate SWE-bench Verified" (23 Feb 2026) — https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/ (checked 2026-10)
- GitHub Docs, "About Copilot cloud agent" (59-minute session limit; one repository per task) — https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent (checked 2026-10)
- Claude Code overview (surfaces, subagents, hooks, skills, MCP, GitHub Actions, routines) — https://code.claude.com/docs/en/overview ; OpenAI Codex docs (CLI, IDE, cloud, SDK, GitHub Action, AGENTS.md, sandboxing) — https://developers.openai.com/codex ; Cursor docs (Agent, Plan Mode, Composer models) — https://cursor.com/docs (all checked 2026-10)
- Pearce et al., "Asleep at the Keyboard?" (arXiv 2108.09293; IEEE S&P 2022) — https://arxiv.org/abs/2108.09293 ; Perry et al., "Do Users Write More Insecure Code with AI Assistants?" (arXiv 2211.03622; CCS 2023) — https://arxiv.org/abs/2211.03622 (checked 2026-10)
- Veracode 2025 GenAI Code Security Report press release (30 Jul 2025) — https://www.veracode.com/press-release/ai-generated-code-poses-major-security-risks-in-nearly-half-of-all-development-tasks-veracode-research-reveals/ ; Spracklen et al., USENIX Security 2025 — https://www.usenix.org/conference/usenixsecurity25/presentation/spracklen (checked 2026-10)
- Alshahwan et al., "Automated Unit Test Improvement using LLMs at Meta" (arXiv 2402.09171) — https://arxiv.org/abs/2402.09171 ; Foster et al., "Mutation-Guided LLM-based Test Generation at Meta" (arXiv 2501.12862) — https://arxiv.org/abs/2501.12862 (checked 2026-10)
- Peng et al. (arXiv 2302.06590) — https://arxiv.org/abs/2302.06590 ; Paradis et al. (arXiv 2410.12944) — https://arxiv.org/abs/2410.12944 ; Stanford HAI AI Index 2026 — https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf (checked 2026-10)

_Last reviewed: 2026-10_
