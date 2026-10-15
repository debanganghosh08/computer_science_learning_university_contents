# DSA for hiring · Pattern 06 · Stack and monotonic stack

| Theory first | Time | Problems | Must-do |
|---|---|---|---|
| [FND112](../../../01_year_1_foundations/semester_2/FND112_data_structures_and_algorithms_i/README.md) lesson 5.3 | ~10 hours | 15 | 5 |

A stack answers "what is the most recent unfinished thing?". Use it for nesting (brackets, expressions, decoding) and, in its monotonic form, for "the nearest element to the left or right that is bigger or smaller". The monotonic stack is the single most under-practised pattern relative to how often it unlocks an O(n) solution.

## Recognise it

| When you see… | Think… |
|---|---|
| matching brackets, nested structure, "undo", path simplification | plain stack |
| expression evaluation with precedence or parentheses | operand stack (+ sign or operator stack) |
| "next greater / next warmer / previous smaller element" | monotonic stack of indices |
| "for every element, how far can it extend while it is the min/max?" | previous-smaller and next-smaller boundaries |
| "largest rectangle", "sum of minimums over all subarrays" | contribution technique with boundaries |
| "remove k digits to make the smallest number", "smallest subsequence" | greedy with an increasing stack |
| collisions moving in one direction (asteroids, cars) | stack of survivors |

## Core templates

**Brackets.** Map each closer to its opener; the stack must be empty at the end.

```python
def is_valid(s):
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for ch in s:
        if ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
        else:
            stack.append(ch)
    return not stack
```

**Min stack.** Store the minimum *so far* with each value.

```python
class MinStack:
    def __init__(self):
        self.st = []                    # (value, min of stack up to here)

    def push(self, x):
        self.st.append((x, min(x, self.st[-1][1]) if self.st else x))

    def pop(self):
        self.st.pop()

    def top(self):
        return self.st[-1][0]

    def getMin(self):
        return self.st[-1][1]
```

**Next greater element (monotonic decreasing stack).** Each index is pushed once and popped at most once, so the loop is O(n) in total.

```python
def daily_temperatures(t):
    ans = [0] * len(t)
    stack = []                          # indices with strictly decreasing temperatures
    for i, x in enumerate(t):
        while stack and t[stack[-1]] < x:
            j = stack.pop()
            ans[j] = i - j              # i is j's next warmer day
        stack.append(i)
    return ans
```

**Largest rectangle.** When a bar is popped, the current index is its next-smaller boundary and the new stack top is its previous-smaller boundary. A height-0 sentinel flushes the stack at the end.

```python
def largest_rectangle_area(heights):
    stack, best = [], 0                 # indices with increasing heights
    for i, h in enumerate(heights + [0]):
        while stack and heights[stack[-1]] >= h:
            top = stack.pop()
            left = stack[-1] if stack else -1
            best = max(best, heights[top] * (i - left - 1))
        stack.append(i)
    return best
```

**Contribution technique.** Each `a[i]` is the minimum of `left[i] * right[i]` subarrays. To count each subarray exactly once when values repeat, use *strictly* smaller on one side and *smaller-or-equal* on the other.

```python
def sum_subarray_mins(a, mod=10**9 + 7):
    n = len(a)
    left, right = [0] * n, [0] * n
    st = []
    for i in range(n):                  # previous strictly smaller
        while st and a[st[-1]] >= a[i]:
            st.pop()
        left[i] = i - (st[-1] if st else -1)
        st.append(i)
    st = []
    for i in range(n - 1, -1, -1):      # next smaller-or-equal
        while st and a[st[-1]] > a[i]:
            st.pop()
        right[i] = (st[-1] if st else n) - i
        st.append(i)
    return sum(a[i] * left[i] * right[i] for i in range(n)) % mod
```

**Expression with `+`, `-` and parentheses.** Keep a stack of signs: the sign in front of each parenthesis multiplies everything inside.

```python
def calculate(s):
    total, num, sign = 0, 0, 1
    signs = [1]                         # effective sign of the current parenthesis level
    for ch in s + "+":
        if ch.isdigit():
            num = num * 10 + int(ch)
        elif ch in "+-":
            total += signs[-1] * sign * num
            num = 0
            sign = 1 if ch == "+" else -1
        elif ch == "(":
            signs.append(signs[-1] * sign)
            sign = 1
        elif ch == ")":
            total += signs[-1] * sign * num
            num = 0
            signs.pop()
            sign = 1
    return total
```

**Greedy increasing stack.** Drop a larger digit when a smaller one arrives, while removals remain.

```python
def remove_k_digits(num, k):
    st = []
    for d in num:
        while k and st and st[-1] > d:
            st.pop()
            k -= 1
        st.append(d)
    st = st[:len(st) - k] if k else st
    return "".join(st).lstrip("0") or "0"
```

**Java.** Use `ArrayDeque` as the stack; `java.util.Stack` is synchronised and legacy.

```java
static int[] dailyTemperatures(int[] t) {
    int[] ans = new int[t.length];
    Deque<Integer> stack = new ArrayDeque<>();
    for (int i = 0; i < t.length; i++) {
        while (!stack.isEmpty() && t[stack.peek()] < t[i]) {
            int j = stack.pop();
            ans[j] = i - j;
        }
        stack.push(i);
    }
    return ans;
}
```

## Complexity

Every monotonic-stack template above is O(n) time, by the push-once/pop-once argument, and O(n) space. Bracket and expression parsing is O(n). Min stack is O(1) per operation.

## Common bugs

1. Returning `True` for `"("` because the final emptiness check is missing; popping an empty stack for `")"`.
2. Storing values instead of indices, so distances and widths cannot be computed.
3. Both boundaries strict (or both non-strict) in contribution problems: duplicates are counted twice or not at all (exercise 1).
4. Forgetting the sentinel, so bars still on the stack at the end are never measured.
5. In Remove K Digits, forgetting the leftover `k` (input already increasing) or the leading zeros.
6. Using recursion for deeply nested input (10⁴ levels) and hitting Python's recursion limit; the stack version has no limit.

## Problems (easy → hard)

Lists: **B75** Blind 75 · **N150** NeetCode 150 · **N250** NeetCode 250. ★ = in the [must-do 100](../problem_list.md).

| # | Problem | Level | What it teaches | Lists |
|---|---|---|---|---|
| 1 | ★ [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | Easy | stack for nesting; both failure modes | B75 · N150 · N250 |
| 2 | [Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/) | Easy | the monotonic stack plus a lookup map | |
| 3 | ★ [Min Stack](https://leetcode.com/problems/min-stack/) | Medium | carry an aggregate with each element | N150 · N250 |
| 4 | ★ [Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) | Medium | operand stack; truncating division toward zero | N150 · N250 |
| 5 | [Simplify Path](https://leetcode.com/problems/simplify-path/) | Medium | stack of path components; `..` and `.` | N250 |
| 6 | [Decode String](https://leetcode.com/problems/decode-string/) | Medium | stack of (prefix, repeat count) frames | N250 |
| 7 | [Asteroid Collision](https://leetcode.com/problems/asteroid-collision/) | Medium | stack of survivors; only right-moving vs left-moving collide | N250 |
| 8 | ★ [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) | Medium | next greater element, distances | N150 · N250 |
| 9 | [Online Stock Span](https://leetcode.com/problems/online-stock-span/) | Medium | monotonic stack in a streaming class | N250 |
| 10 | [Car Fleet](https://leetcode.com/problems/car-fleet/) | Medium | sort by position, stack of arrival times | N150 · N250 |
| 11 | [Remove K Digits](https://leetcode.com/problems/remove-k-digits/) | Medium | greedy increasing stack | |
| 12 | [Sum of Subarray Minimums](https://leetcode.com/problems/sum-of-subarray-minimums/) | Medium | contribution technique, tie-breaking | |
| 13 | ★ [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) | Hard | both boundaries from one pass | N150 · N250 |
| 14 | [Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle/) | Hard | histogram per row of a binary matrix | |
| 15 | [Basic Calculator](https://leetcode.com/problems/basic-calculator/) | Hard | sign stack; unary minus | |

## AI-era exercises

**Exercise 1 · Find the double count.** An assistant's Sum of Subarray Minimums extends over equal values on both sides:

```python
def sum_subarray_mins_ai(a):
    n = len(a)
    total = 0
    for i in range(n):
        l = i
        while l > 0 and a[l - 1] >= a[i]:
            l -= 1
        r = i
        while r < n - 1 and a[r + 1] >= a[i]:
            r += 1
        total += a[i] * (i - l + 1) * (r - i + 1)
    return total
```

Give the smallest input where it is wrong, explain which subarrays are double-counted, and name a second problem with the same flaw. Then state its complexity.

<details><summary>Answer</summary>

`[1, 1]`: the correct sum is 1 + 1 + 1 = 3; the code returns 2 + 2 = 4, because the subarray `[1, 1]` is credited to both 1s (each one extends over the other). Using `>` on both sides fails the other way: `[1, 1]` is credited to neither and the result is 2. Fix: extend over `>=` on one side and `>` on the other, as in the template. The same tie-breaking issue appears in Sum of Subarray Ranges and in "count subarrays where a[i] is the maximum". Separately, the scans make this O(n²) on an increasing input; the stack version is O(n).
</details>

**Exercise 2 · Prove the bound.** An assistant says the template `daily_temperatures` is "O(n²) in the worst case because of the nested while loop". Write the argument that it is O(n), then construct the input on which the inner `while` pops the most elements in a single iteration.

<details><summary>Answer</summary>

Each index is pushed exactly once and popped at most once, so the total number of pops over the whole run is at most n, and the total work is O(n) even though one iteration may pop many items. A strictly decreasing sequence followed by one large value (for example `[5, 4, 3, 2, 1, 6]`) makes the last iteration pop all five earlier indices, which is still only n pops in total. This is amortised analysis ([CS201](../../../02_year_2_core_computer_science/semester_3/CS201_algorithms_and_complexity/README.md) lesson 3.3); interviewers expect this sentence whenever you use a monotonic stack.
</details>

## You own this pattern when

- You can derive previous-smaller and next-smaller boundaries for an array by hand and explain the tie-breaking rule.
- You solve Largest Rectangle in Histogram from a blank file in under 20 minutes and justify the sentinel.
- You recognise "nearest bigger/smaller" in a disguised statement (stock span, car fleet, visible people).
