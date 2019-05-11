class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        result = []
        for i in range(1, len(num2) + 1):
            current = int(num2[-i])

            result.append(self.multiply_one(num1, current) * 10 ** (i - 1))
        return sum(result)

    def multiply_one(self, num1: str, one: int) -> int:
        sub = 0

        result = ""
        for i in range(1, len(num1) + 1):
            current = int(num1[-i])

            current_result = current * one + sub

            sub = current_result // 10
            result = str(current_result % 10) + result

        if sub != 0:
            result = str(sub) + result

        return int(result)


if __name__ == '__main__':
    s = Solution()
    print(s.multiply("23534534", "23534534"))
    print(23534534 * 23534534)
