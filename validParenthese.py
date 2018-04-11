class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        while True:
            s1 = s.replace('[]', '')
            s2 = s1.replace('{}', '')
            s3 = s2.replace('()', '')
            if s3 == s:
                return False
            else:
                if s3 == '':
                    return True
                else:
                    s = s3


