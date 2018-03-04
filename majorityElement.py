class Solution:
    def majorityElement(self, nums):
        n = len(nums)
        dict = {i:0 for i in nums}
        for i in nums:
            dict[i] += 1
            if dict[i] > n/2:
                return i






        """
        :type nums: List[int]
        :rtype: int
        """