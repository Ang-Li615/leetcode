class Solution:
    def isPowerOfTwo(self, n):
        while n // 2 != 0:
            r = n % 2
            if r != 0:
                return False
            n = n // 2
        if n != 1:
            return False
        else:
            return True