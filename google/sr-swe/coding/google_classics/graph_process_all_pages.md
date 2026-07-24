# Coding Interview: Process All Pages (Graph Traversal / Web Crawler)

**Topic**: Graph traversal, BFS/DFS
**Difficulty**: Medium
**Pattern**: Web crawler — same as Number of Islands but on an explicit graph

---

## Problem Statement

Given two APIs:

```python
def getAllLinks(page: Page) -> List[Page]: ...  # returns child pages linked from this page
def processPage(page: Page) -> None: ...        # processes a single page
```

Write a method `processAllPages(root: Page)` that processes every reachable page exactly once.

---

## Key Insight

This is a **graph traversal**, not a tree traversal. Pages can link back to each other (cycles).
Without a `visited` set, page A → page B → page A creates an infinite loop.

---

## Solution 1: BFS (preferred for web crawlers)

```python
from collections import deque

def processAllPages_bfs(root: Page) -> None:
    if root is None:
        return

    visited = set()
    queue = deque([root])
    visited.add(root)          # mark BEFORE enqueue — prevents duplicate queue entries

    while queue:
        page = queue.popleft()
        processPage(page)

        for link in getAllLinks(page):
            if link not in visited:
                visited.add(link)
                queue.append(link)
```

**Why BFS**: processes pages level-by-level (pages closest to root first). Natural fit for
web crawlers where "nearby" pages are higher priority.

---

## Solution 2: DFS Iterative (explicit stack)

```python
def processAllPages_dfs(root: Page) -> None:
    if root is None:
        return

    visited = set()
    stack = [root]

    while stack:
        page = stack.pop()
        if page in visited:    # check AFTER pop — same page can be pushed multiple times
            continue
        visited.add(page)
        processPage(page)

        for link in getAllLinks(page):
            if link not in visited:
                stack.append(link)
```

**Mark timing difference**:
- BFS: mark visited **before enqueue** — ensures each page enters the queue at most once
- DFS: check visited **after pop** — a page may be in the stack multiple times, harmlessly skipped on pop

---

## Complexity

| | BFS | DFS |
|---|---|---|
| Time | O(V + E) | O(V + E) |
| Space | O(max width of graph) | O(max depth of graph) |

V = pages, E = total links across all pages

---

## Interview Talking Points

### Say upfront
*"This is a graph traversal — pages can link back to each other so I need a visited set to
avoid infinite loops. BFS for breadth-first (closer pages first), DFS for depth-first."*

### BFS vs DFS tradeoff
- BFS: better when nearby pages are more relevant; memory = O(width)
- DFS: better for very deep graphs with low branching; memory = O(depth)
- For web crawlers, BFS is the standard answer

### Follow-up 1: getAllLinks throws an exception
```python
try:
    links = getAllLinks(page)
except Exception as e:
    log(f"Failed to get links for {page}: {e}")
    links = []
```
*"Wrap in try/except, log the error, treat as a dead end — don't crash the whole crawl."*

### Follow-up 2: Parallel processing
- Use a thread pool (`concurrent.futures.ThreadPoolExecutor`)
- Make `visited` thread-safe: use a `threading.Lock` or switch to a concurrent set
- Or use a distributed lock in Redis if crawling across multiple machines

### Follow-up 3: Scale to billions of pages
- Partition pages by URL hash — each worker owns a shard of the URL space
- `visited` becomes a distributed set (Redis or Bloom filter for memory efficiency)
- A Bloom filter trades a small false-positive rate for massive memory savings
  (say: *"Bloom filter for visited — O(1) membership check, ~10 bits per URL vs. storing full URL"*)

---

## Variations

- **Clone Graph** (LeetCode 133) — same BFS/DFS with a `visited` map that stores the clone
- **Course Schedule** (LeetCode 207) — same graph traversal but looking for cycles
- **Word Ladder** (LeetCode 127) — BFS on an implicit graph (word neighbors)
