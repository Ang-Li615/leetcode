class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict1 = {i: [] for i in s}
        dict2 = {i: [] for i in t}
        for tag, i in enumerate(s):
            dict1[i].append(tag)
        for tag, i in enumerate(t):
            dict2[i].append(tag)

        L1 = []
        L2 = []
        for key in dict1:
            if len(dict1[key]) != 1:
                L1.append(dict1[key])
        for key in dict2:
            if len(dict2[key]) != 1:
                L2.append(dict2[key])

        if len(L1) != len(L2):
            return False
        else:
            if sorted(L1) == sorted(L2):
                return True
            else:
                return False