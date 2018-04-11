# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        node = head
        L = []
        while node:
            L.append(node.val)
            node = node.next
        l = len(L)
        i = 0
        j = l-1
        while i < j:
            if L[i] == L[j]:
                i += 1
                j -= 1
                continue
            else:
                return False
        return True