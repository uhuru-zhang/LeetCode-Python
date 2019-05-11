class Solution:
    def subsets(self, nums: list) -> list:
        if len(nums) == 0:
            return [[]]

        if len(nums) == 1:
            return [[nums[0]], []]

        result = []
        next_result = self.subsets(nums[1:])

        for r in next_result:
            result.append([nums[0]] + r)
            result.append(r)

        return result