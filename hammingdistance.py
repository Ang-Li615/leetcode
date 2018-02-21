class Solution:
    def hammingDistance(self, x, y):
        z = x ^ y
        count = 0
        for i in bin(z):
            if i == '1':
                count = count + 1

        return count
