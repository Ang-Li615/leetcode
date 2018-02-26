class Solution:
    def fizzBuzz(self, n):
        L = []
        for i in range(1,n+1):
            if i % 3 == 0 and i % 5 != 0:
                L.append('Fizz')
            elif i % 3 != 0 and i % 5 == 0:
                L.append('Buzz')
            elif i % 3 == 0 and i % 5 == 0:
                L.append('FizzBuzz')
            else:
                L.append(str(i))
        return L
