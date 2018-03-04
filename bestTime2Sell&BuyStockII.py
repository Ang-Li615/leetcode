class Solution:
    def maxProfit(self, prices):
        l = len(prices)
        L = []
        for i in range(l):
            L.append(False)
        buy = False

        for i in range(l-1):
            if buy == False:
                if prices[i+1] > prices[i]:
                    buy = True
                    L[i] = True
            if buy == True:
                if prices[i+1] < prices[i]:
                    buy = False
                    L[i] = False
        sum = 0
        for i in range(l-1):
            if L[i] == False:
                pass
            if L[i] == True:
                sum += prices[i+1] - prices[i]
        return sum



        """
        :type prices: List[int]
        :rtype: int
        """