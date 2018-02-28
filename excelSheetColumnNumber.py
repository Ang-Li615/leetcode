class Solution:
    def titleToNumber(self, s):
        l = len(s)
        sum = 0

        for i in range(l):   #i = 0,1,2
            j = l-1-i        #j = 2,1,0
            mul = ord(s[i]) - 64
            while j >= 1:
                mul = mul * (ord('Z')- 64)
                j = j - 1
            sum = sum + mul

        return sum








        """
        :type s: str
        :rtype: int
        """