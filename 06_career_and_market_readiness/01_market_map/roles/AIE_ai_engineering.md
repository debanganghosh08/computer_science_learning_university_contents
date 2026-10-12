# AIE · AI Engineering: LLM Applications and Agents: roles and market (2026)

| Learning path | Interview loop | AI impact | Market overview |
|---|---|---|---|
| [AI Engineering major](../../../03_majors/ai_engineering/README.md) | [AI-driven interviews](../../04_ai_driven_interviews/) | [Matrix row](../ai_impact_matrix.md) | [Market map](../README.md) |

All figures were checked in October 2026. Paragraphs marked **Analysis** are interpretation, not measurement.

## Role titles and seniority ladder

| Level | Common titles |
|---|---|
| Entry | AI Engineer I, Associate AI Engineer, Software Engineer (AI features), GenAI Developer |
| Mid | AI Engineer, LLM Engineer, Applied AI Engineer, Agent Engineer |
| Senior | Senior AI Engineer, AI Platform Engineer, AI Evaluation Lead |
| Staff and above | Staff/Principal AI Engineer, Head of Applied AI |

This family builds products on top of foundation models: retrieval-augmented generation (RAG), tool-using agents, evaluation, guardrails and cost control. It is closer to software engineering than to model research. "Applied AI" roles at model companies sit between AI engineering and forward-deployed engineering ([FDE](FDE_forward_deployed_engineering.md)).

## What the work looks like day to day

- Design prompts and, more importantly, the context a model sees: instructions, retrieved documents, tool results, memory (AIE302).
- Build retrieval: chunking, embeddings, hybrid search, re-ranking (AIE303).
- Build agents: the loop of plan, call tool, observe, continue; harnesses, memory and persistence (AIE304).
- Write evaluations: test sets, graders, regression suites, human review (AIE305).
- Connect models to tools and data through standard protocols such as the Model Context Protocol (MCP) (AIE401).
- Add guardrails, tracing, cost and latency budgets (AIE403).
- Fine-tune or distil small models when a general model is too slow or costly (AIE402).
- Design the user experience of AI features with product and design teams (AIE404).

## Demand signals

- **Postings are shifting to agents.** Mentions of generative AI skills in US AI job postings grew 111% from 2024 to 2025, and postings referencing agentic AI, AI agents or orchestration frameworks such as LangGraph increased sharply, while the share mentioning ChatGPT, chatbots or conversational AI declined ([AI Index 2026](https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf)).
- **Builders.** More than 1.1 million public GitHub repositories import an LLM SDK; new ones in the past year rose 178% ([Octoverse 2025](https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/)).
- **Employer intentions.** 78% of leaders were considering hiring for AI-specific roles; 32% of managers were considering AI agent specialists ([Microsoft Work Trend Index 2025](https://www.microsoft.com/en-us/worklab/work-trend-index/2025-the-year-the-frontier-firm-is-born)).
- **Deployment gap.** Organisational AI adoption reached 88%, but AI agent deployment was "in the single digits across nearly all business functions" ([AI Index 2026](https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf)). 26.2% of developers use AI agents or automated workflows at work ([Stack Overflow 2026](https://survey.stackoverflow.co/2026/ai/data)). The gap between interest and production is the work of this role.
- **Snapshot.** On 12 Oct 2026, OpenAI listed 66 and Anthropic 47 roles with "Applied AI" in the title, including India-based roles in Delhi, Bengaluru and Mumbai ([OpenAI careers](https://openai.com/careers), [Anthropic careers](https://www.anthropic.com/jobs)).
- **India.** Coding is over half of Claude usage in India, against roughly a third globally ([Anthropic, Sept 2025](https://www.anthropic.com/research/anthropic-economic-index-september-2025-report)).

No official statistics count "AI engineers" yet.

## How AI is changing the role

AI engineers use AI to build AI systems, so automation hits the easy parts first.

**Automated or mostly automated.** Glue code for API calls, prompt templates, basic RAG pipelines, framework boilerplate, synthetic test data.

**Augmented.** Writing graders, analysing failure cases, comparing models, generating adversarial test inputs.

**Growing in value.**

- **Evaluation.** Models fail often in real use: Anthropic estimated a 49% task success rate for API traffic and about 61% for software-development requests ([Anthropic, Jan 2026](https://www.anthropic.com/research/anthropic-economic-index-january-2026-report)). Measuring and raising that rate is the core skill.
- **Reliability engineering for agents.** Even top models have an 80%-reliability time horizon near one hour on METR's tasks ([METR data](https://metr.org/assets/benchmark_results_1_1.yaml)), so long agent runs need checkpoints, verification and recovery.
- **Security.** Prompt injection is the first entry, and excessive agency the sixth, in the [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/llm-top-10/).
- **Cost and latency engineering.**
- **Product judgement**: knowing when not to use an LLM.

**Analysis.** Writing prompts is now something most engineers do. What makes this role distinctive is the engineering discipline around non-deterministic components: evals, observability, security and cost.

## Pay (indicative)

**No reliable public salary data exists for "AI engineer" as a distinct title** in India or the US as of October 2026. Closest proxies:

| Market | Role in source | Figure | Type | Source |
|---|---|---|---|---|
| US | Software developers | Median $135,980; 90th $214,670 (May 2025) | Official survey | [BLS](https://www.bls.gov/ooh/computer-and-information-technology/software-developers.htm) |
| India | Machine Learning Engineer | Average base ₹10.2 lakh; base range ₹3.6–30 lakh (232 profiles, Jul 2026) | Self-reported, whole market | [Payscale](https://www.payscale.com/research/IN/Job=Machine_Learning_Engineer/Salary) |
| India | Software Engineer | Median total pay ₹30.6 lakh (product-company-heavy) | Self-reported | [Levels.fyi](https://www.levels.fyi/t/software-engineer/locations/india) |

## The hiring loop

Typical loop (varies by company; still settling):

1. Coding round, sometimes AI-assisted.
2. LLM application design: "design a support assistant over 50,000 documents" or "design an agent that files expense reports". Strong answers cover retrieval, tool permissions, evaluation, failure handling, cost and latency.
3. Practical exercise or take-home: build a small RAG or agent system with an evaluation set and report results honestly.
4. Debugging session: given traces of a failing agent, find the cause.
5. Behavioural and product sense.

Interview AI policies diverge: Canva expects AI tool use in coding interviews ([Canva](https://www.canva.dev/blog/engineering/yes-you-can-use-ai-in-our-interviews/)); Anthropic forbids AI in live interviews unless stated ([Anthropic](https://www.anthropic.com/candidate-ai-guidance)). See [AI-driven interviews](../../04_ai_driven_interviews/).

## Durable skills that make you hard to replace

- Strong software engineering (testing, APIs, data handling).
- Information retrieval and search fundamentals.
- Evaluation design and statistics.
- Security of LLM applications.
- Distributed systems basics for agent backends (durable execution, queues).
- Product and UX sense for AI features.

## Adjacent roles and transitions

- **Backend engineering** ([BE](BE_backend_engineering.md)): overlap OV08 and BE403.
- **Machine learning engineering** ([MLE](MLE_machine_learning_engineering.md)).
- **Forward deployed engineering** ([FDE](FDE_forward_deployed_engineering.md)).
- **AI security and safety**: overlap OV05 ([SAR](SAR_security_architecture.md)).
- **Agent infrastructure and platform**: overlap OV12 ([OPS](OPS_devops_sre_platform_engineering.md)).
- **Frontend for AI interfaces** ([FE](FE_frontend_engineering.md)).

## Sources

All checked October 2026.

- Stanford HAI, AI Index 2026. https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf
- GitHub, Octoverse 2025. https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/
- Microsoft, 2025 Work Trend Index (23 Apr 2025). https://www.microsoft.com/en-us/worklab/work-trend-index/2025-the-year-the-frontier-firm-is-born
- Stack Overflow, 2026 Developer Survey. https://survey.stackoverflow.co/2026/ai/data
- Anthropic Economic Index (15 Sep 2025; 15 Jan 2026). https://www.anthropic.com/research/anthropic-economic-index-september-2025-report ; https://www.anthropic.com/research/anthropic-economic-index-january-2026-report
- METR, benchmark results v1.1. https://metr.org/assets/benchmark_results_1_1.yaml
- OWASP, Top 10 for LLM Applications 2025. https://genai.owasp.org/llm-top-10/
- Job boards on 12 Oct 2026: https://openai.com/careers ; https://www.anthropic.com/jobs
- BLS, Software Developers. https://www.bls.gov/ooh/computer-and-information-technology/software-developers.htm ; Payscale India, Machine Learning Engineer. https://www.payscale.com/research/IN/Job=Machine_Learning_Engineer/Salary ; Levels.fyi India. https://www.levels.fyi/t/software-engineer/locations/india
- Canva Engineering (11 Jun 2025). https://www.canva.dev/blog/engineering/yes-you-can-use-ai-in-our-interviews/ ; Anthropic candidate AI guidance. https://www.anthropic.com/candidate-ai-guidance

_Last reviewed: 2026-10_
