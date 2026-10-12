# CS216 · Programming Languages, Compilers and Interpreters

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 2 · 4 | 4 (≈ 120 hours) | L1 → L3 | [CS201](../../semester_3/CS201_algorithms_and_complexity/README.md), [FND111](../../../01_year_1_foundations/semester_2/FND111_programming_ii_object_oriented_and_typed/README.md) | [CSG302](../../../03_majors/computer_science_general/year_3/CSG302_compiler_construction/README.md), [CSG404](../../../03_majors/computer_science_general/year_4/CSG404_programming_language_theory_and_type_systems/README.md), [CSG401](../../../03_majors/computer_science_general/year_4/CSG401_formal_methods_and_program_verification/README.md), [SWE303](../../../03_majors/software_engineering/year_3/SWE303_programming_languages_in_practice_go_rust/README.md), [SWE304](../../../03_majors/software_engineering/year_3/SWE304_ai_assisted_software_engineering_agents/README.md) |

Part of [Year 2 · Core Computer Science](../../README.md). It uses automata, grammars and graph algorithms from [CS201](../../semester_3/CS201_algorithms_and_complexity/README.md) and the typed programming of [FND111](../../../01_year_1_foundations/semester_2/FND111_programming_ii_object_oriented_and_typed/README.md). Memory layout from [CS202](../../semester_3/CS202_computer_architecture_and_systems_programming/README.md) helps in Chapters 8–10.

## Why this course matters now

Every tool a developer touches is a language implementation: compilers, interpreters, type checkers, linters, formatters, bundlers and query engines. These are still being rebuilt for speed:

- **TypeScript 7.0** (July 2026) is a native port of the compiler to Go, with Microsoft reporting 8–12× faster full builds.
- **Python tooling:** core linting and type-checking tools are now written in Rust (Ruff, ty).
- **CPython:** has an experimental JIT (PEP 744) and an optional free-threaded build (PEP 703).
- **Go:** introduced the "Green Tea" garbage collector in Go 1.25.

AI coding assistants rest on the same machinery:

- **Aider** builds its repository map by parsing code with tree-sitter.
- **GitHub's** precise code navigation turns tree-sitter parse trees into stack graphs.
- **Claude Code** exposes a Language Server Protocol tool for definitions, references and type errors.

Assistants can write a parser in seconds. A human still has to define what a program *means*, decide whether a type system is sound enough, read bytecode or IR when performance or correctness is in doubt, and build the tools that check AI-generated code before it ships.

## Learning outcomes

By the end you can:

1. **Explain** the phases of a language implementation and **compare** interpreters, compilers, JITs and transpilers with real examples (CPython, the JVM, V8, TypeScript, LLVM).
2. **Implement** a scanner and a recursive-descent / Pratt parser with good error recovery, and **reason** about grammars (ambiguity, precedence, LL vs LR vs PEG).
3. **Implement** a tree-walking interpreter with lexical scope, closures and classes.
4. **Specify and implement** a static type checker, and **explain** inference, subtyping, generics and gradual typing trade-offs.
5. **Use** functional programming ideas (higher-order functions, immutability, algebraic data types, pattern matching) and **explain** them through the lambda calculus.
6. **Implement** a bytecode compiler and stack VM, and **measure** the speed-up over a tree-walker.
7. **Implement** a mark-sweep garbage collector, and **explain** reference counting, generational, copying and concurrent collectors with their trade-offs.
8. **Read** three-address code, SSA and LLVM IR, and **apply** classic optimizations by hand.
9. **Build** language tooling (tree-sitter grammars, an LSP server, AST-based lints and codemods), and **explain** how AI coding assistants use these structures.

## Chapters and lessons

### Chapter 1 · What a language implementation is (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Syntax, semantics, pragmatics | What a language specifies vs what an implementation chooses; the Lox language (Crafting Interpreters) | Write ten Lox programs that exercise every feature |
| 1.2 The pipeline | Scanning, parsing, semantic analysis, IR, optimization, code generation, runtime | Trace one statement through each phase on paper |
| 1.3 Interpreters, compilers, JITs, transpilers | CPython bytecode, JVM bytecode plus JIT tiers, V8 tiers, TypeScript to JavaScript, ahead-of-time compilers via LLVM | Use Compiler Explorer to compare C at `-O0` and `-O2`; use `dis` on a Python function |
| 1.4 Looking inside Python | `ast` and `dis` modules; CPython's PEG parser (PEP 617) | Print the AST and bytecode of a list comprehension and explain both |

**Check your understanding:** (1) Is Python "interpreted"? Answer precisely. (2) Why does TypeScript need a compiler if browsers run JavaScript? (3) What does a JIT know at run time that an ahead-of-time compiler does not?

### Chapter 2 · Scanning (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Tokens and lexemes | Token types, literals, keywords vs identifiers, source positions | Write a scanner for Lox with line and column tracking |
| 2.2 Regular languages | Regular expressions, NFAs, Thompson's construction, subset construction to DFAs | Convert `(a|b)*abb` to an NFA and a DFA by hand |
| 2.3 Practical scanning | Maximal munch, lookahead, comments, string escapes, Unicode identifiers | Handle nested block comments and report unterminated strings |
| 2.4 Errors that help | Error tokens, recovery, messages with spans | Make the scanner report all errors in a file, not just the first |

**Check your understanding:** (1) Why can't a regular expression match balanced parentheses? (2) Why is maximal munch needed for `>=`? (3) Why keep the scanner separate from the parser at all?

### Chapter 3 · Parsing (weeks 3–4)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Grammars | Context-free grammars, BNF/EBNF, derivations, parse trees vs ASTs, ambiguity (dangling else) | Write an unambiguous expression grammar with precedence levels |
| 3.2 Recursive descent | One function per rule, left-recursion removal, synchronization for error recovery | Parse Lox expressions and statements |
| 3.3 Pratt parsing | Binding power, prefix and infix parselets (Nystrom's Pratt-parser article) | Rewrite the expression parser in Pratt style and add a new operator in 5 lines |
| 3.4 LL and LR families | FIRST/FOLLOW, LL(1) tables, shift-reduce and LALR intuition, conflicts | Build an LL(1) table by hand; explain one shift-reduce conflict |
| 3.5 PEG and generators | PEG ordered choice and packrat parsing (CPython since 3.9), ANTLR, Lark | Implement the same grammar in Lark and compare error messages with yours |

**Check your understanding:** (1) Why can't recursive descent handle left recursion directly? (2) What does PEG's ordered choice give up compared with a CFG? (3) Why do most production compilers use hand-written parsers?

### Chapter 4 · Tree-walking interpreters (week 5)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 AST design | Node types, visitor pattern vs pattern matching (Java, TypeScript, Python `match`) | Design AST classes for Lox |
| 4.2 Evaluating expressions | Values, dynamic types, truthiness, equality, runtime errors | Evaluate arithmetic and logic with precise runtime errors |
| 4.3 Statements and state | Environments, variable declaration and assignment, blocks, control flow | Add `if`, `while`, `for` (as desugaring) |
| 4.4 Functions and closures | Call frames, return via exceptions or signals, closures capturing environments | Implement closures and a counter generator test |

**Check your understanding:** (1) Why is `for` easy to desugar into `while`? (2) What exactly does a closure capture: values or variables? (3) Why does a tree-walker run slowly?

### Chapter 5 · Scope, resolution and objects (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Lexical vs dynamic scope | Static resolution, shadowing, the closure-binding bug that a resolver fixes | Write a program whose output differs under lexical and dynamic scope |
| 5.2 A resolver pass | Semantic analysis before execution; variable depth; static errors (return outside function, self-initialization) | Add a resolver and three static errors |
| 5.3 Classes and inheritance | Instances, fields, methods, `this`, initializers, `super`, method resolution | Implement classes and single inheritance |
| 5.4 Operational semantics, informally | Big-step vs small-step rules for a tiny language | Write evaluation rules for `if` and `while`, and check your interpreter against them |

**Check your understanding:** (1) Why does resolving variables before running the program fix closure bugs? (2) How is `this` bound when a method is pulled off an object? (3) What do semantics rules give you that tests alone don't?

### Chapter 6 · Types and type checking (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Why types | Static vs dynamic checking, soundness, what "well-typed programs don't go wrong" means | Classify ten bugs as caught or not caught by a static checker |
| 6.2 Type rules | Typing judgments, environments, checking expressions and functions | Implement a checker for a typed Lox subset (numbers, strings, booleans, functions) |
| 6.3 Inference | Local inference; Hindley–Milner intuition via unification | Unify five type equations by hand; add `let` inference to your checker |
| 6.4 Subtyping and generics | Structural vs nominal typing, variance, parametric polymorphism | Explain why a `List<Cat>` is not safely a `List<Animal>` for writes |
| 6.5 Gradual typing | TypeScript's deliberate unsoundness, Python type hints with mypy or ty, `any`, runtime validation at boundaries | Find three unsound TypeScript programs that type-check, and add runtime checks |

**Check your understanding:** (1) Why can a sound type system still reject correct programs? (2) Why are TypeScript's types erased at runtime, and what does that imply for API input? (3) What does unification do when two type variables meet?

### Chapter 7 · Functional programming concepts (week 8)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Functions as values | Higher-order functions, map, filter, fold, currying | Rewrite five loops as folds, and one fold back as a loop |
| 7.2 Immutability and recursion | Persistent data structures, structural sharing, tail calls | Implement a persistent list and measure sharing |
| 7.3 Algebraic data types | Sum and product types, pattern matching, exhaustiveness checking (OCaml, Rust, TypeScript unions) | Model an AST as an ADT in OCaml or Rust and write an evaluator |
| 7.4 The lambda calculus | Abstraction, application, β-reduction, Church numerals, evaluation strategies (strict vs lazy) | Reduce three lambda terms by hand; encode booleans |

**Check your understanding:** (1) Why do exhaustive pattern matches catch bugs that `switch` statements miss? (2) When does immutability cost performance, and when does it save it? (3) What is the difference between call-by-value and call-by-name?

### Chapter 8 · Bytecode virtual machines (weeks 9–10)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 VM design | Stack vs register machines, instruction encoding, constant pools, dispatch loops | Write a disassembler for your bytecode |
| 8.2 Compiling expressions | Single-pass compilation from tokens to bytecode (clox style) | Compile and run arithmetic in your VM |
| 8.3 Control flow | Jumps, backpatching, loops, short-circuit `and`/`or` | Compile `if`, `while`, `and`, `or` with correct jumps |
| 8.4 Functions and closures in a VM | Call frames, locals on the stack, upvalues for captured variables | Implement closures with upvalues; pass the closure tests |
| 8.5 Real VMs | CPython's bytecode and specializing interpreter, JVM bytecode, WebAssembly as a portable target | Compare the bytecode for one function in CPython, the JVM and Wasm |

**Check your understanding:** (1) Why is a bytecode VM usually much faster than a tree-walker? (2) Why do closed-over variables need to move off the stack? (3) Why do register VMs execute fewer instructions but larger ones?

### Chapter 9 · Memory management and garbage collection (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 Reachability | Roots, object graphs, manual memory vs automatic | List every GC root in your VM |
| 9.2 Reference counting | CPython's refcounts plus cycle collector; costs and cycles | Create a cycle in Python and watch `gc` collect it |
| 9.3 Tracing collectors | Mark-sweep, mark-compact, copying (Cheney); tri-colour marking; write barriers for incremental and concurrent GC | Implement mark-sweep in your VM with a "stress GC" mode |
| 9.4 Generational and concurrent GCs | Generational hypothesis; Go's GC and `GOGC`, Go's Green Tea collector (Go 1.25); Java's generational ZGC (JEP 439); V8's Orinoco | Tune `GOGC` for a Go program and plot pause times vs memory |
| 9.5 Ownership instead of GC | Rust ownership and borrowing as compile-time memory management | Port one GC'd data structure to Rust and explain each borrow error you hit |

**Check your understanding:** (1) Why can reference counting not reclaim cycles alone? (2) What invariant does a write barrier protect during concurrent marking? (3) Why do generational collectors make most allocations cheap?

### Chapter 10 · IR, optimization and code generation (week 12)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Intermediate representations | Three-address code, control-flow graphs, basic blocks; SSA and φ-nodes | Convert a small function to SSA by hand |
| 10.2 Classic optimizations | Constant folding and propagation, dead-code elimination, common-subexpression elimination, inlining, loop-invariant code motion | Optimize a CFG by hand and confirm with `clang -O2` in Compiler Explorer |
| 10.3 Data-flow analysis | Liveness, reaching definitions, fixed-point iteration | Compute liveness for a 10-block CFG |
| 10.4 Back ends | Instruction selection, register allocation (graph colouring, linear scan), calling conventions; LLVM IR and the Kaleidoscope tutorial | Emit LLVM IR for arithmetic functions from your language and run it |
| 10.5 Getting compilers right | JIT tiers and deoptimization; compiler testing with random programs (Csmith); verified compilation (CompCert) | Read the Csmith paper's summary and list two bug classes it found |

**Check your understanding:** (1) Why does SSA make many optimizations simpler? (2) Why is an optimization that is "correct on all my tests" not enough? (3) When must a JIT deoptimize?

### Chapter 11 · Language tooling and AI coding assistants (weeks 13–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Error-tolerant, incremental parsing | Concrete syntax trees, tree-sitter grammars and queries, incremental re-parsing | Write a tree-sitter grammar for Lox and query all function definitions |
| 11.2 The Language Server Protocol | JSON-RPC, capabilities, diagnostics, go-to-definition, hover, rename (LSP 3.17) | Build a minimal LSP server for Lox with diagnostics |
| 11.3 Code intelligence at scale | Symbol indexes (SCIP), stack graphs for name resolution, fast linters and formatters (Ruff, Biome, Oxc) | Index a repository and answer "who calls this function?" |
| 11.4 How AI assistants see code | Repository maps from parse trees (Aider + tree-sitter), LSP tools in agents (Claude Code), local search indexes (Cursor), tool protocols (Model Context Protocol) | Build a ranked repo map of a project within a 1,000-token budget |
| 11.5 Checking AI-generated code mechanically | AST-based lint rules, codemods, type checks and tests as gates; research on LLMs for compilers (Meta LLM Compiler, 2024) | Write three AST lint rules that catch patterns you have seen in generated code, and run them on 20 AI-written patches |

**Check your understanding:** (1) Why must an editor's parser tolerate broken code when a compiler's need not? (2) Why does an agent with an LSP tool answer "where is this defined?" more reliably than one that only reads text? (3) What can an AST rule guarantee that a code-review prompt cannot?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1: inside Python and C | Annotated AST, bytecode and assembly |
| 2 | 2 | Lab 2: scanner | Scanner with all-errors reporting; P1 starts |
| 3 | 3 | Lab 3: parser (recursive descent) | Statement and expression parser |
| 4 | 3 | Lab 3: Pratt and Lark | Pratt rewrite, grammar comparison; P1 due |
| 5 | 4 | Lab 4: tree-walker | Expressions, statements, closures; P2 starts |
| 6 | 5 | Lab 4: resolver and classes | Static errors, inheritance |
| 7 | 6 | Lab 5: type checker | Checker with inference |
| 8 | 7 | Lab 6: functional programming | ADT evaluator in OCaml or Rust; P2 due |
| 9 | 8 | Lab 7: bytecode VM | Expressions and control flow; P3 track chosen |
| 10 | 8 | Lab 7: closures in the VM | Upvalue tests passing |
| 11 | 9 | Lab 8: garbage collector | Mark-sweep with stress mode |
| 12 | 10 | Lab 9: SSA and LLVM IR | Hand optimizations, emitted IR |
| 13 | 11 | Lab 10: tree-sitter and LSP | Grammar and minimal server |
| 14 | 11 | P3 completion | P3 demo and report |
| 15 | Review and exam | — | Written exam, live parsing oral |

## Working with AI in this course

- **Use AI for:** explaining unfamiliar grammar conflicts, bytecode or IR; generating large sets of test programs (valid and invalid) for your scanner, parser and checker; drafting tree-sitter queries and LSP boilerplate; reviewing your error messages for clarity.
- **Do without AI (drills):** the scanner, the recursive-descent parser, the resolver, the bytecode compiler's jump patching and the garbage collector; FIRST/FOLLOW sets, LL(1) tables, NFA-to-DFA conversion, unification and SSA conversion by hand; reading a `dis` or LLVM IR listing aloud.
- **Verify AI output by:**
  - running the Crafting Interpreters test suite (or your own golden tests) on every change;
  - differential testing (your interpreter vs your VM, your parser vs Lark);
  - fuzzing parsers for crashes;
  - running the VM in stress-GC mode;
  - checking generated optimizations against `clang -O2` output;
  - asking for the grammar or typing rule behind a suggested change and checking it against your spec.
- **Where AI still fails here:** generated parsers and VMs often pass the happy path and break on edge cases such as error recovery, closures over loop variables, upvalue closing and GC roots. You can show this yourself: generate a component, run the official test suite and stress-GC mode, and record what fails. For agents, the lesson of Chapter 11 is concrete: their reliability on large codebases depends on the parse trees, symbol indexes and language servers this course teaches you to build.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs 1–10 | 30% |
| Projects P1 / P2 / P3 | 5% / 15% / 20% |
| Written exam (grammars, automata, type rules, GC, SSA) | 20% |
| Live oral: extend your parser and interpreter | 10% |

**Mastery gate:** you pass when you can, without AI help, (a) add a new language feature to your interpreter in a 90-minute live session, with grammar, parser, resolver, evaluator and tests (for example a ternary operator or `break`); (b) explain, using your own VM, exactly what happens to a captured variable when its function returns, and find a planted GC-root bug; and (c) convert a 6-block function to SSA, apply three optimizations, and prove each is safe.

## Industry reality

Language-implementation skills are used far beyond compiler teams: in developer tools, databases (query planners and bytecode engines, as in SQLite), browsers, ML compilers, infrastructure (configuration languages and policy engines) and AI coding tools. Recent public examples:

- **TypeScript 7:** the compiler was ported to Go.
- **Python tooling:** linters and type checkers rewritten in Rust (Ruff, ty).
- **CPython:** experimental JIT work (PEP 744) and supported free-threading criteria (PEP 779).
- **Go:** the Green Tea collector, planned as the default from Go 1.26.
- **GitHub:** stack-graph code navigation built on tree-sitter.

Interview questions from this course:

1. **"Walk me through what a compiler does to your code."** Cover each phase and what it produces (tokens, AST, typed AST, IR, optimized IR, machine code), where errors are found, and how JITs and interpreters differ.
2. **"Write a parser for arithmetic with precedence and parentheses."** Use recursive descent or Pratt with correct associativity, unary minus, error messages with positions, and tests.
3. **"How does garbage collection work in Java, Go or Python, and how would you debug long pauses?"** Cover tracing vs reference counting, generations, concurrent marking and write barriers, heap-size tuning (`GOGC`, JVM heap flags), allocation profiling, and reducing allocation.
4. **"What is a closure and how is it implemented?"** Cover captured variables vs values, environments or upvalues, heap allocation on escape, and the loop-variable capture pitfall.
5. **"What does TypeScript's type system guarantee at runtime?"** Types are erased, and the system is unsound by design in places (`any`, bivariance, casts). That means validating untrusted input at boundaries, and weighing the trade-offs of gradual typing.

## Resources (free first)

- **Primary text:** Robert Nystrom, [Crafting Interpreters](https://craftinginterpreters.com/) (free online; [code and tests](https://github.com/munificent/craftinginterpreters)).
- **Courses:**
  - [Stanford CS143](https://web.stanford.edu/class/cs143/)
  - [Cornell CS 6120 self-guided](https://www.cs.cornell.edu/courses/cs6120/2023fa/self-guided/)
  - [MIT 6.035 (OCW)](https://ocw.mit.edu/courses/6-035-computer-language-engineering-spring-2010/)
  - NPTEL [Compiler Design](https://nptel.ac.in/courses/106105190) (Prof. Santanu Chattopadhyay, IIT Kharagpur)
- **Free books:** [PLAI](https://www.plai.org/); [SICP](https://mitp-content-server.mit.edu/books/content/sectbyfn/books_pres_0/6515/sicp.zip/index.html) and its [JavaScript edition](https://sourceacademy.org/sicpjs/index); [OCaml Programming (Cornell CS 3110)](https://cs3110.github.io/textbook/); [Essentials of Compilation (source and materials)](https://github.com/IUCompilerCourse/Essentials-of-Compilation).
- **Articles and tutorials:** [Pratt Parsers: Expression Parsing Made Easy](https://journal.stuffwithstuff.com/2011/03/19/pratt-parsers-expression-parsing-made-easy/); [LLVM Kaleidoscope tutorial](https://llvm.org/docs/tutorial/MyFirstLanguageFrontend/index.html); [Go GC guide](https://go.dev/doc/gc-guide); [Green Tea GC](https://go.dev/blog/greenteagc); [V8 Orinoco](https://v8.dev/blog/trash-talk); [Introducing stack graphs](https://github.blog/open-source/introducing-stack-graphs/); [Aider repo map with tree-sitter](https://aider.chat/2023/10/22/repomap.html).
- **Specifications and docs:**
  - [tree-sitter](https://tree-sitter.github.io/tree-sitter/) ([writing grammars](https://tree-sitter.github.io/tree-sitter/creating-parsers/))
  - [LSP 3.17](https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/)
  - [SCIP](https://github.com/sourcegraph/scip)
  - [Model Context Protocol](https://modelcontextprotocol.io/specification)
  - [Python `ast`](https://docs.python.org/3/library/ast.html) and [`dis`](https://docs.python.org/3/library/dis.html)
  - [PEP 617](https://peps.python.org/pep-0617/), [PEP 744](https://peps.python.org/pep-0744/), [PEP 703](https://peps.python.org/pep-0703/)
  - [JEP 439](https://openjdk.org/jeps/439)
  - [LLVM LangRef](https://llvm.org/docs/LangRef.html)
  - [WebAssembly spec](https://webassembly.github.io/spec/)
  - [Rust ownership](https://doc.rust-lang.org/book/ch04-00-understanding-ownership.html)
- **Tools:** [Compiler Explorer](https://godbolt.org/), [AST Explorer](https://astexplorer.net/), [Lark](https://lark-parser.readthedocs.io/), [ANTLR](https://www.antlr.org/), [mypy](https://mypy.readthedocs.io/), [ty](https://docs.astral.sh/ty/), [Ruff](https://docs.astral.sh/ruff/).
- **Papers:** [Finding and Understanding Bugs in C Compilers (Csmith, PLDI 2011)](https://users.cs.utah.edu/~regehr/papers/pldi11-preprint.pdf); [CompCert](https://compcert.org/); [Meta LLM Compiler](https://arxiv.org/abs/2407.02524).
- **Paid, worth it:** Thorsten Ball, [Writing an Interpreter in Go](https://interpreterbook.com/); *The Garbage Collection Handbook*, 2nd edition ([site](https://gchandbook.org/)).

## Sources

All checked 12 Oct 2026.
- [Announcing TypeScript 7.0](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/) (8 Jul 2026): native Go port, "typically… 8x and 12x on full builds", no stable API yet.
- [Go blog: Green Tea GC](https://go.dev/blog/greenteagc) (29 Oct 2025): experimental in Go 1.25, planned default in Go 1.26.
- [PEP 744](https://peps.python.org/pep-0744/) (JIT); [PEP 703](https://peps.python.org/pep-0703/) and [PEP 779](https://peps.python.org/pep-0779/) (free-threading, phase II targeted at 3.14).
- [Aider: Building a better repository map with tree-sitter](https://aider.chat/2023/10/22/repomap.html).
- [GitHub: Introducing stack graphs](https://github.blog/open-source/introducing-stack-graphs/) (Dec 2021, updated Jul 2024).
- [Claude Code tools reference](https://code.claude.com/docs/en/tools-reference): LSP tool for definitions, references and type errors.
- [Cursor codebase indexing docs](https://cursor.com/docs/context/codebase-indexing): local "Instant Grep" index.
- [Meta LLM Compiler](https://arxiv.org/abs/2407.02524) (Jun 2024).
- [Ruff](https://docs.astral.sh/ruff/) and [ty](https://docs.astral.sh/ty/) documentation.

_Last reviewed: 2026-10_
