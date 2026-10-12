# FND104 · Labs and projects

Work in a Linux environment you control: native Linux, a VM, or WSL 2. Destructive commands are practised only in throwaway VMs or containers. All work is submitted as Git repositories from week 6 onward, and as signed commits from week 9.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Linux setup and Bandit 0–5 | A working Linux environment; first navigation skills | Setup notes (`uname -a`, shell, editor); Bandit level passwords replaced by the commands you used | 3 h |
| 2 · Permissions and processes | Bandit 6–12; permission puzzles; signals | 8 puzzle answers with octal modes explained; a job paused and resumed with signals, shown in a terminal recording | 4 h |
| 3 · Log pipelines | Answer real questions with pipes | One pipeline per question on the NASA HTTP logs: top 10 hosts, 404 rate, busiest hour, largest responses; each verified by a second method | 4 h |
| 4 · Safe shell scripting | A script you would trust on a server | Backup-rotation script with `--dry-run`, `set -euo pipefail`, `trap`, zero ShellCheck findings, and a Python version for comparison | 4 h |
| 5 · Git internals | See how Git stores history | A drawing of the object graph for a 4-commit repo built from `git cat-file -p` output | 3 h |
| 6 · Branches, conflicts and rescue | Merge, rebase, recover, bisect | Three resolved conflicts with green tests; a "lost" commit recovered with `reflog`; a `git bisect run` log that finds a planted regression in 200 commits | 5 h |
| 7 · Pull-request exchange | Collaborate like a team | A PR to a classmate's repo with ≥ 2 review rounds, merged under branch protection; your review comments on theirs | 3 h |
| 8 · SSH and a hardened VM | Run a remote machine safely | Key-only SSH, root and password login disabled (proof: failed password attempt), firewall rules, static site deployed with `rsync` | 4 h |
| 9 · Hooks, CI and supply chain | Automate quality gates | pre-commit config; GitHub Actions workflow with a Python version matrix and least-privilege `permissions:`; actions pinned to SHAs; three OpenSSF Scorecard findings fixed | 5 h |
| 10 · AI agent audit | Use agents without losing control | An agent run inside a container on a throwaway branch; a hunk-by-hunk review (accept, edit, reject, with reasons); three captured unsafe or wrong suggestions with the safe alternative | 4 h |

## Projects

### P1 · Dotfiles and machine bootstrap (L1, ~6 hours)

**Real-world inspiration.** Engineers keep their shell, Git and editor configuration in version control so a new laptop or cloud VM is productive in minutes; tools such as chezmoi exist for exactly this.

**What to build.** A public `dotfiles` repository with an `install.sh` that sets up your shell configuration, aliases, prompt, Git identity and defaults (`init.defaultBranch main`, SSH commit signing), editor settings and `tmux` configuration on a fresh Ubuntu machine.

**Acceptance criteria**
- Running `install.sh` on a fresh VM or container succeeds; running it a second time changes nothing (idempotent), shown by a clean `git status` and identical file hashes.
- Existing files are backed up, never overwritten silently.
- Zero ShellCheck findings; `set -euo pipefail`; a `--dry-run` mode.
- No secrets in history, checked by a gitleaks scan in CI.
- README with what it installs, how to undo it, and a screenshot of the result.

**Stretch goals.** Support macOS as well (handle BSD vs GNU tool differences); manage it with chezmoi; add a CI job that runs the installer in an Ubuntu container on every push.

**What it proves to an employer.** You can automate your own environment safely and repeatably, the first step towards infrastructure as code.

### P2 · `logscope`: log report tool with tests and CI (L2, ~15 hours)

**Real-world inspiration.** On-call engineers answer "what is happening to this server?" from access logs under time pressure; tools such as GoAccess and every observability platform start from the same parsing and aggregation.

**What to build.** A command-line tool (Bash for orchestration, `awk`/Python for heavy lifting) that reads web-server access logs in Common or Combined Log Format, plain or gzipped, and writes a Markdown report: requests per hour, status-code distribution, top paths and clients, 4xx and 5xx error rates, largest responses, and suspicious patterns (for example, one client hitting many distinct 404 paths).

**Acceptance criteria**
- Correct results on a hand-made fixture log whose answers you computed by hand, and on the NASA HTTP July 1995 log (record your numbers in the README and cross-check two of them with a second method).
- Processes 1 GB of logs in under 60 seconds on a typical laptop (measured, with machine stated).
- ≥ 25 tests using bats-core (shell) and `pytest` (Python parts).
- CI on GitHub Actions: ShellCheck, `ruff`, tests; required to pass before merge on a protected `main`.
- Released as `v1.0.0` with a Git tag, Semantic Versioning, and a `CHANGELOG.md` in Keep a Changelog format.
- Malformed lines are counted and reported, never crash the tool.

**Stretch goals.** A `--since` time filter; JSON output for dashboards; a `systemd` timer or cron entry that emails or saves the daily report; package it for installation with `uv tool install`.

**What it proves to an employer.** You can build a practical operations tool, test shell code, and ship releases through CI like a professional team.

### P3 · Ship it like a team (L3, portfolio-grade, ~30 hours per person)

**Real-world inspiration.** Mature open-source projects run on protected branches, review rules, CI gates and written contribution processes; the xz incident and GitLab's 2017 outage show what happens when trust or verification is missing.

**What to build.** In a team of 3–4, adopt one member's FND101 project (P2 or P3) and run it as a real open-source project for four weeks:
- Repository hygiene: `README`, `CONTRIBUTING.md`, code of conduct, licence, issue and PR templates, `CODEOWNERS`, `AGENTS.md` with rules for AI agents.
- Process: protected `main`, one approving review required, Conventional Commits, squash merges, signed commits.
- Automation: CI with lint, tests on three Python versions, a coverage threshold, Dependabot, actions pinned to SHAs, least-privilege tokens.
- Security: OpenSSF Scorecard run with at least three findings fixed and documented; secret scanning and push protection enabled.
- An incident drill: one member (announced to the instructor, not the team) deletes a branch or force-pushes over `main` on a copy; the team detects it, recovers with `reflog` or a clone, and writes a blameless postmortem (timeline, impact, cause, actions).
- Upstream: each member opens one PR to an external open-source project and links it.

**Acceptance criteria**
- Each member authors ≥ 5 merged PRs and leaves ≥ 5 substantive reviews; the Git history shows it.
- No direct pushes to `main` after day 1 (verifiable from branch protection and history).
- CI is green on `main` at the end; median PR review time is reported from the GitHub data.
- At least one PR was produced mainly by an AI agent, with the human review visible in the PR conversation and at least one requested change.
- Postmortem is published in the repository; all action items are either done or have an issue.
- Final 10-minute demo plus a live AI-off task: the examiner asks you to resolve a conflict and bisect a bug in your repo.

**Stretch goals.** Publish the package to TestPyPI from a tagged release using trusted publishing; add SLSA provenance; get an upstream PR merged.

**What it proves to an employer.** You already work the way professional teams work: reviewed changes, automated gates, secure defaults, recovery from mistakes, and controlled use of AI agents.

## Feeds into

- [CS205 Software Engineering I](../../../02_year_2_core_computer_science/semester_3/CS205_software_engineering_i_design_testing/README.md): team process, reviews and CI become the default for all projects.
- [CS215 Cloud and DevOps Foundations](../../../02_year_2_core_computer_science/semester_4/CS215_cloud_and_devops_foundations/README.md) and [CS204 Computer Networks](../../../02_year_2_core_computer_science/semester_3/CS204_computer_networks/README.md): SSH, VMs and automation extend to cloud infrastructure.
- [FND114 Web Foundations](../../semester_2/FND114_web_foundations_http_html_css_and_javascript/README.md): deploying sites built in semester 2.
- [CAR301 Career Lab I](../../../05_shared_years_3_to_5/CAR301_career_lab_i_dsa_mastery_portfolio_and_open/README.md): sustained open-source contribution.
- The [DevOps, SRE and Platform Engineering major](../../../03_majors/devops_sre_platform_engineering/README.md) and the [DevSecOps overlap](../../../04_overlaps/OV03_devsecops/README.md).
