class Solution:
    def romanToInt(self, s):
        dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        int = 0
        for i in range(len(s)-1):
            if dict[s[i]] >= dict[s[i+1]]:
                int += dict[s[i]]
            else:
                int -= dict[s[i]]
        int += dict[s[-1]]
        return int




        """
        :type s: str
        :rtype: int
        """
