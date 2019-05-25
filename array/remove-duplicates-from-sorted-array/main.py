class Solution:
    def removeDuplicates(self, nums: list) -> int:
        if len(nums) == 0:
            return 0
        current_index = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[current_index] = nums[i]
                current_index += 1

        return current_index
