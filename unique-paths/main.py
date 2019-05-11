class Solution:
    # def uniquePaths(self, m: int, n: int) -> int:
    #     num = 0
    #     queue = [(0, 0)]
    #
    #     while len(queue) > 0:
    #         if queue[0] == (m - 1, n - 1):
    #             num += 1
    #         father = queue.pop(0)
    #
    #         if father[0] < m - 1:
    #             queue.append((father[0] + 1, father[1]))
    #         if father[1] < n - 1:
    #             queue.append((father[0], father[1] + 1))
    #     return num
    # def uniquePaths(self, m: int, n: int) -> int:
    #     if m == 1 or n == 1:
    #         return 1
    #     return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for i in range(n):
            dp[0][i] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]


if __name__ == '__main__':
    s = Solution()
    a = s.uniquePaths(m=23, n=12)
    print(a)
