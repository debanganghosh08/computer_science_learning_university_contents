# DSA for hiring · Pattern 13 · Backtracking

| Theory first | Time | Problems | Must-do |
|---|---|---|---|
| [FND112](../../../01_year_1_foundations/semester_2/FND112_data_structures_and_algorithms_i/README.md) lesson 2.5 | ~10 hours | 15 | 5 |

Backtracking explores a tree of partial solutions: **choose** an option, **explore** recursively, **unchoose** it. It is exhaustive search with discipline, used when the problem asks for *all* solutions or when constraints are small (n ≤ 10–20). The interview tests three things: the shape of the decision tree, how you avoid duplicate answers, and how you prune.

## Recognise it

| When you see… | Think… |
|---|---|
| "all subsets / combinations / permutations / partitions" | backtracking; the output itself is exponential |
| "all ways to place / fill / arrange" (queens, sudoku, parentheses) | backtracking with constraint checks and pruning |
| a word to find in a grid of letters | DFS with mark/unmark of the current path |
| input contains duplicates, output must not | sort, then skip equal values at the same depth |
| n ≤ 20 with "choose a subset to optimise" | bitmask enumeration or backtracking with pruning; consider DP if states repeat |
| "count" rather than "list" the solutions | check whether DP can count without enumerating ([Pattern 21](21_dp_subsequences_knapsack.md)) |

## Core templates

**Subsets (index-based).** Each node of the recursion is one subset; record it, then extend with later elements only.

```python
def subsets(nums):
    out, path = [], []

    def dfs(start):
        out.append(path[:])                  # copy: path keeps changing
        for i in range(start, len(nums)):
            path.append(nums[i])             # choose
            dfs(i + 1)                       # explore
            path.pop()                       # unchoose

    dfs(0)
    return out
```

**Skip duplicates at the same depth.** After sorting, equal values in the same loop would start identical branches.

```python
def subsets_with_dup(nums):
    nums = sorted(nums)
    out, path = [], []

    def dfs(start):
        out.append(path[:])
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue                     # same value, same depth: duplicate branch
            path.append(nums[i])
            dfs(i + 1)
            path.pop()

    dfs(0)
    return out


def combination_sum2(candidates, target):    # each candidate used at most once
    c = sorted(candidates)
    out, path = [], []

    def dfs(start, remain):
        if remain == 0:
            out.append(path[:])
            return
        for i in range(start, len(c)):
            if i > start and c[i] == c[i - 1]:
                continue
            if c[i] > remain:
                break                        # sorted: every later value is too big
            path.append(c[i])
            dfs(i + 1, remain - c[i])
            path.pop()

    dfs(0, target)
    return out
```

**Reuse allowed (Combination Sum).** Recurse with `i`, not `i + 1`.

```python
def combination_sum(candidates, target):
    c = sorted(candidates)
    out, path = [], []

    def dfs(start, remain):
        if remain == 0:
            out.append(path[:])
            return
        for i in range(start, len(c)):
            if c[i] > remain:
                break
            path.append(c[i])
            dfs(i, remain - c[i])            # same i: the value may be reused
            path.pop()

    dfs(0, target)
    return out
```

**Permutations with a `used` array.**

```python
def permute(nums):
    out, path, used = [], [], [False] * len(nums)

    def dfs():
        if len(path) == len(nums):
            out.append(path[:])
            return
        for i, x in enumerate(nums):
            if not used[i]:
                used[i] = True
                path.append(x)
                dfs()
                path.pop()
                used[i] = False

    dfs()
    return out
```

**Grid word search.** Mark the cell as part of the current path, restore it on the way back.

```python
def exist(board, word):
    m, n = len(board), len(board[0])

    def dfs(r, c, k):
        if k == len(word):
            return True
        if not (0 <= r < m and 0 <= c < n) or board[r][c] != word[k]:
            return False
        board[r][c] = "#"                    # mark
        found = (dfs(r + 1, c, k + 1) or dfs(r - 1, c, k + 1)
                 or dfs(r, c + 1, k + 1) or dfs(r, c - 1, k + 1))
        board[r][c] = word[k]                # unmark
        return found

    return any(dfs(r, c, 0) for r in range(m) for c in range(n))
```

**Constraint sets (N-Queens).** A queen at (r, c) occupies column c, diagonal r − c and anti-diagonal r + c.

```python
def solve_n_queens(n):
    cols, diag, anti = set(), set(), set()
    board = [["."] * n for _ in range(n)]
    out = []

    def place(r):
        if r == n:
            out.append(["".join(row) for row in board])
            return
        for c in range(n):
            if c in cols or r - c in diag or r + c in anti:
                continue                     # prune before recursing
            cols.add(c); diag.add(r - c); anti.add(r + c)
            board[r][c] = "Q"
            place(r + 1)
            board[r][c] = "."
            cols.remove(c); diag.remove(r - c); anti.remove(r + c)

    place(0)
    return out
```

**Count-constrained generation (Generate Parentheses).**

```python
def generate_parenthesis(n):
    out = []

    def dfs(s, open_, close):
        if len(s) == 2 * n:
            out.append(s)
            return
        if open_ < n:
            dfs(s + "(", open_ + 1, close)
        if close < open_:
            dfs(s + ")", open_, close + 1)

    dfs("", 0, 0)
    return out
```

**Java.** Copy with `new ArrayList<>(path)` and remove the last element by index.

```java
static List<List<Integer>> permute(int[] nums) {
    List<List<Integer>> out = new ArrayList<>();
    permuteDfs(nums, new boolean[nums.length], new ArrayList<>(), out);
    return out;
}

static void permuteDfs(int[] nums, boolean[] used, List<Integer> path, List<List<Integer>> out) {
    if (path.size() == nums.length) {
        out.add(new ArrayList<>(path));
        return;
    }
    for (int i = 0; i < nums.length; i++) {
        if (used[i]) continue;
        used[i] = true;
        path.add(nums[i]);
        permuteDfs(nums, used, path, out);
        path.remove(path.size() - 1);       // remove(int index), not remove(Object)
        used[i] = false;
    }
}
```

## Complexity

The output size dominates: subsets O(n · 2ⁿ), permutations O(n · n!), combinations C(n, k) · k. Word search is O(m · n · 3^L) for a word of length L (each step has at most three new directions). N-Queens is bounded by n! with heavy pruning. Recursion depth is the solution length, so space is O(n) plus the output.

## Common bugs

1. Appending `path` instead of a copy, so every recorded answer is the same (finally empty) list (exercise 1).
2. Skipping duplicates with `i > 0` instead of `i > start`, which also removes valid answers that use a repeated value (exercise 2).
3. Forgetting to unmark a grid cell or to remove from the constraint sets.
4. Java `path.remove(x)` with an `Integer` value instead of an index.
5. String concatenation in deep recursion creating many copies; a list of characters with append/pop is cheaper for long outputs.
6. No pruning on sorted candidates (`break` when the value exceeds the remainder).

## Problems (easy → hard)

Lists: **B75** Blind 75 · **N150** NeetCode 150 · **N250** NeetCode 250. ★ = in the [must-do 100](../problem_list.md).

| # | Problem | Level | What it teaches | Lists |
|---|---|---|---|---|
| 1 | [Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths/) | Easy | path building and undoing on a tree | |
| 2 | ★ [Subsets](https://leetcode.com/problems/subsets/) | Medium | the basic choose/explore/unchoose shape | N150 · N250 |
| 3 | [Subsets II](https://leetcode.com/problems/subsets-ii/) | Medium | skip duplicates at the same depth | N150 · N250 |
| 4 | ★ [Permutations](https://leetcode.com/problems/permutations/) | Medium | `used` array; n! leaves | N150 · N250 |
| 5 | [Permutations II](https://leetcode.com/problems/permutations-ii/) | Medium | duplicate skipping with `used[i - 1]` | N250 |
| 6 | [Combinations](https://leetcode.com/problems/combinations/) | Medium | pruning when too few elements remain | N250 |
| 7 | ★ [Combination Sum](https://leetcode.com/problems/combination-sum/) | Medium | reuse by recursing on `i` | B75 · N150 · N250 |
| 8 | [Combination Sum II](https://leetcode.com/problems/combination-sum-ii/) | Medium | single use plus duplicate skipping | N150 · N250 |
| 9 | [Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) | Medium | product of choices per position | N150 · N250 |
| 10 | ★ [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/) | Medium | generate only valid prefixes | N150 · N250 |
| 11 | [Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/) | Medium | cut positions as choices; precomputed palindrome table | N150 · N250 |
| 12 | ★ [Word Search](https://leetcode.com/problems/word-search/) | Medium | grid DFS with mark/unmark | B75 · N150 · N250 |
| 13 | [N-Queens](https://leetcode.com/problems/n-queens/) | Hard | constraint sets for O(1) checks | N150 · N250 |
| 14 | [Sudoku Solver](https://leetcode.com/problems/sudoku-solver/) | Hard | most-constrained-cell ordering as pruning | |
| 15 | [Word Search II](https://leetcode.com/problems/word-search-ii/) | Hard | backtracking guided by a trie ([Pattern 18](18_tries.md)) | B75 · N150 · N250 |

## AI-era exercises

**Exercise 1 · Find the aliasing bug.**

```python
def subsets_ai(nums):
    out, path = [], []

    def dfs(start):
        out.append(path)
        for i in range(start, len(nums)):
            path.append(nums[i])
            dfs(i + 1)
            path.pop()

    dfs(0)
    return out
```

What does it return for `[1, 2]`, and why does printing `out` *during* the recursion make the bug harder to see?

<details><summary>Answer</summary>

It returns `[[], [], [], []]`: four references to the same list object, which is empty when the recursion finishes. During the recursion, printing `out` shows the current contents of that one list repeated, which changes as you watch, so debugging prints look plausible at some moments. Append `path[:]` (or `list(path)`). In Java the same bug is `out.add(path)` instead of `out.add(new ArrayList<>(path))`.
</details>

**Exercise 2 · Duplicates done wrong.**

```python
def combination_sum2_ai(candidates, target):
    c = sorted(candidates)
    out, path = [], []

    def dfs(start, remain):
        if remain == 0:
            out.append(path[:])
            return
        for i in range(start, len(c)):
            if i > 0 and c[i] == c[i - 1]:
                continue
            if c[i] > remain:
                break
            path.append(c[i])
            dfs(i + 1, remain - c[i])
            path.pop()

    dfs(0, target)
    return out
```

Find the smallest input where an answer is missing and explain the difference between "same depth" and "anywhere".

<details><summary>Answer</summary>

`candidates = [1, 1], target = 2` should return `[[1, 1]]` but returns `[]`. With `i > 0`, the second 1 is skipped even when it is the *next* element of the same combination (depth 2), not a sibling branch (depth 1). Skipping is only correct among siblings, that is, when `i > start`. Compare against a brute force that enumerates all index subsets and deduplicates sorted tuples; inputs with repeated values find the bug immediately.
</details>

## You own this pattern when

- You can draw the decision tree for subsets, permutations and combination sum and say what each node and leaf represents.
- You handle duplicates with sorting and the `i > start` rule without looking it up.
- You state the output-size complexity before writing code, and add at least one pruning rule.
