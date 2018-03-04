from math import sqrt
class Solution:
    def constructRectangle(self, area):
        n = int(sqrt(area))
        for i in range(n,area):
            if area % i == 0:
                return [i, area//i]
    #
    #
    #
    #
    #
    #
    #     if self.is_prime(area):
    #         return [area,1]
    #
    #     i = int(sqrt(area))
    #     if i * i == area:
    #         return [i, i]
    #     else:
    #         i = i + 1
    #         while area % i != 0:
    #             i = i + 1
    #         return [i, area // i]
    #
    # def is_prime(self,x):
    #     if x > 1:
    #         n = x // 2
    #         for i in range(2, n + 1):
    #             if x % i == 0:
    #                 return False
    #         return True
    #     else:
    #         return False

