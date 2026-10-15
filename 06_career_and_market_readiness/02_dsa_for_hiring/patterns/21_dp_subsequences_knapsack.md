# DSA for hiring · Pattern 21 · DP on subsequences, strings and knapsack

| Theory first | Time | Problems | Must-do |
|---|---|---|---|
| [CS201](../../../02_year_2_core_computer_science/semester_3/CS201_algorithms_and_complexity/README.md) lessons 5.2, 5.3 (edit distance, LCS, knapsack, pseudo-polynomial time) | ~12 hours | 13 | 4 |

Two families dominate the hardest common DP questions:

- **Knapsack:** items with sizes, a capacity, and a yes/no, count or best-value question. `dp[c]` over capacities, with the loop direction deciding whether an item may be reused.
- **Two-sequence DP:** `dp[i][j]` answers the question for the prefixes `a[:i]` and `b[:j]` (longest common subsequence, edit distance, interleaving, pattern matching). Each cell looks at most three neighbours.

Knapsack DP is **pseudo-polynomial**: O(n · W) is polynomial in the *value* W, not in the number of bits needed to write it. Say this if asked why subset sum is NP-complete yet "solvable in O(nW)".

## Recognise it

| When you see… | Think… |
|---|---|
| "split into two groups with equal/closest sums" | 0/1 knapsack over sums up to total / 2 |
| "assign + or − to each number to reach a target" | count subsets with sum (total + target) / 2 |
| "number of ways to make an amount" with unlimited coins | unbounded knapsack, coins in the **outer** loop |
| two strings, "common", "transform", "interleave", "match a pattern" | `dp[i][j]` over prefixes, size (m + 1) × (n + 1) |
| "longest palindromic subsequence" | LCS of the string and its reverse, or interval DP |
| two budgets at once (count of 0s and 1s) | knapsack with a two-dimensional capacity |

## Core templates

**0/1 knapsack (each item once).** Iterate capacity **downwards** so `dp[c - x]` still refers to the state before item x.

```python
from functools import lru_cache


def can_partition(nums):
    total = sum(nums)
    if total % 2:
        return False
    half = total // 2
    dp = [True] + [False] * half          # dp[c]: some subset sums to c
    for x in nums:
        for c in range(half, x - 1, -1):
            dp[c] = dp[c] or dp[c - x]
    return dp[half]


def find_target_sum_ways(nums, target):
    total = sum(nums)
    if abs(target) > total or (total + target) % 2:
        return 0
    goal = (total + target) // 2          # sum of the numbers given a '+'
    dp = [1] + [0] * goal                 # dp[c]: number of subsets with sum c
    for x in nums:
        for c in range(goal, x - 1, -1):
            dp[c] += dp[c - x]
    return dp[goal]
```

**Unbounded knapsack, counting combinations.** Coins in the outer loop: each multiset is counted once, in coin order.

```python
def change(amount, coins):
    dp = [1] + [0] * amount
    for c in coins:
        for a in range(c, amount + 1):    # ascending: coin c may be reused
            dp[a] += dp[a - c]
    return dp[amount]
```

**Longest common subsequence.**

```python
def lcs(a, b):
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]
```

**Edit distance.** Insert, delete or replace; row 0 and column 0 are the cost of building from or to the empty string.

```python
def min_distance(a, b):
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j],      # delete a[i-1]
                                   dp[i][j - 1],      # insert b[j-1]
                                   dp[i - 1][j - 1])  # replace
    return dp[m][n]
```

**Interleaving.** `dp[i][j]`: can `s3[:i + j]` be formed from `s1[:i]` and `s2[:j]`?

```python
def is_interleave(s1, s2, s3):
    m, n = len(s1), len(s2)
    if m + n != len(s3):
        return False
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True
    for i in range(m + 1):
        for j in range(n + 1):
            if i and s1[i - 1] == s3[i + j - 1] and dp[i - 1][j]:
                dp[i][j] = True
            if j and s2[j - 1] == s3[i + j - 1] and dp[i][j - 1]:
                dp[i][j] = True
    return dp[m][n]
```

**Counting subsequences (Distinct Subsequences).**

```python
def num_distinct(s, t):
    dp = [1] + [0] * len(t)               # dp[j]: ways to form t[:j] from the prefix of s seen so far
    for ch in s:
        for j in range(len(t), 0, -1):    # backwards: each character of s used once per way
            if t[j - 1] == ch:
                dp[j] += dp[j - 1]
    return dp[len(t)]
```

**Pattern matching (Regular Expression Matching, top-down).** `*` means "zero or more of the previous element".

```python
def is_match(s, p):
    @lru_cache(maxsize=None)
    def dp(i, j):                          # does s[i:] match p[j:]?
        if j == len(p):
            return i == len(s)
        first = i < len(s) and p[j] in (s[i], ".")
        if j + 1 < len(p) and p[j + 1] == "*":
            return dp(i, j + 2) or (first and dp(i + 1, j))
        return first and dp(i + 1, j + 1)
    return dp(0, 0)
```

**Java.**

```java
static int longestCommonSubsequence(String a, String b) {
    int m = a.length(), n = b.length();
    int[][] dp = new int[m + 1][n + 1];
    for (int i = 1; i <= m; i++)
        for (int j = 1; j <= n; j++)
            dp[i][j] = a.charAt(i - 1) == b.charAt(j - 1)
                ? dp[i - 1][j - 1] + 1
                : Math.max(dp[i - 1][j], dp[i][j - 1]);
    return dp[m][n];
}

static boolean canPartition(int[] nums) {
    int total = 0;
    for (int x : nums) total += x;
    if (total % 2 != 0) return false;
    boolean[] dp = new boolean[total / 2 + 1];
    dp[0] = true;
    for (int x : nums)
        for (int c = total / 2; c >= x; c--)
            dp[c] |= dp[c - x];
    return dp[total / 2];
}
```

## Complexity

Knapsack: O(n · W) time, O(W) space. Two-sequence DP: O(m · n) time; O(min(m, n)) space when only the previous row is kept (LCS length, edit distance, interleaving), but reconstructing the actual alignment needs the full table or Hirschberg's algorithm. Regular expression matching: O(m · n) states, O(1) work each.

## Common bugs

1. Ascending capacity loop in a 0/1 knapsack, so items are reused (exercise 2).
2. Amount in the outer loop for Coin Change II, which counts orderings (exercise 1).
3. Off-by-one between string indices and table indices: the table is (m + 1) × (n + 1) and cell (i, j) compares `a[i - 1]` with `b[j - 1]`.
4. Missing base row or column (edit distance from the empty string is the other string's length).
5. Target Sum without the parity and range checks, so `goal` is negative or fractional.
6. Recursion depth in top-down string DP: lengths of a few thousand exceed Python's default limit.

## Problems (easy → hard)

Lists: **B75** Blind 75 · **N150** NeetCode 150 · **N250** NeetCode 250. ★ = in the [must-do 100](../problem_list.md).

| # | Problem | Level | What it teaches | Lists |
|---|---|---|---|---|
| 1 | ★ [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) | Medium | 0/1 knapsack, downward loop | N150 · N250 |
| 2 | [Target Sum](https://leetcode.com/problems/target-sum/) | Medium | algebra first: reduce to subset counting | N150 · N250 |
| 3 | [Last Stone Weight II](https://leetcode.com/problems/last-stone-weight-ii/) | Medium | disguised partition: closest to total / 2 | N250 |
| 4 | ★ [Coin Change II](https://leetcode.com/problems/coin-change-ii/) | Medium | combinations vs permutations by loop order | N150 · N250 |
| 5 | [Ones and Zeroes](https://leetcode.com/problems/ones-and-zeroes/) | Medium | two-dimensional capacity | |
| 6 | ★ [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) | Medium | the canonical two-sequence table | B75 · N150 · N250 |
| 7 | [Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence/) | Medium | LCS with the reverse, or interval DP | |
| 8 | ★ [Edit Distance](https://leetcode.com/problems/edit-distance/) | Medium | three operations, three neighbours | N150 · N250 |
| 9 | [Interleaving String](https://leetcode.com/problems/interleaving-string/) | Medium | boolean table over two prefixes | N150 · N250 |
| 10 | [Distinct Subsequences](https://leetcode.com/problems/distinct-subsequences/) | Hard | counting with a backwards 1-D update | N150 · N250 |
| 11 | [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/) | Hard | `*` as "skip" or "consume one and stay" | N150 · N250 |
| 12 | [Wildcard Matching](https://leetcode.com/problems/wildcard-matching/) | Hard | `*` matching any sequence; compare with 11 | |

[Is Subsequence](https://leetcode.com/problems/is-subsequence/) (two pointers, [Pattern 02](02_two_pointers.md)) is the warm-up; its follow-up with many queries is a good discussion question.

## AI-era exercises

**Exercise 1 · Combinations or permutations?**

```python
def change_ai(amount, coins):
    dp = [1] + [0] * amount
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a:
                dp[a] += dp[a - c]
    return dp[amount]
```

Find the smallest input where it disagrees with Coin Change II, and name the LeetCode problem this code *does* solve.

<details><summary>Answer</summary>

`amount = 3, coins = [1, 2]`: there are 2 combinations ({1, 1, 1}, {1, 2}) but the code returns 3, because it counts 1 + 2 and 2 + 1 separately. With the amount in the outer loop, every ordering of the last coin is counted: this is [Combination Sum IV](https://leetcode.com/problems/combination-sum-iv/), which counts ordered sequences. Swapping the loops (coins outside) counts each multiset once. Check either version against a brute force that enumerates multisets on amounts up to 10.
</details>

**Exercise 2 · Items used twice.**

```python
def can_partition_ai(nums):
    total = sum(nums)
    if total % 2:
        return False
    half = total // 2
    dp = [True] + [False] * half
    for x in nums:
        for c in range(x, half + 1):
            dp[c] = dp[c] or dp[c - x]
    return dp[half]
```

Find a two-element input where it answers `True` wrongly, and explain the loop direction in one sentence.

<details><summary>Answer</summary>

`[1, 5]`: total 6, half 3. With the ascending loop, processing 1 sets `dp[1]`, then `dp[2]` from `dp[1]`, then `dp[3]` from `dp[2]`: the 1 has been used three times. The answer should be `False`. In a 0/1 knapsack, iterate capacities downwards so that `dp[c - x]` still describes subsets that do not contain x; ascending order is exactly the unbounded knapsack.
</details>

## You own this pattern when

- You can explain loop order and loop direction for 0/1 vs unbounded knapsack, and combinations vs permutations, without notes.
- You fill an edit-distance table by hand for "horse" → "ros" and read off the operations.
- You solve LCS, Edit Distance and Partition Equal Subset Sum AI off in under 15 minutes each.
