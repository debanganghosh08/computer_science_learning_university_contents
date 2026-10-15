# DSA for hiring · Pattern 05 · Binary search (including search on the answer)

| Theory first | Time | Problems | Must-do |
|---|---|---|---|
| [FND112](../../../01_year_1_foundations/semester_2/FND112_data_structures_and_algorithms_i/README.md) lessons 7.5, 7.6; [CS201](../../../02_year_2_core_computer_science/semester_3/CS201_algorithms_and_complexity/README.md) lesson 1.2 (invariants) | ~10 hours | 15 | 5 |

Binary search is not "find x in a sorted array". It is: **find the boundary of a monotone yes/no predicate** over an index range or a range of possible answers. Write one template, understand its invariant, and reuse it everywhere. Most binary-search bugs come from mixing two templates.

## Recognise it

| When you see… | Think… |
|---|---|
| sorted array, "first/last position", "insert position" | lower bound / upper bound |
| "minimum speed / capacity / time such that it is possible" | search on the answer; write `feasible(x)` and check it is monotone |
| "maximise the minimum" or "minimise the maximum" | search on the answer |
| rotated sorted array | one half is always sorted; decide which |
| `n` up to 10⁹ or 10¹⁸ in the answer range, small input | O(log range) iterations of an O(n) check |
| "find any peak / local extremum" | compare `mid` with `mid + 1` and move uphill |
| a matrix sorted row-wise and column-wise | treat as one sorted array (fully sorted) or walk from a corner (row/column sorted) |

## Core templates

**One template for everything: first index where `pred` is true.** Search space `[lo, hi)`; invariant: everything before `lo` is false, everything from `hi` on is true.

```python
def first_true(lo, hi, pred):
    """Smallest x in [lo, hi) with pred(x) True, or hi if none. pred must be monotone F..F T..T."""
    while lo < hi:
        mid = (lo + hi) // 2
        if pred(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo


def lower_bound(a, x):                 # first index with a[i] >= x
    return first_true(0, len(a), lambda i: a[i] >= x)


def upper_bound(a, x):                 # first index with a[i] > x
    return first_true(0, len(a), lambda i: a[i] > x)


def search_range(a, x):                # Find First and Last Position
    lo = lower_bound(a, x)
    if lo == len(a) or a[lo] != x:
        return [-1, -1]
    return [lo, upper_bound(a, x) - 1]
```

**Search on the answer.** The answer is the first value for which the plan is feasible.

```python
def min_eating_speed(piles, h):        # Koko Eating Bananas
    def feasible(k):
        return sum((p + k - 1) // k for p in piles) <= h   # ceil without floats
    return first_true(1, max(piles) + 1, feasible)


def ship_within_days(weights, days):
    def feasible(cap):
        need, load = 1, 0
        for w in weights:
            if load + w > cap:
                need += 1
                load = 0
            load += w
        return need <= days
    return first_true(max(weights), sum(weights) + 1, feasible)
```

**Rotated sorted array (distinct values).** Compare with the right end: if `a[mid] > a[hi]`, the minimum is to the right of `mid`.

```python
def find_min_rotated(a):
    lo, hi = 0, len(a) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] > a[hi]:
            lo = mid + 1
        else:
            hi = mid
    return a[lo]


def search_rotated(a, target):
    lo, hi = 0, len(a) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] == target:
            return mid
        if a[lo] <= a[mid]:                       # left half sorted
            if a[lo] <= target < a[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:                                     # right half sorted
            if a[mid] < target <= a[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1
```

**Peak finding.** If `a[mid] < a[mid + 1]` a peak exists to the right (the sequence must come down or end). The predicate `a[i] > a[i + 1]` is not monotone, yet the same loop works: it keeps "`a[lo - 1] < a[lo]` or `lo = 0`" and "`a[hi] > a[hi + 1]` or `hi = n - 1`", so the index where `lo` and `hi` meet is a peak. Being able to say why a template still works outside its usual precondition is what interviewers probe.

```python
def find_peak(a):
    return first_true(0, len(a) - 1, lambda i: a[i] > a[i + 1])
```

**Median of two sorted arrays.** Binary-search the cut in the shorter array so the left halves hold exactly half the elements and every left value ≤ every right value.

```python
def find_median_sorted_arrays(A, B):
    if len(A) > len(B):
        A, B = B, A
    m, n = len(A), len(B)
    half = (m + n + 1) // 2
    lo, hi = 0, m
    NEG, POS = float("-inf"), float("inf")
    while True:
        i = (lo + hi) // 2                # elements taken from A
        j = half - i                      # elements taken from B
        a_left = A[i - 1] if i > 0 else NEG
        a_right = A[i] if i < m else POS
        b_left = B[j - 1] if j > 0 else NEG
        b_right = B[j] if j < n else POS
        if a_left <= b_right and b_left <= a_right:
            if (m + n) % 2:
                return float(max(a_left, b_left))
            return (max(a_left, b_left) + min(a_right, b_right)) / 2
        if a_left > b_right:
            hi = i - 1
        else:
            lo = i + 1
```

**Java.** Use `(lo + hi) >>> 1` (or `lo + (hi - lo) / 2`) so the sum cannot overflow, and `long` for answer ranges.

```java
static int lowerBound(int[] a, int x) {
    int lo = 0, hi = a.length;
    while (lo < hi) {
        int mid = (lo + hi) >>> 1;
        if (a[mid] >= x) hi = mid; else lo = mid + 1;
    }
    return lo;
}

static int minEatingSpeed(int[] piles, int h) {
    int lo = 1, hi = 0;
    for (int p : piles) hi = Math.max(hi, p);
    while (lo < hi) {
        int k = (lo + hi) >>> 1;
        long hours = 0;
        for (int p : piles) hours += (p + (long) k - 1) / k;
        if (hours <= h) hi = k; else lo = k + 1;
    }
    return lo;
}
```

## Complexity

Index search: O(log n). Search on the answer: O(log R) calls of the feasibility check, where R is the size of the answer range; with an O(n) check this is O(n log R). Median of two sorted arrays: O(log min(m, n)). All use O(1) extra space.

## Common bugs

1. Mixing templates: `while lo <= hi` with `hi = mid` loops forever; `while lo < hi` with `hi = mid - 1` can skip the answer.
2. "Last true" searches with `lo = mid` and a floor midpoint loop forever when `hi = lo + 1` (exercise 1). Either use a ceiling midpoint or convert to "first false" and subtract one.
3. A predicate that is not monotone. Check it on paper with two values before coding.
4. Float division for ceilings (`math.ceil(p / k)`) breaks for values near 2⁵³; use `(p + k - 1) // k`.
5. Wrong answer-range bounds: Ship Packages needs `lo = max(weights)`, not 1, or `feasible` can never place a heavy package.
6. Rotated arrays with duplicates (`[1, 0, 1, 1, 1]`): the "which half is sorted" test fails and the worst case becomes O(n); say this if asked.

## Problems (easy → hard)

Lists: **B75** Blind 75 · **N150** NeetCode 150 · **N250** NeetCode 250. ★ = in the [must-do 100](../problem_list.md).

| # | Problem | Level | What it teaches | Lists |
|---|---|---|---|---|
| 1 | ★ [Binary Search](https://leetcode.com/problems/binary-search/) | Easy | the invariant, written down | N150 · N250 |
| 2 | [Search Insert Position](https://leetcode.com/problems/search-insert-position/) | Easy | lower bound returns the insert point | N250 |
| 3 | [Sqrt(x)](https://leetcode.com/problems/sqrtx/) | Easy | "last true" = first false − 1 | N250 |
| 4 | [First Bad Version](https://leetcode.com/problems/first-bad-version/) | Easy | binary search over an API predicate | |
| 5 | ★ [Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) | Medium | lower and upper bound from one template | |
| 6 | [Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/) | Medium | index `i` → cell `(i // n, i % n)` | N150 · N250 |
| 7 | [Find Peak Element](https://leetcode.com/problems/find-peak-element/) | Medium | binary search without sorted input | |
| 8 | ★ [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | Medium | compare with the right end | B75 · N150 · N250 |
| 9 | ★ [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | Medium | which half is sorted | B75 · N150 · N250 |
| 10 | [Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/) | Medium | `bisect_right` on per-key timestamp lists | N150 · N250 |
| 11 | ★ [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) | Medium | search on the answer; integer ceilings | N150 · N250 |
| 12 | [Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/) | Medium | greedy feasibility check; correct lower bound | N250 |
| 13 | [Minimum Number of Days to Make m Bouquets](https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/) | Medium | feasibility with contiguous groups; impossible case | |
| 14 | [Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/) | Hard | "minimise the maximum"; the same check as 12 | N250 |
| 15 | [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) | Hard | binary search on a partition | N150 · N250 |

## AI-era exercises

**Exercise 1 · Find the hang.** An assistant's integer square root:

```python
def my_sqrt_ai(x):
    lo, hi = 0, x
    while lo < hi:
        mid = (lo + hi) // 2
        if mid * mid <= x:
            lo = mid
        else:
            hi = mid - 1
    return lo
```

Find the smallest input that never returns, explain why, and fix it two different ways.

<details><summary>Answer</summary>

`x = 1`: `lo = 0, hi = 1`, `mid = 0`, `0 <= 1` sets `lo = 0` again, forever. With a floor midpoint, `lo = mid` makes no progress whenever `hi = lo + 1`. Fix 1: ceiling midpoint `mid = (lo + hi + 1) // 2`. Fix 2: search for the first `m` with `m * m > x` using `first_true(0, x + 2, ...)` and return that minus one. Tests on `x = 0..1000` against `math.isqrt` would catch both the hang (with a timeout) and any off-by-one.

```python
def my_sqrt_fixed(x):
    lo, hi = 0, x
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if mid * mid <= x:
            lo = mid
        else:
            hi = mid - 1
    return lo
```
</details>

**Exercise 2 · Check the predicate.** An assistant's Koko solution:

```python
def min_eating_speed_ai(piles, h):
    lo, hi = 1, max(piles)
    while lo < hi:
        k = (lo + hi) // 2
        hours = sum(p // k + 1 for p in piles)
        if hours <= h:
            hi = k
        else:
            lo = k + 1
    return lo
```

It passes `piles = [3, 6, 7, 11], h = 8`. Find a one-pile input where it fails and state the exact property the hours formula must have.

<details><summary>Answer</summary>

`piles = [4], h = 2` should return 2 (two hours at speed 2), but `4 // 2 + 1 = 3` hours makes speed 2 look infeasible, and the code returns 3. `p // k + 1` overcounts whenever k divides p. The formula must equal ⌈p / k⌉ exactly: `(p + k - 1) // k`. The binary search itself was fine; the predicate was wrong. When reviewing a search on the answer, test the feasibility function alone on hand-computed values before testing the search.
</details>

## You own this pattern when

- You use one template (`first_true`) for all problems above and can state its invariant.
- For a search on the answer you write `feasible`, its bounds and a monotonicity argument before the loop.
- You solve problems 9, 11 and 14 AI off in under 20 minutes each.
