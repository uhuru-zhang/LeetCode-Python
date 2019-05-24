# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        result = None
        while head is not None:
            tmp = head
            head = head.next

            tmp.next = result
            result = tmp

        return result