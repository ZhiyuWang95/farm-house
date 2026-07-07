"""
Problem: Clone Graph
Link: https://leetcode.com/problems/clone-graph/
Topic: Graph (DFS/BFS + hash map)
Difficulty: Medium

=========================
Explanation
=========================
The core challenge isn't traversal -- it's that the graph can contain
CYCLES (it's explicitly undirected, so every edge is mutual, and the
example is literally a 4-cycle). A naive recursive clone ("for each
neighbor, recursively clone it") would infinite-loop on a cycle unless you
remember which original nodes you've already cloned.

Fix: maintain a hash map from {original node -> cloned node}. DFS (or
BFS) from the starting node:
  - If the current original node is already in the map, return its
    existing clone immediately (this is what breaks the infinite loop on
    a cycle).
  - Otherwise, create a new clone node, IMMEDIATELY store it in the map
    (before recursing into neighbors -- this order matters), then for each
    neighbor of the original, recursively clone it and append to the new
    node's neighbor list.

The "store in the map before recursing" detail is the part people get
wrong: if you wait until after processing neighbors to register the
clone, a neighbor that cycles back to this node will recurse infinitely
before ever finding the map entry.

=========================
Complexity
=========================
Time:  O(V + E) -- every node and edge visited exactly once.
Space: O(V) -- the hash map holds one entry per original node, plus O(V)
       recursion depth in the worst case.
"""

from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if node is None:
            return None

        cloned = {}

        def dfs(original: "Node") -> "Node":
            if original in cloned:
                return cloned[original]

            copy = Node(original.val)
            cloned[original] = copy  # register BEFORE recursing -- breaks cycles

            for neighbor in original.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node)


class Solution2:
    """Iterative DFS — same dict approach, explicit stack instead of recursion.

    Common mistake: using a set instead of a dict. A set tells you "visited
    or not" but can't give back the clone you already created — so edges to
    already-visited neighbors get silently dropped. The dict fixes this:
    cloned[cur].neighbors.append(cloned[neighbor]) always works whether
    neighbor was just created or already existed.
    """
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if node is None:
            return None

        original_to_clone = {node: Node(node.val)}
        stack = [node]

        while stack:
            original = stack.pop()
            clone = original_to_clone[original]

            for neighbor in original.neighbors:
                # create the neighbor's clone if we haven't seen it yet
                if neighbor not in original_to_clone:
                    original_to_clone[neighbor] = Node(neighbor.val)
                    stack.append(neighbor)

                # always wire the edge, whether neighbor is new or already existed
                clone.neighbors.append(original_to_clone[neighbor])

        return original_to_clone[node]


if __name__ == "__main__":
    # Build a 4-cycle: 1-2-3-4-1
    n1, n2, n3, n4 = Node(1), Node(2), Node(3), Node(4)
    n1.neighbors = [n2, n4]
    n2.neighbors = [n1, n3]
    n3.neighbors = [n2, n4]
    n4.neighbors = [n1, n3]

    sol = Solution()
    cloned_start = sol.cloneGraph(n1)
    print(cloned_start.val, [n.val for n in cloned_start.neighbors])  # 1 [2, 4]
    print(cloned_start is n1)  # False -- genuinely a new object


"""
=========================
Google-asked variations (2-3)
=========================

1. Copy List with Random Pointer (LeetCode 138, Medium)
   Same "deep-copy a structure with cycle-prone references" shape, just
   on a linked list where each node has an extra `random` pointer that can
   point anywhere (including forward, backward, or to itself). Same
   {original -> clone} hash map technique applies directly. Frequently
   paired with Clone Graph as "two versions of the same underlying idea."

2. Clone N-ary Tree (LeetCode 1490, Medium, premium but commonly asked
   verbally)
   A simpler special case: if the input is guaranteed to be a tree (no
   cycles, since trees are acyclic by definition), you don't even need the
   hash map for cycle-breaking -- plain recursive cloning works directly.
   A good check for whether you understand *why* Clone Graph needs the
   map at all (it's specifically the cycle, not the cloning itself, that
   demands it).

3. Clone Graph with weighted edges / Network Delay Time-style graph
   (no single canonical LeetCode #, but a common follow-up: "what if
   neighbors also carry edge weights?")
   Forces you to extend the Node structure (or use a parallel adjacency
   map) to carry (neighbor, weight) pairs instead of bare neighbor
   references, while keeping the same hash-map-based cycle-safe cloning
   logic. Tests whether your solution is rigidly tied to the exact Node
   shape given, or whether you understand the underlying clone-with-
   memoization pattern well enough to adapt it.
"""
