from functools import reduce


class Solution:
    def productExceptSelf(self, nums):
        left = 1
        result = []

        for n in nums:
            result.append(left)
            left *= n

        right = 1

        for i in range(1, len(nums) + 1):
            result[-i] *= right
            right *= nums[-i]

        return result