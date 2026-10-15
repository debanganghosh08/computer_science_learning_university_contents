# DSA for hiring · Pattern 18 · Tries (prefix trees)

| Theory first | Time | Problems | Must-do |
|---|---|---|---|
| [FND112](../../../01_year_1_foundations/semester_2/FND112_data_structures_and_algorithms_i/README.md) lesson 8.4; [CS201](../../../02_year_2_core_computer_science/semester_3/CS201_algorithms_and_complexity/README.md) lesson 9.3 | ~6 hours | 11 | 3 |

A trie stores strings character by character along root-to-node paths, so every prefix is a node. Lookups cost O(length of the word), independent of how many words are stored, and "all words with this prefix" is a subtree. Use it for autocomplete, dictionary-guided search (find many words at once in a grid), and, over bits, for maximum-XOR queries.

## Recognise it

| When you see… | Think… |
|---|---|
| "starts with", "autocomplete", "suggestions for each typed prefix" | trie with optional per-node data (counts, top-3 words) |
| "search with wildcards" (`.` matches any letter) | trie + DFS at wildcard positions |
| find **many** dictionary words in a grid or text | build one trie of the words; walk the grid once guided by it |
| "replace words by their shortest root" | walk the trie and stop at the first end-of-word |
| "maximum XOR of two numbers" | binary trie over bits, greedy from the highest bit |
| a single word or a handful of exact lookups | a hash set is simpler; say why you are not using a trie |

## Core templates

**A dictionary-based trie.** `end` marks that a whole word ends here; without it, every prefix looks like a word.

```python
class TrieNode:
    __slots__ = ("children", "end")

    def __init__(self):
        self.children = {}
        self.end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.end = True

    def _walk(self, s):
        node = self.root
        for ch in s:
            node = node.children.get(ch)
            if node is None:
                return None
        return node

    def search(self, word):
        node = self._walk(word)
        return node is not None and node.end

    def startsWith(self, prefix):
        return self._walk(prefix) is not None
```

**Wildcard search.**

```python
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.end = True

    def search(self, word):
        def dfs(node, i):
            if i == len(word):
                return node.end
            ch = word[i]
            if ch == ".":
                return any(dfs(child, i + 1) for child in node.children.values())
            child = node.children.get(ch)
            return child is not None and dfs(child, i + 1)
        return dfs(self.root, 0)
```

**Word Search II: one trie, one grid walk.** Store the word at its end node; remove it once found (no duplicates) and prune empty branches.

```python
def find_words(board, words):
    root = {}
    for w in words:
        node = root
        for ch in w:
            node = node.setdefault(ch, {})
        node["$"] = w                         # end marker holds the word
    m, n = len(board), len(board[0])
    found = []

    def dfs(r, c, parent):
        ch = board[r][c]
        node = parent[ch]
        if "$" in node:
            found.append(node.pop("$"))       # pop: report each word once
        board[r][c] = "#"
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n and board[nr][nc] in node:
                dfs(nr, nc, node)
        board[r][c] = ch
        if not node:
            parent.pop(ch)                    # prune a finished branch

    for r in range(m):
        for c in range(n):
            if board[r][c] in root:
                dfs(r, c, root)
    return found
```

**Per-node data (Search Suggestions System).** Keep up to three lexicographically smallest words at each node by inserting in sorted order.

```python
def suggested_products(products, search_word):
    root = {}
    for p in sorted(products):
        node = root
        for ch in p:
            node = node.setdefault(ch, {"#": []})
            if len(node["#"]) < 3:
                node["#"].append(p)
    out, node = [], root
    for ch in search_word:
        node = node.get(ch) if node else None    # None once the prefix leaves the trie
        out.append(node["#"] if node else [])
    return out
```

**Binary trie for maximum XOR.** For each number, walk the trie preferring the opposite bit at every level, from the highest bit down.

```python
def find_maximum_xor(nums, bits=31):
    root, best = {}, 0
    for x in nums:
        node = root
        for b in range(bits, -1, -1):
            node = node.setdefault((x >> b) & 1, {})
        node, cur = root, 0
        for b in range(bits, -1, -1):
            want = 1 - ((x >> b) & 1)
            if want in node:
                cur |= 1 << b
                node = node[want]
            else:
                node = node[1 - want]
        best = max(best, cur)
    return best
```

**Java.** A fixed `Node[26]` array is fast and simple for lowercase letters.

```java
static class Trie {
    private static class Node {
        Node[] next = new Node[26];
        boolean end;
    }

    private final Node root = new Node();

    void insert(String word) {
        Node node = root;
        for (char ch : word.toCharArray()) {
            int i = ch - 'a';
            if (node.next[i] == null) node.next[i] = new Node();
            node = node.next[i];
        }
        node.end = true;
    }

    private Node walk(String s) {
        Node node = root;
        for (char ch : s.toCharArray()) {
            node = node.next[ch - 'a'];
            if (node == null) return null;
        }
        return node;
    }

    boolean search(String word) { Node n = walk(word); return n != null && n.end; }

    boolean startsWith(String prefix) { return walk(prefix) != null; }
}
```

## Complexity

Insert, search and prefix checks are O(L) for a word of length L. Space is O(total characters) nodes; array children cost 26 references per node, dictionary children only what is used. Word Search II is O(m · n · 4 · 3^(L−1)) in the worst case, much less in practice thanks to pruning. Maximum XOR is O(n · B) for B bits.

## Common bugs

1. `search` returning `True` for a prefix because the end flag is not checked (exercise 1).
2. Word Search II reporting the same word twice when it appears twice in the grid (exercise 2).
3. Forgetting to restore the grid cell after DFS.
4. Building one trie per starting cell, or running one DFS per word, instead of one trie for all words.
5. Unbounded per-node lists in autocomplete; cap them (top 3) or memory explodes.
6. For the binary trie, inconsistent bit width (31 for non-negative 32-bit ints).

## Problems (easy → hard)

Lists: **B75** Blind 75 · **N150** NeetCode 150 · **N250** NeetCode 250. ★ = in the [must-do 100](../problem_list.md).

| # | Problem | Level | What it teaches | Lists |
|---|---|---|---|---|
| 1 | [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/) | Easy | vertical scan vs trie; when a trie is overkill | N250 |
| 2 | ★ [Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/) | Medium | nodes, children, end flag | B75 · N150 · N250 |
| 3 | ★ [Design Add and Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/) | Medium | DFS at wildcards | B75 · N150 · N250 |
| 4 | [Replace Words](https://leetcode.com/problems/replace-words/) | Medium | stop at the first end-of-word | |
| 5 | [Search Suggestions System](https://leetcode.com/problems/search-suggestions-system/) | Medium | per-node top-k lists | |
| 6 | [Map Sum Pairs](https://leetcode.com/problems/map-sum-pairs/) | Medium | per-node aggregates updated by deltas | |
| 7 | [Longest Word in Dictionary](https://leetcode.com/problems/longest-word-in-dictionary/) | Medium | BFS/DFS over end-of-word nodes only | |
| 8 | [Maximum XOR of Two Numbers in an Array](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/) | Medium | binary trie, greedy bit choice | |
| 9 | ★ [Word Search II](https://leetcode.com/problems/word-search-ii/) | Hard | trie-guided backtracking with pruning | B75 · N150 · N250 |
| 10 | [Palindrome Pairs](https://leetcode.com/problems/palindrome-pairs/) | Hard | reversed-word trie or hash map of reversed words | |
| 11 | [Concatenated Words](https://leetcode.com/problems/concatenated-words/) | Hard | word-break DP with a trie or a set | |

## AI-era exercises

**Exercise 1 · Find the bug.**

```python
class TrieAI:
    def __init__(self):
        self.root = {}

    def insert(self, word):
        node = self.root
        for ch in word:
            node = node.setdefault(ch, {})

    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node:
                return False
            node = node[ch]
        return True
```

Which call returns the wrong answer after `insert("apple")`? Fix it with one marker.

<details><summary>Answer</summary>

`search("app")` returns `True`, but "app" was never inserted. Without an end-of-word marker the structure cannot tell a word from a prefix. Store a marker at the last node (`node["$"] = True`) during insert and check it at the end of `search`. The test that catches it: insert a word, then search every proper prefix and expect `False`.
</details>

**Exercise 2 · Duplicates and cost.** An assistant's Word Search II keeps the end marker in place after a match:

```python
def find_words_ai(board, words):
    root = {}
    for w in words:
        node = root
        for ch in w:
            node = node.setdefault(ch, {})
        node["$"] = w
    m, n = len(board), len(board[0])
    found = []

    def dfs(r, c, node):
        ch = board[r][c]
        if ch not in node:
            return
        node = node[ch]
        if "$" in node:
            found.append(node["$"])
        board[r][c] = "#"
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n:
                dfs(nr, nc, node)
        board[r][c] = ch

    for r in range(m):
        for c in range(n):
            dfs(r, c, root)
    return found
```

Find a 1 × 2 board that exposes the bug, then explain what the template's two `pop` calls buy you in running time on a board full of `"a"` with the word list `["aaaaaaaaaa"]`.

<details><summary>Answer</summary>

`board = [["a", "a"]], words = ["a"]` returns `["a", "a"]`: the word is found from both cells. Removing the marker when a word is reported (`node.pop("$")`) fixes the duplicates. The second `pop`, pruning a branch once it has no words left below it, is a performance fix: after the only word is found, its whole path is deleted from the trie, so later DFS calls stop immediately instead of re-exploring every path of length 10 from every cell. Without pruning, the search keeps walking up to 4 · 3⁹ paths per starting cell after the answer is already known.
</details>

## You own this pattern when

- You implement a trie with insert, search and prefix search in under 7 minutes, with the end flag.
- You explain why one trie for all words beats one DFS per word in Word Search II.
- You can say when a hash set of words or prefixes is the simpler correct answer.
