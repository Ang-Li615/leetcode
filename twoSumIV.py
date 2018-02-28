class Solution:
    def findTarget(self, root, k):
        if root == None:
            return False
        else:
            self.L = [root]
            self.appendValue([root])
            print(self.L)
            LL = []
            for e in self.L:
                LL.append(e.val)

        sorted(LL)
        i = 0
        j = len(LL) - 1
        while i < j:
            if LL[i] + LL[j] < k:
                i += 1
            elif LL[i] + LL[j] == k:
                return True
            elif LL[i] + LL[j] > k:
                j -=1

        return False




    def appendValue(self,l):
        L = []
        for node in l:
            if node.left != None:
                self.L.append(node.left)
                L.append(node.left)
            if node.right != None:
                self.L.append(node.right)
                L.append(node.right)

        if L != []:
            L1 = L
            return self.appendValue(L1)
        print(L)











        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """