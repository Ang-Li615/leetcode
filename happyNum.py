class Solution:
    def isHappy(self, n):
        sum = 0
        oldsum = []
        while True:
            n = str(n)
            l = len(n)
            for i in range(l):
                sum += int(n[i]) * int(n[i])
            if sum == 1:
                return True
            if sum in oldsum:
                return False
            oldsum.append(sum)
            n = sum
            sum = 0
