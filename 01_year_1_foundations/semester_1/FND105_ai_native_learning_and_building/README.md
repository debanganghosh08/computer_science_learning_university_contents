# FND105 · AI-Native Learning and Building

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 1 · 1 | 4 (≈ 120 hours) | L0 → L2 | none (taken alongside [FND101](../FND101_programming_i_computational_thinking_with_python/README.md)) | no formal dependents; recommended before [CS214](../../../02_year_2_core_computer_science/semester_4/CS214_machine_learning_foundations/README.md), [AIE301](../../../03_majors/ai_engineering/year_3/AIE301_llm_fundamentals_for_engineers/README.md), [AIE302](../../../03_majors/ai_engineering/year_3/AIE302_prompt_and_context_engineering/README.md), [AIE305](../../../03_majors/ai_engineering/year_3/AIE305_evaluating_llm_systems/README.md), [SWE304](../../../03_majors/software_engineering/year_3/SWE304_ai_assisted_software_engineering_agents/README.md) |

## Why this course matters now

AI tools are now the default working environment: 84% of developers in the 2025 Stack Overflow survey use or plan to use them, Google's 2025 DORA report puts adoption among software professionals at 90%, and GitHub reports that nearly 80% of new developers use Copilot in their first week. Trust has not kept up: more developers distrust AI accuracy (46%) than trust it (33%). The evidence on learning is a warning: in Anthropic's January 2026 randomized trial, learners who delegated code to an assistant scored far lower on a follow-up quiz, while those who used it only for conceptual questions kept their learning; in METR's 2025 trial, experienced developers took 19% longer with AI tools yet believed they were 20% faster. This course teaches how large language models work at an intuitive level, how to learn faster with them without losing skills, how to verify and evaluate their output, and how to build small AI-powered tools responsibly.

## Learning outcomes

By the end you can:

1. Explain tokens, embeddings, next-token prediction, sampling temperature, context windows and the training stages (pretraining, instruction tuning, reinforcement learning from feedback) without jargon.
2. Explain why models hallucinate and name concrete mitigations.
3. Write structured prompts and supply context deliberately, and compare prompt variants with a measured evaluation.
4. Verify AI output with tests, primary sources and independent recomputation, and keep an evidence log.
5. Build an evaluation set of 30+ cases and score a tool with exact-match, rubric and LLM-as-judge methods, measuring judge agreement with your own labels.
6. Use AI coding assistants and agents in a reviewable workflow: spec, plan, small diffs, tests, review.
7. Call an LLM API (or a local model with Ollama) from Python with structured output, retries, timeouts, and cost and latency logging.
8. Recognise and mitigate failure modes: hallucination, package hallucination, prompt injection, sycophancy and data leakage.
9. Apply academic integrity, privacy (India's DPDP Act 2023 and Rules 2025), and disclosure rules to your own AI use.
10. Run an AI-off practice routine and show, with data, that your unaided skills held or improved.

## Chapters and lessons

### Chapter 1 · Learning how to learn, with and without AI (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 How skills form | Retrieval practice, spacing, interleaving, and the generation effect: you learn what you produce, not what you read. | Take a 30-minute AI-off baseline test (Python, maths, shell) and save your score. |
| 1.2 Delegation vs inquiry | Anthropic's 2026 trial: AI delegation, progressive reliance and AI-driven debugging scored lowest; conceptual inquiry scored highest. | Classify 10 of your own past AI chats into these patterns. |
| 1.3 AI as tutor, not ghostwriter | Socratic prompts ("ask me questions until I find the bug"); the CS50 Duck model; explain-then-quiz. | Write a tutor system prompt and use it for one FND101 problem; log every hint. |
| 1.4 The AI-off routine | Weekly unaided drills, a skill journal, monthly re-tests; when AI is allowed for learning vs for producing. | Draft your personal AI-use policy for each Year 1 course. |
| 1.5 A personal knowledge system | Markdown notes in Git, spaced-repetition cards (Anki), weekly review. | Set up the notes repo and 30 cards from FND101 and FND103. |

**Check your understanding:** (1) Why can a session in which AI wrote perfect code leave you less able than before? (2) Which of your weekly tasks should be AI-off, and why those? (3) What evidence would show your policy is working?

### Chapter 2 · How LLMs work: an intuition (weeks 2–3)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Tokens | Text is split into sub-word tokens; prices and context limits are counted in tokens; scripts and languages tokenise differently. | Measure token counts for the same sentence in English, Hindi and Bengali in two tokenizer playgrounds; explain the cost difference. |
| 2.2 Embeddings | Words and passages as vectors; similarity as angle; why "king − man + woman" works roughly. | Embed 20 sentences with a small open model and find nearest neighbours. |
| 2.3 Next-token prediction | A model outputs a probability for every next token; sampling, temperature, top-p; why answers vary. | Run one prompt 10 times at temperature 0, 0.7 and 1.2 with Ollama; compare. |
| 2.4 Transformers and attention | Attention lets each token weigh every earlier token; layers; parameters; why GPUs matter (see [FND102](../FND102_how_computers_work_bits_hardware/README.md)). | Step through Transformer Explainer and 3Blue1Brown's chapters on transformers; draw the data flow. |
| 2.5 Training stages | Pretraining on large text corpora, supervised instruction tuning, reinforcement learning from human feedback and from verifiable rewards; reasoning models that spend tokens thinking; knowledge cutoffs. | Write a one-page explanation for a non-technical relative; have a peer check it for errors. |

**Check your understanding:** (1) Why does a model sometimes answer the same question differently? (2) Why does a model know nothing about events after its training cutoff unless you give it context? (3) What does "the model has 70 billion parameters" mean, in one sentence?

### Chapter 3 · Why models are wrong (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Hallucination | Fluent, confident, false output; Kalai et al. (2025): training and benchmarks reward guessing over saying "I don't know". | Ask 20 questions with checkable answers; tag each answer correct, wrong or abstained. |
| 3.2 Fabricated sources | Invented citations, URLs and quotes; why every source must be opened. | Request 10 citations on a topic; check each exists and says what is claimed. |
| 3.3 Package hallucination | Code models recommend packages that do not exist; attackers register those names ("slopsquatting"). | Collect AI-suggested imports for 20 tasks; check each on PyPI. |
| 3.4 Sycophancy and drift | Agreeing with the user's wrong premise; changing a correct answer under pushback; losing track in long contexts. | Push back on 5 correct answers; record how many flip. |
| 3.5 A failure taxonomy | Knowledge, reasoning, instruction-following, context, tool-use and safety failures. | Build a shared class spreadsheet of failures with evidence. |

**Check your understanding:** (1) Why does penalising "I don't know" in a benchmark make hallucination worse? (2) What makes a hallucinated package a security risk rather than an inconvenience? (3) How would you tell sycophancy from genuine correction?

### Chapter 4 · Prompting and context engineering (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Prompt anatomy | Role, task, context, constraints, examples, output format; being explicit beats being clever. | Rewrite 5 vague prompts; compare outputs side by side. |
| 4.2 Examples and structure | Few-shot examples; delimiting data with XML-style tags; asking for JSON. | Build a classifier prompt for bank-SMS categories with 3 examples. |
| 4.3 Reasoning | Asking for step-by-step reasoning vs using reasoning models; when extra thinking helps and when it only adds cost. | Compare accuracy and token cost on 20 maths word problems with and without reasoning. |
| 4.4 Context engineering | Choosing what goes into the context window: documents, retrieved passages, tool results, memory; long-context pitfalls. | Answer questions about a 40-page PDF by pasting it all vs pasting only relevant pages; compare. |
| 4.5 Project memory files | `AGENTS.md` and `CLAUDE.md` for coding agents: commands, conventions, boundaries. | Write one for your FND101 project and test whether an agent follows it. |

**Check your understanding:** (1) Why does putting the data inside clear delimiters reduce mistakes? (2) When is a shorter context more accurate than a longer one? (3) How do you know a prompt change was an improvement and not luck?

### Chapter 5 · Verification habits (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 The verification ladder | Run it (tests) → check primary sources → recompute independently → ask for evidence → second method or model → human expert. | Verify 10 AI claims about Python and Linux; log the rung that settled each. |
| 5.2 Reading sources | Official docs, standards (RFCs), papers, changelogs; lateral reading (leave the page to check who is behind it). | Trace three AI-stated "facts" to their original source. |
| 5.3 Code verification | Tests written before generation, property tests, reading diffs, checking dependencies and licences. | Verify an AI-written function with your own tests; find at least one edge-case bug or show none exists in 1,000 Hypothesis cases. |
| 5.4 Calibrated confidence | Stating how sure you are and why; separating "verified", "plausible" and "unchecked" in your notes. | Mark every claim in one of your own write-ups with its verification status. |

**Check your understanding:** (1) Why is asking the same model "are you sure?" weak verification? (2) Which rung of the ladder is cheapest for code, and which for facts? (3) When is it acceptable to ship something unverified, and how should you label it?

### Chapter 6 · Evals literacy (weeks 7–8)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Why evals | You cannot improve what you do not measure; evals as regression tests for prompts and models. | Write the success criteria for a summariser before building it. |
| 6.2 Building a test set | Representative, edge and adversarial cases; golden answers; keeping a held-out set; labelling guidelines. | Label 30 cases for a bank-SMS categoriser. |
| 6.3 Scoring | Exact match, accuracy, precision and recall in plain terms, rubric scoring, LLM-as-judge and its biases (position, length, self-preference). | Score two prompts; measure how often an LLM judge agrees with your labels. |
| 6.4 Tools | promptfoo and the UK AI Security Institute's Inspect; `pytest`-style evals in CI. | Run your eval in promptfoo or Inspect and in a plain `pytest` file. |
| 6.5 Reading benchmarks | Leaderboards (LMArena), SWE-bench Verified, contamination, why a benchmark score is not your use case. | Explain in one page why a top leaderboard model may be wrong for your task. |

**Check your understanding:** (1) Why must you label examples yourself before trusting an LLM judge? (2) What is overfitting to an eval set, and how does a held-out set help? (3) Why can a model score highly on a benchmark and still fail your users?

### Chapter 7 · AI coding assistants (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 The landscape | Inline completion (GitHub Copilot), chat, terminal agents (Claude Code, OpenAI Codex, Gemini CLI), agentic IDEs (Cursor, Google Antigravity). | Set up one completion tool and one agent; note what data each sends to its provider. |
| 7.2 A reviewable workflow | Spec → plan → small steps → tests → diff review → commit; keeping the agent's scope small. | Implement a feature in 4 commits, each reviewed before the next prompt. |
| 7.3 Reading AI code | Explaining every line, spotting unnecessary complexity, hidden behaviour changes, new dependencies. | Annotate an AI-written 100-line module line by line. |
| 7.4 Measuring yourself | Perception vs measurement (METR 2025); timing, defect counts and understanding as metrics. | Build the same small tool three ways (no AI, chat, agent); log time, defects found by tests, and a self-quiz score. |

**Check your understanding:** (1) Why did developers in METR's study feel faster while measuring slower? (2) What makes a task a good fit for an agent, and what makes it a bad fit? (3) Which check would you never delegate to the agent that wrote the code?

### Chapter 8 · Agents, tools and MCP (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 What an agent is | An LLM in a loop that calls tools and reads results; workflows vs agents (Anthropic's "Building effective agents"). | Draw the loop for a coding agent fixing a failing test. |
| 8.2 Tool calling | Tool schemas, arguments as JSON, validating tool inputs, step limits. | Write a 100-line Python agent with a calculator and a file reader, a 10-step limit and full logging. |
| 8.3 MCP | The Model Context Protocol as an open standard for connecting tools and data (now under the Linux Foundation's Agentic AI Foundation). | Connect a local MCP server to an assistant; list what it can access. |
| 8.4 Prompt injection | Untrusted text (web pages, emails, files) carrying instructions; OWASP's LLM01:2025; defences: least privilege, human approval, separating data from instructions; no single fix. | In a sandbox, show your agent obeying an instruction hidden in a file; then add a defence and re-test. |

**Check your understanding:** (1) Why is an agent with email access and web access more dangerous than either alone? (2) What should require human approval in an agent you build? (3) Why does a step limit matter?

### Chapter 9 · Building small AI-powered tools (weeks 11–12)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 API basics | HTTP requests, API keys in environment variables (never in Git), official SDKs, local models via Ollama. | Call a hosted model and a local model with the same prompt; compare latency. |
| 9.2 Structured output | JSON schemas, validation with Pydantic, retrying on invalid output. | Extract structured fields from 50 synthetic bank SMS messages; report the validation-failure rate. |
| 9.3 Reliability | Timeouts, retries with backoff, rate limits, caching, fallbacks. | Make your tool survive a simulated outage and a malformed response. |
| 9.4 Cost and latency | Tokens × price, input vs output tokens, measuring p50 and p95 latency, choosing a smaller model. | Log cost and latency per request; estimate the monthly cost for 1,000 users. |
| 9.5 Retrieval basics | Chunking, embedding, cosine similarity, top-k retrieval, answering with citations, abstaining when nothing relevant is found. | Build Q&A over your own course notes with file-and-section citations. |

**Check your understanding:** (1) Why validate model output even when you asked for JSON? (2) What is the cheapest way to cut cost for repeated identical requests? (3) Why should a retrieval tool be allowed to say "not found"?

### Chapter 10 · Responsible use: integrity, privacy, security (week 13)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Academic integrity | Course AI policies (CS50 allows its own Duck but not other AI that completes answers); disclosure statements; why AI detectors are unreliable and biased against non-native English writers (Liang et al. 2023). | Write the AI-disclosure section for one of your projects. |
| 10.2 Privacy | What you paste is sent to a provider; retention and training settings; India's DPDP Act 2023 and Rules notified November 2025, with most obligations from May 2027; Samsung's 2023 restriction after internal code was uploaded to a chatbot. | Redact a synthetic customer dataset before sending it to an API; document what you removed and why. |
| 10.3 Intellectual property | Licences of generated code and training data are unsettled; employer and course policies decide; attribution habits. | Compare two companies' published AI-use policies (or your college's) and summarise the rules. |
| 10.4 Language and fairness | Uneven quality across languages; India's Bhashini and AI4Bharat efforts for Indian languages. | Test one task in English and an Indian language you know; document quality differences. |

**Check your understanding:** (1) Why is "I'll just remove the names" often not enough to anonymise data? (2) Why is a detector's "90% AI" score not evidence of misconduct? (3) What must a disclosure statement contain to be useful?

### Chapter 11 · Staying sharp (week 14)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Re-test | Comparing your week-1 and week-14 AI-off scores; what changed and why. | Retake the baseline test under the same conditions. |
| 11.2 A decision table | When to use AI (production, exploration) vs not (first learning, assessments, safety-critical checks). | Publish your Year 1 AI-use policy in your notes repo. |
| 11.3 Staying current without hype | Changelogs, model cards, system cards, papers, and replicating claims before repeating them. | Pick one AI news claim from this month; verify or refute it with primary sources. |
| 11.4 Exam practice | Part A AI-off concepts; Part B AI-allowed timed build with verification. | One full mock exam. |

**Check your understanding:** (1) What would you do if your week-14 score dropped? (2) Which AI claim from this semester turned out wrong, and how did you find out? (3) Which skill do you now refuse to delegate, and why?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Baseline test and learning system | Baseline score; AI-use policy draft |
| 2 | 2 | Tokens and embeddings | Token-count table across languages |
| 3 | 2 | Sampling with Ollama | Temperature experiment |
| 4 | 3 | Hallucination hunt | Failure spreadsheet entries |
| 5 | 4 | Prompt A/B | **P1 due** |
| 6 | 5 | Verification ladder | Evidence log |
| 7 | 6 | Labelling a test set | 30 labelled cases |
| 8 | 6 | promptfoo or Inspect | Eval report with judge agreement |
| 9 | 7 | Three ways to build | Comparison report |
| 10 | 8 | Minimal agent and injection demo | Agent code and logs |
| 11 | 9 | Structured output and reliability | Extraction tool |
| 12 | 9 | Retrieval with citations | **P2 due** |
| 13 | 10 | Redaction and disclosure | Policy and redaction log |
| 14 | 11 | Re-test | **P3 due**; score comparison |
| 15 | Review and exam | Mock exam | Final exam (Part A AI-off, Part B AI-allowed) |

## Working with AI in this course

- **Use AI for:** almost every lab, deliberately and with a log: the prompt, the output, what you verified and how. Tools: Claude, ChatGPT and Gemini (chat); Claude Code, OpenAI Codex, Gemini CLI, GitHub Copilot and Cursor (coding); Ollama (local models).
- **Do without AI (drills):** a 30-minute weekly AI-off drill drawn from FND101 and FND103; explaining LLM concepts on paper; labelling your own eval data (the labels are your ground truth); Part A of the exam.
- **Verify AI output by:** tests written before generation; opening every cited source; recomputing numbers; evals with held-out data; comparing an LLM judge with your own labels before trusting it.
- **Where AI still fails here:** you will document these yourself rather than take them on trust: fabricated citations, non-existent packages, answers that flip under pushback, prompt injection succeeding in your sandbox, token costs that differ across languages, and the gap between how fast you feel and how fast you measure.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs and AI-use log | 25% |
| AI-off drills and the week-1 vs week-14 comparison | 10% |
| Projects: P1 5%, P2 12%, P3 18% | 35% |
| Final exam: Part A AI-off (concepts, 15%), Part B AI-allowed timed build with verification (15%) | 30% |

**Gate:** you pass when you can (1) explain on a whiteboard, AI-off, how an LLM turns a prompt into an answer and why it can be confidently wrong; (2) build a small LLM-powered command-line tool with structured output, error handling and cost logging; (3) present an eval of at least 30 cases that reports your tool's accuracy and shows at least one failure mode with evidence; and (4) show a 14-week AI-off drill log in which your final unaided score is at least your week-1 baseline.

## Industry reality

Employers now assume AI-tool fluency and test what sits on top of it: judgment, verification and fundamentals. Roles such as AI engineer and forward-deployed engineer are built around evaluating and integrating models, and India is investing through the IndiaAI Mission, the Bhashini language platform and companies such as Sarvam AI building Indian-language models.

**Interview questions from this course**

1. *"How would you know your LLM feature got worse after a prompt change?"* A labelled eval set with held-out cases, metrics agreed in advance, judge calibration against human labels, running evals in CI before release.
2. *"Why do LLMs hallucinate, and how do you reduce it in a product?"* Next-token prediction, incentives to guess, missing context; retrieval with citations, abstention, output validation, evals that penalise confident errors.
3. *"What is prompt injection, and how would you protect an agent that reads email?"* Untrusted content acting as instructions; least privilege, human approval for actions, separating data from instructions, monitoring; no complete defence today.
4. *"You used an AI assistant on this code. How did you verify it?"* Tests written first, edge cases, reading the full diff, dependency and licence checks, what was changed by hand and why.
5. *"Estimate the monthly cost of an LLM feature for 10,000 users making 20 requests a day."* Tokens per request (input and output), price per million tokens, 6 million requests a month, caching and model choice, latency trade-offs; shows the arithmetic.

## Resources (free first)

- **How LLMs work:** Andrej Karpathy, [Intro to Large Language Models](https://www.youtube.com/watch?v=zjkBMFhNj_g) and [Deep Dive into LLMs like ChatGPT](https://www.youtube.com/watch?v=7xTGNNLPyMI); 3Blue1Brown, [neural networks series](https://www.3blue1brown.com/topics/neural-networks) and [Transformers](https://www.youtube.com/watch?v=wjZofJX0v4M); [Transformer Explainer](https://poloclub.github.io/transformer-explainer/); [LLM visualisation](https://bbycroft.net/llm); [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/); [Hugging Face LLM course](https://huggingface.co/learn/llm-course); [tokenizer playground](https://huggingface.co/spaces/Xenova/the-tokenizer-playground) and [Tiktokenizer](https://tiktokenizer.vercel.app/).
- **Prompting, context and agents:** [Anthropic prompt engineering guide](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview); [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents); [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents); [Claude Academy](https://academy.claude.com/); [Anthropic courses on GitHub](https://github.com/anthropics/courses); [OpenAI Cookbook](https://cookbook.openai.com/); [Gemini API docs](https://ai.google.dev/gemini-api/docs); [MCP](https://modelcontextprotocol.io/); [AGENTS.md](https://agents.md/); [MIT Missing Semester: Agentic Coding](https://missing.csail.mit.edu/2026/agentic-coding/).
- **Evals:** [promptfoo](https://www.promptfoo.dev/docs/intro/); [Inspect](https://inspect.aisi.org.uk/); Hamel Husain, [Your AI product needs evals](https://hamel.dev/blog/posts/evals/); Eugene Yan, [Patterns for building LLM-based systems](https://eugeneyan.com/writing/llm-patterns/); [SWE-bench](https://www.swebench.com/).
- **Security and failure modes:** [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/llm-top-10/); Simon Willison's [prompt injection series](https://simonwillison.net/series/prompt-injection/); Kalai et al., [Why Language Models Hallucinate](https://arxiv.org/abs/2509.04664).
- **Tools:** [Ollama](https://ollama.com/); [Claude Code](https://code.claude.com/docs/en/overview); [OpenAI Codex CLI](https://github.com/openai/codex); [Gemini CLI](https://github.com/google-gemini/gemini-cli); [GitHub Copilot docs](https://docs.github.com/en/copilot); [Cursor docs](https://cursor.com/docs); [Pydantic](https://docs.pydantic.dev/latest/); [Sentence Transformers](https://www.sbert.net/); [Anki](https://apps.ankiweb.net/).
- **Learning science:** [Learning How to Learn](https://www.coursera.org/learn/learning-how-to-learn) (Coursera; free to audit).

## Sources

- 84% use or plan to use AI; 46% distrust vs 33% trust: [Stack Overflow 2025 Survey, AI](https://survey.stackoverflow.co/2025/ai) (checked Oct 2026).
- 90% AI adoption among software professionals: [Google, 2025 DORA report announcement](https://blog.google/technology/developers/dora-report-2025/) (checked Oct 2026).
- Nearly 80% of new developers use Copilot in week one: [GitHub Octoverse 2025](https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/) (checked Oct 2026).
- Skill-formation trial (52 engineers; AI group 50% vs 67% quiz; interaction patterns): [Anthropic, 29 Jan 2026](https://www.anthropic.com/research/AI-assistance-coding-skills); [arXiv:2601.20245](https://arxiv.org/abs/2601.20245) (checked Oct 2026).
- 19% longer with AI, believed 20% faster (16 developers, 246 tasks); METR marks these early-2025 results as out of date after February 2026 data: [METR](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) (checked Oct 2026).
- Hallucination and evaluation incentives: [Kalai, Nachum, Vempala, Zhang, Sep 2025](https://arxiv.org/abs/2509.04664) (checked Oct 2026).
- Package hallucinations: [Spracklen et al., USENIX Security 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/spracklen) (checked Oct 2026).
- Detector bias against non-native writers: [Liang et al., 2023](https://arxiv.org/abs/2304.02819) (checked Oct 2026).
- CS50 AI policy: [CS50 academic honesty](https://cs50.harvard.edu/x/honesty/) (checked Oct 2026).
- DPDP Rules notified 13 Nov 2025; main obligations from May 2027: [AZB & Partners note, Nov 2025](https://www.azbpartners.com/bank/indias-digital-personal-data-protection-act-phased-rollout-and-key-compliance-milestones/) (checked Oct 2026).
- Samsung restricts generative AI after internal data upload (May 2023): [TechCrunch](https://techcrunch.com/2023/05/02/samsung-bans-use-of-generative-ai-tools-like-chatgpt-after-april-internal-data-leak/) (checked Oct 2026).
- MCP and AGENTS.md under the Agentic AI Foundation (9 Dec 2025): [Linux Foundation](https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation) (checked Oct 2026).
- OWASP LLM01:2025 Prompt Injection: [OWASP GenAI](https://genai.owasp.org/llm-top-10/) (checked Oct 2026).
- India's AI programmes: [IndiaAI](https://indiaai.gov.in/), [Bhashini](https://bhashini.gov.in/), [AI4Bharat](https://ai4bharat.iitm.ac.in/), [Sarvam AI](https://www.sarvam.ai/) (checked Oct 2026).

_Last reviewed: 2026-10_
