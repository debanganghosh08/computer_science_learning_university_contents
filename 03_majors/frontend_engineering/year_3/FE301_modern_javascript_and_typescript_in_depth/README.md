# FE301 · Modern JavaScript and TypeScript in Depth

| Year · Semester | Credits | Level | Prerequisites | Leads to |
|---|---|---|---|---|
| 3 · 5 | 4 (≈ 120 hours) | L2 → L3 | [FND114](../../../../01_year_1_foundations/semester_2/FND114_web_foundations_http_html_css_and_javascript/README.md), [CS205](../../../../02_year_2_core_computer_science/semester_3/CS205_software_engineering_i_design_testing/README.md) | [FE401](../../year_4/FE401_full_stack_frameworks_rendering_data_fetching/README.md), [FE302](../FE302_react_and_component_architecture/README.md), [FE305](../FE305_frontend_testing_and_tooling/README.md), [FE404](../../year_4/FE404_frontend_system_design_at_scale/README.md) |

Part of the [Frontend Engineering major](../../README.md). FND114 taught closures, promises and event-loop ordering at the level of "predict the output". FND111 introduced TypeScript syntax. This course goes underneath both: the specification, the engine, the type checker and the module system. It uses the parsing and type-checking ideas from [CS216](../../../../02_year_2_core_computer_science/semester_4/CS216_programming_languages_compilers_and_interpreters/README.md).

## Why this course matters now

TypeScript became the most-used language on GitHub by monthly contributors in August 2025, ahead of Python and JavaScript (Octoverse 2025). In July 2026 Microsoft shipped TypeScript 7.0, a native port of the compiler written in Go. It reports full builds typically 8–12× faster than 6.0. TypeScript 6.0 had already changed long-standing defaults (`strict` on, `types` empty, `module` set to `esnext`), and 7.0 removes options such as `baseUrl` and `moduleResolution: node10`, so most real codebases have migration work to do this year. Coding assistants such as Claude Code, GitHub Copilot and Cursor write fluent TypeScript. In the 2026 Stack Overflow survey, 48.0% of respondents said they trust AI output only when they can easily verify it. In this language, verifying means knowing the answers to some hard questions. What will the event loop do? Which closure keeps megabytes alive? Where is the type system deliberately unsound? Which `as` cast hides a runtime crash? Those are the places where both the type checker and a quick read say "fine" and production says otherwise.

## Learning outcomes

By the end you can:

1. **Explain** any surprising JavaScript result (coercion, equality, `this`, ordering) by citing the ECMAScript or HTML specification algorithm that produces it.
2. **Implement** `bind`, `new`, `instanceof`, a Promises/A+-compliant promise, `debounce`/`throttle` and a concurrency-limited task pool from scratch, each with tests.
3. **Predict and control** scheduling across tasks, microtasks and rendering. Keep long work off the main thread or split it.
4. **Find and fix** memory leaks with heap snapshots and allocation timelines, and show retained-size evidence before and after.
5. **Design** types with generics, conditional, mapped and template-literal types that catch real bugs, and **test** those types.
6. **Configure** `tsconfig` for an app, a library and a Node service under TypeScript 6/7 defaults, and **publish** a typed package that works in ESM, bundlers and Node.
7. **Validate** every trust boundary (network, storage, URL, environment, LLM output) at runtime with schemas, deriving static types from them.
8. **Audit** AI-generated JavaScript and TypeScript for unsound casts, unhandled rejections, race conditions and leaks.

## Chapters and lessons

### Chapter 1 · Values, types and the specification (week 1)
| Lesson | What you learn | Practice |
|---|---|---|
| 1.1 Reading the spec | ECMAScript structure: abstract operations, completion records, the `?`/`!` shorthand; where to find `ToPrimitive`, `IsLooselyEqual`, `SameValueZero` | Trace `[] + {}` and `[0] == false` step by step through tc39.es/ecma262 |
| 1.2 Numbers | IEEE 754 doubles, `0.1 + 0.2`, `Number.MAX_SAFE_INTEGER`, `-0`, `NaN`; `BigInt`; money as integer paise, never floats | Write a rupee formatter that stores paise as `bigint` and formats with `Intl.NumberFormat('en-IN')` (lakh/crore grouping) |
| 1.3 Strings and text | UTF-16 code units vs code points vs grapheme clusters; why `"नमस्ते".length` is 6; `Intl.Segmenter` (Baseline since April 2024) | Truncate Hindi, Tamil and emoji strings to 10 user-perceived characters without breaking a conjunct |
| 1.4 Equality and collections | `===`, `Object.is`, `SameValueZero` in `Map`/`Set`/`includes`; ES2025 `Set` methods (`union`, `intersection`) | Implement `looseEquals` from the spec; fuzz it against `==` on 10,000 random pairs |

**Check your understanding:** Why does `[NaN].includes(NaN)` return `true` while `[NaN].indexOf(NaN)` returns `-1`? Why is "number of characters" ambiguous for a Bengali name, and which answer does a form's `maxlength` use? When would `Object.is` and `===` disagree in real code?

### Chapter 2 · Scope, closures, `this` and prototypes (week 2)
| Lesson | What you learn | Practice |
|---|---|---|
| 2.1 Environments | Lexical environments, temporal dead zone, block scope, why `var` in a loop shares one binding | Explain and fix the classic `setTimeout` loop bug three ways |
| 2.2 Closures as objects | Closures capture bindings, not values; module pattern; closures and memory retention | Build a private counter; show in a heap snapshot what the closure keeps alive |
| 2.3 `this` | Default, implicit, explicit (`call`/`apply`/`bind`) and `new` binding; arrow functions; class methods passed as callbacks | Implement `Function.prototype.bind`, including `new` on a bound function |
| 2.4 Prototypes and classes | `[[Prototype]]` chain, `Object.create`, class desugaring, `#private` fields, `static` blocks, `super` | Implement `myNew` and `myInstanceOf`; compare memory of 100,000 objects with methods on the prototype vs as arrow-function fields |
| 2.5 Meta-programming | Property descriptors, getters/setters, `Proxy` and `Reflect` (how Vue's reactivity tracks reads) | Build a 40-line reactive store with `Proxy` that logs dependency reads |

**Check your understanding:** A React event handler loses `this` and a Vue `Proxy` breaks `===` comparison with the raw object. Explain both from first principles. Why do arrow-function class fields cost memory per instance? When is a closure-based "private" variable better than `#private`, and when is it worse?

### Chapter 3 · Modules and packages (week 3)
| Lesson | What you learn | Practice |
|---|---|---|
| 3.1 ES modules | Static structure, live bindings, module records, linking and evaluation order, cyclic imports, top-level `await` | Create a cycle that yields `undefined` at import time; fix it by restructuring |
| 3.2 CommonJS and interop | `require` vs `import`, default-export interop, the dual-package hazard, Node's `require(esm)` support | Publish a package that is loaded twice as two copies; detect it and fix it |
| 3.3 `package.json` exports | `exports` and `imports` maps, conditions (`types`, `import`, `browser`, `development`), `sideEffects` | Write an `exports` map serving Node, bundlers and types; verify with `publint` and "Are the types wrong?" |
| 3.4 In the browser | Import maps (Baseline 2023), `modulepreload`, JSON modules with import attributes (`with { type: 'json' }`) | Ship a no-build app using import maps; measure the request waterfall in DevTools |

**Check your understanding:** Why can a bundler tree-shake ES modules but not most CommonJS? What breaks when two copies of a library each hold their own singleton? Why does top-level `await` in a deeply imported module delay the whole app?

### Chapter 4 · The event loop in depth (week 4)
| Lesson | What you learn | Practice |
|---|---|---|
| 4.1 The processing model | HTML spec event loop: task queues, microtask checkpoint, "update the rendering" steps, `requestAnimationFrame` timing | Annotate 20 ordering puzzles with the exact spec step that explains each line |
| 4.2 Starvation and long tasks | Microtask loops that block rendering; tasks over 50 ms; link to INP (FE304) | Build a page that freezes with recursive `queueMicrotask`, then fix it by yielding |
| 4.3 Yielding and scheduling | `setTimeout` clamping, `MessageChannel`, `requestIdleCallback` and `scheduler.postTask` (neither Baseline as of Oct 2026); feature detection | Split a 300 ms JSON-processing job into chunks that keep input latency under 50 ms |
| 4.4 Node vs browser | libuv phases, `process.nextTick`, `setImmediate`; why server and client ordering differ | Run the same file in Node 24 and Chrome; explain every difference |
| 4.5 Workers | Dedicated workers, `postMessage` and structured clone cost, transferables, `SharedArrayBuffer` and cross-origin isolation | Move Markdown parsing of a 2 MB file into a worker; compare main-thread blocking time |

**Check your understanding:** Why can a page whose code is "all async" still be unresponsive? What is the difference between yielding with `await Promise.resolve()` and yielding with `setTimeout`? When does moving work to a worker make things slower?

### Chapter 5 · Async patterns and cancellation (weeks 5–6)
| Lesson | What you learn | Practice |
|---|---|---|
| 5.1 Promise internals | The resolution procedure, thenables, why `then` callbacks are always async, `Promise.withResolvers` | Implement a promise that passes the Promises/A+ compliance suite (no AI) |
| 5.2 Errors | `async` stack traces, unhandled rejections in browser and Node, `Error.cause`, `AggregateError` | Make every rejection in a sample app either handled or reported with context |
| 5.3 Cancellation | `AbortController`, `AbortSignal.timeout`, `AbortSignal.any`, passing signals through layers | Add cancellation to a three-step upload pipeline so that "Cancel" stops all network work |
| 5.4 Concurrency control | Semaphores and pools, `mapLimit`, retries with exponential backoff and full jitter, idempotency for retried writes | Write a pool that keeps at most 4 requests in flight and respects `Retry-After` |
| 5.5 UI races | Stale responses ("last request wins"), out-of-order streams, optimistic updates and rollback | Fix a search box that shows results for "ban" after the user typed "bangalore" |
| 5.6 Streams and async iteration | `ReadableStream`, `for await`, `TextDecoderStream`, backpressure (preview of FE403's streaming UIs) | Parse a streamed NDJSON response and render rows as they arrive |

**Check your understanding:** Why is `await` inside a `forEach` a bug, and what are the two correct fixes with different semantics? What can go wrong when you retry a `POST` with backoff? How do you prove that a cancelled request did not update the UI?

### Chapter 6 · Memory, engines and leaks (week 6)
| Lesson | What you learn | Practice |
|---|---|---|
| 6.1 How V8 runs your code | Ignition, Sparkplug, Maglev and TurboFan tiers; hidden classes (shapes) and inline caches; deoptimisation | Show a 5× slowdown from megamorphic property access and remove it |
| 6.2 Garbage collection | Reachability, generational GC, why "memory leak" in JS means "still reachable" | Predict which of 8 objects are collectable; confirm with a heap snapshot |
| 6.3 Leak patterns | Detached DOM nodes, forgotten listeners and timers, unbounded caches, closures over large data, global stores | Find three planted leaks in an SPA using the DevTools Memory panel's three-snapshot technique |
| 6.4 Weak references | `WeakMap`, `WeakSet`, `WeakRef`, `FinalizationRegistry` and why finalisers must not hold correctness logic | Build a cache that cannot grow without bound; test that entries disappear |
| 6.5 Honest benchmarking | JIT warm-up, dead-code elimination, `performance.now()` resolution, variance and confidence | Re-run a "X is 10× faster" claim from a blog post and report what you actually find |

**Check your understanding:** Why does a single-page app leak more easily than a multi-page site? A heap snapshot shows 40,000 `Detached HTMLDivElement` objects: what is your next step? Why does a micro-benchmark that shows a big speed-up often vanish in a real app?

### Chapter 7 · TypeScript I: structural types, narrowing and soundness (week 7)
| Lesson | What you learn | Practice |
|---|---|---|
| 7.1 Structural typing | Assignability, excess property checks, `interface` vs `type`, declaration merging | Find 5 cases where two "different" types are interchangeable and decide whether that is a bug |
| 7.2 Narrowing | Control-flow analysis, `typeof`/`in`/`instanceof`, discriminated unions, user-defined type predicates, `asserts` functions | Model a payment state (`created` → `authorised` → `captured` / `failed`) so that invalid transitions do not compile |
| 7.3 `unknown`, `any`, `never` | Top and bottom types, exhaustiveness checks, `satisfies`, `as const` | Replace every `any` in a 500-line file; count how many hidden bugs appear |
| 7.4 Where TypeScript is unsound | Type assertions, array covariance, method parameter bivariance, unchecked index access, `!` | Write one runtime crash per hole that type-checks cleanly; turn on `noUncheckedIndexedAccess` and `exactOptionalPropertyTypes` and count the fixes |

**Check your understanding:** Why did TypeScript choose structural over nominal typing, and how do branded types bring back nominal safety? What does `satisfies` give you that a type annotation does not? Why is a type predicate that lies worse than an `as` cast?

### Chapter 8 · TypeScript II: generics and type-level programming (weeks 8–9)
| Lesson | What you learn | Practice |
|---|---|---|
| 8.1 Generics that earn their place | Inference sites, constraints, defaults, `const` type parameters, `NoInfer`; when a generic is just noise | Type `groupBy`, `pick` and a typed `fetchJson<T>`, then decide which generics to delete |
| 8.2 Conditional types | Distributivity over unions, `infer`, built-ins (`ReturnType`, `Awaited`, `Parameters`) from scratch | Implement `DeepPartial`, `UnionToIntersection` and `Awaited` yourself |
| 8.3 Mapped and template-literal types | Key remapping with `as`, modifiers, template-literal parsing | Type a router so that `"/trains/:trainNo/coach/:coachId"` yields `{ trainNo: string; coachId: string }` |
| 8.4 Variance | Covariance, contravariance, `in`/`out` annotations; why event handler types bite | Explain a variance error in a typed event emitter, then fix it |
| 8.5 Testing and profiling types | `expectTypeOf` in Vitest, `tsd`; `--extendedDiagnostics`, `--generateTrace`; instantiation-depth limits | Write 30 type tests for your router; cut type-check time of a slow generic by half |

**Check your understanding:** When should a library expose a complex generic, and when should it expose overloads? Why does `T extends any ? X : Y` behave differently from `[T] extends [any] ? X : Y`? How do you know a type-level "improvement" did not make the editor slower for every user?

### Chapter 9 · `tsconfig`, compilers and publishing (week 10)
| Lesson | What you learn | Practice |
|---|---|---|
| 9.1 TypeScript 6 and 7 defaults | `strict` on, `types: []`, `rootDir: ./`, `module: esnext`; removed `baseUrl`, `moduleResolution: node10`, `target: es5` | Migrate a TypeScript 5 project to 7.0; record every error class and its fix |
| 9.2 Module resolution | `bundler` vs `nodenext`; `verbatimModuleSyntax`, `isolatedModules`, `erasableSyntaxOnly` | Configure one repo for a Vite app, a Node service and a library, and explain each choice |
| 9.3 Running TypeScript directly | Node's type stripping (stable since v24.12; enums, namespaces with values and parameter properties unsupported); `tsx`; transpile-only bundlers vs type-checking | Run a Node service from `.ts` files with no build step; add a CI type-check job |
| 9.4 Native compiler and tooling | `tsc` 7 (Go), `--checkers`, `--builders`; no stable programmatic API in 7.0, so tools such as typescript-eslint keep 6.0 through `@typescript/typescript6` | Measure 6.0 vs 7.0 type-check time on a 50k-line repository; set up the side-by-side install |
| 9.5 Publishing typed libraries | `.d.ts` generation, declaration maps, project references, `exports` with `types`, provenance on npm | Publish a scoped package with types that "Are the types wrong?" reports clean |

**Check your understanding:** Why can a bundler compile TypeScript in milliseconds while `tsc` takes seconds? Why does `erasableSyntaxOnly` matter for Node's type stripping? What breaks for editor tooling if a team jumps to TypeScript 7.0 today in a Vue or Svelte project?

### Chapter 10 · Runtime validation at trust boundaries (week 11)
| Lesson | What you learn | Practice |
|---|---|---|
| 10.1 Types vanish at runtime | "Parse, don't validate"; every boundary that lies: `fetch`, `JSON.parse`, `localStorage`, `URLSearchParams`, `postMessage`, env vars | List every boundary in a sample app and the type each one falsely claims |
| 10.2 Zod 4 in depth | Schemas, `z.infer`, discriminated unions, refinements, transforms, coercion, error formatting; Zod Mini for bundle size | Validate an API response; render field-level errors in Hindi and English |
| 10.3 Standard Schema | One interface implemented by Zod, Valibot and ArkType, so forms and routers accept any of them; bundle and speed trade-offs | Swap Zod for Valibot behind Standard Schema; compare bundle bytes with `size-limit` |
| 10.4 Validating model output | Structured LLM output is untrusted input; schema-constrained generation still needs runtime checks and repair loops | Validate 200 generated JSON objects; log failure classes and retry strategy |

**Check your understanding:** Why is `const data = (await res.json()) as User` a bug even when the API "always" returns users? Where do you validate in a server-rendered app: server, client or both? What does a schema library cost on a low-end phone, and how do you measure it?

### Chapter 11 · The evolving language, migration and review (weeks 12–14)
| Lesson | What you learn | Practice |
|---|---|---|
| 11.1 How JavaScript changes | TC39 stages 0–4, test262, browser intents to ship; reading a proposal repository | Summarise one Stage 3 proposal in 300 words with a code example |
| 11.2 What is safe to use | MDN Baseline ("newly" vs "widely available"), web-features data; Temporal and explicit resource management (`using`) are not Baseline as of Oct 2026; iterator helpers are (March 2025) | Write a feature-support policy for a team targeting low-end Android in India |
| 11.3 Decorators and signals | Stage 3 decorators (implemented in TypeScript 5.0+), the TC39 Signals proposal (Stage 1) and why frameworks converged on signals | Implement a 60-line signal/computed/effect library; compare it with the proposal's polyfill |
| 11.4 Migrating and reviewing real code | `allowJs`/`checkJs`, per-folder strictness, `@ts-expect-error` budgets; a review checklist for AI-written code (casts, `!`, floating promises, missing abort, unbounded caches, `any` leaks) | Migrate 2,000 lines of JavaScript to strict TypeScript with zero `any`; review three AI-generated pull requests and file each finding with a failing test |

**Check your understanding:** Why might a team ban a Stage 3 feature that already works in Chrome? How do you migrate a codebase to strict mode without freezing feature work? Which lint rules catch floating promises and unsafe `any`, and what do they miss?

## Weekly rhythm

| Week | Chapter | Lab | Deliverable |
|---|---|---|---|
| 1 | 1 | Lab 1 · Spec detective | `looseEquals` with fuzz report |
| 2 | 2 | Lab 2 · Closures and prototypes | `bind`, `new`, `instanceof` with tests |
| 3 | 3 | Lab 3 · Packaging | Dual-format package; **P1 starts** |
| 4 | 4 | Lab 4 · Event-loop clinic | Annotated puzzles; chunked job |
| 5 | 5 | Lab 5 · Promises/A+ (no AI) | Passing suite; **P1 due** |
| 6 | 5–6 | Lab 6 · Leak hunt | Heap-snapshot report |
| 7 | 7 | Lab 7 · Soundness holes | Crash catalogue |
| 8 | 8 | Lab 8 · Type-level router | Type tests; mid-term (AI off) |
| 9 | 8 | Lab 8 (cont.) | **P2 due** |
| 10 | 9 | Lab 9 · TypeScript 7 migration | Migration log, timing data |
| 11 | 10 | Lab 10 · Validation boundary | Schema suite |
| 12 | 11 | Proposal summary | Feature-support policy; **P3 starts** |
| 13 | 11 | Migration sprint | Migrated module |
| 14 | 11 | AI code review | **P3 due** |
| 15 | Review | Oral defence of P3 | Final exam (AI off) |

## Working with AI in this course

- **Use AI for:** explaining a spec algorithm after you have tried to read it; generating fuzz inputs and edge cases; drafting type tests; converting JSDoc to TypeScript; first drafts of Zod schemas from sample JSON, which you then check against real responses. Claude Code, GitHub Copilot, Cursor and OpenAI Codex all work in this course's repositories. Chrome DevTools' AI assistance can explain a heap snapshot or a trace.
- **Do without AI (drills):** the Promises/A+ implementation; `bind`/`new`/`instanceof`; weekly event-loop and coercion puzzles on paper; type challenges at "medium" level from type-challenges; the mid-term and final. You cannot audit an `as` cast or a microtask ordering bug that you cannot reason about alone.
- **Verify AI output by:** running `tsc` with `strict`, `noUncheckedIndexedAccess` and `exactOptionalPropertyTypes`; typescript-eslint's `no-floating-promises` and `no-unsafe-*` rules; fuzz tests against a reference implementation; heap snapshots after 100 mount/unmount cycles; checking every API claim against MDN, the spec or Baseline data rather than the model's memory.
- **Where AI still fails here (collect your own evidence):** keep a log of every AI suggestion that type-checks but is wrong. Common classes to look for are `as` casts on `JSON.parse` output, `!` on values that can be `null`, `await` in `forEach`, missing `AbortSignal` propagation, listeners added without removal, and confident claims about which features are "supported everywhere". Models trained before July 2026 also tend to suggest `baseUrl` and `moduleResolution: node`, which TypeScript 7.0 rejects. Your log is part of the P3 assessment.

## Assessment and mastery gate

| Component | Weight |
|---|---|
| Labs (10) | 25% |
| Projects P1 · P2 · P3 | 10% · 15% · 20% |
| Mid-term (AI off, 90 min) | 10% |
| Final exam (AI off, 3 h) and P3 oral defence | 20% |

**Mastery gate.** You pass when you can, with AI off: (1) implement a cancellable, concurrency-limited `mapLimit` with retries, plus its tests, in 45 minutes; (2) explain the output of an unseen 15-line event-loop puzzle by naming the spec steps; (3) find a planted memory leak in a provided app within 20 minutes using heap snapshots; (4) type a provided untyped module under `strict` with no `any` and no unchecked casts, with type tests.

## Industry reality

TypeScript is the default for new frontend work. The TypeScript 7.0 announcement reports build-time speed-ups of 7.7–11.9× on the VS Code, Sentry, Bluesky, Playwright and tldraw codebases. React, Angular, Vue, Svelte and Next.js all document TypeScript-first setups. Node.js runs `.ts` files directly through type stripping, stable since v24.12.0. Runtime schemas (Zod, Valibot, ArkType, unified by Standard Schema) sit at the edge of most production apps. Frontend interviews in India and elsewhere still open with JavaScript fundamentals ([FE market page](../../../../06_career_and_market_readiness/01_market_map/roles/FE_frontend_engineering.md)). One self-reported senior frontend loop at an Indian product company (September 2025) included a round that asked the candidate to implement a custom `Promise` ([candidate report](https://www.jointaro.com/interviews/companies/flipkart/experiences/senior-frontend-engineer-india-september-16-2025-declined-offer-positive-f89c4ee4/)).

**Interview questions from this course**

1. *Implement `debounce` with `leading`, `trailing` and `cancel`.* A strong answer handles `this` and arguments correctly, clears timers on cancel, and explains when leading-edge firing is wrong for a search box. It tests with fake timers and compares debounce with throttle using a scroll example.
2. *Implement `Promise.all`, then a version with a concurrency limit.* A strong answer preserves result order and rejects fast on the first error (or settles all, if asked), handles empty input and non-promise values, and adds abort support. It states the time and memory behaviour.
3. *What does this code log, and why?* (mixing `setTimeout`, `queueMicrotask`, `await`, `requestAnimationFrame`). A strong answer names tasks, microtask checkpoints and rendering steps, and explains why rendering cannot happen between microtasks. It links long tasks to INP.
4. *Explain prototypal inheritance and implement `new`.* A strong answer covers `[[Prototype]]` and `Object.create`, returning an object from a constructor, `instanceof` via `Symbol.hasInstance`, and the memory difference between prototype methods and per-instance arrow functions.
5. *Type `get(obj, "a.b.c")` so that the return type is correct.* A strong answer uses template-literal parsing with recursive conditional types, handles optional properties and arrays, and admits the limits (recursion depth, editor performance). It offers a simpler overload-based alternative.

## Resources (free first)

- **Language:** [javascript.info](https://javascript.info/); Kyle Simpson, [You Don't Know JS Yet](https://github.com/getify/You-Dont-Know-JS); Axel Rauschmayer's free online books at [exploringjs.com](https://exploringjs.com/); [MDN JavaScript reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript); [ECMAScript specification](https://tc39.es/ecma262/).
- **Event loop and engines:** [HTML spec: event loops](https://html.spec.whatwg.org/multipage/webappapis.html#event-loops); Jake Archibald, [Tasks, microtasks, queues and schedules](https://jakearchibald.com/2015/tasks-microtasks-queues-and-schedules/); [V8 blog](https://v8.dev/blog), especially [Fast properties](https://v8.dev/blog/fast-properties); Mathias Bynens, [Shapes and inline caches](https://mathiasbynens.be/notes/shapes-ics); [Chrome DevTools: memory problems](https://developer.chrome.com/docs/devtools/memory-problems); [MDN memory management](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Memory_management).
- **TypeScript:** [Handbook](https://www.typescriptlang.org/docs/handbook/intro.html); [tsconfig reference](https://www.typescriptlang.org/tsconfig/); [typescript-go repository](https://github.com/microsoft/typescript-go); [type-challenges](https://github.com/type-challenges/type-challenges); Matt Pocock, [Total TypeScript Essentials](https://www.totaltypescript.com/books/total-typescript-essentials) (free online).
- **Validation and runtime:** [Zod](https://zod.dev/); [Valibot](https://valibot.dev/); [Standard Schema](https://standardschema.dev/); [Node.js TypeScript support](https://nodejs.org/api/typescript.html); [Node.js modules](https://nodejs.org/api/modules.html).
- **Proposals and support data:** [TC39 process](https://tc39.es/process-document/); [TC39 proposals](https://github.com/tc39/proposals); [Temporal](https://github.com/tc39/proposal-temporal); [Signals proposal](https://github.com/tc39/proposal-signals); [web-features / Baseline](https://web-platform-dx.github.io/web-features/); [Promises/A+](https://promisesaplus.com/) and its [test suite](https://github.com/promises-aplus/promises-tests).
- **Paid, optional:** Dan Vanderkam, *Effective TypeScript*, 2nd ed. (O'Reilly, 2024). The free resources above cover the syllabus.

## Sources

All checked 12 Oct 2026.

- GitHub, Octoverse 2025 (TypeScript most-used by monthly contributors, Aug 2025) — https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/
- Microsoft, Announcing TypeScript 7.0 (8 Jul 2026: speed-ups, defaults inherited from 6.0, removed options, no stable API in 7.0, `@typescript/typescript6`) — https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/ · TypeScript 6.0 (23 Mar 2026) — https://devblogs.microsoft.com/typescript/announcing-typescript-6-0/
- Stack Overflow, 2026 Developer Survey, AI section (48.0% trust only when easily verifiable) — https://survey.stackoverflow.co/2026/ai/data
- Node.js documentation v26, TypeScript type stripping (stable in v24.12.0/v25.2.0; unsupported syntax) — https://nodejs.org/api/typescript.html
- web-features 3.42.0 Baseline data (Intl.Segmenter Apr 2024; iterator methods Mar 2025; Temporal, explicit resource management, `requestIdleCallback`, `scheduler` not Baseline) — https://web-platform-dx.github.io/web-features/
- npm registry latest versions on 12 Oct 2026: typescript 7.0.2, zod 4.6.6, valibot 1.5.0 — https://registry.npmjs.org/
- Candidate interview report, senior frontend engineer, India (self-reported, Sep 2025) — https://www.jointaro.com/interviews/companies/flipkart/experiences/senior-frontend-engineer-india-september-16-2025-declined-offer-positive-f89c4ee4/

_Last reviewed: 2026-10_
