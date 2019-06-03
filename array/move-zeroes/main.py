class Solution:
    def moveZeroes(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if 0 not in nums:
            return

        index_left = nums.index(0)

        i = index_left + 1

        while i < len(nums):
            while i < len(nums) and nums[i] == 0:
                i += 1
            if i >= len(nums) or index_left >= len(nums):
                break
            nums[index_left], nums[i] = nums[i], nums[index_left]
            index_left += 1