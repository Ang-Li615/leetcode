class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        i = l-1
        while i >= 1:
            if nums[i] == nums[i-1]:
                del nums[i]
            i -= 1
        return len(nums)



