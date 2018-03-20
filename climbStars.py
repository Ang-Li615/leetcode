class Solution:
    def climbStairs(self, n):
        t = n // 2
        sum = 0
        for i in range(t+1):
            j = n - i*2
            if i == 0 or j == 0:
                sum += 1
            else:
                sum += self.method(i,j)
        return sum

    def factorial(self,n):
        if n == 0:
            return 0
        mul = n
        while n > 2:
            n -= 1
            mul = mul * n
        return mul

    def method(self,n1,n2):
        n = n1 + n2
        m = self.factorial(n)
        r = self.factorial(n1) * self.factorial(n2)
        return m//r
