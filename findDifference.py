class Solution:
    def findTheDifference(self, s, t):
        for i in t:
            if i not in s:
                return i
            else:
                n = s.find(i)
                s = s[:n] + s[n+1:]