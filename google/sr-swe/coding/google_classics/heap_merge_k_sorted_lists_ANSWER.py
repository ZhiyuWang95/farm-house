"""
Problem: Merge K Sorted Lists
Link: https://leetcode.com/problems/merge-k-sorted-lists/
Topic: Heap
Difficulty: Hard

=========================
Explanation
=========================
Merging two sorted lists is O(n). Naively merging k lists one by one is
O(k * n) where n is total nodes — the first merge touches n/k + n/k nodes, but
by the last merge we're touching n nodes per step, giving O(k * n) total.

Better: use a min-heap. Push the head of each non-empty list onto the heap.
Repeatedly pop the minimum node, append it to the result, then push that node's
next (if it exists) onto the heap. This is the k-way merge from Design Twitter's
getNewsFeed — the same algorithm.

The heap always holds at most k nodes (one per list), so heap operations are
O(log k). We process n total nodes, giving O(n log k).

Gotcha in Python: ListNode objects aren't directly comparable. Store tuples
(val, index, node) where index breaks ties — ensures a total ordering without
comparing node objects.
=========================
Complexity
=========================
Time:  O(n log k) where n = total nodes across all lists, k = number of lists.
Space: O(k) for the heap.
"""

from typing import List, Optional
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode()
        curr = dummy
        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next


def make_list(vals):
    dummy = ListNode()
    curr = dummy
    for v in vals:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


def list_to_arr(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


if __name__ == "__main__":
    sol = Solution()
    lists = [make_list([1, 4, 5]), make_list([1, 3, 4]), make_list([2, 6])]
    print(list_to_arr(sol.mergeKLists(lists)))  # [1,1,2,3,4,4,5,6]
    print(list_to_arr(sol.mergeKLists([])))     # []


"""
=========================
Google-asked variations (2-3)
=========================

1. Design Twitter — getNewsFeed (LeetCode 355, Medium)
   The news feed merge is exactly k-way merge: each followee's tweet list is
   one sorted stream; merge them with a heap to get the top 10 globally. Same
   algorithm, new framing.

2. Merge K Sorted Arrays
   Same heap approach — no linked list pointer chasing, just array indices.
   Often asked in Google system design context: "you have k sorted files on
   disk, merge them into one sorted output with limited memory." The heap-based
   k-way merge is the answer — process one element at a time, never load all
   k files into memory at once.

3. Smallest Range Covering Elements from K Lists (LeetCode 632, Hard)
   "Find the smallest range [a,b] such that at least one number from each of
   the k lists falls in [a,b]." Uses the same k-way merge heap, but tracks the
   current range [min_in_heap, current_max] and slides the window by advancing
   the list with the current minimum. The hardest heap problem in this family.
"""
