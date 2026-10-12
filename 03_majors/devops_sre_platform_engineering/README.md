# DevOps, SRE and Platform Engineering (OPS)

**The major for people who want to keep software running: shipping it safely, watching it, fixing it under pressure, and building the platforms and automation that let everyone else move fast.**

| Entry requirements | Major courses | Market and roles | Interview loop |
|---|---|---|---|
| [CS215](../../02_year_2_core_computer_science/semester_4/CS215_cloud_and_devops_foundations/README.md), [CS203](../../02_year_2_core_computer_science/semester_3/CS203_operating_systems/README.md) | OPS301–305, OPS401–404, OPS501 | [OPS market page](../../06_career_and_market_readiness/01_market_map/roles/OPS_devops_sre_platform_engineering.md) | [AI-driven interviews](../../06_career_and_market_readiness/04_ai_driven_interviews/) |

The neighbouring [Cloud Engineering major (CLD)](../cloud_engineering/) owns cloud architecture, infrastructure as code, Kubernetes internals, cloud networking and FinOps. This major owns **delivery, operations, reliability and platforms**: how changes reach production, how production is observed and kept within its reliability targets, how incidents are handled, and how internal platforms and AI agents take over routine work safely.

## 1. Who this major is for, and the roles it leads to

It suits you if you like systems more than screens, enjoy debugging, stay calm when things break, and get satisfaction from making other engineers faster. You will write a lot of code (automation, controllers, tooling), but the product you serve is the production system itself.

| Role | What people in it actually do | Core courses |
|---|---|---|
| **DevOps engineer** | Builds and maintains CI/CD pipelines, infrastructure automation and deployment tooling; often the first operations hire in a startup | OPS301, OPS302, OPS305 |
| **Site reliability engineer (SRE)** | Owns reliability targets (SLOs), alerting, on-call, incident response, post-mortems and capacity; writes software to remove toil | OPS303, OPS304, OPS402, OPS404 |
| **Platform engineer** | Builds the internal developer platform: golden paths, self-service infrastructure, developer portals; treats developers (and now agents) as users | OPS401, OPS305, OPS301 |
| **Release / build engineer** | Owns build systems, release processes, artifact management and safe rollout of code and configuration | OPS301 |
| **Production engineer** | Meta's name for a role close to SRE: software engineers who run and improve production services | OPS302, OPS304, OPS404 |
| **Infrastructure engineer** | Runs fleets of Linux hosts, clusters, storage and networks; often overlaps with cloud engineering | OPS302, OPS305, [CLD303](../cloud_engineering/year_3/CLD303_containers_and_kubernetes/README.md) |
| **Observability engineer** | Designs the telemetry pipeline (metrics, logs, traces, profiles), its cost and its alerting standards | OPS303 |
| **Developer productivity engineer** | Measures and improves developer experience; speeds up builds, tests and reviews | OPS301, OPS401 |
| **AI operations / agent infrastructure engineer** | Integrates and evaluates AI incident assistants and remediation agents; runs agent platforms with guardrails | OPS403, OPS501, [OV12](../../04_overlaps/OV12_agent_infrastructure_platform/README.md) |

Titles, seniority ladders, demand signals and pay are on the [OPS market page](../../06_career_and_market_readiness/01_market_map/roles/OPS_devops_sre_platform_engineering.md). For orientation: Payscale's self-reported data for India (mid-2026) shows an average base of ₹10.0 lakh for DevOps engineers and ₹17.5 lakh for SREs. The US BLS has no DevOps or SRE category; its closest proxies are listed on the market page.

## 2. How AI is changing this field

All figures checked October 2026.

**What the evidence says**

- **AI amplifies whatever delivery system it meets.** DORA's 2025 research (about 5,000 technology professionals) found AI adoption positively related to software delivery throughput but still negatively related to delivery stability. Its summary: "AI doesn't fix a team; it amplifies what's already there". More code, written faster, raises the value of strong pipelines, tests, small batches and fast rollback (OPS301), and of internal platforms. 90% of organisations have adopted at least one ([DORA 2025](https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report)).
- **Operations is the least-automated part of software work.** In the Stack Overflow 2026 survey, 20% of AI users use AI for "deploying, operating, or troubleshooting production systems", against 67% for generating code ([Stack Overflow, Oct 2026](https://stackoverflow.blog/2026/10/06/the-results-of-the-2026-developer-survey-are-here/)).
- **Operations agents are now a product category,** with measured limits. Examples are AWS DevOps Agent, Azure SRE Agent (with an approval "Review mode"), Gemini Cloud Assist, Datadog's Bits AI investigations, Grafana Assistant, PagerDuty's agents and the open-source HolmesGPT and K8sGPT. On independent benchmarks, agents resolved 13.8% of SRE scenarios in ITBench ([2025](https://arxiv.org/abs/2502.05352)). The best configuration located the root cause in 11.34% of 335 real failures in OpenRCA ([ICLR 2025](https://proceedings.iclr.cc/paper_files/paper/2025/file/d29b8d53678015079e1d245c023e49d2-Paper-Conference.pdf)).
- **Agents with production access have already caused incidents.** In July 2025, Replit's agent deleted a production database ([heise](https://heise.de/-10499597)). The same month, an over-scoped CI token let an attacker ship malicious code in the Amazon Q Developer extension ([AWS-2025-015](https://aws.amazon.com/security/security-bulletins/AWS-2025-015/)).
- **The work moves into code; it does not disappear.** The US BLS projects classic system administrator jobs to decline 4% from 2025 to 2035, partly because tasks shift to "DevOps-focused software developers" ([BLS](https://www.bls.gov/ooh/computer-and-information-technology/network-and-computer-systems-administrators.htm)). Meanwhile "DevOps Engineer" is among the 15 fastest-growing jobs to 2030 in the WEF's employer survey ([WEF 2025](https://reports.weforum.org/docs/WEF_Future_of_Jobs_Report_2025.pdf)).

**What is being automated:** writing pipeline YAML, Dockerfiles, Helm values, Ansible tasks, alert rules and dashboard queries; summarising logs, traces and incident channels; drafting runbooks and post-mortems; first-pass alert correlation.

**What is growing in value (what stays human):**

- **Judgement under uncertainty:** commanding an incident when data is incomplete, deciding to roll back, fail over or wait.
- **System design for reliability:** choosing SLOs, designing staged rollouts for code *and* configuration, removing hidden shared dependencies, preventing retry storms and metastable failures.
- **Permissions and guardrails for automation:** deciding what agents may do, with which identity, under which approval, with what blast radius, and proving it with tests and audit.
- **Evaluation:** telling a measured improvement from a vendor anecdote.
- **Platform product thinking:** building paths that humans and agents both use safely.

Every course in this major has a "Working with AI" section with named tools, AI-off drills, verification steps and failure modes you demonstrate yourself. [OPS403](year_4/OPS403_aiops_and_agentic_operations/README.md) makes AI in operations its main subject.

## 3. The 5-year path

### Years 1–2: common core (courses that matter most for this major in bold)

| Year · Semester | Courses |
|---|---|
| 1 · 1 | [FND101](../../01_year_1_foundations/semester_1/FND101_programming_i_computational_thinking_with_python/README.md), **[FND102](../../01_year_1_foundations/semester_1/FND102_how_computers_work_bits_hardware/README.md)**, [FND103](../../01_year_1_foundations/semester_1/FND103_discrete_mathematics_for_computing/README.md), **[FND104](../../01_year_1_foundations/semester_1/FND104_the_developers_toolkit_linux_shell_git/README.md)** (Linux, shell, Git: the base of everything here), [FND105](../../01_year_1_foundations/semester_1/FND105_ai_native_learning_and_building/README.md), **[FND106](../../01_year_1_foundations/semester_1/FND106_technical_communication_and_professional_skills/README.md)** (incident communication starts here) |
| 1 · 2 | [FND111](../../01_year_1_foundations/semester_2/FND111_programming_ii_object_oriented_and_typed/README.md), [FND112](../../01_year_1_foundations/semester_2/FND112_data_structures_and_algorithms_i/README.md), [FND113](../../01_year_1_foundations/semester_2/FND113_linear_algebra_and_calculus_for_computing/README.md), [FND114](../../01_year_1_foundations/semester_2/FND114_web_foundations_http_html_css_and_javascript/README.md), [FND115](../../01_year_1_foundations/semester_2/FND115_databases_i_data_modeling_and_sql/README.md), **[FND116](../../01_year_1_foundations/semester_2/FND116_probability_and_statistics_i/README.md)** (percentiles, distributions, queueing in OPS404) |
| 2 · 3 | [CS201](../../02_year_2_core_computer_science/semester_3/CS201_algorithms_and_complexity/README.md), [CS202](../../02_year_2_core_computer_science/semester_3/CS202_computer_architecture_and_systems_programming/README.md), **[CS203](../../02_year_2_core_computer_science/semester_3/CS203_operating_systems/README.md)** (entry requirement), **[CS204](../../02_year_2_core_computer_science/semester_3/CS204_computer_networks/README.md)**, **[CS205](../../02_year_2_core_computer_science/semester_3/CS205_software_engineering_i_design_testing/README.md)**, [CS206](../../02_year_2_core_computer_science/semester_3/CS206_mathematics_for_machine_learning/README.md) |
| 2 · 4 | [CS211](../../02_year_2_core_computer_science/semester_4/CS211_database_systems_internals/README.md), **[CS212](../../02_year_2_core_computer_science/semester_4/CS212_distributed_systems_i/README.md)** (consensus, replication, failure models), **[CS213](../../02_year_2_core_computer_science/semester_4/CS213_security_foundations/README.md)**, [CS214](../../02_year_2_core_computer_science/semester_4/CS214_machine_learning_foundations/README.md) (needed for OPS403), **[CS215](../../02_year_2_core_computer_science/semester_4/CS215_cloud_and_devops_foundations/README.md)** (entry requirement), [CS216](../../02_year_2_core_computer_science/semester_4/CS216_programming_languages_compilers_and_interpreters/README.md) |

### Years 3–5: the major

| Year · Semester | Major courses | Shared courses | Recommended elective or overlap slot |
|---|---|---|---|
| 3 · 5 | [OPS301 CI/CD Engineering](year_3/OPS301_ci_cd_engineering/README.md), [OPS302 Linux Systems Administration in Depth](year_3/OPS302_linux_systems_administration_in_depth/README.md), [OPS303 Observability](year_3/OPS303_observability_metrics_logs_traces/README.md) | [PRO301 Professional Practice: Ethics, Law and Responsible AI](../../05_shared_years_3_to_5/PRO301_professional_practice_ethics_law_and_responsible/README.md) | [CLD303 Containers and Kubernetes](../cloud_engineering/year_3/CLD303_containers_and_kubernetes/README.md) (strongly recommended), or [SEC302](../cybersecurity_defense/year_3/SEC302_security_operations_soc_siem_and_monitoring/README.md) if you plan the OV03 overlap |
| 3 · 6 | [OPS304 Site Reliability Engineering](year_3/OPS304_site_reliability_engineering_slos_error_budgets/README.md), [OPS305 Configuration Management and GitOps](year_3/OPS305_configuration_management_and_gitops/README.md) | [CAR301 Career Lab I](../../05_shared_years_3_to_5/CAR301_career_lab_i_dsa_mastery_portfolio_and_open/README.md) | [CLD302 Infrastructure as Code](../cloud_engineering/year_3/CLD302_infrastructure_as_code_terraform_opentofu/README.md), or [SAR305](../security_architecture/year_3/SAR305_secure_sdlc_and_devsecops_architecture/README.md) for OV03 |
| 4 · 7 | [OPS401 Platform Engineering and IDPs](year_4/OPS401_platform_engineering_and_internal_developer/README.md), [OPS402 Chaos Engineering and Resilience](year_4/OPS402_chaos_engineering_and_resilience/README.md) | [IND401 Industry Co-op Studio](../../05_shared_years_3_to_5/IND401_industry_co_op_studio/README.md) | Overlap course A (default: [OV03A Software Supply Chain Security](../../04_overlaps/OV03_devsecops/OV03A_software_supply_chain_security/README.md)) |
| 4 · 8 | [OPS403 AIOps and Agentic Operations](year_4/OPS403_aiops_and_agentic_operations/README.md), [OPS404 Performance and Capacity Engineering](year_4/OPS404_performance_and_capacity_engineering/README.md) | [CAR401 Career Lab II](../../05_shared_years_3_to_5/CAR401_career_lab_ii_interviews_system_design_and_ai/README.md) | Overlap course B (default: [OV03B Policy as Code and Secure CI/CD](../../04_overlaps/OV03_devsecops/OV03B_policy_as_code_and_secure_ci_cd/README.md)) |
| 5 · 9 | [OPS501 Frontier Seminar: Autonomous Infrastructure and Self-Healing Systems](year_5/OPS501_frontier_seminar_autonomous_infrastructure/README.md) | [RES501](../../05_shared_years_3_to_5/RES501_research_methods_and_scientific_writing/README.md), [RES502](../../05_shared_years_3_to_5/RES502_reading_reproducing_and_extending_papers/README.md), [THS501 Thesis or Capstone I](../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) | — |
| 5 · 10 | — | [THS502 Thesis or Capstone II](../../05_shared_years_3_to_5/THS502_thesis_or_capstone_ii/README.md), [LCH502 Career Launch and Founder Studio](../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md) | Electives or a second overlap (for example OV12, see section 5) |

Course dependencies inside the major: OPS401 needs OPS301; OPS402 needs OPS302; OPS403 needs OPS303; OPS404 needs OPS304; OPS501 needs OPS401 and OPS403. The Year 3 courses all need CS215 and CS203.

## 4. Skill map by level

| Level | You can… | Where it is built |
|---|---|---|
| **L0 · Absolute beginner** | Use a Linux shell, edit files, run commands from instructions, use Git to commit and push | FND104 |
| **L1 · Foundations** | Explain processes, memory, files, TCP/IP and DNS; write small scripts; containerise an app; explain what a pipeline and an SLO are | FND102, CS203, CS204, CS215 |
| **L2 · Practitioner (intern-ready)** | Build a CI/CD pipeline with tests and a canary; instrument a service with OpenTelemetry; run an app on Kubernetes with probes and autoscaling; write a blameless post-mortem; debug a broken Linux host with guidance | CS215, start of OPS301–303 |
| **L3 · Professional (job-ready)** | Design delivery for a team with immutable artifacts, progressive delivery and config rollout safety; run Linux fleets hardened and observable; build a cost-controlled telemetry pipeline; set SLOs with burn-rate alerting; command an incident; run GitOps across clusters with secrets and drift control | OPS301–305 |
| **L4 · Expert (senior, hard to replace)** | Build an internal platform as a product with golden paths for humans and agents; make systems resilient to retry storms, overload and metastability and prove it with chaos experiments; plan capacity with queueing models; integrate and evaluate AI operations agents with least privilege, approvals and adversarial tests; lead on-call and reliability programmes | OPS401–404, overlaps, IND401 |
| **L5 · Research and frontier** | Specify and model-check infrastructure protocols; reproduce and extend papers on self-healing, controller verification and agentic operations; publish an evaluated artefact | OPS501, RES501–502, THS501–502 |

**Mastery gates you will pass along the way** (each course defines its own in detail): cut a slow pipeline's time-to-green by 40% without removing tests (OPS301); solve 4 of 5 unseen Linux break-fix scenarios in 20 minutes each (OPS302); find a planted fault from telemetry alone in 20 minutes (OPS303); command a simulated incident judged competent by two examiners (OPS304); rebuild a deleted cluster from Git in 30 minutes (OPS305); show real users completing your golden path in under 15 minutes (OPS401); recover a metastable system you did not build (OPS402); zero unsafe actions by your remediation agent across an adversarial suite (OPS403); predict latency at a new load within 25% (OPS404); a specification that finds a bug, and a reproduced paper (OPS501).

## 5. Recommended overlaps and electives

| Overlap | Why it fits OPS | Composed of | Planning note |
|---|---|---|---|
| [OV03 DevSecOps](../../04_overlaps/OV03_devsecops/README.md) | Secure pipelines, supply chain (SBOM, signing, provenance), policy as code: the natural next step after OPS301 | OPS301, SAR305, SEC302 | **Default for this major.** Take SEC302 (semester 5) and SAR305 (semester 6) as electives, then OV03A/OV03B in semesters 7–8 |
| [OV04 MLOps and ML Platform Engineering](../../04_overlaps/OV04_mlops_ml_platform/README.md) | Platforms for training and serving models, LLMOps at scale | MLE401, OPS401, CLD404 | Needs MLE401 and CLD404 as electives first; usually fits semesters 9–10 |
| [OV12 Agent Infrastructure and Platform Engineering](../../04_overlaps/OV12_agent_infrastructure_platform/README.md) | Running agents in production: sandboxes, durable execution, evaluation and reliability of agents | AIE401, OPS403, BE501 | OPS403 is in semester 8, so OV12A/OV12B fit semesters 9–10 alongside OPS501 |
| [OV01 Cloud Security](../../04_overlaps/OV01_cloud_security/README.md) | Kubernetes and container security, cloud detection and response | CLD301, SAR401, SEC303 | Needs three courses from other majors; best for students moving towards cloud security roles |

**Electives that pay off most:** [CLD303 Containers and Kubernetes](../cloud_engineering/year_3/CLD303_containers_and_kubernetes/README.md) (almost essential), [CLD302 Infrastructure as Code](../cloud_engineering/year_3/CLD302_infrastructure_as_code_terraform_opentofu/README.md), [CLD304 Cloud Networking](../cloud_engineering/year_3/CLD304_cloud_networking_vpcs_dns_load_balancing/README.md), [CLD403 FinOps](../cloud_engineering/year_4/CLD403_finops_and_cloud_cost_engineering/README.md), [BE404 Microservices, Service Mesh and Platform APIs](../backend_engineering/year_4/BE404_microservices_service_mesh_and_platform_apis/README.md), [QAE304 Testing in CI/CD](../software_quality_test_engineering/year_3/QAE304_testing_in_ci_cd_and_test_infrastructure/README.md), [SEC302 Security Operations](../cybersecurity_defense/year_3/SEC302_security_operations_soc_siem_and_monitoring/README.md), [NET303 Network Automation](../it_infrastructure_networking/year_3/NET303_network_automation_and_netdevops/README.md), [NET305 IT Service Management](../it_infrastructure_networking/year_3/NET305_it_service_management_and_operations/README.md), [AIE304 Tool Use and AI Agents](../ai_engineering/year_3/AIE304_tool_use_and_ai_agents_loops_harnesses_memory/README.md), [AIE403 LLMOps](../ai_engineering/year_4/AIE403_llmops_observability_guardrails_cost_and_latency/README.md).

## 6. Flagship industry project

The [OPS flagship industry project](../../06_career_and_market_readiness/05_industry_projects/OPS_devops_sre_platform_engineering.md) asks you to build and operate a production-shaped system end to end and defend it like a senior engineer: delivery, telemetry, SLOs, GitOps, a platform layer, a game day and an evaluated AI operations assistant. The portfolio-grade projects in this major are designed to feed it: OPS301 P3 (a release system that contains config failures), OPS303 P3 (a blind-tested on-call platform), OPS304 P3 (a payment-style reliability engagement), OPS401 P3 (an IDP for humans and agents) and OPS403 P3 (a guarded remediation agent).

## 7. Certifications worth having (optional, never required)

Hands-on, performance-based exams carry more weight with employers than multiple-choice ones. Current names and formats were checked on the official pages in October 2026.

| Certification | Format and fit | Honest value |
|---|---|---|
| [LFCS](https://training.linuxfoundation.org/certification/linux-foundation-certified-sysadmin-lfcs/) (Linux Foundation Certified System Administrator) | 2-hour performance-based exam at a live Linux command line; matches OPS302 | Good proof of Linux skill for first jobs, especially if you come from support or non-CS backgrounds |
| [CKA, CKAD, CKS](https://www.cncf.io/training/certification/) (CNCF/Linux Foundation) | Performance-based Kubernetes exams: administration, application development, security | **CKA is the most widely recognised hands-on credential in this field.** Take it after CLD303; CKS after OV01B or OV03 |
| [CNCF associate exams](https://www.cncf.io/training/certification/): PCA (Prometheus), OTCA (OpenTelemetry), CGOA (GitOps), CAPA (Argo), CBA (Backstage), CNPA (platform engineering); and CNPE (Certified Cloud Native Platform Engineer) | Mostly multiple choice; aligned with OPS303, OPS305 and OPS401 | Useful structure for study and a signal for career changers; weaker than projects for experienced hires |
| [HashiCorp Terraform Associate](https://developer.hashicorp.com/certifications/infrastructure-automation) | Multiple-choice Terraform exam (higher levels also exist) | Common in job adverts for DevOps roles; pairs with CLD302 |
| [AWS Certified DevOps Engineer – Professional](https://aws.amazon.com/certification/certified-devops-engineer-professional/) | 180 minutes, US$300 | Valued where a company is AWS-heavy; hard, so take it after real AWS experience |
| [Google Cloud Professional Cloud DevOps Engineer](https://cloud.google.com/learn/certification/cloud-devops-engineer) | Covers SRE principles on Google Cloud | Valued by Google Cloud shops; good overlap with OPS304 |
| [Microsoft Certified: DevOps Engineer Expert](https://learn.microsoft.com/en-us/credentials/certifications/devops-engineer/) | AZ-400 plus a prerequisite associate certification | Valued in Azure-centred enterprises |

No certification replaces a public portfolio of the projects above. If you can afford only one, choose CKA, or LFCS if Linux is your weaker side.

## 8. The interview loop

Typical loops for DevOps, SRE and platform roles ([market page](../../06_career_and_market_readiness/01_market_map/roles/OPS_devops_sre_platform_engineering.md)) have five parts. Each maps to courses in this major:

| Round | What happens | Prepare with |
|---|---|---|
| Linux and networking troubleshooting | "A server is slow", "DNS fails intermittently": interviewers watch your method | OPS302 drills, CS204, SadServers-style practice |
| Coding and scripting | Automation in Python, Go or Bash; sometimes DSA at product companies | OPS302 Chapter 11, [CAR301](../../05_shared_years_3_to_5/CAR301_career_lab_i_dsa_mastery_portfolio_and_open/README.md) |
| System design for reliability | Monitoring and alerting for a service, a deployment pipeline, multi-region failover, capacity estimates | OPS301, OPS303, OPS304, OPS404, [CAR401](../../05_shared_years_3_to_5/CAR401_career_lab_ii_interviews_system_design_and_ai/README.md) |
| Incident scenario | "You're on call, alerts fire": what you do, in what order, and how you communicate | OPS304 tabletops and incident simulation exam |
| Behavioural | An outage you caused or fixed; how you improved on-call; working with developers | Post-mortems you wrote in OPS304 and OPS402 |

Interview formats that use AI (AI-proctored screens, AI-assisted coding rounds, and debugging with an AI assistant allowed) are covered in [AI-driven interviews](../../06_career_and_market_readiness/04_ai_driven_interviews/). Every course page here ends with five interview questions and what a strong answer must cover.

## 9. Fast tracks for working professionals

Budget 12–15 hours a week. Use each course's mastery gate as a placement test: if you can pass it today, skip the course and do only its P3.

**From system administration, IT support or NOC operations** (common in Indian IT services; 12–18 months):
1. Check your base with [FND104](../../01_year_1_foundations/semester_1/FND104_the_developers_toolkit_linux_shell_git/README.md) and [CS204](../../02_year_2_core_computer_science/semester_3/CS204_computer_networks/README.md) gates; learn Python to the level of [FND101](../../01_year_1_foundations/semester_1/FND101_programming_i_computational_thinking_with_python/README.md).
2. [CS215](../../02_year_2_core_computer_science/semester_4/CS215_cloud_and_devops_foundations/README.md), then [OPS302](year_3/OPS302_linux_systems_administration_in_depth/README.md) (you may test out) and LFCS.
3. [OPS301](year_3/OPS301_ci_cd_engineering/README.md), [CLD303](../cloud_engineering/year_3/CLD303_containers_and_kubernetes/README.md) and CKA.
4. [OPS303](year_3/OPS303_observability_metrics_logs_traces/README.md), [OPS304](year_3/OPS304_site_reliability_engineering_slos_error_budgets/README.md), [OPS305](year_3/OPS305_configuration_management_and_gitops/README.md).
5. Publish OPS303 P3 and OPS304 P3 as your portfolio; prepare with the interview loop above.

**From software development** (6–9 months): [CS215](../../02_year_2_core_computer_science/semester_4/CS215_cloud_and_devops_foundations/README.md) → OPS302 (focus on Chapters 6–8 and 12) → OPS303 → OPS304 → OPS301. Your coding is an advantage for SRE and platform roles; your gap is usually Linux, networking and incident practice.

**From cloud engineering** (4–6 months): OPS303, OPS304 and OPS401, then OPS403 if you want to work on AI operations.

**For senior engineers moving into platform or AI operations leadership:** OPS401 and OPS403 projects, plus OPS501's reading list.

## Sources

All checked 12 Oct 2026.
- Google Cloud, [Announcing the 2025 DORA report](https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report) (24 Sep 2025); DORA, [capabilities catalog](https://dora.dev/capabilities/).
- Stack Overflow, [2026 developer survey results](https://stackoverflow.blog/2026/10/06/the-results-of-the-2026-developer-survey-are-here/) (6 Oct 2026), as summarised in this repository's [market page](../../06_career_and_market_readiness/01_market_map/roles/OPS_devops_sre_platform_engineering.md).
- US BLS, [Network and Computer Systems Administrators](https://www.bls.gov/ooh/computer-and-information-technology/network-and-computer-systems-administrators.htm) (2025–35 projection).
- WEF, [Future of Jobs Report 2025](https://reports.weforum.org/docs/WEF_Future_of_Jobs_Report_2025.pdf).
- Payscale India: [DevOps Engineer](https://www.payscale.com/research/IN/Job=Development_Operations_(DevOps)_Engineer/Salary) and [Site Reliability Engineer](https://www.payscale.com/research/IN/Job=Site_Reliability_Engineer_(SRE)/Salary) (self-reported), via the market page.
- Jha et al., [ITBench](https://arxiv.org/abs/2502.05352) (2025); Xu et al., [OpenRCA](https://proceedings.iclr.cc/paper_files/paper/2025/file/d29b8d53678015079e1d245c023e49d2-Paper-Conference.pdf) (ICLR 2025).
- Product pages: [AWS DevOps Agent](https://aws.amazon.com/devops-agent/), [Azure SRE Agent](https://learn.microsoft.com/en-us/azure/sre-agent/overview), [HolmesGPT](https://github.com/HolmesGPT/holmesgpt) (CNCF sandbox).
- heise online, [Replit deletes production database](https://heise.de/-10499597) (Jul 2025); AWS, [security bulletin AWS-2025-015](https://aws.amazon.com/security/security-bulletins/AWS-2025-015/).
- Certification pages: [CNCF certifications](https://www.cncf.io/training/certification/), [LFCS](https://training.linuxfoundation.org/certification/linux-foundation-certified-sysadmin-lfcs/), [HashiCorp](https://developer.hashicorp.com/certifications/infrastructure-automation), [AWS DevOps Engineer – Professional](https://aws.amazon.com/certification/certified-devops-engineer-professional/), [Google Professional Cloud DevOps Engineer](https://cloud.google.com/learn/certification/cloud-devops-engineer), [Microsoft DevOps Engineer Expert](https://learn.microsoft.com/en-us/credentials/certifications/devops-engineer/).

_Last reviewed: 2026-10_
