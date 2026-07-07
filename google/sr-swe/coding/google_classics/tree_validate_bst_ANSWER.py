"""
Problem: Validate Binary Search Tree
Link: https://leetcode.com/problems/validate-binary-search-tree/
Topic: Tree (DFS with bounds)
Difficulty: Medium

=========================
Explanation
=========================
The bug almost everyone writes first: checking only `node.left.val <
node.val < node.right.val` at each node. This is WRONG -- it only verifies
the *immediate* parent-child relationship, not the full BST invariant that
EVERY node in the left subtree must be less than the current node, no
matter how deep. Example 2 in the problem statement is built exactly to
catch this bug: node 3 is less than 5 (the root) but it's nested under 4,
which is itself fine locally, yet 3 sitting in 5's RIGHT subtree at any
depth is invalid since it should be > 5.

Correct approach: DFS while threading a valid (low, high) RANGE down to
each node -- not just comparing to its immediate parent.
  - Start the root with range (-infinity, +infinity).
  - At each node, it must satisfy low < node.val < high. If not, return
    False immediately.
  - Recurse left with the same `low`, but `high` tightened to node.val
    (everything in the left subtree must be less than this node).
  - Recurse right with the same `high`, but `low` tightened to node.val.
  - A None node is trivially valid (base case: return True).

Alternative approach worth knowing: an in-order traversal of a valid BST
must produce a STRICTLY increasing sequence of values. So you can also
do an in-order DFS and just check that each visited value is greater than
the previous one -- often considered the "cleaner" solution, and the one
that generalizes better to the Recover Binary Search Tree variation below.

=========================
Complexity
=========================
Time:  O(n) -- every node visited once either way.
Space: O(h) -- recursion stack depth (tree height).
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node: Optional[TreeNode], low: float, high: float) -> bool:
            if node is None:
                return True
            if not (low < node.val < high):
                return False
            return validate(node.left, low, node.val) and validate(
                node.right, node.val, high
            )

        return validate(root, float("-inf"), float("inf"))

    # In-order traversal alternative: a BST's in-order sequence must be
    # strictly increasing.
    def isValidBSTInorder(self, root: Optional[TreeNode]) -> bool:
        prev = [None]

        def inorder(node: Optional[TreeNode]) -> bool:
            if node is None:
                return True
            if not inorder(node.left):
                return False
            if prev[0] is not None and node.val <= prev[0]:
                return False
            prev[0] = node.val
            return inorder(node.right)

        return inorder(root)


if __name__ == "__main__":
    # [2,1,3] -- valid
    valid = TreeNode(2, TreeNode(1), TreeNode(3))
    # [5,1,4,null,null,3,6] -- invalid (3 and 6 nested under 4, but 3 < 5)
    invalid = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))

    sol = Solution()
    print(sol.isValidBST(valid))     # True
    print(sol.isValidBST(invalid))   # False
    print(sol.isValidBSTInorder(valid))   # True
    print(sol.isValidBSTInorder(invalid))  # False


"""
=========================
Google-asked variations (2-3)
=========================

1. Kth Smallest Element in a BST (LeetCode 230, Medium)
   Directly reuses the in-order-traversal insight from this problem: an
   in-order traversal of a BST visits nodes in sorted order, so the kth
   value visited during in-order traversal IS the kth smallest -- no
   sorting needed. Tests whether you carry the "in-order = sorted" BST
   property forward into a different question.

2. Recover Binary Search Tree (LeetCode 99, Medium/Hard)
   "Exactly two nodes of a BST were swapped by mistake -- recover the
   tree without changing its structure." Run the same in-order traversal
   from this problem's alternative solution; the two places where the
   strictly-increasing invariant is violated point you directly at the
   two swapped nodes. A great "you already wrote 90% of this solution"
   follow-up.

3. Convert Sorted Array to Binary Search Tree (LeetCode 108, Easy/Medium)
   The reverse direction of this problem's core insight: if in-order
   traversal of a BST produces a sorted sequence, then building a
   balanced BST FROM a sorted array is done by picking the middle element
   as the root (so in-order traversal would reproduce the array) and
   recursing on the left and right halves. Good to bring up as "the
   inverse construction problem" if asked to relate BST validation to BST
   construction.
"""
