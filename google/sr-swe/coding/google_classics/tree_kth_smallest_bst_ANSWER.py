"""
Problem: Kth Smallest Element in a BST
Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
Topic: Tree (BST in-order traversal)
Difficulty: Medium

=========================
Explanation
=========================
In-order traversal (left → node → right) of a BST visits nodes in ascending
sorted order. So the kth node visited in-order is the kth smallest element.

Two approaches:
1. Recursive: run full in-order, collect all values, return result[k-1].
   Simple but O(n) time and O(n) extra space — wasteful if k is small.

2. Iterative with early stop (optimal): use an explicit stack to simulate
   in-order traversal. Count visited nodes; stop as soon as the counter
   reaches k. This visits only k nodes instead of n, and uses O(h) space
   for the stack.

The iterative version is preferred in interviews because it demonstrates both
mastery of iterative tree traversal and the early-stop optimization.

Follow-up insight: if the BST is frequently modified and kth smallest is
queried often, augment each node with a subtree_size counter. Then kth
smallest becomes an O(log n) lookup (similar to order-statistics trees).

=========================
Complexity
=========================
Time:  O(h + k) iterative with early stop; O(n) full traversal
Space: O(h) for the stack
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        node = root
        count = 0

        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            count += 1
            if count == k:
                return node.val
            node = node.right

        return -1


if __name__ == "__main__":
    root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
    sol = Solution()
    print(sol.kthSmallest(root, 1))  # 1
    print(sol.kthSmallest(root, 2))  # 2
    print(sol.kthSmallest(root, 3))  # 3
