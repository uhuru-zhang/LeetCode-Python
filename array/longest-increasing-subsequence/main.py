class Solution:
    def increasingTriplet(self, nums: list) -> bool:
        m_l = 0
        # dp[i]: 所有长度为i+1的递增子序列中, 最小的那个序列尾数.
        # 由定义知dp数组必然是一个递增数组, 可以用 maxL 来表示最长递增子序列的长度.
        # 对数组进行迭代, 依次判断每个数num将其插入dp数组相应的位置:
        #   1. num > dp[maxL], 表示num比所有已知递增序列的尾数都大, 将num添加入dp数组尾部, 并将最长递增序列长度maxL加1
        #   2. dp[i-1] < num <= dp[i], 只更新相应的dp[i]

        dp = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            l, h = 0, m_l
            while l < h:
                # 二分法查找, 也可以调用库函数如binary_search
                mid = (l + h) // 2
                if dp[mid] < nums[i]:
                    l = mid + 1
                else:
                    h = mid
            dp[l] = nums[i]
            if l == m_l:
                m_l += 1
        return m_l >= 3