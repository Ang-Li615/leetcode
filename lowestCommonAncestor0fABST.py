# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if root == None:
            return None
        if p.val == root.val:
            t = p
        if q.val == root.val:
            t = q
        if p.val < root.val and root.val < q.val:
            t = root
        if q.val < root.val and root.val < p.val:
            t = root
        if p.val < root.val and q.val < root.val:
            self.lowestCommonAncestor(root.left,p,q)
        if p.val > root.val and q.val > root.val:
            self.lowestCommonAncestor(root.right,p,q)
        return t







        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
