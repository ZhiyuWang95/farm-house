"""
Problem: Pacific Atlantic Water Flow
Link: https://leetcode.com/problems/pacific-atlantic-water-flow/
Topic: Graph (multi-source DFS/BFS, grid)
Difficulty: Medium

Problem statement:
There is an m x n rectangular island that borders both the Pacific Ocean
and Atlantic Ocean. The Pacific touches the island's left and top edges,
and the Atlantic touches the right and bottom edges.

The island is partitioned into a grid of cells. You are given an m x n
integer matrix heights, where heights[r][c] represents the height above
sea level of the cell at (r, c).

The island receives a lot of rain, and the rain water can flow to
neighboring cells directly north, south, east, and west if the
neighboring cell's height is less than or equal to the current cell's
height. Water can flow from any cell adjacent to an ocean into that ocean.

Return a 2D list of grid coordinates where rain water can flow to BOTH the
Pacific and Atlantic oceans.

Example:
Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

Constraints:
m == heights.length
n == heights[r].length
1 <= m, n <= 200
0 <= heights[r][c] <= 10^5

Approach:
(write your approach/intuition here BEFORE coding)

Complexity:
Time: O(?)
Space: O(?)
"""

from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pass
