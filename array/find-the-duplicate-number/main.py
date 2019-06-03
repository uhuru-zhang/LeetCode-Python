class Solution:
    def findDuplicate(self, nums: list) -> int:
        # 此题目 等价于 循环链表

        fast = slow = 0

        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]

            if fast == slow:
                fast = 0
                while nums[fast] != nums[slow]:
                    fast = nums[fast]
                    slow = nums[slow]
                return nums[slow]