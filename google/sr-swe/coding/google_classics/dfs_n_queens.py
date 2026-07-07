"""
Problem: N-Queens
Link: https://leetcode.com/problems/n-queens/
Topic: DFS (backtracking, constraint satisfaction)
Difficulty: Hard

Problem statement:
The n-queens puzzle: place n queens on an n x n chessboard such that no two
queens attack each other (no shared row, column, or diagonal). Return all
distinct solutions as board configurations.

Example 1:
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]

Example 2:
Input: n = 1
Output: [["Q"]]

Constraints:
1 <= n <= 9

Approach:
(write your approach/intuition here BEFORE coding)
Hint: place queens one row at a time. For each row, try each column. Track
which columns and diagonals are already occupied.

Complexity:
Time: O(?)
Space: O(?)
"""

from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        pass
