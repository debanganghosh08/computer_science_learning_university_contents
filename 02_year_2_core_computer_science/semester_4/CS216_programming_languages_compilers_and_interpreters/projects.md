# CS216 · Labs and projects

Labs follow the arc of [Crafting Interpreters](https://craftinginterpreters.com/): a tree-walking interpreter first, then a bytecode VM. Use a different implementation language from the book's (for example Python, TypeScript, Go or Rust for the tree-walker, and C, Rust or Zig for the VM) so that you translate ideas rather than copy code. The book's [test suite](https://github.com/munificent/craftinginterpreters/tree/master/test) is your acceptance oracle. Labs 2, 3 (the recursive-descent part), 4, 7 and 8 are done without AI assistance.

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Inside real implementations | Inspect Python with `ast` and `dis`; compare C at `-O0` and `-O2` in Compiler Explorer | An annotated AST, bytecode and assembly for three functions, each with a one-paragraph explanation | 3 h |
| 2 · Scanner | A Lox scanner with line and column spans, nested comments, string escapes and all-errors reporting | Code passing the scanning tests, plus a fuzz run of 10 minutes with no crashes | 4 h |
| 3 · Parsers | Recursive-descent statement parser; Pratt expression parser; the same grammar in Lark | Parsers passing the parsing tests; a comparison of error messages on 20 broken programs | 8 h |
| 4 · Tree-walking interpreter | Evaluation, environments, closures, a resolver pass, classes and inheritance | Passing the book's tests for the tree-walker through inheritance (at least 95%), and a list of any failures with reasons | 14 h |
| 5 · Type checker | A typed Lox subset with checking and local inference via unification | 30 ill-typed programs rejected with positioned messages; zero false rejections on 50 valid programs | 6 h |
| 6 · Functional programming | An AST evaluator using algebraic data types and exhaustive pattern matching in OCaml or Rust; a small lambda-calculus reducer | Code plus reductions of five terms under call-by-value and call-by-name | 5 h |
| 7 · Bytecode VM | Single-pass compiler, stack VM, jumps and backpatching, call frames, closures with upvalues | A disassembler; tests for expressions, control flow and closures passing | 14 h |
| 8 · Garbage collector | Mark-sweep for the VM, with a stress mode that collects on every allocation; then a `GOGC` tuning experiment in Go | VM passing all tests in stress mode; a pause-time vs memory plot for three `GOGC` values | 6 h |
| 9 · IR and optimization | Hand SSA conversion and three optimizations on a 6-block function; emit LLVM IR for arithmetic functions from your language | Worked SSA, before-and-after IR, and a run of the emitted IR | 5 h |
| 10 · Tree-sitter and LSP | A tree-sitter grammar for Lox with highlight queries; a minimal LSP server publishing diagnostics | Grammar with corpus tests, and a screen recording of diagnostics in an editor | 6 h |

## Projects

### P1 · A JSON parser that survives the conformance suite (L1, ~6 hours)

**Real-world inspiration:** JSON parsers in different languages disagree on edge cases (deep nesting, number limits, invalid Unicode, trailing commas). [JSONTestSuite](https://github.com/nst/JSONTestSuite) collects hundreds of such cases. When two services parse the same document differently, they disagree about what the data says, so conformance matters for any API.

**What to build:** a hand-written scanner and recursive-descent parser for JSON (RFC 8259) in the language of your choice, producing native values, with positioned errors.

**Acceptance criteria:**
- **Conformance:** all `y_` ("must accept") and `n_` ("must reject") cases in JSONTestSuite pass. Your behaviour on every `i_` (implementation-defined) case is documented.
- **Error messages:** every rejection reports line and column.
- **Robustness:** 10 minutes of fuzzing (random mutation of valid documents) produces no crashes and no hangs. Nesting depth is limited, with a clear error.
- **Speed:** parsing a 10 MB file takes no more than 20× the time of your language's standard-library parser, measured and reported.

**Stretch goals:** a streaming (event-based) mode; exact decimal numbers; a pretty-printer that round-trips every accepted test file.

**What it proves to an employer:** you can turn a specification into a robust parser and test it like a professional. Every backend, tooling and security team needs this.

### P2 · A safe, typed rules language (L2, ~15 hours)

**Real-world inspiration:**
- Google's [Common Expression Language (CEL)](https://cel.dev/) evaluates untrusted expressions safely and is used for validation rules in [Kubernetes](https://kubernetes.io/docs/reference/using-api/cel/).
- [Cedar](https://www.cedarpolicy.com/) is a policy language designed to be analyzable.
- Feature-flag targeting and discount-eligibility rules in Indian e-commerce and fintech apps are the *illustrative scenario*: product managers write rules, and engineers must guarantee the rules cannot crash, loop or leak data.

**What to build:** a small expression language with:
- literals, field access, comparisons, boolean logic, `in`, list functions (`all`, `any`, `map`, `filter` with bounded iteration) and string functions;
- a documented EBNF grammar;
- a Pratt parser;
- a type checker with declared input schemas;
- a tree-walking evaluator with a cost budget;
- a second, faster evaluator that compiles the AST into closures;
- an embedding API so an application can call `check(rule)` once and `evaluate(rule, input)` many times.

**Acceptance criteria:**
- **Tests:** at least 150 golden tests (valid programs with expected values, and invalid programs with expected errors).
- **Type checker:** rejects all 30 ill-typed rules in your negative suite with positioned, actionable messages, and rejects none of 50 valid ones.
- **Termination:** every program terminates, because the language has no unbounded loops and the evaluator enforces a step budget. A 15-minute fuzz run produces no crash, hang or budget overrun.
- **Agreement:** the two evaluators match on all tests plus 10,000 randomly generated well-typed expressions.
- **Speed:** the closure-compiled evaluator is at least 3× faster than the tree-walker on a 100,000-evaluation benchmark (numbers reported).
- **Documentation:** a one-page user guide written for a non-programmer product manager.

**Stretch goals:** partial evaluation when some inputs are known; a "why did this rule match?" explanation trace; compile rules to SQL `WHERE` clauses for a subset.

**What it proves to an employer:** you can design a language that others safely use, with grammar, types, semantics, safety limits and performance. Platform, policy, data and fintech teams build exactly these.

### P3 · Choose a track (L3, portfolio-grade, ~30 hours)

#### Track A · A fast VM with a garbage collector

**Real-world inspiration:** production runtimes keep moving: TypeScript 7's compiler port to Go reports 8–12× faster full builds ([announcement](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/)), and Go's Green Tea collector cut garbage-collection time by about 10% for many workloads ([Go blog](https://go.dev/blog/greenteagc)).

**What to build:** complete your Lab 7–8 VM into a full Lox implementation: classes, methods, inheritance, closures, a mark-sweep GC with a stress mode, string interning and a benchmark suite.

**Acceptance criteria:**
- **Tests:** the book's full test suite passes, both in normal mode and in stress-GC mode.
- **Memory safety:** AddressSanitizer (or Miri for Rust) reports no errors across the test suite.
- **Speed:** at least 5× faster than your Lab 4 tree-walker on recursive `fib(30)` and on two other benchmarks, with a table and a flame graph explaining where time goes.
- **GC behaviour:** pause times reported as a histogram, plus one GC optimization (such as a heap-growth policy) with a measured effect.

**Stretch goals:** NaN-boxing; computed-goto dispatch; inline caches for property access; a simple generational nursery.

#### Track B · Language tooling for humans and agents

**Real-world inspiration:**
- Aider builds a ranked repository map from tree-sitter parse trees ([Aider](https://aider.chat/2023/10/22/repomap.html)).
- Claude Code gives its agent an LSP tool for definitions, references and type errors ([tools reference](https://code.claude.com/docs/en/tools-reference)).
- GitHub's code navigation uses stack graphs built on tree-sitter ([GitHub blog](https://github.blog/open-source/introducing-stack-graphs/)).

**What to build:** for Lox (or the P2 rules language), build:
- a tree-sitter grammar;
- an LSP server with diagnostics, go-to-definition, find-references, hover and rename;
- a repository-map generator that ranks symbols to fit a token budget;
- an evaluation of whether these tools help an AI coding assistant.

**Acceptance criteria:**
- **Grammar:** the tree-sitter grammar parses every valid test program with no `ERROR` nodes. Re-parsing after a one-character edit to a 5,000-line file takes under 5 ms.
- **Navigation:** go-to-definition and find-references are correct on a 50-case test set (at least 98%). Rename is verified across files by tests.
- **Diagnostics:** they appear within 200 ms of a keystroke on a 2,000-line file.
- **Repo map:** the generator's output stays within a configurable token budget (for example 1,000 tokens).
- **Agent evaluation:** run 20 coding tasks with an AI assistant, with and without your repo map and LSP server. Report success rate, tool calls and failure modes honestly, including tasks where the tools did not help.

**Stretch goals:** semantic highlighting; code actions with quick fixes; exposing your server's capabilities through a Model Context Protocol server.

**What either track proves to an employer:** Track A shows you can build and tune a runtime: memory management, performance engineering and correctness under stress. Track B shows you can build the code-intelligence layer that editors and AI agents depend on, and measure whether it works. Both are rare skills in 2026.

## Feeds into

- [CSG302 Compiler Construction](../../../03_majors/computer_science_general/year_3/CSG302_compiler_construction/README.md): optimization, register allocation and back ends in depth.
- [CSG404 Programming Language Theory and Type Systems](../../../03_majors/computer_science_general/year_4/CSG404_programming_language_theory_and_type_systems/README.md) and [CSG401 Formal Methods and Program Verification](../../../03_majors/computer_science_general/year_4/CSG401_formal_methods_and_program_verification/README.md): Chapters 5–7 formalized.
- [SWE303 Programming Languages in Practice: Go, Rust and the JVM](../../../03_majors/software_engineering/year_3/SWE303_programming_languages_in_practice_go_rust/README.md) and [SWE305 Concurrency and Performance Engineering](../../../03_majors/software_engineering/year_3/SWE305_concurrency_and_performance_engineering/README.md): runtimes, GC and performance.
- [SWE304 AI-Assisted Software Engineering](../../../03_majors/software_engineering/year_3/SWE304_ai_assisted_software_engineering_agents/README.md) and [AIE304 Tool Use and AI Agents](../../../03_majors/ai_engineering/year_3/AIE304_tool_use_and_ai_agents_loops_harnesses_memory/README.md): P3 Track B is the starting point.
- [CS211 Database Systems Internals](../CS211_database_systems_internals/README.md): query parsing and bytecode engines (SQLite's VM) use the same ideas.
