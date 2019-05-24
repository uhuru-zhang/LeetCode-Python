# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = head
        slow = head

        while fast is not None and fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next

            if fast.val == slow.val:
                break

        if not (fast is not None and fast.next is not None and fast.next.next is not None):
            return None

        flag = head

        while flag.val != slow.val:
            flag = flag.next
            slow = slow.next
        return flag.val


if __name__ == '__main__':
    array = [3, 2, 0, -4]
    index = 1

    head = None
    current = None
    entry = None

    for i in range(len(array)):
        if head is None:
            head = ListNode(array[i])
            current = head
        else:
            current.next = ListNode(array[i])
            current = current.next

        if i == index:
            entry = current

    current.next = entry

    s = Solution()
    a = s.detectCycle(head)
    print(a)
