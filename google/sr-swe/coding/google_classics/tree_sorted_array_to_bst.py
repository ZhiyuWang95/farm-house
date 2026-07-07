"""
Problem: Convert Sorted Array to Binary Search Tree
Link: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
Topic: Tree (divide and conquer, construction)
Difficulty: Easy

Problem statement:
Given an integer array nums where the elements are sorted in ascending order,
convert it to a height-balanced BST. A height-balanced BST is one where the
depth of the two subtrees of every node never differs by more than 1.

Example 1:
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]  (or [0,-10,5,null,-3,null,9])

Example 2:
Input: nums = [1,3]
Output: [3,1]  (or [1,null,3])

Constraints:
1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
nums is sorted in ascending order.

Approach:
(write your approach/intuition here BEFORE coding)
Hint: which element should be the root to guarantee height balance?

Complexity:
Time: O(?)
Space: O(?)
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        pass
