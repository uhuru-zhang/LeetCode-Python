class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        # dp[i][j] 代表 word1 前i个字符 变为 word2 前j个字符所需要的最小操作数
        dp = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]

        for i in range(len(word1) + 1):
            dp[i][0] = i

        for i in range(len(word2) + 1):
            dp[0][i] = i

        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                temp = dp[i - 1][j - 1]
                if word1[i - 1] != word2[j - 1]:
                    temp += 1
                dp[i][j] = min(min(dp[i - 1][j] + 1, dp[i][j - 1] + 1), temp)

        return dp[len(word1)][len(word2)]
