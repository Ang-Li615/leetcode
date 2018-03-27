class Solution:
    def rob(self, nums):
        l = len(nums)
        if l == 0:
            return 0
        if l <= 2:
            return max(nums)
        else:
            nums[2] = nums[2] + nums[0]

        i = 3
        while i < l:
            nums[i] = nums[i] + max(nums[i-3],nums[i-2])
            i += 1
        return max(nums[l-1],nums[l-2])
