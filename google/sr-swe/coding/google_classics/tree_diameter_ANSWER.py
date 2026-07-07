"""
Problem: Diameter of Binary Tree
Link: https://leetcode.com/problems/diameter-of-binary-tree/
Topic: Tree (DFS, depth computation)
Difficulty: Easy

=========================
Explanation
=========================
The diameter passing through a given node = depth(left subtree) + depth(right
subtree). The global diameter is the maximum of this value across all nodes.

This is a simpler version of Binary Tree Maximum Path Sum (tree_max_path_sum.py).
The pattern is the same: a global variable tracks the best answer seen so far,
while the recursive function returns only a single value to its parent (the
longest single-arm depth, not the through-node diameter — because the parent
can only extend one arm, not both).

Two-in-one DFS:
- Returns: max depth of the current subtree (for the parent to extend).
- Side effect: updates `self.diameter` with left_depth + right_depth at this node.

=========================
Complexity
=========================
Time:  O(n) — each node visited once
Space: O(h) recursion stack
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def depth(node):
            if not node:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            self.diameter = max(self.diameter, left + right)
            return 1 + max(left, right)

        depth(root)
        return self.diameter


if __name__ == "__main__":
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    sol = Solution()
    print(sol.diameterOfBinaryTree(root))          # 3
    print(sol.diameterOfBinaryTree(TreeNode(1, TreeNode(2))))  # 1
