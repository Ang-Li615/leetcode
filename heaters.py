class Solution:
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.sort()
        heaters.insert(0,float('-inf'))
        heaters.append(float('inf'))
        i = 0
        ans = 0
        for house in houses:
            while house > heaters[i+1]:
                i += 1
            m = min(house-heaters[i],heaters[i+1]-house)
            ans = max(ans,m)
        return ans

