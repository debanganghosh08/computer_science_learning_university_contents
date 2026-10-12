# BE501 · Frontier Seminar: Durable Execution, Serverless and Edge Backends

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 5 · 9 | 4 (≈ 120 hours) | L4 → L5 | [BE401](../../year_4/BE401_payments_grade_systems_transactions_idempotency/README.md), [BE403](../../year_4/BE403_backends_for_ai_serving_llm_features_vector/README.md) | [OV12A](../../../../04_overlaps/OV12_agent_infrastructure_platform/OV12A_running_agents_in_production_sandboxes_durable/README.md), [OV12B](../../../../04_overlaps/OV12_agent_infrastructure_platform/OV12B_agent_evaluation_and_reliability_engineering/README.md), [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) |

Part of the [Backend Engineering major](../../README.md). Taken alongside [RES501 Research Methods](../../../../05_shared_years_3_to_5/RES501_research_methods_and_scientific_writing/README.md) and [RES502 Reading, Reproducing and Extending Papers](../../../../05_shared_years_3_to_5/RES502_reading_reproducing_and_extending_papers/README.md). This is a seminar. Each week you read papers and engineering write-ups, one student presents and leads the critique, and everyone builds or measures something small. The semester ends with a reproduction or extension that could become a thesis ([THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md)).

## Why this course matters now

Backend platforms are absorbing work that engineers used to hand-write. Durable execution engines now persist every step of a workflow and replay it after a crash:
- Temporal and Restate are open-source servers. DBOS is a library that checkpoints into PostgreSQL.
- Cloudflare Workflows has been generally available since April 2025.
- AWS Lambda durable functions (announced December 2025) let a function run for up to a year through checkpoint and replay.
- Temporal's integration with the OpenAI Agents SDK became generally available in March 2026.

AI agents are long-running, failure-prone programs with side effects, which is exactly the workload these engines were built for. Elsewhere, WebAssembly's WASI 0.3 was ratified in June 2026 with native async. Akamai acquired Fermyon, the company behind the Spin WebAssembly framework, at the end of 2025. Sync engines for local-first apps reached 1.0: ElectricSQL in March 2025 and Zero in June 2026. Hype and genuine progress are mixed together in this area. The skill this seminar builds is telling them apart with evidence: reading the paper, measuring the system and reproducing the claim.

## Learning outcomes

By the end you can:

1. **Explain** how durable execution works (event histories, deterministic replay, activities, timers, signals, checkpoints), and **compare** Temporal, Restate, DBOS, Cloudflare Workflows and Lambda durable functions on guarantees, failure behaviour, cost and operations.
2. **Analyse** research systems for exactly-once workflows on serverless platforms (Beldi, Boki, DBOS), and **reproduce** a key result at small scale.
3. **Evaluate** serverless and edge platforms (cold starts, isolates vs microVMs, SnapStart, Durable Objects, connection limits, pricing) for a stated workload, with measurements.
4. **Build** server-side WebAssembly components with WASI and **assess** them for plugin sandboxing and agent tool isolation.
5. **Design** a backend for local-first and sync-engine applications: partial replication, authorization of sync and conflict resolution.
6. **Architect** agent infrastructure: durable agent loops, sandboxes, stateless MCP servers at scale, idempotent tools, approvals and budgets.
7. **Apply** frontier correctness techniques (deterministic simulation testing, TLA+ or P models, property-based testing) to a backend design.
8. **Critique** a paper or vendor claim in writing, separating measured results from marketing, and **write** a research-grade report of your own reproduction or extension.

## Chapters and lessons

### Chapter 1 · How to read the frontier (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Reading systems papers | Problem, assumptions, design, evaluation, threats to validity; the three-pass method (see RES502) | Write a one-page critique of a short systems paper |
| 1.2 Reading vendor claims | Benchmarks without baselines, cherry-picked workloads, "up to" numbers, survivorship in case studies | Annotate a vendor benchmark post with the questions it doesn't answer |
| 1.3 Reproducibility | Artifacts, versions, hardware, seeds, variance, reporting distributions | Re-run a published microbenchmark and report variance honestly |
| 1.4 Choosing a research question | Gaps between papers and practice, scoping to one semester, falsifiable claims | Draft three candidate questions and rank them by feasibility and interest |

**Check your understanding:** (1) What makes a benchmark claim reproducible? (2) Why can a paper's evaluation be correct and still not apply to your workload? (3) What should you look for first in a vendor case study?

### Chapter 2 · Durable execution: engines (weeks 2–3)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Workflows as code | Event history, deterministic replay, activities vs workflow code, timers, signals, queries; why non-determinism breaks replay | Write a workflow, then break replay with a non-deterministic call and read the error |
| 2.2 Temporal | History, matching and frontend services, task queues, workflow versioning and patching, continue-as-new | Run a Temporal server locally; kill workers and the server mid-workflow |
| 2.3 Restate and DBOS | Restate's log-based design and virtual objects; DBOS as a library checkpointing into Postgres | Implement the same 5-step workflow on Restate and DBOS |
| 2.4 Managed engines | Cloudflare Workflows (GA April 2025), AWS Lambda durable functions (checkpoint and replay, up to one year), Azure Durable Functions | Port the workflow to one managed engine; compare code and failure handling |
| 2.5 Choosing and versioning | Long-running workflow upgrades, migrations of in-flight executions, cost per step, vendor lock-in | Upgrade a workflow definition while 1,000 executions are in flight |

**Check your understanding:** (1) Why must workflow code be deterministic but activity code need not be? (2) What does a durable execution engine guarantee about an activity that sends an email, and what must you still add? (3) What is the hardest operational problem with workflows that run for months?

### Chapter 3 · Durable execution: research (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Beldi (OSDI 2020) | Exactly-once semantics and transactions for serverless functions over a database, using linked logs | Present Beldi's design and its overhead measurements |
| 3.2 Boki (SOSP 2021) | Shared logs as the foundation for stateful serverless functions | Compare Boki's log abstraction with Kafka and with Restate's log |
| 3.3 DBOS (VLDB 2022) | Building operating-system services on a distributed DBMS; from research to a durable execution library | Trace how DBOS's research idea became its production library |
| 3.4 From papers to products | What changed between research prototypes and production engines: APIs, operations, pricing, and the guarantees that were weakened or dropped | Compare one paper's guarantees with a production engine's documentation, claim by claim |

**Check your understanding:** (1) What problem do Beldi and Boki solve that a plain function platform does not? (2) What does putting state in a database buy, and what does it cost in latency? (3) Which assumptions in these papers fail in a multi-region deployment?

### Chapter 4 · Serverless backends (weeks 5–6)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 The serverless model | The Berkeley view (2019): promise and limitations; pricing by request and duration | Model the monthly cost of one API on Lambda vs containers at three traffic levels |
| 4.2 Isolation and cold starts | Firecracker microVMs (NSDI 2020); SnapStart snapshots (Java, Python 3.12+, .NET 8+) and their uniqueness caveats; provisioned concurrency | Measure cold starts with and without SnapStart; break uniqueness and fix it |
| 4.3 State and connections | Connection limits to relational databases, proxies, HTTP-based database drivers; idempotent event handlers | Overload a database with a function burst; fix it with a proxy and concurrency limits |
| 4.4 Streaming and long work | Response streaming, step-based orchestration vs durable functions | Stream an LLM response from a function and measure time to first byte |
| 4.5 When serverless loses | High steady load, chatty orchestration, state transitions as cost (Prime Video, 2023) | Find the break-even traffic level for your workload |

**Check your understanding:** (1) Why can a snapshot-restored function produce duplicate "random" IDs? (2) At what traffic shape does serverless stop being cheaper? (3) Why do serverless functions and relational databases fight over connections?

### Chapter 5 · Edge compute (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Isolates vs containers | V8 isolates in Cloudflare Workers, startup and memory trade-offs, language limits | Deploy the same handler as a Worker and as a container; compare startup and latency from three regions |
| 5.2 Durable Objects | Globally unique, stateful coordination objects with attached storage (SQLite-backed storage GA); placement near first use | Build a rate limiter and a chat room with Durable Objects |
| 5.3 Data at the edge | Read replicas at the edge, edge SQL databases, consistency vs latency, the speed of light | Measure write latency from three continents to one primary and explain it |
| 5.4 What belongs at the edge | Auth checks, personalization, caching logic, AI inference at the edge; what must stay central | Write a placement decision record for five functions of a product |

**Check your understanding:** (1) Why can't you put a strongly consistent global database "at the edge"? (2) What does a Durable Object give you that a cache does not? (3) Which work should never move to the edge?

### Chapter 6 · WebAssembly on the server (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 The component model and WASI | WIT interfaces, components, WASI 0.2 (January 2024) and WASI 0.3's native async (ratified June 2026) | Build a component with a WIT interface and call it from a host |
| 6.2 Runtimes and platforms | Wasmtime, Spin and SpinKube (Fermyon, acquired by Akamai), wasmCloud (CNCF incubating) | Deploy one component on Spin and one on wasmCloud |
| 6.3 Sandboxing untrusted code | Capability-based security for plugins, user scripts and agent tools; resource limits | Run untrusted plugin code with CPU, memory and capability limits |
| 6.4 Honest comparison | Startup, throughput and density vs containers; ecosystem gaps | Benchmark startup and throughput vs a container for the same function |

**Check your understanding:** (1) What does capability-based security change compared with a container's default permissions? (2) What did WASI 0.3's native async fix? (3) Where is WebAssembly on the server clearly better today, and where is it not yet?

### Chapter 7 · Local-first and sync engines (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Local-first ideals | Ink & Switch's seven ideals (2019): fast, multi-device, offline, collaboration, longevity, privacy, user control | Score three apps you use against the seven ideals |
| 7.2 CRDTs | Automerge and Yjs; convergence; intention preservation; metadata growth | Build a collaborative list with a CRDT; test convergence under random partitions |
| 7.3 Sync engines over Postgres | ElectricSQL (1.0, March 2025), Zero (1.0, June 2026), PowerSync; partial replication by query | Sync a subset of a Postgres table to a client and keep it live |
| 7.4 The backend's new job | Authorizing what syncs, server-side validation, schema migrations with old clients offline, conflict policies | Design authorization for sync so a user never receives another tenant's rows |

**Check your understanding:** (1) What does the backend still own in a local-first app? (2) Why are schema migrations harder when clients hold data offline for weeks? (3) When is last-writer-wins acceptable, and when is it data loss?

### Chapter 8 · Agent infrastructure (weeks 10–11)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Agents as durable workflows | The agent loop as workflow code; model and tool calls as activities; Temporal with the OpenAI Agents SDK (GA March 2026) | Build an agent whose run survives worker crashes and deploys |
| 8.2 Sandboxes | MicroVMs, gVisor-style kernels, WebAssembly; network egress control; secrets never in the sandbox | Run agent-generated code in a sandbox with no network except an allowlist |
| 8.3 Tool servers at scale | MCP's stateless Streamable HTTP (2026-07-28 version), authentication, rate limits, idempotent tools | Load-test an MCP server horizontally scaled behind a load balancer |
| 8.4 Control | Budgets, step limits, approvals, audit, kill switches, evaluation in production (see OV12B) | Add a kill switch and a per-run budget; prove both work mid-run |

**Check your understanding:** (1) Why is an agent loop a good fit for durable execution, and what breaks if model calls run inside workflow code? (2) What must never be inside an agent's sandbox? (3) Why did removing protocol-level sessions make MCP servers easier to scale?

### Chapter 9 · Correctness at the frontier (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Deterministic simulation testing | FoundationDB's simulation (SIGMOD 2021), TigerBeetle's simulator, Antithesis | Build a seeded simulator for a small replicated service and find a bug |
| 9.2 Formal methods in industry | TLA+ and P at AWS ("Use of Formal Methods at Amazon Web Services", 2015; "Systems Correctness Practices at AWS", CACM 2025) | Model a workflow engine's retry protocol in TLA+ or P and check a safety property |
| 9.3 Combining methods | Property-based tests, fuzzing, simulation and models: which bugs each finds | Map 10 known bug classes to the technique most likely to find each |
| 9.4 Checking AI-generated distributed code | Models, simulators and property tests as the verifier for generated protocol and workflow code | Generate a retry protocol with an AI assistant and find a bug in it with your simulator or model |

**Check your understanding:** (1) Why can simulation find concurrency bugs that ordinary integration tests almost never hit? (2) What does a TLA+ model prove, and what does it not prove about the code? (3) Which technique would you apply first to a new payments workflow?

### Chapter 10 · Research project (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Proposal | A falsifiable question, baseline, metrics and threats to validity | Submit a two-page proposal (by week 6, refined here) |
| 10.2 Reproduction or extension | Running the experiment, reporting variance, negative results | Complete the experiments for P3 |
| 10.3 Writing and presenting | Paper structure, figures that show distributions, an honest limitations section | Submit a workshop-style paper and give a 20-minute talk |
| 10.4 Peer review | Reviewing for soundness, reproducibility and clarity; writing a response to reviewers | Write a structured review of a classmate's draft and respond to the reviews of yours |

**Check your understanding:** (1) What makes a negative result worth publishing? (2) How do you show that a difference is not noise? (3) What would someone need to reproduce your work?

## Weekly rhythm

| Week | Chapter | Seminar and build | Deliverable |
|---|---|---|---|
| 1 | 1 | Reading method; critique practice | One-page critique |
| 2 | 2 | Temporal internals; crash tests | Lab 1 report |
| 3 | 2 | Restate, DBOS and managed engines | Lab 2 comparison; P1 due |
| 4 | 3 | Beldi, Boki, DBOS papers | Paper presentation and critique |
| 5 | 4 | Serverless model and cost | Lab 3 cost model |
| 6 | 4 | Cold starts, SnapStart, connections | Lab 4 measurements; research proposal due |
| 7 | 5 | Edge and Durable Objects | Lab 5 build and latency map |
| 8 | 6 | WebAssembly components | Lab 6 sandbox and benchmark; P2 due |
| 9 | 7 | Local-first and sync engines | Lab 7 convergence and sync authorization |
| 10 | 8 | Durable agents | Lab 8 crash-surviving agent |
| 11 | 8 | Sandboxes and MCP at scale | Lab 9 load test and kill switch |
| 12 | 9 | Simulation and formal methods | Simulator bug or TLA+/P model |
| 13 | 10 | Research project | Draft paper |
| 14 | 10 | Research project | Final paper and talk |
| 15 | Review | — | Oral examination on the reading list |

## Working with AI in this course

- **Use AI for:** first-pass summaries of papers (then check every claim against the paper); scaffolding workflows, components and simulators; generating experiment scripts and plots; drafting related-work sections that you verify citation by citation.
- **Do without AI (drills):** the weekly critique; the paper presentation and its Q&A; your research proposal's question and threats to validity; the oral examination.
- **Verify AI output by:** checking every summary against the paper's own text and figures; running every generated experiment twice with different seeds and reporting variance; confirming that each citation exists and says what is claimed.
- **Where AI still fails here (show it yourself):** ask an assistant to summarize Beldi or Boki and compare its description of the guarantees with the paper's. Ask for a durable workflow and check whether it puts non-deterministic calls (time, randomness, network) in workflow code. Ask it for the cold-start difference between two platforms and compare with your own measurements. Ask for a related-work list on durable execution and check whether every reference exists. Record what you find; it becomes part of your critique practice.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Weekly critiques and lab reports | 20% |
| Paper presentation and discussion leadership | 10% |
| Projects P1 / P2 | 10% / 15% |
| P3 research project (paper and talk) | 30% |
| Oral examination on the reading list | 15% |

**Mastery gate:** you pass when you can (a) explain, without notes, how a durable execution engine recovers a workflow after a crash and what it does and does not guarantee about side effects; (b) defend a platform choice (containers, serverless, edge or WebAssembly) for a stated workload with your own measurements; and (c) submit a reproduction or extension whose methods another student can follow to get results within your reported variance.

## Industry reality

- **Durable execution engines in October 2026:** Temporal server 1.32 (October 2026); Restate 1.7 (1.8 in release candidates); DBOS libraries for Python, TypeScript, Go and Java; Cloudflare Workflows (GA April 2025); AWS Lambda durable functions (runs of up to one year, SDKs for JavaScript/TypeScript, Python and Java).
- **Agents:** Temporal's OpenAI Agents SDK integration (preview July 2025, GA March 2026) runs each agent invocation as a durable activity. MCP's 2026-07-28 version removed protocol-level sessions from Streamable HTTP, which simplifies horizontal scaling.
- **Serverless and edge:** Lambda SnapStart supports Java, Python 3.12+ and .NET 8+, with documented uniqueness and connection caveats. Cloudflare's SQLite-backed Durable Objects storage is generally available.
- **WebAssembly:** WASI 0.3 was ratified on 11 June 2026. Akamai announced its acquisition of Fermyon on 1 December 2025, and wasmCloud has been CNCF incubating since November 2024.
- **Local-first:** ElectricSQL 1.0 (March 2025) and Rocicorp's Zero 1.0 (June 2026).
- **Correctness:** AWS described its use of TLA+, P, property-based testing, fault injection and simulation in *Systems Correctness Practices at Amazon Web Services* (CACM, June 2025).

Interview and research-defence questions from this course:

1. **"How does a durable execution engine make a workflow survive a crash?"** A strong answer covers event histories or checkpoints, deterministic replay, activities vs workflow code, timers and signals, at-least-once activities with idempotency, and versioning in-flight workflows.
2. **"Should this API run on Lambda, on Workers, or in containers?"** Cover traffic shape and cost break-even, cold starts and mitigations, state and connection needs, latency from user regions, vendor lock-in and observability, with numbers.
3. **"How would you run thousands of AI agents reliably for hours each?"** Cover durable agent loops, sandboxes, idempotent tools, budgets and step limits, approvals, stateless tool servers, observability and evaluation.
4. **"What does the backend do in a local-first app?"** Cover sync authorization, partial replication, validation, conflict policies, schema evolution with offline clients, and backups of user-owned data.
5. **"Defend the main claim of your research project."** Cover the question, baseline, metrics, variance, threats to validity, what a negative result would have meant, and how someone else can reproduce it.

## Resources (free first)

- **Durable execution:** [Temporal docs](https://docs.temporal.io/workflows) and [event history](https://docs.temporal.io/encyclopedia/event-history); [Restate docs](https://docs.restate.dev/); [DBOS docs](https://docs.dbos.dev/); [Cloudflare Workflows GA](https://blog.cloudflare.com/workflows-ga-production-ready-durable-execution/); [AWS Lambda durable functions](https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html); [Azure Durable Functions](https://learn.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-overview); [Inngest docs](https://www.inngest.com/docs).
- **Papers:** Jonas et al., [Cloud Programming Simplified: A Berkeley View on Serverless Computing](https://arxiv.org/abs/1902.03383) (2019); Agache et al., [Firecracker](https://www.usenix.org/conference/nsdi20/presentation/agache) (NSDI 2020); Zhang et al., [Beldi](https://www.usenix.org/conference/osdi20/presentation/zhang-haoran) (OSDI 2020); Jia and Witchel, [Boki](https://dl.acm.org/doi/10.1145/3477132.3483541) (SOSP 2021); Skiadopoulos et al., [DBOS: A DBMS-Oriented Operating System](https://www.vldb.org/pvldb/vol15/p21-skiadopoulos.pdf) (VLDB 2022); Zhou et al., [FoundationDB](https://www.foundationdb.org/files/fdb-paper.pdf) (SIGMOD 2021); Brooker and Desai, [Systems Correctness Practices at AWS](https://queue.acm.org/detail.cfm?id=3712057) (2025); Kleppmann et al., [Local-first software](https://www.inkandswitch.com/essay/local-first/) (2019).
- **Serverless and edge:** [Lambda SnapStart](https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html); [Lambda response streaming](https://docs.aws.amazon.com/lambda/latest/dg/configuration-response-streaming.html); [How Workers works](https://developers.cloudflare.com/workers/reference/how-workers-works/); [Durable Objects](https://developers.cloudflare.com/durable-objects/).
- **WebAssembly:** [WASI 0.3 announcement](https://bytecodealliance.org/articles/WASI-0.3); [WASI.dev](https://wasi.dev/); [Component Model book](https://component-model.bytecodealliance.org/); [Wasmtime](https://docs.wasmtime.dev/); [Spin](https://spinframework.dev/); [wasmCloud](https://wasmcloud.com/docs/intro).
- **Local-first:** [Automerge](https://automerge.org/); [Yjs](https://docs.yjs.dev/); [ElectricSQL](https://electric-sql.com/); [Zero](https://zero.rocicorp.dev/); [PowerSync](https://www.powersync.com/).
- **Correctness tools:** [TLA+](https://lamport.azurewebsites.net/tla/tla.html); [P language](https://p-org.github.io/P/); [Hydro](https://hydro.run/) (Berkeley research on distributed programming).

## Sources

All checked 12 Oct 2026.

- Temporal server releases (v1.32.1, 8 Oct 2026): https://github.com/temporalio/temporal/releases ; Restate releases (v1.7.13, 1 Oct 2026): https://github.com/restatedev/restate/releases
- Cloudflare Workflows GA (7 Apr 2025): https://developers.cloudflare.com/changelog/2025-04-07-workflows-ga
- AWS Lambda durable functions docs: https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html ; re:Invent 2025 announcement coverage (Classmethod, Dec 2025): https://dev.classmethod.jp/en/articles/lambda-durable-function-25
- Temporal and OpenAI Agents SDK integration (30 Jul 2025; GA 23 Mar 2026): https://temporal.io/blog/announcing-openai-agents-sdk-integration
- Bytecode Alliance, WASI 0.3 (ratified 11 Jun 2026): https://bytecodealliance.org/articles/WASI-0.3
- Akamai acquisition of Fermyon (announced 1 Dec 2025; Akamai FY2025 10-K): https://www.sec.gov/Archives/edgar/data/1086222/000108622226000022/akam-20251231.htm
- wasmCloud CNCF incubating (8 Nov 2024): https://www.cncf.io/projects/wasmcloud/
- ElectricSQL 1.0 (17 Mar 2025): https://electric.ax/blog/2025/03/17/electricsql-1.0-released ; Zero 1.0 (InfoQ, Jun 2026): https://www.infoq.com/news/2026/06/zero-version-1
- MCP Streamable HTTP, 2026-07-28: https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http
- Brooker and Desai, *Systems Correctness Practices at Amazon Web Services* (CACM 68(6), Jun 2025): https://cacm.acm.org/practice/systems-correctness-practices-at-amazon-web-services

_Last reviewed: 2026-10_
