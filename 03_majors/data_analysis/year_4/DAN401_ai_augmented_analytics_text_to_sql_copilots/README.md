# DAN401 · AI-Augmented Analytics: Text-to-SQL, Copilots and Their Failure Modes

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 7 | 4 (≈ 120 hours) | L3 → L4 | [DAN301](../../year_3/DAN301_spreadsheets_to_sql_analytical_querying_in_depth/README.md) | [DAN501](../../year_5/DAN501_frontier_seminar_decision_intelligence/README.md), [OV06B](../../../../04_overlaps/OV06_data_platform_analytics_engineering/OV06B_semantic_layers_and_self_serve_analytics_with_ai/README.md), [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) |

Part of the [Data Analysis major](../../README.md). Assumes analyst-grade SQL and query testing from DAN301. The semantic layers from [DAN304](../../year_3/DAN304_analytics_engineering_dbt_modeling_and_semantic/README.md) and the statistics from [DAN302](../../year_3/DAN302_business_statistics_and_experimentation/README.md) are strongly recommended. The engineering of LLM applications in general belongs to the AI Engineering major ([AIE302](../../../ai_engineering/year_3/AIE302_prompt_and_context_engineering/README.md), [AIE305](../../../ai_engineering/year_3/AIE305_evaluating_llm_systems/README.md)). This course is about using, evaluating and governing AI for analysis, where a wrong answer looks exactly like a right one.

## Why this course matters now

Natural-language analytics is now a standard feature of the tools analysts use. Power BI's report Copilot pane is generally available. Looker's Conversational Analytics answers questions over LookML. Snowflake's Cortex Analyst turns questions into SQL over semantic views. Databricks' Genie documentation (September 2026) describes Genie One, Genie Agents and Genie Code. In dbt Labs' 2025 survey, 80% of data practitioners used AI daily. Benchmarks show both the progress and the gap. The top BIRD system scores 82.95% execution accuracy against 92.96% for human experts. On Spider 2.0, the original paper's best model solved 17.1% of enterprise tasks, and leaderboard entries now report up to 96.70 on its Snowflake setting but 65.6 on dbt project tasks. Where questions are ambiguous and the system must ask for clarification (BIRD-Interact), GPT-5 solved 8.67% to 17.00% of tasks. On multi-step analysis tasks (DABstep), the best agent solved 14.55% of the hard ones. The vendors document the limits themselves. Power BI's Copilot answers from the model's "general knowledge" when a question is not about the semantic model. Cortex Analyst cannot reuse earlier query results in a conversation. Looker's agent does not answer forecasting, correlation or anomaly questions. The analysts who matter in 2026 can measure how often an AI answer is right, make it right more often, and stop wrong ones from reaching a decision.

## Learning outcomes

By the end you can:

1. **Explain** how text-to-SQL systems work (schema linking, retrieval of tables and examples, decomposition, candidate generation and selection, execution feedback, semantic-layer grounding), and **predict** where each design fails.
2. **Read** text-to-SQL and data-agent benchmarks critically: settings, metrics, oracle knowledge, contamination. **Explain** why leaderboard numbers do not transfer to your warehouse.
3. **Build** an evaluation harness for natural-language analytics: gold sets from real questions, result-set equality, test-suite accuracy, component metrics, run-to-run variance, cost and latency.
4. **Classify** AI analytics failures with a taxonomy (schema hallucination, fan-out, wrong grain, wrong business definition, time-zone, `NULL` and dialect errors, unasked clarification, out-of-scope fallback), and **reproduce** each one on demand.
5. **Configure and compare** at least two BI or warehouse copilots on the same semantic model, and **raise** their accuracy with descriptions, synonyms, AI instructions and verified queries.
6. **Build** a guarded analytics assistant: question routing, a semantic layer or verified queries first, SQL generation, static validation, read-only execution with cost limits, result checks and an answer with provenance.
7. **Validate** AI-generated exploratory analyses and narratives, including multiple-comparison risk when an AI tries many cuts.
8. **Govern** AI answers: permissions, row-level security, PII, data residency, prompt injection, audit logs, approval of verified answers, and incident response for a wrong number.

## Chapters and lessons

### Chapter 1 · The AI analytics landscape in 2026 (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Surfaces | Copilots in BI tools, in warehouses, in spreadsheets and notebooks; general assistants; agents with database tools via the Model Context Protocol | Map every AI surface your organisation (or a case company) exposes to data |
| 1.2 Case studies | Uber QueryGPT: workspaces, intent, table and column-pruning agents, golden-set evaluation (2024); Swiggy Hermes (2024) | Write a one-page comparison of their designs and lessons |
| 1.3 What changed for analysts | Drafting is cheap; checking, definitions and context are not; Excel's preview `COPILOT()` function withdrawn on 14 Sep 2026 | List 10 tasks you do; mark automated, augmented or owned |
| 1.4 Honest productivity | Uber's reported 10 → 3 minutes per query and 78% of pilot users saying it saved time; what such numbers do and do not show | Design a fair measurement of time saved and errors introduced |

**Check your understanding:** Why did Uber split text-to-SQL into intent, table selection and column pruning? What does "78% said it saved time" not tell you? What did workbooks that depended on `COPILOT()` lose when it was withdrawn?

### Chapter 2 · How text-to-SQL works (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 LLM basics for analysts | Tokens, context windows, sampling and temperature, non-determinism, caching (Power BI caches identical prompts on an unchanged model for 24 hours) | Ask the same question 10 times; measure answer variance |
| 2.2 Schema linking and retrieval | Picking tables and columns; retrieving similar verified queries; pruning wide schemas | Implement table retrieval over 200 tables; measure recall |
| 2.3 Decomposition and selection | DIN-SQL style decomposition; CHASE-SQL style multiple candidates plus a selector | Compare single-shot vs best-of-5 with execution checks |
| 2.4 Execution feedback | Agent loops that run, read errors and retry; why "runs without error" is a weak signal | Build a 3-retry loop; count silent wrong answers |
| 2.5 Grounding in a semantic layer | The model picks metrics and dimensions; the layer writes the SQL (Looker's approach); verified queries (Cortex Analyst) | Answer 10 questions through MetricFlow or Cube vs raw SQL |

**Check your understanding:** Why does grounding in a semantic layer remove whole classes of errors but not all? Why can a retry loop make wrong answers more confident? What does non-determinism mean for a monthly report?

### Chapter 3 · Benchmarks and what they measure (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Spider to Spider 2.0 | Cross-domain academic SQL vs 632 enterprise workflow tasks on BigQuery and Snowflake; GPT-4o at 86.6% on Spider 1.0 vs 10.1% on Spider 2.0 in the paper | Run 10 Spider 2.0-Lite tasks with one assistant |
| 3.2 BIRD and its family | Execution accuracy and efficiency on dirty values; BIRD-Interact (clarification), BIRD-Critic (SQL debugging), LiveSQLBench (contamination-free) | Read the human baseline note ("oracle knowledge used") and explain its effect |
| 3.3 Data-agent benchmarks | DABstep: 450+ multi-step tasks from a financial analytics platform; factoid answers | Attempt 5 DABstep tasks yourself; compare with the agents |
| 3.4 Reading a leaderboard | Settings, hidden test sets, contamination, cost, what "96.70" can and cannot mean for you | Write a one-page critique of one leaderboard entry |

**Check your understanding:** Why do scores on one Spider 2.0 setting not predict scores on its dbt setting? Why does a human baseline with oracle knowledge differ from your analysts' accuracy? What would contamination look like, and how does LiveSQLBench try to avoid it?

### Chapter 4 · A failure-mode taxonomy (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Structural errors | Hallucinated tables or columns, wrong join path, fan-out, wrong grain, dialect mix-ups | Provoke each error on TheLook; save the prompt and output |
| 4.2 Semantic errors | Business terms with silent meanings ("active", "revenue", "churned"), wrong time window, IST vs UTC, `NULL` semantics, averages of ratios | Provoke each; write the definition that prevents it |
| 4.3 Interaction errors | Answering ambiguous questions without asking; losing context across turns; caching surprises | 10 ambiguous questions; score which systems ask before answering |
| 4.4 Scope errors | Answers from general knowledge instead of your data; questions the tool cannot answer (forecasts, correlations) presented as answers | Find the boundary of scope for two copilots |
| 4.5 Visual and narrative errors | Misread charts (CharXiv: 47.1% for GPT-4o vs 80.5% for humans), causal words in summaries | Grade 10 generated narratives sentence by sentence |

**Check your understanding:** Which failure class is hardest to detect from the output alone, and why? Why is a confident answer to an ambiguous question worse than a clarifying question? How would you detect that an answer came from general knowledge rather than your data?

### Chapter 5 · Building an evaluation harness (weeks 5–6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Gold sets | Collecting real questions from logs and stakeholders; difficulty tiers; gold SQL and gold results; refresh policy | A 60-question gold set over your DAN304 warehouse |
| 5.2 Scoring | Result-set equality (order-insensitive, float tolerance, column-name independence); why text similarity and LLM judges mislead | A scorer with unit tests for 12 tricky equality cases |
| 5.3 Test-suite accuracy | Perturbed databases that expose queries correct only by coincidence (Zhong, Yu and Klein, 2020) | Generate 3 perturbed copies; re-score |
| 5.4 Component metrics | Intent accuracy, table recall and precision (QueryGPT-style), clarification rate, abstention rate | Add component metrics; find the weakest stage |
| 5.5 Variance, cost and regressions | Repeated runs, confidence intervals on accuracy, cost per question, latency; a regression gate when models or prompts change | CI job that fails if accuracy drops beyond its noise band |

**Check your understanding:** Why can a query that returns the gold result on one database still be wrong? With 60 questions, how big must an accuracy change be before you believe it? Why should abstaining count differently from answering wrongly?

### Chapter 6 · Prompting and context for analysis (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Context that matters | Dialect, grain, definitions, time zone, fiscal calendar, examples of good queries | Measure accuracy as you add each context element |
| 6.2 Structured outputs | SQL plus stated assumptions plus suggested checks; JSON schemas for downstream validation | Force structured output; parse and validate it |
| 6.3 Asking before answering | Instructions and patterns that make a model ask clarifying questions; measuring over-asking | Tune for ambiguous vs clear questions; report both rates |
| 6.4 Limits of prompting | When more prompt text stops helping; when a semantic layer or verified query is the fix | Plot accuracy vs prompt length for your harness |

**Check your understanding:** Which single context element improved accuracy most in your experiment, and why? When does asking clarifying questions become a usability problem? Why is a verified query more reliable than a longer prompt?

### Chapter 7 · Copilots in BI tools and warehouses (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Power BI Copilot | Report pane (generally available), standalone Copilot (preview), app Copilot with verified answers; capacity requirements; preparing the model for AI | Prepare a semantic model; measure before/after accuracy on 20 questions |
| 7.2 Looker and Gemini | Conversational Analytics grounded in LookML; agent context; listed limits (50,000 rows, unsupported question types) | Build an Explore agent; test its stated limits |
| 7.3 Snowflake and Databricks | Cortex Analyst with semantic views and verified queries; Genie Agents with instructions, sample queries and verified answers | Configure one; run your gold set through it |
| 7.4 Tableau Pulse and Agent | Metric definitions with generated insights; Tableau Agent in Pulse uses pre-computed insights, not raw data | Compare Pulse insights with your own analysis of the same metric |
| 7.5 Choosing and configuring | Accuracy on your gold set, governance, cost, data residency, lock-in | A tool comparison memo for an illustrative bank |

**Check your understanding:** Why do all four vendors ask you to curate examples or verified answers? What does "answers from general knowledge" mean for a finance user? Which copilot limitations would you write into user training?

### Chapter 8 · AI for exploratory analysis and narratives (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Code-executing assistants | ChatGPT data analysis, Claude with code execution, Gemini in Colab, Jupyter AI; reading the code, not the summary | Run one EDA with two assistants; diff their findings |
| 8.2 The forking-paths problem | An AI that tries 50 cuts will find "significant" ones; correcting for multiple comparisons | Ask for "interesting findings" on noise; count false discoveries |
| 8.3 Verifying an analysis | Recompute key numbers, check denominators and units, check the statistical test and its unit | Audit 5 AI analyses with planted errors |
| 8.4 Narrative checking | Every sentence traced to a query result; causal words removed unless the design supports them | Line-by-line fact check of an AI-written weekly business review |

**Check your understanding:** Why are "interesting findings" from an AI exploration usually exploratory hypotheses, not results? What is the minimum you must check before forwarding an AI analysis? Which words in a generated summary trigger a check?

### Chapter 9 · Building a guarded analytics assistant (weeks 10–11)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Architecture | Router → semantic layer or verified query → SQL generation → validation → execution → result checks → answer with provenance | Design document with failure handling for each stage |
| 9.2 Static validation | Parse with `sqlglot`; allow-listed schemas; forbid DDL and DML; enforce `LIMIT`; dialect transpilation | Validator that blocks 20 unsafe or out-of-scope queries |
| 9.3 Safe execution | Read-only roles, row-level security inherited from the user, BigQuery dry-run byte caps, timeouts | Execution layer that refuses a query over 10 GB |
| 9.4 Result checks | Empty results, implausible magnitudes, row-count explosions, comparison with a certified metric | Add 6 sanity checks; show each firing |
| 9.5 Answers with provenance | Show the SQL, the definitions used, data freshness and a confidence label; log everything | Answer format plus an audit log you can query |

**Check your understanding:** Why should the assistant try the semantic layer before generating raw SQL? What must the execution role never be able to do? How does showing the SQL change user trust, and for which users?

### Chapter 10 · Security and governance of AI answers (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Prompt injection through data | Instructions hidden in text fields or documents (OWASP Top 10 for LLM Applications 2025: LLM01 Prompt Injection, LLM06 Excessive Agency) | Show, on your own test data, how a malicious comment field changes an assistant's behaviour; then defend it |
| 10.2 Permissions and PII | Row-level security passing through to AI answers; masking; small-cell suppression | Prove a regional user cannot extract another region's numbers via the assistant |
| 10.3 Data residency and contracts | Power BI's tenant setting for processing outside the geographic region; cross-border processing and India's DPDP Rules, 2025 | A one-page data-flow note for an India-hosted tenant |
| 10.4 Verified answers and approval | Who certifies a verified answer; expiry and review cycles | An approval workflow with owners |
| 10.5 Incident response | When an AI answer was wrong and used: detection, correction, notification, root cause | Run a tabletop exercise on a wrong revenue figure sent to leadership |

**Check your understanding:** Why does an analytics agent with write access turn prompt injection from a nuisance into a serious risk? What does row-level security have to do with chat interfaces? What goes in a post-incident review of a wrong AI-generated number?

### Chapter 11 · The analyst's job, redesigned (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 New responsibilities | Curating gold sets, semantic layers and verified answers; monitoring accuracy; teaching users the limits | A job description for an "analytics AI owner" |
| 11.2 Keeping core skills | AI-off SQL and statistics drills; why reviewers need to be able to do the work themselves | Timed AI-off SQL round |
| 11.3 Measuring impact | Time saved vs errors introduced; adoption vs trust; a dashboard for the assistant itself | Instrument your P3 assistant |
| 11.4 Demo day | Present P3 with live failure demonstrations | Demo and panel questions |

**Check your understanding:** Which analyst tasks became more valuable because of AI, and why? How would you know if an assistant is making a team faster but less correct? What should every user of a data copilot be told on day one?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · AI surface map and case comparison | — |
| 2 | 2 | Lab 2 · Retrieval and candidates | — |
| 3 | 3 | Lab 3 · Benchmark hands-on | Leaderboard critique |
| 4 | 4 | Lab 4 · Failure zoo | **P1 due** |
| 5 | 5 | Lab 5 · Gold set and scorer | — |
| 6 | 5 | Lab 5 (cont.) · Test suites and CI gate | Mid-term (AI off: SQL + taxonomy) |
| 7 | 6 | Lab 6 · Context ablation | — |
| 8 | 7 | Lab 7 · Copilot bake-off | — |
| 9 | 8 | Lab 8 · Forking paths and narrative audit | **P2 due** |
| 10 | 9 | Lab 9 · Validator and safe execution | — |
| 11 | 9 | Lab 9 (cont.) · Provenance | — |
| 12 | 10 | Lab 10 · Injection and permissions | Data-flow note |
| 13 | 11 | Assistant instrumentation | — |
| 14 | 11 | Demo day | **P3 due** |
| 15 | Review | Oral defence | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** everything you are evaluating (that is the point), plus scaffolding harness code, generating paraphrases of gold questions, and producing perturbed test databases. Claude, ChatGPT, Gemini, Power BI Copilot, Looker Conversational Analytics, Cortex Analyst and Genie all appear in labs.
- **Do without AI (drills):** writing gold SQL for every gold question; scoring disputed cases by hand; weekly AI-off SQL sets; designing the taxonomy; the mid-term and final. A gold set written by the system under test is not a gold set.
- **Verify AI output by:**
  - result-set equality against gold SQL on the original and perturbed databases;
  - checking the definitions and filters an answer used;
  - repeating a question to measure variance;
  - comparing with certified semantic-layer metrics;
  - reading the generated SQL before trusting any number.
- **Where AI still fails here:** the benchmark gaps in "Why this course matters now", plus vendor-documented limits: general-knowledge fallback in Power BI, no reuse of earlier results across turns in Cortex Analyst, and unsupported forecasting and anomaly questions in Looker. Uber reports that hallucinated tables were not fully solved. Your failure zoo (Lab 4) and P2 harness are your own evidence, and they are what employers will ask about.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 20% |
| Projects P1 · P2 · P3 | 10% · 20% · 25% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) + oral defence of P3 | 15% |

**Mastery gate.** You pass when you can: (1) given an unseen warehouse and 15 questions, write gold SQL with AI off and build a scorer that grades an assistant by result equality in 2 hours; (2) reproduce, on request, at least 6 failure classes from the taxonomy against a live copilot, and fix each with context, a semantic definition or a guardrail; (3) demonstrate an assistant that refuses unsafe, out-of-scope and over-budget queries, enforces row-level security and shows provenance for every answer.

## Industry reality

Large companies build internal text-to-SQL tools (Uber's QueryGPT, Swiggy's Hermes) and buy vendor copilots, and both face the same issues: context, evaluation and trust. Vendor documentation now asks customers to prepare semantic models, add verified answers and set AI instructions, which is analyst and analytics-engineering work. Interviews for senior analyst and analytics-engineering roles increasingly ask how candidates use AI and how they check it.

**Interview questions from this course**

1. *"Our CEO wants to ask the data warehouse questions in plain English. How would you do it safely?"* Strong answer: start with a governed semantic layer and verified queries; route questions; read-only, permission-aware execution with cost limits; provenance and confidence labels; a gold-set evaluation with a release gate; human review for high-stakes numbers.
2. *"How do you measure the accuracy of a text-to-SQL system?"* Strong answer: real questions with gold SQL; result-set equality, not text similarity; perturbed databases; component metrics; repeated runs with intervals; abstention and clarification rates; cost and latency.
3. *"An AI tool says revenue grew 12%; finance says 9%. What do you do?"* Strong answer: get the generated SQL; compare definitions (gross vs net, refunds, taxes), time windows and time zones, filters and joins; reconcile with the certified metric; fix the definition or the tool; log the incident.
4. *"What is prompt injection, and why does it matter for analytics?"* Strong answer: instructions hidden in data that the model treats as commands; risks with tool-using agents; least privilege, read-only roles, input isolation, output validation, no write tools; OWASP LLM01.
5. *"Will AI replace data analysts?"* Strong answer: cites concrete evidence (benchmark gaps, vendor limits, adoption data); separates automated drafting from owned judgement (definitions, verification, causal reasoning, communication); describes how the role shifts toward curating context and verifying answers.

## Resources (free first)

- **Benchmarks:** [BIRD](https://bird-bench.github.io/); [BIRD-Interact](https://bird-interact.github.io/); [LiveSQLBench](https://livesqlbench.ai/); [Spider 2.0](https://spider2-sql.github.io/) and [paper](https://arxiv.org/abs/2411.07763); [DABstep](https://huggingface.co/spaces/adyen/DABstep) and [paper](https://arxiv.org/abs/2506.23719).
- **Methods:** [DIN-SQL](https://arxiv.org/abs/2304.11015); [CHASE-SQL](https://arxiv.org/abs/2410.01943); Zhong, Yu and Klein, [test-suite accuracy](https://arxiv.org/abs/2010.02840); Sequeda et al., [knowledge graphs and LLM accuracy](https://arxiv.org/abs/2311.07509).
- **Case studies:** [Uber QueryGPT](https://www.uber.com/blog/query-gpt/); [Swiggy Hermes](https://medium.com/swiggy-bytes/hermes-a-text-to-sql-solution-at-swiggy-81573fb4fb6e).
- **Vendor docs:** [Copilot for Power BI](https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-introduction) and [privacy and security](https://learn.microsoft.com/en-us/fabric/get-started/copilot-power-bi-privacy-security); [Conversational Analytics in Looker](https://docs.cloud.google.com/looker/docs/conversational-analytics-overview); [Cortex Analyst](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst); [Databricks Genie](https://docs.databricks.com/aws/en/genie/); [Tableau Pulse](https://help.tableau.com/current/online/en-us/pulse_intro.htm); [Gemini in BigQuery](https://docs.cloud.google.com/bigquery/docs/gemini-overview).
- **Tools:** [sqlglot](https://github.com/tobymao/sqlglot); [Jupyter AI](https://github.com/jupyterlab/jupyter-ai); [Model Context Protocol](https://modelcontextprotocol.io/).
- **Security:** [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/).

## Sources

All checked 12 Oct 2026.

- BIRD leaderboard and BIRD-Interact results (updated 9 Oct 2026) — https://bird-bench.github.io/
- Spider 2.0 site and leaderboards — https://spider2-sql.github.io/ · Lei et al., "Spider 2.0" (ICLR 2025) — https://arxiv.org/abs/2411.07763
- Egg et al., "DABstep" (arXiv 2506.23719, Jun 2025) — https://arxiv.org/abs/2506.23719
- Uber Engineering, QueryGPT (19 Sep 2024) — https://www.uber.com/blog/query-gpt/
- Microsoft Learn, Copilot for Power BI overview (updated 24 Aug 2026) — https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-introduction
- Google Cloud, Conversational Analytics in Looker (updated 9 Oct 2026) — https://docs.cloud.google.com/looker/docs/conversational-analytics-overview
- Snowflake, Cortex Analyst — https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-analyst
- Databricks, Genie (updated 18 Sep 2026) — https://docs.databricks.com/aws/en/genie/
- Tableau Help, Tableau Pulse — https://help.tableau.com/current/online/en-us/pulse_intro.htm
- dbt Labs, 2025 State of Analytics Engineering — https://www.getdbt.com/resources/state-of-analytics-engineering-2025
- Microsoft Support, COPILOT function — https://support.microsoft.com/en-us/office/copilot-function-5849821b-755d-4030-a38b-9e20be0cbf62
- Wang et al., CharXiv (arXiv 2406.18521, 2024) — https://arxiv.org/abs/2406.18521

_Last reviewed: 2026-10_
