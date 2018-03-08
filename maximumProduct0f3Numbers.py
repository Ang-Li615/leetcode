class Solution:
    def maximumProduct(self, nums):
        l = sorted(nums)
        r1 = l[0]*l[1]*l[-1]
        r2 = l[-3]*l[-2]*l[-1]
        return max(r1,r2)




        """
        :type nums: List[int]
        :rtype: int
        """