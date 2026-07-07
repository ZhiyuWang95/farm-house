"""
Problem: Linked List Cycle II
Link: https://leetcode.com/problems/linked-list-cycle-ii/
Topic: Linked List (fast/slow pointers)
Difficulty: Medium

Problem statement:
Given the head of a linked list, return the node where the cycle begins.
If there is no cycle, return null.

There is a cycle in a linked list if some node can be reached again by
continuously following the next pointer. Internally, a `pos` index
indicates the index of the node the tail's next pointer connects to
(0-indexed). It is -1 if there is no cycle. Note: pos is not passed as a
parameter -- it's only used to construct the test case internally.

Do not modify the linked list.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1 (the node with value 2)

Example 2:
Input: head = [1,2], pos = 0
Output: tail connects to node index 0 (the node with value 1)

Example 3:
Input: head = [1], pos = -1
Output: no cycle

Constraints:
The number of nodes in the list is in the range [0, 10^4].
-10^5 <= Node.val <= 10^5
pos is -1 or a valid index in the linked-list.

Follow-up: Can you solve it using O(1) (i.e. constant) memory?

Approach:
(write your approach/intuition here BEFORE coding)

Complexity:
Time: O(?)
Space: O(?)
"""

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pass
