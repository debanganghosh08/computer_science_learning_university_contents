# DSA for hiring · Pattern 04 · Prefix sums and difference arrays

| Theory first | Time | Problems | Must-do |
|---|---|---|---|
| [FND112](../../../01_year_1_foundations/semester_2/FND112_data_structures_and_algorithms_i/README.md) lesson 3.3 | ~8 hours | 13 | 4 |

With `pre[i]` = sum of the first i elements, the sum of `a[l..r]` is `pre[r + 1] - pre[l]`. That one identity turns "count subarrays with property P" into "count pairs of prefix values with property P", which a hash map answers in one pass. It works with negative numbers, which is exactly where [sliding window](03_sliding_window.md) fails.

## Recognise it

| When you see… | Think… |
|---|---|
| many range-sum queries on a fixed array | prefix array, O(1) per query |
| "number of subarrays with sum = k" (negatives allowed) | prefix sum + hash map of counts, seeded with `{0: 1}` |
| "subarray sum divisible by k / multiple of k" | prefix sums modulo k; equal remainders |
| "equal number of 0s and 1s" | map 0 → −1, then "sum = 0" |
| many range **updates**, then read once | difference array: `+v` at l, `−v` at r + 1, prefix-sum at the end |
| 2-D grid, sub-rectangle sums | 2-D prefix with inclusion-exclusion |
| "product of all except self" | prefix products times suffix products |
| "shortest subarray with sum ≥ k" with negatives | monotonic deque over prefix sums |

## Core templates

**Prefix array with a leading zero.** The leading zero removes every `if l == 0` special case.

```python
from collections import defaultdict, deque
from itertools import accumulate


def build_prefix(a):
    return [0] + list(accumulate(a))          # pre[i] = a[0] + ... + a[i-1]


def range_sum(pre, l, r):                     # inclusive l..r
    return pre[r + 1] - pre[l]
```

**Count subarrays with sum k.** A subarray ending at j has sum k exactly when some earlier prefix equals `pre[j+1] - k`.

```python
def subarray_sum(nums, k):
    seen = defaultdict(int)
    seen[0] = 1                               # the empty prefix
    total = count = 0
    for x in nums:
        total += x
        count += seen[total - k]
        seen[total] += 1
    return count
```

**Remainders.** `a[l..r]` is divisible by k exactly when `pre[r+1] % k == pre[l] % k`.

```python
def subarrays_div_by_k(nums, k):
    seen = defaultdict(int)
    seen[0] = 1
    total = count = 0
    for x in nums:
        total = (total + x) % k               # Python % is never negative for k > 0
        count += seen[total]
        seen[total] += 1
    return count
```

**Difference array.** O(1) per range update, one O(n) pass to read.

```python
def apply_range_updates(n, updates):          # updates: (l, r, v), inclusive, 0-based
    diff = [0] * (n + 1)
    for l, r, v in updates:
        diff[l] += v
        diff[r + 1] -= v
    return list(accumulate(diff))[:n]
```

**2-D prefix.** `P[i][j]` is the sum of the rectangle above and left of cell (i, j), exclusive.

```python
def build_prefix_2d(grid):
    m, n = len(grid), len(grid[0])
    P = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m):
        for j in range(n):
            P[i + 1][j + 1] = grid[i][j] + P[i][j + 1] + P[i + 1][j] - P[i][j]
    return P


def rect_sum(P, r1, c1, r2, c2):              # inclusive corners
    return P[r2 + 1][c2 + 1] - P[r1][c2 + 1] - P[r2 + 1][c1] + P[r1][c1]
```

**Product except self**, O(1) extra space besides the output.

```python
def product_except_self(nums):
    n = len(nums)
    out = [1] * n
    left = 1
    for i in range(n):
        out[i] = left
        left *= nums[i]
    right = 1
    for i in range(n - 1, -1, -1):
        out[i] *= right
        right *= nums[i]
    return out
```

**Kadane = best prefix difference.** The best subarray ending at j is `pre[j+1] - min(pre[0..j])`; Kadane keeps that minimum implicitly.

```python
def max_subarray(nums):
    best = cur = nums[0]
    for x in nums[1:]:
        cur = max(x, cur + x)                 # extend or restart
        best = max(best, cur)
    return best
```

**Shortest subarray with sum ≥ k (negatives allowed).** Keep prefix indices with increasing prefix values; pop the front while it forms a valid subarray.

```python
def shortest_subarray(nums, k):
    pre = build_prefix(nums)
    dq, best = deque(), float("inf")
    for j, pj in enumerate(pre):
        while dq and pj - pre[dq[0]] >= k:
            best = min(best, j - dq.popleft())
        while dq and pre[dq[-1]] >= pj:
            dq.pop()                          # a later, smaller prefix is a better start
        dq.append(j)
    return -1 if best == float("inf") else best
```

**Java.** Java's `%` keeps the sign of the dividend, so normalise remainders; use `long` for running sums.

```java
static int subarraySum(int[] nums, int k) {
    Map<Long, Integer> seen = new HashMap<>();
    seen.put(0L, 1);
    long total = 0;
    int count = 0;
    for (int x : nums) {
        total += x;
        count += seen.getOrDefault(total - k, 0);
        seen.merge(total, 1, Integer::sum);
    }
    return count;
}

static int subarraysDivByK(int[] nums, int k) {
    int[] seen = new int[k];
    seen[0] = 1;
    int total = 0, count = 0;
    for (int x : nums) {
        total = ((total + x) % k + k) % k;    // normalise: -1 % 5 is -1 in Java
        count += seen[total];
        seen[total]++;
    }
    return count;
}
```

## Complexity

Building a prefix array is O(n) time and space; each range query is O(1). The hash-map counting templates are O(n) expected time, O(n) space. A difference array takes O(1) per update and O(n) to read. 2-D: O(mn) to build, O(1) per query. The deque template is O(n) because each index enters and leaves once.

## Common bugs

1. Forgetting `seen[0] = 1`, which misses every subarray that starts at index 0 (exercise 1).
2. Java negative remainders (exercise 2).
3. Off-by-one between `pre[r] - pre[l]` (half-open) and `pre[r + 1] - pre[l]` (inclusive). Decide once and write it in a comment.
4. A difference array of size n instead of n + 1, so `diff[r + 1]` overflows the last index.
5. Integer overflow of running sums in Java/C++; use `long`.
6. In "first index where the remainder appeared" problems (Continuous Subarray Sum), overwriting the earliest index with later ones.

## Problems (easy → hard)

Lists: **B75** Blind 75 · **N150** NeetCode 150 · **N250** NeetCode 250. ★ = in the [must-do 100](../problem_list.md).

| # | Problem | Level | What it teaches | Lists |
|---|---|---|---|---|
| 1 | [Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/) | Easy | the leading-zero prefix array | |
| 2 | [Find Pivot Index](https://leetcode.com/problems/find-pivot-index/) | Easy | left sum vs total − left − self | |
| 3 | ★ [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) | Medium | prefix and suffix products, no division | B75 · N150 · N250 |
| 4 | ★ [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) | Medium | prefix + hash map of counts | N250 |
| 5 | [Continuous Subarray Sum](https://leetcode.com/problems/continuous-subarray-sum/) | Medium | remainders with the *earliest* index (length ≥ 2) | |
| 6 | [Subarray Sums Divisible by K](https://leetcode.com/problems/subarray-sums-divisible-by-k/) | Medium | counting equal remainders; negative remainders | |
| 7 | [Contiguous Array](https://leetcode.com/problems/contiguous-array/) | Medium | re-encode 0 as −1, then sum = 0 | |
| 8 | [Range Sum Query 2D - Immutable](https://leetcode.com/problems/range-sum-query-2d-immutable/) | Medium | inclusion-exclusion | N250 |
| 9 | [Corporate Flight Bookings](https://leetcode.com/problems/corporate-flight-bookings/) | Medium | difference arrays | |
| 10 | [Car Pooling](https://leetcode.com/problems/car-pooling/) | Medium | difference array over time as a capacity check | N250 |
| 11 | ★ [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) | Medium | Kadane as "best prefix difference" | B75 · N150 · N250 |
| 12 | [Random Pick with Weight](https://leetcode.com/problems/random-pick-with-weight/) | Medium | prefix sums + binary search for sampling | |
| 13 | ★ [Shortest Subarray with Sum at Least K](https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/) | Hard | monotonic deque over prefix sums | |

## AI-era exercises

**Exercise 1 · Find the bug.**

```python
def subarray_sum_ai(nums, k):
    seen = {}
    total = count = 0
    for x in nums:
        total += x
        count += seen.get(total - k, 0)
        seen[total] = seen.get(total, 0) + 1
    return count
```

Find a one-element input where it fails, and a property-based test that would have caught it.

<details><summary>Answer</summary>

`subarray_sum_ai([1], 1)` returns 0 instead of 1. The subarray `[1]` starts at index 0, so its matching prefix is the empty prefix, whose sum 0 was never inserted. Fix: start with `seen = {0: 1}`. Property test: for random arrays of length ≤ 8 with values in −3..3, compare against the O(n²) double loop over all `(i, j)`; random tests hit "subarray starting at 0" almost immediately.
</details>

**Exercise 2 · A Java-only bug.** An assistant translated the Python solution of Subarray Sums Divisible by K to Java:

```java
static int subarraysDivByKAi(int[] nums, int k) {
    Map<Integer, Integer> seen = new HashMap<>();
    seen.put(0, 1);
    int total = 0, count = 0;
    for (int x : nums) {
        total = (total + x) % k;
        count += seen.getOrDefault(total, 0);
        seen.merge(total, 1, Integer::sum);
    }
    return count;
}
```

The Python version is correct. Why is this one wrong, and what is the smallest failing input you can find?

<details><summary>Answer</summary>

In Java, `-1 % 5 == -1`, while in Python `-1 % 5 == 4`. Prefix sums that are congruent modulo k can get different Java remainders (−1 and 4), so equal classes are not matched. `nums = [-1, 5], k = 5`: the subarray `[5]` is divisible, and its prefixes are −1 and 4, which are congruent. Java stores remainder −1 then 4 and counts nothing, so it returns 0 instead of 1. Fix: `total = ((total + x) % k + k) % k`. Translation between languages is a common source of AI errors; test the translated code, not just the original.
</details>

## You own this pattern when

- You can derive the hash-map counting template from `pre[r + 1] - pre[l] = k` on paper in two minutes.
- You solve problems 4, 6 and 13 AI off and explain why sliding window fails on each.
- You know the remainder semantics of `%` in every language you interview in.
