# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        self.L = []
        self.obtainList(l1)
        self.obtainList(l2)
        L = sorted(self.L)
        self.l = len(L)
        if self.l == 0:
            return None
        self.i = 0
        self.n = ListNode(L[0])
        self.combine(L,self.n)
        return self.n

    def obtainList(self,l):
        if l != None:
            self.L.append(l.val)
            self.obtainList(l.next)

    def combine(self,L,n):
        if self.i < self.l - 1:
            self.i += 1
            m = ListNode(L[self.i])
            n.next = m
            self.combine(L,m)
        else:
            n.next = None