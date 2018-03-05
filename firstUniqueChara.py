class Solution:
    def firstUniqChar(self, s):
        if s == '':
            return -1


        dict = {i:0 for i in s}
        for i in s:
            dict[i] += 1
        l = len(s)
        for i in range(l):
            if dict[s[i]] == 1:
                return i









        """
        :type s: str
        :rtype: int
        """