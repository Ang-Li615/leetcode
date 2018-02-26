class Solution:
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if len(a) < len(b):
            return len(b)
        elif len(a) > len(b):
            return len(a)
        else:
            if a != b:
                return len(a)
            else:
                return -1