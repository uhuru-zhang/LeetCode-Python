# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def __init__(self):
        self.last_n_1 = None

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        self.get_last_n_1(head, n)

        if self.last_n_1 is None:
            return head.next
        self.last_n_1.next = self.last_n_1.next.next

        return head

    # 获得 倒数 n + 1 个节点 如果练笔哦长度只有 n 那么 就 设为None
    def get_last_n_1(self, head: ListNode, n: int) -> int:
        if head is None:
            return 0

        l = self.get_last_n_1(head.next, n)

        if l == n:
            self.last_n_1 = head
            return n + 1
        return l + 1
