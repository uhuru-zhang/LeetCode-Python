class Solution:
    def sortColors(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        left, length = -1, 0

        for i in range(len(nums)):
            if nums[i] == 0:
                left += 1

                nums[left + length], nums[i] = nums[i], nums[left + length]
                nums[left], nums[left + length] = nums[left + length], nums[left]
            elif nums[i] == 1:
                length += 1
                nums[left + length], nums[i] = nums[i], nums[left + length]



        print(nums)


if __name__ == '__main__':
    s = Solution()
    nums = [2, 0, 2, 1, 1, 0]
    s.sortColors(nums)
