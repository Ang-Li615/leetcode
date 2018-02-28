# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        self.depth = 1
        if root == None:
            return 0
        else:
            self.count([root])
            return self.depth







    def count(self,l):
        L = []
        for e in l:
            if e.left != None:
                L.append(e.left)
            if e.right != None:
                L.append(e.right)
        if len(L) != 0:
            self.depth = self.depth + 1
            return self.count(L)






        """
        :type root: TreeNode
        :rtype: int
        """