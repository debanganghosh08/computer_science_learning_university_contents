# SWE304 · Labs and projects

Every lab keeps an **agent log**: the prompt or task, the agent and model version, time, cost, the diff, what you rejected and why. Security exercises (Lab 7) run only in a disposable sandbox with no real credentials and no network access beyond an allow-list; they test defences, never real systems. Use at least two commercial agents and one open-source harness across the semester so that conclusions are not about one product.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Tool map and model diff | Categorise 8 tools from their docs; run two model generations on the same 5 tasks | Category table with limits and sources; per-task outcomes and what changed | 3 h |
| 2 · Build a minimal harness | A ≤ 250-line agent (read, search, edit, run tests) on a toy repo with 10 seeded issues; compare with mini-SWE-agent | Code, success rate, steps and cost per issue, and 3 failure transcripts explained | 6 h |
| 3 · Context ablation | Replay 15 tasks on a real open-source repo under 4 context conditions (none, bloated file, concise file, concise file + module map) | Success, steps, cost and review defects per condition, with the raw logs | 5 h |
| 4 · Spec Kit end to end | One feature through specification, plan and tasks with GitHub Spec Kit (or Kiro) | Spec, plan, tasks, the merged PR, and the list of spec gaps the agent exposed | 4 h |
| 5 · Tests the agent cannot touch | Acceptance tests written first; `tests/` write-protected by permissions and a hook; CI fails on any test-file change in agent PRs | Hook config, one blocked tampering attempt (or evidence none occurred), mutation score of agent-added tests before and after your fixes | 5 h |
| 6 · Review pipeline | PR template check, lint, types, Semgrep/CodeQL, secret scan, dependency allow-list, two AI reviewers | 20 PRs with planted issues: catch rate per gate and per reviewer; false-positive rate | 6 h |
| 7 · Agent security (sandboxed) | Threat-model a harness; plant an injected instruction in an issue in a sandbox repo; apply containment (least privilege, egress allow-list, approvals) | Threat model, before/after behaviour logs, and the controls that stopped the action | 5 h |
| 8 · CI agent with a budget | Agent triggered by a failing nightly test proposes a fix PR, with step, time and cost caps | 5 runs on planted failures: fixes proposed, correct, and cost per run | 4 h |
| 9 · Parallel agents | 4 issues in parallel worktrees vs sequentially; one planted semantic conflict | Wall-clock, your review time, cost, and whether CI caught the conflict | 4 h |
| 10 · Evaluation design | A 4-week evaluation plan for a 10-person team; pilot it on yourself with 12 matched tasks | Plan (design, metrics, threats to validity), pilot data with intervals | 4 h |

## Projects

### P1 · Agent-ready repository (L1, ~6 hours)

**Real-world inspiration:** open-source maintainers adding `AGENTS.md` files and contribution rules for AI-generated PRs; teams preparing a codebase before rolling out agents.

**What to build:** take a real open-source repository you can build locally (10k–50k lines). Add a concise context file (build, test, conventions, module map, forbidden actions), two skills or commands (for example "reproduce a bug as a failing test" and "prepare a PR"), hooks for format/lint/test, and a PR template for AI-assisted contributions. Then run 5 real "good first issues" through an agent.

**Acceptance criteria:**
- Context file ≤ 120 lines; every command in it runs successfully on a clean checkout (CI job proves it).
- At least 4 of 5 issues produce a PR that passes CI and that you would approve after review; the agent log explains every rejection.
- Hooks block a commit with a lint error and a commit touching a protected path (demonstrated).
- A before/after comparison on the same 5 issues without the context file and skills (success and steps).

**Stretch goals:** upstream the context file to the project; add an MCP server for the project's docs.

**What it proves to an employer:** you can make a codebase work well with agents, which many teams are trying to do right now.

### P2 · Verified feature delivery with an agent (L2, ~15 hours)

**Real-world inspiration:** regulated domains where every change needs evidence, such as fintech in India under RBI oversight or healthcare apps handling personal data under the DPDP Act 2023. The product is an **illustrative scenario**.

**What to build:** a "refunds" feature for an existing payments-style sample service (create refund, partial refunds, idempotency keys, webhook notifications, reconciliation report). You write the spec (EARS requirements, non-goals, failure cases), the data model and the acceptance tests; agents implement in tasks of ≤ 2 hours each through your review pipeline.

**Acceptance criteria:**
- Acceptance tests written before any implementation (commit history proves order) and never modified by an agent (CI check).
- Idempotency: 10,000 randomised retry sequences (property-based) never create a duplicate refund or a refund exceeding the captured amount.
- Mutation score ≥ 70% on the refunds module.
- Zero high-severity findings from CodeQL or Semgrep; every new dependency passes the allow-list check.
- Every agent PR carries the evidence template; median review time and rework count are reported.
- A written retrospective: which spec gaps caused agent mistakes, and the spec changes that fixed them.

**Stretch goals:** a second agent in a different tool implements the same spec; compare defects found in review.

**What it proves to an employer:** you can deliver correct, secure features at agent speed without lowering the bar, and you can show the evidence.

### P3 · Private benchmark and workflow evaluation (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** SWE-bench builds tasks from real GitHub issues with hidden tests; companies now build private versions from their own history to decide which tools and workflows to adopt, because public benchmarks can be contaminated (OpenAI stopped reporting SWE-bench Verified in February 2026).

**What to build:** from one active open-source repository, mine at least 25 closed issues whose fixing PRs added tests. Package each as a task (repo snapshot, issue text, hidden tests). Build a runner that executes an agent workflow in a sandbox and scores it. Evaluate two workflows (for example: commercial agent with your P1 context setup vs open-source harness with a fixed pipeline), three runs each.

**Acceptance criteria:**
- Task set reproducible from one script; each task's hidden tests fail on the pre-fix snapshot and pass on the real fix (validated automatically).
- Runner isolates each task (container), enforces time and cost caps, and records full transcripts.
- Report: success rate with 95% confidence intervals, cost and time per task, a failure taxonomy (localisation, wrong fix, test tampering, environment, timeout) with counts, and run-to-run variance.
- At least 3 tasks where the agent's patch passes the hidden tests but is still wrong (you show why), or a justified statement that none occurred after checking every passing patch.
- A 2-page recommendation to an imaginary engineering lead, stating what the evidence does and does not support.

**Stretch goals:** check for contamination by testing whether models reproduce the original fix verbatim; publish the task set if the repository's licence allows.

**What it proves to an employer:** you can evaluate AI tooling rigorously, which developer-productivity, platform and AI-tooling teams hire for.

## Feeds into

- [SWE404 Engineering Leadership and Technical Strategy](../../year_4/SWE404_engineering_leadership_and_technical_strategy/README.md): the Chapter 11 policy and P3 evaluation become inputs to managing AI-augmented teams.
- [SWE402 Legacy Modernization and Refactoring with AI](../../year_4/SWE402_legacy_modernization_and_refactoring_with_ai/README.md): verification loops from P2 at migration scale.
- [SWE501 Frontier Seminar](../../year_5/SWE501_frontier_seminar_agentic_software_engineering/README.md): P3's benchmark method is the starting point for research.
- [OV12 Agent Infrastructure and Platform Engineering](../../../../04_overlaps/OV12_agent_infrastructure_platform/README.md): running agents for a whole organisation.
- [SWE flagship industry project](../../../../06_career_and_market_readiness/05_industry_projects/SWE_software_engineering.md): its agent workflow comes from P1 and P2.
