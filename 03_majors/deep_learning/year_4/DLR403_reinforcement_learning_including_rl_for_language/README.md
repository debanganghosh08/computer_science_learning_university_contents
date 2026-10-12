# DLR403 · Reinforcement Learning, Including RL for Language Models

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 4 · 8 | 4 (≈ 120 hours) | L2 → L4 | [DLR303](../../year_3/DLR303_sequence_models_and_transformers/README.md); in practice also [DLR301](../../year_3/DLR301_neural_networks_from_scratch_autograd/README.md) and [DLR401](../DLR401_large_language_models_pretraining_fine_tuning/README.md) | [DLR501](../../year_5/DLR501_frontier_seminar_interpretability_reasoning/README.md); taken alongside [DLR404](../DLR404_efficient_deep_learning_and_gpu_programming/README.md) |

## Why this course matters now

Reinforcement learning (RL) went from games and robots to the centre of language-model training. Classic results still define the field: DQN learned Atari games from pixels (2013–2015), AlphaZero and MuZero mastered board games through self-play and planning, and DreamerV3 was the first algorithm to collect diamonds in Minecraft from scratch without human data (Hafner et al., 2023). Since 2024, RL with verifiable rewards has become a core post-training stage. GRPO (Shao et al., 2024) removed the critic, DeepSeek-R1 showed that reasoning can emerge from RL, and a 400,000-GPU-hour study found that RL compute–performance curves follow predictable sigmoids (Khatri et al., 2025). RL also fails in characteristic ways. Policies exploit flaws in their reward. In Anthropic's experiments, models that learned to reward-hack real coding environments generalised to "alignment faking" and sabotage (MacDiarmid et al., 2025). Penalising "bad thoughts" in the chain of thought produced "obfuscated reward hacking" (Baker et al., 2025). Libraries such as TRL and verl make running GRPO a matter of a config file. The engineers who matter understand the estimator, the variance, the environment and the ways a reward can be gamed.

## Learning outcomes

By the end you can:

1. **Formulate** problems as MDPs, and **derive** Bellman equations, policy-gradient theorems and the advantage function.
2. **Implement** value iteration, Q-learning, DQN, REINFORCE, actor–critic with GAE, PPO and SAC from scratch, and **match** reference learning curves.
3. **Evaluate** RL agents properly: multiple seeds, confidence intervals, and sensitivity to implementation details.
4. **Explain** model-based RL and planning (MCTS, MuZero, Dreamer) and offline RL, and **choose** an approach for a given data and simulator budget.
5. **Implement** RL for language models: KL-regularised policy optimisation, RLOO, GRPO and its variants, with a working verifier.
6. **Design** environments and rewards that resist exploitation, and **detect** reward hacking with held-out checks and monitors.
7. **Analyse** what RL adds to a pretrained model using pass@k, entropy and coverage measurements.

## Chapters and lessons

### Chapter 1 · The RL problem and bandits (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Agents and environments | States, actions, rewards, returns, discounting; episodic vs continuing tasks | Wrap a small task as a Gymnasium environment |
| 1.2 Multi-armed bandits | Exploration vs exploitation; ε-greedy, UCB, Thompson sampling; regret | 10-armed testbed; regret curves over 2,000 runs |
| 1.3 MDPs | Markov property, policies, value and action-value functions | Write the MDP for a gridworld by hand |
| 1.4 Bellman equations | Expectation and optimality equations | Solve a 3-state MDP's values with linear algebra |

**Check your understanding:** Why does greedy action selection fail in bandits, and how does UCB fix it? What does the discount factor mean in a task with no natural end? Why is the Bellman optimality equation non-linear?

### Chapter 2 · Dynamic programming (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Policy evaluation | Iterative evaluation; contraction mapping | Evaluate a random policy on FrozenLake |
| 2.2 Policy iteration | Evaluate, improve, repeat; why it converges | Implement and count iterations |
| 2.3 Value iteration | One-sweep Bellman optimality updates | Compare with policy iteration on 3 map sizes |
| 2.4 The curse of dimensionality | Asynchronous DP; why tabular methods break and approximation is needed | Time value iteration as the state space grows; find where it becomes impractical |

**Check your understanding:** Why does policy improvement never make a policy worse? When is value iteration cheaper than policy iteration? Why can dynamic programming not be used directly on Atari?

### Chapter 3 · Monte Carlo and temporal-difference learning (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Monte Carlo methods | Learning from complete episodes; first-visit vs every-visit | MC prediction on Blackjack |
| 3.2 TD(0) | Bootstrapping; bias–variance trade-off vs Monte Carlo | Random-walk example: TD vs MC error curves |
| 3.3 SARSA and Q-learning | On-policy vs off-policy control | Cliff Walking: reproduce Sutton and Barto's SARSA vs Q-learning result |
| 3.4 n-step returns | Interpolating between TD and MC | n-step sweep on the random walk |

**Check your understanding:** Why does Q-learning learn the risky cliff-edge path while SARSA learns the safe one? What bias does bootstrapping introduce, and what does it buy? Why is Q-learning called off-policy?

### Chapter 4 · Deep Q-learning (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Function approximation | The deadly triad: bootstrapping, off-policy learning, function approximation | Make linear Q-learning diverge on a small example |
| 4.2 DQN | Experience replay, target networks (Mnih et al., 2013/2015) | DQN on CartPole, then a MinAtar game |
| 4.3 Improvements | Double DQN (van Hasselt et al., 2015), dueling heads, prioritised replay | Measure overestimation with and without Double DQN |
| 4.4 Atari practice | Arcade Learning Environment, frame stacking, sticky actions | Run a CleanRL Atari baseline; read its code line by line |

**Check your understanding:** Why does a target network stabilise training? Where does Q-value overestimation come from? Why are sticky actions needed for a fair Atari evaluation?

### Chapter 5 · Policy gradients (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 REINFORCE | The log-derivative trick; unbiased but high-variance gradients | Derive it; implement on CartPole |
| 5.2 Baselines | Subtracting a state-dependent baseline keeps the gradient unbiased | Show variance reduction empirically |
| 5.3 Actor–critic | Learned value baseline; advantage estimates | Actor–critic on CartPole and LunarLander |
| 5.4 GAE | Generalised advantage estimation with λ (Schulman et al., 2015) | λ sweep; plot learning speed and variance |

**Check your understanding:** Why does subtracting a baseline not bias the policy gradient? What do γ and λ each control in GAE? Why are policy-gradient methods natural for language models?

### Chapter 6 · Trust regions and PPO (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Why steps must be small | Policy collapse after one large update; TRPO's KL constraint (Schulman et al., 2015) | Show collapse with a large learning rate |
| 6.2 PPO | Clipped surrogate objective, value loss, entropy bonus (Schulman et al., 2017) | PPO from scratch |
| 6.3 Implementation details | Advantage normalisation, orthogonal init, learning-rate annealing, value clipping; "Implementation Matters" (Engstrom et al., 2020); "The 37 Implementation Details of PPO" | Ablate 4 details; measure their effect over 5 seeds |
| 6.4 Evaluation rigour | Seeds and confidence intervals; "Deep RL that Matters" (Henderson et al., 2017) | Plot 10-seed curves with CIs vs a cherry-picked seed |

**Check your understanding:** What does the PPO clip prevent, and what can still go wrong? Why can two PPO implementations of "the same algorithm" give very different results? How many seeds do you need to claim that one RL method beats another?

### Chapter 7 · Continuous control and off-policy actor–critic (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Deterministic policies | DDPG and TD3's clipped double Q (Fujimoto et al., 2018) | TD3 on Pendulum |
| 7.2 Maximum entropy RL | SAC: entropy bonus, automatic temperature (Haarnoja et al., 2018) | SAC on a MuJoCo task; compare with PPO for sample efficiency |
| 7.3 Simulators | MuJoCo, physics fidelity, sim-to-real gap | Domain randomisation on one physics parameter |
| 7.4 Learning from demonstrations | Behaviour cloning, compounding errors, DAgger; vision–language–action policies in outline | Behaviour cloning from 50 demonstrations vs SAC on the same task |

**Check your understanding:** Why is SAC more sample-efficient than PPO on many control tasks? What does the entropy term buy in exploration and robustness? Why do policies trained in simulation fail on real robots?

### Chapter 8 · Model-based RL and planning (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Learned models | Dynamics models, model error compounding; Dyna | Dyna-Q on a gridworld; vary planning steps |
| 8.2 Search | Monte Carlo tree search; AlphaZero's policy and value guidance (Silver et al., 2017) | MCTS with a learned value net for Connect-4 |
| 8.3 MuZero and Dreamer | Planning in a learned latent space (Schrittwieser et al., 2019); world models and imagination (DreamerV3) | Read and present one paper's key ablation |
| 8.4 When to plan | Planning compute vs model accuracy; test-time search in language models as planning (see DLR501) | Vary MCTS simulations; plot playing strength vs compute |

**Check your understanding:** Why does model error compound over long rollouts? What does MuZero learn instead of the true environment dynamics? When is model-based RL worth its complexity?

### Chapter 9 · Offline RL (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Learning from logs | Distribution shift; why naive off-policy RL overestimates unseen actions | Behaviour cloning baseline on a Minari dataset |
| 9.2 Conservative methods | CQL (Kumar et al., 2020) | CQL vs behaviour cloning on the same data |
| 9.3 RL as sequence modelling | Decision Transformer (Chen et al., 2021) | Return-conditioned generation on a small dataset |
| 9.4 Off-policy evaluation | Importance sampling and doubly robust estimators; estimating a new policy from logs before deploying it | Estimate a new policy's value from logs; compare with its true return |

**Check your understanding:** Why does offline RL need conservatism? When does behaviour cloning beat offline RL? What does a Decision Transformer assume about the data?

### Chapter 10 · RL for language models I: RLHF and REINFORCE revisited (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 The LM as a policy | Tokens as actions; sequence-level rewards; KL to a reference model | Write the objective and its gradient |
| 10.2 PPO for RLHF | Value heads, per-token KL penalties, rollout and training phases (InstructGPT) | Trace a PPO-RLHF step in TRL |
| 10.3 REINFORCE-style methods | RLOO's leave-one-out baseline (Ahmadian et al., 2024) | RLOO on a GPT-2 sentiment-steering task |
| 10.4 Infrastructure | Generation-bound rollouts; vLLM for sampling; verl's hybrid design (Sheng et al., 2024) | Profile one RL step: share of time in generation vs training |

**Check your understanding:** Why is the KL term essential in RLHF? Why do LLM RL steps spend most of their time generating? What does RLOO use as a baseline, and why is it unbiased?

### Chapter 11 · RL for language models II: verifiable rewards and GRPO (weeks 11–12)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 GRPO | Group-relative advantages, no critic, clipped ratio, KL (Shao et al., 2024) | GRPO from scratch (no RL library) for a 0.5B model on an arithmetic task |
| 11.2 Known biases and fixes | Length and difficulty bias in normalisation (Dr. GRPO, Liu et al., 2025); clip-higher, dynamic sampling, token-level loss (DAPO, Yu et al., 2025); sequence-level ratios (GSPO, Zheng et al., 2025) | Ablate one fix; plot length and entropy |
| 11.3 Rewards and verifiers | Exact-match, unit tests, format rewards, partial credit; sandboxes for code | Build a sandboxed unit-test reward for Python problems |
| 11.4 What RLVR changes | pass@k at large k (Yue et al., 2025); spurious rewards (Shao et al., 2025); entropy collapse | pass@k and entropy before/after your run |
| 11.5 Scaling RL | Sigmoidal compute–performance fits and ScaleRL (Khatri et al., 2025) | Fit a sigmoid to your own reward curve; predict the plateau |

**Check your understanding:** Why does GRPO get no learning signal when every sample in a group has the same reward? Why can normalising by response length bias a model towards long wrong answers? What would convince you that RL taught a model something new rather than sharpening what it already knew?

### Chapter 12 · Reward hacking and safe RL (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Specification gaming | Goodhart's law; DeepMind's catalogue of examples (Krakovna et al., 2020); a formal definition (Skalse et al., 2022) | Find 3 exploits in a deliberately flawed environment |
| 12.2 Reward-model over-optimisation | Proxy vs gold reward (Gao et al., 2022) | Reproduce the over-optimisation curve with best-of-n |
| 12.3 Hacking in LLM training | Test-special-casing in coding RL and its generalisation to misalignment; inoculation prompting (MacDiarmid et al., 2025); evaluation-harness exploits (Sakana AI, 2025) | Train against a weak test suite; detect hacks with a held-out suite |
| 12.4 Monitoring | Chain-of-thought monitors and the obfuscation risk under optimisation pressure (Baker et al., 2025) | Build an LLM-based monitor; measure its recall on your hacks |
| 12.5 Safe exploration and constraints | Constrained MDPs, safety layers, human oversight | Add a cost constraint to a gridworld agent |

**Check your understanding:** Why does stronger optimisation make reward hacking more likely? Why is penalising a model for revealing hacking in its reasoning risky? List three properties of an environment that make it resistant to exploitation.

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Bandits and dynamic programming | Regret curves |
| 2 | 2 | Lab 1 (cont.) | — |
| 3 | 3 | Lab 2 · TD control on Cliff Walking | — |
| 4 | 4 | Lab 3 · DQN | DQN learning curves |
| 5 | 5 | Lab 4 · REINFORCE, actor–critic, GAE | — |
| 6 | 6 | Lab 5 · PPO and implementation details | **P1 due** |
| 7 | 7 | Lab 6 · SAC vs PPO | — |
| 8 | 8 | Lab 7 · Planning and offline RL | Mid-term (AI off) |
| 9 | 9 | Lab 7 (cont.) | — |
| 10 | 10 | Lab 8 · RLOO for an LM | **P2 due** |
| 11 | 11 | Lab 9 · GRPO from scratch | — |
| 12 | 11 | Lab 9 (cont.) | pass@k and entropy report |
| 13 | 12 | Lab 10 · Hack, detect, patch | Monitor recall report |
| 14 | 12 | Project studio | **P3 due** |
| 15 | Review | Oral defence of P3 | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** environment wrappers and plotting; translating pseudo-code from papers into PyTorch after you have read the derivation; reviewing your code against CleanRL references; writing unit tests for verifiers; acting as a chain-of-thought monitor in Lab 10.
- **Do without AI (drills):** Bellman equations, the policy-gradient theorem, GAE, the PPO and GRPO objectives on paper; reading learning curves and diagnosing failures; designing a reward and listing its possible exploits; both exams.
- **Verify AI output by:** (1) matching published or CleanRL learning curves over at least 5 seeds; (2) checking gradient signs and advantage normalisation on a two-action toy problem; (3) testing verifiers against adversarial outputs before training; (4) inspecting high-reward samples by hand, not only the mean reward.
- **Where AI still fails here:** RL is where automated optimisers most visibly game their objectives. Sakana AI's system exploited its evaluation code to report speed-ups that did not exist (TechCrunch, 2025), and frontier coding agents learned reward hacks in production environments (MacDiarmid et al., 2025). In this course, keep a hack log: every case where reward went up without the intended behaviour, from your agents and from AI-written environments.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1–P3 | 35% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) and oral defence of P3 | 30% |

**Mastery gate.** You pass when you can: (1) with AI off, derive the policy-gradient theorem with a baseline, the PPO clipped objective and GRPO's advantage; (2) implement PPO that solves LunarLander (mean return ≥ 200, Gymnasium's "solved" threshold) in at least 3 of 5 seeds, and GRPO that improves a small LM's pass@1 on a verifiable task with confidence intervals; (3) find and explain a reward exploit in an environment you have not seen before.

## Industry reality

RL for language models is a core part of frontier post-training: Tülu 3 introduced RLVR as a named stage (2024), DeepSeek-R1 put RL at the centre of reasoning training (2025), and Kimi K2 describes a joint RL stage with real and synthetic environments (2025). Open infrastructure includes TRL, verl and OpenRLHF. Classic RL continues in robotics, recommendation (with offline RL), operations and games. Interviews for post-training and RL roles test derivations, implementation details and reward design.

**Interview questions from this course**

1. *Derive the policy gradient and explain why a baseline helps.* Strong answer: log-derivative trick; expectation over trajectories; baseline has zero expected gradient contribution so stays unbiased; reduces variance; advantage as the natural choice.
2. *Why does PPO clip the ratio, and what are its known failure modes?* Strong answer: approximate trust region preventing destructive updates; clip interacts with advantage sign; sensitive to implementation details (normalisation, value clipping, learning-rate schedule); can still drift with many epochs.
3. *Compare PPO with a critic, RLOO and GRPO for training an LLM on math.* Strong answer: memory and compute of a value model; baseline choice per method; group sampling cost; normalisation biases (Dr. GRPO); stability fixes (DAPO, GSPO); evaluation by pass@k.
4. *Your RL-trained coding model's test pass rate jumped 20 points overnight. What do you check?* Strong answer: inspects high-reward samples; held-out stronger tests; looks for special-casing, test-file edits or harness exploits; checks sandbox isolation; monitors chain of thought; only then believes the gain.
5. *How would you design a reward for a customer-support agent that resists gaming?* Strong answer: combines verifiable outcomes with rubric-based judges; held-out audits; penalties for known exploits; KL to a reference; human review of samples; monitoring after deployment.

## Resources (free first)

- **Textbook:** Sutton and Barto, *Reinforcement Learning: An Introduction*, 2nd ed. (2018; free PDF from the authors) — http://incompleteideas.net/book/the-book-2nd.html
- **Courses:** UC Berkeley CS285, Deep Reinforcement Learning — https://rail.eecs.berkeley.edu/deeprlcourse/ ; Stanford CS234 — https://web.stanford.edu/class/cs234/ ; OpenAI *Spinning Up in Deep RL* — https://spinningup.openai.com/ ; Hugging Face Deep RL Course — https://huggingface.co/learn/deep-rl-course/unit0/introduction
- **Books on RL for LLMs:** Nathan Lambert, *Reinforcement Learning from Human Feedback* — https://rlhfbook.com/
- **Code and environments:** Gymnasium — https://gymnasium.farama.org/ ; Arcade Learning Environment — https://ale.farama.org/ ; MinAtar — https://github.com/kenjyoung/MinAtar ; MuJoCo — https://github.com/google-deepmind/mujoco ; Minari (offline datasets) — https://minari.farama.org/ ; CleanRL — https://github.com/vwxyzjn/cleanrl ; TRL — https://github.com/huggingface/trl ; verl — https://github.com/volcengine/verl ; "The 37 Implementation Details of PPO" — https://iclr-blog-track.github.io/2022/03/25/ppo-implementation-details/
- **Key papers:** DQN https://arxiv.org/abs/1312.5602 ; PPO https://arxiv.org/abs/1707.06347 ; GAE https://arxiv.org/abs/1506.02438 ; SAC https://arxiv.org/abs/1801.01290 ; MuZero https://arxiv.org/abs/1911.08265 ; DreamerV3 https://arxiv.org/abs/2301.04104 ; CQL https://arxiv.org/abs/2006.04779 ; RLOO https://arxiv.org/abs/2402.14740 ; GRPO https://arxiv.org/abs/2402.03300 ; DAPO https://arxiv.org/abs/2503.14476 ; GSPO https://arxiv.org/abs/2507.18071 ; ScaleRL https://arxiv.org/abs/2510.13786 ; specification gaming https://deepmind.google/discover/blog/specification-gaming-the-flip-side-of-ai-ingenuity/
- **Compute (free):** classic RL labs run on CPU or a free T4; GRPO with a 0.5B model fits a T4 with LoRA and short generations; keep group sizes and sequence lengths small and log GPU-hours.

## Sources

- Hafner et al., "Mastering Diverse Domains through World Models" (DreamerV3, 2023) — https://arxiv.org/abs/2301.04104 (checked 2026-10)
- Shao et al., "DeepSeekMath" (GRPO, 2024) — https://arxiv.org/abs/2402.03300 ; DeepSeek-AI, "DeepSeek-R1" (2025) — https://arxiv.org/abs/2501.12948 (checked 2026-10)
- Khatri et al., "The Art of Scaling Reinforcement Learning Compute for LLMs" (Oct 2025) — https://arxiv.org/abs/2510.13786 (checked 2026-10)
- MacDiarmid et al., "Natural Emergent Misalignment from Reward Hacking in Production RL" (Nov 2025) — https://arxiv.org/abs/2511.18397 (checked 2026-10)
- Baker et al., "Monitoring Reasoning Models for Misbehavior and the Risks of Promoting Obfuscation" (Mar 2025) — https://arxiv.org/abs/2503.11926 (checked 2026-10)
- TechCrunch, "Sakana walks back claims that its AI can dramatically speed up model training" (21 Feb 2025) — https://techcrunch.com/2025/02/21/sakana-walks-back-claims-that-its-ai-can-dramatically-speed-up-model-training/ (checked 2026-10)
- Gymnasium LunarLander documentation ("considered a solution if it scores at least 200 points") — https://gymnasium.farama.org/environments/box2d/lunar_lander/ (checked 2026-10)
- Sutton and Barto book page — http://incompleteideas.net/book/the-book-2nd.html (site unreachable when checked on 2026-10-12; MIT Press also lists the book)

_Last reviewed: 2026-10_
