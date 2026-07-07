"""
Problem: Pacific Atlantic Water Flow
Link: https://leetcode.com/problems/pacific-atlantic-water-flow/
Topic: Graph (multi-source DFS/BFS, grid)
Difficulty: Medium

=========================
Explanation
=========================
The naive framing ("for every cell, can water starting there reach the
Pacific AND the Atlantic") would mean running a DFS/BFS from every single
cell -- O((mn)^2) in the worst case. The trick that makes this efficient:
REVERSE the direction of flow and start from the oceans instead of from
every cell.

Water flows from a HIGHER (or equal) cell to a LOWER (or equal) neighbor.
So instead of asking "can I flow downhill from cell X to the ocean
border," flip it: starting AT the ocean border, walk UPHILL (to a
neighbor whose height is >= the current cell's height) -- a cell is
reachable from the Pacific (in reverse) if and only if water from that
cell could originally flow forward, downhill, INTO the Pacific.

Algorithm:
1. Multi-source DFS (or BFS) starting from every cell on the Pacific
   border (entire top row + entire left column) simultaneously, moving to
   neighbors with height >= current height. Mark every cell reached as
   "can_reach_pacific."
2. Do the same multi-source DFS starting from the Atlantic border (entire
   bottom row + entire right column). Mark "can_reach_atlantic."
3. The answer is every cell marked in BOTH sets.

This is the same "flood-fill from the boundary inward, not from every
interior cell outward" trick used in Surrounded Regions and the 01 Matrix
family -- recognizing when to reverse a directional flow problem and seed
the BFS/DFS from the destination(s) instead of from every possible source
is one of the most reusable ideas in grid problems.

=========================
Complexity
=========================
Time:  O(m * n) -- two flood fills, each visiting every cell at most once.
Space: O(m * n) -- two boolean visited grids, plus recursion stack.
"""

from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])
        pacific = [[False] * cols for _ in range(rows)]
        atlantic = [[False] * cols for _ in range(rows)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(r: int, c: int, visited: List[List[bool]]) -> None:
            visited[r][c] = True
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < rows and 0 <= nc < cols
                    and not visited[nr][nc]
                    and heights[nr][nc] >= heights[r][c]
                ):
                    dfs(nr, nc, visited)

        for c in range(cols):
            dfs(0, c, pacific)           # top row -> Pacific
            dfs(rows - 1, c, atlantic)   # bottom row -> Atlantic
        for r in range(rows):
            dfs(r, 0, pacific)           # left column -> Pacific
            dfs(r, cols - 1, atlantic)   # right column -> Atlantic

        return [
            [r, c]
            for r in range(rows)
            for c in range(cols)
            if pacific[r][c] and atlantic[r][c]
        ]


if __name__ == "__main__":
    heights = [
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4],
    ]
    sol = Solution()
    result = sol.pacificAtlantic(heights)
    print(sorted(result))
    # [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]


"""
=========================
Google-asked variations (2-3)
=========================

1. Surrounded Regions (LeetCode 130, Medium)
   The same "flood-fill from the boundary inward" trick, but for marking
   which 'O' regions are NOT connected to the border (so they get
   captured). Directly analogous: start multi-source DFS/BFS from every
   border cell, mark what's safe, flip everything else.

2. Number of Enclaves (LeetCode 1020, Medium)
   "Count land cells that can never walk off the grid boundary." Same
   reversed-boundary-flood-fill idea: flood fill from all border land
   cells first (these can escape), then count remaining unmarked land
   cells (these are enclosed). Tests the same pattern recognition with a
   counting answer instead of a coordinate-list answer.

3. Trapping Rain Water II (LeetCode 407, Hard)
   The natural escalation: instead of just determining "can water flow
   off the grid in 2 specific directions," compute the actual VOLUME of
   water trapped in a 3D height map. Requires a min-heap (priority queue)
   flood fill from the boundary inward, always expanding from the
   currently-lowest boundary cell -- a significant step up in difficulty
   but built on the exact same "start from the border, work inward"
   instinct as this problem.
"""
