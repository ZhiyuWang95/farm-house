"""
Problem: Reverse Linked List
Link: https://leetcode.com/problems/reverse-linked-list/
Pattern: Linked List
Difficulty: Easy

Approach:
(write your approach/intuition here BEFORE coding)

Complexity:
Time: O(N)
Space: O(1)
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while(curr is not None):
            nextt = curr.next
            curr.next = prev
            prev = curr
            curr = nextt
        
        return prev
        


# --- Notes / follow-ups discussed ---
#
