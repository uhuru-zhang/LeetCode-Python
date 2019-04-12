class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k >= len(num):
            return "0"

        j = 0
        num = list(num)

        for i in range(k):
            while j < len(num) - 1 and num[j] <= num[j + 1]:
                j += 1

            num.pop(j)
            j = max(0, j - 1)

        while len(num) > 0 and num[0] == "0":
            num.pop(0)

        if len(num) == 0:
            return "0"
        return "".join(num)


