class Solution:
    def distributeCandies(self, candies):
        dict = {i:0 for i in candies}
        for c in candies:
            dict[c] = dict[c] + 1
        l1 = len(candies)
        l2 = l1 // 2
        L = []
        for key in dict:
            L.append(key)
        l3 = len(L)

        if l3 >= l2:
            return l2
        else:
            return l3
