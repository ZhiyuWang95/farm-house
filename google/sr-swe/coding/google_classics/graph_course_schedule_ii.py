"""
Problem: Course Schedule II
Link: https://leetcode.com/problems/course-schedule-ii/
Topic: Graph (topological sort)
Difficulty: Medium

Problem statement:
There are numCourses courses labeled 0 to numCourses - 1. Given prerequisites[i] = [ai, bi]
(must take bi before ai), return the ordering of courses to finish all courses.
Return empty array if impossible (cycle exists).

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0, 1]

Example 2:
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]  (any valid topological order)

Constraints:
1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)

Approach:
(write your approach/intuition here BEFORE coding)

Complexity:
Time: O(?)
Space: O(?)
"""

from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pass
