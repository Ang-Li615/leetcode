class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        newBinary = bin(int(a, 2) + int(b, 2))
        return newBinary[2:]


