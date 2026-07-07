"""
Problem: Kth Smallest Element in a BST
Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
Topic: Tree (BST in-order traversal)
Difficulty: Medium

Problem statement:
Given the root of a BST and an integer k, return the kth smallest value
(1-indexed) among all the node values in the tree.

Example 1:
Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3

Constraints:
1 <= k <= n <= 10^4
All node values are unique.

Follow-up: If the BST is modified (insert/delete) often and you need to find
the kth frequently, how would you optimize?

Approach:
(write your approach/intuition here BEFORE coding)
Hint: In-order traversal of a BST visits nodes in ascending sorted order.

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
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        pass
