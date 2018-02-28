class Solution:
    def findDisappearedNumbers(self, nums):
        L = set([i for i in range(1,len(nums)+1)]) - set(nums)
        return list(L)
