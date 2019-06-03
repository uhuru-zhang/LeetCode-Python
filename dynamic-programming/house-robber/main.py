class Solution:
    def rob(self, nums: list) -> int:
        # 动态规划 dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        if len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return max(nums)

        dp = [nums[0], max(nums[:2])]

        for i in range(2, len(nums)):
            dp.append(max(dp[i - 1], dp[i - 2] + nums[i]))

        return dp[-1]
