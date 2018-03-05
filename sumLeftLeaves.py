# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root):
        if root == None:
            return 0
        else:
            self.L = []
            self.levelList([root])
            s = sum(self.L)
            return s

    def levelList(self, l):
        L = []
        for i in l:
            if i.left != None:
                L.append(i.left)
                if i.left.left == None and i.left.right == None:
                    self.L.append(i.left.val)
            if i.right != None:
                L.append(i.right)
        if L != []:
            return self.levelList(L)