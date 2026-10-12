# FND104 · The Developer's Toolkit: Linux, Shell, Git and GitHub

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 1 · 1 | 4 (≈ 120 hours) | L0 → L2 | none | [FND114](../../semester_2/FND114_web_foundations_http_html_css_and_javascript/README.md), [CS204](../../../02_year_2_core_computer_science/semester_3/CS204_computer_networks/README.md), [CS205](../../../02_year_2_core_computer_science/semester_3/CS205_software_engineering_i_design_testing/README.md), [CS215](../../../02_year_2_core_computer_science/semester_4/CS215_cloud_and_devops_foundations/README.md) |

## Why this course matters now

Software is built in terminals, versioned in Git and shipped through pull requests and CI. GitHub reported more than 180 million developers and 630 million repositories in October 2025, with India adding over 5 million developers that year and now having the largest open-source contributor base. AI coding agents (Claude Code, OpenAI Codex, Gemini CLI, GitHub Copilot's coding agent) now work in exactly this environment: they run shell commands, edit files and open pull requests, and MIT's 2026 "Missing Semester" added a lecture on agentic coding for that reason. That raises the bar for the human: you must read every command an agent proposes, review its diffs, contain it with branches and sandboxes, and undo damage with Git when it goes wrong. The 2024 xz backdoor (CVE-2024-3094), caught by an engineer who noticed `sshd` using too much CPU, showed that this toolkit is also where supply-chain security begins.

## Learning outcomes

By the end you can:

1. Work fluently in a Linux shell: navigate, manage files, permissions and processes, and read `man` pages.
2. Combine `grep`, `sed`, `awk`, `sort`, `uniq`, `jq` and pipes to answer questions about large text files.
3. Write safe, ShellCheck-clean Bash scripts with quoting, exit codes and `set -euo pipefail`, and know when to switch to Python.
4. Explain Git's data model (blobs, trees, commits, refs) and use it to branch, merge, rebase, bisect and recover lost work.
5. Collaborate on GitHub: SSH keys, forks, pull requests, reviews, protected branches, issues and the `gh` CLI.
6. Administer a remote Linux machine over SSH with key-only login and deploy files with `rsync`.
7. Automate checks with pre-commit hooks and GitHub Actions, and apply basic supply-chain hygiene (pinning, least-privilege tokens, Dependabot).
8. Make a first contribution to a real open-source project following its contribution guide.
9. Run an AI coding agent inside a branch or sandbox, review its changes hunk by hunk, and revert safely.

## Chapters and lessons

### Chapter 1 · The terminal and Linux (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Terminal, shell, OS | Terminal emulator vs shell (Bash, Zsh) vs kernel; why servers are run from the command line. | Set up Ubuntu LTS natively, in a VM, or with WSL 2 on Windows; record `uname -a`. |
| 1.2 Navigation | `pwd`, `ls -la`, `cd`, absolute vs relative paths, `~`, `.` and `..`, tab completion, history search (`Ctrl+R`). | Navigate a provided directory maze using only the keyboard. |
| 1.3 The file system layout | Filesystem Hierarchy Standard: `/etc`, `/var/log`, `/usr/bin`, `/home`, `/tmp`. | Find where your system keeps its logs, its config and its programs. |
| 1.4 Getting help | `man` (sections, searching with `/`), `--help`, `tldr`, explainshell.com, `apropos`. | Answer 10 questions about `ls` and `find` using only `man`. |
| 1.5 Wargames | Learning by solving puzzles in a legal practice environment. | OverTheWire Bandit levels 0–5. |

**Check your understanding:** (1) Why does `cd` have to be built into the shell rather than be a separate program? (2) What is the difference between `/home/you/notes` and `notes`? (3) Where do you look first when a command's behaviour surprises you?

### Chapter 2 · Files, permissions and processes (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Working with files | `cp`, `mv`, `rm` (no undo), `mkdir -p`, globbing (`*`, `?`, `{a,b}`), `find` with `-name`, `-mtime`, `-exec`. | Find and list every `.log` file over 10 MB modified in the last 7 days. |
| 2.2 Permissions | Users, groups, `rwx` for user/group/other, octal modes, `chmod`, `chown`, `umask`, the execute bit on directories. | Solve 8 permission puzzles; explain why `chmod 777` is a smell. |
| 2.3 sudo and least privilege | Root, `sudo`, why you run as an ordinary user; the GitLab 2017 outage where a deletion ran on the wrong database server. | Read GitLab's postmortem; list three safeguards that would have helped. |
| 2.4 Processes and signals | `ps aux`, `top`/`htop`, `kill` with `SIGTERM` vs `SIGKILL`, jobs, `&`, `fg`/`bg`, `nohup`. | Start, pause, resume and stop a long-running job; explain each signal. |
| 2.5 Disks | `df -h`, `du -sh`, finding what fills a disk. | Bandit levels 6–12. |

**Check your understanding:** (1) Why should you prefer `SIGTERM` before `SIGKILL`? (2) What lets a user list a directory but not read the files inside? (3) What habit would have prevented the GitLab deletion from hitting the wrong host?

### Chapter 3 · Text, pipes and data (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Streams | stdin, stdout, stderr; `>`, `>>`, `2>`, `2>&1`, `\|`; the Unix philosophy of small composable tools. | Separate a program's output and errors into two files. |
| 3.2 Searching | `grep` with `-i -v -c -r -E`; regular expressions; `ripgrep` for code. | Find all failed SSH logins in an auth log. |
| 3.3 Transforming | `cut`, `sort`, `uniq -c`, `wc`, `head`, `tail -f`, `tr`, `sed` substitutions, `awk` fields and sums. | Top 10 client IPs and status-code counts from a web-server log. |
| 3.4 Structured data | `jq` for JSON; `xargs` for building commands; `column` for tables. | Extract fields from a JSON API response saved to a file. |
| 3.5 Real logs | Using the NASA HTTP access logs (1995, public) as a large realistic dataset. | Requests per hour and the 10 most requested paths, as one pipeline each. |

**Check your understanding:** (1) Why does `sort | uniq -c` need the `sort`? (2) Where does stderr go in `cmd > out.txt`, and why? (3) When does a 3-line `awk` pipeline beat a 30-line Python script, and when does it lose?

### Chapter 4 · Shell scripting (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Scripts | Shebang, executable bit, arguments (`$1`, `$@`), variables, exit codes and `$?`. | A script that greets each argument and fails with code 2 when given none. |
| 4.2 Quoting | Word splitting and globbing, the reason most shell bugs exist; always `"$var"`. | Break a script with a file name containing spaces; fix it. |
| 4.3 Control flow | `if`, `[[ ]]`, `case`, `for`, `while read`, functions, `local`. | Rotate backups: keep the newest 7 archives of a folder. |
| 4.4 Safety | `set -euo pipefail`, `trap` for cleanup, dry-run flags, echoing before deleting; ShellCheck. | Make the backup script ShellCheck-clean and add `--dry-run`. |
| 4.5 Shell or Python? | Rules of thumb: under ~50 lines of glue, shell; data structures or error handling, Python. | Rewrite the backup script in Python; compare clarity and failure handling. |

**Check your understanding:** (1) What can `rm -rf "$DIR/"*` do if `DIR` is empty and `set -u` is missing? (2) Why does `pipefail` matter for `curl … | tar x`? (3) What does ShellCheck catch that testing might not?

### Chapter 5 · Environment, packages and editors (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Environment variables | `PATH`, `HOME`, `export`, `.bashrc`/`.zshrc`, why "command not found" happens. | Add a personal `~/bin` to `PATH`; explain the order of lookup. |
| 5.2 Package managers | `apt`, Homebrew, `winget`; language managers (`uv` for Python); versions and lockfiles; checking package names against typosquatting. | Install, pin and remove a tool; record exactly what changed. |
| 5.3 Editors | VS Code (extensions, integrated terminal, debugger, Remote-SSH); Vim's modal editing (`vimtutor`); Neovim. | Finish `vimtutor`; edit a config file on a server with Vim. |
| 5.4 Terminal multiplexing | `tmux` sessions, windows and panes; surviving disconnects. | Run a long job in `tmux` on a remote machine, disconnect, reattach. |
| 5.5 Dotfiles | Keeping configuration in Git; idempotent install scripts; tools such as chezmoi. | Start your dotfiles repository (Project P1). |

**Check your understanding:** (1) Two versions of `python` are installed; which one runs, and how do you prove it? (2) Why is a lockfile part of reproducibility? (3) Why should an install script be safe to run twice?

### Chapter 6 · Git fundamentals (weeks 6–7)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Why version control | History, collaboration, blame, revert; snapshots, not diffs. | Recover a deleted paragraph from a 10-commit history. |
| 6.2 The data model | Blobs, trees, commits as a DAG, content hashes (SHA-1 today; Git 3.0 plans SHA-256 for new repositories), refs, `HEAD`. | Inspect `.git/objects` with `git cat-file -p`; draw the object graph. |
| 6.3 Daily workflow | `init`, `status`, `add` (the staging area), `commit`, `diff`, `diff --staged`, `log --oneline --graph`. | Stage part of a file with `git add -p`. |
| 6.4 Good commits | Atomic commits, message format (summary line, body explaining why), Conventional Commits. | Rewrite 5 bad commit messages. |
| 6.5 What never to commit | `.gitignore`, secrets, large binaries; GitHub push protection and secret scanning. | Set up `.gitignore` from the github/gitignore templates; scan a repo with gitleaks. |

**Check your understanding:** (1) Why do two identical files in different folders share one blob? (2) What does the staging area let you do that committing everything cannot? (3) You committed a password but have not pushed; what are your options?

### Chapter 7 · Branching, merging and recovery (weeks 7–8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Branches | A branch is a movable pointer; `switch`, `branch`, detached `HEAD`. | Create, switch and delete branches; watch the refs change in `.git`. |
| 7.2 Merging | Fast-forward vs three-way merge, merge conflicts, conflict markers, resolving and testing. | Resolve three staged conflicts, running tests after each. |
| 7.3 Rebasing | Replaying commits, interactive-free rebase, the rule: never rewrite history others have pulled. | Rebase a feature branch onto an updated `main`; compare history shapes. |
| 7.4 Undoing | `restore`, `reset --soft/--mixed/--hard`, `revert`, `stash`, `cherry-pick`; `reflog` as the safety net. | Recover a "lost" commit after a hard reset using `reflog`. |
| 7.5 Finding bugs | `git bisect` with a test script; `git blame`, `git log -S`. | Bisect a regression planted somewhere in 200 commits; automate it with `git bisect run`. |

**Check your understanding:** (1) Why is `revert` safe on a shared branch but `reset --hard` is not? (2) What exactly is lost after `reset --hard`, and for how long can `reflog` still find it? (3) Why does `bisect` need only about 8 steps for 200 commits?

### Chapter 8 · GitHub and collaboration (week 9)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Remotes | `clone`, `fetch`, `pull`, `push`, tracking branches, `origin` vs `upstream`. | Keep a fork in sync with its upstream. |
| 8.2 Authentication | SSH keys (Ed25519), the agent, HTTPS with tokens (GitHub stopped accepting account passwords for Git on 13 Aug 2021); signing commits with SSH keys. | Set up SSH auth and signed commits; get the "Verified" badge. |
| 8.3 Pull requests | Branch → PR → review → merge; PR descriptions; draft PRs; squash vs merge vs rebase merges. | Open a PR to a classmate's repo, address review comments, merge. |
| 8.4 Team settings | Protected branches, required reviews and checks, CODEOWNERS, issue and PR templates. | Protect `main` so nothing merges without one review and green CI. |
| 8.5 Workflows | Trunk-based development vs GitFlow; the `gh` CLI. | Run a full issue → branch → PR → merge cycle using only `gh`. |

**Check your understanding:** (1) Why is a private SSH key never sent to the server? (2) What does a required status check protect against? (3) When does trunk-based development work better than long-lived branches?

### Chapter 9 · Remote machines and SSH (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 How SSH works | Client and server, host keys and `known_hosts`, key exchange (RFC 4253), public-key authentication. | Explain the first-connection "authenticity can't be established" prompt and what to check. |
| 9.2 Configuration | `~/.ssh/config` host aliases, `ssh-agent`, `scp`, `rsync -avz --delete`. | Deploy a static site to a VM with one `rsync` command. |
| 9.3 Hardening basics | Disable password login, disable root login, keep the system updated, firewall basics (`ufw`). | Harden a fresh VM; verify password login fails. |
| 9.4 Tunnels | Local port forwarding to reach a service bound to localhost. | Reach a remote web app on `localhost:8080` through a tunnel. |

**Check your understanding:** (1) What attack does checking a host key fingerprint prevent? (2) Why is key-only login stronger than a long password? (3) What does `--delete` in `rsync` risk?

### Chapter 10 · Automation and CI (weeks 11–12)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Task runners | `make` targets as documented commands (`make test`, `make lint`). | Add a Makefile to your FND101 project. |
| 10.2 Hooks | Git hooks and the pre-commit framework running `ruff`, ShellCheck and gitleaks before every commit. | Make a commit fail on a lint error, then fix it. |
| 10.3 GitHub Actions | Workflows, triggers, jobs, steps, runners, matrices (Python 3.13–3.15), caching, artifacts; free for public repositories on standard runners. | CI that runs lint and tests on every PR; a red X blocks merge. |
| 10.4 Secrets and permissions | Encrypted secrets, the `GITHUB_TOKEN` and least-privilege `permissions:`, never echoing secrets. | Restrict a workflow to read-only permissions; prove it still passes. |
| 10.5 Supply chain | Pinning actions to commit SHAs, Dependabot, OpenSSF Scorecard, SLSA levels; lessons from the xz backdoor and Knight Capital's 2012 deployment failure. | Run Scorecard on your repo; fix three findings. |

**Check your understanding:** (1) Why pin a third-party action to a commit SHA instead of a tag? (2) What could a malicious dependency do inside a CI job that has write permissions? (3) What does CI prove, and what does it not prove?

### Chapter 11 · Open-source workflow (week 13)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 How projects work | Maintainers, `CONTRIBUTING.md`, codes of conduct, issue triage, governance; India's ecosystem (FOSS United, Zerodha's FLOSS/fund). | Read the contribution guides of three projects; compare their rules. |
| 11.2 Licences | MIT, Apache-2.0, GPL-3.0; permissive vs copyleft; why unlicensed code is not free to use. | Choose a licence for your projects and justify it. |
| 11.3 Reading a big codebase | Entry points, tests, `git log`, `ripgrep`, running the test suite locally. | Map one module of a real project in a one-page note. |
| 11.4 Contributing | Good first issues, asking before large changes, small focused PRs, responding to review; the Linux kernel's email-based patch process as a contrast. | Open your first upstream PR (docs, tests or a small fix). |

**Check your understanding:** (1) Why do maintainers prefer an issue discussion before a large PR? (2) What does the xz incident teach about maintainer burnout and trust? (3) Why might a company forbid copying GPL code into its product?

### Chapter 12 · Working with terminal AI agents safely (week 14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 How coding agents work | An LLM in a loop with tools (read files, run commands); permission prompts; context limits. | Watch an agent's tool calls on a small task and annotate each. |
| 12.2 Project guidance files | `AGENTS.md` (an open format now under the Linux Foundation's Agentic AI Foundation) and `CLAUDE.md`: build commands, conventions, forbidden actions. | Write an `AGENTS.md` for your P2 repository. |
| 12.3 Containment | Work on a branch or `git worktree`; run "skip permissions" modes only inside a VM or container; never give agents production credentials. | Run an agent in a container on a throwaway branch. |
| 12.4 Reviewing agent work | `git diff`, `git add -p` to accept hunk by hunk, re-running tests yourself, checking for new dependencies; untrusted repo text can carry prompt injection. | Have an agent implement a feature; accept, edit or reject each hunk with a written reason. |

**Check your understanding:** (1) Why is "the agent said the tests pass" not evidence? (2) What can a malicious README do to an agent that reads it? (3) Which Git commands let you undo everything an agent did in one step?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Linux setup, Bandit 0–5 | Setup notes |
| 2 | 2 | Bandit 6–12, permissions | Puzzle answers |
| 3 | 3 | Log pipelines | Pipeline answers |
| 4 | 4 | Backup script | ShellCheck-clean script |
| 5 | 5 | Dotfiles | **P1 due** |
| 6 | 6 | Git internals | Object-graph drawing |
| 7 | 6–7 | Branches and conflicts | Conflict lab |
| 8 | 7 | Reflog rescue and bisect | Bisect log |
| 9 | 8 | PR exchange | Merged peer PR |
| 10 | 9 | SSH and VM hardening | Deployed static site |
| 11 | 10 | Pre-commit and Actions | Green CI; **P2 due** |
| 12 | 10 | Supply-chain hygiene | Scorecard fixes |
| 13 | 11 | First upstream contribution | PR link |
| 14 | 12 | Agent-in-a-branch review | Review notes; **P3 due** |
| 15 | Review and exam | Disaster drills | Practical exam (AI-off) |

## Working with AI in this course

- **Use AI for:** explaining an unfamiliar command or flag (then confirm in `man` or explainshell); drafting a regex, `awk` program or Actions workflow that you test on sample input and lint (ShellCheck, actionlint); suggesting conflict resolutions you then verify with tests; summarising a long log. Agents: Claude Code, OpenAI Codex CLI, Gemini CLI, GitHub Copilot.
- **Do without AI (drills):** Bandit levels; weekly Git disaster drills (recover a deleted branch, undo a bad rebase, remove a committed secret) from memory; writing pipelines from a spoken question; the practical exam.
- **Verify AI output by:** running commands first in a throwaway VM or container, or with `--dry-run`/`echo`; using `set -x` to see what actually runs; ShellCheck and actionlint; checking that every suggested package or action exists and is the official one; reading every command before approving an agent's tool call.
- **Where AI still fails here:** destructive suggestions in a confident tone (`git push --force`, `reset --hard`, `rm -rf` with unquoted variables) without a warning about data loss; GNU vs BSD flag differences (`sed -i` behaves differently on macOS); outdated action versions; flags that do not exist. Lab 10 asks you to capture three such failures in a sandbox, with the command, the effect, and the safe alternative.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs | 25% |
| Projects: P1 5%, P2 10%, P3 15% | 30% |
| Upstream open-source contribution | 10% |
| Practical exam (2 hours, AI-off, on a fresh VM) | 35% |

**Gate:** you pass when, on a fresh Linux VM with AI off, within 2 hours you can (1) set up key-only SSH access; (2) clone a repository, find the commit that broke the tests with `git bisect run`, and fix it on a branch; (3) open a pull request whose CI passes; (4) recover a deliberately "lost" commit with `reflog`; and (5) write a ShellCheck-clean script of about 30 lines that answers a question about a log file with a pipeline.

## Industry reality

Every software, cloud, DevOps and security team works this way. GitLab's 2017 database incident (about six hours of production data lost after a deletion on the wrong server, with backups that had been silently failing) and Knight Capital's 2012 incident (more than $460 million lost in 45 minutes after a faulty deployment, per the US SEC) are still taught because they are failures of tooling discipline, not of algorithms. The xz backdoor showed how an open-source supply chain can be attacked through a trusted maintainer role.

**Interview questions from this course**

1. *"Merge vs rebase: when would you not rebase?"* History shape, rewriting public commits, the golden rule, conflict handling, team conventions.
2. *"You pushed an API key to GitHub. What now?"* Revoke and rotate first; check access logs; then remove from history (`git filter-repo`) knowing clones may persist; add push protection and pre-commit scanning.
3. *"A Linux server is slow. What do you run first?"* `uptime`/load, `top` (CPU vs I/O wait), `free -h`, `df -h`, `dmesg`/`journalctl` for errors; a method, not random commands.
4. *"What happens when you run `git commit`?"* Blobs for staged content, a tree, a commit object with parent, author and message, the branch ref moved, `HEAD` following it.
5. *"Design CI for a Python repository."* Lint, type check, tests across versions, caching, required checks on protected `main`, least-privilege tokens, pinned actions, secrets handling.

## Resources (free first)

- **Courses:** [MIT Missing Semester 2026](https://missing.csail.mit.edu/) (including [Version Control](https://missing.csail.mit.edu/2026/version-control/) and [Agentic Coding](https://missing.csail.mit.edu/2026/agentic-coding/)); [GitHub Skills](https://skills.github.com/); [Microsoft Learn GitHub Foundations](https://learn.microsoft.com/en-us/training/paths/github-foundations/); [Ubuntu command line for beginners](https://ubuntu.com/tutorials/command-line-for-beginners).
- **Books and guides:** [*Pro Git*](https://git-scm.com/book/en/v2); William Shotts, [*The Linux Command Line*](https://linuxcommand.org/tlcl.php); [Greg's Bash Guide](https://mywiki.wooledge.org/BashGuide); [Debian Reference](https://www.debian.org/doc/manuals/debian-reference/); [ArchWiki](https://wiki.archlinux.org/); [Filesystem Hierarchy Standard 3.0](https://refspecs.linuxfoundation.org/FHS_3.0/fhs/index.html); [Open Source Guides](https://opensource.guide/how-to-contribute/).
- **Practice:** [OverTheWire Bandit](https://overthewire.org/wargames/bandit/); [Learn Git Branching](https://learngitbranching.js.org/); [Oh My Git!](https://ohmygit.org/); [first-contributions](https://github.com/firstcontributions/first-contributions); [goodfirstissue.dev](https://goodfirstissue.dev/); [NASA HTTP logs](https://ita.ee.lbl.gov/html/contrib/NASA-HTTP.html).
- **Docs and tools:** [Git reference](https://git-scm.com/docs/git-bisect) (`bisect`, [`reflog`](https://git-scm.com/docs/git-reflog)); [GitHub SSH keys](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent); [commit signature verification](https://docs.github.com/en/authentication/managing-commit-signature-verification/about-commit-signature-verification); [protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches); [GitHub Actions](https://docs.github.com/en/actions); [`gh` manual](https://cli.github.com/manual/); [ShellCheck](https://www.shellcheck.net/); [explainshell](https://explainshell.com/); [tldr](https://tldr.sh/); [pre-commit](https://pre-commit.com/); [actionlint](https://github.com/rhysd/actionlint); [gitleaks](https://github.com/gitleaks/gitleaks); [git-filter-repo](https://github.com/newren/git-filter-repo); [OpenSSF Scorecard](https://scorecard.dev/); [SLSA](https://slsa.dev/); [WSL install](https://learn.microsoft.com/en-us/windows/wsl/install); [choosealicense.com](https://choosealicense.com/); [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/); [AGENTS.md](https://agents.md/); Julia Evans, [confusing Git terminology](https://jvns.ca/blog/2023/11/01/confusing-git-terminology/).

## Sources

- GitHub scale (180M+ developers, 630M repositories, India's 5M+ new developers and largest contributor base): [GitHub Octoverse 2025, 28 Oct 2025](https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/) (checked Oct 2026).
- Missing Semester 2026 lecture list and Agentic Coding content: [missing.csail.mit.edu](https://missing.csail.mit.edu/) (checked Oct 2026).
- Latest Git release 2.56.0 (28 Sep 2026): [git-scm.com](https://git-scm.com/); Git 3.0 plans (`main` default branch, SHA-256, reftable; no release date): [BreakingChanges](https://git-scm.com/docs/BreakingChanges) (checked Oct 2026).
- xz backdoor: [NVD CVE-2024-3094](https://nvd.nist.gov/vuln/detail/CVE-2024-3094) and the [original disclosure on oss-security, 29 Mar 2024](https://www.openwall.com/lists/oss-security/2024/03/29/4) (checked Oct 2026).
- Password authentication for Git operations ended 13 Aug 2021: [GitHub blog](https://github.blog/security/application-security/token-authentication-requirements-for-git-operations/) (checked Oct 2026).
- Actions free on public repositories with standard runners: [GitHub Actions billing](https://docs.github.com/en/billing/concepts/product-billing/github-actions) (checked Oct 2026).
- GitLab 31 Jan 2017 outage: [GitLab postmortem](https://about.gitlab.com/blog/postmortem-of-database-outage-of-january-31/); Knight Capital: [SEC press release 2013-222](https://www.sec.gov/newsroom/press-releases/2013-222) (checked Oct 2026).
- AGENTS.md and MCP under the Agentic AI Foundation (9 Dec 2025): [Linux Foundation](https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation) (checked Oct 2026).
- FLOSS/fund ($1M a year, an initiative from Zerodha): [floss.fund](https://floss.fund/); [FOSS United](https://fossunited.org/) (checked Oct 2026).

_Last reviewed: 2026-10_
