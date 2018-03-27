class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = len(nums)
        S1 = [i for i in range(1,l+1)]
        D = set(S1) - set(nums)
        dict = {i:0 for i in nums}
        for i in nums:
            dict[i] += 1
            if dict[i] == 2:
                break
        return [i,list(D)[0]]
