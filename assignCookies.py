class Solution:
    def findContentChildren(self, g, s):
        g = sorted(g)
        s = sorted(s)
        l1 = len(g)
        l2 = len(s)
        i = l1 - 1
        j = l2 - 1
        count = 0
        while min(i,j) >= 0:
            if g[i] <= s[j]:
                count += 1
                i -= 1
                j -= 1
            else:
                i -= 1
        return count
