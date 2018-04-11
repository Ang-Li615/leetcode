# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        else:
            root.val = 1
        self.L = []
        self.treeDepth([root])
        return min(self.L)

    def treeDepth(self, nodeList):
        L = []
        for node in nodeList:
            if node.left != None and node.right != None:
                node.left.val = node.val + 1
                L.append(node.left)
                node.right.val = node.val + 1
                L.append(node.right)
            elif node.left != None and node.right == None:
                node.left.val = node.val + 1
                L.append(node.left)
            elif node.left == None and node.right != None:
                node.right.val = node.val + 1
                L.append(node.right)
            else:
                self.L.append(node.val)

        if L != []:
            self.treeDepth(L)
