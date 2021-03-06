class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        l1 = len(haystack)
        l2 = len(needle)

        if l1 == 0:
            if l2 == 0:
                return 0
            else:
                return -1

        if l1 < l2:
            return -1

        if l2 == 0:
            return 0

        for i in range(l1 - l2 + 1):
            if haystack[i:i + l2] == needle:
                return i
        return -1