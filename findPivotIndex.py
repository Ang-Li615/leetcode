class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        S = sum(nums)
        leftsum = 0
        for i,j in enumerate(nums):
            if leftsum == S - leftsum - j:
                return i
            else:
                leftsum += j
