"""
Problem: Lowest Common Ancestor of a Binary Search Tree
Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
Topic: Tree (BST property)
Difficulty: Medium

=========================
Explanation
=========================
The general Binary Tree LCA (tree_lowest_common_ancestor.py) uses post-order
DFS and works regardless of tree structure. This BST version is simpler because
the BST ordering property eliminates the need to recurse into both subtrees.

At each node: if both p and q are smaller than root → LCA is in the left
subtree. If both are larger → LCA is in the right subtree. Otherwise (p and q
are on opposite sides, or one equals root) → root IS the LCA.

Iterative implementation (no recursion overhead):
Simply walk down the tree following the above logic until you can't proceed
in one direction — that node is the answer. This works in O(h) time with O(1)
space (vs O(h) stack space for recursive version).

Contrast with general tree LCA: the BST property replaces a two-subtree
post-order scan (O(n)) with a guided descent (O(h)), which is O(log n) for
a balanced BST.

=========================
Complexity
=========================
Time:  O(h) where h = tree height; O(log n) for balanced BST, O(n) worst case
Space: O(1) iterative; O(h) recursive
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        node = root
        while node:
            if p.val < node.val and q.val < node.val:
                node = node.left
            elif p.val > node.val and q.val > node.val:
                node = node.right
            else:
                return node
        return None


if __name__ == "__main__":
    # Build BST: [6,2,8,0,4,7,9]
    root = TreeNode(6)
    root.left = TreeNode(2); root.right = TreeNode(8)
    root.left.left = TreeNode(0); root.left.right = TreeNode(4)
    root.right.left = TreeNode(7); root.right.right = TreeNode(9)

    sol = Solution()
    print(sol.lowestCommonAncestor(root, root.left, root.right).val)       # 6
    print(sol.lowestCommonAncestor(root, root.left, root.left.right).val)  # 2
