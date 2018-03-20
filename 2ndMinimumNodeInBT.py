# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root):
        if root == None:
            return -1
        self.s = set()
        self.s.add(root.val)
        self.findValue([root])
        L = list(self.s)
        LL = sorted(L)
        if len(LL) <= 1:
            return -1
        else:
            return LL[1]

    def findValue(self, list0fLevel):
        level = []
        for node in list0fLevel:
            if node.left != None:
                level.append(node.left)
            if node.right != None:
                level.append(node.right)

        if level != []:
            for node in level:
                self.s.add(node.val)
            self.findValue(level)

        """
        :type root: TreeNode
        :rtype: int
        """
