# AI Engineering: LLM Applications and Agents (AIE)

| Entry requirements | Major courses | Recommended overlaps | Market and role page | Interview loop |
|---|---|---|---|---|
| [CS214](../../02_year_2_core_computer_science/semester_4/CS214_machine_learning_foundations/README.md), [CS205](../../02_year_2_core_computer_science/semester_3/CS205_software_engineering_i_design_testing/README.md) | 10 (AIE301–AIE501) | OV05, OV08, OV12, OV04 | [AIE roles and market](../../06_career_and_market_readiness/01_market_map/roles/AIE_ai_engineering.md) | [AI-driven interviews](../../06_career_and_market_readiness/04_ai_driven_interviews/) |

AI engineers build products and systems on top of foundation models: assistants that answer from company knowledge, agents that use tools and finish multi-step tasks, and the evaluation, security, cost and operations work that makes them dependable. This major takes you from your first API call to designing agent platforms, shipping AI products to real users, and doing research on long-horizon agents and agent safety.

## 1. Who this major is for, and the roles it leads to

Choose this major if you like building software that people use, enjoy working with uncertain, probabilistic components, and want to work with models mostly through APIs and post-training rather than inventing new architectures. If you want to train models from scratch or research architectures, look at [Deep Learning (DLR)](../deep_learning/). If you want classical ML pipelines and model deployment, look at [Machine Learning Engineering (MLE)](../machine_learning_engineering/). If you want to deploy AI inside customer organisations, look at [Forward Deployed Engineering (FDE)](../forward_deployed_engineering/). The boundaries are porous, and the overlaps below connect them.

| Role | What people in it actually do | Courses that matter most |
|---|---|---|
| AI engineer / LLM application engineer | Build features on LLM APIs: prompts and context, retrieval, structured outputs, streaming UIs, evals, cost control | AIE301–AIE305, AIE403 |
| Agent engineer | Build tool-using agents and their harnesses: tools, sandboxes, permissions, memory, durable execution, MCP integrations | AIE304, AIE401, AIE501 |
| Applied AI engineer | Work with customers or internal teams to solve a domain problem with models, often at model companies; prototype fast, then harden | AIE302–AIE305, AIE404, FDE electives |
| AI solutions engineer / AI architect | Design AI solutions for clients: model choice, data flows, security, compliance, cost; lead pilots | AIE301, AIE401, AIE403, PRO301 |
| AI evaluation engineer | Build golden sets, graders, judges, regression suites, red-team programmes; own the release gate | AIE305, OV05, OV12B |
| AI platform engineer | Run the shared layer: gateways, tracing, guardrails, model registries, agent infrastructure | AIE403, OV12, OV04 |
| AI product engineer | Full-stack builders who own an AI feature from problem to metrics | AIE404, OV08 |

Seniority runs from entry titles (AI Engineer I, Software Engineer – AI features) to staff and principal AI engineer or head of applied AI. See the [role page](../../06_career_and_market_readiness/01_market_map/roles/AIE_ai_engineering.md) for titles, pay proxies and demand signals.

## 2. How AI is changing this field

Everything below was checked in October 2026.

**Demand is real and shifting toward agents.** LinkedIn's US "Jobs on the Rise" list ranked AI engineer first in both 2025 and 2026. The Stanford AI Index 2026 reports that mentions of generative AI skills in US AI job postings grew 111% from 2024 to 2025. Postings that mention AI agents and agentic systems rose sharply, while mentions of chatbots declined.

**Adoption runs ahead of deployment.** The AI Index reports organisational AI use at 88%, but agent deployment "in the single digits across nearly all business functions". In the 2026 Stack Overflow survey, 26.2% of developers used AI agents or automated workflows at work. Closing that gap safely is this major's job.

**What is being automated.** AI coding assistants and agent SDKs generate glue code, API clients, basic RAG pipelines, framework boilerplate, prompt drafts and synthetic test data. Managed services cover retrieval, tracing and evaluation. A demo that took a team weeks in 2023 now takes an afternoon.

**What is growing in value.**
- **Evaluation.** Anthropic estimated that about 49% of API tasks and about 61% of software-development requests to Claude succeed (Jan 2026). Measuring and raising real success rates is the core skill ([AIE305](year_3/AIE305_evaluating_llm_systems/README.md)).
- **Reliability of long-running agents.** On METR's tasks, the best model measured in early 2026 succeeds half the time on tasks that take a human expert about 12 hours, but at 80% reliability the horizon is about 70 minutes. Long runs need checkpoints, verification and recovery ([AIE304](year_3/AIE304_tool_use_and_ai_agents_loops_harnesses_memory/README.md), [AIE501](year_5/AIE501_frontier_seminar_long_horizon_autonomous_agents/README.md)).
- **Security.** Prompt injection is first and excessive agency sixth in the OWASP Top 10 for LLM Applications 2025, and OWASP published a separate Top 10 for Agentic Applications in December 2025.
- **Cost, latency and operations.** Batch discounts, prompt caching and routing move bills by large factors; production incidents and legal liability (Moffatt v. Air Canada, 2024) make operations a discipline ([AIE403](year_4/AIE403_llmops_observability_guardrails_cost_and_latency/README.md)).
- **Product judgement.** Knowing when not to use a model, and measuring value honestly ([AIE404](year_4/AIE404_ai_product_engineering_and_ux/README.md)).

**Platforms churn, so concepts come first.** In the past year alone, OpenAI shut down its Assistants API (26 Aug 2026) and began winding down its self-serve fine-tuning platform (May 2026). The MCP specification moved to a stateless design (2026-07-28 revision), and Claude models stopped accepting prefilled responses and manual thinking budgets. Every course here teaches the concept first and the tool as one current example of it.

**India.** The IndiaAI Mission was approved in March 2024 with ₹10,371.92 crore over five years, and Sarvam AI was selected in April 2025 to build a sovereign LLM. Coding is over half of Claude usage in India against roughly a third globally (Anthropic, Sept 2025). Razorpay, NPCI and OpenAI piloted agentic UPI payments in ChatGPT in October 2025. The DPDP Rules, notified in November 2025, phase in most obligations over 18 months. Multilingual, voice-first and payments-adjacent AI products are where Indian AI engineers can lead.

## 3. The five-year path

### Years 1–2: the common core

Every student takes all Year 1–2 courses. The ones marked ★ matter most for this major; give them extra time.

| Semester | Courses (★ = most important for AIE) |
|---|---|
| 1 | ★ [FND101 Programming I (Python)](../../01_year_1_foundations/semester_1/FND101_programming_i_computational_thinking_with_python/README.md) · [FND102 How Computers Work](../../01_year_1_foundations/semester_1/FND102_how_computers_work_bits_hardware/README.md) · [FND103 Discrete Mathematics](../../01_year_1_foundations/semester_1/FND103_discrete_mathematics_for_computing/README.md) · ★ [FND104 Linux, Shell, Git](../../01_year_1_foundations/semester_1/FND104_the_developers_toolkit_linux_shell_git/README.md) · ★ [FND105 AI-Native Learning and Building](../../01_year_1_foundations/semester_1/FND105_ai_native_learning_and_building/README.md) · [FND106 Technical Communication](../../01_year_1_foundations/semester_1/FND106_technical_communication_and_professional_skills/README.md) |
| 2 | ★ [FND111 Programming II (Java and TypeScript)](../../01_year_1_foundations/semester_2/FND111_programming_ii_object_oriented_and_typed/README.md) · [FND112 Data Structures and Algorithms I](../../01_year_1_foundations/semester_2/FND112_data_structures_and_algorithms_i/README.md) · [FND113 Linear Algebra and Calculus](../../01_year_1_foundations/semester_2/FND113_linear_algebra_and_calculus_for_computing/README.md) · ★ [FND114 Web Foundations](../../01_year_1_foundations/semester_2/FND114_web_foundations_http_html_css_and_javascript/README.md) · ★ [FND115 Databases I and SQL](../../01_year_1_foundations/semester_2/FND115_databases_i_data_modeling_and_sql/README.md) · ★ [FND116 Probability and Statistics I](../../01_year_1_foundations/semester_2/FND116_probability_and_statistics_i/README.md) |
| 3 | [CS201 Algorithms](../../02_year_2_core_computer_science/semester_3/CS201_algorithms_and_complexity/README.md) · [CS202 Architecture and C](../../02_year_2_core_computer_science/semester_3/CS202_computer_architecture_and_systems_programming/README.md) · [CS203 Operating Systems](../../02_year_2_core_computer_science/semester_3/CS203_operating_systems/README.md) · [CS204 Networks](../../02_year_2_core_computer_science/semester_3/CS204_computer_networks/README.md) · ★ [CS205 Software Engineering I](../../02_year_2_core_computer_science/semester_3/CS205_software_engineering_i_design_testing/README.md) (entry requirement) · ★ [CS206 Mathematics for ML](../../02_year_2_core_computer_science/semester_3/CS206_mathematics_for_machine_learning/README.md) |
| 4 | ★ [CS211 Database Internals](../../02_year_2_core_computer_science/semester_4/CS211_database_systems_internals/README.md) · ★ [CS212 Distributed Systems I](../../02_year_2_core_computer_science/semester_4/CS212_distributed_systems_i/README.md) · ★ [CS213 Security Foundations](../../02_year_2_core_computer_science/semester_4/CS213_security_foundations/README.md) · ★ [CS214 Machine Learning Foundations](../../02_year_2_core_computer_science/semester_4/CS214_machine_learning_foundations/README.md) (entry requirement) · ★ [CS215 Cloud and DevOps](../../02_year_2_core_computer_science/semester_4/CS215_cloud_and_devops_foundations/README.md) · [CS216 Compilers and Interpreters](../../02_year_2_core_computer_science/semester_4/CS216_programming_languages_compilers_and_interpreters/README.md) |

Why these: Python and TypeScript are the languages of AI applications; SQL and database internals underlie retrieval and vector indexes; probability and statistics underlie evaluation; distributed systems underlie durable agents; security underlies every agent permission decision; cloud and DevOps underlie LLMOps.

### Years 3–5: the major

| Year · Semester | Major courses | Shared courses | Electives and overlap slots |
|---|---|---|---|
| 3 · 5 | [AIE301 LLM Fundamentals for Engineers](year_3/AIE301_llm_fundamentals_for_engineers/README.md) · [AIE302 Prompt and Context Engineering](year_3/AIE302_prompt_and_context_engineering/README.md) · [AIE303 RAG and Search](year_3/AIE303_retrieval_augmented_generation_and_search/README.md) | [PRO301 Ethics, Law and Responsible AI](../../05_shared_years_3_to_5/PRO301_professional_practice_ethics_law_and_responsible/README.md) | One of: OPS303, BE303, FE303, DLR303, SAR303 (start of an overlap chain, see §5) |
| 3 · 6 | [AIE304 Tool Use and AI Agents](year_3/AIE304_tool_use_and_ai_agents_loops_harnesses_memory/README.md) · [AIE305 Evaluating LLM Systems](year_3/AIE305_evaluating_llm_systems/README.md) | [CAR301 Career Lab I](../../05_shared_years_3_to_5/CAR301_career_lab_i_dsa_mastery_portfolio_and_open/README.md) | One or two of: BE304, FDE304, SEC305, MLE304, CLD304 |
| 4 · 7 | [AIE401 Multi-Agent Systems, MCP and Orchestration](year_4/AIE401_multi_agent_systems_mcp_and_orchestration/README.md) · [AIE402 Fine-Tuning and Small Models](year_4/AIE402_fine_tuning_and_small_models_for_products/README.md) | [IND401 Industry Co-op Studio](../../05_shared_years_3_to_5/IND401_industry_co_op_studio/README.md) | Overlap slot A (see §5) |
| 4 · 8 | [AIE403 LLMOps](year_4/AIE403_llmops_observability_guardrails_cost_and_latency/README.md) · [AIE404 AI Product Engineering and UX](year_4/AIE404_ai_product_engineering_and_ux/README.md) | [CAR401 Career Lab II](../../05_shared_years_3_to_5/CAR401_career_lab_ii_interviews_system_design_and_ai/README.md) | Overlap slot B (see §5) |
| 5 · 9 | [AIE501 Frontier Seminar: Long-Horizon Agents and Agent Safety](year_5/AIE501_frontier_seminar_long_horizon_autonomous_agents/README.md) | [RES501 Research Methods](../../05_shared_years_3_to_5/RES501_research_methods_and_scientific_writing/README.md) · [RES502 Reproducing Papers](../../05_shared_years_3_to_5/RES502_reading_reproducing_and_extending_papers/README.md) · [THS501 Thesis or Capstone I](../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) | — |
| 5 · 10 | — | [THS502 Thesis or Capstone II](../../05_shared_years_3_to_5/THS502_thesis_or_capstone_ii/README.md) · [LCH502 Career Launch and Founder Studio](../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md) | Overlap courses if not yet taken; or electives such as DLR401 or DLR403 |

Catalog prerequisites to watch: AIE401 needs AIE301, AIE402 needs AIE302, AIE403 needs AIE303, AIE404 needs AIE304, and AIE501 needs AIE401 and AIE403. Every Year 3 AIE course needs CS214 and CS205.

## 4. Skill map by level

| Level | You can… | Where you build it | Gate (show it to move on) |
|---|---|---|---|
| L0 · Beginner | Call a model through a chat UI and an SDK by following examples | FND101, FND105 | Run a provided script that calls an API and explain each line |
| L1 · Foundations | Explain tokens, sampling, embeddings and costs; write a spec-first prompt; build BM25 and a basic RAG demo | CS214, AIE301–AIE303 (first half) | AIE301 P1 and AIE303 P1 pass their acceptance criteria |
| L2 · Practitioner (intern-ready) | Build a streaming, tool-calling, structured-output client from raw HTTP; hybrid RAG with citations; a sandboxed agent with budgets; a golden set with agreement | AIE301–AIE305 | Mastery gates of AIE301 and AIE303; AIE304 P1 runs in a sandbox with traces |
| L3 · Professional (job-ready) | Ship permission-safe RAG and durable agents with calibrated evals in CI, cost and latency budgets, and an honest launch decision | AIE304, AIE305, AIE401, AIE403, IND401 | AIE305 mastery gate plus the [flagship industry project](../../06_career_and_market_readiness/05_industry_projects/AIE_ai_engineering.md) |
| L4 · Expert (hard to replace) | Design agent platforms (MCP gateways, identity, policy, tracing), run AI incidents, make fine-tune and model-routing investment calls, and ship AI products that measurably help users | AIE401–AIE404, overlap courses | AIE401 P3 and AIE403 P3 (game-day operations) |
| L5 · Research | Reproduce and extend frontier agent results; design rigorous agent evaluations and control protocols | AIE501, RES501, RES502, THS501–THS502 | AIE501 P3 reproduction and an accepted thesis proposal |

## 5. Recommended overlaps and electives

Real AI jobs sit between fields. Pick one overlap, and plan its component courses early. The catalog lists each overlap's component courses as prerequisites of its two overlap courses, and several of those run in Year 4 Semester 8 or later. So start the chain in Year 3, use the Year 4 overlap slots for component courses, and take the overlap courses (A and B) when their prerequisites are done: in Year 4 with instructor approval of co-requisites, or in Year 5 Semester 10.

| Overlap | Why it fits AIE | Component courses (prerequisites) | Chain to start in Year 3 |
|---|---|---|---|
| [OV05 AI Security and Safety Engineering](../../04_overlaps/OV05_ai_security_safety/) | Injection, excessive agency and agent misuse are the top risks in AI products; security-literate AI engineers are scarce | AIE305, OFF403, SAR403 | OFF303 or SAR303 in Y3 S5 → OFF403 or SAR403 in Y4 S8 |
| [OV08 Full-Stack AI Product Engineering](../../04_overlaps/OV08_full_stack_ai_product_engineering/) | Most AI value is delivered as product features: streaming UIs, backends for AI, analytics | FE403, BE403, AIE404 | FE303 and BE303 in Y3 S5 → FE403 and BE403 in Y4 S8 |
| [OV12 Agent Infrastructure and Platform Engineering](../../04_overlaps/OV12_agent_infrastructure_platform/) | Agents in production need sandboxes, durable execution, observability and reliability engineering | AIE401, OPS403, BE501 | OPS303 in Y3 S5 → OPS403 in Y4 S8; BE501 needs BE401 and BE403, so this overlap usually completes in Year 5 |
| [OV04 MLOps and ML Platform Engineering](../../04_overlaps/OV04_mlops_ml_platform/) | For AI engineers who want to own model serving, GPUs and LLMOps at platform scale | MLE401, OPS401, CLD404 | MLE301, OPS301 and CLD304 in Year 3 → MLE401, OPS401, CLD404 in Year 4 (heavy; plan with an adviser) |

**Electives worth taking.** [DLR303 Sequence Models and Transformers](../deep_learning/year_3/DLR303_sequence_models_and_transformers/README.md) (to understand the models you build on). [OPS303 Observability](../devops_sre_platform_engineering/year_3/OPS303_observability_metrics_logs_traces/README.md) (feeds AIE403). [BE304 Asynchronous Systems](../backend_engineering/year_3/BE304_asynchronous_systems_queues_streams_and_event/README.md) (queues and durable workflows for agents). [FDE304 Deploying AI in the Enterprise](../forward_deployed_engineering/year_3/FDE304_deploying_ai_in_the_enterprise/README.md) (customer-facing deployment). [SEC305 Governance, Risk and Compliance](../cybersecurity_defense/year_3/SEC305_governance_risk_and_compliance/README.md) (for regulated sectors). [DLR401 Large Language Models](../deep_learning/year_4/DLR401_large_language_models_pretraining_fine_tuning/README.md) and [DLR403 RL for Language Models](../deep_learning/year_4/DLR403_reinforcement_learning_including_rl_for_language/README.md) (for post-training depth after AIE402; check their prerequisites).

## 6. Flagship industry project

The AI Engineering flagship project is specified in [06_career_and_market_readiness/05_industry_projects/AIE_ai_engineering.md](../../06_career_and_market_readiness/05_industry_projects/AIE_ai_engineering.md). Build it after AIE305, in parallel with IND401, and finish it before CAR401 interviews. It is the main piece of evidence for the L3 gate. It draws on the projects of this major: AIE303 P2 (permission-aware RAG), AIE304 P2 (durable agent with approvals), AIE305 P2 (calibrated judges and a CI gate) and AIE403 P2 (gateway, budgets and failover).

## 7. Certifications worth having (optional)

No certification is required, and none replaces a portfolio. Hiring for AI engineering roles mostly tests what you can build and explain (see §8). Certifications help in two situations: services and consulting firms (common in India) that staff cloud AI projects and count certified engineers, and enterprise roles tied to one cloud platform. Status as of October 2026:

| Certification | Issuer | Honest value note |
|---|---|---|
| AWS Certified Generative AI Developer – Professional (AIP-C01) | AWS | The most directly relevant cloud certification for building generative AI applications on AWS; standard exam since the beta closed in March 2026 (180 min, US$300). Worth it if your employer or clients are on AWS. |
| Microsoft Certified: Azure AI Apps and Agents Developer Associate (AI-103) | Microsoft | Replaced the retired Azure AI Engineer Associate (AI-102, retired June 2026). Useful for Microsoft-centric enterprises and services firms. |
| Google Cloud Professional Machine Learning Engineer | Google Cloud | Covers generative AI on Google Cloud as part of a broader ML exam. Google's Generative AI Leader certification is non-technical and adds little for engineers. |
| Databricks Certified Generative AI Engineer Associate | Databricks | Useful if you work in Databricks-based data platforms building RAG and agents over enterprise data. |
| NVIDIA-Certified Associate: Generative AI LLMs (NCA-GENL) | NVIDIA | Entry-level; signals familiarity with LLM concepts and NVIDIA tooling. The professional-level exam was listed as "coming soon" in October 2026. |
| Claude certifications (Associate, Developer, Architect) | Anthropic | Launched in 2026 and open only to members of the Claude Partner Network (free membership). Relevant if you work at a partner firm delivering Claude-based solutions. |

Free learning with certificates of completion: Anthropic Academy courses, Hugging Face LLM, Agents and MCP courses, and DeepLearning.AI short courses. They are good for learning, but they carry little weight as hiring signals on their own.

## 8. The interview loop

The loop for AI engineering roles is still settling. A typical loop, with the course that prepares each round:

| Round | What happens | Prepared by |
|---|---|---|
| Coding | DSA or practical coding, sometimes with AI tools allowed (Canva requires them) and sometimes forbidden (Anthropic forbids AI in live interviews unless stated) | CAR301, CS201 |
| LLM application design | "Design a support assistant over 50,000 documents" or "an agent that files expense reports": retrieval, tools and permissions, evaluation, failure handling, cost and latency | AIE303, AIE304, AIE401, AIE403 |
| Practical or take-home | Build a small RAG or agent system with an eval set and report results honestly | AIE305, flagship project |
| Debugging | Find the cause of a failing agent or RAG system from traces | AIE304 Lab 10, AIE403 |
| Product and behavioural | When not to use an LLM, measuring value, handling an incident | AIE404, IND401 |

Full simulations and question banks are in [04_ai_driven_interviews](../../06_career_and_market_readiness/04_ai_driven_interviews/), and every course README in this major lists five interview questions with what a strong answer covers.

## 9. Fast track for working developers

For software engineers who already ship production code (backend, frontend, data or mobile) and can give 10–12 hours a week. Skip the Year 1–2 core if you can pass the [CS205](../../02_year_2_core_computer_science/semester_3/CS205_software_engineering_i_design_testing/README.md) and [CS214](../../02_year_2_core_computer_science/semester_4/CS214_machine_learning_foundations/README.md) mastery gates. Then follow this 24-week plan, using each course's labs and projects as checkpoints:

| Weeks | Focus | Do these | Checkpoint |
|---|---|---|---|
| 1–3 | Model and API fundamentals | AIE301 Chapters 1–3 and 6–8 | AIE301 P2 (raw-HTTP client) passes |
| 4–6 | Prompts and context | AIE302 Chapters 1, 2, 5, 6, 9, 10 | AIE302 P1 meets its accuracy targets |
| 7–10 | Retrieval | AIE303 Chapters 1–4, 7–9 | AIE303 P2 (permission-aware RAG) |
| 11–14 | Agents | AIE304 Chapters 1, 2, 4, 5, 8, 9 | AIE304 P2 (durable agent, zero duplicate side effects) |
| 15–17 | Evaluation | AIE305 Chapters 2, 3, 5, 6, 7 | AIE305 P2 (calibrated judge + CI gate) |
| 18–20 | Protocols and operations | AIE401 Chapters 1–4; AIE403 Chapters 2, 4, 5, 7 | An OAuth-protected MCP server and a gateway with budgets |
| 21–24 | Flagship project | [AIE flagship project](../../06_career_and_market_readiness/05_industry_projects/AIE_ai_engineering.md) | Public repo, eval report, demo, written trade-offs |

**Shortcuts by background.** Backend developers can skim AIE301 Chapter 6 and AIE403 Chapter 7, and should spend the saved time on AIE305. Frontend developers should add AIE404 Chapters 3–6 and the [FE403](../frontend_engineering/year_4/FE403_ai_native_interfaces_streaming_generative_ui/README.md) syllabus. Data scientists can skim AIE305 Chapter 6 and AIE301 Chapter 4, and should spend extra time on AIE304 Chapters 5 and 8 (sandboxes and durability), which are usually new to them. Everyone should do the AI-off drills in each course: interviews and production incidents do not let you outsource understanding.

## Sources

- LinkedIn News, "Jobs on the Rise 2026: the 25 fastest-growing roles in the US" (Jan 2026) — https://www.linkedin.com/pulse/linkedin-jobs-rise-2026-25-fastest-growing-roles-us-linkedin-news-dlb1c ; 2025 list — https://www.linkedin.com/pulse/linkedin-jobs-rise-2025-25-fastest-growing-us-linkedin-news-gryie (checked 2026-10)
- Stanford HAI, AI Index 2026 (postings, adoption, agent deployment) — https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf (checked 2026-10)
- Stack Overflow Developer Survey 2026, AI section — https://survey.stackoverflow.co/2026/ai/data (checked 2026-10)
- Anthropic Economic Index (Jan 2026; Sept 2025) — https://www.anthropic.com/research/anthropic-economic-index-january-2026-report ; https://www.anthropic.com/research/anthropic-economic-index-september-2025-report (checked 2026-10)
- METR benchmark results v1.1 — https://metr.org/assets/benchmark_results_1_1.yaml (checked 2026-10)
- OWASP Top 10 for LLM Applications 2025 — https://genai.owasp.org/llm-top-10/ ; OWASP Top 10 for Agentic Applications (Dec 2025) — https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/ (checked 2026-10)
- OpenAI Assistants API migration (sunset 26 Aug 2026) — https://developers.openai.com/api/docs/assistants/migration ; OpenAI deprecations (fine-tuning notice, May 2026) — https://developers.openai.com/api/docs/deprecations ; MCP specification 2026-07-28 — https://modelcontextprotocol.io/specification/2026-07-28 ; Anthropic prompting best practices — https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices (checked 2026-10)
- CTV News on Moffatt v. Air Canada (Feb 2024) — https://www.ctvnews.ca/vancouver/article/air-canadas-chatbot-gave-a-bc-man-the-wrong-information-now-the-airline-has-to-pay-for-the-mistake/ (checked 2026-10)
- PIB, IndiaAI Mission approval (Mar 2024) — https://www.pib.gov.in/PressReleaseIframePage.aspx?PRID=2012355 ; Sarvam, "India's sovereign LLM" (Apr 2025) — https://www.sarvam.ai/blogs/indias-sovereign-llm ; Razorpay agentic payments (Oct 2025) — https://razorpay.com/newsroom/razorpay-npci-and-openai-come-together-to-launch-agentic-payments-ushering-in-ai-driven-commerce-at-national-scale/ ; PIB, DPDP Rules 2025 — https://www.pib.gov.in/PressReleasePage.aspx?PRID=2190014 (checked 2026-10)
- Certifications: AWS AIP-C01 — https://aws.amazon.com/certification/certified-generative-ai-developer-professional/ ; Microsoft AI-102 retirement — https://learn.microsoft.com/en-us/credentials/certifications/azure-ai-engineer/ ; Microsoft AI-103 — https://learn.microsoft.com/en-us/credentials/certifications/azure-ai-apps-and-agents-developer-associate/ ; Google Cloud PMLE — https://cloud.google.com/learn/certification/machine-learning-engineer ; Generative AI Leader — https://cloud.google.com/learn/certification/generative-ai-leader ; Databricks — https://www.databricks.com/learn/certification/genai-engineer-associate ; NVIDIA NCA-GENL — https://www.nvidia.com/en-us/learn/certification/generative-ai-llm-associate/ ; Anthropic, role-based Claude certifications — https://claude.com/resources/articles/four-role-based-claude-certifications ; Anthropic Academy — https://anthropic.skilljar.com/ (checked 2026-10)
- Canva, "Yes, You Can Use AI in Our Interviews" (Jun 2025) — https://www.canva.dev/blog/engineering/yes-you-can-use-ai-in-our-interviews/ ; Anthropic candidate AI guidance — https://www.anthropic.com/candidate-ai-guidance (checked 2026-10)

_Last reviewed: 2026-10_
