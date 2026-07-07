"""
Problem: Recover Binary Search Tree
Link: https://leetcode.com/problems/recover-binary-search-tree/
Topic: Tree (BST in-order, find misplaced nodes)
Difficulty: Medium

Problem statement:
You are given the root of a BST in which exactly two nodes were swapped by
mistake. Recover the tree without changing its structure (swap them back).

Example 1:
Input: root = [1,3,null,null,2]  (3 and 1 are swapped)
Output: [3,1,null,null,2]

Example 2:
Input: root = [3,1,4,null,null,2]  (3 and 2 are swapped)
Output: [2,1,4,null,null,3]

Constraints:
The number of nodes in the tree is in the range [2, 1000].
-2^31 <= Node.val <= 2^31 - 1

Follow-up: Can you solve this in O(1) extra space (Morris traversal)?

Approach:
(write your approach/intuition here BEFORE coding)
Hint: In-order traversal of a valid BST is strictly ascending. Two swapped
nodes create exactly 1 or 2 "inversions" (places where prev > current).

Complexity:
Time: O(?)
Space: O(?)
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """Do not return anything, modify root in-place instead."""
        pass
