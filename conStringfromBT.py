class Solution:
    def tree2str(self,t):
        if t == None:
            return ''

        if t.left == None and t.right == None:
            return str(t.val)+''
        elif t.right == None:
            return str(t.val)+'('+self.tree2str(t.left)+')'
        elif t.left == None:
            return str(t.val)+'()'+'('+self.tree2str(t.right)+')'
        else:
            return str(t.val)+ '('+self.tree2str(t.left)+')' + '('+self.tree2str(t.right)+')'