"""
Problem: Path with Maximum Probability
Link: https://leetcode.com/problems/path-with-maximum-probability/
Topic: Graph (modified Dijkstra)
Difficulty: Medium

Problem statement:
Undirected weighted graph of n nodes. succProb[i] is the probability of
traversing edge i successfully. Find the path from start_node to end_node
with maximum probability of success.

Example 1:
Input: n=3, edges=[[0,1],[1,2],[0,2]], succProb=[0.5,0.5,0.2], start=0, end=2
Output: 0.25000  (path 0->1->2: 0.5*0.5=0.25)

Example 2:
Input: n=3, edges=[[0,1],[1,2],[0,2]], succProb=[0.5,0.5,0.3], start=0, end=2
Output: 0.30000  (direct 0->2 beats 0->1->2)

Constraints:
2 <= n <= 10^4
0 <= start, end < n
start != end
succProb[i] in [0, 1]

Approach:
(write your approach/intuition here BEFORE coding)

Complexity:
Time: O(?)
Space: O(?)
"""

from typing import List


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float],
                       start_node: int, end_node: int) -> float:
        pass
