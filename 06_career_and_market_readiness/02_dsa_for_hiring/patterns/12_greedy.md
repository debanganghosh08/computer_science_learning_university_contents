# DSA for hiring · Pattern 12 · Greedy

| Theory first | Time | Problems | Must-do |
|---|---|---|---|
| [CS201](../../../02_year_2_core_computer_science/semester_3/CS201_algorithms_and_complexity/README.md) chapter 4 (exchange arguments, when greedy fails) | ~8 hours | 12 | 4 |

A greedy algorithm commits to the locally best choice and never revisits it. It is the fastest pattern to code and the easiest to get wrong, because a plausible greedy rule can pass every sample and still be false. In an interview, a greedy answer is only as good as the one-paragraph argument behind it: an **exchange argument** (any optimal solution can be changed into the greedy one without getting worse) or **greedy stays ahead** (after every step, greedy is at least as far along as any other solution).

## Recognise it

| When you see… | Think… |
|---|---|
| "can you reach the end", "minimum jumps" | track the farthest reachable index; BFS layers without a queue |
| a circular route with gains and costs | if the total is non-negative a start exists; restart after every deficit |
| "partition so each item appears in one part" | last occurrence of each item decides the cut |
| "match the smallest with the smallest that fits" | sort both sides, two pointers |
| "each element must beat its neighbours" (candies, ratings) | two passes, one per direction |
| "fewest stops/refuels", "maximise with a budget of picks" | greedy with a heap of passed options |
| a greedy rule you just invented | try to break it with a brute force on all small inputs before coding |

**Not this pattern when** a small counterexample exists: coin change with coins `{1, 3, 4}`, 0/1 knapsack, longest path. Those need [dynamic programming](19_dp_1d.md).

## Core templates

**Farthest reach.**

```python
import heapq
from collections import Counter


def can_jump(nums):
    reach = 0
    for i, x in enumerate(nums):
        if i > reach:
            return False                    # i is unreachable
        reach = max(reach, i + x)
    return True


def jump(nums):                             # minimum jumps; BFS by layers
    jumps = cur_end = farthest = 0
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if i == cur_end:                    # layer finished: one more jump
            jumps += 1
            cur_end = farthest
    return jumps
```

**Circular gains: restart after a deficit.** If the tank goes negative between start and i, no station in that range can be the start.

```python
def can_complete_circuit(gas, cost):
    if sum(gas) < sum(cost):
        return -1
    start = tank = 0
    for i in range(len(gas)):
        tank += gas[i] - cost[i]
        if tank < 0:
            start, tank = i + 1, 0
    return start
```

**Cut at the last occurrence.**

```python
def partition_labels(s):
    last = {ch: i for i, ch in enumerate(s)}
    out, start, end = [], 0, 0
    for i, ch in enumerate(s):
        end = max(end, last[ch])
        if i == end:
            out.append(end - start + 1)
            start = i + 1
    return out
```

**Smallest first (Hand of Straights).** The smallest remaining card must start a group, so the choice is forced.

```python
def is_n_straight_hand(hand, size):
    if len(hand) % size:
        return False
    count = Counter(hand)
    for x in sorted(count):
        c = count[x]
        if c:
            for y in range(x, x + size):
                if count[y] < c:
                    return False
                count[y] -= c
    return True
```

**A range of possibilities (Valid Parenthesis String).** Track the minimum and maximum number of open brackets; `*` widens the range.

```python
def check_valid_string(s):
    lo = hi = 0
    for ch in s:
        if ch == "(":
            lo, hi = lo + 1, hi + 1
        elif ch == ")":
            lo, hi = lo - 1, hi - 1
        else:
            lo, hi = lo - 1, hi + 1
        if hi < 0:
            return False                    # too many ')' even if every * is '('
        lo = max(lo, 0)
    return lo == 0
```

**Two passes (Candy).** Left-to-right enforces the left neighbour rule, right-to-left the right neighbour rule; taking the max satisfies both.

```python
def candy(ratings):
    n = len(ratings)
    c = [1] * n
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            c[i] = c[i - 1] + 1
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            c[i] = max(c[i], c[i + 1] + 1)
    return sum(c)
```

**Greedy with a heap of passed options (Minimum Number of Refueling Stops).** Drive as far as possible; when stuck, retroactively refuel at the biggest station already passed.

```python
def min_refuel_stops(target, fuel, stations):
    passed, stops, i = [], 0, 0
    while fuel < target:
        while i < len(stations) and stations[i][0] <= fuel:
            heapq.heappush(passed, -stations[i][1])
            i += 1
        if not passed:
            return -1
        fuel -= heapq.heappop(passed)
        stops += 1
    return stops
```

## Complexity

Most greedy solutions are O(n) after an O(n log n) sort. Hand of Straights is O(n log n) for sorting the distinct values plus O(n · size) for the inner loop in the worst case. Heap-based greedy (refuelling) is O(n log n).

## Common bugs

1. No proof. A greedy rule that "obviously" works fails on an input you did not try (exercise 1).
2. Sorting by the wrong key (start instead of end, value instead of ratio).
3. One pass where two directions constrain the answer (exercise 2).
4. Jump Game II counting a jump at the last index (loop to `n - 2`).
5. Forgetting the global feasibility check (Gas Station's total) and returning a start that cannot finish.
6. Mistaking a greedy for DP and over-engineering: if you can prove the exchange argument, the O(n) answer is the expected one.

## Problems (easy → hard)

Lists: **B75** Blind 75 · **N150** NeetCode 150 · **N250** NeetCode 250. ★ = in the [must-do 100](../problem_list.md).

| # | Problem | Level | What it teaches | Lists |
|---|---|---|---|---|
| 1 | [Assign Cookies](https://leetcode.com/problems/assign-cookies/) | Easy | sort both, smallest cookie that satisfies | |
| 2 | [Lemonade Change](https://leetcode.com/problems/lemonade-change/) | Easy | give the largest note first | N250 |
| 3 | ★ [Jump Game](https://leetcode.com/problems/jump-game/) | Medium | farthest reach | B75 · N150 · N250 |
| 4 | ★ [Jump Game II](https://leetcode.com/problems/jump-game-ii/) | Medium | implicit BFS layers | N150 · N250 |
| 5 | ★ [Gas Station](https://leetcode.com/problems/gas-station/) | Medium | restart after a deficit; why skipped starts are impossible | N150 · N250 |
| 6 | [Hand of Straights](https://leetcode.com/problems/hand-of-straights/) | Medium | the smallest card's group is forced | N150 · N250 |
| 7 | [Merge Triplets to Form Target Triplet](https://leetcode.com/problems/merge-triplets-to-form-target-triplet/) | Medium | discard any triplet that exceeds the target | N150 · N250 |
| 8 | ★ [Partition Labels](https://leetcode.com/problems/partition-labels/) | Medium | last occurrence decides the cut | N150 · N250 |
| 9 | [Valid Parenthesis String](https://leetcode.com/problems/valid-parenthesis-string/) | Medium | tracking a range instead of a value | N150 · N250 |
| 10 | [Queue Reconstruction by Height](https://leetcode.com/problems/queue-reconstruction-by-height/) | Medium | tallest first, insert at index k | |
| 11 | [Candy](https://leetcode.com/problems/candy/) | Hard | two passes | N250 |
| 12 | [Minimum Number of Refueling Stops](https://leetcode.com/problems/minimum-number-of-refueling-stops/) | Hard | retroactive choice with a max-heap | |

[Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) (Kadane) is also a greedy; it is listed under [Pattern 04](04_prefix_sums.md).

## AI-era exercises

**Exercise 1 · Break the greedy.** Asked for Coin Change ("fewest coins to make the amount"), an assistant answered:

```python
def coin_change_greedy_ai(coins, amount):
    count = 0
    for c in sorted(coins, reverse=True):
        take = amount // c
        count += take
        amount -= take * c
    return count if amount == 0 else -1
```

Find the smallest counterexample with three coin values, and a second input where it returns −1 although an answer exists.

<details><summary>Answer</summary>

`coins = [1, 3, 4], amount = 6`: greedy takes 4 + 1 + 1 (3 coins), but 3 + 3 uses 2. `coins = [3, 5], amount = 9`: greedy takes 5, is left with 4, cannot use 3 to make 4 and returns −1, but 3 + 3 + 3 works. Greedy is optimal only for special coin systems (such as 1, 2, 5, 10, …). A brute-force DP over amounts up to 30 with random coin sets finds counterexamples in milliseconds. The correct solution is the DP in [Pattern 19](19_dp_1d.md).
</details>

**Exercise 2 · One pass is not enough.**

```python
def candy_ai(ratings):
    c = [1] * len(ratings)
    for i in range(1, len(ratings)):
        if ratings[i] > ratings[i - 1]:
            c[i] = c[i - 1] + 1
    return sum(c)
```

Find a three-element failing input. Then state the two constraints the correct answer must satisfy and why the second pass with `max` keeps the first pass's guarantee.

<details><summary>Answer</summary>

`[1, 0, 2]` returns 4 (`[1, 1, 2]`), but child 0 has a higher rating than child 1 and must get more: the answer is 5 (`[2, 1, 2]`). Constraints: if `r[i] > r[i-1]` then `c[i] > c[i-1]`; if `r[i] > r[i+1]` then `c[i] > c[i+1]`. The first pass satisfies the left constraint. The second pass only *raises* values (`max`), so the left constraint stays satisfied, and processing right to left satisfies the right constraint. Each value is the minimum that satisfies both, so the total is minimal.
</details>

## You own this pattern when

- For every greedy you write, you state the exchange or stays-ahead argument before coding.
- You try to break your own greedy rule with a brute force on small inputs, and you have a list of three classic counterexamples (coin change, 0/1 knapsack, interval scheduling sorted by start).
- You solve Gas Station and Jump Game II AI off and explain why skipped indices can be skipped.
