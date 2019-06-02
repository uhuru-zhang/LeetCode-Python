# 带有剪枝的搜索
# class Solution:
#     def __init__(self):
#         self.can_not_jumps = set()
#
#     def canJump(self, nums: list) -> bool:
#         self.nums = nums
#         return self._can_jump(0)
#
#     def _can_jump(self, i):
#         if self.nums[i] == 0:
#             return False
#         if len(self.nums) <= i + 1 or self.nums[i] >= len(self.nums) - 1 - i:
#             return True
#
#         for j in reversed(range(self.nums[i])):
#             if i + j + 1 in self.can_not_jumps:
#                 continue
#             if self._can_jump(i + j + 1):
#                 return True
#             else:
#                 self.can_not_jumps.add(i + j + 1)
#
#         return False

# 其实不用搜索，只要数组中不存在0 就一定功能到达最后
# 采用从后向前查找
class Solution:
    def canJump(self, nums: list) -> bool:
        n = 1  # n 代表距离末尾的长度

        for i in reversed(range(len(nums) - 1)):
            if nums[i] > n:
                n = 1  # 如果当前位置可以到达末尾 就重置 n 为 1 （因为只要能达到 现有位置 就能达到末尾）
            else:
                n += 1 # 如果不能 n + 1 这其实只有在 倒数第二个位置 为 0 的时候回发生
        if n > 1:
            return False
        return True
