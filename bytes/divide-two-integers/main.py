import math


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend > 0 and divisor > 0:
            return self.divide_positive(dividend, divisor)
        if dividend < 0 and divisor < 0:
            return self.divide_positive(-dividend, -divisor)

        return - self.divide_positive(int(math.fabs(dividend)), int(math.fabs(divisor)))

    def divide_positive(self, dividend: int, divisor: int) -> int:
        if dividend < divisor:
            return 0

        n = 0

        while dividend - (divisor << (n + 1)) > 0:
            n += 1

        return (1 << n) + self.divide(dividend - (divisor << n), divisor)

if __name__ == '__main__':
    s = Solution()
    a = s.divide(2147483648, -1)
    print(a)