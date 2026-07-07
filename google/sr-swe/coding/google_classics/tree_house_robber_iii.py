"""
Problem: House Robber III
Link: https://leetcode.com/problems/house-robber-iii/
Topic: Tree (DP on tree / post-order DFS)
Difficulty: Medium

Problem statement:
Houses are arranged as a binary tree. You cannot rob two directly-linked
houses (parent and child). Return the maximum amount you can rob.

Example 1:
Input: root = [3,2,3,null,3,null,1]
Output: 7  (rob 3 + 3 + 1)

Example 2:
Input: root = [3,4,5,1,3,null,1]
Output: 9  (rob 4 + 5)

Constraints:
The number of nodes in the tree is in the range [1, 10^4].
0 <= Node.val <= 10^4

Approach:
(write your approach/intuition here BEFORE coding)
Hint: at each node you have two choices: rob it (can't rob children) or
skip it (children are free to rob or skip). Return BOTH options up the tree.

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
    def rob(self, root: Optional[TreeNode]) -> int:
        pass
