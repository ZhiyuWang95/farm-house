"""
Problem: Rotting Oranges
Link: https://leetcode.com/problems/rotting-oranges/
Topic: BFS (multi-source, grid)
Difficulty: Medium

=========================
Explanation
=========================
The key recognition: this is BFS, but with MULTIPLE SOURCES instead of one.
Every rotten orange on the grid at minute 0 is a simultanerus BFS source --
they all spread outward in lockstep, one "ring" per minute. This is exactly
why BFS (level-by-level) is the right tool, not DFS: BFS naturally
processes "all nodes at distance k" before "all nodes at distance k+1",
and here "distance k" literally means "k minutes for the rot to reach
here."

Algorithm:
1. Scan the grid once: push every rotten orange's (row, col) into a queue
   as a BFS source, and count the total number of fresh oranges.
2. Run standard multi-source BFS: process the queue level by level. Each
   full "level" (everything currently in the queue) represents one minute.
   For each rotten orange popped, look at its 4 neighbors; if a neighbor
   is fresh, rot it (decrement the fresh count, mark grid value 2), and
   push it onto the queue for the *next* level.
3. Track how many levels (minutes) you process. After the queue empties,
   if fresh_count > 0, some oranges were unreachable -- return -1.
   Otherwise return the minute count.

The "process by levels, not by individual pops" detail is the part people
get wrong under time pressure -- you must track queue size at the start of
each minute (`for _ in range(len(queue))`) so the minute counter only
increments once per full ring, not once per individual orange.

=========================
Complexity
=========================
Time:  O(m * n) -- every cell is visited and enqueued at most once.
Space: O(m * n) -- worst case, the queue holds up to the full grid.
"""

from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1

        if fresh_count == 0:
            return 0

        minutes = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue and fresh_count > 0:
            minutes += 1
            for _ in range(len(queue)):  # process exactly one "ring"/minute
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_count -= 1
                        queue.append((nr, nc))

        return minutes if fresh_count == 0 else -1


if __name__ == "__main__":
    sol = Solution()
    print(sol.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))  # 4
    print(sol.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]))  # -1
    print(sol.orangesRotting([[0, 2]]))  # 0


"""
=========================
Google-asked variations (2-3)
=========================

1. Word Ladder (LeetCode 127) -- see bfs_word_ladder.py in this folder.
   Different domain (words instead of a grid), but the exact same
   "multi-step BFS where each level = one unit of time/transformation"
   shape. Good to point out the structural similarity if asked to compare.

2. Shortest Path in Binary Matrix (LeetCode 1091, Medium)
   "Find the shortest 8-directionally-connected path from top-left to
   bottom-right in a binary grid." Single-source (not multi-source) BFS,
   but tests whether you can adapt the grid-BFS template to 8 directions
   instead of 4, and to "find shortest path to a specific target" instead
   of "find time until everything is reached."

3. 01 Matrix / Distance to nearest 0 (LeetCode 542, Medium)
   "For each cell in a binary matrix, find the distance to the nearest 0."
   This is the generalized version of Rotting Oranges: instead of asking
   "when does everything get reached," it asks "what's each cell's
   individual distance from the nearest source" -- same multi-source BFS
   starting from all the 0-cells simultaneously, just tracking distance
   per cell instead of a single global minute counter.
"""
