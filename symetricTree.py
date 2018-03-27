# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        if root == None:
            return True
        level = self.getLevel([root])
        while level != []:
            l = len(level)
            i = 0
            j = l - 1
            while i < j:
                if level[i] == None and level[j] != None:
                    return False
                elif level[i] != None and level[j] == None:
                    return False
                elif level[i] != None and level[j] != None:
                    if level[i].val != level[j].val:
                        return False
                i += 1
                j -= 1
            level = self.getLevel(level)
        return True

    def getLevel(self,List):
        L = []
        for node in List:
            if node != None:
                L.append(node.left)
                L.append(node.right)
        return L