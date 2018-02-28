class Solution:
    def addDigits(self, num):
        sum = self.add(num)
        return sum



    def add(self,n):
        sum = 0
        for i in str(n):
            sum = sum + int(i)
        if sum >= 10:
            return self.add(sum)
        else:
            return sum