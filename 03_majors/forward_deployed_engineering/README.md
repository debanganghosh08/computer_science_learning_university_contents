# Forward Deployed Engineering (FDE)

| Entry requirements | Major courses | Recommended overlaps | Market and role page | Interview loop |
|---|---|---|---|---|
| [CS205](../../02_year_2_core_computer_science/semester_3/CS205_software_engineering_i_design_testing/README.md), [CS215](../../02_year_2_core_computer_science/semester_4/CS215_cloud_and_devops_foundations/README.md) | 10 (FDE301–FDE501) | OV08, OV12, OV06 | [FDE roles and market](../../06_career_and_market_readiness/01_market_map/roles/FDE_forward_deployed_engineering.md) | [AI-driven interviews](../../06_career_and_market_readiness/04_ai_driven_interviews/) |

A forward deployed engineer (FDE) is a software engineer who works with one customer, or a few, often inside their offices and systems. The FDE finds the real problem behind the request, connects the product to the customer's messy systems and data, puts it into production inside the customer's security and compliance rules, and brings what they learn back to the product team. Palantir built the model. OpenAI, Anthropic, Salesforce and AI startups in India and elsewhere now hire for it, mostly to deploy AI products. This major takes you from your first customer conversation to running deployments that matter to a business, and on to productising what you learn in the field or starting a company from it.

**How this major differs from AI Engineering.** [AI Engineering (AIE)](../ai_engineering/README.md) teaches how to build LLM applications and agents: retrieval, tool use, evaluation, LLMOps. This major assumes you can use those techniques (or learn them in AIE electives) and teaches what surrounds them in a customer deployment: discovery, integration with legacy systems and enterprise identity, data modelling across messy sources, security reviews, data residency, change management, return on investment, and operating in environments you do not control.

## 1. Who this major is for, and the roles it leads to

Choose this major if you like building things that people use the next week, can handle ambiguity, enjoy learning a new industry's vocabulary quickly, and are comfortable being the person a customer calls when something breaks. It suits engineers who would rather own a business outcome than one component. It is a poor fit if you want long uninterrupted stretches on a single codebase; consider [Software Engineering](../software_engineering/) or [Backend Engineering](../backend_engineering/README.md) instead.

| Role | What people in it actually do | Courses that matter most |
|---|---|---|
| Forward deployed engineer / forward deployed software engineer | Embed with a customer; own discovery, scoping, build and production rollout; write production code in the customer's environment; feed field patterns back to product. OpenAI's postings say FDEs "own discovery, technical scoping, system design, build, and production rollout" | FDE302, FDE303, FDE304, FDE402 |
| Deployment strategist / deployment lead | Own the customer's problem, the delivery plan, adoption and value measurement; technical but closer to product management. Palantir calls this role "Echo"; OpenAI's Deployment Leads "own value cases and ROI" and "change management for adoption" | FDE301, FDE302, FDE305, FDE403 |
| Solutions engineer / sales engineer | Support the sales process: technical discovery, demos, proofs of concept, security questionnaires; hand over to delivery after the contract | FDE302, FDE305, FDE403 |
| Solutions architect / applied AI architect | Design the customer's target architecture and integration plan; often pre-sales and senior. Anthropic's India-based Applied AI Architect roles are described as pre-sales architects who help customers "develop evaluation frameworks" | FDE303, FDE304, FDE403 |
| Implementation engineer / technical consultant | Configure, integrate and migrate a SaaS product for a customer; common at enterprise SaaS companies, systems integrators and GCCs | FDE303, FDE401, FDE402 |
| Customer engineer / technical deployment lead | Technical owner of a customer relationship after sale: onboarding, integrations, escalations, upgrades | FDE402, FDE305 |
| Forward deployed security engineer | Deploy and secure products in sensitive customer environments (OpenAI listed such a role in October 2026) | FDE304, FDE402, SEC303 |
| Field CTO / head of deployment | Senior technical leader facing a portfolio of customers; shapes product strategy from field evidence | FDE403, FDE501 |

Titles overlap and the same title means different work at different companies. In India, much customer-facing engineering work at SaaS companies, systems integrators and global capability centres (GCCs) carries titles such as solutions engineer, implementation engineer or technical consultant; no reliable counts of these roles exist. The [role page](../../06_career_and_market_readiness/01_market_map/roles/FDE_forward_deployed_engineering.md) has seniority ladders, pay proxies and demand signals.

## 2. How AI is changing this field

Everything below was checked in October 2026.

**The model started before AI, at Palantir.** Palantir's engineers are "Devs" (product) and "Deltas" (forward deployed software engineers). "Delta" comes from early Business Development teams named after NATO alphabet letters. Palantir describes the difference as "one capability, many customers" for a Dev against "one customer, many capabilities" for a Delta (Palantir blog, April 2019). Deployment strategists are called "Echos" internally; Palantir says Echos are in theory closer to product managers and Deltas more technical, but "the lines between the two roles blur heavily" (Palantir blog, March 2022).

**AI companies adopted it to close the deployment gap.** The Stanford AI Index 2026 reports that 88% of surveyed organisations use AI, but agent deployment is "in the single digits across nearly all business functions". On 12 October 2026, OpenAI's careers site returned 32 roles for "forward deployed", including FDE roles by industry (financial services, healthcare, legal), Deployment Leads, a Forward Deployed Security Engineer and roles for government. Anthropic listed FDE roles in London, Paris and Munich and Applied AI Architect roles in Bengaluru and Mumbai. Salesforce's careers site returned more than 100 results for "Forward Deployed Engineer", most of them FDE and Deployment Strategist roles for its Agentforce and Data 360 products across Europe, the Middle East, Asia-Pacific and Latin America. A venture capital analysis (a16z, June 2025) argued that AI application companies should accept lower gross margins and invest in forward deployed services to become the "system of work" inside customers.

**India.** Sarvam AI (Bengaluru) advertised an early-career Forward Deployed Software Engineer role building voice and WhatsApp agents for customers. Razorpay advertised an FDE role in August 2026 "embedded with one of Razorpay's largest merchants", explicitly modelled on Palantir's role. Indian IT services firms are training people to deploy specific AI platforms: Infosys, TCS and Wipro each committed to 10,000 Claude certifications, and Anthropic reports more than 36,000 consultants certified across more than 1,300 organisations since March 2026. Nasscom and Zinnov count 2,117 GCCs in India employing about 2.36 million people (FY26), with more than 1,200 of them having AI and machine learning capabilities. NASSCOM also reports Indian providers moving "away from FTE delivery to outcome-based, risk-sharing constructs", which rewards engineers who can deliver measurable results inside client environments.

**What is being automated.** Integration boilerplate (API clients, data mappers), first-draft scripts and SQL, documentation, and demo scaffolding. a16z's analysis notes that the best services teams automate "process mining, data pipeline automation, system integrations, and combing through API documentation". Razorpay's FDE posting expects the engineer to lean on coding agents for routine pull requests and to be "the most AI-leveraged engineer in the org".

**What is growing in value.**
- **Discovery and judgement.** A prototype now takes hours, so the bottleneck moves to knowing what to build and whether it is good enough to go live ([FDE302](year_3/FDE302_customer_discovery_and_requirements_engineering/README.md)).
- **Evaluation on the customer's own data.** OpenAI measures FDE success through "production adoption, measurable workflow impact, and eval-driven feedback that changes product and model roadmaps" ([FDE304](year_3/FDE304_deploying_ai_in_the_enterprise/README.md)).
- **Operating in production.** Only 20% of developers who use AI use it for "deploying, operating, or troubleshooting production systems" (Stack Overflow 2026), which is exactly the work an FDE owns ([FDE402](year_4/FDE402_debugging_and_operating_in_customer_environments/README.md)).
- **Trust, security and compliance.** Customers grant people, not tools, access to sensitive systems. India's DPDP Rules (November 2025) phase in obligations over 18 months, and the RBI's FREE-AI report (August 2025) recommends board-approved AI policies at regulated entities.
- **Turning field work into product.** Anthropic asks its FDEs to "identify and codify repeatable deployment patterns"; Razorpay asks for a write-up when the same thing is built for two or more merchants ([FDE501](year_5/FDE501_frontier_seminar_productizing_field_patterns/README.md)).

**Analysis.** AI makes building cheap, so the scarce work is everything around the code: understanding the customer, getting access, cleaning data, earning trust and proving value. That is why AI companies hire forward deployed engineers while AI writes more of the code.

## 3. The five-year path

### Years 1–2: the common core

Every student takes all Year 1–2 courses. The ones marked ★ matter most for this major.

| Semester | Courses (★ = most important for FDE) |
|---|---|
| 1 | ★ [FND101 Programming I (Python)](../../01_year_1_foundations/semester_1/FND101_programming_i_computational_thinking_with_python/README.md) · [FND102 How Computers Work](../../01_year_1_foundations/semester_1/FND102_how_computers_work_bits_hardware/README.md) · [FND103 Discrete Mathematics](../../01_year_1_foundations/semester_1/FND103_discrete_mathematics_for_computing/README.md) · ★ [FND104 Linux, Shell, Git](../../01_year_1_foundations/semester_1/FND104_the_developers_toolkit_linux_shell_git/README.md) · ★ [FND105 AI-Native Learning and Building](../../01_year_1_foundations/semester_1/FND105_ai_native_learning_and_building/README.md) · ★ [FND106 Technical Communication](../../01_year_1_foundations/semester_1/FND106_technical_communication_and_professional_skills/README.md) |
| 2 | ★ [FND111 Programming II (Java and TypeScript)](../../01_year_1_foundations/semester_2/FND111_programming_ii_object_oriented_and_typed/README.md) · [FND112 Data Structures and Algorithms I](../../01_year_1_foundations/semester_2/FND112_data_structures_and_algorithms_i/README.md) · [FND113 Linear Algebra and Calculus](../../01_year_1_foundations/semester_2/FND113_linear_algebra_and_calculus_for_computing/README.md) · ★ [FND114 Web Foundations](../../01_year_1_foundations/semester_2/FND114_web_foundations_http_html_css_and_javascript/README.md) · ★ [FND115 Databases I and SQL](../../01_year_1_foundations/semester_2/FND115_databases_i_data_modeling_and_sql/README.md) · ★ [FND116 Probability and Statistics I](../../01_year_1_foundations/semester_2/FND116_probability_and_statistics_i/README.md) |
| 3 | [CS201 Algorithms](../../02_year_2_core_computer_science/semester_3/CS201_algorithms_and_complexity/README.md) · [CS202 Architecture and C](../../02_year_2_core_computer_science/semester_3/CS202_computer_architecture_and_systems_programming/README.md) · ★ [CS203 Operating Systems](../../02_year_2_core_computer_science/semester_3/CS203_operating_systems/README.md) · ★ [CS204 Networks](../../02_year_2_core_computer_science/semester_3/CS204_computer_networks/README.md) · ★ [CS205 Software Engineering I](../../02_year_2_core_computer_science/semester_3/CS205_software_engineering_i_design_testing/README.md) (entry requirement) · [CS206 Mathematics for ML](../../02_year_2_core_computer_science/semester_3/CS206_mathematics_for_machine_learning/README.md) |
| 4 | ★ [CS211 Database Internals](../../02_year_2_core_computer_science/semester_4/CS211_database_systems_internals/README.md) · ★ [CS212 Distributed Systems I](../../02_year_2_core_computer_science/semester_4/CS212_distributed_systems_i/README.md) · ★ [CS213 Security Foundations](../../02_year_2_core_computer_science/semester_4/CS213_security_foundations/README.md) · ★ [CS214 Machine Learning Foundations](../../02_year_2_core_computer_science/semester_4/CS214_machine_learning_foundations/README.md) · ★ [CS215 Cloud and DevOps](../../02_year_2_core_computer_science/semester_4/CS215_cloud_and_devops_foundations/README.md) (entry requirement) · [CS216 Compilers and Interpreters](../../02_year_2_core_computer_science/semester_4/CS216_programming_languages_compilers_and_interpreters/README.md) |

Why these: FDEs write Python and TypeScript glue every day; HTTP, SQL and shell are the languages of integration; networks and operating systems are what you debug at a customer site; security foundations underlie SSO and security reviews; statistics underlie evaluation and ROI claims; ML foundations let you judge AI products; technical communication is half the job.

### Years 3–5: the major

| Year · Semester | Major courses | Shared courses | Electives and overlap slots |
|---|---|---|---|
| 3 · 5 | [FDE301 The Forward Deployed Engineer: Role, Mindset and Operating Model](year_3/FDE301_the_forward_deployed_engineer_role_mindset/README.md) · [FDE302 Customer Discovery and Requirements Engineering](year_3/FDE302_customer_discovery_and_requirements_engineering/README.md) · [FDE303 Rapid Integration Engineering](year_3/FDE303_rapid_integration_engineering_apis_legacy/README.md) | [PRO301 Ethics, Law and Responsible AI](../../05_shared_years_3_to_5/PRO301_professional_practice_ethics_law_and_responsible/README.md) | One or two of: [BE301 API Design](../backend_engineering/year_3/BE301_api_design_rest_grpc_and_graphql/README.md), [SEC303 Identity and Access Management](../cybersecurity_defense/year_3/SEC303_identity_and_access_management/README.md), [AIE302 Prompt and Context Engineering](../ai_engineering/year_3/AIE302_prompt_and_context_engineering/README.md), [AIE303 RAG and Search](../ai_engineering/year_3/AIE303_retrieval_augmented_generation_and_search/README.md), [OPS303 Observability](../devops_sre_platform_engineering/year_3/OPS303_observability_metrics_logs_traces/README.md) |
| 3 · 6 | [FDE304 Deploying AI in the Enterprise](year_3/FDE304_deploying_ai_in_the_enterprise/README.md) · [FDE305 Technical Communication in the Field](year_3/FDE305_technical_communication_in_the_field_demos/README.md) | [CAR301 Career Lab I](../../05_shared_years_3_to_5/CAR301_career_lab_i_dsa_mastery_portfolio_and_open/README.md) | Two or three of: [AIE305 Evaluating LLM Systems](../ai_engineering/year_3/AIE305_evaluating_llm_systems/README.md) (strongly recommended), [AIE304 Tool Use and Agents](../ai_engineering/year_3/AIE304_tool_use_and_ai_agents_loops_harnesses_memory/README.md), [BE304 Asynchronous Systems](../backend_engineering/year_3/BE304_asynchronous_systems_queues_streams_and_event/README.md), [DAN304 Analytics Engineering](../data_analysis/year_3/DAN304_analytics_engineering_dbt_modeling_and_semantic/README.md), [SEC305 Governance, Risk and Compliance](../cybersecurity_defense/year_3/SEC305_governance_risk_and_compliance/README.md) |
| 4 · 7 | [FDE401 Data Integration and Ontology Modeling](year_4/FDE401_data_integration_and_ontology_modeling/README.md) · [FDE402 Debugging and Operating in Customer Environments](year_4/FDE402_debugging_and_operating_in_customer_environments/README.md) | [IND401 Industry Co-op Studio](../../05_shared_years_3_to_5/IND401_industry_co_op_studio/README.md) | Overlap slot A (see §5) |
| 4 · 8 | [FDE403 Solution Architecture, Pricing and ROI](year_4/FDE403_solution_architecture_pricing_and_roi/README.md) · [FDE404 Field Studio: Three Simulated Customer Deployments](year_4/FDE404_field_studio_three_simulated_customer/README.md) | [CAR401 Career Lab II](../../05_shared_years_3_to_5/CAR401_career_lab_ii_interviews_system_design_and_ai/README.md) | Overlap slot B (see §5) |
| 5 · 9 | [FDE501 Frontier Seminar: Productizing Field Patterns and the FDE-to-Founder Path](year_5/FDE501_frontier_seminar_productizing_field_patterns/README.md) | [RES501 Research Methods](../../05_shared_years_3_to_5/RES501_research_methods_and_scientific_writing/README.md) · [RES502 Reproducing Papers](../../05_shared_years_3_to_5/RES502_reading_reproducing_and_extending_papers/README.md) · [THS501 Thesis or Capstone I](../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) | — |
| 5 · 10 | — | [THS502 Thesis or Capstone II](../../05_shared_years_3_to_5/THS502_thesis_or_capstone_ii/README.md) · [LCH502 Career Launch and Founder Studio](../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md) | Overlap courses if not yet taken |

Catalog prerequisites to watch: every Year 3 FDE course needs CS205 and CS215; FDE401 needs FDE301, FDE402 needs FDE302, FDE403 needs FDE303, FDE404 needs FDE304, and FDE501 needs FDE401 and FDE403. For the capstone, the strongest choice is a real deployment with a partner organisation from IND401, written up as a case study with measured outcomes.

## 4. Skill map by level

| Level | You can… | Where you build it | Gate (show it to move on) |
|---|---|---|---|
| L0 · Beginner | Call an API with curl, query a database, write a script that moves data from a CSV into a table | FND101, FND104, FND115 | Load a messy public CSV into Postgres with a written list of every cleaning decision |
| L1 · Foundations | Explain the FDE role and its trade-offs; run a structured user interview; integrate one REST API with retries and pagination | FND114, CS205, FDE301, first half of FDE302 and FDE303 | FDE302 P1 (interview synthesis) and FDE303 P1 (resilient connector) pass their acceptance criteria |
| L2 · Practitioner (intern-ready) | Map a real workflow, write a scoped pilot charter, integrate REST, files and SSO, and demo a working slice to a non-technical audience | FDE301–FDE305 | Mastery gates of FDE302 and FDE303; FDE305 P2 demo survives a scripted failure |
| L3 · Professional (job-ready) | Deploy an AI workflow on customer-like data with a customer-specific eval set, pass a security review, measure value against a baseline and hand over to support | FDE304, FDE401, FDE402, IND401 | FDE304 mastery gate plus the [flagship industry project](../../06_career_and_market_readiness/05_industry_projects/FDE_forward_deployed_engineering.md) |
| L4 · Expert (hard to replace) | Lead multi-month deployments end to end, design solution architectures and business cases, operate in restricted or air-gapped environments, and turn repeated field work into product | FDE402–FDE404, overlap courses | FDE404 (three deployments, graded by simulated customers) and FDE403 P3 (business case defended before a panel) |
| L5 · Research and frontier | Study deployments rigorously (case studies, field experiments), build reusable deployment platforms, or found a company from a repeated customer problem | FDE501, RES501, RES502, THS501–THS502, LCH502 | FDE501 P3 and an accepted thesis or venture proposal |

## 5. Recommended overlaps and electives

Plan an overlap in Year 3, because each overlap course has catalog prerequisites. Use the Year 3 elective slots for those prerequisites and the Year 4 overlap slots (or Year 5 Semester 10) for the overlap courses themselves.

| Overlap | Why it fits FDE | Overlap courses' prerequisites | Suggested chain |
|---|---|---|---|
| [OV08 Full-Stack AI Product Engineering](../../04_overlaps/OV08_full_stack_ai_product_engineering/) | FDEs ship whole working tools to customers: interface, backend and AI. This overlap makes you fast at the full stack | OV08A and OV08B need FE302, BE301 and AIE302 (overlap also draws on FE403, BE403, AIE404) | BE301 and AIE302 in Y3 S5, FE302 in Y3 S6 (check timetabling, since FE302 is a semester 5 course) → OV08A in Y4 S7, OV08B in Y4 S8 |
| [OV12 Agent Infrastructure and Platform Engineering](../../04_overlaps/OV12_agent_infrastructure_platform/) | Agentic deployments at customers need sandboxes, durable execution, tracing and reliability engineering | OV12A and OV12B need AIE304, OPS303 and BE304 (overlap also draws on AIE401, OPS403, BE501) | OPS303 in Y3 S5; AIE304 and BE304 in Y3 S6 → OV12A in Y4 S7, OV12B in Y4 S8 |
| [OV06 Data Platform and Analytics Engineering](../../04_overlaps/OV06_data_platform_analytics_engineering/) | Most deployments are data integration projects; this overlap adds lakehouse, modelling and semantic layer depth to FDE401 | OV06A and OV06B need DEN305, DAN304 and CLD305 | DAN304 and DEN305 in Y3 S6; CLD305 in Y4 S7 → OV06A and OV06B in Y4 S8 and Y5 S10 |

**Electives worth taking.** [AIE305 Evaluating LLM Systems](../ai_engineering/year_3/AIE305_evaluating_llm_systems/README.md) (evaluation is the most important AI skill in FDE304 and FDE404). [SEC303 Identity and Access Management](../cybersecurity_defense/year_3/SEC303_identity_and_access_management/README.md) (enterprise SSO is in almost every deployment). [SEC305 Governance, Risk and Compliance](../cybersecurity_defense/year_3/SEC305_governance_risk_and_compliance/README.md) (for banks, insurers, hospitals and government). [BE401 Payments-Grade Systems](../backend_engineering/year_4/BE401_payments_grade_systems_transactions_idempotency/README.md) (for fintech deployments; needs BE301). [SWE402 Legacy Modernization](../software_engineering/year_4/SWE402_legacy_modernization_and_refactoring_with_ai/README.md) (check its prerequisite, SWE302). [DAN302 Business Statistics and Experimentation](../data_analysis/year_3/DAN302_business_statistics_and_experimentation/README.md) (for honest ROI measurement).

## 6. Flagship industry project

The FDE flagship project is specified in [06_career_and_market_readiness/05_industry_projects/FDE_forward_deployed_engineering.md](../../06_career_and_market_readiness/05_industry_projects/FDE_forward_deployed_engineering.md). Build it after FDE304, alongside IND401, and finish it before CAR401 interviews. It is a complete deployment for a real or realistically simulated customer: discovery notes, a pilot charter, integrations, an AI workflow with a customer-specific eval set, a security review pack, a measured outcome and a handover. It draws on FDE302 P2 (discovery and pilot charter), FDE303 P2 (multi-source integration with SSO), FDE304 P2 (AI deployment with evals and security pack) and FDE401 P2 (entity resolution and canonical model). It is the main evidence for the L3 gate.

## 7. Certifications worth having (optional)

No certification exists for forward deployed engineering, and none replaces evidence of deployments you have done. Platform certifications help when an employer or its clients run on that platform, and in services firms that count certified staff. Status as of October 2026:

| Certification | Issuer | Honest value note |
|---|---|---|
| AWS Certified Solutions Architect – Associate; Microsoft Certified: Azure Solutions Architect Expert; Google Cloud Professional Cloud Architect | AWS, Microsoft, Google Cloud | Useful proof of cloud architecture vocabulary for customer conversations; pick the cloud your target customers use |
| Foundry certifications | Palantir | Palantir offers a "Foundry & AIP Builder Foundations" badge and domain certification exams. Relevant if you work at Palantir, a Palantir partner, or a customer that runs Foundry |
| Salesforce Certified Agentforce Specialist | Salesforce | Relevant for Agentforce deployment roles at Salesforce, its partners and customers |
| Claude certifications (Associate, Developer, Architect) | Anthropic | Exams are open only to members of the Claude Partner Network (free membership for firms). Large Indian services firms have committed to certify thousands of staff, so they carry weight at those employers |

## 8. The interview loop

FDE loops are not standardised. What companies publicly state: OpenAI says skills assessments "may include: pair coding interviews, take-home projects, technical tests", that rules on AI tools vary by interview, and that final rounds typically take 4–6 hours with 4–6 people. Anthropic's guidance says live interviews are without AI assistance unless stated. OpenAI's Tokyo FDE role interviews in both Japanese and English. Candidate reports widely describe a "decomposition" interview at Palantir, in which you break down a vague real-world problem live; Palantir's own pages do not describe it (unconfirmed).

| Round | What happens | Prepared by |
|---|---|---|
| Coding | Practical coding, sometimes with AI allowed and sometimes forbidden | CAR301, FDE303 labs |
| Decomposition or case | A vague goal ("reduce hospital discharge delays"); you ask questions, define the problem, propose data, a plan and success metrics | FDE302, FDE301 |
| Integration or build exercise | Connect to an unfamiliar API or dataset and produce something working in limited time | FDE303, FDE401 |
| Customer role-play | An interviewer plays a sceptical customer, an IT security lead or an executive; you handle objections and explain trade-offs | FDE305, FDE304 |
| System design under constraints | Legacy systems, SSO, data residency, on-premises or restricted networks | FDE402, FDE403 |
| Written communication | A short design note, status update or executive summary | FDE305 |
| Behavioural | Ambiguity, travel, ownership, a deployment that went wrong | FDE301, IND401 |

Full simulations and question banks are in [04_ai_driven_interviews](../../06_career_and_market_readiness/04_ai_driven_interviews/). Every course README in this major lists five interview questions with what a strong answer covers.

## 9. Fast track for working professionals

Pick the track that matches your background. Each assumes 10–12 hours a week and uses course projects as checkpoints. Everyone does the AI-off drills: interviews and customer sites do not let you outsource understanding.

**From software engineering (backend, full-stack, data), 20 weeks.** You can build; you need customer skills and enterprise context. Skip the Year 1–2 core if you pass the CS205 and CS215 mastery gates.

| Weeks | Do | Checkpoint |
|---|---|---|
| 1–2 | FDE301 Chapters 1–4 and 8 | A written engagement plan for an illustrative customer |
| 3–6 | FDE302 Chapters 1–5 and 8 | FDE302 P1 (five real user interviews synthesised) |
| 7–9 | FDE303 Chapters 6, 7 and 9–11 (files, legacy databases, SSO, India integrations) | FDE303 P2 |
| 10–13 | FDE304 all chapters; AIE305 Chapters 2–5 | FDE304 P2 with a customer-specific golden set |
| 14–15 | FDE305 Chapters 2, 4 and 6 | A recorded demo with a scripted failure and recovery |
| 16–20 | [Flagship project](../../06_career_and_market_readiness/05_industry_projects/FDE_forward_deployed_engineering.md) | Public write-up with measured outcome |

**From consulting or business analysis, 28 weeks.** You can run discovery and talk to executives; you need engineering depth. Start with the [FND115](../../01_year_1_foundations/semester_2/FND115_databases_i_data_modeling_and_sql/README.md), [FND114](../../01_year_1_foundations/semester_2/FND114_web_foundations_http_html_css_and_javascript/README.md) and [CS205](../../02_year_2_core_computer_science/semester_3/CS205_software_engineering_i_design_testing/README.md) mastery gates (8 weeks), then FDE303 in full (6 weeks), FDE304 (5 weeks), FDE401 Chapters 2–5 (4 weeks) and the flagship project (5 weeks). Skim FDE302 and FDE305, but do their projects.

**From support, implementation or customer success engineering, 24 weeks.** You know customers and production incidents; you need to own builds and AI deployments. Do FDE303 Chapters 2–5 and 9 (5 weeks), FDE304 (5 weeks), AIE303 and AIE305 core chapters (5 weeks), FDE401 Chapters 4–6 (3 weeks), FDE403 Chapters 4–6 (2 weeks), then the flagship project (4 weeks). Your FDE402 experience counts: write two incident case studies from your past work (anonymised, with your employer's permission) as portfolio evidence.

## Sources

- Palantir, "Dev versus Delta: Demystifying engineering roles at Palantir" (8 Apr 2019) — https://blog.palantir.com/dev-versus-delta-demystifying-engineering-roles-at-palantir-ad44c2a6e87 (checked 2026-10)
- Palantir, "A Day in the Life of a Palantir Deployment Strategist" (8 Mar 2022) — https://blog.palantir.com/a-day-in-the-life-of-a-palantir-deployment-strategist-951cb59a5a96 (checked 2026-10)
- OpenAI careers: search for "forward deployed" (32 roles, 12 Oct 2026) — https://openai.com/careers/search/?q=forward%20deployed ; Forward Deployed Engineer, Tokyo — https://openai.com/careers/forward-deployed-engineer-tokyo/ ; Deployment Lead, FDE, San Francisco — https://openai.com/careers/deployment-lead-fde-sf-san-francisco/ ; interview guide — https://openai.com/interview-guide/ (checked 2026-10)
- Anthropic job board (Greenhouse), 12 Oct 2026: Forward Deployed Engineer, London — https://job-boards.greenhouse.io/anthropic/jobs/5423029008 ; Applied AI Architect, Bangalore — https://job-boards.greenhouse.io/anthropic/jobs/5390746008 ; candidate AI guidance — https://www.anthropic.com/candidate-ai-guidance (checked 2026-10)
- Salesforce careers search "Forward Deployed Engineer" (12 Oct 2026) — https://salesforce.wd12.myworkdayjobs.com/External_Career_Site (checked 2026-10)
- a16z (Joe Schmidt), "Trading Margin for Moat: Why the Forward Deployed Engineer Is the Hottest Job in Startups" (4 Jun 2025) — https://a16z.com/services-led-growth/ (checked 2026-10)
- Sarvam AI, Forward Deployed Software Engineer — https://careers.kula.ai/sarvam-ai/17986 ; Razorpay, Forward Deployed Engineer (Bengaluru, Aug 2026; closed by Oct 2026) — https://portfoliojobs.tcv.com/companies/razorpay/jobs/89918935-forward-deployed-engineer (checked 2026-10)
- Anthropic, "Four role-based certifications for the people who put Claude to work for customers" (2026) — https://claude.com/resources/articles/four-role-based-claude-certifications (checked 2026-10)
- Nasscom–Zinnov, GCC Value Orbit (July 2026), as reported by The Tribune — https://www.tribuneindia.com/news/business/india-s-gccs-are-increasingly-leading-the-ai-mandate-for-global-enterprises-driving-global-value-creation-nasscom-zinnov-report/ ; NASSCOM Strategic Review 2026 — https://nasscom.in/knowledge-center/publications/technology-sector-india-strategic-review-2026 (checked 2026-10)
- Stanford HAI, AI Index 2026 — https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf ; Stack Overflow, 2026 survey results blog (6 Oct 2026) — https://stackoverflow.blog/2026/10/06/the-results-of-the-2026-developer-survey-are-here/ (checked 2026-10)
- PIB, DPDP Rules 2025 — https://www.pib.gov.in/PressReleasePage.aspx?PRID=2190014 ; RBI, FREE-AI Committee report (13 Aug 2025) — https://rbidocs.rbi.org.in/rdocs/PublicationReport/Pdfs/FREEAIR130820250A24FF2D4578453F824C72ED9F5D5851.PDF (checked 2026-10)
- Certifications: AWS — https://aws.amazon.com/certification/certified-solutions-architect-associate/ ; Microsoft — https://learn.microsoft.com/en-us/credentials/certifications/azure-solutions-architect/ ; Google Cloud — https://cloud.google.com/learn/certification/cloud-architect ; Palantir — https://learn.palantir.com/ ; Salesforce — https://trailhead.salesforce.com/credentials/agentforcespecialist (checked 2026-10)

_Last reviewed: 2026-10_
