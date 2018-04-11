class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        L = s.split()
        if L != []:
            return len(L[-1])
        else:
            return 0

