# DAN401 · Labs and projects

Every lab and project ships with the prompts, model names and versions, dates of each run, raw outputs, and the scoring code, so that someone else can rerun your evaluation. Accuracy figures always carry their denominator and, where runs repeat, an interval. All security exercises use your own test data and systems only.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · AI surface map and case comparison | Map every AI surface over data in a case organisation; compare Uber QueryGPT's and Swiggy Hermes' published designs | Surface map; a one-page design comparison with lessons for your own team | 3 h |
| 2 · Retrieval and candidates | Table retrieval over a 200-table schema; single-shot vs best-of-5 candidates with execution checks | Table recall@k; accuracy of both strategies on 30 questions; cost per question | 5 h |
| 3 · Benchmark hands-on | Run 10 Spider 2.0-Lite or BIRD mini-dev tasks with one assistant; attempt 5 DABstep tasks yourself | Your scores vs the assistant's; a one-page critique of one leaderboard entry | 4 h |
| 4 · Failure zoo | Reproduce 10 failure classes on TheLook with two assistants | For each: prompt, output, why it is wrong, the gold answer, and the fix | 5 h |
| 5 · Gold set, scorer and CI gate | 60 gold questions; result-equality scorer; 3 perturbed databases; a CI job that fails on regressions beyond the noise band | Gold set with tiers, scorer with 12 unit tests, CI config, a run report | 6 h |
| 6 · Context ablation | Measure accuracy as you add dialect, grain, definitions, time zone, examples and verified queries | Accuracy-vs-context chart with intervals; the element that helped most | 4 h |
| 7 · Copilot bake-off | Run 20 gold questions through two of: Power BI Copilot, Looker Conversational Analytics, Cortex Analyst, Genie, BigQuery's Gemini features (trial or free tiers where available) | Accuracy, abstention and clarification rates per tool; configuration steps that changed results | 5 h |
| 8 · Forking paths and narrative audit | Ask an assistant for "interesting findings" on data with no real effects; fact-check an AI-written weekly business review | False-discovery count; a sentence-by-sentence audit table | 3 h |
| 9 · Validator, safe execution and provenance | `sqlglot` validator, read-only role, dry-run byte cap, timeouts, answer format with SQL, definitions and freshness | Code, 20 blocked-query tests, and sample answers with provenance | 6 h |
| 10 · Injection and permissions | On your own test warehouse, show that instruction-like text in a data field can alter an assistant's behaviour; add defences; test row-level security through the assistant | Before/after behaviour, the defences, and an RLS leakage test that passes | 4 h |

## Projects

### P1 · Field guide to AI analytics failures (L1, ~6 hours)

**Real-world inspiration.** Uber's QueryGPT write-up lists hallucinated tables, vague prompts and multiple valid answers as unsolved problems; vendor documentation lists scope limits. Teams adopting copilots need a concrete field guide for their users.

**What to build.** A field guide of at least 10 failure classes reproduced on a public warehouse (BigQuery `thelook_ecommerce` or a DuckDB extract) with two different assistants. Each entry: a minimal prompt that triggers the failure, the output, the gold answer, why the error is easy to miss, and the prevention (definition, semantic-layer metric, verified query, guardrail or user training).

**Acceptance criteria**
- At least 10 distinct classes, including fan-out, wrong grain, time-zone, `NULL` handling, silent business definition, ambiguous question answered without clarification, and out-of-scope answer.
- Each failure is reproducible: rerun 5 times, with the failure rate reported.
- Each prevention is tested: the same prompt after the fix, with the new failure rate.
- A one-page summary ranks the failures by how likely they are to reach a decision unnoticed.

**Stretch goals.** Add a third assistant; turn the guide into a short user-training module with a 10-question quiz.

**What it proves to an employer.** You understand concretely how AI answers go wrong on data, and you can teach others to catch it.

### P2 · Open text-to-SQL evaluation harness (L2, ~15 hours)

**Real-world inspiration.** Uber evaluates QueryGPT with a golden set, component signals and tracking over time. Academic work (BIRD, Spider 2.0, test-suite accuracy) gives scoring methods. Few teams have a reusable harness for their own warehouse.

**What to build.** An open-source Python package and CLI that, given a warehouse connection, a gold set and a system under test, produces an evaluation report. Features: result-set equality with configurable tolerance; test-suite scoring on perturbed databases; component metrics (table recall, clarification, abstention); repeated runs with intervals; cost and latency; HTML or Markdown report; a CI regression gate. Evaluate at least three configurations: raw schema, schema with descriptions and definitions, and semantic layer or verified queries (from your DAN304 work).

**Acceptance criteria**
- At least 60 gold questions in 3 difficulty tiers, written and verified with AI off, each with gold SQL and gold results.
- The scorer passes unit tests for column order, row order, duplicate rows, floats, `NULL`s, extra columns and renamed columns.
- Perturbed-database scoring finds at least 2 queries that pass on the original but are wrong.
- Each configuration is run at least 3 times; accuracy is reported with a 95% interval, and differences between configurations are stated only where the intervals support them.
- A new user can run the harness against DuckDB from the README in under 15 minutes.

**Stretch goals.** Plug in an LLM-as-judge and measure how often it disagrees with result equality; add an "ambiguity" tier where the correct behaviour is to ask.

**What it proves to an employer.** You can tell a team, with evidence, how accurate their AI analytics really is and whether a change made it better, which few people can do today.

### P3 · Guarded analytics assistant for a governed warehouse (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** Organisations want leaders to ask questions in plain language without exposing data or producing wrong numbers. Vendor copilots and internal tools such as QueryGPT combine retrieval, semantic grounding and validation. The deployment scenario below is illustrative.

**What to build.** An assistant over your DAN304 P3 payments warehouse (or TheLook with a semantic layer) for three user roles with different permissions:
1. A router that sends metric questions to the semantic layer or verified queries, and other questions to guarded SQL generation.
2. Static validation (`sqlglot`), an allow-list of schemas, a read-only role per user with row-level security, dry-run cost caps and timeouts.
3. Result checks (empty, implausible magnitude, row explosion, mismatch with certified metric).
4. Answers with SQL, definitions used, data freshness and a confidence label; abstention with a helpful message when out of scope.
5. Full audit logging and a small dashboard of the assistant's own accuracy, cost and abstention rate.
6. An incident runbook for a wrong number that reached a decision-maker.

**Acceptance criteria**
- On your P2 harness, accuracy on in-scope questions beats a raw-schema baseline by a margin larger than both intervals, reported with the denominator.
- On a 20-question out-of-scope set, the assistant abstains or asks for clarification on at least 16.
- On a 50-query red-team set of unsafe or over-budget requests built on your own system, zero unsafe statements execute.
- Row-level security leakage tests pass for all three roles.
- Every answer in a sample of 30 shows SQL, definitions and freshness; p95 latency and cost per question are reported.
- Demo day: a panel member asks 5 unseen questions live; you explain each answer's provenance, and any failure, on the spot.

**Stretch goals.** Expose the assistant as an MCP server for other tools; add a "second opinion" mode that computes the same answer two ways and flags disagreement; run a usability test with 5 non-technical users.

**What it proves to an employer.** You can ship AI analytics that is measurably accurate, safe and auditable, the capability every data team is being asked for in 2026.

## Feeds into

- [DAN501 Frontier Seminar](../../year_5/DAN501_frontier_seminar_decision_intelligence/README.md): automated insight generation and decision support build on this course's evaluation methods.
- [OV06B Semantic Layers and Self-Serve Analytics with AI](../../../../04_overlaps/OV06_data_platform_analytics_engineering/OV06B_semantic_layers_and_self_serve_analytics_with_ai/README.md): self-serve analytics at platform scale.
- [DAN404 Data Governance, Quality and Privacy for Analysts](../DAN404_data_governance_quality_and_privacy_for_analysts/README.md): governance of AI answers joins the wider governance programme.
- [THS501 Thesis or Capstone I](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md): an evaluation of AI analytics on a new domain is a strong thesis topic.
- [CAR401 Career Lab II](../../../../05_shared_years_3_to_5/CAR401_career_lab_ii_interviews_system_design_and_ai/README.md): P2 and P3 are the portfolio evidence for AI-era analyst interviews.
