import math


class Solution:
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return False
        i = 2
        sum = 1
        sq = math.sqrt(num)
        print(sq)
        while i < sq:
            if sum > num:
                return False
            if num % i == 0:
                sum += i
                sum += num // i
            i += 1

        if sum == num:
            return True
        else:
            return False


