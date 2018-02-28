class Solution:
    def isOneBitCharacter(self, bits):
        i = 0
        while i < len(bits):
            if bits[i] == 1:
                judge = False
                i = i + 2
                continue
            if bits[i] == 0:
                judge = True
                i = i + 1
                continue
        return judge







        """
        :type bits: List[int]
        :rtype: bool
        """