import sys


class Solution:
    def maxProfit(self, k, prices):
        if k <= 0 or len(prices) <= 1:
            return 0

        if k >= len(prices) / 2:
            max_ = 0
            for i in range(1, len(prices)):
                max_ += max(prices[i] - prices[i - 1], 0)
            return max_

        profits = [{"buy_profit": -sys.maxsize, "sell_profit": 0} for _ in range(k)]

        for p in prices:
            profits[0]["buy_profit"] = max(profits[0]["buy_profit"], -p)
            profits[0]["sell_profit"] = max(profits[0]["sell_profit"], profits[0]["buy_profit"] + p)

            for i in range(1, k):
                profits[i]["buy_profit"] = max(profits[i]["buy_profit"], profits[i - 1]["sell_profit"] - p)
                profits[i]["sell_profit"] = max(profits[i]["sell_profit"], profits[i]["buy_profit"] + p)

        return profits[k - 1]["sell_profit"]