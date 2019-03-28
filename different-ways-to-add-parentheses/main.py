class Solution:
    def countDigitOne(self, n: int) -> int:
        if n < 0:
            return 0

        current, low, temp, high, i, total = 0, 0, 0, n, 1, 0

        while high != 0:
            high = n // int(10 ** i)
            temp = n % int(10 ** i)
            current = temp // int(10 ** (i - 1))
            low = temp % int(10 ** (i - 1))

            if current == 1:
                total += high * int(10 ** (i - 1)) + low + 1
            elif current > 1:
                total += (high + 1) * int(10 ** (i - 1))
            else:
                total += high * int(10 ** (i - 1))
        return total


if __name__ == '__main__':
    s = Solution()
    # a = s.PrintFromTopToBottom([1, 2, 3, 4, 5])
    print()
