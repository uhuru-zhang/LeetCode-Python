class Solution:
    def maxProfit(self, prices):
        result = 0
        for i in range(0, len(prices) - 1):
            if prices[i + 1] > prices[i]:
                result += prices[i + 1] - prices[i]

        return result


if __name__ == '__main__':
    s = Solution()
    a = s.maxProfit([1, 2, 3, 4, 5]
                    )
    print(a)
