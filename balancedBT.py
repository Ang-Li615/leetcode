# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        return self.checkDepth(root) != -1

    def checkDepth(self,node):
        if node == None:
            return 0

        left = self.checkDepth(node.left)
        right = self.checkDepth(node.right)
        if abs(left - right) > 1 or left == -1 or right == -1:
            return -1
        else:
            return 1 + max(left,right)
