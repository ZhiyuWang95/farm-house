"""
Problem: Number of Islands
Link: https://leetcode.com/problems/number-of-islands/
Topic: DFS (grid / flood fill)
Difficulty: Medium

=========================
Explanation
=========================
This is the canonical "flood fill" problem -- the template you'll reuse
across dozens of grid problems (Word Search, Surrounded Regions, Max Area
of Island, Pacific Atlantic Water Flow, etc.).

Scan every cell in the grid. Whenever you find an unvisited '1' (land),
that's the start of a NEW island -- increment the island count, then DFS
outward from it, marking every connected '1' as visited so the outer scan
never recounts the same island.

The DFS itself: from (r, c), recurse into the 4-directional neighbors
that are in-bounds and still '1'. Mark the current cell visited (flip it
to '0', or use a separate visited set if you don't want to mutate the
input) BEFORE or AS you recurse, to avoid infinite recursion between two
cells that point back at each other.

Why DFS and not BFS here: doesn't matter for correctness -- both correctly
flood-fill a connected component. DFS is usually written with fewer lines
(simple recursion, no explicit queue), so it's the default choice for "how
many connected components" style questions. BFS is preferred when you
specifically need shortest-distance information (as in Rotting Oranges).

=========================
Complexity
=========================
Time:  O(m * n) -- every cell is visited at most a constant number of
       times (once by the outer scan, plus once when flood-filled).
Space: O(m * n) worst case for the recursion stack (a grid that's entirely
       one giant snaking island), plus O(1) extra if you mutate the grid
       in place instead of a separate visited set.
"""

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        island_count = 0

        def dfs(r: int, c: int) -> None:
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != "1":
                return
            grid[r][c] = "0"  # mark visited by sinking the land
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    island_count += 1
                    dfs(r, c)

        return island_count


class Solution2:
    """Iterative DFS using an explicit stack."""
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        island_count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    island_count += 1
                    stack = [(r, c)]
                    grid[r][c] = "0"  # mark visited before pushing
                    while stack:
                        cr, cc = stack.pop()
                        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            nr, nc = cr + dr, cc + dc
                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                                grid[nr][nc] = "0"  # mark before pushing to avoid duplicates
                                stack.append((nr, nc))

        return island_count


if __name__ == "__main__":
    sol = Solution()
    grid1 = [
        list("11110"),
        list("11010"),
        list("11000"),
        list("00000"),
    ]
    print(sol.numIslands(grid1))  # 1

    grid2 = [
        list("11000"),
        list("11000"),
        list("00100"),
        list("00011"),
    ]
    print(sol.numIslands(grid2))  # 3


"""
=========================
Google-asked variations (2-3)
=========================

1. Max Area of Island (LeetCode 695, Medium)
   "Instead of counting islands, return the area of the LARGEST island."
   Identical flood-fill structure, but the DFS now returns a count (1 +
   sum of recursive calls) instead of just marking cells, and you take the
   max over all island DFS calls instead of incrementing a counter.

2. Number of Islands II (LeetCode 305, Hard)
   "Land is added one cell at a time (via a stream of operations); after
   each addition, report the current number of islands." Flood-fill DFS
   no longer works efficiently since you'd recompute everything after each
   add -- this forces a Union-Find approach instead, where adding land
   merges adjacent island-components. A great "same problem family, but
   now the input is a stream / online" twist Google likes to test.

3. Surrounded Regions (LeetCode 130, Medium)
   "Capture all regions of 'O' that are NOT connected to the border."
   Same flood-fill mechanics, but inverted: instead of flood-filling every
   island independently, you flood-fill ONLY from the border cells first
   (marking what's safe), then flip everything else. Tests whether you can
   adapt "flood fill from every land cell" into "flood fill from a
   specific subset of starting cells" (the border) to invert the logic.
"""
