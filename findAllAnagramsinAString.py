class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        l1 = len(p)
        l2 = len(s)
        L = []
        for i in range(l2-l1+1):
            if sorted(s[i:i+l1]) == sorted(p):
                L.append(i)
        return L