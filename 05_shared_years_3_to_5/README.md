# Shared courses, Years 3–5

Every major in this university (software, backend, cloud, security, data, ML, AI engineering, embedded and the rest) takes the same nine courses in Years 3–5. They do not teach a technology. They teach the parts of the job that no single major owns: how to act within the law and your own ethics, how to get hired and keep getting better, how to work inside a real team for a real client, how to produce and check new knowledge, how to finish a large piece of work alone, and how to launch a career or a company.

| Code | Course | Year · Semester | Prerequisite | What you walk out with |
|---|---|---|---|---|
| [PRO301](PRO301_professional_practice_ethics_law_and_responsible/README.md) | Professional Practice: Ethics, Law and Responsible AI | 3 · 5 | CS213 | A compliance and ethics dossier for a real product: data map, DPDP/GDPR duties with dates, licence audit, fairness and accessibility audit |
| [CAR301](CAR301_career_lab_i_dsa_mastery_portfolio_and_open/README.md) | Career Lab I: DSA Mastery, Portfolio and Open Source | 3 · 6 | CS201 | The 16-week DSA track completed under timed conditions, a merged open-source contribution, a three-project portfolio, two published technical posts |
| [IND401](IND401_industry_co_op_studio/README.md) | Industry Co-op Studio | 4 · 7 | CS205 | A 14-week placement with a real client or open-source organisation: shipped changes, an on-call shift, a postmortem, a client sign-off |
| [CAR401](CAR401_career_lab_ii_interviews_system_design_and_ai/README.md) | Career Lab II: Interviews, System Design and AI-Driven Assessments | 4 · 8 | CAR301 | Full interview loops passed under mock conditions, a running application pipeline with conversion data, a negotiation plan |
| [RES501](RES501_research_methods_and_scientific_writing/README.md) | Research Methods and Scientific Writing | 5 · 9 | none | A research proposal and a short paper with sound statistics that survives a mock peer review |
| [RES502](RES502_reading_reproducing_and_extending_papers/README.md) | Reading, Reproducing and Extending Papers | 5 · 9 | RES501 | A reproducibility report on a published paper, with a packaged artifact and one extension experiment |
| [THS501](THS501_thesis_or_capstone_i/README.md) | Thesis or Capstone I | 5 · 9 | RES501 | An approved proposal, a working pilot or walking skeleton, an evaluation harness |
| [THS502](THS502_thesis_or_capstone_ii/README.md) | Thesis or Capstone II | 5 · 10 | THS501 | A defended thesis or capstone, a public release (paper preprint, workshop submission or open-source release) |
| [LCH502](LCH502_career_launch_and_founder_studio/README.md) | Career Launch and Founder Studio | 5 · 10 | CAR401 | A signed offer and a first-90-days plan, or a launched product with paying users and a company-formation decision |

## Why every major shares these

1. **The junior squeeze is real, and tacit knowledge is the answer.** US payroll data show employment of software developers aged 22–25 close to 20% below its late-2022 peak by September 2025, while older developers kept growing. The study's authors argue that AI substitutes most for codified "book" knowledge and least for judgement built by doing real work (see the [market map](../06_career_and_market_readiness/01_market_map/README.md)). The shared spine is built to give you that judgement early: real contributions in CAR301, a real client in IND401, real production work on call, and real research in Year 5.
2. **Law and ethics now land on engineers, not just lawyers.** India's DPDP Rules were notified in November 2025 with most duties applying from May 2027; the EU AI Act's obligations are phasing in through 2028; CERT-In expects incidents reported within 6 hours. The person who designs the logging pipeline or the consent screen decides whether the company is compliant. PRO301 teaches you to make those calls.
3. **Hiring is a skill that can be trained.** Interview formats have changed (AI-proctored assessments, AI interviewers, AI-allowed coding rounds), but the underlying tests have not: can you solve a problem, design a system, explain trade-offs and be trusted with production. Two career labs a year apart give you a full year of deliberate practice.
4. **Everyone needs research skills now.** Every AI-era engineer reads papers, judges benchmark claims, designs experiments (A/B tests are experiments) and checks whether a result is real or noise. Research methods and paper reproduction are taught to every major, not only to future PhD students.
5. **Finishing something large, alone, is the final proof.** The two-semester thesis or capstone is the single artefact that shows an employer, an admissions committee or an investor what you can do without a syllabus.

## How the courses sit in each semester

Each semester is six 4-credit courses (about 120 hours each). The shared course is one slot; your major fills the rest.

| Year · Semester | Your major's courses | Shared course(s) | Other slots |
|---|---|---|---|
| 3 · 5 | Three major core courses | PRO301 | 1 elective |
| 3 · 6 | Two major core courses | CAR301 | 1–2 electives |
| 4 · 7 | Two advanced courses | IND401 | Overlap course A |
| 4 · 8 | Two advanced courses | CAR401 | Overlap course B |
| 5 · 9 | The major's frontier seminar | RES501, RES502, THS501 | — |
| 5 · 10 | — | THS502, LCH502 | Electives |

**A note on Semester 9.** RES501 is listed as the prerequisite of RES502 and THS501, yet all three run in the same semester. In practice RES501 is front-loaded: its weeks 1–5 (research questions, literature search, experimental design) produce the material for the THS501 proposal, which is due in week 6, and RES502 starts its reproduction work in week 4 once the paper is chosen. If you can, take RES501 one semester early as an elective; it makes Semester 9 much lighter.

## The two Year 5 routes

Year 5 has a research route and an industry route. Both take RES501 and RES502, because reading and checking papers is now an industry skill.

| | Research route | Industry route |
|---|---|---|
| THS501–THS502 | Research thesis: a question, a method, results, a paper | Capstone: a production-grade system for real users, or a startup MVP |
| Publication | arXiv preprint, workshop or conference submission, reproducibility track | Open-source release, technical report, launch write-up |
| LCH502 track | Job launch (research engineer, applied scientist) or PhD/MS applications | Job launch, or founder track |
| Who it suits | People aiming for research labs, ML research engineering, graduate school | People aiming for senior engineering roles or their own company |

You choose the route in THS501 week 1 and can switch at the week 6 proposal defence, not after.

## How each major plugs in

The process in every shared course is common; the content comes from your major.

- **PRO301.** Every major brings its own legal hot spots: authorization and the IT Act for SEC and OFF; the DPDP Act for DEN, DSC and DAN; the EU AI Act and model licences for AIE, MLE and DLR; accessibility for FE and MOB; product safety and device data for EMB; client contracts and NDAs for FDE. The privacy overlap ([OV07](../04_overlaps/OV07_privacy_engineering/)) builds directly on PRO301.
- **CAR301.** The DSA track ([02_dsa_for_hiring](../06_career_and_market_readiness/02_dsa_for_hiring/)) is identical for everyone. The open-source project you choose should sit in your field (for example Kubernetes or OpenTofu for OPS and CLD, OWASP projects for SEC, DuckDB or Apache Arrow for DEN, scikit-learn or Hugging Face libraries for MLE and DSC, Zephyr for EMB). Portfolio projects come from your major's L3 projects.
- **IND401.** The placement is in your field; the studio process (sprints, review, on-call, demo days) is common.
- **CAR401.** Each role has its own interview loop in [04_ai_driven_interviews](../06_career_and_market_readiness/04_ai_driven_interviews/) and its own role page in the [market map](../06_career_and_market_readiness/01_market_map/README.md). System design preparation uses [03_system_design](../06_career_and_market_readiness/03_system_design/).
- **RES501 and RES502.** The papers you read and reproduce come from your major's frontier seminar (for example MLE501 on reproducing ML papers pairs naturally with RES502).
- **THS501 and THS502.** Your major's flagship project in [05_industry_projects](../06_career_and_market_readiness/05_industry_projects/) is an acceptable starting point for a capstone only if the capstone goes clearly beyond it (new users, new scale, or a new question).
- **LCH502.** The job track uses your role page; the founder track is open to every major. FDE501 (the field-to-founder seminar) feeds it directly.

## How these courses use the career-readiness section

The folder [`06_career_and_market_readiness/`](../06_career_and_market_readiness/) holds the reference material: the market map, the 16-week DSA track, the system design track, the AI-driven interview question banks and the flagship industry projects. The courses here are the structured semesters that make you work through that material on a schedule, with deliverables, mocks and a gate. Do not read 06 instead of these courses; use these courses to get through 06.

## External calendars to plan around

| Programme | When | Used in |
|---|---|---|
| Google Summer of Code | Contributor applications ran 16–31 March in 2026; coding from late May | CAR301 (proposal), IND401 (can count as the placement) |
| Outreachy | Two cohorts a year: May–August and December–March; the December 2026 cohort's initial applications closed on 31 August 2026 | CAR301, IND401 |
| LFX Mentorship | Several terms a year; check the portal for current terms | CAR301, IND401 |
| Hacktoberfest | October each year | CAR301 (first contributions; quality over count) |
| ML Reproducibility Challenge | 2026 edition: TMLR papers submitted 20 June 2025 – 30 September 2026, presented at NeurIPS 2026 in Sydney, 6–13 December | RES502, THS502 |

Dates were checked in October 2026; every programme publishes a new timeline each year.

## For self-learners

Every course page has a self-learner path. The common substitutes are: an open-source maintainer instead of a co-op employer, a reading group instead of a seminar, a volunteer mentor (a maintainer, an author of a paper you reproduced, or a working engineer two or three levels above you) instead of an advisor, and peers met through open-source communities or FOSS United meetups for mock interviews. Treat the mastery gates as non-negotiable; they are what make self-study count.

## Sources

- Brynjolfsson, Chandar and Chen, "Canaries in the Coal Mine?" (Nov 2025), cited in the market map — https://digitaleconomy.stanford.edu/app/uploads/2025/12/CanariesintheCoalMine_Nov25.pdf (checked 2026-10)
- Google Summer of Code timeline and FAQ — https://developers.google.com/open-source/gsoc/timeline, https://developers.google.com/open-source/gsoc/faq (checked 2026-10)
- Outreachy December 2026 cohort and eligibility rules — https://www.outreachy.org/outreachy-dec-2026-internship-cohort/, https://www.outreachy.org/apply/eligibility/ (checked 2026-10)
- LFX Mentorship — https://mentorship.lfx.linuxfoundation.org/ (checked 2026-10)
- NeurIPS blog, "MLRC 2026: Reproducibility as an Official Track at NeurIPS" (4 May 2026) — https://blog.neurips.cc/2026/05/04/mlrc-2026-reproducibility-as-an-official-track-at-neurips/ (checked 2026-10)
- Shardul Amarchand Mangaldas, "Enforcement of the DPDP Act and notification of the DPDP Rules" — https://www.amsshardul.com/insight/enforcement-of-the-dpdp-act-and-notification-of-the-dpdp-rules/ (checked 2026-10)
- European Commission, AI Act page (application timeline as amended by the AI Omnibus) — https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai (checked 2026-10)

_Last reviewed: 2026-10_
