"""
Problem: N-Queens
Link: https://leetcode.com/problems/n-queens/
Topic: DFS (backtracking, constraint satisfaction)
Difficulty: Hard

=========================
Explanation
=========================
Classic backtracking: place one queen per row (guarantees no row conflicts),
try each column in that row, and check column + diagonal constraints before
placing. If a placement is invalid, skip it; if valid, recurse to the next row.

Constraint tracking with 3 sets (O(1) lookup):
- `cols`: occupied columns.
- `diag1`: occupied "top-left to bottom-right" diagonals. Cells on the same
  diagonal share the same (row - col) value.
- `diag2`: occupied "top-right to bottom-left" diagonals. Cells on the same
  anti-diagonal share the same (row + col) value.

When we place a queen at (row, col), we add col to `cols`, (row - col) to
`diag1`, and (row + col) to `diag2`. We remove them when backtracking.

Board construction: maintain a `queens` list (queens[row] = col). After
successfully placing all n queens, convert to the string format.

=========================
Complexity
=========================
Time:  O(n!) worst case (n choices row 0, n-1 row 1, etc.), but diag pruning
       significantly reduces actual work. Often cited as O(n!).
Space: O(n) for the sets and queens list; O(n^2) per solution board.
"""

from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        queens = []  # queens[row] = col
        cols = set()
        diag1 = set()  # row - col
        diag2 = set()  # row + col

        def backtrack(row):
            if row == n:
                board = []
                for c in queens:
                    board.append("." * c + "Q" + "." * (n - c - 1))
                result.append(board)
                return
            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue
                cols.add(col); diag1.add(row - col); diag2.add(row + col)
                queens.append(col)
                backtrack(row + 1)
                queens.pop()
                cols.remove(col); diag1.remove(row - col); diag2.remove(row + col)

        backtrack(0)
        return result


if __name__ == "__main__":
    sol = Solution()
    for board in sol.solveNQueens(4):
        for row in board:
            print(row)
        print()
    print(len(sol.solveNQueens(8)))  # 92 solutions for 8-queens
