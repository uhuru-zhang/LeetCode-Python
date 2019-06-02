# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = head
        slow = head
        # 两个指针一快一慢，如果在慢指针到达结尾之前 快慢指针相遇，那么就存在循环

        while fast is not None and fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next

            if fast.val == slow.val:
                return True
        return False