"""
Problem: Cheapest Flights Within K Stops
Link: https://leetcode.com/problems/cheapest-flights-within-k-stops/
Topic: Graph (Bellman-Ford with stop constraint)
Difficulty: Medium

=========================
Explanation
=========================
The k-stops constraint breaks standard Dijkstra: you can't mark a node as
"done" once visited because a path with fewer stops (even if currently more
expensive) might enable cheaper connections later — and you need to prune by
stop count, not just cost.

Bellman-Ford is the natural fit: run exactly k+1 relaxation rounds (k stops
means k+1 edges). The critical detail: use a COPY of `prices` from the START
of each round for lookups, not the prices being updated during the round.
Without this, a single round might chain multiple edges, effectively allowing
more than k+1 edges.

Algorithm:
1. prices[src] = 0, prices[i] = inf for i != src.
2. Repeat k+1 times: prev = prices[:] (snapshot). For each edge (u, v, w):
   if prev[u] + w < prices[v], update prices[v].
3. Return prices[dst] if finite, else -1.

Alternatively, use modified BFS with state (cost, city, stops_remaining),
treating stops like a resource budget. Both run in O(k * E).

=========================
Complexity
=========================
Time:  O(k * E) where E = number of flights
Space: O(n) for prices array
"""

from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        for _ in range(k + 1):
            prev = prices[:]
            for u, v, w in flights:
                if prev[u] != float("inf") and prev[u] + w < prices[v]:
                    prices[v] = prev[u] + w

        return prices[dst] if prices[dst] != float("inf") else -1


if __name__ == "__main__":
    sol = Solution()
    print(sol.findCheapestPrice(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1))  # 700
    print(sol.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1))  # 200
    print(sol.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0))  # 500
