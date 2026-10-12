# FND105 · Labs and projects

Every lab and project keeps an `AI_LOG.md`: the tool and model, the prompt, what you used, what you rejected, and how you verified it. API keys live in environment variables or a git-ignored `.env` file; a gitleaks check in CI fails the build if a key is committed. Only synthetic or public data is sent to hosted models. If you cannot pay for an API, every lab works with a local model through Ollama.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Baseline and learning system | Measure your unaided skill; set up notes and spaced repetition | Week-1 AI-off test score; notes repo; 30 Anki cards; first AI-use policy | 3 h |
| 2 · Tokens and embeddings | See text the way a model does | Token counts for 10 sentences in English, Hindi and one more language in two tokenizers; nearest-neighbour results for 20 embedded sentences | 3 h |
| 3 · Sampling | Understand variability | Outputs of one prompt × 10 runs × 3 temperatures on a local model, with a written explanation | 3 h |
| 4 · Hallucination hunt | Find and classify failures with evidence | 20 checkable questions and 10 citation requests, each tagged correct, wrong, fabricated or abstained; 5 entries in the class failure sheet | 4 h |
| 5 · Prompt A/B | Change prompts with evidence | Two prompt versions scored on a 20-case set; the winner and the margin; one case where the "worse" prompt won | 3 h |
| 6 · Verification ladder | Settle claims at the cheapest reliable rung | Evidence log for 10 claims (rung used, source, verdict) | 3 h |
| 7 · Build an eval | Labelling, metrics and an LLM judge | 30+ labelled cases; scores from two methods; judge-vs-your-labels agreement rate and the cases where they disagree | 5 h |
| 8 · Three ways to build | Measure your own productivity and learning | One small tool built without AI, with chat and with an agent: time, test-detected defects, and a 10-question self-quiz score for each | 5 h |
| 9 · Minimal agent and injection | Understand the agent loop and its main risk | A tool-calling agent under 150 lines with step limit and logs; a sandbox demo of an injected instruction succeeding, then failing after your defence | 4 h |
| 10 · Privacy and disclosure | Handle data and credit honestly | Redaction script and log for a synthetic customer dataset; your published AI-disclosure template | 3 h |

## Projects

### P1 · `dost`: a study buddy that won't do your homework (L1, ~6 hours)

**Real-world inspiration.** Harvard's CS50 Duck (cs50.ai) is an AI tutor designed to guide students without handing over answers, and CS50's policy allows it while disallowing other AI that completes answers. Universities and ed-tech companies in India and elsewhere face the same design problem.

**What to build.** A command-line tutor (hosted API or local model) with a system prompt and simple rules that: asks Socratic questions, gives graded hints, quizzes you from your own Markdown notes, refuses to output full solutions to marked assignment problems, and saves each session to a log.

**Acceptance criteria**
- An eval of 20 adversarial "just give me the code" prompts (including role-play and "my teacher allowed it" tricks): the tutor withholds a full solution in ≥ 90% of them, judged by you with a written rubric.
- An eval of 20 conceptual questions: ≥ 80% answered correctly by the same rubric.
- Quiz mode generates questions only from your notes and cites the note file for each.
- README documents both evals, every failure case, and what you changed after seeing them.

**Stretch goals.** Spaced-repetition scheduling of quiz questions; Hindi or Bengali mode with its own small eval; compare a local model and a hosted model on both evals.

**What it proves to an employer.** You can shape model behaviour with prompts and guardrails and prove the result with an evaluation instead of a demo.

### P2 · `pramaan`: cited answers over a document set (L2, ~15 hours)

**Real-world inspiration.** Support assistants, internal knowledge bots and government-scheme helplines all need answers grounded in specific documents, with citations and the ability to say "not found". India's Bhashini and AI4Bharat efforts aim to make such access work across Indian languages.

**What to build.** A retrieval-augmented Q&A tool over a public document set you choose (for example, the Python tutorial, this university's syllabi, or a public government policy PDF): chunk, embed, retrieve the top passages, answer with file-and-section citations, and abstain when nothing relevant is retrieved.

**Acceptance criteria**
- An eval of 40 questions you wrote and answered yourself, including 10 whose answers are not in the documents.
- Answer correctness ≥ 80% on answerable questions (rubric scored by you).
- Citation accuracy ≥ 85%: the cited passage actually supports the answer, checked by you for every case.
- Abstains on ≥ 80% of unanswerable questions.
- Logs latency per query (reports p50 and p95) and cost per 100 queries (or tokens per query for a local model).
- Structured output validated with Pydantic; network errors and invalid responses retried with backoff and never crash the tool.
- No secrets in the repository; CI runs tests and a reduced eval (10 cases) on every pull request.

**Stretch goals.** Compare two chunk sizes and two embedding models on the same eval; answer in an Indian language with sources in English; add a re-ranking step and measure its effect.

**What it proves to an employer.** You can build the most common pattern in applied AI end to end, and report its accuracy honestly, including where it fails.

### P3 · Agent-built, human-owned (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** Teams now ship features where an AI agent writes much of the code while engineers own the specification, tests, evaluation and review: the workflow described in MIT's 2026 Missing Semester lecture on agentic coding and in vendor guidance such as Anthropic's "Building effective agents".

**What to build.** A genuinely useful small AI tool, chosen from: an expense categoriser for synthetic bank-SMS exports; a pull-request description writer that reads `git diff`; or a meeting-notes action-item extractor. An AI coding agent may write most of the code. You own:
- a written spec and a decision log (at least 5 dated decisions with alternatives considered);
- a test suite you write before generation (≥ 30 tests);
- an eval suite of ≥ 50 labelled cases, with LLM-judge agreement measured against your labels on 20 of them;
- CI that runs tests and the eval on every pull request and fails if accuracy drops more than 3 percentage points below the last release;
- a cost and latency report (CSV plus one chart);
- a threat-model note covering prompt injection, data privacy (what leaves the machine; DPDP considerations for real deployments) and failure behaviour;
- an `AGENTS.md` and an AI-disclosure section in the README.

**Acceptance criteria**
- All of the above present and passing in CI on `main`.
- At least three agent-proposed changes rejected or reworked, each documented in the PR conversation with the reason.
- The eval report includes a confusion table or per-category scores and three analysed failure cases.
- A 10-minute AI-off defence: you explain any file the examiner chooses and change one behaviour live, with tests passing.

**Stretch goals.** A/B two models (one local, one hosted) on accuracy, cost and latency; add a human-feedback loop that turns corrected outputs into new eval cases; publish a short write-up of what the agent did well and badly, with evidence.

**What it proves to an employer.** You can direct AI agents productively while keeping full ownership of quality, security and cost: the profile hiring managers look for as AI writes more of the code.

## Feeds into

- [CS214 Machine Learning Foundations](../../../02_year_2_core_computer_science/semester_4/CS214_machine_learning_foundations/README.md): the mathematics behind embeddings, training and evaluation.
- [AIE301 LLM Fundamentals](../../../03_majors/ai_engineering/year_3/AIE301_llm_fundamentals_for_engineers/README.md), [AIE302 Prompt and Context Engineering](../../../03_majors/ai_engineering/year_3/AIE302_prompt_and_context_engineering/README.md), [AIE303 Retrieval-Augmented Generation](../../../03_majors/ai_engineering/year_3/AIE303_retrieval_augmented_generation_and_search/README.md) (P2 grows into it) and [AIE305 Evaluating LLM Systems](../../../03_majors/ai_engineering/year_3/AIE305_evaluating_llm_systems/README.md).
- [SWE304 AI-Assisted Software Engineering](../../../03_majors/software_engineering/year_3/SWE304_ai_assisted_software_engineering_agents/README.md): P3's workflow at team scale.
- [PRO301 Professional Practice: Ethics, Law and Responsible AI](../../../05_shared_years_3_to_5/PRO301_professional_practice_ethics_law_and_responsible/README.md) and the [AI Security and Safety overlap](../../../04_overlaps/OV05_ai_security_safety/README.md).
