# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        self.answer = 1
        self.depth(root)
        return self.answer-1




    def depth(self,node):
        if node == None:
            return 0
        L = self.depth(node.left)
        R = self.depth(node.right)
        self.answer = max(self.answer,L+R+1)
        return max(L,R)+1







        """
        :type root: TreeNode
        :rtype: int
        """