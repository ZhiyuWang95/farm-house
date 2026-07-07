"""
Problem: Convert Sorted Array to Binary Search Tree
Link: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
Topic: Tree (divide and conquer, construction)
Difficulty: Easy

=========================
Explanation
=========================
To build a height-balanced BST from a sorted array: always make the MIDDLE
element the root. This guarantees the left and right subtrees have equal (or
off-by-one) sizes, producing a balanced tree. Recursively apply the same
logic to the left and right halves.

The invariant: at every recursive call, the subarray is already sorted, so
the middle element is always the correct BST root for that subarray.

For an even-length array there are two possible midpoints; either produces a
valid balanced BST. Consistently using `mid = (lo + hi) // 2` (left-biased)
is fine; LeetCode accepts both.

This is a textbook divide-and-conquer tree construction. Recognize the
connection to merge sort's "split at midpoint" — the same spatial bisection
that makes merge sort O(n log n) is what makes this tree height O(log n).

=========================
Complexity
=========================
Time:  O(n) — each element becomes exactly one node
Space: O(log n) recursion stack (height of the balanced tree)
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build(lo, hi):
            if lo > hi:
                return None
            mid = (lo + hi) // 2
            node = TreeNode(nums[mid])
            node.left = build(lo, mid - 1)
            node.right = build(mid + 1, hi)
            return node

        return build(0, len(nums) - 1)


if __name__ == "__main__":
    def inorder(root):
        if not root:
            return []
        return inorder(root.left) + [root.val] + inorder(root.right)

    sol = Solution()
    t = sol.sortedArrayToBST([-10, -3, 0, 5, 9])
    print(inorder(t))   # [-10, -3, 0, 5, 9]
    print(t.val)        # 0 (root is middle element)
