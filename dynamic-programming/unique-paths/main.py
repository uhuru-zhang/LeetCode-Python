class Solution:
    # 搜索方法 时间复杂度过高
    # def uniquePaths(self, m: int, n: int) -> int:
    #     if m == 1 or n == 1:
    #         return 1
    #     return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)

    # 动态规划
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]

        # 首先 到达 位置 i, 0 和 0, i 的方式只会有一种
        for i in range(m):
            dp[i][0] = 1
        for i in range(n):
            dp[0][i] = 1

        for i in range(1, m):
            for j in range(1, n):

                # 迭代方程 到达 位置 i, j 的方式 为 到达他 左侧的方法 和 到达他上侧的方法的 二者之和
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]


if __name__ == '__main__':
    s = Solution()
    a = s.uniquePaths(m=23, n=12)
    print(a)
