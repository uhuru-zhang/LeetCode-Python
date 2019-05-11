class Solution:
    def permute(self, nums: list) -> list:
        result = []

        if len(nums) == 1:
            return [nums]

        for i in range(len(nums)):
            for r in self.permute(nums[:i] + nums[i + 1:]):
                result.append([nums[i]] + r)
        return result
if __name__ == '__main__':
    s = Solution()
    print(s.permute([1, 2, 3]))
