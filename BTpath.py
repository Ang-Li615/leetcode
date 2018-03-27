# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def binaryTreePaths(self, root):
#         if root == None:
#             return []
#         self.L = []
#         self.path(root,str(root.val))
#
#     def path(self,node,route):
#         if node.left != None:
#             leftpath = route + '->' + str(node.left.value)
#             return self.path(node.left,leftpath)
#         if node.right != None:
#             rightpath = route + '->' + str(node.right.value)
#             return self.path(node.right,rightpath)
#         if node.right == None and node.left == None:
#             self.L.append(route)
L = []

def binaryTreePaths(root):
    if root == None:
        return []
    path(root,str(root.val))
    return L

def path(node,route):
    if node.left != None:
        leftpath = route + '->' + str(node.left.value)
        path(node.left,leftpath)
    if node.right != None:
        rightpath = route + '->' + str(node.right.value)
        path(node.right,rightpath)
    if node.right == None and node.left == None:
        L.append(route)
