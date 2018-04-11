class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''

        for i, lettergroups in enumerate(zip(*strs)):
            print(i, lettergroups)
            if len(set(lettergroups)) > 1:
                return strs[0][:i]

        return min(strs)