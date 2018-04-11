# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        self.L = []
        self.checkPath(root)


    def checkPath(self, node):
        if node == None:
            return 0
        left = self.checkPath(node.left)
        right = self.checkPath(node.right)
        l = r = 0
        if node.left and node.left.val == node.val:
            l = left + 1
        if node.right and node.right.val == node.val:
            r = right + 1
        self.L.append(l + r + 1)
        return max(l, r)