class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        while head and head.val == val:
            head = head.next
        node = head
        while node and node.next:
            while node.next and node.next.val == val:
                node.next = node.next.next
            node = node.next
        return head