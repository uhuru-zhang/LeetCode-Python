"""
https://leetcode-cn.com/problems/3sum-closest/submissions/
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).



"""
class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        nums.sort()
        res = float("inf")
        ans = float("inf")
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if abs(s - target) < res:
                    res, ans = abs(s - target), s
                if s > target:
                    k -= 1
                elif s < target:
                    j += 1
                else:
                    return s
        return ans