# DSA for hiring · Pattern 02 · Two pointers

| Theory first | Time | Problems | Must-do |
|---|---|---|---|
| [FND112](../../../01_year_1_foundations/semester_2/FND112_data_structures_and_algorithms_i/README.md) lessons 4.1, 4.2, 4.5 | ~8 hours | 15 | 5 |

Two indices move through a sequence so that each step discards something that provably cannot be part of the answer. The whole skill is stating *why* a discard is safe. Interviewers ask for that sentence.

## Recognise it

| When you see… | Think… |
|---|---|
| sorted array + "pair/triple with sum X" | opposite-end pointers; move the side that cannot help |
| "in place", "O(1) extra space", "remove/compact/partition" | a read pointer and a write pointer moving the same way |
| "palindrome", "compare from both ends" | `l` from the left, `r` from the right, meet in the middle |
| "3 values / 3 colours, one pass" | Dutch national flag: three regions `[0, lo)`, `[lo, i)`, `(hi, n)` |
| "maximise area/width between two lines" | start widest, move the shorter side |
| unsorted input, sum of pairs, sorting allowed | sort first (O(n log n)), then pointers; say so aloud |

**Not this pattern when** you need original indices from unsorted input and cannot sort (use a hash map, [Pattern 01](01_arrays_and_hashing.md)), or the condition is about a contiguous window whose validity changes with its contents (use [sliding window](03_sliding_window.md)).

## Core templates

**Opposite ends on sorted input.** Invariant: every pair outside `[l, r]` has already been ruled out.

```python
def two_sum_sorted(nums, target):
    l, r = 0, len(nums) - 1
    while l < r:
        s = nums[l] + nums[r]
        if s == target:
            return [l, r]
        if s < target:
            l += 1          # nums[l] + (anything <= nums[r]) is too small: drop l
        else:
            r -= 1          # nums[r] + (anything >= nums[l]) is too large: drop r
    return []
```

**Read/write compaction.** `w` marks the end of the kept prefix; `r` scans.

```python
def remove_duplicates_sorted(nums):
    if not nums:
        return 0
    w = 1
    for r in range(1, len(nums)):
        if nums[r] != nums[w - 1]:
            nums[w] = nums[r]
            w += 1
    return w                 # nums[:w] holds the unique values
```

**Sort, fix one, two-pointer the rest (3Sum).** Skip duplicates at both levels, or the output repeats triples.

```python
def three_sum(nums):
    nums = sorted(nums)
    out = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        if nums[i] > 0:
            break                       # smallest value positive: no zero sum
        l, r = i + 1, len(nums) - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0:
                l += 1
            elif s > 0:
                r -= 1
            else:
                out.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
    return out
```

**Move the shorter side.** Any container using the shorter line with a closer partner is narrower and no taller, so the shorter line can be discarded.

```python
def max_area(height):
    l, r, best = 0, len(height) - 1, 0
    while l < r:
        best = max(best, (r - l) * min(height[l], height[r]))
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return best
```

**Dutch national flag.** After a swap with `hi`, the incoming value is unexamined, so `i` must stay put.

```python
def sort_colors(a):
    lo, i, hi = 0, 0, len(a) - 1
    while i <= hi:
        if a[i] == 0:
            a[lo], a[i] = a[i], a[lo]
            lo += 1
            i += 1
        elif a[i] == 2:
            a[i], a[hi] = a[hi], a[i]
            hi -= 1                  # do not advance i
        else:
            i += 1
```

**Trapping rain water with two pointers.** Water above a bar is bounded by the smaller of the two side maxima; the side with the smaller maximum is already decided.

```python
def trap(height):
    l, r = 0, len(height) - 1
    lmax = rmax = water = 0
    while l < r:
        if height[l] < height[r]:
            lmax = max(lmax, height[l])
            water += lmax - height[l]
            l += 1
        else:
            rmax = max(rmax, height[r])
            water += rmax - height[r]
            r -= 1
    return water
```

**Java (3Sum).**

```java
static List<List<Integer>> threeSum(int[] nums) {
    int[] a = nums.clone();
    Arrays.sort(a);
    List<List<Integer>> out = new ArrayList<>();
    for (int i = 0; i + 2 < a.length; i++) {
        if (i > 0 && a[i] == a[i - 1]) continue;
        int l = i + 1, r = a.length - 1;
        while (l < r) {
            int s = a[i] + a[l] + a[r];
            if (s < 0) l++;
            else if (s > 0) r--;
            else {
                out.add(List.of(a[i], a[l], a[r]));
                l++; r--;
                while (l < r && a[l] == a[l - 1]) l++;
            }
        }
    }
    return out;
}
```

## Complexity

Each pointer moves monotonically, so a single pass is O(n). 3Sum is O(n²) after an O(n log n) sort; 4Sum is O(n³). Space is O(1) beyond the output, except that sorting a copy costs O(n) and Python's sort uses up to O(n) auxiliary memory.

## Common bugs

1. `while l <= r` in pair problems lets an element pair with itself.
2. Advancing `i` after swapping with `hi` in the Dutch flag (see exercise 1).
3. Skipping duplicates *before* recording a triple, or only at one level, which drops or repeats answers.
4. Sorting when the problem needs original indices (Two Sum on unsorted input): sort `(value, index)` pairs or use a map.
5. In 4Sum, Java `int` overflow on `a[i] + a[j] + a[k] + a[l]` with values near 10⁹: use `long`.
6. Moving the taller line in Container With Most Water: it can only lose.

## Problems (easy → hard)

Lists: **B75** Blind 75 · **N150** NeetCode 150 · **N250** NeetCode 250. ★ = in the [must-do 100](../problem_list.md).

| # | Problem | Level | What it teaches | Lists |
|---|---|---|---|---|
| 1 | ★ [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | Easy | skip non-alphanumerics without building a new string | B75 · N150 · N250 |
| 2 | [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/) | Easy | fill from the back so nothing is overwritten | N250 |
| 3 | [Move Zeroes](https://leetcode.com/problems/move-zeroes/) | Easy | read/write compaction, stable order | |
| 4 | [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) | Easy | compare with the last *kept* value | N250 |
| 5 | [Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/) | Easy | the largest square is at one of the two ends | |
| 6 | [Is Subsequence](https://leetcode.com/problems/is-subsequence/) | Easy | two pointers on two different sequences | |
| 7 | [Valid Palindrome II](https://leetcode.com/problems/valid-palindrome-ii/) | Easy | one allowed mismatch: try both skips | N250 |
| 8 | ★ [Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | Medium | the discard argument in its purest form | N150 · N250 |
| 9 | ★ [3Sum](https://leetcode.com/problems/3sum/) | Medium | sort, fix one, duplicate skipping | B75 · N150 · N250 |
| 10 | ★ [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | Medium | the exchange argument for moving the shorter side | B75 · N150 · N250 |
| 11 | [Sort Colors](https://leetcode.com/problems/sort-colors/) | Medium | three-region invariant | N250 |
| 12 | [Boats to Save People](https://leetcode.com/problems/boats-to-save-people/) | Medium | greedy pairing of heaviest with lightest | N250 |
| 13 | [Rotate Array](https://leetcode.com/problems/rotate-array/) | Medium | three reversals; `k %= n` | N250 |
| 14 | [4Sum](https://leetcode.com/problems/4sum/) | Medium | generalising k-sum; overflow | N250 |
| 15 | ★ [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) | Hard | prefix maxima vs two pointers vs stack | N150 · N250 |

## AI-era exercises

**Exercise 1 · Find the bug.** An assistant's Sort Colors:

```python
def sort_colors_ai(a):
    lo, i, hi = 0, 0, len(a) - 1
    while i <= hi:
        if a[i] == 0:
            a[lo], a[i] = a[i], a[lo]
            lo += 1
            i += 1
        elif a[i] == 2:
            a[i], a[hi] = a[hi], a[i]
            hi -= 1
            i += 1
        else:
            i += 1
    return a
```

Find a failing input of length 3, then write the invariant that the fix restores.

<details><summary>Answer</summary>

`[1, 2, 0]` returns `[1, 0, 2]`. At `i = 1` the 2 is swapped with the 0 at `hi`, and `i` moves past the 0 without examining it. The invariant is: `a[0:lo]` are 0s, `a[lo:i]` are 1s, `a[hi+1:]` are 2s, and `a[i:hi+1]` is unexamined. A value swapped in from `hi` comes from the unexamined region, so `i` must not advance. Exhaustive testing of all 3⁵ = 243 arrays of length 5 finds this in milliseconds; do that before trusting any partition code.
</details>

**Exercise 2 · Make the assistant prove it.** Another assistant's `max_area` uses `if height[l] > height[r]: l += 1 else: r -= 1` (it moves the *taller* side). Find an input where it is wrong, then write the two-sentence argument for moving the shorter side that you would say in an interview.

```python
def max_area_ai(height):
    l, r, best = 0, len(height) - 1, 0
    while l < r:
        best = max(best, (r - l) * min(height[l], height[r]))
        if height[l] > height[r]:
            l += 1
        else:
            r -= 1
    return best
```

<details><summary>Answer</summary>

`[1, 8, 6, 2, 5, 4, 8, 3, 7]` should give 49 (lines at indices 1 and 8) but the buggy version returns 8: it drops the 7 at the right end on the first step and never reaches the pair (1, 8). Argument: the area is limited by the shorter line. Every container that keeps the shorter line and moves the other end inward is narrower and no taller, so none of them can beat the current one, and the shorter line can be discarded safely. Moving the taller line gives no such guarantee.
</details>

## You own this pattern when

- You write 3Sum with correct duplicate handling in under 15 minutes and explain both skip rules.
- You can state, for any two-pointer solution you write, the one-sentence reason a discard is safe.
- You test partition code exhaustively on all small arrays, not just the sample.
