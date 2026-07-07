"""
Problem: Surrounded Regions
Link: https://leetcode.com/problems/surrounded-regions/
Topic: Graph (DFS from boundary, multi-source flood fill)
Difficulty: Medium

=========================
Explanation
=========================
Key inversion: instead of finding which 'O' cells ARE surrounded (hard to
prove directly), find which are NOT surrounded — those connected to the
boundary — and protect them. Everything else gets flipped.

Three-pass algorithm:
1. DFS from every border 'O': mark all reachable connected 'O's as 'S' (safe).
2. Scan the entire board: remaining 'O's are enclosed → flip to 'X'.
3. Restore: 'S' → back to 'O'.

This is the same "reverse source" pattern as Pacific Atlantic Water Flow:
computing connectivity FROM the boundary is simpler than asking "can this
cell reach the boundary?", even though they're logically equivalent questions.

Use iterative DFS (explicit stack) for large boards to avoid Python's default
recursion limit of 1000 frames on a 200×200 grid (40,000 cells worst case).

=========================
Complexity
=========================
Time:  O(m * n) — each cell visited at most once
Space: O(m * n) — explicit stack worst case (all cells are 'O')
"""

from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return
        rows, cols = len(board), len(board[0])

        def dfs(r, c):
            stack = [(r, c)]
            while stack:
                cr, cc = stack.pop()
                if cr < 0 or cr >= rows or cc < 0 or cc >= cols or board[cr][cc] != 'O':
                    continue
                board[cr][cc] = 'S'
                for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                    stack.append((cr + dr, cc + dc))

        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)
        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'S':
                    board[r][c] = 'O'


if __name__ == "__main__":
    sol = Solution()
    board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    sol.solve(board)
    for row in board:
        print(row)
    # Row 3 bottom-left 'O' stays (border-connected); middle 'O's become 'X'
