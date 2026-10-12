# SWE402 · Labs and projects

The labs use three provided legacy systems: a 12-year-old Java 8 Spring MVC "insurance policy admin" app with almost no tests, a COBOL batch program set (run with GnuCOBOL) that computes interest and statements, and a small C library. You may substitute a real open-source legacy project with similar traits. Any production-like data you use must be synthetic or properly anonymised. The mid-term and the characterization work in Lab 3 are AI-off; migration labs are AI-heavy by design, with every pipeline run logged.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Options and the case | Assess the policy-admin app: hotspots, dependencies, runtime usage, risks; choose an option per component | One-page case and a component table with option and reason | 4 h |
| 2 · Archaeology and rule extraction | Use an agent to extract 25 business rules from the premium-calculation module with line citations; verify each | Rule catalogue with status (confirmed by test / contradicted / unverifiable) and the agent's error rate | 5 h |
| 3 · Golden masters and seams (AI off) | Approval tests for the premium calculation over 5,000 generated inputs; break 2 hard dependencies with seams | Tests, seam diffs, mutation score of the new tests | 5 h |
| 4 · Strangler proxy | Put a routing proxy in front of the app; move the "policy quote" endpoint to a new service | Routing config, traffic split evidence, rollback demonstration | 5 h |
| 5 · Expand–contract and CDC | Split a `customer` table into two tables online; stream changes with Debezium into the new service's database | Zero-error load test during migration; parity report (counts, checksums, 1% deep sample) | 6 h |
| 6 · Shadow, diff, Scientist | Shadow the new quote service; diff 100,000 responses with noise filters; wrap one refactored method in a Scientist-style experiment | Mismatch classification, fixes, final mismatch rate | 5 h |
| 7 · Codemods | OpenRewrite recipe set to move the app from JUnit 4 to JUnit 5 and from `java.util.Date` to `java.time` in one package; an ast-grep rule for a deprecated internal API | Recipes, the diff, and the list of cases the recipes could not handle | 5 h |
| 8 · LLM migration pipeline | Pipeline: shard → context → generate → compile/test/lint → retry with errors → human queue; migrate 200 test files between frameworks | Pass rate per stage, retries per file, cost per file, and the sample-tune-sweep changes that raised the pass rate | 8 h |
| 9 · COBOL or C translation with equivalence proof | Track A: translate one COBOL interest program to Java with `BigDecimal`; Track B: translate the C library to Rust | Equivalence evidence: 10,000-record golden comparison (A) or differential fuzzing for 1 hour (B); idiomaticity review | 6 h |
| 10 · Kill switches and burn-down | Flag per migrated slice with automatic rollback on mismatch > 0.1%; migration burn-down chart from real data | Drill recording or logs; the chart with its data source | 4 h |

## Projects

### P1 · Rescue a legacy module (L1, ~6 hours)

**Real-world inspiration:** the most common legacy task in industry: "add this feature to code nobody understands, by Friday, without breaking anything".

**What to build:** in the policy-admin app (or an open-source legacy project), add a new rider (an optional insurance add-on) that changes premium calculation. Pin the existing behaviour first, then add the feature with sprout or wrap techniques.

**Acceptance criteria:**
- Characterization tests written before any production-code change (commit order proves it), covering the premium path with mutation score ≥ 60%.
- Existing behaviour unchanged for all 5,000 golden inputs; new behaviour covered by at least 10 example tests and 2 property tests.
- No method in your change exceeds cognitive complexity 15; the old code is touched in at most 3 places.
- A one-page note on what you learned about the module that was not documented anywhere.

**Stretch goals:** have an agent attempt the same task without characterization tests first; compare the regressions it introduces.

**What it proves to an employer:** you can change legacy code safely on a deadline, the most frequent senior-engineer task there is.

### P2 · AI-assisted framework migration pipeline (L2, ~15 hours)

**Real-world inspiration:** Airbnb's Enzyme-to-React-Testing-Library migration (about 3,500 files in six weeks with validation-and-retry loops) and Google's JUnit 3 to 4 migration (5,359 files in three months).

**What to build:** a reusable migration pipeline for one real migration on an open-source codebase with at least 300 affected files (for example JUnit 4 → 5, Enzyme → React Testing Library, Python `unittest` → `pytest`, or a deprecated SDK version). Combine deterministic recipes for regular patterns with an LLM for the remainder.

**Acceptance criteria:**
- Every migrated file passes compile, lint, type-check and its tests; the full suite's pass/fail set is identical before and after (excluding documented, pre-existing flaky tests).
- Report: share handled by codemod vs LLM vs human; pass rate after first pass and after tuning; retries per file distribution; cost per file in tokens and in human minutes.
- Risk-based review: a written sampling plan, and evidence it was followed (reviewed sample, defects found, extrapolated defect rate with an interval).
- No test assertion weakened: a script compares assertion counts and types per test before and after and lists every difference, each one justified.
- The pipeline is re-runnable from one command on a fresh checkout.

**Stretch goals:** upstream the migration (or a first batch) to the project; publish the pipeline as a template.

**What it proves to an employer:** you can run AI migrations with engineering rigour and honest numbers, a capability many companies are now hiring for.

### P3 · Strangle a legacy system in production conditions (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** banks, insurers and government portals replacing monolith functions slice by slice while the old system keeps running; Fowler and Thoughtworks' legacy displacement patterns. The system is **illustrative**; the techniques are standard.

**What to build:** move two business capabilities of the policy-admin app (for example quotes and policy endorsements) to a new service in a modern stack (Java 25 or Go 1.27 or Kotlin), including data. Use a strangler facade, an anti-corruption layer, CDC-based data sync, shadow traffic with diffing, Scientist-style experiments for one refactored rule, and flags with automatic rollback. Agents may write the new code; you own specification, equivalence and rollout.

**Acceptance criteria:**
- Equivalence specification signed off by a "domain owner" (an instructor or classmate role), listing every acceptable difference.
- Shadow traffic of at least 500,000 replayed requests with a final unexplained mismatch rate below 0.01% for quotes and zero for monetary fields in endorsements.
- Data parity: counts match exactly; checksums match per partition; a 1% deep sample shows zero differences, re-checked after a simulated week of writes.
- Cutover under load (200 requests/s) with zero failed requests, then a drilled rollback to the old path within 60 seconds and a second cutover.
- The old code paths for both capabilities are removed, with a decommissioning checklist completed.
- Migration report: plan vs actual, burn-down, incidents (real or drilled), cost (including AI usage) and lessons.

**Stretch goals:** add a third capability using only agents for implementation under your gates, and compare its defect rate with the first two; translate one COBOL batch job and run it in parallel with the original for a month of synthetic data.

**What it proves to an employer:** you can modernize a live system without an outage and prove that nothing changed that should not have, which is exactly what large enterprises and IT services firms need from senior engineers.

## Feeds into

- [THS501 Thesis or Capstone I](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md): P3 is a strong industry capstone base.
- [SWE501 Frontier Seminar](../../year_5/SWE501_frontier_seminar_agentic_software_engineering/README.md): equivalence checking and translation verification are open research problems.
- [SWE404 Engineering Leadership and Technical Strategy](../SWE404_engineering_leadership_and_technical_strategy/README.md): the modernization case and status reporting become strategy documents.
- [IND401 Industry Co-op Studio](../../../../05_shared_years_3_to_5/IND401_industry_co_op_studio/README.md): co-op placements often involve legacy systems; P1's method applies on day one.
