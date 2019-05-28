class Solution:
    def maxProfit(self, prices, fee):
        n = len(prices)
        if n < 2:
            return 0
        buy = -prices[0]
        sell = 0

        for i in range(1, n):
            buy = max(buy, sell - prices[i])
            sell = max(sell, buy + prices[i] - fee)
        return sell
