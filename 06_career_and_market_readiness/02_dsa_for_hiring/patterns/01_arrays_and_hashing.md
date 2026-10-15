# DSA for hiring · Pattern 01 · Arrays and hashing

| Theory first | Time | Problems | Must-do |
|---|---|---|---|
| [FND112](../../../01_year_1_foundations/semester_2/FND112_data_structures_and_algorithms_i/README.md) chapters 3 and 6 (arrays, hash tables) | ~8 hours | 15 | 6 |

Hash maps and sets turn "search the array again" into an expected O(1) lookup. Most first-round problems either are a hashing problem or contain one as a step, so this pattern comes first.

## Recognise it

| When you see… | Think… |
|---|---|
| "find two items that combine to a target", "has this been seen before?" | one pass with a map from value to index (complement lookup) |
| "group items that are equivalent" (anagrams, same shape, same pattern) | a **canonical key**: sorted letters, a count tuple, a normalised form |
| "most frequent", "count of each", "majority" | `Counter` / `HashMap.merge`; bucket by frequency for O(n) top-k |
| "longest run of consecutive values" in unsorted input | a set, and start counting only at run starts |
| values in the range 1..n, O(1) extra space demanded | the array itself is the hash table: index `v - 1` stores value `v` |
| a grid or matrix to validate, rotate or scan | index arithmetic; sets keyed by row, column or box |

**Not this pattern when** the input is sorted and memory is tight (use [two pointers](02_two_pointers.md)), the question is about contiguous subarrays (use [sliding window](03_sliding_window.md) or [prefix sums](04_prefix_sums.md)), or the order of keys matters (use a sorted structure, [Pattern 09](09_binary_search_trees.md)).

## Core templates

**Complement lookup.** Store each element *after* checking for its partner, so an element never pairs with itself.

```python
from collections import Counter, defaultdict


def two_sum(nums, target):
    seen = {}                          # value -> index of an earlier element
    for i, x in enumerate(nums):
        j = seen.get(target - x)
        if j is not None:
            return [j, i]
        seen[x] = i                    # insert after the check
    return []
```

**Canonical key.** Two items belong together exactly when their keys are equal. A count tuple costs O(k) per word of length k; sorting costs O(k log k).

```python
def group_anagrams(words):
    groups = defaultdict(list)
    for w in words:
        key = [0] * 26
        for ch in w:
            key[ord(ch) - ord("a")] += 1
        groups[tuple(key)].append(w)   # lists are unhashable; tuples are not
    return list(groups.values())
```

**Frequency buckets.** A frequency is at most n, so bucket index = frequency gives top-k in O(n) without a heap.

```python
def top_k_frequent(nums, k):
    count = Counter(nums)
    buckets = [[] for _ in range(len(nums) + 1)]
    for x, c in count.items():
        buckets[c].append(x)
    out = []
    for c in range(len(buckets) - 1, 0, -1):
        for x in buckets[c]:
            out.append(x)
            if len(out) == k:
                return out
    return out
```

**Run starts.** The inner loop runs only from a value whose predecessor is absent, so every value is visited by at most one inner loop: O(n) total.

```python
def longest_consecutive(nums):
    s = set(nums)
    best = 0
    for x in s:
        if x - 1 not in s:             # x starts a run
            y = x
            while y + 1 in s:
                y += 1
            best = max(best, y - x + 1)
    return best
```

**The array as its own hash table.** For values that should be 1..n, swap each value into slot `v - 1`. Each swap puts one value in its final place, so there are at most n swaps.

```python
def first_missing_positive(nums):
    n = len(nums)
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            j = nums[i] - 1            # compute the target index BEFORE swapping
            nums[i], nums[j] = nums[j], nums[i]
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    return n + 1
```

**Java.** `getOrDefault`, `merge` and `computeIfAbsent` replace most hand-written "if absent" branches.

```java
static int[] twoSum(int[] nums, int target) {
    Map<Integer, Integer> seen = new HashMap<>();
    for (int i = 0; i < nums.length; i++) {
        Integer j = seen.get(target - nums[i]);
        if (j != null) return new int[]{j, i};
        seen.put(nums[i], i);
    }
    return new int[0];
}

static List<List<String>> groupAnagrams(String[] words) {
    Map<String, List<String>> groups = new HashMap<>();
    for (String w : words) {
        int[] cnt = new int[26];
        for (char ch : w.toCharArray()) cnt[ch - 'a']++;
        groups.computeIfAbsent(Arrays.toString(cnt), k -> new ArrayList<>()).add(w);
    }
    return new ArrayList<>(groups.values());
}

static Map<Integer, Integer> counts(int[] nums) {
    Map<Integer, Integer> c = new HashMap<>();
    for (int x : nums) c.merge(x, 1, Integer::sum);
    return c;
}
```

## Complexity

| Template | Time | Extra space |
|---|---|---|
| Complement lookup | O(n) expected | O(n) |
| Canonical key (count tuple) | O(total characters) | O(total characters) |
| Frequency buckets | O(n) | O(n) |
| Run starts | O(n) expected | O(n) |
| Array as hash table | O(n) (at most n swaps) | O(1) |

"Expected" matters: hash operations are O(1) on average, O(n) per operation in the worst case for adversarial keys ([FND112](../../../01_year_1_foundations/semester_2/FND112_data_structures_and_algorithms_i/README.md) lesson 6.4). Say this in an interview when asked about worst cases.

## Common bugs

1. Inserting before checking in Two Sum, so `[3]` with target 6 pairs index 0 with itself.
2. Python swap with a computed index: `nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i]` assigns `nums[i]` first, then evaluates `nums[i] - 1` with the *new* value. Compute `j` first.
3. Using a list as a dictionary key (`TypeError: unhashable type`); convert to a tuple.
4. A key that is not canonical: `sum(ord(c))` or a product of letter codes collides for non-anagrams.
5. Java: comparing two `Integer` objects with `==`. It works for -128..127 (the cache) and fails above; use `.equals` or unbox.
6. Iterating over a dict while modifying it (`RuntimeError` in Python, `ConcurrentModificationException` in Java).
7. Forgetting that `Counter` subtraction drops zero and negative counts.

## Problems (easy → hard)

Lists: **B75** Blind 75 · **N150** NeetCode 150 · **N250** NeetCode 250. ★ = in the [must-do 100](../problem_list.md).

| # | Problem | Level | What it teaches | Lists |
|---|---|---|---|---|
| 1 | ★ [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | Easy | set membership; the O(n log n) sort alternative when memory is tight | B75 · N150 · N250 |
| 2 | ★ [Valid Anagram](https://leetcode.com/problems/valid-anagram/) | Easy | count arrays vs `Counter`; what changes for Unicode input | B75 · N150 · N250 |
| 3 | ★ [Two Sum](https://leetcode.com/problems/two-sum/) | Easy | complement lookup, insert-after-check | B75 · N150 · N250 |
| 4 | [Isomorphic Strings](https://leetcode.com/problems/isomorphic-strings/) | Easy | a mapping must be checked in both directions | |
| 5 | [Majority Element](https://leetcode.com/problems/majority-element/) | Easy | counting, then Boyer-Moore voting for O(1) space | N250 |
| 6 | ★ [Group Anagrams](https://leetcode.com/problems/group-anagrams/) | Medium | canonical keys | B75 · N150 · N250 |
| 7 | ★ [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | Medium | bucket by frequency vs a size-k heap | B75 · N150 · N250 |
| 8 | [Encode and Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/) (Premium; free mirror [LintCode 659](https://www.lintcode.com/problem/659/)) | Medium | length-prefix framing, the idea behind real wire protocols | B75 · N150 · N250 |
| 9 | ★ [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) | Medium | run starts; amortised O(n) | B75 · N150 · N250 |
| 10 | [Valid Sudoku](https://leetcode.com/problems/valid-sudoku/) | Medium | sets keyed by row, column and box index `(r // 3, c // 3)` | N150 · N250 |
| 11 | [Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/) | Medium | reuse the first row and column as marker storage | B75 · N150 · N250 |
| 12 | [Rotate Image](https://leetcode.com/problems/rotate-image/) | Medium | transpose then reverse rows, in place | B75 · N150 · N250 |
| 13 | [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/) | Medium | four shrinking boundaries; stopping conditions for one row or column | B75 · N150 · N250 |
| 14 | [Find All Duplicates in an Array](https://leetcode.com/problems/find-all-duplicates-in-an-array/) | Medium | sign-marking: the array as a visited set | |
| 15 | [First Missing Positive](https://leetcode.com/problems/first-missing-positive/) | Hard | cyclic placement in O(n) time, O(1) space | N250 |

## AI-era exercises

**Exercise 1 · Find the bug.** An assistant was asked to group anagrams "faster than sorting each word" and returned this. It passes the sample `["eat","tea","tan","ate","nat","bat"]`.

```python
def group_anagrams_ai(words):
    groups = {}
    for w in words:
        key = sum(ord(c) for c in w)      # "same letters -> same sum"
        groups.setdefault(key, []).append(w)
    return list(groups.values())
```

Find the smallest input on which it is wrong, explain why the sample did not catch it, and fix it without sorting.

<details><summary>Answer</summary>

The key is not canonical: different multisets of letters can have the same sum. `["ad", "bc"]` gives 97 + 100 = 98 + 99 = 197, so two non-anagrams are grouped. The sample only contains words whose sums happen to differ. Any key built by a lossy operation (sum, xor, product modulo something) has this flaw. Use the 26-count tuple:

```python
def group_anagrams_fixed(words):
    groups = {}
    for w in words:
        cnt = [0] * 26
        for c in w:
            cnt[ord(c) - 97] += 1
        groups.setdefault(tuple(cnt), []).append(w)
    return list(groups.values())
```

Habit to build: when an AI invents a "faster key", ask whether two different inputs can share it, and test with a brute-force grouping on random short words.
</details>

**Exercise 2 · Prove the complexity.** An assistant claims this is O(n):

```python
def longest_consecutive_ai(nums):
    s = set(nums)
    best = 0
    for x in s:
        y = x
        while y + 1 in s:
            y += 1
        best = max(best, y - x + 1)
    return best
```

Is the claim true? Give an input family that shows the real growth, count the set lookups for it, and confirm by timing n = 2,000, 4,000 and 8,000.

<details><summary>Answer</summary>

It is O(n²) in the worst case. On `list(range(n))` the inner loop starts from every value: from x it makes n − x lookups, so about n²/2 lookups in total. Doubling n should roughly quadruple the time. The fix is the run-start check `if x - 1 not in s`, which makes each value part of exactly one inner loop, giving O(n). Many AI answers to this problem include the check; when one does not, the code still passes small tests, which is why a doubling experiment is the right tool.
</details>

## You own this pattern when

- You solve problems 3, 6, 7 and 9 from a blank file in under 15 minutes each, AI off, and state the expected and worst-case complexity unprompted.
- You can explain why a count tuple is a canonical key and a letter sum is not.
- You write First Missing Positive without the swap bug and argue the O(n) bound from "each swap fixes one value".
