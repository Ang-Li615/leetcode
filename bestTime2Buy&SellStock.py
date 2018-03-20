# class Solution:
#     def maxProfit(self, prices):
#         l = len(prices)
#         if l == 0:
#             return 0
#         s = sorted(prices)
#         m1 = 0
#         m2 = 0
#
#         i = 0
#         j = l - 1
#         while i < l-1:
#             if j > i:
#                 if self.getIndex(s[j],prices) >= prices.index(s[i]):
#                     m1 = s[j] - s[i]
#                     break
#                 else:
#                     j -= 1
#                     continue
#             else:
#                 j = l - 1
#                 i += 1
#
#
#         i = 0
#         j = l - 1
#         while j > 0:
#             if i < j:
#                 if prices.index(s[i]) <= self.getIndex(s[j],prices):
#                     m2 = s[j] - s[i]
#                     break
#                 else:
#                     i += 1
#                     continue
#             else:
#                 i = 0
#                 i -= 1
#
#         m = max(m1,m2)
#         return m
#
#
#
#
#
#
#     def getIndex(self,e,L):
#         l = len(L)
#         for i in range(l-1,-1,-1):
#             if L[i] == e:
#                 return i



class Solution:
    def maxProfit(self, prices):
        min = prices[0]
        maxprofit = 0
        for p in prices:
            if p < min:
                min = p
            else:
                if p - min > maxprofit:
                    maxprofit = p - min

        return maxprofit



