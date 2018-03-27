# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):

        self.checkNext(head)
        return head








    def checkNext(self,node):
        if node != None and node.next != None:
            print('ha')
            if node.val == node.next.val:
                node.next = node.next.next
                self.checkNext(node)
            else:
                self.checkNext(node.next)







        """
        :type head: ListNode
        :rtype: ListNode
        """
