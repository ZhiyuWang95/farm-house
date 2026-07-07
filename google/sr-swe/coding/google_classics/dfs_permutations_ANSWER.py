"""
Problem: Permutations
Link: https://leetcode.com/problems/permutations/
Topic: DFS (backtracking, non-grid)
Difficulty: Medium

=========================
Explanation
=========================
This is the "pure" backtracking template with no grid and no target sum
to prune against -- worth contrasting with Word Search (grid-constrained
DFS) and Combination Sum (sum-constrained DFS) to see how the same
mark/recurse/unmark skeleton adapts to different constraints.

Maintain a `current` list (the permutation being built) and a `used`
boolean array tracking which indices of `nums` are already placed in
`current`. At each recursive call:
  - Base case: if len(current) == len(nums), every element has been
    placed -- append a COPY of `current` to the result (a copy matters --
    appending the list reference itself would later be mutated by
    backtracking and corrupt the stored answer).
  - Otherwise, try every index i not yet used: mark it used, append
    nums[i] to current, recurse, then UNDO both (pop from current, mark
    i unused again) before trying the next index -- this "undo" step is
    what lets the same index be available again on a different branch of
    the search tree.

Alternative implementation some interviewers prefer: swap-based
in-place permutation generation (swap the element at the current
position with each candidate, recurse, swap back) -- avoids the `used`
array entirely, at the cost of mutating/restoring the input array. Both
are O(1) extra space beyond the output and recursion stack; the
used-array version above is usually easier to explain out loud.

=========================
Complexity
=========================
Time:  O(n! * n) -- n! permutations total, each costing O(n) to copy into
       the result.
Space: O(n) for the recursion depth and `used` array (excluding the
       O(n! * n) output itself).
"""

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        used = [False] * len(nums)
        current = []

        def backtrack():
            if len(current) == len(nums):
                result.append(current[:])  # copy! current keeps mutating
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                current.append(nums[i])
                backtrack()
                current.pop()
                used[i] = False

        backtrack()
        return result

    # Swap-based alternative -- no `used` array, mutates nums in place.
    def permuteSwap(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(start: int):
            if start == len(nums):
                result.append(nums[:])
                return
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]  # swap back

        backtrack(0)
        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.permute([1, 2, 3]))
    print(sol.permuteSwap([0, 1]))


"""
=========================
Google-asked variations (2-3)
=========================

1. Permutations II (LeetCode 47, Medium)
   "Input may contain duplicates; return all UNIQUE permutations." Sort
   `nums` first, then add a dedup guard at each recursion level:
   skip index i if nums[i] == nums[i-1] AND nums[i-1] hasn't been used in
   the current branch (used[i-1] is False) -- this specific condition
   ("not used" rather than "used") is the subtle part that prevents
   both under-counting and over-counting duplicate permutations. One of
   the most commonly botched dedup conditions in all of backtracking.

2. Next Permutation (LeetCode 31, Medium)
   Deliberately NOT a backtracking problem -- a great contrast question.
   Given one permutation, find the next one in lexicographic order using
   an O(n) in-place algorithm (find the rightmost ascent, swap with the
   smallest larger element to its right, reverse the suffix). Tests
   whether you reach for backtracking out of habit when a more targeted
   O(n) technique exists for a differently-shaped "permutation" question.

3. Letter Case Permutation (LeetCode 784, Medium)
   "Given a string with letters and digits, return all strings that can
   be formed by changing the case of each letter." Simpler binary-choice
   backtracking (at each letter position: branch into lowercase OR
   uppercase) rather than this problem's "choose-from-remaining-pool"
   branching -- good for confirming you understand backtracking as a
   general decision-tree exploration, not specifically tied to
   "rearranging a fixed multiset."
"""
