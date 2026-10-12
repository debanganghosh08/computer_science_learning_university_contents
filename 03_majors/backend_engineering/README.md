# Backend Engineering (BE) · Learning path

| Code | Years | Entry requirements | Market page | Interview loop |
|---|---|---|---|---|
| BE | 3–5 (after the common Years 1–2) | [CS211](../../02_year_2_core_computer_science/semester_4/CS211_database_systems_internals/README.md), [CS212](../../02_year_2_core_computer_science/semester_4/CS212_distributed_systems_i/README.md) | [BE roles and market](../../06_career_and_market_readiness/01_market_map/roles/BE_backend_engineering.md) | [AI-driven interviews](../../06_career_and_market_readiness/04_ai_driven_interviews/) |

Backend engineers build the part of software that users never see and always depend on: APIs, data models, queues, authentication, payments, caches, and now the systems that serve AI features and run agents. The work is judged by what happens under failure. A request can time out after the money moved, a message can arrive twice, two users can write at once, traffic can jump ten times in a minute, or a key can leak. This major takes you from a Year 2 student who knows how databases and distributed systems work inside to an engineer who can design, build, operate and prove the correctness of production backends. It ends at the research frontier of durable execution, serverless and edge systems.

## 1. Who this major is for, and the roles it leads to

Choose this major if you like systems that must be correct, enjoy reasoning about data, concurrency and failure, and want work that stays valuable as AI writes more of the happy path. It suits people who would rather prove that money cannot be lost than make a screen look good.

| Role | What people in it actually do | Where this major prepares you |
|---|---|---|
| Backend Engineer I / SDE-1 (backend) | Build and test endpoints, write migrations and queries, fix bugs, join on-call with support | BE301, BE302, BE303, CAR301 |
| Backend Engineer II / SDE-2 | Own a service end to end: API, data model, queues, auth, dashboards, rollout and incidents | BE304, BE305, BE402 |
| API / Platform Engineer | Design APIs other teams and partners build on; run gateways, service templates and internal platform APIs | BE301, BE404, OV02 |
| Payments / Ledger Engineer | Build money movement that is idempotent, reconciled and auditable; integrate UPI, cards and bank rails | BE401, OV10 |
| Distributed Systems Engineer | Own replication, sharding, streams and consistency for high-scale services | BE304, BE402, CSG303 elective |
| Backend-for-AI Engineer | Serve LLM features: streaming, vector search, gateways, quotas, cost control, durable agent runs | BE403, BE501, OV08, OV12 |
| Senior / Staff Backend Engineer, Architect | Set technical direction for many services; design for failure nobody planned; lead reviews and incidents | BE404, BE501, THS501–502 |
| Founding Backend Engineer | Choose the stack, build the first version alone, then make it survive growth | All of the above, plus LCH502 |

Titles are not standard: "SDE-2" at a product company and "Senior Engineer" at a services company can be the same level. The [BE market page](../../06_career_and_market_readiness/01_market_map/roles/BE_backend_engineering.md) lists titles, day-to-day work and pay sources.

## 2. How AI is changing backend work

All figures were checked in October 2026. Paragraphs marked **Analysis** are interpretation.

**Backend is a large, well-defined slice of the profession.** In the 2025 Stack Overflow survey, 14.2% of respondents described themselves as back-end developers and 27% as full-stack. PostgreSQL was used by 58.2% of professional developers ([Stack Overflow 2025](https://survey.stackoverflow.co/2025/developers), [technology](https://survey.stackoverflow.co/2025/technology)). There is no separate official count of backend jobs: the US BLS projects software developers overall at +10% for 2025–35 ([BLS](https://www.bls.gov/ooh/computer-and-information-technology/software-developers.htm)).

**AI tools are standard, but used least where backends are hardest.** In 2026, 65.9% of Stack Overflow respondents use AI coding assistants or agents at work. Only 20% of AI users use them for "deploying, operating, or troubleshooting production systems" ([Stack Overflow 2026](https://survey.stackoverflow.co/2026/ai/data); [blog](https://stackoverflow.blog/2026/10/06/the-results-of-the-2026-developer-survey-are-here/)). In Claude Code, 79% of conversations were automation, and Python (14%) and SQL (6%) were among the most common languages ([Anthropic, Apr 2025](https://www.anthropic.com/research/impact-software-development)).

**Generated backend code needs review.** Veracode's 2025 GenAI Code Security Report tested over 100 models on Java, JavaScript, Python and C# tasks, and found that AI-generated code "introduced risky security flaws in 45% of tests" ([Veracode, updated Oct 2025](https://www.veracode.com/resources/analyst-reports/2025-genai-code-security-report/)). DORA found AI adoption still linked to lower delivery stability ([DORA 2025](https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report)).

**AI agents are becoming API consumers.** In Postman's 2025 survey of over 5,700 respondents, 24% design APIs with AI agents in mind. 51% named unauthorized or excessive API calls from agents as their top security worry. About 70% knew of the Model Context Protocol, but only about 10% used it regularly ([Postman, Oct 2025](https://www.postman.com/state-of-api/2025/)).

**Running systems at scale is what employers ask for.** The fastest-growing skills in US AI job postings were about operating systems at scale: AWS (+1,358% against a decade earlier), scalability (+733%) and workflow management (+818%) ([AI Index 2026](https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf)). Employers in the WEF survey rank "FinTech Engineers" among the fastest-growing jobs to 2030 ([WEF 2025](https://reports.weforum.org/docs/WEF_Future_of_Jobs_Report_2025.pdf)).

| Mostly automated now | Augmented (you decide, AI helps) | Growing in value |
|---|---|---|
| CRUD endpoints, request validation, ORM models, serializers, SDK stubs, first-draft SQL, OpenAPI drafts, Dockerfiles, load-test scripts | Debugging with traces and plans, migrations, refactoring legacy services, writing tests, reading unfamiliar code | Data modeling and isolation, idempotency and reconciliation, failure design (timeouts, retries, backpressure), authorization logic, cost and latency of AI features, durable agent infrastructure, operating production |

**Analysis.** AI writes the happy path well. Backend value has always been in the unhappy paths: partial failures, duplicate messages, concurrent writes, stale caches and money that must reconcile. Those paths are where generated code most often looks right and is wrong, and where review needs someone who understands the whole system. Every course in this major therefore has AI-off drills and verification by measurement: crash harnesses, invariant checks, load tests and adversarial authorization tests.

## 3. The 5-year path

### Years 1–2: the common core

Every Year 1–2 course is required. These matter most for backend engineers:

| Course | Why it matters for BE |
|---|---|
| [FND111 Programming II (Java and TypeScript)](../../01_year_1_foundations/semester_2/FND111_programming_ii_object_oriented_and_typed/README.md) | Two of the four backend ecosystems taught in BE302 |
| [FND114 Web Foundations: HTTP](../../01_year_1_foundations/semester_2/FND114_web_foundations_http_html_css_and_javascript/README.md) | HTTP semantics are the raw material of BE301 |
| [FND115 Databases I](../../01_year_1_foundations/semester_2/FND115_databases_i_data_modeling_and_sql/README.md) | SQL and modeling, used every week of the major |
| [CS201 Algorithms and Complexity](../../02_year_2_core_computer_science/semester_3/CS201_algorithms_and_complexity/README.md) | Coding rounds; reasoning about cost |
| [CS203 Operating Systems](../../02_year_2_core_computer_science/semester_3/CS203_operating_systems/README.md) and [CS204 Computer Networks](../../02_year_2_core_computer_science/semester_3/CS204_computer_networks/README.md) | Threads, sockets and TCP, which sit under every concurrency model in BE302 |
| [CS205 Software Engineering I](../../02_year_2_core_computer_science/semester_3/CS205_software_engineering_i_design_testing/README.md) | Testing, review and CI |
| [CS211 Database Systems Internals](../../02_year_2_core_computer_science/semester_4/CS211_database_systems_internals/README.md) | Entry requirement: B+trees, MVCC, WAL, isolation; the base for BE303 and BE401 |
| [CS212 Distributed Systems I](../../02_year_2_core_computer_science/semester_4/CS212_distributed_systems_i/README.md) | Entry requirement: failure models, retries, idempotency, replication; the base for BE304 |
| [CS213 Security Foundations](../../02_year_2_core_computer_science/semester_4/CS213_security_foundations/README.md) and [CS215 Cloud and DevOps Foundations](../../02_year_2_core_computer_science/semester_4/CS215_cloud_and_devops_foundations/README.md) | The base for BE305 and for deploying everything you build |

### Years 3–5: the major

| Semester | Major courses | Shared courses | Other |
|---|---|---|---|
| 5 (Year 3) | [BE301 API Design: REST, gRPC and GraphQL](year_3/BE301_api_design_rest_grpc_and_graphql/README.md) · [BE302 Backend Frameworks and Service Internals](year_3/BE302_backend_frameworks_and_service_internals/README.md) · [BE303 Data Modeling and Storage: Postgres, Redis and NoSQL](year_3/BE303_data_modeling_and_storage_for_backends_postgres/README.md) | [PRO301 Professional Practice: Ethics, Law and Responsible AI](../../05_shared_years_3_to_5/PRO301_professional_practice_ethics_law_and_responsible/README.md) | 1 elective (CLD303 recommended) |
| 6 (Year 3) | [BE304 Asynchronous Systems: Queues, Streams and Event-Driven Architecture](year_3/BE304_asynchronous_systems_queues_streams_and_event/README.md) · [BE305 Authentication, Authorization and Backend Security](year_3/BE305_authentication_authorization_and_backend/README.md) | [CAR301 Career Lab I: DSA Mastery, Portfolio and Open Source](../../05_shared_years_3_to_5/CAR301_career_lab_i_dsa_mastery_portfolio_and_open/README.md) | 1–2 electives |
| 7 (Year 4) | [BE401 Payments-Grade Systems](year_4/BE401_payments_grade_systems_transactions_idempotency/README.md) · [BE402 Scalability and Performance](year_4/BE402_scalability_and_performance_caching_sharding/README.md) | [IND401 Industry Co-op Studio](../../05_shared_years_3_to_5/IND401_industry_co_op_studio/README.md) | Overlap course A |
| 8 (Year 4) | [BE403 Backends for AI](year_4/BE403_backends_for_ai_serving_llm_features_vector/README.md) · [BE404 Microservices, Service Mesh and Platform APIs](year_4/BE404_microservices_service_mesh_and_platform_apis/README.md) | [CAR401 Career Lab II: Interviews, System Design and AI-Driven Assessments](../../05_shared_years_3_to_5/CAR401_career_lab_ii_interviews_system_design_and_ai/README.md) | Overlap course B |
| 9 (Year 5) | [BE501 Frontier Seminar: Durable Execution, Serverless and Edge Backends](year_5/BE501_frontier_seminar_durable_execution_serverless/README.md) | [RES501 Research Methods](../../05_shared_years_3_to_5/RES501_research_methods_and_scientific_writing/README.md) · [RES502 Reading, Reproducing and Extending Papers](../../05_shared_years_3_to_5/RES502_reading_reproducing_and_extending_papers/README.md) · [THS501 Thesis or Capstone I](../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) | — |
| 10 (Year 5) | — | [THS502 Thesis or Capstone II](../../05_shared_years_3_to_5/THS502_thesis_or_capstone_ii/README.md) · [LCH502 Career Launch and Founder Studio](../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md) | Electives |

Prerequisites inside the major (from the catalog): BE301 → BE401; BE302 → BE402; BE303 → BE403; BE304 → BE404; BE401 + BE403 → BE501. The courses also build on each other more than the catalog lists. BE401 uses BE303, BE304 and BE305; BE404 uses BE301, BE302 and BE305. Take all five Year 3 courses before Year 4.

**How the courses connect.** BE301 decides the contract and BE302 implements it. BE303 stores the data, BE304 moves work off the request path, and BE305 decides who may do what. In Year 4, BE401 makes all of that correct for money, BE402 keeps it fast under load, BE403 adds AI features and BE404 splits it across teams. BE501 asks what replaces these patterns next.

## 4. Skill map by level

| Level | You can… | Mastery gate (do it, don't describe it) |
|---|---|---|
| L0 → L1 (Year 1) | Write programs in Python, Java and TypeScript; use Git; write SQL; explain an HTTP request | Build a CLI and a tiny HTTP API with tests, a README and passing CI |
| L2 (end of Year 2) | Explain B+trees, MVCC, isolation anomalies, replication and retries with idempotency; build a small service | CS211's and CS212's gates: recover an ARIES log by hand; implement Raft that passes adversarial tests |
| L3 (end of Year 3) | Design an API, build it in two stacks, model and migrate its data, move work to queues with an outbox, add OAuth and object-level authorization, and operate it with traces and graceful shutdown | Ship a service that survives 200 random crash points with zero lost or duplicated effects, deploys with zero dropped requests, and passes an every-endpoint × every-role authorization matrix |
| L4 (end of Year 4) | Build payments-grade flows with ledgers and reconciliation; scale with caches, replicas and shards; serve LLM features with cost control; split a system into services with contracts and a mesh | Run a game day on your flagship project (spike, cache-node loss, provider outage, bad deploy) without breaking money invariants or the SLO; pass a 60-minute system-design round |
| L5 (Year 5) | Read, reproduce and extend systems research on durable execution, serverless, edge and agent infrastructure | Submit a reproduction or extension (BE501 P3) that another student reproduces within your reported variance, and defend it orally |

## 5. Recommended overlaps and electives

**Overlaps** (Year 4; each has an A course in semester 7 and a B course in semester 8):

| Overlap | The real job it maps to | Composed of | Notes for BE students |
|---|---|---|---|
| [OV02 Cloud-Native Backend](../../04_overlaps/OV02_cloud_native_backend/README.md) | Backend engineer who owns services on Kubernetes and managed cloud | BE301, BE304, CLD303 | The easiest fit: take CLD303 as a Year 3 elective |
| [OV10 FinTech Systems Engineering](../../04_overlaps/OV10_fintech_systems_engineering/README.md) | Payments, lending and trading backends at banks, fintechs and marketplaces | BE401, SEC305, DEN303 | Take SEC305 and DEN303 as Year 3 electives; BE401 runs in the same semester as OV10A |
| [OV12 Agent Infrastructure and Platform Engineering](../../04_overlaps/OV12_agent_infrastructure_platform/README.md) | Platform engineer running agents in production: sandboxes, durable execution, evaluation | AIE401, OPS403, BE501 | BE501 is a Year 5 course, so this overlap fits best as Year 5 work alongside the thesis; check the catalog before planning |
| [OV08 Full-Stack AI Product Engineering](../../04_overlaps/OV08_full_stack_ai_product_engineering/README.md) | Product or founding engineer shipping AI features end to end | FE403, BE403, AIE404 | BE403 is in semester 8; plan OV08A after it or take it with the instructor's permission |

**Electives** (pick 3–5):

- [CLD303 Containers and Kubernetes](../cloud_engineering/year_3/CLD303_containers_and_kubernetes/README.md): needed for BE404 and OV02.
- [OPS303 Observability](../devops_sre_platform_engineering/year_3/OPS303_observability_metrics_logs_traces/README.md) and [OPS304 Site Reliability Engineering](../devops_sre_platform_engineering/year_3/OPS304_site_reliability_engineering_slos_error_budgets/README.md): for on-call-heavy roles.
- [CSG303 Distributed Systems II](../computer_science_general/year_3/CSG303_distributed_systems_ii_consensus_replication/README.md): for distributed-systems roles and BE501 research.
- [SWE305 Concurrency and Performance Engineering](../software_engineering/year_3/SWE305_concurrency_and_performance_engineering/README.md) and [SWE401 Large-Scale System Design](../software_engineering/year_4/SWE401_large_scale_system_design/README.md): depth for senior interviews.
- [DEN303 Streaming Systems: Kafka and Flink](../data_engineering/year_3/DEN303_streaming_systems_kafka_and_flink/README.md): stream processing beyond BE304.
- [AIE303 Retrieval-Augmented Generation and Search](../ai_engineering/year_3/AIE303_retrieval_augmented_generation_and_search/README.md) and [AIE304 Tool Use and AI Agents](../ai_engineering/year_3/AIE304_tool_use_and_ai_agents_loops_harnesses_memory/README.md): before BE403.
- [SAR302 Threat Modeling](../security_architecture/year_3/SAR302_threat_modeling/README.md) and [SEC305 Governance, Risk and Compliance](../cybersecurity_defense/year_3/SEC305_governance_risk_and_compliance/README.md): for payments and regulated domains.
- [CLD403 FinOps and Cloud Cost Engineering](../cloud_engineering/year_4/CLD403_finops_and_cloud_cost_engineering/README.md): cost is a design constraint in BE402 and BE403.

## 6. Flagship industry project

The BE flagship is described in [`05_industry_projects/BE_backend_engineering.md`](../../06_career_and_market_readiness/05_industry_projects/BE_backend_engineering.md). It joins the major's threads into one production-style system that you design, build, load-test, break on purpose and document. Its parts come from the course projects:
- BE301 P3 (multi-protocol API with an agent interface);
- BE303 P3 (multi-tenant storage);
- BE304 P3 (sagas and event sourcing);
- BE401 P3 (payments with reconciliation);
- BE402 P3 (built for a 10× spike);
- BE403 P3 (an AI assistant with durable agents);
- BE404 P3 (a platform with a golden path).

Build it across Year 4 and present it in CAR401 and LCH502. It is the evidence that you have moved past CRUD.

## 7. Certifications (optional, never required)

| Certification | Honest value for backend engineers |
|---|---|
| [AWS Certified Developer – Associate](https://aws.amazon.com/certification/certified-developer-associate/) or [Google Professional Cloud Developer](https://cloud.google.com/learn/certification/cloud-developer) | Shows familiarity with one cloud's managed services. Useful when applying to services firms and cloud-heavy teams; product companies weigh projects more. |
| [CNCF Certified Kubernetes Application Developer (CKAD)](https://www.cncf.io/training/certification/ckad/) | Hands-on, performance-based exam, so it carries more signal than multiple-choice ones. Worth it if you target OV02-style roles. |
| [Confluent Certified Developer for Apache Kafka](https://www.confluent.io/certification/) | Narrow but recognized where Kafka is central (fintech, streaming). BE304 P2 shows more. |
| Oracle Certified Professional: Java SE Developer | Proves language knowledge; sometimes asked for in Java-heavy services work (unconfirmed as a general rule). Low signal at product companies. |
| [MongoDB Associate Developer](https://learn.mongodb.com/pages/mongodb-associate-developer-exam) | Useful only if your target employers run MongoDB. |
| Vendor AI-tool certificates | Very low signal. A repository showing your agent workflow with review gates and measured results says far more. |

**Analysis.** For backend roles, certificates rarely decide a hire. A project with load-test numbers, a crash-test harness, a reconciliation report or a merged contribution to an open-source backend tool does.

## 8. The interview loop for this role

A typical loop (it varies by company; see the [market page](../../06_career_and_market_readiness/01_market_map/roles/BE_backend_engineering.md)):

| Round | What is tested | Prepared by |
|---|---|---|
| Online assessment and coding (1–3 rounds) | DSA problems, often with a scale twist (streams, top-k, rate limits) | CS201, CAR301 |
| Low-level design | Rate limiter, LRU cache, idempotent payment endpoint, seat booking: clean interfaces and concurrency | BE302, BE301, BE303 |
| System design (mid-level and above) | URL shortener, notification service, payment flow, chat: data model, consistency, idempotency, failure handling, capacity estimates | BE402, BE304, BE401, CAR401 |
| Database deep dive | Indexes, query plans, isolation levels and anomalies, migrations | BE303, CS211 |
| Debugging or production scenario | A slow endpoint or a failing consumer: find the cause from logs, traces and metrics | BE302, BE402, BE404 |
| AI-assisted coding (growing) | Using AI tools on a realistic task and catching their mistakes. Canva expects backend candidates to use AI tools in interviews ([Canva, Jun 2025](https://www.canva.dev/blog/engineering/yes-you-can-use-ai-in-our-interviews/)) | Every BE course's "Working with AI" section |
| Behavioural | An incident you handled; a trade-off you got wrong; working across teams | IND401, BE404 |

Some employers forbid AI in live rounds ([Anthropic](https://www.anthropic.com/candidate-ai-guidance)), so prepare both ways. Every BE course lists five interview questions with what a strong answer covers. Simulations and question banks are in [AI-driven interviews](../../06_career_and_market_readiness/04_ai_driven_interviews/).

## 9. Fast track for working professionals

For developers with 1–5 years of experience, for example writing Java, Node.js or Python services at a services company, who want product-company backend, payments or platform roles. Budget 12–15 hours a week for about 12 months.

1. **Placement (week 1).** Attempt the mastery gates of [CS211](../../02_year_2_core_computer_science/semester_4/CS211_database_systems_internals/README.md) and [CS212](../../02_year_2_core_computer_science/semester_4/CS212_distributed_systems_i/README.md). If you cannot explain write skew or idempotent retries, start there.
2. **Months 1–3: correctness first.** BE303 (data modeling, isolation, migrations) and BE304 (outbox, idempotent consumers, sagas). These fix the bugs most production backends ship with.
3. **Months 4–5: contracts and security.** BE301 and BE305. Run the BE305 authorization test matrix on a service you own at work, within your employer's rules.
4. **Months 6–7: service internals.** BE302, focusing on the stack you do not use at work, plus its pool-sizing and graceful-shutdown labs.
5. **Months 8–11: pick a specialization.** BE401 for payments and fintech; BE402 for scale and performance; BE403 for AI features; BE404 for platform roles. Do one course's P3 to portfolio quality.
6. **Month 12: interview readiness.** CAR401 system design practice using your P3 as the anchor story, and one mock interview a week.
7. **Throughout.** One timed DSA set a week from CAR301, and write a short public post on each P3 with its numbers.

## Sources

All checked October 2026.

- Stack Overflow Developer Survey 2025: developer types (back-end 14.2%, full-stack 27%) — https://survey.stackoverflow.co/2025/developers ; technology (PostgreSQL 58.2% of professional developers) — https://survey.stackoverflow.co/2025/technology
- Stack Overflow Developer Survey 2026, AI (6 Oct 2026) — https://survey.stackoverflow.co/2026/ai/data ; results blog — https://stackoverflow.blog/2026/10/06/the-results-of-the-2026-developer-survey-are-here/
- Anthropic, *The impact of AI on software development* (28 Apr 2025) — https://www.anthropic.com/research/impact-software-development
- Veracode, *2025 GenAI Code Security Report* (update, Oct 2025) — https://www.veracode.com/resources/analyst-reports/2025-genai-code-security-report/
- Postman, *2025 State of the API Report* (8 Oct 2025) — https://www.postman.com/state-of-api/2025/
- Google Cloud, *Announcing the 2025 DORA report* (24 Sep 2025) — https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report
- US BLS, Occupational Outlook Handbook, Software Developers (2025–35) — https://www.bls.gov/ooh/computer-and-information-technology/software-developers.htm
- Stanford HAI, *AI Index 2026* — https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf
- World Economic Forum, *Future of Jobs Report 2025* — https://reports.weforum.org/docs/WEF_Future_of_Jobs_Report_2025.pdf
- Canva Engineering, *Yes, you can use AI in our interviews* (11 Jun 2025) — https://www.canva.dev/blog/engineering/yes-you-can-use-ai-in-our-interviews/ ; Anthropic, candidate AI guidance — https://www.anthropic.com/candidate-ai-guidance
- BE market page, which collects further role, pay and demand sources: [roles/BE_backend_engineering.md](../../06_career_and_market_readiness/01_market_map/roles/BE_backend_engineering.md)

_Last reviewed: 2026-10_
