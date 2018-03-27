class Solution:
    def isPowerOfThree(self, n):
        while n // 3 != 0:
            r = n % 3
            if r != 0:
                return False
            n = n // 3
        if n != 1:
            return False
        else:
            return True