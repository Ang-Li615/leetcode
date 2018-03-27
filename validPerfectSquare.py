# class Solution:
#     def isPerfectSquare(self, num):
#         """
#         :type num: int
#         :rtype: bool
#         """
#         if num <= 0:
#             return False
#         if num == 1:
#             return True
#
#         half = num // 2
#         i = 2
#         while i <= half:
#             if num == i * i:
#                 return True
#             else:
#                 continue


class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        r = num
        while r*r > num:
            r = (r + num//r)//2
        return r*r == num