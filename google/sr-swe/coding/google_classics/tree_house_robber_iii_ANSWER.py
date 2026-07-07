"""
Problem: House Robber III
Link: https://leetcode.com/problems/house-robber-iii/
Topic: Tree (DP on tree / post-order DFS)
Difficulty: Medium

=========================
Explanation
=========================
Classic tree DP. At each node, there are two states: rob this node or skip it.
Instead of memoizing (which requires a map from node to state), propagate BOTH
states up the tree in the return value — (rob_gain, skip_gain).

At a leaf node: rob_gain = node.val, skip_gain = 0.

For an internal node:
- rob_gain = node.val + skip_left + skip_right
  (rob this node → MUST skip both children)
- skip_gain = max(rob_left, skip_left) + max(rob_right, skip_right)
  (skip this node → children are FREE to rob OR skip, take the best)

The key: returning BOTH options avoids recomputing subtrees. A naive
memoized solution (hash each node to its best value) is O(n) but slightly
heavier; this tuple-propagation approach is also O(n) with no extra data
structure, just clean recursion.

The final answer is max(rob_gain, skip_gain) at the root.

=========================
Complexity
=========================
Time:  O(n) — each node visited once
Space: O(h) recursion stack
"""

from typing import Optional, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dp(node) -> Tuple[int, int]:
            """Returns (rob_gain, skip_gain) for this subtree."""
            if not node:
                return 0, 0
            rob_l, skip_l = dp(node.left)
            rob_r, skip_r = dp(node.right)
            rob_gain = node.val + skip_l + skip_r
            skip_gain = max(rob_l, skip_l) + max(rob_r, skip_r)
            return rob_gain, skip_gain

        return max(dp(root))


if __name__ == "__main__":
    sol = Solution()
    # [3,2,3,null,3,null,1]
    root = TreeNode(3, TreeNode(2, None, TreeNode(3)), TreeNode(3, None, TreeNode(1)))
    print(sol.rob(root))  # 7

    # [3,4,5,1,3,null,1]
    root2 = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(3)), TreeNode(5, None, TreeNode(1)))
    print(sol.rob(root2))  # 9
