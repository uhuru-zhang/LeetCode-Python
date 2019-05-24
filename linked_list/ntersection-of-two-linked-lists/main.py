# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA: ListNode, headB: ListNode):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        lenA = 0
        currentA = headA
        while currentA is not None:
            lenA += 1
            currentA = currentA.next

        lenB = 0
        currentB = headB
        while currentB is not None:
            lenB += 1
            currentB = currentB.next

        if lenA > lenB:
            for _ in range(lenA - lenB):
                headA = headA.next
        if lenA < lenB:
            for _ in range(lenB - lenA):
                headB = headB.next

        while headA is not None and headA.val != headB.val:
            headA = headA.next
            headB = headB.next

        return headB if headA is not None else None


def get_list(array):
    head = None
    current = None

    for i in range(len(array)):
        if head is None:
            head = ListNode(array[i])
            current = head
        else:
            current.next = ListNode(array[i])
            current = current.next
    return head


if __name__ == '__main__':
    headA = get_list([4, 1, 8, 4, 5])
    headB = get_list([5, 0, 1, 8, 4, 5])

    s = Solution()
    a = s.getIntersectionNode(headA, headB)
    print(a.val)
