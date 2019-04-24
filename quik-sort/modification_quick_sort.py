import random

"""
修复随机快排在 重复数字过多的情况下 时间复杂度 退化为 O(n^2) 的问题
"""


def quick_sort(nums, begin, end):
    if begin < end:
        partition_left, partition_right = rand_partition(nums, begin, end)
        quick_sort(nums, begin, partition_left - 1)
        quick_sort(nums, partition_right + 1, end)


def rand_partition(nums: [int], begin: int, end: int) -> (int, int):
    left = random.randint(begin, end)
    nums[left], nums[end] = nums[end], nums[left]

    partition_num = nums[end]
    left, length = begin - 1, 0
    for j in range(begin, end):
        if nums[j] < partition_num:
            left += 1

            nums[left + length], nums[j] = nums[j], nums[left + length]
            nums[left], nums[left + length] = nums[left + length], nums[left]
            # if length > 0:
            #     nums[left + length], nums[j] = nums[j], nums[left + length]
        elif nums[j] == partition_num:
            length += 1
            nums[left + length], nums[j] = nums[j], nums[left + length]

    nums[left + 1 + length], nums[end] = nums[end], nums[left + 1 + length]

    return left + 1, left + 1 + length
