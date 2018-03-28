class Solution:
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pattern = ''
        l = len(s)
        i = 0
        j = 0
        while i < l - 1:
            j += 1
            pattern += s[i]
            if l % j == 0:
                if s.replace(pattern, '') == '':
                    return True

            i += 1
        return False