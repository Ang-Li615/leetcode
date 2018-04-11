class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(list(set(nums)))
        if len(nums) < 3:
            return max(nums)
        j = len(nums) - 1
        j -= 1
        j -= 1
        return nums[j]
