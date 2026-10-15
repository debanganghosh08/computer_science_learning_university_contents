# OV02 · Cloud-Native Backend

| Composed of | Overlap courses | When | Typical entry majors | Market pages |
|---|---|---|---|---|
| [BE301](../../03_majors/backend_engineering/year_3/BE301_api_design_rest_grpc_and_graphql/README.md) · [BE304](../../03_majors/backend_engineering/year_3/BE304_asynchronous_systems_queues_streams_and_event/README.md) · [CLD303](../../03_majors/cloud_engineering/year_3/CLD303_containers_and_kubernetes/README.md) | [OV02A](OV02A_building_cloud_native_services/README.md) · [OV02B](OV02B_event_driven_serverless_backends/README.md) | Year 4 (semesters 7–8) | Backend Engineering, Software Engineering, Cloud Engineering, Frontend (towards full stack) | [BE](../../06_career_and_market_readiness/01_market_map/roles/BE_backend_engineering.md) · [CLD](../../06_career_and_market_readiness/01_market_map/roles/CLD_cloud_engineering.md) · [SWE](../../06_career_and_market_readiness/01_market_map/roles/SWE_software_engineering.md) |

## The job this overlap maps to

The most common senior backend job today is not "write endpoints". It is **own a service end to end on a cloud platform**: design its API and events, build it to run on Kubernetes or serverless infrastructure, make it survive retries, restarts, zone failures and traffic spikes, observe it, ship it many times a day, and keep its cost per request sensible. Job ads call this Backend Engineer (Cloud), Senior Software Engineer (Distributed Systems), Cloud-Native Developer, Product Engineer (Backend) or, in Indian product companies, SDE-2/SDE-3 on a platform-heavy team.

A day in the role, concretely:

- Design an API and the events it publishes ([BE301](../../03_majors/backend_engineering/year_3/BE301_api_design_rest_grpc_and_graphql/README.md), [BE304](../../03_majors/backend_engineering/year_3/BE304_asynchronous_systems_queues_streams_and_event/README.md)).
- Make it behave well on the platform: probes, graceful shutdown, resource limits, autoscaling.
- Add resilience: timeouts, retries with budgets, idempotency, circuit breaking.
- Instrument it with OpenTelemetry and own its SLO.
- Choose between a container on Kubernetes, a serverless function, or a serverless container, and justify the choice with latency, cost and operational load.

## Why this overlap exists

Backend courses teach correctness of APIs and asynchronous flows; cloud courses teach the platform. Production failures happen where they meet: a pod killed mid-request because shutdown was not graceful, a retry storm because timeouts were longer upstream than downstream, a connection pool multiplied by 200 autoscaled pods exhausting the database, a duplicate payment from an at-least-once event. These are design problems that need both sides.

**Demand evidence (checked October 2026).**

| Signal | Figure | Source |
|---|---|---|
| Kubernetes in production | 82% of container users run Kubernetes in production | [CNCF Annual Cloud Native Survey, Jan 2026](https://www.cncf.io/reports/the-cncf-annual-cloud-native-survey/) |
| US software developers | +10% projected 2025–35 (+174,700 jobs) | [BLS](https://www.bls.gov/ooh/computer-and-information-technology/software-developers.htm) |
| US software development postings | 78.3 on 2 Oct 2026 (1 Feb 2020 = 100), up from 64.3 a year earlier | [Indeed Hiring Lab](https://github.com/hiring-lab/job_postings_tracker) |
| Skills in AI-related postings | AWS +1,358% against a decade earlier; scalability +733%; workflow management +818% | [AI Index 2026](https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf) |
| India | Hiring shifting "from volume to skill mix"; GCC expansion driving demand | [NASSCOM 2026](https://nasscom.in/knowledge-center/publications/technology-sector-india-strategic-review-2026) |

**Analysis.** AI assistants generate CRUD handlers and Kubernetes manifests well, so those alone no longer set anyone apart ([market map](../../06_career_and_market_readiness/01_market_map/README.md)). What keeps value is the judgement around them: failure modes, consistency under retries, cost, and operating the service in production. That judgement is what this overlap trains.

## Before you start

Prerequisites for both overlap courses (from [catalog.json](../../catalog.json)): **BE301** API Design, **BE304** Asynchronous Systems, **CLD303** Containers and Kubernetes. Useful but not required: [OPS303 Observability](../../03_majors/devops_sre_platform_engineering/year_3/OPS303_observability_metrics_logs_traces/README.md), [BE303 Data Modeling and Storage for Backends](../../03_majors/backend_engineering/year_3/BE303_data_modeling_and_storage_for_backends_postgres/README.md), and [CLD401 Serverless and Event-Driven Cloud](../../03_majors/cloud_engineering/year_4/CLD401_serverless_and_event_driven_cloud/README.md) alongside OV02B for platform internals.

## How to sequence the courses

| Semester | Composed courses | Overlap course | Notes |
|---|---|---|---|
| 5 (Y3) | **BE301**, **CLD303** | — | Backend majors take CLD303 as a Year 3 elective; cloud majors take BE301 |
| 6 (Y3) | **BE304** | — | Event-driven foundations: outbox, sagas, idempotent consumers |
| 7 (Y4) | — | **OV02A** Building Cloud-Native Services | Pairs well with [BE404 Microservices, Service Mesh and Platform APIs](../../03_majors/backend_engineering/year_4/BE404_microservices_service_mesh_and_platform/README.md) for backend majors |
| 8 (Y4) | — | **OV02B** Event-Driven Serverless Backends | Cloud majors can take CLD401 in semester 7 first |
| 9–10 (Y5) | — | Capstone via [THS501](../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md)/[THS502](../../05_shared_years_3_to_5/THS502_thesis_or_capstone_ii/README.md) or [IND401](../../05_shared_years_3_to_5/IND401_industry_co_op_studio/README.md) | [BE501](../../03_majors/backend_engineering/year_5/BE501_frontier_seminar_durable_execution_serverless/README.md) extends both courses |

Division of labour, so nothing is taught twice: BE301 owns API contracts; BE304 owns messaging semantics (queues, logs, outbox, sagas); CLD303 owns how Kubernetes works. **OV02A** builds and operates long-running services on Kubernetes with those pieces; **OV02B** builds event-driven products on serverless and durable-execution platforms, and compares them with the Kubernetes path.

## The two overlap courses

| Course | Semester | What you can do at the end |
|---|---|---|
| [OV02A · Building Cloud-Native Services](OV02A_building_cloud_native_services/README.md) | 7 | Ship a service on Kubernetes that drains cleanly, scales on the right signal, degrades gracefully, has an SLO and a cost per request, and deploys by canary |
| [OV02B · Event-Driven Serverless Backends](OV02B_event_driven_serverless_backends/README.md) | 8 | Build an event-driven backend on managed brokers, functions and durable workflows with exactly-once effects, replay, tracing and a cost model per business event |

## Capstone: an order platform two ways

**Brief.** Build an illustrative food-ordering backend (orders, payments simulator, restaurant acceptance, delivery assignment, notifications) inspired by the public shape of Indian quick-commerce and food-delivery apps. Implement the core order flow as Kubernetes services (OV02A style) and the asynchronous side (notifications, settlement, analytics events, delayed refunds) as serverless functions and a durable workflow (OV02B style). Compare the two halves with measurements.

**Acceptance criteria (all measurable).**

1. **APIs and events.** OpenAPI and AsyncAPI documents exist for every public interface; a breaking-change check (oasdiff or buf) runs in CI and blocks a planted breaking change.
2. **Correctness under failure.** A fault-injection suite (pod kills, broker redelivery, duplicate webhooks, a 30-second database outage) runs 10,000 orders with zero duplicate charges, zero lost orders and every order in a terminal state within 10 minutes of the fault ending.
3. **Performance.** At 300 orders per second sustained for 15 minutes, p99 order-creation latency stays under 400 ms on a stated cluster size; autoscaling adds capacity before error rate exceeds 0.5%.
4. **Deployments.** A canary release with automated analysis rolls back a deliberately faulty version without manual action; a normal release completes with zero failed requests.
5. **Observability.** One trace follows an order from HTTP request through Kafka or the event bus, functions and the workflow; SLO dashboards and burn-rate alerts exist for two user journeys.
6. **Cost.** A cost model reports cost per 1,000 orders for the Kubernetes half and the serverless half at three traffic levels, with the break-even point explained.
7. **Security.** No static cloud keys: all cloud access uses workload identity; webhook endpoints verify HMAC signatures; images are signed.
8. **Write-up.** A design document with three architecture decision records, including one you would reverse at ten times the traffic.

## Roles it leads to

| Role | What people in it do | Entry route |
|---|---|---|
| Backend Engineer (cloud-native) / SDE-2 | Owns services end to end on Kubernetes or serverless | Direct entry after the overlap with the capstone as evidence |
| Distributed Systems Engineer | Consistency, messaging, multi-region data, resilience | Usually after a first backend role |
| Platform-minded backend / Platform API Engineer | Builds internal APIs and golden paths for other teams | Pairs with [OPS401](../../03_majors/devops_sre_platform_engineering/year_4/OPS401_platform_engineering_and_internal_developer/README.md) |
| Serverless / Event-Driven Architect (later) | Designs event-driven estates, workflow engines, cost models | After several years of building them |

A certification such as the CNCF Certified Kubernetes Application Developer (CKAD) is hands-on and carries some signal for these roles; it is optional ([BE major](../../03_majors/backend_engineering/README.md)).

## Sources

All checked 12 Oct 2026.

- CNCF, *The CNCF Annual Cloud Native Survey: The Infrastructure of AI's Future* (20 Jan 2026) — https://www.cncf.io/reports/the-cncf-annual-cloud-native-survey/
- US BLS, Software developers (2025–35) — https://www.bls.gov/ooh/computer-and-information-technology/software-developers.htm
- Indeed Hiring Lab, job postings tracker (data to 2 Oct 2026) — https://github.com/hiring-lab/job_postings_tracker
- Stanford HAI, *AI Index Report 2026* — https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf
- NASSCOM, *Technology Sector in India: Strategic Review 2026* — https://nasscom.in/knowledge-center/publications/technology-sector-india-strategic-review-2026

_Last reviewed: 2026-10_
