class Solution:
    def mergeTrees(self, t1, t2):
        if t1 == None and t2 == None:
            return 'null'
        elif t1 == None and t2 != None:
            return t2
        elif t1 != None and t2 == None:
            return t1
        else:
            t1.val = t1.val + t2.val
            return t1
