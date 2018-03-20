# class Solution:
#     def convertToBase7(self, num):
#         s = ''
#         n = abs(num)
#         while True:
#             if n // 7 == 0:
#                 remain = n % 7
#                 s += str(remain)
#                 n = n // 7
#             else:
#                 break
#         s = s[-1:]
#         if num >= 0:
#             return s
#         else:
#             return '-'+s

def convertToBase7(num):
    s = ''
    n = abs(num)
    while True:
        if n // 7 != 0:
            remain = n % 7
            s += str(remain)
            n = n // 7
        else:
            s += str(n)
            break
    s = s[::-1]
    if num >= 0:
        return s
    else:
        return '-'+s

num = 100
a = convertToBase7(num)
print(a)