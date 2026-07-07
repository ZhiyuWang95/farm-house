"""
Problem: Reorganize String
Link: https://leetcode.com/problems/reorganize-string/
Topic: Heap
Difficulty: Medium

=========================
Explanation
=========================
If any character appears more than ceil(n/2) times, it's impossible — you'd be
forced to place it adjacent to itself. Otherwise a valid arrangement always exists.

Greedy: at each position, place the most frequent remaining character that isn't
the same as the last placed character. A max-heap gives us the most frequent
character in O(log 26) = O(1).

Algorithm: count frequencies, push (-count, char) onto a max-heap. At each step,
pop the most frequent char. If it's the same as the last placed char, pop the
second most frequent instead (then push the first back). Append the chosen char
and decrement its count; push back if count > 0.

Simpler implementation: always pop the top two from the heap simultaneously —
place both (most frequent first, then second most frequent), decrement counts,
push back. This avoids the "same as last" check entirely.
=========================
Complexity
=========================
Time:  O(n log 26) = O(n) — n characters to place, heap over at most 26 entries.
Space: O(26) = O(1) for the heap; O(n) for the output string.
"""

import heapq
from collections import Counter


class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        max_heap = [(-freq, char) for char, freq in count.items()]
        heapq.heapify(max_heap)
        result = []
        prev_freq, prev_char = 0, ""

        while max_heap:
            freq, char = heapq.heappop(max_heap)
            result.append(char)
            if prev_freq < 0:
                heapq.heappush(max_heap, (prev_freq, prev_char))
            prev_freq, prev_char = freq + 1, char

        result_str = "".join(result)
        return result_str if len(result_str) == len(s) else ""


if __name__ == "__main__":
    sol = Solution()
    print(sol.reorganizeString("aab"))    # "aba"
    print(sol.reorganizeString("aaab"))   # ""
    print(sol.reorganizeString("vvvlo"))  # "vlvov" or similar


"""
=========================
Google-asked variations (2-3)
=========================

1. Task Scheduler (LeetCode 621, Medium)
   The general version: same character must be at least n positions apart (not
   just 1). Reorganize String is Task Scheduler with n=1. The same max-heap +
   cooldown-queue simulation handles both — just parameterize the gap.

2. Rearrange String k Distance Apart (LeetCode 358, Hard)
   "Same as Reorganize String but any repeated character must be at least k
   positions apart." Requires a cooldown queue (like Task Scheduler) rather
   than just tracking the previous character. Tests whether you can generalize
   the n=1 greedy to arbitrary k.

3. Distant Barcodes (LeetCode 1054, Medium)
   "Rearrange barcodes so no two adjacent barcodes are the same." Identical to
   Reorganize String with different variable names. A common "recognize the
   same problem in disguise" test.
"""
