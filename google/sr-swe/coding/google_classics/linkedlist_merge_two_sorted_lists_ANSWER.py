"""
Problem: Merge Two Sorted Lists
Link: https://leetcode.com/problems/merge-two-sorted-lists/
Topic: Linked List
Difficulty: Easy

=========================
Explanation
=========================
Classic two-pointer merge, same idea as the merge step of merge sort, just
applied to linked lists instead of arrays.

Use a dummy head node so you never have to special-case "is this the first
node of the result." Keep a `tail` pointer at the end of the merged list so
far. At each step, compare the current heads of list1 and list2, splice
the smaller one onto `tail.next`, and advance that list's pointer. When one
list runs out, splice the *entire remaining tail* of the other list on
directly (no need to keep stepping node by node -- it's already sorted).

Why the dummy head matters: without it, you'd need an if/else to handle
"is this the very first node" separately from every subsequent node. The
dummy absorbs that case for free.

=========================
Complexity
=========================
Time:  O(n + m) -- visit every node of both lists exactly once.
Space: O(1) extra -- you're re-linking existing nodes, not allocating new
       ones. (Contrast with the recursive version below: that one is
       O(n + m) call-stack space.)
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode(-1)
        tail = dummy

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 if list1 is not None else list2
        return dummy.next

    # Recursive version -- elegant but O(n+m) stack space, worth mentioning
    # as a tradeoff if asked for an alternative.
    def mergeTwoListsRecursive(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val <= list2.val:
            list1.next = self.mergeTwoListsRecursive(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoListsRecursive(list1, list2.next)
            return list2


if __name__ == "__main__":
    def build(vals):
        dummy = ListNode(-1)
        cur = dummy
        for v in vals:
            cur.next = ListNode(v)
            cur = cur.next
        return dummy.next

    def to_list(node):
        out = []
        while node:
            out.append(node.val)
            node = node.next
        return out

    sol = Solution()
    print(to_list(sol.mergeTwoLists(build([1, 2, 4]), build([1, 3, 4]))))
    # [1, 1, 2, 3, 4, 4]


"""
=========================
Google-asked variations (2-3)
=========================

1. Merge k Sorted Lists (LeetCode 23, Hard)
   "Merge k linked lists instead of 2." Direct generalization -- the naive
   approach folds this pairwise (merge list 1&2, then merge that with 3,
   etc., O(kn) per merge), but the efficient approach uses a min-heap of
   size k (or divide-and-conquer pairwise merging, O(n log k) total). This
   is one of Google's most commonly cited "easy problem, hard follow-up"
   pairs.

2. Sort List (LeetCode 148, Medium)
   "Sort a linked list in O(n log n) time and O(1) space." Requires
   implementing merge sort *on* a linked list -- the merge step is exactly
   this problem, but you also need to implement the split step (find the
   middle via slow/fast pointers, recursively sort each half). Tests
   whether you can compose this problem as a subroutine inside a bigger
   algorithm.

3. Merge Two Sorted Arrays In-Place (LeetCode 88, Easy)
   "Same merge idea, but on two sorted arrays where one has extra trailing
   space to merge into in-place." Same two-pointer merge logic, but the
   array version is usually solved by merging from the *back* (largest
   first) to avoid overwriting unprocessed elements -- a good check for
   whether you understand *why* the linked-list version doesn't need that
   trick (no overwrite risk when you're just relinking pointers).
"""
