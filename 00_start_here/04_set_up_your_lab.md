# Set up your lab

| Time needed | When | Used by |
|---|---|---|
| 2–4 hours (mostly downloads) | Your first week | Every course from [FND101](../01_year_1_foundations/semester_1/FND101_programming_i_computational_thinking_with_python/README.md) and [FND104](../01_year_1_foundations/semester_1/FND104_the_developers_toolkit_linux_shell_git/README.md) onwards |

Your "lab" is the set of tools every course assumes: a Linux shell, an editor, Git, Python, Node.js, Java, Docker, a database, a local language model, and a cloud account with a budget alarm. This page sets them up on **Windows (through WSL 2)**, **macOS** and **Linux**, then covers **low-budget and phone-only** options.

Commands were checked against the official documentation linked next to each step in October 2026. Versions move quickly: if a command fails, follow the linked page, which is always the authority.

**Safety first.** Several steps download and run an install script (`curl … | sh`). Only run scripts from the official domains shown here, read the linked page first, and never run install commands you find in random videos or chats.

## 1. What hardware you need

| | Minimum | Comfortable |
|---|---|---|
| RAM | 8 GB (Docker Desktop's stated minimum for Windows) | 16 GB, so Docker, an editor, a browser and a small local LLM can run together |
| Storage | 256 GB SSD with 40 GB free | 512 GB SSD |
| CPU | Any 64-bit processor from the last ~8 years with virtualization enabled in the BIOS/UEFI | Recent 4+ core laptop |
| GPU | Not needed | Helpful only for local LLMs and deep-learning labs; cloud notebooks cover most of these |
| OS | Windows 10 version 2004 (build 19041) or later, Windows 11, macOS, or a current Linux | Windows 11, a recent macOS, or Ubuntu LTS |

No laptop, or an old one? Jump to [section 8](#8-low-budget-and-phone-only-options).

## 2. Windows: set up WSL 2

Most courses assume a Linux shell. On Windows you get one through **WSL 2** (Windows Subsystem for Linux), which runs a real Linux kernel alongside Windows ([Microsoft: Install WSL](https://learn.microsoft.com/en-us/windows/wsl/install)).

1. Open **PowerShell as Administrator** (right-click → "Run as administrator") and run:

   ```powershell
   wsl --install
   ```

   This enables the required Windows features and installs Ubuntu. Restart when asked.
2. After the restart, Ubuntu opens and asks you to create a Linux username and password. This password is for `sudo` inside Linux; it does not need to match your Windows password.
3. Check that the distribution runs under WSL 2:

   ```powershell
   wsl -l -v
   ```

   The `VERSION` column should show `2`. If it shows `1`, run `wsl --set-version Ubuntu 2`.
4. If `wsl --install` only prints help text, WSL is already present: list distributions with `wsl --list --online` and install one with `wsl --install -d Ubuntu`.
5. Use **Windows Terminal** (built into Windows 11; [install page](https://learn.microsoft.com/en-us/windows/terminal/install)) and open an Ubuntu tab.

**Rules for WSL that save hours later:**

- Keep your code **inside the Linux file system** (for example `~/code`), not under `/mnt/c/...`. Linux tools are much faster there ([Microsoft: WSL best practices](https://learn.microsoft.com/en-us/windows/wsl/setup/environment)).
- Edit with **VS Code + the WSL extension**: run `code .` inside a project folder in Ubuntu and VS Code opens connected to WSL ([VS Code: Developing in WSL](https://code.visualstudio.com/docs/remote/wsl)).
- From here on, follow the **Linux** steps in section 4 inside your Ubuntu terminal, with the Windows-specific notes for Docker and Ollama.

## 3. macOS: command-line tools and Homebrew

1. Install Apple's command-line developer tools (compilers, `git`, `make`):

   ```bash
   xcode-select --install
   ```

2. Install **Homebrew**, the package manager most macOS developers use ([brew.sh](https://brew.sh/)):

   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

   Follow the "Next steps" the installer prints (it tells you how to add `brew` to your `PATH`).
3. Install a current Git:

   ```bash
   brew install git
   ```

Then continue with section 4. Where a step differs on macOS, it says so.

## 4. The core toolchain (Linux, WSL and macOS)

On Ubuntu (native or WSL), start by updating the system and installing the basics:

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y build-essential git curl unzip zip sqlite3
```

### 4.1 Editor

Any editor works. Most courses show [Visual Studio Code](https://code.visualstudio.com/download) because it runs on all three systems and connects to WSL, containers and remote machines. Alternatives: Neovim, Emacs, or a JetBrains IDE. Choose one and learn its keyboard shortcuts, debugger and Git view in week 1.

### 4.2 Git and GitHub

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global init.defaultBranch main
```

Create an SSH key and add it to GitHub ([GitHub: generate an SSH key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)):

```bash
ssh-keygen -t ed25519 -C "you@example.com"
cat ~/.ssh/id_ed25519.pub     # copy this line into GitHub → Settings → SSH and GPG keys
ssh -T git@github.com         # should greet you by username
```

Turn on two-factor authentication for your GitHub account, and protect the key with a passphrase. [FND104](../01_year_1_foundations/semester_1/FND104_the_developers_toolkit_linux_shell_git/README.md) teaches Git properly; this step only gets you connected.

### 4.3 Python (with uv)

The Python courses use **uv**, a fast tool that installs Python versions and manages project dependencies and lockfiles ([uv installation](https://docs.astral.sh/uv/getting-started/installation/)).

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh     # macOS alternative: brew install uv
# open a new terminal, then:
uv python install 3.14
uv init hello-python && cd hello-python
uv add requests
uv run main.py
```

`uv init` creates a project with a `pyproject.toml`; `uv add` records a dependency and its lockfile; `uv run` runs code inside the project's environment ([uv: working on projects](https://docs.astral.sh/uv/guides/projects/)). Do not install packages into the system Python with `sudo pip`.

### 4.4 Node.js (with nvm)

Use **nvm** to install the current long-term-support (LTS) release, so you can switch versions per project ([nvm README](https://github.com/nvm-sh/nvm)). In October 2026 the LTS line was Node.js 24 ([nodejs.org](https://nodejs.org/en/download)).

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.8/install.sh | bash
# open a new terminal, then:
nvm install --lts
nvm use --lts
node --version && npm --version
```

The script version (`v0.40.8` here) changes over time; copy the current line from the nvm README.

### 4.5 Java (with SDKMAN)

[FND111](../01_year_1_foundations/semester_2/FND111_programming_ii_object_oriented_and_typed/README.md) uses Java 25, the current long-term-support release. **SDKMAN** installs and switches Java versions on Linux, WSL and macOS ([SDKMAN install](https://sdkman.io/install/), [usage](https://sdkman.io/usage)):

```bash
curl -s "https://get.sdkman.io" | bash
source "$HOME/.sdkman/bin/sdkman-init.sh"
sdk list java          # shows available builds; Temurin builds end in -tem
sdk install java       # installs the default build (25.0.4-tem in October 2026)
java -version
```

macOS alternative: `brew install openjdk@25`, then follow the `brew info openjdk@25` instructions to link it.

### 4.6 Docker

Containers appear from Year 1 onwards (databases for labs) and are central in [CS215](../02_year_2_core_computer_science/semester_4/CS215_cloud_and_devops_foundations/README.md).

**Windows.** Two good options:

- **Docker Desktop with the WSL 2 backend** ([install](https://docs.docker.com/desktop/setup/install/windows-install/), [WSL backend](https://docs.docker.com/desktop/features/wsl/)). Requirements listed in October 2026: WSL 2.1.5 or later, 8 GB RAM, hardware virtualization enabled. Licensing: free for personal use, education, non-commercial open source and small businesses ("fewer than 250 employees AND less than $10 million in annual revenue"); larger companies need a paid subscription.
- **Docker Engine inside Ubuntu on WSL**, installed exactly as for Linux below. No Desktop app and no licence question; you manage it from the terminal.

**macOS.** [Docker Desktop for Mac](https://docs.docker.com/desktop/setup/install/mac-install/) (same licence terms), or the open-source [Colima](https://github.com/abiosoft/colima) with the Docker CLI:

```bash
brew install colima docker
colima start
```

**Linux (and Docker Engine in WSL).** Use Docker's apt repository ([Docker: install on Ubuntu](https://docs.docker.com/engine/install/ubuntu/), which supports Ubuntu 22.04, 24.04 and 26.04 LTS):

```bash
# Add Docker's official GPG key:
sudo apt update
sudo apt install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
sudo tee /etc/apt/sources.list.d/docker.sources <<EOF
Types: deb
URIs: https://download.docker.com/linux/ubuntu
Suites: $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}")
Components: stable
Architectures: $(dpkg --print-architecture)
Signed-By: /etc/apt/keyrings/docker.asc
EOF

sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
sudo docker run hello-world
```

To run `docker` without `sudo`, follow [Linux post-installation steps](https://docs.docker.com/engine/install/linux-postinstall/). Read its warning first: members of the `docker` group effectively have root access on that machine.

Docker also publishes a convenience script (`get.docker.com`); its own documentation says it "isn't recommended for production environments". Prefer the repository method above.

### 4.7 A database

Two databases cover almost every lab: **SQLite** (a file, no server) and **PostgreSQL** (a full server). [FND115](../01_year_1_foundations/semester_2/FND115_databases_i_data_modeling_and_sql/README.md) uses PostgreSQL 18, the newest major version in October 2026 ([PostgreSQL versioning](https://www.postgresql.org/support/versioning/)).

- **SQLite:** installed above (`sqlite3`). On macOS it is preinstalled. Test with `sqlite3 test.db "select sqlite_version();"`.
- **PostgreSQL in Docker** (same on every system, easy to delete and recreate) using the [official image](https://hub.docker.com/_/postgres):

  ```bash
  docker run --name pg -e POSTGRES_PASSWORD=change-me-locally -p 5432:5432 -v pgdata:/var/lib/postgresql -d postgres:18
  docker exec -it pg psql -U postgres
  ```

  The password is for your local lab only. Never reuse a real password, and never expose port 5432 to the internet.
- **PostgreSQL installed directly** (optional): on macOS `brew install postgresql@18` then `brew services start postgresql@18`; on Ubuntu, follow the [PostgreSQL download page](https://www.postgresql.org/download/), which explains the official apt repository.

The volume path matters. From PostgreSQL 18 the official image stores data under `/var/lib/postgresql/18/docker` and declares its volume at `/var/lib/postgresql`, which is what the command above mounts. For PostgreSQL 17 and older images, mount at `/var/lib/postgresql/data` instead, or your data will not survive re-creating the container ([image documentation](https://hub.docker.com/_/postgres), section `PGDATA`).

## 5. Check your toolchain

Run this in your Linux, WSL or macOS terminal. Every line should print a version, and `hello-world` should print a greeting.

```bash
git --version
uv --version && uv run --python 3.14 python --version
node --version && npm --version
java -version
docker --version && docker run --rm hello-world
sqlite3 --version
docker exec pg psql -U postgres -c "select version();"
```

Save the output as `lab-check.txt` in your progress repository. When something breaks later, comparing against it shows what changed.

## 6. A local LLM (Ollama)

A local model runs on your own machine. It is slower and less capable than hosted models, but it is free per request, works offline, and keeps private text on your laptop. [FND105](../01_year_1_foundations/semester_1/FND105_ai_native_learning_and_building/README.md) uses one for API practice.

**Install** ([Ollama quickstart](https://docs.ollama.com/quickstart)):

| System | How | Requirements stated in the docs (October 2026) |
|---|---|---|
| Windows | Run `OllamaSetup.exe` from [ollama.com/download](https://ollama.com/download); it installs per user and does not need administrator rights ([Windows docs](https://docs.ollama.com/windows)) | Windows 10 22H2 or newer; NVIDIA driver 551.61+ or a supported AMD driver for GPU use; at least 4 GB for the program, and models often need tens of GB |
| macOS | Open `ollama.dmg` and move Ollama to Applications ([macOS docs](https://docs.ollama.com/macos)) | macOS 14 Sonoma or newer; Apple silicon uses CPU and GPU, Intel Macs use CPU only |
| Linux / WSL | `curl -fsSL https://ollama.com/install.sh \| sh`, then `ollama serve` if the server is not already running ([Linux docs](https://docs.ollama.com/linux)) | GPU optional (NVIDIA with CUDA, or AMD with ROCm) |

On Windows, install it where your code runs: the Windows app for Windows tools, or the Linux version inside WSL if your Python code runs in Ubuntu.

**Pick a model that fits your memory.** Sizes are from each model's tags page on [ollama.com](https://ollama.com/library), October 2026:

| Model tag | Download size | Good for |
|---|---|---|
| `qwen3:0.6b` | 523 MB | Any laptop; testing your code's API calls |
| `llama3.2:1b` | 1.3 GB | 8 GB laptops; simple tasks |
| `qwen3:4b` | 2.5 GB | 16 GB laptops; better answers |
| `gemma4:e2b` (the quickstart's example) | 4.6 GB | 16 GB laptops, or 8 GB of GPU memory as the quickstart recommends |

```bash
ollama run qwen3:0.6b          # downloads the model and opens a chat; type /bye to leave
ollama list                    # models on disk
ollama rm qwen3:0.6b           # free the space
```

Your programs talk to Ollama over a local HTTP API at `http://localhost:11434` ([API docs](https://docs.ollama.com/api/introduction)):

```bash
curl http://localhost:11434/api/generate -d '{"model": "qwen3:0.6b", "prompt": "Explain a hash map in one sentence.", "stream": false}'
```

Small local models make more mistakes than large hosted ones. That makes them good for practising verification ([study protocol](03_ai_native_study_protocol.md#5-verifying-ai-explanations)), and a poor choice for facts you will not check.

## 7. Cloud accounts with budget alarms

From [CS215](../02_year_2_core_computer_science/semester_4/CS215_cloud_and_devops_foundations/README.md) onwards you deploy to a real cloud. You need **one** provider at first; pick the one your target employers use, or the one whose free offer fits you.

**Before you create any resource, set a budget alarm.** Then follow three rules: tag everything you create, delete it when the lab ends, and check the billing page weekly.

| Provider | New-customer offer (checked October 2026) | Budget alarm |
|---|---|---|
| **AWS** | Free plan: US$100 credit at sign-up plus up to US$100 more for exploring services, for 6 months or until credits run out. You are not charged unless you upgrade to a paid plan; the free-plan account closes when it ends. "30+" services have always-free monthly limits ([AWS Free Tier](https://aws.amazon.com/free/)) | AWS Budgets → "Use a template" → **Zero spend budget** (notifies you once spending exceeds free-tier limits) or **Monthly cost budget** ([AWS docs](https://docs.aws.amazon.com/cost-management/latest/userguide/budget-templates.html)) |
| **Google Cloud** | US$300 free-trial credit for 90 days; no charges during the trial unless you upgrade. Free Tier monthly limits include one e2-micro VM in selected US regions, 2 million Cloud Run requests, 1 TiB of BigQuery querying and 10 GiB of BigQuery storage, and 5 GB-months of regional Cloud Storage in US regions ([Free Tier docs](https://docs.cloud.google.com/free/docs/free-cloud-features), updated 9 Oct 2026) | Billing → Budgets & alerts. Default alerts at 50%, 90% and 100%. An alerts-only budget "doesn't automatically cap" spending ([docs](https://docs.cloud.google.com/billing/docs/how-to/budgets)) |
| **Microsoft Azure** | US$200 credit to use within 30 days, free monthly amounts of 20+ services for 12 months, and 65+ always-free services; you must move to pay-as-you-go to continue ([Azure free account](https://azure.microsoft.com/en-us/pricing/purchase-options/azure-account)). Students: [Azure for Students](https://azure.microsoft.com/en-us/free/students) gives US$100 credit without a credit card, with an academic email address | Cost Management → Budgets ([tutorial](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets)) |
| **Oracle Cloud** | "Always free cloud services" plus US$300 credit towards other services (page description, October 2026; check the [Free Tier page](https://www.oracle.com/cloud/free/) for current limits) | Billing → Budgets |

**Budget alarms notify; they usually do not stop spending.** A runaway resource can still cost money between the alert and your response. Keep labs small, delete resources at the end of every session, and never commit cloud keys to Git. Prefer short-lived credentials (taught in CS215) over long-lived access keys.

**Students:** the [GitHub Student Developer Pack](https://education.github.com/pack) bundles free offers from many developer tools for verified students. Offers change; read each one's terms.

## 8. Low-budget and phone-only options

You can do most of Years 1–2 without a powerful laptop.

| Option | What you get (checked October 2026) | Good for | Limits |
|---|---|---|---|
| [GitHub Codespaces](https://docs.github.com/en/codespaces/overview) | A full Linux development environment with VS Code in the browser. Personal accounts get 120 compute hours and 15 GB-months of storage a month on GitHub Free (180 hours and 20 GB-months on Pro); compute use scales with the machine's core count, so a 2-core machine uses the quota at twice the hourly rate ([billing docs](https://docs.github.com/en/billing/concepts/product-billing/github-codespaces)) | Any course that needs a shell, Git, Python, Node, Java or Docker | Without a payment method on file, usage stops when the quota is used up; stop codespaces when you finish |
| [Google Colab](https://colab.research.google.com/) | Free Python notebooks in the browser, sometimes with a GPU. Limits are not published and vary; free notebooks run for at most 12 hours and time out when idle ([Colab FAQ](https://research.google.com/colaboratory/faq.html)) | FND113, FND116, CS206, CS214 and ML labs | Not for long-running servers; GPUs are not guaranteed |
| [Kaggle Notebooks](https://www.kaggle.com/docs/notebooks) | Free notebooks with a weekly GPU and TPU quota (check the docs for current hours) | ML and data labs, public datasets | Session and weekly limits |
| [Google Cloud Shell](https://docs.cloud.google.com/shell/docs/quotas-limits) | A browser terminal with a 5 GB persistent home directory; default quota 50 hours a week, sessions capped at 12 hours | Shell, Git and cloud CLI practice | Needs a Google account |
| [Termux](https://termux.dev/en/) on Android | A Linux-like terminal and package manager on your phone | Shell, Git, Python and SQLite practice on the go | Small screen; no Docker; install only from the sources listed on the Termux site |
| A second-hand laptop with Linux | Ubuntu LTS runs well on many older laptops with an SSD and 8 GB RAM | Everything except heavy ML | Check that the CPU supports virtualization if you need Docker |
| College, library or community labs | Shared computers, often with good internet | Downloads, long builds | Do not leave credentials on shared machines; use a browser profile you can delete |

**A phone-only week that works:** read the lesson on the phone, do the AI-off drill on paper, write code in a Codespace or Colab from a borrowed or shared computer twice a week, and use Termux for shell and Git drills in between.

**Saving data costs:** download large installers and models once over Wi-Fi, keep them on an external drive, and use `uv` and `npm` caches instead of reinstalling per project.

## 9. Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| `wsl --install` hangs at 0.0% | Store download problem | `wsl --install --web-download -d Ubuntu` ([WSL install](https://learn.microsoft.com/en-us/windows/wsl/install)) |
| Docker says virtualization is disabled | BIOS/UEFI setting | Enable Intel VT-x or AMD-V (often called "SVM") in the firmware settings |
| Everything in WSL is slow | Code stored under `/mnt/c` | Move the project to `~/code` inside Linux |
| `command not found` right after installing uv, nvm or SDKMAN | Shell not reloaded | Open a new terminal, or `source ~/.bashrc` (`~/.zshrc` on macOS) |
| `permission denied` on `/var/run/docker.sock` | User not in the `docker` group | Follow the Linux post-install steps, then log out and back in |
| Port 5432 already in use | Another PostgreSQL is running | Stop it, or map a different port: `-p 5433:5432` |
| Ollama runs very slowly | Model too large for RAM or GPU | Use a smaller tag from the table in section 6 |
| `git push` asks for a password | Remote uses HTTPS instead of SSH | `git remote set-url origin git@github.com:you/repo.git` |

## 10. Keep it healthy

- Update monthly: `sudo apt update && sudo apt upgrade` (or `brew update && brew upgrade`), `uv self update`, `nvm install --lts`.
- Clean up: `docker system df` shows space used; `docker system prune` removes stopped containers and dangling images (read what it will delete first). Remove local models you no longer use with `ollama rm`.
- Back up your work by pushing to GitHub, not by copying folders.
- Keep a `SETUP.md` in your progress repository with what you installed and any fixes you needed. Future you, and your study circle, will use it.

## Sources

All checked October 2026.

- Microsoft. Install WSL (updated 2 Jun 2026). https://learn.microsoft.com/en-us/windows/wsl/install ; WSL development environment best practices. https://learn.microsoft.com/en-us/windows/wsl/setup/environment
- Visual Studio Code. Developing in WSL. https://code.visualstudio.com/docs/remote/wsl
- Homebrew. https://brew.sh/
- GitHub Docs. Generating a new SSH key. https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent
- Astral. uv installation and projects guides. https://docs.astral.sh/uv/getting-started/installation/ ; https://docs.astral.sh/uv/guides/projects/
- nvm README (v0.40.8). https://github.com/nvm-sh/nvm ; Node.js downloads (LTS v24). https://nodejs.org/en/download
- SDKMAN. Install and usage; default Java candidate list. https://sdkman.io/install/ ; https://sdkman.io/usage
- Docker Docs. Install Docker Engine on Ubuntu; Linux post-installation steps; Docker Desktop for Windows (requirements and licensing); Docker Desktop for Mac. https://docs.docker.com/engine/install/ubuntu/ ; https://docs.docker.com/engine/install/linux-postinstall/ ; https://docs.docker.com/desktop/setup/install/windows-install/ ; https://docs.docker.com/desktop/setup/install/mac-install/
- PostgreSQL. Versioning policy (18.6 current). https://www.postgresql.org/support/versioning/ ; Docker official image. https://hub.docker.com/_/postgres
- Ollama documentation: quickstart, Windows, macOS, Linux, API. https://docs.ollama.com/quickstart ; model library. https://ollama.com/library
- AWS Free Tier. https://aws.amazon.com/free/ ; AWS Budgets templates. https://docs.aws.amazon.com/cost-management/latest/userguide/budget-templates.html
- Google Cloud. Free Tier and free trial (updated 9 Oct 2026). https://docs.cloud.google.com/free/docs/free-cloud-features ; Budgets. https://docs.cloud.google.com/billing/docs/how-to/budgets ; Cloud Shell quotas. https://docs.cloud.google.com/shell/docs/quotas-limits
- Microsoft Azure. Free account. https://azure.microsoft.com/en-us/pricing/purchase-options/azure-account ; Free services. https://azure.microsoft.com/en-us/pricing/free-services ; Budgets tutorial. https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets
- Oracle Cloud Free Tier. https://www.oracle.com/cloud/free/
- GitHub. Codespaces billing. https://docs.github.com/en/billing/concepts/product-billing/github-codespaces ; Student Developer Pack. https://education.github.com/pack
- Google Colab FAQ. https://research.google.com/colaboratory/faq.html
- Termux. https://termux.dev/en/

_Last reviewed: 2026-10_
