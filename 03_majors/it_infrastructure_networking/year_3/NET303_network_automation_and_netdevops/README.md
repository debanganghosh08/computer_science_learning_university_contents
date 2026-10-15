# NET303 · Network Automation and NetDevOps

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 5 | 4 (≈ 120 hours) | L1 → L3 | [CS204](../../../../02_year_2_core_computer_science/semester_3/CS204_computer_networks/README.md), [CS203](../../../../02_year_2_core_computer_science/semester_3/CS203_operating_systems/README.md); [FND101](../../../../01_year_1_foundations/semester_1/FND101_programming_i_computational_thinking_with_python/README.md) Python is assumed | [NET403](../../year_4/NET403_aiops_and_intent_based_networking/README.md); best taken with [NET301](../NET301_routing_and_switching/README.md) |

## Why this course matters now

A network engineer who logs in to 400 switches one by one is now the most automatable person on the team. The US Bureau of Labor Statistics names automation of routine work as one reason system administrator jobs are projected to shrink 4% from 2025 to 2035, while network architect jobs grow 8%. Vendors are building agents into their controllers: in February 2026 Cisco announced "risk-aware agentic assessments" that validate network changes against live topology, configuration and telemetry. Cisco also renamed its programmability certifications to CCNA Automation and CCNP Automation. But automation multiplies mistakes as fast as it multiplies work. On 19–20 October 2025, a latent race condition in the automation that manages DynamoDB's DNS records in AWS us-east-1 left the regional endpoint with an empty DNS record for about three hours of API errors. On 18 November 2025, a database permissions change made a machine-generated Cloudflare configuration file double in size and crash the proxy software; Cloudflare's fix was to treat its own generated files like untrusted user input. AI assistants write Netmiko scripts and Ansible playbooks well, but benchmarks such as NetConfEval (2024) show that generating correct low-level configuration is still hard even for large models. This course teaches the discipline that makes automation safe: a source of truth, model-driven interfaces, tests before deployment, and staged rollout with rollback.

## Learning outcomes

By the end you can:

1. **Write** Python tools that configure and audit multi-vendor devices over SSH with Netmiko or Scrapli, and **parse** command output into structured data.
2. **Build** Nornir and Ansible workflows that are idempotent, run in check mode with diffs, and handle partial failure.
3. **Read** YANG models and **configure** devices through NETCONF and RESTCONF, using candidate datastores and confirmed commits.
4. **Stream** telemetry with gNMI into a time-series database and **compare** it with SNMP polling for timeliness and load.
5. **Model** a network in NetBox as the source of truth and **generate** device configurations and drift reports from it.
6. **Test** changes before deployment with Batfish and pyATS, and **write** pre- and post-change checks that fail loudly.
7. **Run** a CI/CD pipeline for network changes that lints, renders, tests in a Containerlab topology, waits for approval and deploys in canary stages.
8. **Evaluate** an AI assistant on network-automation tasks and **design** guardrails so it can propose but not silently apply changes.

## Chapters and lessons

### Chapter 1 · Why automate, and the NetDevOps model (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 The cost of manual work | Toil, configuration drift, "snowflake" devices, change failure rate; what to automate first (read-only audits) | Estimate the hours a 400-switch password change takes by hand vs scripted |
| 1.2 Three generations of interfaces | Screen scraping the CLI, vendor REST APIs, model-driven interfaces (NETCONF, RESTCONF, gNMI) | Make the same read on one device through CLI, REST and NETCONF |
| 1.3 The pipeline | Source of truth → intended configuration → validation → deployment → verification → telemetry | Draw the pipeline you will build this semester |
| 1.4 The lab | Containerlab with Nokia SR Linux, Arista cEOS and FRRouting; Cisco DevNet always-on sandboxes; Python virtual environments and Git | Bring up a 6-node multi-vendor topology from a YAML file |

**Check your understanding:** Why should the first automation in a new team be read-only? Why does screen scraping break when a vendor upgrades its software? What is the difference between automating a task and automating a process?

### Chapter 2 · Python for network engineers (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Data first | Lists, dicts, YAML and JSON; modelling interfaces, VLANs and neighbours as data | Convert a spreadsheet of VLANs into validated YAML |
| 2.2 Templates | Jinja2 loops, conditionals, filters, macros; separating data from templates | Render configurations for 3 vendors from one data file |
| 2.3 Validation | The `ipaddress` module, Pydantic models for input data, failing early | Reject a data file with an overlapping subnet and a VLAN ID of 4095 |
| 2.4 Concurrency | Threads vs asyncio for I/O-bound device work; rate limits; timeouts | Collect `show version` from 50 simulated devices in under 30 seconds |
| 2.5 Logging and errors | Structured logs, retries with back-off, never swallowing exceptions | Make a collector that reports which devices failed and why |

**Check your understanding:** Why is validating input data more important than validating the rendered configuration? Why do threads help for SSH sessions even with Python's global interpreter lock? What should a script do when 3 of 200 devices time out?

### Chapter 3 · CLI automation and parsing (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Netmiko and Scrapli | SSH sessions, prompts, `send_command`, `send_config_set`, privilege modes, timing problems | Push an NTP and syslog configuration to every lab device |
| 3.2 Parsing output | TextFSM with ntc-templates, Cisco Genie parsers, TTP; why regex alone does not last | Turn `show ip interface brief` from 3 platforms into one table |
| 3.3 Audits | Compliance checks: required lines, forbidden lines, golden-configuration comparisons | Report every device missing SNMPv3 or with Telnet enabled |
| 3.4 Credentials | Never in code; environment variables, a vault, per-user accounts with AAA logging | Move your scripts' credentials to a vault and prove Git history is clean |

**Check your understanding:** Why does a missing prompt pattern make a Netmiko script hang? Why prefer a maintained template library to your own regex? Why should automation run with named accounts rather than one shared "automation" password?

### Chapter 4 · Abstraction with NAPALM and Nornir (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 NAPALM getters | Vendor-neutral `get_facts`, `get_interfaces`, `get_bgp_neighbors`, `get_lldp_neighbors` | Build an inventory report across 3 vendors with one code path |
| 4.2 Configuration replace vs merge | `load_merge_candidate`, `load_replace_candidate`, `compare_config`, `commit_config`, `rollback` | Replace a full configuration; show the diff before committing |
| 4.3 Nornir | Inventory, tasks, threaded runs, results and failed hosts, plugins | Port your Chapter 3 audit to Nornir and compare run time |
| 4.4 Partial failure | What happens when device 37 fails mid-run; idempotent retries; stop-on-failure thresholds | Inject failures and make the run stop after 5% of devices fail |

**Check your understanding:** Why is configuration replace safer than merge for a device fully described by your source of truth, and riskier for one that is not? What does NAPALM have to do differently on IOS vs Junos to offer rollback? Why is a failure threshold better than "continue on error"?

### Chapter 5 · Ansible for networks (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 How Ansible talks to network devices | `network_cli`, `netconf` and `httpapi` connections; collections such as `cisco.ios`, `arista.eos`, `junipernetworks.junos`, `ansible.netcommon` | Gather facts from all lab devices |
| 5.2 Resource modules | States `merged`, `replaced`, `overridden`, `deleted`, `gathered`, `rendered`; why `overridden` is powerful and dangerous | Manage VLANs with `overridden`; show what it removes |
| 5.3 Check mode and diff | `--check --diff`, idempotence as a test: second run must report no changes | A CI job that fails if a second run changes anything |
| 5.4 Structure | Inventories, group variables, roles, Ansible Vault | Turn a single playbook into a role used by 3 sites |

**Check your understanding:** Why is a second run with zero changes the simplest test of a playbook? When would `replaced` be right and `overridden` wrong? Why does check mode not guarantee the real run will succeed?

### Chapter 6 · YANG, NETCONF and RESTCONF (weeks 6–7)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 YANG | Modules, containers, lists, leaves, types, `must` and `when` constraints (RFC 7950); OpenConfig vs vendor-native models | Read the OpenConfig interfaces model with `pyang -f tree` |
| 6.2 NETCONF | RPCs over SSH (RFC 6241, RFC 6242), `get-config`, `edit-config`, datastores (running, candidate, startup), `validate`, `confirmed-commit` | Change an interface through the candidate datastore with ncclient |
| 6.3 Transactions | Network-wide transactions, locking, rollback on error; why the CLI cannot give you this | Apply a change to 3 devices; abort all if one fails |
| 6.4 RESTCONF | HTTP access to the same models (RFC 8040), JSON encoding | Read and update a device with `curl` and Python `requests` |
| 6.5 Choosing models | Coverage gaps in OpenConfig, mixing native and OpenConfig models, deviations | Find a feature your platform supports only in its native model |

**Check your understanding:** What does a candidate datastore give you that a running-only device cannot? Why can a YANG `must` statement catch errors before a device applies them? When would you choose RESTCONF over NETCONF?

### Chapter 7 · gNMI and streaming telemetry (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Polling vs streaming | SNMP polling intervals, load and blind spots; streaming subscriptions | Compare a 5-minute SNMP poll with 10-second streaming on a flapping link |
| 7.2 gNMI | `Capabilities`, `Get`, `Set`, `Subscribe`; sample vs on-change subscriptions; paths and encodings | Subscribe to interface counters and BGP state with gnmic |
| 7.3 The pipeline | Collector (gnmic or Telegraf) → time-series database (Prometheus or InfluxDB) → Grafana; cardinality | Build a dashboard of interface errors and BGP sessions for the lab |
| 7.4 Flow and routing data | IPFIX (RFC 7011), sFlow, BGP Monitoring Protocol (RFC 7854); what each is good for | Export flows from a lab router and find the top talker |

**Check your understanding:** Why can a 5-minute poll miss a problem that users felt? Why is on-change better than sampling for BGP session state? What makes high-cardinality labels expensive in a time-series database?

### Chapter 8 · Source of truth with NetBox (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Why a source of truth | Intended state vs actual state; one authoritative place per fact | List every place your lab's VLANs are currently "documented" |
| 8.2 NetBox data model | Sites, racks, devices, interfaces, cables, IPAM (prefixes, VLANs, VRFs), circuits, custom fields, config contexts | Model the whole lab in NetBox |
| 8.3 APIs | REST and GraphQL APIs, pynetbox, webhooks and event rules | Generate a Nornir inventory from NetBox |
| 8.4 Configurations from data | Render full device configurations from NetBox plus templates; config templates in NetBox | Regenerate every lab configuration and diff against the running devices |
| 8.5 Drift | Detect and report devices that differ from intent; deciding whether to fix the device or the data | A nightly drift report with a list of differences per device |

**Check your understanding:** Why must a source of truth be authoritative for each fact it holds, and not just a copy? When drift is found, how do you decide which side is wrong? Why do many teams keep NetBox and the configuration templates in separate systems?

### Chapter 9 · Testing network changes (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Pre- and post-checks | pyATS and Genie `learn` and `diff`: snapshot routing tables, neighbours and interfaces before and after | Snapshot the lab, make a change, and show exactly what moved |
| 9.2 Batfish | Analysing configurations without devices: reachability, ACL and firewall analysis, BGP session compatibility, differential analysis between snapshots (Fogel et al., NSDI 2015) | Prove a proposed ACL change blocks only what was intended |
| 9.3 Template unit tests | Tests on rendered output: required lines present, forbidden lines absent, syntax check on a virtual device | 10 tests for your Jinja2 templates |
| 9.4 Digital twin lite | A Containerlab copy of production topology built from NetBox; running the change there first | Build the twin automatically from NetBox data |

**Check your understanding:** What can Batfish find that a post-change ping test cannot, and what can it not find? Why must a test fail when the network is wrong, not just pass when it is right? What makes a lab twin differ from production in ways that matter?

### Chapter 10 · CI/CD for the network (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Git workflow | Branches, pull requests, code owners, review checklists for network changes | Submit a VLAN change as a pull request with a reviewer |
| 10.2 The pipeline | Lint (yamllint, ansible-lint), render, Batfish checks, deploy to the Containerlab twin, pyATS tests, approval gate | Build it in GitHub Actions or GitLab CI |
| 10.3 Deployment strategies | Canary devices, waves by site, maintenance windows, automatic halt on failed post-checks | Deploy to one canary, then waves of 10%, 40%, 50% with halt rules |
| 10.4 Rollback | NETCONF confirmed-commit, NAPALM rollback, Git revert plus redeploy; testing rollback in the pipeline | Break a deployment on purpose; prove automatic rollback restores the previous state |

**Check your understanding:** Why should the approval gate come after the automated tests rather than before? What decides the size of the first deployment wave? Why is "revert the commit" not enough on its own to roll back a network change?

### Chapter 11 · Safe automation at scale (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Blast radius | Limiting what one run can touch; per-run device caps; separating read and write credentials | Add a hard cap of 20 devices per run unless an override is approved |
| 11.2 Generated data is input | Cloudflare's November 2025 lesson: validate size, schema and sanity of machine-generated files before use | Add schema and size checks to every generated artifact in your pipeline |
| 11.3 Races and ordering | AWS's October 2025 DNS automation race; locking, versioning and "never apply an older plan over a newer one" | Make two pipeline runs collide in the lab; add a lock |
| 11.4 Kill switches and observability | Feature flags, a stop button, run logs and change records linked to telemetry | Show a dashboard annotation for every automated change |

**Check your understanding:** Why did a file generated by Cloudflare's own systems need the same validation as user input? What property of the AWS DNS automation let an older plan delete a newer one? What is the smallest change to your pipeline that would most reduce blast radius?

### Chapter 12 · AI in network automation (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 What assistants do well | Drafting scripts, templates, tests and YANG queries; explaining unfamiliar output | Have an assistant draft a Nornir task; review it like a pull request |
| 12.2 What the research shows | Mondal et al. (2023): GPT-4 router configurations had "egregious errors" until verifiers fed back localised errors; NetConfEval (CoNEXT 2024): low-level configuration generation needs the largest models and still fails often | Run 20 tasks from your own benchmark with an assistant; score pass/fail with Batfish and lab tests |
| 12.3 Tools for assistants | Model Context Protocol (MCP) servers that expose NetBox, Batfish or read-only device commands to an assistant | Give an assistant read-only access to the lab through a small tool server |
| 12.4 Guardrails | Read-only by default; changes only as pull requests through the same pipeline; human approval; logs of every tool call | Let the assistant propose a fix to a planted fault; it must pass the pipeline to deploy |

**Check your understanding:** Why is "the assistant can only open pull requests" a stronger guardrail than "the assistant asks before running commands"? Which task in your benchmark did the assistant fail most, and why? What evidence would make you allow an assistant to apply a change on its own?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Multi-vendor Containerlab and Git | — |
| 2 | 2 | Lab 2 · Data, templates and validation | — |
| 3 | 3 | Lab 3 · Netmiko audit and parsing | **P1 due** |
| 4 | 4 | Lab 4 · NAPALM and Nornir | — |
| 5 | 5 | Lab 5 · Ansible resource modules and idempotence | — |
| 6 | 6 | Lab 6 · NETCONF transactions | — |
| 7 | 6 | Lab 6 (cont.) and RESTCONF | Mid-term (AI off) |
| 8 | 7 | Lab 7 · gNMI telemetry pipeline | — |
| 9 | 8 | Lab 8 · NetBox source of truth and drift | **P2 due** |
| 10 | 9 | Lab 9 · Batfish and pyATS testing | — |
| 11 | 10 | Lab 10 · CI/CD with canary and rollback | — |
| 12 | 11 | Safety controls added to the pipeline | — |
| 13 | 12 | AI benchmark and guardrails | AI evaluation report |
| 14 | 12 | P3 | **P3 due** |
| 15 | Review | Oral defence of P3 | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** first drafts of Python, Jinja2, Ansible and Batfish queries; explaining a YANG tree or a pyATS diff; writing test cases you then check; generating Containerlab topologies. GitHub Copilot, Claude Code, Cursor and ChatGPT all work here; Cisco AI Assistant and similar vendor tools appear inside controllers.
- **Do without AI (drills):** writing a Netmiko audit from a blank file; reading a YANG tree; writing a NETCONF `edit-config` by hand; designing the pipeline's stages and halt rules; the mid-term and final.
- **Verify AI output by:** running it against the Containerlab twin, never production; idempotence (second run shows no change); Batfish differential analysis; pyATS before/after diffs; reading the module or library documentation for every parameter; reviewing the diff, not the script.
- **Where AI still fails here:** assistants mix NAPALM, Netmiko and Ansible APIs from different versions, invent module parameters, and generate vendor syntax that looks right and is rejected (or, worse, accepted with a different meaning). The research above shows the same in controlled tests. Your Chapter 12 benchmark is the evidence you keep: 20 tasks, scored by tests, with each failure classified.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1–P3 | 35% |
| Mid-term (AI off) | 10% |
| Final exam (AI off) + P3 oral defence | 30% |

**Mastery gate.** You pass when you can, without AI: (1) write a Nornir or Netmiko tool in 60 minutes that audits 20 devices for 5 compliance rules and reports failures as structured data; (2) make a change through NETCONF's candidate datastore with a confirmed commit and demonstrate automatic rollback; (3) given a pipeline and a proposed change, find the planted defect (in data, template or policy) using Batfish or tests within 30 minutes.

## Industry reality

Where this is used: service providers, cloud and hyperscale operators, banks and large enterprises run network changes through pipelines; NetBox is widely used as an open-source source of truth; Cisco, Juniper (now part of HPE since July 2025), Arista and Nokia all expose model-driven interfaces. Public incident reports from AWS (October 2025) and Cloudflare (November 2025) show that automation failures now cause the largest outages, which is why testing and staged rollout are part of the job, not extras. Cisco's CCNA Automation and CCNP Automation certifications cover this ground.

**Interview questions from this course**

1. *How would you change the SNMP community on 2,000 devices from 4 vendors?* Strong answer: inventory from the source of truth, read-only audit first, templated change per platform, check mode and diff, canary then waves with halt rules, post-checks, rollback, credentials in a vault, change record.
2. *NETCONF, RESTCONF or gNMI: which and why?* Strong answer: NETCONF for transactional configuration with candidate datastores; RESTCONF for simple HTTP integration; gNMI for streaming telemetry and also configuration where supported; model coverage decides in practice.
3. *What is idempotence and how do you test it?* Strong answer: running twice gives the same state and the second run reports no changes; tested in CI; explains why CLI scripts often are not idempotent.
4. *Your automation pushed a bad ACL to 50 sites. What now, and what do you change afterwards?* Strong answer: stop the run, roll back with tested method, verify, communicate; then add Batfish checks, smaller waves, automatic halt on post-check failure, and a review of why tests passed.
5. *Should an AI agent be allowed to change production network configuration?* Strong answer: separates read from write; proposes via pull requests through the same tests and approvals; cites evidence of failure rates; logs every action; defines the measured conditions under which autonomy could grow.

## Resources (free first)

- **Libraries and tools:** Netmiko — https://github.com/ktbyers/netmiko ; Scrapli — https://github.com/carlmontanari/scrapli ; NAPALM — https://napalm.readthedocs.io/ ; Nornir — https://nornir.readthedocs.io/ ; ntc-templates — https://github.com/networktocode/ntc-templates ; Ansible network automation docs — https://docs.ansible.com/ansible/latest/network/index.html ; ncclient — https://github.com/ncclient/ncclient ; pyang — https://github.com/mbj4668/pyang ; gnmic — https://gnmic.openconfig.net/ ; NetBox — https://netboxlabs.com/docs/netbox/ ; Batfish — https://batfish.org/ ; pyATS — https://developer.cisco.com/docs/pyats/ ; Containerlab — https://containerlab.dev/
- **Free practice:** Cisco DevNet sandboxes — https://developer.cisco.com/site/sandbox/ ; SR Linux learning site — https://learn.srlinux.dev/
- **Standards:** RFC 7950 (YANG 1.1), RFC 6241 (NETCONF), RFC 6242 (NETCONF over SSH), RFC 8040 (RESTCONF), RFC 7011 (IPFIX), RFC 7854 (BMP) — https://www.rfc-editor.org/ ; OpenConfig and gNMI specification — https://www.openconfig.net/
- **Papers:** Fogel et al., "A General Approach to Network Configuration Analysis" (NSDI 2015) — https://www.usenix.org/conference/nsdi15/technical-sessions/presentation/fogel ; Mondal et al. (2023) — https://arxiv.org/abs/2307.04945 ; NetConfEval code and data — https://github.com/NetConfEval/NetConfEval
- **Paid, optional:** Oswalt, Adell, Lowe and Edelman, *Network Programmability and Automation*, 2nd ed. (O'Reilly).

## Sources

- BLS Occupational Outlook Handbook (administrators −4%, architects +8%, 2025–35) — https://www.bls.gov/ooh/computer-and-information-technology/network-and-computer-systems-administrators.htm ; https://www.bls.gov/ooh/computer-and-information-technology/computer-network-architects.htm (checked 2026-10)
- Cisco newsroom, "Cisco Expands AgenticOps Innovations Across Portfolio" (10 Feb 2026) — https://newsroom.cisco.com/content/r/newsroom/en/us/a/y2026/m02/cisco-expands-agenticops-innovations-across-portfolio.html (checked 2026-10)
- Cisco certifications page (CCNA Automation, CCNP Automation) — https://www.cisco.com/site/us/en/learn/training-certifications/certifications/index.html (checked 2026-10)
- AWS, "Summary of the Amazon DynamoDB Service Disruption in the Northern Virginia (US-EAST-1) Region" (Oct 2025) — https://aws.amazon.com/message/101925/ (checked 2026-10)
- Cloudflare, "Cloudflare outage on November 18, 2025" — https://blog.cloudflare.com/18-november-2025-outage/ (checked 2026-10)
- Wang et al., "NetConfEval: Can LLMs Facilitate Network Configuration?", Proc. ACM Netw. 2, CoNEXT2 (Jun 2024) — https://github.com/NetConfEval/NetConfEval (checked 2026-10)
- Mondal et al., arXiv 2307.04945 (Jul 2023) — https://arxiv.org/abs/2307.04945 (checked 2026-10)
- HPE, closing of the Juniper Networks acquisition (2 Jul 2025) — https://www.hpe.com/us/en/newsroom/press-release/2025/07/hewlett-packard-enterprise-closes-acquisition-of-juniper-networks-to-offer-industry-leading-comprehensive-cloud-native-ai-driven-portfolio.html (checked 2026-10)

_Last reviewed: 2026-10_
