"""
Problem: Course Schedule II
Link: https://leetcode.com/problems/course-schedule-ii/
Topic: Graph (topological sort)
Difficulty: Medium

=========================
Explanation
=========================
Direct extension of Course Schedule (207): return the actual topological order
instead of just True/False for cycle detection.

Kahn's algorithm (BFS/in-degree) naturally emits nodes in topological order
as it drains the zero-in-degree queue:
1. Build adjacency list and in-degree count for each node.
2. Push all nodes with in-degree 0 (no prerequisites) into a queue.
3. Pop a node, append to result, decrement neighbors' in-degree. If a
   neighbor's in-degree reaches 0, push it to the queue.
4. If result length == numCourses, return result. Otherwise a cycle exists
   (some nodes were never reachable) — return [].

The DFS approach works too: 3-color nodes (0=unvisited, 1=in-stack, 2=done).
If we reach an in-stack node during DFS, there's a cycle. After all neighbors
complete, push the current node onto a stack; reversed stack = topological order.

=========================
Complexity
=========================
Time:  O(V + E) where V = numCourses, E = len(prerequisites)
Space: O(V + E) for adjacency list and queue
"""

from typing import List
from collections import deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses

        for course, pre in prerequisites:
            adj[pre].append(course)
            in_degree[course] += 1

        queue = deque(i for i in range(numCourses) if in_degree[i] == 0)
        order = []

        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in adj[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return order if len(order) == numCourses else []


if __name__ == "__main__":
    sol = Solution()
    print(sol.findOrder(2, [[1, 0]]))                       # [0, 1]
    print(sol.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))      # [0,1,2,3] or [0,2,1,3]
    print(sol.findOrder(1, []))                             # [0]
    print(sol.findOrder(2, [[1,0],[0,1]]))                  # [] (cycle)
