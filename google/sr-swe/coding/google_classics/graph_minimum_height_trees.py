"""
Problem: Minimum Height Trees
Link: https://leetcode.com/problems/minimum-height-trees/
Topic: Graph (BFS leaf peeling)
Difficulty: Medium

Problem statement:
A tree is an undirected graph with n nodes labeled 0 to n-1 and n-1 edges.
Given n and edges, return a list of all root labels that produce minimum-height
trees. There are at most 2 such roots.

Example 1:
Input: n = 4, edges = [[1,0],[1,2],[1,3]]
Output: [1]

Example 2:
Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
Output: [3,4]

Constraints:
1 <= n <= 2 * 10^4
edges.length == n - 1
0 <= ai, bi < n
ai != bi

Approach:
(write your approach/intuition here BEFORE coding)

Complexity:
Time: O(?)
Space: O(?)
"""

from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        pass
