# Definition for singly-linked list.
"""
https://leetcode-cn.com/problems/add-two-numbers/submissions/
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

    输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
    输出：7 -> 0 -> 8
    原因：342 + 465 = 807


"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sub = 0

        result = ListNode(0)
        a = result
        while not (l1 is None and l2 is None and sub == 0):
            num_1 = num_2 = 0

            if l1 is not None:
                num_1 = l1.val
                l1 = l1.next

            if l2 is not None:
                num_2 = l2.val
                l2 = l2.next

            result.val = (sub + num_1 + num_2) % 10
            sub = (sub + num_1 + num_2) // 10

            if not (l1 is None and l2 is None and sub == 0):
                result.next = ListNode(0)

                result = result.next
        return a


if __name__ == '__main__':
    s = Solution()
    s.addTwoNumbers(ListNode(5), ListNode(5))