class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        l = len(str(x))
        i = 0
        j = l - 1
        while i < j:
            if str(x)[i] != str(x)[j]:
                return False
            i += 1
            j -= 1
        return True