# import math
#
#   动态规划 + 搜索 ==> 超时
# class Solution:
#     def __init__(self):
#         self.num_dict = {1: 1,
#                          2: 2,
#                          3: 3}
#
#     def numSquares(self, n: int) -> int:
#         if n in self.num_dict:
#             return self.num_dict[n]
#
#         current_result = int(math.sqrt(n))
#         if (current_result + 1) ** 2 <= n:
#             current_result += 1
#
#         if current_result ** 2 == n:
#             return current_result
#
#         result = n
#         for m in reversed(range(1, current_result + 1)):
#             if n - m ** 2 not in self.num_dict:
#                 self.numSquares(n - m ** 2)
#
#             if 1 + self.num_dict[n - m ** 2] > result:
#                 break
#
#             result = 1 + self.num_dict[n - m ** 2]
#         self.num_dict[n] = result
#
#         return result

# 动态规划
# import math
import sys


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0]

        for i in range(1, n + 1):
            min_num = sys.maxsize
            j = 1
            while j ** 2 <= i:
                min_num = min(min_num, dp[i - j ** 2])
                j += 1
            dp.append(min_num + 1)
        return dp[n]

