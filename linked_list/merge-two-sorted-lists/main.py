# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        if l1.val < l2.val:
            result = ListNode(l1.val)
            l1 = l1.next
        else:
            result = ListNode(l2.val)
            l2 = l2.next

        current = result
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                current.next = ListNode(l1.val)
                l1 = l1.next
            else:
                current.next = ListNode(l2.val)
                l2 = l2.next

            current = current.next

        if l1 is None:
            current.next = l2
            return result
        if l2 is None:
            current.next = l1
            return result