class Solution:
    def removeElement(self, nums, val):
        l = len(nums)
        for i in range(l-1,-1,-1):
            if nums[i] == val:
                del nums[i]
        return len(nums)




        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
