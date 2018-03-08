class Solution:
    def missingNumber(self, nums):
        l = len(nums)
        s = set()
        for i in range(l+1):
            s.add(i)
        s = s - set(nums)
        for e in s:
            return e










        """
        :type nums: List[int]
        :rtype: int
        """