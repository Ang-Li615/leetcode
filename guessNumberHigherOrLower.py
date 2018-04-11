# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        myguess = n//2
        while guess(myguess) != 0:
            if guess(myguess) == 1:
                higher = n
                lower = myguess
            if guess(myguess) == -1:
                higher = myguess
                lower = 1
            myguess = (higher - lower)//2 + lower
        return myguess

