class Solution:
    def longestPalindrome(self, s):
        dict = {i:0 for i in s}
        for i in s:
            dict[i] += 1

        s1 = 0
        l = 0
        for key in dict:
            if dict[key] % 2 == 0:
                l += dict[key]
            else:
                if dict[key] != 1:
                    l += dict[key] - 1
                else:
                    s1 += 1

        if s1 > 0:
            l += 1
        return l







        """
        :type s: str
        :rtype: int
        """