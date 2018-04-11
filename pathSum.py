# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            return False
        return self.sumTree([root],sum)



    def sumTree(self,nodeList,sum):
        L = []
        for node in nodeList:
            if node.left != None and node.right != None:
                node.left.val = node.left.val + node.val
                L.append(node.left)
                node.right.val = node.right.val + node.val
                L.append(node.right)
            elif node.left != None and node.right == None:
                node.left.val = node.left.val + node.val
                L.append(node.left)
            elif node.left == None and node.right != None:
                node.right.val = node.right.val + node.val
                L.append(node.right)
            else:
                if node.val == sum:
                    return True

        if L != []:
            return self.sumTree(L,sum)
        else:
            return False