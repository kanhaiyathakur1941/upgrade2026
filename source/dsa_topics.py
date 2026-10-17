from helper import lesson, mod

DSA = [
    mod("dsa-core", "Complexity and core structures", [
        lesson(
            "dsa-big-o",
            "Time and space: Big O, Theta, Omega",
            "beginner", "essential", 40,
            "Interviews want the growth class, not a proof course. Say the worst case, then the typical case if they differ.",
            what="Big O is an upper bound. Theta is tight. Omega is a lower bound. Practical talk is O(1), O(log n), O(n), O(n log n), O(n²), O(2^n).",
            why="A nested loop on a loan list is why Religare needed indexes. Same language applies to Python.",
            code='''def has_role(roles: list[str], needle: str) -> bool:
    return needle in roles  # O(n)

def has_role_set(roles: set[str], needle: str) -> bool:
    return needle in roles  # average O(1)''',
            interview=["Is binary search always faster than linear? Only when n is large and the array is sorted."],
            refs=["[TimeComplexity](https://wiki.python.org/moin/TimeComplexity)"],
            nxt="#dsa-array",
        ),
        lesson(
            "dsa-array",
            "Arrays, lists, strings as sequences",
            "beginner", "essential", 40,
            "Python list is a dynamic array. Index is O(1). Insert at 0 is O(n). Strings are immutable sequences.",
            why="Most coding screens start here. Your Laravel collections already taught map/filter; the interview wants indexes and two pointers.",
            code='''def reverse_words(s: str) -> str:
    return " ".join(reversed(s.split()))

def first_unique(s: str) -> str | None:
    from collections import Counter
    counts = Counter(s)
    for ch in s:
        if counts[ch] == 1:
            return ch
    return None

print(reverse_words("fit paradox portal"))
print(first_unique("aabbc"))''',
            out="portal paradox fit then c.",
            exercise="Two sum. Valid parentheses. Reverse words. Write pytest for each.",
            nxt="#dsa-hash",
        ),
        lesson(
            "dsa-hash",
            "Hash maps and sets",
            "beginner", "essential", 40,
            "dict and set are the default interview upgrade from nested loops.",
            code='''def two_sum(nums: list[int], target: int) -> tuple[int, int] | None:
    seen: dict[int, int] = {}
    for i, n in enumerate(nums):
        if target - n in seen:
            return seen[target - n], i
        seen[n] = i
    return None

print(two_sum([2, 7, 11, 15], 9))''',
            out="(0, 1)",
            nxt="#dsa-stack",
        ),
        lesson(
            "dsa-stack",
            "Stacks and queues",
            "beginner", "essential", 35,
            "Stack is LIFO: undo, DFS, parentheses. Queue is FIFO: BFS, worker intake. collections.deque is the Python queue. list.pop(0) is the wrong queue.",
            code='''from collections import deque

def valid_parens(s: str) -> bool:
    pairs = {")": "(", "]": "[", "}": "{"}
    stack: list[str] = []
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif not stack or stack.pop() != pairs[ch]:
            return False
    return not stack

q = deque(["ingest", "embed"])
q.append("index")
print(valid_parens("{[()]}"), q.popleft())''',
            out="True then ingest.",
            nxt="#dsa-linked",
        ),
        lesson(
            "dsa-linked",
            "Linked lists",
            "intermediate", "essential", 40,
            "You will rarely ship a linked list in FastAPI. You will reverse one on a whiteboard. Know dummy heads and two pointers.",
            code='''class Node:
    def __init__(self, val: int, next: "Node | None" = None) -> None:
        self.val = val
        self.next = next

def reverse(head: Node | None) -> Node | None:
    prev = None
    cur = head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return prev''',
            task="Write pytest that 1→2→3 becomes 3→2→1. Then merge two sorted lists.",
            nxt="#dsa-tree",
        ),
        lesson(
            "dsa-tree",
            "Trees, BST, heaps, tries",
            "intermediate", "essential", 55,
            "A heap is Python's heapq. A trie is a nested dict. BST inorder is sorted. Document tags and autocomplete are trie-shaped.",
            code='''import heapq

def top_k(nums: list[int], k: int) -> list[int]:
    return heapq.nlargest(k, nums)

trie: dict = {}
for word in ("loan", "log"):
    node = trie
    for ch in word:
        node = node.setdefault(ch, {})
    node["$"] = True
print(top_k([3, 1, 4, 1, 5, 9], 2))
print("loan"[:2] in ("lo",))''',
            out="[9, 5] then True.",
            nxt="#dsa-graph",
        ),
        lesson(
            "dsa-graph",
            "Graphs, BFS, DFS",
            "intermediate", "essential", 50,
            "Org charts, document links, and service dependencies are graphs. BFS for shortest unweighted path. DFS for cycle and finish order.",
            code='''from collections import deque

def bfs(start: str, edges: dict[str, list[str]]) -> list[str]:
    seen = {start}
    q = deque([start])
    order = []
    while q:
        node = q.popleft()
        order.append(node)
        for nxt in edges.get(node, []):
            if nxt not in seen:
                seen.add(nxt)
                q.append(nxt)
    return order''',
            nxt="#dsa-search",
        ),
    ]),
    mod("dsa-patterns", "Interview patterns and a problem ladder", [
        lesson(
            "dsa-search",
            "Linear search, binary search, sorting",
            "beginner", "essential", 40,
            "Binary search needs a sorted view or a monotonic predicate. bisect is the library. sort in Python is Timsort, O(n log n).",
            code='''import bisect

def first_gte(nums: list[int], target: int) -> int:
    return bisect.bisect_left(nums, target)

print(first_gte([1, 3, 3, 7], 3))''',
            out="1, the first index where value is >= 3.",
            when="Linear search for n under a few dozen or unsorted input. Binary search when the predicate is monotonic.",
            nxt="#dsa-two-pointers",
        ),
        lesson(
            "dsa-two-pointers",
            "Two pointers, sliding window, prefix sums",
            "intermediate", "essential", 50,
            "Use two pointers on sorted arrays or on a string window. Prefix sums turn range sums into O(1).",
            code='''def max_window(nums: list[int], k: int) -> int:
    s = sum(nums[:k])
    best = s
    for i in range(k, len(nums)):
        s += nums[i] - nums[i - k]
        best = max(best, s)
    return best''',
            nxt="#dsa-backtrack",
        ),
        lesson(
            "dsa-backtrack",
            "Recursion, backtracking, greedy",
            "intermediate", "essential", 45,
            "Recursion needs a base case. Backtracking undoes a choice. Greedy works only with a proof or a known pattern (interval scheduling).",
            nxt="#dsa-dp",
        ),
        lesson(
            "dsa-dp",
            "Dynamic programming, including your two files",
            "advanced", "essential", 70,
            "script.py is edit distance (done). knapsackzeroonebyset.py is a stub. Finish knapsack with tests.",
            why="DP stores answers to overlapping subproblems. Edit distance is the grid you already wrote. 0/1 knapsack is the next grid or the set-of-states version in your comments.",
            code='''def knapsack(weights: list[int], values: list[int], capacity: int) -> int:
    possible = {(0, 0)}
    for w, v in zip(weights, values):
        extra = {(cw + w, cv + v) for cw, cv in possible if cw + w <= capacity}
        possible |= extra
    return max(cv for _, cv in possible)

print(knapsack([1, 3, 4, 5], [10, 40, 50, 70], 7))''',
            out="90, from items 3 and 4 (weights 3+4).",
            task="Replace the stub in a copy under the new repo. Keep the Desktop file as history. Parametrize tests for capacity 0 and one item too heavy.",
            interview=["Top-down memo versus bottom-up table", "When greedy fails on knapsack"],
            nxt="#dsa-ladder",
        ),
        lesson(
            "dsa-ladder",
            "Progressive problem list",
            "intermediate", "essential", 20,
            "Four problems a week in months 1–2, two a week after that. Speak complexity before code.",
            exercise="Beginner: two sum, valid parentheses, merge two sorted lists, first unique character. Intermediate: longest substring without repeat (Accenture Day 10), product except self, BST kth smallest, course schedule DFS. Advanced: edit distance, 0/1 knapsack, median of two sorted arrays, word break.",
            task="A folder problems/ with one test file per pattern. Commit one pattern a week.",
            nxt="#http-basics",
        ),
    ]),
]
