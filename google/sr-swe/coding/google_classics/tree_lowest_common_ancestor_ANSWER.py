"""
Problem: Lowest Common Ancestor of a Binary Tree
Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
Topic: Tree (DFS)
Difficulty: Medium

=========================
Explanation
=========================
Post-order DFS where each call answers: "does the subtree rooted at this
node contain p, q, both, or neither?"

Recursive case, at node `node`:
  - If node is None, it contains neither -- return None.
  - If node IS p or q, return node itself (it "contains" that target by
    definition, regardless of what's below it).
  - Otherwise, recurse into left and right subtrees.
    - If BOTH left and right recursions return non-None, that means p was
      found in one subtree and q in the other -- so `node` itself is the
      split point, i.e. the LCA. Return node.
    - If only ONE side returned non-None, that side already contains the
      LCA (either it found one target and is still looking for the
      other higher up, or it already found the LCA further down) --
      propagate that result upward unchanged.
    - If neither side found anything, return None.

The elegant part: you never need to explicitly compute "is p an ancestor
of q" or build parent pointers first. The first node where the search
paths to p and q diverge into different children is naturally identified
as the place where both recursive calls return non-None simultaneously.

=========================
Complexity
=========================
Time:  O(n) -- in the worst case, you visit every node once (e.g. if
       p, q are in the very last subtree explored).
Space: O(h) -- recursion stack depth, where h is the tree height (O(log n)
       balanced, O(n) worst-case skewed tree).
"""

from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> Optional["TreeNode"]:
        if root is None or root is p or root is q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left is not None and right is not None:
            return root  # p and q found in different subtrees -> split point
        return left if left is not None else right


class Solution2:
    """Iterative — builds parent map, then finds ancestor intersection.

    Preferred over recursive when the tree is extremely deep (skewed tree
    with n=100k nodes would blow the recursion stack).

    Step 1: DFS to build parent map until both p and q are found.
    Step 2: Walk up from p, collecting all its ancestors into a set.
    Step 3: Walk up from q until we hit a node in p's ancestor set — that's the LCA.
    """
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        parent = {root: None}
        stack = [root]

        # step 1: build parent map until both p and q are found
        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)

        # step 2: collect all ancestors of p (including p itself)
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]

        # step 3: walk up from q until hitting p's ancestor set
        while q not in ancestors:
            q = parent[q]
        return q


if __name__ == "__main__":
    # Build: 3 -> (5 -> (6, 2 -> (7, 4)), 1 -> (0, 8))
    n6, n7, n4, n0, n8 = (
        TreeNode(6), TreeNode(7), TreeNode(4), TreeNode(0), TreeNode(8)
    )
    n2 = TreeNode(2)
    n2.left, n2.right = n7, n4
    n5 = TreeNode(5)
    n5.left, n5.right = n6, n2
    n1 = TreeNode(1)
    n1.left, n1.right = n0, n8
    root = TreeNode(3)
    root.left, root.right = n5, n1

    sol = Solution()
    print(sol.lowestCommonAncestor(root, n5, n1).val)  # 3
    print(sol.lowestCommonAncestor(root, n5, n4).val)  # 5


"""
=========================
Google-asked variations (2-3)
=========================

1. LCA of a Binary Search Tree (LeetCode 235, Easy/Medium)
   Same question, but the tree is a BST. Don't need full DFS at all --
   use the BST ordering property: walk down from root, and the first node
   where p.val and q.val end up on DIFFERENT sides (or equal to the
   current node) is the LCA, since everything left is smaller and
   everything right is larger. O(h) time with NO recursion into both
   sides -- a direct test of whether you exploit the BST invariant instead
   of reaching for the generic binary-tree algorithm out of habit.

2. LCA of a Binary Tree with Parent Pointers (LeetCode 1650, Medium,
   premium but commonly asked verbally)
   If each node has a `.parent` pointer instead of you doing top-down DFS,
   this becomes "find the intersection point of two linked lists" (walk
   up from p and from q) -- literally the same two-pointer-length-
   equalization trick used in Intersection of Two Linked Lists (LeetCode
   160). Good to mention as a structurally different but related
   approach if they hand you parent pointers.

3. LCA of a Binary Tree where node may NOT exist (LeetCode 1644, Medium)
   Same problem, but p or q might not actually be in the tree -- this
   problem's optimization of returning early at `root is p or root is q`
   becomes a bug here, because you might return a "found" answer for a
   node that isn't truly present. Requires a full traversal that
   explicitly tracks "was p actually found" and "was q actually found" as
   booleans, only trusting the LCA result if both are true. A sharp test
   of whether you understand *why* the original solution's early-return
   correctness depends on the problem's guarantee that both nodes exist.
"""
