# FND101 · Labs and projects

Every lab and project lives in its own Git repository (you learn Git in [FND104](../FND104_the_developers_toolkit_linux_shell_git/README.md) in parallel; until week 6, a zip with a `README.md` is accepted). Weeks 1–6 are AI-off for writing code. From week 7, keep an `AI_LOG.md` in each repo: the prompt, what you accepted, what you rejected and why.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Setup and first scripts | Install Python 3.14+ and `uv`, use the REPL, run a script from the terminal and from VS Code | Screenshot of `python --version`; 3 scripts with design-recipe comments | 3 h |
| 2 · Trace tables | Predict the state of variables line by line before running | 12 completed trace tables; Python Tutor links for the 3 you got wrong, with the reason | 3 h |
| 3 · Conditions and loops | Turn rules into exact conditions; test every boundary | Leap-year and slab-calculator functions with test tables; Collatz report (longest chain ≤ 10⁶, run time) | 4 h |
| 4 · Functions and pytest | Decompose and test | 5 functions, ≥ 40 parametrized `pytest` cases, all green | 4 h |
| 5 · TDD and properties | Red–green–refactor; property-based tests | `slugify()` built in ≥ 6 small commits; a Hypothesis round-trip property and the bug it found | 4 h |
| 6 · Debugging clinic | Systematic debugging from tracebacks | Debug log for 5 broken programs: hypothesis, test, result, fix, regression test; plus 5 documented AI failures, with the AI used only as the subject under test (prompt, output, the test it fails) | 4 h |
| 7 · Text and Unicode | Parse real-looking text safely | SMS parser extracting amount, date and reference from 50 synthetic messages with ≥ 95% field accuracy against a hand-labelled answer key; byte/code-point table for 5 strings | 4 h |
| 8 · Collections and cost | Choose structures by the questions asked; measure | Word-frequency report for one Gutenberg book; `timeit` chart of list vs set membership at 10³–10⁶ items with a 3-sentence explanation | 5 h |
| 9 · Messy data | Validate input and report errors instead of crashing | Validator that splits a messy CSV into `clean.csv` and `errors.csv` (line number + reason); `logging` at two levels | 4 h |
| 10 · A real CLI | Package a program professionally | `pywc` as a `uv` project: `argparse`, exit codes, `ruff` clean, README; output identical to `wc -lwc` on 10 test files | 4 h |

## Projects

### P1 · `checkid`: check-digit validator (L1, ~6 hours)

**Real-world inspiration.** Payment card numbers end in a [Luhn](https://en.wikipedia.org/wiki/Luhn_algorithm) check digit; Aadhaar numbers use the [Verhoeff](https://en.wikipedia.org/wiki/Verhoeff_algorithm) scheme (the article cites an NPCI note for bank implementations); ISBN-13 uses a weighted mod-10 sum. Check digits are why a single mistyped digit in a payment form is rejected before any server is called.

**What to build.** A command-line tool: `checkid luhn 79927398713` prints `valid`; `checkid verhoeff --make 236` prints the number with its check digit appended; supports `luhn`, `verhoeff` and `isbn13`.

**Acceptance criteria**
- All three algorithms pass the published test vectors from their reference pages, included as `pytest` cases.
- ≥ 30 tests; a Hypothesis property shows that changing any single digit of a valid number makes it invalid, for Luhn and Verhoeff.
- A test demonstrates the adjacent transposition Luhn cannot detect (`09` ↔ `90`) and shows Verhoeff detects it.
- Exit codes: 0 valid, 1 invalid, 2 bad input (letters, empty string); never a traceback for user input.
- Only synthetic numbers anywhere in the repo, tests or README; the README states this rule.

**Stretch goals.** Add GSTIN or IBAN check digits from their public specifications; benchmark 10⁶ validations; explain in the README why Verhoeff uses the dihedral group D5 (ties to [FND103](../FND103_discrete_mathematics_for_computing/README.md)).

**What it proves to an employer.** You can turn a precise specification into tested code, you think about edge cases and error handling, and you treat personal identifiers carefully.

### P2 · `hisaab`: group expense settler (L2, ~15 hours)

**Real-world inspiration.** Group-expense apps such as Splitwise, and the "who owes whom" sums every hostel and trip group does after paying each other over UPI. The hard parts in production are the same as here: exact money arithmetic, bad input, and explaining the result.

**What to build.** A CLI that reads a CSV of shared expenses (`date, payer, amount, participants, split`) where `split` is `equal`, `exact:...` or `percent:...`, computes each person's net balance, and prints a short settlement plan ("Asha pays Ravi ₹450.00").

**Acceptance criteria**
- All money is stored as integer paise; no `float` touches an amount (checked by a test that greps the source, and by review).
- Remainders from equal splits are allocated deterministically and documented (for example, the first participants alphabetically pay one extra paisa).
- Balances always sum to exactly 0; a Hypothesis property checks this on random inputs.
- The plan settles all balances with at most *n − 1* payments for *n* people (greedy largest-debtor-to-largest-creditor), verified by a test that applies the plan and gets all zeros.
- Invalid rows (negative amounts, unknown split type, percentages not summing to 100) go to an error report with line numbers; valid rows are still processed.
- ≥ 40 tests, ≥ 90% branch coverage, `ruff` clean, `uv` lockfile committed.
- Processes a generated 100,000-row file in under 5 seconds on a typical laptop; the README records the machine and the measured time.

**Stretch goals.** JSON output; a `--explain NAME` flag that lists every expense affecting one person; Hindi and English output; prove in the README why greedy matching needs at most *n − 1* payments.

**What it proves to an employer.** You handle money correctly, validate messy input, and back claims with tests and measurements: the habits fintech teams screen for.

### P3 · `transit`: offline journey planner on real GTFS data (L3, portfolio-grade, ~30 hours)

**Real-world inspiration.** GTFS (General Transit Feed Specification) is the open format transit agencies use to give schedules to Google Maps ([Google's GTFS docs](https://developers.google.com/transit/gtfs)) and other apps ([gtfs.org](https://gtfs.org/)). Delhi's [Open Transit Data portal](https://otd.delhi.gov.in/) publishes static transit datasets, and the [Mobility Database](https://mobilitydatabase.org/) lists feeds worldwide.

**What to build.** A CLI over one real static GTFS feed (`stops.txt`, `routes.txt`, `trips.txt`, `stop_times.txt`, `calendar.txt`):
- `transit stops "Kashmere"`: fuzzy stop search.
- `transit next STOP_ID --after 08:30`: next 5 departures with route and headsign.
- `transit direct A B --after 08:30`: trips that serve A then B.
- `transit plan A B --after 08:30`: earliest arrival with at most one transfer, with transfer stop and wait time.

**Acceptance criteria**
- Loads the full feed in under 30 seconds and answers each query in under 1 second (measured and reported in the README with the feed name and date).
- Correctly handles GTFS times past `24:00:00` (trips after midnight) and service calendars, each with a dedicated test.
- A hand-made fixture feed of ≤ 10 stops whose answers you computed by hand; ≥ 60 tests in total, ≥ 85% branch coverage.
- Errors in the feed (missing columns, bad times) produce clear messages naming the file and line.
- Repository has a README (install, usage, design decisions, limitations), `AI_LOG.md`, and tests running on GitHub Actions on every push (set up in FND104 week 11).
- A 3-minute terminal recording (for example, asciinema) or GIF of the four commands.
- Oral check: you explain any function and change one behaviour live, with AI off.

**Stretch goals.** Unlimited transfers using a simple connection scan; a `--walk` option using stop coordinates and the haversine formula; export a journey as JSON for the web front end you build in [FND114](../../semester_2/FND114_web_foundations_http_html_css_and_javascript/README.md).

**What it proves to an employer.** You can read a real data specification, model messy public data, write a non-trivial program with clean structure, test it properly, and present it.

## Feeds into

- [FND111](../../semester_2/FND111_programming_ii_object_oriented_and_typed/README.md): rebuild `hisaab` with classes and static types, and compare the bugs the type checker catches.
- [FND112](../../semester_2/FND112_data_structures_and_algorithms_i/README.md): `transit plan` becomes a graph-search problem (BFS, Dijkstra).
- [FND115](../../semester_2/FND115_databases_i_data_modeling_and_sql/README.md): load the GTFS feed and the expenses into SQL tables and rewrite queries in SQL.
- [FND114](../../semester_2/FND114_web_foundations_http_html_css_and_javascript/README.md): a web page for the journey planner.
- [CS205](../../../02_year_2_core_computer_science/semester_3/CS205_software_engineering_i_design_testing/README.md): testing and design practices scale up to team projects.
