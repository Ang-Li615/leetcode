# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root):
        self.invert(root)
        return root




    def invert(self,root):
        if root != None:
            t = root.left
            root.left = root.right
            root.right = t
        else:
            return 0

        if root.left != None:
            self.invert(root.left)
        if root.right != None:
            self.invert(root.right)