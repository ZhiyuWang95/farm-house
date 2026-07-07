"""
Problem: Binary Tree Maximum Path Sum
Link: https://leetcode.com/problems/binary-tree-maximum-path-sum/
Topic: Tree (DFS, global max tracking)
Difficulty: Hard

=========================
Explanation
=========================
The conceptual trap: a "path" through the tree can BEND at most once --
at a single peak node, it can go down into the left child and down into
the right child -- but once the path continues upward past a node to its
PARENT, it can only have come from ONE side, not both (otherwise it
wouldn't be a simple connected path, it'd branch). This mismatch between
"what a node can contribute to its parent" (one side only) and "what the
best path THROUGH a node can use" (both sides) is exactly why you need
two different quantities at every node.

Define a recursive helper `max_gain(node)` = the maximum sum of a
downward path starting at `node` and extending into AT MOST ONE child
(this is what's safe to report to the node's parent, since the parent can
only chain through one branch).

At each node:
1. left_gain = max(0, max_gain(node.left))   -- clamp negative to 0: if a
   branch would only hurt the sum, simply don't take it.
2. right_gain = max(0, max_gain(node.right))  -- same idea.
3. "Path THROUGH this node" (using both children as a peak) =
   node.val + left_gain + right_gain. Update a global `best` with this
   value -- this is a candidate for the overall answer, even though it's
   NOT what gets returned to the parent.
4. Return node.val + max(left_gain, right_gain) -- only one side, since
   that's all a parent can legally chain onto.

The two different numbers -- "best path peaking here" (used for the
global max) vs. "best one-sided extension from here" (returned up the
call stack) -- is the core insight. Miss this distinction and you'll
either under-count valid peak paths or accidentally let a parent "double
dip" into both of a child's branches.

=========================
Complexity
=========================
Time:  O(n) -- every node visited once.
Space: O(h) -- recursion stack depth.
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        best = float("-inf")

        def max_gain(node: Optional[TreeNode]) -> int:
            nonlocal best
            if node is None:
                return 0

            left_gain = max(0, max_gain(node.left))
            right_gain = max(0, max_gain(node.right))

            best = max(best, node.val + left_gain + right_gain)

            return node.val + max(left_gain, right_gain)

        max_gain(root)
        return best


if __name__ == "__main__":
    # [1,2,3] -> best path 2 -> 1 -> 3 = 6
    t1 = TreeNode(1, TreeNode(2), TreeNode(3))
    # [-10,9,20,null,null,15,7] -> best path 15 -> 20 -> 7 = 42
    t2 = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))

    sol = Solution()
    print(sol.maxPathSum(t1))  # 6
    print(sol.maxPathSum(t2))  # 42


"""
=========================
Google-asked variations (2-3)
=========================

1. Diameter of Binary Tree (LeetCode 543, Easy/Medium)
   The simplified ancestor of this problem: instead of maximizing a SUM
   of node values along a path, maximize the NUMBER OF EDGES along a
   path. Uses the exact same shape -- a helper returns "max depth from
   this node downward" while a global variable tracks
   "left_depth + right_depth" at every node as a candidate diameter. A
   great warm-up to establish the pattern before tackling this harder
   sum-based version.

2. House Robber III (LeetCode 337, Medium)
   A different "DFS returns one thing, but tracks/considers two
   possibilities at each node" tree-DP pattern: at each node, compute
   both "max money if we rob this node" and "max money if we don't,"
   derived from the same two values computed for its children. Doesn't
   share the exact mechanics of this problem, but tests the same general
   skill of designing a DFS return value that carries enough information
   for the PARENT to make an optimal decision.

3. Longest Univalue Path (LeetCode 687, Medium)
   Same "global max updated at every node using both children, but only
   one side returned upward" skeleton as this problem, except the
   accumulation condition is "child value equals current node's value"
   (continuing a same-value chain) instead of "always extend, just clamp
   negatives." Tests whether you can swap out the aggregation rule while
   keeping the same overall DFS structure.
"""
