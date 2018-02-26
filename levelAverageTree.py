# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def averageOfLevels(self, root):
        self.avgList = []
        self.avgList.append(root.val)
        self.average([root])
        return self.avgList

    def average(self, l):
        L = []
        for e in l:
            if e != None:
                L.append(e.left)
                L.append(e.right)
        sum = 0
        j = 0
        for i in L:
            if i != None:
                j = j + 1
                sum = sum + i.val
        if j != 0:
            avg = 1.0 * sum / j
            self.avgList.append(avg)
            return self.average(L)
        else:
            pass


