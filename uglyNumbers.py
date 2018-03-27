class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False
        if num == 1:
            return True

        if num % 2 == 0:
            num = num // 2
            return self.isUgly(num)
        elif num % 3 == 0:
            num = num // 3
            return self.isUgly(num)
        elif num % 5 == 0:
            num = num // 5
            return self.isUgly(num)
        else:
            return False
