"""
Problem: Recover Binary Search Tree
Link: https://leetcode.com/problems/recover-binary-search-tree/
Topic: Tree (BST in-order, find misplaced nodes)
Difficulty: Medium

=========================
Explanation
=========================
In-order traversal of a valid BST produces a strictly increasing sequence.
Swapping two nodes creates inversions (places where prev.val > curr.val).

Two cases to handle:
- Adjacent swap: only ONE inversion. e.g., [1,3,2,4] → inversion at (3,2).
  first = 3 (the larger of the pair), second = 2 (the smaller).
- Non-adjacent swap: TWO inversions. e.g., [1,4,3,2,5] → inversions at (4,3)
  and (3,2). first = 4 (larger of FIRST inversion), second = 2 (smaller of
  SECOND inversion).

Algorithm:
Track `prev`, `first` (first misplaced node), `second` (second misplaced node).
During in-order traversal: if prev.val > curr.val → this is an inversion.
Set first = prev on the FIRST occurrence, set second = curr on EVERY occurrence.
After traversal, swap first.val and second.val.

The trick: always update `second` on every inversion — this handles the
non-adjacent case where second gets updated twice (first to the wrong value,
then corrected to the right one).

=========================
Complexity
=========================
Time:  O(n)
Space: O(h) recursion stack; O(1) with Morris traversal (follow-up)
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        self.prev = None
        self.first = None
        self.second = None

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            if self.prev and self.prev.val > node.val:
                if not self.first:
                    self.first = self.prev  # first misplaced: the larger node
                self.second = node          # second misplaced: always update
            self.prev = node
            inorder(node.right)

        inorder(root)
        self.first.val, self.second.val = self.second.val, self.first.val


if __name__ == "__main__":
    def inorder_vals(root):
        if not root:
            return []
        return inorder_vals(root.left) + [root.val] + inorder_vals(root.right)

    # [3,1,4,null,null,2] — 3 and 2 swapped
    root = TreeNode(3, TreeNode(1), TreeNode(4, TreeNode(2)))
    Solution().recoverTree(root)
    print(inorder_vals(root))  # [1, 2, 3, 4]

    # [1,3,null,null,2] — 1 and 3 swapped (adjacent case)
    root2 = TreeNode(1, TreeNode(3, None, TreeNode(2)))
    Solution().recoverTree(root2)
    print(inorder_vals(root2))  # [1, 2, 3]
