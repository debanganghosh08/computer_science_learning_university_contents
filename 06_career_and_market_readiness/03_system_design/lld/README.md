# Low-level design (LLD)

A low-level design round asks you to turn a small, concrete problem ("design a parking lot", "design an LRU cache") into classes, interfaces and working code in 45–60 minutes. It is common for new graduates and early-career engineers, and many Indian product companies run a "machine coding" variant where you must produce runnable code in 60–90 minutes (analysis; confirm the format with your recruiter). Patterns and principles behind it are taught in [SWE301](../../../03_majors/software_engineering/year_3/SWE301_software_architecture_and_design_patterns/README.md).

## What is evaluated

| Area | Strong signal | Weak signal |
|---|---|---|
| Requirements | Asks 4–6 clarifying questions; writes down scope and non-goals | Starts coding at minute 1 |
| Modelling | Nouns become classes with one responsibility; behaviour lives with the data it uses | One `Manager` class with every method; anaemic data classes plus a god service |
| Extensibility | New vehicle type, new split type or new pricing rule needs a new class, not edits everywhere (open/closed) | `if type == ...` chains spread through the code |
| Correctness | Edge cases handled (full lot, expired lock, rounding money) and tested | Happy path only |
| Concurrency | Says where races occur and how they are prevented (locks, atomic operations, single writer) | Ignores two users booking the same seat |
| Code quality | Readable names, small methods, types, errors as exceptions with meaning | Clever one-liners; magic numbers |
| Communication | Explains trade-offs while coding | Silent typing |

## A method that fits in 45 minutes

1. **Clarify (5 min).** Actors, core use cases, scale (one process or many), concurrency, what is out of scope.
2. **Entities and relationships (5 min).** List nouns and verbs. Draw a class diagram with the 5–8 most important classes.
3. **Interfaces first (5 min).** Public methods with types; where you need a strategy or state machine.
4. **Code the core path (20 min).** One working flow end to end, with an in-memory store behind an interface.
5. **Test and extend (10 min).** A few asserts for edge cases; then talk through one extension and one concurrency issue.

## Patterns that come up again and again

| Pattern | Typical use in these problems |
|---|---|
| Strategy | Spot allocation, pricing, split types, elevator scheduling, rate-limit algorithms |
| State | Elevator, booking lifecycle, order lifecycle |
| Observer / pub-sub | Display boards, notifications, log appenders |
| Composite | File system (directories contain files and directories) |
| Factory | Creating vehicles, splits or limiters from configuration |
| Repository | Hide storage behind an interface so in-memory can become a database |
| Singleton (use sparingly) | One lot or one system instance; prefer passing dependencies explicitly |

## The 8 problems

| # | Problem | Key ideas |
|---|---|---|
| 01 | [Parking lot](01_parking_lot.md) | Strategy for allocation and pricing; spot types; thread-safe allocation |
| 02 | [LRU cache](02_lru_cache.md) | Hash map + doubly linked list, O(1) operations, locking |
| 03 | [Rate limiter class](03_rate_limiter_class.md) | Token bucket and sliding window behind one interface; injectable clock |
| 04 | [Splitwise](04_splitwise.md) | Split strategies; integer money; debt simplification |
| 05 | [Elevator](05_elevator.md) | State per car; dispatch strategy; LOOK scheduling |
| 06 | [BookMyShow seat locking](06_bookmyshow_seat_locking.md) | All-or-nothing locks with TTL; idempotent confirmation; races |
| 07 | [Logger and pub-sub](07_logger_pubsub.md) | Log-structured topic, consumer offsets, appenders as subscribers |
| 08 | [In-memory file system](08_in_memory_file_system.md) | Composite pattern; path resolution; errors |

All Python skeletons use only the standard library and end with a few `assert` checks; they run with `python3 file.py` once copied out. They are deliberately compact: in an interview, aim for this size, then extend on request.

_Last reviewed: 2026-10_
