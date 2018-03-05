# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root):
        if root == None:
            return 0
        self.L = []
        self.getValue([root])
        L = sorted(self.L)
        n = len(L)
        if n == 1:
            return 0
        t = L[1] - L[0]
        for i in range(1,n-1):
            t = min(L[i+1] - L[i],t)
        return t

    def getValue(self,L):
        l = []
        for i in L:
            self.L.append(i.val)
            if i.left != None:
                l.append(i.left)
            if i.right != None:
                l.append(i.right)
        if l != []:
            return self.getValue(l)