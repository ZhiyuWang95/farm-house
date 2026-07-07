"""
Problem: Next Permutation
Link: https://leetcode.com/problems/next-permutation/
Topic: Array (permutation, in-place)
Difficulty: Medium

=========================
Explanation
=========================
The algorithm finds the next lexicographic permutation in O(n) with O(1) space.
Despite being in the "DFS/permutation" topic cluster, this problem is NOT solved
by backtracking — it's a direct in-place operation on the suffix.

Three-step algorithm:
1. Find the rightmost index i such that nums[i] < nums[i+1]. This is the
   "pivot" — the rightmost position where the suffix is NOT already in
   descending order (i.e., not the largest possible suffix). If no such i
   exists, the entire array is descending (largest permutation) → just reverse.

2. Find the rightmost index j > i such that nums[j] > nums[i]. This is the
   smallest number in the suffix that's larger than nums[i] — swapping them
   makes the smallest possible increase at position i.

3. Swap nums[i] and nums[j]. Then reverse the suffix nums[i+1:] to make it
   the smallest possible arrangement (it was descending, reversing makes it
   ascending).

The reverse in step 3 produces the smallest suffix after the pivot, which
combined with the swap gives the next permutation.

=========================
Complexity
=========================
Time:  O(n) — at most two linear scans and one reverse
Space: O(1) — in-place
"""

from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        i = n - 2

        # Step 1: find rightmost i where nums[i] < nums[i+1]
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            # Step 2: find rightmost j > i where nums[j] > nums[i]
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        # Step 3: reverse suffix from i+1 onward
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


if __name__ == "__main__":
    sol = Solution()

    nums = [1, 2, 3]
    sol.nextPermutation(nums)
    print(nums)  # [1, 3, 2]

    nums = [3, 2, 1]
    sol.nextPermutation(nums)
    print(nums)  # [1, 2, 3]

    nums = [1, 1, 5]
    sol.nextPermutation(nums)
    print(nums)  # [1, 5, 1]
