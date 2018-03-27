class Solution:
    def minCostClimbingStairs(self, cost):
        l = len(cost)
        i = 2
        while i <= l-1:
            cost[i] = cost[i] + min(cost[i-1],cost[i-2])
            i += 1
        return min(cost[l-1],cost[l-2])


















        """
        :type cost: List[int]
        :rtype: int
        """
