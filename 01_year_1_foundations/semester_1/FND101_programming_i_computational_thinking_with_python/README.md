# FND101 · Programming I: Computational Thinking with Python

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 1 · 1 | 4 (≈ 120 hours) | L0 → L2 | none | [FND111](../../semester_2/FND111_programming_ii_object_oriented_and_typed/README.md), [FND112](../../semester_2/FND112_data_structures_and_algorithms_i/README.md), [FND114](../../semester_2/FND114_web_foundations_http_html_css_and_javascript/README.md), [FND115](../../semester_2/FND115_databases_i_data_modeling_and_sql/README.md), [CS214](../../../02_year_2_core_computer_science/semester_4/CS214_machine_learning_foundations/README.md) |

## Why this course matters now

Python was used by 57.9% of respondents to the 2025 Stack Overflow Developer Survey, up 7 percentage points in a year. AI assistants (GitHub Copilot, Claude Code, OpenAI Codex, Gemini CLI, Cursor) now write correct code for small, well-specified tasks in seconds, so the scarce skills are the ones around typing: turning a vague problem into a precise spec, choosing tests that expose wrong answers, reading unfamiliar code, and debugging "almost right" code (the top AI frustration in that survey, at 66%). In a January 2026 randomized trial by Anthropic, learners who used an AI assistant while learning a new Python library scored 17 percentage points lower on a follow-up quiz than those who coded by hand, with the biggest gap in debugging. This course builds thinking, testing and debugging habits first, then adds AI as a tutor and reviewer you can check.

## Learning outcomes

By the end you can:

1. Decompose a word problem into inputs, outputs, examples and steps, and write the plan before the code.
2. Write Python 3.14+ programs using values, types, conditionals, loops, functions, strings, lists, tuples, dicts, sets and files.
3. Read any traceback and state the exception type, the failing line, the cause, and a fix.
4. Trace code by hand with a state table and predict its output, then confirm with Python Tutor or `pdb`.
5. Write `pytest` tests with boundary and edge cases, use `parametrize`, and apply red–green–refactor.
6. Debug systematically: reproduce, minimise, hypothesise, test the hypothesis, fix, and add a regression test.
7. Measure the cost of code with `timeit` and explain why `x in set` beats `x in list` for large inputs.
8. Package a small program as a `uv` project with a command-line interface, a lockfile, `ruff` formatting and a README.
9. Use an AI assistant to explain, review and generate tests, and verify every claim it makes against tests and the official docs.

## Chapters and lessons

### Chapter 1 · Thinking in steps (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 What a program is | A program is an exact sequence of steps; the interpreter does what you wrote, not what you meant. REPL vs script, `print`, `input`. Installing Python 3.14 or 3.15 from python.org or with `uv python install`. | Predict, then run, 15 expressions in the REPL; record every surprise. |
| 1.2 The design recipe | From *How to Design Programs*: purpose statement, signature, worked examples, template, code, tests. Pólya's four steps (understand, plan, carry out, look back). | Write the full recipe for "convert seconds to `h:mm:ss`" before writing any code. |
| 1.3 Values, types, names | `int`, `float`, `str`, `bool`, `None`; variables as names bound to objects; `type()`; dynamic typing; reassignment. | Fill a state table for a 12-line program, then check with Python Tutor. |
| 1.4 Expressions and operators | Precedence, `//` and `%` (integer division and remainder), `**`, why `0.1 + 0.2 != 0.3`. | Make change for any rupee amount using the fewest notes and coins with `//` and `%`. |
| 1.5 Your first errors | `SyntaxError`, `NameError`, `TypeError`, `ZeroDivisionError`; reading the caret and the "Did you mean…?" hints added in recent versions. | Break a working program 10 different ways; log each message and what it told you. |

**Check your understanding:** (1) Why does writing examples before code catch misunderstandings that code alone cannot? (2) `x = 5; y = x; x = 7` — what is `y`, and why? (3) A program prints the wrong total but raises no error; which step of the design recipe was probably skipped?

### Chapter 2 · Decisions and repetition (weeks 2–3)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Booleans and conditions | Comparisons, `and`/`or`/`not`, short-circuit evaluation, truthiness of `0`, `""`, `[]`, `None`. | Gregorian leap-year rule as one boolean expression, with a 12-row test table. |
| 2.2 Branching | `if`/`elif`/`else`, flattening nested conditions, guard clauses, `match` with literal and capture patterns. | Slab-based tax calculator from a slab table given in the lab sheet; test every boundary. |
| 2.3 `while` loops | Loop condition, sentinel loops, loop variants (something must shrink), off-by-one errors. | Number-guessing game where the computer guesses your number by halving; count guesses for 1–1000. |
| 2.4 `for` loops | `range(start, stop, step)`, accumulators, nested loops, `break`/`continue`, the `else` clause on loops. | Digit sum, multiplication grid, and a primality check by trial division up to √n. |
| 2.5 Runaway loops | Spotting infinite loops, `Ctrl+C` and `KeyboardInterrupt`, adding a loop counter as a safety net. | Collatz step counts for 1…10⁶; find the start value with the longest chain and time the run. |

**Check your understanding:** (1) Why is `if x > 0 and 10 / x > 1` safe when `x == 0`? (2) Give an input on which `for i in range(1, n)` silently skips the last item you needed. (3) How do you argue a `while` loop will stop before running it?

### Chapter 3 · Functions and decomposition (weeks 3–4)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Defining functions | Parameters vs arguments, `return` vs `print`, implicit `None`, keyword arguments. | Refactor three Chapter 2 programs into pure functions that return values. |
| 3.2 Scope | Local, enclosing, global, built-in (LEGB); why global state makes bugs hard to find. | Predict the output of six scope puzzles; explain each with a frame diagram. |
| 3.3 Contracts | Docstrings, type hints (PEP 484) as documentation, the mutable default argument trap. | Add docstrings and hints to five functions; find and fix a `def f(items=[])` bug. |
| 3.4 Top-down design | Stepwise refinement, stubs that return fake values, helper functions, one job per function. | Design a month-calendar printer top-down: write stubs first, then fill them in one at a time. |
| 3.5 Recursion | Base case, recursive case, the call stack, `RecursionError` and the default recursion limit. | Recursive power, palindrome check and digit sum; draw the call stack for `power(2, 4)`. |

**Check your understanding:** (1) Why is a function that both computes and prints harder to test than one that returns? (2) What exactly is shared between two calls of `def add(x, acc=[])`? (3) Which recursive call in your palindrome function makes the problem smaller, and by how much?

### Chapter 4 · Testing (weeks 4–5)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Tests as specifications | `assert`, `doctest`, a test as an executable example; tests document intent. | Add doctests to every Chapter 3 function. |
| 4.2 pytest | Test discovery, plain `assert` with rich failure output, `pytest -x`, `-k`, `@pytest.mark.parametrize`, `pytest.raises`. | Turn the leap-year table into 20 parametrized cases. |
| 4.3 Choosing cases | Equivalence classes, boundary values, edge cases: empty, zero, negative, huge, non-ASCII text. | Write a test plan (not code) for a Luhn checksum validator; get a peer to find a missing case. |
| 4.4 Red–green–refactor | Test-driven development: failing test, simplest pass, clean up while green. | Build `slugify()` by TDD, committing after each green step. |
| 4.5 Properties | Property-based testing with Hypothesis: round-trip and invariant properties, shrinking to a minimal failing input. | Property `decode(encode(s)) == s` for a Caesar cipher; let Hypothesis find your bug. |
| 4.6 Coverage | `coverage.py` line and branch coverage; why 100% coverage does not mean correct. | Reach 100% branch coverage on one module, then show a bug the tests still miss. |

**Check your understanding:** (1) Which bug in a leap-year function would pass a test suite containing only 2024 and 2023? (2) Why does a shrunk Hypothesis counterexample speed up debugging? (3) When is a test that never fails worse than no test?

### Chapter 5 · Debugging and reading errors (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Anatomy of a traceback | "Most recent call last", frames, exception type and message, chained exceptions ("During handling…"). | Annotate five real tracebacks line by line. |
| 5.2 Debugging as science | Reproduce, minimise, hypothesise, predict, test, fix, regression-test; keep a debug log. | Fix a planted bug while writing every hypothesis down before testing it. |
| 5.3 Tools | f-string `=` specifier (`f"{x=}"`), `breakpoint()`, `pdb` commands (`n`, `s`, `c`, `p`, `l`, `w`, `up`), the VS Code debugger. | Find three planted bugs using `pdb` only, no prints. |
| 5.4 Halving the search | Bisect the input (cut a failing file in half) and the code (disable halves); preview of `git bisect`. | Shrink a 1,000-row CSV that crashes a parser to the single row that causes it. |
| 5.5 Asking for help | Minimal reproducible example (Stack Overflow's MRE guide), rubber-duck explanation, what to include in a question. | Write an MRE of under 15 lines for a bug and post it to the class forum. |

**Check your understanding:** (1) Why fix the cause the traceback points to, not just the line it names? (2) Why write a prediction before stepping in the debugger? (3) What makes a reproducible example "minimal"?

### Chapter 6 · Strings, text and Unicode (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Strings as sequences | Indexing, slicing with steps, immutability, common methods (`split`, `join`, `strip`, `replace`, `find`). | Reverse word order, normalise whitespace, title-case names with particles ("de", "van"). |
| 6.2 Unicode and encodings | Code points vs bytes, UTF-8, `encode`/`decode`, combining characters; Python 3.15 makes UTF-8 the default for file I/O (PEP 686). | Compare `len()`, code points and UTF-8 byte counts for "नमस्ते", "₹500" and an emoji. |
| 6.3 Formatting | f-strings, width, precision, alignment; formatting numbers with Indian grouping (1,00,000) by hand. | Write `format_inr(n)` with tests for 0, 999, 1000, 100000, 12345678 and negatives. |
| 6.4 Patterns | The `re` module: character classes, quantifiers, groups, `fullmatch` vs `search`; test patterns on regex101. | Extract amounts, dates and reference numbers from 50 synthetic bank SMS messages. |
| 6.5 Checksums | Luhn (payment card numbers) and Verhoeff (used for Aadhaar numbers): why a check digit catches typing errors. | Implement Luhn; prove with tests that it catches every single-digit error in a sample. |

**Check your understanding:** (1) Why can `len(s)` disagree with what a reader counts as characters? (2) When would `re.search` accept input that `re.fullmatch` rejects? (3) Which common typing error does Luhn miss that Verhoeff catches?

### Chapter 7 · Collections (weeks 8–9)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Lists | Mutability, aliasing vs copying (`copy`, slicing), methods, list comprehensions. | Ten aliasing puzzles in Python Tutor; explain each arrow. |
| 7.2 Tuples and unpacking | Immutable records, multiple assignment, `enumerate`, `zip`, `*rest` unpacking. | Transpose a matrix with `zip(*rows)`; explain why it works. |
| 7.3 Dictionaries | Key → value maps, hashing intuition, `get`, counting, `collections.Counter`, `defaultdict`. | Word frequencies for a Project Gutenberg book; the 20 most common words without stop words. |
| 7.4 Sets | Membership, de-duplication, union, intersection, difference (links to [FND103](../FND103_discrete_mathematics_for_computing/README.md)). | Find students enrolled in both of two courses from two CSV files. |
| 7.5 Nested data | Lists of dicts, dicts of lists, JSON-shaped data; choosing a structure from the questions you must answer. | Model a train timetable as nested dicts; answer five queries on it. |
| 7.6 Cost of operations | Counting steps, `timeit`, growth from 10³ to 10⁶ items, why dict and set lookups stay fast on average. | Benchmark `in` on a list vs a set at four sizes; plot the timings and explain the shapes. |

**Check your understanding:** (1) After `b = a; b.append(1)`, why did `a` change, and how do you prevent it? (2) Why can a list not be a dict key but a tuple can? (3) Your program is slow with 10⁶ records; which line would you suspect first, and how would you confirm it?

### Chapter 8 · Files, exceptions and real data (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Files and paths | `pathlib.Path`, `with open(..., encoding="utf-8")`, reading line by line, writing safely. | Count lines, words and bytes of a file; compare with `wc`. |
| 8.2 CSV and JSON | `csv.DictReader`, `csv.writer`, `json.load`/`dump`, round-tripping data. | Load a public dataset from data.gov.in; produce a five-line summary. |
| 8.3 Exceptions | `try`/`except`/`else`/`finally`, raising, custom exception classes, never `except: pass`, EAFP vs LBYL. | Make an input loop that survives every bad input a classmate can type. |
| 8.4 Validation | Validating at the boundary, `assert` vs `raise`, reporting errors with line numbers instead of crashing. | Validate a messy transactions CSV; output a clean file plus an error report. |
| 8.5 Logging | The `logging` module, levels, why logs beat prints in programs that run unattended. | Replace prints with logging in your validator; run at `INFO` and `DEBUG`. |

**Check your understanding:** (1) Why is catching every exception and continuing dangerous in a payments script? (2) Where should input validation happen in a program, and why there? (3) What does `finally` guarantee that the line after a `try` block does not?

### Chapter 9 · Programs as projects (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Modules | `import`, packages, `if __name__ == "__main__":`, avoiding circular imports. | Split a 200-line script into three modules with tests. |
| 9.2 Environments and dependencies | Virtual environments, `pip`, `uv init`/`uv add`/`uv run`, lockfiles, version pinning; checking that a package is the real one on PyPI before installing. | Create a `uv` project, add `pytest`, commit the lockfile, reproduce it on a second machine. |
| 9.3 Command-line programs | `sys.argv`, `argparse`, exit codes, stdin/stdout so your program works in pipelines (see [FND104](../FND104_the_developers_toolkit_linux_shell_git/README.md)). | Build `pywc`, a clone of `wc -lwc` with flags, and compare outputs on 10 files. |
| 9.4 Style | PEP 8, naming, small functions, `ruff check` and `ruff format`. | Clean a deliberately messy file to zero `ruff` findings without changing behaviour (tests stay green). |
| 9.5 Standard library tour | `random` with seeds, `datetime` and `zoneinfo` (Asia/Kolkata vs UTC), `statistics`, `itertools`. | Convert a list of UTC timestamps to IST; handle a date-line case. |

**Check your understanding:** (1) Why commit a lockfile? (2) How can a program "work on my machine" yet fail on yours, and which tool prevents it? (3) Why should a CLI return a non-zero exit code on failure?

### Chapter 10 · First objects (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Classes and instances | `class`, `__init__`, attributes, methods, `self`. | A `BankAccount` with deposit, withdraw and an overdraft rule, fully tested. |
| 10.2 Representations | `__repr__` vs `__str__`, `__eq__`, why equality matters in tests. | Make two equal accounts compare equal; test it. |
| 10.3 Dataclasses | `@dataclass`, `frozen=True`, default factories. | Rewrite a dict-based train record as a frozen dataclass. |
| 10.4 When not to use classes | Functions plus data often suffice; invariants are the reason to use a class. Preview of [FND111](../../semester_2/FND111_programming_ii_object_oriented_and_typed/README.md). | Argue in five sentences whether your project needs a class; defend it to a peer. |

**Check your understanding:** (1) What invariant does `BankAccount` protect that a plain dict cannot? (2) Why does `frozen=True` make a dataclass safe to use as a dict key? (3) What does a good `__repr__` save you during debugging?

### Chapter 11 · Classic algorithms you can write (week 13)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Searching | Linear search, binary search on sorted data, the off-by-one traps in `lo`/`hi`. | Implement binary search; test it against `bisect` on 10,000 random cases. |
| 11.2 Sorting | Selection and insertion sort, counting comparisons, `sorted` with `key=` and stability. | Sort students by marks then name; count comparisons for n = 10…1,000. |
| 11.3 Simulation | Seeded randomness, Monte Carlo estimation, reproducibility. | Estimate π and a dice probability; show the error shrinking as samples grow. |
| 11.4 Generate and test | Brute force with `itertools.permutations`/`product`, backtracking idea. | Solve a small timetable puzzle by brute force; count how many candidates you tried. |

**Check your understanding:** (1) What precondition does binary search need, and what happens if it is violated? (2) Why does a stable sort let you sort by two keys in two passes? (3) Why must a simulation record its random seed?

### Chapter 12 · Reading and reviewing code you did not write (week 14)
| Lesson | What you learn | Practice |
|---|---|---|
| 12.1 Reading strategy | Start from entry points and tests, trace one input end to end, write a one-paragraph summary. | Summarise a 300-line open-source Python script; a peer checks your summary against the code. |
| 12.2 A review checklist | Correctness at boundaries, error handling, naming, duplication, hidden global state, dependencies. | Review three classmates' P2 submissions with the checklist. |
| 12.3 Spec → tests → AI → verify | Write the spec and tests yourself, let an assistant draft the code, accept only what passes and what you can explain. | Do one lab problem this way; keep the prompt, the diff, and your accept/reject notes. |
| 12.4 Exam practice | Timed, AI-off: spec to tested program, and traceback-driven bug fixing. | Two mock exams under exam conditions. |

**Check your understanding:** (1) Why read the tests before the implementation? (2) An AI-written function passes your tests but you cannot explain one line; what do you do? (3) What does a dependency you have never heard of in AI-written code require you to check?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1: setup, REPL, first scripts | Design recipe for 3 problems |
| 2 | 2 | Lab 2: trace tables | Leap year + slab calculator |
| 3 | 2–3 | Lab 3: loops | Collatz report |
| 4 | 3–4 | Lab 4: functions + pytest | 5 tested functions |
| 5 | 4 | Lab 5: TDD and Hypothesis | **P1 due** |
| 6 | 5 | Lab 6: debugging clinic | Debug log for 5 bugs |
| 7 | 6 | Lab 7: Unicode and regex | SMS parser |
| 8 | 7 | Lab 8: lists, dicts, sets | Word-frequency report |
| 9 | 7 | Lab 8 continued: timing | Benchmark chart |
| 10 | 8 | Lab 9: messy CSV | Validator + error report |
| 11 | 9 | Lab 10: uv, argparse, ruff | `pywc` CLI; **P2 due** |
| 12 | 10 | Classes lab | Tested `BankAccount` |
| 13 | 11 | Algorithms lab | Binary search vs `bisect` |
| 14 | 12 | Review lab | **P3 due**; peer reviews |
| 15 | Review and exam | Two mock exams | Final exam (AI-off) |

## Working with AI in this course

- **Use AI for:** explaining an error *after* you have written your own hypothesis; Socratic tutoring that gives hints, not code (Harvard's CS50 Duck at cs50.ai is the model); proposing extra test cases, whose expected values you then work out by hand; reviewing your finished code against PEP 8 and your checklist; explaining a standard-library page. Tools: GitHub Copilot (free Copilot Student plan for verified students), Claude Code, OpenAI Codex, Gemini CLI, Cursor.
- **Do without AI (drills):** weeks 1–6 are AI-off for writing code; AI may only explain. Every week, a 45-minute closed-book drill: one trace table, one function from a spec with tests, and three bugs to fix from their tracebacks. The final exam is AI-off.
- **Verify AI output by:** running the tests you wrote *before* asking; checking every import exists in the Python docs or on PyPI (a USENIX Security 2025 study found code models recommended non-existent packages in at least 5.2% of cases for commercial models and 21.7% for open-source models); running Hypothesis properties; reading the full diff line by line; comparing explanations with docs.python.org.
- **Where AI still fails here:** code that is almost right at boundaries (empty input, the last element, the 1,000th rupee); invented functions or parameters; "fixes" that silently change behaviour elsewhere; and learning loss when you delegate. In Anthropic's 2026 trial, learners who delegated code generation scored under 40% on the quiz, while those who asked only conceptual questions scored highest. Lab 6 asks you to collect five AI failures with evidence (the prompt, the output, and the failing test).

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Weekly AI-off drills | 10% |
| Projects: P1 5%, P2 10%, P3 15% | 30% |
| Final exam (3 hours, AI-off, Python docs allowed) | 35% |

**Gate:** you pass when, with AI off and only docs.python.org open, you can (1) take a one-page spec you have not seen, write a plan, and deliver a working program of up to 150 lines split into functions, with at least 15 `pytest` tests covering boundaries, within 3 hours; and (2) take an unfamiliar 200-line program with three planted bugs and their tracebacks, and fix all three within 60 minutes, adding a regression test for each.

## Industry reality

Python is the main interface to AI and data tooling (PyTorch, scikit-learn and the official LLM SDKs ship Python packages) and is common in backend services and automation. GitHub's Octoverse 2025 reports that TypeScript overtook Python by contributor count in August 2025 (hence the typed language in [FND111](../../semester_2/FND111_programming_ii_object_oriented_and_typed/README.md)) and that nearly 80% of new GitHub developers use Copilot in their first week, so interviews increasingly probe whether you can reason without it.

**Interview questions from this course**

1. *"List or set: when would you use each?"* A strong answer covers order and duplicates, hashability, average O(1) set membership vs O(n) list scans, and cites a measurement rather than a slogan.
2. *"This function gives wrong output for some inputs. How do you debug it?"* Reproduce, find the smallest failing input, form and test hypotheses with a debugger, fix the cause, add a regression test, look for the same bug elsewhere.
3. *"What does `def f(x, acc=[])` do wrong?"* The default is created once when `def` runs, so calls share one list; fix with a `None` sentinel; explain how a test would expose it.
4. *"Write `is_palindrome(s)` and test it."* States decisions (case, spaces, Unicode normalisation), uses two pointers or slicing, and tests empty, single-character, even/odd length and non-ASCII input.
5. *"An AI wrote this function. Would you merge it?"* Reads it fully, runs and extends tests, checks boundaries and dependencies, questions any line it cannot explain, and states what evidence would change the decision.

## Resources (free first)

- **Courses:** [Harvard CS50's Introduction to Programming with Python (CS50P)](https://cs50.harvard.edu/python/); [MIT 6.100L Introduction to CS and Programming Using Python (Fall 2022)](https://ocw.mit.edu/courses/6-100l-introduction-to-cs-and-programming-using-python-fall-2022/); NPTEL [The Joy of Computing using Python](https://nptel.ac.in/courses/106106182) (Prof. Sudarshan Iyengar) and [Programming, Data Structures and Algorithms using Python](https://nptel.ac.in/courses/106106145) (Prof. Madhavan Mukund).
- **Books:** [*Think Python*, 3rd edition](https://allendowney.github.io/ThinkPython/) (Allen Downey; free notebooks, with AI-assistant suggestions in every chapter); [*How to Design Programs*](https://htdp.org/) for the design recipe; [Princeton IntroCS in Python](https://introcs.cs.princeton.edu/python/home/).
- **Docs:** [The Python Tutorial](https://docs.python.org/3/tutorial/); [What's New in Python 3.14](https://docs.python.org/3/whatsnew/3.14.html) and [3.15](https://docs.python.org/3.15/whatsnew/3.15.html); [pytest](https://docs.pytest.org/en/stable/); [Hypothesis](https://hypothesis.readthedocs.io/en/latest/); [coverage.py](https://coverage.readthedocs.io/); [uv](https://docs.astral.sh/uv/); [ruff](https://docs.astral.sh/ruff/); [pdb](https://docs.python.org/3/library/pdb.html); [PEP 8](https://peps.python.org/pep-0008/).
- **Tools and practice:** [Python Tutor](https://pythontutor.com/) (visualise execution); [regex101](https://regex101.com/); [Exercism Python track](https://exercism.org/tracks/python) (free mentoring); [Advent of Code](https://adventofcode.com/); [Stack Overflow's minimal reproducible example guide](https://stackoverflow.com/help/minimal-reproducible-example); [data.gov.in](https://data.gov.in/) and [Project Gutenberg](https://www.gutenberg.org/) for real data.

## Sources

- Python 3.15.0 released 9 Oct 2026; 3.14 released 7 Oct 2025: [python.org/downloads](https://www.python.org/downloads/) (checked Oct 2026).
- PEP 686 UTF-8 default and 3.15 error-message changes: [What's New in Python 3.15](https://docs.python.org/3.15/whatsnew/3.15.html); keyword-typo suggestions and REPL highlighting in 3.14: [What's New in Python 3.14](https://docs.python.org/3/whatsnew/3.14.html) (checked Oct 2026).
- Python 57.9%, +7 points; 49,000+ respondents: [Stack Overflow 2025 Survey, Technology](https://survey.stackoverflow.co/2025/technology); 66% "almost right" frustration: [Stack Overflow 2025 Survey, AI](https://survey.stackoverflow.co/2025/ai) (checked Oct 2026).
- 17-point quiz gap, delegation patterns under 40%: [Anthropic, "How AI assistance impacts the formation of coding skills", 29 Jan 2026](https://www.anthropic.com/research/AI-assistance-coding-skills) and [arXiv:2601.20245](https://arxiv.org/abs/2601.20245) (checked Oct 2026).
- Package hallucination rates (5.2% / 21.7%): [Spracklen et al., USENIX Security 2025](https://www.usenix.org/conference/usenixsecurity25/presentation/spracklen) (checked Oct 2026).
- TypeScript overtaking Python (Aug 2025); ~80% of new developers using Copilot in week one: [GitHub Octoverse 2025](https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/) (checked Oct 2026).
- Copilot Student plan for verified students: [GitHub Docs](https://docs.github.com/en/copilot/how-tos/copilot-on-github/set-up-copilot/enable-copilot/set-up-for-students) (checked Oct 2026).
- CS50 AI policy and CS50 Duck: [CS50 academic honesty](https://cs50.harvard.edu/x/honesty/) (checked Oct 2026).
- Verhoeff used for Aadhaar numbers (citing an NPCI document): [Wikipedia, Verhoeff algorithm](https://en.wikipedia.org/wiki/Verhoeff_algorithm); Luhn: [Wikipedia, Luhn algorithm](https://en.wikipedia.org/wiki/Luhn_algorithm) (checked Oct 2026).

_Last reviewed: 2026-10_
