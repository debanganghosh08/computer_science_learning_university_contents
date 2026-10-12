# OPS501 · Frontier Seminar: Autonomous Infrastructure and Self-Healing Systems

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 5 · 9 | 4 (≈ 120 hours) | L4 → L5 | [OPS401](../../year_4/OPS401_platform_engineering_and_internal_developer/README.md), [OPS403](../../year_4/OPS403_aiops_and_agentic_operations/README.md); recommended alongside: [RES501](../../../../05_shared_years_3_to_5/RES501_research_methods_and_scientific_writing/README.md), [RES502](../../../../05_shared_years_3_to_5/RES502_reading_reproducing_and_extending_papers/README.md) | [THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md), [THS502](../../../../05_shared_years_3_to_5/THS502_thesis_or_capstone_ii/README.md), [LCH502](../../../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md) |

Part of the [DevOps, SRE and Platform Engineering major](../../README.md). This is a research seminar, not a tools course. Each week you read two or three papers, present one, and reproduce a result in the lab. The semester ends with a short research paper and artefact of your own. The question running through the course: how far can infrastructure safely manage itself, and how can we know that it is correct? You bring the control loops of [OPS305](../../year_3/OPS305_configuration_management_and_gitops/README.md), the platforms of [OPS401](../../year_4/OPS401_platform_engineering_and_internal_developer/README.md), the failure knowledge of [OPS402](../../year_4/OPS402_chaos_engineering_and_resilience/README.md) and the agents of [OPS403](../../year_4/OPS403_aiops_and_agentic_operations/README.md).

## Why this course matters now

Infrastructure already runs on automatic control loops:

- **Kubernetes controllers** reconcile desired state continuously.
- **Google's Autopilot** sets container resource limits automatically (EuroSys 2020).
- **Microsoft's Gandalf** watches deployments and stops bad ones across Azure (NSDI 2020).

The new step is AI agents that diagnose and act. Microsoft Research calls the vision "AgentOps" (AIOpsLab, 2025), and every major cloud now ships an operations agent. Yet the best agents resolve a minority of realistic SRE scenarios (13.8% in ITBench). Automation itself causes outages: AWS's October 2025 us-east-1 event began with a race condition between two automated DNS components.

The research frontier is about both capability and assurance:

- **Formal methods at AWS:** TLA+ and the P language are used to find design bugs before they ship (CACM 2015 and 2025).
- **Automated reasoning:** SMT solvers answer questions about every IAM policy and network path (Zelkova, Tiros).
- **Verified controllers:** Kubernetes controllers can be tested systematically (Sieve, Acto) and their liveness verified (Anvil, OSDI 2024 Best Paper).

Engineers who can combine these (autonomy with proofs, tests and bounded permissions) will design the next generation of operations systems, or found the companies that sell them.

## Learning outcomes

By the end you can:

1. **Explain** infrastructure automation as control theory (feedback, stability, oscillation, level- vs edge-triggered reconciliation) and **analyse** a controller for instability.
2. **Summarise and critique** the main published self-healing and safe-deployment systems (Autopilot, Gandalf, Kubernetes controllers, AWS static stability), including their evaluation methods.
3. **Write** a TLA+ (or P) specification of an infrastructure protocol, **state** safety and liveness properties, and **find** a bug with the model checker.
4. **Explain** how automated reasoning (SMT-based policy analysis, network reachability, configuration verification with Batfish) gives guarantees that testing cannot.
5. **Apply** controller testing and verification ideas (Sieve, Acto, Anvil) to a Kubernetes operator.
6. **Model** metastable and gray failures, and **evaluate** detection or mitigation proposals.
7. **Evaluate** agentic operations research (AIOpsLab, ITBench, OpenRCA) for realism, contamination and safety, and **propose** better evaluations.
8. **Design** bounded-autonomy systems in which agent actions are checked against formal constraints, policies and blast-radius limits.
9. **Produce** a workshop-quality paper with a reproducible artefact.

## Chapters and lessons

### Chapter 1 · Control loops everywhere (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Feedback control | Set point, sensor, controller, actuator; proportional control, lag, overshoot, oscillation | Simulate an autoscaler with lag and make it oscillate |
| 1.2 Reconciliation | Level-triggered vs edge-triggered; idempotent reconcile; Kubernetes controller design ("Borg, Omega, and Kubernetes", ACM Queue 2016) | Write a toy reconciler; crash it mid-loop; show convergence |
| 1.3 Interacting controllers | HPA vs VPA vs cluster autoscaler; controllers fighting each other | Reproduce two controllers fighting over one resource |
| 1.4 Stabilisers in practice | Damping, hysteresis, cool-down periods and rate limits as engineering fixes for unstable loops | Add hysteresis to your autoscaler and show the oscillation stops |

**Check your understanding:** (1) Why is level-triggered reconciliation more robust than event handling? (2) What makes two correct controllers unsafe together? (3) How does lag cause oscillation in autoscaling?

### Chapter 2 · Self-healing in production (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Autopilot | ML-based vertical and horizontal scaling at Google; slack vs OOM risk (EuroSys 2020) | Present the paper; reproduce its recommender idea on your VPA data |
| 2.2 Gandalf | Safe deployment analytics across Azure: correlating failures with rollouts, stopping bad changes (NSDI 2020) | Re-implement a simplified rollout-blame detector |
| 2.3 Static stability and cells | AWS Builders' Library ideas as design-time self-healing | Critique one design for hidden control-plane dependencies |
| 2.4 When automation causes outages | AWS DynamoDB DNS race (Oct 2025); Google Service Control (Jun 2025) | Write a "failure of automation" analysis for both |

**Check your understanding:** (1) What evidence do Autopilot and Gandalf give that their automation is safe? (2) Why did a race between two automation components cause the AWS 2025 outage? (3) What should every self-healing system be unable to do?

### Chapter 3 · Formal methods in industry (weeks 3–4)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Why model check | Newcombe et al., "How Amazon Web Services Uses Formal Methods" (CACM 2015): TLA+ on S3, DynamoDB and other systems | Present the paper's bug-finding examples |
| 3.2 TLA+ basics | States, actions, invariants, temporal properties, TLC model checking | Specify a deploy lock; find a two-writer bug |
| 3.3 Beyond TLA+ | P language, property-based testing, deterministic simulation; Brooker and Desai, "Systems Correctness Practices at AWS" (CACM 2025) | Compare TLA+ and P on the same protocol |
| 3.4 Databases and replication | Azure Cosmos DB's consistency levels specified in TLA+ (public specs) | Read the specification; explain one consistency level from it |
| 3.5 Specs for operations | Specifying GitOps reconciliation, leader election and failover runbooks | Specify a failover runbook; find a split-brain trace |

**Check your understanding:** (1) What can a model checker prove that testing cannot, and what are its limits? (2) Why did AWS engineers find TLA+ worth the effort? (3) What is the gap between a verified spec and running code?

### Chapter 4 · Automated reasoning about configuration (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Policies | Zelkova: translating IAM policies to SMT to answer "can anyone outside my account read this?" (FMCAD 2018) | Encode a small policy language in Z3; answer an access question |
| 4.2 Networks | Tiros: reachability analysis for VPCs (CAV 2019); Batfish for router configuration (NSDI 2015) | Use Batfish to find a reachability bug in a sample network |
| 4.3 Configuration at scale | Facebook's holistic configuration management and validators (SOSP 2015) | Design a validator that would have stopped the Cloudflare 2025 file |
| 4.4 Limits of automated reasoning | What the model abstracts away (timing, partial deployment, failures), solver timeouts, keeping models in sync with reality | List three assumptions behind Zelkova or Tiros and how each could fail |

**Check your understanding:** (1) Why is "for all requests" a question only reasoning can answer? (2) What makes SMT-based analysis tractable for policies? (3) Which outage in this course would a configuration verifier have caught?

### Chapter 5 · Testing and verifying controllers (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Sieve | Testing controllers by perturbing their view of cluster state (OSDI 2022) | Present the bug classes Sieve found |
| 5.2 Acto | End-to-end testing of operators' operation correctness (SOSP 2023) | Run Acto, or a simplified variant, on a toy operator |
| 5.3 Anvil | Verifying liveness of controllers with Verus (OSDI 2024 Best Paper) | Write the liveness property for your toy operator |
| 5.4 Designing for verifiability | Small state machines, idempotent reconcile, explicit preconditions: operators that tools can reason about | Refactor your toy operator so its liveness property is easy to state |

**Check your understanding:** (1) Why are controllers hard to test with ordinary unit tests? (2) What does a liveness property say that a safety property does not? (3) What did Anvil have to assume about the environment?

### Chapter 6 · Metastability and gray failure (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Metastable failures | Trigger, sustaining effect and recovery (Bronson et al., HotOS 2021; Huang et al., OSDI 2022) | Model a retry-driven metastable system and find its stable regions |
| 6.2 Gray failure | Differential observability (Huang et al., HotOS 2017) | Propose a detector for one gray-failure case and evaluate it in simulation |
| 6.3 Implications for autonomy | Self-healing loops as sustaining effects; automation amplifying failures | Show a self-healing loop that makes a metastable failure worse |
| 6.4 Early-warning signals | Retry ratio, queue age and cache hit-rate collapse as predictors of metastable entry; evaluating detectors | Evaluate one early-warning signal on your model with precision and lead time |

**Check your understanding:** (1) How can a restart policy become a sustaining effect? (2) Why are gray failures a problem for automated remediation? (3) What should an autonomous system do when its view of the world disagrees with users' experience?

### Chapter 7 · Agentic operations research (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Visions | "Building AI Agents for Autonomous Clouds" (2024) and AIOpsLab (2025): AgentOps and its evaluation framework | Present the design principles and critique one |
| 7.2 Benchmarks | ITBench (94 scenarios), OpenRCA (335 failures), and critiques of what they measure | Reproduce one published number on a subset |
| 7.3 Evaluation validity | Realism, contamination, the gap between benchmark tasks and real incidents, cost reporting | Propose one improvement to an existing benchmark |
| 7.4 Agent architectures | Single vs multi-agent designs, tool selection, memory of past incidents; what papers report about cost | Compare two architectures from the readings on accuracy and cost |

**Check your understanding:** (1) Why can benchmark success overstate real-world ability? (2) What would a realistic RCA benchmark need? (3) How should cost be reported in agent evaluations?

### Chapter 8 · Bounded autonomy and safety (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Ironies of automation | Bainbridge (1983) and its modern versions for on-call | Write a position paragraph on skill fade |
| 8.2 Constraining actions | Policies, formal pre/postconditions, blast-radius budgets, model checking of action plans | Check an agent's proposed plan against a TLA+ or policy model before execution |
| 8.3 Learning from agent incidents | Replit (July 2025), Amazon Q extension (AWS-2025-015) | Classify each by violated principle |
| 8.4 Human-on-the-loop interfaces | Presenting plans, evidence and uncertainty for fast, correct approval; measuring approval quality | Design an approval screen and test it with two classmates under time pressure |

**Check your understanding:** (1) What does "bounded autonomy" bound, exactly? (2) Can you verify an LLM's plan without verifying the LLM? (3) Who is accountable for an approved agent action?

### Chapter 9 · Deterministic simulation and whole-system testing (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 FoundationDB | Simulation testing as the main correctness tool (SIGMOD 2021) | Present how simulation found bugs |
| 9.2 Jepsen and beyond | Black-box consistency testing; commercial deterministic testing (Antithesis) | Run a Jepsen-style test on a toy replicated store |
| 9.3 Simulation for operations | Simulating fleets, controllers and agents before production | Design a simulator for your project |
| 9.4 Trace replay | Replaying recorded traffic and events against simulated infrastructure; fidelity limits | Replay one week of synthetic traces through your simulator and compare with the original |

**Check your understanding:** (1) What does determinism buy you when a bug appears once in a million runs? (2) What can simulation never tell you? (3) How would you simulate an operations agent safely?

### Chapter 10 · Research project (weeks 11–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Proposal | Question, hypothesis, method, evaluation, threats to validity | 2-page proposal reviewed by peers |
| 10.2 Building the artefact | Reproducibility from one command; data and seeds published | Weekly progress with evidence |
| 10.3 Writing | Workshop paper structure (6 pages), related work, honest limitations | Full draft; two peer reviews |
| 10.4 Defence | Talk, questions, artefact evaluation | 20-minute talk and artefact check |

**Check your understanding:** (1) What would falsify your hypothesis? (2) Which threat to validity worries you most? (3) Could a stranger rerun your results from the README?

## Weekly rhythm

| Week | Chapter | Seminar and lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Control loops; oscillating autoscaler | Reading notes |
| 2 | 2 | Autopilot and Gandalf | Presentation 1 |
| 3 | 3 | AWS formal methods; TLA+ lab | Deploy-lock spec |
| 4 | 3 | P, Cosmos DB specs | **P1 due** |
| 5 | 4 | Zelkova, Tiros, Batfish | Z3 or Batfish exercise |
| 6 | 5 | Sieve, Acto, Anvil | Operator test results |
| 7 | 6 | Metastability and gray failure | Model; project ideas |
| 8 | 7 | Agentic operations research | Reproduction plan |
| 9 | 8 | Bounded autonomy | **P2 due** |
| 10 | 9 | Simulation testing | Proposal (P3) |
| 11 | 10 | Project work | Progress report |
| 12 | 10 | Project work | Draft paper |
| 13 | 10 | Peer review | Reviews |
| 14 | 10 | Defences | **P3 due** |
| 15 | — | Final artefact evaluation | Camera-ready paper |

## Working with AI in this course

- **Use AI for:** finding related work (then reading the actual papers); explaining unfamiliar notation; drafting TLA+ or P boilerplate; writing simulation and plotting code; critiquing your draft's clarity.
- **Do without AI (drills):** writing invariants and liveness properties; your presentations; the threats-to-validity section; peer reviews of classmates' papers. Reasoning about correctness is the skill being trained.
- **Verify AI output by:** checking every citation exists and says what is claimed; running TLC or the P checker on any AI-drafted spec and seeding a known bug to confirm the spec can catch it; reproducing any number before you use it.
- **Where AI still fails here (show it):** ask an assistant to write a TLA+ invariant for your protocol and check whether the invariant is trivially true (it can never fail) or too weak to catch your seeded bug. Ask for related work and count invented or misattributed papers. Report both in your P1 write-up.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Weekly reading notes and participation | 15% |
| Two paper presentations | 15% |
| P1 (specification) / P2 (reproduction) | 10% / 20% |
| P3 research paper, artefact and defence | 40% |

**Mastery gate.** You pass when you can: (1) present a paper from this list to the class and answer questions on its method and weaknesses; (2) write a formal specification that finds a real or seeded bug in an infrastructure protocol; (3) submit a workshop-quality paper whose artefact another student reproduces from the README alone, and whose claims survive two peer reviews.

## Industry reality

The methods in this seminar are used in industry. AWS describes TLA+, P, property-based testing, fault injection and simulation as normal correctness practice, and runs automated reasoning on customer policies and networks. Microsoft and Google publish research on safe deployment and automatic resource management. A wave of companies now sells AI operations agents, so engineers who can evaluate and constrain them are in demand. Graduates of this seminar are prepared for infrastructure research roles, staff-level reliability work, a thesis ([THS501](../../../../05_shared_years_3_to_5/THS501_thesis_or_capstone_i/README.md)) or a startup ([LCH502](../../../../05_shared_years_3_to_5/LCH502_career_launch_and_founder_studio/README.md)).

**Interview and research-discussion questions from this course**

1. *How would you make an autonomous remediation system safe?* Strong answer: narrow action set, pre/postconditions, policies and blast-radius limits enforced outside the model, approvals, kill switch, audit, simulation and shadow mode, formal checks of plans where possible, evaluation with adversarial cases.
2. *Where have formal methods paid off in infrastructure?* Strong answer: AWS TLA+ (design bugs in S3 and DynamoDB), P at AWS, Zelkova and Tiros for policy and network reasoning, Batfish, Cosmos DB specs; explains what was verified (designs, not code) and the cost.
3. *Explain metastable failures and how automation can make them worse.* Strong answer: trigger and sustaining effect; retries, cache misses and restart loops as sustaining effects; examples; mitigation by cutting the loop and shedding load.
4. *What is wrong with current AIOps benchmarks?* Strong answer: limited realism, small scale, contamination risk, single-cause labels, missing cost reporting, no safety metrics; proposes improvements.
5. *How do you test a Kubernetes operator properly?* Strong answer: state-perturbation testing (Sieve), end-to-end operation correctness (Acto), liveness specification (Anvil), crash-in-reconcile tests, idempotency, interaction with other controllers.

## Resources (free first)

**Reading list** (the core of the course):
- Burns et al., [Borg, Omega, and Kubernetes](https://queue.acm.org/detail.cfm?id=2898444) (ACM Queue, 2016).
- Rzadca et al., [Autopilot: workload autoscaling at Google scale](https://research.google/pubs/autopilot-workload-autoscaling-at-google-scale/) (EuroSys 2020).
- Li et al., [Gandalf: an intelligent, end-to-end analytics service for safe deployment in large-scale cloud infrastructure](https://www.usenix.org/conference/nsdi20/presentation/li) (NSDI 2020).
- Newcombe et al., [How Amazon Web Services Uses Formal Methods](https://lamport.azurewebsites.net/tla/formal-methods-amazon.pdf) (CACM, 2015).
- Brooker and Desai, [Systems Correctness Practices at Amazon Web Services](https://queue.acm.org/detail.cfm?id=3712057) (CACM and ACM Queue, 2025).
- Backes et al., [Semantic-based Automated Reasoning for AWS Access Policies using SMT](https://www.amazon.science/publications/semantic-based-automated-reasoning-for-aws-access-policies-using-smt) (FMCAD 2018); [Reachability Analysis for AWS-based Networks](https://www.amazon.science/publications/reachability-analysis-for-aws-based-networks) (CAV 2019); Bornholt et al., [Using Lightweight Formal Methods to Validate a Key-Value Storage Node in Amazon S3](https://www.amazon.science/publications/using-lightweight-formal-methods-to-validate-a-key-value-storage-node-in-amazon-s3) (SOSP 2021).
- Fogel et al., [A General Approach to Network Configuration Analysis](https://www.usenix.org/conference/nsdi15/technical-sessions/presentation/fogel) (Batfish, NSDI 2015).
- Tang et al., [Holistic Configuration Management at Facebook](https://research.facebook.com/publications/holistic-configuration-management-at-facebook/) (SOSP 2015).
- Sun et al., [Automatic Reliability Testing for Cluster Management Controllers](https://www.usenix.org/conference/osdi22/presentation/sun) (Sieve, OSDI 2022); [Acto](https://github.com/xlab-uiuc/acto) (SOSP 2023); Sun et al., [Anvil: Verifying Liveness of Cluster Management Controllers](https://www.usenix.org/conference/osdi24/presentation/sun-xudong) (OSDI 2024).
- Bronson et al., [Metastable Failures in Distributed Systems](https://sigops.org/s/conferences/hotos/2021/papers/hotos21-s11-bronson.pdf) (HotOS 2021); Huang et al., [Metastable Failures in the Wild](https://www.usenix.org/conference/osdi22/presentation/huang-lexiang) (OSDI 2022); Huang et al., "Gray Failure: The Achilles' Heel of Cloud-Scale Systems" (HotOS 2017).
- [Building AI Agents for Autonomous Clouds](https://arxiv.org/abs/2407.12165) (2024); [AIOpsLab](https://arxiv.org/abs/2501.06706); [ITBench](https://arxiv.org/abs/2502.05352); [OpenRCA](https://proceedings.iclr.cc/paper_files/paper/2025/file/d29b8d53678015079e1d245c023e49d2-Paper-Conference.pdf) (ICLR 2025).
- [FoundationDB: A Distributed Unbundled Transactional Key Value Store](https://www.foundationdb.org/files/fdb-paper.pdf) (SIGMOD 2021).
- Bainbridge, "Ironies of Automation", *Automatica*, 1983.

**Tools and learning:** [TLA+ home](https://lamport.azurewebsites.net/tla/tla.html), [Learn TLA+](https://learntla.com/), [TLA+ examples](https://github.com/tlaplus/Examples), [P language](https://p-org.github.io/P/), [Azure Cosmos DB TLA+ specifications](https://github.com/Azure/azure-cosmos-tla), [Batfish](https://www.batfish.org/), [Sieve](https://github.com/sieve-project/sieve), [Anvil](https://github.com/anvil-verifier/anvil), [Jepsen](https://jepsen.io/), [AIOpsLab code](https://github.com/microsoft/AIOpsLab), [ITBench code](https://github.com/itbench-hub/ITBench).

**Practice locally:** everything runs on a laptop: TLC and the P checker, Z3, Batfish in Docker, kind for operators, AIOpsLab environments.

## Sources

All checked 12 Oct 2026.
- Papers and pages as listed in the reading list (venues and years as stated; links checked).
- ITBench abstract (13.8% of SRE scenarios resolved), [arXiv 2502.05352](https://arxiv.org/abs/2502.05352).
- AWS, [DynamoDB service disruption summary](https://aws.amazon.com/message/101925/) (race condition in DNS automation, Oct 2025).
- USENIX, [Anvil](https://www.usenix.org/conference/osdi24/presentation/sun-xudong) (awarded Best Paper, OSDI 2024).
- Brooker and Desai, Systems Correctness Practices at AWS (CACM, June 2025; TLA+, P, property-based testing, fault injection, simulation), confirmed via the [ACM Queue listing](https://queue.acm.org/detail.cfm?id=3712057).

_Last reviewed: 2026-10_
