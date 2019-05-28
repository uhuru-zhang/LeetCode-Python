class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        i, j = 1, 2

        for _ in range(2, n):
            i, j = j, i + j

        return j