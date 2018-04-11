class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L = sorted(nums)
        l = len(L)
        i = 0
        sum = 0
        while i < l:
            if L[i] == nums[i]:
                sum += 1
                i += 1
            else:
                break
        j = l - 1
        while j > i:
            if L[j] == nums[j]:
                sum += 1
                j -= 1
            else:
                break
        return l - sum