"""
Problem: Clone Graph
Link: https://leetcode.com/problems/clone-graph/
Topic: Graph (DFS/BFS + hash map)
Difficulty: Medium

Problem statement:
Given a reference of a node in a connected undirected graph, return a deep
copy (clone) of the graph. Each node in the graph contains a value (int)
and a list of its neighbors.

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

Test case format: the graph is represented in the test case using an
adjacency list. Each list[i] contains a list of neighbors of node i+1.
The first node with val == 1 is always used as the starting node.

Example 1:
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: node 1's neighbors are 2 and 4, node 2's neighbors are 1 and
3, etc. -- a 4-node cycle.

Example 2:
Input: adjList = [[]]
Output: [[]]
Explanation: a single node with no neighbors.

Constraints:
The number of nodes in the graph is in the range [0, 100].
1 <= Node.val <= 100
Node.val is unique for each node.
There are no repeated edges and no self-loops in the graph.
The graph is connected.

Approach:
(write your approach/intuition here BEFORE coding)

Complexity:
Time: O(?)
Space: O(?)
"""

from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        pass
