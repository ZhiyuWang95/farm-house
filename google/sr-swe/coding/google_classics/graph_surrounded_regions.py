"""
Problem: Surrounded Regions
Link: https://leetcode.com/problems/surrounded-regions/
Topic: Graph (DFS/BFS from boundary)
Difficulty: Medium

Problem statement:
Given an m x n matrix board of 'X' and 'O', capture all regions surrounded
by 'X'. A region is captured by flipping all enclosed 'O's into 'X's.
A region is surrounded if NO 'O' in it is connected to a border 'O'.

Example:
Input:
  [["X","X","X","X"],
   ["X","O","O","X"],
   ["X","X","O","X"],
   ["X","O","X","X"]]
Output:
  [["X","X","X","X"],
   ["X","X","X","X"],
   ["X","X","X","X"],
   ["X","O","X","X"]]
(The bottom-left 'O' is on the border, so it's safe.)

Constraints:
m == board.length, n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'

Approach:
(write your approach/intuition here BEFORE coding)

Complexity:
Time: O(?)
Space: O(?)
"""

from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """Do not return anything, modify board in-place instead."""
        pass
