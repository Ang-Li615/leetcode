# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None
#
# class Solution:
#     def convertBST(self, root):
#         if root == None:
#             return root
#
#         self.L = [root]
#         self.appendNode([root])
#         LL = []
#         for e in self.L:
#             LL.append(e.val)
#         LLL = sorted(LL)
#         for node in self.L:
#             valindex = len(LLL) - 1 - LLL[::-1].index(node.val)
#             while valindex < len(LLL):
#                 node.val += LLL[valindex]
#                 valindex += 1
#         return root
#
#     def appendNode(self,l):
#         L = []
#         for node in l:
#             if node.left != None:
#                 self.L.append(node.left)
#                 L.append(node.left)
#             if node.right != None:
#                 self.L.append(node.right)
#                 L.append(node.right)
#
#         if L != []:
#             L1 = L
#             return self.appendNode(L1)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def __init__(self):
        self.total = 0

    def convertBST(self, root):
        if root != None:
            self.convertBST(root.right)
            self.total += root.val
            root.val = self.val
            self.convertBST(root.left)
        return root