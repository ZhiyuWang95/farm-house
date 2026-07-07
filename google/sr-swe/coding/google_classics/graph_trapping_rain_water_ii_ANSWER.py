"""
Problem: Trapping Rain Water II
Link: https://leetcode.com/problems/trapping-rain-water-ii/
Topic: Graph (min-heap BFS from boundary)
Difficulty: Hard

=========================
Explanation
=========================
3D extension of Trapping Rain Water I. The 1D two-pointer approach doesn't
generalize because water can escape in all four directions, not just left/right.

Key insight: water can only escape over the LOWEST boundary cell. Process
cells in order of increasing height (min-heap), starting from the entire border.

Algorithm:
1. Push all border cells into a min-heap as (height, row, col). Mark visited.
2. Pop the minimum-height boundary cell (h, r, c). For each unvisited neighbor:
   - Water trapped = max(0, h - neighbor_height): the boundary "wall" is h.
   - Push neighbor with height = max(h, neighbor_height): even if the neighbor
     is shorter than h, the effective ceiling for cells further inward is still h
     (the lowest wall water must pass over to escape).
3. Accumulate all water.

The min-heap ensures we always process from the shortest current boundary
outward, correctly computing each interior cell's water capacity. This is
essentially Dijkstra's BFS applied to water containment rather than distances.

=========================
Complexity
=========================
Time:  O(m * n * log(m * n)) — each cell pushed/popped from heap once
Space: O(m * n)
"""

from typing import List
import heapq


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or len(heightMap) < 3 or len(heightMap[0]) < 3:
            return 0

        rows, cols = len(heightMap), len(heightMap[0])
        visited = [[False] * cols for _ in range(rows)]
        heap = []

        for r in range(rows):
            for c in range(cols):
                if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                    heapq.heappush(heap, (heightMap[r][c], r, c))
                    visited[r][c] = True

        water = 0
        while heap:
            h, r, c = heapq.heappop(heap)
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                    visited[nr][nc] = True
                    water += max(0, h - heightMap[nr][nc])
                    heapq.heappush(heap, (max(h, heightMap[nr][nc]), nr, nc))

        return water


if __name__ == "__main__":
    sol = Solution()
    print(sol.trapRainWater([[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]))  # 4
    print(sol.trapRainWater([[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]))  # 10
