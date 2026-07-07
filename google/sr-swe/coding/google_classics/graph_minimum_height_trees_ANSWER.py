"""
Problem: Minimum Height Trees
Link: https://leetcode.com/problems/minimum-height-trees/
Topic: Graph (BFS leaf peeling / topological)
Difficulty: Medium

=========================
Explanation
=========================
The roots of minimum-height trees are the "centroids" — the 1 or 2 nodes at
the center of the longest path. Instead of trying every node as root (O(n^2)),
use leaf-peeling — iteratively remove all current leaves until 1 or 2 nodes
remain. Those survivors are the MHT roots.

This mirrors Kahn's topological sort: start with all degree-1 nodes (leaves),
remove them and their edges, then repeat with the new leaves. The process
converges because we always reduce the tree toward its center.

Algorithm:
1. Build undirected adjacency list and degree array.
2. Initialize queue with all degree-1 nodes (leaves). Track remaining node count.
3. While remaining > 2: remove len(queue) leaf nodes, reduce neighbors' degree,
   add new degree-1 nodes to next queue. Decrement remaining by each batch.
4. Return remaining nodes (the final queue contents).

Edge case: n == 1 → return [0] directly (no edges, single node is root).

=========================
Complexity
=========================
Time:  O(n) — each node processed once
Space: O(n) — adjacency sets and queue
"""

from typing import List
from collections import deque


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        adj = [set() for _ in range(n)]
        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)

        leaves = deque(i for i in range(n) if len(adj[i]) == 1)
        remaining = n

        while remaining > 2:
            remaining -= len(leaves)
            next_leaves = deque()
            for leaf in leaves:
                neighbor = next(iter(adj[leaf]))
                adj[neighbor].remove(leaf)
                if len(adj[neighbor]) == 1:
                    next_leaves.append(neighbor)
            leaves = next_leaves

        return list(leaves)


if __name__ == "__main__":
    sol = Solution()
    print(sol.findMinHeightTrees(4, [[1,0],[1,2],[1,3]]))              # [1]
    print(sol.findMinHeightTrees(6, [[3,0],[3,1],[3,2],[3,4],[5,4]])) # [3,4]
    print(sol.findMinHeightTrees(1, []))                               # [0]
    print(sol.findMinHeightTrees(2, [[0,1]]))                          # [0,1]
