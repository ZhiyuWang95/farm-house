"""
Problem: Linked List Cycle II
Link: https://leetcode.com/problems/linked-list-cycle-ii/
Topic: Linked List (fast/slow pointers)
Difficulty: Medium

=========================
Explanation
=========================
Floyd's Cycle Detection ("tortoise and hare"), in two phases.

Phase 1 -- detect whether a cycle exists:
Move `slow` one step at a time, `fast` two steps at a time. If there's no
cycle, `fast` hits None and you return null. If there IS a cycle, `slow`
and `fast` are guaranteed to meet *somewhere inside* the cycle (fast laps
slow eventually, since it gains 1 net step on slow per iteration while
both are inside a cycle).

Phase 2 -- find WHERE the cycle starts (the actual ask of this problem):
This is the part people memorize without understanding -- here's the proof
so you can derive it live in an interview instead of just reciting it.

Let:
  a = distance from head to the cycle's start node
  b = distance from the cycle's start node to the meeting point (phase 1)
  c = total length of the cycle

When slow and fast meet:
  slow has traveled:  a + b
  fast has traveled:  a + b + k*c   (it lapped the cycle k extra times)

fast always travels exactly 2x what slow travels (2 steps per 1 step), so:
  2*(a + b) = a + b + k*c
  a + b = k*c
  a = k*c - b = (k-1)*c + (c - b)

Read the last line as: "the distance from head to the cycle start (a) is
the same as the distance from the meeting point forward to the cycle start
(c - b), plus zero or more full laps of the cycle ((k-1)*c)."

That means: if you place one pointer at `head` and leave the other at the
`meeting point` from phase 1, and advance BOTH one step at a time, they
will arrive at the cycle's start node at exactly the same time -- because
"a steps from head" and "(c-b) steps + full laps from the meeting point"
land on the same node.

This is why the algorithm is just: detect the meeting point with
slow/fast, then reset one pointer to head and walk both one step at a time
until they meet again -- that second meeting point IS the cycle start.

=========================
Complexity
=========================
Time:  O(n) -- each phase is linear; fast/slow meeting takes at most one
       full lap of the list+cycle.
Space: O(1) -- only two pointers, no extra data structure. This satisfies
       the problem's explicit O(1) memory follow-up (the "obvious" approach
       of storing visited nodes in a hash set is O(n) space).
"""

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        # Phase 1: does a cycle exist, and where do slow/fast first meet?
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                break
        else:
            return None  # fast ran off the end -- no cycle

        # Phase 2: find the start of the cycle.
        slow = head
        while slow is not fast:
            slow = slow.next
            fast = fast.next
        return slow

    # O(n) space alternative -- simpler to state, good to mention as the
    # "obvious" baseline before optimizing to Floyd's.
    def detectCycleHashSet(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = set()
        node = head
        while node is not None:
            if node in seen:
                return node
            seen.add(node)
            node = node.next
        return None


if __name__ == "__main__":
    # Build [3,2,0,-4] with tail (-4) pointing back to node index 1 (val 2)
    n1, n2, n3, n4 = ListNode(3), ListNode(2), ListNode(0), ListNode(-4)
    n1.next, n2.next, n3.next, n4.next = n2, n3, n4, n2
    sol = Solution()
    print(sol.detectCycle(n1).val)  # 2


"""
=========================
Google-asked variations (2-3)
=========================

1. Linked List Cycle (LeetCode 141, Easy)
   "Just return True/False -- does a cycle exist?" The phase-1-only version
   of this problem. Frequently asked as a 5-minute warm-up before Google
   escalates to "now find WHERE it starts" (this problem).

2. Happy Number (LeetCode 202, Easy)
   "Determine if repeatedly summing the squares of a number's digits
   eventually reaches 1, or loops forever." There's no explicit linked
   list here, but the sequence of digit-sum transformations forms an
   implicit "linked list" (each number points to the next), and detecting
   whether it loops is literally Floyd's cycle detection again. A good
   test of whether you recognize the *pattern* of cycle detection outside
   of an explicit list structure -- a classic Google move (disguise a
   known pattern in an unfamiliar wrapper).

3. Find the Duplicate Number (LeetCode 287, Medium)
   "Given an array of n+1 integers where each is in [1,n], find the
   duplicate, in O(1) space and without modifying the array." Treat the
   array as an implicit linked list where index i "points to" index
   nums[i] -- the duplicate value creates a cycle, and the cycle's
   entry point IS the duplicate number. Same exact two-phase Floyd's
   algorithm, just applied to an array-as-graph instead of literal nodes.
   This is one of the most-cited "secretly the same problem" pairs in
   Google interview prep.
"""
