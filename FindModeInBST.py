# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        self.L = []
        self.checkLevel([root])
        dict = {i: 0 for i in self.L}
        for i in self.L:
            dict[i] += 1
        m = 0
        L = []
        for key in dict:
            L.append(dict[key])
        m = max(L)
        newL = []
        for key in dict:
            if dict[key] == m:
                newL.append(key)
        return newL

    def checkLevel(self, nodeList):
        L = []
        for node in nodeList:
            if node != None:
                self.L.append(node.val)
                L.append(node.left)
                L.append(node.right)
        if L != []:
            self.checkLevel(L)





