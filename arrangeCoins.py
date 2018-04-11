class Solution:
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        count = 0
        while count <= n:
            count += i
            i += 1
        if count - n == 0:
            return i-1
        else:
            return i-2

