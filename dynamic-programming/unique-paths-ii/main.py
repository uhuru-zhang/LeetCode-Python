class Solution:
    # 动态规划
    def uniquePathsWithObstacles(self, obstacleGrid: list) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        if obstacleGrid[0][0] == 1 or obstacleGrid[m - 1][n - 1]  == 1:
            return 0

        for i in range(m):
            for j in range(n):
                if i == j == 0:
                    dp[i][j] = 1
                else:
                    # 迭代方程 到达 位置 i, j 的方式 为 到达他 左侧的方法 和 到达他上侧的方法的 二者之和
                    dp[i][j] = (dp[i - 1][j] if i > 0 and obstacleGrid[i - 1][j] != 1 else 0) + \
                               (dp[i][j - 1] if j > 0 and obstacleGrid[i][j - 1] != 1 else 0)

        return dp[m - 1][n - 1]


if __name__ == '__main__':
    s = Solution()
    a = s.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]])

    print(a)
