class Solution:
    def arrayPairSum(self, nums):
        n = len(nums)//2
        new_nums = sorted(nums)
        count = 0
        j = 0
        for i in range(n):
            count = count + new_nums[j]
            j = j + 2
        return count