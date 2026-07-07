"""
Problem: Network Delay Time
Link: https://leetcode.com/problems/network-delay-time/
Topic: Graph (weighted shortest path / Dijkstra)
Difficulty: Medium

=========================
Explanation
=========================
This is the first graph problem in this set with WEIGHTED edges, which is
exactly why plain BFS (correct for unweighted shortest path) doesn't work
here -- BFS assumes every edge costs the same "1 step," but here edges
have different travel times. The right tool is Dijkstra's algorithm:
single-source shortest path on a graph with non-negative edge weights.

Algorithm:
1. Build a weighted adjacency list: graph[u] = list of (v, weight).
2. Maintain dist[] (best known time to reach each node, init infinity
   except dist[k] = 0) and a min-heap seeded with (0, k).
3. Repeatedly pop the (currently smallest distance, node) pair. If this
   distance is already worse than what's recorded in dist[] for that
   node (a stale heap entry from before we found a better path), skip it
   -- this is what makes a "lazy deletion" heap-based Dijkstra correct
   without needing to physically remove stale entries.
4. Otherwise, relax every neighbor: if dist[node] + weight < dist[neighbor],
   update dist[neighbor] and push (new_dist, neighbor) onto the heap.
5. After the heap empties, the answer is max(dist.values()) -- the time
   for ALL nodes to receive the signal is bounded by the SLOWEST node to
   receive it. If any node's dist is still infinity, return -1
   (unreachable).

Why the min-heap (priority queue) instead of a plain queue: Dijkstra's
greedy correctness relies on always expanding the closest known unvisited
node next -- a plain FIFO queue (BFS) doesn't guarantee that ordering once
edges have different weights.

=========================
Complexity
=========================
Time:  O(E log V) -- each edge can trigger one heap push/pop, and heap
       operations are O(log V).
Space: O(V + E) -- adjacency list, dist array, and the heap.
"""

import heapq
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n + 1)]
        for u, v, w in times:
            graph[u].append((v, w))

        dist = {node: float("inf") for node in range(1, n + 1)}
        dist[k] = 0
        heap = [(0, k)]  # (distance, node)

        while heap:
            d, node = heapq.heappop(heap)
            if d > dist[node]:
                continue  # stale entry, a better path was already found
            for neighbor, weight in graph[node]:
                new_dist = d + weight
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    heapq.heappush(heap, (new_dist, neighbor))

        max_dist = max(dist.values())
        return max_dist if max_dist != float("inf") else -1


if __name__ == "__main__":
    sol = Solution()
    print(sol.networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))  # 2
    print(sol.networkDelayTime([[1, 2, 1]], 2, 1))  # 1
    print(sol.networkDelayTime([[1, 2, 1]], 2, 2))  # -1


"""
=========================
Google-asked variations (2-3)
=========================

1. Cheapest Flights Within K Stops (LeetCode 787, Medium)
   "Same weighted shortest-path shape, but you're also constrained to at
   most K stops/edges." Plain Dijkstra doesn't track hop count, so the
   standard fix is Bellman-Ford run for exactly K+1 rounds (relax all
   edges K+1 times), or a modified Dijkstra where the state in the heap
   is (cost, node, stops_used). Tests whether you can extend Dijkstra's
   state space when a second constraint (hop count) is added on top of
   cost.

2. Path with Maximum Probability (LeetCode 1514, Medium)
   "Edges have a success probability (0 to 1); find the path maximizing
   the PRODUCT of probabilities." Same Dijkstra skeleton, but you MAXIMIZE
   instead of minimize, and combine edge weights by multiplying instead of
   summing -- the heap becomes a max-heap (or negate values for Python's
   min-heap), and the relaxation condition flips to "if new_prob >
   dist[neighbor]." Tests whether you understand Dijkstra's greedy
   correctness argument well enough to adapt it beyond pure summed
   distances.

3. Swim in Rising Water (LeetCode 778, Hard)
   On a grid instead of an explicit graph, find the minimum elevation
   threshold such that a connected path of cells <= that threshold exists
   from top-left to bottom-right. This is Dijkstra in disguise: treat each
   cell as a node, "cost" to enter a cell is its height, and you're
   minimizing the MAX cell height along the path rather than the SUM --
   a "minimax path" variant of Dijkstra, solvable with the same
   min-heap-of-frontier-cells structure as this problem.
"""
