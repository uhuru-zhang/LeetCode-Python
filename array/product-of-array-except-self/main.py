from functools import reduce


class Solution:
    def productExceptSelf(self, nums):
        left = 1
        result = []

        # 将位置i 左侧的累乘 放在位置i
        for n in nums:
            result.append(left)
            left *= n

        right = 1

        # 将位置i 右侧的累乘 乘以位置i 现有的数据
        for i in range(1, len(nums) + 1):
            result[-i] *= right
            right *= nums[-i]

        return result