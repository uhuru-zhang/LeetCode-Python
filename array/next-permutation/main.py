import sys


class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:
            return

        max_r = nums[-1]
        min_l_index = -1
        # 找到第一个这样的位置 i 使得 位置i 之后的字符存在大于 位置i 处的字符
        for i in reversed(range(0, len(nums) - 1)):
            if nums[i] < max_r:
                min_l_index = i
                break
            max_r = max(nums[i], max_r)

        # 如果此位置为 开始（此时一定为倒序排列） 则将数组逆转
        if min_l_index == -1:
            nums.reverse()

        # 否则找到位置 i 之后位置的最小值 将最小值和i位置的数值置换
        else:
            min_dis = sys.maxsize
            min_r_index = -1
            for i in range(min_l_index + 1, len(nums)):
                if 0 < nums[i] - nums[min_l_index] <= min_dis:
                    min_r_index = i

            nums[min_l_index], nums[min_r_index] = nums[min_r_index], nums[min_l_index]

            # 之后再进行排序使得 位置 i 之后按照升序排列
            nums[min_l_index + 1:] = sorted(nums[min_l_index + 1:])
        print(nums)


if __name__ == '__main__':
    s = Solution()
    s.nextPermutation([2, 3, 1])
