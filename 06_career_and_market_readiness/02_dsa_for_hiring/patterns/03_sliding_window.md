# DSA for hiring · Pattern 03 · Sliding window

| Theory first | Time | Problems | Must-do |
|---|---|---|---|
| [FND112](../../../01_year_1_foundations/semester_2/FND112_data_structures_and_algorithms_i/README.md) lessons 4.3, 4.4 | ~10 hours | 13 | 6 |

A window `[l, r]` over a sequence grows on the right and shrinks on the left while you maintain a summary of its contents (a sum, a count map, a deque). It works when validity is **monotone**: if a window is invalid, every larger window containing it is invalid too (or the reverse). That condition is what you must check before using it.

## Recognise it

| When you see… | Think… |
|---|---|
| "longest/shortest **contiguous** subarray/substring such that…" | variable window |
| "every window of size k", "average/max of each k-window" | fixed window, O(1) update per step |
| "contains all characters of t", "is a permutation/anagram of p" | count map + a counter of satisfied keys |
| "at most k distinct / k replacements / k zeros flipped" | variable window with a budget |
| "exactly k distinct" | `at_most(k) - at_most(k - 1)` |
| "max/min of every window" | monotonic deque |
| "buy low, sell later" | a one-sided window: keep the best left end so far |

**Not this pattern when** the array has negative numbers and the condition is on a sum: adding an element can make the sum smaller, so validity is not monotone. Use [prefix sums](04_prefix_sums.md) with a hash map, or a monotonic deque over prefix sums (Shortest Subarray with Sum at Least K).

## Core templates

**Longest valid window.** Expand `r`; while the window is invalid, shrink `l`; the window is valid when you record.

```python
from collections import Counter, defaultdict, deque


def length_of_longest_substring(s):
    last = {}                 # char -> last index seen
    l = best = 0
    for r, ch in enumerate(s):
        if ch in last and last[ch] >= l:
            l = last[ch] + 1   # jump l past the previous copy
        last[ch] = r
        best = max(best, r - l + 1)
    return best
```

**Shortest valid window** (positive numbers only). Record while valid, then shrink.

```python
def min_subarray_len(target, nums):
    l = total = 0
    best = float("inf")
    for r, x in enumerate(nums):
        total += x
        while total >= target:
            best = min(best, r - l + 1)
            total -= nums[l]
            l += 1
    return 0 if best == float("inf") else best
```

**Budget window.** Valid while `length - count of most frequent letter <= k`. `maxf` may be stale (too high) after shrinking, but a stale value only stops the window from growing, never produces a wrong longer answer.

```python
def character_replacement(s, k):
    count = defaultdict(int)
    l = maxf = best = 0
    for r, ch in enumerate(s):
        count[ch] += 1
        maxf = max(maxf, count[ch])
        while (r - l + 1) - maxf > k:
            count[s[l]] -= 1
            l += 1
        best = max(best, r - l + 1)
    return best
```

**Cover all required characters.** `formed` counts keys whose requirement is met, so the validity check is O(1).

```python
def min_window(s, t):
    need = Counter(t)
    have = defaultdict(int)
    formed, required = 0, len(need)
    l, best = 0, (float("inf"), 0, 0)
    for r, ch in enumerate(s):
        have[ch] += 1
        if ch in need and have[ch] == need[ch]:
            formed += 1
        while formed == required:
            if r - l + 1 < best[0]:
                best = (r - l + 1, l, r + 1)
            left = s[l]
            have[left] -= 1
            if left in need and have[left] < need[left]:
                formed -= 1
            l += 1
    return "" if best[0] == float("inf") else s[best[1]:best[2]]
```

**Exactly k = at most k minus at most k − 1.**

```python
def subarrays_with_k_distinct(nums, k):
    def at_most(k):
        count = defaultdict(int)
        l = res = 0
        for r, x in enumerate(nums):
            if count[x] == 0:
                k -= 1
            count[x] += 1
            while k < 0:
                count[nums[l]] -= 1
                if count[nums[l]] == 0:
                    k += 1
                l += 1
            res += r - l + 1        # windows ending at r
        return res
    return at_most(k) - at_most(k - 1)
```

**Window maximum with a monotonic deque.** The deque holds indices with decreasing values; the front is the maximum.

```python
def max_sliding_window(nums, k):
    dq, out = deque(), []
    for i, x in enumerate(nums):
        while dq and nums[dq[-1]] <= x:
            dq.pop()                 # smaller values can never be a future max
        dq.append(i)
        if dq[0] <= i - k:
            dq.popleft()             # front left the window
        if i >= k - 1:
            out.append(nums[dq[0]])
    return out
```

**Java.** A fixed `int[128]` beats a `HashMap<Character, Integer>` for ASCII input.

```java
static int lengthOfLongestSubstring(String s) {
    int[] last = new int[128];
    Arrays.fill(last, -1);
    int l = 0, best = 0;
    for (int r = 0; r < s.length(); r++) {
        char c = s.charAt(r);
        if (last[c] >= l) l = last[c] + 1;
        last[c] = r;
        best = Math.max(best, r - l + 1);
    }
    return best;
}
```

## Complexity

Both pointers only move forward, so a window does at most 2n pointer moves: O(n) time even with a nested `while`. Space is O(size of the alphabet or distinct keys), O(k) for the deque. The "exactly k" trick doubles the constant, not the order.

## Common bugs

1. Using a sum window with negative numbers (exercise 1).
2. Recording the answer in the wrong place: for "longest" record after shrinking; for "shortest" record inside the shrink loop.
3. In the last-seen version, jumping `l` *backwards* when the previous copy is left of the window; guard with `last[ch] >= l`.
4. Checking `all(have[c] >= need[c] for c in need)` on every step: correct but O(n·m) for m distinct required keys.
5. Off-by-one on window length: `r - l + 1`, not `r - l`.
6. Deque storing values instead of indices, so you cannot tell when the front left the window.

## Problems (easy → hard)

Lists: **B75** Blind 75 · **N150** NeetCode 150 · **N250** NeetCode 250. ★ = in the [must-do 100](../problem_list.md).

| # | Problem | Level | What it teaches | Lists |
|---|---|---|---|---|
| 1 | ★ [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | Easy | keep the best left end so far | B75 · N150 · N250 |
| 2 | [Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii/) | Easy | a fixed-size window as a set | N250 |
| 3 | [Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/) | Easy | fixed window, add one and remove one | |
| 4 | ★ [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | Medium | the canonical variable window; last-seen jump | B75 · N150 · N250 |
| 5 | ★ [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) | Medium | budget windows; why a stale max is safe | B75 · N150 · N250 |
| 6 | ★ [Permutation in String](https://leetcode.com/problems/permutation-in-string/) | Medium | fixed window of counts, O(26) or O(1) compare | N150 · N250 |
| 7 | [Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/) | Medium | same as 6, collecting every start | |
| 8 | [Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/) | Medium | shortest valid window; requires positives | N250 |
| 9 | [Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/) | Medium | "flip at most k" as a budget | |
| 10 | [Fruit Into Baskets](https://leetcode.com/problems/fruit-into-baskets/) | Medium | at most 2 distinct, disguised | |
| 11 | [Subarrays with K Different Integers](https://leetcode.com/problems/subarrays-with-k-different-integers/) | Hard | exactly k = at most k − at most (k − 1) | |
| 12 | ★ [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) | Hard | the `formed` counter for O(1) validity | B75 · N150 · N250 |
| 13 | ★ [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) | Hard | monotonic deque | N150 · N250 |

## AI-era exercises

**Exercise 1 · Spot the wrong pattern.** Asked for Shortest Subarray with Sum at Least K (the array may contain negative numbers), an assistant reused the positive-only template:

```python
def shortest_subarray_ai(nums, k):
    l = total = 0
    best = float("inf")
    for r, x in enumerate(nums):
        total += x
        while total >= k:
            best = min(best, r - l + 1)
            total -= nums[l]
            l += 1
    return -1 if best == float("inf") else best
```

Find a failing input with two elements and explain which property of the window breaks.

<details><summary>Answer</summary>

`nums = [-1, 5], k = 5` should return 1 (the subarray `[5]`), but the window sum is 4 and never reaches 5, so the code returns -1. The template relies on "removing the leftmost element never increases the sum", which is false when that element is negative: the best window may start *after* a negative prefix the code never drops. The correct solution is in [Pattern 04](04_prefix_sums.md): a monotonic deque over prefix sums, O(n). Whenever an assistant applies sliding window to a sum problem, check the constraints for negative values first.
</details>

**Exercise 2 · Bound the hidden cost.** An assistant's Minimum Window Substring checks validity with `all(have[c] >= need[c] for c in need)` inside the shrink loop. It says the solution is O(n). Give the real bound in terms of n = len(s) and m = number of distinct characters in t, say when it matters (think of the problem generalised to integer IDs instead of letters), and show how the `formed` counter above removes the factor.

<details><summary>Answer</summary>

Each of the up to 2n pointer moves runs an O(m) check, so the time is O(n·m). For English letters m ≤ 52 and the difference is a constant factor. For the same problem over integer IDs (say "the shortest log segment that contains all 10⁴ required event types") with n = 10⁶, it is about 10¹⁰ operations. The `formed` counter changes only when one key crosses its requirement, so each move costs O(1) and the total is O(n + m).
</details>

## You own this pattern when

- Before writing a window, you say aloud why validity is monotone for this problem, or why it is not.
- You solve problems 4, 5 and 12 from a blank file, AI off, each in under 20 minutes.
- You can derive "exactly k" from "at most k" and explain why the count `r - l + 1` is right.
