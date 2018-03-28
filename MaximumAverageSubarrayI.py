class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        i = 1
        while i < len(nums):
            nums[i] += nums[i-1]
        i = k - 1
        m = 1.0*nums[i]/k
        j = 0
        while i < len(nums) - 1:
            i += 1
            m = max(m,1.0*(nums[i] - nums[j])/k)
        return m