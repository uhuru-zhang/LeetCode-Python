import math


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        return x == self.reverse(x)

    def reverse(self, x: int) -> int:
        result = 0
        flag = True if x < 0 else False
        x = int(math.fabs(x))

        while x != 0:
            a = x % 10
            x //= 10

            result = result * 10 + a

        if not (-2 ** 31 <= result <= 2 ** 31 - 1):
            return 0
        return -result if flag else result
