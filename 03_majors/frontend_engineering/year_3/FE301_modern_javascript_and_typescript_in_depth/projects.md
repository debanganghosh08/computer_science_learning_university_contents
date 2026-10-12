# FE301 · Labs and projects

Every lab ships as a repository with tests that run in CI under `tsc --strict`. Lab 5 (Promises/A+) and the type drills in Lab 8 are done without AI assistants. Everywhere else you may use them, but you must keep the AI-error log described in the [syllabus](README.md#working-with-ai-in-this-course).

## Labs

| Lab | Goal | You submit | Time |
|---|---|---|---|
| 1 · Spec detective | Implement `looseEquals` and `toPrimitive` from the ECMAScript algorithms | Code; fuzz report showing agreement with `==` on 10,000 random pairs; 5 annotated spec traces | 4 h |
| 2 · Closures and prototypes | `bind` (including `new` on bound functions), `myNew`, `myInstanceOf`, a `Proxy`-based reactive store | 40+ tests; heap-snapshot screenshot showing what one closure retains | 5 h |
| 3 · Packaging | A library with an `exports` map for Node ESM, CommonJS consumers, bundlers and types | `publint` and "Are the types wrong?" reports with zero problems; a test that imports it four ways | 4 h |
| 4 · Event-loop clinic | 20 ordering puzzles explained by spec step; chunk a 300 ms job | Annotated puzzles; Performance-panel trace showing no task over 50 ms | 5 h |
| 5 · Promises/A+ (no AI) | Implement a promise from scratch | All tests in the Promises/A+ compliance suite pass; a one-page explanation of the resolution procedure | 6 h |
| 6 · Leak hunt | Find three planted leaks in a provided SPA | Three-snapshot report with retained sizes before and after; heap growth under 1 MB after 100 route changes | 5 h |
| 7 · Soundness holes | Show one runtime crash per TypeScript unsoundness class | Crash catalogue (at least 6 classes); the compiler flags or lint rules that catch each one | 4 h |
| 8 · Type-level router (type drills without AI) | Infer params from path templates; typed `navigate()` | 30 passing `expectTypeOf` tests; type-check time under 1 s for 200 routes | 6 h |
| 9 · TypeScript 7 migration | Move a TypeScript 5 project to 7.0 defaults | Migration log by error class; 6.0 vs 7.0 type-check timings; typescript-eslint still working through `@typescript/typescript6` | 5 h |
| 10 · Validation boundary | Zod schemas for every boundary of a sample app; swap to Valibot behind Standard Schema | Fuzz suite of 500 malformed payloads with zero uncaught exceptions; bundle-size comparison | 4 h |

## Projects

### P1 · `safe-fetch`: a typed, cancellable HTTP client (L1, ~6 hours)

**Real-world inspiration:** small fetch wrappers such as ky and ofetch exist because raw `fetch` does not reject on HTTP errors, has no timeout, and returns untyped JSON. Your test target is India's Open Government Data platform ([data.gov.in](https://www.data.gov.in/)), whose APIs need a free key and return paginated JSON. Use any open API if you prefer.

**What to build:** a library of under 300 lines that wraps `fetch` with:
- timeouts (`AbortSignal.timeout`) and caller cancellation (`AbortSignal.any`);
- retries with exponential backoff and full jitter, only for idempotent methods, honouring `Retry-After`;
- response validation through any Standard Schema validator, returning a typed `Result<T, FetchError>` (never throwing on expected failures);
- a discriminated `FetchError` union: `network`, `timeout`, `aborted`, `http` (with status) and `invalid-body` (with schema issues).

**Acceptance criteria:**
- 30 provided tests pass: timeout, abort mid-retry, 429 with `Retry-After`, 500 then success, malformed JSON, schema mismatch and non-JSON content type.
- `tsc` reports zero errors with `strict`, `noUncheckedIndexedAccess` and `exactOptionalPropertyTypes`; the code contains no `any` and no `as` (except one documented, tested cast).
- Bundle size is at most 2 KB minified and gzipped, excluding the validator, enforced by `size-limit` in CI.
- Branch coverage on the retry module is 100%.
- A README example fetches a real data.gov.in dataset with a schema and handles all five error kinds in the UI.

**Stretch goals:** request deduplication for identical in-flight GETs; an `onRetry` hook for telemetry; a version that works in Node 24 and in Cloudflare Workers unchanged.

**What it proves to an employer:** you handle failure, cancellation and untrusted data at the network edge, which is where most production frontend bugs start.

### P2 · A fine-grained reactivity library (L2, ~15 hours)

**Real-world inspiration:** Solid, Preact Signals, Vue's reactivity, Angular signals and Svelte 5 runes all use signals: values that track who reads them and update only dependents. TC39 is considering a common [Signals proposal](https://github.com/tc39/proposal-signals) (Stage 1).

**What to build:** `signal`, `computed`, `effect`, `batch` and `untrack`, plus a 50-line DOM binding that renders a live-filtered list of 10,000 items. Requirements:
- lazy, cached `computed` values;
- glitch-free updates (no intermediate inconsistent states);
- automatic dependency tracking with cleanup;
- disposal that releases every subscription;
- full TypeScript inference (`computed(() => a() + b())` is `Signal<number>` with no annotation).

**Acceptance criteria:**
- **Correctness:** the provided suite of 60 tests passes, including the "diamond" test (A → B, A → C, B + C → D: D recomputes exactly once per change of A) and effect-ordering tests.
- **Memory:** 10,000 create–dispose cycles leave retained heap growth under 200 KB (three-snapshot evidence).
- **Speed:** within 3× of `@preact/signals-core` on the provided benchmark (propagation through 1,000 nodes), with warm-up and 20 runs, reporting median and spread.
- **Types:** 25 `expectTypeOf` tests pass; no `any` in the public API.
- **Explanation:** a design note comparing your push-pull algorithm with the proposal's polyfill.

**Stretch goals:** async computeds with cancellation; a devtools graph view; run the TC39 polyfill's tests against your implementation.

**What it proves to an employer:** you understand the reactivity model under every modern framework, and you can prove correctness, memory safety and speed with numbers.

### P3 · Typed API client generator for real OpenAPI specs (L3, portfolio-grade, ~30 hours)

**Real-world inspiration:** teams generate typed clients from OpenAPI with tools such as openapi-typescript, Orval and Hey API. India's [API Setu](https://apisetu.gov.in/) publishes government and partner APIs in OpenAPI form, and GitHub publishes a large public OpenAPI description of its REST API.

**What to build:** a CLI that reads OpenAPI 3.1 and emits:
- TypeScript types and a tree-shakeable client (one function per operation);
- optional runtime validators via Standard Schema;
- typed errors per status code;
- cursor/offset pagination helpers as async iterators;
- `AbortSignal` support on every call.

Ship it as an npm package with provenance, docs and a migration guide from a hand-written client.

**Acceptance criteria:**
- **Breadth:** generated code type-checks under TypeScript 7.0 with `strict` for three specs: GitHub's REST description, one API Setu specification of your choice, and a provided spec full of edge cases (`oneOf`/`anyOf` discriminators, nullable fields, recursive schemas, `additionalProperties`).
- **Tree-shaking:** importing a single operation adds at most 2 KB gzipped to a Vite 8 production bundle (measured with `size-limit`).
- **Editor performance:** type-checking the full GitHub client takes under 10 s with `tsc` 7.0 on a mid-range laptop; you report `--extendedDiagnostics` output.
- **Runtime safety:** with validation on, 1,000 fuzzed malformed responses produce typed errors with zero uncaught exceptions.
- **Types tested:** at least 50 type tests, including that a misspelt path parameter fails to compile.
- **Evidence of review:** a write-up lists every AI-generated code path you rejected and the test that showed it was wrong.

**Stretch goals:** watch mode with incremental regeneration; MSW mock handlers generated from the same spec (used in FE305); a codemod that moves call sites from the old client to the new one.

**What it proves to an employer:** you can build developer tooling that other engineers depend on, with type-level design, packaging, performance and runtime safety together. This is the core of a senior frontend platform role.

## Feeds into

- [FE302 React and Component Architecture](../FE302_react_and_component_architecture/README.md): P2's signals explain what React's rendering model deliberately does differently.
- [FE305 Frontend Testing and Tooling](../FE305_frontend_testing_and_tooling/README.md): P3's package goes through a full CI, release and supply-chain pipeline.
- [FE401 Full-Stack Frameworks](../../year_4/FE401_full_stack_frameworks_rendering_data_fetching/README.md): validated, typed clients and cancellation at server and client boundaries.
- [FE403 AI-Native Interfaces](../../year_4/FE403_ai_native_interfaces_streaming_generative_ui/README.md): streams, cancellation and schema validation of model output.
