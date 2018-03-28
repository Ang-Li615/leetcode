class Solution:
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0

        while True:
            if len(s.strip(' ')) < len(s):
                s = s.strip(' ')
                continue
            if len(s.strip(',')) < len(s):
                s = s.strip(',')
                continue
            break
        if len(s) == 0:
            return 0
        s1 = s.replace(',', '')
        s2 = s1.replace(' ', '')
        if s2 == '':
            return 0
        else:
            return len(s1) - len(s2) + 1