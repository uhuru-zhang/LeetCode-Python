class Solution:
    def maximalSquare(self, matrix: list) -> int:
        if not matrix or not matrix[0]:
            return 0
        nums = [int(''.join(row), base=2) for row in matrix]
        ans, N = 0, len(nums)

        # i 为高度的起始位置
        for i in range(N):
            j, num = i, nums[i]

            # j 为高度的终止位置
            while j < N:
                # 长方形的宽度就是将高度所在的所有行进行 & 操作 如果结果不为零说明至少有一列是全为 1 的
                num = num & nums[j]
                if not num:
                    break

                # l 为最长宽度
                l, curnum = 0, num

                # 假设最长宽度为 l 则至多有连续 l 个位置为1 第 l+1 个位置为 0 此时，连续 & l + 1 次时 就会导致所有的 1 都变成 0
                while curnum:
                    l += 1
                    curnum = curnum & (curnum << 1)
                # 取最大值
                ans = max(ans, min(l, (j - i + 1)) ** 2)
                j += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    a = s.maximalRectangle(
        [
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"]
        ]
    )
    print(a)
