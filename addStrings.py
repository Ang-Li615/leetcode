class Solution:
    def addStrings(self, num1, num2):
        sum = 0
        l1 = len(num1)
        l2 = len(num2)

        power = 1
        for i in range(l1):
            sum += int(num1[-1-i]) * power
            power = power * 10

        power = 1
        for i in range(l2):
            sum += int(num2[-1-i]) * power
            power = power * 10

        return str(sum)
