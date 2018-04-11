# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        node = headA
        L1 = []
        while node:
            L1.append(node.val)
            node = node.next
        node = headB
        L2 = []
        while node:
            L2.append(node.val)
            node = node.next

        l1 = len(L1)
        l2 = len(L2)
        i = l1 - 1
        j = l2 - 1
        while i >= 0 and j >= 0:
            if L1[i] == L2[j]:
                i -= 1
                j -= 1
            else:
                break

        j = 0
        node = headA
        while j <= i:
            node = node.next
            j += 1
        return node


