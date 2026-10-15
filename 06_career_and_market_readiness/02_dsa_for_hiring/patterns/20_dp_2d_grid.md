# DSA for hiring · Pattern 20 · Grid, interval and game DP

| Theory first | Time | Problems | Must-do |
|---|---|---|---|
| [CS201](../../../02_year_2_core_computer_science/semester_3/CS201_algorithms_and_complexity/README.md) lessons 5.1, 5.4 | ~10 hours | 12 | 3 |

When the state needs two numbers, the table becomes two-dimensional. Three families cover most interview questions:

- **Grid DP:** `dp[r][c]` is the best (or count) for reaching cell (r, c). Moves only go right/down (or down a triangle), so the grid is a DAG and a row-by-row order works.
- **Interval DP:** `dp[l][r]` is the answer for the sub-array `l..r`. Compute by increasing interval length.
- **Game DP:** `dp[l][r]` is the best score *difference* the player to move can force on `l..r`.

The five parts from [Pattern 19](19_dp_1d.md) still apply: state, recurrence, base cases, order, answer.

## Recognise it

| When you see… | Think… |
|---|---|
| "number of paths / minimum path sum" in a grid, moving right or down | grid DP; keep one row |
| "largest square of 1s" | `dp[r][c]` = side of the largest square ending at (r, c) |
| "minimum starting health so you never drop to 0" | DP **backwards** from the goal |
| two agents moving together (two robots, there-and-back) | add both positions to the state, move in lockstep |
| "best order to remove/burst/merge items", cost depends on neighbours | interval DP; choose the **last** item in the interval |
| two players alternately take from the ends, both play optimally | game DP on score difference |

## Core templates

**Grid paths with one row of memory.** `dp[c]` holds the value for the cell above before it is overwritten with the current row's value.

```python
def unique_paths_with_obstacles(grid):
    n = len(grid[0])
    dp = [0] * n
    dp[0] = 1
    for row in grid:
        for c in range(n):
            if row[c] == 1:
                dp[c] = 0                          # blocked: no path ends here
            elif c > 0:
                dp[c] += dp[c - 1]                 # from above (old dp[c]) + from the left
    return dp[-1]


def min_path_sum(grid):
    m, n = len(grid), len(grid[0])
    dp = [float("inf")] * n
    dp[0] = 0
    for r in range(m):
        dp[0] += grid[r][0]
        for c in range(1, n):
            dp[c] = grid[r][c] + min(dp[c], dp[c - 1])
    return dp[-1]
```

**Largest square.** A square of side k ends at (r, c) only if squares of side k − 1 end above, left and diagonally above-left.

```python
def maximal_square(matrix):
    m, n = len(matrix), len(matrix[0])
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    best = 0
    for r in range(m):
        for c in range(n):
            if matrix[r][c] == "1":
                dp[r + 1][c + 1] = 1 + min(dp[r][c + 1], dp[r + 1][c], dp[r][c])
                best = max(best, dp[r + 1][c + 1])
    return best * best
```

**Backwards DP (Dungeon Game).** `need[r][c]` is the minimum health needed when entering (r, c). The future decides the requirement, so compute from the goal.

```python
def calculate_minimum_hp(dungeon):
    m, n = len(dungeon), len(dungeon[0])
    INF = float("inf")
    need = [[INF] * (n + 1) for _ in range(m + 1)]
    need[m][n - 1] = need[m - 1][n] = 1            # after the goal you need 1 health
    for r in range(m - 1, -1, -1):
        for c in range(n - 1, -1, -1):
            nxt = min(need[r + 1][c], need[r][c + 1])
            need[r][c] = max(1, nxt - dungeon[r][c])
    return need[0][0]
```

**Two agents in lockstep (Cherry Pickup II).** State: the row and both robots' columns; if they share a cell, count it once.

```python
def cherry_pickup(grid):
    m, n = len(grid), len(grid[0])
    NEG = float("-inf")
    dp = [[NEG] * n for _ in range(n)]
    dp[0][n - 1] = grid[0][0] + grid[0][n - 1]
    for r in range(1, m):
        new = [[NEG] * n for _ in range(n)]
        for a in range(n):
            for b in range(n):
                prev = max(
                    (dp[pa][pb] for pa in (a - 1, a, a + 1) for pb in (b - 1, b, b + 1)
                     if 0 <= pa < n and 0 <= pb < n),
                    default=NEG,
                )
                if prev == NEG:
                    continue
                gain = grid[r][a] + (grid[r][b] if a != b else 0)
                new[a][b] = prev + gain
        dp = new
    return max(max(row) for row in dp)
```

**Interval DP: choose the last item (Burst Balloons).** If balloon k is burst *last* in `(l, r)`, its neighbours at that moment are exactly `l` and `r`, so the two sides become independent.

```python
def max_coins(nums):
    a = [1] + nums + [1]
    n = len(a)
    dp = [[0] * n for _ in range(n)]               # dp[l][r]: best for balloons strictly between l and r
    for length in range(2, n):
        for l in range(0, n - length):
            r = l + length
            dp[l][r] = max(dp[l][k] + a[l] * a[k] * a[r] + dp[k][r] for k in range(l + 1, r))
    return dp[0][n - 1]
```

**Game DP on score difference.** The player to move takes one end; the opponent then plays optimally on the rest.

```python
def stone_game_diff(piles):
    n = len(piles)
    dp = [[0] * n for _ in range(n)]               # dp[l][r]: (mover's total) - (other's total)
    for i in range(n):
        dp[i][i] = piles[i]
    for length in range(2, n + 1):
        for l in range(0, n - length + 1):
            r = l + length - 1
            dp[l][r] = max(piles[l] - dp[l + 1][r], piles[r] - dp[l][r - 1])
    return dp[0][n - 1]
```

**Java.**

```java
static int uniquePathsWithObstacles(int[][] grid) {
    int n = grid[0].length;
    int[] dp = new int[n];
    dp[0] = 1;
    for (int[] row : grid)
        for (int c = 0; c < n; c++) {
            if (row[c] == 1) dp[c] = 0;
            else if (c > 0) dp[c] += dp[c - 1];
        }
    return dp[n - 1];
}

static int maximalSquare(char[][] matrix) {
    int m = matrix.length, n = matrix[0].length, best = 0;
    int[][] dp = new int[m + 1][n + 1];
    for (int r = 0; r < m; r++)
        for (int c = 0; c < n; c++)
            if (matrix[r][c] == '1') {
                dp[r + 1][c + 1] = 1 + Math.min(dp[r][c], Math.min(dp[r][c + 1], dp[r + 1][c]));
                best = Math.max(best, dp[r + 1][c + 1]);
            }
    return best * best;
}
```

## Complexity

Grid DP: O(m · n) time, O(n) space with one row. Cherry Pickup II: O(m · n² · 9). Interval DP: O(n²) states × O(n) choices = O(n³) time, O(n²) space. Game DP on ends: O(n²).

## Common bugs

1. Computing the dungeon forwards (exercise 1).
2. Iterating interval DP by `l` and `r` instead of by length, so `dp[l][k]` or `dp[k][r]` is read before it is computed.
3. Choosing the *first* balloon to burst instead of the last, which leaves the two sides dependent.
4. Double-counting a shared cell when two agents meet.
5. One-row grid DP updated right-to-left when the recurrence needs the new left value (or vice versa).
6. Forgetting obstacles in the first row or column (everything after an obstacle is unreachable).

## Problems (easy → hard)

Lists: **B75** Blind 75 · **N150** NeetCode 150 · **N250** NeetCode 250. ★ = in the [must-do 100](../problem_list.md).

| # | Problem | Level | What it teaches | Lists |
|---|---|---|---|---|
| 1 | [Pascal's Triangle](https://leetcode.com/problems/pascals-triangle/) | Easy | each row from the previous one | |
| 2 | ★ [Unique Paths](https://leetcode.com/problems/unique-paths/) | Medium | grid counting; one-row DP; the closed form C(m + n − 2, m − 1) | B75 · N150 · N250 |
| 3 | [Unique Paths II](https://leetcode.com/problems/unique-paths-ii/) | Medium | obstacles as zeroed states | N250 |
| 4 | [Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/) | Medium | min instead of count | N250 |
| 5 | [Triangle](https://leetcode.com/problems/triangle/) | Medium | bottom-up removes edge cases | |
| 6 | [Minimum Falling Path Sum](https://leetcode.com/problems/minimum-falling-path-sum/) | Medium | three predecessors per cell | |
| 7 | ★ [Maximal Square](https://leetcode.com/problems/maximal-square/) | Medium | the min-of-three recurrence | |
| 8 | [Count Square Submatrices with All Ones](https://leetcode.com/problems/count-square-submatrices-with-all-ones/) | Medium | the same table, summed | |
| 9 | [Stone Game](https://leetcode.com/problems/stone-game/) | Medium | score-difference game DP (and a proof that the first player wins) | N250 |
| 10 | [Dungeon Game](https://leetcode.com/problems/dungeon-game/) | Hard | backwards DP | |
| 11 | [Cherry Pickup II](https://leetcode.com/problems/cherry-pickup-ii/) | Hard | two agents in one state | |
| 12 | ★ [Burst Balloons](https://leetcode.com/problems/burst-balloons/) | Hard | interval DP; choose the last item | N150 · N250 |

[Longest Increasing Path in a Matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/) (memoised DFS on a grid DAG) is listed under [Pattern 15](15_topological_sort.md).

## AI-era exercises

**Exercise 1 · Wrong direction.** An assistant's Dungeon Game picks the path with the largest total, then computes the health that path needs:

```python
def calculate_minimum_hp_ai(dungeon):
    m, n = len(dungeon), len(dungeon[0])
    total = [[0] * n for _ in range(m)]
    came = [[None] * n for _ in range(m)]
    for r in range(m):
        for c in range(n):
            best, frm = None, None
            if r > 0:
                best, frm = total[r - 1][c], (r - 1, c)
            if c > 0 and (best is None or total[r][c - 1] > best):
                best, frm = total[r][c - 1], (r, c - 1)
            total[r][c] = dungeon[r][c] + (best or 0)
            came[r][c] = frm
    path, cell = [], (m - 1, n - 1)
    while cell:
        path.append(dungeon[cell[0]][cell[1]])
        cell = came[cell[0]][cell[1]]
    running, lowest = 0, 0
    for v in reversed(path):
        running += v
        lowest = min(lowest, running)
    return 1 - lowest
```

Find a 2 × 3 grid where it asks for far more health than needed, and explain why "best total" is the wrong objective.

<details><summary>Answer</summary>

`[[0, -10, 20], [-1, -1, -1]]`: the right-right-down path has the best total (+9) but dips to −10 on the way, so the code returns 11. The path down-right-right never dips below −3, so 4 health is enough. The requirement depends on the lowest point of the running sum, and that depends on what comes *after* each cell, which is why the correct DP runs backwards from the goal. A brute force over all right/down paths on grids up to 3 × 3 catches this.
</details>

**Exercise 2 · Check a too-short answer.** Asked for Stone Game (even number of piles, odd total, both players optimal; return whether the first player wins), an assistant replied `return True` with a short proof. Verify the claim with `stone_game_diff` on random inputs, then write the proof yourself.

```python
def stone_game_ai(piles):
    return True
```

<details><summary>Answer</summary>

It is correct under the problem's constraints. Colour the piles alternately by index parity. With an even number of piles, the first player can always take a pile of the colour she chooses: at the start the two ends have different colours, and whatever the opponent takes, one end of her chosen colour is again exposed. So she can collect all even-indexed piles or all odd-indexed piles. The total is odd, so one colour has the larger sum, and she picks that one. The DP agrees on every random test with even length and odd sum, and the answer changes once you drop either constraint (try three piles). Accepting a short AI answer is fine when you can prove it and state the conditions it depends on.
</details>

## You own this pattern when

- You can say for any grid DP which neighbours a cell depends on and pick the loop order from that.
- You solve Burst Balloons from the "last balloon" idea in under 25 minutes, AI off.
- You recognise when the DP must run backwards (requirements that depend on the future).
