class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = ''
        d = n // 26
        r = n % 26
        while d != 0:
            if r == 0:
                s += 'Z'
                d -= 1
            else:
                s += chr(ord('A') + r - 1)
            n = d
            d = n // 26
            r = n % 26
        if r != 0:
            s += chr(ord('A')+r-1)
        return s[::-1]
