# CSG305 · Human-Computer Interaction

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 6 | 4 (≈ 120 hours) | L1 → L4 | [CS201](../../../../02_year_2_core_computer_science/semester_3/CS201_algorithms_and_complexity/README.md), [CS212](../../../../02_year_2_core_computer_science/semester_4/CS212_distributed_systems_i/README.md), [CS216](../../../../02_year_2_core_computer_science/semester_4/CS216_programming_languages_compilers_and_interpreters/README.md); draws on [FND116](../../../../01_year_1_foundations/semester_2/FND116_probability_and_statistics_i/README.md) and [FND114](../../../../01_year_1_foundations/semester_2/FND114_web_foundations_http_html_css_and_javascript/README.md) | [AIE404](../../../ai_engineering/year_4/AIE404_ai_product_engineering_and_ux/README.md) (elective); [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md); pairs with [DSC304](../../../data_science/year_3/DSC304_experimental_design_and_causal_inference/README.md) |

Part of the [Computer Science (Theory, Systems and Research) major](../../README.md). This is the course where the subject of study is people. It covers how humans perceive, decide and make errors; how to find out what users need; how to prototype and test; how to build for people with disabilities; how to run controlled experiments that survive peer review; and how to evaluate AI interfaces, where what people *feel* and what actually happens often differ.

## Why this course matters now

AI products have made HCI measurement urgent. In METR's randomised trial, 16 experienced open-source developers took 19% longer on tasks when allowed AI tools, yet expected a 24% speed-up beforehand and believed afterwards that they had been 20% faster ([METR, Jul 2025](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)). A survey of 319 knowledge workers at CHI 2025 found that higher confidence in generative AI was associated with less critical thinking ([Lee et al., Microsoft Research](https://www.microsoft.com/en-us/research/publication/the-impact-of-generative-ai-on-critical-thinking-self-reported-reductions-in-cognitive-effort-and-confidence-effects-from-a-survey-of-knowledge-workers/)). Self-reports, demos and satisfaction scores are not evidence of benefit; a well-designed study is. Accessibility has become law as well as craft: in its February 2026 scan, WebAIM found detectable WCAG failures on 95.9% of the top one million home pages ([WebAIM Million 2026](https://webaim.org/projects/million/)); India's Supreme Court held on 30 April 2025 that digital access is part of the right to life, in a case about eKYC steps that blind users and acid-attack survivors could not complete ([Business Today](https://www.businesstoday.in/personal-finance/news/story/supreme-court-mandates-inclusive-ekyc-for-disabled-says-digital-access-a-right-report-474226-2025-04-30)); and the European Accessibility Act has applied since 28 June 2025 ([European Commission](https://commission.europa.eu/strategy-and-policy/policies/justice-and-fundamental-rights/disability/union-equality-strategy-rights-persons-disabilities-2021-2030/european-accessibility-act_en)). AI can now draft interview guides, transcribe and code interviews, and even simulate participants, but research shows simulated participants can misportray and flatten identity groups ([Wang et al., arXiv 2402.01908](https://arxiv.org/abs/2402.01908)). The human work is choosing the right question, observing real people, designing the study, and judging what the data can support.

## Learning outcomes

By the end you can:

1. **Apply** models of human perception, memory, attention and motor control (Fitts's law, Hick–Hyman law, KLM-GOMS) to predict and explain interface performance.
2. **Diagnose** usability problems with heuristic evaluation, cognitive walkthroughs and error analysis (slips vs mistakes), and **identify** deceptive design patterns.
3. **Plan and run** interviews, contextual inquiry, diary studies and surveys, and **analyse** qualitative data with reliable coding.
4. **Prototype** at the right fidelity (paper, Wizard of Oz, Figma, code) and **run** moderated and unmoderated usability tests with task success, time, errors and SUS.
5. **Audit and build** accessible interfaces to WCAG 2.2 AA using automated tools, keyboard-only and screen-reader testing, and testing with disabled users.
6. **Design, pre-register and analyse** controlled experiments (within/between subjects, counterbalancing, power analysis, mixed-effects models, effect sizes).
7. **Evaluate** AI interfaces for appropriate reliance, trust calibration, explanation quality and real productivity, not only satisfaction.
8. **Use** AI tools in research (transcription, coding assistance, analysis scripts) with documented checks, and **argue** where synthetic participants are and are not acceptable.
9. **Write** a study report to the standard of a CHI late-breaking work or short paper.

## Chapters and lessons

### Chapter 1 · Modelling the human (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Perception and attention | Pre-attentive features, change blindness, visual search, the limits of attention | Design two dashboards for the same alert; time how fast five people spot it |
| 1.2 Memory and cognitive load | Working memory limits, chunking, recognition vs recall, cognitive load theory | Redesign a 6-digit OTP entry flow to reduce load; justify each change |
| 1.3 Motor control | Fitts's law (MT = a + b·log₂(D/W + 1)), steering law, touch target sizes | Lab 1: measure your own Fitts parameters with mouse and touch |
| 1.4 Decision time and predictive models | Hick–Hyman law; KLM-GOMS keystroke-level predictions | Predict the time of a UPI payment flow with KLM; compare with measured times |

**Check your understanding:** (1) Why do bigger buttons at screen edges behave as if they were infinitely deep? (2) When does Hick's law stop predicting menu selection time? (3) What does a KLM model leave out that a real user does?

### Chapter 2 · Design principles and how interfaces fail (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Affordances, signifiers, mappings, feedback | Norman's design principles; conceptual models and mental models | Explain three real interface errors in these terms |
| 2.2 Human error | Slips vs mistakes, mode errors, Swiss-cheese model; designing for recovery (undo, confirmation, constraints) | Analyse a published UI-related incident (for example the January 2018 Hawaii false missile alert) |
| 2.3 Heuristic evaluation | Nielsen's 10 heuristics, severity ratings, evaluator aggregation | Lab 2: three-evaluator heuristic evaluation of a public service website |
| 2.4 Deceptive design | Dark patterns (false urgency, basket sneaking, confirm-shaming, subscription traps); India's CCPA Guidelines for Prevention and Regulation of Dark Patterns (2023) list 13 types | Find and classify five dark patterns in apps you use; propose honest alternatives |
| 2.5 Gestalt and visual hierarchy | Proximity, similarity, alignment, contrast, typography for readability | Restructure a cluttered form using Gestalt principles; measure completion time |

**Check your understanding:** (1) Why is "user error" usually a design finding? (2) Why do heuristic evaluations need several evaluators? (3) Where is the line between persuasion and a dark pattern?

### Chapter 3 · User research: collecting data (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Choosing a method | Attitudinal vs behavioural, qualitative vs quantitative; what each method can answer | Map 10 product questions to the right method |
| 3.2 Interviews | Open questions, avoiding leading questions, the "last time you did X" technique, follow-ups | Lab 3: five interviews on a real problem (for example how students manage deadlines) |
| 3.3 Contextual inquiry and diaries | Master–apprentice model; diary studies for behaviour over time | Run a 5-day diary study with three participants |
| 3.4 Surveys | Question wording, Likert scales, sampling bias, response rates, attention checks | Critique and fix a 15-question survey |
| 3.5 Ethics and consent | Informed consent, vulnerable groups, data minimisation; personal data under India's Digital Personal Data Protection Act, 2023 | Write a consent form and data plan for Lab 3 |

**Check your understanding:** (1) Why do people's predictions of their future behaviour make poor data? (2) What makes a survey sample unrepresentative even when it is large? (3) What must participants know before they agree to a recording?

### Chapter 4 · User research: analysis and synthesis (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Thematic analysis | Coding, codebooks, themes; inductive vs deductive | Code your Lab 3 transcripts with a shared codebook |
| 4.2 Reliability | Inter-rater agreement (Cohen's κ); disagreement as data | Lab 4: two humans and one AI model code the same transcripts; compute κ for each pair |
| 4.3 Synthesis artefacts | Affinity diagrams, journey maps, jobs-to-be-done; criticism of fictional personas | Build a journey map with evidence links to quotes |
| 4.4 From findings to decisions | Insight statements, opportunity areas, prioritisation | Turn findings into three design briefs |

**Check your understanding:** (1) What does a κ of 0.4 between a human and an AI coder tell you? (2) Why should every theme link back to raw quotes? (3) When is a persona harmful?

### Chapter 5 · Prototyping and design iteration (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Fidelity | Sketches, paper prototypes, wireframes, high fidelity; matching fidelity to the question | Paper-prototype three alternative designs in an afternoon |
| 5.2 Wizard of Oz | Simulating intelligence with a hidden human; testing AI features before building them | Wizard-of-Oz a voice assistant for one task with two participants |
| 5.3 Interactive prototypes | Figma prototypes; code prototypes with real data | Lab 5: build an interactive prototype for your P2 |
| 5.4 Design critique | Structured critique, divergence and convergence; AI-generated variants as a starting point, not an answer | Run a critique session; record decisions and reasons |

**Check your understanding:** (1) Why test several rough designs rather than one polished one? (2) What does a Wizard-of-Oz study tell you about a future AI feature, and what can it not tell you? (3) Why can high-fidelity prototypes get less honest feedback?

### Chapter 6 · Usability testing (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Planning | Tasks, success criteria, scenarios, pilot tests | Write a test plan with 6 tasks |
| 6.2 Moderating | Think-aloud (concurrent, retrospective), neutral prompts, when to intervene | Lab 6: moderate three sessions; get feedback from an observer |
| 6.3 Measures | Task success, time on task, errors, SUS, Single Ease Question, NASA-TLX | Score SUS correctly; compare with task success |
| 6.4 How many users? | The "five users" argument and its limits; problem-discovery models; unmoderated remote testing | Estimate how many participants you need to see a problem affecting 10% of users with 80% probability |
| 6.5 Reporting | Severity, frequency, evidence clips, recommended fixes | Write a one-page findings report |

**Check your understanding:** (1) Why can a design have a high SUS score and low task success? (2) When are five participants enough, and when are they badly too few? (3) How does thinking aloud change what people do?

### Chapter 7 · Accessibility (weeks 7–8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Disability and design | Medical vs social models; permanent, temporary and situational impairments; ageing | Interview one person who uses assistive technology (with consent) |
| 7.2 WCAG 2.2 | Perceivable, operable, understandable, robust; levels A/AA/AAA; new 2.2 criteria (focus not obscured, target size, accessible authentication) | Map 10 issues to WCAG success criteria |
| 7.3 Assistive technology | Screen readers (NVDA, VoiceOver, TalkBack), keyboard navigation, switch access, magnification | Complete three tasks on a website using only NVDA or TalkBack |
| 7.4 Building accessibly | Semantic HTML first, ARIA Authoring Practices, focus management, accessible names, contrast, captions | Lab 7: fix an inaccessible component (modal, combobox, data table) and verify with a screen reader |
| 7.5 Testing and law | Automated checks (axe-core) catch only part of the problems; manual and user testing; India's Rights of Persons with Disabilities Act 2016, the IS 17802 ICT standard and draft rules on conformance, GIGW; the EU Accessibility Act | Audit a site with axe, then manually; report what each found |
| 7.6 Cognitive and language accessibility | Plain language, reading level, low literacy, Indian-language interfaces, error messages | Rewrite an error-heavy form for low-literacy users; test with two participants |

**Check your understanding:** (1) Why does a page with zero axe errors still fail blind users? (2) What is wrong with "ARIA everywhere"? (3) Why did selfie-and-blink eKYC fail some users, and what alternative designs would meet the same security goal?

### Chapter 8 · Quantitative experiments (weeks 9–10)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Experimental design | Hypotheses, independent and dependent variables, confounds, within vs between subjects, Latin-square counterbalancing | Design a two-factor experiment on menu design |
| 8.2 Power and sample size | Effect sizes, power analysis, why underpowered studies mislead | Lab 8: power analysis for your P3 with a simulation |
| 8.3 Running studies | Piloting, randomisation, instrumentation (jsPsych, PsychoPy, custom logging), exclusion criteria fixed in advance | Run a Fitts's-law pointing experiment with 12 participants |
| 8.4 Analysis | t-tests and ANOVA vs mixed-effects models (random effects for participant and item); log-transforming times; non-parametric options; confidence intervals over p-values | Lab 9: analyse the pointing data with a mixed-effects model in statsmodels or lme4 |
| 8.5 Open science | Pre-registration (OSF), the replication crisis, reporting deviations, sharing data and analysis | Pre-register your P3 |

**Check your understanding:** (1) Why do repeated measures from the same participant violate the assumptions of a simple t-test? (2) What does "statistically significant" fail to tell a product team? (3) Why must exclusion rules be fixed before you see the data?

### Chapter 9 · Evaluating AI interfaces (weeks 11–12)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Guidelines for human-AI interaction | Microsoft's 18 guidelines (CHI 2019); Google PAIR guidebook; setting expectations, showing uncertainty, efficient correction | Evaluate an AI assistant against the 18 guidelines |
| 9.2 Reliance and trust | Over-reliance and under-reliance; appropriate reliance as the goal; trust calibration | Lab 10: measure over-reliance on an AI that is right 70% of the time |
| 9.3 Explanations and forcing functions | Explanations can increase acceptance of wrong AI advice (Bansal et al., CHI 2021); cognitive forcing functions reduce over-reliance (Buçinca et al., 2021) | Add a forcing function to Lab 10; compare reliance |
| 9.4 Measuring productivity honestly | Self-report vs measured time (METR 2025); learning effects; task selection bias | Design a study that would detect a 10% slowdown |
| 9.5 Conversational and agent interfaces | Error recovery in chat, hallucination disclosure, approval and undo for agents that act, human oversight | Design the confirmation flow for an agent that sends money or emails |

**Check your understanding:** (1) Why can adding explanations make a human–AI team worse? (2) What is the difference between trust and appropriate reliance? (3) Why are users' estimates of their own speed-up unreliable evidence?

### Chapter 10 · Interaction beyond the desktop (week 13)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Mobile-first and low-bandwidth design | Thumb zones, intermittent connectivity, low-end Android devices, data costs | Test a web app on a low-end phone with network throttling |
| 10.2 Multilingual interfaces | Indian scripts, mixed-language (code-mixed) input, transliteration keyboards, voice input | Evaluate a voice or transliteration input with three participants in two languages |
| 10.3 Voice and multimodal | Turn-taking, error handling in speech, discoverability | Wizard-of-Oz a voice flow and log failures |
| 10.4 AR, VR and wearables | Comfort, motion sickness, spatial UI basics | Critique an AR interface against comfort guidelines |

**Check your understanding:** (1) Which design choices change when users pay per megabyte? (2) Why are voice interfaces hard to discover? (3) What does code-mixed input break in a standard search box?

### Chapter 11 · AI in the research process (week 14)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Synthetic participants | LLM-simulated users and their documented failures (flattening of groups, stereotyped answers) | Lab 11: compare 20 simulated survey responses with 20 real ones on the same questions |
| 11.2 AI-assisted analysis | Transcription, first-pass coding, analysis scripts; auditing each step | Write the audit trail for every AI step in P3 |
| 11.3 Writing HCI research | CHI paper structure, contribution types (empirical, artefact, method), limitations | Draft the P3 paper |

**Check your understanding:** (1) For which research questions might synthetic participants be acceptable as a pilot, and for which never? (2) How do you show reviewers that AI-assisted coding did not bias your themes? (3) What makes an HCI contribution new?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Fitts and KLM | Fitted parameters |
| 2 | 2 | Lab 2 · Heuristic evaluation | **P1 starts** |
| 3 | 3 | Lab 3 · Interviews | Consent form approved |
| 4 | 4 | Lab 4 · Coding and reliability | **P1 due** |
| 5 | 5 | Lab 5 · Prototyping | **P2 starts** |
| 6 | 6 | Lab 6 · Usability testing | Test plan |
| 7 | 7 | Lab 7 · Accessible components | Mid-term (AI off) |
| 8 | 7 | Accessibility audit | — |
| 9 | 8 | Lab 8 · Power analysis | **P2 due**; P3 proposal |
| 10 | 8 | Lab 9 · Mixed-effects analysis | P3 pre-registration |
| 11 | 9 | Lab 10 · Over-reliance | P3 data collection |
| 12 | 9 | Forcing functions | P3 data collection |
| 13 | 10 | Multilingual and low-bandwidth testing | P3 analysis |
| 14 | 11 | Lab 11 · Synthetic vs real | **P3 due** |
| 15 | Review | Study-design oral | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** transcribing interviews (with participant consent and a privacy-safe tool); first-pass coding that you then check against human coders; generating variants of a design to critique; drafting survey items that you then review for leading wording; writing analysis scripts (statsmodels, lme4, power simulations) that you test on simulated data with a known effect; checking reading level of interface text.
- **Do without AI (drills):** moderating sessions; writing interview questions; the heuristic evaluation; the first coding pass of at least two transcripts; designing the experiment and choosing the analysis; screen-reader testing; the mid-term and final.
- **Verify AI output by:** computing inter-rater agreement between AI and human coding; tracing every theme to raw quotes; running analysis scripts on simulated data where you know the true effect; checking every accessibility fix with a real screen reader and keyboard, not only with an automated checker; comparing synthetic responses with real ones before trusting them.
- **Where AI still fails here (show it):** Lab 4 (κ between AI and human coders), Lab 7 (AI-suggested ARIA fixes that pass automated checks but break screen-reader announcements) and Lab 11 (synthetic vs real survey responses) each produce your own evidence. Published work shows that LLM-simulated participants can misportray and flatten identity groups (Wang et al.) and that users misjudge AI's effect on their own speed (METR). Record every case where the AI output would have changed a conclusion.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (11) | 25% |
| Projects P1 / P2 / P3 | 5% / 15% / 25% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) + study-design oral | 20% |

**Mastery gate.** You pass when you can, with AI off: (1) given a product question, choose a method, write the study plan, consent text and analysis plan in 90 minutes; (2) find at least 8 of 10 planted usability and accessibility problems in an interface, mapping the accessibility ones to WCAG 2.2 criteria; (3) moderate a usability session that an observer rates as neutral and non-leading; and (4) defend your P3 analysis, including power, exclusions, model choice and limitations, under questioning.

## Industry reality

HCI skills are used by UX researchers, product designers, accessibility specialists, design technologists and product engineers, and by research labs that study human–AI interaction. Companies that build AI assistants now hire researchers to measure reliance, trust and real productivity, not just satisfaction. In India, accessibility obligations for digital services are tightening (the 2025 Supreme Court eKYC judgment, IS 17802, government website guidelines), and consumer law now names dark patterns explicitly (CCPA 2023).

**Interview questions from this course**

1. *Checkout abandonment rose 15% after a redesign. How do you find out why?* Strong answer: start with analytics funnels to localise the drop; session recordings; usability test on the new flow with representative users; check accessibility and slow devices; form hypotheses, then an A/B test or holdout to confirm; avoid asking users to explain why in a survey alone.
2. *How many participants do you need?* Strong answer: depends on the question: 5–8 per round for iterative problem discovery with caveats; power analysis for comparative experiments; much larger samples for A/B tests on conversion; segments multiply the requirement.
3. *Design a study to test whether an AI code-review assistant makes reviewers better.* Strong answer: define "better" (defects found, false approvals, time); within-subjects with counterbalancing or between-subjects; planted defects with known ground truth; measure reliance on wrong suggestions; pre-register; power analysis; do not rely on self-reported speed.
4. *How would you make a complex data table accessible?* Strong answer: semantic `<table>` with headers and scope, captions, keyboard navigation, sorting announcements via live regions, responsive alternatives, contrast; test with NVDA/VoiceOver and with users; avoid div-based grids unless following the ARIA grid pattern fully.
5. *A stakeholder says users love the AI feature because 80% rated it 4 or 5 stars. What do you ask?* Strong answer: who responded (selection bias), what behaviour changed (task success, retention, errors), whether the AI was wrong when they accepted it, novelty effects, comparison with a control group.

## Resources (free first)

- **Courses:** [Stanford CS147](https://web.stanford.edu/class/cs147/); [MIT 6.831 User Interface Design and Implementation (OCW)](https://ocw.mit.edu/courses/6-831-user-interface-design-and-implementation-spring-2011/); NPTEL [User-centric Computing for Human-Computer Interaction](https://onlinecourses.nptel.ac.in/noc25_cs72/preview) (Prof. Samit Bhattacharya, IIT Guwahati).
- **Free books:** Amy J. Ko, [User Interface Software and Technology](https://faculty.washington.edu/ajko/books/user-interface-software-and-technology/) and [Design Methods](https://faculty.washington.edu/ajko/books/design-methods/).
- **Methods:** [Nielsen's 10 heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/); [How many test users](https://www.nngroup.com/articles/how-many-test-users/); [SUS guide (MeasuringU)](https://measuringu.com/sus/); [NASA-TLX](https://www.nasa.gov/human-systems-integration-division/nasa-task-load-index-tlx/); [OSF pre-registration](https://osf.io/prereg/); [jsPsych](https://www.jspsych.org/); [PsychoPy](https://www.psychopy.org/); [statsmodels mixed models](https://www.statsmodels.org/stable/mixed_linear.html).
- **Accessibility:** [WCAG 2.2](https://www.w3.org/TR/WCAG22/); [W3C evaluation resources](https://www.w3.org/WAI/test-evaluate/); [ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/); [axe-core](https://github.com/dequelabs/axe-core); [NVDA screen reader](https://www.nvaccess.org/); [GIGW (India)](https://guidelines.india.gov.in/); [WebAIM Million](https://webaim.org/projects/million/).
- **Human–AI interaction:** [Guidelines for Human-AI Interaction](https://www.microsoft.com/en-us/research/publication/guidelines-for-human-ai-interaction/); [PAIR Guidebook](https://pair.withgoogle.com/guidebook/); [Bansal et al., CHI 2021](https://arxiv.org/abs/2006.14779); [Buçinca et al., CSCW 2021](https://arxiv.org/abs/2102.09692); [Wang et al., LLMs replacing participants](https://arxiv.org/abs/2402.01908); [Deceptive Design](https://www.deceptive.design/).
- **Paid, worth it:** Don Norman, *The Design of Everyday Things* (revised ed.); MacKenzie, *Human-Computer Interaction: An Empirical Research Perspective*.

## Sources

All checked 12 Oct 2026.

- METR, "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity" (10 Jul 2025) — https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
- Lee et al., "The Impact of Generative AI on Critical Thinking" (CHI 2025) — https://www.microsoft.com/en-us/research/publication/the-impact-of-generative-ai-on-critical-thinking-self-reported-reductions-in-cognitive-effort-and-confidence-effects-from-a-survey-of-knowledge-workers/
- WebAIM, "The WebAIM Million" (data collected Feb 2026) — https://webaim.org/projects/million/
- Business Today, "Supreme Court mandates inclusive eKYC for disabled, says digital access a right" (30 Apr 2025) — https://www.businesstoday.in/personal-finance/news/story/supreme-court-mandates-inclusive-ekyc-for-disabled-says-digital-access-a-right-report-474226-2025-04-30
- European Commission, European Accessibility Act — https://commission.europa.eu/strategy-and-policy/policies/justice-and-fundamental-rights/disability/union-equality-strategy-rights-persons-disabilities-2021-2030/european-accessibility-act_en
- IndiaLaw, "Draft RPwD (Amendment) Rules, 2026" (IS 17802 conformance; draft status) — https://www.indialaw.in/blog/regulatory/rpwd-amendment-rules-2026/
- AZB & Partners, "A New Dawn for Dark Patterns" (CCPA Guidelines, notified 30 Nov 2023, 13 patterns) — https://www.azbpartners.com/bank/a-new-dawn-for-dark-patterns/
- Wang, Morgenstern, Dickerson, "Large language models that replace human participants can harmfully misportray and flatten identity groups" — https://arxiv.org/abs/2402.01908
- W3C, WCAG 2.2 — https://www.w3.org/TR/WCAG22/

_Last reviewed: 2026-10_
