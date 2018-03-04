class Solution:
    def canConstruct(self, ransomNote, magazine):
        dict = {i:0 for i in ransomNote}
        for i in ransomNote:
            if i not in magazine:
                return False
            else:
                dict[i] += 1

        dict1 = {j:0 for j in magazine}
        for j in magazine:
            dict1[j] += 1

        for i in dict:
            if dict[i] > dict1[i]:
                return False

        return True







        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
