# Coding Problem List — 2 algo + 1 OOD/day, Google high-frequency

Mapped to the weekly themes in `../prep_plan.md`. Each entry: difficulty, LeetCode link, pattern tag.
Check items off as you complete them. Solution write-ups/notes go in `solutions/`.

The **OOD** entry each day is a class/system-design coding problem (distinct from
the LRU/Twitter-style "Design" pattern problems already mixed into the algo list)
— builds clean interface/API design instincts that carry over to the system
design round. All entries below are free (non-premium) LeetCode problems.

Each OOD entry also carries a **real-world angle**: a one-line framing connecting
the abstract data structure to a GKE/K8s or Vertex MaaS concept. Solving the
LeetCode problem is the coding rep; the framing is a reusable analogy/talking
point for the system design and infra-experience rounds.

---

## Week 1 — Foundations (untimed, pattern-focused)

### Day 1 — Arrays & Hashmaps
- [x] [Two Sum](https://leetcode.com/problems/two-sum/) (Easy) — Hashmap
- [x] [Group Anagrams](https://leetcode.com/problems/group-anagrams/) (Medium) — Hashmap
- [x] [Design Parking System](https://leetcode.com/problems/design-parking-system/) (Easy) — OOD
  - *Real-world angle*: fixed-capacity resource pools — GKE node pool slots per machine type, reject `addCar` when a pool is full (like a scheduler rejecting a pod that doesn't fit any node pool).

### Day 2 — Sliding Window / Two Pointers
- [x] [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) (Medium) — Sliding Window
- [x] [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) (Medium) — Two Pointers
- [x] [Design HashSet](https://leetcode.com/problems/design-hashset/) (Easy) — OOD
  - *Real-world angle*: the building block under an informer's local object cache (lookup a K8s object by UID without hitting the API server).

### Day 3 — Arrays
- [x] [3Sum](https://leetcode.com/problems/3sum/) (Medium) — Two Pointers
- [x] [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) (Medium) — Prefix/Suffix
- [x] [Design HashMap](https://leetcode.com/problems/design-hashmap/) (Medium) — OOD
  - *Real-world angle*: the building block under etcd's key-value store (bucket/chain or open-addressing — same tradeoffs as etcd's backend storage).

### Day 4 — Linked Lists
- [ ] [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) (Easy) — Linked List
- [ ] [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) (Medium) — Linked List
- [ ] [Min Stack](https://leetcode.com/problems/min-stack/) (Medium) — OOD
  - *Real-world angle*: tracking the min/max of a metric over a sliding window of recent samples — the core of HPA's stabilization-window logic (don't scale down on a single low blip).

### Day 5 — Stacks & Binary Search
- [ ] [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) (Easy) — Stack
- [ ] [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) (Medium) — Binary Search
- [ ] [Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/) (Easy) — OOD
  - *Real-world angle*: getting FIFO ordering guarantees on top of LIFO primitives — the same kind of ordering contract a controller workqueue needs to provide.

### Day 6 — Trees
- [ ] [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) (Medium) — BFS/Tree
- [ ] [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) (Medium) — DFS/Tree
- [ ] [Design Circular Queue](https://leetcode.com/problems/design-circular-queue/) (Medium) — OOD
  - *Real-world angle*: a bounded ring buffer — how a controller's event/workqueue or an informer's resync buffer caps memory under backpressure.

### Day 7 — Grid BFS/DFS + Intro DP
- [ ] [Number of Islands](https://leetcode.com/problems/number-of-islands/) (Medium) — BFS/DFS Grid
- [ ] [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) (Easy) — 1D DP
- [ ] [Design Linked List](https://leetcode.com/problems/design-linked-list/) (Medium) — OOD
  - *Real-world angle*: the underlying doubly-linked-list structure that an LRU/LFU eviction cache (Day 14, model/image cache) is built on.

---

## Week 2 — Deep Dives (timed, 25-35 min/problem)

### Day 8 — Graphs
- [ ] [Clone Graph](https://leetcode.com/problems/clone-graph/) (Medium) — Graph DFS
- [ ] [Course Schedule](https://leetcode.com/problems/course-schedule/) (Medium) — Topological Sort
- [ ] [Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/) (Medium) — OOD
  - *Real-world angle*: O(1) random pick of a healthy backend from a dynamic pool — load-balancer endpoint selection as pods/replicas come and go.

### Day 9 — Union-Find / Multi-source Search
- [ ] [Redundant Connection](https://leetcode.com/problems/redundant-connection/) (Medium) — Union-Find
- [ ] [Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/) (Medium) — Multi-source BFS/DFS
- [ ] [Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/) (Medium) — OOD
  - *Real-world angle*: directly mirrors etcd's MVCC model — "get the value of this key as of revision/timestamp T".

### Day 10 — 2D DP
- [ ] [Unique Paths](https://leetcode.com/problems/unique-paths/) (Medium) — 2D DP
- [ ] [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) (Medium) — 2D DP
- [ ] [Design Twitter](https://leetcode.com/problems/design-twitter/) (Medium) — OOD
  - *Real-world angle*: fan-out event feed — K8s Events API for a namespace, or a MaaS partner-facing notification feed (model version released, quota changed).

### Day 11 — Knapsack-style DP
- [ ] [Coin Change](https://leetcode.com/problems/coin-change/) (Medium) — DP
- [ ] [Word Break](https://leetcode.com/problems/word-break/) (Medium) — DP
- [ ] [Design Underground System](https://leetcode.com/problems/design-underground-system/) (Medium) — OOD
  - *Real-world angle*: average latency between two checkpoints — distributed tracing, e.g. p50 time from ingress gateway to model-server response.

### Day 12 — Heaps
- [ ] [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) (Medium) — Heap
- [ ] [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) (Medium) — Heap/Bucket Sort
- [ ] [Design Browser History](https://leetcode.com/problems/design-browser-history/) (Medium) — OOD
  - *Real-world angle*: Deployment revision history with back/forward navigation — `kubectl rollout history` / `kubectl rollout undo`.

### Day 13 — Greedy / Intervals
- [ ] [Merge Intervals](https://leetcode.com/problems/merge-intervals/) (Medium) — Sorting/Greedy
- [ ] [Task Scheduler](https://leetcode.com/problems/task-scheduler/) (Medium) — Greedy/Heap
- [ ] [Design A Leaderboard](https://leetcode.com/problems/design-a-leaderboard/) (Medium) — OOD
  - *Real-world angle*: scheduler node-scoring — rank candidate nodes (or model replicas) by a fitness/load score and pick the top one.

### Day 14 — Design (end-of-week mock candidates)
- [ ] [LRU Cache](https://leetcode.com/problems/lru-cache/) (Medium) — Design
  - *Real-world angle*: container image cache eviction on a node, or KV-cache block reuse in LLM serving.
- [ ] [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) (Hard) — Heap/Design
- [ ] [LFU Cache](https://leetcode.com/problems/lfu-cache/) (Hard) — OOD (natural follow-up to LRU)
  - *Real-world angle*: frequency-aware eviction for the same caches above — vLLM's PagedAttention KV-cache block eviction leans more LFU-like than pure LRU.

---

## Week 3 — Mocks & Integration (timed, mixed)

### Day 15 — Backtracking
- [ ] [Word Search](https://leetcode.com/problems/word-search/) (Medium) — Backtracking
- [ ] [Subsets](https://leetcode.com/problems/subsets/) (Medium) — Backtracking
- [ ] [Encode and Decode TinyURL](https://leetcode.com/problems/encode-and-decode-tinyurl/) (Medium) — OOD
  - *Real-world angle*: a service registry — map a long internal model-artifact URI (GCS path) to a short stable handle/ID partners reference.

### Day 16 — Backtracking
- [ ] [Permutations](https://leetcode.com/problems/permutations/) (Medium) — Backtracking
- [ ] [Combination Sum](https://leetcode.com/problems/combination-sum/) (Medium) — Backtracking
- [ ] [Random Pick with Weight](https://leetcode.com/problems/random-pick-with-weight/) (Medium) — OOD
  - *Real-world angle*: weighted load balancing — route more traffic to higher-capacity model replicas proportional to their weight.

### Day 17 — Mock #1 candidates (Hard Trees)
- [ ] [Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) (Hard) — Tree/Design
- [ ] [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) (Hard) — Tree/DFS
- [ ] [Flatten Nested List Iterator](https://leetcode.com/problems/flatten-nested-list-iterator/) (Medium) — OOD
  - *Real-world angle*: lazily traversing a nested resource tree — e.g. walking a nested owner-reference graph or a multi-model serving spec without materializing it all upfront.

### Day 18 — Hard Sliding Window
- [ ] [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) (Hard) — Deque
- [ ] [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) (Hard) — Sliding Window
- [ ] [Number of Recent Calls](https://leetcode.com/problems/number-of-recent-calls/) (Easy) — OOD
  - *Real-world angle*: sliding-window rate limiter — exactly the shape of a MaaS per-partner API quota ("N requests per rolling window").

### Day 19 — Arrays/Matrix
- [ ] [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) (Hard) — Two Pointers
- [ ] [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/) (Medium) — Matrix
- [ ] [Design Add and Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/) (Medium) — OOD
  - *Real-world angle*: a Trie is how Ingress/Gateway path routing and wildcard model-name routing rules are matched efficiently.

### Day 20 — Mock #2 candidates (Trie/Intervals)
- [ ] [Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/) (Medium) — Trie
- [ ] [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) (Medium) — Greedy/Intervals
- [ ] [Design Circular Deque](https://leetcode.com/problems/design-circular-deque/) (Medium) — OOD
  - *Real-world angle*: a reconciliation queue that's normally FIFO but allows pushing urgent work to the front — priority requeue in a controller's workqueue.

### Day 21 — Mixed Review
- [ ] [Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/) (Medium) — Linked List/Hashmap
- [ ] [House Robber](https://leetcode.com/problems/house-robber/) (Medium) — DP
- [ ] [All O`one Data Structure](https://leetcode.com/problems/all-oone-data-structure/) (Hard) — OOD
  - *Real-world angle*: hot/cold tiering — track the most- and least-used model endpoints/cache entries in O(1) to decide what to promote or evict.

---

## Week 4 — Polish (final review pool, pick as needed for mocks/gaps)
- [ ] [Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) (Medium) — Tree
- [ ] [Rotate Image](https://leetcode.com/problems/rotate-image/) (Medium) — Matrix
- [ ] [Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/) (Medium) — Matrix
- [ ] [Network Delay Time](https://leetcode.com/problems/network-delay-time/) (Medium) — Graph/Dijkstra
- [ ] [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) (Medium) — Linked List

### OOD polish pool
- [ ] [Maximum Frequency Stack](https://leetcode.com/problems/maximum-frequency-stack/) (Hard) — OOD
  - *Real-world angle*: frequency-based eviction prioritization — same family as LFU Cache, useful for cache/queue tie-breaking discussions.
- [ ] [Binary Search Tree Iterator](https://leetcode.com/problems/binary-search-tree-iterator/) (Medium) — OOD
  - *Real-world angle*: lazy, paginated iteration over an ordered resource set (e.g., `kubectl get` with continue-tokens over a sorted node/namespace list).
