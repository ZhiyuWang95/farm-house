"""
Problem: Cheapest Flights Within K Stops
Link: https://leetcode.com/problems/cheapest-flights-within-k-stops/
Topic: Graph (Bellman-Ford / modified BFS)
Difficulty: Medium

Problem statement:
There are n cities connected by flights. flights[i] = [fromi, toi, pricei].
Given src, dst, and k, return the cheapest price from src to dst with at most
k stops. If no such route exists, return -1.
(k stops = k+1 edges)

Example 1:
Input: n=4, flights=[[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src=0, dst=3, k=1
Output: 700  (0->1->3)

Example 2:
Input: n=3, flights=[[0,1,100],[1,2,100],[0,2,500]], src=0, dst=2, k=1
Output: 200  (0->1->2)

Constraints:
1 <= n <= 100
0 <= flights.length <= n*(n-1)/2
src != dst
0 <= k < n

Approach:
(write your approach/intuition here BEFORE coding)

Complexity:
Time: O(?)
Space: O(?)
"""

from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        pass
