"""
Problem: Course Schedule
Link: https://leetcode.com/problems/course-schedule/
Topic: Graph (topological sort / cycle detection)
Difficulty: Medium

=========================
Explanation
=========================
Reframe the problem: courses are nodes, and a prerequisite [a, b] is a
directed edge b -> a ("b must come before a"). "Can you finish all
courses" is exactly "does this directed graph have a valid topological
ordering," which is exactly "is this directed graph acyclic." So the
entire problem reduces to: detect whether a directed graph has a cycle.

Two standard approaches, both worth knowing:

1. DFS with 3-coloring (white/gray/black), this answer's approach:
   - WHITE (unvisited): haven't started exploring this node yet.
   - GRAY (in progress): currently on the recursion stack for this DFS
     branch -- if you reach a GRAY node again, you've found a back-edge,
     i.e. a cycle.
   - BLACK (done): fully explored, confirmed cycle-free from this node.
   DFS each node; if you ever hit a GRAY node mid-traversal, return False
   (cycle found). Mark a node BLACK only after all its neighbors are
   fully explored (post-order).

2. Kahn's algorithm (BFS, in-degree counting):
   Compute each node's in-degree (number of prerequisites). Push all
   in-degree-0 nodes (no prerequisites) into a queue. Repeatedly pop a
   node, "complete" it, and decrement the in-degree of its neighbors;
   any neighbor that drops to in-degree 0 gets pushed. If you manage to
   process all numCourses nodes this way, no cycle exists. If the queue
   empties early with nodes unprocessed, those remaining nodes are stuck
   in a cycle (their in-degree never reaches 0).

Either is a fully correct, expected answer. Kahn's algorithm is usually
preferred when you need the ACTUAL ordering (Course Schedule II) since it
naturally produces one as a byproduct; DFS coloring is often a few lines
shorter when you only need a yes/no cycle check.

=========================
Complexity
=========================
Time:  O(V + E) -- V courses, E prerequisite edges, each visited once.
Space: O(V + E) -- adjacency list plus the color/in-degree arrays.
"""

from collections import deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        visiting = set()  # nodes on the current DFS path
        visited = set()   # nodes fully processed, confirmed cycle-free

        def has_cycle(node: int) -> bool:
            if node in visiting:
                return True   # came back to a node on our path — cycle!
            if node in visited:
                return False  # already cleared, safe to skip

            visiting.add(node)
            for neighbor in graph[node]:
                if has_cycle(neighbor):
                    return True
            visiting.remove(node)
            visited.add(node)
            return False

        for course in range(numCourses):
            if has_cycle(course):
                return False
        return True

    # Kahn's algorithm (BFS) alternative -- preferred when you also need
    # the actual valid ordering (see Course Schedule II below).
    def canFinishKahn(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1

        queue = deque(c for c in range(numCourses) if in_degree[c] == 0)
        completed = 0

        while queue:
            node = queue.popleft()
            completed += 1
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return completed == numCourses


if __name__ == "__main__":
    sol = Solution()
    print(sol.canFinish(2, [[1, 0]]))          # True
    print(sol.canFinish(2, [[1, 0], [0, 1]]))  # False
    print(sol.canFinishKahn(2, [[1, 0]]))          # True
    print(sol.canFinishKahn(2, [[1, 0], [0, 1]]))  # False


"""
=========================
Google-asked variations (2-3)
=========================

1. Course Schedule II (LeetCode 210, Medium)
   "Return the actual ordering of courses, not just true/false." Kahn's
   algorithm gives this directly -- the order nodes are popped from the
   queue IS a valid topological order. With DFS coloring, you'd need to
   append nodes to a result list in post-order (after exploring all
   neighbors) and reverse it at the end. Tests whether you picked the
   right one of the two approaches for what's actually being asked.

2. Alien Dictionary (LeetCode 269, Hard, premium but a very commonly
   cited Google question)
   "Given a list of words sorted according to an unknown alien alphabet's
   ordering, derive that ordering." You first have to construct the graph
   yourself by comparing adjacent words letter-by-letter to infer "this
   letter comes before that letter" edges, THEN run topological sort.
   Tests whether you can recognize "this is secretly a topo-sort problem"
   when the graph isn't handed to you explicitly -- a very Google-style
   layer of indirection on top of this exact pattern.

3. Minimum Height Trees (LeetCode 310, Medium)
   Not exactly topological sort, but uses the same "repeatedly peel off
   degree-1 (leaf) nodes" idea as Kahn's "repeatedly peel off in-degree-0
   nodes" -- on an undirected tree, iteratively stripping leaves layer by
   layer (BFS-like) converges on the tree's center, which minimizes
   height. Good to mention as a related "peel the graph from the outside
   in, layer by layer" pattern if asked to compare/contrast.
"""
