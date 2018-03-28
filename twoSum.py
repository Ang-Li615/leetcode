class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if target % 2 == 0 and target // 2 in nums:
            i = nums.index(target//2)
            T = nums[:i:1] + nums[i+1::1]
            if target // 2 in T:
                j  = T.index(target//2) + 1
                return [i,j]

        dict = {}
        for i,j in enumerate(nums):
            dict[j] = i
        nums = sorted(nums)
        l = len(nums)
        i = 0
        j = l - 1
        while i < j:
            if nums[i] + nums[j] == target:
                return [dict[nums[i]],dict[nums[j]]]
            elif nums[i] + nums[j] < target:
                i += 1
            elif nums[i] + nums[j] > target:
                j -= 1

