# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        current = head
        current_next = head.next

        current.next = current_next.next
        head = current_next
        head.next = current

        current = head.next
        while current is not None and current.next is not None and current.next.next is not None:
            current_next = current.next
            current.next = current.next.next
            current_next.next = current.next.next
            current.next.next = current_next

            current = current.next.next

        return head
