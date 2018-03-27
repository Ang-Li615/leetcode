class Solution:
    def isSubtree(self, s, t):
        print(t.val)
        self.L = []
        self.findRoot([s], t)
        if self.L == []:
            return False
        self.Result = True
        for node in self.L:
            self.checkLevel([node], [t])
            if self.Result == True:
                break
        return self.Result

    def findRoot(self, List, Root):
        L = []
        if List != []:
            for node in List:
                if node.val == Root.val:
                    self.L.append(node)
                else:
                    if node.left != None:
                        L.append(node.left)
                    if node.right != None:
                        L.append(node.right)
            self.findRoot(L, Root)

    def checkLevel(self, List1, List2):
        if len(List1) != len(List2):
            self.Result = False
            return None

        L1 = []
        LL1 = []
        for node in List1:
            if node != None:
                L1.append(node.val)
                LL1.append(node.left)
                LL1.append(node.right)

        L2 = []
        LL2 = []
        for node in List2:
            if node != None:
                L2.append(node.val)
                LL2.append(node.left)
                LL2.append(node.right)
        print(L1)
        print(L2)
        if L1 != L2:
            self.Result = False
            return None

        if L1 != [] and L2 != []:
            print('ha')
            self.checkLevel(LL1, LL2)


