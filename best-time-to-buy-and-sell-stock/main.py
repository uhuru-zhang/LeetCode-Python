class Solution:
    def maxProfit(self, prices):
        if len(prices) == 0:
            return 0
        min_ = prices[0]
        result = 0

        for i in range(1, len(prices)):
            min_ = min(min_, prices[i])
            result = max(result, prices[i] - min_)

        return result

if __name__ == '__main__':
    s = Solution()
    a = s.maxProfit([7, 1, 5, 3, 6, 4]
                    )
    print(a)
