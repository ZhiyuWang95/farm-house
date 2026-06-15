"""
Problem: Product of Array Except Self
Link: https://leetcode.com/problems/product-of-array-except-self/
Pattern: Prefix/Suffix
Difficulty: Medium

Approach:
(write your approach/intuition here BEFORE coding)

Complexity:
Time: O(N)
Space: O(N)
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []

        left_products = self.calculate_left_products(nums)
        right_products = self.calculate_right_products(nums)

        for i in range(len(nums)):
            answer.append(left_products[i] * right_products[i])
        return answer
    
    def calculate_left_products(self, nums: List[int]) -> List[int]:
        products = []
        i = 0

        while(i < len(nums)):
            if i == 0:
                products.append(1)
            else:
                products.append(products[i-1] * nums[i-1])
            i += 1
        return products
    
    def calculate_right_products(self, nums: List[int]) -> List[int]:
        products = [1 for _ in range(len(nums))]

        i = len(nums) - 2
        while i >= 0:
            products[i] = products[i+1] * nums[i+1]
            i -= 1
        return products

    # Time: O(n), Space: O(1) extra (excluding the output array)
    def productExceptSelfOptimized(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        # Pass 1: answer[i] becomes the product of everything left of i
        for i in range(1, n):
            answer[i] = answer[i - 1] * nums[i - 1]

        # Pass 2: fold in the product of everything right of i,
        # tracked with a single running variable
        right_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]

        return answer


nums = [1,2,3,4]
print(Solution().productExceptSelf(nums))
print(Solution().productExceptSelfOptimized(nums))


# --- Notes / follow-ups discussed ---
#
