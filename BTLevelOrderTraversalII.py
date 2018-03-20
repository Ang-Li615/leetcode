# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        if root == None:
            return []
        self.value = [[root.val]]
        self.treeComplement([root])
        l = len(self.value)
        L = []
        for i in range(l - 1, -1, -1):
            L.append(self.value[i])
        return L

    def treeComplement(self, list0fTreeNode):
        tree = []
        value = []
        for node in list0fTreeNode:
            if node != None:
                tree.append(node.left)
                tree.append(node.right)
        for node in tree:
            if node != None:
                value.append(node.val)
        if value != []:
            self.value.append(value)
            self.treeComplement(tree)


