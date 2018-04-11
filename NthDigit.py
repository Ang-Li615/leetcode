class Solution:
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = 9
        i = 1
        while True:
            if n <= num * i:
                break
            else:
                n = n - num * i
                num = num * 10
                i += 1
        s = '1'
        j = 1
        while j <= i - 1:
            s += '0'
            j += 1
        start = int(s)
        d = n // i
        r = n % i
        if r == 0:
            start = start + d - 1
            return int(str(start)[-1])
        else:
            start = start + d
            return int(str(start)[r - 1])