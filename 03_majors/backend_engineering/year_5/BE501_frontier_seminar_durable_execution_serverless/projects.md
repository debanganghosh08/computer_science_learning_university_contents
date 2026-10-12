# BE501 · Labs and projects

The seminar's labs are short, measured experiments that feed the weekly discussion. Every lab report states the hardware, versions, seeds and variance, and ends with one claim from the week's reading that your results support or contradict. Cloud work fits within free tiers or a small course budget; every lab has a local alternative (Temporal, Restate and DBOS run locally; Workers and Durable Objects have local development servers; WebAssembly runtimes run anywhere).

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Temporal under failure | Run a 5-step workflow with timers and signals; kill workers, the server and the database mid-run; break replay with a non-deterministic call | Recovery timeline for each failure and the replay error you triggered, explained | 5 h |
| 2 · Three engines, one workflow | Implement the same order-fulfilment workflow on Restate, DBOS and one managed engine (Cloudflare Workflows or Lambda durable functions) | Lines of code, p50/p99 step latency, recovery behaviour, and cost per 1M executions for each | 8 h |
| 3 · Serverless cost model | Model one API on Lambda, a container service and a VM at three traffic shapes (spiky, steady, idle) | A cost model with break-even points and the assumptions that move them | 4 h |
| 4 · Cold starts and connections | Measure cold starts with and without SnapStart; reproduce a uniqueness bug from a snapshot; overload Postgres with a burst and fix it | Distributions (not averages), the bug and its fix, and connection counts before and after | 6 h |
| 5 · Edge coordination | A rate limiter and a chat room on Durable Objects; latency measured from at least three regions | Code, latency map, and an explanation of where each object was placed | 5 h |
| 6 · WebAssembly sandbox | A WASI component plugin system with CPU, memory and capability limits; startup and throughput vs a container | Benchmark results and a demonstration that a misbehaving plugin cannot escape its limits | 6 h |
| 7 · CRDTs and sync | A collaborative list with Automerge or Yjs under random partitions; partial sync from Postgres with an authorization rule | Convergence test results over 1,000 random schedules; proof that no unauthorized row reaches a client | 6 h |
| 8 · Durable agent | An agent loop with model and tool calls as activities; kill workers and redeploy mid-run | 100-kill report: runs resumed, zero repeated side effects, budget and step limits enforced | 6 h |
| 9 · Correctness method | Either a seeded simulator that finds a planted bug in a small replicated service, or a TLA+/P model of a retry protocol with a violated safety property | The failing seed or counterexample trace, the fix, and the passing re-run | 6 h |

## Projects

### P1 · Durable execution engine comparison report (L4, ~8 hours)

**Real-world inspiration:** teams choosing between Temporal, Restate, DBOS and managed engines rely on vendor documents that rarely compare like with like. Cloudflare ([Workflows GA](https://blog.cloudflare.com/workflows-ga-production-ready-durable-execution/)) and AWS ([Lambda durable functions](https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html)) each describe their own model.

**What to build:** a public, reproducible comparison of at least three engines on one workload (a payment-and-fulfilment workflow from BE401 with a 24-hour timer and a human approval). It covers guarantees, failure recovery, latency per step, throughput limits, operational burden, workflow versioning, cost and lock-in.

**Acceptance criteria:**
- Every claim in the report is either measured by you (with scripts in the repository) or cited from documentation with the date checked.
- Failure tests cover worker crash, engine or control-plane restart, and a deploy with a changed workflow definition while 100 executions are in flight, for every engine.
- Latency and throughput are reported as distributions over at least three runs, with variance.
- A reviewer runs your scripts and reproduces your headline numbers within 20%.
- The report ends with a decision matrix for three different organizations (startup, regulated fintech, AI-agent platform) and explains why the answer differs.

**Stretch goals:** add a fourth engine; measure the cost of workflow history growth for long-running executions.

**What it proves to an employer:** you can make a platform choice with evidence and explain it to a team, which is architect-level work.

### P2 · Edge-and-serverless redesign of a BE402 service (L4, ~15 hours)

**Real-world inspiration:** the Berkeley view on serverless ([Jonas et al., 2019](https://arxiv.org/abs/1902.03383)) predicted serverless as the default; Prime Video's 2023 move back to containers ([InfoQ](https://www.infoq.com/news/2023/05/prime-ec2-ecs-saves-costs/)) shows where it loses. Durable Objects ([Cloudflare](https://developers.cloudflare.com/durable-objects/)) offer a different model for coordination.

**What to build:** take your BE402 P3 (live-event platform) or BE403 P1 (streaming chat) and redesign part of it on serverless and edge primitives, for example score snapshots and auth at the edge, reactions coordinated by Durable Objects, and background work on a durable engine. Keep the original as the baseline.

**Acceptance criteria:**
- Both versions run the same open-model load test. The report gives p50/p99 latency from at least three regions, error rates and cost per million requests for each.
- A 5× spike in 30 seconds is handled by the redesigned version without errors, or the report explains exactly which limit was hit and why.
- Cold starts, connection limits and consistency trade-offs are measured, not asserted.
- A break-even analysis shows the traffic shape at which each design is cheaper.
- A decision record recommends what to keep from each design, including at least one thing the edge version does worse.

**Stretch goals:** move one component to WebAssembly components; add a multi-region failover test.

**What it proves to an employer:** you can evaluate new platforms against a real system, with numbers, and resist both hype and inertia.

### P3 · Research project: reproduction or extension (L5, portfolio-grade, ~35 hours)

**Real-world inspiration:** systems research advances through reproduction and careful extension. Beldi ([OSDI 2020](https://www.usenix.org/conference/osdi20/presentation/zhang-haoran)), Boki ([SOSP 2021](https://dl.acm.org/doi/10.1145/3477132.3483541)), DBOS ([VLDB 2022](https://www.vldb.org/pvldb/vol15/p21-skiadopoulos.pdf)) and FoundationDB's simulation testing ([SIGMOD 2021](https://www.foundationdb.org/files/fdb-paper.pdf)) all make claims you can test at small scale.

**What to build:** choose one, agreed with the instructor by week 6.

- **Reproduce** a central result from a paper on the reading list at small scale, and explain any differences.
- **Extend** a system. For example:
  - measure the overhead of exactly-once guarantees in a modern durable execution engine against Beldi's reported overheads;
  - add deterministic simulation to an open-source workflow engine's test suite;
  - measure how workflow history size affects recovery time in Temporal or Restate;
  - evaluate the cost of authorization filtering in a sync engine;
  - compare sandbox technologies for agent tool execution on startup, density and escape resistance (defensive testing on your own systems only).
- **Build** a small new system that tests a falsifiable hypothesis about one of the course topics.

**Acceptance criteria:**
- **Proposal:** a two-page proposal (week 6) with a falsifiable question, baseline, metrics, expected result and threats to validity, approved before experiments start.
- **Artifact:** a repository with code, pinned versions, experiment scripts, raw data and a one-command reproduction path. Another student reproduces your main figure within your reported variance.
- **Statistics:** results are reported as distributions with confidence intervals or variance across at least five runs. Negative or null results are reported as such.
- **Paper:** a 6–8 page workshop-style paper (introduction, background, design, evaluation, limitations, related work with every citation checked), plus a 20-minute talk with questions.
- **Honesty:** a limitations section that names at least three threats to validity and what you did about each.

**Stretch goals:** submit to a student workshop or a systems conference's poster track; contribute a fix or benchmark back to the project you studied.

**What it proves to an employer or a research group:** you can produce new, trustworthy knowledge about backend systems. That is the bar for research engineering roles, PhD programmes and the hardest platform teams.

## Feeds into

- [OV12A Running Agents in Production: Sandboxes, Durable Execution and Observability](../../../../04_overlaps/OV12_agent_infrastructure_platform/OV12A_running_agents_in_production_sandboxes_durable/README.md) and [OV12B Agent Evaluation and Reliability Engineering](../../../../04_overlaps/OV12_agent_infrastructure_platform/OV12B_agent_evaluation_and_reliability_engineering/README.md).
- [THS501 Thesis or Capstone I](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) and [THS502](../../../../05_shared_years_3_to_5/THS502_thesis_or_capstone_ii/README.md): P3 is designed to grow into a thesis.
- [RES502 Reading, Reproducing and Extending Papers](../../../../05_shared_years_3_to_5/RES502_reading_reproducing_and_extending_papers/README.md) and [LCH502 Career Launch and Founder Studio](../../../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md).
