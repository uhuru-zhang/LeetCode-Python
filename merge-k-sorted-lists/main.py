# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: list) -> ListNode:
        nums = []
        for node in lists:
            while node is not None:
                nums.append(node.val)
                node = node.next
        if len(nums) == 0:
            return None

        nums = sorted(nums)

        result = ListNode(nums[0])
        current = result
        nums.pop(0)

        for n in nums:
            current.next = ListNode(n)
            current = current.next
        return result