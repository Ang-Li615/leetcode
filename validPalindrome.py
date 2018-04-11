class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = len(s)
        i = 0
        j = l - 1
        while i < j:
            if (s[i].lower() > '9' and s[i].lower() < 'a') or s[i].lower() > 'z' or s[i].lower() < '0':
                i += 1
                continue
            if (s[j].lower() > '9' and s[j].lower() < 'a') or s[j].lower() > 'z' or s[j].lower() < '0':
                j -= 1
                continue
            if s[i].lower() != s[j].lower:
                return False
            i += 1
            j -= 1
        return True
