class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l == 1:
            return nums[0]
        n = max(nums)
        i = 1
        while i < l:
            nums[i] = nums[i] + nums[i - 1]
            i += 1
        p = max(nums)
        i = 0
        m = nums[i]
        for j in range(l):
            if nums[j] <= nums[i]:
                i = j
            else:
                m = max(m, nums[j] - nums[i])
        return max(m, n, p)




