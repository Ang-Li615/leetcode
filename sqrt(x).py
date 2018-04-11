class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 1:
            return 1
        approx = x//2
        while approx*approx > x:
            approx = (approx + x//approx)//2
        return approx

