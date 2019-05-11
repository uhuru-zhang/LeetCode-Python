# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if k == 0 or head is None or head.next is None:
            return head

        n = 0
        current = head

        while current is not None:
            current = current.next
            n += 1

        k = k % n

        if k == 0:
            return head

        current = head
        for _ in range(n - k - 1):
            current = current.next

        new_head = current.next
        current.next = None

        current = new_head
        while current.next is not None:
            current = current.next

        current.next = head

        return new_head