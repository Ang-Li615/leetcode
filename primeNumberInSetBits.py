from math import sqrt
# class Solution:
#     def countPrimeSetBits(self, L, R):
#         """
#         :type L: int
#         :type R: int
#         :rtype: int
#         """
#         total = 0
#         for i in range(L,R+1):
#             isPrime = True
#             sum = 0
#             for j in bin(i):
#                 if j == '1':
#                     sum = sum + 1
#             if sum > 2:
#                 for n in range(2,int(sqrt(sum)+1)):
#                     if sum % n == 0:
#                         isPrime = False
#                         break
#             else:
#                 isPrime = False
#
#             if isPrime:
#                 total = total + 1
#
#         return total
L = 567
R = 607
total = 0
for i in range(L,R+1):
    isPrime = True
    sum = 0
    print(bin(i))
    for j in bin(i):
        if j == '1':
            sum = sum + 1
    print(sum)
    if sum > 1:
        for n in range(2,int(sqrt(sum)+1)):
            if sum % n == 0:
                isPrime = False
                break
            else:
                continue
    else:
        isPrime = False

    if isPrime:
        total = total + 1
    print(total)