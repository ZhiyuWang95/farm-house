"""
Problem: Sliding Window Maximum
Link: https://leetcode.com/problems/sliding-window-maximum/
Topic: Sliding Window
Difficulty: Hard

=========================
Explanation
=========================
A naive approach checks all k elements in each window — O(nk). A heap works but
gives O(n log n) with lazy deletion complexity. The optimal solution uses a
monotonic deque to maintain the maximum in O(1) per window.

Monotonic deque invariant: the deque stores indices in decreasing order of their
values — deque[0] is always the index of the current window's maximum.

On each new element at index i:
1. Remove from the BACK of the deque any indices whose values are ≤ nums[i].
   These can never be the maximum of any future window (nums[i] is both more
   recent and larger/equal). This keeps the deque monotonically decreasing.
2. Remove from the FRONT if the front index has fallen outside the window
   (deque[0] <= i - k).
3. Append i to the back.
4. Once i >= k-1 (first full window), record nums[deque[0]] as the window max.

Why discard from the back: a smaller element that entered earlier will always be
in the window for fewer remaining steps AND has a smaller value — it can never
win, so it's useless.
=========================
Complexity
=========================
Time:  O(n) — each index is added and removed from the deque at most once.
Space: O(k) — the deque holds at most k indices.
"""

from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()  # stores indices, decreasing by value
        result = []

        for i, num in enumerate(nums):
            while dq and nums[dq[-1]] <= num:
                dq.pop()
            dq.append(i)
            if dq[0] <= i - k:
                dq.popleft()
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))  # [3,3,5,5,6,7]
    print(sol.maxSlidingWindow([1], 1))                           # [1]
    print(sol.maxSlidingWindow([1, -1], 1))                       # [1,-1]


"""
=========================
Google-asked variations (2-3)
=========================

1. Jump Game VI (LeetCode 1696, Medium)
   "From index i jump to any j in [i+1, i+k]; each index has a score; maximize
   total score to reach the end." DP with sliding window maximum: dp[i] = max
   dp[j] for j in [i-k, i-1], plus score[i]. The monotonic deque maintains the
   max of the last k dp values in O(1). Tests whether you can embed the deque
   optimization inside a DP recurrence.

2. Longest Continuous Subarray with Absolute Diff ≤ Limit (LeetCode 1438, Medium)
   "Find the longest subarray where max - min ≤ limit." Requires TWO monotonic
   deques simultaneously — one for the sliding max and one for the sliding min —
   to check the constraint in O(1). Tests whether you can run multiple deques
   in parallel.

3. Sliding Window Median (LeetCode 480, Hard)
   "Find the median of each window of size k." Requires two heaps (max + min)
   with lazy deletion instead of a deque — median is harder to maintain
   monotonically than max/min. A good "harder sibling" after mastering the
   deque approach for maximum.
"""
