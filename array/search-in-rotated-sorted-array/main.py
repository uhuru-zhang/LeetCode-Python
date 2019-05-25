class Solution:
    def search(self, nums: list, target: int) -> int:
        if len(nums) == 0:
            return -1
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            elif nums[0] > target:
                if nums[middle] >= nums[0]:
                    left = middle + 1
                else:
                    if nums[middle] < target:
                        left = middle + 1
                    else:
                        right = middle - 1
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
