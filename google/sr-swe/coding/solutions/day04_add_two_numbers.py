"""
Problem: Add Two Numbers
Link: https://leetcode.com/problems/add-two-numbers/
Pattern: Linked List
Difficulty: Medium

Approach:
(write your approach/intuition here BEFORE coding)

Complexity:
Time: O(?)
Space: O(?)
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None:
            return l2
        
        if l2 is None:
            return l1
        
        dummyHead = ListNode(-1)

        d_travel = dummyHead
        t1 = l1
        t2 = l2
        c = 0

        while(t1 is not None or t2 is not None):
            val_1 = t1.val if t1 is not None else 0
            val_2 = t2.val if t2 is not None else 0
            sum_up = val_1 + val_2 + c
            curr = sum_up % 10
            c = sum_up // 10
            d_travel.next = ListNode(curr)

            d_travel = d_travel.next
            t1 = t1.next if t1 is not None else None
            t2 = t2.next if t2 is not None else None
        
        if c > 0:
            d_travel.next = ListNode(c)
        
        result = dummyHead.next

        dummyHead.next = None
        return result
        


# --- Notes / follow-ups discussed ---
#
