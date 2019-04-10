class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        m_l = 0
        dp = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            l, h = 0, m_l
            while l < h:
                mid = (l + h) // 2
                if dp[mid] < nums[i]:
                    l = mid + 1
                else:
                    h = mid
            dp[l] = nums[i]
            if l == m_l:
                m_l += 1
        return m_l >= 3