class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sorted()
        l = len(nums)
        i = 0
        sum = 0
        while i < l:
            j = i
            while j < l:
                if nums[j] - nums[i] < k:
                    j += 1
                    continue
                if nums[j] - nums[i] == k:
                    sum += 1
                    j += 1
                    continue
                if nums[j] - nums[i] > k:
                    break
            i += 1
        return sum