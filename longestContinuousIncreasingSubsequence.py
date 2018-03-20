class Solution:
    def findLengthOfLCIS(self, nums):
        l = len(nums)
        if l == 0:
            return 0
        if l == 1:
            return 1

        L = []
        ll = 1
        for i in range(l-1):
            if nums[i+1] > nums[i]:
                ll += 1
            else:
                L.append(ll)
                ll = 1
        L.append(ll)
        return max(L)












        """
        :type nums: List[int]
        :rtype: int
        """