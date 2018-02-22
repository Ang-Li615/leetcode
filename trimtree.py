# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def trimBST(self, root, L, R):
        root = self.trimBSTright(root, R)
        root = self.trimBSTleft(root, L)
        return root

    def trimBSTleft(self, root, L):
        if root.val < L:
            return root.right
        else:
            root.left = self.trimBSTleft(root.left, L)
            return root

    def trimBSTright(self, root, R):
        if root.val > R:
            return root.left
        else:
            root.right = self.trimBSTright(root.right, R)
            return root

        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """