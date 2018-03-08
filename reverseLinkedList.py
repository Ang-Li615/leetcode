# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        if head == None:
            return head
        if head.next == None:
            return head
        self.reverse(head)

        head.next = None
        return self.newhead

    def reverse(self,t):
        if t.next.next != None:
            self.reverse(t.next)
        else:
            self.newhead = t.next
        t1 = t.next
        t1.val = t1.val
        t1.next = t
        return t1







        """
        :type head: ListNode
        :rtype: ListNode
        """
