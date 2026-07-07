"""
Problem: Lowest Common Ancestor of a Binary Search Tree
Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
Topic: Tree (BST property)
Difficulty: Medium

Problem statement:
Given a BST, find the lowest common ancestor (LCA) of two given nodes p and q.
The LCA is the lowest node in the tree that has both p and q as descendants
(a node is allowed to be a descendant of itself).

Example 1:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6

Example 2:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2  (2 is ancestor of itself)

Constraints:
All node values are unique.
p != q
Both p and q exist in the BST.

Approach:
(write your approach/intuition here BEFORE coding)
Hint: use BST property — how does the relationship between root.val, p.val,
and q.val tell you which direction to go?

Complexity:
Time: O(?)
Space: O(?)
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        pass
