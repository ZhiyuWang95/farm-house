"""
Problem: 3Sum
Link: https://leetcode.com/problems/3sum/
Pattern: Two Pointers
Difficulty: Medium

Approach:
(write your approach/intuition here BEFORE coding)

Complexity:
Time: O(N^2)
Space: O(n)
"""


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        answer = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            current_value = nums[i]
            target = 0 - current_value

            match_list = self.twoSum(nums, i, target)
            if len(match_list) > 0:
                for match in match_list:
                    ans_list = [current_value, *match]
                    answer.append(ans_list)
        return answer
    
    def twoSum(self, nums: list[int], index: int, target: int) -> list[list[int]]:
        result_list = []
        left = index + 1
        right = len(nums) - 1

        while(left < right):
            cur_sum = nums[left] + nums[right]
            if (cur_sum > target):
                right -= 1
            elif (cur_sum < target):
                left += 1
            else:
                result_list.append([nums[left], nums[right]])
                while(left < right and nums[left] == nums[left + 1]):
                    left += 1
                while(left < right and nums[right] == nums[right - 1]):
                    right -= 1
                left += 1
                right -= 1
        return result_list

        


nums = [-1,0,1,2,-1,-4]
print(Solution().threeSum(nums))
# --- Notes / follow-ups discussed ---
#
