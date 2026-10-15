# QAE301 · Labs and projects

Every lab and project uses a **bug zoo**: a set of deliberately faulty implementations of the same specification, provided by the instructor or built by a classmate, plus a correct reference kept hidden. Your test design is scored by how many faulty versions it detects, not by how many tests you write. Every test case must name the technique and the risk it comes from. Exploratory work happens only on applications you run yourself or on public demo sites whose terms allow testing; never probe production systems you do not own.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Input space and quality model | Count the input space of a 6-field sign-up form; map 15 real app-store complaints to ISO/IEC 25010:2023 characteristics | Arithmetic with assumptions; mapping table with one sentence per complaint | 2 h |
| 2 · Risk workshop | Run a 45-minute risk session with two classmates acting as product owner and support lead for an illustrative wallet app | Risk register (≥ 20 risks, likelihood, impact, owner) and an 80-hour test-effort allocation | 3 h |
| 3 · Boundary bug zoo | Apply EP, 2- and 3-value BVA and domain testing to a fee calculator with 12 faulty versions (rounding, paise, inclusive/exclusive limits, Unicode lengths) | pytest suite; detection table per faulty version; one paragraph per miss | 4 h |
| 4 · Decision tables and MC/DC | Model a ticket-refund policy (4 conditions); collapse it; build an MC/DC set for a 4-condition guard | Full and collapsed tables, MC/DC proof table, tests that run | 3 h |
| 5 · State models and stateful tests | Model an order lifecycle; derive 0-switch and 1-switch suites; write a Hypothesis `RuleBasedStateMachine` | Diagram, state table with invalid transitions, both suites, the shrunk failing sequence for the seeded bug | 4 h |
| 6 · Pairwise with PICT | PICT model for browser × OS × locale × payment method × network with constraints; run 2-way and 3-way sets on a simulator with planted interaction faults | Models, generated sets, faults found per strength, cost per fault | 3 h |
| 7 · Coverage vs mutation | Write a 100%-branch-coverage suite that kills < 30% of mutants, then raise the mutation score by ≥ 30 points | Both suites, coverage and mutmut reports, list of equivalent mutants with reasons | 4 h |
| 8 · Differential and metamorphic oracles | Differential-test two JSON parsers on generated input; write 5 metamorphic relations for a route-distance function | Harness, disagreements triaged (bug in A, bug in B, spec gap), relation tests | 4 h |
| 9 · Session-based exploratory testing | Three 60-minute chartered sessions on a self-hosted RealWorld (Conduit) implementation | Session sheets (charter, notes, bugs, issues, % on charter), PROOF debrief notes | 4 h |
| 10 · AI vs technique | Generate tests for P1's spec with two AI tools, once from the spec and once from the buggy code | Bug-zoo detection and mutation score for each AI suite vs yours; list of planted bugs the code-derived suite "confirmed" | 4 h |

## Projects

### P1 · Fee and tax calculator test design (L1, ~6 hours)

**Real-world inspiration:** income-tax and fee calculators, where slabs, rebates and rounding rules create many boundaries. Take the slab rules for one assessment year from the [Income Tax Department portal](https://www.incometax.gov.in/iec/foportal/) or use the instructor's illustrative fee schedule; do not invent rules.

**What to build:** a test design document and a pytest suite for a calculator specification (slabs, a rebate condition, a surcharge condition, rounding to the nearest rupee, invalid inputs). Use equivalence partitioning, boundary value analysis and a decision table for the rebate and surcharge rules.

**Acceptance criteria:**
- Every test case carries an ID, the technique, the partition or rule it covers, and the expected value computed by hand from the specification (not from running the reference).
- The suite detects at least 18 of the 20 faulty implementations in the bug zoo with at most 60 test cases.
- A traceability table maps each specification clause to at least one test; any clause without a test is listed as residual risk.
- Mutation score of the suite against the reference implementation ≥ 85% (mutmut), with equivalent mutants justified.

**Stretch goals:** add property tests (monotonicity: higher income never yields lower tax before rebate); compare the number of tests needed for 3-value vs 2-value BVA.

**What it proves to an employer:** you derive tests from specifications with named techniques and can show that they find faults, which is the core of every "how would you test this?" round.

### P2 · Risk-based exploratory campaign on a real web app (L2, ~15 hours)

**Real-world inspiration:** product teams that run session-based exploratory testing before a release alongside their automated checks. The target is a [RealWorld (Conduit)](https://docs.realworld.show/) frontend and backend pair that you run locally; pick a less-used implementation pair, which is more likely to contain real bugs.

**What to build:** a risk register for the app; 8 chartered sessions (60–90 minutes each) covering at least four SFDIPOT families; a state model of the article lifecycle (draft, published, edited, deleted, favourited, commented); 20 automated checks for the top risks (pytest + httpx against the API, or Playwright); a test summary report.

**Acceptance criteria:**
- Risk register with ≥ 25 risks; each session charter traces to one or more risks.
- Session sheets show ≥ 70% of time on charter, with notes another tester can follow.
- ≥ 5 reproducible bugs with reports that score ≥ 4/5 on the course rubric (summary, minimal steps, expected vs actual, evidence, impact); if fewer than 5 real bugs exist, the report shows the coverage achieved and why.
- At least one bug filed upstream on the implementation's repository, following its contribution rules, or a written reason why it was not appropriate.
- The 20 automated checks pass 50 consecutive runs with no flaky result.
- The summary report states residual risk by area and a go/no-go recommendation.

**Stretch goals:** run the same charters on a second implementation of the same RealWorld spec and compare defect profiles (differential exploration).

**What it proves to an employer:** you can find real bugs in software you did not write, communicate them well, and connect testing effort to risk.

### P3 · Test strategy for a real open-source application (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** the quality programmes of mature open-source projects and enterprise ERP rollouts. Recommended target: one business flow of [ERPNext](https://github.com/frappe/erpnext) (for example quotation → sales order → delivery note → sales invoice → payment entry, with taxes and partial deliveries), run locally with its documented setup. Alternatives with the instructor's approval: [AntennaPod](https://github.com/AntennaPod/AntennaPod) or [Kiwix Android](https://github.com/kiwix/kiwix-android).

**What to build:**
1. A product risk analysis (≥ 30 risks) with a stakeholder interview (a maintainer's public issues, discussions or roadmap can stand in for a stakeholder).
2. A test strategy: levels, techniques per risk, oracles, data, environments, entry and exit criteria, what is out of scope.
3. Test designs using at least five techniques from this course, including a state model and a decision table drawn from the application's real business rules.
4. At least 60 automated tests on the riskiest paths using the project's own test framework (for ERPNext, the [Frappe testing tools](https://docs.frappe.io/framework/user/en/testing)) or its API.
5. A mutation-testing run on one module you chose by risk.
6. A test summary report with residual risk and a one-page "what I would test next with twice the time".

**Acceptance criteria:**
- Every automated test traces to a risk and a technique; the traceability table is generated, not hand-maintained.
- The suite passes 30 consecutive runs locally with zero flaky results.
- Mutation score on the chosen module is reported with equivalent mutants triaged; it improves by ≥ 15 points over the project's existing tests for that module, or you explain why existing tests already saturate it.
- At least 2 issues filed upstream with reproducible steps, linked in the report, plus the maintainers' response if any; issues must follow the project's reporting guidelines.
- A 10-minute defence where you justify the three highest-risk decisions and one thing you chose not to test.

**Stretch goals:** submit one of your tests upstream as a pull request; generate a second suite with an AI tool and compare (feeds QAE401).

**What it proves to an employer:** you can walk into an unfamiliar, real business application and produce a defensible strategy, working tests and accepted bug reports in a few weeks, which is what a QE lead expects of a new hire.

## Feeds into

- [QAE302 Test Automation Engineering](../QAE302_test_automation_engineering_ui_and_api/README.md): P2 and P3 test designs become automated suites.
- [QAE401 AI in Testing](../../year_4/QAE401_ai_in_testing_generated_tests_self_healing/README.md): Lab 10 and the bug-zoo method are the evaluation method for AI tools.
- [QAE404 Quality Engineering Leadership](../../year_4/QAE404_quality_engineering_leadership_and_metrics/README.md): risk analysis and residual-risk reporting at organisation scale.
- [QAE flagship industry project](../../../../06_career_and_market_readiness/05_industry_projects/QAE_software_quality_test_engineering.md): P3's strategy is its first deliverable.
