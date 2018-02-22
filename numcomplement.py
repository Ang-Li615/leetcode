class Solution:
    def findComplement(self, num):
        l = len(bin(num)) - 2
        s = '0b'
        for i in range(l):
            s = s + '1'

        n = num ^ int(s,2)
        return n