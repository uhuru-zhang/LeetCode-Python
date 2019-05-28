class Solution:
    def search(self, nums: list, target: int) -> int:
        if len(nums) == 0:
            return -1
        # 采用二分查找
        left, right = 0, len(nums) - 1

        while left <= right:
            # 取中间位置
            middle = (left + right) // 2

            # 如果中间位置即为目标则直接返回
            if nums[middle] == target:
                return middle
            # 如果位置 0 大于目标 则目标在小的升序序列中
            elif nums[0] > target:
                # 中间位置大于开始位置 则自开始位置到中间位置是升序 目标一定在中间位置的右侧
                if nums[middle] >= nums[0]:
                    left = middle + 1
                else:
                    # 中间位置小于开始位置 则数组中的最小值在位置0 和 中间位置之间

                    # 则 如果中间位置 小于目标 目标在中间位置右侧
                    if nums[middle] < target:
                        left = middle + 1
                    # 否则在左侧
                    else:
                        right = middle - 1
            # 如果位置 0 小于目标 则目标在大的升序序列中 其他同理
            elif nums[0] < target:
                if nums[middle] < nums[0]:
                    right = middle - 1
                else:
                    if nums[middle] < target:
                        left = middle + 1
                    else:
                        right = middle - 1
            else:
                return 0

        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.search([3, 1], 1))
