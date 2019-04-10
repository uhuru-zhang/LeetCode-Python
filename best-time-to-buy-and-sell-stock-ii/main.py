class Solution:
    def maxProfit(self, prices):
        if len(prices) == 0:
            return 0
        min_index, max_index = -1, -1
        result = 0

        for i in range(1, len(prices)):
            if min_index == -1:
                if prices[i] > prices[i - 1]:
                    min_index = i - 1
                    max_index = i
            else:
                if prices[i] > prices[i - 1]:
                    max_index = i
                else:
                    result += prices[max_index] - prices[min_index]
                    min_index = -1

        if min_index != -1 and max_index > min_index:
            result += prices[max_index] - prices[min_index]
        return result


if __name__ == '__main__':
    s = Solution()
    a = s.maxProfit([7,1,5,3,6,4]
)
    print(a)
