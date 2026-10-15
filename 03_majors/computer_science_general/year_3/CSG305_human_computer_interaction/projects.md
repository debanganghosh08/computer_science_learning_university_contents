# CSG305 · Labs and projects

Every study with people needs informed consent, a data-handling plan and, for P3, approval from your institution's ethics committee (or the instructor acting under the course's approved protocol). Record only what you need, store it securely, and anonymise before sharing. Moderation, the first coding pass and the experiment design are AI-off; AI may assist elsewhere if every AI step is logged in an audit trail.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Fitts and KLM | Measure your Fitts's-law parameters (mouse and touch); predict a payment flow with KLM and time five people doing it | Fitted a and b with R²; KLM prediction vs measured times with an explanation of the gap | 4 h |
| 2 · Heuristic evaluation (AI off) | Three evaluators independently assess a public-service or university website, then merge | Merged issue list with heuristic, severity and screenshot; overlap analysis between evaluators | 4 h |
| 3 · Interviews (moderation AI off) | Five semi-structured interviews on a real problem | Interview guide, consent forms, anonymised transcripts | 5 h |
| 4 · Coding and reliability | Two human coders and one AI model code the same transcripts with one codebook | Codebook, κ for each pair, three disagreements analysed | 4 h |
| 5 · Prototyping | Paper prototypes of 3 alternatives, then one interactive Figma or code prototype | Photos, prototype link, critique notes and decisions | 5 h |
| 6 · Usability testing | Moderate 3 sessions with an observer; collect success, time, errors, SUS | Test plan, notes, metrics table, observer feedback on your moderation | 5 h |
| 7 · Accessible components | Fix an inaccessible modal, combobox and data table; test with axe, keyboard and NVDA or TalkBack | Before/after code, axe results, screen-reader transcript of each task | 6 h |
| 8 · Power analysis | Simulation-based power analysis for a within-subjects design with random participant effects | Script, chosen N, and the assumptions it depends on | 3 h |
| 9 · Mixed-effects analysis | Analyse the pointing-experiment data from Chapter 8 | Model specification, estimates with CIs, diagnostic plots, a plain-language summary | 4 h |
| 10 · Over-reliance | A small study: participants judge answers with help from an AI that is right 70% of the time; then add a forcing function | Reliance measures (accepting wrong advice, rejecting right advice) in both conditions | 5 h |
| 11 · Synthetic vs real participants | Same 10-item survey answered by 20 real people and 20 LLM-simulated personas | Distribution comparison, where the simulation flattened or stereotyped answers, a recommendation | 3 h |

## Projects

### P1 · Usability and accessibility audit of a real service (L1, ~6 hours)

**Real-world inspiration:** WebAIM's 2026 scan found detectable WCAG failures on 95.9% of the top million home pages, and India's Supreme Court ruled in 2025 that inaccessible digital KYC excluded disabled citizens. Audits like this are a routine paid service.

**What to build:** an audit of a public website or app you use (a university portal, a public-transport app, a government service), combining a heuristic evaluation, an automated scan, keyboard-only use and screen-reader use for three core tasks.

**Acceptance criteria:**
- At least 15 distinct issues, each with evidence (screenshot or transcript), severity (0–4) and the affected user group.
- Every accessibility issue mapped to a WCAG 2.2 success criterion; the report states how many issues the automated scan found versus manual testing.
- Three core tasks attempted with a screen reader, with the exact point of failure for each failed task.
- A prioritised fix list with concrete code or design changes for the top five issues.
- No claims about the organisation's intent or internal processes; findings are about the interface only.

**Stretch goals:** send the report through the organisation's official feedback or accessibility channel and record the response; re-test after any fix.

**What it proves to an employer:** you can find and explain real usability and accessibility problems, a core skill for UX, front-end and QA roles.

### P2 · Research-led redesign with before/after testing (L2, ~15 hours)

**Real-world inspiration:** product teams redesign flows (onboarding, payment, booking) on the basis of research and test the result before shipping.

**What to build:** pick one flow in an app or site you can legally prototype (for example, booking a lab slot or splitting a bill). Run 5 interviews or contextual inquiries, synthesise the findings, prototype a redesign, and compare it with the original in a usability test.

**Acceptance criteria:**
- Research summary with themes traced to quotes and a κ ≥ 0.6 between two coders on the codebook (or an explanation of why agreement was lower and how you resolved it).
- At least 6 usability participants per version, counterbalanced so half see the original first.
- Task success, time on task (median and range), errors and SUS for both versions, with an honest statement of what the sample size allows you to conclude.
- The redesign meets WCAG 2.2 AA for its components, verified with axe and a screen reader.
- A 4-page report with design rationale, evidence and limitations.

**Stretch goals:** a remote unmoderated round with 20 participants; a version for a second language and a low-end Android device.

**What it proves to an employer:** you can go from research to design to evidence, the full loop that UX researchers and product designers run.

### P3 · A pre-registered experiment on an AI interface (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** studies such as METR's 2025 trial and the CHI work on over-reliance and cognitive forcing have changed how AI products are evaluated; AI companies and labs hire researchers who can run them properly.

**What to build:** a controlled experiment on a human–AI task. Example question: *Does requiring users to commit to their own answer before seeing the AI's suggestion (a cognitive forcing function) reduce acceptance of wrong AI advice when reviewing short code snippets or factual answers, and at what cost in time?* You build the study software, recruit participants, run the study and write a short paper.

**Acceptance criteria:**
- A pre-registration (OSF or equivalent) time-stamped before data collection, with hypotheses, primary measures, exclusion rules, sample size and analysis plan.
- A simulation-based power analysis justifying N (expect at least 24 participants for a within-subjects design; more if the analysis requires).
- Ground truth for every trial (the AI's correctness is controlled by you), so reliance can be measured: rate of accepting wrong advice, rate of rejecting correct advice, time per trial.
- Analysis with a mixed-effects model (random intercepts for participant and item), effect sizes with 95% confidence intervals, and every deviation from the pre-registration reported.
- Consent and ethics documentation; anonymised data, materials and analysis code published so all numbers in the paper regenerate with one command.
- A 6–8 page paper in CHI format, with a limitations section that discusses sample, task realism and novelty effects.

**Stretch goals:** a second condition with explanations, testing whether explanations raise acceptance of wrong advice; submission to a CHI late-breaking-work track or a student research competition.

**What it proves to an employer or lab:** you can produce evidence about humans and AI that survives review, which is rare and increasingly in demand.

## Feeds into

- [AIE404 AI Product Engineering and UX](../../../ai_engineering/year_4/AIE404_ai_product_engineering_and_ux/README.md): elective that applies these methods to shipping AI features.
- [DSC304 Experimental Design and Causal Inference](../../../data_science/year_3/DSC304_experimental_design_and_causal_inference/README.md): deeper statistics for online experiments.
- [RES501 Research Methods and Scientific Writing](../../../../05_shared_years_3_to_5/RES501_research_methods_and_scientific_writing/README.md) and [THS501 Thesis or Capstone I](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md): P3 is a ready thesis seed.
- [CSG501 Frontier Seminar](../../year_5/CSG501_frontier_seminar_ai_for_mathematics_science/README.md): how mathematicians and scientists actually use AI tools is an HCI question.
