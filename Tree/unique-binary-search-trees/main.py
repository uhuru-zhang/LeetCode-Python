# 动态规划
# 一维 动态规划 dp[i] 代表着 1至i 构成的子树个数 由于 i至j 的子树个数 其实是和 1至i 的子树个数是相等的 所以采用一维就可以实现
class Solution:
    def numTrees(self, n: int) -> int:
        # 该树的中序遍历结果一定是 list(range(1, n + 1))
        dp = [-1 for _ in range(n + 1)]
        dp[0] = dp[1] = 1
        self.dp = dp
        return self.num_trees(n)

    def num_trees(self, n) -> int:
        result = 0
        # 以位置 i 所在元素为根节点进行遍历
        for i in range(1, n + 1):
            if i == 1:
                left = 1
            else:
                if self.dp[i - 1] == -1:
                    self.dp[i - 1] = self.num_trees(i - 1)
                left = self.dp[i - 1]

            if i == n:
                right = 1
            else:
                if self.dp[n - i] == -1:
                    self.dp[n - i] = self.num_trees(n - 1)
                right = self.dp[n - i]

            # 结果为 左树的数目 * 右树的数目
            result += left * right
        return result


# 二维的动态规划 dp[i][j] 代表着 i至j 构成的子树的个数
# class Solution:
#     def numTrees(self, n: int) -> int:
#         # 该树的中序遍历结果一定是 list(range(1, n + 1))
#         dp = [[-1 for _ in range(n)] for _ in range(n)]
#         for i in range(n):
#             dp[i][i] = 1
#
#         self.dp = dp
#         return self.num_trees(0, n - 1)
#
#     def num_trees(self, l, r) -> int:
#         if l == r:
#             return 1
#
#         result = 0
#         # 以位置 i 所在元素为根节点进行遍历
#         for i in range(l, r + 1):
#             if i - l <= 1:
#                 left = 1
#             else:
#                 if self.dp[l][i - 1] == -1:
#                     self.dp[l][i - 1] = self.num_trees(l, i - 1)
#                 left = self.dp[l][i - 1]
#
#             if r - i <= 1:
#                 right = 1
#             else:
#                 if self.dp[i + 1][r] == -1:
#                     self.dp[i + 1][r] = self.num_trees(i + 1, r)
#                 right = self.dp[i + 1][r]
#
#             # 结果为 左树的数目 * 右树的数目
#             result += left * right
#         return result

# 深度优先搜索
# class Solution:
#     def numTrees(self, n: int) -> int:
#         return self.num_trees(list(range(1, n + 1)))
#
#     def num_trees(self, nums: list) -> int:
#         if len(nums) <= 1:
#             return 1
#
#         result = 0
#         for i in range(len(nums)):
#             left = self.num_trees(nums[:i])
#             right = self.num_trees(nums[i + 1:])
#
#             result += left * right
#         return result


if __name__ == '__main__':
    s = Solution()
    a = s.numTrees(3)
    print(a)
