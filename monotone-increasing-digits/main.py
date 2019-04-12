class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        """
        找到下降的点，之后全部变为9
        然后向前扫面，把小于前一位的数字变为9
        :param N:
        :return:
        """
        num = str(N)
        if len(num) == 1:
            return N

        result = [-1 for _ in range(len(num))]
        result[0] = int(num[0])
        flag = True

        for i in range(1, len(num)):
            if num[i] >= num[i - 1] and flag:
                result[i] = int(num[i])
            else:
                result[i] = 9
                if flag:
                    result[i - 1] -= 1
                    flag = False
                    j = i - 1

                    while j >= 1 and result[j] < result[j - 1]:
                        result[j] = 9
                        result[j - 1] -= 1
                        j -= 1

        if result[0] == 0:
            result.pop(0)

        return int("".join(map(str, result)))