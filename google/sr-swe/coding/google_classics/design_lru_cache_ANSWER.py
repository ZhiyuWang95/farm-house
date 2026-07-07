"""
Problem: LRU Cache
Link: https://leetcode.com/problems/lru-cache/
Topic: Design / OOD
Difficulty: Medium

=========================
Explanation
=========================
The naive approach — an array or plain dict — can do O(1) get/put but not O(1)
eviction of the least-recently-used entry, because finding the LRU item takes
O(n) scan. We need a structure where we can (1) look up any key in O(1), and
(2) move a node to "most recent" and evict from "least recent" end in O(1).

The solution combines two structures: a hashmap (key → node) for O(1) lookup,
and a doubly linked list to maintain recency order. The list's head is the most
recent, tail is the least recent. On get or put, we move the accessed node to
the head. On eviction, we remove the tail node. Both operations are O(1) with a
DLL because we have direct pointers.

Sentinel head and tail dummy nodes eliminate edge-case checks for empty list or
single-element removals — every real node always has neighbors.

Python's OrderedDict implements exactly this internally, but Google interviewers
expect you to implement the DLL manually to show you understand the underlying
mechanism. Know both; code the manual version.
=========================
Complexity
=========================
Time:  O(1) for both get and put — hashmap lookup is O(1), DLL insert/remove
       with known pointers is O(1).
Space: O(capacity) — at most capacity nodes in the list and map.
"""

from collections import OrderedDict


class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> Node
        self.head = Node()  # dummy most-recent sentinel
        self.tail = Node()  # dummy least-recent sentinel
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def _insert_front(self, node: Node) -> None:
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._insert_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node
        self._insert_front(node)
        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]


class LRUCacheOrderedDict:
    """Shortcut using OrderedDict — mention this but code the DLL version above."""
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))    # 1
    cache.put(3, 3)        # evicts key 2
    print(cache.get(2))    # -1
    cache.put(4, 4)        # evicts key 1
    print(cache.get(1))    # -1
    print(cache.get(3))    # 3
    print(cache.get(4))    # 4


"""
=========================
Google-asked variations (2-3)
=========================

1. LFU Cache (LeetCode 460, Hard)
   "Evict the least FREQUENTLY used entry instead of least recently used; break
   ties by recency." Same hashmap+DLL skeleton but now each frequency bucket has
   its own DLL, and you track a global min_freq to find the eviction bucket in
   O(1). The jump from LRU to LFU is a very common Google follow-up: "What if
   you wanted to keep hot data even if it was accessed a while ago?"

2. All O(1) Data Structure (LeetCode 432, Hard)
   "Design a structure supporting insert(key), delete(key), getMaxKey(),
   getMinKey() all in O(1)." Generalizes the frequency-bucket idea from LFU:
   maintain a doubly linked list of frequency buckets (each bucket is a set of
   keys), so min and max are the list's tail and head. Tests whether you can
   build the full O(1) bookkeeping machinery without a specific eviction policy.

3. Design In-Memory File System (LeetCode 588, Hard)
   "Implement ls, mkdir, addContentToFile, readContentFromFile." Reuses the
   LRU-style pointer/hashmap combination but for a tree of directory nodes
   instead of a linear recency list. A good signal that the interviewer wants
   to see whether you can apply the same O(1)-via-hashmap-plus-structure
   pattern to a hierarchical domain.
"""
