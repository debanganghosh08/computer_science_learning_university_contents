# FND111 · Programming II: Object-Oriented and Typed Programming (Java and TypeScript)

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 1 · 2 | 4 (≈ 120 hours) | L1 → L2 | [FND101](../../semester_1/FND101_programming_i_computational_thinking_with_python/README.md) | [CS202](../../../02_year_2_core_computer_science/semester_3/CS202_computer_architecture_and_systems_programming/README.md), [CS205](../../../02_year_2_core_computer_science/semester_3/CS205_software_engineering_i_design_testing/README.md), [CS216](../../../02_year_2_core_computer_science/semester_4/CS216_programming_languages_compilers_and_interpreters/README.md), [MOB301](../../../03_majors/mobile_engineering/year_3/MOB301_android_with_kotlin_and_jetpack_compose/README.md) |

## Why this course matters now

Most production backends, Android apps and enterprise systems are written in statically typed, object-oriented languages. Java runs core services at companies such as Netflix, and TypeScript became the most-used language on GitHub in 2025. AI assistants (GitHub Copilot, Cursor, Claude Code, OpenAI Codex, JetBrains AI Assistant) now write classes, boilerplate and unit tests in seconds, and companies use them for large code migrations: Google and Airbnb have published how they do it and how they check the results. The assistant cannot decide what your types should mean, where module boundaries go, which behaviour a test must pin down, or whether a 400-line generated diff is safe to merge. This course trains those decisions in two languages at once, so you learn the ideas rather than one syntax.

## Learning outcomes

By the end you can:

1. Build, run and debug Java 25 and strict TypeScript programs from the command line, an IDE and CI, and explain what each compiler checks and erases.
2. Model a domain so that invalid states do not compile: records, enums and sealed interfaces with exhaustive `switch` in Java; discriminated unions with a `never` check in TypeScript.
3. Demonstrate nominal vs structural typing, type inference, null safety and type erasure with a code example of each.
4. Design classes with explicit invariants, immutability and a correct `equals`/`hashCode` contract, and show the bug when the contract breaks.
5. Choose between inheritance and composition, and justify each SOLID principle or pattern you use by the change it makes cheaper.
6. Write generic code with bounds and wildcards (PECS) in Java and constraints, mapped and conditional types in TypeScript.
7. Design error handling with checked and unchecked exceptions, try-with-resources, typed `Result` values and async errors.
8. Write unit tests in JUnit 6 and Vitest 5 that reach a mutation score of at least 70% on your own modules.
9. Find your way around an unfamiliar codebase of 50,000+ lines, trace one feature end to end and land a reviewed change.
10. Refactor with an AI agent behind a verification gate (characterization tests, compiler, mutation testing, diff review) and keep a log of what the AI got wrong.

## Chapters and lessons

### Chapter 1 · From Python to typed languages (week 1)

| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Why static types | Compile-time vs run-time errors; types as checked documentation; inference (`var`, TypeScript) and annotating public boundaries; Python hints with `mypy --strict` as the bridge | Add hints to a FND101 program, run `mypy --strict`, fix every error and note which ones were real bugs |
| 1.2 The Java toolchain | JDK 25 (the current LTS; JDK 27 is the newest feature release), `javac`/`java`, single-file launch (`java Main.java`), compact source files and instance `main` (JEP 512), `jshell`, Maven/Gradle layout | Port word-count and FizzBuzz to Java; run them three ways (jshell, single file, Maven) |
| 1.3 The TypeScript toolchain | Node.js 24 LTS, TypeScript 7 `tsc` (the native compiler) or 6.0, `tsconfig.json` with `strict` and `noUncheckedIndexedAccess`, npm and lockfiles | Port the same programs to TypeScript; make `tsc --noEmit` pass with zero `any` |
| 1.4 Values, references, numbers | Java primitives vs boxed types, `==` vs `.equals`, 32-bit `int` overflow; JavaScript `number` as IEEE 754 double, `bigint`, `===` | Predict then run 12 snippets (e.g. `Integer.valueOf(127) == Integer.valueOf(127)` vs 128, `0.1 + 0.2`) |

**Check your understanding:** (1) Name a bug that `tsc --strict` catches and that Python only finds at run time, and one bug neither catches. (2) Why does `Integer` caching make `==` "work" for small numbers and fail for large ones? (3) What does a lockfile protect you from that `package.json` alone does not?

### Chapter 2 · Types as design (week 2)

| Lesson | What you learn | Practice |
|---|---|---|
| 2.2 Nominal vs structural typing | Java needs declared `implements`; TypeScript accepts any matching shape; excess-property checks; branded types (`type Rupees = number & {__brand}`) | Write a case that TypeScript accepts and Java rejects, then fix it with a brand |
| 2.3 Null safety | `NullPointerException`, `Optional` (return types only), `strictNullChecks`, `?.` and `??`, `null` vs `undefined` | Remove all nulls from a module; the tests must still pass |
| 2.4 Algebraic data types | Records, enums, sealed interfaces plus pattern-matching `switch`; TypeScript discriminated unions with `assertNever`; "make illegal states unrepresentable" | Model a UPI-style payment (illustrative): `Initiated`, `Pending`, `Success`, `Failed(reason)`, `Reversed`, with exhaustive handling in both languages |
| 2.5 Types end at the boundary | Java generics erased at run time; TypeScript types erased completely; validate untrusted JSON with a schema (Zod) | Parse a malformed API response; show the typed code crashing without validation and failing cleanly with it |

**Check your understanding:** (1) Your TypeScript function accepts `{amount: number}` and a caller passes a `User` that also has `amount`. Is that a bug or a feature? (2) Why does adding a new variant to a sealed interface break compilation, and why is that good? (3) If types are erased, what exactly protects you from a bad API response?

### Chapter 3 · Classes, encapsulation and equality (week 3)

| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 Classes and objects | Fields, constructors, methods, `this`, `static`; TypeScript `private` vs `#private` | Implement `Wallet` in both languages |
| 3.2 Invariants and immutability | Class invariants, validation in constructors, defensive copies, `final`, records, `readonly`, `Object.freeze` limits | Write tests that try to break `balance >= 0` through every public method; make them all fail to break it |
| 3.3 Equality and hashing | Identity vs value equality; the `equals`/`hashCode` contract; why mutable keys corrupt a `HashMap` | Put a mutable key in a `HashSet`, mutate it, and explain why `contains` now returns `false` |
| 3.4 Interfaces and abstract classes | Interfaces as contracts, default methods, abstract classes for shared state; TypeScript `interface` vs `type` | Define `PaymentMethod` and implement UPI, card and wallet variants |

**Check your understanding:** (1) Why is a record a better `HashMap` key than a class with setters? (2) A constructor validates its input but a getter returns the internal `List`. What invariant is now at risk? (3) When is an abstract class a better choice than an interface?

### Chapter 4 · Inheritance, polymorphism and composition (week 4)

| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 Subtyping and dispatch | Overriding vs overloading, `@Override`, dynamic dispatch, `super` | Trace which method runs in 8 overload/override puzzles |
| 4.2 Liskov substitution | Preconditions and postconditions of overrides; the rectangle/square trap; the fragile base class problem | Write the test that fails when `Square extends Rectangle` |
| 4.3 Composition and delegation | "Favour composition over inheritance" (Gamma et al., 1994); has-a vs is-a; delegation | Refactor a `Notifier` hierarchy (SMS, email, WhatsApp, with/without retry) from 6 subclasses to 2 composable parts |
| 4.4 Patterns that last | Strategy, Factory, Adapter, Decorator, Observer, Builder; when a lambda or a Stream pipeline replaces a pattern | Implement a pricing engine with pluggable discount strategies, once with classes and once with functions |

**Check your understanding:** (1) Why did the subclass count explode in the `Notifier` hierarchy, and what does composition change? (2) Give a case where inheritance is the right tool. (3) When is a Strategy class better than passing a function?

### Chapter 5 · Generics and advanced types (weeks 5–6)

| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Generic classes and methods | Type parameters, bounds (`<T extends Comparable<? super T>>`), generic methods | Write `max`, `groupBy` and a generic `LruCache<K, V>` |
| 5.2 Variance | Invariance of `List<Integer>` vs `List<Number>`; covariant arrays and `ArrayStoreException`; wildcards and PECS | Make `copy(List<? super T> dst, List<? extends T> src)` compile, then explain each wildcard |
| 5.3 TypeScript's type language | Unions, intersections, `keyof`, indexed access, mapped and conditional types, `Partial`/`Pick`/`Record`, `satisfies` | Type a `pick(obj, keys)` function so wrong keys fail to compile |
| 5.4 A typed `Result<T, E>` | Errors as values; generic sum types in both languages | Replace exceptions in a parser with `Result` and compare the call sites |
| 5.5 Escape hatches | `any` vs `unknown`, type assertions, `@SuppressWarnings("unchecked")`; when each is acceptable | Audit a small open-source TypeScript package for `as` and `any`; classify each as justified or not |

**Check your understanding:** (1) Why would making `List<Integer>` a subtype of `List<Number>` be unsound? (2) Where is TypeScript deliberately unsound, and why did its designers accept that? (3) When does a `Result` type make code worse than exceptions?

### Chapter 6 · Errors, exceptions and resources (week 7)

| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 Exceptions | `throw`/`catch`/`finally`, reading stack traces, Java's checked vs unchecked split, wrapping with a cause | Find the root cause of three bugs from stack traces alone |
| 6.3 Resources | `try`-with-resources and `AutoCloseable`; TypeScript `using` declarations; `finally` pitfalls | Prove with a test that files close even when parsing throws |
| 6.4 Designing failure | Fail fast, preconditions (`Objects.requireNonNull`), error messages people can act on, never swallowing exceptions, logging with context | Turn a CSV importer that crashes on line 4,812 into one that reports every bad row |
| 6.5 Async errors | `async`/`await`, unhandled rejections, `Promise.allSettled`, timeouts with `AbortController` | Call three flaky fake services and return partial results with a clear error report |

**Check your understanding:** (1) Why is `catch (Exception e) {}` worse than letting the program crash? (2) When should a payment client throw, and when should it return a failure value? (3) What happens to an unhandled promise rejection in Node.js?

### Chapter 7 · Collections, streams and text (week 8)

| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Java Collections Framework | `ArrayList`, `HashMap`, `TreeMap`, `LinkedHashMap`, `ArrayDeque`, `PriorityQueue`, `List.of`, `ConcurrentModificationException`; their costs (see [FND112](../FND112_data_structures_and_algorithms_i/README.md)) | Choose and justify a collection for five described workloads |
| 7.3 JavaScript collections | `Array`, `Map`, `Set`, `WeakMap`; plain objects as maps and their prototype pitfalls; `[10, 9, 1].sort()` | Write a correct numeric sort and a frequency counter with `Map` |
| 7.4 Streams and grouping | `Collectors.groupingBy`, `toMap` collisions, `Object.groupBy` | Daily totals by category from 100,000 synthetic transactions in both languages |
| 7.5 Strings and Unicode | Immutability, `StringBuilder`, UTF-16 code units, emoji and Devanagari grapheme clusters, `Intl.Segmenter`, `BreakIterator` | Count the user-visible characters in "नमस्ते" correctly in both languages |

**Check your understanding:** (1) Why does `"नमस्ते".length` not equal what a reader counts? (2) When is `TreeMap` worth its O(log n) cost? (3) What goes wrong when you use a plain object as a map keyed by user input?

### Chapter 8 · Unit testing with JUnit and Vitest (weeks 9–10)

| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 What a unit test is | Arrange-act-assert, one behaviour per test, naming, the test pyramid; JUnit 6 (Jupiter API) `@Test`, `@BeforeEach`, AssertJ | Test `Wallet` and the payment state machine |
| 8.2 Vitest 5 | `describe`/`it`/`expect`, `test.each`, watch mode, V8 coverage | Mirror the Java tests in TypeScript |
| 8.3 Parameterised and property-based tests | `@ParameterizedTest`, `@CsvSource`; properties with jqwik and fast-check (e.g. "sorting twice equals sorting once") | Find a real bug in your `groupBy` with a property test |
| 8.4 Test doubles and design for testability | Stubs, fakes and mocks (Mockito, `vi.fn`), injecting a `Clock`, why over-mocking hides bugs | Make a time-dependent "offer expires at midnight IST" rule testable |
| 8.5 Measuring test quality | Line coverage vs mutation testing with PIT (Java) and StrykerJS (TypeScript) | Raise a module from 100% line coverage and 55% mutation score to ≥ 80% |

**Check your understanding:** (1) How can a suite reach 100% coverage and still miss a bug? (2) What does a surviving mutant tell you? (3) Why is injecting a clock better than mocking `LocalDate.now()`?

### Chapter 9 · SOLID, code smells and refactoring (week 11)

| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 SRP and OCP | Cohesion, coupling, reasons to change; extension through interfaces | Split a 600-line `OrderService` along its reasons to change |
| 9.2 LSP, ISP, DIP | Narrow interfaces, depending on abstractions, constructor injection, ports and adapters | Swap a real SMS gateway for a fake without touching business code |
| 9.3 Smells and refactorings | Long method, feature envy, primitive obsession, shotgun surgery; Extract Function, Introduce Parameter Object, Replace Conditional with Polymorphism | Run the Gilded Rose kata: tests first, then refactor in small commits |
| 9.4 Knowing when to stop | YAGNI, Beck's four rules of simple design, the cost of premature abstraction | Delete one interface from your own code that has a single implementation and no test seam |

**Check your understanding:** (1) Which SOLID principle does a 15-case `switch` on payment type usually violate, and when is that `switch` fine? (2) What makes a refactoring safe? (3) Name a cost of dependency inversion.

### Chapter 10 · Reading large codebases (week 12)

| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Getting it to build | README and CONTRIBUTING, build files, running the tests, reading CI config | Build and test Spring PetClinic (Java) and a mid-size TypeScript project |
| 10.2 Navigation and code maps | Go to definition, find usages, call hierarchy, `ripgrep`, `git blame`, breakpoints; a one-page map with a Mermaid sequence diagram | Trace one HTTP request in PetClinic from controller to database and draw it |
| 10.4 Contributing | Good-first issues, style guides (Google Java Style), Checkstyle, ESLint, Prettier, small reviewable PRs | Open a documentation or test PR to an open-source project |
| 10.5 AI as a guide, not an oracle | Ask an assistant for a map of the code, then confirm each claim with navigation | Log every claim the AI made, marked confirmed or false, with evidence |

**Check your understanding:** (1) What three files do you read first in an unknown repository, and why? (2) Why is a debugger trace more trustworthy than a summary? (3) How do you choose a first PR that is likely to be merged?

### Chapter 11 · AI-assisted refactoring with verification (weeks 13–14)

| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 Characterization tests | Pinning current behaviour before change (Feathers); approval/golden-master tests | Write approval tests for a legacy report generator |
| 11.2 Refactoring with an agent | Scoped prompts, one change per step, compile and test after every step, reading the diff hunk by hunk | Use Claude Code, Copilot agent mode, Cursor or Codex to modernise a module; reject at least one suggestion with a reason |
| 11.3 Deterministic tools first | IDE refactorings, OpenRewrite recipes (Java), ts-morph and jscodeshift codemods | Do the same rename-and-move with a codemod and with an LLM; compare the diffs |
| 11.5 Migration studio | Java 8-style code to modern Java (records, sealed types, pattern matching), or loose JavaScript to strict TypeScript, using the Google and Airbnb verification pipelines (see Industry reality) as models | Finish the migration with all tests green, mutation score held or improved, and a verification log |

**Check your understanding:** (1) Why must characterization tests come before any AI-generated change? (2) The AI's diff passes all tests. What else do you check before merging? (3) When is a codemod a better tool than an LLM?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Two toolchains, one CI | Green CI badge |
| 2 | 2 | Lab 2 · Payment state machine | Exhaustive state handling in both languages |
| 3 | 3 | Lab 3 · Breaking equality | Bug report with a fix |
| 4 | 4 | Lab 4 · Composition refactor | P1 starts |
| 5–6 | 5 | Lab 5 · Generics and `Result` | P1 due (end of week 6) |
| 7 | 6 | Lab 6 · Error design | Importer with error report |
| 8 | 7 | Lab 7 · Collections and Unicode | P2 starts |
| 9–10 | 8 | Lab 8 · Mutation testing | Mutation report |
| 11 | 9 | Gilded Rose kata | P2 due |
| 12 | 10 | Lab 9 · Codebase safari | Code map and opened PR; P3 starts |
| 13–14 | 11 | Lab 10 · AI refactor with log | Verification log |
| 15 | Review and exam | Practical exam (AI off) and P3 demo | P3 due |

## Working with AI in this course

- **Use AI for:** explaining a compiler error after you have read it yourself; translating Python snippets to compare idioms; listing edge cases for tests (you decide the expected result); drafting boilerplate such as builders and DTOs; mapping an unfamiliar module before you verify it; proposing refactorings that you apply in small, tested steps.
- **Do without AI (drills):** turn off inline completion for Labs 1–4. Each week, do a 45-minute closed-book drill: implement a class with invariants and tests from a written spec, alternating Java and TypeScript. Do predict-the-output drills on equality, overloading and variance. Read a stack trace and name the faulty line. Draw the class diagram of an existing module by hand.
- **Verify AI output by:** compiling with the strictest settings (`javac -Xlint:all -Werror`, `tsc --strict --noUncheckedIndexedAccess`); running the full test suite and a mutation run; writing characterization tests before any AI refactor; checking that every API it uses exists in the official Javadoc or TypeScript docs for your exact version; running Checkstyle or PMD and typescript-eslint; reading the diff hunk by hunk.
- **Where AI still fails here:** in the Stack Overflow 2025 survey, 66% of developers named "AI solutions that are almost right, but not quite" as their top frustration, and a 2025 randomized study by METR found experienced open-source developers took 19% longer with AI tools on their own repositories while believing they were faster (METR has since called those early-2025 results out of date, and its 2026 follow-up was inconclusive, so treat this as a warning about self-assessment, not a law). In this course you will check for and log specific failures: tests generated from the current code that lock in its bugs; `equals` without `hashCode`; `any` or `as` casts added to silence the compiler; `catch` blocks that swallow errors; annotations or APIs from a different JUnit or Java version. Your Lab 10 log records which of these you actually saw.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10, graded on the acceptance criteria in [projects.md](projects.md)) | 25% |
| Projects P1 · P2 · P3 | 10% · 15% · 20% |
| Practical exam, AI off (3 hours) | 30% |

**Mastery gate.** You pass when you can, with AI tools off, take a 300-line module you have never seen (in Java or TypeScript, the examiner chooses), write characterization tests for it, redesign its types so that two listed invalid states no longer compile, and finish with all tests green and a mutation score of at least 70%. You must then explain, line by line, a 100-line AI-generated diff to the same module and say whether you would merge it.

## Industry reality

Java is a mainstay of large backends: Netflix has described running about 2,800 Java applications, mostly on Java 17 and standardised on Spring Boot, and Amazon reported upgrading tens of thousands of production applications from Java 8 or 11 to Java 17 with its Amazon Q Developer assistant. Android moved to Kotlin-first in 2019, but Kotlin runs on the JVM and calls Java libraries, so these ideas carry over directly. TypeScript became the most-used language on GitHub in August 2025 by monthly contributors (GitHub Octoverse), VS Code is written in it, and in July 2026 Microsoft shipped TypeScript 7.0, a compiler rewritten in Go whose full builds are typically 8–12x faster. Large-scale AI refactoring is real and documented: Google reports that in a JUnit 3 to JUnit 4 migration of 5,359 files, about 87% of AI-generated code was committed unchanged after review, and Airbnb reports moving nearly 3,500 React test files from Enzyme to React Testing Library in six weeks with an LLM pipeline, against an estimated 1.5 years by hand. Tests, builds and human review decide what ships. Hiring is adapting too: Canva now runs an AI-assisted coding interview, and Meta was reported in July 2025 to be letting candidates use AI in coding tests.

**Interview questions from this course**

1. *"You overrode `equals` but not `hashCode`. What breaks?"* A strong answer states the contract, shows a `HashMap` lookup failing because the key lands in a different bucket, mentions that records generate both methods, and warns about mutable keys.
2. *"Design the classes for a Splitwise-style expense splitter in 45 minutes."* A strong answer clarifies requirements first, names the entities and their responsibilities, puts an interface where the split rule varies (equal, exact, percentage), keeps money in integer paise or `BigDecimal`, and shows tests for rounding.
3. *"Why is `List<Integer>` not a `List<Number>`, when `Integer[]` is a `Number[]`?"* Covers the unsoundness with a concrete write, `ArrayStoreException`, wildcards and PECS, and compares TypeScript's deliberately unsound array covariance.
4. *"How would you design errors for a payments API client?"* Separates caller mistakes from transient failures, uses typed errors with causes, retries only idempotent operations or uses idempotency keys, never swallows errors, and logs with request IDs.
5. *"An AI agent opened a 600-line refactoring PR. How do you review it?"* Asks for characterization tests first, insists on small commits, runs build, tests and mutation testing, checks API versions and new casts, reads every hunk, and is willing to reject it.

## Resources (free first)

- **Primary courses:** [MIT 6.102 Software Construction](https://web.mit.edu/6.102/www/sp25/) (TypeScript: specs, ADTs, testing, immutability); [Berkeley CS61B](https://fa26.datastructur.es/) (Java); [CMU 17-214 Agentic Software Development](https://cmu-17-214.github.io/f2026/) (design, testing and coding agents, Fall 2026); [University of Helsinki Java Programming MOOC](https://java-programming.mooc.fi/) (no longer updated, but its exercises still work).
- **Official documentation:** [dev.java Learn](https://dev.java/learn/); [Java SE 25 API](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/util/HashMap.html); [JEP 512](https://openjdk.org/jeps/512); [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html); [JUnit User Guide](https://docs.junit.org/current/user-guide/); [Vitest guide](https://vitest.dev/guide/); [typescript-eslint](https://typescript-eslint.io/).
- **Style and design:** [Google Java Style Guide](https://google.github.io/styleguide/javaguide.html); [Google TypeScript Style Guide](https://google.github.io/styleguide/tsguide.html); [Refactoring.Guru code smells](https://refactoring.guru/refactoring/smells).
- **Testing and refactoring tools:** [PIT](https://pitest.org/); [StrykerJS](https://stryker-mutator.io/); [jqwik](https://jqwik.net/); [fast-check](https://fast-check.dev/); [Mockito](https://site.mockito.org/); [AssertJ](https://assertj.github.io/doc/); [OpenRewrite](https://docs.openrewrite.org/); [ts-morph](https://github.com/dsherret/ts-morph); [jscodeshift](https://github.com/facebook/jscodeshift); [Zod](https://zod.dev/).
- **Practice:** [Exercism Java](https://exercism.org/tracks/java) and [TypeScript](https://exercism.org/tracks/typescript) tracks; [Gilded Rose refactoring kata](https://github.com/emilybache/GildedRose-Refactoring-Kata); [Spring PetClinic](https://github.com/spring-projects/spring-petclinic).
- **Paid, optional:** *Effective Java* (3rd ed., Bloch); *Refactoring* (2nd ed., Fowler); *Working Effectively with Legacy Code* (Feathers). Nothing free covers the same ground as compactly.

## Sources

All checked 12 Oct 2026.

- Netflix and Java: Paul Bakker, "How Netflix Really Uses Java", QCon SF 2023 (InfoQ, Feb 2024) — https://www.infoq.com/presentations/netflix-java/
- Amazon Q Developer Java upgrades: AWS DevOps blog (1 Aug 2024) — https://aws.amazon.com/blogs/devops/amazon-q-developer-just-reached-a-260-million-dollar-milestone/
- TypeScript as GitHub's most-used language: GitHub Octoverse 2025 (28 Oct 2025) — https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/
- TypeScript compiler port to Go: "A 10x Faster TypeScript" (Mar 2025) — https://devblogs.microsoft.com/typescript/typescript-native-port/ · "Announcing TypeScript 7.0" (8 Jul 2026) — https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/
- Google, "How is Google using AI for internal code migrations?" (arXiv 2501.06972, Jan 2025) — https://arxiv.org/abs/2501.06972
- Airbnb Engineering, "Accelerating Large-Scale Test Migration with LLMs" (2025) — https://medium.com/airbnb-engineering/accelerating-large-scale-test-migration-with-llms-9565c208023b · InfoQ coverage (28 Mar 2025) — https://www.infoq.com/news/2025/03/airbnb-llm-test-migration/
- Canva, "Yes, You Can Use AI in Our Interviews" (11 Jun 2025) — https://canva.dev/blog/engineering/yes-you-can-use-ai-in-our-interviews · 404 Media on Meta (29 Jul 2025) — https://www.404media.co/meta-is-going-to-let-job-candidates-use-ai-during-coding-tests/
- Android's Kotlin-first approach — https://developer.android.com/kotlin/first
- JDK 25 (GA 16 Sep 2025, LTS per Adoptium and Microsoft) and JEP 512 — https://openjdk.org/projects/jdk/25/ · https://adoptium.net/support/ · https://openjdk.org/jeps/512 · JDK 27 (GA 15 Sep 2026) — https://openjdk.org/projects/jdk/27/
- JUnit 6.0.0 release notes (30 Sep 2025) — https://docs.junit.org/6.0.0/release-notes/ · Vitest 5 (3 Sep 2026) — https://vitest.dev/blog/vitest-5 · Node.js release schedule — https://github.com/nodejs/Release
- Stack Overflow Developer Survey 2025, AI section — https://survey.stackoverflow.co/2025/ai
- METR, "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity" (10 Jul 2025) — https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ · follow-up (24 Feb 2026) — https://metr.org/blog/2026-02-24-uplift-update/
- Gamma, Helm, Johnson, Vlissides, *Design Patterns* (Addison-Wesley, 1994), source of "favour object composition over class inheritance".

_Last reviewed: 2026-10_
