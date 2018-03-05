# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def findTilt(self, root):
        if root == None:
            return 0
        self.diff = 0
        self.subtreeSum(root)
        return self.diff

    def subtreeSum(self,root):
        if root.left != None and root.right == None:
            self.subtreeSum(root.left)
            root.val = root.val + root.left.val
            self.diff += abs(root.left.val)
        elif root.left == None and root.right != None:
            self.subtreeSum(root.right)
            root.val = root.val + root.right.val
            self.diff += abs(root.right.val)
        elif root.left == None and root.right == None:
            root.val = root.val
            self.diff += 0
        else:
            self.subtreeSum(root.left)
            self.subtreeSum(root.right)
            root.val = root.val + root.left.val + root.right.val
            self.diff += abs(root.left.val - root.right.val)
        return root





















        # if root.left != None:
        #     self.findTilt(root.left)
        #     ld = root.left.val
        # else:
        #     ld = 0
        #
        # if root.right != None:
        #     self.findTilt(root.right)
        # else:
        #     rd = 0
        #
        # self.sum += abs(ld - rd)
        # sum = root.val + ld + rd
        # root.val = sum
















    #     self.sum = 0
    #     self.findLevel([root])
    #     return self.sum
    #
    # def findLevel(self,L):
    #     l = []
    #     for i in L:
    #         if i.left != None:
    #             ld = i.left.val
    #             l.append(i.left)
    #         else:
    #             ld = 0
    #
    #         if i.right != None:
    #             rd = i.right.val
    #             l.append(i.right)
    #         else:
    #             rd = 0
    #         self.sum += abs(ld - rd)
    #
    #     if l != []:
    #         return self.findLevel(l)

