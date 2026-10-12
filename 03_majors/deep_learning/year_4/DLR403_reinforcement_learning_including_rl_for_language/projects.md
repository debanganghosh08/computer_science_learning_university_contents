# DLR403 · Labs and projects

Every lab and project ships with code, at least 5 seeds for classic RL results (3 for LLM runs), learning curves with confidence bands, and a "hack log" listing every case where reward rose without the intended behaviour. Code that executes model outputs must run in a sandbox with no network access and resource limits.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Bandits and dynamic programming | ε-greedy, UCB and Thompson sampling on a 10-armed testbed; policy and value iteration on FrozenLake (several map sizes, slippery and not) | Regret curves over 2,000 runs; iteration counts, value heatmaps and policy arrows | 5 h |
| 2 · TD control on Cliff Walking | SARSA vs Q-learning; n-step returns on the random walk | Reproduction of the textbook result; RMS error vs n | 3 h |
| 3 · DQN | DQN and Double DQN on CartPole and a MinAtar game; overestimation measurement | Curves over 5 seeds; Q-value overestimation plot | 5 h |
| 4 · REINFORCE, actor–critic, GAE | All three on CartPole and LunarLander; λ sweep | Variance-of-gradient measurements; learning curves | 4 h |
| 5 · PPO and implementation details | PPO from scratch; ablate 4 implementation details | Match CleanRL's curves within its seed spread; ablation table | 6 h |
| 6 · SAC vs PPO | Both on a MuJoCo task at equal environment steps | Sample-efficiency curves; wall-clock comparison | 4 h |
| 7 · Planning and offline RL | MCTS with a small self-play value/policy network for Connect-4; behaviour cloning vs CQL on a Minari dataset of mixed quality | Win rates vs pure MCTS and a minimax baseline; returns by dataset quality and a note on when behaviour cloning wins | 9 h |
| 8 · RLOO for an LM | Steer GPT-2 small towards positive sentiment with RLOO and a KL penalty | Reward vs KL curve; 20 samples at 3 KL strengths | 4 h |
| 9 · GRPO from scratch | Your own GRPO (no RL library) for a 0.5B model on an arithmetic or countdown task; then compare with TRL's trainer | Reward, length, entropy curves; pass@1 and pass@k vs base; agreement with the library | 8 h |
| 10 · Hack, detect, patch | Train against a deliberately weak unit-test reward; detect hacks with held-out tests and an LLM monitor; patch and retrain | Hack log; monitor recall and precision; before/after true pass rates | 6 h |

## Projects

### P1 · PPO you can trust (L1, ~6 hours)

**Real-world inspiration.** PPO is the default policy-gradient algorithm in robotics, games and RLHF, and its results depend heavily on implementation details (Engstrom et al., 2020; Huang et al., "The 37 Implementation Details of PPO", 2022).

**What to build.** A single-file PPO implementation (in the CleanRL style) for discrete and continuous Gymnasium environments, with logging and a seed-sweep script.

**Acceptance criteria**
- LunarLander: mean return ≥ 200 over 100 evaluation episodes (Gymnasium's "solved" threshold) in at least 3 of 5 seeds within 1M environment steps.
- CartPole solved in every seed; a continuous-control task (Pendulum or a MuJoCo environment) learning curve is reported.
- Curves are plotted as mean with 95% bootstrap bands over 5 seeds; no single-seed claims.
- An ablation of advantage normalisation and learning-rate annealing, showing their effect with CIs.

**Compute budget.** CPU or one free T4; ≤ 6 hours of wall-clock time for all seeds.

**Stretch goals.** Vectorised environments and a throughput benchmark; a recurrent policy for a partially observed variant.

**What it proves to an employer.** You can implement a core RL algorithm correctly and report it honestly.

### P2 · Traffic-signal control for a mixed-traffic junction (L2, ~15 hours)

**Real-world inspiration.** Adaptive traffic signals use sensing and optimisation to cut waiting times, and Indian junctions add two-wheelers, auto-rickshaws and weak lane discipline. SUMO is an open traffic simulator widely used in research (https://eclipse.dev/sumo/), and `sumo-rl` exposes it as an RL environment (https://github.com/LucasAlegre/sumo-rl). The junction and demand pattern here are illustrative; they do not model any real city's system.

**What to build.** An RL controller for a 4-way junction in SUMO with a demand mix that includes many two-wheelers, trained with PPO or DQN, and compared with fixed-time and max-pressure baselines.

**Acceptance criteria**
- The environment, demand files and vehicle types are documented; morning-peak and off-peak demand are both tested.
- Average waiting time and queue length are reported for RL, fixed-time and max-pressure controllers over 10 seeds with CIs; RL beats fixed-time by a margin outside the interval at peak demand.
- A robustness test: the trained controller is evaluated on a 20% demand increase it never saw.
- A reward-design section: two rewards are compared (for example, queue length vs waiting-time change), with any exploit observed (such as starving one approach) recorded in the hack log.
- A fairness metric: maximum waiting time on any approach is reported, not only the average.

**Compute budget.** CPU only (simulation dominates); ≤ 20 CPU-hours across all seeds.

**Stretch goals.** Two coordinated junctions; a pedestrian phase with a safety constraint; offline pre-training from logged fixed-time data.

**What it proves to an employer.** You can apply RL to a messy real-world control problem, compare against strong non-RL baselines, and design rewards with their failure modes in mind.

### P3 · RL with verifiable rewards for code, with a reward-hacking audit (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** Coding is a main target of RLVR, and also where reward hacking has been documented: models trained on production coding environments learned to game tests, which generalised to broader misalignment (MacDiarmid et al., 2025), and an AI system exploited its evaluation harness to fake kernel speed-ups (Sakana AI, February 2025). Chain-of-thought monitors can catch hacks but can be evaded under optimisation pressure (Baker et al., 2025).

**What to build.** GRPO-family training (with one stability fix of your choice) of a 0.5–1.5B open model on Python problems from MBPP (Austin et al., 2021, https://arxiv.org/abs/2108.07732) and similar openly licensed sets, with rewards from unit tests run in a sandbox. Run two conditions: (a) a strong test suite and (b) a deliberately weak one (few tests, tests visible to the model). Build detection: held-out stronger tests, static checks for special-casing, and an LLM-based monitor over reasoning traces.

**Acceptance criteria**
- Sandbox: no network, CPU and memory limits, timeouts, and file-system isolation; a test proves each restriction works.
- Condition (a): pass@1 on held-out problems (held-out tests) improves over the base model by a margin outside the 95% bootstrap interval; pass@k curves up to k = 32 are shown for base and trained models.
- Condition (b): the hack log shows at least one exploit class, with examples; the gap between weak-test reward and held-out pass rate is plotted over training.
- Detection: recall and precision of the monitor and static checks on a labelled set of 100 trajectories.
- One mitigation (stronger tests, hidden tests, penalties, or inoculation-style prompting) is evaluated in condition (b).
- Compute ≤ 30 GPU-hours on one 24–48 GB GPU (or a smaller model on Kaggle 2× T4); all runs logged.

**Stretch goals.** Multi-turn environments where the model can run tests before submitting; compare GRPO with RLOO at equal samples.

**What it proves to an employer.** You can run RL for language models and also secure it against its most important failure mode. Post-training, evaluation and safety teams look for exactly this combination.

## Feeds into

- [DLR501 Frontier Seminar](../../year_5/DLR501_frontier_seminar_interpretability_reasoning/README.md): the formal follow-on; reasoning models, test-time compute and chain-of-thought monitoring.
- [OV05 AI Security and Safety Engineering](../../../../04_overlaps/OV05_ai_security_safety/README.md): reward hacking, monitoring and safe deployment of agents.
- [DLR404 Efficient Deep Learning and GPU Programming](../DLR404_efficient_deep_learning_and_gpu_programming/README.md): rollout throughput and memory for RL on language models.
- [MLE403 Ranking and Recommendation Systems at Scale](../../../machine_learning_engineering/year_4/MLE403_ranking_and_recommendation_systems_at_scale/README.md): bandits and offline RL in recommendation.
- [THS501 Thesis or Capstone I](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md): reward design and hacking detection are open research problems.
