"""
Problem: Diameter of Binary Tree
Link: https://leetcode.com/problems/diameter-of-binary-tree/
Topic: Tree (DFS, depth computation)
Difficulty: Easy

Problem statement:
Given the root of a binary tree, return the length of the diameter.
The diameter is the length of the longest path between any two nodes
(the path may or may not pass through the root). Length = number of edges.

Example 1:
Input: root = [1,2,3,4,5]
Output: 3  (path: 4->2->1->3 or 5->2->1->3)

Example 2:
Input: root = [1,2]
Output: 1

Constraints:
The number of nodes is in the range [1, 10^4].
-100 <= Node.val <= 100.

Approach:
(write your approach/intuition here BEFORE coding)
Hint: at each node, the diameter passing through it = left_depth + right_depth.

Complexity:
Time: O(?)
Space: O(?)
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        pass
