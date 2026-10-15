# System design: interviews and practice

This section is the interview-and-practice layer on top of the system design courses. It does not re-teach the theory. It shows how design is tested, gives you one method that works for every prompt, and gives you 16 full designs, 8 low-level designs and a review checklist to practise against.

| You need first | Where it is taught |
|---|---|
| Replication, consensus, clocks, partial failure | [CS212 · Distributed Systems I](../../02_year_2_core_computer_science/semester_4/CS212_distributed_systems_i/README.md) |
| Storage engines, indexes, transactions | [CS211 · Database Systems Internals](../../02_year_2_core_computer_science/semester_4/CS211_database_systems_internals/README.md) |
| The full design method, Indian and global case studies | [SWE401 · Large-Scale System Design](../../03_majors/software_engineering/year_4/SWE401_large_scale_system_design/README.md) |
| Caching, sharding, load balancing, overload, capacity | [BE402 · Scalability and Performance](../../03_majors/backend_engineering/year_4/BE402_scalability_and_performance_caching_sharding/README.md) |
| ML system design (labels, features, serving, evaluation) | [MLE302 · Machine Learning System Design](../../03_majors/machine_learning_engineering/year_3/MLE302_machine_learning_system_design/README.md) |
| Classes, interfaces and design patterns (for LLD) | [SWE301 · Software Architecture and Design Patterns](../../03_majors/software_engineering/year_3/SWE301_software_architecture_and_design_patterns/README.md) |

## What is in this folder

| File | What it gives you |
|---|---|
| [building_blocks.md](building_blocks.md) | The 17 components you will reach for, each with when, why, trade-offs and real numbers; the latency table with its sources |
| [estimation.md](estimation.md) | The back-of-the-envelope method and 6 worked examples (QPS, storage, bandwidth, cache size, concurrency, GPU and token cost) |
| [case_studies/](#the-16-case-studies) | 16 complete high-level designs, each with requirements, estimates, API, data model, a diagram, deep dives, failure modes, trade-offs, evolution and level expectations |
| [lld/](lld/README.md) | 8 low-level design problems with class diagrams, patterns and tested Python skeletons |
| [review_checklist.md](review_checklist.md) | A self-review checklist and the 25 most common design-interview mistakes |

---

## 1. How system design is tested now

### 1.1 What a design round is

A system design round gives you an open prompt ("design a ride-hailing dispatch system") and 45–60 minutes. There is no single right answer. The interviewer watches how you turn ambiguity into requirements, whether your numbers are in the right order of magnitude, whether each component is justified by an access pattern, and whether you can go deep on the part that is hard. Most companies run it alongside coding rounds; a design round usually decides your level more than your hire/no-hire.

### 1.2 By level

Formats differ by company and change often, so confirm the loop with your recruiter. The table below is **analysis**: it summarises what the public interview guides of large employers and the courses linked above converge on. It is not any one company's rubric.

| Level | Typical design rounds | What "good" looks like | What sinks candidates |
|---|---|---|---|
| **New grad / intern** (L2 → L3) | Often none. Where present: one LLD or object-oriented design round, or a "light" HLD (URL shortener, rate limiter) | Clean classes and interfaces; a correct single-server design; knows what a cache, index, queue and load balancer are for; asks clarifying questions | Jumping to Kafka and microservices for a problem that fits on one machine; no data model |
| **SDE-2 / mid** (L3) | One HLD round, sometimes one LLD round | Full framework in time; estimates within 10×; correct storage choice from access patterns; one solid deep dive (cache invalidation, sharding key, idempotency) | Components with no reason; no numbers; hand-waving at "eventual consistency" |
| **Senior** (L3 → L4) | One or two HLD rounds, often one with a product or domain flavour; ML/AI design for ML/AI roles | Drives the conversation; picks the hardest part and goes deep unprompted; failure modes, hot keys, multi-region, cost; states trade-offs with numbers | Breadth without depth; never says "this is what breaks first" |
| **Staff+** (L4) | Design rounds plus a "past project deep dive" or architecture review | Frames the problem as a business and organisational choice; migration paths from the current system; blast radius, cells, operability; knows when *not* to build | Designing a greenfield system when the prompt was about evolving an existing one; ignoring teams, rollout and cost |

### 1.3 HLD and LLD

| | High-level design (HLD) | Low-level design (LLD) |
|---|---|---|
| Question | "Design WhatsApp", "design a payment switch" | "Design a parking lot", "design an LRU cache class" |
| Unit of design | Services, data stores, queues, regions | Classes, interfaces, methods, state machines |
| Evidence of skill | Estimates, storage and partitioning choices, consistency per operation, failure handling | Cohesive classes, the right pattern (strategy, state, observer), thread safety, extensibility |
| Output | Box-and-arrow diagram, API, data model, deep dives | Class diagram and runnable code |
| Who gets it most | SDE-2 and above | New grads, SDE-1/2, and in Indian product companies frequently at all levels (analysis) |

This folder covers both: [case_studies/](#the-16-case-studies) for HLD, [lld/](lld/README.md) for LLD.

### 1.4 ML and AI system design

ML engineering loops add an ML system design round. Chip Huyen's *Machine Learning Interviews* says of these questions: "Almost all companies I've talked to ask at least a question of this type" ([source](https://huyenchip.com/ml-interviews-book/)). The structure differs from backend HLD: problem framing → metrics → data and labels → features → model → serving → evaluation → monitoring. [MLE302](../../03_majors/machine_learning_engineering/year_3/MLE302_machine_learning_system_design/README.md) teaches it in full.

Since 2024, AI-product prompts have joined the classic list: retrieval-augmented assistants, agent platforms and LLM inference serving. They test the same fundamentals (queues, caches, idempotency, isolation) plus new ones: token budgets, GPU memory, evaluation, and permission boundaries for tools. Case studies [14](case_studies/14_rag_enterprise_assistant.md), [15](case_studies/15_ai_agent_platform.md) and [16](case_studies/16_llm_inference_serving.md) cover them.

### 1.5 How AI tools change design interviews and design work

**Evidence (what employers have said publicly):**

- **Some interviews now require AI.** Canva "now expect[s] Backend, Machine Learning and Frontend engineering candidates to use AI tools" in interviews and assesses whether candidates can "identify and fix issues in AI-generated code" ([Canva Engineering, 11 Jun 2025](https://www.canva.dev/blog/engineering/yes-you-can-use-ai-in-our-interviews/)).
- **Meta began allowing an AI assistant in some coding interviews**, saying it is "more representative of the developer environment that our future employees will work in" ([404 Media, 29 Jul 2025](https://www.404media.co/meta-is-going-to-let-job-candidates-use-ai-during-coding-tests/)). The report does not say whether design rounds changed.
- **Others forbid it.** Anthropic's candidate guidance says live interviews are "all you–no AI assistance unless we indicate otherwise" ([Anthropic](https://www.anthropic.com/candidate-ai-guidance)).
- **Cheating pressure is pushing some rounds back on site.** CNBC reported that Google's CEO suggested in a February 2025 town hall that "some fraction of the interviews" be in person, in a story about AI tools used to cheat in remote interviews ([CNBC, 9 Mar 2025](https://www.cnbc.com/2025/03/09/google-ai-interview-coder-cheat.html)).

**Analysis (what this means for you):**

1. **The template answer is worth nothing.** Any assistant produces "load balancer, Redis, Kafka, sharding" in seconds. Interviewers now probe the parts a template cannot supply: the numbers, the access pattern that chooses the database, the failure that matters, and why you rejected the alternative. [SWE401](../../03_majors/software_engineering/year_4/SWE401_large_scale_system_design/README.md) records the typical AI failures: skipped or wrong estimates, components no access pattern needs, "exactly-once" claims without idempotent effects, and ignored constraints such as data residency.
2. **Where AI is allowed, the skill being tested is verification.** Expect to be handed an AI-generated design and asked what is wrong with it. Practise this: generate a design with any assistant, then mark every unsupported number, every unjustified box and every missing failure mode (the [review checklist](review_checklist.md) is the marking scheme).
3. **Design work itself has changed less than coding.** Assistants draft design documents, diagrams and load-test scripts quickly. The decisions (what consistency a screen needs, where the shard key goes, what to do when the bank does not answer) remain the engineer's, because they depend on facts about the business that the model does not have. The [market map](../01_market_map/README.md) lists system design and failure analysis among the skills least automated so far.
4. **AI-system prompts are now standard.** Know the vocabulary and numbers of [LLM serving](building_blocks.md#17-llm-serving) and [vector search](building_blocks.md#16-vector-databases): time to first token, KV-cache size, batching, recall@k, prompt injection, tool permissions.

---

## 2. The framework

Use the same nine steps for every HLD prompt. The order matters: each step produces an input for the next.

```mermaid
flowchart LR
  R["1 Requirements"] --> E["2 Estimates"] --> A["3 API"] --> D["4 Data model"] --> H["5 High-level design"]
  H --> DD["6 Deep dives"] --> B["7 Bottlenecks and failures"] --> T["8 Trade-offs"] --> V["9 Evolution"]
```

| Step | Produce | Questions to ask | Minutes (45 / 60) |
|---|---|---|---|
| **1 · Requirements** | 3–5 functional requirements; non-functional targets (availability, latency p99, durability, consistency, freshness); explicit non-goals | Who are the users? What are the top 3 actions? Read/write ratio? What must never happen (double charge, double booking)? Any regulatory constraint (data residency, payment rules)? | 5 / 7 |
| **2 · Estimates** | Peak QPS for reads and writes, storage per year, bandwidth, hot-set size; one line each | What is daily volume? What is the peak factor and why (festival sale, 10:00 ticket opening, match end)? | 4 / 5 |
| **3 · API** | 3–6 endpoints or RPCs with request, response, idempotency and pagination | Sync or async? Who retries? What does the client see on timeout? | 4 / 5 |
| **4 · Data model** | Entities, keys, the access-pattern table (query → key → store) | Which query is hottest? Which needs a transaction? What is the partition key? | 4 / 6 |
| **5 · High-level design** | One diagram: clients, edge, services, stores, queues, with the read and write paths traced | Which path is latency-critical? Which can be asynchronous? | 8 / 10 |
| **6 · Deep dives** | 1–3 hard parts in detail (chosen by you, or by the interviewer) | What is the hardest problem here? Usually: hot keys, ordering, consistency, idempotency, fan-out, real-time location | 12 / 15 |
| **7 · Bottlenecks and failures** | What breaks first at 10× load; what happens when each dependency is slow or down | Single points of failure? Retry storms? Region loss? | 4 / 6 |
| **8 · Trade-offs** | 2–3 decisions with the rejected alternative and the reason | What did you give up? When would you choose differently? | 2 / 3 |
| **9 · Evolution** | v1 (small team, one region) → v2 → v3; what you would measure before each step | What is the simplest thing that works today? What triggers the next step? | 2 / 3 |

**Rules that make the framework work:**

- **Write numbers down.** A number on the board is a decision the interviewer can follow. "A lot of traffic" is not.
- **Trace a request.** After drawing the diagram, walk one write and one read through it, naming each hop and its latency budget.
- **Every box earns its place.** For each component say which access pattern or failure it serves. If you cannot, remove it.
- **Choose consistency per operation, not per system.** A booking confirmation and a "seats left" counter need different guarantees.
- **Say what breaks first.** Seniors are expected to volunteer the bottleneck before the interviewer finds it.
- **Leave time for evolution.** It shows judgement: what you would not build yet, and what metric would make you build it.

---

## 3. The 16 case studies

Each case study follows the framework and ends with what interviewers look for at each level. Public sources are cited wherever a company has described its system. Where nothing public exists, the design is labelled **illustrative**: it is a reasonable design, not a description of any company's system.

| # | System | Core difficulty | Basis |
|---|---|---|---|
| 01 | [URL shortener](case_studies/01_url_shortener.md) | ID generation, read-heavy caching, analytics pipeline | Illustrative; Twitter Snowflake for IDs |
| 02 | [Rate limiter](case_studies/02_rate_limiter.md) | Accuracy vs latency across a fleet | Stripe and Cloudflare public posts |
| 03 | [News feed](case_studies/03_news_feed.md) | Fan-out on write vs read, celebrity accounts | Twitter's public talks (2012–13), Meta TAO |
| 04 | [Chat at WhatsApp scale](case_studies/04_chat_whatsapp_scale.md) | Persistent connections, ordering, receipts, E2EE | WhatsApp and Discord public posts; numbers illustrative |
| 05 | [Notification system](case_studies/05_notification_system.md) | Fan-out, provider limits, deduplication, preferences | Illustrative; FCM/APNs limits, Uber RAMEN |
| 06 | [Ride-hailing dispatch and ETA](case_studies/06_ride_hailing_dispatch_eta.md) | Location ingest, geo-indexing, matching, ETA | Uber H3, RAMEN, DeepETA posts |
| 07 | [Food delivery ETA and order tracking](case_studies/07_food_delivery_eta_tracking.md) | Multi-party state machine, live tracking, ETA | Swiggy and Zomato posts; architecture illustrative |
| 08 | [UPI-style payment switch](case_studies/08_upi_style_payment_switch.md) | Idempotency, timeouts, deemed approval, reconciliation | NPCI circulars and RBI TAT rules; internals illustrative |
| 09 | [Tatkal-style flash booking](case_studies/09_tatkal_flash_booking.md) | Admission control, fairness, inventory locking | IRCTC public records and Railway Ministry rules; internals illustrative |
| 10 | [Live video streaming](case_studies/10_live_video_streaming.md) | Live cricket spikes, transcoding, CDN egress | Hotstar talk (2019), ICC (2026), YouTube and Netflix posts |
| 11 | [Search autocomplete](case_studies/11_search_autocomplete.md) | Top-k per prefix at p99 < 100 ms, freshness | Illustrative |
| 12 | [Distributed key-value store](case_studies/12_distributed_kv_store.md) | Partitioning, replication, quorums, repair | Dynamo (2007), DynamoDB (2022) papers |
| 13 | [Recommendation system](case_studies/13_recommendation_system.md) | Candidate generation and multi-stage ranking | YouTube (2016), Instagram Explore (2023) |
| 14 | [RAG enterprise assistant](case_studies/14_rag_enterprise_assistant.md) | Permission-aware retrieval, freshness, evaluation | Anthropic contextual retrieval (2024); architecture illustrative |
| 15 | [AI agent platform](case_studies/15_ai_agent_platform.md) | Sandboxes, durable execution, tool permissions, evals | Firecracker, Temporal, MCP spec, OWASP LLM Top 10 |
| 16 | [LLM inference serving](case_studies/16_llm_inference_serving.md) | Batching, KV cache, routing, cost | Orca, vLLM, DistServe papers; NVIDIA specs |

---

## 4. A 10-week study plan

About 8–10 hours a week. If you are in Year 4, run it alongside [CAR401](../../05_shared_years_3_to_5/CAR401_career_lab_ii_interviews_system_design_and_ai/README.md). "AI-off" means you do the drill without any assistant; check your work with one afterwards.

| Week | Learn | Practise (AI-off first) | Deliverable |
|---|---|---|---|
| 1 | The framework (this page); [estimation.md](estimation.md) examples 1–3; latency table in [building_blocks.md](building_blocks.md) | 10 estimation drills, 3 minutes each; recite the latency table | Estimation sheet with every assumption written |
| 2 | Building blocks 1–8 (load balancing to queues) | [01 URL shortener](case_studies/01_url_shortener.md), [02 rate limiter](case_studies/02_rate_limiter.md); LLD [LRU cache](lld/02_lru_cache.md), [rate limiter class](lld/03_rate_limiter_class.md) | Two 45-minute designs on paper, then compare with the case study |
| 3 | Building blocks 9–15; [estimation.md](estimation.md) examples 4–6 | [03 news feed](case_studies/03_news_feed.md), [05 notifications](case_studies/05_notification_system.md); LLD [parking lot](lld/01_parking_lot.md), [logger/pub-sub](lld/07_logger_pubsub.md) | One recorded solo mock; score it with the [review checklist](review_checklist.md) |
| 4 | Real-time systems: connections, presence, geo-indexing | [04 chat](case_studies/04_chat_whatsapp_scale.md), [06 ride-hailing](case_studies/06_ride_hailing_dispatch_eta.md); LLD [elevator](lld/05_elevator.md) | Peer mock (you interview, then swap) |
| 5 | Correctness and money: idempotency, sagas, reconciliation (SWE401 ch. 8) | [08 UPI switch](case_studies/08_upi_style_payment_switch.md), [09 Tatkal booking](case_studies/09_tatkal_flash_booking.md); LLD [BookMyShow seat locking](lld/06_bookmyshow_seat_locking.md), [Splitwise](lld/04_splitwise.md) | Write a 2-page design doc for one of them |
| 6 | Scale at the edge: CDNs, video, overload (BE402 ch. 6, 10) | [10 live streaming](case_studies/10_live_video_streaming.md), [07 food delivery](case_studies/07_food_delivery_eta_tracking.md) | LLM mock using the [mock kit](../04_ai_driven_interviews/how_to_run_a_mock_with_any_llm.md) |
| 7 | Storage internals for interviews: quorums, compaction, repair | [12 key-value store](case_studies/12_distributed_kv_store.md), [11 autocomplete](case_studies/11_search_autocomplete.md); LLD [in-memory file system](lld/08_in_memory_file_system.md) | Explain consistent hashing and quorum reads to a peer in 5 minutes, no notes |
| 8 | ML and AI design: retrieval, ranking, vector search, LLM serving (blocks 16–17) | [13 recommendations](case_studies/13_recommendation_system.md), [14 RAG assistant](case_studies/14_rag_enterprise_assistant.md) | One ML design mock using the MLE302 structure |
| 9 | AI infrastructure | [15 agent platform](case_studies/15_ai_agent_platform.md), [16 LLM serving](case_studies/16_llm_inference_serving.md) | Critique an AI-generated design for one of them; list every error |
| 10 | Mixed timed practice | 4 unseen prompts (from SWE401's interview list or your target company's reported prompts), 45 minutes each; 2 LLD problems in 40 minutes each | Final self-score; list your 3 weakest framework steps and redo those drills |

**Mastery gate for this section.** You are ready when, with AI off, you can take a prompt you have not seen and in 45 minutes produce: written requirements with non-goals; estimates within an order of magnitude of a reference; an API and access-pattern table; a diagram whose every box you can justify; one deep dive with numbers; three failure modes with mitigations; and a v1 → v3 evolution, scoring at least 80% on the [review checklist](review_checklist.md).

---

## 5. How to practise

1. **Solo, timed, on paper.** Set a 45-minute timer. Talk out loud (record yourself). Afterwards score the recording with the [review checklist](review_checklist.md), then read the matching case study and list what you missed.
2. **With a peer.** Take turns as interviewer. The interviewer's job is to interrupt: "What is your peak QPS?", "The cache is down, what happens?", "Why not Postgres?". Use the level table in section 1.2 to decide which level the answer was.
3. **With an LLM as interviewer.** Use the [mock kit](../04_ai_driven_interviews/how_to_run_a_mock_with_any_llm.md): it gives the prompt that makes a model behave as an interviewer (asks one question at a time, refuses to design for you, pushes on weak spots, scores against a rubric). Two rules: do the design yourself, and check every number and claim the model makes about real companies against the sources in these pages, because models invent precise figures.
4. **Critique drills.** Ask an assistant to design one of the 16 systems. Mark its answer with the checklist. This is the skill AI-enabled interviews test, and it is fast practice.
5. **Build one thing.** Pick the riskiest path of one design (the seat-lock, the rate limiter, the idempotent payment endpoint) and build it with a load test. A small, measured prototype is stronger interview evidence than ten memorised diagrams.

---

## Resources (free first)

- *The System Design Primer* — https://github.com/donnemartin/system-design-primer
- AWS Builders' Library (articles by AWS engineers on timeouts, retries, load shedding, cells) — https://aws.amazon.com/builders-library/
- Google SRE book (free online), especially "Handling Overload" and "Addressing Cascading Failures" — https://sre.google/sre-book/table-of-contents/
- MIT 6.5840 Distributed Systems — https://pdos.csail.mit.edu/6.824/
- Malte Ubl, "Design Docs at Google" — https://www.industrialempathy.com/posts/design-docs-at-google/
- Chip Huyen, *Machine Learning Interviews* (free online) — https://huyenchip.com/ml-interviews-book/
- Paid, optional: Kleppmann, *Designing Data-Intensive Applications*; Xu, *System Design Interview* vols. 1–2 (useful for prompt lists; check its numbers against primary sources).

## Sources

All checked 12 Oct 2026.

- Canva Engineering, "Yes, You Can Use AI in Our Interviews" (11 Jun 2025) — https://www.canva.dev/blog/engineering/yes-you-can-use-ai-in-our-interviews/
- 404 Media, "Meta Is Going to Let Job Candidates Use AI During Coding Tests" (29 Jul 2025) — https://www.404media.co/meta-is-going-to-let-job-candidates-use-ai-during-coding-tests/
- Anthropic, candidate AI guidance — https://www.anthropic.com/candidate-ai-guidance
- CNBC, "Meet the 21-year-old helping coders use AI to cheat in Google and other tech job interviews" (9 Mar 2025) — https://www.cnbc.com/2025/03/09/google-ai-interview-coder-cheat.html
- Chip Huyen, *Machine Learning Interviews* — https://huyenchip.com/ml-interviews-book/
- Case-study and building-block sources are listed on each page.

_Last reviewed: 2026-10_
