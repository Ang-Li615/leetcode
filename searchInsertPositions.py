class Solution:
    def searchInsert(self, nums, target):
        l = len(nums)
        ind = 0
        for i in range(l):
            if i < target:
                ind += 1
            else:
                ind += 1
        return ind





        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """