# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        root = TreeNode()
        self.l = len(nums)
        self.p = nums
        if self.l % 2 == 1:
            root.val = nums[self.l//2]
            i = self.l // 2
            if i > 0:
                self.left(root,i)
            if i < self.l-1:
                self.right(root,i)
        else:
            pass
        return root


    def left(self,root,i):
        root.left.val = self.p[i-1]
        if i - 1 > 0:
            self.left(root.left,i-1)
        return root.left


    def right(self,root,i):
        root.right.val = self.p[i+1]
        if i + 1 < self.l - 1:
            self.right(root.right,i+1)
        return root.right






