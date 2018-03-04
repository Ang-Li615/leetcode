# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        decision = True
        if p == None and q == None:
            pass
        elif p == None:
            print('ah')
            decision = False
        elif q == None:
            print('ha')
            decision = False

        self.Lp = [p]
        self.Lq = [q]
        self.LLp = [p.val]
        self.LLq = [q.val]

        while True:
            print('yay')
            print(self.LLp)
            print(self.LLq)
            self.Lp = [x for x in self.Lp if x != None]
            self.Lq = [x for x in self.Lq if x != None]
            print(self.Lp)
            print(self.Lq)
            if self.Lp == [] and self.Lq == []:
                decision = True
                break
            elif self.Lp == []:
                decision = False
                break
            elif self.Lq == []:
                decision = False
                break

            if self.LLp != self.LLq:
                print('ahha')
                decision = False
                break
            else:
                self.Lp = self.checkChildren(self.Lp)
                self.Lq = self.checkChildren(self.Lq)
                self.LLp = self.checkValue(self.Lp)
                self.LLq = self.checkValue(self.Lp)
        return decision

    def checkChildren(self,L):
        l = []
        for i in L:
            l.append(i.left)
            l.append(i.right)
        return l

    def checkValue(self,L):
        l1 = []
        for i in L:
            if i == None:
                l1.append('null')
            else:
                l1.append(i.val)
        return l1