"""
Problem: Path with Maximum Probability
Link: https://leetcode.com/problems/path-with-maximum-probability/
Topic: Graph (modified Dijkstra with max-heap)
Difficulty: Medium

=========================
Explanation
=========================
Dijkstra's algorithm adapted for two changes: (1) maximize instead of
minimize, and (2) multiply edge weights instead of add (path probability =
product of each edge's probability).

Use a max-heap (negate probabilities since Python's heapq is a min-heap).
Start with (-1.0, start_node). Pop the node with highest current probability;
if it's end_node, return immediately — first pop is optimal just like Dijkstra.
For each neighbor, compute new_prob = cur_prob * edge_prob; if this beats
the best known probability for that neighbor, update and push to heap.

The structure is identical to Network Delay Time (graph_network_delay_time.py)
but with `*` instead of `+` and `max` instead of `min` in the relaxation step.
Recognizing this structural parallel is the key insight for the interview.

=========================
Complexity
=========================
Time:  O((V + E) log V)
Space: O(V + E)
"""

from typing import List
import heapq
from collections import defaultdict


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float],
                       start_node: int, end_node: int) -> float:
        adj = defaultdict(list)
        for (u, v), p in zip(edges, succProb):
            adj[u].append((v, p))
            adj[v].append((u, p))

        prob = [0.0] * n
        prob[start_node] = 1.0
        max_heap = [(-1.0, start_node)]

        while max_heap:
            neg_p, node = heapq.heappop(max_heap)
            cur_p = -neg_p
            if node == end_node:
                return cur_p
            if cur_p < prob[node]:
                continue
            for neighbor, edge_p in adj[node]:
                new_p = cur_p * edge_p
                if new_p > prob[neighbor]:
                    prob[neighbor] = new_p
                    heapq.heappush(max_heap, (-new_p, neighbor))

        return 0.0


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProbability(3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.2], 0, 2))  # 0.25
    print(sol.maxProbability(3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.3], 0, 2))  # 0.3
    print(sol.maxProbability(3, [[0,1]], [0.5], 0, 2))                      # 0.0
