import datetime
import random
import time


def quick_sort(nums, begin, end):
    if begin < end:
        partition_index = rand_partition(nums, begin, end)
        quick_sort(nums, begin, partition_index - 1)
        quick_sort(nums, partition_index + 1, end)


def rand_partition(nums, begin: int, end: int) -> int:
    i = random.randint(begin, end)
    nums[i], nums[end] = nums[end], nums[i]

    partition_num = nums[end]
    i = begin - 1
    for j in range(begin, end):
        if nums[j] <= partition_num:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]

    nums[i + 1], nums[end] = nums[end], nums[i + 1]

    return i + 1