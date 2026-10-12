# FDE501 · Labs and projects

Seminar labs use your own FDE404 deployment records (decision logs, time logs, AI-failure logs, field reports) as data, plus public sources. Any study involving people, including customer-development interviews, follows RES501's ethics process and has informed consent. Never use confidential information from an employer, co-op host or customer; if in doubt, ask your supervisor and leave it out.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Productisation rubric | Score ten field reports from FDE404 on frequency, workaround cost, willingness to pay and product fit; pick two to pursue | Scored rubric, selection memo | 3 h |
| 2 · Services-economics critique | Critique a16z's "Trading Margin for Moat" with evidence; model a services firm's margin under outcome pricing as automation improves | Essay (≤ 1,500 words), margin model | 5 h |
| 3 · Connector-scaffolding agent | Build an agent skill (MCP tools plus instructions) that scaffolds a connector from an OpenAPI file and a sample response | Skill, tools, ten example runs | 6 h |
| 4 · Agent reliability | Measure pass^k on 20 integration tasks with state-based checks; classify failures | Reliability report, failure taxonomy | 4 h |
| 5 · Upgrade orchestrator and per-customer evals | Simulate 50 sites with different maintenance windows and constraints; gate a model change on five customers' eval suites | Orchestrator, per-customer decisions with evidence | 5 h |
| 6 · Field-study presentation | Present the design, results and validity threats of one field study (NBER w31161, HBS 24-013 or METR 2025) | Slides, one-page critique | 3 h |
| 7 · Governance pack | Map one product deployed to a bank and a hospital against ISO/IEC 42001, NIST AI RMF, RBI FREE-AI, DPDP and the EU AI Act | Mapping, gaps, governance features to build into the product | 4 h |
| 8 · Customer-development interviews | Ten interviews about one problem from your field work; record commitments (letters of intent, paid pilots, introductions), not compliments | Consent records, interview notes, commitment log | 8 h |
| 9 · 24-month venture model | Revenue, services and software margins, hiring plan, cash; sensitivity on three drivers | Model, assumptions register | 4 h |
| 10 · Proposal review | Review two classmates' proposals with the course rubric; revise your own | Reviews, revision log | 3 h |

## Projects

### P1 · A pattern library from your deployments (L1, ~6 hours)

**Real-world inspiration.** OpenAI measures Deployment Leads on "operating leverage (patterns reused across deployments)"; Anthropic asks FDEs to "identify and codify repeatable deployment patterns"; Palantir's Deltas decide between building into the core platform and building custom (2019).

**What to build.** A pattern library from your three FDE404 deployments and your solo deployment: at least eight patterns (for example, "human-review screen with edit tracking", "reconciled webhook ingestion", "evaluation agreement before results"), each with context, problem, solution, evidence of recurrence, cost to apply, and when not to use it.

**Acceptance criteria**
- Every pattern cites at least two deployments where it recurred, with time or defect data.
- Each pattern names its anti-patterns and failure cases.
- A classmate applies two patterns to a new brief and reports whether the descriptions were sufficient.
- A confidentiality review confirms no customer-specific detail is included.

**Stretch goals.** Publish the library openly with illustrative examples only.

**What it proves to an employer.** You turn experience into reusable knowledge, which is the senior-FDE and product-minded habit employers ask for.

### P2 · A deployment kit as a product, measured on a fresh customer (L2, ~15 hours)

**Real-world inspiration.** a16z describes the best services teams automating "process mining, data pipeline automation, system integrations, and combing through API documentation" (2025); Palantir's Apollo encodes product and environment constraints to automate upgrades across many sites.

**What to build.** Turn your FDE404 P2 component and Lab 3 agent into a small product: installable, documented, configurable, with an evaluation gate. Then run a controlled comparison: two classmates deploy for the same new illustrative customer brief, one with your kit and one with only the course templates.

**Acceptance criteria**
- The kit installs from its README in under 30 minutes on a clean machine.
- Time to first working integration and to first passing evaluation measured for both deployers; defects counted with the same checklist.
- Agent steps report state-based verification; every failed step is surfaced to the human, never silently skipped.
- An honest results section: effect size, what the comparison cannot show (one pair, learning effects), and what you would change.

**Stretch goals.** Repeat with a second pair of deployers and a different brief.

**What it proves to an employer.** You can build platform leverage for a deployment team and measure it honestly.

### P3 · Research paper or venture (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** Field evidence on AI at work comes from staggered rollouts and randomised experiments (NBER w31161; HBS 24-013; METR 2025). Many AI companies started from services and later productised (a16z's argument, 2025).

**What to build.** Choose one track.

- **Research track.** A short paper (6–8 pages, workshop format) on an open problem from Chapter 9, using your deployment data, a designed experiment or a multiple-case study: for example, "Do customer-specific evaluation suites transfer within an industry?" or "How reliable are agents at integration scaffolding?". Pre-register the hypotheses and analysis with your supervisor.
- **Venture track.** A venture memo and a working MVP for a problem from your field experience, supported by your Lab 8 customer-development evidence, with a pricing model, a 24-month plan, a services-to-product strategy and a legal boundaries statement reviewed by your supervisor.

**Acceptance criteria (research)**
- Pre-registration dated before data analysis; deviations reported.
- Methods reproducible from the repository by a reviewer in under three hours.
- A threats-to-validity section reviewed by a classmate; results reported with uncertainty.
- Submitted to a workshop, student venue or preprint server, or accepted as a THS501 proposal.

**Acceptance criteria (venture)**
- At least ten customer interviews and at least two concrete commitments (letter of intent, paid pilot or signed evaluation agreement).
- MVP demonstrated on an illustrative customer workload with an evaluation agreement.
- Pricing and unit economics with ranges; a clear path from services to product.
- Legal boundaries statement confirming no use of employer or customer confidential information.
- Rated "investable with conditions" or better by an external reviewer (mentor, angel or incubator).

**Stretch goals.** Research: release the dataset or benchmark (synthetic or consented). Venture: secure a paid pilot.

**What it proves to an employer or investor.** You can create new knowledge or a new business from field experience, the L5 outcome of this major.

## Feeds into

- [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md) and [THS502](../../../../05_shared_years_3_to_5/THS502_thesis_or_capstone_ii/README.md): the research track becomes the thesis; the venture track can become a capstone.
- [LCH502 Career Launch and Founder Studio](../../../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md): the venture memo and MVP.
- [RES502 Reading, Reproducing and Extending Papers](../../../../05_shared_years_3_to_5/RES502_reading_reproducing_and_extending_papers/README.md): reproduction of a field study's analysis.
