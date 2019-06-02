# 带有剪枝的搜索 超时
# import sys
#
#
# class Solution:
#     def __init__(self):
#         self.jumps = []
#
#     def jump(self, nums: list) -> int:
#         self.nums = nums
#         self.jumps = [-1 for _ in nums]
#         return self.jumps[0]
#
#     def _can_jump(self, i):
#         if len(self.nums) <= i + 1:
#             self.jumps[i] = 0
#             return 0
#         if self.nums[i] >= len(self.nums) - 1 - i:
#             self.jumps[i] = 1
#             return 1
#         if self.nums[i] == 0:
#             return sys.maxsize
#
#         result = sys.maxsize
#         for j in reversed(range(self.nums[i])):
#             if self.jumps[i + j + 1] == -1:
#                 result = min(result, 1 + self._can_jump(i + j + 1))
#             else:
#                 result = min(result, 1 + self.jumps[i + j + 1])
#         self.jumps[i] = result


# 贪心算法 首先设定一个 一定会到达的点
#   第一个点为位置0 那么首先步数加一
#   同时向前寻找第二个跳跃位置的点，第二个跳跃位置的点肯定在 第一个跳跃点 至 第一个跳跃位置的点可以到达的最远点之间（左开右闭区间）
#   并且这个区间内只可能存在一个最短的跳跃点，如果存在两个那么跳跃最远的那个将被选中 这是互相矛盾的
#   所以在第二次到达 reach 的时候有且只有一个 next_reach 会被选出来
#   这样不停地迭代 直到 next_reach 超过数组长度 算法结束
class Solution:
    def jump(self, nums: list) -> int:
        if len(nums) <= 1:
            return 0
        reach, next_reach, step = 0, nums[0], 0

        for i, n in enumerate(nums):
            next_reach = max(i + nums[i], next_reach)
            if next_reach >= len(nums) - 1:
                return step + 1

            if i == reach:
                step += 1
                reach = next_reach

        return step