# AIE302 · Prompt and Context Engineering

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 5 | 4 (≈ 120 hours) | L1 → L3 | [CS214](../../../../02_year_2_core_computer_science/semester_4/CS214_machine_learning_foundations/README.md), [CS205](../../../../02_year_2_core_computer_science/semester_3/CS205_software_engineering_i_design_testing/README.md); taken alongside [AIE301](../AIE301_llm_fundamentals_for_engineers/README.md) | [AIE402](../../year_4/AIE402_fine_tuning_and_small_models_for_products/README.md), [AIE303](../AIE303_retrieval_augmented_generation_and_search/README.md), [AIE304](../AIE304_tool_use_and_ai_agents_loops_harnesses_memory/README.md), [AIE305](../AIE305_evaluating_llm_systems/README.md) |

## Why this course matters now

At runtime every LLM feature is a block of text that code assembles: instructions, examples, retrieved documents, tool results and conversation history. Anthropic's engineering team calls the work of curating that block **context engineering**, and treats context as a finite budget with diminishing returns (Sept 2025). Small choices have large effects. Changing only the formatting of a few-shot prompt moved LLaMA-2-13B's accuracy by up to 76 points (Sclar et al., 2023). Model upgrades also break prompts: from Claude 4.6 onward, a prefilled assistant turn returns a 400 error, although many production prompts relied on prefill to force JSON (Anthropic docs, checked 2026-10). AI already drafts prompts (Anthropic's metaprompt notebook, OpenAI's prompt optimizer) and searches prompt space automatically (DSPy's MIPROv2 and GEPA). The human work is deciding what the model must see and in what order, building the eval that separates a better prompt from a lucky one, and designing the context so that untrusted text cannot steer the system.

## Learning outcomes

By the end you can:

1. **Explain** how a chat request becomes one token sequence (chat template, roles, special tokens, instruction hierarchy), and **predict** what the model actually sees.
2. **Write** system prompts, few-shot sets and output contracts that pass a written spec on at least 95% of a 100-case test set.
3. **Choose** between zero-shot, few-shot, chain-of-thought and a reasoning model with an effort setting, and **justify** the choice with measured accuracy, latency and cost.
4. **Enforce** structured output with schema-constrained decoding or validated retries, and **measure** whether the format constraint hurts task quality.
5. **Design** a context-assembly policy (ordering, budgets, truncation, summarisation) for a multi-turn assistant, and **measure** its effect on quality as the conversation grows.
6. **Decide** between retrieval, long context and a router between them, using cost and accuracy numbers.
7. **Threat-model** an LLM feature for direct and indirect prompt injection and **apply** architectural defences (least privilege, separation of trusted and untrusted text, confirmation steps). This is defence only.
8. **Run** prompts as versioned code: templates in git, pinned model snapshots, a regression eval in CI and a migration checklist for model upgrades.
9. **Use** an automatic prompt optimiser and **detect** when it overfits the dev set.

## Chapters and lessons

### Chapter 1 · What the model actually sees (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 One sequence, many roles | Chat templates (Jinja in Hugging Face tokenizers), system/user/assistant/tool roles, special tokens, why "the prompt" includes hidden scaffolding | Render the same conversation through the chat templates of two open-weight models and diff the token streams |
| 1.2 Instruction hierarchy | System > developer > user > tool output; how models are trained to rank privileged instructions (Wallace et al., 2024) | Write 10 conflicting system/user pairs; record which instruction wins on two providers |
| 1.3 Variance is a property of prompts | Sampling noise, temperature, prompt-format sensitivity (Sclar et al., 2023) | Run one classification prompt 20 times × 5 formats; plot the accuracy spread |
| 1.4 The prompt as a program | Inputs, outputs, preconditions, failure modes; a prompt spec template (task, audience, inputs, output contract, refusals, examples) | Write a one-page spec for a support-ticket triage prompt before writing the prompt |

**Check your understanding:** Two prompts differ only in whitespace and separators, yet accuracy differs by 10 points. What does that say about any single-format evaluation you read? Why can text placed in a tool result never be trusted as an instruction? What will you lose if you evaluate with temperature 0 only?

### Chapter 2 · Instructions that survive production (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Clear and direct | Audience, goal, constraints, success criteria; positive instructions ("do X") over prohibitions; explaining why a rule exists | Rewrite three vague prompts; measure pass rate before and after on 30 cases |
| 2.2 Structure with delimiters | XML tags or Markdown sections for instructions, data and examples; naming tags consistently; quoting user content | Refactor a 900-token prompt into tagged sections; compare errors |
| 2.3 Long inputs | Put long documents first and the query last (Anthropic reports up to 30% better responses in its tests); ask for quotes before answers | Reproduce the ordering effect on a 40-page policy PDF with 25 questions |
| 2.4 Over-prompting and model drift | Emphatic rules written for older models cause over-triggering on newer ones; effort settings replace "think harder" text | Remove every "ALWAYS/NEVER" from a prompt; measure what changes |
| 2.5 Code-mixed and Indic users | Hinglish and other code-mixed input, transliteration, answering in the user's script, token cost by language (Petrov et al. found up to 15× length differences across languages) | Build a 50-case Hinglish/Hindi/English test set; compare token counts and accuracy |

**Check your understanding:** Why does explaining the reason for a rule often work better than repeating the rule? A prompt worked on last year's model and now over-uses a tool: what do you change first? Why can a feature be 2–5× more expensive for Hindi users than for English users, and what can you do about it?

### Chapter 3 · Examples and in-context learning (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 What examples teach | Format, label space and input distribution matter more than label correctness in some settings (Min et al., 2022) | Swap gold labels for random labels; measure the drop on your task |
| 3.2 Biases of few-shot | Majority-label, recency and common-token bias; calibration (Zhao et al., 2021) | Reorder 8 examples 10 ways; report the accuracy range |
| 3.3 Choosing examples | Diversity, edge cases, 3–5 well-chosen examples (Anthropic guidance); retrieving the k nearest examples per input | Implement kNN example selection with embeddings; compare with a fixed set |
| 3.4 Many-shot | Hundreds of examples in long context (Agarwal et al., 2024); cost with and without prompt caching | Plot accuracy against 0/4/16/64/256 shots and the cost of each point |

**Check your understanding:** When does adding examples make results worse? How would you detect that the model is copying surface features of your examples? Why does prompt caching change the economics of many-shot prompting?

### Chapter 4 · Reasoning: chain-of-thought, sampling and reasoning models (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Chain-of-thought | Few-shot CoT (Wei et al., 2022), zero-shot "think step by step" (Kojima et al., 2022), where it helps (multi-step maths, logic) and where it does not | Compare direct vs CoT on 100 GSM8K-style items: accuracy, tokens, latency |
| 4.2 Self-consistency and verification | Sample k reasoning paths and vote (Wang et al., 2022); verifier prompts; why self-correction without new information often fails (Huang et al., 2023) | Plot accuracy against k = 1, 3, 5, 9 with the cost curve |
| 4.3 Reasoning models | Models that think before answering; effort and thinking settings; adaptive thinking; why step-by-step micromanagement can hurt them | Same task on a reasoning model at three effort levels; pick the cheapest that meets the target |
| 4.4 Faithfulness | Visible reasoning is not guaranteed to reflect the computation; monitorability is useful but fragile (Korbak et al., 2025) | Find three cases where the stated reasoning and the final answer disagree |

**Check your understanding:** Self-consistency triples cost: when is that worth it? Why might a detailed "first do A, then B" prompt make a reasoning model worse? What would convince you that a model's explanation is not the real reason for its answer?

### Chapter 5 · Structured output contracts (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Why parsing breaks | Free text vs JSON mode vs strict schemas; LinkedIn reported ~90% correctly formatted outputs before a defensive parser cut errors to ~0.01% (2024) | Measure the parse-failure rate of a naive JSON prompt on 500 calls |
| 5.2 Constrained decoding | Grammar- and schema-constrained generation (Outlines, XGrammar); provider structured outputs (OpenAI, Anthropic); limits of supported JSON Schema | Implement the same extractor with provider structured outputs and with Pydantic + retry |
| 5.3 Format can cost quality | Strict format constraints reduce reasoning accuracy (Tam et al., 2024); reason first, then format; two-step extraction | Compare "answer in JSON" with "reason, then emit JSON" on 100 reasoning items |
| 5.4 Designing schemas | Enums for labels, nullable fields, explicit "unknown", evidence/quote fields, refusal fields, versioned schemas | Design a schema for invoice extraction (GSTIN, HSN codes, totals) and validate against 50 real invoice layouts |

**Check your understanding:** Constrained decoding guarantees valid JSON: what two things can it not guarantee? Why add an "unknown" value instead of letting the model guess? When is a tool call a better output contract than a JSON answer?

### Chapter 6 · Context assembly and the token budget (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Context is a budget | Attention spreads thin as context grows; "context rot" and the shift from prompt to context engineering (Anthropic, Sept 2025) | Measure accuracy on one question as irrelevant context grows from 1k to 100k tokens |
| 6.2 Position effects | U-shaped recall: models use the start and end of long inputs best (Liu et al., 2023) | Reproduce the lost-in-the-middle curve on 20 documents |
| 6.3 Distractors | Irrelevant context lowers accuracy (Shi et al., 2023); filtering and ranking before inclusion | Add 0/2/5 distractor passages; measure degradation and recovery with a filter |
| 6.4 Assembly code | Templates (Jinja), slots with token budgets, priority order, truncation rules, deterministic rendering, snapshot tests of the rendered prompt | Build a context assembler with per-slot budgets and golden-file tests |
| 6.5 Conversation state | What to keep from history: last N turns, pinned facts, tool results, user profile; when to start a fresh window | Simulate 60-turn chats and compare three history policies on 30 probe questions |

**Check your understanding:** Your assistant degrades after turn 25: which three causes in the context are likely, and what experiment separates them? Why should the rendered prompt be snapshot-tested like any other build artefact? What belongs in the system prompt and what belongs in a per-request slot?

### Chapter 7 · Retrieval, long context, or both (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 The trade-off | When well resourced, long context beat RAG on average, but RAG was far cheaper; Self-Route sends each query to one or the other (Li et al., 2024) | Answer 100 questions over a 300-page corpus three ways: RAG, full context, router |
| 7.2 Caching changes the maths | Prompt caching discounts for repeated prefixes; designing stable prefixes; cache-hit monitoring | Restructure a prompt so 80% of tokens sit in a cacheable prefix; measure hit rate and cost |
| 7.3 Just-in-time context | Agents that fetch by reference (file paths, IDs, grep, search tools) instead of pre-loading everything | Give a model a "search docs" tool instead of the docs; compare tokens and accuracy |
| 7.4 Citations and grounding | Quote-then-answer, citation spans, "answer only from the sources" with an abstain path | Add citations to the P2 assistant and verify each citation automatically |

**Check your understanding:** Your corpus is 400k tokens and changes weekly. Which design would you choose, and what would change your mind? Why does a cache hit-rate dashboard belong next to a cost dashboard? What does an abstain path cost you, and what does it save?

### Chapter 8 · Compaction, summarisation and memory (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Compaction | Summarising history when nearing the window limit; server-side compaction and context editing (clearing old tool results) in current APIs | Implement compaction at 70% of the window; measure facts lost |
| 8.2 Structured notes | Agent-written notes files and to-do lists that persist across windows; what to write down (decisions, open questions, IDs) | Add a notes file to a long task; compare completion with and without |
| 8.3 Prompt compression | Token-level compression (LLMLingua) vs abstractive summaries; where compression hurts (numbers, names, code) | Compress 20 prompts at 2×, 5×; measure task accuracy |
| 8.4 Probing what was lost | Probe questions about early-conversation details; regression tests for memory | Build a 40-probe "memory test" and run it after each compaction policy |

**Check your understanding:** Which kinds of facts do summaries drop first, and how would you protect them? When is clearing old tool results safer than summarising them? How would you know that a compaction change caused a user-visible regression?

### Chapter 9 · Prompt injection: threat model and defences (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 The threat | Direct vs indirect prompt injection via web pages, emails, documents and tool output (Greshake et al., 2023); OWASP LLM01:2025; why no prompt-only fix is complete | Draw the data-flow diagram of an email assistant; mark every untrusted input |
| 9.2 Dangerous combinations | Private data + untrusted content + an exfiltration channel; removing one leg of that triangle | Classify five product designs by which legs they have |
| 9.3 Prompt-level mitigations | Delimiting, spotlighting/datamarking (Hines et al., 2024), instruction hierarchy, refusing instructions found in data; their measured limits | Implement spotlighting; evaluate on the AgentDojo benchmark in its sandbox |
| 9.4 Architectural defences | Least-privilege tools, a planner that never reads untrusted text, human confirmation for side effects, output allow-lists (Beurer-Kellner et al., 2025; CaMeL, 2025) | Redesign the email assistant so that no untrusted text can trigger a send |

**Check your understanding:** Why is "tell the model to ignore instructions in documents" not a security boundary? Which single permission change removes most of the risk from your design? How would you test a defence without writing an attack against a real system?

### Chapter 10 · Prompts as versioned code (weeks 10–11)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Prompt repositories | Templates in git, typed variables, code review for prompts, prompt registries (e.g. Langfuse prompt management) | Move the P2 prompts into a typed template module with reviewers |
| 10.2 Pinning and migration | Model snapshot IDs vs aliases; deprecations (removed prefill, removed thinking budgets); a migration checklist | Migrate a prompt suite between two model versions; document every diff |
| 10.3 Release engineering | Feature flags, shadow runs, staged rollout, rollback, changelogs linking prompt version → eval result | Ship a prompt change behind a flag with a shadow comparison |
| 10.4 Cost and latency budgets | Token budgets per request, output-length control, caching-aware layout | Add a CI check that fails when rendered prompt tokens grow by >10% |

**Check your understanding:** Why should production code reference a model snapshot rather than an alias? A teammate edits a prompt in a web console at 2 a.m.: what process would have caught the regression? What is the minimum evidence to attach to a prompt pull request?

### Chapter 11 · Prompt evaluation and automatic optimisation (weeks 12–13)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Eval sets for prompts | Spec-derived cases, real-traffic samples, adversarial and edge cases; train/dev/test splits for prompts | Build a 150-case set from the P2 spec and logs, with a hidden test split |
| 11.2 Assertions and graders | Exact match, regex, schema checks, code checks, LLM-judge rubrics (full treatment in [AIE305](../AIE305_evaluating_llm_systems/README.md)) | Write promptfoo assertions for 10 properties of one prompt |
| 11.3 Comparing prompts honestly | Paired comparison on the same cases, bootstrap confidence intervals, multiple samples per case | Decide between two prompts with a 95% bootstrap CI on the paired difference |
| 11.4 Automatic optimisation | DSPy signatures and modules; MIPROv2 (Opsahl-Ong et al., 2024) and GEPA (Agrawal et al., 2025) optimisers; overfitting to dev sets | Optimise a pipeline with DSPy; report dev vs held-out test gains |
| 11.5 Regression in CI | Running the eval on every prompt or model change, thresholds, flaky-test handling for stochastic outputs | Wire the suite into GitHub Actions with a pass threshold and a cost cap |

**Check your understanding:** An optimiser raised dev accuracy by 9 points and test accuracy by 1. What happened and what do you change? Why sample each case several times when comparing prompts? Which metric would you refuse to let an LLM judge alone?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Template and variance explorer | Prompt spec for triage task |
| 2 | 2 | Lab 1 (cont.): Instruction rewrite clinic | — |
| 3 | 3 | Lab 2 · Few-shot sensitivity | **P1 due** |
| 4 | 4 | Lab 3 · Reasoning cost curves | — |
| 5 | 5 | Lab 4 · Structured extraction | Schema design review |
| 6 | 6 | Lab 5 · Context assembler | Mid-term (AI off): read a rendered prompt, predict failures |
| 7 | 7 | Lab 6 · RAG vs long context vs router | — |
| 8 | 8 | Lab 7 · Compaction and memory probes | — |
| 9 | 9 | Lab 8 · Injection threat model (defensive) | Threat model write-up |
| 10 | 10 | Lab 9 · Prompt repo and migration | **P2 due** |
| 11 | 10 | Lab 9 (cont.) | Migration report |
| 12 | 11 | Lab 10 · Eval suite and CI | — |
| 13 | 11 | Lab 10 (cont.): DSPy optimisation | Optimiser overfitting report |
| 14 | Integration | P3 demo day | **P3 due** |
| 15 | Review | Oral defence of P3 | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** generating first-draft prompts from your spec (Anthropic's metaprompt notebook, OpenAI's prompt optimizer); generating synthetic and adversarial test inputs, which you then label yourself; critiquing a prompt against your spec; writing the eval harness with Claude Code, Cursor or GitHub Copilot; running DSPy optimisers.
- **Do without AI (drills):** write a system prompt from a written spec in 30 minutes; read a rendered context and predict which instruction will be ignored and why; hand-label 50 outputs before any LLM judge touches them; count a context budget by hand (slots, tokens, cost) for a given request; draw an injection data-flow diagram.
- **Verify AI output by:** running every AI-written prompt against the held-out test split, with at least 3 samples per case; comparing with the baseline on the same cases (paired), not with last week's numbers; reading 20 raw outputs, not only the score; checking that a "better" prompt did not grow tokens or latency beyond budget.
- **Where AI still fails here (show it):** AI-generated prompts tend to be long and emphatic; measure their token cost and over-triggering against a short version. Automatic optimisers overfit small dev sets; show the dev–test gap in Lab 10. Model-written test cases cluster around easy inputs; compare their difficulty distribution with real logs. And no model can reliably detect every injected instruction in data, which is why Chapter 9 relies on architecture rather than prompts.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10, each with a measured result) | 25% |
| Projects P1–P3 | 35% |
| Written reviews (spec, schema, threat model, migration) | 10% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) + oral defence of P3 | 20% |

**Mastery gate.** You pass when you can: (1) given a new task spec and 40 labelled examples, ship a versioned prompt with a 100-case eval within 4 hours and show a statistically supported improvement over a naive baseline (paired bootstrap CI excluding zero); (2) given a 60-turn conversation and a token budget, write an assembly and compaction policy and show that 90% of probe facts survive; (3) given an LLM feature design, name every untrusted input path and the architectural control for each, without writing an attack.

## Industry reality

Prompt and context engineering is daily work for anyone shipping LLM features. GitHub described how Copilot assembles context from neighbouring editor tabs and ranks snippets to fit a limited window (GitHub blog, 2023). LinkedIn's generative AI team reported reaching 80% of its target experience in one month and spending four more months chasing the last 20%, including a defensive parser that cut format errors from about 10% to about 0.01% (LinkedIn Engineering, Apr 2024). Vendors now publish model-specific prompting guides that change with each model generation (Anthropic, OpenAI and Google docs, checked 2026-10), so migration work is ongoing. India-specific context: multilingual, code-mixed users and up to 15× token-length differences across languages (Petrov et al., 2023) make token budgeting a product decision, not a detail.

**Interview questions from this course**

1. *Our extraction prompt fails on 8% of invoices. Walk me through fixing it.* Strong answer: collects and buckets the failures first; separates format failures (fix with structured outputs, schema design, validated retry) from content failures (examples, instructions, "unknown" values); builds a regression set from the failures; reports before/after on a held-out split.
2. *How do you decide what goes into the context window?* Strong answer: treats context as a budget; orders by importance and position effects; uses retrieval or just-in-time tools for large corpora; summarises or clears stale history; tests with probe questions; mentions caching-aware layout.
3. *RAG or a 1M-token context?* Strong answer: cites cost, latency and accuracy trade-offs; mentions caching, corpus change rate, citation needs and position effects; proposes measuring both on a real question set, possibly with a router.
4. *Is prompt injection solved if the system prompt says "ignore instructions in documents"?* Strong answer: no; explains indirect injection and why models cannot reliably separate data from instructions; proposes least privilege, separation of planning from untrusted data, confirmations and egress controls; mentions OWASP LLM01.
5. *A new model version is released. How do you upgrade safely?* Strong answer: pinned snapshots; run the regression suite with multiple samples; read model-specific migration notes (e.g. removed prefill, effort settings); shadow traffic; staged rollout with rollback; compare cost and latency, not just quality.

## Resources (free first)

- **Vendor guides:** Anthropic prompting best practices — https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices ; Anthropic interactive tutorial — https://github.com/anthropics/prompt-eng-interactive-tutorial ; OpenAI prompt engineering — https://developers.openai.com/api/docs/guides/prompt-engineering ; Google Gemini prompting strategies — https://ai.google.dev/gemini-api/docs/prompting-strategies ; Google prompt engineering whitepaper (Kaggle) — https://www.kaggle.com/whitepaper-prompt-engineering
- **Context engineering:** Anthropic, "Effective context engineering for AI agents" — https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents ; Anthropic compaction — https://platform.claude.com/docs/en/build-with-claude/compaction ; context editing — https://platform.claude.com/docs/en/build-with-claude/context-editing
- **Structured output:** OpenAI Structured Outputs — https://developers.openai.com/api/docs/guides/structured-outputs ; Anthropic structured outputs — https://platform.claude.com/docs/en/build-with-claude/structured-outputs ; Outlines — https://github.com/dottxt-ai/outlines ; Instructor — https://github.com/567-labs/instructor
- **Surveys and reading:** The Prompt Report (arXiv 2406.06608) — https://arxiv.org/abs/2406.06608 ; Lilian Weng, "Prompt Engineering" — https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/ ; Prompt Engineering Guide — https://www.promptingguide.ai/ ; "What We've Learned From A Year of Building with LLMs" — https://applied-llms.org/
- **Tools:** DSPy — https://dspy.ai/ ; promptfoo — https://www.promptfoo.dev/docs/intro/ ; Langfuse prompt management — https://langfuse.com/docs/prompt-management/overview ; Tiktokenizer — https://tiktokenizer.vercel.app/ ; LLMLingua — https://github.com/microsoft/LLMLingua
- **Security (defensive):** OWASP LLM01:2025 — https://genai.owasp.org/llmrisk/llm01-prompt-injection/ ; Simon Willison's prompt-injection series — https://simonwillison.net/series/prompt-injection/ ; AgentDojo (arXiv 2406.13352) — https://arxiv.org/abs/2406.13352
- **Paid, optional:** Chip Huyen, *AI Engineering* (O'Reilly, 2025), chapter 5 covers prompt engineering; its free companion repo is https://github.com/chiphuyen/aie-book

## Sources

- Anthropic, "Effective context engineering for AI agents" (Sept 2025) — https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents (checked 2026-10)
- Anthropic prompting best practices: long-context ordering "up to 30 percent", 3–5 examples, prefill returns 400 from Claude 4.6, `budget_tokens` removed from Claude 4.7 — https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices (checked 2026-10)
- Sclar et al., "Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design" (2023) — https://arxiv.org/abs/2310.11324 (checked 2026-10)
- Wallace et al., "The Instruction Hierarchy" (2024) — https://arxiv.org/abs/2404.13208 ; Petrov et al., "Language Model Tokenizers Introduce Unfairness Between Languages" (2023) — https://arxiv.org/abs/2305.15425 (checked 2026-10)
- Min et al. (2022) — https://arxiv.org/abs/2202.12837 ; Zhao et al., "Calibrate Before Use" (2021) — https://arxiv.org/abs/2102.09690 ; Agarwal et al., "Many-Shot In-Context Learning" (2024) — https://arxiv.org/abs/2404.11018 (checked 2026-10)
- Wei et al. (2022) — https://arxiv.org/abs/2201.11903 ; Kojima et al. (2022) — https://arxiv.org/abs/2205.11916 ; Wang et al. (2022) — https://arxiv.org/abs/2203.11171 ; Huang et al. (2023) — https://arxiv.org/abs/2310.01798 ; Korbak et al. (2025) — https://arxiv.org/abs/2507.11473 (checked 2026-10)
- Tam et al., "Let Me Speak Freely?" (2024) — https://arxiv.org/abs/2408.02442 ; Willard and Louf, Outlines (2023) — https://arxiv.org/abs/2307.09702 ; Dong et al., XGrammar (2024) — https://arxiv.org/abs/2411.15100 (checked 2026-10)
- Liu et al., "Lost in the Middle" (2023) — https://arxiv.org/abs/2307.03172 ; Shi et al. (2023) — https://arxiv.org/abs/2302.00093 ; Li et al., Self-Route (2024) — https://arxiv.org/abs/2407.16833 ; Jiang et al., LLMLingua (2023) — https://arxiv.org/abs/2310.05736 (checked 2026-10)
- Greshake et al. (2023) — https://arxiv.org/abs/2302.12173 ; Hines et al., Spotlighting (2024) — https://arxiv.org/abs/2403.14720 ; Beurer-Kellner et al. (2025) — https://arxiv.org/abs/2506.08837 ; Debenedetti et al., CaMeL (2025) — https://arxiv.org/abs/2503.18813 (checked 2026-10)
- Khattab et al., DSPy (2023) — https://arxiv.org/abs/2310.03714 ; Opsahl-Ong et al., MIPROv2 (2024) — https://arxiv.org/abs/2406.11695 ; Agrawal et al., GEPA (2025) — https://arxiv.org/abs/2507.19457 (checked 2026-10)
- LinkedIn Engineering, "Musings on building a Generative AI product" (25 Apr 2024) — https://www.linkedin.com/blog/engineering/generative-ai/musings-on-building-a-generative-ai-product (checked 2026-10)
- GitHub, "How GitHub Copilot is getting better at understanding your code" (2023) — https://github.blog/ai-and-ml/github-copilot/how-github-copilot-is-getting-better-at-understanding-your-code/ (checked 2026-10)
- OpenAI prompt optimizer — https://developers.openai.com/api/docs/guides/prompt-optimizer ; Anthropic metaprompt notebook — https://colab.research.google.com/github/anthropics/claude-cookbooks/blob/main/misc/metaprompt.ipynb (checked 2026-10)

_Last reviewed: 2026-10_
