class Solution:
    def findLHS(self, nums):
        dict = {i:0 for i in nums}
        for i in nums:
            dict[i] += 1
        m = 0
        for key in dict:
            if key+1 in dict:
                m = max(dict[key]+dict[key+1],m)
        return m