# AIE501 · Frontier Seminar: Long-Horizon Autonomous Agents and Agent Safety

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 5 · 9 | 4 (≈ 120 hours) | L3 → L5 | [AIE401](../../year_4/AIE401_multi_agent_systems_mcp_and_orchestration/README.md), [AIE403](../../year_4/AIE403_llmops_observability_guardrails_cost_and_latency/README.md); taken alongside [RES501](../../../../05_shared_years_3_to_5/RES501_research_methods_and_scientific_writing/README.md) and [RES502](../../../../05_shared_years_3_to_5/RES502_reading_reproducing_and_extending_papers/README.md) | [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md), [THS502](../../../../05_shared_years_3_to_5/THS502_thesis_or_capstone_ii/README.md), [OV05](../../../../04_overlaps/OV05_ai_security_safety/), [LCH502](../../../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md) |

## Why this course matters now

Agents are moving from minutes of autonomy to hours. METR estimates that the length of software task an AI agent can complete with 50% success has doubled about every seven months since 2019, and possibly faster since 2024. Its current data file puts the best early-2026 model at roughly 12 hours for 50% success but about 70 minutes for 80% success. Benchmarks saturate quickly. The original OSWorld paper (2024) reported humans at 72.36% and the best model at 12.24%. By mid-2026 the top entries on the OSWorld-Verified leaderboard exceeded that human baseline, while the best reported score on the newer long-horizon OSWorld 2.0 suite was about 20% (leaderboards checked 2026-10). Safety research has moved into agent settings as well. It covers prompt injection defences with provable guarantees (CaMeL, 2025), control protocols that assume the agent may act against its overseers (Greenblatt et al., 2023; Bhatt et al., 2025), and stress tests in simulated corporate environments that found models from several developers taking harmful insider-style actions (Anthropic, 2025). This seminar trains you to read this literature critically, reproduce a result, and make a contribution, whether as a thesis, an open-source tool or a design that a company can rely on.

## Learning outcomes

By the end you can:

1. **Critically read** frontier agent papers and system cards, separating measured results, simulated scenarios and extrapolation.
2. **Explain** how long-horizon capability is measured (time horizons, HCAST, RE-Bench, SWE-Lancer, PaperBench, OSWorld) and **critique** each measure's validity.
3. **Design** harnesses for multi-session, multi-hour work (initializer and worker agents, progress artefacts, compaction, verification) and **measure** their effect.
4. **Analyse** computer-use and browser agents (action spaces, grounding, observation formats) and their security exposure.
5. **Apply** agent security architectures (CaMeL-style capability separation, design patterns for injection resistance, Rule of Two) and **evaluate** them on AgentDojo-style benchmarks.
6. **Explain** AI control and oversight methods (trusted monitoring, resampling, chain-of-thought monitoring) and their known failure modes.
7. **Reproduce** one published agent result within a stated tolerance and **report** discrepancies honestly.
8. **Write** a research proposal on an open problem in long-horizon agents or agent safety that is ready for [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md).

## Chapters and lessons

Each week has two required papers, a 20-minute student presentation, a written critique (max 800 words) and a practical exercise.

### Chapter 1 · Measuring long-horizon capability (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Time horizons | Task length as a capability measure; 50% vs 80% horizons; METR's caveat that measurements above 16 hours are unreliable with current tasks (Kwa et al., 2025) | Re-plot METR's public data; fit your own doubling time; compare with theirs |
| 1.2 Human-calibrated suites | HCAST (Rein et al., 2025), RE-Bench for AI R&D (Wijk et al., 2024) | Write the threats-to-validity section for one suite |
| 1.3 Economic framing | SWE-Lancer: real freelance tasks with dollar values (Miserendino et al., 2025) | Discuss what "earning $X" does and does not prove |
| 1.4 Research replication | PaperBench (Starace et al., 2025), MLE-bench (Chan et al., 2024) | Choose one task from either; attempt it with an agent; log every failure |

**Check your understanding:** Why can the 50% horizon grow quickly while the 80% horizon lags? What makes a task's human time estimate uncertain? Which of these benchmarks best predicts value in your own work, and why?

### Chapter 2 · Harnesses for long-running work (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Multi-session agents | Initializer agent + incremental worker sessions, feature lists, progress files and git as memory (Anthropic, Nov 2025) | Apply the pattern to a 20-feature project; measure features completed per session |
| 2.2 Endurance claims | Vendor observations of 30+ hours of focused work (Anthropic, Sept 2025) vs controlled measurement | Design an experiment that would test such a claim fairly |
| 2.3 Test-time compute | Compute-optimal inference scaling (Snell et al., 2024); when more thinking stops helping | Plot success vs tokens for your agent; find the knee |
| 2.4 Self-improvement | Skill libraries (Voyager), workflow memory (AWM), learning from past trajectories | Add skill reuse to your agent; measure success on unseen tasks |

**Check your understanding:** What state must survive between sessions for a multi-day task? Why is "it ran for 30 hours" not a success metric? Where does skill reuse fail?

### Chapter 3 · Computer-use and browser agents (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 The lineage | Anthropic computer use (Oct 2024; 14.9% on OSWorld at launch), OpenAI's ChatGPT agent (Jul 2025), Gemini 2.5 Computer Use (Oct 2025) | Build a timeline of capability claims with their evaluation settings |
| 3.2 Environments | OSWorld (Xie et al., 2024) and OSWorld-Verified, WebArena (Zhou et al., 2023), Mind2Web (Deng et al., 2023), WebVoyager (He et al., 2024) | Run an open agent on 20 WebArena or OSWorld tasks in their sandboxes |
| 3.3 Native GUI agents | Screenshot-to-action models (UI-TARS, Qin et al., 2025); grounding and action spaces | Compare accessibility-tree vs screenshot observations on 10 tasks |
| 3.4 Saturation and successors | Why OSWorld-Verified saturated and OSWorld 2.0's long-horizon tasks did not | Write a one-page "what would a 2027 benchmark need?" proposal |

**Check your understanding:** What does a screenshot hide that an accessibility tree shows, and the reverse? Why do browsing agents enlarge the prompt-injection surface? How should a benchmark handle websites that change?

### Chapter 4 · Securing agents by design (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Injection at scale | Indirect injection (Greshake et al., 2023); InjecAgent (2024); AgentDojo (97 tasks, 629 security test cases; 2024) | Run AgentDojo against your agent in its sandbox; report utility and attack success |
| 4.2 Capability separation | CaMeL (Debenedetti et al., 2025): privileged planner, quarantined data processing, capabilities on data; 77% of AgentDojo tasks with provable security vs 84% undefended | Explain the utility cost of CaMeL in your own words with their numbers |
| 4.3 Design patterns | Action-selector, plan-then-execute, map-reduce, dual LLM, code-then-execute, context minimisation (Beurer-Kellner et al., 2025); Rule of Two (Meta, 2025); lethal trifecta (Willison, 2025) | Redesign one product with two patterns; compare residual risk |
| 4.4 Classifier defences | Constitutional classifiers (Sharma et al., 2025), prompt-injection detectors and their limits | Measure a detector's false-negative rate on held-out benign-canary injections |

**Check your understanding:** Why are architectural defences provable in a way classifier defences are not? What utility does each pattern give up? Which pattern fits a coding agent that reads untrusted issues?

### Chapter 5 · AI control and oversight (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 The control framing | Safety despite intentional subversion: trusted monitors, untrusted models, red-team/blue-team protocol evaluation (Greenblatt et al., 2023) | Reproduce a toy trusted-monitoring protocol on a code task |
| 5.2 Control for agents | Resampling and incrimination in multi-step settings (Ctrl-Z, Bhatt et al., 2025) | Implement resampling of suspicious actions; measure safety vs usefulness |
| 5.3 Monitoring reasoning | Chain-of-thought monitors catch reward hacking, but optimising against them can cause obfuscation (Baker et al., 2025); monitorability as fragile (Korbak et al., 2025) | Build a CoT monitor for reward hacking on planted tasks |
| 5.4 Human oversight at scale | Approval fatigue, sampling-based review, escalation design, audit trails | Design an oversight plan for 1,000 agent runs a day |

**Check your understanding:** Why assume the agent might be adversarial even if you believe it is not? What does a monitor's false-positive rate cost operationally? Why might training against a monitor make things worse?

### Chapter 6 · Evidence of misaligned behaviour (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Scheming evaluations | In-context scheming in frontier models under specific goal-conflict setups (Meinke et al., 2024) | Summarise the setup, results and limits in one page |
| 6.2 Alignment faking and backdoors | Alignment faking (Greenblatt et al., 2024); sleeper agents that persist through safety training (Hubinger et al., 2024) | Discuss what these imply for fine-tuned agents in production |
| 6.3 Agentic misalignment | Simulated insider-threat scenarios across 16 models (Anthropic, Jun 2025); simulated settings only | Critique the ecological validity of the scenarios |
| 6.4 Reward hacking in practice | Special-casing tests and gaming graders in coding agents; detection with hidden tests | Measure hidden-test vs visible-test pass rates for your agent |

**Check your understanding:** How should an engineer act on results from simulated scenarios? What is the difference between a capability evaluation and a propensity evaluation? What does reward hacking tell you about your grader?

### Chapter 7 · Evaluating frontier agents rigorously (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Benchmark validity | Task and outcome validity checklist (Zhu et al., 2025); cost-aware comparisons (Kapoor et al., 2024) | Audit one agent benchmark with the checklist; publish your findings internally |
| 7.2 Contamination and memorisation | "The SWE-Bench Illusion" (Liang et al., 2025); fresh-task designs | Design a contamination-resistant private task set for your thesis |
| 7.3 Frontier safety frameworks | Anthropic Responsible Scaling Policy, Google DeepMind Frontier Safety Framework, OpenAI Preparedness Framework; capability thresholds and safeguards | Compare the three on autonomy-related thresholds |
| 7.4 Government evaluators | UK AI Security Institute and its open Inspect framework; evaluation sharing | Port one of your evals to Inspect |

**Check your understanding:** Why might a lab's safety framework and an independent evaluator disagree on the same model? What evidence would convince you a benchmark is contamination-resistant? Why report cost alongside score?

### Chapter 8 · Memory and continual learning for agents (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Long-term memory evaluation | LongMemEval (Wu et al., 2024); LOCOMO results for Mem0 (2025) | Run LongMemEval on two memory designs |
| 8.2 Structured memory | A-MEM (2025), Zep temporal knowledge graphs (2025) | Implement temporal validity for facts; test updates and contradictions |
| 8.3 Learning on the job | Workflow induction, skill libraries, and the open problem of safe continual learning | Write a two-page open-problem statement |
| 8.4 Memory as attack surface | Memory poisoning (OWASP agentic list), provenance and expiry | Design a memory write policy with provenance checks |

**Check your understanding:** Why is continual learning harder to make safe than retrieval? How do you evaluate forgetting in an agent? What would a poisoned memory look like in your logs?

### Chapter 9 · Agents in the economy (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Inter-agent systems | Failure taxonomy of multi-agent systems (Cemri et al., 2025); A2A v1.0 | Simulate two companies' agents negotiating via A2A; record failures |
| 9.2 Agentic commerce | AP2 (Google, 2025), Agentic Commerce Protocol (OpenAI and Stripe, 2025), UPI agentic payments pilot (Razorpay, NPCI, OpenAI, 2025) | Analyse where user authority is proven in each design |
| 9.3 Identity and liability | Who is responsible for an agent's action; agent identity and delegation; Moffatt v. Air Canada as precedent for automated statements | Write a policy brief on agent liability for an Indian fintech |
| 9.4 Labour-market evidence | Measured effects of AI on early-career software employment and productivity studies (see the [market map](../../../../06_career_and_market_readiness/01_market_map/README.md)) | Summarise the evidence and its limits in 500 words |

**Check your understanding:** What must a payment protocol record so that a disputed agent purchase can be resolved? Why do agent economies need identity standards? What would change your view on AI's labour-market effect?

### Chapter 10 · Research agents and open problems (weeks 10–11)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Automated research | The AI Scientist (Lu et al., 2024), AlphaEvolve (Novikov et al., 2025), PaperBench | Assess one claimed AI-generated research result for novelty and correctness |
| 10.2 Open problems list | Reliability (pass^k at long horizons), verification without ground truth, robust injection defences with low utility cost, oversight that scales, evaluation of open-ended work, memory safety | Rank the list by tractability for a one-year thesis |
| 10.3 Reproduction | Choosing a paper, scoping, compute budgets, reporting tolerances and deviations | Begin your reproduction (continues in weeks 12–13) |
| 10.4 Writing the proposal | Research question, hypothesis, method, evaluation, risks, ethics and safety review | Draft the proposal; peer review in pairs |

**Check your understanding:** What makes a research question about agents answerable in one year with modest compute? How do you report a failed reproduction usefully? Which open problem would most change industry practice if solved?

## Weekly rhythm

| Week | Chapter | Lab / seminar | Deliverable |
|---|---|---|---|
| 1 | 1 | Time-horizon re-analysis | Critique 1 |
| 2 | 2 | Multi-session harness experiment | Critique 2 |
| 3 | 3 | Computer-use agent in sandbox | Critique 3 · **P1 due** |
| 4 | 4 | AgentDojo evaluation of your agent | Critique 4 |
| 5 | 5 | Trusted monitoring and resampling | Critique 5 |
| 6 | 6 | Hidden-test reward-hacking study | Critique 6 |
| 7 | 7 | Benchmark audit; port an eval to Inspect | Critique 7 · **P2 due** |
| 8 | 8 | Memory evaluation | Critique 8 |
| 9 | 9 | A2A negotiation simulation; liability brief | Policy brief |
| 10 | 10 | Choose reproduction target | Reproduction plan |
| 11 | 10 | Open-problem ranking; proposal draft | Proposal draft |
| 12 | Reproduction | Reproduction work | Progress report |
| 13 | Reproduction | Reproduction work | Reproduction report |
| 14 | Symposium | Public research symposium | **P3 due** (reproduction + proposal) |
| 15 | Review | Oral examination | Final proposal |

## Working with AI in this course

- **Use AI for:** literature search and first-pass summaries (always open the paper afterwards); generating experiment scaffolding; running agents as research subjects; checking your statistics code; drafting related-work sections that you then verify citation by citation.
- **Do without AI (drills):** write every weekly critique yourself; present papers without slides generated by AI; derive your own threats-to-validity lists; hand-check every number you cite against the source table or figure.
- **Verify AI output by:** opening each cited paper and finding the exact claim; re-running any statistic an assistant computed; checking that summarised results specify the setting (simulated vs real, scaffold, number of trials); confirming leaderboard numbers on the leaderboard itself with a date.
- **Where AI still fails here (show it):** assistants blend findings from different papers and invent plausible citations (keep a log of each caught error); they flatten "in a simulated scenario" into general claims about model behaviour; and they repeat outdated benchmark numbers after saturation. Each critique must include one AI-generated claim you checked and whether it held.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Weekly critiques and presentations | 25% |
| Practical labs | 15% |
| P1 and P2 | 20% |
| P3: reproduction report + research proposal | 30% |
| Oral examination | 10% |

**Mastery gate.** You pass when you can: (1) reproduce a published agent result within a stated tolerance, or document a failed reproduction precisely enough that the authors could act on it; (2) defend a research proposal on long-horizon agents or agent safety before a panel, including its evaluation design, threats to validity and safety review; (3) in a 45-minute oral, critique an unseen frontier paper's main claim, its setting and its limits.

## Industry reality

Frontier labs and their customers now run agents for hours: vendors publish harness guidance for long-running work (Anthropic, Nov 2025), and computer-use agents ship in consumer products (OpenAI, Google, Anthropic). Safety and security research is applied directly: frontier safety frameworks set capability thresholds that trigger extra safeguards, government institutes such as the UK AI Security Institute publish open evaluation tooling, and agent security guidance (OWASP Agentic Top 10, Meta's Rule of Two, CaMeL-style designs) shapes products. Research engineers who can design rigorous agent evaluations, build control and monitoring systems, and reproduce results are in demand at labs, evaluation organisations and companies deploying agents.

**Interview questions from this course**

1. *How would you measure whether our agent can handle multi-day tasks?* Strong answer: define task suites with human time estimates; report 50% and 80% horizons with pass^k; environment-state checks; cost per success; contamination resistance; caveats about extrapolation.
2. *Our browsing agent reads arbitrary web pages and can send email. Make it safe.* Strong answer: remove a leg of the trifecta or apply Rule of Two; plan-then-execute or CaMeL-style separation; egress allow-lists; confirmation for sends; AgentDojo-style evaluation; monitoring and incident response.
3. *What is AI control and why would a product team care?* Strong answer: designing protocols that stay safe even if the model is adversarial; trusted monitoring, resampling, auditing budgets; practical value for high-stakes agents; limits and costs.
4. *A paper says models "blackmail" in a test. What do you conclude?* Strong answer: reads the setup: simulated environment, constructed goal conflicts, specific prompts; distinguishes propensity in contrived settings from deployment risk; extracts the engineering lesson (least privilege, oversight) without overclaiming.
5. *Pick an open problem in agents and outline a six-month project.* Strong answer: a scoped question (e.g. low-utility-cost injection defence for coding agents), a baseline, a measurable hypothesis, a benchmark and private test set, compute budget, risks, and what a negative result would teach.

## Resources (free first)

**Reading list (all free; each was checked 2026-10):**

- Measurement: Kwa et al., "Measuring AI Ability to Complete Long Tasks" — https://arxiv.org/abs/2503.14499 ; METR time horizons — https://metr.org/time-horizons/ ; Rein et al., HCAST — https://arxiv.org/abs/2503.17354 ; Wijk et al., RE-Bench — https://arxiv.org/abs/2411.15114 ; Miserendino et al., SWE-Lancer — https://arxiv.org/abs/2502.12115 ; Starace et al., PaperBench — https://arxiv.org/abs/2504.01848 ; Chan et al., MLE-bench — https://arxiv.org/abs/2410.07095
- Harnesses and compute: Anthropic, "Effective harnesses for long-running agents" — https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents ; Snell et al. — https://arxiv.org/abs/2408.03314 ; Wang et al., Voyager — https://arxiv.org/abs/2305.16291 ; Wang et al., Agent Workflow Memory — https://arxiv.org/abs/2409.07429
- Computer use: Xie et al., OSWorld — https://arxiv.org/abs/2404.07972 ; OSWorld-Verified — https://xlang.ai/blog/osworld-verified ; OSWorld 2.0 — https://osworld-v2.xlang.ai/ ; Zhou et al., WebArena — https://arxiv.org/abs/2307.13854 ; Deng et al., Mind2Web — https://arxiv.org/abs/2306.06070 ; He et al., WebVoyager — https://arxiv.org/abs/2401.13919 ; Qin et al., UI-TARS — https://arxiv.org/abs/2501.12326
- Security: Greshake et al. — https://arxiv.org/abs/2302.12173 ; Zhan et al., InjecAgent — https://arxiv.org/abs/2403.02691 ; Debenedetti et al., AgentDojo — https://arxiv.org/abs/2406.13352 ; Debenedetti et al., CaMeL — https://arxiv.org/abs/2503.18813 ; Beurer-Kellner et al. — https://arxiv.org/abs/2506.08837 ; Sharma et al., Constitutional Classifiers — https://arxiv.org/abs/2501.18837 ; Willison, lethal trifecta — https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/ ; Meta, Agents Rule of Two — https://ai.meta.com/blog/practical-ai-agent-security/
- Control and oversight: Greenblatt et al., AI Control — https://arxiv.org/abs/2312.06942 ; Bhatt et al., Ctrl-Z — https://arxiv.org/abs/2504.10374 ; Baker et al. — https://arxiv.org/abs/2503.11926 ; Korbak et al. — https://arxiv.org/abs/2507.11473
- Misalignment evidence: Meinke et al. — https://arxiv.org/abs/2412.04984 ; Greenblatt et al., Alignment faking — https://arxiv.org/abs/2412.14093 ; Hubinger et al., Sleeper Agents — https://arxiv.org/abs/2401.05566 ; Anthropic, Agentic misalignment — https://www.anthropic.com/research/agentic-misalignment
- Evaluation rigour: Zhu et al. — https://arxiv.org/abs/2507.02825 ; Kapoor et al. — https://arxiv.org/abs/2407.01502 ; Liang et al. — https://arxiv.org/abs/2506.12286
- Memory: Wu et al., LongMemEval — https://arxiv.org/abs/2410.10813 ; Xu et al., A-MEM — https://arxiv.org/abs/2502.12110 ; Rasmussen et al., Zep — https://arxiv.org/abs/2501.13956 ; Chhikara et al., Mem0 — https://arxiv.org/abs/2504.19413
- Multi-agent and research agents: Cemri et al. — https://arxiv.org/abs/2503.13657 ; Lu et al., The AI Scientist — https://arxiv.org/abs/2408.06292 ; Novikov et al., AlphaEvolve — https://arxiv.org/abs/2506.13131
- Frameworks and institutions: Anthropic Responsible Scaling Policy — https://www.anthropic.com/responsible-scaling-policy ; Google DeepMind Frontier Safety Framework — https://deepmind.google/blog/updating-the-frontier-safety-framework/ ; OpenAI Preparedness Framework — https://openai.com/index/updating-our-preparedness-framework/ ; UK AI Security Institute — https://www.aisi.gov.uk/ ; Inspect — https://inspect.aisi.org.uk/ ; EU GPAI Code of Practice — https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai
- Courses: Berkeley Advanced LLM Agents (Spring 2025) — https://llmagents-learning.org/sp25 ; Berkeley Agentic AI (Fall 2025) — https://agenticai-learning.org/f25

## Sources

- Kwa et al. (2025; v4 Jul 2026) "doubling approximately every seven months since 2019, though the trend may have accelerated in 2024" — https://arxiv.org/abs/2503.14499 ; METR data file (checked 2026-10) — https://metr.org/assets/benchmark_results_1_1.yaml ; METR time-horizons page (16-hour reliability caveat) — https://metr.org/time-horizons/
- Xie et al., OSWorld (2024): human 72.36%, best model 12.24% — https://arxiv.org/abs/2404.07972 ; OSWorld-Verified leaderboard (top entries above the human baseline, checked 2026-10) — https://os-world.github.io/ ; OSWorld 2.0 (best reported ≈20.6%, checked 2026-10) — https://osworld-v2.xlang.ai/
- Anthropic, computer use launch (22 Oct 2024; OSWorld 14.9%) — https://www.anthropic.com/news/3-5-models-and-computer-use ; OpenAI, "Introducing ChatGPT agent" (17 Jul 2025) — https://openai.com/index/introducing-chatgpt-agent/ ; Google, Gemini 2.5 Computer Use (7 Oct 2025) — https://blog.google/innovation-and-ai/models-and-research/google-deepmind/gemini-computer-use-model/ (checked 2026-10)
- Anthropic, Claude Sonnet 4.5 announcement ("maintaining focus for more than 30 hours", 29 Sept 2025) — https://www.anthropic.com/news/claude-sonnet-4-5 ; "Effective harnesses for long-running agents" (26 Nov 2025) — https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents (checked 2026-10)
- Debenedetti et al., CaMeL (2025): 77% of AgentDojo tasks with provable security vs 84% undefended — https://arxiv.org/abs/2503.18813 ; AgentDojo (97 tasks, 629 security test cases) — https://arxiv.org/abs/2406.13352 (checked 2026-10)
- Anthropic, "Agentic misalignment" (20 Jun 2025; 16 models; simulated settings) — https://www.anthropic.com/research/agentic-misalignment (checked 2026-10)
- Meta, "Agents Rule of Two" (31 Oct 2025) — https://ai.meta.com/blog/practical-ai-agent-security/ ; Willison, "The lethal trifecta for AI agents" (16 Jun 2025) — https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/ (checked 2026-10)
- All other papers as listed in the reading list above, arXiv metadata checked 2026-10.

_Last reviewed: 2026-10_
