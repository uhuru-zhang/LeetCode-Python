class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        secondHalfHead = self.getSecondHalfHead(head)
        reversedSecondHalfHead = self.reverseLinkedList(secondHalfHead)
        if head == None or head.next == None:
            return True
        cur1 = head
        cur2 = reversedSecondHalfHead
        while cur2 != None:
            if cur1.val != cur2.val:
                return False
            cur1 = cur1.next
            cur2 = cur2.next
        return True

    def getSecondHalfHead(self, head):
        qP = head
        sP = head
        if head == None:
            return None
        if head.next == None:
            return head
        while qP != None and qP.next != None:
            sP = sP.next
            qP = qP.next.next
        return sP

    def reverseLinkedList(self, head):
        if head is None:
            return None
        reversedHead = head
        notReversedHead = head.next
        helper = head.next
        if notReversedHead == None:
            return head
        reversedHead.next = None
        while notReversedHead != None:
            notReversedHead = notReversedHead.next
            helper.next = reversedHead
            reversedHead = helper
            helper = notReversedHead
        return reversedHead
