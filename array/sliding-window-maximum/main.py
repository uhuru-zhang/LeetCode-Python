class Solution:
    def maxSlidingWindow(self, nums: list, k: int) -> list:
        if len(nums) == 0 or k == 0 or len(nums) < k:
            return []

        result = []
        queue = []

        for i in range(len(nums)):
            # 保证队列中的值 永远是 自大到小排列的
            while len(queue) > 0 and nums[i] >= nums[queue[-1]]:
                queue.pop()
            queue.append(i)
            # 如果边界值超出范围则删除
            if i - queue[0] >= k:
                queue.pop(0)

            if i - k + 1 >= 0:
                result.append(nums[queue[0]])

        return result
