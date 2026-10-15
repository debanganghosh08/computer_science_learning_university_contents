# Portfolio, resume and GitHub

| Used in | Start | Produces | Back to |
|---|---|---|---|
| [CAR301](../../05_shared_years_3_to_5/CAR301_career_lab_i_dsa_mastery_portfolio_and_open/) (main), [IND401](../../05_shared_years_3_to_5/IND401_industry_co_op_studio/), [CAR401](../../05_shared_years_3_to_5/CAR401_career_lab_ii_interviews_system_design_and_ai/) | Year 3, semester 5 | A resume, a GitHub profile, written case studies, a LinkedIn profile, open-source contributions | [Career hub](../README.md) |

A portfolio is a set of claims plus the evidence for each claim. A resume makes the claims in one page. GitHub, case studies and open-source contributions are the evidence. LinkedIn helps people find both. When AI tools can produce a plausible project in an afternoon, the evidence that still separates candidates is the kind that is hard to fake: **measured results, written trade-offs, code that others reviewed and merged, and the ability to explain all of it live**.

## Pages

| Page | What it covers | Time to a first version |
|---|---|---|
| [resume.md](resume.md) | One-page resumes for intern, new-graduate and experienced levels; Markdown and LaTeX templates; how applicant tracking systems really work; quantified bullets; honest AI-assisted writing | 6 hours |
| [github_profile.md](github_profile.md) | Profile README, pinned repositories, contribution-graph myths, project READMEs, licences, secrets hygiene | 5 hours |
| [case_studies_and_writing.md](case_studies_and_writing.md) | Writing project case studies and technical blog posts that hiring managers read | 4 hours per piece |
| [linkedin_and_personal_brand.md](linkedin_and_personal_brand.md) | A credible, non-spammy presence; outreach etiquette; job-scam warning signs | 3 hours |
| [open_source.md](open_source.md) | Finding projects, the first contribution, AI-generated contribution etiquette, GSoC, Outreachy, LFX, MLH Fellowship and others with 2026 dates | 10–20 hours to a first merged pull request |

## The portfolio in one table

| Evidence | Minimum for intern-ready (L2) | Minimum for job-ready (L3) |
|---|---|---|
| Resume | One page, 3 projects, every bullet with an action and a result | One page, flagship project first, every bullet measured or verifiable |
| Repositories | 3 pinned, each builds from a clean clone with one command, tests in CI | Flagship project with tests, CI, a deployed demo, a design document and an evaluation or load-test report |
| Writing | One case study | Three: the flagship, one debugging or incident story, one design decision |
| Open source | 2 merged pull requests in projects you do not own | Sustained contributions to one project (5+ merged pull requests, or a maintained feature) |
| References | One mentor or teacher | One manager or maintainer who has reviewed your work |

## Weekly rhythm during CAR301

| Week | Task |
|---|---|
| 1 | Choose a target role ([market map](../01_market_map/README.md)); collect 10 real job descriptions for it; highlight repeated requirements |
| 2 | Resume v1 from the [template](resume.md#4-templates) for your level |
| 3 | GitHub clean-up: profile README, archive weak repos, pin 3 ([guide](github_profile.md)) |
| 4 | Rewrite the READMEs of the 3 pinned repositories |
| 5–6 | Find an open-source project and land a first contribution ([guide](open_source.md)) |
| 7 | Case study of your best project ([guide](case_studies_and_writing.md)) |
| 8 | LinkedIn profile aligned with the resume ([guide](linkedin_and_personal_brand.md)) |
| 9 | Two external reviews of the resume and profile; revise |
| 10–14 | One merged contribution and one written piece every two weeks |

## Common mistakes

- **Tutorial clones as projects.** A to-do app or a Netflix clone shows you can follow instructions. Add something a tutorial does not have: real users, a measured constraint (for example, "p95 latency under 200 ms at 500 requests per second"), a failure you diagnosed, or a design choice with alternatives you rejected.
- **Claims without evidence.** "Built a scalable microservice architecture" invites the question "how many requests per second, and how did you measure it?" Have the answer, or rewrite the line.
- **Ten half-finished repositories.** Three finished, documented projects beat ten abandoned ones. Archive or make private what you would not discuss in an interview.
- **AI-written everything.** Reviewers increasingly recognise generic AI phrasing. More importantly, you will be asked about every line. See [honest AI-assisted writing](resume.md#7-honest-ai-assisted-writing).

_Last reviewed: 2026-10_
