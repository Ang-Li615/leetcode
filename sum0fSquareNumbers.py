import math
class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        if c < 0:
            return False
        if c == 0:
            return True
        sq = math.sqrt(c)

        if c % sq == 0:
            return True
        sq = int(c // sq)
        while sq >= 1:
            a = c - sq*sq
            if a % (math.sqrt(a)) == 0:
                return True
            else:
                sq -= 1
        return False


