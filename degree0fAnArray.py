class Solution:
    def findShortestSubArray(self, nums):
        dict1 = {i:0 for i in nums}
        dict2 = {i:[] for i in nums}
        l = len(nums)
        deg = 0
        for i in range(l):
            dict1[nums[i]] += 1
            deg = max(deg,dict1[nums[i]])
            dict2[nums[i]].append(i)

        m = l
        for key in dict1:
            if dict1[key] == deg:
                m = min(m,dict2[key][-1] - dict2[key][0] + 1)

        return m







        """
        :type nums: List[int]
        :rtype: int
        """

